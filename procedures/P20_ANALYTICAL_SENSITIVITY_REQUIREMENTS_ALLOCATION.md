# P20 — analytical sensitivity / numerical requirements allocation

**Status:** CONTROLLED SYSTEM-INTEGRATION / PRE-SPECIFICATION METHOD  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert P19 detector-level requirements into defensible intermediate numerical specifications without inventing tolerances from historical values or observed process spread.

P20 sits between:

- P19 requirements/physics/process traceability;
- the P01–P16 fabrication and measurement modules;
- P17 statistical process release/capability;
- P18 failure analysis.

The controlled chain is:

`detector requirement -> output definition -> analytical/model sensitivity -> empirical missing Jacobian -> uncertainty/tolerance allocation -> local verification -> P17 specification/capability`.

P20 does **not** authorize a production limit merely because a derivative can be calculated.

---

## 2. Why this module is required

The repository now contains many historical anchors and local qualification variables, but most numerical tolerance bands remain `LOCAL-SPEC-OPEN`.

Two failure modes must be prevented:

1. assigning a narrow process tolerance because a historical paper used one nominal value;
2. assigning a broad process tolerance because current process data happen to have a broad spread.

The correct sequence is the opposite:

1. state the detector/system requirement;
2. determine how intermediate quantities affect that requirement;
3. allocate an allowable error/variation budget;
4. determine whether the process and metrology are capable of meeting it.

P17 begins only after steps 1–3 are technically defensible.

---

## 3. Sensitivity evidence classes

Every numerical process/performance sensitivity shall be tagged as one of:

### `IDENTITY`

Exact derivative of a controlled definition or algebraic relation.

Examples:

- `D*=R_v sqrt(A)/e_n`;
- `NEP=e_n/R_v`;
- `f_3dB=1/(2 pi tau)` for a model already validated as one pole.

### `MODEL-CONDITIONAL`

Exact derivative inside a stated physical model whose adequacy must be tested.

Examples:

- Hansen `x,T -> Eg -> lambda_Eg`;
- one-carrier rectangular resistance/current;
- Planck filled-cone background model;
- single-pass `1-exp(-alpha d)` absorption.

### `PROXY-CONDITIONAL`

Useful order-of-magnitude chain containing at least one approximation not demonstrated as the required local differential.

Examples:

- using the tie-line ratio `xS/xL=3.54` as `dxS/dxL`;
- converting Hansen `lambda_Eg` sensitivity into detector-cutoff sensitivity.

A proxy may size a DOE or instrument but shall not define a production specification.

### `EMPIRICAL-REQUIRED`

The derivative is process/apparatus/device specific or the physics is too coupled for a defensible scalar analytical derivative.

Examples:

- anneal cooldown -> final Hall/lifetime state;
- RIE converted profile -> minority-carrier sweepout/D*;
- sidewall passivation -> 1/f and lifetime;
- LPE supercooling/time/inventory -> x/thickness/morphology.

---

## 4. Mathematical framework

Let the detector/performance output vector be

`y = {lambda_edge, R_v, e_n, NEP, D*, f_3dB, tau_eff, R_device, P_J, DeltaT, yield metrics, ...}`

and the intermediate/process variable vector be

`x = {x,d,n,mu,E,L,W,A,tau_eff,Ns,dconv,Sc,rho_c,TL,DeltaT_SC,t_growth,pHg,...}`.

The local dimensional Jacobian is

`J_ij = partial y_i / partial x_j`.

The normalized sensitivity matrix is

`S_ij = partial ln(y_i) / partial ln(x_j)`

where both variables are nonzero and logarithmic scaling is meaningful.

For small perturbations,

`delta y ≈ J delta x`.

For a covariance matrix `Sigma_x`, first-order output covariance is

`Sigma_y ≈ J Sigma_x J^T`.

A diagonal/RSS treatment may be used only after independence is justified.

---

## 5. Do not compare raw derivatives without normalization

A dimensional derivative such as

`partial lambda/partial x = -33 um per composition unit`

cannot be ranked directly against

`partial ln Phi/partial T = 0.040/K`.

Use normalized sensitivities for relative leverage, but preserve dimensional derivatives for engineering tolerance conversion.

Even normalized sensitivity is not a complete priority metric. Actual contribution depends on the current/achievable relative uncertainty or process variation.

Define an uncertainty-weighted contribution where appropriate:

`C_ij = |S_ij| (u_xj/x_j)`.

A process with a large sensitivity but negligible actual variation may contribute less than a modest-sensitivity process with poor control.

---

# 6. Initial controlled analytical matrix

The detailed derivation is in

`calculations/RP01_FIRST_ORDER_SENSITIVITY_MATRIX.md`.

Core currently established entries are summarized below.

| Output | Input | Local normalized sensitivity | Evidence |
|---|---|---:|---|
| `D*` | `R_v` | `+1` | IDENTITY |
| `D*` | `e_n` | `-1` | IDENTITY |
| `D*` | `A` | `+0.5` | IDENTITY |
| `NEP` | `e_n` | `+1` | IDENTITY |
| `NEP` | `R_v` | `-1` | IDENTITY |
| `R_bulk` | `L` | `+1` | MODEL-CONDITIONAL |
| `R_bulk` | `n,mu,W,d` | `-1` each | MODEL-CONDITIONAL |
| `P_J` | `E` | `+2` | MODEL-CONDITIONAL |
| `P_J` | `n,mu,W,d,L` | `+1` each | MODEL-CONDITIONAL |
| `lambda_Eg` at x=.30/80K | `x` | `-1.949` | MODEL-CONDITIONAL Hansen |
| `lambda_Eg` at x=.30/80K | `T` | `-0.0703` | MODEL-CONDITIONAL Hansen |
| `f_3dB` | `tau` | `-1` | IDENTITY after one-pole validation |
| `n_conv=Ns/dconv` | `Ns` | `+1` | IDENTITY under uniform-layer representation |
| `n_conv=Ns/dconv` | `dconv` | `-1` | IDENTITY under uniform-layer representation |
| ideal 300K in-band background | blackbody `T` | `+12.08` | MODEL-CONDITIONAL |
| ideal 300K in-band background | effective step `lambda_c` | `+9.08` | MODEL-CONDITIONAL |
| ideal 60-degree cone background | cone angle | `+1.814` | MODEL-CONDITIONAL |

The high blackbody sensitivities are a radiometry warning, not fabrication sensitivities. They show why physical aperture geometry and measured spectral weighting must replace a scalar FOV/cutoff approximation for precision BLIP verification.

---

# 7. Current detector-level benchmark vector

For RP-01 comparison, the historical benchmark condition remains:

- detector type: n-type MWIR HgCdTe photoconductor;
- `T≈80 K`;
- `E≈10 V/cm` for the canonical spectral/noise condition;
- `lambda≈4 um` for the quoted D* point;
- measured detector response cutoff approximately `4.4 um`, convention not fully closed;
- chopping/signal frequency `1 kHz`;
- stated FOV `60 degrees`, provisionally interpreted as full cone;
- `D*≈2e11 cm sqrt(Hz)/W` at 4 um;
- historical `1/f` knee about 3 kHz;
- high-frequency g-r level about 24.5 nV/sqrt(Hz).

These are `HISTORICAL-REFERENCE` values, not tolerance bands.

A numerical specification band around any one of these must be defined by a user/system requirement or an explicit reproduction objective before P20 can allocate tolerances backward.

---

# 8. Requirement allocation workflow

## Step 1 — freeze the final requirement and operating condition

For every allocation record state:

- metric;
- target;
- allowed deviation or uncertainty;
- wavelength;
- frequency;
- electric field;
- temperature;
- background/FOV;
- geometry/area convention;
- maturity class.

Example of a complete requirement statement:

`D*(4 um,1 kHz,80 K,10 V/cm,defined background,measured A) >= target`

not merely

`D* high`.

If the system-level allowed variation is unknown, the allocation remains open.

## Step 2 — define the measurement equation

Write the exact equation connecting measured intermediate quantities to the final metric.

For D*:

`D* = R_v(lambda,f,E,T) sqrt(A) / e_n(f,E,T)`.

The exact same operating condition is part of the equation.

## Step 3 — populate `IDENTITY` derivatives

These require no fabrication data and should be entered first.

For D* this immediately establishes direct leverage of responsivity, noise and area.

## Step 4 — populate justified `MODEL-CONDITIONAL` derivatives

Examples:

- Hansen composition sensitivity;
- one-pole frequency response;
- ideal one-carrier DC electrical model;
- Planck background model.

Every model entry must state:

- equation;
- valid domain;
- operating point;
- calibration/model uncertainty;
- known model mismatch.

## Step 5 — identify the missing empirical Jacobian

Do not fill a blank derivative with a handbook guess.

Create a local DOE/model plan instead.

Examples:

`{xL,yL,TL,DeltaT_SC,t} -> {x,d}`

`{T_dwell,t,pHg,cooldown} -> {n,mu,tau}`

`{Ns,dconv,Lconv,damage} -> {R_v,e_n,tau_eff,D*}`.

## Step 6 — allocate a requirement budget

For a small bounded worst-case budget:

`sum_i |S_i| b_i <= b_y`.

For independent standard uncertainties:

`u_y^2 ≈ J Sigma J^T`.

Use covariance explicitly when variables are coupled, e.g.:

- n and mu from the same Hall reduction;
- width/gap/area from the same image calibration;
- source composition and actual liquidus;
- anneal temperature and Hg pressure;
- responsivity/noise drift with detector temperature.

## Step 7 — compare allocated need with metrology/process capability

For each proposed intermediate requirement determine:

- measurement uncertainty;
- current process spread;
- expected control authority;
- sample cost/destructiveness;
- whether a process output can be corrected/reworked.

If metrology uncertainty consumes a large fraction of the allocated band, improve metrology before evaluating capability.

## Step 8 — verify the sensitivity experimentally

A calculated local derivative becomes a release basis only after the relevant operating region is verified.

Use:

- center-point repeats;
- controlled perturbations;
- response-surface DOE for interactions/nonlinearity;
- holdout confirmation runs;
- detector-level correlation.

## Step 9 — promote the resulting specification into P17

Only after the allocation and verification are complete should P17 receive:

- nominal/target;
- LSL/USL or one-sided limit;
- rationale;
- measurement uncertainty;
- capability/yield requirement.

---

# 9. Specific first allocation consequences

## 9.1 D* metrology

Because

`D* = R_v sqrt(A)/e_n`,

responsivity and noise calibration have equal first-order magnitude and opposite sign; area has half the fractional leverage.

Therefore:

- P11 and P12 uncertainty budgets should be designed jointly;
- spending extreme metrology effort on active-area uncertainty while responsivity or detector-referred noise is substantially worse is inefficient;
- the historical 24.5-nV/sqrtHz plateau cannot close the 1-kHz D* benchmark because the signal frequency is below the ~3-kHz 1/f knee.

No D* tolerance is released until the reproduction objective defines one.

## 9.2 Electric field and self-heating

Ideal Joule power scales as `E^2`.

Therefore field calculation, series/contact voltage correction and gap metrology have direct thermal leverage.

P10 should allocate a field/voltage/gap uncertainty only after a detector-temperature or responsivity/noise stability requirement is defined.

## 9.3 Composition / spectral response

At x=.30/80 K the Hansen model gives about `-33 nm` band-gap-equivalent wavelength shift per `+0.001` in x.

This is enough to show that composition is potentially high leverage.

It is **not** enough to state an `x +/- ...` production limit because:

- Hansen model error is finite;
- measured detector cutoff differs from `lambda_Eg`;
- cutoff convention is historically unresolved;
- thickness/absorption/optics/response weighting contribute.

The next required derivative is empirical:

`partial lambda_response / partial x_P06`

under fixed detector process/temperature.

## 9.4 Background radiometry

The idealized RP-01 background model near 300 K is extremely sensitive to source temperature and spectral boundary.

This means BLIP verification should not be based on:

`nominal 300 K + nominal 60 degrees + scalar 4.4-um cutoff`.

P11/P12 should instead use:

- calibrated source radiance/temperature;
- measured physical aperture/view factor;
- measured spectral response/QE/window weighting;
- uncertainty propagation.

## 9.5 Thickness

Thickness sensitivity to absorbed fraction ranges from nearly unity in the optically thin limit to nearly zero when optically thick.

Therefore a thickness tolerance cannot be allocated from the historical 9.5-um number alone. It requires the P06 absorption/transmission model at the wavelengths and geometry that matter to P11 performance.

## 9.6 Blocking contact

No scalar sensitivity of D* to `dconv`, `Ns` or `rho_c` is released.

The key detector-level variable is minority-carrier loss/sweepout, and `rho_c != S_c`.

The required local response block is:

`{Ns,dconv,Lconv,transport profile,contact geometry} -> {R(E),e_n(E),tau_eff(E),D*(E)}`.

This likely requires a 2-D drift-diffusion/contact model plus matched-device DOE.

---

# 10. Prioritizing empirical work

P20 uses three separate priority concepts.

## Physics leverage

Magnitude of a justified sensitivity `|S_ij|`.

## Current contribution

`C_ij = |S_ij| u_xj/x_j` or the variance-equivalent contribution.

## Information value

How much the uncertainty in the final requirement decision would be reduced by measuring/closing the derivative more accurately.

Do not rank experiments solely by `|S|` if the input is already tightly controlled or if another unresolved model term dominates.

### Current high-value empirical blocks

1. **P03/P06:** source/thermal/growth -> x/thickness/edge;
2. **P04/P05/P13:** full anneal trajectory -> carrier state/mobility/lifetime;
3. **P08/P10/P12/P13:** blocking-contact state -> sweepout/noise/bandwidth/D*;
4. **P02/P12/P13:** passivation/sidewall state -> 1/f/lifetime/responsivity;
5. **P15/P10/P13:** package thermal/parasitic state -> self-heating/bandwidth/noise.

---

# 11. Nonlinear and coupled processes

First-order sensitivity is not sufficient when:

- the process crosses carrier-type conversion;
- a response contains an optimum or saturation point;
- interactions are strong;
- a threshold/phase transition exists;
- distributions are strongly non-Gaussian;
- one variable changes the meaning of another.

Examples:

### Hg anneal

Carrier sign can change. A local linear derivative across the conversion boundary is physically misleading.

Use a response surface/classification boundary plus local continuous derivatives inside one state.

### Blocking contact

Responsivity can improve while bandwidth falls and 1/f noise changes.

Use a vector/multi-objective response, not a single scalar derivative.

### LPE

Temperature, liquid composition, finite inventory and time interact.

Use a coupled response surface around the actual measured liquidus rather than independent min/max tolerances.

---

# 12. Yield / Monte Carlo allocation

Once response functions and variance components exist, P20 may propagate full distributions instead of only first-order standard uncertainty.

Recommended sequence:

1. fit physically constrained response models;
2. estimate covariance/variance components from P17-compatible independent runs;
3. sample process distributions with correlations retained;
4. propagate through the detector model;
5. estimate requirement pass probability/yield;
6. identify dominant variance contributions;
7. tighten only the variables that materially improve final yield/performance.

Map points on one wafer do not substitute for independent run variation.

---

# 13. P20 record requirements

Every numerical allocation shall record:

- requirement ID and P19 link;
- final metric definition;
- operating condition;
- target and allowed band/uncertainty;
- sensitivity equation;
- dimensional derivative;
- normalized derivative;
- evidence class;
- source/model revision;
- operating point;
- input measurement uncertainty;
- input process variation;
- covariance assumptions;
- allocated contribution;
- local verification dataset;
- nonlinearity/interaction check;
- resulting proposed intermediate specification;
- P17 promotion status.

Use `travelers/P20_REQUIREMENTS_ALLOCATION_REGISTER.md`.

---

# 14. Release rules

A numerical intermediate specification may be promoted to P17 only when:

1. the protected detector requirement is explicit;
2. the operating condition is explicit;
3. the relevant sensitivity is `IDENTITY`, validated `MODEL-CONDITIONAL`, or locally measured;
4. major interaction terms have been tested or bounded;
5. measurement uncertainty is characterized;
6. the allocation method and covariance assumptions are recorded;
7. the proposed band is not derived from process spread alone;
8. detector-level verification shows the intermediate metric actually protects the requirement.

A `PROXY-CONDITIONAL` relation is never sufficient by itself for production release.

---

# 15. Current maturity

The project now has a first analytical sensitivity matrix, but most fabrication-specific Jacobian blocks remain open because no local fabrication dataset exists.

Current state:

- D*/NEP/geometry identities: `CLOSED-D`;
- one-carrier DC screening sensitivities: `CLOSED-D / MODEL-CONDITIONAL`;
- Hansen local derivatives: `CLOSED-D / MODEL-CONDITIONAL`;
- one-pole bandwidth relations: `CLOSED-D after model validation`;
- ideal Planck/FOV background derivatives: `CLOSED-D / MODEL-CONDITIONAL`;
- source mass -> xL: `CLOSED-D`;
- xL/process -> xS: `EMPIRICAL-REQUIRED`;
- anneal trajectory -> transport/lifetime: `EMPIRICAL-REQUIRED`;
- passivation -> 1/f/lifetime: `EMPIRICAL-REQUIRED`;
- blocking contact -> sweepout/noise/bandwidth: `EMPIRICAL-REQUIRED`;
- package -> electrothermal/dynamic behavior: `EMPIRICAL-REQUIRED`.

No new production capability claim is created by P20.

---

# 16. Immediate next work

The next strongest technical work is to close the highest-value empirical Jacobian blocks in this order:

1. P03/P06 analytical + response-surface map from actual melt/source/thermal state to `x`, thickness and optical edge;
2. P04/P05/P13 anneal-trajectory map to carrier state, mobility and lifetime;
3. P08/P10/P12/P13 reduced blocking-contact model linking converted profile/contact loss to responsivity, noise and bandwidth;
4. P02/P02C perimeter/interface sensitivity to 1/f/lifetime;
5. P15 electrothermal/RC sensitivity after a package construction is selected.

The chapter-ordered manual can be assembled in parallel, but it should preserve these `EMPIRICAL-REQUIRED` allocations rather than presenting nominal setpoints as mature tolerances.

---

## Governing files

- `procedures/P19_REQUIREMENTS_TRACEABILITY_MATRIX.md`
- `calculations/RP01_FIRST_ORDER_SENSITIVITY_MATRIX.md`
- `procedures/P17_STATISTICAL_PROCESS_CAPABILITY_RELEASE.md`
- `travelers/P17_PROCESS_RELEASE_CAPABILITY_REGISTER.md`
- `procedures/P18_FAILURE_ANALYSIS_DIAGNOSTIC_ATLAS.md`
- P03/P04/P05/P06/P08/P10/P11/P12/P13/P15 and their controlled addenda.