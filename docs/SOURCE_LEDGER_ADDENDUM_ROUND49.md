# Source ledger addendum — Round 49 operational provenance reference application

**Date:** 2026-08-16 America/New_York  
**Classification:** `DERIVED-INTERNAL-CONTROL / SOFTWARE-REFERENCE-IMPLEMENTATION`

## Scope

Round 49 introduces no new historical HgCdTe process evidence and performs no external literature search.

It operationalizes already controlled Round-45 through Round-48 requirements using Python standard library and SQLite.

## Controlled internal basis

Primary inputs:

- Round-45 genealogy/material allocation;
- Round-46 sequential material-release control;
- Round-47 zero-HgCdTe control-system dry run;
- Round-48 digital provenance schema/validator;
- P16G/P16H/P16I/P16J registers.

## New derived implementation claims

### Append-only database behavior

Evidence class: `DERIVED-INTERNAL / EXECUTABLE-SOFTWARE-TEST`.

SQLite triggers in the reference database reject UPDATE/DELETE against controlled append-only tables.

Restriction: this does not protect against a privileged user replacing/copying the database file outside the application.

### Transactional state changes

Evidence class: `DERIVED-INTERNAL / EXECUTABLE-SOFTWARE-DESIGN`.

Multi-record batches use one SQLite transaction so a new state node and corresponding process event can commit atomically.

### Holdout logical sealing

Evidence class: `DERIVED-INTERNAL / APPLICATION-PERMISSION-TEST`.

Protected values are stored separately and exposed only through a model-freeze/independent-reviewer path.

Restriction: no encryption-at-rest claim. Direct database administrators can bypass application enforcement.

### Raw-data content addressing

Evidence class: `DERIVED-INTERNAL / BYTE-INTEGRITY-TEST`.

Raw files are copied into a SHA-256-addressed object store and rehashed. Synthetic tampering is detected.

### Configuration invalidation propagation

Evidence class: `DERIVED-INTERNAL / EXECUTABLE-CONTROL-TEST`.

Superseding a configuration marks dependent historical GO decisions nonreusable for future release. The original historical gate record is retained.

### Prototype electronic signature

Evidence class: `DERIVED-INTERNAL / CONTENT-AUTHENTICATION-PROTOTYPE`.

HMAC-SHA256 binds target record digest, actor label, key ID and signing time in the reference implementation.

Restriction: no identity, nonrepudiation, regulatory, trusted-time or production key-custody claim.

## Synthetic-only restriction

Round 49 uses synthetic material IDs and synthetic raw files. No local HgCdTe material, instrument calibration or laboratory identity has been instantiated.

## No evidence promotion

Round 49 does not change any historical/process readiness state. Its positive result applies only to the repository reference application if the final committed CI succeeds.
