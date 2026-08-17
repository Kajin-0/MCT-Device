# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 50  
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

`research/2026-08-16_checkpoint_after_deployment_security_round50.md`

Then:

- `research/2026-08-16_checkpoint_after_operational_provenance_round49.md`
- `research/2026-08-16_checkpoint_after_digital_provenance_round48.md`
- `research/2026-08-16_checkpoint_after_control_system_dry_run_round47.md`
- `research/2026-08-16_checkpoint_after_sequential_material_release_round46.md`
- `research/2026-08-16_checkpoint_after_sample_genealogy_round45.md`
- `research/2026-08-16_checkpoint_after_information_optimal_jacobian_round44.md`
- `research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`
- earlier checkpoints as needed.

Latest machine/control artifacts:

- `tools/mct_deployment_control.py`
- `tools/mct_protected_vault.py`
- `tools/round50_fixture.py`
- `tools/run_round50_security.py`
- `provenance/deployment/README.md`
- `docs/DIGITAL_PROVENANCE_DEPLOYMENT_SECURITY_ROUND50.md`
- `travelers/P16L_DEPLOYMENT_SECURITY_DRY_RUN_REGISTER.md`
- `tools/mct_provenance_store.py`
- `tools/run_round49_reference.py`
- `schemas/mct_provenance_bundle.schema.json`
- `tools/validate_mct_provenance.py`
- `travelers/P16K_PROVENANCE_REFERENCE_IMPLEMENTATION_REGISTER.md`
- `travelers/P16J_DIGITAL_PROVENANCE_VALIDATION_REGISTER.md`
- `travelers/P16I_CONTROL_SYSTEM_DRY_RUN_REGISTER.md`
- `travelers/P16H_SEQUENTIAL_MATERIAL_RELEASE_CONTROL_REGISTER.md`

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND50.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND50.md`

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
12. `P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED` — schema + semantic validator pass controlled repository tests.
13. `P16J-LAB-PROVENANCE-SYSTEM-READY` — real laboratory provenance system implemented.
14. `P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED` — local transactional reference application passes synthetic operational tests and Round-48 validation.
15. `P16K-LAB-DEPLOYMENT-QUALIFIED` — deployed laboratory instance is operationally integrated/qualified.
16. `P16L-REFERENCE-DEPLOYMENT-SECURITY-DRY-RUN-PASSED` — Round-50 reference deployment/security simulation passes declared identity, protected-data, key, clock, backup and adapter tests.
17. `P16L-LAB-SECURITY-DEPLOYMENT-READY` — real laboratory host/security deployment is instantiated and qualified.

Current after final Round-50 main CI:

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
- `P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED = YES`
- `P16K-LAB-DEPLOYMENT-QUALIFIED = NO / NOT PHYSICALLY INSTANTIATED`
- `P16L-REFERENCE-DEPLOYMENT-SECURITY-DRY-RUN-PASSED = YES` after final main CI PASS
- `P16L-LAB-SECURITY-DEPLOYMENT-READY = NO / NOT PHYSICALLY INSTANTIATED`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != campaign ready != genealogy ready != release control ready != logic dry run != provenance validator != reference application != reference deployment/security dry run != lab deployment != first-build ready != historical reproduction != reproducible release`.

---

# Round-50 deployment/security controls — permanent

## 1. Protected raw data is part of holdout secrecy

Do not seal only a parsed holdout value while copying the protected raw instrument file into the ordinary CAS.

Round-50 reference architecture requires:

`ordinary provenance/CAS != protected holdout vault/CAS`.

Ordinary measurement may retain the protected field name, `vault://sha256/...` URI and digest while protected bytes/value remain in the restricted vault.

## 2. No homebrew encryption

Round 50 deliberately uses split-store isolation rather than inventing encryption with unsuitable primitives.

Future production protected storage must use vetted authenticated encryption/key management or a formally approved equivalent isolation control.

`split-store reference isolation != encryption`.

## 3. Application identities are not trusted identities

Reference identities/sessions demonstrate authorization mechanics only.

`bearer session != authenticated human != OS service account != regulatory signer identity`.

## 4. Clock guard is not trusted time

Round 50 rejects obvious backward wall-clock movement.

`clock-regression guard != authoritative UTC != authenticated NTP/PTP != trusted timestamp`.

## 5. Key lifecycle

Reference key lifecycle:

`ACTIVE -> VERIFY_ONLY -> REVOKED`.

- VERIFY_ONLY may validate historical content but may not create new signatures.
- Revocation changes trust interpretation, not historical MAC equality.
- Verification events are retained.

No HSM/KMS/TPM, custody, escrow or nonrepudiation claim.

## 6. Backup integrity is separate from confidentiality

Round-50 backup uses SQLite backup, complete object trees, SHA-256 manifest and backup-HMAC authentication.

It deliberately excludes key files.

`integrity-authenticated backup != encrypted backup != disaster recovery qualification`.

## 7. Instrument preflight before byte copy

Configuration/calibration validity must be checked before instrument raw bytes are admitted to controlled storage.

A superseded configuration must block stale adapter use and dependent future gate reuse while preserving historical records.

## 8. Reference permissions

Repository simulation checks `0700` directories and `0600` key files/control files where applicable.

This does not prove actual uid/gid ownership, ACL/MAC confinement or root resistance.

---

# Round-50 controlled test result

Temporary validation branch:

`agent/round50-security-dryrun`

Candidate commit:

`1639fee3f75d9ba11df066ed7d194c946953ac3d`

Candidate Actions run:

`31980899498`

Candidate result:

- Round-48 regression PASS;
- Round-49 operational controls `19/19` PASS;
- Round-50 deployment/security controls `33/33` PASS;
- generated provenance records `50`;
- Round-48 semantic errors `0`;
- protected vault `1` protected raw + `1` sealed value;
- 3 key objects;
- 3 signature-verification events;
- 2 total configuration supersessions in combined traversal;
- 10 total gate invalidations.

Final repository P16L YES requires reproduction on the final controlled `main` commit.

---

# Round-49/48/47 controls retained

## Transaction/provenance

- controlled SQLite records are append-only at application/database-trigger layer;
- irreversible multi-record state transitions use one transaction;
- IDs use `MCT-<CLASS>-YYYYMMDDTHHMMSSZ-<12-hex>`;
- raw data are SHA-256 content addressed;
- configuration supersession preserves historical gate records but blocks reuse;
- reference HMAC signature is content authentication only.

## P16F phase repair

Permanent chain:

`P16F skeleton -> Stage-0 -> P16F design definition -> P16G -> final P16F readiness`.

Do not reintroduce the old `P16F <-> P16G` prerequisite cycle.

## Stage-0 scoped G0

Stage-0 G0 requires only what is needed for Stage-0 execution/interpretation, not unrelated package/P17 capability.

## Sequential release

Every irreversible GO requires:

`T=PASS AND M=PASS AND all declared prerequisite assertions=PASS`.

## Holdouts

- prediction failure != execution invalidity;
- holdout outcome cannot tune the tested model;
- holdouts are not spare inventory;
- QC and scientific-outcome access are distinct;
- model freeze precedes protected outcome access.

## Rework

State-changing rework creates a new scientific state. Protected fit/holdout/bridge identity is not retained automatically.

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
- Reference application != reference deployment/security simulation != hardened laboratory platform.
- Surrogate/software result != HgCdTe empirical evidence.
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

Repository procedures/software do not authorize Hg/Cd/Br2/HBr/H2/CH4 handling, sealed high-temperature processing, RF/vacuum/high voltage, solvents, cryogens or other hazardous laboratory work.

Physical execution requires real facility/institution controls.

---

# Next logical work — Round 51

Build a **reproducible real-host surrogate deployment harness** rather than adding another in-process security abstraction.

Priority:

1. declarative host bootstrap;
2. genuinely separate OS users/service accounts;
3. filesystem ownership/group/ACL tests;
4. service confinement;
5. select vetted encryption/KMS technology for protected storage;
6. signing/backup key custody and recovery;
7. external time synchronization/failure policy;
8. synthetic serial/network instrument endpoint;
9. concurrent writers;
10. crash/restart/power-loss simulation;
11. disk-full/read-only-filesystem cases;
12. backup loss/key loss/partial restore cases;
13. full no-HgCdTe P16I-style traversal on that deployed host.

Do not use HgCdTe merely to commission software/security controls.