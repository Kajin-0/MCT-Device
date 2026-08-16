# RP-01 LPE-to-spectral Jacobian framework

**Status:** CONTROLLED DERIVED / EMPIRICAL-JACOBIAN DESIGN  
**Date:** 2026-08-16 America/New_York

## Purpose

Define the quantitative bridge needed to propagate an RP-01 detector spectral requirement backward into Te-rich LPE source composition, actual liquidus, supercooling, growth time, finite melt inventory, source-use state, Hg-loss state and metrology requirements.

This calculation supplements P03B/P03C/P03D/P03E, P06 and P20. It does **not** release production tolerances.

---

## 1. Controlled process and material vectors

Use the upstream process/state vector

`u = {xL, yL, TL_actual, DeltaT_SC, t_contact, T(t), h_liquid, M_liquid, source_use, Hg_loss_state, substrate_state, wipeoff_state}`

and the first material-output vector

`m = {x_opt_mean, x_gradient, sigma_x, d_mean, sigma_d, edge_metric, morphology, usable_area}`.

The local P03/P06 Jacobian is

`J_m,u = partial m / partial u`.

The detector spectral-response vector is then

`r = {lambda_det_metric, edge_slope, R_v(lambda), spectral_uniformity}`

and the P06/P11 bridge is

`J_r,m = partial r / partial m`.

The production-relevant chain is

`J_r,u = J_r,m J_m,u`.

This is the quantity P20 ultimately needs for backward requirements allocation.

---

## 2. Honeywell tie-line table: what can and cannot be differentiated

Bowers-Schmit U.S. Patent 4,317,689 reports five Te-rich source/solid tie-line points:

| xL | yL | TL (C) | xS | xS/xL |
|---:|---:|---:|---:|---:|
| 0.100 | 0.825 | 508 | 0.40 | 4.00 |
| 0.095 | 0.820 | 508 | 0.37 | 3.89 |
| 0.082 | 0.810 | 507 | 0.29 | 3.54 |
| 0.060 | 0.800 | 510 | 0.22 | 3.67 |
| 0.050 | 0.800 | 499 | 0.195 | 3.90 |

The RP-01 candidate anchor is

`xL=.082, yL=.810, TL=507 C -> xS=.29`.

### 2.1 Directional secants around the candidate row

Using adjacent table rows only as an empirical directional diagnostic:

Upper-side secant:

`(0.37-0.29)/(0.095-0.082) = 6.154`

Lower-side secant:

`(0.29-0.22)/(0.082-0.060) = 3.182`

Central adjacent-row secant:

`(0.37-0.22)/(0.095-0.060) = 4.286`.

These differ materially from the tabulated ratio

`xS/xL = 3.54`.

### 2.2 Interpretation

These numbers are **not** `partial xS/partial xL` because the adjacent table rows simultaneously change:

- `xL`;
- `yL`;
- liquidus temperature;
- equilibrium solid composition.

They are directional slopes along a sparse historical tie-line manifold.

The spread `3.18 to 6.15` is itself useful evidence that the ratio `xS/xL=3.54` cannot be promoted to a local differential transfer coefficient.

**Evidence class:** `PROXY-CONDITIONAL`.

---

## 3. Required thermodynamic partials

The local source/phase-equilibrium block needs, at minimum,

`partial xS/partial xL | yL,T,state`

`partial xS/partial yL | xL,T,state`

`partial xS/partial T | xL,yL,state`

plus interaction terms if the local response is measurably nonlinear.

The historical five-row table does not identify these independent partial derivatives.

P03E is therefore correct to forbid deriving a universal `dx/dT` from the table.

The required data must come from local controlled perturbations or a validated ternary phase-equilibrium model independently verified against local P06 composition.

---

## 4. Supercooling must be referenced to the actual liquidus

Define

`DeltaT_SC = TL_actual - T_contact`.

Therefore a perturbation of nominal furnace temperature does not map cleanly into supercooling unless the actual melt liquidus and sensor-to-melt offset are known.

For first-order propagation,

`delta(DeltaT_SC) = delta(TL_actual) - delta(T_contact)`.

Thus the variance is

`var(DeltaT_SC) = var(TL_actual) + var(T_contact) - 2 cov(TL_actual,T_contact)`.

Do not RSS the two terms independently when they share calibration, furnace-position or source-state effects.

**Evidence class:** `IDENTITY` for the definition and covariance propagation; material response to `DeltaT_SC` remains `EMPIRICAL-REQUIRED`.

---

## 5. Finite-liquid dimensionless state

The 1990 Sanz-Maudes et al. diffusion-based HgCdTe LPE model explicitly shows that, after a characteristic time related to liquid thickness, finite-reservoir depletion reduces growth rate; Hg loss can also drive the grown solid toward higher Cd composition.

A useful local dimensionless classifier is the diffusion Fourier number

`Fo_L = D_eff t_contact / h_liquid^2`

where

- `D_eff` is an effective solute-diffusion coefficient appropriate to the locally validated model;
- `h_liquid` is the effective mass-transfer liquid depth;
- `t_contact` is growth contact time.

Interpretation:

- small `Fo_L`: the diffusion length is small relative to liquid depth and the remote liquid boundary is less influential;
- order-unity/larger `Fo_L`: finite-liquid geometry can become increasingly important.

The threshold coefficient is apparatus/model dependent. Do **not** define a release threshold at `Fo_L=1` without validation.

**Evidence class:** `MODEL-CONDITIONAL`.

### 5.1 Equivalent diffusion-length form

`ell_D = sqrt(D_eff t_contact)`

and

`ell_D/h_liquid = sqrt(Fo_L)`.

This gives P03D a physically interpretable way to compare growth time and melt depth rather than controlling gram mass alone.

---

## 6. Material-extraction loading

Define the exact bookkeeping ratio

`epsilon_m = m_epilayer / M_liquid,initial`.

If direct layer mass is not measurable, a geometric estimate can be formed only with a stated solid density model:

`m_epilayer = rho_s A_grown d_mean`.

Then

`epsilon_m = rho_s A_grown d_mean / M_liquid,initial`.

This ratio does not predict depletion by itself, but it provides a normalized source-loading coordinate for comparing differently sized boats/substrates.

**Evidence class:** `IDENTITY` for the ratio; any mapping `epsilon_m -> x,d` is `EMPIRICAL-REQUIRED`.

---

## 7. Hg-loss state variable

Use a cumulative fractional Hg-inventory loss where measurable:

`f_Hg = N_Hg,lost / N_Hg,initial`.

If an independently validated molar Hg-loss flux `J_Hg(t)` and free-surface area `A_free` are available,

`N_Hg,lost = integral J_Hg(t) A_free dt`.

The finite-melt literature establishes that Hg loss and finite liquid dimensions are coupled process drivers, but the local derivative

`partial xS/partial f_Hg`

must be measured or computed with a validated local transport/thermodynamic model.

Do not use auxiliary-Hg-source mass alone as the Hg-loss state unless its transfer relationship to the growth liquid has been calibrated.

---

## 8. Time dependence: no universal power law is released

The finite-liquid HgCdTe model reports short-time behavior consistent with diffusion-limited LPE theory in the no-Hg-leak case, but finite-liquid effects alter the long-time response.

Therefore P03B shall not globally impose one of

- `d proportional t`;
- `d proportional sqrt(t)`;
- `d proportional t^(3/2)`

without local evidence for the selected thermal mode and time window.

Instead fit candidate physically plausible local models and test residuals. The production derivative is the measured local

`partial d/partial t_contact`

at the selected process center.

---

## 9. Local response-surface parameterization

A practical second-order local model around centered variables may be written

`m_k = beta0 + sum_i beta_i z_i + sum_i beta_ii z_i^2 + sum_(i<j) beta_ij z_i z_j + error`

for each material output `m_k`, where `z_i` are centered/scaled local process variables.

The Jacobian at the process center is then the vector of first-order coefficients after conversion back to engineering units.

Candidate primary factors for the first identified block:

- actual `xL`;
- actual `yL`;
- corrected/local `DeltaT_SC`;
- contact time;
- effective liquid depth or inventory;
- source-use/run index or an equivalent continuous depletion coordinate.

Thermal trajectory should be frozen to one mode during the first local Jacobian campaign; step, ramp and combined trajectories should not be pooled into one model.

---

## 10. Sequential identification strategy

A full six-factor high-order DOE is unnecessarily expensive before screening interactions.

### Block A — source/phase state

Hold geometry/time/trajectory fixed and perturb:

`{xL, yL, DeltaT_SC}`

Measure:

`{x_opt_mean, edge_metric, d_mean, morphology}`.

Goal: identify the local thermodynamic/compositional response and interactions.

### Block B — kinetic thickness state

At the selected source composition, perturb:

`{DeltaT_SC, t_contact}`

Measure full P06 maps.

Goal: obtain

`partial d/partial t`, `partial d/partial DeltaT`, `partial x/partial t`, `partial x/partial DeltaT`

and their interaction.

### Block C — finite reservoir/source history

At the centered source/thermal/time condition, perturb:

`{h_liquid or M_liquid, source-use/depletion state}`.

Measure:

`{d,x,spatial gradients,morphology,TL_actual}`.

Goal: identify finite-liquid and source-history drift separately from nominal recipe variation.

### Block D — confirmation

Run holdout combinations near the predicted robust center. Do not use all confirmation runs in model fitting.

---

## 11. Center-point replication and variance separation

The Jacobian campaign must contain independent repeated center runs, not merely repeated P06 map points on one wafer.

Separate:

`P06 measurement repeatability`

from

`within-wafer spatial variation`

from

`independent LPE run-to-run variation`.

A derivative whose perturbation effect is not resolved above the combined measurement/run noise shall remain `UNRESOLVED`; do not report a numerically precise near-zero slope.

---

## 12. P06 material-to-detector spectral bridge

The missing detector-relevant relation is not simply Hansen `lambda_Eg(x)`.

Build an empirical/validated-model bridge using matched material and detector coordinates:

`lambda_det = F(x_opt, d, composition_gradient, edge_metric, detector_process, T_detector, cutoff_convention)`.

Required controls:

- same P06 model/version;
- same detector cutoff convention;
- same detector temperature;
- same downstream process branch;
- mapped die position back to the P06 wafer coordinate;
- preserve composition gradient/thickness rather than reducing every wafer to one scalar x.

The first production-relevant spectral derivative is

`partial lambda_det / partial x_opt`

conditional on thickness/gradient/process state.

A more complete local row is

`delta lambda_det ≈ J_x delta x_opt + J_d delta d + J_g delta gradient + ...`.

---

## 13. Backward tolerance allocation after the Jacobian exists

If the final allowed spectral variation is `u_lambda`, and the local chain `J_lambda,u` has been verified, then

`u_lambda^2 ≈ J_lambda,u Sigma_u J_lambda,u^T + u_model^2 + u_measurement^2`

within the linearized region.

Only then may P20 allocate contributions to:

- charge weighing/composition;
- liquidus/temperature metrology;
- contact timing;
- melt geometry/inventory;
- source-use/Hg-loss state.

A balance requirement is therefore an **output** of the completed chain, not an input assumption.

---

## 14. Current strongest conclusions

1. The historical `xS/xL=3.54` ratio is demonstrably not a reliable local differential; adjacent historical directional secants span about `3.18-6.15` while yL and TL also change.
2. The dominant missing information is a multivariable local Jacobian, not another isolated literature setpoint.
3. Effective liquid depth must enter the state explicitly because finite-liquid effects have a characteristic time tied to liquid dimensions.
4. Hg-loss state must be separated from solute extraction/source-use state.
5. P06 spatial composition, thickness and edge descriptors are the immediate response variables; detector cutoff enters only in the later matched P06/P11 bridge.
6. No source-composition, temperature, timing, melt-mass or balance tolerance is released by this file.

---

## References

1. J. E. Bowers and J. L. Schmit, U.S. Patent 4,317,689, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution” (1982).
2. J. Sanz-Maudes, J. Sangrador, T. Rodriguez, A. Pernichi, C. Gonzalez, “Numerical simulation of the growth of HgCdTe layers by liquid phase epitaxy from Te-rich solutions: The effect of liquid dimensions and mercury loss,” *Journal of Crystal Growth* 106, 303-317 (1990), DOI `10.1016/0022-0248(90)90076-W`.
3. T. C. Harman, Te-rich Hg-Cd-Te liquidus/solidus and horizontal-slider LPE study, *Journal of Electronic Materials* 9 (1980), DOI `10.1007/BF02822728`.
4. P03B/P03C/P03D/P03E, P06 and P20 in this repository.
