# Source ledger addendum — Round 47 zero-HgCdTe control-system dry run

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`  
**Round classification:** `DERIVED-INTERNAL-CONTROL / SYNTHETIC-FAULT-INJECTION`

## 1. Scope

Round 47 introduces no new historical HgCdTe process source and makes no new claim about the exact RP-01 traveler.

The round tests the repository's own control architecture using synthetic dependency analysis and synthetic fault cases.

No physical material, equipment or laboratory result is assumed.

---

# 2. Controlled internal basis

Primary controlled inputs:

- P16F empirical-Jacobian campaign register;
- P16G genealogy/material-allocation register;
- P16H sequential material-release register;
- P22A/B/C DOE, genealogy and release-control procedures;
- P18 failure-analysis atlas;
- P36/P36A commissioning/acceptance architecture;
- Round-43 uncertainty allocation;
- Round-44 information-optimal design;
- Round-45 sample genealogy;
- Round-46 sequential material release.

Round 47 derives systems-control consequences from those modules.

---

# 3. New artifacts

Round 47 adds:

- `calculations/RP01_CONTROL_DEPENDENCY_FAULT_INJECTION.md`;
- `procedures/P22D_ZERO_HGCDTE_CONTROL_SYSTEM_DRY_RUN.md`;
- `travelers/P16I_CONTROL_SYSTEM_DRY_RUN_REGISTER.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND47.md`;
- this source-ledger addendum;
- `research/2026-08-16_checkpoint_after_control_system_dry_run_round47.md`.

It also repairs the P16F/P16G readiness interface and refreshes AGENTS.

---

# 4. Finding R47-01 — P16F/P16G circular prerequisite

## Controlled text basis

P16G requires the campaign structure, independent-unit definitions, holdouts and structural design counts that are defined through P16F/P22A.

P16F final disposition also asks whether the genealogy/material plan is feasible, which P16G provides.

## Derived systems result

Representing both P16F and P16G as monolithic final states yields:

`P16F -> P16G -> P16F`.

### Evidence class

`DERIVED-INTERNAL / CONTROL-GRAPH-DEFECT`.

### Repair

P16F is split into:

- `P16F-CAMPAIGN-SKELETON-DEFINED`;
- `P16F-DESIGN-DEFINITION-READY`;
- `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`.

P16G consumes the design-definition state; final P16F readiness then consumes P16G.

### Post-repair result

Directed prerequisite cycles in the tested dependency spine: `0`.

This does not prove a future lab's local workflow is cycle-free; it validates the current repository-level graph.

---

# 5. Finding R47-02 — Stage-0 readiness ambiguity

## Controlled text basis

P16F information-optimal design needs Stage-0 repeatability/variance to establish resolvable perturbations and practical design size.

P22C G0 requires an active campaign-design state before material consumption.

## Derived systems result

If G0 Stage-0 were interpreted to require final P16F readiness, a data-before-readiness deadlock would occur.

### Repair

Stage-0 G0 requires:

- relevant P16C/P16D capability/acceptance;
- scope-adequate P16E measurement discrimination;
- `P16F-CAMPAIGN-SKELETON-DEFINED`;
- Stage-0 material protection;
- data/genealogy controls;
- EH&S.

Final P16F readiness is not required before the Stage-0 data used to define it exist.

### Evidence class

`DERIVED-INTERNAL / SCOPE-DEPENDENCY-REPAIR`.

---

# 6. Finding R47-03 — technical eligibility and material feasibility remain orthogonal

Round 46 established:

`GO iff T=PASS and M=PASS`.

Round-47 FI-07 deliberately tests `T=PASS, M=FAIL`.

Expected and obtained logical disposition:

`NO GO`.

### Evidence class

`DERIVED-INTERNAL / INVARIANT-TEST`.

This is a logical validation, not a physical material result.

---

# 7. Finding R47-04 — holdout failure and holdout invalidity require different routing

## Scientific prediction failure

If execution-valid holdout data disagree with the model:

- holdout remains valid evidence;
- empirical promotion is blocked/downgraded;
- revised model requires a new independent holdout for equivalent verification.

## Execution invalidity

If a predeclared validity criterion fails, such as broken wiring or corrupt acquisition:

- result may be invalidated under that criterion;
- replacement follows the predeclared rule;
- scientific response cannot be used for tuning before replacement.

### Evidence class

`DERIVED-INTERNAL / HOLDOUT-CONTROL-TEST`.

---

# 8. Finding R47-05 — configuration invalidation is local but strict

Synthetic case: an RIE MFC is replaced after commissioning.

Derived result:

- affected gas-delivery equivalence/acceptance must be re-reviewed even if the calendar calibration date elsewhere is still valid;
- releases relying on that realization are held;
- unrelated FTIR/Hall/package evidence is not globally invalidated without common-cause evidence.

### Evidence class

`DERIVED-INTERNAL / CONFIGURATION-CONTROL-TEST`.

This is consistent with P36's principle that configuration change can invalidate prior acceptance.

---

# 9. Finding R47-06 — minimum justified invalidation set

Round 47 formalizes a containment concept:

For fault `f`, begin with directly affected nodes and descendants that depend on the affected state/equivalence.

Do not expand the invalidation set without evidence of common cause.

Do not contract it merely to preserve schedule/material.

### Evidence class

`DERIVED-INTERNAL / SYSTEMS-CONTROL`.

---

# 10. Synthetic fault cases

Round 47 exercises 15 logical cases covering:

- late-stage subsystem unavailability;
- readiness cycle;
- metrology insufficiency;
- LPE execution excursion;
- anneal multicarrier transition;
- RIE excursion;
- material shortage despite technical PASS;
- valid holdout prediction failure;
- execution-invalid holdout;
- MFC/configuration change;
- attempted holdout-as-spare use;
- state-changing holdout rework;
- genealogy loss;
- detector test-chain invalidity;
- package holdout failure.

After the two architecture repairs, all 15 cases produce the intended fail-safe logical disposition.

### Restriction

`15/15` is not a reliability rate, probability of safe operation, software test coverage metric or process yield. It means only that the 15 declared synthetic scenarios comply with the repaired rule set.

---

# 11. New P16I states

Round 47 introduces:

`P16I-LOGIC-DRY-RUN-PASSED`

and

`P16I-LAB-DRY-RUN-PASSED`.

Current:

- `P16I-LOGIC-DRY-RUN-PASSED = YES`;
- `P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`.

The first is a repository-level systems-design validation.

The second requires a real laboratory traveler/LIMS/configuration system and cannot be claimed now.

---

# 12. Non-promotion constraints

Round 47 does not promote:

- `TRACEABLE-FIRST-BUILD-READY`;
- `HISTORICAL-RP01-REPRODUCED`;
- `REPRODUCIBLE-RELEASE`;
- P16C/P16D physical readiness;
- P16E completion;
- P16F/P16G/P16H physical readiness.

It validates control logic only.

---

# 13. Documentary status

No external source search was required because all Round-47 claims are about internal dependency/control logic and synthetic scenarios derived from already controlled repository modules.

No historical evidence class is changed.

---

# 14. Next evidence need

The next control layer should convert the human-readable genealogy/gate architecture into a machine-checkable data schema.

Key objects should include:

- immutable material nodes;
- parent-child edges;
- treatment events;
- configuration/calibration revisions;
- gate decisions;
- holdout locks/access events;
- reserve locks/releases;
- model-freeze records;
- deviations/rework;
- raw-data references;
- audit history.

This would be a digital-provenance architecture, not another process-recipe search.