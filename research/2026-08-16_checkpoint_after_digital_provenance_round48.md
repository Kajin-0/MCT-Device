# Research checkpoint — after machine-checkable digital provenance Round 48

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 47 proved that the repaired repository control architecture was logically coherent under the declared synthetic fault set, but all controls remained primarily prose/register logic.

Round 48 objective:

> Convert the highest-value genealogy, release, holdout, reserve, configuration, rework and evidence-promotion rules into an executable data contract and semantic validator before any physical HgCdTe or laboratory system exists.

No HgCdTe was processed. No instrument/calibration/sample inventory exists in the repository.

---

# 2. New controlled artifacts

Added:

- `schemas/mct_provenance_bundle.schema.json`
- `tools/validate_mct_provenance.py`
- `provenance/README.md`
- `provenance/fixtures/valid/nominal_round48_bundle.json`
- one invalid-case mutation bundle under `provenance/fixtures/invalid/` defining eight invalid cases
- `.github/workflows/provenance-validation.yml`
- `docs/DIGITAL_PROVENANCE_STATE_MACHINE_SPEC_ROUND48.md`
- `travelers/P16J_DIGITAL_PROVENANCE_VALIDATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND48.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND48.md`
- this checkpoint.

AGENTS is refreshed at end of round.

---

# 3. New P16J states

Round 48 separates repository software validation from actual laboratory implementation.

Repository:

`P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED`

Laboratory:

`P16J-LAB-PROVENANCE-SYSTEM-READY`

Controlled Round-48 result:

- repository validator = YES;
- lab provenance system = NO / NOT PHYSICALLY INSTANTIATED.

---

# 4. Major result 1 — immutable scientific state versus persistent physical object

A physical HgCdTe piece can undergo anneal, RIE, passivation, metallization, singulation and packaging while remaining physically related to an earlier state.

Overwriting one “sample row” would erase causally important state history.

Round 48 therefore freezes:

`physical_object_id != material_node.id`.

For an ordinary state transition:

- one input;
- one output;
- same physical-object ID;
- new immutable scientific-state node.

For a physical split:

- one input;
- at least two outputs;
- distinct physical-object IDs;
- immutable parent link retained.

This formalizes Round-45 genealogy and Round-47 rework identity.

---

# 5. Major result 2 — two validation layers

Structural contract:

`schemas/mct_provenance_bundle.schema.json`

uses JSON Schema Draft 2020-12.

Cross-record validator:

`tools/validate_mct_provenance.py`

uses Python standard library only.

Reason for split:

JSON Schema is suitable for local shape/type/enumeration constraints.

It is not sufficient by itself for:

- graph cycles;
- parent/root consistency;
- event chronology;
- cross-record references;
- configuration/calibration validity at event time;
- holdout freeze/access chronology;
- training-set leakage;
- reserve-release ordering;
- rework role changes;
- evidence-state progression.

---

# 6. Major result 3 — fourteen normalized record types

Implemented:

1. material_node
2. process_event
3. measurement
4. configuration
5. calibration
6. gate_decision
7. holdout_lock
8. reserve_lock
9. reserve_release
10. model_freeze
11. access_event
12. deviation_rework
13. evidence_promotion
14. audit_event

This is intentionally smaller than a full laboratory database.

The objective is to preserve scientific/control invariants, not model every administrative field.

---

# 7. Major result 4 — machine-readable gate prerequisites

A gate no longer contains only aggregate T/M state.

It also contains:

`prerequisite_assertions = [{key, status, evidence_record_ids}, ...]`.

Validator requirement:

`GO iff T=PASS AND M=PASS AND all declared prerequisite assertions PASS`.

All referenced evidence records must exist.

This means software can reject a GO even when an operator accidentally records an aggregate PASS but one prerequisite assertion remains HOLD/FAIL.

P22C/P16H remain authoritative for which domain prerequisites must exist.

---

# 8. Major result 5 — configuration/calibration validity is temporal and bound

Every process event, measurement and gate may reference configuration and calibration objects.

The validator checks:

- configuration valid interval;
- calibration valid interval/status;
- calibration belongs to referenced configuration;
- event time lies inside both.

This prevents the Round-47 MFC-replacement failure mode from being hidden by an unexpired old calibration date.

---

# 9. Major result 6 — holdout data can exist while outcome remains sealed

Round 48 explicitly supports:

`measurement acquired -> QC fields inspected -> model frozen -> protected outcome opened`.

Protected response fields are named in the holdout lock.

QC access before freeze is legal only if fields do not overlap protected response fields.

Outcome access before model freeze is rejected.

The validator also rejects protected holdout response fields inside the training data of the model being tested.

This is stronger than simply recording a holdout label.

---

# 10. Major result 7 — reserve release is append-only

The initial design considered a mutable lock state.

Round 48 strengthened this before commit.

Controlled architecture is now:

`reserve_lock -> reserve_release`.

The lock freezes a release-trigger key.

The release event must:

- reference the lock;
- use the same trigger key;
- cite basis records;
- occur after lock.

A GO on protected material before a valid release event is rejected.

This better preserves auditability than toggling a Boolean field.

---

# 11. Major result 8 — rework creates a new state node

State-changing rework is not an edit to the prior sample state.

It is:

`old node -> REWORK process event -> new node`.

If the old node is HOLDOUT/FIT_POINT/DETECTOR_BRIDGE, the new node cannot retain that protected role without explicit equivalence approval.

This is the executable version of Round-47 FI-12.

---

# 12. Major result 9 — evidence promotion is sequential

Machine progression remains:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`.

The validator rejects skipped stages.

Verified and later states require PASS holdout evidence.

Detector-bridged/allocation states require a detector bridge.

Allocation eligibility also requires uncertainty and valid-range references.

A G8 GO is required.

---

# 13. Major result 10 — raw data is content-addressed

Measurement records require:

- raw-data URI;
- SHA-256 digest.

The repository bundle can therefore refer to large raw files without embedding them.

Round 48 validates hash syntax only.

Future lab implementation must calculate/check hashes against actual bytes.

---

# 14. Synthetic self-test result

Local controlled test set:

- valid fixtures: 1;
- invalid fixtures: 8.

Invalid scenarios:

1. gate GO with material FAIL;
2. genealogy cycle;
3. holdout outcome before freeze;
4. protected holdout field leaked into model training;
5. locked reserve consumed;
6. reserve release uses wrong trigger key;
7. stale configuration/calibration used;
8. state-changing rework retains protected role.

Result:

`SELF-TEST PASSED: 1 valid + 8 invalid fixtures`.

The nominal bundle was additionally checked against the declared Draft-2020-12 JSON Schema during Round-48 development and produced zero schema errors.

The GitHub workflow uses dependency-free semantic validation and JSON syntax checking so validation does not depend on a third-party runtime package.

---

# 15. CI protection

New workflow:

`.github/workflows/provenance-validation.yml`.

On changes to schema/validator/fixtures/workflow it:

1. checks schema JSON syntax;
2. runs provenance self-test.

This turns future regression in the control logic into an explicit CI failure.

No claim is made until the workflow actually runs on GitHub after commit.

---

# 16. Important implementation boundary

Repository-level P16J PASS does not establish:

- user authentication;
- authorization/ACL;
- real holdout field sealing;
- trusted electronic signatures;
- trusted time source;
- tamper-evident storage;
- backup/disaster recovery;
- automatic instrument ingestion;
- real raw-byte hash verification;
- physical configuration IDs;
- calibration integration;
- a real LIMS/database.

These remain future lab implementation requirements.

---

# 17. Relationship to P16I

Round 47:

`P16I-LOGIC-DRY-RUN-PASSED = YES`.

Round 48:

`P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED = YES`.

Future intended chain:

`P16I logic dry run`
`-> P16J repository implementation`
`-> P16J real lab implementation`
`-> P16I lab dry run`
`-> controlled HgCdTe use when all other gates permit`.

This keeps software/control maturity separate from process maturity.

---

# 18. Maturity after Round 48

Remain NO/open:

- TRACEABLE-FIRST-BUILD-READY;
- HISTORICAL-RP01-REPRODUCED;
- REPRODUCIBLE-RELEASE;
- P16C infrastructure;
- P16D surrogate commissioning;
- P16E allocation completion;
- P16F campaign readiness;
- P16G genealogy readiness;
- P16H sequential-control lab readiness;
- P16I lab dry run;
- P16J lab provenance system.

Repository logic states:

- `P16I-LOGIC-DRY-RUN-PASSED = YES`;
- `P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED = YES`.

No physical promotion occurred.

---

# 19. Next logical work — Round 49

The next high-value zero-HgCdTe step is to make the provenance layer **operationally instantiable**, not merely validatable.

Recommended Round 49:

1. define canonical ID namespaces and lifecycle;
2. define file/database layout and transaction semantics;
3. define actor/role/permission matrix for holdout sealing and gate approvals;
4. define raw-data ingestion + SHA-256 verification workflow;
5. define configuration supersession/invalidation propagation;
6. define electronic signature/audit semantics without claiming regulatory compliance;
7. build a small local reference implementation that creates/validates bundles;
8. run an automated synthetic G0–G8 traversal through that reference implementation.

The goal should be a deployable local prototype suitable for a future no-HgCdTe P16I lab dry run.
