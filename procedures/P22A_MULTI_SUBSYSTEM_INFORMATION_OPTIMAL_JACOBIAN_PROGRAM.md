# P22A — multi-subsystem information-optimal empirical-Jacobian program

**Status:** CONTROLLED ANALYTICAL / PRE-EXPERIMENT EXECUTION ARCHITECTURE  
**Date:** 2026-08-16 America/New_York  
**Use with:** P20/P20A, P21, P22, P23, P24, P25, P33, P16E and `calculations/RP01_EMPIRICAL_JACOBIAN_INFORMATION_DESIGN.md`.

## 1. Purpose

Define how the future laboratory shall close the highest-value `EMPIRICAL-JACOBIAN-REQUIRED` blocks with the minimum number of scientifically identifiable HgCdTe experiments.

P22A is not a generic factorial-design recipe. It controls:

- experimental-unit identity;
- matched blocking/genealogy;
- perturbation-size selection from actual variance;
- model rank and conditioning;
- final-decision information criterion;
- sequential candidate selection;
- holdout confirmation;
- stopping rules;
- promotion into P20/P16E.

The governing chain is:

`P16E dominant uncertainty -> missing derivative/boundary -> experiment unit -> Stage-0 variance -> admissible contrast -> information design -> model/holdout -> detector bridge -> allocation`.

---

# 2. New program-level state

Use:

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`.

This means the planned local empirical campaigns have:

- identified factors/state coordinates;
- identified responses;
- valid experimental-unit structure;
- measured Stage-0 variance/metrology sufficient to choose physical perturbation ranges;
- rank/conditioning reviewed;
- holdout and stopping criteria defined;
- material/genealogy path available.

It does **not** mean the empirical Jacobians have been measured.

Current repository state before physical implementation:

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO`.

Reason: physical infrastructure, Stage-0 variance, actual feasible perturbation ranges and material genealogy do not exist locally.

---

# 3. Campaign priority is dynamic

P22A does not hard-code a permanent execution order.

At each campaign review calculate which missing block contributes most to uncertainty in the current protected detector decision.

Priority inputs:

- P16E current uncertainty contribution;
- P20 downstream sensitivity;
- current coefficient/boundary uncertainty;
- number/cost of independent HgCdTe units;
- surrogate commissioning already available;
- risk of confounding or irreversible material loss;
- whether one run informs multiple protected outputs.

Default analytical order from Round 44 is:

1. canonical field derivatives `s_R,E`, `s_n,E`;
2. P21 LPE Jacobian;
3. P23 anneal boundary/n-like Jacobian;
4. P24/P25 blocking-contact/passivation vector response;
5. P33 package thermal/dynamic Jacobian.

Re-rank once local data exist.

---

# 4. Universal pre-design gate

Before specifying a run matrix, record:

### Requirement

- P19/P16E protected metric;
- numerical decision requirement if available;
- operating condition;
- current uncertainty contribution from the missing block.

### Experimental unit

- what receives one independently assignable treatment;
- what observations are repeated/spatial measures within that unit;
- what genealogy/blocking factor is shared.

### Factor/state coordinate

For every variable:

- actuator/setpoint;
- actual measured physical state;
- whether independently controllable;
- whether hard-to-change;
- whether sequential by definition;
- metrology uncertainty;
- same-regime bounds.

### Response

- measurement method;
- repeatability;
- independent-unit variance;
- expected detector relevance;
- categorical/boundary versus continuous status.

A run matrix shall not be frozen while the unit or factor is still ambiguous.

---

# 5. Stage-0 variance and resolution gate

Before a finite-difference or response-surface campaign, obtain enough center-state data to estimate the variance at the **correct independent-unit level**.

For each protected response estimate separately where possible:

- instrument/measurement repeatability;
- within-unit spatial/repeated-measure variation;
- independent-unit variation;
- time drift.

Then choose perturbation half-range `Delta u` so the protected effect is resolvable.

For an independent symmetric plus/minus pair:

`SE(g)=sigma_y/[sqrt(2m) Delta u]`.

For planning at two-sided alpha=.05 and power=.80:

`eta_min≈1.981/sqrt(m)`

where

`eta=|g|Delta u/sigma_y`.

If the desired derivative contrast cannot be resolved without leaving the same physical regime, do not execute the DOE. Improve metrology/stability or redefine the response first.

---

# 6. Model-rank and conditioning gate

For every proposed design matrix `X`, record:

- model formula;
- `n` independent experimental units;
- number of fitted coefficients `p`;
- `rank(X)`;
- residual degrees of freedom;
- `cond(X^T W X)` or equivalent conditioning diagnostic;
- coefficient covariance / variance-inflation measure;
- exact factor coding.

Require full rank for the claimed model.

A model with unstable partial coefficients because physical variables are not independently actuated shall be replaced by:

- a smaller model;
- a combined physical state coordinate;
- or a different experimental design.

Do not publish unstable regression coefficients as process sensitivities.

---

# 7. Information criterion selection

Use one of the following based on the actual question.

### D-optimal

Use when broad coefficient estimation is desired.

### c-optimal

Use when P20 protects one derivative or linear combination strongly.

Minimize:

`c^T M^-1 c`.

### weighted A/trace

Use when several protected derivatives/outputs matter with known relative importance.

### classifier information

For anneal boundary localization, prioritize points near classifier uncertainty where Bernoulli information is high, while preserving feasible-region constraints.

### decision-variance reduction

Preferred when a current detector requirement and downstream Jacobian exist:

select the candidate expected to reduce final detector-decision variance most.

The chosen criterion and weights are part of the controlled design record.

---

# 8. Universal genealogy/blocking rule

Use matched material aggressively, but analyze the match correctly.

Examples:

- neighboring coupons from one growth assigned across anneal treatments;
- one wafer providing matched RIE/passivation descendants;
- same detector measured before/after package when feasible.

Matching reduces nuisance variance but does not create additional independent process units.

Record:

- growth/wafer/source ID;
- coordinate;
- split assignment;
- treatment order;
- processing history before divergence;
- common downstream processing after convergence.

Randomize treatment within blocks where the physics permits.

---

# 9. Campaign F1 — canonical field derivatives

## 9.1 Objective

Estimate near 80 K / 10 V/cm:

- `s_R,E = partial ln R_v / partial ln E`;
- `s_n,E = partial ln e_n / partial ln E`;
- `s_D,E = s_R,E - s_n,E`.

These close a direct Round-43 field/gap covariance term.

## 9.2 Experimental unit

Completed detector/contact-pair/package state.

Field points on one detector are repeated measurements, not independent devices.

## 9.3 Factor

Use normalized field coordinate

`z_E = ln(E/E0)`

with `E0=10 V/cm` for the canonical RP-01 comparison.

Choose physical `h` only after:

- P10 active-voltage uncertainty;
- P11 responsivity repeatability;
- P12 ASD repeatability;
- temperature/self-heating sensitivity;
- sweepout reversibility

are known.

## 9.4 Acquisition sequence

For each detector use a counterbalanced sequence that contains:

- center;
- `E_-`;
- center;
- `E_+`;
- center;
- reversed order where practical.

This exposes drift and hysteresis rather than confounding them with slope.

Acquire responsivity/noise at matched optical background and load state.

## 9.5 Responses

- `R_v(4 um,1 kHz)`;
- `e_n(1 kHz)`;
- `D*`;
- I/V/R/power;
- temperature proxy;
- sweepout metric;
- polarity/order dependence.

## 9.6 Analysis

Use paired/repeated-measures covariance.

Estimate log slopes by symmetric difference or a local mixed-effects regression when more field points/devices are used.

Test for:

- curvature;
- heating;
- hysteresis;
- device-to-device random slope.

## 9.7 Holdout

Predict at least one interior field not used in the slope estimate.

Promotion to `EMPIRICAL-VERIFIED` requires local prediction agreement and stable thermal state.

---

# 10. Campaign F2 — P21 LPE Jacobian

P21/P22 remain authoritative.

Round-44 additions:

## 10.1 Choose design objective first

If the current P16E need is a local material Jacobian only and interactions/curvature are not required, permit a Jacobian-first axial design.

For three independently controlled factors `{xL,yL,DeltaT_SC}` plus three distributed centers:

`n=2(3)+3=9` independent growths.

This design estimates first-order slopes only.

If interaction/curvature evidence is required, use the existing P22 candidates:

- BBD + centers: `n=15`;
- FCCCD + centers: `n=17`.

No design is selected before morphology/same-regime review.

## 10.2 Sequential factor blocks

Preserve P21 structure:

- source/phase block;
- kinetic `{DeltaT_SC,t_contact}` block;
- inventory/source-use repeated-measures block;
- holdout.

Do not fold source-use sequence into ordinary iid factorial rows.

## 10.3 Protected downstream information

Selected growths must produce matched descendants sufficient to estimate the P06-to-P11 bridge. The campaign is incomplete if it identifies `x_opt` precisely but does not establish how that material state controls the detector response metric actually protected by P16E.

---

# 11. Campaign F3 — Hg-anneal boundary/Jacobian

P23 remains authoritative.

## 11.1 Phase 1 — classifier/boundary

Use the complete pre-anneal state and a rank-adequate coarse design over physically qualified descriptors:

- `T_dwell`;
- dwell duration;
- Hg-source/chemical-potential coordinate;
- cooldown coordinate.

Fit a carrier-state classifier using P05 tensor/signed Hall state.

Do not regress one-carrier `n_H` globally across the p/n boundary.

## 11.2 Active selection

After a usable classifier exists, prioritize feasible candidate coupons with high classification uncertainty and high parameter information.

Keep some points safely inside stable regions for calibration/model checking; do not spend most material there while the boundary remains uncertain.

## 11.3 Phase 2 — n-like local response

Once the intended center lies safely within the n-like region, fit continuous local responses:

- `log10(n_H)` where valid;
- `mu_H`;
- `R_s`;
- P06 edge/x preservation;
- downstream P13/P11/P12 metrics on selected descendants.

Use axial or response-surface support based on required interactions.

## 11.4 Stop condition

Stop boundary refinement when remaining uncertainty in the boundary-normal margin cannot change the P20/P17 process-state decision at the required confidence.

---

# 12. Campaign F4 — blocking contact / passivation

## 12.1 Objective

Identify the vector mapping

`{RIE/passivation physical state}`

`-> {sweepout,R_v,e_n,tau_eff,D*,contact state}`.

`rho_c` alone is not the objective.

## 12.2 Freeze before RIE mapping

Freeze:

- incoming material/Hall state;
- P28/P25 passivation branch;
- Mask-2 geometry;
- Cr/Au branch;
- contact geometry;
- package/test state.

## 12.3 RIE factors versus measured state

Treat controller variables as actuators and record measured state:

- CH4/H2 flow;
- pressure;
- forward/reflected power;
- self-bias/sheath proxy;
- sample temperature;
- oxide-clear time;
- semiconductor exposure;
- chamber clean/season history.

If self-bias and pressure/power cannot be independently varied, do not report independent causal slopes for all three without a design that resolves them.

## 12.4 Jacobian-first option

For `k` independently controllable RIE factors, symmetric axial support with three distributed centers has structural run count

`n=2k+3`.

For `k=4`, this gives 11 independent RIE treatments.

This is a structural information design only, not a final power/sample-size prescription.

## 12.5 Interaction augmentation

Use residuals and physics to add targeted two-factor states rather than immediately executing a full high-dimensional factorial.

Priority interactions include, where independently identifiable:

- pressure × sheath/energy state;
- semiconductor exposure × sample thermal state;
- passivation state × RIE contact state.

## 12.6 Passivation branch

After selecting a stable RIE center, map P25/P28 surface-state factors separately enough to identify:

- oxide/electrochemical trajectory;
- oxide thickness/fingerprint;
- mesa-to-oxide handoff;
- oxide-to-Mask2 history;
- impact on 1/f, responsivity and temporal response.

Do not use mutually dependent coordinates such as `I`, `J` and `A_exposed` as independent factors.

## 12.7 Experimental unit and blocks

Use matched regions/coupons from common growths as blocks. Independent RIE chamber executions remain the process units.

Carry selected treatments through common downstream fabrication so detector-level differences are not confounded with metal/package revision.

---

# 13. Campaign F5 — package thermal/dynamic Jacobian

## 13.1 Surrogate-first screen

Use non-HgCdTe thermal/mechanical assemblies to screen:

- attach-family feasibility;
- bondline control;
- void/coverage metrology;
- thermal response repeatability;
- cryogenic/vacuum cycle survivability.

## 13.2 Freeze discrete construction family

Before estimating a continuous derivative, fix:

- carrier/cold-finger family;
- adhesive family;
- interconnect family;
- optical shield/window;
- vacuum architecture.

Changing family defines another block/branch rather than another point on one continuous slope unless equivalence is demonstrated.

## 13.3 Primary continuous coordinates

Measure, rather than merely nominally set:

- bondline thickness;
- coverage/void fraction;
- die tilt;
- thermal-reference geometry.

## 13.4 Responses

- `R_theta,eff`;
- thermal poles/kernel;
- detector `DeltaT` under defined dissipated power;
- P10 electrical state;
- P12 noise/microphonics;
- P13 raw and de-embedded response;
- mechanical/interconnect survival.

## 13.5 Paired before/after design

Whenever possible characterize the same detector before and after package assembly. Analyze the package-induced difference, retaining paired covariance.

Repeated thermal pulses and cycles on one package estimate repeatability/durability, not package-to-package manufacturing variance.

## 13.6 Curvature

If bondline thickness is treated as one continuous control and a linear slope is insufficient, use at least three distinct qualified levels before fitting curvature. Independent package builds at the levels are required for package-process variance.

No fixed package count is released without Stage-0 variance/power information.

---

# 14. Cross-campaign detector descendants

A major cost-saving rule is to plan descendants before upstream experiments begin.

For selected LPE/anneal/RIE/passivation states, reserve devices/coupons so the same experimental state can feed multiple downstream measurements:

- P05;
- P06;
- P10;
- P11;
- P12;
- P13.

This creates a covariance-aware chain rather than independent datasets from unmatched material.

Do not maximize the number of measured outputs at the cost of destroying independence. The primary experimental unit remains the upstream treatment unit.

---

# 15. Model hierarchy and promotion

For continuous responses:

1. local linear;
2. physically motivated interaction;
3. curvature only when supported;
4. constrained/nonlinear model where regime physics requires it.

For state boundaries:

1. classifier;
2. explicit transition/multicarrier zone;
3. local continuous model within stable region.

Promotion:

`EMPIRICAL-REQUIRED -> DESIGN-IDENTIFIED -> DESIGN-RESOLUTION-VERIFIED -> EMPIRICAL-PRELIMINARY -> EMPIRICAL-VERIFIED -> DETECTOR-BRIDGED -> ALLOCATION-ELIGIBLE`.

Every promotion record shall state:

- model version;
- local factor range;
- coefficient/boundary uncertainty;
- residual diagnostics;
- holdout result;
- genealogy;
- detector operating state.

---

# 16. Sequential next-run algorithm

At each stage:

1. update the fitted model/covariance;
2. generate physically admissible candidates;
3. exclude candidates violating morphology, carrier-state, thermal or EH&S constraints;
4. compute D/c/A/decision-variance information according to the declared objective;
5. penalize/conflict-check candidates with poor identifiability or genealogy aliasing;
6. ask whether a surrogate can answer the question;
7. select the highest scientific-value remaining candidate;
8. freeze its physical setpoints/state expectations before execution;
9. preserve the full result even if it fails.

Failed states can be highly informative about feasible-region boundaries and should enter P18 rather than disappearing from the DOE record.

---

# 17. Stopping criteria

A campaign does not stop because its original run matrix has been completed.

Stop or hand off when:

### Derivative

- derivative contribution to the protected P16E decision is sufficiently small/known;
- model/holdout checks pass;
- further runs have low expected decision-value.

### Boundary

- candidate-center margin and transition-zone uncertainty support the desired state/yield decision.

### Multiresponse

- remaining uncertainty cannot alter the selected process branch under the protected detector requirement.

### Invalidation

Pause if:

- perturbations leave the intended regime;
- independent-unit variance makes the planned effect unresolved;
- metrology fails the Round-42 decision-discrimination gate;
- design matrix becomes confounded/rank deficient;
- apparatus state is not measured sufficiently to assign the treatment coordinate.

---

# 18. Required design record

Before physical execution of any P22A campaign, complete `travelers/P16F_EMPIRICAL_JACOBIAN_INFORMATION_REGISTER.md` with:

- requirement/uncertainty target;
- unit/block/genealogy;
- factors and measured state coordinates;
- Stage-0 variance;
- physical/coded ranges;
- response vector;
- model;
- rank/conditioning;
- information criterion;
- exact run/candidate matrix;
- randomization/sequential constraints;
- holdout plan;
- descendant plan;
- stopping rule;
- EH&S/facility status.

---

# 19. Current project disposition

P22A defines the analytical architecture only.

Because no local physical laboratory/variance/factor-range data exist:

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO`.

No P21/P23/P24/P25/P33 derivative is promoted by this document.

No P16A/P16C/P16D/P16E/P17 state is promoted.

---

## Permanent Round-44 rule

**A run is valuable only to the extent that it resolves an identifiable uncertainty that can change the detector decision.**

Do not consume HgCdTe to estimate coefficients that are neither identifiable nor decision-relevant.