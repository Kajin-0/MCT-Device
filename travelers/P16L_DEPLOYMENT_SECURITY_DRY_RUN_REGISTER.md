# P16L — deployment/security dry-run register

**Status:** CONTROLLED REPOSITORY DEPLOYMENT-SECURITY REGISTER / ROUND 50  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16I/P16J/P16K, Round-48 validator, Round-49 application, Round-50 deployment modules.

## 1. States

`P16L-REFERENCE-DEPLOYMENT-SECURITY-DRY-RUN-PASSED = YES / NO`

`P16L-LAB-SECURITY-DEPLOYMENT-READY = YES / NO`

Round-50 target after final committed CI:

- reference = YES;
- laboratory = NO / NOT PHYSICALLY INSTANTIATED.

## 2. Implementation identity

Repository commit: ____________________  
CI run: ____________________  
Deployment-control module: `tools/mct_deployment_control.py`  
Protected-vault module: `tools/mct_protected_vault.py`  
Fixture: `tools/round50_fixture.py`  
Integrated runner: `tools/run_round50_security.py`  
Reviewer: ____________________  
Date: ____________________

## 3. Identity/session matrix

| identity type | intended capability | forbidden cross-capability tested? | PASS/FAIL |
|---|---|---|---|
| SERVICE_INSTRUMENT | instrument/protected ingest | gate approval |  |
| SERVICE_CONFIG | config/calibration import and supersession | unrelated release |  |
| SERVICE_SIGNER | sign/verify | instrument/release operation |  |
| SERVICE_BACKUP | backup create/verify/restore | release/instrument operation |  |
| OP_RELEASE | release gate | instrument ingest |  |
| OP_INDEPENDENT | holdout outcome open/verify | protected ingest |  |
| OP_DOE | holdout/model/evidence control | direct instrument ingest |  |
| OP_ADMIN | deployment administration | N/A reference superuser |  |

Session stored by digest only: YES / NO  
Expiry checked: YES / NO  
Append-only revocation present: YES / NO  
Revoked-session denial tested: YES / NO

**Boundary:** bearer session != authenticated person/service account.

## 4. Clock audit

Forward observation accepted: PASS / FAIL  
Backward wall-clock observation rejected: PASS / FAIL  
Later forward observation accepted: PASS / FAIL  
Monotonic observation recorded: YES / NO

External authoritative time source integrated: YES / NO  
Round-50 repository expected: NO.

`CLOCK-REGRESSION-GUARD != TRUSTED-TIME`.

## 5. Instrument/configuration audit

Initial synthetic configuration/calibration imported: PASS / FAIL  
Dummy measurement acquired under valid pair: PASS / FAIL  
Replacement configuration imported: PASS / FAIL  
Replacement calibration imported: PASS / FAIL  
Old configuration superseded: PASS / FAIL  
Dependent historical GO marked nonreusable: PASS / FAIL  
Stale adapter rejected before raw copy: PASS / FAIL  
Replacement adapter acquired successfully: PASS / FAIL

Real instrument interface qualified: YES / NO  
Round-50 expected: NO.

## 6. Protected-vault audit

Protected vault root isolated from ordinary store: YES / NO  
Protected raw CAS separate: YES / NO  
Protected value database separate: YES / NO  
Ordinary measurement contains vault URI + hash only: YES / NO  
Unique protected marker absent from ordinary store tree: PASS / FAIL  
Round-49 ordinary sealed table unused for new Round-50 holdout: PASS / FAIL  
Protected raw hash verifies: PASS / FAIL  
Pre-freeze outcome access denied: PASS / FAIL  
Wrong-role outcome access denied: PASS / FAIL  
Post-freeze independent-reviewer access succeeds: PASS / FAIL  
Round-48 access event emitted: YES / NO

Protected storage encrypted: YES / NO  
Round-50 expected: NO.

Reason: split-store isolation was selected rather than introducing custom cryptography.

## 7. File-permission audit

Key file mode `0600`: PASS / FAIL  
Key directory mode `0700`: PASS / FAIL  
Protected vault directory mode `0700`: PASS / FAIL  
Main store directory mode `0700`: PASS / FAIL

Separate actual OS users: YES / NO  
ACL/MAC confinement tested: YES / NO  
Root/admin bypass prevented: YES / NO

Round-50 repository expected for all three: NO.

## 8. Key lifecycle audit

Signature key created ACTIVE: PASS / FAIL  
Rotation creates new ACTIVE key: PASS / FAIL  
Old key becomes VERIFY_ONLY: PASS / FAIL  
Historical signature remains cryptographically valid under VERIFY_ONLY: PASS / FAIL  
VERIFY_ONLY key prohibited from new signing: PASS / FAIL  
New-key signature trusted: PASS / FAIL  
Old key revoked: PASS / FAIL  
Old historical signature still cryptographically valid but trust state REVOKED: PASS / FAIL  
Verification history append-only: PASS / FAIL

KMS/HSM/TPM integrated: YES / NO  
Escrow/recovery policy qualified: YES / NO  
Round-50 expected: NO / NO.

## 9. Backup/restore audit

Backup databases captured through SQLite backup API: PASS / FAIL  
Ordinary CAS included: PASS / FAIL  
Protected CAS included: PASS / FAIL  
Canonical file manifest generated: PASS / FAIL  
Manifest authenticated with BACKUP_HMAC: PASS / FAIL  
Backup key excluded from backup: PASS / FAIL  
Untampered backup verifies: PASS / FAIL  
Tampered backup fails: PASS / FAIL  
Restore requires verification first: PASS / FAIL  
Restore goes to new destination: PASS / FAIL  
Restored main raw objects verify: PASS / FAIL  
Restored protected raw objects verify: PASS / FAIL  
Restored main record count matches: PASS / FAIL  
Restored vault count matches: PASS / FAIL

Backup encrypted: YES / NO  
Remote/off-site durability tested: YES / NO  
Key-loss recovery tested: YES / NO

Round-50 expected: NO / NO / NO.

## 10. Regression audit

Round-48 fixture suite PASS: YES / NO  
Round-49 operational suite `19/19`: YES / NO  
Round-50 deployment/security suite `33/33`: YES / NO  
Round-50 generated bundle Round-48 semantic errors: ________  
Required: `0`.

Round-50 generated provenance record count: ________  
Candidate result: `50`.

## 11. Candidate-branch controlled result

Candidate commit: `1639fee3f75d9ba11df066ed7d194c946953ac3d`  
Candidate CI run: `31980899498`

Observed:

- Round-48 regression: PASS;
- Round-49: `19/19`;
- Round-50: `33/33`;
- final generated records: `50`;
- Round-48 semantic errors: `0`;
- protected vault raw objects: `1`;
- protected vault sealed values: `1`;
- key objects: `3`;
- signature verification events: `3`;
- configuration supersessions in combined run: `2`;
- gate invalidations: `10`.

Candidate PASS does not alone set the final main-branch state. Final controlled main CI must reproduce the result.

## 12. Repository disposition

After final main CI:

All declared Round-50 controls PASS: YES / NO  
Earlier regression suites PASS: YES / NO  
No Round-48 semantic errors: YES / NO  
No real HgCdTe used: YES / NO  
No unresolved repository-level invariant violation: YES / NO

Final repository state:

`P16L-REFERENCE-DEPLOYMENT-SECURITY-DRY-RUN-PASSED = YES / NO`

## 13. Laboratory disposition

Actual dedicated host instantiated: YES / NO  
Actual service accounts/OS ownership instantiated: YES / NO  
Production authentication instantiated: YES / NO  
Vetted protected-data encryption/KMS or approved equivalent instantiated: YES / NO  
Real key custody/rotation/recovery exercised: YES / NO  
External time policy instantiated: YES / NO  
Real backup/restore drill complete: YES / NO  
Real instrument adapter qualified: YES / NO  
Real configuration/calibration source integrated: YES / NO  
P16I laboratory dry run passed: YES / NO

Final laboratory state:

`P16L-LAB-SECURITY-DEPLOYMENT-READY = YES / NO`

Round-50 repository disposition remains:

`NO / NOT PHYSICALLY INSTANTIATED`.

## 14. Prohibited inference

Do not infer any of the following from a repository P16L pass:

- production cybersecurity certification;
- regulatory electronic-signature compliance;
- encrypted backup;
- trusted signer identity;
- trusted time;
- laboratory LIMS qualification;
- HgCdTe process validation;
- first-build readiness;
- historical RP-01 reproduction;
- reproducible release.
