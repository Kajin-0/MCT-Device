# Source ledger addendum — Round 46 sequential campaign execution / material release

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`  
**Round classification:** `DERIVED-INTERNAL-CONTROL`

## 1. Scope

Round 46 does not introduce a new historical HgCdTe source family and does not claim new RP-01 documentary closure.

It derives a controlled campaign-execution/material-release architecture from already controlled modules covering:

- infrastructure and subsystem acceptance;
- uncertainty allocation;
- information-optimal DOE;
- sample genealogy/material allocation;
- LPE, anneal, RIE/passivation, detector characterization, singulation and packaging;
- failure analysis and statistical release.

No physical sample was released. No local yield, sample count, process result or power calculation was invented.

---

# 2. New controlled artifacts

Round 46 adds:

- `calculations/RP01_SEQUENTIAL_MATERIAL_RELEASE_DECISION_CONTROL.md`;
- `procedures/P22C_FIRST_BUILD_CAMPAIGN_EXECUTION_MATERIAL_RELEASE_CONTROL.md`;
- `travelers/P16H_SEQUENTIAL_MATERIAL_RELEASE_CONTROL_REGISTER.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND46.md`;
- this source-ledger addendum;
- `research/2026-08-16_checkpoint_after_sequential_material_release_round46.md`.

AGENTS is refreshed separately.

---

# 3. Evidence basis — two-predicate release rule

## Controlled internal sources

- P16E uncertainty-allocation register;
- P16F empirical-Jacobian campaign register;
- P16G sample-genealogy/material register;
- Round-43 uncertainty calculation;
- Round-44 information-design calculation;
- Round-45 sample-genealogy/material calculation.

## Round-46 derived rule

For physical node `v` and irreversible operation `e`, release requires both:

- technical/scientific eligibility `T(v,e)=PASS`;
- post-commit material/genealogy feasibility `M(v,e)=PASS`.

`GO` requires both.

### Evidence class

`DERIVED-INTERNAL / EXECUTION-CONTROL`.

### Restriction

This does not create a process acceptance band or historical RP-01 criterion.

---

# 4. Evidence basis — GO/HOLD/REWORK/STOP

## Controlled internal sources

- P18 failure-analysis routing;
- P16A readiness distinction between controlled method and physically closed row;
- P16F stopping rules;
- P16G protected holdout/archive/FA roles.

## Round-46 derived control states

Every irreversible gate uses exactly:

- `GO` — advance;
- `HOLD` — preserve state pending evidence/capability/material feasibility;
- `REWORK` — only through a qualified recovery route with role reassignment review;
- `STOP` — remove node from the protected forward path and assign terminal/archive/FA use.

### Evidence class

`DERIVED-INTERNAL / STATE-MACHINE-CONTROL`.

No state is a historical evidence class.

---

# 5. Holdout locking and outcome quarantine

## Controlled internal basis

P21/P22/P22A/P22B and P16F require independent holdouts and frozen model logic. P16G protects holdout material from reassignment.

## Round-46 derived rule

A holdout is not spare material.

Before protected scientific response inspection, retain:

- holdout identity;
- independent-unit basis;
- frozen process state;
- response vector;
- model/version being challenged;
- model-freeze ID/revision;
- validity-QC rule;
- replacement rule for execution-invalid observations.

Instrument-validity QC may be inspected without permitting the scientific outcome to tune the fitted model.

A failed prediction remains holdout evidence unless a predeclared execution-invalidity criterion is satisfied.

### Evidence class

`DERIVED-INTERNAL / ANTI-LEAKAGE-CONTROL`.

---

# 6. Dynamic reserve release

## Controlled internal basis

Round 45 separates:

- process reserve;
- metrology reserve;
- layout reserve;
- holdout reserve;
- destructive-FA reserve;
- statistical-power reserve.

## Round-46 derived rule

Reserve is released when its protected decision/role is closed or replaced by an equivalent controlled allocation—not merely because another sample failed or because the reserve has been unused for some time.

If an empirical success probability later exists, a probability-based reserve may be sized from the appropriate success-count distribution. Correlated genealogy requires a model more appropriate than iid binomial sampling.

### Evidence class

`DERIVED-INTERNAL / RESERVE-CONTROL`.

No reserve percentage is introduced.

---

# 7. G0 active-campaign authorization

## Controlled basis

- P16C minimum laboratory capability;
- P16D IQ/OQ/surrogate acceptance;
- P16E uncertainty allocation;
- P16F campaign design;
- P16G genealogy/material feasibility;
- P36/P36A acceptance methods.

## Round-46 interpretation

A future early-stage campaign does not necessarily require every late-stage subsystem in the entire program to be complete, but every subsystem required for the proposed irreversible edge and for preserving the intended evidence must be physically ready.

This prevents:

- using HgCdTe as a commissioning standard for an unqualified measurement chain;
- blocking a scientifically self-contained upstream experiment solely because unrelated late-stage equipment is absent.

### Evidence class

`DERIVED-INTERNAL / RELEVANT-SUBSYSTEM-GATE`.

Current repository state is not physically instantiated.

---

# 8. G1 Stage-0 -> formal F2 release

## Controlled basis

- P21 response-surface/Jacobian method;
- P22 information-optimal DOE;
- P22A multi-subsystem empirical program;
- Round-44 perturbation-resolution relation;
- Round-45 root-count/material plan.

## Required derived logic

Formal F2 roots are not released until:

- Stage-0 variance is available;
- P06 repeatability is known;
- perturbation range has an information lower bound and same-regime upper bound with non-empty overlap;
- exact design/run-order/holdouts are frozen;
- structural root/material plan closes.

### Evidence class

`DERIVED-INTERNAL / SEQUENTIAL-DOE-RELEASE`.

---

# 9. G2 F2 -> F3 anneal release

## Controlled basis

- P06 non-destructive material mapping;
- P05 material-control branch;
- P23 anneal boundary/Jacobian;
- P16G delayed-differentiation/material rules.

## Round-46 derived rule

Not every F2 root advances to anneal.

A selected root must have accepted material-state data, assigned F3 role, preserved P05 branch and feasible post-commit descendant balance.

Selection must follow a predetermined or frozen adaptive rule rather than post-hoc visual/performance cherry picking.

### Evidence class

`DERIVED-INTERNAL / GENEALOGY-SELECTION-CONTROL`.

---

# 10. G3 anneal -> F4 release

## Controlled basis

- P23 carrier boundary;
- P05 Hall/VdP;
- P06 optical preservation;
- P24/P34 RIE process-state qualification.

## Round-46 derived rule

Stable n-like material may advance to the standard detector-process Jacobian when other gates pass.

Transition/multicarrier material remains valuable F3 classifier/boundary evidence but is not silently forced into a one-carrier standard-detector branch.

### Evidence class

`DERIVED-INTERNAL / MODEL-REGIME-CONTROL`.

---

# 11. G4 witness -> detector-bearing RIE state

## Controlled basis

P24 requires material-state and detector-level validation and already warns against optimizing contact resistance alone. Round 44 identifies RIE as a treatment-level empirical Jacobian. Round 45 separates treatment bundle from detector descendant count.

## Round-46 derived staging

Use:

`Tier 1 witness/material-state learning -> Tier 2 selected detector-bearing confirmation`.

Complete detectors are reserved for center/baseline, high-information contrasts, required interaction states, holdouts and detector bridges unless a documented process-geometry reason prevents staged witness use.

### Evidence class

`DERIVED-INTERNAL / SCARCE-MATERIAL-STAGING`.

---

# 12. G5 matched P10-P13/F1 characterization

## Controlled basis

- P10/P11/P12/P13 procedures;
- Round-43 shared-state/covariance logic;
- Round-44 F1 repeated-measure design;
- Round-45 shared-detector rule.

## Round-46 derived release rule

Characterization proceeds only after device geometry/contact identity, measurement-chain acceptance and heating/loading guards are frozen.

Where reversible, preserve the same physical detector across P10/P11/P12/P13/F1.

### Evidence class

`DERIVED-INTERNAL / MATCHED-STATE-EXECUTION`.

---

# 13. G6/G7 singulation and package gates

## Controlled basis

- P35 singulation/die-edge process window;
- P33/P15 package qualification;
- Round-45 F5 die accounting.

## Round-46 derived rule

A characterized detector is not released to singulation until its pre-cut baseline, street/edge exclusion, support/protection and package geometry are controlled.

A singulated die is not released to actual HgCdTe packaging until:

- post-singulation state passes required checks;
- non-HgCdTe package family screening is complete;
- construction level/role is assigned prospectively;
- paired pre-package baseline exists;
- protected die reserve remains feasible.

### Evidence class

`DERIVED-INTERNAL / IRREVERSIBLE-DOWNSTREAM-RELEASE`.

---

# 14. Run-order / blocking basis

## Controlled sources

P22/P22A already distinguish independent units and recognize hard-to-change/sequential structure. P03D/P21 identify LPE source-use/depletion. P24/P34 require chamber genealogy. P23 requires anneal history. P33 requires package build genealogy.

## Round-46 derived rule

Randomize within physically feasible blocks and explicitly model hard-to-change/sequential factors.

If safety or physics prevents randomization, use deliberate counterbalancing/blocking and record the identifiability loss.

Do not permit perfect treatment alias with root/source/chamber/calendar/operator/package batch.

### Evidence class

`DERIVED-INTERNAL / ANTI-CONFOUNDING-EXECUTION`.

---

# 15. Next-action decision basis

## Controlled sources

- Round-43 uncertainty budget;
- Round-44 D/c/A/decision-variance information criteria;
- Round-45 material burden/genealogy accounting.

## Round-46 derived quantities

For candidate action `a`:

`DeltaV_a = V_current - E[V_after | a]`.

Record separately a burden vector containing material and optionality costs.

A candidate is dominated when another feasible candidate produces no smaller expected protected decision-variance reduction while imposing no greater protected burden/confounding, with at least one strict improvement.

### Evidence class

`DERIVED-INTERNAL / DECISION-DOMINANCE`.

Round 46 does not invent one scalar exchange rate between a growth, chamber treatment and package die.

---

# 16. Failure/deviation basis

## Controlled source

P18 failure-analysis diagnostic atlas and related change-control modules.

## Round-46 derived workflow

Unexpected failure triggers:

- sibling HOLD/freeze;
- event classification;
- P18 route;
- use of designated FA reserve where possible;
- determination whether result is true process response or execution-invalid;
- controlled REWORK/STOP/replacement/resume decision.

A true treatment failure is retained as campaign data.

### Evidence class

`DERIVED-INTERNAL / FAILURE-ROUTING`.

---

# 17. Configuration-change basis

## Controlled basis

Round 42 already states configuration change can invalidate calibration/acceptance before calendar expiration.

## Round-46 extension

Every GO decision references exact process, apparatus, calibration, DOE/model and P16G plan revisions.

A decision-affecting configuration change triggers `CONFIGURATION-IMPACT-REVIEW-REQUIRED`; prior GO does not transfer automatically.

### Evidence class

`DERIVED-INTERNAL / CONFIGURATION-CONTROL`.

---

# 18. New integration state

Round 46 defines:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY`.

Current:

`NO / NOT PHYSICALLY INSTANTIATED`.

P16H readiness is not:

- an individual material GO;
- P16A first-build readiness;
- empirical verification;
- historical reproduction;
- P17 reproducible release.

---

# 19. Permanent restrictions

Round 46 shall not be used to claim that:

- a controlled gate procedure means a physical gate passed;
- a technically good sample must be consumed downstream;
- a holdout is spare material;
- a failed process point may be dropped automatically;
- rework preserves original sample role automatically;
- randomization can ignore hard physical constraints;
- more material repairs structural confounding;
- late detector success retroactively validates undocumented upstream execution.

All such claims require separate evidence.