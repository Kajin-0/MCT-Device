#!/usr/bin/env python3
"""Round-50 single-host deployment/security simulation helpers; stdlib only.

This module deliberately avoids claiming production security.  It adds an
application/session boundary, restricted holdout vault, key lifecycle audit,
clock-regression detection, dummy instrument/configuration adapters, and
integrity-authenticated backup/restore around the Round-49 reference store.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import secrets
import shutil
import sqlite3
import stat
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mct_provenance_store import PermissionDenied, StateViolation, canon, dt, new_id, now, sha_file

SESSION_ACTIONS = {
    "SERVICE_INSTRUMENT": {"INSTRUMENT_INGEST", "PROTECTED_INGEST", "PROTECTED_SEAL"},
    "SERVICE_CONFIG": {"CONFIG_IMPORT", "CALIBRATION_IMPORT", "CONFIG_SUPERSEDE"},
    "SERVICE_SIGNER": {"SIGN_RECORD", "VERIFY_SIGNATURE"},
    "SERVICE_BACKUP": {"BACKUP_CREATE", "BACKUP_VERIFY", "BACKUP_RESTORE"},
    "OP_RELEASE": {"GATE_APPROVE"},
    "OP_INDEPENDENT": {"HOLDOUT_OPEN", "VERIFY_SIGNATURE"},
    "OP_DOE": {"HOLDOUT_LOCK", "MODEL_FREEZE", "EVIDENCE_PROMOTE"},
    "OP_ADMIN": {
        "IDENTITY_MANAGE", "KEY_MANAGE", "CLOCK_ACCEPT", "CONFIG_IMPORT",
        "CALIBRATION_IMPORT", "CONFIG_SUPERSEDE", "BACKUP_CREATE",
        "BACKUP_VERIFY", "BACKUP_RESTORE", "VERIFY_SIGNATURE",
    },
}
KEY_PURPOSES = {"SIGNATURE_HMAC", "BACKUP_HMAC"}
KEY_STATES = {"ACTIVE", "VERIFY_ONLY", "REVOKED"}


def _utc(x: str) -> str:
    return dt(x).astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _deploy_id(kind: str, at: str | None = None) -> str:
    stamp = dt(at or now()).astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"MCT-{kind}-{stamp}-{uuid.uuid4().hex[:12].upper()}"


def _chmod_file(path: Path, mode: int = 0o600) -> None:
    path.chmod(mode)


def _chmod_dir(path: Path, mode: int = 0o700) -> None:
    path.mkdir(parents=True, exist_ok=True)
    path.chmod(mode)


def _append_only_triggers(db: sqlite3.Connection, table: str) -> None:
    db.executescript(
        f"CREATE TRIGGER IF NOT EXISTS {table}_no_update BEFORE UPDATE ON {table} "
        f"BEGIN SELECT RAISE(ABORT,'{table} append-only');END;"
        f"CREATE TRIGGER IF NOT EXISTS {table}_no_delete BEFORE DELETE ON {table} "
        f"BEGIN SELECT RAISE(ABORT,'{table} append-only');END;"
    )


class DeploymentSecurity:
    """Deployment-side identity/session, clock, and key-lifecycle control plane."""

    def __init__(self, root: str | Path, store):
        self.root = Path(root)
        _chmod_dir(self.root)
        self.store = store
        self.keys_dir = self.root / "keys"
        _chmod_dir(self.keys_dir)
        self.db_path = self.root / "deployment.sqlite3"
        self.db = sqlite3.connect(self.db_path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA synchronous=FULL")
        self._init()
        _chmod_file(self.db_path)

    def close(self) -> None:
        self.db.close()

    def _init(self) -> None:
        self.db.executescript(
            """
CREATE TABLE IF NOT EXISTS identities(
 identity_id TEXT PRIMARY KEY, identity_type TEXT NOT NULL, store_actor_id TEXT NOT NULL,
 created_at TEXT NOT NULL, label TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS sessions(
 session_hash TEXT PRIMARY KEY, identity_id TEXT NOT NULL REFERENCES identities(identity_id),
 issued_at TEXT NOT NULL, expires_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS session_revocations(
 session_hash TEXT NOT NULL REFERENCES sessions(session_hash), revoked_at TEXT NOT NULL,
 reason TEXT NOT NULL, PRIMARY KEY(session_hash,revoked_at));
CREATE TABLE IF NOT EXISTS clock_events(
 seq INTEGER PRIMARY KEY AUTOINCREMENT, observed_utc TEXT NOT NULL, source TEXT NOT NULL,
 monotonic_ns INTEGER NOT NULL, actor_identity TEXT NOT NULL, accepted INTEGER NOT NULL,
 reason TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS keys(
 key_id TEXT PRIMARY KEY, purpose TEXT NOT NULL, created_at TEXT NOT NULL,
 key_path TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS key_events(
 seq INTEGER PRIMARY KEY AUTOINCREMENT, key_id TEXT NOT NULL REFERENCES keys(key_id),
 state TEXT NOT NULL, at TEXT NOT NULL, actor_identity TEXT NOT NULL, reason TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS verification_events(
 seq INTEGER PRIMARY KEY AUTOINCREMENT, signature_id TEXT NOT NULL, key_id TEXT,
 verified_at TEXT NOT NULL, actor_identity TEXT NOT NULL, crypto_valid INTEGER NOT NULL,
 trust_state TEXT NOT NULL);
"""
        )
        for table in (
            "identities", "sessions", "session_revocations", "clock_events",
            "keys", "key_events", "verification_events",
        ):
            _append_only_triggers(self.db, table)
        self.db.commit()

    def add_identity(self, identity_id: str, identity_type: str, store_actor_id: str,
                     label: str, at: str) -> None:
        if identity_type not in SESSION_ACTIONS:
            raise ValueError(identity_type)
        with self.db:
            self.db.execute(
                "INSERT INTO identities VALUES(?,?,?,?,?)",
                (identity_id, identity_type, store_actor_id, at, label),
            )

    def issue_session(self, identity_id: str, issued_at: str, expires_at: str) -> str:
        if dt(expires_at) <= dt(issued_at):
            raise ValueError("session expiry must follow issue")
        if not self.db.execute("SELECT 1 FROM identities WHERE identity_id=?", (identity_id,)).fetchone():
            raise PermissionDenied(identity_id)
        token = secrets.token_urlsafe(32)
        digest = hashlib.sha256(token.encode()).hexdigest()
        with self.db:
            self.db.execute("INSERT INTO sessions VALUES(?,?,?,?)", (digest, identity_id, issued_at, expires_at))
        return token

    def revoke_session(self, token: str, at: str, reason: str) -> None:
        digest = hashlib.sha256(token.encode()).hexdigest()
        with self.db:
            self.db.execute("INSERT INTO session_revocations VALUES(?,?,?)", (digest, at, reason))

    def authorize(self, token: str, action: str, at: str) -> sqlite3.Row:
        digest = hashlib.sha256(token.encode()).hexdigest()
        row = self.db.execute(
            "SELECT s.*,i.identity_type,i.store_actor_id,i.identity_id FROM sessions s "
            "JOIN identities i ON i.identity_id=s.identity_id WHERE s.session_hash=?",
            (digest,),
        ).fetchone()
        if not row or dt(at) < dt(row["issued_at"]) or dt(at) > dt(row["expires_at"]):
            raise PermissionDenied("invalid/expired session")
        if self.db.execute(
            "SELECT 1 FROM session_revocations WHERE session_hash=? AND revoked_at<=?",
            (digest, at),
        ).fetchone():
            raise PermissionDenied("revoked session")
        if action not in SESSION_ACTIONS[row["identity_type"]]:
            raise PermissionDenied(f"{row['identity_type']} cannot {action}")
        return row

    def accept_clock(self, token: str, observed_utc: str, source: str,
                     tolerance_seconds: float = 0.0) -> bool:
        actor = self.authorize(token, "CLOCK_ACCEPT", observed_utc)
        observed_utc = _utc(observed_utc)
        last = self.db.execute(
            "SELECT observed_utc FROM clock_events WHERE accepted=1 ORDER BY seq DESC LIMIT 1"
        ).fetchone()
        accepted = True
        reason = "accepted"
        if last and dt(observed_utc).timestamp() + tolerance_seconds < dt(last[0]).timestamp():
            accepted = False
            reason = "backward-clock-step"
        with self.db:
            self.db.execute(
                "INSERT INTO clock_events(observed_utc,source,monotonic_ns,actor_identity,accepted,reason) "
                "VALUES(?,?,?,?,?,?)",
                (observed_utc, source, time.monotonic_ns(), actor["identity_id"], int(accepted), reason),
            )
        if not accepted:
            raise StateViolation(reason)
        return True

    def create_key(self, token: str, purpose: str, at: str, reason: str = "initial") -> str:
        actor = self.authorize(token, "KEY_MANAGE", at)
        if purpose not in KEY_PURPOSES:
            raise ValueError(purpose)
        active = self.db.execute(
            "SELECT k.key_id FROM keys k JOIN key_events e ON e.key_id=k.key_id "
            "WHERE k.purpose=? AND e.seq=(SELECT max(seq) FROM key_events WHERE key_id=k.key_id) "
            "AND e.state='ACTIVE'",
            (purpose,),
        ).fetchone()
        if active:
            raise StateViolation(f"active {purpose} key already exists")
        kid = _deploy_id("KEY", at)
        path = self.keys_dir / f"{kid}.key"
        path.write_bytes(secrets.token_bytes(32))
        _chmod_file(path)
        with self.db:
            self.db.execute("INSERT INTO keys VALUES(?,?,?,?)", (kid, purpose, at, str(path.relative_to(self.root))))
            self.db.execute("INSERT INTO key_events(key_id,state,at,actor_identity,reason) VALUES(?,?,?,?,?)",
                            (kid, "ACTIVE", at, actor["identity_id"], reason))
        return kid

    def key_state(self, key_id: str) -> str:
        row = self.db.execute(
            "SELECT state FROM key_events WHERE key_id=? ORDER BY seq DESC LIMIT 1", (key_id,)
        ).fetchone()
        if not row:
            raise StateViolation(f"unknown key {key_id}")
        return row[0]

    def key_bytes(self, key_id: str) -> bytes:
        row = self.db.execute("SELECT key_path FROM keys WHERE key_id=?", (key_id,)).fetchone()
        if not row:
            raise StateViolation(key_id)
        path = self.root / row[0]
        if not path.is_file():
            raise StateViolation(f"key material unavailable {key_id}")
        return path.read_bytes()

    def active_key(self, purpose: str) -> str:
        rows = self.db.execute("SELECT key_id FROM keys WHERE purpose=? ORDER BY created_at", (purpose,)).fetchall()
        active = [r[0] for r in rows if self.key_state(r[0]) == "ACTIVE"]
        if len(active) != 1:
            raise StateViolation(f"expected exactly one ACTIVE {purpose} key")
        return active[0]

    def rotate_key(self, token: str, purpose: str, at: str) -> tuple[str, str]:
        actor = self.authorize(token, "KEY_MANAGE", at)
        old = self.active_key(purpose)
        with self.db:
            self.db.execute("INSERT INTO key_events(key_id,state,at,actor_identity,reason) VALUES(?,?,?,?,?)",
                            (old, "VERIFY_ONLY", at, actor["identity_id"], "rotation"))
        new = self.create_key(token, purpose, at, "rotation-successor")
        return old, new

    def revoke_key(self, token: str, key_id: str, at: str, reason: str) -> None:
        actor = self.authorize(token, "KEY_MANAGE", at)
        if self.key_state(key_id) == "REVOKED":
            raise StateViolation("already revoked")
        with self.db:
            self.db.execute("INSERT INTO key_events(key_id,state,at,actor_identity,reason) VALUES(?,?,?,?,?)",
                            (key_id, "REVOKED", at, actor["identity_id"], reason))

    def sign_record(self, token: str, target_record_id: str, at: str) -> str:
        actor = self.authorize(token, "SIGN_RECORD", at)
        kid = self.active_key("SIGNATURE_HMAC")
        return self.store.sign(target_record_id, actor["store_actor_id"], kid, self.key_bytes(kid), at)

    def verify_signature(self, token: str, signature_id: str, at: str) -> dict[str, Any]:
        actor = self.authorize(token, "VERIFY_SIGNATURE", at)
        sig = self.store.db.execute("SELECT key_id FROM signatures WHERE signature_id=?", (signature_id,)).fetchone()
        if not sig:
            raise StateViolation(signature_id)
        kid = sig[0]
        crypto = self.store.verify_sig(signature_id, self.key_bytes(kid))
        state = self.key_state(kid)
        trust = "TRUSTED" if crypto and state in {"ACTIVE", "VERIFY_ONLY"} else ("REVOKED" if crypto and state == "REVOKED" else "INVALID")
        with self.db:
            self.db.execute(
                "INSERT INTO verification_events(signature_id,key_id,verified_at,actor_identity,crypto_valid,trust_state) "
                "VALUES(?,?,?,?,?,?)",
                (signature_id, kid, at, actor["identity_id"], int(crypto), trust),
            )
        return {"crypto_valid": crypto, "key_state": state, "trust_state": trust}

    def import_configuration(self, token: str, spec_path: str | Path, at: str) -> dict[str, Any]:
        actor = self.authorize(token, "CONFIG_IMPORT", at)
        spec = json.loads(Path(spec_path).read_text())
        record = {
            "id": new_id("configuration", at), "record_type": "configuration", "created_at": at,
            "revision": 1, "synthetic": True, "config_class": spec["config_class"],
            "version_label": spec["version_label"], "status": "ACTIVE", "valid_from": at,
            "valid_to": spec.get("valid_to"), "supersedes_id": spec.get("supersedes_id"),
        }
        deps = [(record["supersedes_id"], "supersedes")] if record["supersedes_id"] else []
        self.store.append(record, actor["store_actor_id"], deps)
        return record

    def import_calibration(self, token: str, spec_path: str | Path, at: str) -> dict[str, Any]:
        actor = self.authorize(token, "CALIBRATION_IMPORT", at)
        spec = json.loads(Path(spec_path).read_text())
        record = {
            "id": new_id("calibration", at), "record_type": "calibration", "created_at": at,
            "revision": 1, "synthetic": True, "configuration_id": spec["configuration_id"],
            "scope": spec["scope"], "status": "VALID", "valid_from": at,
            "valid_to": spec.get("valid_to"),
        }
        self.store.append(record, actor["store_actor_id"], [(record["configuration_id"], "configuration")])
        return record

    def supersede_configuration(self, token: str, old_id: str, new_id_: str, at: str, reason: str) -> list[str]:
        actor = self.authorize(token, "CONFIG_SUPERSEDE", at)
        return self.store.supersede(old_id, new_id_, at, actor["store_actor_id"], reason)
