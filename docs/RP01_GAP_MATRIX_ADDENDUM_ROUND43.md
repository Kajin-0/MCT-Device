# RP-01 gap matrix addendum — Round 43 uncertainty / requirements allocation

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Purpose

Record what Round 43 analytically closes, what remains parameterized because the detector/system requirement is not yet numerically defined, and which fabrication-to-device sensitivities still require empirical local closure.

New controlled artifacts:

- `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`;
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`;
- `travelers/P16E_FIRST_BUILD_UNCERTAINTY_ALLOCATION_REGISTER.md`.

No P16A readiness state is changed by this addendum.

---

## G43-01 — final detector uncertainty/acceptance objectives

**State:** `REQUIREMENT-DEFINITION-OPEN`.

Historical anchors exist for D*, cutoff, 80-K/10-V/cm operation and noise features, but the repository does not yet contain a justified allowed deviation/uncertainty for:

- `D*(4 um,1 kHz)`;
- absolute responsivity;
- NEP;
- response-edge/cutoff convention and uncertainty;
- detector lifetime/bandwidth;
- allowable detector self-heating;
- BLIP/background verification uncertainty.

**Round-43 consequence:** calculations remain parameterized (`g_D`, `g_Phi`, `u_lambda`, etc.) rather than choosing 1%, 5% or 10% arbitrarily.

**Closure:** define the actual reproduction/system decision requirement in P19/P20/P16E.

---

## G43-02 — D*/NEP algebraic propagation

**State:** `IDENTITY-ALLOCATABLE / PARAMETRIC-ALLOCATION-ONLY`.

Exact equations:

`NEP=e_n/R_v`

`D*=R_v sqrt(A)/e_n`.

Full covariance propagation is now explicitly controlled.

**Remaining:** numeric final requirement and actual instrument uncertainties/covariance.

---

## G43-03 — common P11/P12 voltage gain

**State:** `IDENTITY-ALLOCATABLE / COVARIANCE-REQUIRED`.

If signal and noise use the same linear detector-terminal voltage gain at the same frequency/loading, that gain cancels exactly from D*.

**Gap closed:** do not double-count one common gain as two independent uncertainty terms.

**Remaining:** actual future signal/noise path identity and gain-ratio calibration if paths differ.

---

## G43-04 — active-area / optical-power convention

**State:** `CONVENTION-OPEN / IDENTITY-ALLOCATABLE`.

Define

`gamma_A=partial ln P_inc/partial ln A`.

Then

`S_D,A=0.5-gamma_A`.

Direct power gives `+0.5`; uniform irradiance times the same area gives `-0.5`.

**Critical gap:** final active-area and incident-power conventions are still not frozen.

**Closure:** P10/P11/P12 joint geometry/radiometry definition plus beam/aperture evidence.

---

## G43-05 — contact-gap / electric-field / D* coupling

**State:** `COVARIANCE-REQUIRED / EMPIRICAL-JACOBIAN-REQUIRED`.

For fixed physical voltage and `A=WL`:

`S_D,L=0.5-gamma_L-s_R,E+s_n,E`.

The missing local terms are:

`s_R,E=partial ln R_v/partial ln E`

`s_n,E=partial ln e_n/partial ln E`.

**Meaning:** gap uncertainty cannot be budgeted as area-only because it changes physical field and therefore responsivity/noise.

**Closure:** matched P10/P11/P12 field perturbations around the canonical state.

---

## G43-06 — detector-terminal field uncertainty

**State:** `IDENTITY-ALLOCATABLE`.

`E=V_active/L` with covariance retained.

**Remaining:** actual four-terminal/two-terminal voltage transfer, contact/series correction, gap metrology uncertainty and field-control law.

P16C/P16D can close the metrology portion when a real station exists.

---

## G43-07 — power/self-heating uncertainty

**State:** `IDENTITY-ALLOCATABLE` for measured `P=VI`; `MODEL-CONDITIONAL` for one-carrier/electrothermal predictions.

**Remaining:** detector/package thermal transfer, allowed `DeltaT`, electrothermal feedback and field-response stability.

No universal mW or K limit is introduced.

---

## G43-08 — electronics-floor subtraction

**State:** `IDENTITY-ALLOCATABLE`.

For

`beta=e_elec^2/e_det^2`,

local sensitivities are:

- measured ASD: `1+beta`;
- electronics ASD: `-beta`.

This quantifies subtraction conditioning.

**Remaining:** future measured `beta` and actual ASD uncertainties at the D* frequency.

The Round-41 `beta=.10` example remains design-only.

---

## G43-09 — spectral comparator uncertainty

**State:** `IDENTITY-ALLOCATABLE / COVARIANCE-REQUIRED`.

`R_DUT=(V_DUT/V_ref)R_ref` is exact for the declared comparator convention.

**Remaining:** real reference certificate uncertainty, gain/source covariance, wavelength scale, spectral convolution, substitution geometry, atmospheric state, linearity and power convention.

---

## G43-10 — idealized background sensitivity

**State:** `MODEL-CONDITIONAL / DIAGNOSTIC`.

Round 43 parameterizes source-temperature, full-cone-angle and step-boundary uncertainty versus desired relative flux uncertainty.

**Gap not closed:** real BLIP radiometry must use measured spectral response, transmission and physical view factor rather than a scalar cutoff.

No background acceptance tolerance is released.

---

## G43-11 — Hansen composition/temperature back-solve

**State:** `MODEL-CONDITIONAL`.

Band-gap-equivalent wavelength sensitivity can size FTIR/composition work.

**Gap:** detector response edge is not identical to Hansen `lambda_Eg`; production-relevant `partial lambda_response/partial x` remains unresolved.

No x tolerance is released from the historical 4.4-um cutoff.

---

## G43-12 — LPE charge/thermal -> material uncertainty

**State:** `EMPIRICAL-JACOBIAN-REQUIRED`.

Exact source-mass -> nominal `xL,yL` propagation exists.

Still missing:

`partial{xS,d,morphology}/partial{xL,yL,TL,DeltaT_SC,t,inventory,Hg-loss,source-use}`.

**Closure:** P21 local response-surface/Jacobian work with independent process runs.

Do not use tabulated `xS/xL=3.54` as the released differential.

---

## G43-13 — anneal -> electrical/material state uncertainty

**State:** `EMPIRICAL-JACOBIAN-REQUIRED`.

Still missing:

`{T_s(t),T_Hg(t),dwell,cooldown,start state} -> {carrier sign,n,mu,tau}`.

**Closure:** P23 response map, with separate treatment near carrier-type boundary.

A single derivative across p/n conversion is prohibited.

---

## G43-14 — mesa/passivation -> detector performance

**State:** `EMPIRICAL-JACOBIAN-REQUIRED`.

Required local response:

`{mesa profile,oxide/interface state,sidewall trajectory} -> {R_v,e_n,tau}`.

**Closure:** matched-device DOE and P12/P13 correlation.

---

## G43-15 — RIE/contact -> detector performance

**State:** `EMPIRICAL-JACOBIAN-REQUIRED`.

Required:

`{Ns,dconv,Lconv,self-bias,damage,S_c,geometry} -> {sweepout,R_v,e_n,tau,D*}`.

`rho_c` alone remains insufficient.

**Closure:** P24 plus transport/device response study.

---

## G43-16 — Cr/Au/contact transfer uncertainty

**State:** `LOCAL-METROLOGY-ALLOCATABLE / DEVICE-JACOBIAN-REQUIRED`.

Metal thickness/QCM/contact geometry can be measured and uncertainty-budgeted.

The detector consequence of contact/process variation requires TLM + P10/P12/P13 evidence.

---

## G43-17 — temporal/frequency-response uncertainty

**State:** `MODEL-CONDITIONAL-ALLOCATABLE / DEEMBEDDING-OPEN`.

After one-pole validation:

`u_r(f3dB)=u_r(tau)` for the same fitted pole before model discrepancy.

Near the corner, amplitude/phase sensitivities can size measurement precision.

**Gap:** full source/electrical/package complex-transfer uncertainty and model discrepancy remain local.

Fit covariance alone is insufficient.

---

## G43-18 — package thermal/dynamic uncertainty

**State:** `EMPIRICAL-JACOBIAN-REQUIRED`.

Required:

`{bondline,carrier,vacuum,interconnect,optics} -> {R_th,H_pkg(f),noise/microphonics}`.

This is required both for self-heating and for separating package poles from carrier lifetime.

---

## G43-19 — metrology adequacy versus decision margin

**State:** `METHOD-CLOSED / NUMERIC-OPEN`.

Round-42 discrimination rule retained:

`U_X<DeltaX_decision/2`, preferred approximately `<=DeltaX_decision/4` where practical.

Round-43 restriction:

`DeltaX_decision` must first come from a detector/system requirement or deliberate DOE contrast.

Instrument capability must not define the process tolerance by inversion.

---

## G43-20 — P16E project integration

**State:** `NEW-CONTROLLED-REGISTER / NOT PHYSICALLY POPULATED`.

P16E now records:

- final requirement status;
- analytical/model/empirical sensitivity state;
- covariance/common-path terms;
- required metrology if derivable;
- actual P16C/P16D performance when tools exist;
- detector-level verification.

Current:

`P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`.

Reason:

- final numerical detector/system requirements are still open for several metrics;
- physical infrastructure is not instantiated;
- empirical fabrication Jacobians do not exist.

---

# Round-43 maturity disposition

Unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO`;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`;
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`;
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`;
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`.

Round 43 closes analytical structure, not physical evidence.
