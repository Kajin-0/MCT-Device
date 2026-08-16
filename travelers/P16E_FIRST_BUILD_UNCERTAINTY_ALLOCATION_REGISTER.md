# P16E — first-build uncertainty / requirements-allocation register

**Status:** CONTROLLED PRE-BUILD INTEGRATION REGISTER / ROUND 43  
**Date:** 2026-08-16 America/New_York  
**Use with:** P19, P20/P20A, P16A–P16D and `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`.

## 1. Purpose

Provide a cross-system fill-in record showing whether the first-build measurement/control decisions have defensible uncertainty allocations and whether any proposed numerical limit is supported by a downstream detector/system requirement.

P16E does not replace detailed P20 records and does not promote any P16A readiness row automatically.

Final integration state:

`P16E-REQUIREMENTS-ALLOCATION-COMPLETE = YES / NO`.

---

# 2. Register header

Laboratory/facility: ____________________  
Responsible analyst: ____________________  
Date: ____________________  
P16B branch revision: ____________________  
P16C infrastructure revision: ____________________  
P16D acceptance revision: ____________________  
P19/P20 revision: ____________________  
Calculation revision: ____________________

---

# 3. Allowed allocation states

- `REQUIREMENT-DEFINITION-OPEN`
- `IDENTITY-ALLOCATABLE`
- `MODEL-CONDITIONAL-ALLOCATABLE`
- `COVARIANCE-REQUIRED`
- `EMPIRICAL-JACOBIAN-REQUIRED`
- `PARAMETRIC-ALLOCATION-ONLY`
- `LOCAL-ALLOCATION-DEFINED`
- `DETECTOR-LEVEL-VERIFIED`
- `READY-FOR-P17`

---

# 4. Final detector/system requirement register

| ID | Metric | Operating state | Historical reference | Actual local requirement/allowed uncertainty | Maturity | State |
|---|---|---|---|---|---|---|
| U01 | `D*(4 um,1 kHz)` | ~80 K, 10 V/cm, declared background/package | ~`2e11 cm sqrt(Hz)/W` |  | HISTORICAL-REFERENCE | REQUIREMENT-DEFINITION-OPEN |
| U02 | `R_v(4 um,1 kHz)` | matched U01 | historical curve/reference only |  | LOCAL-SPEC-OPEN | REQUIREMENT-DEFINITION-OPEN |
| U03 | `NEP(4 um,1 kHz)` | matched U01 | derived only if matched R/noise known |  | LOCAL-SPEC-OPEN | REQUIREMENT-DEFINITION-OPEN |
| U04 | response edge/cutoff | ~80 K, declared convention | ~4.4 um |  | HISTORICAL-REFERENCE | REQUIREMENT-DEFINITION-OPEN |
| U05 | detector `f3dB/tau` | defined package/readout state | RP-01 direct value not recovered |  | LOCAL-SPEC-OPEN | REQUIREMENT-DEFINITION-OPEN |
| U06 | self-heating/`DeltaT` | canonical bias state | no direct limit recovered |  | LOCAL-SPEC-OPEN | REQUIREMENT-DEFINITION-OPEN |
| U07 | BLIP/background decision | defined source/aperture/spectrum | 300 K/60° reference |  | LOCAL-SPEC-OPEN | REQUIREMENT-DEFINITION-OPEN |

---

# 5. D*/NEP metrology allocation

Final desired relative standard uncertainty `g_D`: ____________________  
Final desired relative standard uncertainty `g_NEP`: ____________________

## Measurement convention

Incident optical quantity:

- [ ] direct radiant power
- [ ] irradiance x active area
- [ ] mapped/nonuniform beam with aperture model
- [ ] other: ____________________

Active area definition: ____________________  
`gamma_A = partial ln P_inc/partial ln A`: ____________________

Signal path ID: ____________________  
Noise path ID: ____________________  
Signal frequency: ____________________  
Noise evaluation frequency: ____________________

Common gain path?: YES / NO  
If YES, common gain cancellation used?: YES / NO  
If NO/different path, gain-ratio uncertainty: ____________________

| Input | Standard uncertainty | Sensitivity | Covariance/common-path note | Variance contribution | Status |
|---|---:|---:|---|---:|---|
| P11 signal/reference response |  |  |  |  |  |
| reference responsivity |  |  |  |  |  |
| optical power / irradiance |  |  |  |  |  |
| active area |  | `0.5-gamma_A` |  |  |  |
| P12 measured ASD |  |  |  |  |  |
| electronics ASD/subtraction |  |  |  |  |  |
| gain ratio |  |  |  |  |  |
| detector T state |  | empirical local |  |  |  |
| detector E state |  | empirical local |  |  |  |

Calculated `u_r(D*)`: ____________________  
Calculated `u_r(NEP)`: ____________________

Disposition: ____________________

---

# 6. Electronics-noise subtraction conditioning

At D* frequency:

Measured ASD `e_meas`: ____________________  
Electronics ASD `e_elec`: ____________________  
Derived detector ASD `e_det`: ____________________

`beta = e_elec^2/e_det^2 =` ____________________

Derived local sensitivities:

- to measured ASD: `1+beta =` ____________________
- to electronics ASD: `-beta =` ____________________

Measured-ASD relative uncertainty: ____________________  
Electronics-ASD relative uncertainty: ____________________  
Subtraction contribution to `u_r(e_det)`: ____________________

Condition acceptable for final D* budget?: YES / NO / OPEN

---

# 7. Geometry / electric-field coupling

Contact pair: ____________________  
Measured `L`: ____________________  
Measured `W`: ____________________  
`u(L)`: ____________________  
`u(W)`: ____________________  
Active voltage `V_active`: ____________________  
`u(V_active)`: ____________________

`E=V_active/L`: ____________________  
Calculated `u(E)`: ____________________

Field control law:

- [ ] voltage independently fixed
- [ ] voltage commanded from measured gap to target E
- [ ] current bias / load network
- [ ] other: ____________________

Optical-power gap exponent `gamma_L`: ____________________  
Local `s_R,E = partial ln R_v/partial ln E`: ____________________  
Local `s_n,E = partial ln e_n/partial ln E`: ____________________

Derived effective gap sensitivity where applicable:

`S_D,L = 0.5 - gamma_L - s_R,E + s_n,E =` ____________________

State:

- [ ] COVARIANCE-REQUIRED
- [ ] EMPIRICAL-JACOBIAN-REQUIRED
- [ ] LOCAL-ALLOCATION-DEFINED

---

# 8. Power / self-heating allocation

Measured `V_active`: ____________________  
Measured `I`: ____________________  
`P=VI`: ____________________  
`u(P)`: ____________________

Package `R_th` or direct thermal transfer: ____________________  
Detector temperature proxy: ____________________  
Allowed `DeltaT` / response drift: ____________________ (`REQUIREMENT-DEFINITION-OPEN` until justified)

One-carrier `E^2` screening used?: YES / NO  
If used, model-validation status: ____________________

State: ____________________

---

# 9. Radiometry / background allocation

Reference detector ID/calibration: ____________________  
Wavelength calibration uncertainty: ____________________  
Source radiance/temperature uncertainty: ____________________  
Aperture/view-factor uncertainty: ____________________  
Window/filter transmission uncertainty: ____________________  
Substitution/beam-profile uncertainty: ____________________  
Source drift correction: ____________________  
Atmospheric/purge contribution: ____________________

Idealized scalar background sensitivity used for diagnostics?: YES / NO

If yes:

- `u_T` screening contribution: ____________________
- `u_Theta_full` screening contribution: ____________________
- `u_lambda_step` screening contribution: ____________________

Final BLIP calculation uses measured spectral weighting?: YES / NO / PENDING

State: ____________________

---

# 10. Material-state / upstream allocation

## Charge / composition

Selected `M_charge`: ____________________  
Balance uncertainties at Hg/Cd/Te mass ranges: ____________________  
Propagated `u(xL),u(yL)`: ____________________

LPE response Jacobian P21 available?: YES / NO  
If NO: `EMPIRICAL-JACOBIAN-REQUIRED`.

## FTIR / composition / thickness

FTIR wavelength/fit uncertainty: ____________________  
Independent thickness uncertainty: ____________________  
Hansen screening model used?: YES / NO  
Measured detector-edge derivative `partial lambda_response/partial x_P06` available?: YES / NO

## Hall / anneal

B-field uncertainty: ____________________  
Current/voltage/geometry uncertainty: ____________________  
Hall reduction covariance for `n/mu`: ____________________  
P23 anneal-state Jacobian available?: YES / NO

State: ____________________

---

# 11. Microfabrication / contact empirical blocks

| Block | Inputs | Required outputs | Jacobian/model available? | State |
|---|---|---|---|---|
| mesa/passivation | profile, oxide/interface state | `R_v,e_n,tau` |  | EMPIRICAL-JACOBIAN-REQUIRED |
| RIE conversion | `Ns,dconv,Lconv,self-bias,damage` | sweepout, `R_v,e_n,tau,D*` |  | EMPIRICAL-JACOBIAN-REQUIRED |
| Cr/Au/contact | `rho_c`, geometry, interface | terminal transfer/noise |  | EMPIRICAL-JACOBIAN-REQUIRED |
| singulation | edge/subsurface state | resistance/noise/responsivity/survival |  | EMPIRICAL-JACOBIAN-REQUIRED |
| package | bondline/thermal/optical/interconnect | `R_th,H_pkg,noise` |  | EMPIRICAL-JACOBIAN-REQUIRED |

---

# 12. Temporal/frequency-response allocation

System transfer function revision: ____________________  
Source transfer uncertainty: ____________________  
Optical reference transfer uncertainty: ____________________  
Bias/preamp/cable/instrument transfer uncertainty: ____________________  
Package transfer uncertainty/model: ____________________

Detector model:

- [ ] one pole validated
- [ ] multi-pole
- [ ] non-exponential / other
- [ ] not yet established

Fit-only `u(f3dB)` / `u(tau)`: ____________________  
De-embedding contribution: ____________________  
Model discrepancy: ____________________  
Final combined uncertainty: ____________________

Required bandwidth/lifetime decision margin: ____________________

State: ____________________

---

# 13. Covariance register

| Shared term | Appears in | Expected sign/cancellation | Quantified? | Result |
|---|---|---|---|---|
| common voltage gain | P11 signal / P12 noise | may cancel in D* |  |  |
| active gap `L` | area / E | coupled; may reinforce/cancel |  |  |
| active area | power conversion / D* normalization | convention dependent |  |  |
| detector temperature | responsivity / noise / resistance | correlated state error |  |  |
| detector field | responsivity / noise / self-heating | correlated state error |  |  |
| source/timebase | P11/P13 transfers | common calibration |  |  |
| Hall reduction | `n,mu` | correlated |  |  |
| source composition/liquidus | LPE state | coupled physics |  |  |

---

# 14. First-build decision matrix

| Decision | Final requirement defined? | Analytical budget closed? | Empirical Jacobian needed? | Metrology adequate? | Detector-level verified? | Status |
|---|---|---|---|---|---|---|
| charge acceptance |  |  | YES for solid/device consequence |  |  |  |
| LPE thermal/contact acceptance |  |  | YES |  |  |  |
| anneal final-state acceptance |  |  | YES |  |  |  |
| lithography/mesa/oxide acceptance |  |  | YES for detector consequence |  |  |  |
| RIE/contact acceptance |  |  | YES |  |  |  |
| Cr/Au contact acceptance |  |  | YES for detector consequence |  |  |  |
| canonical E/T operating state |  | identity + empirical slopes | YES for field response slopes |  |  |  |
| responsivity |  | identity | limited |  |  |  |
| noise ASD |  | identity | limited |  |  |  |
| `NEP/D*` |  | identity + covariance | field/process slopes |  |  |  |
| `f3dB/tau` |  | model conditional | package/model |  |  |  |

---

# 15. P16E disposition

Every first-build detector/system requirement numerically defined or explicitly declared qualification-only: YES / NO  
Every identity/model sensitivity entered: YES / NO  
Every covariance/common-path term reviewed: YES / NO  
Every empirical Jacobian gap assigned to a controlled DOE/model: YES / NO  
Every derivable metrology requirement compared with P16C/P16D capability: YES / NO  
No arbitrary historical tolerance introduced: YES / NO  
Detector-level verification complete where required: YES / NO

Final:

`P16E-REQUIREMENTS-ALLOCATION-COMPLETE = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** P16E completion does not itself set P16A, P16C, P16D or P17 state.
