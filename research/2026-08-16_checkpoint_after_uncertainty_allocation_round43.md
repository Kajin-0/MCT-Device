# Research checkpoint — after integrated uncertainty / requirements allocation Round 43

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 43 began from the Round-42 conclusion that the project had a capability envelope and a subsystem acceptance architecture, but still lacked a quantitative answer to:

> How accurate must each measurement/control coordinate be to support the final detector decision, and where is such a number impossible until an empirical HgCdTe response Jacobian exists?

The round therefore built a covariance-aware first-build uncertainty / requirements-allocation layer.

No vendor was selected. No physical measurement was invented. No historical nominal value was converted automatically into a process tolerance.

---

## 2. New controlled artifacts

Created:

- `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`;
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`;
- `travelers/P16E_FIRST_BUILD_UNCERTAINTY_ALLOCATION_REGISTER.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND43.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND43.md`;
- this checkpoint.

AGENTS is refreshed at the end of the round.

---

# 3. New integration concept — P16E

P16A–P16E now answer different questions:

1. **P16A:** is a complete first build executable without undocumented irreversible choices?
2. **P16B:** which evidence-ranked process branch should be pursued?
3. **P16C:** does a real laboratory have the required physical capability?
4. **P16D:** has that infrastructure passed controlled IQ/OQ/surrogate acceptance?
5. **P16E:** are the first-build measurement/control uncertainties and requirements allocated well enough to support the decisions being made?

New integration state:

`P16E-REQUIREMENTS-ALLOCATION-COMPLETE`.

Current:

`NO`.

This state is independent of P16A/P16C/P16D/P17 maturity.

---

# 4. Round-43 allocation states

Added:

- `REQUIREMENT-DEFINITION-OPEN`;
- `IDENTITY-ALLOCATABLE`;
- `MODEL-CONDITIONAL-ALLOCATABLE`;
- `COVARIANCE-REQUIRED`;
- `EMPIRICAL-JACOBIAN-REQUIRED`;
- `PARAMETRIC-ALLOCATION-ONLY`;
- `LOCAL-ALLOCATION-DEFINED`;
- `DETECTOR-LEVEL-VERIFIED`;
- `READY-FOR-P17`.

The important distinction is that a formula may be fully allocatable while the numerical target remains open because the final detector/system requirement has not been specified.

---

# 5. Major result 1 — common gain cancels from D* when the path is truly common

P11/P12 give

`R_v=(S_sig/G)/P_inc`

and

`e_n=e_out/G`.

If the same linear voltage gain `G` applies at the same frequency and loading state,

`D*=S_sig sqrt(A)/(P_inc e_out)`.

The common gain cancels exactly.

This is a real metrology simplification and a warning against double-counting one calibration uncertainty twice.

If signal and noise use different paths, only the gain ratio `G_noise/G_signal` remains.

**New design rule:** whenever possible, make P11/P12 share the same detector-terminal transfer state at the canonical 1-kHz D* point.

---

# 6. Major result 2 — active-area sensitivity changes with the optical-power convention

Write

`D*=V_sig sqrt(A)/(P_inc e_n)`

and define

`gamma_A=partial ln P_inc/partial ln A`.

Then

`S_D,A=0.5-gamma_A`.

Therefore:

- direct total-power calibration independent of A -> `S_D,A=+0.5`;
- uniform irradiance with `P_inc=H A` using the same area -> `S_D,A=-0.5`.

Thus the familiar `+0.5` area sensitivity is **not universal**.

This makes the P10/P11/P12 active-area convention a first-class uncertainty coordinate rather than a documentation detail.

---

# 7. Major result 3 — contact gap couples D* normalization and physical bias state

For `A=WL`, fixed physical active voltage and optical-power exponent `gamma_L`, define local field sensitivities:

`s_R,E=partial ln R_v/partial ln E`

`s_n,E=partial ln e_n/partial ln E`.

Because `E=V/L`,

`S_D,L=0.5-gamma_L-s_R,E+s_n,E`.

Consequences:

- the gap does not enter D* only through `sqrt(A)`;
- a gap error changes actual electric field;
- responsivity and noise are known to depend on field;
- the effective gap sensitivity can be larger, smaller or opposite-sign depending on the local field slopes and optical-power convention.

The next local detector experiment needed for this part is a matched P10/P11/P12 determination of `s_R,E` and `s_n,E` near 80 K / 10 V/cm.

---

# 8. Major result 4 — electronics subtraction has an exact condition number

For P12:

`e_det=sqrt(e_meas^2-e_elec^2)`.

Define

`beta=e_elec^2/e_det^2`.

Then

`partial ln e_det/partial ln e_meas=1+beta`

and

`partial ln e_det/partial ln e_elec=-beta`.

This provides an exact local conditioning metric.

Examples:

- `beta=.10`: sensitivities 1.10 and -0.10;
- `beta=1`: 2 and -1;
- `beta=4`: 5 and -4.

Thus subtraction becomes rapidly fragile as the electronics floor approaches/exceeds the detector noise.

Round 41's example `beta=.10` / electronics ASD ≈0.316 detector ASD remains a useful engineering design point, but not an RP-01 criterion.

---

# 9. Major result 5 — D* uncertainty should be covariance-aware, not three independent percentages

Exact first-order relation:

`delta ln D*=delta ln R_v + 0.5 delta ln A - delta ln e_n`.

The covariance terms matter because:

- common gain can cancel;
- area can enter the optical-power denominator;
- gap controls field;
- detector T/E perturbations can move Rv and noise together.

The Round-43 calculation therefore uses

`u_r(D*)^2=s^T Sigma_r s`

rather than assuming diagonal RSS.

A simple equal-variance D* planning table is retained only as `DESIGN-CHECK`.

For example, if a future goal were `g_D=2%` and the direct-power Rv/noise/area terms were independent/equally allocated, the mathematical planning values would be approximately:

- Rv 1.15%;
- noise 1.15%;
- area 2.31%.

This is not a recommendation or released requirement.

---

# 10. Background-radiometry result

The existing idealized 300-K/60-degree/4.4-um model has very high sensitivity:

- ~4.027%/K source temperature;
- ~3.04% per degree of full cone around 60°;
- ~2.064% per 0.01 um of step spectral boundary.

For a one-term 1% flux uncertainty, the diagnostic scales are approximately:

- 0.248 K;
- 0.329° full cone;
- 4.85 nm effective step-boundary wavelength.

This does **not** motivate a 4.85-nm detector cutoff tolerance. It proves the opposite: a scalar uncertain cutoff is a poor precision radiometric boundary.

Final BLIP work must use measured spectral weighting and physical aperture/view factor.

---

# 11. Hansen screening result

At x=.30/80 K:

`partial lambda_Eg/partial x=-33.0525 um/x`

`partial lambda_Eg/partial T=-0.004468 um/K`.

One-term model screening examples:

- 10-nm `lambda_Eg` uncertainty -> `u_x≈3.03e-4` or `u_T≈2.24 K`;
- 5-nm -> `u_x≈1.51e-4` or `u_T≈1.12 K`.

These remain `MODEL-CONDITIONAL` and do not apply directly to the measured ~4.4-um response cutoff.

The production-relevant response-edge derivative is still missing.

---

# 12. Temporal uncertainty result

After one-pole validation:

`u_r(f3dB)=u_r(tau)`

for the same physical fitted pole before model discrepancy.

At the corner, one-pole local sensitivities imply approximately:

- relative corner-frequency uncertainty ≈2x relative amplitude uncertainty from amplitude alone;
- relative corner-frequency uncertainty ≈2x phase uncertainty in radians from phase alone.

These are instrument/fit design relations only.

The full lifetime budget must include:

- source transfer;
- optics/reference;
- bias/readout;
- cable/instrument;
- package thermal transfer;
- model discrepancy.

Fit covariance alone is not lifetime uncertainty.

---

# 13. What is analytically allocatable now

Substantially closed at the equation level:

- `E=V/L`;
- `A=WL` once convention is declared;
- `P=VI`;
- spectral comparison ratio;
- NEP;
- D*;
- common-gain covariance/cancellation;
- electronics subtraction condition number;
- model-conditional Hansen/background/one-pole screening.

These can be back-solved once a final numeric detector/system requirement is supplied.

---

# 14. What remains empirical

Still cannot be assigned a defensible manufacturing tolerance:

1. LPE controls -> x/thickness/morphology;
2. anneal path -> carrier sign/n/mu/lifetime;
3. mesa/passivation -> responsivity/1/f/lifetime;
4. RIE conversion/contact state -> sweepout/noise/D*/bandwidth;
5. Cr/Au/contact variation -> final detector performance;
6. singulation edge/subsurface state -> noise/responsivity/survival;
7. package construction -> thermal/dynamic detector response.

These are assigned to P21/P23 and matched-device empirical/model work rather than filled with handbook sensitivities.

---

# 15. Project state after Round 43

The project is now:

**branch-selected + capability-specified + acceptance-method-specified + uncertainty-allocation-architecture-defined + not physically instantiated**.

Current states remain:

- `TRACEABLE-FIRST-BUILD-READY = NO`;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`;
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`;
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`;
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`.

The P16E `NO` is expected: several final requirement bands are undefined and the empirical process Jacobians have not been measured.

---

# 16. Strongest next analytical work — Round 44

The analytical bottleneck is no longer generic uncertainty propagation. It is the **missing process-to-material/device Jacobian architecture**.

Round 44 should construct a unified empirical-Jacobian / DOE execution package that prioritizes which derivatives most reduce uncertainty in the final detector decisions.

Strongest blocks:

1. P10/P11/P12 canonical-field local derivatives `s_R,E`, `s_n,E`;
2. P21 LPE response surface around the selected measured liquidus;
3. P23 Hg-anneal state boundary/Jacobian away from the p/n singular region;
4. blocking-contact/passivation vector response into `{Rv,en,tau,D*}`;
5. package thermal/dynamic Jacobian.

The next step should use information value and identifiability, not a generic full-factorial experiment list.

---

## Permanent Round-43 rule

**No final detector requirement means no defensible numerical process tolerance.**

Use exact/covariance-aware parameterized allocations where possible and stop honestly at empirical boundaries.
