# P22D — zero-HgCdTe control-system dry run and fault-injection qualification

**Status:** CONTROLLED SYSTEMS-QUALIFICATION METHOD / ROUND 47  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16F/P16G/P16H/P16I, P22C, P18, P36/P36A, P20/P20A.

## 1. Purpose

Qualify the logic of the development-control system before scarce HgCdTe is consumed.

P22D is a zero-HgCdTe exercise. It uses synthetic material IDs, synthetic gate records and synthetic failure events to test whether the repository's readiness, genealogy, holdout and release rules behave coherently.

It must detect:

- circular prerequisites;
- impossible gate requirements;
- unintended global blocking;
- unsafe reserve release;
- holdout contamination;
- invalid rework-role retention;
- configuration-change propagation errors;
- genealogy dead ends;
- evidence-promotion paths that bypass a required gate.

P22D does not commission physical equipment and does not replace P36.

---

# 2. Two dry-run layers

## Layer A — repository logic dry run

Uses documents and synthetic cases only.

State:

`P16I-LOGIC-DRY-RUN-PASSED = YES / NO`.

This layer may be completed without a physical lab.

## Layer B — laboratory control dry run

Uses the actual LIMS/traveler system, actual configuration IDs, real calibration records and surrogate/dummy samples, but no HgCdTe where avoidable.

State:

`P16I-LAB-DRY-RUN-PASSED = YES / NO`.

This layer cannot be completed until the laboratory exists.

The states must never be conflated.

---

# 3. Required graph model

Construct a directed graph containing at minimum:

- P16B candidate branch;
- relevant P16C capability nodes;
- relevant P16D commissioning/acceptance nodes;
- scope-adequate P16E measurement-discrimination nodes;
- P16F phased design states;
- P16G material/genealogy states;
- P16H control-system state;
- G0-G8 material/evidence gates;
- protected holdout/reserve roles;
- major terminal archive/FA/STOP states.

Every edge shall identify:

- prerequisite output;
- scope;
- whether it is physical, analytical, configuration, material or governance dependence;
- invalidation rule if the parent changes.

A graph with an unexplained directed cycle fails the logic dry run.

---

# 4. P16F phased readiness — mandatory Round-47 interpretation

P16F shall no longer be interpreted as one prerequisite node for every phase.

## 4.1 `P16F-CAMPAIGN-SKELETON-DEFINED`

Used before Stage-0.

Minimum fields:

- protected quantity/decision;
- response vector;
- experimental unit;
- candidate factor/state list;
- Stage-0 variance/repeatability plan;
- preliminary feasibility/safety bounds;
- candidate blocking variables.

This state is intentionally incomplete.

## 4.2 `P16F-DESIGN-DEFINITION-READY`

Used after Stage-0 and before final P16G allocation.

Minimum fields:

- Stage-0 variance/repeatability data;
- frozen experimental unit;
- model/design family;
- structural run count;
- information criterion;
- perturbation-resolution check;
- blocking/hard-to-change structure;
- holdout structural definition;
- stopping/invalidation logic.

This is the direct upstream input to P16G.

## 4.3 `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`

Final state after P16G has shown physical genealogy/material feasibility and relevant infrastructure/EH&S are ready.

Permanent dependency:

`P16F skeleton -> Stage-0 -> P16F design definition -> P16G -> final P16F readiness`.

---

# 5. G0 scope rule

G0 is evaluated for the immediate material-consuming action, not for the eventual entire program.

For a Stage-0 experiment, G0 requires:

- capability and P16D acceptance for the Stage-0 process/measurement chain;
- P16E discrimination adequate to interpret the Stage-0 contrast/repeatability question;
- `P16F-CAMPAIGN-SKELETON-DEFINED`;
- a Stage-0 material-protection allocation showing that the proposed pilot does not consume protected future roles;
- data/genealogy controls;
- EH&S authorization.

It does **not** require:

- full P16F campaign readiness;
- the full final P16G material plan;
- package infrastructure unrelated to the Stage-0 evidence;
- P17 release capability.

For later formal campaigns, the required readiness level rises according to the edge.

---

# 6. Dry-run roles

Assign for the exercise:

- dry-run controller;
- mock process owner;
- mock metrology owner;
- mock genealogy/material owner;
- mock statistical owner;
- holdout reviewer;
- configuration-control reviewer;
- auditor.

One person may simulate multiple roles for the repository-only exercise, but the role transitions must still be explicit.

---

# 7. Synthetic material namespace

Use IDs that cannot be confused with real material.

Recommended prefix:

`SYN-R47-...`

Examples:

- `SYN-R47-ROOT-001`;
- `SYN-R47-ANNEAL-003-A`;
- `SYN-R47-RIE-007-HALL`;
- `SYN-R47-DET-004`;
- `SYN-R47-PKG-HOLDOUT-002`.

Every synthetic descendant must retain parent links exactly as a real node would.

Do not reuse real detector IDs in a dry run.

---

# 8. Mandatory fault classes

The logic dry run shall inject at least one case from each class.

## 8.1 Dependency fault

Examples:

- circular readiness prerequisite;
- final-state requirement before the data needed to define that state exist.

Expected control behavior: detect and repair graph before physical execution.

## 8.2 Metrology fault

Examples:

- P06 repeatability inadequate;
- calibration invalid after configuration change;
- detector test transfer function invalid.

Expected: HOLD the affected edge; do not compensate by consuming more samples.

## 8.3 Process-execution fault

Examples:

- LPE thermal excursion;
- anneal trajectory excursion;
- RIE pressure/self-bias/temperature excursion.

Expected: preserve raw event, contain affected siblings, invoke P18, protect uncommitted material.

## 8.4 Scientific-regime fault

Examples:

- multicarrier anneal state;
- RIE state outside the model's valid regime;
- package introduces an unmodeled dominant pole.

Expected: retain as scientific evidence but prevent inappropriate model/evidence promotion.

## 8.5 Material-feasibility fault

Example:

- technically good candidate would consume the only holdout/bridge.

Expected: technical PASS + material FAIL = no GO.

## 8.6 Holdout fault

Two separate cases are mandatory:

- scientifically failed but execution-valid holdout;
- execution-invalid holdout.

Expected outcomes must differ.

## 8.7 Reserve fault

Attempt unauthorized use of locked reserve/holdout after unrelated sample loss.

Expected: denial unless a release trigger/substitute/redesign is formally recorded.

## 8.8 Rework fault

Apply a state-changing rework to a fit point or holdout.

Expected: re-evaluate scientific role; old role not retained automatically.

## 8.9 Identity/genealogy fault

Inject ambiguous or lost node identity.

Expected: quarantine/STOP; never reconstruct identity from expected response.

## 8.10 Late-stage subsystem fault

Make a package subsystem unavailable during an upstream campaign.

Expected: no upstream deadlock unless that subsystem is required to preserve the intended evidence.

---

# 9. Pass/fail criteria for a synthetic fault

A fault case passes only if all applicable conditions are satisfied:

1. correct gate result occurs;
2. affected material set is no larger than necessary and no smaller than justified;
3. protected holdouts/reserves remain locked unless their explicit trigger fires;
4. failed/negative evidence remains in the ledger;
5. rework role is reassigned correctly;
6. configuration invalidation propagates to affected descendants;
7. no unrelated evidence is silently erased;
8. no evidence state is promoted through the fault;
9. terminal node role is explicit;
10. audit trail is complete.

---

# 10. Minimum justified invalidation set

For fault `f`, define:

`A_f` = directly affected configuration/material nodes.

`D(A_f)` = descendants that rely on the affected state or equivalence.

The initial invalidation set is:

`I_f = A_f union D(A_f)`

subject to explicit preserved baselines/equivalence boundaries.

The set may be expanded only when a shared-cause hypothesis is supported by evidence.

It may not be contracted merely to protect schedule or yield.

This prevents both overreaction and under-containment.

---

# 11. Holdout access simulation

For each synthetic holdout record two permissions:

- `QC_ACCESS`;
- `SCIENTIFIC_OUTCOME_ACCESS`.

Before model freeze:

- QC_ACCESS may be granted only to fields needed to establish execution validity;
- SCIENTIFIC_OUTCOME_ACCESS remains locked.

After model freeze:

- outcome may be opened by the designated reviewer;
- model/version hash is stored before opening.

If prediction fails:

- record failed prediction;
- do not modify that frozen model and still call the same holdout independent verification;
- if a revised model is fitted, allocate a new independent holdout for new verification.

---

# 12. Configuration-change simulation

At least one fault shall modify a configuration element after commissioning, for example:

- MFC replacement;
- chamber electrode/holder change;
- FTIR optical-path change;
- Hall contact method change;
- preamplifier/cable change;
- package fixture change.

The dry run must demonstrate:

- calendar-valid calibration alone does not preserve equivalence;
- affected P16D/P36 acceptance is placed in impact review/HOLD;
- prior material evidence remains historically recorded;
- future releases using the altered configuration are blocked until the required requalification is complete;
- unrelated subsystems remain usable.

---

# 13. Stage-by-stage synthetic traversal

Execute at least one nominal synthetic node through:

`G0 -> Stage-0 -> G1 -> F2 -> G2 -> F3 -> G3 -> F4 Tier-1 -> G4 -> detector -> G5 -> G6 -> G7 -> G8`.

At each edge verify:

- gate identity;
- scoped prerequisites;
- material state transition;
- remaining protected roles;
- configuration revision;
- final disposition.

The nominal traversal is not sufficient by itself; injected failures are mandatory.

---

# 14. Round-47 repository dry-run result

The repository-only exercise performed in Round 47 found:

- one circular dependency when P16F/P16G were treated as monolithic completion nodes;
- one Stage-0 readiness ambiguity that could create a data-before-readiness deadlock.

Repairs:

- P16F phased readiness states;
- P16G consumes `P16F-DESIGN-DEFINITION-READY`;
- G0 uses scope-appropriate readiness, with the P16F skeleton sufficient for Stage-0.

After repair:

- directed prerequisite cycles = 0;
- 15 synthetic fault scenarios exercised;
- 15/15 reached the intended fail-safe disposition under the repaired rules.

These are logical test cases, not empirical reliability statistics.

---

# 15. Required P16I record

Every dry run shall record:

- graph revision;
- node/edge list;
- detected cycles;
- repair decisions;
- scenario IDs;
- injected fault;
- expected response;
- observed logical/system response;
- invariant violations;
- residual ambiguity;
- final logic-dry-run state;
- final lab-dry-run state.

---

# 16. Promotion rules

`P16I-LOGIC-DRY-RUN-PASSED = YES` requires:

- graph constructed;
- all detected cycles resolved or explicitly accepted with rigorous justification;
- mandatory fault classes exercised;
- no unresolved invariant violation;
- repairs reflected in controlled documents.

`P16I-LAB-DRY-RUN-PASSED = YES` additionally requires:

- actual lab data/traveler system instantiated;
- actual configuration/calibration objects exercised;
- actual holdout-access mechanism tested;
- actual reserve lock tested;
- actual audit/event logging tested;
- representative surrogate/dummy workflow traversed without HgCdTe where possible.

Round-47 state:

- `P16I-LOGIC-DRY-RUN-PASSED = YES`;
- `P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`.

---

# 17. Non-promotion warning

P16I logic pass does not imply:

- P16H physical implementation;
- P16F/P16G physical feasibility;
- equipment readiness;
- empirical process validation;
- first-build readiness;
- historical identity;
- P17 release.

It only establishes that the currently tested control logic is internally coherent under the declared synthetic cases.