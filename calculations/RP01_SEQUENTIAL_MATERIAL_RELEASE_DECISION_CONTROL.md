# RP-01 sequential material-release / campaign-decision control

**Status:** DERIVED CONTROL FRAMEWORK / ROUND 46  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16E/P16F/P16G, P20/P20A, P21/P22/P22A/P22B, P23/P24/P25, P33/P35, P18 and P17.

## 1. Purpose

Round 44 defined information-efficient empirical campaigns. Round 45 defined the sample-genealogy/material-allocation DAG. This calculation closes the next logical gap:

> Given an actual material node in that DAG, when is it rational and controlled to spend that node on the next irreversible process step?

The output is a sequential release logic, not a physical result.

No local data exist. No sample is released by this document. No historical RP-01 tolerance is inferred.

---

# 2. Release decisions are not equivalent to process acceptance

For a material node `v`, define two logically separate predicates:

`T(v,e)` = technical/scientific eligibility of node `v` for irreversible edge/process `e`.

`M(v,e)` = post-commit material/genealogy feasibility if `v` is consumed by `e`.

The minimum release condition is

`GO(v,e) only if T(v,e)=PASS and M(v,e)=PASS`.

A sample can therefore be technically excellent and still remain `HOLD` if consuming it would destroy:

- an independent holdout;
- the sole remaining detector bridge;
- the sole destructive-failure-analysis witness;
- the physical-area balance for another protected campaign;
- treatment/root balance needed to avoid confounding.

Conversely, excess material does not permit a scientifically ineligible state to advance.

---

# 3. Controlled decision outcomes

Every irreversible release gate ends in exactly one of four execution outcomes.

## 3.1 GO

Advance the identified node through the identified irreversible edge.

Requires:

- technical eligibility PASS;
- post-commit genealogy/material feasibility PASS;
- configuration frozen;
- required signatures complete;
- no unresolved deviation that can change the protected decision.

## 3.2 HOLD

Do not advance the node.

Use when:

- evidence is incomplete;
- a needed calibration/measurement is pending;
- downstream capacity is not yet available;
- material allocation would become infeasible;
- a model/holdout has not yet been frozen;
- a deviation is under investigation.

`HOLD != FAIL`.

The material should remain in the most reversible/stable qualified state available.

## 3.3 REWORK

Apply a specific qualified recovery route and then repeat the appropriate gate.

`REWORK` is allowed only when:

- the route itself is documented and qualified for the current material state;
- the rework does not erase the scientific meaning of the sample role;
- genealogy records the pre/post state;
- holdout status is reconsidered explicitly.

An improvised cleanup, re-anneal, re-passivation or re-metallization is not a controlled `REWORK`.

## 3.4 STOP

Do not advance the node on its protected development path.

Possible terminal dispositions include:

- archive;
- controlled destructive failure analysis;
- method-development witness;
- non-protected engineering experiment;
- disposal under facility controls.

`STOP` does not imply the node is useless. It means the node is no longer eligible for the protected release path.

---

# 4. Material release is a state transition on a genealogy DAG

Represent the physical program as a directed acyclic graph.

A node contains at minimum:

`v = {physical ID, root ID, process state, geometry/usable region, evidence state, protected role, reserve class}`.

An irreversible edge contains:

`e = {process/treatment, configuration revision, burden/consumption, required measurements, allowed downstream roles}`.

A release creates a descendant state:

`v --e--> v'`.

The edge is not permitted merely because the procedure exists.

The edge requires a release record tied to the exact physical node and exact configuration revision.

---

# 5. Post-commit material-feasibility condition

Round 45 separates independent-unit count, piece count, area and reserve. Round 46 applies that separation to every proposed release.

Let the current available material/resource vector be

`r = [independent roots, usable polygons/areas, treatment slots, detector descendants, package-ready dies, protected holdouts, archive/FA pieces, ...]`.

Let the proposed irreversible action consume or lock

`c_e`.

Then

`r_after = r - c_e`.

Let `F_future` denote the set of still-protected future obligations under the frozen P16F/P16G plan.

The release is material-feasible only if at least one valid descendant allocation still exists after commitment:

`exists allocation X_after satisfying all F_future constraints`.

For a simple scalar-area subproblem this reduces to

`A_remaining_after >= A_required_protected_future`.

But the real problem is usually multi-constraint because orientation, root independence, chamber/ampoule blocking, holdout identity and package genealogy are not interchangeable with raw area.

### Permanent rule

`unused physical area != available protected material`.

A leftover polygon can be unusable if it has the wrong root, orientation, history or role.

---

# 6. Protected-role locking

Every planned descendant receives one of these material-role states:

- `UNCOMMITTED`;
- `ACTIVE-FIT`;
- `ACTIVE-BRIDGE`;
- `HOLDOUT-LOCKED`;
- `ARCHIVE-LOCKED`;
- `FA-LOCKED`;
- `CONTINGENCY-LOCKED`;
- `RELEASED-FROM-RESERVE`;
- `TERMINAL`.

A role lock is not removed because another sample failed.

It is removed only by a documented decision that the protected purpose is closed, superseded or redesigned.

---

# 7. Holdout quarantine

A scientific holdout is not spare material and its outcome is not ordinary exploratory data.

For each holdout define before result inspection:

- holdout ID;
- independent-unit basis;
- exact process/configuration state;
- response vector to be evaluated;
- model/version to be challenged;
- pass/fail or predictive scoring rule;
- analyst/reviewer;
- model-freeze identifier/hash or immutable revision.

### 7.1 Validity QC versus outcome leakage

Holdout measurements may be inspected for validity checks required to determine whether the measurement itself is usable, for example:

- instrument fault;
- missing file;
- sample misidentification;
- temperature excursion;
- broken wire/interconnect;
- invalid optical alignment.

Those checks may not be used to tune the fitted process model.

The protected scientific response remains quarantined until the model is frozen.

### 7.2 Failed holdout

A failed holdout is evidence.

Do not discard it as an outlier or reclassify it as a pilot merely because the prediction failed.

If a documented execution fault invalidates the observation, retain the invalid record and create a replacement holdout according to the frozen replacement rule.

---

# 8. Dynamic reserve release

Reserve is released by closure of the decision it protects, not by elapsed time.

For each reserve class `R_k` define:

`R_k = {protected purpose, quantity/geometry, release trigger, prohibited uses before trigger}`.

Examples:

- holdout reserve releases only after model validation/decision closure;
- FA reserve releases only after the corresponding process-risk period is closed or an alternative FA node exists;
- package reserve releases only after package-build need is closed;
- statistical-power reserve cannot be converted to convenience samples before the power/variance decision is made.

### 8.1 Probability-based reserve when yield exists

If an empirically supported independent success probability `p` later exists and at least `k` successes are required, choose total attempts `n` from

`P[X >= k] >= C`,

with

`X ~ Binomial(n,p)`

only when the binomial independence model is defensible.

Correlated failures by growth, chamber, source lot or package batch require a genealogy-aware model instead.

No reserve percentage is released in Round 46.

---

# 9. Stage-to-stage execution gates

Round 46 defines the following chronological gate classes.

## G0 — authorization to consume any HgCdTe in an active campaign

Required locally:

- relevant P16C physical capability identified;
- relevant P16D IQ/OQ/surrogate acceptance passed;
- relevant P16E uncertainty allocation sufficient for the immediate decision;
- active P16F campaign block resolution/identifiability passed;
- active P16G genealogy/material block feasible;
- current EH&S/facility authorization;
- configuration and data system revision frozen.

Global P16C/P16D/P16E/P16F/P16G need not all be complete for every future subsystem before one upstream experiment is scientifically possible; however every subsystem needed for the proposed irreversible edge and for preserving its intended evidence must be ready.

This avoids both extremes:

- fabricating material into a measurement vacuum;
- demanding unrelated late-stage infrastructure before an early safe qualification can begin.

## G1 — Stage-0/pilot LPE -> formal F2 root campaign

Require:

- local LPE capability/thermal/charge branch instantiated enough for controlled perturbation;
- P06 measurement repeatability established;
- Stage-0 independent-growth variance estimate available for the protected response;
- candidate perturbation range satisfies information-resolution and same-regime bounds;
- exact F2 design matrix frozen;
- root/holdout assignments frozen;
- Stage-0 reuse status declared prospectively;
- physical root inventory/material balance feasible.

If variance is too large for any feasible perturbation:

`HOLD` and improve process/metrology rather than consume the formal root set blindly.

## G2 — F2 grown root -> F3 anneal branch

Require for each selected root/descendant:

- accepted P06 map / material state;
- morphology/usable region adequate for the planned role;
- growth genealogy complete;
- root selection follows the frozen/adaptive rule rather than post-hoc cherry picking;
- dedicated P05 branch or qualified reuse branch reserved;
- anneal treatment role assigned;
- post-commit material plan leaves F2 holdouts/bridges/reserves intact.

Not every F2 root must advance to F3.

## G3 — annealed descendant -> F4 RIE/passivation qualification

Require:

- exact anneal trajectory valid;
- P05 carrier-state classification available under the declared model;
- P06 optical-preservation comparison available where required;
- sample is in the intended stable n-like region for a continuous detector-process Jacobian, or explicitly assigned to a boundary/failure role;
- transition/multicarrier specimen is not silently relabeled as a standard one-carrier detector input;
- F4 witness/detector/holdout allocation remains feasible;
- RIE chamber relevant P16D acceptance current.

A useful anneal-boundary sample may be `STOP` for the standard detector path but retained as valuable F3 evidence.

## G4 — RIE/material-state qualification -> full detector-bearing fabrication

This is a major scarcity gate.

Require:

- realized chamber state recorded, including flow, pressure, RF, self-bias/sheath proxy, thermal state and chamber genealogy;
- oxide-clear/semiconductor-exposure state measured or bounded sufficiently for the design decision;
- material-state witnesses show the intended conversion/physical-state behavior;
- no unresolved stability problem over the required RIE-to-metal/process interval;
- the candidate RIE state is selected by the frozen information/decision criterion;
- detector fabrication adds material information not already dominated by a cheaper witness-only state;
- full detector descendant, matched controls and holdout remain physically feasible.

### Permanent staging rule

`witness-qualified state -> selected detector-bearing state`.

Do not fabricate complete detectors on every exploratory chamber state by default.

## G5 — completed detector -> P10/P11/P12/P13/F1 matched characterization

Require:

- final geometry/contact pair identified and measured;
- detector survives basic continuity/I-V checks;
- measurement chain relevant P16D/P16E acceptance current;
- test sequence/loading/heating reversibility controls defined;
- matched-state plan preserved.

The preferred chain remains

`P10 -> P11 -> P12 -> P13 -> F1/verification`

where the state remains reversible.

Failure of one instrument does not justify substituting unmatched devices for D* or lifetime without an explicit correction model.

## G6 — characterized bare detector -> singulation

Require:

- pre-singulation baseline complete for the protected metrics;
- P35 method/support/protection/clean branch locally qualified sufficiently for the selected device stack;
- cut street and functional edge exclusion frozen;
- die identity mapped to the parent detector/root;
- package candidate still needs this die;
- consuming the die does not destroy the sole remaining un-singulated comparator unless that is intentional.

## G7 — singulated detector die -> actual HgCdTe package build

Require:

- die passes post-singulation edge/electrical/noise checks required by P35;
- non-HgCdTe package surrogate screen complete for the selected family;
- P33 package construction branch frozen sufficiently for this test;
- pre-package P10/P12/P13 baseline exists on the same die where required;
- package-build role is fit/holdout/confirmation and was assigned before post-package outcome;
- protected unconsumed die reserve remains feasible.

Absent qualified reversible rework, `GO` at G7 commits one detector die to one package build.

## G8 — empirical result -> evidence promotion / P17 handoff

A completed campaign does not automatically promote an empirical derivative or release a process.

Require:

- model frozen;
- fit diagnostics/rank/conditioning passed;
- holdout result evaluated;
- uncertainty small enough for the protected P16E decision;
- detector bridge completed where required;
- failure/deviation records resolved;
- local valid range stated;
- result entered into P20/P16E with evidence class.

Only then may a derivative progress toward `ALLOCATION-ELIGIBLE`.

P17 remains a separate frozen-route capability/yield problem.

---

# 10. Run-order / blocking control

Randomization must respect physics and safety, but physical constraints do not permit undocumented ordering.

For every campaign classify factors as:

- easy-to-change/randomizable;
- hard-to-change/split-plot;
- sequential/source-history;
- block/covariate only.

Examples:

- LPE source-use/depletion may be sequential and cannot be naively randomized;
- anneal ampoule/reservoir state may create hard-to-change blocks;
- RIE clean/season/chamber history may constrain run order;
- package batch/cure fixture may block builds.

### Required rule

Randomize within feasible blocks where possible and model the hard-to-change hierarchy explicitly.

Do not let treatment order become perfectly aliased with:

- root growth;
- wafer position;
- source-use;
- chamber age;
- calendar time;
- operator;
- package batch.

If randomization is impossible, create deliberate counterbalancing or include the ordering variable in the model and document the loss of identifiability.

---

# 11. Next-action decision: upstream information versus downstream consumption

At many points there will be a choice between:

A. run another upstream information-rich experiment; or

B. consume an existing descendant in a more expensive downstream build.

Round 46 does not force these into one arbitrary scalar cost.

For candidate action `a`, define expected protected decision-variance reduction

`DeltaV_a = V_current - E[V_after | a]`.

Also record a burden vector

`b_a = {HgCdTe roots/pieces/area, irreversible descendants, instrument time, package dies, confounding risk, schedule dependence}`.

### Dominance rule

Action `a` is dominated by action `b` if:

- `DeltaV_b >= DeltaV_a`;
- every protected material burden of `b` is no worse than `a`;
- feasibility/confounding of `b` is no worse;
- at least one comparison is strictly better.

Do not choose a dominated action.

If a calibrated common burden/utility model later exists, an efficiency such as

`eta_a = DeltaV_a / C_a`

may be used.

Without such a model, retain the Pareto decision rather than inventing a currency conversion between one LPE root, one chamber treatment and one package die.

---

# 12. Sequential stopping

A campaign stage should stop consuming material when any of the following becomes true:

1. protected decision uncertainty is already below its allocated requirement;
2. additional candidate states are expected to produce negligible decision-variance reduction;
3. model discrepancy/holdout failure shows the current design family is invalid and redesign is required;
4. feasible perturbations cannot resolve the target effect;
5. process state leaves the intended physical regime;
6. remaining material is needed to preserve protected holdouts/bridges/reserve;
7. infrastructure/calibration/configuration validity is lost.

More samples are not a remedy for a structurally invalid model or invalid measurement chain.

---

# 13. Failure/deviation routing

When an unexpected failure occurs:

1. place the affected node and directly dependent descendants in `HOLD`;
2. freeze remaining protected siblings before consuming them;
3. classify whether the event is measurement fault, handling fault, process excursion, true treatment response or unknown;
4. use P18 diagnostic routing;
5. prefer designated FA/reserve material over holdouts;
6. determine whether the current design/model remains valid;
7. decide `REWORK`, `STOP`, replacement independent unit, or resumed `GO` through documented review.

### Anti-bias rule

A process failure is not automatically an invalid observation.

If the process was executed as intended and the material failed, that result is part of the treatment response and must remain in the dataset under the frozen analysis rule.

---

# 14. Configuration invalidation

Every `GO` references exact revisions for:

- process procedure;
- apparatus configuration;
- calibration set;
- measurement method;
- DOE/model;
- genealogy/material plan.

A configuration change after release requires impact review.

Examples that can invalidate a gate even before a calibration's calendar expiration:

- RIE electrode/holder change;
- MFC replacement;
- LPE boat geometry change;
- FTIR aperture/model change;
- Hall contact process change;
- package adhesive/cure change;
- preamp/analyzer transfer change.

Do not carry forward a prior `GO` automatically across a material change in configuration.

---

# 15. Gate precedence

A downstream gate may never repair a failed upstream release basis retrospectively.

Examples:

- good detector D* does not retroactively validate an undocumented RIE state;
- good package survival does not retroactively validate unknown singulation damage;
- a clean holdout fit does not make pseudoreplicated training data independent;
- later large sample size does not repair a confounded treatment/root design.

The evidence chain must remain reconstructable forward from the physical root.

---

# 16. New Round-46 control labels

Use the following labels where applicable:

- `GATE-EVIDENCE-OPEN`;
- `TECHNICAL-ELIGIBILITY-PASS`;
- `POST-COMMIT-FEASIBILITY-PASS`;
- `MATERIAL-RELEASE-GO`;
- `MATERIAL-RELEASE-HOLD`;
- `MATERIAL-RELEASE-REWORK`;
- `MATERIAL-RELEASE-STOP`;
- `HOLDOUT-LOCKED`;
- `HOLDOUT-MODEL-FROZEN`;
- `RESERVE-LOCKED`;
- `RESERVE-RELEASED`;
- `CONFIGURATION-IMPACT-REVIEW-REQUIRED`;
- `EXECUTION-DEVIATION-OPEN`.

These are execution-control states, not historical evidence classes.

---

# 17. What this calculation does not establish

It does not establish:

- any physical `GO` decision;
- any actual material quantity;
- any local yield;
- any acceptable failure probability;
- any final sample size;
- any empirical Jacobian;
- any process acceptance band;
- historical RP-01 execution details.

It establishes the logic by which those future decisions must be made.

---

# 18. Round-46 integration state

The corresponding integration register is P16H:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY`.

Current repository state:

`NO / NOT PHYSICALLY INSTANTIATED`.

A future `YES` means the laboratory has instantiated a controlled gate/release system for the active campaign.

It does not imply:

- P16A first-build readiness;
- empirical verification;
- historical reproduction;
- P17 capability/yield release.