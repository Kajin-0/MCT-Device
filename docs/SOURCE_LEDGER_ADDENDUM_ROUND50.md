# Source ledger addendum — Round 50 deployment/security simulation

**Date:** 2026-08-16 America/New_York  
**Classification:** `DERIVED-INTERNAL-CONTROL / EXECUTABLE-DEPLOYMENT-SECURITY-SIMULATION`

## Scope

Round 50 introduces no new historical HgCdTe process evidence and no new external literature evidence.

It extends the controlled Round-48/49 provenance software using Python standard library, SQLite, filesystem permissions and synthetic files/identities.

No real instrument, laboratory host, human identity, calibration system or HgCdTe material is instantiated.

## Controlled internal basis

Primary inputs:

- Round-45 genealogy/material accounting;
- Round-46 sequential release control;
- Round-47 logic dry run;
- Round-48 provenance schema/semantic validator;
- Round-49 transactional provenance reference application;
- P16I/P16J/P16K controlled states.

## New derived claims

### Service/operator action separation

Evidence class: `DERIVED-INTERNAL / EXECUTABLE-AUTHORIZATION-TEST`.

The deployment layer distinguishes instrument, configuration, signing, backup, release, independent-review, DOE and administrator identities. Cross-role denial cases are executed.

Restriction: identities are synthetic labels with bearer sessions, not authenticated real people or OS service accounts.

### Session revocation

Evidence class: `DERIVED-INTERNAL / EXECUTABLE-SESSION-CONTROL-TEST`.

Session tokens are stored by SHA-256 digest and append-only revocation blocks later use.

Restriction: no SSO, MFA, certificate identity or production secret store is established.

### Clock-regression guard

Evidence class: `DERIVED-INTERNAL / TEMPORAL-CONSISTENCY-TEST`.

A backwards UTC observation relative to the last accepted event is rejected and recorded.

Restriction: this is not trusted time or authenticated NTP/PTP.

### Protected split-store isolation

Evidence class: `DERIVED-INTERNAL / DATA-ISOLATION-TEST`.

Protected holdout raw bytes and protected parsed values are placed outside the ordinary provenance store in a restricted vault. The ordinary measurement retains a vault URI and SHA-256 identity. A unique protected marker is confirmed absent from the ordinary store tree.

Restriction: the protected vault is not encrypted. A privileged host administrator can read both roots.

### Rejection of custom encryption

Evidence class: `DERIVED-INTERNAL / DESIGN-DECISION`.

Round 50 deliberately does not invent an encryption format using ad hoc primitives. A future laboratory deployment must select vetted authenticated encryption and key-management technology, or document an equivalent approved isolation mechanism.

### Signing-key lifecycle

Evidence class: `DERIVED-INTERNAL / EXECUTABLE-KEY-LIFECYCLE-TEST`.

Reference HMAC signing keys transition through `ACTIVE`, `VERIFY_ONLY`, and `REVOKED`. Rotation, retired-key signing denial and trust downgrade after revocation are tested. Verification decisions are retained.

Restriction: keys are synthetic local files. No HSM/KMS/TPM, custody, dual control, identity assurance, escrow or regulatory-signature claim.

### Filesystem-mode reference profile

Evidence class: `DERIVED-INTERNAL / HOST-PERMISSION-SIMULATION`.

Reference directories/files are checked for `0700`/`0600` modes.

Restriction: this does not prove separate uid/gid ownership, ACL/MAC confinement, container isolation or root resistance.

### Dummy instrument/configuration integration

Evidence class: `DERIVED-INTERNAL / SYNTHETIC-ADAPTER-TEST`.

A CSV adapter binds measurements to exact configuration/calibration records and performs validity preflight before copying bytes. After configuration supersession, the stale adapter is rejected before raw-data ingestion and the replacement adapter succeeds.

Restriction: no real instrument protocol, driver or vendor file format is qualified.

### Backup integrity and restore

Evidence class: `DERIVED-INTERNAL / BACKUP-INTEGRITY-TEST`.

SQLite backup APIs and object-tree copies are covered by a canonical SHA-256 manifest authenticated with a separate backup HMAC. Deliberate backup modification is detected. An intact backup restores to a new destination and restored raw/vault integrity is checked.

Restriction: backup is not encrypted. Off-site durability, retention, key-loss recovery and disaster recovery are not established.

## Candidate CI evidence

Temporary candidate commit:

`1639fee3f75d9ba11df066ed7d194c946953ac3d`.

GitHub Actions run:

`31980899498`.

Observed:

- Round-48 regression PASS;
- Round-49 operational controls `19/19` PASS;
- Round-50 deployment/security controls `33/33` PASS;
- generated bundle records `50`;
- Round-48 semantic errors `0`.

Final repository-level evidence class is promoted only when the final controlled main commit reproduces these checks.

## No physical/process evidence promotion

Round 50 does not change any HgCdTe process, infrastructure, commissioning, campaign, genealogy, first-build, historical-reproduction or reproducible-release state.

Positive evidence is restricted to the tested repository deployment/security reference architecture.