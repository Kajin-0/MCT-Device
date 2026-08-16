# RP-01 empirical-Jacobian information design — Round 44

**Status:** CONTROLLED DERIVED CALCULATION / DOE-PLANNING INPUT  
**Date:** 2026-08-16 America/New_York  
**Use with:** P20/P20A, P21, P22, P23, P24, P25, P33, P16E and the Round-43 uncertainty budget.

## 1. Purpose

Provide the mathematical design layer for the missing empirical Jacobians that currently block detector-derived process allocation.

The controlling problem is not simply “run a DOE.” It is:

`final detector decision -> protected linear/nonlinear response combination -> missing empirical derivative/boundary -> admissible experimental unit -> information-optimal perturbation -> holdout validation`.

The same design is not appropriate for:

- repeated electrical measurements on one completed detector;
- independent LPE growths;
- matched anneal coupons;
- RIE chamber runs;
- package builds.

Round 44 therefore treats **experimental-unit identity and covariance** as part of the design matrix.

No physical perturbation magnitude in this document is a released process tolerance.

---

# 2. Evidence states for empirical derivatives

Use:

- `EMPIRICAL-REQUIRED` — derivative/boundary has no local data;
- `DESIGN-IDENTIFIED` — factors/responses/experimental unit/model are defined, but physical factor ranges or variance are still open;
- `DESIGN-RESOLUTION-VERIFIED` — Stage-0 variance and metrology show the selected perturbations can resolve the protected effect;
- `EMPIRICAL-PRELIMINARY` — coefficient/boundary is estimable but not independently confirmed;
- `EMPIRICAL-VERIFIED` — holdout-confirmed over a declared local region;
- `DETECTOR-BRIDGED` — intermediate derivative has been connected to a protected detector response under matched state;
- `ALLOCATION-ELIGIBLE` — P20/P16E may use the derivative in a local requirement allocation.

A p-value alone does not advance an evidence state.

---

# 3. Experimental-unit rule

For every design declare the unit that receives an independently assignable process treatment.

Examples:

- P10/P11/P12 field sweep: completed detector is the unit; multiple field points are repeated measures on that detector;
- P21 LPE: independent growth is the process unit; P06 map points are within-growth observations;
- P23 anneal: coupon/anneal history is the treatment unit, with growth/wafer as a block/random effect;
- P24 RIE: independently executed RIE chamber treatment is the process unit; multiple structures within the same RIE exposure are within-run observations;
- P33 package: independently assembled package is the package-process unit; multiple pulses/cycles on one package are repeated measures.

Do not multiply nominal sample size by counting spatial points, FFT bins, repeated pulses, or repeated source-use observations as independent process replicates.

---

# 4. Symmetric local derivative estimator

For a scalar response `y(u)` around center `u0`, use a symmetric perturbation when physically admissible:

`u_- = u0 - Delta u`

`u_+ = u0 + Delta u`.

The central first-order estimator is

`g_hat = [y(u_+) - y(u_-)]/(2 Delta u)`.

For independent equal-variance observations with residual standard deviation `sigma_y` and `m` independent plus/minus pairs:

`SE(g_hat) = sigma_y / [sqrt(2m) Delta u]`.

Define the standardized half-range effect

`eta = |g| Delta u / sigma_y`.

Using a normal-approximation two-sided alpha=0.05 and target power=0.80,

`z_(.975)+z_(.80) = 2.8016`.

Therefore a one-pair slope requires approximately

`eta >= 2.8016/sqrt(2) = 1.981`

for the stated planning approximation.

For `m` independent pairs:

`eta_min ≈ 1.981/sqrt(m)`.

Examples:

- `m=1`: `eta_min≈1.981`;
- `m=2`: `eta_min≈1.401`;
- `m=3`: `eta_min≈1.144`;
- `m=4`: `eta_min≈0.991`.

These are **planning scales**, not release thresholds. Exact finite-sample power should use the final model, degrees of freedom and variance structure.

---

# 5. Paired/correlated derivative estimator

When plus/minus conditions are measured on matched units or one repeated-measures unit, covariance matters.

For one pair:

`Var(g_hat) = [Var(y_+) + Var(y_-) - 2 Cov(y_+,y_-)]/(4 Delta u^2)`.

Positive common-mode covariance can improve contrast precision because common drift cancels. Negative or hysteretic covariance can worsen it.

Therefore matched-wafer, matched-device and before/after designs should preserve pairing in the analysis rather than discarding it and applying an iid RSS formula.

---

# 6. Logarithmic derivative for canonical electric-field slopes

Round 43 requires

`s_R,E = partial ln R_v / partial ln E`

and

`s_n,E = partial ln e_n / partial ln E`

near the canonical 80-K / 10-V/cm state.

Use multiplicatively symmetric fields when safe:

`E_- = E0 exp(-h)`

`E_+ = E0 exp(+h)`.

Then

`s_y,E ≈ [ln y(E_+) - ln y(E_-)]/(2h)`.

This is preferable to an asymmetric absolute-voltage perturbation because it estimates the normalized derivative directly.

The protected detectivity field sensitivity at fixed optical power/area convention is

`s_D,E = s_R,E - s_n,E`.

Round-43 gap coupling then becomes

`S_D,L = 0.5 - gamma_L - s_R,E + s_n,E`

for fixed physical active voltage and `A=W L`.

### Required nuisance observations

Every field-slope dataset must also record:

- active-region voltage, not only source voltage;
- measured gap;
- current and dissipated power;
- direct or qualified detector-temperature proxy;
- load network;
- optical power/background;
- noise-chain state;
- sweep direction/order;
- time at field.

A field derivative contaminated by self-heating or sweepout hysteresis is not a local isothermal derivative.

---

# 7. Axial Jacobian-first design

If the immediate objective is only a first-order local Jacobian for `k` independently controllable factors and interactions/curvature are not yet required, an orthogonal symmetric axial design is information-efficient:

- `+1` and `-1` on each factor axis;
- `r` center runs distributed through time.

Run count:

`n = 2k + r`.

For the coded first-order model

`y = beta0 + sum beta_i z_i + error`,

the axis columns are orthogonal and each has sum of squares 2 for one plus/minus pair per factor.

Thus, before using center runs to estimate residual variance,

`SE(beta_i) = sigma/sqrt(2)`.

Physical derivative:

`g_i = beta_i/Delta u_i`.

### Restriction

The axial design contains no information for factor-factor interactions and only limited evidence about curvature. It is appropriate only when:

- P20 needs local slopes first;
- the perturbation region is demonstrably small/same-regime;
- prior physics does not require an interaction term immediately;
- sequential augmentation is planned.

If interactions are scientifically expected, use P22 FCCCD/BBD/targeted-corner augmentation instead.

---

# 8. Information criteria — D-optimal is not always the final objective

For model matrix `X` and inverse-variance weights `W`, information is

`M = X^T W X`.

P22 already uses the D-information increment for a candidate row `x_c`:

`q_c = w_c x_c^T M^-1 x_c`.

Adding the run multiplies `det(M)` by `1+q_c`.

D-optimality is useful when all model coefficients matter comparably.

Round 44 adds two task-targeted alternatives.

## 8.1 c-optimal protected combination

If P20 identifies a protected linear combination

`theta = c^T beta`,

its variance is

`Var(theta_hat) = c^T M^-1 c`.

Choose candidates that most reduce this variance when the final detector decision depends primarily on `theta`, not on every coefficient equally.

Example: if the final need is the LPE-to-spectral derivative in one disturbance direction, estimating unrelated quadratic terms with high precision may have less value than reducing variance of that one projected derivative.

## 8.2 A/trace criterion for a protected vector

For several protected quantities with weighting matrix `W_p`, use

`Phi_A = trace[W_p Cov(beta_protected)]`.

Minimize this when multiple derivative directions matter but determinant balance is not the scientific objective.

### Permanent rule

Select an information criterion from the downstream decision, not from generic DOE habit.

---

# 9. Multiresponse final-decision information

Suppose process controls `u` produce intermediate response vector `m`, and the detector metric `d` has local sensitivity row vector `J_d,m`.

Then

`J_d,u = J_d,m J_m,u`.

The uncertainty of the empirical Jacobian `J_m,u` contributes to uncertainty in `J_d,u`.

A candidate experiment is high value when it reduces the covariance of the components of `J_m,u` that project strongly through `J_d,m`.

Thus an information priority can be based on expected reduction in

`Var(J_d,u)`

rather than equal weighting of every measured response.

Until `J_d,m` is known, use explicit surrogate weights and label them `INFORMATION-PRIORITY-ASSUMPTION`.

---

# 10. Classification-boundary information — Hg anneal

For a logistic-style carrier-state classifier

`p(N-LIKE|a) = 1/[1+exp(-g(a))]`,

the Bernoulli information multiplier for the linear predictor is proportional to

`p(1-p)`.

This is maximized at

`p=0.5`.

Therefore, once a coarse P23 carrier-state model exists, new boundary-location coupons should preferentially challenge the uncertain transition region rather than repeatedly sample points with `p≈0` or `p≈1`, subject to optical/morphology safety and initial-state balance.

This mathematically supports P23's active-boundary rule.

### Important restriction

Boundary-location points are not automatically the best points for precise n-like continuous derivatives. The campaign must separate:

1. classifier/boundary information;
2. local n-like response-surface information safely away from the singular transition region.

---

# 11. Blocked and mixed designs

Material genealogy commonly creates nuisance variation larger than the process perturbation.

Use matched blocks where possible:

- neighboring coupons from one growth;
- matched device geometry from one wafer;
- same process lot split across treatments.

A generic model is

`y_ijk = fixed(process factors) + b_growth/wafer + b_run + error`.

Use random effects only at genuinely sampled grouping levels.

Do not model one source charge or one wafer as a random population merely because it contains many measurement locations.

---

# 12. Campaign A — canonical field derivatives

## Objective

Close the Round-43 derivatives:

- `s_R,E`;
- `s_n,E`;
- consequently `s_D,E`.

## Unit

Completed detector/contact-pair/package state.

## Design

For each qualified detector:

1. center at `E0=10 V/cm`;
2. choose multiplicative half-range `h` only after P10/P11/P12 precision and heating/sweepout checks;
3. measure `E_-`, center, `E_+` with order reversal/counterbalancing;
4. repeat center after the excursion to measure drift/hysteresis;
5. use several independent detectors to estimate device-to-device variation in slope.

No universal `h` is assigned. It must satisfy:

- predicted contrast is resolvable using Section 4;
- temperature change remains negligible or explicitly corrected;
- response remains in the same local sweepout regime;
- detector state is reversible over the excursion.

## Responses

- `ln R_v(4 um,1 kHz)`;
- `ln e_n(1 kHz)`;
- `D*` reconstructed from matched state;
- current/resistance/power;
- detector-temperature proxy;
- polarity/sweep-direction diagnostics.

## Holdout

Predict one interior field not used in the derivative estimate and verify local linearity in log-space within declared uncertainty.

---

# 13. Campaign B — P21 LPE Jacobian

P21/P22 remain authoritative for the complete LPE design.

Round-44 priority sequence is:

1. Stage-0 independent center-run variance and metrology;
2. decide whether immediate need is Jacobian-only or interaction/curvature capable;
3. if Jacobian-only is scientifically adequate, a `k=3` axial screen for `{xL,yL,DeltaT_SC}` plus three distributed centers has structural size `n=9` independent growths;
4. if interactions/curvature must be identified, use P22's 15-run BBD or 17-run FCCCD candidate instead;
5. Stage-2 `{DeltaT_SC,t_contact}` and Stage-3 inventory/source-use are then added sequentially;
6. select later runs by protected P06/P11 information value, not determinant alone.

The 9-run axial option is not a replacement for P22. It is a lower-dimensional **Jacobian-first option** that is invalid if interaction/curvature evidence is required.

### Highest-value bridge

The eventual protected quantity is not merely `x_opt`; it is the matched P06-to-P11 spectral response derivative.

Therefore reserve matched downstream detector descendants from selected LPE states early enough to estimate

`J_lambda,m` and `J_D,m`.

---

# 14. Campaign C — P23 Hg-anneal boundary and n-like Jacobian

## Phase C0 — initial-state blocking

Use coupons with pre-anneal P05/P06 state recorded. Block by growth/wafer and preserve spatial coordinates.

## Phase C1 — boundary localization

Factors/state descriptors may include:

- dwell sample temperature;
- dwell time;
- Hg-source/chemical-potential coordinate;
- one controlled cooldown descriptor.

Use a rank-adequate coarse design to seed the classifier, then select additional coupons near high classification uncertainty (`p≈0.5`) subject to feasible-region constraints.

## Phase C2 — n-like local Jacobian

Once a candidate center is demonstrably inside a stable n-like region, estimate continuous derivatives only there.

Use an axial or response-surface design depending on required interactions.

Primary outputs:

- signed Hall/tensor state;
- `log10(n_H)` where one-carrier-valid;
- `mu_H`;
- P06 edge/x preservation;
- selected P13/P11/P12 downstream metrics.

## Stop condition

Boundary exploration may stop when the uncertainty of the boundary-normal margin at the candidate center is small enough for P20/P17 to make the desired state-yield decision. No universal sigma margin is assigned.

---

# 15. Campaign D — blocking-contact / passivation vector response

## 15.1 Why process actuators and physical state must be separated

RIE controller variables are not the final physical coordinates.

Candidate actuators include:

- pressure;
- RF forward power or other energy actuator;
- total/plasma exposure time;
- chuck/thermal control where available.

Measured state coordinates include:

- actual gas flows;
- pressure;
- self-bias/sheath proxy;
- reflected power;
- sample-temperature trajectory;
- oxide-clear time `t_clear`;
- semiconductor exposure `t_sem`;
- converted sheet state;
- `d_conv/L_conv`;
- physical etch depth/damage.

Regress detector response against the measured physical state where possible; do not call a controller wattage a transport-state derivative.

## 15.2 Sequential design — do not vary everything at once

### D0 — passivation baseline freeze

Hold P25 oxide branch, Mask-2, contact geometry and downstream metal/package state fixed while first mapping the RIE response.

### D1 — local RIE state Jacobian

If `k` independent RIE factors are selected, a Jacobian-first structural design is `2k+r` independent chamber treatments. For four independently controllable factors and three distributed centers this is 11 treatments.

This 11-run number is a mathematical structural example, not a power recommendation and not required if fewer factors are independently controllable.

Responses:

- `t_clear`;
- `d_etch`;
- self-bias/thermal state;
- converted sheet transport;
- `d_conv/L_conv` where measured;
- `rho_c`;
- LBIC/junction signature;
- `R_v(E)` and sweepout metric;
- `e_n(f,E)`;
- `tau_eff/f3dB`;
- `D*`.

### D2 — interaction augmentation

Add targeted two-factor combined perturbations only for interactions justified by D1 residuals/physics, particularly pressure × energy/sheath state and exposure × thermal state.

### D3 — passivation/sidewall branch

After an RIE center is selected, vary the small number of independently controlled P25/P28 surface-state factors without simultaneously reopening the entire RIE design.

Useful physical coordinates include:

- oxide charge/current-density trajectory;
- charge per exposed area;
- oxide thickness/optical fingerprint;
- mesa/oxide handoff delay;
- post-oxide lithography exposure history.

Avoid choosing mathematically dependent factors such as current, current density and exposed area as if they were independent.

### D4 — matched detector confirmation

Carry selected state perturbations through the identical Cr/Au/package chain and confirm predicted vector response.

## Analysis

Because improvements in `R_v`, `e_n`, `tau` and sweepout may conflict, use a multiresponse/c-optimal criterion tied to the final P20 protected quantity rather than optimizing `rho_c` alone.

---

# 16. Campaign E — package thermal/dynamic Jacobian

## Phase E0 — surrogate construction screen

Before consuming detector-quality HgCdTe, use thermal/mechanical surrogate assemblies to screen:

- candidate attachment family;
- bondline-process controllability;
- void/coverage metrology;
- thermal transfer repeatability;
- vacuum/cycle survivability.

Do not infer HgCdTe stress/noise equivalence from surrogate success.

## Phase E1 — choose one construction family

Freeze carrier, adhesive family, interconnect family, window/shield and vacuum architecture before estimating continuous derivatives.

## Phase E2 — local package state design

Primary measured coordinates should include:

- bondline thickness;
- coverage/void fraction;
- die tilt;
- carrier/cold-finger temperature geometry;
- interconnect state.

For one dominant continuous factor such as bondline thickness, use at least three separated levels if curvature must be tested. Multiple independent package builds per level are required to estimate package-build variance; repeated pulses on one package are not independent builds.

For two continuous package factors, use an axial/quadratic sequential design only after surrogate screening identifies a feasible region.

## Responses

- `R_theta,eff`;
- package thermal kernel / poles;
- die-temperature rise under defined power;
- P10 resistance/bias shift;
- P12 noise/microphonics;
- P13 measured transfer before and after package de-embedding;
- crack/delamination/interconnect survival.

## Paired detector design

Whenever possible obtain a pre-package electrical/noise/dynamic baseline and analyze the package-induced change on the same detector. This removes a large amount of material/device common-mode variation.

---

# 17. Run-value score

Before selecting the next expensive HgCdTe run, record:

1. protected detector requirement or uncertainty term;
2. current posterior/coefficient uncertainty;
3. candidate expected information reduction;
4. experimental-unit cost/material consumption;
5. genealogy/confounding risk;
6. feasibility/morphology/safety risk;
7. whether a non-HgCdTe surrogate can answer the same question.

A conceptual utility is

`U(c) = Delta V_decision(c) / Cost(c)`

subject to feasibility and identifiability gates.

Do not assign arbitrary monetary weights unless the laboratory actually uses them. The purpose is to prevent low-information repetition from consuming scarce HgCdTe.

---

# 18. Sequential stopping rules

A campaign stage can stop only when its scientific objective is met, not merely because a planned run count is complete.

Possible stopping conditions:

### derivative stage

- target derivative confidence/prediction interval is narrow enough that its contribution to the P20 final decision is below the allocated uncertainty;
- local-linearity/interaction checks pass;
- holdout prediction passes.

### boundary stage

- candidate process-center margin to the transition boundary is resolved sufficiently for the required state/yield decision;
- transition-zone uncertainty is included.

### multiresponse stage

- remaining model uncertainty cannot change the process-branch decision within the protected detector metric;
- further candidate runs have low expected decision-variance reduction relative to cost.

### failure stop

Pause/redefine the design if:

- perturbations cross a new physical regime;
- metrology/run variance is larger than the resolvable contrast;
- rank/conditioning degrades;
- factor actuation is confounded with unmeasured state;
- genealogy prevents identifying the intended coefficient.

---

# 19. Holdout rule

Every empirical Jacobian intended for P20 allocation requires independent confirmation not used to fit the coefficient.

Holdouts should challenge the actual protected prediction, not merely repeat the easiest center.

Examples:

- one interior off-axis LPE state;
- one anneal state near the selected boundary margin;
- one RIE combined perturbation predicted from separate slopes;
- one package build at an interior bondline state;
- one electrical field point between the fitted plus/minus conditions.

Prediction interval and model discrepancy must be reported.

---

# 20. Round-44 information hierarchy

Current order of analytical value is:

1. **Field derivatives `s_R,E`, `s_n,E`** — low additional material cost once a qualified device exists; closes a direct Round-43 covariance term.
2. **P21 LPE response surface** — high upstream leverage but expensive independent growth unit.
3. **P23 anneal boundary/Jacobian** — necessary because carrier-state sign creates a nonlinear boundary rather than one global slope.
4. **P24/P25 blocking-contact/passivation vector response** — direct D*/sweepout/noise/lifetime leverage, but requires matched downstream detector descendants.
5. **P33 package thermal/dynamic Jacobian** — required to separate device lifetime/self-heating from assembly response.

The order is not a fixed execution calendar. A future laboratory should recompute information value from actual variances, availability and current P16E dominant uncertainty.

---

## Permanent Round-44 rule

**Optimize experiments for the uncertainty of the detector decision, not for the number of process coefficients estimated.**

A smaller, well-conditioned design aimed at the protected Jacobian can be scientifically superior to a larger generic factorial that spends HgCdTe estimating parameters irrelevant to the final decision.