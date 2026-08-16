# RP-01 first-order analytical sensitivity matrix

**Status:** CONTROLLED DERIVED CALCULATION / REQUIREMENTS-ALLOCATION INPUT  
**Date:** 2026-08-16 America/New_York

## Purpose

Quantify the first derivatives that can be established without local fabrication data and identify the process-to-device derivatives that cannot yet be assigned honestly.

This file is an input to `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`.

It does **not** create production tolerances. A large sensitivity does not by itself imply a tight process limit; the actual contribution also depends on the achievable variation/uncertainty of the input and on covariance with other inputs.

---

## 1. Sensitivity definitions

For output `y` and input `x_i`, define the dimensional local derivative

`J_i = partial y / partial x_i`

and, where `x_i` and `y` are nonzero, the normalized/logarithmic sensitivity

`S_i = partial ln(y) / partial ln(x_i) = (x_i/y)(partial y/partial x_i)`.

For small changes,

`delta y ≈ sum_i J_i delta x_i`

or

`delta ln(y) ≈ sum_i S_i delta ln(x_i)`.

For independent standard uncertainties,

`u_y^2 ≈ J Sigma J^T`

which reduces to

`(u_y/y)^2 ≈ sum_i (S_i u_xi/xi)^2`

only when the variables are independent and the local linearization is adequate.

### Evidence classes used here

- `IDENTITY` — exact derivative of a controlled definition/equation.
- `MODEL-CONDITIONAL` — exact derivative inside a stated physical model, but not automatically valid for the real detector outside that model.
- `PROXY-CONDITIONAL` — chains two or more approximations and is useful only for order-of-magnitude screening.
- `EMPIRICAL-REQUIRED` — no defensible numerical derivative exists yet; local DOE, metrology or validated transport/thermal modeling is required.

---

# 2. D*, NEP and active-area sensitivities

P12 defines

`NEP = e_n / R_v`

and

`D* = R_v sqrt(A) / e_n`.

Therefore, exactly:

| Output | Input | Normalized sensitivity | Class |
|---|---|---:|---|
| `NEP` | `e_n` | `+1` | IDENTITY |
| `NEP` | `R_v` | `-1` | IDENTITY |
| `D*` | `R_v` | `+1` | IDENTITY |
| `D*` | `e_n` | `-1` | IDENTITY |
| `D*` | `A` | `+1/2` | IDENTITY |

Thus a 1% responsivity scale error produces a 1% D* scale error, a 1% noise-ASD error produces a 1% opposite D* error, and a 1% area error produces a 0.5% D* error, before correlations.

This is why P11/P12 calibration and the common-frequency/common-operating-point rule have direct first-order leverage on the final benchmark.

---

# 3. Uniform one-carrier DC geometry sensitivities

P10 uses the screening model

`rho = 1/(q n mu)`

and for a uniform rectangular active region

`R_bulk = L/(q n mu W d)`.

Hence:

| `R_bulk` input | `S` |
|---|---:|
| `L` | `+1` |
| `n` | `-1` |
| `mu` | `-1` |
| `W` | `-1` |
| `d` | `-1` |

At fixed electric field,

`V_active = E L`

`I_bulk = q n mu E W d`

and

`P_J = V I = q n mu E^2 W d L`.

Therefore:

| Output | Input | `S` | Class |
|---|---|---:|---|
| `V_active` | `E` | `+1` | IDENTITY within uniform geometry |
| `V_active` | `L` | `+1` | IDENTITY within uniform geometry |
| `I_bulk` | `n` | `+1` | MODEL-CONDITIONAL one-carrier |
| `I_bulk` | `mu` | `+1` | MODEL-CONDITIONAL one-carrier |
| `I_bulk` | `E` | `+1` | MODEL-CONDITIONAL one-carrier |
| `I_bulk` | `W` | `+1` | MODEL-CONDITIONAL one-carrier |
| `I_bulk` | `d` | `+1` | MODEL-CONDITIONAL one-carrier |
| `P_J` | `E` | `+2` | MODEL-CONDITIONAL one-carrier |
| `P_J` | `n,mu,W,d,L` | `+1` each | MODEL-CONDITIONAL one-carrier |

The `E^2` dependence is particularly important. A 1% field error changes ideal Joule power by approximately 2% before temperature-dependent resistance, mobility or thermal feedback are included.

If the steady-state linear thermal model

`Delta T = P_J R_th`

is valid, then `S_DeltaT,E = +2` and `S_DeltaT,Rth = +1`. Actual `R_th` and electrothermal feedback remain local package/device quantities.

---

# 4. Hansen band-gap-equivalent wavelength sensitivity

The controlled Hansen relation in `HANSEN_BANDGAP_MODEL.md` is

`Eg(x,T) = -0.302 + 1.93x - 0.810x^2 + 0.832x^3 + 5.35e-4 T (1-2x)` eV

and

`lambda_Eg = 1.239841984/Eg` micrometers.

At the nominal RP-01 point `x=0.30`, `T=80 K`:

- `Eg = 0.243684 eV`;
- `lambda_Eg = 5.08791 um`;
- `partial Eg/partial x = 1.58304 eV per x`;
- `partial lambda_Eg/partial x = -33.0525 um per x`;
- equivalently, `Delta x = +0.001` gives local `Delta lambda_Eg ≈ -0.03305 um = -33.1 nm`;
- `partial Eg/partial T = 2.14e-4 eV/K`;
- `partial lambda_Eg/partial T = -0.004468 um/K = -4.47 nm/K`.

Normalized sensitivities at this point are:

- `S_lambda,x = -1.9489`;
- `S_lambda,T = -0.07025`.

**Critical restriction:** this is sensitivity of the **Hansen band-gap-equivalent wavelength**, not sensitivity of the measured detector cutoff. RP-01's measured response cutoff is about 4.4 um while the nominal Hansen value at x=.30/80 K is about 5.09 um. The Hansen fit also has finite empirical error. Therefore P20 must obtain the production-relevant `partial lambda_response/partial x` from P06/P11 data or a separately validated optical model before assigning an x tolerance from detector cutoff.

---

# 5. LPE charge-mass -> composition -> wavelength screening proxy

`LPE_CHARGE_COMPOSITION_SENSITIVITY.md` already establishes that Cd weighing dominates direct `xL` sensitivity for the candidate tie line.

For a +0.1 mg Cd mass error, the existing local calculation gives approximately:

| Total charge | `delta xL` | proxy `delta xS = 3.54 delta xL` | Hansen local `delta lambda_Eg` proxy |
|---:|---:|---:|---:|
| 1 g | `+6.02e-4` | `+2.131e-3` | `-70.4 nm` |
| 2 g | `+3.01e-4` | `+1.066e-3` | `-35.2 nm` |
| 5 g | `+1.20e-4` | `+4.248e-4` | `-14.0 nm` |
| 10 g | `+6.02e-5` | `+2.131e-4` | `-7.04 nm` |

This chain is `PROXY-CONDITIONAL` twice over:

1. `xS/xL=3.54` is a tabulated ratio, not a measured local differential `dxS/dxL`;
2. Hansen `lambda_Eg` is not the measured detector response cutoff.

Use this table only to size balance/charge-mass experiments. Do not convert it into a released balance tolerance.

The local production derivative that is actually needed is

`partial xS / partial {xL,yL,TL,DeltaT_SC,t_growth,inventory,Hg-loss state}`.

That derivative remains `EMPIRICAL-REQUIRED`.

---

# 6. One-pole bandwidth sensitivity

For the validated one-pole model in P13,

`H(f)=1/(1+i 2 pi f tau)`

and

`f_3dB = 1/(2 pi tau)`.

Therefore

`S_f3dB,tau = -1`.

A 1% increase in a true one-pole time constant produces a 1% decrease in the -3 dB bandwidth.

At a fixed measurement frequency, let

`z = 2 pi f tau = f/f_3dB`.

Then

`partial ln|H| / partial ln(tau) = -z^2/(1+z^2)`.

Consequences:

- far below the pole (`z << 1`), responsivity is weakly sensitive to tau through dynamic attenuation;
- at `f=f_3dB`, the normalized sensitivity is `-1/2`;
- far above the pole, it approaches `-1`.

### Plateau criterion lookup

If a one-pole detector is required to have less than fractional amplitude attenuation `delta` at a signal frequency, then

`f_3dB/f_sig >= 1 / sqrt[1/(1-delta)^2 - 1]`.

| Allowed amplitude attenuation | Required `f_3dB/f_sig` | At `f_sig=1 kHz` |
|---:|---:|---:|
| 5% | 3.04 | >3.04 kHz |
| 2% | 4.92 | >4.92 kHz |
| 1% | 7.02 | >7.02 kHz |
| 0.5% | 9.96 | >9.96 kHz |
| 0.1% | 22.34 | >22.34 kHz |

These are mathematical criteria for a one-pole model, not RP-01 bandwidth specifications. P13 must first show that a one-pole model is valid.

---

# 7. Background photon-flux sensitivity near the RP-01 condition

`RP01_300K_BACKGROUND_FLUX_CHECK.md` uses the idealized model

`Phi = pi sin^2(theta) integral_0^lambda_c N_lambda(T) d(lambda)`

with a filled Lambertian cone, step spectral boundary and no spectral QE/window weighting.

At

- `T=300 K`;
- 60-degree full cone, hence `theta=30 degrees` half-angle;
- `lambda_c=4.4 um`;

it gives `Phi≈1.1239e15 photons cm^-2 s^-1`.

Local derivatives of the same idealized model are:

### 7.1 FOV / half-angle

Because `Phi ∝ sin^2(theta)`, exactly within the model:

`partial ln Phi / partial theta = 2 cot(theta)` with theta in radians.

At `theta=30 degrees`:

- `partial ln Phi/partial theta = 3.4641 rad^-1`;
- normalized `S_Phi,theta = 2 theta cot(theta) = 1.8138`.

A +1-degree change in **full cone angle** around 60 degrees means +0.5 degree half-angle and changes the ideal flux by approximately +3.04%; -1 degree changes it by about -3.01%.

### 7.2 Blackbody temperature

Numerical differentiation of the same Planck integral at 300 K gives

`partial ln Phi / partial T ≈ 0.04027 K^-1`.

Thus near 300 K, the ideal in-band photon flux changes by about **4.03% per kelvin**.

The normalized sensitivity is

`S_Phi,T ≈ 12.08`.

This very large value occurs because 4.4 um lies on the short-wavelength tail of a 300-K blackbody.

### 7.3 Effective step boundary

For the step-response model,

`partial Phi/partial lambda_c` equals the spectral integrand at the upper boundary.

At 4.4 um:

`partial ln Phi / partial lambda_c ≈ 2.0638 per um`.

So a +0.01-um shift in the effective step boundary changes the ideal flux by about +2.06% locally.

Normalized sensitivity:

`S_Phi,lambda_c ≈ 9.081`.

### 7.4 Diagnostic one-term uncertainty scales

If **one term alone** were allowed to contribute 1% relative uncertainty to this idealized flux calculation, the approximate local limits would be:

- blackbody T: `u_T ≈ 0.248 K`;
- 60-degree full cone angle: `u_Theta_full ≈ 0.331 degree`;
- effective step boundary: `u_lambda_c ≈ 0.00485 um = 4.85 nm`.

These are **not release specifications**. They demonstrate that a scalar `300 K / 60 degrees / 4.4 um` background model is too sensitive for precision BLIP work unless the source temperature, physical aperture geometry and actual spectral weighting are characterized directly.

The correct P11/P12 path is to integrate measured/qualified `eta(lambda) tau_opt(lambda)` and physical view factor rather than use a sharp cutoff proxy.

---

# 8. Absorption versus thickness

For the elementary single-pass absorption model

`eta_abs = 1 - exp(-alpha d)`

let `u=alpha d`. Then

`S_eta,d = S_eta,alpha = u/(exp(u)-1)`.

This gives a useful structural result:

- optically thin (`u << 1`): sensitivity approaches `+1`;
- `u=1`: sensitivity is about `0.582`;
- `u=2`: about `0.313`;
- `u=3`: about `0.157`;
- optically thick: sensitivity approaches zero.

Therefore the leverage of P03 thickness on responsivity cannot be ranked from the 9.5-um number alone. It depends on `alpha(lambda,x,T)`, reflection, interference and the actual generation profile. P06 full-spectrum fitting is required before assigning thickness tolerance from responsivity.

---

# 9. RIE sheet-density / conversion-depth identity

P08B distinguishes measured sheet state from a converted-region volume density.

For a uniform converted layer only,

`n_conv = N_s / d_conv`.

Thus:

- `S_nconv,Ns = +1`;
- `S_nconv,dconv = -1`.

This is an exact algebraic identity under the uniform-layer assumption, but it does **not** establish how `N_s` or `d_conv` affect contact sweepout, `rho_c`, noise or D*. Those detector-level derivatives remain `EMPIRICAL-REQUIRED` / 2-D-model dependent.

---

# 10. Process-to-device derivatives still requiring local closure

The following are the high-value missing Jacobian blocks.

| Process/input block | Required local derivative(s) | Why no number is released yet |
|---|---|---|
| P03 source/thermal/growth | `partial{xS,d,morphology}/partial{xL,yL,TL,DeltaT_SC,t_growth,inventory,source-use}` | finite melt, Hg loss and apparatus-specific thermal/mass transport |
| P04 anneal trajectory | `partial{n,mu,tau,x}/partial{T_sample(t),T_reservoir(t),pHg(t),dwell,cooldown}` | defect chemistry/kinetics and strong path dependence |
| P07 interface state | `partial{mu,tau,yield}/partial{removed depth,roughness,chemistry,clean-to-load,face/miscut}` | surface/process interaction not reducible to one scalar etch time |
| P01/P02 passivation | `partial{tau,1/f,R_v}/partial{mesa profile,oxide process,sidewall state}` | surface recombination/interface charge require device data |
| P08 blocking contact | `partial{R_v,e_n,tau_eff,D*}/partial{Ns,dconv,Lconv,damage,S_c}` | intrinsically 2-D minority-carrier/contact problem |
| P09 metal transfer | `partial{rho_c,noise,stability}/partial{delay,pressure,rate,T_sub}` | interface chemistry/history and contact transport |
| P15 package | `partial{DeltaT,bandwidth,noise,R_v}/partial{R_th,C_parasitic,bake,mechanical stress,optics}` | construction-specific thermal/electrical/optical model |

These blocks should be attacked before tightening historical setpoint tolerances that have no demonstrated detector leverage.

---

# 11. First leverage ranking

This ranking is **not** a production tolerance ranking. It identifies where the existing physics says small fractional changes can propagate strongly or directly.

## 11.1 Detector/characterization chain

High direct/model leverage:

1. **background radiometry near 300 K / 4.4 um** — model sensitivities `S_T≈12.1`, `S_lambda_boundary≈9.08`, `S_FOV≈1.81`;
2. **electric field for heating** — `S_P,E=2`;
3. **composition for band-gap-equivalent wavelength** — `|S_lambda,x|≈1.95` at x=.30/80 K;
4. **responsivity and detector noise in D*** — `+1` and `-1` exactly;
5. **bulk n/mu/geometry in resistance/current** — order-unity normalized sensitivities;
6. **tau in one-pole bandwidth** — `-1` exactly;
7. **area in D*** — `+0.5`.

## 11.2 Fabrication variables with potentially high leverage but presently unquantified

- P04 anneal trajectory -> carrier type/n/mu/lifetime;
- P08 blocking-contact state -> sweepout/responsivity/noise/bandwidth;
- P02/P02C interface state -> 1/f/surface recombination/lifetime;
- P03 thermal/source state -> x/thickness/uniformity;
- package thermal resistance/parasitics -> self-heating/bandwidth/noise.

These should not be called low leverage merely because the current repository lacks numerical derivatives.

---

# 12. Requirements-allocation consequence

The first numerical specifications should be allocated only after the detector-level tolerance/uncertainty objective is stated.

For an output requirement `y` with allowable small relative budget `b_y`, two common allocation forms are:

### Worst-case bounded allocation

`sum_i |S_i| b_i <= b_y`.

### Independent standard-uncertainty allocation

`sum_i (S_i u_i)^2 <= u_y^2`

using relative/log quantities and adding covariance terms when inputs are correlated.

The project must not choose equal budgets by default. Allocate based on:

- sensitivity magnitude;
- achievable measurement/process control;
- physical coupling/correlation;
- cost/sample destruction;
- downstream detectability and rework risk.

P17 capability is evaluated **after** P20 establishes a defensible engineering specification; process spread must not define the specification.

---

# 13. Immediate analytical priorities

1. Replace the Hansen cutoff proxy with an empirical/local `P06 material edge -> P11 detector response edge` derivative.
2. Establish P03 local response surfaces for `x` and thickness versus actual liquidus/supercooling/time/source state.
3. Establish P04 local response surface for Hall/lifetime versus full anneal/cooldown trajectory.
4. Build a reduced P08/P10/P13 2-D contact model or empirical DOE linking blocking state to `R(E)`, `tau(E)`, noise and D*.
5. Use measured spectral weighting and exact aperture geometry for P11/P12 background calculations.
6. Use P12/P13 same-frequency data to decide whether the historical 1-kHz condition is a detector plateau or a dynamically/noise-penalized operating point.

---

## Provenance

Controlled equations and numerical anchors are taken from:

- `calculations/HANSEN_BANDGAP_MODEL.md`;
- `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`;
- `calculations/RP01_300K_BACKGROUND_FLUX_CHECK.md`;
- P08B/P08F;
- P10;
- P11;
- P12;
- P13;
- P19;
- RP-01 Smith et al. 2001 and the primary sources already recorded in the repository source ledger.

All additional derivatives/numerical sensitivities in this file are derived from those controlled equations.