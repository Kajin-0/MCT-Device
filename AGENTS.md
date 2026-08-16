# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 44  
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

`research/2026-08-16_checkpoint_after_information_optimal_jacobian_round44.md`

Then:

- `research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`
- `research/2026-08-16_checkpoint_after_subsystem_acceptance_round42.md`
- `research/2026-08-16_checkpoint_after_minimum_lab_capability_round41.md`
- `research/2026-08-16_checkpoint_after_first_qualification_build_integration_round40.md`
- Round39/38/37/36/35/34 checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND44.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND44.md`

Current integration/control registers:

- P16A first-build readiness;
- P16B preferred candidate branch;
- P16C laboratory capability;
- P16D/P16D1 subsystem acceptance;
- P16E first-build uncertainty allocation;
- **P16F empirical-Jacobian information campaign register**.

Current analytical architecture:

- `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`
- `procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`
- `procedures/P22_INFORMATION_OPTIMAL_DOE_PLANNING.md`
- `procedures/P22A_MULTI_SUBSYSTEM_INFORMATION_OPTIMAL_JACOBIAN_PROGRAM.md`
- `procedures/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_QUALIFICATION.md`
- `calculations/RP01_FIRST_ORDER_SENSITIVITY_MATRIX.md`
- `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`
- `calculations/RP01_EMPIRICAL_JACOBIAN_INFORMATION_DESIGN.md`

---

# Maturity / implementation states — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — complete build can execute without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — historical identity sufficiently closed to claim reproduction of Smith et al.
3. `REPRODUCIBLE-RELEASE` — repeated stability/MSA/capability/yield/change-control/performance evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual laboratory infrastructure is identified/calibrated/commissioned.
5. `P16D-SURROGATE-COMMISSIONING-COMPLETE` — non-HgCdTe IQ/OQ/surrogate-PQ acceptance is complete.
6. `P16E-REQUIREMENTS-ALLOCATION-COMPLETE` — first-build decisions have justified allocations/qualification rules.
7. `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY` — active empirical campaigns have Stage-0 variance, resolution-verified physical contrasts, rank/conditioning, genealogy, holdouts and stopping criteria.

Current:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`
- `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO / NOT PHYSICALLY INSTANTIATED`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != campaign ready != empirical verified != local branch frozen != historical identity != reproducible release`.

---

# Permanent evidence discipline

- Never invent a missing number.
- Separate direct RP-01, same-lineage, transfer-family, derived, apparatus-calibration, local-qualification, acceptance, uncertainty-allocation and empirical-design evidence.
- Repetition does not promote evidence class.
- “Not recovered” does not mean absent.
- Preserve negative searches, rejected inferences, conflicts and failed branches.
- Theory/identities can allocate uncertainty; they do not manufacture process tolerances.
- A DOE run count does not become a power-based sample size without actual variance/effect requirements.
- Do not splice incompatible process generations into a fictional recipe.
- Engineering capability ranges are not historical process setpoints.
- Surrogate commissioning is not HgCdTe process equivalence.
- Configuration changes can invalidate calibration before calendar expiration.
- Measurement uncertainty, physical state uncertainty, process variation and engineering tolerance are distinct.
- No final detector/system requirement -> no justified numerical process tolerance.
- Pseudoreplication is prohibited: map points, FFT bins, repeated pulses and repeated field points are not automatically independent process replicates.

---

# Evidence / allocation / empirical states

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

Round-42 acceptance:

`IQ -> OQ -> surrogate PQ -> HgCdTe residual qualification`.

Round-43 allocation states include:

- `REQUIREMENT-DEFINITION-OPEN`
- `IDENTITY-ALLOCATABLE`
- `MODEL-CONDITIONAL-ALLOCATABLE`
- `COVARIANCE-REQUIRED`
- `EMPIRICAL-JACOBIAN-REQUIRED`
- `PARAMETRIC-ALLOCATION-ONLY`
- `LOCAL-ALLOCATION-DEFINED`
- `DETECTOR-LEVEL-VERIFIED`
- `READY-FOR-P17`

Round-44 empirical progression:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`.

No current local process Jacobian is beyond `DESIGN-IDENTIFIED`.

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
- RIE direct controller state: printed CH4/5H2, total 64 sccm, 100 mTorr, 50 W, 60 s;
- same-lineage candidate gas interpretation 1:5 -> derived 10.6667 sccm CH4 / 53.3333 sccm H2;
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
7. wet mesa Srivastav center: `2% Br2 / 3:1 EG:HBr`, ~21 °C, ~2.78 µm/min, `A≈.63`, best roughness ~2 nm; preparation bases open.
8. anodization TI center: 0.1 mol KOH per stated 1 L of 90% EG/10% DI-water solvent, carbon cathode, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å; solvent basis open.
9. Mask-2: 4–5 µm / 80 °C 30 min / chlorobenzene 30 min.
10. Cr/Au 30/270 nm; thermal evaporation strongest same-UWA method-family candidate.
11. low-force wire-saw first singulation screen.
12. compliant silicone-family first package-attach screen.
13. P10–P13 share one matched detector/contact/package/T/field/background state.

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

# Round-43 uncertainty rules retained

## Common gain cancellation

If identical linear gain `G` applies to P11 signal and P12 noise at the same frequency/loading:

`D*=S_sig sqrt(A)/(P_inc e_out)`.

Do not count common gain uncertainty twice.

## Area convention

`S_D,A=0.5-gamma_A`, where `gamma_A=partial ln P_inc/partial ln A`.

Direct total-power calibration -> +0.5; uniform irradiance with `P=HA` -> -0.5.

## Gap/field coupling

For fixed active V and `A=WL`:

`S_D,L=0.5-gamma_L-s_R,E+s_n,E`.

Need empirical canonical-field slopes.

## Electronics subtraction

For `e_det=sqrt(e_meas^2-e_elec^2)` and `beta=e_elec^2/e_det^2`:

- sensitivity to measured ASD = `1+beta`;
- sensitivity to electronics ASD = `-beta`.

## Background scalar-model warning

Idealized local sensitivities near 300 K / 60° full cone / 4.4 µm are very high. Precision BLIP work must use calibrated spectral weighting and physical view factor rather than scalar cutoff/FOV shorthand.

---

# Round-44 empirical information rules

## 1. Perturbation-size rule

For symmetric local derivative with `m` independent plus/minus pairs:

`SE(g)=sigma/[sqrt(2m)Delta u]`.

At planning alpha=.05 / power=.80:

`eta_min≈1.981/sqrt(m)`

where `eta=|g|Delta u/sigma`.

Examples:

- m=1 -> 1.981;
- m=2 -> 1.401;
- m=3 -> 1.144;
- m=4 -> 0.991.

These are planning scales only.

Required factor range must satisfy both information resolvability and same-regime physics.

## 2. Paired covariance

`Var(g_hat)=[Var(y+)+Var(y-)-2Cov(y+,y-)]/(4Delta u^2)`.

Retain pairing/common-mode cancellation in field, anneal blocking and package before/after analyses.

## 3. Information criterion follows detector decision

- D-optimal: broad coefficient information;
- c-optimal: protected linear combination;
- weighted A/trace: protected vector;
- classifier information: boundary localization;
- final decision-variance reduction: preferred when downstream P20 sensitivity exists.

Do not default to D-optimality if the final detector decision depends on one projected derivative.

## 4. Experimental units

- field sweep: detector is unit; field points repeated measures;
- LPE: independent growth;
- anneal: independently treated coupon/history, with growth/wafer blocking;
- RIE: independent chamber treatment;
- package: independent package build.

## 5. Field derivative campaign

At canonical `E0=10 V/cm`, use multiplicative coordinate `z=ln(E/E0)` and symmetric `E±=E0 exp(±h)`.

Estimate:

`s_R,E`, `s_n,E`, `s_D,E`.

`h` remains local until precision/heating/sweepout data exist.

## 6. LPE design options

If only first-order `{xL,yL,DeltaT_SC}` Jacobian is required and interactions/curvature can be neglected locally:

- 6 axial states + 3 centers -> structural `n=9` independent growths.

If interactions/curvature matter, P22 retains:

- BBD n=15;
- FCCCD n=17;
- Stage-2 2-factor quadratic n=11.

Structural counts are not power-based final sample sizes.

## 7. Anneal boundary

For logistic-style classifier, information multiplier `p(1-p)` is maximal at `p=.5`.

Use uncertain feasible boundary points to locate carrier-state transition; use stable n-like points separately for continuous Hall/mobility derivatives.

## 8. RIE/passivation

Separate controller actuators from measured physical state:

- flows/pressure;
- self-bias/sheath;
- reflected power;
- sample T;
- `t_clear`;
- `t_sem`;
- converted sheet/depth/lateral state.

For k independent factors plus 3 centers, Jacobian-first structural support is `2k+3` chamber treatments. For k=4 this is 11. Add interactions sequentially.

Freeze passivation during first RIE mapping; then map surface-state/passivation factors separately rather than one huge factorial.

`rho_c` alone is not the protected response.

## 9. Package

Surrogate-screen discrete construction families first. Freeze one family before continuous derivative estimation.

Use measured bondline/coverage/void/tilt. Package build is independent unit. Pair pre/post detector data where possible. Repeated pulses/cycles on one build are not independent builds.

## 10. Holdout / stopping

Every allocation-eligible derivative needs a held-out prediction.

Stop a stage when remaining uncertainty cannot materially change the protected detector decision and model/holdout checks pass—not merely because a planned run count was completed.

---

# Current empirical blockers

Still open physically:

1. Stage-0 independent-unit variances;
2. actual physical perturbation ranges;
3. local design matrices under real tool constraints;
4. all empirical derivative values;
5. anneal transition boundary;
6. matched detector descendants;
7. package-build data;
8. empirical P20/P16E allocations;
9. P17 capability/yield.

---

# Round-42 acceptance rules retained

- IQ -> OQ -> surrogate PQ -> HgCdTe residual qualification.
- `U_X<DeltaX_decision/2` minimum discriminability; approximately `<=DeltaX_decision/4` preferred where practical.
- `DeltaX_decision` must arise from a detector requirement or deliberate DOE contrast.
- `50 W != reactor equivalence`; RIE self-bias/sheath/thermal/chamber state must be measured.
- Johnson-noise validation remains the end-to-end PSD-chain absolute check.

---

# EH&S

Repository procedures do not replace facility/institution-specific controls for Hg/Cd compounds, Br2/HBr, H2/CH4, high temperature/sealed ampoules, solvents/chlorobenzene, RF/vacuum, high voltage or cryogens.

Physical execution remains blocked until institutional authorization and actual infrastructure exist.

---

# Strategic state after Round 44

The project is now:

**branch-selected + capability-specified + acceptance-method-specified + uncertainty-allocation-architecture-defined + information-optimal empirical-campaign architecture-defined + not physically instantiated**.

Broad historical searching has diminishing return unless a genuinely new primary archive/source family appears.

The next analytical bottleneck is **material/sample allocation across the designed empirical campaigns**.

---

# Next logical work — Round 45

Build a first-build **sample genealogy / descendant / material-consumption architecture**.

At minimum determine:

1. sample genealogy graph from growth -> coupon -> process split -> device -> package;
2. which P05/P06/P10/P11/P12/P13 measurements are destructive or repeatable on the same descendant;
3. structural minimum number of independent growths/coupons/devices/packages for each candidate DOE branch;
4. where matched split-coupon designs reduce variance;
5. which descendants must be reserved for holdout rather than model fitting;
6. contingency reserve logic for failed processing without inventing yield;
7. how to distinguish structural minimum inventory from final power-based sample size.

Do not invent wafer dimensions, die yield, material availability or failure rate.