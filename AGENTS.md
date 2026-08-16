# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 46  
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

`research/2026-08-16_checkpoint_after_sequential_material_release_round46.md`

Then:

- `research/2026-08-16_checkpoint_after_sample_genealogy_round45.md`
- `research/2026-08-16_checkpoint_after_information_optimal_jacobian_round44.md`
- `research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`
- `research/2026-08-16_checkpoint_after_subsystem_acceptance_round42.md`
- `research/2026-08-16_checkpoint_after_minimum_lab_capability_round41.md`
- `research/2026-08-16_checkpoint_after_first_qualification_build_integration_round40.md`
- older checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND46.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND46.md`

Current integration/control registers:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`
- `travelers/P16C_MINIMUM_LAB_CAPABILITY_IMPLEMENTATION_REGISTER.md`
- `travelers/P16D_SUBSYSTEM_ACCEPTANCE_REGISTER.md`
- `travelers/P16D1_SUPPORTING_METROLOGY_MICROFAB_ACCEPTANCE_REGISTER.md`
- `travelers/P16E_FIRST_BUILD_UNCERTAINTY_ALLOCATION_REGISTER.md`
- `travelers/P16F_EMPIRICAL_JACOBIAN_INFORMATION_REGISTER.md`
- `travelers/P16G_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION_REGISTER.md`
- `travelers/P16H_SEQUENTIAL_MATERIAL_RELEASE_CONTROL_REGISTER.md`

Latest analytical/control modules:

- `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`
- `procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`
- `procedures/P22_INFORMATION_OPTIMAL_DOE_PLANNING.md`
- `procedures/P22A_MULTI_SUBSYSTEM_INFORMATION_OPTIMAL_JACOBIAN_PROGRAM.md`
- `procedures/P22B_FIRST_BUILD_DESCENDANT_GENEALOGY_MATERIAL_ALLOCATION.md`
- `procedures/P22C_FIRST_BUILD_CAMPAIGN_EXECUTION_MATERIAL_RELEASE_CONTROL.md`
- `procedures/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_QUALIFICATION.md`
- `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`
- `calculations/RP01_EMPIRICAL_JACOBIAN_INFORMATION_DESIGN.md`
- `calculations/RP01_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION.md`
- `calculations/RP01_SEQUENTIAL_MATERIAL_RELEASE_DECISION_CONTROL.md`

---

# Maturity / implementation states — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — complete build can execute without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — historical identity sufficiently closed to claim reproduction of Smith et al.
3. `REPRODUCIBLE-RELEASE` — repeated stability/MSA/capability/yield/change-control/performance evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual laboratory infrastructure is identified/calibrated/commissioned.
5. `P16D-SURROGATE-COMMISSIONING-COMPLETE` — non-HgCdTe IQ/OQ/surrogate-PQ acceptance complete for selected infrastructure.
6. `P16E-REQUIREMENTS-ALLOCATION-COMPLETE` — measurement/control uncertainties and requirements adequately allocated.
7. `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY` — empirical campaigns physically feasible, identifiable, resolution-justified and holdout-defined.
8. `P16G-MATERIAL-GENEALOGY-PLAN-READY` — sample genealogy, descendant allocation, holdouts and structural material balance feasible.
9. `P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY` — actual laboratory has an instantiated gate/release system for irreversible material commitments.

Current:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`
- `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16G-MATERIAL-GENEALOGY-PLAN-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY = NO / NOT PHYSICALLY INSTANTIATED`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != empirical campaign ready != genealogy ready != release-control ready != local branch frozen != historical identity != reproducible release`.

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
- Configuration changes can invalidate calibration/acceptance before calendar expiration.
- Measurement uncertainty, physical-state uncertainty, process variation and engineering tolerance are distinct.
- No final detector/system requirement -> no justified numerical process tolerance.
- Preserve real experimental units; reject pseudoreplication.
- A controlled gate method does not mean a physical gate passed.
- A failed treatment response is data unless a predeclared execution-invalidity criterion applies.

---

# Key controlled labels

P20 sensitivity:

- `IDENTITY`
- `MODEL-CONDITIONAL`
- `PROXY-CONDITIONAL`
- `EMPIRICAL-REQUIRED`

Round-44 empirical progression:

`EMPIRICAL-REQUIRED -> DESIGN-IDENTIFIED -> DESIGN-RESOLUTION-VERIFIED -> EMPIRICAL-PRELIMINARY -> EMPIRICAL-VERIFIED -> DETECTOR-BRIDGED -> ALLOCATION-ELIGIBLE`.

Round-45 genealogy states include:

- `STRUCTURAL-COUNT-DERIVED`
- `ROOT-INVENTORY-OPEN`
- `DESCENDANT-FOOTPRINT-OPEN`
- `PHYSICAL-AREA-OPEN`
- `P05-DOWNSTREAM-COMPATIBILITY-OPEN`
- `TREATMENT-BUNDLE-LAYOUT-OPEN`
- `HOLDOUT-MATERIAL-OPEN`
- `DESTRUCTIVE-WITNESS-OPEN`
- `TREATMENT-ROOT-CONFOUNDING-OPEN`
- `STATISTICAL-RESERVE-OPEN`
- `POWER-REPLICATION-OPEN`

Round-46 execution states include:

- `GATE-EVIDENCE-OPEN`
- `TECHNICAL-ELIGIBILITY-PASS`
- `POST-COMMIT-FEASIBILITY-PASS`
- `MATERIAL-RELEASE-GO`
- `MATERIAL-RELEASE-HOLD`
- `MATERIAL-RELEASE-REWORK`
- `MATERIAL-RELEASE-STOP`
- `HOLDOUT-LOCKED`
- `HOLDOUT-MODEL-FROZEN`
- `RESERVE-LOCKED`
- `RESERVE-RELEASED`
- `CONFIGURATION-IMPACT-REVIEW-REQUIRED`
- `EXECUTION-DEVIATION-OPEN`

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
- same-lineage 1:5 candidate -> 10.6667 sccm CH4 / 53.3333 sccm H2;
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
11. RIE candidate 1:5 CH4:H2 around the direct 64-sccm total; actual reactor equivalence local.
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

# Round-43 analytical rules retained

- Common P11/P12 gain cancels exactly from D* when the same linear path applies at the same frequency/loading.
- Active-area sensitivity is convention-dependent: `S_D,A=0.5-gamma_A`.
- Gap metrology couples area and field: `S_D,L=0.5-gamma_L-s_R,E+s_n,E` for fixed physical V and A=WL.
- Electronics-noise subtraction with `beta=e_elec²/e_det²` has sensitivities `1+beta` and `-beta`.
- Use covariance, not blind RSS, for shared gain/area/gap/T/E.

---

# Round-44 information-design rules retained

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

# Round-45 genealogy/material rules retained

## Four counts remain distinct

Track:

- independent experimental units;
- physical descendant pieces;
- usable material area/packing;
- yield/power/failure reserve.

## DAG not sum

`N_program != N_F1+N_F2+N_F3+N_F4+N_F5`.

## Delayed differentiation

Split at the latest common state before different irreversible histories.

P06 normally maps intact parent material before cutting.

## P05 conservative branch

Until Hall-contact downstream compatibility is locally qualified, allocate dedicated P05 material-control sibling.

## F2 structural root floors

With current three-holdout policy and reusable Stage-0 centers:

- 9-run Jacobian-first -> >=12 independent roots;
- 15-run BBD -> >=18;
- 17-run FCCCD -> >=20;
- 11-run Stage-2 -> >=14.

These are structural roots, not area/procurement/power counts.

## F3/F4

- four-factor stable n-like axial F3 fit -> 11 fitted histories, excluding boundary/holdout/power;
- four-factor F4 Jacobian-first -> 11 fitted chamber treatments, excluding holdout/power;
- co-loaded siblings do not multiply independent treatment count.

## Detector/package sharing

Prefer one matched detector for P10/P11/P12/P13/F1 where reversible.

Non-HgCdTe package screening consumes zero HgCdTe dies; each actual independent package build consumes one die absent qualified reversible rework.

---

# Round-46 sequential release rules — permanent

## 1. Two-predicate GO

For node `v` and irreversible edge `e`:

`GO only if technical eligibility T(v,e)=PASS and post-commit material/genealogy feasibility M(v,e)=PASS`.

Technically good material can remain HOLD if consuming it would break protected downstream obligations.

## 2. Controlled outcomes

Use only:

`GO / HOLD / REWORK / STOP`.

`HOLD != FAIL`.

`REWORK` requires a qualified route and evidence-role reassessment.

## 3. Holdouts

Holdout is locked material, not spare inventory.

Separate validity-QC access from protected scientific outcome access.

Freeze model/version before opening the protected response.

A failed prediction remains evidence unless execution-invalid by a predeclared criterion.

## 4. Reserve

Release reserve only when its protected purpose closes, is replaced by an equivalent allocation, or is explicitly retired in a redesigned campaign.

No arbitrary reserve percentage.

## 5. G0-G8 ladder

- G0 active-campaign authorization;
- G1 Stage-0 -> formal F2;
- G2 selected F2 root -> F3 anneal;
- G3 annealed state -> F4 RIE/passivation;
- G4 witness-qualified RIE state -> full detector fabrication;
- G5 completed detector -> matched P10-P13/F1;
- G6 characterized detector -> singulation;
- G7 singulated die -> actual package build;
- G8 result -> evidence promotion/P16E update/P17 handoff.

## 6. Relevant-subsystem rule

A future early-stage campaign requires every subsystem needed for its immediate irreversible edge/evidence, not automatically every unrelated late-stage tool. Physical execution still requires actual relevant P16C/P16D/P16E/P16F/P16G/EH&S closure.

## 7. F4 two-tier material strategy

`Tier-1 witnesses -> G4 -> selected detector-bearing states`.

Do not fabricate complete detectors for every exploratory RIE condition by default.

## 8. Next-action dominance

For candidate action `a`, use protected decision-variance reduction

`DeltaV_a = V_current - E[V_after|a]`

with a burden vector, not an invented universal cost scalar.

Do not choose an action dominated by another feasible action that offers no less information with no greater protected burden/confounding.

## 9. Run order

Randomize within feasible blocks; explicitly model hard-to-change/sequential/source-history effects. Do not let treatment alias perfectly with root/source/chamber/time/operator/package batch.

## 10. Failure

Unexpected failure -> HOLD siblings -> classify event -> P18 -> use FA reserve where possible -> controlled resume/REWORK/STOP/replacement.

True treatment failure stays in the dataset.

## 11. Configuration

Every GO references exact procedure/apparatus/calibration/model/material-plan revisions. Decision-affecting configuration changes require impact review; prior GO does not transfer automatically.

---

# EH&S

Repository procedures do not replace facility/institution-specific controls for Hg/Cd compounds, Br2/HBr, H2/CH4, high temperature/sealed ampoules, solvents/chlorobenzene, RF/vacuum, high voltage or cryogens.

Physical execution remains blocked until institutional authorization and actual relevant infrastructure exist.

---

# Strategic state after Round 46

The project is now:

**branch-selected + capability-specified + acceptance-specified + uncertainty architecture defined + information-optimal empirical campaigns designed + sample genealogy/material accounting designed + sequential material-release control designed + not physically instantiated**.

Generic literature searching has diminishing return unless a genuinely new archive/source family appears.

---

# Next logical work — Round 47

Build a **zero-HgCdTe dependency/critical-path and tabletop dry-run audit** of the entire P16A-P16H / G0-G8 architecture.

At minimum:

1. construct one dependency DAG from infrastructure through P17;
2. identify circular prerequisites/deadlocks;
3. derive minimum relevant-subsystem commissioning sequences by material tier;
4. run synthetic PASS/HOLD/FAIL cases without presenting them as physical data;
5. fault-inject configuration change, holdout failure, RIE excursion and material shortage;
6. verify that holdouts/reserves remain protected under those faults;
7. derive the shortest controlled route from empty laboratory to first scientifically interpretable HgCdTe experiment;
8. separate true critical-path tasks from late-stage work that may be deferred.

Do not invent local equipment, measurements, yields or physical results.