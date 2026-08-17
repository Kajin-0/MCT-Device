# Round 50 single-host deployment/security reference profile

**Status:** SYNTHETIC REFERENCE DEPLOYMENT / ZERO-HgCdTe  
**Date:** 2026-08-16 America/New_York  
**Use with:** Round-48 schema/validator, Round-49 SQLite application, P16I/P16J/P16K/P16L.

## Purpose

Round 50 asks whether the Round-49 provenance application can be surrounded by enough deployment controls to fail safely under representative identity, data-isolation, key, clock, backup and instrument/configuration faults.

This profile is a repository/CI reference only. It is not a production security architecture and is not a laboratory deployment qualification.

## Components

- `tools/mct_provenance_store.py` — Round-49 append-only provenance store.
- `tools/mct_deployment_control.py` — identities, sessions, clock events, key lifecycle and config/calibration import.
- `tools/mct_protected_vault.py` — restricted holdout vault, dummy instrument adapter and backup/restore manager.
- `tools/round50_fixture.py` — deterministic deployment bootstrap and configuration-change fixture.
- `tools/run_round50_security.py` — integrated synthetic deployment/security test.

## Reference single-host layout

A synthetic run creates logically separate roots:

```text
<workdir>/
  round49_baseline/
    provenance.sqlite3
    objects/sha256/
  deployment/
    deployment.sqlite3
    keys/
    protected/
      holdout_vault.sqlite3
      objects/sha256/
  backup_good/
  inputs/
```

Reference permissions are tested as:

- deployment/store/vault/key directories: `0700`;
- SQLite files, key files and protected/raw object files after hardening: `0600`.

These mode bits are a reference control only. They do not prove separate OS users, group ACLs, SELinux/AppArmor confinement, container isolation or protection from root/administrator access.

## Identity separation

Reference identities are deliberately split by function:

- instrument service;
- configuration/calibration service;
- signer service;
- backup service;
- release operator;
- independent reviewer;
- DOE owner;
- administrator.

Sessions are random bearer tokens stored only by SHA-256 digest in the deployment database. Session expiry and append-only revocation are checked by the application.

A bearer token is not proof of a human identity or a secure service account. Production authentication remains open.

## Protected holdout isolation

Round 50 does not implement homemade encryption.

The Python standard library does not provide a vetted authenticated-encryption primitive appropriate for production protected-data storage. Therefore the reference profile uses split-store isolation:

`ordinary provenance store != protected holdout vault`.

The protected vault stores:

- protected raw instrument bytes in a separate content-addressed object root;
- protected parsed outcome values in a separate append-only database.

The ordinary provenance measurement keeps only:

- field identity;
- `vault://sha256/<digest>` reference;
- SHA-256 digest.

The synthetic test searches the ordinary store tree for a unique protected marker and requires that it is absent.

This is stronger than Round-49 logical separation but is still not encryption. A host administrator who can read both roots can bypass the separation.

## Model-freeze boundary

Protected outcome access requires:

1. an independent-reviewer session;
2. the applicable holdout lock;
3. a model-freeze record naming the holdout;
4. access time not earlier than model freeze;
5. requested fields contained in the holdout protected-field set.

Successful access emits the ordinary Round-48 `access_event` while the protected value remains in the vault.

## Key lifecycle

Reference key purposes:

- `SIGNATURE_HMAC`;
- `BACKUP_HMAC`.

Reference states:

`ACTIVE -> VERIFY_ONLY -> REVOKED`.

Rotation makes the old signing key `VERIFY_ONLY` and creates a new `ACTIVE` key. A verify-only key may validate historical content but may not create a new signature.

Revocation does not make a historical HMAC mathematically invalid. It changes the trust interpretation:

`cryptographically valid + revoked key -> REVOKED, not TRUSTED`.

Verification decisions are append-only deployment events.

Key bytes are local reference files. No HSM, TPM, KMS, hardware-backed signer, escrow or real custody procedure is established.

## Clock policy

The deployment layer records UTC observations plus a monotonic-clock observation and rejects a wall-clock observation that moves backward relative to the last accepted UTC event beyond the configured tolerance.

This is a consistency guard only.

It does not establish:

- authoritative UTC;
- NTP/PTP authenticity;
- secure time attestation;
- hardware timestamping;
- legal/trusted electronic-signature time.

## Dummy instrument adapter

The synthetic adapter reads a CSV file and binds the measurement to one exact configuration/calibration pair.

Before copying any raw bytes it checks that the configuration/calibration are valid at the acquisition time.

The Round-50 test supersedes configuration B with C and verifies:

- a B-dependent GO becomes nonreusable;
- the stale B adapter is rejected before a new raw object is copied;
- a C adapter with a new calibration can ingest.

No real instrument driver, network/serial protocol or vendor file format has been qualified.

## Backup/restore

The reference backup:

- uses SQLite's online backup API for the main, deployment and protected-vault databases;
- copies ordinary and protected content-addressed object trees;
- creates a canonical manifest of every backed-up file and SHA-256 digest;
- authenticates that manifest with a separate `BACKUP_HMAC` key;
- excludes key files from the backup being authenticated;
- verifies the manifest before restore;
- restores into a new destination only.

The test modifies one backed-up file and requires verification failure, then restores an untampered backup and re-verifies main raw objects, protected raw objects and record counts.

Reference backup is integrity-authenticated, **not encrypted**. Confidentiality, off-host storage, retention, escrow and disaster-site recovery remain open.

## Test command

```bash
python tools/run_round50_security.py
```

The committed CI must also run all earlier Round-48 and Round-49 tests.

## Pass boundary

Repository-level Round-50 PASS requires:

- all declared Round-50 deployment/security controls PASS;
- Round-49 prerequisite remains 19/19;
- exported synthetic bundle has zero Round-48 semantic errors;
- no real HgCdTe or laboratory identity is introduced.

Repository PASS does **not** imply:

`P16L-LAB-SECURITY-DEPLOYMENT-READY`.

A real deployment still requires genuine host/service identities, protected key custody, selected production encryption/isolation technology, operational backup recovery, external time policy, real instrument/configuration interfaces and a no-HgCdTe laboratory dry run.