# Research checkpoint — after sequential campaign execution / material-release Round 46

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 46 began from the Round-45 conclusion that sample genealogy and structural material accounting were defined, but no controlled logic yet determined when a particular physical node should actually be consumed by the next irreversible step.

Objective:

> Build an explicit sequential campaign-execution/material-release system that prevents scarce HgCdTe from advancing before upstream evidence, downstream capacity and protected material reserves justify the commitment.

No physical material was processed. No local result, yield, sample quantity or process tolerance was invented.

---

# 2. New controlled artifacts

Created:

- `calculations/RP01_SEQUENTIAL_MATERIAL_RELEASE_DECISION_CONTROL.md`;
- `procedures/P22C_FIRST_BUILD_CAMPAIGN_EXECUTION_MATERIAL_RELEASE_CONTROL.md`;
- `travelers/P16H_SEQUENTIAL_MATERIAL_RELEASE_CONTROL_REGISTER.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND46.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND46.md`;
- this checkpoint.

AGENTS is refreshed at the end of the round.

---

# 3. New integration layer — P16H

P16A-P16H now separate eight questions:

1. **P16A:** can one complete first build execute without undocumented irreversible choices?
2. **P16B:** which evidence-ranked candidate branch should be pursued?
3. **P16C:** does an actual laboratory have the physical capability?
4. **P16D:** has that infrastructure passed IQ/OQ/surrogate commissioning?
5. **P16E:** are uncertainty and requirements adequately allocated?
6. **P16F:** are the empirical campaigns identifiable, resolution-justified and holdout-defined?
7. **P16G:** is the physical sample genealogy/material allocation feasible?
8. **P16H:** is there an instantiated sequential release-control system governing actual irreversible material commitments?

New state:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY`.

Current:

`NO / NOT PHYSICALLY INSTANTIATED`.

A future P16H YES does not mean an individual sample is GO.

---

# 4. Major result 1 — release requires two independent passes

For physical node `v` and irreversible operation `e`:

- `T(v,e)` = technical/scientific eligibility;
- `M(v,e)` = post-commit genealogy/material feasibility.

Round 46 freezes:

`GO only if T=PASS and M=PASS`.

This means a technically excellent sample can remain HOLD if consuming it would destroy the remaining material plan.

This distinction is important because Round 45 showed that raw area, independent roots, descendants, holdouts and package-ready dies are not interchangeable resources.

---

# 5. Major result 2 — four gate outcomes

Every irreversible gate now ends in exactly:

- `GO` — advance;
- `HOLD` — preserve current state pending evidence/availability;
- `REWORK` — use a qualified recovery route and reassess sample role;
- `STOP` — terminate the protected forward path and assign archive/FA/engineering disposition.

`HOLD` is explicitly not failure.

`REWORK` cannot be improvised. A state-changing rework can invalidate the sample's original fit/holdout identity.

---

# 6. Major result 3 — holdouts are locked material, not spare inventory

A holdout must retain:

- unique ID;
- independent-unit basis;
- frozen process state;
- protected response vector;
- model/version to be challenged;
- model-freeze ID;
- validity-QC rule;
- replacement rule for execution-invalid observations.

Round 46 separates:

- **validity QC access** — enough to detect instrument/sample execution invalidity;
- **scientific outcome access** — the response used to challenge the model.

The first may occur before model opening when necessary. The second cannot tune the fitted model.

A prediction failure is evidence and is not itself an execution-invalidity criterion.

---

# 7. Major result 4 — reserve release has a state machine

Round 45 defined separate reserve classes.

Round 46 now controls when they unlock.

A reserve becomes available only when:

- its protected purpose is closed; or
- an equivalent controlled substitute is allocated; or
- a redesigned campaign explicitly retires the old purpose.

A failure elsewhere does not automatically unlock a holdout or FA reserve.

No arbitrary reserve percentage was introduced.

---

# 8. Major result 5 — chronological G0-G8 release ladder

Round 46 defines:

### G0 — active-campaign authorization

Relevant P16C/P16D/P16E/P16F/P16G + EH&S/data system must be adequate for the immediate irreversible edge.

### G1 — Stage-0 LPE -> formal F2 DOE

Stage-0 variance, P06 repeatability, information-resolution, same-regime factor bounds, exact design, run order, holdouts and root plan must be frozen.

### G2 — selected F2 root -> F3 anneal

Accepted P06 state, controlled selection basis, P05 branch, anneal role and post-commit material feasibility required.

### G3 — annealed material -> F4 RIE/passivation

Valid anneal, P05 carrier state, P06 preservation where required, correct model regime, chamber readiness and descendant allocation required.

### G4 — RIE/material witness -> full detector-bearing fabrication

This is a major scarcity gate. Material-state witnesses, stability, detector information need and post-commit feasibility are required before spending a full detector descendant.

### G5 — completed detector -> matched P10/P11/P12/P13/F1

Geometry/contact identity, instrument-chain readiness and heating/loading guard required.

### G6 — characterized detector -> singulation

Pre-cut baseline, P35 method/street/edge-exclusion and package compatibility required.

### G7 — singulated die -> actual package build

Post-cut state, package surrogate screen, prospective package role, paired baseline and die reserve required.

### G8 — result -> evidence promotion / P16E update / P17 handoff

Model diagnostics, holdout, uncertainty, valid range, detector bridge and deviations must close before evidence promotion.

---

# 9. Relevant-subsystem rule at G0

Round 46 deliberately avoids requiring every late-stage subsystem to exist before any upstream qualification can ever begin.

Instead:

> every subsystem needed to execute the proposed irreversible edge and preserve the intended evidence must be ready.

This prevents two bad extremes:

- using valuable HgCdTe to commission an unqualified tool;
- unnecessarily blocking a self-contained upstream experiment because an unrelated package subsystem is not yet built.

Global maturity states remain separate.

---

# 10. Major result 6 — F4 is explicitly two-tier

The controlled RIE/passivation sequence becomes:

`Tier 1 witness/material-state learning`
`-> G4`
`-> Tier 2 selected detector-bearing confirmation`.

Tier-1 states target:

- oxide clear/recession;
- realized plasma state;
- converted sheet state;
- conversion depth/lateral state;
- contact/TLM state where needed;
- stability.

Full detector descendants are preferentially reserved for:

- center/baseline;
- high-information contrasts;
- required interactions;
- holdouts;
- detector bridges.

This operationalizes the Round-45 rule not to fabricate full detectors at every exploratory RIE state.

---

# 11. Major result 7 — next-action decision uses decision variance plus burden vector

For candidate action `a`:

`DeltaV_a = V_current - E[V_after | a]`.

Burden is retained as a vector:

`{roots/pieces/area, irreversible descendants, detector/package dies, optionality loss, confounding risk, time/dependency}`.

Round 46 freezes a dominance rule:

Do not choose an action when another feasible action provides at least as much expected protected decision-variance reduction with no greater protected burden/confounding and is strictly better in at least one dimension.

A scalar `DeltaV/cost` may be used later only if a defensible common cost model exists.

No fictitious exchange rate between one LPE growth, one RIE run and one package die was created.

---

# 12. Run-order / blocking control

Every campaign must classify factors as:

- easy-to-change/randomizable;
- hard-to-change/split-plot;
- sequential/source-history;
- block/covariate.

Randomize within feasible blocks where possible.

Physical constraints do not justify ignoring order effects.

Important possible aliases include:

- LPE source-use/depletion;
- ampoule/reservoir state;
- RIE clean/season/chamber age;
- calendar/operator;
- package batch/cure fixture.

If randomization is impossible, counterbalance/model the order effect and record the identifiability loss.

---

# 13. Failure/deviation routing

Unexpected failure now triggers:

1. HOLD/freeze affected siblings;
2. event classification;
3. P18 diagnostics;
4. preferential use of designated FA material rather than holdouts;
5. determination whether the observation is execution-invalid or a true process response;
6. controlled REWORK/STOP/replacement/resume decision.

A true treatment failure remains data.

More samples do not repair a structurally invalid or confounded design.

---

# 14. Configuration-change rule

Every GO references exact revisions for:

- procedure;
- apparatus;
- calibration;
- measurement method;
- DOE/model;
- P16G material plan.

A decision-affecting configuration change triggers impact review even when the calendar calibration has not expired.

Prior GO does not transfer automatically to the changed system.

---

# 15. Current project maturity

Unchanged:

`TRACEABLE-FIRST-BUILD-READY = NO`

`HISTORICAL-RP01-REPRODUCED = NO`

`REPRODUCIBLE-RELEASE = NO`

`P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`

`P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`

`P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO / NOT PHYSICALLY INSTANTIATED`

`P16G-MATERIAL-GENEALOGY-PLAN-READY = NO / NOT PHYSICALLY INSTANTIATED`

New:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY = NO / NOT PHYSICALLY INSTANTIATED`.

Strategic state:

**branch-selected + capability-specified + acceptance-specified + uncertainty architecture defined + empirical campaigns designed + sample genealogy designed + sequential material-release control designed + not physically instantiated**.

---

# 16. What remains physically open

Still open:

- all actual equipment/tool identities;
- all local acceptance evidence;
- Stage-0 variance;
- root inventory and usable geometry;
- physical holdouts/reserve;
- empirical Jacobians;
- actual gate records;
- actual run order;
- actual failures/rework routes;
- detector/package descendants;
- P17 capability/yield.

---

# 17. Strongest next analytical work — Round 47

The new control architecture is now complicated enough that the next risk is internal inconsistency rather than another missing standalone SOP.

Round 47 should build a **zero-HgCdTe dependency/critical-path and tabletop dry-run audit**.

Objectives:

1. convert P16A-P16H and G0-G8 into one dependency graph;
2. identify any circular prerequisites/deadlocks;
3. determine the minimum relevant-subsystem commissioning sequence before each material tier;
4. execute a synthetic genealogy through PASS/HOLD/FAIL examples without pretending they are physical data;
5. fault-inject configuration changes, holdout failure, RIE excursion and material shortage to test whether the controls preserve scientific validity;
6. derive the shortest controlled path from an empty laboratory to the first scientifically interpretable HgCdTe experiment;
7. distinguish mandatory critical-path work from late-stage tasks that can be deferred.

This would be a systems-engineering verification of the manual itself, not a fabricated laboratory result.