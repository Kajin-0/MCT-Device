# P16J — digital provenance / machine-validation register

**Status:** CONTROLLED SYSTEMS-IMPLEMENTATION REGISTER / ROUND 48  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16I, P16H, P22C/P22D, `schemas/mct_provenance_bundle.schema.json`, `tools/validate_mct_provenance.py`.

## 1. Purpose

Record whether the MCT-Device provenance/state-machine architecture is:

1. machine-valid at repository level; and
2. actually instantiated in a future laboratory control system.

Two distinct states are tracked:

`P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED = YES / NO`

`P16J-LAB-PROVENANCE-SYSTEM-READY = YES / NO`

Round-48 repository state:

- `P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED = YES`;
- `P16J-LAB-PROVENANCE-SYSTEM-READY = NO / NOT PHYSICALLY INSTANTIATED`.

---

# 2. Repository implementation identity

Repository/commit: ____________________  
Schema path: `schemas/mct_provenance_bundle.schema.json`  
Schema version: `mct-provenance-1.0.0`  
Semantic validator path: `tools/validate_mct_provenance.py`  
Fixture root: `provenance/fixtures/`  
CI workflow: `.github/workflows/provenance-validation.yml`

Validator revision/hash: ____________________  
Schema revision/hash: ____________________  
Reviewer: ____________________  
Date: ____________________

---

# 3. Record-class implementation matrix

| Record class | structural schema present? | semantic references checked? | lab implementation object/table | status |
|---|---|---|---|---|
| material_node | YES | YES |  |  |
| process_event | YES | YES |  |  |
| measurement | YES | YES |  |  |
| configuration | YES | YES |  |  |
| calibration | YES | YES |  |  |
| gate_decision | YES | YES |  |  |
| holdout_lock | YES | YES |  |  |
| reserve_lock | YES | YES |  |  |
| reserve_release | YES | YES |  |  |
| model_freeze | YES | YES |  |  |
| access_event | YES | YES |  |  |
| deviation_rework | YES | YES |  |  |
| evidence_promotion | YES | YES |  |  |
| audit_event | YES | YES |  |  |

---

# 4. Material identity / genealogy audit

Physical-object identity persists across state transitions: PASS / FAIL  
New immutable material-node ID created for each state: PASS / FAIL  
`STATE_TRANSITION` enforces one input / one output: PASS / FAIL  
`STATE_TRANSITION` preserves `physical_object_id`: PASS / FAIL  
`SPLIT` enforces one input / >=2 outputs: PASS / FAIL  
Split output physical-object IDs distinct: PASS / FAIL  
Parent references exist: PASS / FAIL  
Root consistency validated: PASS / FAIL  
Genealogy DAG cycle detection active: PASS / FAIL  
Child cannot predate parent: PASS / FAIL  
Process outputs linked to process inputs: PASS / FAIL

Laboratory implementation evidence IDs: ____________________

---

# 5. Gate-machine audit

For every gate, confirm software stores:

- [ ] gate code G0–G8
- [ ] material node if applicable
- [ ] proposed operation
- [ ] evaluation timestamp
- [ ] flattened evidence record list
- [ ] individual prerequisite assertions
- [ ] technical status
- [ ] material status
- [ ] final `GO/HOLD/REWORK/STOP`
- [ ] configuration IDs
- [ ] calibration IDs
- [ ] reviewer IDs
- [ ] release scope

Machine rule:

`GO only if T=PASS and M=PASS and every prerequisite assertion=PASS`

Implemented: YES / NO  
Negative test executed: YES / NO  
Evidence/test ID: ____________________

---

# 6. Configuration / calibration audit

Configuration object includes validity interval: YES / NO  
Calibration bound to exact configuration ID: YES / NO  
Calibration status checked at event time: YES / NO  
Configuration validity checked at event time: YES / NO  
Calibration cannot be silently used with another configuration: YES / NO  
Stale configuration negative fixture rejected: YES / NO

Future lab change-control test:

Hardware/configuration changed: ____________________  
Old configuration ID: ____________________  
New configuration ID: ____________________  
Old future GO correctly blocked/reviewed: YES / NO  
Requalification evidence: ____________________

---

# 7. Holdout lock / access audit

Holdout lock identifies protected response fields: YES / NO  
Holdout carries explicit model key: YES / NO  
QC and OUTCOME access distinct: YES / NO  
QC access overlapping protected response rejected: YES / NO  
OUTCOME before model freeze rejected: YES / NO  
Freeze must list holdout: YES / NO  
Training-set leakage from protected holdout fields rejected: YES / NO  
Outcome fields constrained to protected set: YES / NO

Future laboratory permission enforcement:

Protected fields actually hidden by software ACL/UI: YES / NO / NOT IMPLEMENTED  
Actor identity authenticated: YES / NO / NOT IMPLEMENTED  
Unauthorized access attempt recorded: YES / NO / NOT TESTED

---

# 8. Reserve audit

Reserve lock has explicit purpose: YES / NO  
Reserve lock has immutable release-trigger key: YES / NO  
Reserve release is a separate append-only event: YES / NO  
Release must use matching trigger key: YES / NO  
Release requires basis records: YES / NO  
GO before valid reserve release rejected: YES / NO  
Wrong-trigger negative fixture rejected: YES / NO

Future laboratory reserve-release approval evidence: ____________________

---

# 9. Rework audit

State-changing rework creates a new material node: YES / NO  
Rework process event linked: YES / NO  
Old node retained in history: YES / NO  
Protected role retention requires explicit equivalence approval: YES / NO  
Negative fixture retaining holdout/bridge role rejected: YES / NO

Future laboratory role-reassignment evidence: ____________________

---

# 10. Evidence-promotion audit

Allowed sequence:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`

No stage skipping: PASS / FAIL  
G8 GO required: PASS / FAIL  
PASS holdout required for verified and later states: PASS / FAIL  
Detector bridge required for detector-bridged and allocation states: PASS / FAIL  
Uncertainty + valid range required for allocation eligibility: PASS / FAIL

---

# 11. Raw-data integrity audit

Measurement raw-data URI present: YES / NO  
SHA-256 digest present: YES / NO  
Digest syntax validated: YES / NO

Future laboratory implementation:

Storage system: ____________________  
Digest computed automatically at ingest: YES / NO  
Digest rechecked before analysis: YES / NO  
Mismatch blocks evidence promotion: YES / NO  
Immutable/archive storage: ____________________

Round-48 repository validator checks digest syntax only. It does not fetch a laboratory URI and verify bytes.

---

# 12. Synthetic fixture result

Valid fixture count expected: `1`  
Invalid fixture count expected: `8`

Invalid cases:

1. `gate_go_material_fail`
2. `genealogy_cycle`
3. `holdout_outcome_before_freeze`
4. `holdout_training_leak`
5. `locked_reserve_consumption`
6. `reserve_release_wrong_trigger`
7. `stale_configuration`
8. `rework_retains_holdout`

Repository self-test result: ____________________  
Valid accepted: __________ / 1  
Invalid rejected: __________ / 8  
Unexpected validator crash: YES / NO

Required repository PASS:

- valid fixture accepted;
- every invalid fixture rejected;
- no unexpected exception;
- schema JSON parses;
- controlled validator version recorded.

---

# 13. CI audit

Workflow file present: YES / NO  
Workflow triggers on schema/validator/fixture changes: YES / NO  
Schema JSON syntax check included: YES / NO  
Semantic self-test included: YES / NO  
External Python package required: YES / NO

Round-48 design target: `NO` external runtime package required.

Latest CI run ID: ____________________  
Result: PASS / FAIL / NOT RUN

---

# 14. Append-only implementation audit

Material state overwritten in place: YES / NO  
Required: NO.

Failed/invalid process record deletable without audit record: YES / NO  
Required: NO.

STOP event retained: YES / NO  
Failed holdout retained: YES / NO  
State-changing rework creates new state: YES / NO  
Audit event used for invalidation/review: YES / NO

Actual database/file-system append-only guarantee: ____________________

---

# 15. Security boundary

The following are not established by repository-level validation alone:

| Capability | repository-level status | future lab status |
|---|---|---|
| user authentication | NOT ESTABLISHED |  |
| authorization / ACL | NOT ESTABLISHED |  |
| protected-field UI enforcement | NOT ESTABLISHED |  |
| trusted timestamp | NOT ESTABLISHED |  |
| cryptographic signer identity | NOT ESTABLISHED |  |
| tamper-evident database | NOT ESTABLISHED |  |
| backup / disaster recovery | NOT ESTABLISHED |  |
| instrument API ingestion | NOT ESTABLISHED |  |
| automatic raw-byte hash verification | NOT ESTABLISHED |  |

Do not promote P16J laboratory readiness while required local security/control capabilities are merely represented as JSON fields rather than enforced.

---

# 16. P16I laboratory dry-run handoff

P16J lab system instantiated: YES / NO  
Dummy/surrogate material nodes created: YES / NO  
Actual configuration objects created: YES / NO  
Actual calibration objects created: YES / NO  
Actual gate records created: YES / NO  
Holdout access permissions tested: YES / NO  
Reserve lock/release tested: YES / NO  
Configuration invalidation tested: YES / NO  
Rework role reassignment tested: YES / NO  
G0–G8 synthetic/surrogate traversal recorded: YES / NO

Eligible to re-run P16I laboratory dry run: YES / NO

---

# 17. Repository disposition

Schema structurally controlled: YES  
Semantic validator controlled: YES  
Nominal synthetic fixture accepted: YES  
Eight declared invalid fixtures rejected: YES  
Repository machine layer therefore:

`P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED = YES`

No actual laboratory system exists:

`P16J-LAB-PROVENANCE-SYSTEM-READY = NO / NOT PHYSICALLY INSTANTIATED`

---

# 18. Final future-lab disposition

Repository validator PASS: YES / NO  
Lab data model instantiated: YES / NO  
Permissions/security implemented: YES / NO  
Configuration/calibration integration implemented: YES / NO  
Raw-data hashing implemented: YES / NO  
Append-only/audit behavior implemented: YES / NO  
P16I lab dry run passed: YES / NO  
Known invariant violations unresolved: YES / NO

Final:

`P16J-LAB-PROVENANCE-SYSTEM-READY = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** P16J lab readiness is control-system readiness. It does not create HgCdTe empirical evidence, P16A first-build readiness, historical reproduction, or P17 reproducible release.
