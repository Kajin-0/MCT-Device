# Source ledger addendum — Round 48 machine-checkable provenance

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`  
**Round classification:** `DERIVED-INTERNAL-CONTROL / SOFTWARE-LOGIC`

## 1. Scope

Round 48 introduces no new historical HgCdTe process source and makes no new RP-01 documentary claim.

The round converts already-controlled P16/P22 systems logic into a machine-readable schema and executable semantic validator.

No physical measurement, material inventory, process setpoint, yield, device result, user credential or laboratory implementation is introduced.

---

# 2. Controlled input basis

Round 48 derives from:

- P16F phased empirical-campaign states;
- P16G sample genealogy/material allocation;
- P16H sequential release control;
- P16I zero-HgCdTe dry-run/fault-injection architecture;
- P22C campaign execution/material release;
- P22D control-system dry run;
- Round-47 repaired acyclic dependency model.

The permanent controlling logic retained is:

`GO only if technical/scientific eligibility passes AND post-commit material feasibility passes`.

Holdout, reserve, rework and configuration rules are also retained.

---

# 3. New implementation artifacts

Added:

- `schemas/mct_provenance_bundle.schema.json`
- `tools/validate_mct_provenance.py`
- `provenance/README.md`
- `provenance/fixtures/valid/nominal_round48_bundle.json`
- one invalid-case mutation bundle defining eight deliberately invalid cases
- `.github/workflows/provenance-validation.yml`
- `docs/DIGITAL_PROVENANCE_STATE_MACHINE_SPEC_ROUND48.md`
- `travelers/P16J_DIGITAL_PROVENANCE_VALIDATION_REGISTER.md`
- this source ledger
- Round-48 gap matrix
- Round-48 checkpoint

AGENTS is refreshed separately.

---

# 4. Schema standard selection

The structural file declares:

`https://json-schema.org/draft/2020-12/schema`

This is a deliberate schema dialect selection, not a claim that it is the newest possible standard.

No network dependency is required by the runtime semantic validator.

Evidence class:

`ENGINEERING-DATA-MODEL-SELECTION`.

---

# 5. Major derived concept — immutable state node

Round 48 separates:

- stable `physical_object_id`;
- immutable `material_node.id`.

Evidence basis:

- Round-45 genealogy requirement;
- Round-46 rework identity restriction;
- Round-47 fault-injection finding that state-changing rework cannot silently retain protected identity.

Derived rule:

For a normal state transition, physical identity persists but scientific-state node identity changes.

Evidence class:

`DERIVED-INTERNAL-CONTROL`.

This is not a physical claim about material behavior.

---

# 6. Process-lineage mode

Two lineage modes are implemented:

- `STATE_TRANSITION`;
- `SPLIT`.

`STATE_TRANSITION` requires one input, one output and preserved physical-object ID.

`SPLIT` requires one input and at least two distinct physical-object outputs.

This implements Round-45 delayed differentiation and explicit singulation/descendant genealogy.

Evidence class:

`DERIVED-INTERNAL-CONTROL`.

---

# 7. Gate prerequisite assertions

P16H previously stored aggregate technical/material status and gate disposition.

Round 48 adds machine-readable prerequisite assertions:

`{key, status, evidence_record_ids}`.

Derived release rule:

A software `GO` is permitted only if:

- technical status PASS;
- material status PASS;
- every prerequisite assertion PASS;
- all assertion evidence records exist.

Evidence class:

`DERIVED-INTERNAL-CONTROL`.

The generic validator does not manufacture the domain prerequisite list; P22C/P16H remain authoritative for what must be asserted at each gate.

---

# 8. Configuration/calibration binding

Round-47 fault injection demonstrated that a calendar-valid calibration does not prove validity after configuration change.

Round 48 encodes:

- time-bounded configuration object;
- calibration bound to configuration;
- event/gate/measurement references to both;
- event-time interval checks.

Evidence class:

`DERIVED-INTERNAL-CONTROL`.

No actual instrument calibration is implied.

---

# 9. Holdout access control

Round-46/47 distinction retained:

`validity QC access != protected scientific outcome access`.

Round 48 encodes:

- protected response fields;
- holdout lock;
- model-freeze event;
- QC access;
- outcome access.

Validator rejects:

- QC access to protected response fields;
- outcome access before model freeze;
- model freeze not linked to holdout;
- training measurement containing protected holdout response fields.

Evidence class:

`DERIVED-INTERNAL-CONTROL`.

This is logical access validation only. Actual future ACL/permissions are not implemented.

---

# 10. Reserve release control

Rounds 45–47 require holdouts/reserves not to become emergency spare inventory.

Round 48 models reserve control append-only:

`reserve_lock -> reserve_release`.

The lock freezes a trigger key.

The release must use the same key and cite basis evidence.

GO on the locked reserve before release is rejected.

Evidence class:

`DERIVED-INTERNAL-CONTROL`.

No real material reserve exists.

---

# 11. Rework control

Round 47 established:

`state-changing rework -> original protected role invalid by default`.

Round 48 encodes this by requiring:

- rework event;
- new material-state node;
- reassigned role;
- explicit equivalence approval if protected role is retained.

Evidence class:

`DERIVED-INTERNAL-CONTROL`.

---

# 12. Evidence promotion

The Round-44/46 empirical progression remains:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`.

Round 48 machine-validates one-step progression and required G8/holdout/bridge/allocation references.

Evidence class:

`DERIVED-INTERNAL-CONTROL`.

No empirical quantity is promoted by the repository fixtures.

---

# 13. Raw-data hash

Round 48 requires a raw-data URI plus SHA-256 digest syntax on measurement records.

Purpose is provenance/content identity.

Evidence class:

`ENGINEERING-CONTROL`.

Repository validation does not dereference the URI or hash real bytes.

That is a future laboratory implementation gap.

---

# 14. Synthetic self-test

Local Round-48 self-test basis:

- one nominal valid bundle;
- eight deliberately invalid cases generated from the controlled mutation bundle.

Expected:

- nominal bundle passes;
- all invalid bundles are rejected.

The invalid bundle classes are:

1. GO despite material FAIL;
2. genealogy cycle;
3. holdout outcome opened before model freeze;
4. protected holdout field leaked into training;
5. locked reserve consumed;
6. reserve release trigger mismatch;
7. stale configuration/calibration used;
8. state-changing rework retains protected role.

Evidence class:

`SOFTWARE-LOGIC-TEST`.

This is not a physical reliability statistic.

---

# 15. New P16J state

Repository software state:

`P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED`.

Physical implementation state:

`P16J-LAB-PROVENANCE-SYSTEM-READY`.

Round-48 repository result:

- repository validator: YES after successful controlled fixture self-test;
- lab provenance system: NO / NOT PHYSICALLY INSTANTIATED.

This does not modify any upstream physical maturity state.

---

# 16. External-source status

No external web search or new literature source family was needed.

Reason:

The work is an internal control/data-model implementation derived from existing repository rules.

Round 48 does not use software architecture choices to upgrade any HgCdTe evidence class.

---

# 17. Remaining evidence boundary

Not established:

- authenticated actor identity;
- ACL enforcement;
- cryptographic signature trust;
- trusted timestamping;
- actual append-only database;
- backup/disaster recovery;
- instrument API integration;
- actual raw-byte digest checking;
- actual laboratory configuration objects;
- actual P16I laboratory dry run.

These remain implementation gaps rather than documentary HgCdTe gaps.
