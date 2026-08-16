# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 47  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual/booklet executable by a competent researcher without undocumented tribal knowledge.

Canonical first process:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is no end-to-end reproducible physical release yet.

---

# READ FIRST

Latest checkpoint:

`research/2026-08-16_checkpoint_after_control_system_dry_run_round47.md`

Then:

- `research/2026-08-16_checkpoint_after_sequential_material_release_round46.md`
- `research/2026-08-16_checkpoint_after_sample_genealogy_round45.md`
- `research/2026-08-16_checkpoint_after_information_optimal_jacobian_round44.md`
- `research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`
- `research/2026-08-16_checkpoint_after_subsystem_acceptance_round42.md`
- `research/2026-08-16_checkpoint_after_minimum_lab_capability_round41.md`
- earlier checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND47.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND47.md`

Latest systems/control modules:

- `calculations/RP01_CONTROL_DEPENDENCY_FAULT_INJECTION.md`
- `procedures/P22D_ZERO_HGCDTE_CONTROL_SYSTEM_DRY_RUN.md`
- `travelers/P16I_CONTROL_SYSTEM_DRY_RUN_REGISTER.md`
- `procedures/P22C_FIRST_BUILD_CAMPAIGN_EXECUTION_MATERIAL_RELEASE_CONTROL.md`
- `travelers/P16H_SEQUENTIAL_MATERIAL_RELEASE_CONTROL_REGISTER.md`
- `procedures/P22B_FIRST_BUILD_DESCENDANT_GENEALOGY_MATERIAL_ALLOCATION.md`
- `travelers/P16G_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION_REGISTER.md`
- `procedures/P22A_MULTI_SUBSYSTEM_INFORMATION_OPTIMAL_JACOBIAN_PROGRAM.md`
- `travelers/P16F_EMPIRICAL_JACOBIAN_INFORMATION_REGISTER.md`
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`
- `travelers/P16E_FIRST_BUILD_UNCERTAINTY_ALLOCATION_REGISTER.md`

---

# Maturity / implementation states — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — complete first build can execute without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — evidence is sufficient to claim reproduction of Smith et al.
3. `REPRODUCIBLE-RELEASE` — repeated frozen-route stability/MSA/capability/yield/change-control evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual lab infrastructure is physically selected/calibrated/implemented.
5. `P16D-SURROGATE-COMMISSIONING-COMPLETE` — relevant IQ/OQ/surrogate acceptance complete.
6. `P16E-REQUIREMENTS-ALLOCATION-COMPLETE` — first-build uncertainty/requirements allocation complete.
7. `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY` — empirical campaign physically feasible and identifiable.
8. `P16G-MATERIAL-GENEALOGY-PLAN-READY` — required physical material genealogy/allocation feasible.
9. `P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY` — real lab has instantiated sequential GO/HOLD/REWORK/STOP control.
10. `P16I-LOGIC-DRY-RUN-PASSED` — repository-level control logic passed declared zero-HgCdTe synthetic fault tests.
11. `P16I-LAB-DRY-RUN-PASSED` — actual laboratory traveler/LIMS/control system passed a no-HgCdTe/surrogate dry run.

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
- `P16I-LOGIC-DRY-RUN-PASSED = YES`
- `P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != campaign design ready != genealogy ready != material-release control ready != logic dry-run pass != lab dry-run pass != first-build ready != historical identity != reproducible release`.

---

# Round-47 P16F phase repair — permanent

Do not represent P16F as a single prerequisite node before Stage-0.

Three scoped states now exist:

### `P16F-CAMPAIGN-SKELETON-DEFINED`

Pre-Stage-0 minimum:

- protected quantity/decision;
- response vector;
- experimental unit;
- candidate factors/states;
- Stage-0 variance/repeatability plan;
- preliminary feasibility/safety bounds.

### `P16F-DESIGN-DEFINITION-READY`

Post-Stage-0 input to P16G:

- Stage-0 variance/repeatability;
- model/design family;
- structural count;
- perturbation-resolution window;
- block/hard-to-change structure;
- holdout structural definition;
- stopping/invalidation logic.

### `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`

Final state after P16G material/genealogy feasibility plus relevant infrastructure/EH&S.

Permanent chain:

`P16F skeleton -> Stage-0 -> P16F design definition -> P16G -> final P16F readiness`.

This repaired the Round-47 detected `P16F <-> P16G` circular prerequisite.

---

# Round-47 G0 scope rule — permanent

Stage-0 G0 does not require final P16F/P16G/P17 or unrelated package capability.

It requires only what is needed to execute and interpret the immediate Stage-0 edge:

- relevant P16C capability;
- relevant P16D acceptance;
- scope-adequate P16E measurement discrimination;
- `P16F-CAMPAIGN-SKELETON-DEFINED`;
- protected Stage-0 material allocation;
- data/genealogy controls;
- EH&S.

Formal later campaign releases require the stronger design/genealogy states appropriate to those edges.

---

# Round-47 dry-run result

Repository-level dependency/fault-injection exercise:

- directed prerequisite cycles before repair: `1`;
- detected cycle: `P16F <-> P16G`;
- Stage-0 scope/deadlock ambiguity: detected;
- directed prerequisite cycles after repair: `0`;
- declared synthetic fault cases exercised: `15`;
- fail-safe post-repair dispositions: `15/15`.

The 15/15 result is a logic-test result only, not a reliability probability or physical process statistic.

Key tested cases:

- downstream package subsystem absent during upstream Stage-0;
- P06 metrology insufficiency;
- LPE excursion;
- anneal multicarrier boundary;
- RIE excursion;
- technical PASS with material-feasibility FAIL;
- valid holdout prediction failure;
- execution-invalid holdout;
- MFC/configuration change;
- attempted holdout-as-spare use;
- holdout rework;
- genealogy loss;
- detector test-chain failure;
- package holdout failure.

---

# Permanent systems-control invariants

1. No irreversible GO unless both technical/scientific eligibility and post-commit material feasibility pass.
2. Holdout outcome cannot tune the model it tests.
3. Holdouts are not spare inventory.
4. State-changing rework invalidates the old protected role by default.
5. Statistical independence follows the actual experimental unit.
6. Configuration change can invalidate acceptance before calendar calibration expiry.
7. Unrelated late-stage subsystem absence must not deadlock an upstream experiment.
8. Surrogate commissioning does not become HgCdTe empirical evidence.
9. Prediction failure is not execution invalidity.
10. Lost genealogy is never reconstructed from expected performance.
11. STOP retains failed/negative evidence and terminal disposition.
12. Controlled prerequisite graph must remain acyclic or any intentional loop must be proven not to be a completion prerequisite.

---

# Permanent evidence discipline

- Never invent a missing number.
- Never convert transfer-family evidence into historical RP-01 fact.
- Repetition does not promote evidence class.
- Structural DOE count is not statistical-power sample size.
- Physical descendant count is not independent-unit count.
- Physical separation does not create upstream independence.
- Measurement uncertainty, operating-state uncertainty, process variation and tolerance remain distinct.
- A controlled method is not physical implementation.
- A logic dry-run is not a lab dry-run.
- A lab dry-run is not HgCdTe process validation.
- A historical reference value is not a production tolerance.
- Preserve negative searches, failed runs, failed predictions and rejected hypotheses.

---

# Canonical technical anchors — do not drift

## RP-01 material/device

- n-HgCdTe on insulating CdZnTe;
- nominal `x≈0.30`;
- active thickness ~9.5 µm;
- reported n ~`9.8e14 cm^-3`;
- reported electron mobility ~`4.0e4 cm^2/Vs`;
- anodic oxide ~80 nm;
- Mask-2 4–5 µm;
- 80 °C / 30 min prebake;
- chlorobenzene 30 min;
- RIE printed as `CH4/5H2`, total 64 sccm, 100 mTorr, 50 W, 60 s;
- same-lineage candidate interpretation 1:5 gives 10.6667/53.3333 sccm;
- Cr/Au 30/270 nm;
- contacts ~300×300 µm;
- gaps 50–400 µm in 50-µm steps;
- key data ~80 K, 10 V/cm, 1 kHz;
- detector cutoff ~4.4 µm with convention open;
- D* ~`2e11 Jones` near 4 µm;
- historical high-frequency g-r ~24.5 nV/sqrtHz;
- 24.5 nV/sqrtHz is not the historical 1-kHz noise;
- RP-01 lifetime/f3dB curve remains open.

## LPE candidate branch

- Cd0.96Zn0.04Te (111)B family;
- Honeywell covered graphite horizontal-slider topology;
- candidate center `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`;
- N2 purge -> H2;
- actual liquidus/thermal offset must be locally measured;
- absolute charge is apparatus coordinate, never scaled from another lab by substrate area.

Authoritative mass convention in `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`:

- Hg 200.59 g/mol;
- Cd 112.414;
- Te 127.60;
- at xL=.082, yL=.810: wHg=0.2497382358, wCd=0.01250164993, wTe=0.7377601143.

---

# Round-43 analytical results retained

- common P11/P12 gain cancels from D* when the same linear path/frequency/loading applies;
- `S_D,A = 0.5-gamma_A`;
- gap couples area and field: `S_D,L=0.5-gamma_L-s_R,E+s_n,E` for fixed physical V and A=WL;
- electronics subtraction with beta=`e_elec^2/e_det^2` has sensitivities `1+beta` and `-beta`;
- use covariance, not blind RSS.

---

# Round-44/45/46 rules retained

## Information design

For symmetric derivative pairs:

`SE(g_hat)=sigma/[sqrt(2m) Delta u]`.

At alpha=.05, power=.80 normal planning approximation:

`eta_min≈1.981/sqrt(m)` where `eta=|g|Delta u/sigma`.

Require:

`information lower bound <= Delta u <= same-regime physics upper bound`.

## Genealogy

Track separately:

- independent units;
- descendant pieces;
- usable area/packing;
- yield/power/failure reserve.

Program is a genealogy DAG, not a sum of F1-F5 counts.

Default P05 branch remains a dedicated material-control sibling until same-specimen Hall->anneal/device compatibility is qualified.

## Sequential release

Every irreversible gate returns only:

`GO / HOLD / REWORK / STOP`.

GO requires:

`T=PASS and M=PASS`.

Holdout validity QC and scientific outcome access remain separate.

Reserve release requires its explicit trigger/substitute/redesign.

---

# Next logical work — Round 48

Build the machine-checkable **digital provenance / traveler state model**.

Priority objects:

- immutable material node ID;
- parent-child genealogy edge;
- treatment/process event;
- measurement event/raw-data reference;
- configuration object;
- calibration object;
- gate decision;
- holdout lock/access event;
- reserve lock/release event;
- model-freeze event;
- deviation/rework event;
- evidence-promotion event;
- actor/signature/audit event.

Priority invariants to encode:

- no GO without required prerequisite objects and T/M PASS;
- no protected holdout outcome access before model freeze;
- no reserve reassignment before release trigger;
- no reworked node retaining protected role without explicit reassignment/equivalence;
- no descendant without immutable parent link;
- configuration change propagates review/HOLD to dependent future gates;
- no deleted failed/negative event history.

Round 48 should remain zero-HgCdTe and should prepare the future real-lab P16I dry run.