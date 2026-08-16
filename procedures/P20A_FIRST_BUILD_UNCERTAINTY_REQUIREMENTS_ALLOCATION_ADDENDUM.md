# P20A — first-build uncertainty / requirements-allocation addendum

**Status:** CONTROLLED SYSTEM-INTEGRATION ADDENDUM / ROUND 43  
**Date:** 2026-08-16 America/New_York  
**Use with:** P19, P20, P10–P13, P16A–P16D, P17, P21–P23, P36/P36A, and `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`.

## 1. Purpose

Turn the existing P20 sensitivity framework into an end-to-end first-build allocation method that answers:

> Given a detector-level comparison/uncertainty requirement, what must each calibration, geometry, operating-state and process coordinate be known or controlled well enough to support that decision?

P20A does not create manufacturing tolerances from historical nominal values. It separates:

- measurement/calibration uncertainty;
- uncertainty in the realized physical operating state;
- process variation;
- model discrepancy;
- unresolved process-to-device Jacobians.

The controlled chain is:

`detector requirement -> measurement equation -> shared-state/covariance model -> analytical allocation -> empirical-Jacobian gaps -> metrology adequacy -> detector-level verification -> P17`.

---

# 2. New Round-43 allocation states

Use these states in P16E/P20A records.

- `REQUIREMENT-DEFINITION-OPEN` — target/allowed error is not defined; only parameterized allocation is possible.
- `IDENTITY-ALLOCATABLE` — exact algebraic uncertainty propagation is available.
- `MODEL-CONDITIONAL-ALLOCATABLE` — allocation can be derived inside a stated validated/validation-pending model.
- `COVARIANCE-REQUIRED` — common path/geometry/state makes diagonal RSS inadequate.
- `EMPIRICAL-JACOBIAN-REQUIRED` — process-to-output derivative must be measured/validated locally.
- `PARAMETRIC-ALLOCATION-ONLY` — formulas are closed but final numeric requirement is not.
- `LOCAL-ALLOCATION-DEFINED` — a numeric local requirement/budget has been justified and recorded.
- `DETECTOR-LEVEL-VERIFIED` — the allocation has been checked against detector response.
- `READY-FOR-P17` — the allocation is mature enough for process capability/specification evaluation.

These are allocation states, not project maturity states.

---

# 3. Governing distinction: uncertainty is not tolerance

For every variable `x`, P20A shall distinguish:

1. `u_meas(x)` — measurement/calibration uncertainty;
2. `u_state(x)` — uncertainty in the actual realized process/operating state;
3. `sigma_process(x)` — actual physical process variation;
4. `TOL(x)` — allowed engineering/process band, if justified;
5. `u_model` — model discrepancy/parameter uncertainty.

A process can have excellent repeatability but poor absolute calibration, or excellent measurement uncertainty but large physical process spread. These are not interchangeable.

No `TOL(x)` is released from `u_meas(x)` alone.

---

# 4. Requirement-first rule

A numerical allocation begins only after the final metric is stated completely.

Minimum statement:

- metric;
- target/limit;
- allowed uncertainty or decision margin;
- wavelength;
- frequency;
- temperature;
- electric field/load;
- background/FOV/aperture state;
- package state;
- active-area and incident-power conventions;
- one/two-sided decision rule.

Examples of incomplete requirements:

- `D* should match RP-01`;
- `cutoff should be about 4.4 um`;
- `lifetime should be fast`.

Historical reference values are not uncertainty bands.

If the final allowed error remains unknown, P20A must leave the allocation symbolic, e.g. `g_D`, `g_Phi`, `u_lambda`.

---

# 5. Stepwise Round-43 workflow

## Step A — freeze the exact measurement equation

Examples:

`D*=R_v sqrt(A)/e_n`

`NEP=e_n/R_v`

`E=V_active/L`

`P=V_active I`

`R_DUT=(V_DUT/V_ref)R_ref`

`f3dB=1/(2 pi tau)` only after one-pole validation.

If a quantity is derived through a different convention, write that convention explicitly before propagating uncertainty.

## Step B — identify shared variables and common paths

Before performing RSS, ask whether one calibration/geometry term appears in multiple factors.

Examples:

- the same voltage gain in P11 signal and P12 noise;
- the same gap `L` in both area and electric field;
- the same active area in irradiance-to-power conversion and D* normalization;
- the same thermometer affecting responsivity and noise state;
- the same timebase affecting source and detector transfer functions;
- the same Hall reduction producing correlated `n` and `mu`.

If yes, mark `COVARIANCE-REQUIRED`.

## Step C — propagate exact/identity terms first

Populate all `IDENTITY-ALLOCATABLE` terms before adding process models.

## Step D — add model-conditional terms with model discrepancy

Examples:

- Hansen composition/temperature wavelength;
- ideal Planck background;
- one-carrier self-heating screening;
- one-pole detector bandwidth.

Every model term requires:

- domain;
- operating point;
- parameter uncertainty;
- validation status;
- model discrepancy term.

## Step E — stop at the empirical boundary

Do not continue a chain through an unsupported derivative.

Create an `EMPIRICAL-JACOBIAN-REQUIRED` row instead.

## Step F — back-solve metrology need from the final decision

For a simple one-term contribution:

`u_x <= u_y/|J|`

or in relative form

`u_r(x) <= g_y/|S|`.

For multiple terms use covariance propagation or a stated bounded allocation.

## Step G — compare allocation with P16C/P16D capability

For each metrology/control term record:

- required standard/expanded uncertainty;
- actual calibrated uncertainty;
- current acceptance state;
- uncertainty-to-decision-margin ratio;
- whether improvement is required before HgCdTe qualification.

## Step H — verify at detector level

A numerical intermediate limit is not mature until changing/observing that intermediate variable produces the expected detector response within uncertainty.

---

# 6. D*/NEP integration rules

Use the detailed derivations in the Round-43 calculation file.

Key rules:

1. `D*` responsivity and noise terms have equal first-order magnitude.
2. A common linear voltage gain can cancel exactly if P11 and P12 use the same path/frequency/state.
3. The active-area sensitivity is `0.5-gamma_A`, not automatically `+0.5`.
4. Gap `L` affects D* through area, optical power convention and field-dependent `R_v/e_n`.
5. Noise electronics subtraction becomes ill-conditioned as electronics approaches detector noise.

### Required P11/P12 joint record

- signal path/revision;
- noise path/revision;
- common/different gain stages;
- signal frequency;
- noise-evaluation frequency;
- detector impedance/loading;
- gain-ratio uncertainty;
- area convention;
- power/irradiance convention;
- covariance terms retained/cancelled.

Do not create two independent gain uncertainty terms when the same physical gain cancels.

---

# 7. Geometry / field / self-heating allocation

P10 shall supply measured:

- `L`, `W`, active-area geometry;
- `V_active`, not merely source voltage;
- current;
- package temperature state/proxy;
- contact/series correction;
- field-dependent `R_v(E)` and `e_n(E)` slopes near the canonical point.

The key missing derivatives are

`s_R,E = partial ln R_v/partial ln E`

and

`s_n,E = partial ln e_n/partial ln E`.

Once measured, P20A can evaluate the effective D* gap sensitivity

`S_D,L = 0.5 - gamma_L - s_R,E + s_n,E`

for a fixed-voltage perturbation model.

### Self-heating

Prefer direct measured power `P=VI` for uncertainty reporting.

The one-carrier `P∝E^2` relation remains a screening model until validated.

A quantitative field tolerance cannot be released until a detector-temperature or detector-response stability requirement establishes how much `DeltaT` is acceptable.

---

# 8. Radiometry allocation

P11 uncertainty shall be decomposed into at least:

- reference detector calibration;
- reference/DUT electrical signal ratio;
- wavelength calibration;
- spectral bandwidth/convolution;
- substitution/position/beam profile;
- source drift;
- modulation/amplitude convention;
- atmosphere/purge;
- window/filter transmission;
- incident-power convention;
- active-area/aperture geometry.

### Background-loaded/BLIP measurements

The 300-K/60-degree/4.4-um scalar model is retained only as a sensitivity diagnostic.

A final BLIP uncertainty budget should integrate:

`source radiance x view factor x window/filter transmission x measured spectral response`

over wavelength and geometry.

Do not assign a 4.4-um step-boundary tolerance as though it were a fabricated detector cutoff requirement.

---

# 9. Noise allocation

P12 shall propagate:

- analyzer/ADC scale;
- complex preamp transfer;
- source impedance/loading;
- PSD/ASD normalization and ENBW;
- averaging/statistical estimator uncertainty;
- stationarity/drift;
- electronics floor and its subtraction condition number;
- detector temperature/field/background uncertainty;
- frequency alignment with P11.

### Conditioning requirement

For

`beta=e_elec^2/e_det^2`,

record `beta` at the D* frequency and the resulting sensitivities:

- measured-ASD sensitivity `1+beta`;
- electronics-ASD sensitivity `beta` in magnitude.

A selected `beta` threshold is an engineering allocation and must be justified by the final D* uncertainty budget, not by convention.

---

# 10. Temporal allocation

P13 uncertainty has three layers:

1. measurement noise/statistical fit uncertainty;
2. de-embedding transfer-function uncertainty;
3. model discrepancy/non-one-pole/package-coupling uncertainty.

Do not report layer 1 alone as lifetime uncertainty.

For a validated one-pole response:

`u_r(f3dB)=u_r(tau)`

for the same fitted pole before adding model discrepancy.

Near the corner, amplitude and phase sensitivities from the Round-43 calculation can be used to size SNR/phase precision.

The extracted detector transfer must include uncertainty from source, optics, bias/readout, cable/instrument and package transfer.

---

# 11. Material-state uncertainty chain

The upstream material chain is deliberately stopped at known boundaries.

## Exact/controlled metrology links

- source masses -> nominal `xL,yL` under frozen atomic weights;
- FTIR wavelength scale/fit -> measured optical quantities;
- Hall voltage/current/B/geometry -> Hall observables under the selected reduction.

## Model-conditional

- Hansen `x,T -> lambda_Eg`;
- one-carrier Hall interpretation where valid.

## Empirical-required

- LPE `{xL,yL,TL,DeltaT_SC,t,inventory,Hg-loss}` -> `{xS,d,morphology}`;
- anneal trajectory -> `{carrier sign,n,mu,tau}`;
- final material state -> detector `R_v,e_n,tau` after complete processing.

Therefore a complete numerical `charge/temperature -> D*` budget cannot be produced before P21/P23 and matched detector data exist.

---

# 12. Current high-value empirical Jacobians

## J43-01 — field dependence at canonical detector state

Measure around `80 K`, `10 V/cm`, matched package/background:

`partial ln R_v/partial ln E`

`partial ln e_n/partial ln E`.

This closes geometry/bias coupling in D*.

## J43-02 — LPE response

P21:

`{xL,yL,TL,DeltaT_SC,t,inventory,source-use} -> {x,d,uniformity,morphology}`.

## J43-03 — Hg anneal state

P23:

`{T_s(t),T_Hg(t),dwell,cooldown,start state} -> {carrier sign,n,mu,tau}`.

Do not linearize across p/n conversion.

## J43-04 — blocking contact/passivation

`{Ns,dconv,Lconv,damage,oxide/sidewall state} -> {R_v,e_n,tau,D*}`.

Likely requires transport model + matched DOE.

## J43-05 — package dynamics

`{bondline,carrier,vacuum,interconnect,geometry} -> {R_th,H_pkg(f),noise/microphonics}`.

Required before detector lifetime is separated cleanly from package recovery.

---

# 13. Allocation priority metric

For a known normalized sensitivity `S_i` and current relative standard uncertainty `u_r(x_i)`, define the first-order contribution magnitude

`C_i = |S_i| u_r(x_i)`.

Where covariance is material, use the full covariance contribution rather than ranking individual `C_i` values independently.

Priority should consider:

- contribution to final decision uncertainty;
- cost/destructiveness of improving the term;
- whether the term is calibratable or process-intrinsic;
- information value of resolving an empirical derivative;
- reworkability/correctability.

The largest mathematical sensitivity is not automatically the highest-value experiment.

---

# 14. Metrology adequacy criterion

Round 42 introduced a general decision-discrimination rule:

`U_X < DeltaX_decision/2`

as minimum logical discriminability and approximately

`U_X <= DeltaX_decision/4`

as a preferred engineering target where practical.

Round 43 applies this only **after** `DeltaX_decision` is derived from a detector/system requirement or a justified experimental contrast.

Do not reverse the logic and create a process tolerance from an instrument's available uncertainty.

---

# 15. P16E integration

P16E is the first-build cross-system uncertainty summary.

It does not replace the detailed P20 allocation record.

P16E shall show, for every critical decision:

- final requirement status;
- exact/model/empirical sensitivity status;
- key covariance/common-path terms;
- required metrology uncertainty if derivable;
- actual P16C/P16D capability when a laboratory exists;
- residual empirical Jacobian;
- disposition.

New integration state:

`P16E-REQUIREMENTS-ALLOCATION-COMPLETE`.

It may be `YES` only when every first-build decision has either:

1. a justified numerical requirement and complete allocation; or
2. an explicit statement that no numeric limit is required before first build and a controlled qualification decision rule exists.

A `YES` P16E state does not imply P16A/P16C/P16D/P17 maturity.

---

# 16. What remains open after Round 43

The project still lacks the system-level tolerance/uncertainty objectives needed to turn many parameterized formulas into numbers.

Especially open:

- acceptable D* comparison uncertainty/deviation from the historical benchmark;
- acceptable responsivity/NEP uncertainty;
- final detector-temperature-rise criterion;
- acceptable response-edge/cutoff uncertainty and convention;
- required lifetime/bandwidth and uncertainty;
- acceptable background-flux uncertainty for BLIP verification;
- empirical process-to-detector Jacobians.

These are not filled by choosing arbitrary 1%, 5% or 10% bands.

---

# 17. Permanent Round-43 discipline

- Prefer cancellation/common-path calibration where the equations permit it.
- Treat active area and optical power as one coupled metrology problem.
- Treat gap and field as one coupled state-setting problem.
- Treat P11/P12 as one D* measurement system, not two independent experiments.
- Treat P13 fit/de-embedding/model uncertainty separately.
- Stop propagation at every empirical Jacobian boundary.
- Parameterize open requirements rather than inventing tolerances.
- Promote to P17 only after detector-level verification.
