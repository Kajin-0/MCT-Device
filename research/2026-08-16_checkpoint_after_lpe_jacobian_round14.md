# Recovery checkpoint — round 14 P03/P06 LPE Jacobian

**Date:** 2026-08-16 America/New_York

**Purpose:** Fast handoff after formalizing the first high-value empirical Jacobian under P20.

Read after `AGENTS.md` and the round-13 checkpoint.

---

## 1. New files

Round 14 adds:

- `calculations/RP01_LPE_TO_SPECTRAL_JACOBIAN_FRAMEWORK.md`
- `procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`
- `travelers/P21_LPE_JACOBIAN_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND14.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND14.md`
- this checkpoint.

No new historical RP-01/Honeywell process setpoint is claimed.

---

## 2. P21 purpose

P21 is the first dedicated empirical-Jacobian module under P20.

It identifies the local mapping

`{xL,yL,TL_actual,DeltaT_SC,t_contact,melt geometry/inventory,source-use,Hg-loss state}`

into

`{x_opt,thickness,spatial uniformity,optical edge,morphology}`.

The detector spectral bridge is then built from matched P06/P11 data:

`{x_opt,d,gradient,edge metric} -> {lambda_det,R_v(lambda),edge slope}`.

Ultimate chain:

`J_detector,process = J_detector,material * J_material,process`.

This is the missing object needed to derive balance, temperature, timing and melt-inventory requirements from detector performance.

---

## 3. Honeywell tie-line derivative warning strengthened quantitatively

Bowers-Schmit US4317689 gives around the candidate row:

- xL=.095,yL=.820,TL=508 C -> xS=.37;
- xL=.082,yL=.810,TL=507 C -> xS=.29;
- xL=.060,yL=.800,TL=510 C -> xS=.22.

Directional secants around the xL=.082 row are:

- upper side: `Delta xS/Delta xL = 6.154`;
- lower side: `3.182`;
- across both adjacent rows: `4.286`.

Candidate-row tabulated ratio:

`xS/xL=3.54`.

The secants are **not partial derivatives** because yL and TL also change.

New continuity rule:

**Do not use xS/xL=3.54 as dxS/dxL. Do not use adjacent tie-line secants as independent partial derivatives.**

Their spread is only diagnostic evidence that the required local thermodynamic response is multivariable/nonlinear.

---

## 4. Actual supercooling covariance

P21/P03E use

`DeltaT_SC = TL_actual - T_contact`.

Therefore

`var(DeltaT_SC) = var(TL_actual) + var(T_contact) - 2 cov(TL_actual,T_contact)`.

Do not blindly RSS the two thermal terms if source state, furnace placement or common calibration couples them.

Material derivatives with respect to supercooling remain empirical.

---

## 5. Finite-liquid state made explicit

Sanz-Maudes et al. 1990 directly model Te-rich slider HgCdTe LPE with finite liquid dimensions and Hg loss and show that after a characteristic time related to liquid thickness, growth rate decreases; Hg loss can drive the grown layer Cd-richer.

Round 14 introduces a model-conditioning coordinate:

`Fo_L = D_eff t_contact / h_liquid^2`.

Equivalent:

`ell_D/h_liquid = sqrt(Fo_L)`.

Use:

- compare time and liquid depth on a physical basis;
- detect when finite-reservoir behavior may become important;
- support transfer between different melt depths only after D_eff/model validation.

Restriction:

`Fo_L=1` is **not** a released threshold. The coefficient/regime transition is apparatus/model dependent.

---

## 6. Source extraction and Hg loss separated

New bookkeeping coordinate:

`epsilon_m = m_epilayer / M_liquid,initial`.

This normalizes solid extraction to source inventory but does not predict depletion by itself.

Separate Hg-loss coordinate:

`f_Hg = N_Hg,lost / N_Hg,initial`

where measurable/calibrated.

Continuity rule:

**Do not conflate source-use index, solute extraction and Hg loss.** They can all drift with run order but represent different physical mechanisms.

---

## 7. No universal growth-time law

Round 14 explicitly rejects pre-imposing one global relationship such as

- d proportional t;
- d proportional sqrt(t);
- d proportional t^(3/2)

for RP-01.

Finite-liquid HgCdTe theory supports diffusion-dominated short-time behavior under appropriate conditions, but long-time finite-reservoir and Hg-loss effects alter the response.

The production quantity is the measured local derivative

`partial d/partial t_contact`

at the selected process center and thermal mode.

---

## 8. Sequential DOE architecture

P21 avoids an expensive/unidentifiable giant factorial.

### Stage 0

Qualify:

- P06 repeatability;
- balance/delivered-mass uncertainty;
- TL_actual method;
- melt geometry/depth;
- independent nominal-center run variance.

### Stage 1 — source/phase block

Perturb:

`{xL,yL,DeltaT_SC}`.

Responses:

`{x_opt,d,edge,morphology,TL_actual}`.

### Stage 2 — kinetic block

Perturb:

`{DeltaT_SC,t_contact}`.

Estimate local thickness/composition derivatives and interaction.

### Stage 3 — finite-reservoir/source-history block

Perturb:

`{h_liquid or inventory coordinate, source-use/depletion state}`.

Track Hg-loss state separately.

### Stage 4 — holdout confirmation

Use combinations not included in fitting. Jacobian remains preliminary until prediction residuals are consistent with declared uncertainty.

---

## 9. Identifiability / collinearity rule

P21 requires design-matrix rank/conditioning and coefficient-covariance checks.

Natural couplings include:

- weighing changes xL and yL together;
- source state changes TL_actual;
- melt mass changes liquid depth and thermal lag;
- run order changes depletion and thermal history;
- Hg loss changes composition and liquidus.

Do not report regression coefficients as physical partial derivatives unless the DOE independently identifies them.

If factors cannot be separated experimentally, control a validated combined state variable instead.

---

## 10. Morphology defines the feasible region

P21 treats morphology/yield as a hard feasibility constraint.

A process point that centers x and 9.5-um thickness but causes secondary nucleation, rough growth, severe terracing, residual melt or wipe-off failure is not a valid optimum.

Define

`Omega_feasible = {process states that pass morphology/yield gates}`.

Sensitivity/tolerance allocation must remain inside this region.

---

## 11. Robust-center concept

After a response surface exists, select a center that:

- reaches the required material/spectral state;
- has acceptable morphology/yield;
- minimizes local sensitivity to realistic process covariance where possible.

P21 gives a candidate design objective

`J_robust = trace(W J Sigma_u J^T) + morphology_penalty`.

This is a local engineering objective, not a historical RP-01 criterion.

---

## 12. P06-to-P11 bridge remains the key downstream closure

P21 cannot convert x/thickness process derivatives into detector cutoff tolerances until matched wafer/die data establish

`lambda_det = F(x_opt,d,composition_gradient,edge_metric,...)`

under a fixed downstream detector process and explicit cutoff convention.

Do not substitute Hansen lambda_Eg for this bridge.

---

## 13. Round-14 open gaps

See `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND14.md`.

Highest priority:

1. local xL/yL/supercooling derivatives;
2. local growth-time derivative;
3. finite-liquid/source-use response;
4. Hg-loss response;
5. P06 material -> P11 detector spectral bridge;
6. define numeric detector spectral acceptance band;
7. only then allocate balance/T/time/inventory tolerances through P20;
8. only then move limits to P17 capability.

---

## 14. Sources added/re-emphasized

See `docs/SOURCE_LEDGER_ADDENDUM_ROUND14.md`.

Main sources:

- Bowers-Schmit US4317689 same-family Honeywell tie-line/process logic;
- Sanz-Maudes et al. 1990 finite-liquid/Hg-loss HgCdTe LPE model;
- Harman 1980 Te-rich phase/growth study;
- Jovic et al. 1994 x<=.3 Te-rich composition-profile model.

---

## 15. Next logical work

The next strongest theoretical/analytical branch is **P21 experimental-design numerics before fabrication**:

1. construct a synthetic/coded DOE matrix for Stages 1-3;
2. test identifiability/condition numbers under realistic factor coupling;
3. derive how many independent growth runs are needed to resolve a specified derivative relative to P06/run variance as a function of effect size;
4. define a Fisher-information / D-optimal-style criterion for selecting the most informative growths;
5. keep all absolute perturbation magnitudes OPEN until apparatus capability and safe same-regime bounds are known.

This can be completed analytically without performing a physical experiment and will make future growth campaigns far more information-efficient.
