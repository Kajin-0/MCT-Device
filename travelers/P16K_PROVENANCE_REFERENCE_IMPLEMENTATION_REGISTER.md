# P16K — operational provenance reference implementation register

**Status:** CONTROLLED REPOSITORY / FUTURE-LAB IMPLEMENTATION REGISTER — ROUND 49  
**Date:** 2026-08-16 America/New_York

## 1. States

`P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED = YES / NO`

`P16K-LAB-DEPLOYMENT-QUALIFIED = YES / NO`

Round-49 target repository state: YES.  
Current laboratory deployment state: `NO / NOT PHYSICALLY INSTANTIATED`.

## 2. Implementation identity

Repository commit: ____________________  
Store module: `tools/mct_provenance_store.py`  
Traversal/self-test: `tools/run_round49_reference.py`  
Round-48 validator: `tools/validate_mct_provenance.py`  
Schema: `schemas/mct_provenance_bundle.schema.json`  
CI workflow: `.github/workflows/provenance-validation.yml`

## 3. Storage audit

SQLite database created: YES / NO  
WAL mode enabled: YES / NO  
Foreign keys enabled: YES / NO  
Synchronous FULL selected: YES / NO  
Controlled tables append-only by trigger: YES / NO  
Direct UPDATE negative test rejected: YES / NO  
Direct DELETE behavior reviewed: YES / NO

## 4. Identity audit

Canonical `MCT-<CLASS>-timestamp-random` generator active: YES / NO  
Record ID immutable: YES / NO  
Physical-object ID distinct from material-state ID: YES / NO  
Split produces distinct physical-object IDs: YES / NO

## 5. Transaction audit

Single-record transaction method: YES / NO  
Atomic multi-record batch method: YES / NO  
State transition commits material node + process event atomically: YES / NO  
Failure rolls back complete batch: YES / NO / NOT TESTED

## 6. Role / permission audit

| Role | implemented | future real identity mapped? |
|---|---|---|
| SYSTEM_ADMIN | YES |  |
| PROCESS_OWNER | YES |  |
| METROLOGY_OWNER | YES |  |
| DOE_OWNER | YES |  |
| MATERIAL_CONTROL | YES |  |
| RELEASE_AUTHORITY | YES |  |
| INDEPENDENT_REVIEWER | YES |  |

Unauthorized holdout outcome access rejected: YES / NO  
Unauthorized gate creation rejected: YES / NO / NOT TESTED  
Real authentication provider: NOT IMPLEMENTED / ____________________

## 7. Holdout sealing audit

Protected outcome stored separately from ordinary measurement record: YES / NO  
Protected field inaccessible through normal measurement payload: YES / NO  
Model freeze required before outcome opening: YES / NO  
Independent-reviewer role required: YES / NO  
Round-48 access event created before value returned: YES / NO  
Direct database administrator bypass possible: YES / NO  
Required current answer for reference SQLite prototype: YES.

Cryptographic field encryption implemented: YES / NO  
Round-49 reference answer: NO.

## 8. Raw-data integrity audit

Content-addressed object directory used: YES / NO  
SHA-256 before copy: YES / NO  
SHA-256 after copy: YES / NO  
Atomic rename: YES / NO  
Byte re-verification before bundle export: YES / NO  
Tamper negative test detected: YES / NO  
Restored object reverified: YES / NO

## 9. Reserve audit

Locked reserve GO rejected: YES / NO  
Explicit reserve-release event required: YES / NO  
Frozen trigger key must match: YES / NO  
Basis record required: YES / NO  
Synthetic legal release succeeds: YES / NO

## 10. Configuration supersession audit

New configuration can declare old configuration superseded: YES / NO  
Operational supersession event stored append-only: YES / NO  
New use of old configuration blocked after supersession: YES / NO  
Dependent prior GO gates marked nonreusable: YES / NO  
Unrelated evidence preserved: YES / NO

## 11. Signature semantics audit

Record payload digest immutable: YES / NO  
HMAC-SHA256 reference signature implemented: YES / NO  
Correct key verifies: YES / NO  
Wrong key fails: YES / NO  
Production key management implemented: YES / NO  
Required Round-49 answer: NO.

Regulatory signature claim made: YES / NO  
Required: NO.

## 12. Synthetic G0-G8 traversal

| Gate | GO observed? | synthetic node/evidence |
|---|---|---|
| G0 |  |  |
| G1 |  |  |
| G2 |  |  |
| G3 |  |  |
| G4 |  |  |
| G5 |  |  |
| G6 |  |  |
| G7 |  |  |
| G8 |  |  |

Nine of nine nominal gates GO: YES / NO

## 13. Round-48 compatibility

Generated bundle record count: __________  
Round-48 semantic errors: __________  
Required: 0.

Schema JSON syntax CI: PASS / FAIL  
Round-48 fixture self-test CI: PASS / FAIL  
Round-49 application self-test CI: PASS / FAIL

## 14. Repository result

Operational controls passed: __________ / __________  
G0-G8 nominal gates: __________ / 9  
Round-48 semantic errors: __________  
CI run ID: ____________________  
CI conclusion: ____________________

`P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED = YES / NO`

## 15. Future laboratory deployment

Real laboratory database location: ____________________  
Authentication/identity provider: ____________________  
Real role assignments: ____________________  
Encrypted protected-field storage: ____________________  
Key-management system: ____________________  
Trusted time source: ____________________  
Backup/restore validation: ____________________  
Instrument adapters: ____________________  
Actual configuration registry: ____________________  
Actual calibration registry: ____________________  
P16I laboratory dry run revision/result: ____________________

`P16K-LAB-DEPLOYMENT-QUALIFIED = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** repository reference-application PASS is not laboratory provenance readiness, HgCdTe validation, P16A first-build readiness, historical reproduction, or P17 release.
