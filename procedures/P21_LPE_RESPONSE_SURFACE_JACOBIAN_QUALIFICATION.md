# P21 — LPE response-surface / Jacobian qualification

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD / PRE-SPECIFICATION  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Experimentally identify the local mapping

`{xL,yL,TL_actual,DeltaT_SC,t_contact,melt inventory/source history,Hg-loss state}`

into

`{x_opt, thickness, spatial uniformity, optical edge, morphology}`

for the selected RP-01 Te-rich horizontal-slider apparatus, then connect those material outputs to detector spectral response through P06/P11.

P21 is the first dedicated empirical-Jacobian module under P20.

It does not prescribe a historical Honeywell growth time, charge mass or temperature tolerance.

---

## 2. Why a dedicated module is required

The current P03 documents correctly establish that:

- the Honeywell xL=.082/yL=.810/507 C tie line is a historical anchor, not a complete recipe;
- growth thickness depends on time, supercooling, thermal trajectory and melt geometry/history;
- actual liquidus must be measured or locally inferred;
- finite liquid dimensions and Hg loss alter growth rate/composition;
- source-use history may change the process state.

P20 now requires numerical derivatives before tolerances can be allocated.

P21 converts those qualitative/coupled dependencies into a statistically identifiable local response surface.

---

## 3. Controlled factors

The first P21 campaign should use one frozen:

- graphite boat revision;
- substrate dimensions/recess;
- substrate face/miscut and P07C surface-prep route;
- source-preparation route/lot class;
- auxiliary-Hg architecture;
- atmosphere sequence;
- thermal trajectory family;
- wipe-off method;
- P06 acquisition/model version.

Changing any of these defines a new apparatus/process block unless equivalence is demonstrated.

Primary continuous/coded factors:

1. actual `xL` reconstructed from delivered masses;
2. actual `yL` reconstructed from delivered masses;
3. corrected local `DeltaT_SC = TL_actual - T_contact`;
4. exact contact time `t_contact`;
5. effective liquid depth `h_liquid` or another validated inventory coordinate;
6. source-use/depletion coordinate;
7. Hg-loss state/proxy where independently calibrated.

Do not substitute controller setpoint for `DeltaT_SC` or nominal gram mass for effective liquid depth when those differ materially.

---

## 4. Mandatory response vector

At each run acquire, at minimum:

### P06 material state

- mean `x_opt`;
- `sigma_x`, min/max and spatial gradient;
- defined transmission-edge metric(s);
- mean `d_FTIR`;
- thickness standard deviation and gradient;
- fit residual/model quality;
- composition-gradient parameter where identifiable.

### morphology/yield state

- full-wafer/coupon optical image;
- residual-melt footprint;
- terrace/macrostep/pit/void metrics;
- usable-area fraction;
- wipe-off damage state.

### thermal/source state

- `TL_actual` evidence/version;
- complete T(t) trace;
- sensor-to-melt correction/version;
- actual contact/separation timestamps;
- source-use index;
- pre/post source/Hg-source mass where meaningful;
- liquid inventory/depth coordinate.

### downstream confirmation state

On selected runs:

- P05 transport after the same P04 route;
- P11 detector spectral response after matched downstream processing.

---

## 5. DOE architecture — sequential, not one giant factorial

### Stage 0 — metrology and center-state qualification

Before estimating derivatives:

1. qualify P06 repeatability on a stable reference specimen;
2. qualify balance/delivered-mass uncertainty from the existing charge-sensitivity method;
3. establish the local `TL_actual` measurement/inference method under P03E;
4. dimension the melt well and calculate the selected inventory/depth coordinate;
5. demonstrate timestamp resolution and thermal-trace synchronization;
6. execute independent nominal-center growths to estimate run-to-run variance.

Do not estimate a process derivative whose intended perturbation is smaller than the combined metrology/run noise.

### Stage 1 — source/phase perturbation block

Hold time, liquid depth and thermal-trajectory family fixed.

Perturb locally around the candidate source state:

`{xL,yL,DeltaT_SC}`.

Use perturbations large enough to resolve output changes but small enough to remain in the same physical epitaxial-growth regime.

Responses:

`{x_opt,d,edge,morphology,TL_actual}`.

Purpose:

- estimate local source-composition response;
- identify xL-yL and composition-supercooling interactions;
- test whether a linear local model is adequate.

### Stage 2 — kinetic block

At the selected source state, vary

`{DeltaT_SC,t_contact}`

with repeated center runs.

Estimate:

- `partial d/partial t`;
- `partial d/partial DeltaT_SC`;
- `partial x_opt/partial t`;
- `partial x_opt/partial DeltaT_SC`;
- `t*DeltaT` interaction;
- corresponding spatial-uniformity/morphology responses.

Do not pool step-cooled and ramp-cooled datasets into one slope.

### Stage 3 — finite-liquid / source-history block

At the selected source/thermal/time state, vary

`{h_liquid or inventory coordinate, source-use/depletion state}`.

Where feasible, include a fresh-source and repeated-use sequence while preserving run order.

Purpose:

- determine when finite-reservoir behavior becomes material;
- determine whether source-use drift is reproducible/correctable;
- separate output drift from nominal recipe perturbation.

Track the model-conditioning variables from `RP01_LPE_TO_SPECTRAL_JACOBIAN_FRAMEWORK.md`, including `Fo_L` where a justified `D_eff` is available and extraction loading `epsilon_m`.

### Stage 4 — holdout confirmation

Select predicted process points that were not used in model fitting, including at least:

- nominal center;
- one combined perturbation inside the intended operating region;
- one near-margin point where morphology remains acceptable.

Prediction residuals must be consistent with the declared local model uncertainty before using the Jacobian for P20 allocation.

---

## 6. Independent-run requirement

P06 map points from one growth are repeated measurements/locations within one run; they are not independent LPE replicates.

Estimate at least three variance layers separately:

`measurement -> within-growth spatial -> independent-run`.

Source-lot and long-term tool variance are later P17 layers and should not be conflated with the initial local Jacobian fit.

---

## 7. Model-fitting hierarchy

For each scalar response, begin with the simplest model that represents the data.

### First-order local model

`y = beta0 + sum beta_i z_i + error`.

### Interaction model

Add only physically motivated/resolved terms:

`+ sum beta_ij z_i z_j`.

### Curvature model

Add quadratic terms when center-vs-edge residuals demonstrate curvature:

`+ sum beta_ii z_i^2`.

Do not retain a higher-order term only because it reduces training residual.

Store:

- coefficient estimates;
- covariance matrix;
- residuals;
- lack-of-fit result;
- leverage/influence diagnostics;
- prediction uncertainty;
- exact factor scaling/centering.

---

## 8. Jacobian extraction

At a selected process point `u0`, calculate

`J_m,u(u0) = partial m/partial u | u0`.

Report both:

- dimensional derivatives in engineering units;
- normalized sensitivities where meaningful.

Every derivative entry must include:

- output;
- input;
- process center;
- model version;
- valid local range;
- standard/expanded uncertainty or confidence interval;
- evidence class `EMPIRICAL-VERIFIED` only after holdout confirmation.

Until then it remains `EMPIRICAL-REQUIRED` or `EMPIRICAL-PRELIMINARY`.

---

## 9. Collinearity guard

Some factors are naturally coupled:

- mass errors change both xL and yL;
- actual liquidus changes with source composition/state;
- changing melt mass changes liquid depth and thermal lag;
- run order changes depletion and cumulative thermal history;
- Hg loss can shift liquidus and solid composition together.

Do not interpret regression coefficients as physical partial derivatives when the DOE has not independently varied the factors enough to identify them.

Required checks:

- design-matrix rank;
- condition number / variance-inflation diagnostic;
- covariance/correlation among fitted coefficients;
- physical identifiability review.

If two factors cannot be independently identified in the apparatus, define and control an appropriate combined state variable rather than reporting unstable separate slopes.

---

## 10. Morphology is a constraint, not merely another scalar optimization target

A mathematically attractive x/thickness center is unacceptable if it crosses into:

- secondary nucleation;
- rough/non-epitaxial growth;
- severe terracing/macrostep instability;
- residual melt/wipe-off failure;
- poor usable-area yield.

Define a feasible region

`Omega_feasible = {u : morphology/yield gates pass}`.

Optimize/center the x/thickness response only inside this region.

P20 tolerance allocation may not extend the allowed process distribution outside `Omega_feasible` even if the linear spectral budget would permit it.

---

## 11. Robust process center

After fitting, do not select the center solely by solving

`d=9.5 um` and `x_opt=target`.

Prefer a point that also minimizes local sensitivity to realistic disturbances.

A candidate robustness objective is

`J_robust = trace(W J_m,u Sigma_u J_m,u^T) + morphology_penalty`

where `W` weights protected material outputs.

This is a design/qualification objective, not a published RP-01 criterion.

The selected center must remain traceable to the detector spectral requirement once the P06/P11 bridge exists.

---

## 12. Build the P06-to-P11 spectral bridge

For matched wafer/die positions and a frozen downstream process, record

`{x_opt,d,gradient,edge_metric}` from P06

and

`{lambda_det_metric,R_v(lambda),edge_slope}` from P11.

Use the same explicit detector cutoff convention for every device.

Fit a local relation such as

`lambda_det = a0 + a_x x_opt + a_d d + a_g gradient + ...`

only when supported by data.

Do not force Hansen `hc/Eg` as the detector-response relation.

Once verified,

`J_lambda,u = J_lambda,m J_m,u`.

This is the first defensible path from detector spectral requirement to LPE process tolerances.

---

## 13. Requirement allocation handoff to P20

P21 hands P20:

- selected process center;
- local valid factor ranges;
- `J_m,u` and covariance;
- P06/P11 `J_lambda,m` when available;
- response-model residual/prediction uncertainty;
- metrology covariance;
- morphology feasible region;
- unresolved interactions.

P20 then allocates the spectral budget backward.

No individual LPE limit becomes a P17 specification until:

1. the relevant derivative is identified and validated;
2. the final detector requirement is numeric;
3. covariance/model uncertainty is included;
4. confirmation devices validate the backward allocation;
5. P17 demonstrates capability.

---

## 14. Minimum data record per growth

- growth ID/date/operator;
- source lot/preparation route;
- source-use index;
- actual component masses and reconstructed xL/yL;
- balance/transfer uncertainty version;
- liquid inventory/depth geometry version;
- `TL_actual` method/result/uncertainty;
- complete thermal trace;
- corrected `DeltaT_SC`;
- contact/separation timestamps;
- contact duration;
- auxiliary-Hg state/proxy;
- substrate lot/face/miscut/P07C state;
- wipe-off state;
- P06 raw spectra/map and model version;
- morphology images/metrics;
- P05/P11 downstream dataset links where applicable;
- DOE factor levels/coded values;
- inclusion/exclusion disposition and reason.

---

## 15. Failure / invalidation conditions

Invalidate or separately model a run when:

- source composition falls outside the planned perturbation region;
- `TL_actual` cannot be established to required confidence;
- thermal trajectory changes mode;
- uncontrolled Hg-loss event occurs;
- substrate prep differs;
- residual melt obscures thickness/optical measurement;
- P06 model fails QC;
- morphology crosses a different growth regime;
- source-use state is unknown;
- equipment revision changes mass-transfer geometry.

Do not silently discard failed runs; preserve them for boundary/failure analysis under P18.

---

## 16. Current release blockers

P21 remains pre-specification until:

1. an explicit local boat/melt geometry is frozen;
2. source preparation and delivered-mass metrology are qualified;
3. `TL_actual` measurement/inference is qualified;
4. independent center-run variance is measured;
5. Stage 1-3 perturbation datasets exist;
6. P06 composition/thickness model repeatability is quantified;
7. holdout predictions verify the material response surface;
8. matched P06/P11 data identify the detector spectral bridge;
9. a detector-level spectral acceptance band is defined;
10. P20 completes backward allocation.

---

## 17. References

- Bowers and Schmit, U.S. Patent 4,317,689 (1982).
- Sanz-Maudes et al., *J. Crystal Growth* 106, 303-317 (1990), DOI `10.1016/0022-0248(90)90076-W`.
- Harman, Te-rich HgCdTe LPE phase/growth work (1980), DOI `10.1007/BF02822728`.
- P03B/P03C/P03D/P03E, P06, P17, P18, P20 and `calculations/RP01_LPE_TO_SPECTRAL_JACOBIAN_FRAMEWORK.md`.
