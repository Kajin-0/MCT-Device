# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 48  
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

`research/2026-08-16_checkpoint_after_digital_provenance_round48.md`

Then:

- `research/2026-08-16_checkpoint_after_control_system_dry_run_round47.md`
- `research/2026-08-16_checkpoint_after_sequential_material_release_round46.md`
- `research/2026-08-16_checkpoint_after_sample_genealogy_round45.md`
- `research/2026-08-16_checkpoint_after_information_optimal_jacobian_round44.md`
- `research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`
- `research/2026-08-16_checkpoint_after_subsystem_acceptance_round42.md`
- earlier checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND48.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND48.md`

Latest machine/control artifacts:

- `docs/DIGITAL_PROVENANCE_STATE_MACHINE_SPEC_ROUND48.md`
- `schemas/mct_provenance_bundle.schema.json`
- `tools/validate_mct_provenance.py`
- `provenance/README.md`
- `provenance/fixtures/`
- `.github/workflows/provenance-validation.yml`
- `travelers/P16J_DIGITAL_PROVENANCE_VALIDATION_REGISTER.md`
- `travelers/P16I_CONTROL_SYSTEM_DRY_RUN_REGISTER.md`
- `procedures/P22D_ZERO_HGCDTE_CONTROL_SYSTEM_DRY_RUN.md`
- `procedures/P22C_FIRST_BUILD_CAMPAIGN_EXECUTION_MATERIAL_RELEASE_CONTROL.md`
- `travelers/P16H_SEQUENTIAL_MATERIAL_RELEASE_CONTROL_REGISTER.md`
- `procedures/P22B_FIRST_BUILD_DESCENDANT_GENEALOGY_MATERIAL_ALLOCATION.md`
- `travelers/P16G_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION_REGISTER.md`
- `procedures/P22A_MULTI_SUBSYSTEM_INFORMATION_OPTIMAL_JACOBIAN_PROGRAM.md`
- `travelers/P16F_EMPIRICAL_JACOBIAN_INFORMATION_REGISTER.md`

---

# Maturity / implementation states — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — one complete first build can execute without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — evidence is sufficient to claim reproduction of Smith et al.
3. `REPRODUCIBLE-RELEASE` — repeated frozen-route stability/MSA/capability/yield/change-control evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual laboratory infrastructure is physically selected/calibrated/implemented.
5. `P16D-SURROGATE-COMMISSIONING-COMPLETE` — relevant IQ/OQ/surrogate acceptance complete.
6. `P16E-REQUIREMENTS-ALLOCATION-COMPLETE` — first-build uncertainty/requirements allocation complete.
7. `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY` — active empirical campaign is physically feasible and identifiable.
8. `P16G-MATERIAL-GENEALOGY-PLAN-READY` — required physical material genealogy/allocation feasible.
9. `P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY` — real lab has instantiated sequential GO/HOLD/REWORK/STOP control.
10. `P16I-LOGIC-DRY-RUN-PASSED` — repository-level control logic passed declared zero-HgCdTe synthetic fault tests.
11. `P16I-LAB-DRY-RUN-PASSED` — actual laboratory traveler/LIMS/control system passed a no-HgCdTe/surrogate dry run.
12. `P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED` — repository schema + semantic validator accept/reject controlled fixtures correctly.
13. `P16J-LAB-PROVENANCE-SYSTEM-READY` — actual laboratory provenance system enforces the Round-48 data/control invariants.

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
- `P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED = YES`
- `P16J-LAB-PROVENANCE-SYSTEM-READY = NO / NOT PHYSICALLY INSTANTIATED`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != campaign ready != genealogy ready != material-release control ready != logic dry-run pass != provenance-validator pass != lab provenance ready != lab dry-run pass != first-build ready != historical identity != reproducible release`.

---

# Round-48 machine provenance — permanent

## Two-layer validator

Structural schema:

`schemas/mct_provenance_bundle.schema.json`

Semantic validator:

`tools/validate_mct_provenance.py`

Schema dialect is deliberately JSON Schema Draft 2020-12.

The semantic runtime uses Python standard library only.

JSON Schema controls local record shape/types/enums.

The semantic validator controls cross-record invariants including:

- globally unique IDs;
- reference integrity;
- material genealogy DAG;
- root/parent consistency;
- process event lineage;
- chronology;
- configuration/calibration validity at use time;
- GO release logic;
- reserve lock/release;
- holdout freeze/access;
- training-data leakage;
- rework role reassignment;
- evidence-promotion sequence.

## Physical object versus scientific state

Never overwrite one sample row through process history.

Use:

`physical_object_id`

for persistent physical identity and:

`material_node.id`

for immutable scientific state.

Ordinary state transition:

`one input -> one output`, same physical-object ID.

Physical split:

`one input -> >=2 outputs`, distinct output physical-object IDs.

## Gate prerequisite assertions

Every gate contains machine-readable prerequisite assertions:

`{key, status, evidence_record_ids}`.

GO requires:

`technical_status=PASS`
`AND material_status=PASS`
`AND every prerequisite assertion=PASS`.

P22C/P16H remain authoritative for which prerequisite keys must exist at each G0-G8 gate.

## Holdout sealing

A protected holdout outcome may be physically acquired before model freeze, but protected fields may not be opened.

QC and OUTCOME access are separate events.

QC before freeze cannot overlap protected response fields.

OUTCOME requires an applicable earlier model freeze.

Protected holdout response fields cannot appear in training measurements for the model being tested.

## Reserve control

Reserve is append-only:

`reserve_lock -> reserve_release`.

A lock freezes a release-trigger key.

A release must use the same key and cite basis records.

GO before valid release is rejected.

## Rework

State-changing rework is:

`old material node -> REWORK event -> new material node`.

Protected roles `HOLDOUT`, `FIT_POINT`, and `DETECTOR_BRIDGE` do not survive automatically.

Explicit equivalence approval is required to retain them.

## Evidence promotion

Allowed progression only:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`.

No skipped states.

Verified and later states require PASS holdout.

Detector-bridged/allocation states require detector bridge.

Allocation-eligible additionally requires uncertainty and valid-range references.

## Raw-data identity

Measurement raw-data references require URI + SHA-256 digest.

Repository validator verifies digest syntax only.

Future lab implementation must verify actual bytes.

---

# Round-48 synthetic machine test

Controlled fixtures:

- valid: `1`
- invalid: `8`

Invalid cases:

1. GO with material FAIL;
2. genealogy cycle;
3. holdout outcome before model freeze;
4. protected holdout response leaked into training;
5. locked reserve consumed;
6. reserve release wrong trigger key;
7. stale configuration/calibration used;
8. state-changing rework retains protected holdout/bridge role.

Development result:

`SELF-TEST PASSED: 1 valid + 8 invalid fixture(s)`.

The nominal bundle also produced zero errors against the declared Draft-2020-12 JSON Schema during Round-48 development.

This is software logic validation only, not physical reliability.

---

# Round-47 P16F phase repair — permanent

Do not represent P16F as a single prerequisite node before Stage-0.

States:

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

---

# Round-47 G0 scope rule — permanent

Stage-0 G0 does not require final P16F/P16G/P17 or unrelated package capability.

It requires only:

- relevant P16C capability;
- relevant P16D acceptance;
- scope-adequate P16E measurement discrimination;
- `P16F-CAMPAIGN-SKELETON-DEFINED`;
- protected Stage-0 material allocation;
- data/genealogy controls;
- EH&S.

---

# Permanent systems-control invariants

1. No irreversible GO unless technical/scientific eligibility and post-commit material feasibility pass.
2. Every declared gate prerequisite must be explicit and traceable.
3. Holdout outcome cannot tune the model it tests.
4. Holdouts are not spare inventory.
5. Reserve release requires its controlled trigger.
6. State-changing rework invalidates old protected role by default.
7. Statistical independence follows the actual experimental unit.
8. Configuration change can invalidate acceptance before calendar calibration expiry.
9. Calibration is bound to configuration.
10. Unrelated late-stage subsystem absence must not deadlock an upstream experiment.
11. Surrogate commissioning does not become HgCdTe empirical evidence.
12. Prediction failure is not execution invalidity.
13. Lost genealogy is never reconstructed from expected performance.
14. STOP retains failed/negative evidence and terminal disposition.
15. Controlled prerequisite graph remains acyclic or any intentional loop must be proven not to be a completion prerequisite.
16. Physical sample state history is append-only in scientific identity.
17. No evidence-state skipping.

---

# Permanent evidence discipline

- Never invent a missing number.
- Never convert transfer-family evidence into historical RP-01 fact.
- Repetition does not promote evidence class.
- Structural DOE count is not statistical-power sample size.
- Physical descendant count is not independent-unit count.
- Physical separation does not create upstream statistical independence.
- Measurement uncertainty, operating-state uncertainty, process variation and tolerance remain distinct.
- A controlled method is not physical implementation.
- A logic dry-run is not a lab dry-run.
- A repository provenance pass is not lab provenance readiness.
- A lab dry-run is not HgCdTe process validation.
- Historical reference value is not production tolerance.
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

- common P11/P12 gain cancels from D* when same linear path/frequency/loading applies;
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

- independent experimental units;
- descendant pieces;
- usable area/packing;
- yield/power/failure reserve.

Program is a genealogy DAG, not a sum of F1–F5 counts.

Default P05 branch remains dedicated material-control sibling until same-specimen Hall->anneal/device compatibility is qualified.

## Sequential release

Every irreversible gate returns only:

`GO / HOLD / REWORK / STOP`.

GO requires T=PASS and M=PASS plus explicit prerequisite assertions.

Holdout validity QC and scientific outcome access remain separate.

Reserve release requires its explicit trigger/substitute/redesign.

---

# Next logical work — Round 49

Make the Round-48 provenance layer operationally instantiable.

Priority:

1. canonical ID namespaces/lifecycle;
2. local file/database storage and transaction semantics;
3. actor/role/permission matrix;
4. holdout sealed-field enforcement;
5. raw-data ingest + SHA-256 verification;
6. configuration supersession/invalidation propagation;
7. electronic signature/audit semantics without unsupported regulatory claims;
8. a small local reference implementation that creates and validates records;
9. automated synthetic G0–G8 traversal through that implementation.

Round 49 should remain zero-HgCdTe.
