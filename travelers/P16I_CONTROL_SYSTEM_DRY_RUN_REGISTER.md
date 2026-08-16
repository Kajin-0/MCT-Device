# P16I — zero-HgCdTe control-system dry-run register

**Status:** CONTROLLED SYSTEMS-QUALIFICATION REGISTER / ROUND 47  
**Date:** 2026-08-16 America/New_York  
**Use with:** P22D, P22C, P16F/P16G/P16H, P18, P36/P36A.

## 1. Purpose

Record synthetic and later laboratory dry runs of the material-release/control architecture before HgCdTe is placed at risk.

Two distinct states are tracked:

`P16I-LOGIC-DRY-RUN-PASSED = YES / NO`

`P16I-LAB-DRY-RUN-PASSED = YES / NO`

Round-47 repository state:

- `P16I-LOGIC-DRY-RUN-PASSED = YES`;
- `P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`.

---

# 2. Dry-run header

Dry-run ID: ____________________  
Repository/commit: ____________________  
P22D revision: ____________________  
P22C revision: ____________________  
P16F revision: ____________________  
P16G revision: ____________________  
P16H revision: ____________________  
Controller: ____________________  
Auditor: ____________________  
Date/time: ____________________

Layer:

- [ ] repository logic only
- [ ] actual laboratory control system using surrogate/dummy nodes

---

# 3. Dependency-graph register

| Node ID | state/output | prerequisite nodes | scope | invalidation class | notes |
|---|---|---|---|---|---|
| P16B | candidate branch |  | branch | configuration |  |
| P16C | relevant capability | P16B | physical | configuration |  |
| P16D | relevant acceptance | P16C | physical | calibration/configuration |  |
| P16E-SCOPE | contrast discrimination | P16D + requirement | measurement | uncertainty |  |
| P16F-SKEL | campaign skeleton | P16E-SCOPE | design | analytical |  |
| G0-STAGE0 | Stage-0 authorization | scoped P16C/D/E + P16F-SKEL + protected material | gate | mixed |  |
| STAGE0 | variance/repeatability data | G0-STAGE0 | empirical precursor | data |  |
| P16F-DESIGN | design-definition ready | STAGE0 + P16F-SKEL | design | analytical/data |  |
| P16G | full genealogy plan | P16F-DESIGN | material | material |  |
| P16F-READY | final campaign ready | P16F-DESIGN + P16G | design/material | mixed |  |
| G1 | formal F2 release | P16F-READY + P16G | gate | mixed |  |
| G2 | F3 release | F2 outputs | gate | mixed |  |
| G3 | F4 release | F3 outputs | gate | mixed |  |
| G4 | detector-bearing release | F4 Tier-1 outputs | gate | mixed |  |
| G5 | detector characterization | detector state | gate | metrology |  |
| G6 | singulation | characterized detector | gate | process/material |  |
| G7 | package | accepted die | gate | process/material |  |
| G8 | evidence promotion | final model + holdout | evidence | analysis |  |

Additional local nodes: ____________________

---

# 4. Cycle audit

Cycle-detection method/tool: ____________________  
Number of directed cycles before repair: __________  
Cycle IDs: ____________________

Round-47 controlled finding:

`P16F <-> P16G` when both are represented as monolithic completion states.

Repair applied:

- [ ] P16F skeleton state
- [ ] P16F design-definition state
- [ ] P16G consumes P16F design-definition state
- [ ] final P16F consumes P16G
- [ ] G0 Stage-0 uses scoped readiness

Directed cycles after repair: __________  
Required for logic PASS: `0` unless a cycle is formally shown not to be a prerequisite cycle.

---

# 5. P16F phased-state audit

## Skeleton

Protected quantity/decision defined: YES / NO  
Experimental unit defined: YES / NO  
Response vector defined: YES / NO  
Candidate factors/states defined: YES / NO  
Stage-0 variance/repeatability plan defined: YES / NO  
Preliminary feasibility/safety bounds defined: YES / NO

`P16F-CAMPAIGN-SKELETON-DEFINED = YES / NO`

## Design definition

Stage-0 data available: YES / NO  
Experimental unit frozen: YES / NO  
Model/design family frozen: YES / NO  
Structural count defined: YES / NO  
Perturbation-resolution check complete: YES / NO  
Blocking structure defined: YES / NO  
Holdout structural definition complete: YES / NO  
Stopping/invalidation logic complete: YES / NO

`P16F-DESIGN-DEFINITION-READY = YES / NO`

## Final readiness

P16F design definition ready: YES / NO  
P16G genealogy/material PASS: YES / NO  
Relevant infrastructure/EH&S ready: YES / NO

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = YES / NO`

---

# 6. G0 Stage-0 scope audit

| Requirement | needed for Stage-0? | evidence ID | PASS/HOLD |
|---|---|---|---|
| relevant P16C capability | YES |  |  |
| relevant P16D acceptance | YES |  |  |
| P16E contrast discrimination adequate | YES |  |  |
| P16F campaign skeleton | YES |  |  |
| protected Stage-0 material allocation | YES |  |  |
| data/genealogy controls | YES |  |  |
| EH&S authorization | YES |  |  |
| full P16F final readiness | NO | N/A | N/A |
| full final P16G plan | NO | N/A | N/A |
| unrelated package subsystem | NO unless evidence preservation requires it | N/A | N/A |
| P17 release | NO | N/A | N/A |

Scope audit PASS / HOLD: __________

---

# 7. Synthetic-node register

Only synthetic IDs are permitted in the repository logic layer.

| Synthetic node | parent | simulated role | configuration | holdout/reserve status | terminal state |
|---|---|---|---|---|---|
| SYN-R47-ROOT-001 |  | F2 root |  |  |  |
| SYN-R47-ANNEAL-001 | SYN-R47-ROOT-001 | F3 |  |  |  |
| SYN-R47-RIE-001 | SYN-R47-ANNEAL-001 | F4 |  |  |  |
| SYN-R47-DET-001 | SYN-R47-RIE-001 | detector bridge |  |  |  |
| SYN-R47-PKG-001 | SYN-R47-DET-001 | F5 |  |  |  |

Additional nodes: ____________________

---

# 8. Fault-injection execution log

| Scenario | injected fault | expected gate/action | expected protected-material response | actual logical/system response | invariant violation? | PASS/FAIL |
|---|---|---|---|---|---|---|
| FI-01 | package subsystem absent during F2 Stage-0 | upstream G0 may GO if unrelated | no upstream reserve loss |  |  |  |
| FI-02 | monolithic P16F/P16G cycle | detect/repair | none consumed |  |  |  |
| FI-03 | P06 repeatability inadequate | G1 HOLD | formal roots protected |  |  |  |
| FI-04 | formal LPE execution excursion | contain/P18/HOLD as scoped | siblings protected |  |  |  |
| FI-05 | anneal transition/multicarrier | G3 HOLD/STOP standard path | retain boundary evidence |  |  |  |
| FI-06 | RIE chamber excursion | G4 HOLD | detector descendants protected |  |  |  |
| FI-07 | technical PASS but material shortage | no GO | holdout/bridge preserved |  |  |  |
| FI-08 | valid holdout prediction failure | G8 promotion blocked | holdout retained as failed evidence |  |  |  |
| FI-09 | execution-invalid holdout | replacement rule | no outcome leakage |  |  |  |
| FI-10 | MFC replacement after commissioning | affected RIE releases HOLD | unrelated evidence preserved |  |  |  |
| FI-11 | request locked holdout as spare | deny | holdout remains locked |  |  |  |
| FI-12 | holdout reworked | original role invalid | reassignment only |  |  |  |
| FI-13 | identity/genealogy lost | quarantine/STOP | no guessed identity |  |  |  |
| FI-14 | detector test-chain invalid | G5 HOLD | detector preserved |  |  |  |
| FI-15 | package holdout failure | F5/G8 blocked | upstream valid data retained |  |  |  |

Additional local fault scenarios: ____________________

---

# 9. Configuration invalidation register

| Configuration change | affected acceptance/calibration | blocked future gates | prior evidence preserved? | unrelated subsystem preserved? | requalification route |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Dry-run checks:

- calendar-valid calibration does not override configuration change: PASS / FAIL
- minimum justified invalidation set applied: PASS / FAIL
- no global invalidation without common-cause evidence: PASS / FAIL

---

# 10. Holdout-access simulation

| Holdout ID | model-freeze ID | QC_ACCESS before freeze | outcome access before freeze | execution-invalid criterion | outcome after freeze | used to tune tested model? |
|---|---|---|---|---|---|---|
|  |  |  | MUST BE NO except allowed QC fields | MUST BE NO |  |  | MUST BE NO |

Failed prediction correctly retained as evidence: PASS / FAIL

Revised model assigned a new independent holdout before equivalent verification: PASS / FAIL / N/A

---

# 11. Reserve-lock simulation

| Reserve/holdout node | protected purpose | simulated failure elsewhere | unauthorized release attempted? | release trigger actually met? | final state |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Any reserve released solely because another sample failed: YES / NO  
Required: NO.

---

# 12. Rework-role simulation

| Node | original role | synthetic rework | scientific identity changed? | original role retained? | correct new role |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

State-changing rework automatically retains holdout/fit identity: YES / NO  
Required: NO.

---

# 13. Nominal synthetic traversal

| Stage | synthetic node | prerequisites PASS? | T | M | decision | next state |
|---|---|---|---|---|---|---|
| G0 |  |  |  |  |  |  |
| Stage-0 |  |  |  |  |  |  |
| G1/F2 |  |  |  |  |  |  |
| G2/F3 |  |  |  |  |  |  |
| G3/F4 Tier-1 |  |  |  |  |  |  |
| G4/detector |  |  |  |  |  |  |
| G5 |  |  |  |  |  |  |
| G6 |  |  |  |  |  |  |
| G7 |  |  |  |  |  |  |
| G8 |  |  |  |  |  |  |

No real HgCdTe ID may appear in a repository-only dry run.

---

# 14. Invariant audit

| Invariant | PASS/FAIL | evidence/scenario |
|---|---|---|
| I1 technical PASS alone cannot GO |  |  |
| I2 holdout cannot tune tested model |  |  |
| I3 holdout not spare inventory |  |  |
| I4 rework changes identity |  |  |
| I5 real experimental unit preserved |  |  |
| I6 configuration change invalidation correct |  |  |
| I7 unrelated downstream absence does not deadlock upstream |  |  |
| I8 surrogate != HgCdTe evidence |  |  |
| I9 prediction failure != invalidity |  |  |
| I10 genealogy loss cannot be guessed |  |  |
| I11 STOP retains record/disposition |  |  |
| I12 prerequisite graph acyclic |  |  |

---

# 15. Round-47 controlled result

Repository logic dry run:

- directed cycles before repair: `1`;
- identified cycle: `P16F <-> P16G`;
- Stage-0 scope ambiguity detected: `YES`;
- repairs applied: `YES`;
- directed cycles after repair: `0`;
- synthetic fault cases exercised: `15`;
- fail-safe post-repair cases: `15/15`.

Therefore:

`P16I-LOGIC-DRY-RUN-PASSED = YES`.

Actual laboratory control system does not yet exist, therefore:

`P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`.

---

# 16. Final disposition

Repository logic graph documented: YES / NO  
All detected prerequisite cycles resolved: YES / NO  
Mandatory fault classes exercised: YES / NO  
Holdout-access logic passed: YES / NO  
Reserve-lock logic passed: YES / NO  
Rework-role logic passed: YES / NO  
Configuration propagation logic passed: YES / NO  
No unresolved invariant violation: YES / NO

`P16I-LOGIC-DRY-RUN-PASSED = YES / NO`

Actual laboratory control system instantiated: YES / NO  
Actual digital traveler/LIMS exercised: YES / NO  
Actual configuration/calibration invalidation exercised: YES / NO  
Actual permissions/holdout locks exercised: YES / NO  
Surrogate/dummy end-to-end traversal complete: YES / NO

`P16I-LAB-DRY-RUN-PASSED = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** a logic dry-run pass validates internal control consistency only. It is not equipment commissioning, empirical verification, first-build readiness, historical reproduction or P17 release.