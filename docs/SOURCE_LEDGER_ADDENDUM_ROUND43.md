# Source ledger addendum — Round 43 integrated uncertainty / requirements allocation

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Scope

Round 43 did not perform a new generic literature search. It integrated the already controlled P10–P13 metrology equations, P19/P20 requirements framework, first-order sensitivity calculations, and Round-41/42 capability/acceptance architecture into a covariance-aware first-build uncertainty package.

New controlled artifacts:

- `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`;
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`;
- `travelers/P16E_FIRST_BUILD_UNCERTAINTY_ALLOCATION_REGISTER.md`.

No numerical fabrication tolerance was created from a historical nominal value.

---

## S43-01 — P20 analytical sensitivity framework

Controlled source:

- `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`;
- `travelers/P20_REQUIREMENTS_ALLOCATION_REGISTER.md`.

**Class:** `CONTROLLED-ANALYTICAL-ALLOCATION-FRAMEWORK`.

Round-43 use:

- retained the requirement-first rule;
- retained sensitivity classes `IDENTITY`, `MODEL-CONDITIONAL`, `PROXY-CONDITIONAL`, `EMPIRICAL-REQUIRED`;
- retained full covariance propagation `Sigma_y≈J Sigma_x J^T`;
- converted the generic framework into first-build-specific allocation records.

Permanent result:

`measurement uncertainty != physical state uncertainty != process variation != engineering tolerance`.

---

## S43-02 — first-order sensitivity matrix

Controlled source:

- `calculations/RP01_FIRST_ORDER_SENSITIVITY_MATRIX.md`.

Retained exact/model entries include:

- `D*`: `S_Rv=+1`, `S_en=-1`, `S_A=+0.5` under the direct-power convention;
- `NEP`: `S_en=+1`, `S_Rv=-1`;
- `E=V/L`;
- one-carrier `P_J` field sensitivity `+2`;
- Hansen `lambda_Eg` sensitivities at x=.30/80 K;
- one-pole `S_f3dB,tau=-1` after model validation;
- idealized 300-K background sensitivities to T, cone and effective spectral boundary.

Round-43 extension:

- made covariance/common-path cancellation explicit;
- generalized active-area sensitivity for power versus irradiance conventions;
- derived gap/field/D* coupling;
- derived electronics-subtraction conditioning;
- converted several entries into parameterized uncertainty back-solves.

No evidence class was promoted.

---

## S43-03 — P10 geometry/bias/self-heating

Controlled source:

- `procedures/P10_DEVICE_DC_BIAS_SELF_HEATING.md`;
- P10A transfer/register lineage.

Direct/controlled equations retained:

`E=V_active/L`

`P=V_active I`.

P10 already requires measured active gap and active-region voltage and gives the independent-error relation for field uncertainty.

Round-43 new integration result:

For `A=WL`, fixed physical V, optical-power gap exponent `gamma_L`, and local field sensitivities

`s_R,E=partial ln R_v/partial ln E`

`s_n,E=partial ln e_n/partial ln E`,

the effective gap sensitivity of D* is

`S_D,L = 0.5 - gamma_L - s_R,E + s_n,E`.

**Class:** algebraic identity plus `EMPIRICAL-REQUIRED` field slopes.

This means contact-gap metrology is not an isolated area-normalization term.

---

## S43-04 — P11 absolute responsivity/radiometry

Controlled source:

- `procedures/P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md`;
- P11A transfer register/lineage.

Retained comparison equation:

`R_DUT=(V_DUT/V_ref)R_ref`.

Round-43 use:

- decomposed signal/reference/calibration uncertainty;
- required covariance for common source/gain/position paths;
- coupled active-area definition to incident-power convention;
- retained exact aperture/spectral weighting as the preferred BLIP path.

New active-area result:

Define `gamma_A=partial ln P_inc/partial ln A`.

Then

`S_D,A=0.5-gamma_A`.

Therefore:

- direct power independent of A -> `+0.5`;
- uniform irradiance with `P=H A` -> `-0.5`.

**Class:** `IDENTITY` for the stated measurement conventions.

---

## S43-05 — P12 noise/PSD/D*

Controlled source:

- `procedures/P12_NOISE_PSD_NEP_DETECTIVITY.md`;
- P12A/P12B/P12C and noise-chain register lineage.

Retained:

`e_det=sqrt(e_meas^2-e_elec^2)`

when PSD contributions are independent and loading assumptions hold.

Round-43 derived conditioning variable:

`beta=e_elec^2/e_det^2`.

Then

`partial ln e_det/partial ln e_meas=1+beta`

and

`partial ln e_det/partial ln e_elec=-beta`.

This quantifies how electronics-floor subtraction becomes ill-conditioned.

At the Round-41 example `beta=.10`, the local sensitivities are `1.10` and `-0.10`; this remains an engineering example, not an RP-01 criterion.

---

## S43-06 — common gain cancellation across P11/P12

Controlled inputs:

- P11 detector-terminal responsivity reduction;
- P12 detector-terminal noise reduction.

If one common linear gain `G` applies at the same frequency/loading:

`R_v=(S_sig/G)/P_inc`

`e_n=e_out/G`.

Therefore

`D*=S_sig sqrt(A)/(P_inc e_out)`.

The common gain cancels exactly.

**Class:** `IDENTITY` under the stated common-path assumptions.

If paths differ, only `G_noise/G_signal` remains.

Permanent Round-43 rule:

Do not RSS-count a common gain twice.

---

## S43-07 — ideal background sensitivity diagnostic

Controlled source:

- `calculations/RP01_300K_BACKGROUND_FLUX_CHECK.md`;
- first-order sensitivity matrix.

At the idealized RP-01-like point:

- `partial ln Phi/partial T≈0.04027 K^-1`;
- full-cone sensitivity around 60° ≈`0.0304 degree^-1`;
- `partial ln Phi/partial lambda_c≈2.0638 um^-1`.

Round-43 parameterized back-solves:

For one term alone and desired relative background uncertainty `g_Phi`:

- `u_T<=g_Phi/0.04027`;
- `u_Theta<=g_Phi/0.0304 degree`;
- `u_lambda<=g_Phi/2.0638 um`.

Example for `g_Phi=1%`:

- ~0.248 K;
- ~0.329° full cone;
- ~4.85 nm step-boundary equivalent.

**Class:** `MODEL-CONDITIONAL / DIAGNOSTIC`.

These numbers demonstrate why the scalar cutoff approximation should not be the final BLIP uncertainty model.

---

## S43-08 — Hansen screening back-solve

Controlled source:

- `HANSEN_BANDGAP_MODEL.md`;
- first-order sensitivity matrix.

At x=.30/80 K:

- `partial lambda_Eg/partial x=-33.0525 um/x`;
- `partial lambda_Eg/partial T=-0.004468 um/K`.

Round-43 examples for **band-gap-equivalent wavelength only**:

- 10-nm one-term uncertainty -> `u_x≈3.03e-4` or `u_T≈2.24 K`;
- 5-nm -> `u_x≈1.51e-4` or `u_T≈1.12 K`.

**Class:** `MODEL-CONDITIONAL`.

These are not response-cutoff production tolerances.

---

## S43-09 — P13 temporal/de-embedding

Controlled source:

- P13/P13A.

For a validated one-pole detector:

`f3dB=1/(2 pi tau)`

so relative uncertainty transfers one-for-one between the same physical pole's `f3dB` and `tau` before model discrepancy.

At the corner:

- logarithmic amplitude slope = `-1/2`;
- phase slope = `-0.5 rad` per relative-log frequency.

Thus local instrument-design checks are approximately:

`u_r(f3dB)≈2 u_r(|H|)` from amplitude alone near the corner;

`u_r(f3dB)≈2 u_phi` with `u_phi` in radians from phase alone.

**Class:** `MODEL-CONDITIONAL` until one-pole adequacy/de-embedding is validated.

Fit statistics alone remain insufficient.

---

## S43-10 — fabrication Jacobian boundary

Controlled P20 result retained:

No defensible detector-level numerical derivative is currently released for:

- LPE controls -> x/thickness/morphology;
- anneal path -> carrier state/mobility/lifetime;
- mesa/passivation -> 1/f/responsivity/lifetime;
- RIE/contact profile -> sweepout/noise/D*/bandwidth;
- package construction -> thermal/dynamic detector behavior.

**Class:** `EMPIRICAL-JACOBIAN-REQUIRED`.

Round 43 does not bridge these gaps with handbook estimates.

---

## S43-11 — parameterized equal-variance D* examples

The Round-43 calculation includes a deliberately non-release planning example.

If `R_v`, `e_n` and direct-power area contributions are independent and assigned equal variance, for desired D* relative standard uncertainty `g_D`:

- `u_r(R_v)=g_D/sqrt(3)`;
- `u_r(e_n)=g_D/sqrt(3)`;
- `u_r(A)=2g_D/sqrt(3)`.

Examples range from a 10% to 1% total planning target.

**Class:** `DESIGN-CHECK`.

Equal allocation is not a physics requirement and must not replace actual covariance-aware optimization.

---

## Source-search disposition

Round 43 used controlled repository equations and evidence only. No new public source family was required because the unresolved issue was analytical allocation, not historical documentary identity.

Generic literature searching remains low priority unless a new source directly closes a historical process identity or a missing physical response derivative with transferable primary data.
