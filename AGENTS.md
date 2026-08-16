# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 43  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual/booklet executable by a competent researcher without undocumented tribal knowledge.

Canonical first process:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is no end-to-end reproducible release yet.

---

# READ FIRST

Latest checkpoint:

`research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`

Then:

- `research/2026-08-16_checkpoint_after_subsystem_acceptance_round42.md`
- `research/2026-08-16_checkpoint_after_minimum_lab_capability_round41.md`
- `research/2026-08-16_checkpoint_after_first_qualification_build_integration_round40.md`
- Round39/38/37/36/35/34 checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND43.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND43.md`

Current integration/control registers:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`
- `travelers/P16C_MINIMUM_LAB_CAPABILITY_IMPLEMENTATION_REGISTER.md`
- `travelers/P16D_SUBSYSTEM_ACCEPTANCE_REGISTER.md`
- `travelers/P16D1_SUPPORTING_METROLOGY_MICROFAB_ACCEPTANCE_REGISTER.md`
- `travelers/P16E_FIRST_BUILD_UNCERTAINTY_ALLOCATION_REGISTER.md`

Current capability/acceptance/allocation architecture:

- `docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`
- `procedures/P36_LAB_SUBSYSTEM_COMMISSIONING_ACCEPTANCE.md`
- `procedures/P36A_SUPPORTING_METROLOGY_LITHOGRAPHY_WET_CHEMISTRY_ACCEPTANCE.md`
- `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`
- `calculations/RP01_FIRST_ORDER_SENSITIVITY_MATRIX.md`
- `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`

---

# Maturity / implementation states — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — complete build can execute without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — historical identity sufficiently closed to claim reproduction of Smith et al.
3. `REPRODUCIBLE-RELEASE` — repeated stability/MSA/capability/yield/change-control/performance evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual laboratory infrastructure is identified/calibrated/commissioned to the P16C requirement.
5. `P16D-SURROGATE-COMMISSIONING-COMPLETE` — all possible non-HgCdTe IQ/OQ/surrogate-PQ acceptance work is complete for selected infrastructure.
6. `P16E-REQUIREMENTS-ALLOCATION-COMPLETE` — every first-build decision has a justified numerical allocation or an explicitly controlled qualification-only decision rule, with covariance/empirical gaps addressed.

Current:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != local branch frozen != historical identity != reproducible release`.

---

# Permanent evidence discipline

- Never invent a missing number.
- Separate direct RP-01, same-lineage, transfer-family, derived, apparatus-calibration, local-qualification, acceptance and uncertainty-allocation evidence.
- Repetition does not promote evidence class.
- “Not recovered” does not mean absent.
- Preserve negative searches, rejected inferences, conflicts and failed branches.
- Theory/identities can allocate uncertainty; they do not manufacture process tolerances.
- Do not splice incompatible process generations into a fictional recipe.
- Engineering capability ranges are not historical process setpoints.
- Surrogate commissioning is not HgCdTe process equivalence.
- Configuration changes can invalidate calibration before calendar expiration.
- Measurement uncertainty, physical state uncertainty, process variation and engineering tolerance are distinct.
- No final detector/system requirement -> no justified numerical process tolerance.

---

# Evidence / allocation classes retained

P20 sensitivity classes:

- `IDENTITY`
- `MODEL-CONDITIONAL`
- `PROXY-CONDITIONAL`
- `EMPIRICAL-REQUIRED`

Round-41 capability classes:

- `HARD-MINIMUM`
- `FIRST-BUILD-ENGINEERING-ENVELOPE`
- `DESIGN-CHECK`
- `SURROGATE-COMMISSIONABLE`
- `HGCDTE-REQUIRED`
- `LOCAL-BLANK`
- `EH&S/FACILITY-GATE`

Round-42 acceptance state includes `ACCEPTANCE-EVIDENCE-OPEN` and IQ -> OQ -> surrogate PQ -> HgCdTe residual qualification.

Round-43 allocation states:

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

# Canonical RP-01 anchors — do not drift

## Material

- LPE n-HgCdTe on insulating CdZnTe;
- nominal `x≈0.30`;
- supplier `n≈9.8×10^14 cm^-3`;
- supplier `mu≈4.0×10^4 cm²/V·s`;
- active layer ~9.5 µm.

## Passivation / lithography / RIE / metal

- anodic oxide ~800 Å = 80 nm;
- Mask-1 wet mesa; historical product/process open;
- Mask-2 4–5 µm;
- 80 °C / 30 min bake;
- chlorobenzene 30 min;
- same Mask-2 survives RIE and supports lift-off;
- RIE: Plasma Technology parallel plate, printed CH4/5H2, total 64 sccm, 100 mTorr, 50 W, 60 s;
- converted average n ~2.0×10^15 cm^-3, mobility ~3.3×10^4 cm²/Vs;
- Cr 30 nm / Au 270 nm;
- contacts ~300×300 µm;
- gaps 50–400 µm by 50 µm;
- `rho_c≈9×10^-4 Ω cm²` at 80 K.

## Detector state

- key data around 80 K;
- stated 60° FOV;
- spectral response chopped at 1 kHz;
- field = measured active contact voltage / measured active gap;
- Figures 5–7 use 10 V/cm;
- cutoff ~4.4 µm, convention open;
- BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm;
- QE ~70%;
- historical 1/f knee ~3 kHz;
- high-frequency g-r ~24.5 nV/sqrtHz;
- 24.5 nV/sqrtHz is not the historical 1-kHz noise;
- RP-01 lifetime/f3dB remains open.

Historical values are references, not tolerance bands.

---

# Preferred candidate architecture retained

1. `Cd0.96Zn0.04Te (111)B` preferred substrate family; actual lot/size/plane/miscut local.
2. P29 Br2/methanol final-surface family; no invented concentration basis.
3. Honeywell covered graphite horizontal-slider LPE topology.
4. composition center `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`.
5. N2 purge -> H2 atmosphere family.
6. Hg anneal first screen ~250 °C / 1 h / Hg-saturated-isothermal-like, released by P05/P06.
7. Mask-1 historical product screen AZ4620 transfer family; modern equivalence unproven.
8. wet mesa Srivastav center: `2% Br2 / 3:1 EG:HBr`, ~21 °C, ~2.78 µm/min, `A≈.63`, best roughness ~2 nm; bases open.
9. anodization TI center: 0.1 mol KOH per stated 1 L of 90% EG/10% DI-water solvent, carbon cathode, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å; solvent basis open.
10. Mask-2: 4–5 µm / 80 °C 30 min / chlorobenzene 30 min.
11. RIE candidate 1:5 CH4:H2; derived 10.6667/53.3333 sccm at total 64 sccm.
12. Cr/Au 30/270 nm; thermal evaporation strongest same-UWA method-family candidate.
13. low-force wire-saw first singulation screen.
14. compliant silicone-family first package-attach screen.
15. P10–P13 share one matched detector/contact/package/T/field/background state.

Candidate centers/families are not released build values.

---

# Authoritative LPE mass convention

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md` freezes:

- Hg 200.59 g/mol;
- Cd 112.414 g/mol;
- Te 127.60 g/mol.

For `xL=.082`, `yL=.810`:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

Later P30A/P16B rounded `0.249740/0.012502/0.737758` values are a controlled ppm-scale numerical erratum. Future calculations use the frozen values. Normalize active large files together when next revised.

`M_charge` remains apparatus-dependent.

---

# Round-43 major analytical results

## 1. Common P11/P12 gain can cancel from D*

If one linear gain `G` applies to signal and noise at the same frequency/loading:

`R_v=(S_sig/G)/P_inc`

`e_n=e_out/G`

therefore

`D*=S_sig sqrt(A)/(P_inc e_out)`.

Do not double-count common gain uncertainty. If paths differ, propagate `G_noise/G_signal`.

## 2. Active-area sensitivity is convention dependent

Define

`gamma_A=partial ln P_inc/partial ln A`.

Then

`S_D,A=0.5-gamma_A`.

- direct power independent of A -> `+0.5`;
- uniform irradiance with `P=H A` -> `-0.5`.

Area and optical power must be treated jointly.

## 3. Gap metrology couples area and field

For fixed physical V and `A=WL`:

`S_D,L=0.5-gamma_L-s_R,E+s_n,E`.

Need local canonical-field derivatives:

`s_R,E=partial ln R_v/partial ln E`

`s_n,E=partial ln e_n/partial ln E`.

Gap is not an area-only uncertainty.

## 4. Electronics subtraction has exact conditioning

For

`e_det=sqrt(e_meas^2-e_elec^2)`

and

`beta=e_elec^2/e_det^2`,

sensitivities are:

- measured ASD: `1+beta`;
- electronics ASD: `-beta`.

Examples:

- beta=.10 -> 1.10 / -0.10;
- beta=1 -> 2 / -1;
- beta=4 -> 5 / -4.

## 5. D* covariance is first-class

`delta ln D*=delta ln R_v + 0.5 delta ln A - delta ln e_n`.

Use full covariance, not blind RSS, when gain/area/gap/T/E are shared.

## 6. Background scalar model is too sensitive for precision BLIP

Idealized local sensitivities near 300 K / 60° full cone / 4.4 µm:

- ~4.027%/K;
- ~3.04%/degree full cone;
- ~2.064% per 0.01 µm step boundary.

One-term 1% diagnostic equivalents:

- ~0.248 K;
- ~0.329°;
- ~4.85 nm.

Do not turn the last number into a detector cutoff tolerance. Use spectral weighting/view factor.

## 7. Hansen screening remains model conditional

At x=.30/80K:

- `d lambda_Eg/dx=-33.0525 um/x`;
- `d lambda_Eg/dT=-0.004468 um/K`.

10-nm model-equivalent uncertainty corresponds one-term to `u_x≈3.03e-4` or `u_T≈2.24 K`. Not a measured detector-edge specification.

## 8. Temporal fit uncertainty is not full lifetime uncertainty

After one-pole validation:

`u_r(f3dB)=u_r(tau)`

for the same fitted pole before model discrepancy.

At the corner, local amplitude/phase slopes can size instrument precision, but source/electrical/package de-embedding and model discrepancy remain mandatory.

---

# Current empirical Jacobian blockers

Do not invent these:

1. P21 LPE `{xL,yL,TL,DeltaT_SC,t,inventory,source-use}` -> `{x,d,uniformity,morphology}`;
2. P23 anneal `{Ts(t),THg(t),dwell,cooldown,start state}` -> `{carrier sign,n,mu,tau}`;
3. mesa/oxide/sidewall -> `{Rv,en,tau}`;
4. RIE/contact `{Ns,dconv,Lconv,self-bias,damage}` -> `{sweepout,Rv,en,tau,D*}`;
5. package `{bondline,carrier,vacuum,interconnect}` -> `{Rth,Hpkg,noise}`.

P16E remains NO until requirements/allocations and empirical blocks are sufficiently closed.

---

# Round-42 acceptance rules retained

- IQ -> OQ -> surrogate PQ -> HgCdTe residual qualification.
- `U_X<DeltaX_decision/2` is minimum measurement discriminability; approximately `<=DeltaX_decision/4` is a preferred engineering target where practical.
- Round-43 restriction: `DeltaX_decision` must come from a detector/system requirement or deliberate DOE contrast first.
- `50 W != reactor equivalence`; RIE self-bias/sheath/thermal/chamber state must be recorded.
- Johnson-noise validation remains the end-to-end absolute PSD-chain check.

---

# EH&S

Repository procedures do not replace facility/institution-specific controls for Hg/Cd compounds, Br2/HBr, H2/CH4, high temperature/sealed ampoules, solvents/chlorobenzene, RF/vacuum, high voltage or cryogens.

Physical execution remains blocked until institutional authorization and actual infrastructure exist.

---

# Strategic state after Round 43

The project is now:

**branch-selected + capability-specified + acceptance-method-specified + uncertainty-allocation-architecture-defined + not physically instantiated**.

Generic historical searching has diminishing return unless a genuinely new archive/source family appears.

The strongest analytical bottleneck is now the missing empirical process-to-material/device Jacobian.

---

# Next logical work — Round 44

Build a unified **empirical-Jacobian / information-optimal DOE execution package** rather than a generic experiment list.

Prioritize by expected reduction in final detector decision uncertainty and identifiability:

1. canonical field derivatives `s_R,E`, `s_n,E`;
2. P21 LPE response surface;
3. P23 anneal state boundary/Jacobian;
4. blocking-contact/passivation vector response;
5. package thermal/dynamic Jacobian.

For each define:

- parameter vector;
- response vector;
- local perturbation scale justified by Round-43 uncertainty needs;
- interaction terms;
- replicate/genealogy structure;
- surrogate controls where possible;
- holdout confirmation;
- information/identifiability metric;
- stopping criterion.

Do not prescribe physical HgCdTe results that do not exist.
