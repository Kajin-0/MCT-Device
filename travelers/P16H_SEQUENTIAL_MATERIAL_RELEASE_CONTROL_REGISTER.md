# P16H — sequential campaign execution / material-release control register

**Status:** CONTROLLED PRE-EXECUTION REGISTER / ROUND 46  
**Date:** 2026-08-16 America/New_York  
**Use with:** P22C, P16E/P16F/P16G, P18, P20-P25, P33/P35/P36.

## 1. Purpose

Provide the future laboratory record for deciding whether each HgCdTe material node may cross the next irreversible development boundary.

Program state:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY = YES / NO`.

Current repository state:

`NO / NOT PHYSICALLY INSTANTIATED`.

P16H controls execution. It does not create empirical evidence and does not supersede P16A or P17.

---

# 2. Program header

Laboratory/facility: ____________________  
Campaign/program revision: ____________________  
P16E revision: ____________________  
P16F revision: ____________________  
P16G revision: ____________________  
P22C revision: ____________________  
Protected detector requirement(s): ____________________  
Date opened: ____________________

Named roles:

Process owner: ____________________  
Metrology owner: ____________________  
DOE/statistical owner: ____________________  
Genealogy/material-control owner: ____________________  
EH&S/facility authority: ____________________  
Independent holdout reviewer: ____________________

---

# 3. Allowed gate outcomes

- `GO`
- `HOLD`
- `REWORK`
- `STOP`

No free-text substitute may replace the controlled outcome.

For every `REWORK`, identify the qualified route and the new sample/evidence role after rework.

---

# 4. Active configuration register

| Configuration class | active revision/ID | calibration/reference | effective date | change since prior gate? | impact review |
|---|---|---|---|---|---|
| LPE apparatus/boat/source |  |  |  |  |  |
| LPE gas/thermal control |  |  |  |  |  |
| FTIR/P06 |  |  |  |  |  |
| Hall/P05 contacts + measurement chain |  |  |  |  |  |
| anneal apparatus |  |  |  |  |  |
| lithography/wet/passivation |  |  |  |  |  |
| RIE chamber |  |  |  |  |  |
| Cr/Au deposition |  |  |  |  |  |
| detector test station |  |  |  |  |  |
| singulation |  |  |  |  |  |
| package/Dewar |  |  |  |  |  |
| data/reduction/model |  |  |  |  |  |

Any decision-affecting change requires impact review before prior gate approvals are reused.

---

# 5. G0 — active-campaign authorization

Campaign: F1 / F2 / F3 / F4 / F5 / other: __________

| Prerequisite | evidence ID | PASS/HOLD | notes |
|---|---|---|---|
| relevant P16C capability physically identified |  |  |  |
| relevant P16D acceptance current |  |  |  |
| relevant P16E uncertainty allocation adequate |  |  |  |
| active P16F campaign design ready |  |  |  |
| active P16G material/genealogy feasible |  |  |  |
| data/genealogy system active |  |  |  |
| EH&S/facility authorization current |  |  |  |

G0 decision: GO / HOLD / REWORK / STOP  
Released material class/scope: ____________________  
Approver(s): ____________________  
Date/time: ____________________

---

# 6. G1 — Stage-0 LPE -> formal F2 release

Selected F2 branch: ____________________  
Formal design revision: ____________________

| G1 item | value/evidence | status |
|---|---|---|
| actual LPE apparatus branch instantiated |  |  |
| P06 repeatability dataset |  |  |
| Stage-0 independent-growth variance |  |  |
| morphology/feasible region |  |  |
| information lower bounds on factor ranges |  |  |
| same-regime upper bounds |  |  |
| exact F2 design matrix frozen |  |  |
| run-order/block plan frozen |  |  |
| F2 holdout states locked |  |  |
| Stage-0 reuse disposition frozen |  |  |
| P16G root/material balance PASS |  |  |

G1 decision: GO / HOLD / REWORK / STOP  
Formal roots authorized: ____________________  
Unauthorized/reserve roots: ____________________  
Approver(s): ____________________

---

# 7. F2 formal growth execution ledger

| execution order | root ID | design row | source-use/block | realized state data ID | P06 map ID | execution valid? | fit/holdout/failure role | current release state |
|---:|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Adaptive selection log if used:

| decision epoch | candidate states | criterion/model revision | predicted information/decision value | selected state | rejected states retained? | reviewer |
|---:|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

---

# 8. G2 — grown root/descendant -> anneal release

Complete one row per proposed anneal release.

| Gate ID | root/node ID | P06 accepted? | morphology/usable region | F2 role | P05 branch reserved? | F3 role/history ID | post-commit material PASS? | decision |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Root-selection basis:

- [ ] predetermined design state
- [ ] predetermined control/center
- [ ] frozen adaptive-information criterion
- [ ] deliberate boundary/failure challenge
- [ ] other controlled basis: ____________________

Do not use post-hoc appearance/performance alone as the selection rule.

---

# 9. F3 anneal execution ledger

| anneal history ID | root/node | ampoule/enclosure | co-loaded sibling IDs | Ts/THg trace | dwell/cooldown | independent-history basis | deviation? | post-state role |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Post-anneal state:

| node ID | P05 state | P06 preservation | stable n-like / transition / p-like / other | one-carrier model eligible? | boundary evidence retained? | downstream candidate? |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

---

# 10. G3 — annealed node -> RIE/passivation release

| Gate ID | node ID | anneal valid? | P05 state acceptable? | P06 required check PASS? | F4 role | RIE acceptance current? | witness/detector allocation feasible? | decision |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

If transition/multicarrier material is stopped from standard detector path, terminal/useful role: ____________________

---

# 11. F4 Tier-1 witness-treatment ledger

| chamber run | design state | root/block | oxide/recession witness | Hall witness | LBIC/depth witness | TLM/contact witness | realized chamber-state ID | stability check | Tier-2 candidate? |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

Tier-1 failures remain data unless execution-invalid under a predeclared rule.

---

# 12. G4 — witness-qualified RIE state -> full detector descendant

| Gate ID | chamber/treatment state | material-state evidence PASS? | stability PASS? | detector information need | dominated by lower-burden state? | full detector slot reserved? | post-commit material PASS? | decision |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Detector-bearing state category:

- [ ] center/baseline
- [ ] high-information contrast
- [ ] required interaction/combined state
- [ ] independent holdout
- [ ] detector bridge
- [ ] other: ____________________

---

# 13. Detector fabrication genealogy ledger

| detector ID | root | anneal | passivation | RIE | Cr/Au | mask/CD | contact pair/gap | handoff-time record | pre-singulation state |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

---

# 14. G5 — completed detector -> matched P10-P13/F1 characterization

| Gate ID | detector ID | continuity/I-V | geometry measured | test-chain acceptance current | heating/loading guard | matched-state plan | decision |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Measurement sequence actually used: ____________________

| detector ID | P10 | P11 | P12 | P13 | F1 | any state-changing event? | final bare-device role |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

---

# 15. G6 — characterized detector -> singulation

| Gate ID | detector ID | pre-cut baseline complete? | P35 branch/revision | street/edge exclusion frozen? | package geometry compatible? | unsingulated comparator protected? | decision |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Post-singulation:

| die ID | parent detector | edge/chip result | electrical check | noise/response check if required | package eligible? | terminal role if not |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

---

# 16. G7 — singulated die -> actual package build

Surrogate package screen revision/result: ____________________  
Selected P33 construction family: ____________________

| Gate ID | die ID | post-singulation PASS? | pre-package baseline ID | package DOE/build role assigned? | protected die reserve after commit PASS? | decision |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Actual package ledger:

| package ID | die ID | construction level | independent build? | post-package P10 | P12 | P13 | P11 if used | holdout/fit role | terminal state |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

---

# 17. Holdout lock / quarantine register

| holdout ID | campaign | independent-unit basis | protected model/decision | response vector | process state frozen? | model-freeze ID | validity-QC access allowed | scientific result opened? | final result |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

### Replacement holdout rule

Predeclared execution-invalidity criteria: ____________________  
Replacement rule: ____________________

A prediction failure alone is not an execution-invalidity criterion.

---

# 18. Reserve-lock register

| reserve node/class | protected purpose | count/geometry | prohibited use before trigger | release trigger | state LOCKED/RELEASED | release decision ID |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Reserve classes should remain distinct:

- process-failure reserve;
- metrology reserve;
- layout reserve;
- holdout reserve;
- destructive-FA reserve;
- statistical-power reserve.

No guessed global percentage is permitted.

---

# 19. Post-commit material-feasibility sheet

Complete before every high-value `GO` at G2/G3/G4/G6/G7.

Gate ID: ____________________  
Proposed node/action: ____________________

| Protected future obligation | required root/history/geometry | available before | consumed/locked by action | available after | feasible after? |
|---|---|---:|---:|---:|---|
| active-fit units |  |  |  |  |  |
| independent holdouts |  |  |  |  |  |
| detector bridges |  |  |  |  |  |
| package builds |  |  |  |  |  |
| archive |  |  |  |  |  |
| destructive FA |  |  |  |  |  |
| power reserve |  |  |  |  |  |

Post-commit feasibility: PASS / HOLD / FAIL  
P16G revision used: ____________________

---

# 20. Run-order / blocking register

| campaign | factor/state | easy/hard/sequential | randomized within block? | block/covariate | alias risk | mitigation/model term |
|---|---|---|---|---|---|---|
| F2 |  |  |  |  |  |  |
| F3 |  |  |  |  |  |  |
| F4 |  |  |  |  |  |  |
| F5 |  |  |  |  |  |  |

Execution-order log:

| sequence | campaign | design row | root/block | source/chamber/ampoule/package batch | calendar/operator | deviation |
|---:|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

---

# 21. Next-action decision register

| decision epoch | current protected uncertainty | candidate action | expected decision-variance reduction | HgCdTe burden | optionality lost | confounding risk | surrogate alternative | dominated? | selected? |
|---:|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

If a common validated cost metric is used, identify it here: ____________________

Do not construct an arbitrary scalar cost from incomparable material classes.

---

# 22. Failure / deviation ledger

| event ID | node/run | stage | observation | preliminary class | siblings frozen? | P18 route | holdout touched? | rework/stop/replacement decision | final disposition |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

Allowed preliminary classes:

- measurement invalidity;
- handling damage;
- process excursion;
- true treatment response;
- identity/genealogy error;
- unknown.

A true treatment failure remains campaign data.

---

# 23. Rework role reassignment

| node ID | original role | rework route | qualified route ID | physical state after rework | original role still valid? | new role | reviewer |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Do not retain holdout/fit identity automatically after state-changing rework.

---

# 24. G8 evidence-promotion register

| campaign/quantity | final model revision | fit diagnostics PASS? | holdout result | uncertainty | local valid range | detector bridge | P20/P16E update ID | empirical state |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Allowed empirical progression:

`EMPIRICAL-REQUIRED -> DESIGN-IDENTIFIED -> DESIGN-RESOLUTION-VERIFIED -> EMPIRICAL-PRELIMINARY -> EMPIRICAL-VERIFIED -> DETECTOR-BRIDGED -> ALLOCATION-ELIGIBLE`.

---

# 25. Campaign stopping review

For each active campaign:

Protected decision: ____________________

- allocated uncertainty requirement met: YES / NO
- additional runs expected to materially reduce decision variance: YES / NO
- current model family still valid: YES / NO
- feasible perturbation range still resolves target effect: YES / NO
- holdout/bridge reserve threatened by further consumption: YES / NO
- infrastructure/configuration acceptance current: YES / NO

Decision:

- [ ] continue
- [ ] pause/HOLD
- [ ] redesign
- [ ] close campaign and release remaining reserve
- [ ] STOP branch

Rationale: ____________________

---

# 26. P16H final disposition

Named release roles assigned: YES / NO  
Relevant configuration/calibration registry active: YES / NO  
Gate IDs and records instantiated: YES / NO  
Technical eligibility and material feasibility evaluated separately: YES / NO  
Holdouts locked and model-freeze rule instantiated: YES / NO  
Reserve locks/release triggers instantiated: YES / NO  
Run-order/blocking plan controlled: YES / NO  
Failure/P18 routing controlled: YES / NO  
Rework role-reassignment rule active: YES / NO  
Post-commit feasibility checked before irreversible releases: YES / NO  
Audit trail complete: YES / NO  
EH&S/facility authority current: YES / NO

Final state:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** P16H readiness means the release-control system is instantiated. It does not mean any individual gate is GO, any empirical campaign has succeeded, P16A is ready, or P17 is released.