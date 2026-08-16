# RP-01 gap matrix addendum — round 14 LPE Jacobian

**Date:** 2026-08-16 America/New_York

This addendum converts the P03/P06 upstream sensitivity problem into explicit closure tasks.

## G-R14-01 — independent source-composition partial derivatives

**Gap:** local values of

- `partial x_opt/partial xL`;
- `partial x_opt/partial yL`;
- interactions with `DeltaT_SC`.

**Why unresolved:** Honeywell tie-line rows change xL, yL and TL together. The table cannot identify independent partial derivatives.

**Closure:** P21 Stage 1 local source/phase perturbation DOE with reconstructed actual xL/yL and qualified P06 composition/edge outputs.

**Status:** `EMPIRICAL-REQUIRED`.

## G-R14-02 — local supercooling sensitivity

**Gap:**

- `partial x_opt/partial DeltaT_SC`;
- `partial d/partial DeltaT_SC`;
- morphology boundary versus supercooling.

**Closure:** P21 Stage 1/2 using `DeltaT_SC=TL_actual-T_contact`, not nominal controller temperature.

**Status:** `EMPIRICAL-REQUIRED`.

## G-R14-03 — local growth-time derivative

**Gap:** `partial d/partial t_contact` and composition-time coupling at the selected thermal mode.

**Why unresolved:** literature growth times span different apparatus, supercooling and finite-melt states; no universal time law is transferable.

**Closure:** P21 Stage 2 with repeated center runs and local model selection.

**Status:** `EMPIRICAL-REQUIRED`.

## G-R14-04 — finite-liquid transition / inventory sensitivity

**Gap:** response to effective liquid depth/inventory and the characteristic time at which finite-reservoir effects become material in the selected boat.

**New controlled diagnostic:**

`Fo_L=D_eff t/h_liquid^2`

may be used as a model-conditioning coordinate only after a justified `D_eff` is selected/validated.

**Closure:** P21 Stage 3 melt-depth/inventory perturbation plus source-use sequence.

**Status:** `MODEL-CONDITIONAL + EMPIRICAL-REQUIRED`.

## G-R14-05 — Hg-loss response

**Gap:** local mapping from Hg-loss state into actual liquidus and grown composition.

**Required distinction:** Hg loss, finite-reservoir solute extraction and source-use thermal history are not the same variable.

**Closure:** calibrate a physically meaningful Hg-loss proxy or cumulative fractional Hg loss and correlate with TL_actual/P06 outputs.

**Status:** `EMPIRICAL-REQUIRED`.

## G-R14-06 — source-use/depletion coordinate

**Gap:** whether run index, cumulative growth time, extracted layer mass fraction or another state best predicts source drift.

**Closure:** sequential reuse experiment with full P03/P06 records and model comparison.

**Status:** `EMPIRICAL-REQUIRED`.

## G-R14-07 — P06 material state to detector spectral response

**Gap:** production-relevant

`partial lambda_det/partial {x_opt,d,composition_gradient,edge_metric}`

under a frozen detector process and explicit cutoff convention.

**Why unresolved:** Hansen `lambda_Eg(x,T)` is not detector-response cutoff and the historical RP-01 cutoff convention is not fully closed.

**Closure:** matched wafer/die P06-to-P11 campaign under P21 Stage 4/downstream confirmation.

**Status:** `EMPIRICAL-REQUIRED`.

## G-R14-08 — spectral requirement itself

**Gap:** numerical allowed detector spectral-response variation around the reproduction target.

**Why needed:** a Jacobian cannot be converted into a process tolerance until the protected output has a numerical allowable deviation/uncertainty.

**Closure:** define the RP-01 reproduction/system spectral requirement in P19/P20 terms, including cutoff convention and operating temperature.

**Status:** `LOCAL-SPEC-OPEN`.

## G-R14-09 — robust LPE center

**Gap:** local operating point that simultaneously centers thickness/composition while minimizing sensitivity and staying inside acceptable morphology/yield region.

**Closure:** validated P21 response surface + holdout confirmation + downstream detector correlation.

**Status:** `EMPIRICAL-REQUIRED`.

## G-R14-10 — backward allocation into apparatus tolerances

**Gap:** numerical requirements for:

- balance/delivered mass;
- liquidus/temperature measurement;
- contact timing;
- melt depth/inventory;
- source-use limit;
- Hg-loss control.

**Closure:** only after G-R14-01 through G-R14-08 are sufficiently closed, propagate the verified Jacobian and covariance through P20 and then promote justified limits into P17.

**Status:** `LOCAL-SPEC-OPEN`.

## Round-14 priority order

1. qualify metrology and independent center-run variance;
2. Stage 1 source/phase perturbations;
3. Stage 2 supercooling/time perturbations;
4. Stage 3 finite-liquid/source-use perturbations;
5. holdout confirmation;
6. matched P06/P11 spectral bridge;
7. P20 backward allocation;
8. P17 capability only after a numerical specification exists.
