# P23 Hg-anneal state-boundary / Jacobian qualification register

**Status:** BLANK CONTROLLED DEVELOPMENT REGISTER  
**Procedure:** `procedures/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_QUALIFICATION.md`

Use one register per anneal-mapping campaign/model version.

---

## A. Campaign identity

- campaign ID:
- date range:
- operator/researcher:
- P03 growth branch / wafer set:
- P04/P04A/P04B recipe family:
- anneal apparatus ID/revision:
- ampoule/chamber/enclosure ID:
- Hg-source architecture:
- P05 method version:
- P06 method/model version:
- P13 method version where used:
- P20 allocation record link:
- P22 design record link:

---

## B. Scientific objective

- protected detector/material output:
- carrier-state objective:
- optical/morphology constraints:
- intended local process center:
- evidence class at campaign start:
- explicit quantities that remain OPEN:

---

## C. Factor / trajectory descriptor table

| Variable | Physical definition | Coded variable | Center | Half-range | Units | Measurement/reconstruction method | Uncertainty | Status |
|---|---|---|---:|---:|---|---|---|---|
| sample dwell T | | | | | | | | |
| dwell time | | | | | | | | |
| Hg-source T | | | | | | | | |
| pHg / muHg proxy | | | | | | | | |
| cooldown descriptor 1 | | | | | | | | |
| cooldown descriptor 2 | | | | | | | | |
| initial Hall state | | | | | | | | |
| initial optical x/edge | | | | | | | | |
| epilayer thickness | | | | | | | | |
| other | | | | | | | | |

Do not assign coded levels to vague labels such as `slow` or `Hg rich` without the physical trace/proxy above.

---

## D. Metrology qualification

### Thermometry

- sample sensor ID/calibration:
- Hg-source sensor ID/calibration:
- sample-to-controller lag model:
- source-to-controller lag model:
- spatial gradient evidence:
- trajectory timestamp synchronization:

### Hg chemical potential / pressure

- source material/lot:
- source geometry:
- pressure measurement or reconstruction:
- vapor-pressure/model source/version:
- source depletion evidence:
- uncertainty:

### P05

- zero-field reciprocity/current reversal:
- field calibration:
- field sweep:
- Hall slope repeatability:
- multicarrier escalation capability:
- measurement-temperature set:

### P06

- edge repeatability:
- x-fit repeatability:
- thickness repeatability:
- matched-coordinate registration:

---

## E. Pre-anneal sample state

| Sample | Wafer/run | Coordinate | x/edge | Thickness | Hall state/class | R_s | n_H/p_H if valid | mu_H if valid | Surface/passivation | Prior thermal history |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

---

## F. Anneal-run matrix

| Run | Sample | Coded factors | T_s(t) trace ID | T_Hg(t) trace ID | pHg/proxy trace ID | Dwell | Cooldown ID | Pre-state class | Post-state class | P05 validity | P06 preservation | Inclusion/disposition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

---

## G. Transport-state classification

For every run record:

- measurement temperature:
- declared low-field fit range:
- signed Hall slope/coefficient:
- standard/expanded uncertainty:
- confidence interval includes zero?:
- Hall curvature metric:
- magnetoresistance metric:
- sign change with B?:
- sign change with T?:
- P05 single-carrier gates pass?:
- assigned class: `N-LIKE` / `P-LIKE` / `TRANSITION-MULTICARRIER`:
- classification comments:

**Do not use reciprocal Hall density as the boundary response.**

---

## H. State-boundary model

- signed boundary response `g(a)`:
- model/classifier family:
- predictor variables:
- training runs:
- excluded runs/reasons:
- boundary equation/representation:
- transition-zone definition:
- classification uncertainty:
- cross-validation/holdout result:
- current evidence state:

### Boundary-normal sensitivity

- `grad g` at candidate center:
- process covariance `Sigma_a` version:
- `u_g^2 = grad(g)^T Sigma_a grad(g)` result:
- model/classification uncertainty contribution:
- estimated margin of candidate center to transition zone:
- status: OPEN / PRELIMINARY / VERIFIED:

---

## I. Local n-like Jacobian

Complete only for runs wholly inside a verified n-like region.

| Output | Input | Process center | Derivative | Units | SE/CI | Local valid range | Model version | Holdout verified? | Evidence state |
|---|---|---|---:|---|---|---|---|---|---|
| log10(n_H) | T_dwell | | | | | | | | |
| log10(n_H) | t_dwell | | | | | | | | |
| log10(n_H) | pHg/muHg | | | | | | | | |
| log10(n_H) | cooldown descriptor | | | | | | | | |
| mu_H | T_dwell | | | | | | | | |
| mu_H | t_dwell | | | | | | | | |
| mu_H | pHg/muHg | | | | | | | | |
| mu_H | cooldown descriptor | | | | | | | | |
| optical edge | anneal factor | | | | | | | | |
| tau_eff | annealed state | | | | | | | | |

---

## J. Diffusion/relaxation diagnostics

### Diffusion exposure

- diffusivity model/source/version:
- evidence class:
- relevant thickness `L` and basis:
- boundary-condition assumption:
- `Theta_D,ramp`:
- `Theta_D,dwell`:
- `Theta_D,cool`:
- `Theta_D,total`:
- `f_cool,D`:
- holdout prediction result:

### First-order relaxation model

For each fitted response:

| Response | y0 | y_eq | tau_y | Conditions | Fit residual | Holdout result | Interpretation restriction |
|---|---:|---:|---:|---|---|---|---|
| | | | | | | | |

Do not force one common `tau` for Hall density, mobility, optical state and lifetime.

---

## K. Optical/morphology feasible region

- allowed pre/post edge shift:
- allowed x-fit shift:
- allowed thickness shift:
- morphology/interface gates:
- void/precipitate/dislocation observations:
- feasible-region model `Omega_A`:
- runs excluded by optical/morphology boundary:

Numerical limits remain OPEN unless traced to P19/P20 requirements.

---

## L. Detector bridge

For selected annealed material:

| Material state ID | n_H / multicarrier state | mu_H | P06 edge/x | tau_eff | Responsivity | Noise | D* | Device process version | Result |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

- detector-performance model version:
- evidence that material target is detector-optimal/reproduction-compatible:
- historical RP-01 reference comparison:

---

## M. Holdout confirmation

| Holdout run | Predicted class | Observed class | Predicted continuous outputs | Observed outputs | Within prediction uncertainty? | Disposition |
|---|---|---|---|---|---|---|
| | | | | | | |

---

## N. Specification-allocation handoff

- final detector/material requirement:
- local n-like center:
- state-boundary margin constraint:
- local Jacobian version:
- covariance version:
- P20 allocated process tolerance candidate:
- optical/morphology constraint:
- tighter constraint:
- P17 handoff status:

No tolerance is released by this register alone.

---

## O. Failure / negative-result preservation

For every failed or excluded sample record:

- run/sample ID:
- observed signature:
- candidate mechanisms:
- discriminating tests:
- confirmed cause if known:
- whether failure marks state boundary / morphology boundary / apparatus failure / metrology failure:
- P18 record link:

---

## P. Campaign conclusion

- boundary model status:
- n-like Jacobian status:
- cooldown-model status:
- initial-state dependence status:
- detector bridge status:
- remaining OPEN items:
- next highest-information action:
- reviewer/date:
