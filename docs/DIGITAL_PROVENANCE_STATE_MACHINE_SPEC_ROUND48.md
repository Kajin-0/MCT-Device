# Round 48 — machine-checkable digital provenance and traveler state model

**Status:** CONTROLLED REPOSITORY ARCHITECTURE / ZERO-HGCDTE  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Purpose

Rounds 44–47 defined information-efficient empirical campaigns, material genealogy, sequential `GO / HOLD / REWORK / STOP` release, and synthetic dependency/fault-injection logic.

Round 48 converts those controls into records that software can validate.

The objective is not to build a full LIMS. It is to define the smallest normalized data model that can later be implemented in a LIMS, database, file-backed traveler, or laboratory application without changing the scientific control semantics.

No physical HgCdTe, instrument, calibration, sample inventory, actor credential or laboratory authorization is asserted.

---

# 2. Controlled implementation

Round 48 adds:

- `schemas/mct_provenance_bundle.schema.json`
- `tools/validate_mct_provenance.py`
- `provenance/README.md`
- synthetic valid/invalid fixtures under `provenance/fixtures/`
- `.github/workflows/provenance-validation.yml`

The structural contract is JSON Schema Draft 2020-12.

The semantic validator uses Python standard library only.

This split is intentional. JSON Schema controls local record shape, required fields, primitive types and enumerations. It does not adequately express whole-program graph cycles, cross-record chronology, holdout access after model freeze, configuration validity at event time, protected reserve release, role retention after state-changing rework, or sequential evidence promotion. Those invariants are checked by the semantic validator.

---

# 3. Bundle identity

Canonical top-level fields:

```text
schema_version = mct-provenance-1.0.0
bundle_id
created_at
mode = SYNTHETIC | LAB
records[]
```

`SYNTHETIC` is used for repository dry runs. `LAB` is reserved for an actual laboratory implementation.

In a `SYNTHETIC` bundle every record must explicitly have:

```text
synthetic = true
```

This prevents synthetic fixture data from being mistaken for physical evidence.

---

# 4. Record classes

The controlled schema contains fourteen scientific/control record classes.

## 4.1 `material_node`

One immutable scientific state of one physical material object.

Key fields include `physical_object_id`, `parent_node_ids`, `root_node_id`, `state_time`, `state_label`, `roles`, `experimental_unit_id`, and `terminal`.

## 4.2 `process_event`

One treatment or physical transformation.

Key fields include event class, procedure, input/output material nodes, configuration/calibration references, start/end times, execution status, irreversibility, state-changing status, and `lineage_mode`.

Allowed lineage modes are:

- `STATE_TRANSITION`
- `SPLIT`

## 4.3 `measurement`

One metrology/acquisition event. It records material node, method, configuration/calibration, acquisition time, QC state, named result fields, and content-addressed raw-data references.

Raw-data references require:

```text
uri
sha256
```

The provenance bundle does not embed large instrument data by default.

## 4.4 `configuration`

A physical/software method configuration such as RIE chamber revision, MFC revision, sample fixture, P06 optical path, P12 transfer chain, or package fixture.

Configuration validity is time bounded.

## 4.5 `calibration`

A calibration belongs to one particular configuration.

A calibration is not portable to an arbitrary later configuration merely because its calendar date has not expired.

## 4.6 `gate_decision`

Machine-readable P22C/P16H release decision.

Required aggregate states are:

```text
technical_status
material_status
decision
```

Every gate also carries explicit prerequisite assertions:

```text
key
status
evidence_record_ids
```

A `GO` requires:

```text
technical_status = PASS
material_status = PASS
every prerequisite assertion = PASS
```

## 4.7 `holdout_lock`

Locks a material node as a scientific holdout and defines the campaign, protected model key, protected response fields, lock time, and replacement rule.

## 4.8 `reserve_lock`

Locks material against ordinary consumption and freezes a `release_trigger_key`.

The reserve is not unlocked by editing the lock record.

## 4.9 `reserve_release`

Append-only event that releases a reserve. It references the lock, uses the same trigger key, supplies basis records/reviewers, and occurs after the lock.

## 4.10 `model_freeze`

Records model identity/revision, freeze time, training measurements, protected holdout locks and model digest.

## 4.11 `access_event`

Records access to protected holdout data.

Modes:

- `QC`
- `OUTCOME`

QC access before model freeze is permitted only for fields that do not overlap protected response fields. Outcome access requires an applicable prior model freeze.

## 4.12 `deviation_rework`

Records deviation class, disposition, state-changing status, rework process event, new state node/reassigned role, and optional equivalence approval.

## 4.13 `evidence_promotion`

Records one step in:

```text
EMPIRICAL-REQUIRED
-> DESIGN-IDENTIFIED
-> DESIGN-RESOLUTION-VERIFIED
-> EMPIRICAL-PRELIMINARY
-> EMPIRICAL-VERIFIED
-> DETECTOR-BRIDGED
-> ALLOCATION-ELIGIBLE
```

No stage skipping is permitted.

## 4.14 `audit_event`

Records review/signature/invalidation actions and a digest. Round 48 validates digest syntax, not real cryptographic signer identity.

---

# 5. Major architecture result — physical object versus scientific state

A single HgCdTe piece can persist physically while changing scientifically.

Round 48 therefore separates:

```text
physical_object_id
```

from:

```text
material_node.id
```

Example:

```text
MAT-GROWTH-001
-> MAT-ANNEALED-001
-> MAT-RIE-001
-> MAT-DETECTOR-001
```

For ordinary `STATE_TRANSITION`:

- exactly one input;
- exactly one output;
- `physical_object_id` remains unchanged.

The old material node is never overwritten.

A physical cut uses `SPLIT`.

For `SPLIT`:

- exactly one input;
- at least two outputs;
- each output receives a distinct physical-object ID;
- each child points immutably to the parent state.

This is the machine-checkable version of Round-45 descendant genealogy.

---

# 6. Material genealogy invariants

The validator requires:

1. globally unique record IDs;
2. every parent reference exists;
3. material parent references point to material nodes;
4. material genealogy is acyclic;
5. root nodes have no parent and point to themselves as root;
6. descendants resolve to their declared root;
7. child state time cannot precede parent state time;
8. process-event output parents equal the process-event input node set;
9. multiple ancestry roots are rejected by the current HgCdTe material model.

The multi-root rejection is deliberate. A package assembly containing a die plus carrier/adhesive is not modeled as merging two HgCdTe roots. Non-HgCdTe construction items belong in configuration/process records.

---

# 7. Gate invariants

For every `gate_decision`, `GO` is legal only when:

```text
technical_status = PASS
AND material_status = PASS
AND all prerequisite assertions = PASS.
```

Assertion evidence must exist and also appear in the flattened prerequisite list.

This allows a future interface to show both the aggregate P22C decision and the individual evidence facts producing it.

Round 48 does not hard-code every domain-specific G0–G8 prerequisite inside the generic validator. Those requirements remain controlled by P22C/P16H. The machine layer validates that declared prerequisites are explicit, traceable and passing before `GO`.

---

# 8. Configuration and calibration invariants

For process events, measurements and gates:

- referenced configuration must be valid at event time;
- referenced calibration must be `VALID`;
- event time must lie inside calibration validity;
- calibration must belong to a configuration also named by that record.

Therefore:

```text
calendar-valid calibration != configuration equivalence.
```

If an MFC or fixture is replaced and a new configuration object is created, a future event cannot silently cite the retired configuration/calibration.

This machine-enforces a major Round-47 fault-injection result.

---

# 9. Holdout invariants

A holdout lock defines protected response fields, for example:

```text
protected_response_fields = [Dstar, noise_asd]
```

Before model freeze, QC access may inspect a field such as:

```text
temperature_qc
```

but may not inspect `Dstar` or `noise_asd`.

An `OUTCOME` access requires:

1. a referenced model-freeze record;
2. the freeze lists this holdout;
3. freeze time precedes outcome access;
4. accessed outcome fields are a subset of protected response fields.

The validator additionally rejects a model freeze whose training measurements contain protected response fields from its own holdout node.

Thus:

```text
measurement acquired
```

does not imply:

```text
scientific outcome opened.
```

A laboratory may physically acquire a holdout result and keep protected fields sealed until model freeze.

---

# 10. Reserve invariants

A reserve is append-only controlled.

Sequence:

```text
reserve_lock
-> reserve_release
-> later GO
```

The validator rejects `GO` on a locked reserve node before a valid release event.

A reserve release must use the exact trigger key frozen by the lock.

For example:

```text
FA_PURPOSE_CLOSED_OR_SUBSTITUTED
```

cannot be replaced after a failure by an informal reason equivalent to “we need more material.”

This prevents emergency relabeling from masquerading as controlled release.

---

# 11. Rework invariants

State-changing rework is represented as:

```text
old material node
-> REWORK process event
-> new material node
```

The old state remains immutable.

If the original node carries a protected role such as `HOLDOUT`, `FIT_POINT`, or `DETECTOR_BRIDGE`, the new node may not automatically retain that role.

The validator requires explicit equivalence approval if a protected role is retained.

The conservative default is therefore:

```text
state-changing rework -> new scientific identity.
```

---

# 12. Evidence-promotion invariants

Evidence advances one step at a time.

The validator rejects:

```text
DESIGN-IDENTIFIED -> EMPIRICAL-VERIFIED
```

as a skipped progression.

Promotion to `EMPIRICAL-VERIFIED`, `DETECTOR-BRIDGED`, or `ALLOCATION-ELIGIBLE` requires a PASS holdout.

Promotion to detector-bridged or allocation-eligible also requires an explicit detector bridge.

Allocation eligibility additionally requires uncertainty and valid-range references.

Every evidence-promotion record references a `G8` gate whose decision is `GO`.

---

# 13. Content-addressed data

A measurement's raw-data reference contains a SHA-256 digest.

Purpose:

- detect accidental or silent replacement;
- allow large raw data to remain outside provenance JSON;
- bind analysis to exact acquisition bytes.

Round 48 does not prescribe storage location. A future lab may use a file server, object store, LIMS attachment store, or immutable archive.

The requirement is that the object at the recorded URI can be checked against the digest.

---

# 14. Append-only philosophy

The preferred implementation is append-only.

Do not overwrite material states, failed process events, failed holdouts, STOP decisions, deviations, invalid measurements, or evidence-promotion failures.

Corrections create new controlled records and invalidate/review prior records through audit events.

Round 48 does not yet implement a transactional database or cryptographic append-only ledger. It establishes the data semantics such a system must preserve.

---

# 15. Synthetic fixture validation

The repository self-test contains one nominal valid synthetic bundle and a mutation-spec bundle defining deliberately invalid cases.

The invalid fixtures currently exercise:

1. `GO` with material status FAIL;
2. material genealogy cycle;
3. holdout outcome access before model freeze;
4. holdout protected-response leakage into training data;
5. locked reserve consumption;
6. reserve release with wrong trigger key;
7. stale configuration/calibration usage;
8. state-changing rework retaining protected holdout/bridge role.

Expected behavior:

```text
valid fixtures -> accepted
invalid fixtures -> rejected
```

This is a software logic test, not a reliability statistic.

---

# 16. Continuous validation

`.github/workflows/provenance-validation.yml` runs on relevant repository changes.

It performs:

1. JSON syntax validation of the schema;
2. semantic self-test of valid/invalid provenance fixtures.

The semantic validator has no third-party runtime dependency.

---

# 17. New integration state — P16J

Round 48 introduces:

```text
P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED
```

and:

```text
P16J-LAB-PROVENANCE-SYSTEM-READY
```

Repository state after successful fixture validation:

```text
P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED = YES
```

Physical laboratory state:

```text
P16J-LAB-PROVENANCE-SYSTEM-READY = NO / NOT PHYSICALLY INSTANTIATED
```

P16J repository PASS means:

- schema parses;
- nominal fixture passes;
- declared invalid fixtures are rejected;
- machine-readable invariants are implemented.

It does not mean actual laboratory IDs, access permissions, authenticated signatures, database/LIMS infrastructure, or P16I laboratory dry-run completion exist.

---

# 18. Security and implementation boundary

Round 48 deliberately does not claim:

- user authentication;
- authorization/ACL enforcement;
- hardware-backed signatures;
- trusted timestamps;
- tamper-evident database storage;
- remote backup;
- disaster recovery;
- instrument API ingestion;
- automatic raw-data hash verification against real storage.

These are future laboratory implementation requirements.

---

# 19. Relationship to P16I

Round 47:

```text
P16I-LOGIC-DRY-RUN-PASSED = YES
```

tested the conceptual state machine.

Round 48 converts major invariants from prose into executable validation.

A future:

```text
P16I-LAB-DRY-RUN-PASSED = YES
```

should require an installed provenance system that creates P16J-compliant records during a complete dummy/surrogate G0–G8 traversal.

Intended systems sequence:

```text
P16I logic dry run
-> P16J repository schema/validator
-> real P16J lab implementation
-> P16I lab dry run
```

---

# 20. Non-promotion warning

Round 48 adds machine-readable control infrastructure.

It does not establish `TRACEABLE-FIRST-BUILD-READY`, `HISTORICAL-RP01-REPRODUCED`, `REPRODUCIBLE-RELEASE`, P16C–P16H physical completion, or P16I laboratory dry-run completion.

No HgCdTe result is created by a JSON record.

---

# 21. Immediate future use

When a real laboratory is identified, instantiate this schema first with surrogate/dummy records for actual equipment configuration, calibration, dummy material, process event, measurement/raw-data hash, gate assertions, holdout lock, reserve lock/release, model freeze, access event, rework, evidence promotion, and audit/signature.

Only after the real implementation passes should this provenance layer be trusted to control HgCdTe campaign execution.
