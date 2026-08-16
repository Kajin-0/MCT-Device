# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 49  
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

`research/2026-08-16_checkpoint_after_operational_provenance_round49.md`

Then:

- `research/2026-08-16_checkpoint_after_digital_provenance_round48.md`
- `research/2026-08-16_checkpoint_after_control_system_dry_run_round47.md`
- `research/2026-08-16_checkpoint_after_sequential_material_release_round46.md`
- `research/2026-08-16_checkpoint_after_sample_genealogy_round45.md`
- `research/2026-08-16_checkpoint_after_information_optimal_jacobian_round44.md`
- `research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`
- earlier checkpoints as needed.

Latest machine/control artifacts:

- `tools/mct_provenance_store.py`
- `tools/run_round49_reference.py`
- `provenance/reference/README.md`
- `docs/DIGITAL_PROVENANCE_OPERATIONAL_REFERENCE_ROUND49.md`
- `travelers/P16K_PROVENANCE_REFERENCE_IMPLEMENTATION_REGISTER.md`
- `schemas/mct_provenance_bundle.schema.json`
- `tools/validate_mct_provenance.py`
- `travelers/P16J_DIGITAL_PROVENANCE_VALIDATION_REGISTER.md`
- `travelers/P16I_CONTROL_SYSTEM_DRY_RUN_REGISTER.md`
- `travelers/P16H_SEQUENTIAL_MATERIAL_RELEASE_CONTROL_REGISTER.md`

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND49.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND49.md`

---

# Maturity / implementation states — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — complete first build can execute without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — evidence supports a historical reproduction claim.
3. `REPRODUCIBLE-RELEASE` — repeated frozen-route stability/MSA/capability/yield/change-control evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual lab infrastructure physically selected/calibrated/implemented.
5. `P16D-SURROGATE-COMMISSIONING-COMPLETE` — relevant IQ/OQ/surrogate acceptance complete.
6. `P16E-REQUIREMENTS-ALLOCATION-COMPLETE` — uncertainty/requirements allocation complete.
7. `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY` — empirical campaign physically feasible and identifiable.
8. `P16G-MATERIAL-GENEALOGY-PLAN-READY` — required physical material genealogy/allocation feasible.
9. `P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY` — real lab has instantiated GO/HOLD/REWORK/STOP control.
10. `P16I-LOGIC-DRY-RUN-PASSED` — repository control logic passed declared synthetic fault tests.
11. `P16I-LAB-DRY-RUN-PASSED` — actual laboratory traveler/LIMS/control system passed a no-HgCdTe/surrogate dry run.
12. `P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED` — Round-48 schema + semantic validator pass repository tests.
13. `P16J-LAB-PROVENANCE-SYSTEM-READY` — real laboratory provenance system implemented.
14. `P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED` — Round-49 local transactional reference application passes its synthetic operational tests and Round-48 validation.
15. `P16K-LAB-DEPLOYMENT-QUALIFIED` — deployed lab instance of the operational provenance application is security/backup/instrument/configuration integrated and qualified.

Current repository state after Round 49, contingent only on final committed CI for P16K:

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
- `P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED = YES` after final CI PASS
- `P16K-LAB-DEPLOYMENT-QUALIFIED = NO / NOT PHYSICALLY INSTANTIATED`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != campaign ready != genealogy ready != release control ready != logic dry run != provenance validator != reference application != lab deployment != first-build ready != historical reproduction != reproducible release`.

---

# Round-49 operational provenance results — permanent if CI passes

## 1. Event-sourced SQLite reference application

`tools/mct_provenance_store.py` is stdlib-only.

Controlled SQLite tables use append-only UPDATE/DELETE triggers.

Do not interpret this as tamper-proof storage: an OS/database administrator can replace the database file.

## 2. Transaction semantics

Use `append_batch()` for irreversible multi-record transitions.

A material-state node and corresponding process event commit in one transaction or roll back together.

Round-49 self-test injects a duplicate-record failure and confirms the first record does not survive.

## 3. Canonical IDs

Generated form:

`MCT-<CLASS>-YYYYMMDDTHHMMSSZ-<12-hex>`.

`physical_object_id` persists across ordinary state transitions.

A physical split gets new physical-object IDs for descendants while retaining genealogy.

## 4. Application roles

Reference roles:

- `SYSTEM_ADMIN`
- `PROCESS_OWNER`
- `METROLOGY_OWNER`
- `DOE_OWNER`
- `MATERIAL_CONTROL`
- `RELEASE_AUTHORITY`
- `INDEPENDENT_REVIEWER`

These are software reference roles, not final staffing requirements.

## 5. Holdout logical sealing

Protected values live in a separate append-only `sealed_outcomes` table.

Normal measurement records carry field identity/raw references, not the protected value.

Protected outcome opening requires model freeze + independent-reviewer/admin role and emits a Round-48 `access_event`.

Security boundary:

`application logical seal != cryptographic encryption != DB-admin isolation`.

## 6. Raw data

Raw ingest is SHA-256 content addressed.

Path:

`objects/sha256/<first2>/<digest>`.

Copy is rehashed before atomic rename.

Bundle export rechecks stored raw bytes.

Synthetic byte tampering must be detected.

## 7. Reserve control

GO on a reserve-locked node is denied until an append-only `reserve_release` exists with:

- matching lock ID;
- exact frozen trigger key;
- basis record;
- release after lock.

## 8. Configuration supersession

Operational supersession does not rewrite the old configuration or historical gate.

It creates:

- append-only configuration-supersession relation;
- dependent gate invalidation rows.

Interpretation:

`historically valid gate != reusable gate after configuration change`.

New records cannot use the superseded configuration after supersession time.

## 9. Prototype signature semantics

Reference HMAC-SHA256 binds:

- target record ID;
- immutable payload SHA-256;
- actor label;
- key ID;
- signing time.

This is content authentication only.

Do not claim trusted signer identity, nonrepudiation, trusted time, protected key custody or regulatory compliance.

No secrets belong in repository files.

## 10. Synthetic traversal

`tools/run_round49_reference.py` performs synthetic:

`G0 -> G1 -> G2 -> G3 -> G4 -> G5 -> G6 -> G7 -> G8`.

The traversal includes:

- LPE-like state;
- anneal-like state;
- RIE-like state;
- detector state;
- raw measurement;
- singulation split;
- reserve sibling;
- package state;
- holdout lock;
- model freeze;
- outcome opening;
- evidence progression to `ALLOCATION-ELIGIBLE`.

No real HgCdTe ID may be introduced into this reference self-test.

## 11. Round-49 operational self-test set

Local standalone controls: 18.

They include:

- transaction rollback;
- gate-role denial;
- raw ingest;
- reserve GO denial;
- pre-freeze holdout denial;
- holdout actor denial;
- post-freeze opening;
- 9/9 nominal GO gates;
- signature good-key/wrong-key behavior;
- record UPDATE denial;
- record DELETE denial;
- raw tamper detection/recovery;
- configuration invalidation propagation;
- invalidated-gate reuse denial;
- superseded-configuration future-use denial;
- canonical ID generation.

Repository CI adds the required Round-48 generated-bundle semantic check.

---

# Round-48/47 controls retained

## P16F phase repair

Permanent chain:

`P16F skeleton -> Stage-0 -> P16F design definition -> P16G -> final P16F readiness`.

Do not reintroduce the old `P16F <-> P16G` cycle.

## Stage-0 scoped G0

Stage-0 G0 requires only what is needed to execute/interpret Stage-0:

- relevant P16C;
- relevant P16D;
- scope-adequate P16E discrimination;
- P16F skeleton;
- protected Stage-0 material;
- data/genealogy control;
- EH&S.

Do not require unrelated package/P17 state before upstream learning.

## Sequential gate equation

Every irreversible GO requires:

`T=PASS AND M=PASS AND all declared prerequisite assertions=PASS`.

## Holdout invariants

- prediction failure != execution invalidity;
- holdout outcome cannot tune the model it tests;
- holdouts are not spare inventory;
- QC access and protected outcome access are distinct;
- model freeze precedes protected outcome access.

## Rework

State-changing rework creates a new scientific state.

Protected fit/holdout/bridge role is not retained automatically.

## Evidence progression

`EMPIRICAL-REQUIRED -> DESIGN-IDENTIFIED -> DESIGN-RESOLUTION-VERIFIED -> EMPIRICAL-PRELIMINARY -> EMPIRICAL-VERIFIED -> DETECTOR-BRIDGED -> ALLOCATION-ELIGIBLE`.

No stage skipping.

---

# Permanent evidence discipline

- Never invent a missing number.
- Never promote transfer-family evidence into direct historical RP-01 evidence.
- Repetition does not promote evidence class.
- Structural DOE count is not power-based sample size.
- Physical descendant count is not independent experimental-unit count.
- Measurement uncertainty, operating-state uncertainty, process variation and tolerance remain distinct.
- Controlled method != physical implementation.
- Logic dry run != lab dry run.
- Repository validator != deployed lab system.
- Reference application != hardened laboratory provenance platform.
- Surrogate result != HgCdTe empirical evidence.
- Preserve negative searches, failed runs, failed predictions and rejected hypotheses.

---

# Canonical RP-01 / candidate anchors — do not drift

## RP-01 detector/process

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
- detector cutoff ~4.4 µm, convention open;
- D* ~`2e11 Jones` near 4 µm;
- historical high-frequency g-r ~24.5 nV/sqrtHz;
- 24.5 nV/sqrtHz is not historical 1-kHz noise;
- RP-01 lifetime/f3dB remains open.

## LPE candidate branch

- Cd0.96Zn0.04Te (111)B family;
- Honeywell covered graphite horizontal-slider topology;
- candidate center `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`;
- N2 purge -> H2;
- actual liquidus/thermal offset must be locally measured;
- absolute charge is apparatus-specific, never substrate-area scaled from another lab.

Authoritative mass convention:

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`

- Hg 200.59 g/mol;
- Cd 112.414;
- Te 127.60;
- xL=.082, yL=.810 -> wHg=0.2497382358, wCd=0.01250164993, wTe=0.7377601143.

---

# EH&S

Repository procedures/software do not authorize Hg/Cd/Br2/HBr/H2/CH4 handling, sealed high-temperature processing, RF/vacuum/high voltage, solvents, cryogens, or other hazardous laboratory work.

Physical execution requires real facility/institution controls.

---

# Next logical work — Round 50

If Round-49 final CI passes, build a **deployment/security simulation** around the reference application without HgCdTe.

Priority:

1. concrete single-host deployment profile;
2. service/operator identity separation;
3. protected-field encryption or explicit alternative isolation design;
4. signing-key lifecycle/rotation/revocation;
5. trusted-time policy;
6. backup/restore integrity qualification;
7. dummy instrument-ingest adapter;
8. configuration/calibration import adapter;
9. P16I laboratory-style dry run against the deployed surrogate system;
10. explicit threat/failure model for direct database/file access.

Do not use HgCdTe merely to commission software/security controls.
