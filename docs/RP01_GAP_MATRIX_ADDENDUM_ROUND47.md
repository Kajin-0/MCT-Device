# RP-01 gap matrix addendum — Round 47 control-system dry run

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Purpose

Update the open-gap structure after the zero-HgCdTe dependency/fault-injection dry run.

Round 47 closes two repository-logic gaps:

1. the P16F/P16G circular prerequisite;
2. the Stage-0 data-before-readiness ambiguity.

It does not close physical implementation gaps.

---

# 2. New/updated gap states

Use the following states where appropriate:

- `CONTROL-GRAPH-CYCLE-CLOSED`
- `STAGE0-SCOPE-DEPENDENCY-CLOSED`
- `LOGIC-DRY-RUN-PASS`
- `LAB-DRY-RUN-OPEN`
- `DIGITAL-GENEALOGY-SCHEMA-OPEN`
- `HOLDOUT-ACCESS-CONTROL-OPEN`
- `CONFIGURATION-INVALIDATION-AUTOMATION-OPEN`
- `RESERVE-LOCK-ENFORCEMENT-OPEN`
- `REAL-LAB-FAULT-INJECTION-OPEN`

---

# 3. Gap G47-01 — monolithic P16F/P16G cycle

### Prior state

P16F defined campaign structure but final P16F disposition required genealogy/material feasibility from P16G. P16G in turn required the campaign structure from P16F.

### Round-47 repair

P16F now has scoped phases:

- campaign skeleton;
- design-definition readiness;
- final campaign readiness.

P16G consumes the design-definition state; final P16F readiness consumes P16G.

### State

`CONTROL-GRAPH-CYCLE-CLOSED`.

### Remaining physical gap

A future lab may introduce new local dependencies/cycles. P16I lab dry run remains required.

---

# 4. Gap G47-02 — Stage-0 readiness deadlock risk

### Prior ambiguity

P16F needs Stage-0 variance/repeatability for final information/resolution planning, but G0 could be read as requiring a ready campaign before Stage-0 material is consumed.

### Round-47 repair

Stage-0 uses `P16F-CAMPAIGN-SKELETON-DEFINED`, not final P16F readiness.

Full P16F design-definition/readiness is evaluated only after Stage-0 data exist.

### State

`STAGE0-SCOPE-DEPENDENCY-CLOSED`.

---

# 5. Gap G47-03 — actual laboratory dry run

The repository logic can be tested synthetically, but no actual lab control system exists.

Still open:

- actual configuration database;
- actual calibration-object linkage;
- real gate workflow;
- sample-ID scanning/labeling;
- real holdout permissions;
- real reserve locks;
- actual event/audit logging;
- surrogate/dummy physical traversal.

### State

`LAB-DRY-RUN-OPEN`.

Blocking for:

`P16I-LAB-DRY-RUN-PASSED`.

Not required to claim the current repository-level logic pass.

---

# 6. Gap G47-04 — digital genealogy/data schema

The repository specifies what must be recorded but does not yet define a machine-checkable schema.

Required entities include:

- material node;
- parent-child edge;
- process/treatment event;
- measurement event;
- configuration revision;
- calibration revision;
- gate decision;
- holdout lock;
- reserve lock;
- model-freeze event;
- deviation;
- rework event;
- evidence-promotion event;
- audit actor/timestamp.

### State

`DIGITAL-GENEALOGY-SCHEMA-OPEN`.

This is the strongest current systems-control gap.

---

# 7. Gap G47-05 — holdout-access enforcement

Human-readable rules distinguish:

- validity-QC access;
- scientific-outcome access.

But no real permissions system exists.

Required future implementation:

- model-freeze ID created before protected outcome open;
- access log;
- pre-freeze QC field whitelist;
- role-based scientific-result release;
- immutable record showing result was not available during model fit.

### State

`HOLDOUT-ACCESS-CONTROL-OPEN`.

---

# 8. Gap G47-06 — configuration invalidation automation

P36/P22C require impact review after configuration change, but no implementation currently propagates invalidation automatically.

Future system should support:

`configuration change -> affected calibration/acceptance objects -> affected future gates -> HOLD until review/requalification`.

It must avoid both:

- under-containment;
- unjustified global invalidation.

### State

`CONFIGURATION-INVALIDATION-AUTOMATION-OPEN`.

---

# 9. Gap G47-07 — reserve-lock enforcement

Round 45/46 define reserve classes and release triggers, but there is no machine-level lock.

Required future behavior:

- reserve node carries protected purpose;
- proposed reassignment checks release trigger;
- unauthorized reassignment is rejected/logged;
- substitute node must be formally allocated before release where applicable.

### State

`RESERVE-LOCK-ENFORCEMENT-OPEN`.

---

# 10. Gap G47-08 — real-lab fault injection

Synthetic logic cases pass after repair, but future physical implementation should inject representative non-HgCdTe failures:

- bad barcode/ID scan;
- expired/changed calibration;
- simulated MFC/fixture revision;
- mock holdout-access denial;
- failed surrogate measurement;
- attempted reserve reassignment;
- rework state transition;
- audit recovery after interrupted workflow.

### State

`REAL-LAB-FAULT-INJECTION-OPEN`.

---

# 11. Synthetic cases now covered

Round 47 covers, at the logic level:

1. irrelevant late-stage subsystem missing;
2. P16F/P16G cycle;
3. P06 metrology failure;
4. LPE execution excursion;
5. anneal multicarrier state;
6. RIE excursion;
7. material shortage despite technical PASS;
8. valid holdout prediction failure;
9. execution-invalid holdout;
10. MFC/configuration change;
11. attempted holdout-as-spare use;
12. state-changing holdout rework;
13. genealogy loss;
14. detector test-chain invalidity;
15. package holdout failure.

No additional numerical process data are generated by these tests.

---

# 12. Maturity status after Round 47

The following remain NO unless separately physically closed:

- `TRACEABLE-FIRST-BUILD-READY`;
- `HISTORICAL-RP01-REPRODUCED`;
- `REPRODUCIBLE-RELEASE`;
- `P16C-INFRASTRUCTURE-READY`;
- `P16D-SURROGATE-COMMISSIONING-COMPLETE`;
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE`;
- `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`;
- `P16G-MATERIAL-GENEALOGY-PLAN-READY`;
- `P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY`.

New design-validation state:

- `P16I-LOGIC-DRY-RUN-PASSED = YES`.

Still open:

- `P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`.

---

# 13. Strategic implication

The project no longer needs another layer of prose describing how to react to obvious failures before the control records themselves are digitized.

The strongest next closure is a normalized digital provenance schema and state machine that makes:

- identity;
- genealogy;
- configuration;
- gate decisions;
- holdout locks;
- reserve locks;
- model freeze;
- deviations;
- evidence promotion

machine-checkable.

That work can also be performed without HgCdTe and will make the future real-lab P16I dry run substantially more meaningful.