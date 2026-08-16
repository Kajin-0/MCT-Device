# Recovery checkpoint — round 13 analytical sensitivity / requirements allocation

**Date:** 2026-08-16 America/New_York

**Purpose:** Fast handoff after converting P19 traceability into a first analytical sensitivity matrix and a controlled numerical requirements-allocation method.

Read after `AGENTS.md` and the round-12 checkpoint.

---

## 1. New files

Round 13 adds:

- `calculations/RP01_FIRST_ORDER_SENSITIVITY_MATRIX.md`
- `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`
- `travelers/P20_REQUIREMENTS_ALLOCATION_REGISTER.md`
- this checkpoint.

No new historical process setpoint was claimed in this round.

The purpose is to determine **which tolerances can be derived, which are only model-dependent, and which require local fabrication/device data**.

---

## 2. New sensitivity evidence classes

P20 requires every numerical derivative to be tagged:

- `IDENTITY` — exact derivative of a controlled equation/definition;
- `MODEL-CONDITIONAL` — exact within a stated model whose adequacy must be tested;
- `PROXY-CONDITIONAL` — order-of-magnitude chain containing an unverified differential/model substitution;
- `EMPIRICAL-REQUIRED` — apparatus/process/device-specific derivative requiring DOE or validated model.

A `PROXY-CONDITIONAL` relation may size an experiment but cannot define a production tolerance.

This is now a non-negotiable continuity rule.

---

## 3. Exact D* / NEP sensitivity block

From P12:

`NEP = e_n/R_v`

`D* = R_v sqrt(A)/e_n`.

Exact normalized sensitivities:

- `S_D*,R = +1`;
- `S_D*,e = -1`;
- `S_D*,A = +0.5`;
- `S_NEP,e = +1`;
- `S_NEP,R = -1`.

Consequences:

- responsivity and detector-referred noise calibration have equal first-order fractional leverage on D*;
- active area has half the fractional leverage;
- P11/P12 must be designed as one uncertainty chain;
- historical 24.5 nV/sqrtHz cannot be substituted automatically into a 1-kHz D* reproduction because 1 kHz is below the historical ~3-kHz 1/f knee.

No D* production tolerance was created because the project has not yet defined an allowed reproduction band around the historical ~2e11 value.

---

## 4. DC field / self-heating leverage

For the P10 uniform one-carrier screening model:

`R_bulk = L/(q n mu W d)`

`I = q n mu E W d`

`P_J = q n mu E^2 W d L`.

Normalized sensitivities include:

- `R_bulk`: +1 to L and -1 to each of n, mu, W, d;
- `P_J`: +2 to E;
- `P_J`: +1 to n, mu, W, d, L.

Thus electric-field error has quadratic leverage on ideal Joule power.

A 1% E error gives approximately a 2% P error before electrothermal feedback.

This strengthens P10's requirement to use actual active-region voltage and measured gap rather than nominal source voltage/mask geometry.

---

## 5. Hansen composition sensitivity quantified

At nominal `x=.30`, `T=80 K`, using the controlled Hansen relation:

- `Eg=0.243684 eV`;
- `lambda_Eg=5.08791 um`;
- `partial Eg/partial x=1.58304 eV/x`;
- `partial lambda_Eg/partial x=-33.0525 um/x`;
- therefore `Delta x=+0.001` gives local `Delta lambda_Eg≈-33.1 nm`;
- `partial lambda_Eg/partial T≈-4.47 nm/K`;
- normalized `S_lambda,x≈-1.949`.

Critical restriction retained:

**this is the band-gap-equivalent wavelength, not detector cutoff.**

RP-01's measured response cutoff is ~4.4 um while nominal Hansen `lambda_Eg` is ~5.09 um. Therefore the repository still cannot derive an x production tolerance directly from the historical cutoff.

Required next empirical derivative:

`partial lambda_response / partial x_P06`.

---

## 6. LPE balance/charge-size proxy connected to wavelength scale

The existing LPE charge-sensitivity calculation gives the following +0.1-mg Cd-error scale:

| Total charge | proxy `delta xS` | Hansen `delta lambda_Eg` proxy |
|---:|---:|---:|
| 1 g | `+2.131e-3` | `-70.4 nm` |
| 2 g | `+1.066e-3` | `-35.2 nm` |
| 5 g | `+4.248e-4` | `-14.0 nm` |
| 10 g | `+2.131e-4` | `-7.04 nm` |

This is intentionally labeled `PROXY-CONDITIONAL` because:

1. the tabulated `xS/xL=3.54` ratio is not proven to equal the local derivative `dxS/dxL`;
2. Hansen `lambda_Eg` is not detector cutoff.

The table only demonstrates why charge mass and Cd weighing capability can become important. It does not release a balance specification.

---

## 7. One-pole temporal sensitivity / 1-kHz plateau criterion

For a validated one-pole detector:

`f_3dB=1/(2 pi tau)`

so

`S_f3dB,tau=-1`.

At fixed frequency,

`partial ln|H|/partial ln(tau) = -z^2/(1+z^2)`

with `z=f/f_3dB`.

P20 now includes a lookup for how far the intrinsic pole must lie above the 1-kHz measurement if a plateau approximation is desired:

- <5% amplitude attenuation -> `f_3dB >3.04 kHz`;
- <2% -> `>4.92 kHz`;
- <1% -> `>7.02 kHz`;
- <0.5% -> `>9.96 kHz`;
- <0.1% -> `>22.34 kHz`.

These are mathematical one-pole criteria, not RP-01 bandwidth specifications. P13 must first validate the model.

---

## 8. Major radiometry finding — 300-K background is highly sensitive

The existing idealized RP-01 background model is

`Phi = pi sin^2(theta) integral N_lambda(T) d(lambda)`

with step upper boundary 4.4 um and 60-degree full cone (`theta=30 degrees`).

New local derivatives at 300 K are:

### Blackbody temperature

`partial ln Phi/partial T≈0.04027 K^-1`

or about **4.03% flux per kelvin**.

Normalized sensitivity:

`S_Phi,T≈12.08`.

### Effective long-wave step boundary

`partial ln Phi/partial lambda_c≈2.0638 per um`.

Thus +0.01 um shifts ideal flux by about +2.06% locally.

Normalized sensitivity:

`S_Phi,lambda_c≈9.081`.

### FOV

For `Phi∝sin^2(theta)` at 30-degree half-angle:

`S_Phi,theta≈1.814`.

A +1-degree **full-cone** change around 60 degrees changes ideal flux by about +3.04%.

### One-term 1% diagnostic scales

If one term alone were allowed to contribute 1% relative uncertainty in this idealized flux:

- source T would need approximately `uT<=0.248 K`;
- full cone angle approximately `uTheta<=0.331 degree`;
- effective step boundary approximately `u_lambda<=4.85 nm`.

These are **not specifications**. They show that the scalar historical shorthand `300 K / 60 degrees / 4.4 um` is too sensitive for precision BLIP reconstruction.

P11/P12 should use calibrated source radiance, physical aperture/view factor and measured spectral weighting rather than an ideal step cutoff.

---

## 9. Thickness leverage cannot yet be assigned from 9.5 um alone

For the simple model

`eta_abs=1-exp(-alpha d)`

normalized thickness sensitivity is

`S_eta,d = alpha d/[exp(alpha d)-1]`.

It approaches:

- 1 in the optically thin limit;
- 0.582 at `alpha d=1`;
- 0.313 at `alpha d=2`;
- 0.157 at `alpha d=3`;
- 0 when optically thick.

Therefore historical `d=9.5 um` does not imply a particular thickness tolerance. P06 must establish the actual alpha/lambda/x/T optical state first.

---

## 10. RIE depth/density identity retained

For a uniform converted layer representation:

`n_conv=Ns/dconv`.

Therefore:

- `S_n,Ns=+1`;
- `S_n,dconv=-1`.

This is only the density-reduction identity. It does not give detector sensitivity to conversion depth.

The detector-level block remains:

`{Ns,dconv,Lconv,transport profile,Sc} -> {R(E),e_n(E),tau(E),D*(E)}`

and requires 2-D modeling and/or matched-device DOE.

---

## 11. First leverage ranking

This is a **physics/measurement leverage ranking**, not a released process-tolerance ranking.

### Direct or model-quantified high leverage

1. background radiometry near the historical condition: `T`, spectral weighting/boundary, FOV;
2. electric field -> Joule power (`E^2`);
3. composition -> band-gap-equivalent wavelength (`|S|≈1.95` at x=.30/80K);
4. responsivity and detector noise -> D* (`|S|=1` each);
5. n/mu/geometry -> resistance/current (order unity);
6. tau -> one-pole bandwidth (`|S|=1`);
7. area -> D* (`0.5`).

### Potentially high-leverage fabrication blocks with no valid scalar number yet

- P04 anneal trajectory -> carrier type/n/mu/lifetime;
- P08 contact converted state -> sweepout/noise/bandwidth;
- P02/P02C passivation -> 1/f/surface recombination/lifetime;
- P03 source/thermal/inventory -> x/thickness/morphology;
- P15 package -> Rth/parasitics/noise/bandwidth.

Do not call these lower leverage simply because their Jacobians are still open.

---

## 12. P20 allocation rule

For small bounded worst-case relative budgets:

`sum |S_i| b_i <= b_y`.

For standard uncertainty with correlations:

`Sigma_y ≈ J Sigma_x J^T`.

P20 explicitly forbids equal allocation by default. Budget based on:

- physics leverage;
- achievable metrology/control;
- covariance/interactions;
- cost/destructiveness;
- downstream detectability;
- rework risk.

P17 capability follows **after** a P20 engineering specification exists.

---

## 13. Highest-value empirical Jacobian work now identified

Recommended order:

1. **P03/P06:** actual source/liquidus/supercooling/time/inventory -> x, thickness, optical edge;
2. **P04/P05/P13:** anneal sample/reservoir/pHg/dwell/cooldown trajectory -> carrier state, mobility, lifetime;
3. **P08/P10/P12/P13:** blocking-contact profile -> sweepout, noise, bandwidth, D*;
4. **P02/P02C/P12/P13:** passivation/sidewall state -> 1/f, lifetime, responsivity;
5. **P15/P10/P13:** package thermal/parasitic state -> self-heating/noise/bandwidth.

This is the strongest next analytical/research branch before production tolerances are attempted.

---

## 14. Project architecture after round 13

The repository now has five integration layers:

1. **P01–P16:** fabrication/material/device methods + master traveler;
2. **P17:** measurement-system/statistical capability/release/change control;
3. **P18:** failure analysis/corrective action;
4. **P19:** detector-requirement -> physics -> process traceability;
5. **P20:** analytical/empirical sensitivity and numerical requirements allocation.

No end-to-end `REPRODUCIBLE-RELEASE` exists because local repeated fabrication data still do not exist.

---

## 15. Next logical work

The strongest technical continuation is **not** another generic archival search.

Proceed by closing the first empirical Jacobian block:

### P03/P06 upstream response surface

Build the analytical/DOE framework for

`{xL,yL,actual TL,DeltaT_SC,t_growth,melt inventory/source-use/Hg-loss state} -> {xS,thickness,uniformity,optical edge}`.

This directly closes the currently missing link between:

- detector spectral requirement;
- x tolerance;
- liquid/source composition tolerance;
- temperature uncertainty;
- balance/charge-mass requirement;
- growth-time window.

After that, repeat the same allocation approach for P04 anneal and P08 blocking contacts.

Manual assembly can occur after or in parallel, but must preserve all `EMPIRICAL-REQUIRED` flags.

---

## 16. Recovery order

1. `AGENTS.md`
2. this checkpoint
3. `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`
4. `calculations/RP01_FIRST_ORDER_SENSITIVITY_MATRIX.md`
5. `travelers/P20_REQUIREMENTS_ALLOCATION_REGISTER.md`
6. `procedures/P19_REQUIREMENTS_TRACEABILITY_MATRIX.md`
7. P17/P18 integration
8. branch-specific P03/P04/P08/P11/P12/P13 files.
