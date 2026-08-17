#!/usr/bin/env python3
"""Round-50 protected vault, dummy adapter, and backup helpers; stdlib only."""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import shutil
import sqlite3
import stat
import tempfile
from pathlib import Path
from typing import Any

from mct_provenance_store import StateViolation, canon, dt, new_id, sha_file
from mct_deployment_control import DeploymentSecurity, _append_only_triggers, _chmod_dir, _chmod_file, _deploy_id

class HoldoutVault:
    """Restricted split-store for protected raw artifacts and outcome values.

    This is OS-permission/process-boundary isolation, not encryption.  It exists
    specifically to avoid inventing cryptography with the Python standard library.
    """

    def __init__(self, root: str | Path, store, security: DeploymentSecurity):
        self.root = Path(root)
        _chmod_dir(self.root)
        self.objects = self.root / "objects" / "sha256"
        _chmod_dir(self.objects)
        self.store = store
        self.security = security
        self.db_path = self.root / "holdout_vault.sqlite3"
        self.db = sqlite3.connect(self.db_path)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(
            """
CREATE TABLE IF NOT EXISTS protected_raw(
 raw_id TEXT PRIMARY KEY,sha256 TEXT NOT NULL,size_bytes INTEGER NOT NULL,object_path TEXT NOT NULL,
 source_name TEXT NOT NULL,ingested_at TEXT NOT NULL,actor_identity TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS sealed_values(
 holdout_lock_id TEXT NOT NULL,measurement_id TEXT NOT NULL,field_name TEXT NOT NULL,
 value_json TEXT NOT NULL,stored_at TEXT NOT NULL,actor_identity TEXT NOT NULL,
 PRIMARY KEY(holdout_lock_id,measurement_id,field_name));
"""
        )
        for table in ("protected_raw", "sealed_values"):
            _append_only_triggers(self.db, table)
        self.db.commit()
        _chmod_file(self.db_path)

    def close(self) -> None:
        self.db.close()

    def ingest_raw(self, token: str, src: str | Path, at: str) -> dict[str, Any]:
        actor = self.security.authorize(token, "PROTECTED_INGEST", at)
        src = Path(src)
        digest = sha_file(src)
        dest_dir = self.objects / digest[:2]
        _chmod_dir(dest_dir)
        dest = dest_dir / digest
        if not dest.exists():
            fd, name = tempfile.mkstemp(prefix="vault-", dir=dest_dir)
            os.close(fd)
            tmp = Path(name)
            try:
                shutil.copyfile(src, tmp)
                if sha_file(tmp) != digest:
                    raise StateViolation("protected ingest hash drift")
                os.replace(tmp, dest)
            finally:
                if tmp.exists():
                    tmp.unlink()
            _chmod_file(dest)
        if sha_file(dest) != digest:
            raise StateViolation("protected CAS hash mismatch")
        rid = _deploy_id("PRAW", at)
        with self.db:
            self.db.execute(
                "INSERT INTO protected_raw VALUES(?,?,?,?,?,?,?)",
                (rid, digest, src.stat().st_size, str(dest.relative_to(self.root)), src.name, at, actor["identity_id"]),
            )
        return {"raw_id": rid, "uri": f"vault://sha256/{digest}", "sha256": digest, "size_bytes": src.stat().st_size}

    def verify_raw(self, raw_id: str) -> bool:
        row = self.db.execute("SELECT sha256,object_path FROM protected_raw WHERE raw_id=?", (raw_id,)).fetchone()
        if not row:
            raise StateViolation(raw_id)
        path = self.root / row["object_path"]
        return path.is_file() and sha_file(path) == row["sha256"]

    def verify_all(self) -> None:
        for row in self.db.execute("SELECT raw_id FROM protected_raw"):
            if not self.verify_raw(row[0]):
                raise StateViolation(f"protected raw integrity failure {row[0]}")

    def seal(self, token: str, holdout_lock_id: str, measurement_id: str,
             field_name: str, value: Any, at: str) -> None:
        actor = self.security.authorize(token, "PROTECTED_SEAL", at)
        holdout = self.store.get(holdout_lock_id)
        measurement = self.store.get(measurement_id)
        if holdout.get("node_id") != measurement.get("node_id"):
            raise StateViolation("holdout/measurement node mismatch")
        if field_name not in holdout.get("protected_response_fields", []) or field_name not in measurement.get("result_fields", []):
            raise StateViolation("field is not protected measurement output")
        with self.db:
            self.db.execute(
                "INSERT INTO sealed_values VALUES(?,?,?,?,?,?)",
                (holdout_lock_id, measurement_id, field_name, canon(value).decode(), at, actor["identity_id"]),
            )

    def open(self, token: str, holdout_lock_id: str, measurement_id: str,
             fields: list[str], model_freeze_id: str, at: str) -> dict[str, Any]:
        actor = self.security.authorize(token, "HOLDOUT_OPEN", at)
        holdout = self.store.get(holdout_lock_id)
        freeze = self.store.get(model_freeze_id)
        protected = set(holdout.get("protected_response_fields", []))
        if holdout_lock_id not in freeze.get("holdout_lock_ids", []) or dt(at) < dt(freeze["frozen_at"]):
            raise StateViolation("holdout outcome not released by model freeze")
        if not fields or not set(fields) <= protected:
            raise StateViolation("illegal protected fields")
        access = {
            "id": new_id("access_event", at), "record_type": "access_event", "created_at": at,
            "revision": 1, "synthetic": True, "holdout_lock_id": holdout_lock_id,
            "access_type": "OUTCOME", "accessed_at": at, "fields": fields,
            "model_freeze_id": model_freeze_id,
        }
        self.store.append(access, actor["store_actor_id"], [(holdout_lock_id, "holdout"), (model_freeze_id, "model_freeze")])
        rows = self.db.execute(
            "SELECT field_name,value_json FROM sealed_values WHERE holdout_lock_id=? AND measurement_id=?",
            (holdout_lock_id, measurement_id),
        ).fetchall()
        out = {r[0]: json.loads(r[1]) for r in rows if r[0] in fields}
        if set(out) != set(fields):
            raise StateViolation("protected value incomplete")
        return out

    def summary(self) -> dict[str, int]:
        return {
            "protected_raw": int(self.db.execute("SELECT count(*) FROM protected_raw").fetchone()[0]),
            "sealed_values": int(self.db.execute("SELECT count(*) FROM sealed_values").fetchone()[0]),
        }


class DummyInstrumentAdapter:
    """Minimal file-ingest adapter bound to one configuration/calibration pair."""

    def __init__(self, store, security: DeploymentSecurity, configuration_id: str,
                 calibration_id: str, method_ref: str, result_fields: list[str]):
        self.store = store
        self.security = security
        self.configuration_id = configuration_id
        self.calibration_id = calibration_id
        self.method_ref = method_ref
        self.result_fields = result_fields

    def _measurement(self, node_id: str, raw_ref: dict[str, Any], at: str) -> dict[str, Any]:
        return {
            "id": new_id("measurement", at), "record_type": "measurement", "created_at": at,
            "revision": 1, "synthetic": True, "node_id": node_id, "method_ref": self.method_ref,
            "configuration_ids": [self.configuration_id], "calibration_ids": [self.calibration_id],
            "acquired_at": at, "qc_status": "PASS", "result_fields": list(self.result_fields),
            "raw_data_refs": [{"uri": raw_ref["uri"], "sha256": raw_ref["sha256"]}],
            "analysis_ref": "ROUND50-DUMMY-ADAPTER",
        }

    def ingest(self, token: str, src: str | Path, node_id: str, at: str) -> dict[str, Any]:
        actor = self.security.authorize(token, "INSTRUMENT_INGEST", at)
        probe = self._measurement(node_id, {"uri": "probe://preflight", "sha256": "0" * 64}, at)
        self.store.check_config(probe)  # preflight before copying bytes
        header = Path(src).read_text().splitlines()[0].split(",")
        if not set(self.result_fields) <= set(header):
            raise StateViolation("dummy instrument fields missing")
        raw = self.store.ingest(src, actor["store_actor_id"], at)
        measurement = self._measurement(node_id, raw, at)
        self.store.append(measurement, actor["store_actor_id"], [(node_id, "measured")])
        return measurement

    def ingest_protected(self, token: str, vault: HoldoutVault, src: str | Path,
                         node_id: str, at: str) -> tuple[dict[str, Any], dict[str, Any]]:
        actor = self.security.authorize(token, "PROTECTED_INGEST", at)
        probe = self._measurement(node_id, {"uri": "probe://preflight", "sha256": "0" * 64}, at)
        self.store.check_config(probe)
        header = Path(src).read_text().splitlines()[0].split(",")
        if not set(self.result_fields) <= set(header):
            raise StateViolation("protected dummy fields missing")
        raw = vault.ingest_raw(token, src, at)
        measurement = self._measurement(node_id, raw, at)
        self.store.append(measurement, actor["store_actor_id"], [(node_id, "measured")])
        return measurement, raw


class BackupManager:
    """Integrity-authenticated backup/restore; confidentiality is explicitly out of scope."""

    def __init__(self, security: DeploymentSecurity, vault: HoldoutVault):
        self.security = security
        self.vault = vault

    @staticmethod
    def _backup_db(conn: sqlite3.Connection, dest: Path) -> None:
        out = sqlite3.connect(dest)
        try:
            conn.backup(out)
        finally:
            out.close()
        _chmod_file(dest)

    @staticmethod
    def _harden_tree(root: Path) -> None:
        for p in root.rglob("*"):
            if p.is_dir():
                _chmod_dir(p)
            elif p.is_file():
                _chmod_file(p)

    @staticmethod
    def _manifest_files(root: Path) -> dict[str, str]:
        files = {}
        for p in sorted(root.rglob("*")):
            if p.is_file() and p.name not in {"manifest.json", "manifest.hmac"}:
                files[str(p.relative_to(root))] = sha_file(p)
        return files

    def create(self, token: str, backup_root: str | Path, at: str, key_id: str) -> Path:
        self.security.authorize(token, "BACKUP_CREATE", at)
        if self.security.key_state(key_id) != "ACTIVE":
            raise StateViolation("backup key not active")
        key_row = self.security.db.execute("SELECT purpose FROM keys WHERE key_id=?", (key_id,)).fetchone()
        if not key_row or key_row[0] != "BACKUP_HMAC":
            raise StateViolation("wrong backup key purpose")
        dest = Path(backup_root)
        if dest.exists():
            raise StateViolation("backup destination exists")
        _chmod_dir(dest)
        self.security.store.verify_all_raw()
        self.vault.verify_all()
        self._backup_db(self.security.store.db, dest / "provenance.sqlite3")
        self._backup_db(self.vault.db, dest / "holdout_vault.sqlite3")
        self._backup_db(self.security.db, dest / "deployment.sqlite3")
        if self.security.store.obj.exists():
            shutil.copytree(self.security.store.obj, dest / "objects")
        if self.vault.objects.exists():
            shutil.copytree(self.vault.objects, dest / "protected_objects")
        self._harden_tree(dest)
        manifest = {
            "format": "MCT-R50-BACKUP-1", "created_at": at, "key_id": key_id,
            "files": self._manifest_files(dest),
        }
        raw = canon(manifest)
        (dest / "manifest.json").write_bytes(raw + b"\n")
        mac = hmac.new(self.security.key_bytes(key_id), raw, hashlib.sha256).hexdigest()
        (dest / "manifest.hmac").write_text(mac + "\n")
        _chmod_file(dest / "manifest.json")
        _chmod_file(dest / "manifest.hmac")
        return dest

    def verify(self, token: str, backup_root: str | Path, at: str) -> bool:
        self.security.authorize(token, "BACKUP_VERIFY", at)
        root = Path(backup_root)
        try:
            manifest = json.loads((root / "manifest.json").read_text())
            raw = canon(manifest)
            mac = (root / "manifest.hmac").read_text().strip()
            expected = hmac.new(self.security.key_bytes(manifest["key_id"]), raw, hashlib.sha256).hexdigest()
            if not hmac.compare_digest(mac, expected):
                return False
            if manifest.get("format") != "MCT-R50-BACKUP-1":
                return False
            actual = self._manifest_files(root)
            return actual == manifest.get("files", {})
        except Exception:
            return False

    def restore(self, token: str, backup_root: str | Path, dest_root: str | Path, at: str) -> Path:
        self.security.authorize(token, "BACKUP_RESTORE", at)
        if not self.verify(token, backup_root, at):
            raise StateViolation("backup integrity check failed")
        src = Path(backup_root)
        dest = Path(dest_root)
        if dest.exists():
            raise StateViolation("restore destination exists")
        _chmod_dir(dest)
        store_root = dest / "store"
        vault_root = dest / "protected"
        _chmod_dir(store_root)
        _chmod_dir(vault_root)
        shutil.copy2(src / "provenance.sqlite3", store_root / "provenance.sqlite3")
        shutil.copy2(src / "holdout_vault.sqlite3", vault_root / "holdout_vault.sqlite3")
        shutil.copy2(src / "deployment.sqlite3", dest / "deployment.sqlite3")
        if (src / "objects").exists():
            shutil.copytree(src / "objects", store_root / "objects" / "sha256")
        if (src / "protected_objects").exists():
            shutil.copytree(src / "protected_objects", vault_root / "objects" / "sha256")
        self._harden_tree(dest)
        return dest


def harden_store_permissions(store) -> None:
    _chmod_dir(store.root)
    if (store.root / "provenance.sqlite3").exists():
        _chmod_file(store.root / "provenance.sqlite3")
    if store.obj.exists():
        for p in [store.obj, *store.obj.rglob("*")]:
            if p.is_dir():
                _chmod_dir(p)
            elif p.is_file():
                _chmod_file(p)


def permission_mode(path: str | Path) -> int:
    return stat.S_IMODE(Path(path).stat().st_mode)


def main_store_contains(store, needle: bytes) -> bool:
    for p in store.root.rglob("*"):
        if p.is_file():
            try:
                if needle in p.read_bytes():
                    return True
            except OSError:
                pass
    return False
