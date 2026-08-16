# RP-01 first-build integrated uncertainty budget

**Status:** CONTROLLED DERIVED CALCULATION / ROUND 43  
**Date:** 2026-08-16 America/New_York  
**Use with:** P10, P11, P12, P13, P19, P20, P20A, P36/P36A and P16E.

## 1. Purpose

Convert the existing analytical sensitivity matrix into an integrated first-build uncertainty framework without inventing fabrication tolerances that require local HgCdTe response data.

This file distinguishes three different objects:

1. **reported-quantity uncertainty** — uncertainty of a calculated/measured value such as `D*`, `E`, `NEP`, `f3dB`;
2. **physical operating-state uncertainty** — uncertainty in the actual detector state such as `T`, `E`, background, optical power or package transfer;
3. **process variation** — run/wafer/device variation in material/process outputs.

The first two can often be propagated from calibrated measurements. The third requires repeated physical process data and, for many HgCdTe steps, an empirical Jacobian.

A mathematical uncertainty budget is not a released manufacturing tolerance.

---

# 2. Notation and covariance rule

For a positive quantity `x`, define a small relative perturbation

`epsilon_x = delta x / x = delta ln x`.

For a scalar output `y` with logarithmic sensitivity vector `s`,

`epsilon_y ≈ s^T epsilon_x`.

The relative variance is

`u_r(y)^2 = s^T Sigma_r s`,

where `Sigma_r` is the covariance matrix of the relative input errors.

The familiar RSS relation

`u_r(y)^2 = sum_i s_i^2 u_r(x_i)^2`

is valid only when the input errors are sufficiently independent.

Round 43 requires covariance to be retained whenever one calibration or geometry variable appears in more than one part of the final equation.

---

# 3. Exact D* and NEP uncertainty identities

P12 defines

`NEP = e_n / R_v`

and

`D* = R_v sqrt(A) / e_n`.

Therefore

`delta ln NEP = delta ln e_n - delta ln R_v`

and

`delta ln D* = delta ln R_v + 0.5 delta ln A - delta ln e_n`.

For the variable order `{R_v,A,e_n}`, the D* sensitivity vector is

`s_D = {+1,+0.5,-1}`.

Thus the complete relative variance is

`u_r(D*)^2 = s_D^T Sigma_r s_D`.

Expanded:

`u_r(D*)^2 = u_r(R_v)^2 + 0.25 u_r(A)^2 + u_r(e_n)^2`

`+ Cov_r(R_v,A) - 2 Cov_r(R_v,e_n) - Cov_r(A,e_n)`.

The covariance terms are not optional bookkeeping: common gain, common geometry and common operating-state errors can produce real cancellation or reinforcement.

---

# 4. Common voltage-gain cancellation in D*

Suppose responsivity and noise are reduced through the same linear voltage path at the same frequency and loading state.

Let

`S_sig` = measured output signal,

`e_out` = measured output noise ASD,

`G` = common voltage gain from detector terminals to the measured output,

`P_inc` = incident optical power.

Then

`R_v = (S_sig/G)/P_inc`

and

`e_n = e_out/G`.

Substitution into D* gives

`D* = S_sig sqrt(A) / (P_inc e_out)`.

The common multiplicative gain `G` cancels exactly.

### Consequence

Do **not** count the same gain-calibration uncertainty independently in both P11 responsivity and P12 detector-referred noise when the same physical gain realization applies.

### When cancellation is incomplete

If signal and noise use different gain states or transfer functions,

`D* = [S_sig sqrt(A)/(P_inc e_out)] [G_noise/G_signal]`.

Only the **gain ratio** matters.

Therefore Round-43 metrology should preferentially:

- evaluate noise at the same `1 kHz` signal frequency used for canonical D*;
- use the same detector/loading path where practical;
- record gain-state identities and transfer functions;
- propagate gain-ratio uncertainty, not two unrelated absolute-gain terms.

This is an `IDENTITY` result under a linear common path.

---

# 5. Active-area sensitivity depends on the optical-power convention

The usual D* identity gives `S_D,A=+0.5` only when `P_inc` used in responsivity is independent of the area used in D* normalization.

Write

`D* = V_sig sqrt(A)/(P_inc e_n)`.

Define

`gamma_A = partial ln P_inc / partial ln A`

for the actual optical-power convention.

Then, holding the intrinsic detector response and other variables fixed,

`S_D,A = 0.5 - gamma_A`.

## 5.1 Direct radiant-power calibration

If a calibrated total optical power incident on the detector/aperture is measured independently of `A`,

`gamma_A = 0`

and

`S_D,A = +0.5`.

## 5.2 Uniform-irradiance calibration

If power is inferred as

`P_inc = H A`

from irradiance `H` and the **same area** `A`, then

`gamma_A = 1`

and

`S_D,A = -0.5`.

Thus the sign reverses.

## 5.3 Partial beam interception / real aperture

For a nonuniform beam, aperture clipping or different optical/electrical areas, `gamma_A` need not be 0 or 1. It must be obtained from the beam/aperture model or map.

### Permanent Round-43 rule

`active-area uncertainty` cannot be assigned to D* until the P11 incident-power convention and P12 area convention are jointly declared.

---

# 6. Geometry and electric-field coupling

P10 defines

`E = V_active / L`.

For independent measurement errors,

`u_r(E)^2 = u_r(V_active)^2 + u_r(L)^2`.

With covariance,

`u_r(E)^2 = u_r(V_active)^2 + u_r(L)^2 - 2 Cov_r(V_active,L)`.

The sign in the reporting equation does not eliminate the need to distinguish how the voltage was physically set.

If voltage command is calculated from a measured gap to realize a target field, the control-law uncertainty shall be modeled explicitly rather than reusing the post-hoc `V/L` covariance by assumption.

---

# 7. Effective D* sensitivity to contact gap is not generally +0.5

Let

- `A = W L` for the selected active-area convention;
- `gamma_L = partial ln P_inc / partial ln L` for the optical-power convention;
- `s_R,E = partial ln R_v / partial ln E` at the operating point;
- `s_n,E = partial ln e_n / partial ln E` at the operating point.

At fixed physical `V_active`, because `E=V_active/L`,

`delta ln E = - delta ln L`.

Then

`S_D,L = 0.5 - gamma_L - s_R,E + s_n,E`.

Similarly, at fixed `L`,

`S_D,V = s_R,E - s_n,E`.

### Interpretation

Gap error affects D* through:

1. the `sqrt(A)` normalization;
2. the optical power if area/irradiance defines `P_inc`;
3. the actual electric field;
4. field-dependent responsivity;
5. field-dependent noise.

The historical device is known to have field-dependent responsivity/sweepout, and P12 noise is bias dependent. Therefore the production-relevant gap sensitivity cannot be reduced to the area term alone.

The missing local derivatives

`s_R,E` and `s_n,E`

must come from matched P10/P11/P12 data around the selected operating point.

This is one of the highest-value Round-43 empirical blocks.

---

# 8. Joule power and self-heating uncertainty

## 8.1 Measured-power identity

If power is calculated from independently measured detector-terminal quantities,

`P_J = V_active I`,

then

`delta ln P_J = delta ln V_active + delta ln I`.

Hence

`u_r(P_J)^2 = u_r(V_active)^2 + u_r(I)^2 + 2 Cov_r(V_active,I)`.

This identity is preferable for reporting actual dissipated power.

## 8.2 One-carrier model

P20/P10 give, at fixed uniform field,

`P_J = q n mu E^2 W d L`.

The normalized sensitivities are:

- `S_E=+2`;
- `S_n=S_mu=S_W=S_d=S_L=+1`.

This is `MODEL-CONDITIONAL` and is appropriate for screening/instrument design, not release until the electrical model is validated.

If

`DeltaT = P_J R_th`

is locally linear, then

`S_DeltaT,E=+2`, `S_DeltaT,Rth=+1`.

The actual package `R_th` and electrothermal feedback remain local.

---

# 9. Spectral responsivity comparator uncertainty

For the P11 direct comparison branch,

`R_DUT = (V_DUT/V_ref) R_ref`.

Therefore

`delta ln R_DUT = delta ln V_DUT - delta ln V_ref + delta ln R_ref`.

If independent,

`u_r(R_DUT)^2 = u_r(V_DUT)^2 + u_r(V_ref)^2 + u_r(R_ref)^2`.

But covariance must be retained for:

- common source drift corrections;
- common gain/calibration paths;
- common positioning/beam-profile errors;
- common timebase/modulation conventions.

The practical P11 uncertainty budget shall also contain separate terms for:

- wavelength calibration / spectral convolution near edge;
- source/reference linearity;
- substitution/beam-position repeatability;
- atmospheric absorption / purge state;
- reference-detector spatial uniformity;
- optical power convention;
- signal-amplitude convention.

No generic percent value is assigned here because the final D* comparison objective remains undefined.

---

# 10. Electronics-floor subtraction conditioning

P12 may obtain detector noise from

`e_det = sqrt(e_meas^2 - e_elec^2)`.

Define the electronics-to-detector PSD ratio

`beta = e_elec^2/e_det^2`.

Because

`e_meas^2 = e_det^2(1+beta)`,

the exact local logarithmic sensitivities are

`partial ln e_det / partial ln e_meas = 1 + beta`

and

`partial ln e_det / partial ln e_elec = -beta`.

For independent relative uncertainties,

`u_r(e_det)^2 ≈ (1+beta)^2 u_r(e_meas)^2 + beta^2 u_r(e_elec)^2`.

### Conditioning table

| `beta` electronics/detector PSD | `e_elec/e_det` | `e_meas/e_det` | sensitivity to measured ASD | magnitude sensitivity to electronics ASD |
|---:|---:|---:|---:|---:|
| 0.01 | 0.100 | 1.005 | 1.01 | 0.01 |
| 0.05 | 0.224 | 1.025 | 1.05 | 0.05 |
| 0.10 | 0.316 | 1.049 | 1.10 | 0.10 |
| 0.25 | 0.500 | 1.118 | 1.25 | 0.25 |
| 0.50 | 0.707 | 1.225 | 1.50 | 0.50 |
| 1.00 | 1.000 | 1.414 | 2.00 | 1.00 |
| 4.00 | 2.000 | 2.236 | 5.00 | 4.00 |

This gives a quantitative reason to keep electronics comfortably below detector noise.

Round 41's example `beta=0.10` (`e_elec≈0.316 e_det`) is well conditioned, but remains an engineering design example rather than an RP-01 historical criterion.

---

# 11. Parameterized D* metrology allocation

Let the desired relative standard uncertainty in D* be

`g_D = u(D*)/D*`.

If, only for planning, the three independent variance contributions from `R_v`, `e_n` and `A` are made equal, then

`u_r(R_v) = g_D/sqrt(3)`

`u_r(e_n) = g_D/sqrt(3)`

and because the area sensitivity is `0.5`,

`u_r(A) = 2 g_D/sqrt(3)`.

Planning examples:

| desired `g_D` | `u_r(R_v)` | `u_r(e_n)` | `u_r(A)` |
|---:|---:|---:|---:|
| 10% | 5.77% | 5.77% | 11.55% |
| 5% | 2.89% | 2.89% | 5.77% |
| 2% | 1.15% | 1.15% | 2.31% |
| 1% | 0.577% | 0.577% | 1.155% |

**Restrictions:**

- this is a `DESIGN-CHECK`, not a recommended universal allocation;
- it assumes direct-power area sensitivity `+0.5`;
- it assumes independence;
- it ignores field/geometry coupling;
- it ignores common-gain cancellation;
- it does not define the required value of `g_D`.

The actual budget should exploit covariance/cancellation instead of enforcing equal contributions mechanically.

---

# 12. Idealized 300-K background uncertainty back-solves

The controlled Planck/cone/step model at the RP-01-like condition gives approximately:

- `partial ln Phi/partial T = 0.04027 K^-1`;
- around a 60-degree full cone, about `0.0304 degree^-1` for full-cone angle;
- `partial ln Phi/partial lambda_c = 2.0638 um^-1` at `lambda_c=4.4 um`.

If one term alone were assigned a fractional background-flux uncertainty `g_Phi`, the local screening relations are

`u_T <= g_Phi/0.04027`

`u_Theta_full <= g_Phi/0.0304 degrees`

`u_lambda_c <= g_Phi/2.0638 um`.

Examples:

| `g_Phi` | one-term `u_T` | one-term `u_Theta_full` | one-term `u_lambda_c` |
|---:|---:|---:|---:|
| 5% | 1.24 K | 1.64 deg | 24.2 nm |
| 2% | 0.497 K | 0.658 deg | 9.69 nm |
| 1% | 0.248 K | 0.329 deg | 4.85 nm |

These are intentionally diagnostic. A real P11/P12 background model shall use measured aperture geometry, radiance and spectral weighting rather than a sharp scalar cutoff.

The very small step-boundary numbers demonstrate why using an uncertain `4.4 um cutoff` as a radiometric integration boundary is unsuitable for precision BLIP verification.

---

# 13. Hansen composition/temperature screening back-solves

At `x=.30`, `T=80 K`, the controlled Hansen model gives

`partial lambda_Eg/partial x = -33.0525 um per x`

and

`partial lambda_Eg/partial T = -0.004468 um/K`.

For an allowed **band-gap-equivalent wavelength** standard uncertainty `u_lambda`, the one-term screening limits are

`u_x <= u_lambda/33.0525`

and

`u_T <= u_lambda/0.004468`.

Examples:

| `u_lambda_Eg` | one-term `u_x` | one-term `u_T` |
|---:|---:|---:|
| 50 nm | 0.00151 | 11.2 K |
| 25 nm | 0.000756 | 5.60 K |
| 10 nm | 0.000303 | 2.24 K |
| 5 nm | 0.000151 | 1.12 K |

**Critical restriction:** these are not detector-cutoff tolerances. RP-01's measured response edge is not equal to `lambda_Eg`. The production-relevant derivative `partial lambda_response/partial x_P06` remains empirical/model-validated.

---

# 14. LPE charge-mass uncertainty remains a proxy chain

The existing charge calculation gives exact derivatives from elemental masses to the **nominal liquid-composition coordinates** `xL,yL` under the frozen atomic-weight convention.

The next chains are not exact:

`{xL,yL,TL,DeltaT_SC,t,inventory,Hg-loss} -> xS,d`

and

`{xS,d,...} -> detector response edge/R_v/e_n`.

Therefore Round 43 allows:

- balance/charge metrology to be sized from mass-to-`xL/yL` sensitivity;
- P21 DOE ranges to be informed by those sensitivities;

but prohibits:

- converting a target detector cutoff directly into a Cd balance tolerance using the `xS/xL=3.54` ratio;
- assigning LPE temperature/time tolerances before the local P21 Jacobian exists.

Status: `PROXY-CONDITIONAL -> EMPIRICAL-JACOBIAN-REQUIRED`.

---

# 15. Temporal/frequency-response uncertainty

After P13 validates a one-pole detector model,

`f_3dB = 1/(2 pi tau)`.

Therefore

`delta ln f_3dB = - delta ln tau`

and

`u_r(f_3dB)=u_r(tau)`

for the same fitted physical pole, excluding separate model discrepancy.

## 15.1 Amplitude-derived corner sensitivity

For

`|H| = 1/sqrt(1+z^2)`, `z=f/f_3dB`,

`partial ln |H| / partial ln f = -z^2/(1+z^2)`.

At the corner `z=1`, this is `-1/2`.

Thus, very locally and using amplitude alone,

`u_r(f_3dB) ≈ 2 u_r(|H|)`

for small relative amplitude uncertainty near the -3-dB point.

This is a fit-design relation, not a substitute for a full multi-frequency fit.

## 15.2 Phase-derived corner sensitivity

For a one-pole phase

`phi=-atan(z)`,

`partial phi/partial ln f = -z/(1+z^2)`.

At `z=1`,

`partial phi/partial ln f = -0.5 rad`.

Hence a local phase uncertainty `u_phi` in radians implies approximately

`u_r(f_3dB) ≈ 2 u_phi`

if phase alone is used near the corner.

Amplitude and phase should be fitted jointly when possible.

---

# 16. De-embedding uncertainty is multiplicative and correlated

P13 uses a transfer decomposition of the form

`H_meas = H_source H_optics H_detector H_bias H_preamp H_cable H_instr H_pkg`

where the package term may require a coupled rather than purely multiplicative model.

For a multiplicative representation,

`ln H_detector = ln H_meas - sum_k ln H_k`.

Thus magnitude and phase covariance from every calibration transfer enter the extracted detector response.

Round-43 requirements:

- preserve complex transfer functions, not magnitude only;
- retain covariance if several terms share one timebase, digitizer or reference detector;
- do not assign detector `tau` uncertainty from fit statistics alone;
- include model discrepancy for package thermal coupling and non-one-pole detector response.

A measured system pole cannot be converted into a detector lifetime uncertainty budget until these transfer terms are bounded.

---

# 17. Requirement-state matrix after analytical propagation

| Final/intermediate quantity | Analytical allocation status | Remaining blocker |
|---|---|---|
| `E=V/L` | `IDENTITY-ALLOCATABLE` | actual voltage/gap metrology covariance/control law |
| `A=W L` | `IDENTITY-ALLOCATABLE` | active-area convention / optical geometry |
| `P=VI` | `IDENTITY-ALLOCATABLE` | actual terminal measurement transfer |
| `R_DUT=(V_DUT/V_ref)R_ref` | `IDENTITY-ALLOCATABLE` | real calibration uncertainties/covariance |
| `NEP=e_n/R_v` | `IDENTITY-ALLOCATABLE` | matched state and P11/P12 uncertainties |
| `D*=R_v sqrt(A)/e_n` | `IDENTITY-ALLOCATABLE` | requirement target + covariance + area/power convention |
| electronics PSD subtraction | `IDENTITY-ALLOCATABLE` | measured electronics/detector ratio and uncertainties |
| Hansen `x,T -> lambda_Eg` | `MODEL-CONDITIONAL` | response-edge model mismatch |
| ideal background flux | `MODEL-CONDITIONAL` | real spectral/aperture weighting |
| one-pole `tau <-> f3dB` | `MODEL-CONDITIONAL` until P13 validation | de-embedding/model adequacy |
| LPE controls -> `x,d` | `EMPIRICAL-JACOBIAN-REQUIRED` | P21/local material runs |
| anneal trajectory -> `n,mu,tau` | `EMPIRICAL-JACOBIAN-REQUIRED` | P23/local state map |
| mesa/oxide -> `R_v,e_n,tau` | `EMPIRICAL-JACOBIAN-REQUIRED` | matched device DOE |
| RIE/contact -> `R_v,e_n,tau,D*` | `EMPIRICAL-JACOBIAN-REQUIRED` | P24 + transport/device data |
| package -> thermal/dynamic detector state | `EMPIRICAL-JACOBIAN-REQUIRED` | P33/P13 package characterization |

---

# 18. What Round 43 can and cannot numerically specify

## Can specify now

- exact uncertainty equations for definitions;
- covariance/cancellation structure;
- parameterized back-solves versus a future detector-level uncertainty goal;
- instrument-conditioning criteria such as electronics-floor subtraction sensitivity;
- model-conditional screening numbers with explicit domains;
- which empirical derivatives are required before fabrication tolerances can be released.

## Cannot specify now

- an allowed percent error in the historical `D*≈2e11` benchmark without a reproduction/system objective;
- an `x +/- ...` production tolerance from the 4.4-um response edge;
- a universal LPE `DeltaT_SC`, contact-time or charge tolerance;
- an anneal temperature/dwell/cooldown tolerance;
- an RIE self-bias/conversion-depth tolerance;
- a passivation thickness/process tolerance from noise alone;
- a package thermal resistance limit;
- a detector lifetime/bandwidth acceptance band before the requirement and model are defined.

---

# 19. Minimum data required to turn the parameterized budget into a numerical allocation

A future allocation record must provide:

1. final detector/system metric and allowed error/uncertainty;
2. exact operating condition and active-area/optical-power convention;
3. actual P16C/P16D tool states and calibration uncertainties;
4. covariance structure/common paths;
5. local `R_v(E)` and `e_n(E)` slopes near the canonical field;
6. P21 LPE response Jacobian;
7. P23 anneal state map/Jacobian in one carrier-state region;
8. blocking-contact/passivation/device response Jacobians;
9. package thermal/dynamic transfer;
10. confirmation data showing the local linearization is adequate.

Until these exist, numerical process specifications remain `LOCAL-SPEC-OPEN`.

---

# 20. Permanent Round-43 rules

1. **Covariance is physics, not bookkeeping.** Common gains/geometries can cancel or reinforce.
2. **Do not count a common gain twice in D*.** If P11/P12 share one linear path, propagate the gain ratio or cancellation.
3. **Active-area sensitivity is convention dependent.** `+0.5` is not universal when power is inferred from irradiance and area.
4. **Gap metrology couples area and bias.** Use the full `S_D,L` relation once field slopes are measured.
5. **Noise subtraction has a condition number.** Electronics close to detector noise can dominate the uncertainty after PSD subtraction.
6. **Fit uncertainty is not full de-embedding uncertainty.** P13 must include source/electrical/package transfer terms.
7. **Model-conditional back-solves do not become manufacturing tolerances.** Hansen, Planck and one-pole results retain their evidence class.
8. **No detector-level requirement -> no justified process tolerance.** Parameterize rather than invent.
