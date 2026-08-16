# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 45  
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

`research/2026-08-16_checkpoint_after_sample_genealogy_round45.md`

Then:

- `research/2026-08-16_checkpoint_after_information_optimal_jacobian_round44.md`
- `research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`
- `research/2026-08-16_checkpoint_after_subsystem_acceptance_round42.md`
- `research/2026-08-16_checkpoint_after_minimum_lab_capability_round41.md`
- `research/2026-08-16_checkpoint_after_first_qualification_build_integration_round40.md`
- older checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND45.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND45.md`

Current integration/control registers:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`
- `travelers/P16C_MINIMUM_LAB_CAPABILITY_IMPLEMENTATION_REGISTER.md`
- `travelers/P16D_SUBSYSTEM_ACCEPTANCE_REGISTER.md`
- `travelers/P16D1_SUPPORTING_METROLOGY_MICROFAB_ACCEPTANCE_REGISTER.md`
- `travelers/P16E_FIRST_BUILD_UNCERTAINTY_ALLOCATION_REGISTER.md`
- `travelers/P16F_EMPIRICAL_JACOBIAN_INFORMATION_REGISTER.md`
- `travelers/P16G_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION_REGISTER.md`

Latest analytical/control modules:

- `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`
- `procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`
- `procedures/P22_INFORMATION_OPTIMAL_DOE_PLANNING.md`
- `procedures/P22A_MULTI_SUBSYSTEM_INFORMATION_OPTIMAL_JACOBIAN_PROGRAM.md`
- `procedures/P22B_FIRST_BUILD_DESCENDANT_GENEALOGY_MATERIAL_ALLOCATION.md`
- `procedures/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_QUALIFICATION.md`
- `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`
- `calculations/RP01_EMPIRICAL_JACOBIAN_INFORMATION_DESIGN.md`
- `calculations/RP01_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION.md`

---

# Maturity / implementation states — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — complete build can execute without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — historical identity sufficiently closed to claim reproduction of Smith et al.
3. `REPRODUCIBLE-RELEASE` — repeated stability/MSA/capability/yield/change-control/performance evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual laboratory infrastructure is identified/calibrated/commissioned to the P16C requirement.
5. `P16D-SURROGATE-COMMISSIONING-COMPLETE` — possible non-HgCdTe IQ/OQ/surrogate-PQ acceptance is complete for selected infrastructure.
6. `P16E-REQUIREMENTS-ALLOCATION-COMPLETE` — first-build measurement/control uncertainties and requirements are adequately allocated.
7. `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY` — empirical campaigns are physically feasible, identifiable, resolution-justified and holdout-defined.
8. `P16G-MATERIAL-GENEALOGY-PLAN-READY` — sample genealogy, physical descendant allocation, holdouts and structural material balance are feasible.

Current:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`
- `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16G-MATERIAL-GENEALOGY-PLAN-READY = NO / NOT PHYSICALLY INSTANTIATED`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != empirical campaign ready != genealogy ready != local branch frozen != historical identity != reproducible release`.

---

# Permanent evidence discipline

- Never invent a missing number.
- Separate direct RP-01, same-lineage, transfer-family, derived, apparatus-calibration, local-qualification, acceptance, uncertainty-allocation and empirical evidence.
- Repetition does not promote evidence class.
- “Not recovered” does not mean absent.
- Preserve negative searches, rejected inferences, conflicts and failed branches.
- Theory/identities may allocate uncertainty; they do not manufacture process tolerances.
- Structural DOE count is not power-based sample size.
- Physical descendant count is not independent experimental-unit count.
- Physical separation does not create upstream statistical independence.
- Engineering capability ranges are not historical process setpoints.
- Surrogate commissioning is not HgCdTe process equivalence.
- Configuration changes can invalidate calibration before calendar expiration.
- Measurement uncertainty, physical-state uncertainty, process variation and engineering tolerance are distinct.
- No final detector/system requirement -> no justified numerical process tolerance.
- Preserve real experimental units; reject pseudoreplication.

---

# Key controlled state/evidence labels

P20 sensitivity:

- `IDENTITY`
- `MODEL-CONDITIONAL`
- `PROXY-CONDITIONAL`
- `EMPIRICAL-REQUIRED`

Round-44 empirical progression:

`EMPIRICAL-REQUIRED -> DESIGN-IDENTIFIED -> DESIGN-RESOLUTION-VERIFIED -> EMPIRICAL-PRELIMINARY -> EMPIRICAL-VERIFIED -> DETECTOR-BRIDGED -> ALLOCATION-ELIGIBLE`.

Round-45 genealogy/gap states include:

- `STRUCTURAL-COUNT-DERIVED`
- `ROOT-INVENTORY-OPEN`
- `DESCENDANT-FOOTPRINT-OPEN`
- `PHYSICAL-AREA-OPEN`
- `P05-DOWNSTREAM-COMPATIBILITY-OPEN`
- `TREATMENT-UNIT-DEFINITION-OPEN`
- `TREATMENT-BUNDLE-LAYOUT-OPEN`
- `SINGULATION-EDGE-EXCLUSION-OPEN`
- `HOLDOUT-MATERIAL-OPEN`
- `DESTRUCTIVE-WITNESS-OPEN`
- `TREATMENT-ROOT-CONFOUNDING-OPEN`
- `STATISTICAL-RESERVE-OPEN`
- `POWER-REPLICATION-OPEN`
- `STRUCTURAL-GENEALOGY-READY`.

---

# Canonical RP-01 anchors — do not drift

## Material

- LPE n-HgCdTe on insulating CdZnTe;
- nominal `x≈0.30`;
- supplier `n≈9.8×10^14 cm^-3`;
- supplier `mu≈4.0×10^4 cm²/Vs`;
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
- detector cutoff ~4.4 µm, convention open;
- BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm;
- QE ~70%;
- historical 1/f knee ~3 kHz;
- high-frequency g-r ~24.5 nV/sqrtHz;
- 24.5 nV/sqrtHz is not the historical 1-kHz noise;
- RP-01 lifetime/f3dB remains open.

Historical values are references, not tolerance bands.

---

# Preferred candidate architecture retained

1. `Cd0.96Zn0.04Te (111)B` substrate family; actual lot/size/plane/miscut local.
2. P29 Br2/methanol final-surface family; exact concentration basis unresolved.
3. Honeywell covered graphite horizontal-slider LPE topology.
4. source center `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`.
5. N2 purge -> H2 atmosphere family.
6. Hg anneal first screen ~250 °C / 1 h / Hg-saturated-isothermal-like, final state released through P05/P06.
7. Mask-1 AZ4620 transfer-family candidate; modern equivalence unproven.
8. wet mesa Srivastav center: 2% Br2 / 3:1 EG:HBr, ~21 °C, ~2.78 µm/min, anisotropy ~.63, best roughness ~2 nm; bases open.
9. anodization TI center: 0.1 mol KOH per stated 1 L 90% EG/10% DI-water solvent, carbon cathode, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å; solvent basis open.
10. Mask-2: 4–5 µm / 80 °C 30 min / chlorobenzene 30 min.
11. RIE candidate 1:5 CH4:H2; derived 10.6667/53.3333 sccm at total 64 sccm.
12. Cr/Au 30/270 nm; thermal evaporation strongest same-UWA method-family candidate.
13. low-force wire-saw first singulation screen.
14. compliant silicone-family first package-attach screen.
15. P10-P13 share one matched detector/contact/package/T/field/background state.

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

Later P30A/P16B rounded `0.249740/0.012502/0.737758` values are a controlled ppm-scale numerical erratum. Future calculations use the frozen values.

`M_charge` remains apparatus-dependent.

---

# Round-43 analytical results retained

- Common P11/P12 gain cancels exactly from D* when the same linear path applies at the same frequency/loading.
- Active-area sensitivity is convention-dependent: `S_D,A=0.5-gamma_A`.
- Gap metrology couples area and field: `S_D,L=0.5-gamma_L-s_R,E+s_n,E` for fixed physical V and A=WL.
- Electronics-noise subtraction conditioning with `beta=e_elec^2/e_det^2` has sensitivities `1+beta` and `-beta`.
- Use covariance, not blind RSS, for shared gain/area/gap/T/E.

---

# Round-44 information-design results retained

For symmetric derivative pairs:

`SE(g_hat)=sigma/[sqrt(2m) Delta u]`.

With alpha=.05 and 80% power normal planning approximation:

`eta_min≈1.981/sqrt(m)` where `eta=|g|Delta u/sigma`.

Physical perturbation must satisfy:

`information lower bound <= Delta u <= same-regime physics upper bound`.

Use D-, c-, A- or downstream decision-variance criteria according to the protected scientific decision.

Experimental units:

- F1 field sweep -> completed detector;
- F2 LPE -> independent growth;
- F3 anneal -> independently executed treatment history/coupon under locally frozen unit definition;
- F4 RIE -> chamber treatment/run;
- F5 package -> independent package build.

---

# Round-45 genealogy / material rules — permanent

## 1. Four counts are distinct

Track separately:

- independent experimental units;
- physical descendant pieces;
- usable material area/packing;
- yield/power/failure reserve.

## 2. Genealogy DAG, not additive campaign counts

`N_program != N_F1+N_F2+N_F3+N_F4+N_F5`.

F1/F3/F4/F5 can use descendants of F2 roots and P10-P13 can share one detector.

## 3. Delayed differentiation

Split material at the latest common state before different irreversible histories are required.

P06 should normally map intact parent material before cutting.

## 4. P05 default branch

Hall acquisition is not inherently destructive, but Hall contact preparation changes specimen state. Until downstream compatibility is qualified, allocate a dedicated P05 material-control descendant.

## 5. F1

One detector gives one within-device local field slope. At least two devices are needed to begin estimating between-device slope variance. Final statistically credible count remains open. F1 normally adds zero incremental devices if suitable completed descendants exist.

## 6. F2 structural root floors

With current P21 three-holdout policy and reusable Stage-0 centers:

- 9-run Jacobian-first -> >=12 independent roots;
- 15-run BBD -> >=18;
- 17-run FCCCD -> >=20;
- 11-run Stage-2 -> >=14.

These are structural independent-growth lower bounds, not area/procurement/power counts.

## 7. F3

`N_treat,F3=N_B+N_J+N_H+N_C+N_X`.

A four-factor stable n-like first-order axial fit has 11 fitted histories (`2k_A+3`), excluding boundary search/holdout/power. Co-loaded ampoule specimens are not automatically independent anneal runs.

## 8. F4

`N_Q,fit=2k_R+3`; k_R=4 -> 11 fitted chamber treatments structurally.

Co-loaded oxide-clear/Hall/LBIC/TLM/detector structures form a treatment bundle and are not separate independent chamber treatments.

Do not fabricate a complete detector for every early RIE state by default; use staged witness -> selected detector -> holdout logic.

## 9. P10-P13

Prefer one matched detector for P10/P11/P12/P13 and F1 where loading is reversible.

## 10. F5

Non-HgCdTe surrogate screening uses zero HgCdTe dies. Each actual independent package build consumes one completed detector die absent qualified reversible rework. Repeated cycles/pulses are repeated measures.

## 11. Physical area

Final material area remains open until actual descendant footprints, kerf/wander, P35 functional edge exclusion, orientation and handling margins are frozen and CAD-packed into measured usable root regions.

## 12. Reserve

No arbitrary reserve percentage. Keep process/metrology/layout/holdout/FA/power reserves separate. Use empirical yield/probability once available.

## 13. Anti-confounding

Material conservation may not alias treatment with root growth/wafer position/source/chamber/time. Distribute treatments across blocks where possible.

---

# EH&S

Repository procedures do not replace facility/institution-specific controls for Hg/Cd compounds, Br2/HBr, H2/CH4, high temperature/sealed ampoules, solvents/chlorobenzene, RF/vacuum, high voltage or cryogens.

Physical execution remains blocked until institutional authorization and actual infrastructure exist.

---

# Strategic state after Round 45

The project is now:

**branch-selected + capability-specified + acceptance-specified + uncertainty architecture defined + information-optimal empirical campaigns designed + sample genealogy/material accounting designed + not physically instantiated**.

Generic literature searching has diminishing return unless a genuinely new archive/source family appears.

---

# Next logical work — Round 46

Build a controlled **campaign execution / material-release gate plan**.

At minimum define:

1. chronological progression through infrastructure/commissioning/Stage-0/F2/F3/F4/F1/F5;
2. go/hold/stop gates that prevent expensive downstream processing before upstream evidence is adequate;
3. material-release gates before detector fabrication and packaging;
4. run-order randomization/blocking subject to source-use, ampoule and chamber constraints;
5. dynamic holdout/reserve release rules;
6. next-action decision rule comparing another upstream information-rich run against consuming an existing descendant downstream;
7. P18 failure/deviation routing that preserves remaining holdout material.

Do not invent physical results, material availability or statistical power that do not exist.
