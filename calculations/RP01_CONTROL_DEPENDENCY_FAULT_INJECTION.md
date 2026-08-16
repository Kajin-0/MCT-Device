# RP-01 control-system dependency graph and synthetic fault-injection dry run

**Status:** DERIVED INTERNAL CONTROL ANALYSIS / ROUND 47  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Objective

Test the P16A-P16H / G0-G8 control architecture without consuming HgCdTe and without inventing local measurements.

This module asks three questions:

1. does the control graph contain circular prerequisites or deadlocks?
2. do failures propagate only as far as justified rather than globally invalidating unrelated evidence?
3. do holdout, reserve, rework and material-release rules fail safe under synthetic fault injection?

No physical process is executed. All sample IDs, failures and responses in this file are synthetic tokens used only to test logic.

---

## 2. Definitions

A **dependency edge** `A -> B` means B cannot be validly completed until the stated output of A exists.

A **scope dependency** is narrower: only the subset of A required for the immediate operation must be ready.

A **material gate** evaluates both:

`T(v,e)` = technical/scientific eligibility of node `v` for operation `e`;

`M(v,e)` = post-commit material/genealogy feasibility.

Round-46 rule retained:

`GO(v,e) iff T(v,e)=PASS and M(v,e)=PASS`.

A **fault-injection pass** means the synthetic event causes the intended containment/decision without violating a permanent invariant.

---

## 3. Permanent invariants tested

### I1 — no irreversible release on one-dimensional approval

A technical PASS alone cannot produce GO if post-commit genealogy fails.

### I2 — holdout outcome cannot tune the model it tests

Validity-QC access is allowed only to identify predeclared execution invalidity. A scientifically unfavorable but valid result remains holdout evidence.

### I3 — holdouts are not reserve inventory

A process failure elsewhere does not release a locked holdout.

### I4 — state-changing rework changes scientific identity unless equivalence is explicitly demonstrated

A re-annealed, re-RIE-treated, re-passivated, re-metallized or package-reworked node cannot retain its old fit/holdout role by default.

### I5 — statistical independence follows the real experimental unit

Splitting a root or co-loading siblings does not create upstream independent replicates.

### I6 — configuration change invalidates only the affected equivalence claim, but it must invalidate that claim even when the calendar calibration date has not expired

### I7 — downstream subsystem absence must not deadlock an unrelated upstream experiment

Only capability required to execute the immediate irreversible edge and preserve the intended evidence is mandatory.

### I8 — synthetic/surrogate commissioning cannot satisfy HgCdTe-specific empirical evidence

### I9 — a prediction failure is not an execution-invalidity criterion

### I10 — no node with broken identity/genealogy may be guessed back into a protected statistical role

### I11 — STOP must preserve a terminal disposition and the failed/negative record

### I12 — no directed prerequisite cycle may remain in the controlled readiness graph

---

# 4. Pre-repair dependency graph

The Round-44/Round-45 text created the following logical relation:

`P16F campaign structure -> P16G genealogy/material plan`

because P16G needs the selected F2/F3/F4/F5 campaign structure, treatment-unit definitions, holdouts and structural counts.

But the P16F final disposition also required:

`P16G genealogy/material plan -> P16F final readiness`.

If P16F is represented as one monolithic node, this becomes:

`P16F -> P16G -> P16F`.

### Round-47 cycle finding

**One directed cycle was detected:**

`P16F <-> P16G`.

This is a design/control defect, not a scientific defect.

It would allow two bad implementations:

- declare P16F ready before genealogy is actually demonstrated; or
- require final P16F readiness before P16G may even be constructed, creating a deadlock.

---

# 5. P16F phase split — cycle repair

Round 47 splits P16F into three scoped states.

## 5.1 `P16F-CAMPAIGN-SKELETON-DEFINED`

Minimum state needed to authorize Stage-0 learning.

Requires:

- protected quantity/decision identified;
- experimental unit identified;
- response vector identified;
- candidate controllable factors/state descriptors identified;
- Stage-0 measurement/variance plan identified;
- provisional same-regime/safety feasibility bounds identified;
- no claim that final perturbations, sample size or genealogy have closed.

This state intentionally does **not** require Stage-0 variance because obtaining that variance is one purpose of Stage 0.

## 5.2 `P16F-DESIGN-DEFINITION-READY`

Post-Stage-0 state sufficient for P16G to perform structural genealogy/material allocation.

Requires:

- Stage-0 variance/repeatability inputs required by the active design;
- experimental unit frozen;
- model family/design objective frozen enough for structural planning;
- fitted-design structure and structural run count defined;
- perturbation-resolution window demonstrated or the design marked HOLD;
- blocking/hard-to-change structure defined;
- holdout type/number/independence requirement defined;
- stopping/invalidation logic defined.

It does not yet assert that the physical material plan is feasible.

## 5.3 `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`

Final P16F state.

Requires:

- `P16F-DESIGN-DEFINITION-READY = YES`;
- P16G genealogy/material feasibility PASS;
- relevant infrastructure/EH&S readiness;
- no unresolved design-resolution failure.

Thus the repaired chain is:

`P16F skeleton -> Stage-0 -> P16F design definition -> P16G -> P16F final readiness`.

The directed cycle is removed.

---

# 6. Stage-0 readiness cycle check

A second potential deadlock exists if G0 for Stage-0 requires final P16F readiness, because P16F design resolution itself needs Stage-0 variance.

Round 47 therefore freezes the scope rule:

### Stage-0 G0 may use

- relevant P16C/P16D capability/acceptance;
- **scope-adequate** P16E discrimination for the Stage-0 measurement;
- `P16F-CAMPAIGN-SKELETON-DEFINED`;
- a P16G **Stage-0 material-protection block**, not the final full-campaign material plan;
- data/genealogy controls;
- EH&S authorization.

### Formal F2/F3/F4/F5 release requires stronger states

Formal campaign release may require:

- `P16F-DESIGN-DEFINITION-READY` or final P16F readiness as appropriate;
- full P16G post-commit genealogy/material feasibility for the edge.

This is scoped readiness, not dilution of standards.

---

# 7. Repaired dependency spine

The principal design/control chain is now:

`P16B candidate branch`
`-> P16C relevant physical capability`
`-> P16D relevant IQ/OQ/surrogate acceptance`
`-> scope-adequate P16E discrimination`
`-> P16F campaign skeleton`
`-> G0 Stage-0 authorization`
`-> Stage-0 data`
`-> P16F design-definition readiness`
`-> P16G full genealogy/material feasibility`
`-> P16F final campaign readiness`
`-> G1 formal F2`
`-> G2 F3 release`
`-> G3 F4 release`
`-> G4 detector-bearing release`
`-> G5 matched detector characterization`
`-> G6 singulation`
`-> G7 package`
`-> G8 evidence promotion`.

P16H is the operating control system that records these gates. It can be instantiated before all campaigns are complete; individual GO decisions still require the scoped prerequisites for the relevant edge.

### Graph result

After the Round-47 P16F phase split and Stage-0 scope rule:

**directed-cycle count = 0**.

No time durations are known, so this is a dependency spine, not a numerical critical-path duration calculation.

---

# 8. Dependency propagation rule

A fault in node `q` invalidates only:

1. q itself;
2. descendants whose validity depends on the affected state/equivalence;
3. prior GO decisions that explicitly reused that affected state without a preserved independent baseline.

It does **not** automatically invalidate:

- unrelated upstream evidence;
- unrelated subsystems;
- independent holdouts from unaffected configurations;
- raw historical observations.

Call this the **minimum justified invalidation set**.

The invalidation set must be expanded only when evidence shows a common-cause relation.

---

# 9. Synthetic fault-injection matrix

## FI-01 — downstream package subsystem unavailable during F2 Stage-0

**Injected state:** package fixture/P33 subsystem not commissioned; LPE/P06/P05 Stage-0 chain is otherwise accepted.

**Expected:** Stage-0 G0 may proceed if the package subsystem is not needed to execute or preserve the Stage-0 evidence. G7 remains HOLD later.

**Reason:** relevant-subsystem rule.

**Result:** PASS.

---

## FI-02 — P16F/P16G circular prerequisite

**Injected state:** interpret both P16F and P16G as monolithic final readiness nodes.

**Expected pre-repair:** deadlock/cycle detected.

**Observed logical result:** one cycle `P16F <-> P16G`.

**Repair:** P16F skeleton/design/final split.

**Post-repair result:** PASS; zero directed cycles.

---

## FI-03 — P06 repeatability fails before formal F2

**Injected state:** Stage-0 FTIR repeatability is too poor to resolve the planned F2 perturbation.

**Expected:** G1 = HOLD. Do not execute the formal independent-growth DOE merely to compensate for inadequate metrology. Improve P06/metrology or redesign factor range.

**Material response:** formal roots remain protected.

**Result:** PASS.

---

## FI-04 — one formal LPE run has source/thermal excursion

**Injected state:** realized source/thermal trace violates the predeclared execution-validity criterion.

**Expected:** preserve the run as failed/deviation evidence; place same-excursion siblings/source cohort on HOLD as justified; invoke P18/source-history diagnosis. Do not silently delete and replace the row after viewing response.

**Result:** PASS.

---

## FI-05 — post-anneal sample is transition/multicarrier

**Injected state:** P05 shows transition/multicarrier behavior rather than the intended stable n-like regime.

**Expected:** retain as F3 boundary/classifier evidence; standard one-carrier detector path at G3 = HOLD/STOP unless the experiment explicitly studies that regime.

**Result:** PASS.

---

## FI-06 — RIE chamber excursion after Tier-1 witness treatment

**Injected state:** pressure/self-bias/sample-temperature state is outside the accepted execution envelope.

**Expected:** G4 detector-bearing release = HOLD. Freeze affected siblings, classify excursion, invoke P18, protect detector descendants/holdouts.

**Result:** PASS.

---

## FI-07 — technically good RIE state but insufficient remaining material

**Injected state:** Tier-1 witness data PASS technically, but committing the only eligible descendant would consume the sole detector bridge or independent holdout.

`T=PASS`, `M=FAIL`.

**Expected:** G4 = HOLD/STOP for that candidate. Do not override material feasibility because the process state looks promising.

**Result:** PASS.

---

## FI-08 — valid holdout disagrees with fitted model

**Injected state:** holdout execution passes all validity-QC criteria but response lies outside predeclared predictive acceptance.

**Expected:** holdout = failed prediction. G8 empirical promotion blocked or downgraded. Model may be revised, but revised model requires a new independent holdout before equivalent verification.

**Forbidden response:** relabel holdout a pilot or execution-invalid solely because prediction failed.

**Result:** PASS.

---

## FI-09 — holdout measurement has broken wire / instrument invalidity

**Injected state:** validity QC detects an execution-invalid measurement before scientific interpretation.

**Expected:** outcome excluded under the predeclared invalidity rule; replacement holdout chosen under the frozen replacement rule. Original protected response is not used to tune the model.

**Result:** PASS.

---

## FI-10 — MFC replaced after RIE commissioning

**Injected state:** CH4 or H2 MFC hardware is replaced; calibration certificate dates elsewhere remain current.

**Expected:** affected RIE gas-delivery equivalence/acceptance invalidated pending impact review/requalification. G3/G4 releases depending on that gas realization = HOLD. Unrelated FTIR/Hall/package evidence is not globally invalidated.

**Result:** PASS.

---

## FI-11 — process failure tempts use of locked holdout as spare

**Injected state:** an F4 fit-point sample is lost; a physically suitable F4 holdout remains.

**Expected:** holdout remains locked. Use process reserve if available, redesign campaign, or document inability to continue. The failure itself does not trigger holdout release.

**Result:** PASS.

---

## FI-12 — holdout receives state-changing rework

**Injected state:** designated holdout is accidentally re-annealed or repeat-RIE-treated.

**Expected:** original holdout identity invalidated. Node may be reassigned as a new treatment/engineering point, but cannot remain the original holdout.

**Result:** PASS.

---

## FI-13 — sample identity/genealogy link lost

**Injected state:** physical node label and electronic genealogy cannot be reconciled uniquely.

**Expected:** protected forward path = STOP/HOLD; siblings with possible mix-up are quarantined. Identity is not reconstructed from expected performance.

**Result:** PASS.

---

## FI-14 — detector test station fails after detector fabrication

**Injected state:** completed detector exists, but P12/P13 transfer calibration becomes invalid.

**Expected:** G5 = HOLD. Preserve detector; do not advance to singulation/package merely to keep schedule. Requalify measurement chain first.

**Result:** PASS.

---

## FI-15 — package holdout fails while upstream detector response remains valid

**Injected state:** package build/thermal response fails holdout prediction, but pre-package P10-P13 data remain valid and traceable.

**Expected:** F5/package model promotion blocked. Do not automatically invalidate upstream LPE/RIE detector measurements unless diagnostic evidence identifies a common upstream cause.

**Result:** PASS.

---

# 10. Synthetic dry-run summary

### Pre-repair

- fault scenarios exercised: 15;
- architectural prerequisite cycles detected: 1;
- cycle: `P16F <-> P16G`;
- Stage-0 readiness ambiguity detected: 1.

### Repairs

1. split P16F into skeleton / design-definition / final readiness;
2. require P16G to consume `P16F-DESIGN-DEFINITION-READY`, not final P16F readiness;
3. freeze scoped G0 rule so Stage-0 does not require the data-dependent final P16F state.

### Post-repair

- directed prerequisite cycles: 0;
- synthetic fault scenarios with fail-safe disposition: 15/15;
- cases that intentionally terminate a sample path rather than preserve GO: allowed and counted as correct behavior;
- physical-laboratory dry run: not performed.

These counts validate the internal logic exercised here; they are not empirical reliability statistics.

---

# 11. New dry-run evidence states

Use:

- `LOGIC-DRY-RUN-NOT-EXECUTED`
- `LOGIC-FAULT-DETECTED`
- `LOGIC-REPAIR-REQUIRED`
- `LOGIC-REPAIRED`
- `LOGIC-DRY-RUN-PASS`
- `LAB-DRY-RUN-OPEN`
- `LAB-DRY-RUN-PASS`

Round-47 repository state:

`P16I-LOGIC-DRY-RUN-PASSED = YES`.

`P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`.

---

# 12. What this does not prove

The synthetic dry run does not prove:

- real hardware interlocks work;
- real calibration invalidation is correctly automated;
- operators will follow the gate sequence;
- file permissions prevent premature holdout access;
- barcode/sample tracking prevents identity loss;
- a real laboratory has enough material;
- any empirical Jacobian is measured;
- P16A/P16C/P16D/P16E/P16F/P16G/P16H physical readiness;
- RP-01 historical reproduction;
- P17 reproducible release.

Those require physical implementation and audit.

---

# 13. Next logical closure after Round 47

The strongest next systems task is to define the actual **data model / digital traveler schema** that can enforce these invariants in a laboratory information system:

- immutable material-node IDs;
- parent/child genealogy;
- configuration/calibration hashes;
- gate-event objects;
- holdout-access permissions;
- reserve locks;
- deviation/rework state transitions;
- raw-data references;
- model-freeze IDs;
- audit history.

That would convert the current human-readable control architecture into a machine-checkable provenance system without requiring HgCdTe processing.