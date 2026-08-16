# P16G — sample genealogy / HgCdTe material-allocation register

**Status:** CONTROLLED PRE-EXPERIMENT REGISTER / ROUND 45  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16F, P22B, P21/P22/P22A, P23, P24/P25, P33/P35, P05/P06/P10-P13.

## 1. Purpose

Provide the future laboratory fill-in record proving that the empirical-Jacobian program has a physically feasible, statistically valid sample genealogy and material-allocation plan.

Program state:

`P16G-MATERIAL-GENEALOGY-PLAN-READY = YES / NO`.

Current repository state:

`NO / NOT PHYSICALLY INSTANTIATED`.

P16G is a prerequisite input to the P16F genealogy/material-feasibility gate. It is not empirical verification, build readiness or P17 release.

---

# 2. Program header

Laboratory/facility: ____________________  
Responsible process engineer: ____________________  
Responsible statistician: ____________________  
P16G revision: ____________________  
P16F revision: ____________________  
P22B revision: ____________________  
Date opened: ____________________  
Selected F2 design branch: ____________________  
Protected detector requirement(s): ____________________

---

# 3. Structural-count basis

Selected F2 fitted-design branch:

- [ ] 9-growth Jacobian-first axial
- [ ] 15-growth BBD
- [ ] 17-growth FCCCD
- [ ] 11-growth Stage-2 two-factor quadratic
- [ ] custom constrained/sequential design

`N_fit`: __________  
New independent F2 holdouts: __________  
Stage-0 growths reusable as formal design rows: __________  
Stage-0 nonreusable pilot growths: __________

Calculated independent-growth structural requirement:

`N_G,F2,total = N_fit + N_holdout,new + N_stage0,nonreusable = __________`.

Current reference lower bounds under the Round-45 three-holdout/reusable-center assumptions:

- 9-run branch -> `>=12` roots;
- 15-run BBD -> `>=18` roots;
- 17-run FCCCD -> `>=20` roots;
- 11-run Stage-2 -> `>=14` roots.

These are design/root counts, not physical-area or procurement quantities.

---

# 4. Stage-0 reuse disposition

| Growth ID | Stage-0 purpose | same apparatus/process revision? | same design center? | compatible P06 method? | selected independent of outcome? | formal design row? | disposition |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Allowed dispositions:

- `FORMAL-CENTER-REUSED`
- `PILOT-NONREUSABLE`
- `ARCHIVE`
- `FAILURE-BOUNDARY`

---

# 5. Root-growth material register

One row per independent LPE root.

| Root ID | F2 design row | growth/source genealogy | physical outline | usable outline/map ID | orientation | P06 complete? | fit/holdout | current material state |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

No descendant cut from one root may later be relabeled an independent LPE root.

---

# 6. Parent usable-area / layout register

For each root or large treated parent:

Parent ID: ____________________  
CAD/layout revision: ____________________  
Usable polygon/outline ID: ____________________  
Excluded morphology/edge regions: ____________________  
Crystal/growth orientation: ____________________

| Descendant role | planned ID | active footprint | street/kerf allowance | functional edge exclusion | handling/fixture margin | orientation constraint | expanded footprint fits? |
|---|---|---|---|---|---|---|---|
| MATERIAL-CONTROL |  |  |  |  |  |  |  |
| ANNEAL-TREATMENT |  |  |  |  |  |  |  |
| RIE-STATE-WITNESS |  |  |  |  |  |  |  |
| TLM-CONTACT-WITNESS |  |  |  |  |  |  |  |
| DETECTOR-BRIDGE |  |  |  |  |  |  |  |
| PACKAGE-BUILD |  |  |  |  |  |  |  |
| ARCHIVE |  |  |  |  |  |  |  |
| DESTRUCTIVE-FA |  |  |  |  |  |  |  |

Packing/CAD result: PASS / HOLD / FAIL  
Unused reserve geometry: ____________________

---

# 7. Measurement/process compatibility decisions

## P06

Intact-parent P06 performed before split where feasible: YES / NO  
Exception/reason: ____________________

## P05

Selected genealogy branch:

- [ ] dedicated P05 material-control sibling — conservative default
- [ ] same-specimen Hall -> anneal reuse locally qualified
- [ ] same-specimen Hall -> detector reuse locally qualified
- [ ] other qualified route

Hall contact product/process: ____________________  
Compatibility evidence ID: ____________________  
Surface/contact removal if applicable: ____________________  
Disposition: ____________________

## P10-P13

Same completed detector intended to support matched P10/P11/P12/P13 state: YES / NO  
Low-injection/heating/reversibility evidence: ____________________  
Measurement order: ____________________

---

# 8. F2 descendant-selection register

Do not fabricate full detector descendants from every F2 root by default.

| Root ID | material-only? | P05 branch | anneal branch | detector bridge | archive | destructive witness | reason / information value |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

P06->P11 bridge-selected roots: ____________________

---

# 9. F3 anneal-treatment register

## Experimental-unit definition

Anneal independent unit is: ____________________  
One ampoule/run contains how many specimens?: __________  
Are co-loaded specimens treated as within-run replicates? YES / NO  
If NO, justification: ____________________

| Anneal run/history ID | root/block IDs | coupon IDs | boundary / n-like / holdout / control | T_s/T_Hg trace ID | pre-state branch | post-anneal P05 descendant | detector descendant | independent history? |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Boundary histories `N_B`: __________  
N-like fit histories `N_J`: __________  
Held-out histories `N_H`: __________  
Controls `N_C`: __________  
Destructive histories `N_X`: __________

`N_treat,F3 = N_B+N_J+N_H+N_C+N_X = __________`.

For a four-factor first-order n-like axial fit, structural fitted count `2k_A+3 = 11`; boundary/holdout/power terms remain separate.

---

# 10. F4 RIE chamber-treatment bundle register

Number of independently controlled RIE factors `k_R`: __________  
Jacobian-first fitted chamber-treatment count `2k_R+3`: __________  
Additional holdout chamber treatments: __________  
Nonreusable Stage-0 chamber treatments: __________  
Stability treatments: __________

| Chamber run ID | design state | root/material block | oxide/recession witness | Hall witness | LBIC/depth witness | TLM witness | detector descendant | chamber position map | independent treatment? |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

Reminder: multiple co-loaded structures do not increase independent treatment count.

Detector-bearing RIE states selected for full downstream fabrication: ____________________

Selection rationale / decision-information value: ____________________

---

# 11. Passivation/surface-state descendant register

Frozen incoming RIE/material state(s): ____________________

| Upstream RIE state | sibling descendant IDs | passivation treatment | mesa->oxide handoff | oxide->Mask2 handoff | detector response descendant | independent surface treatment? |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

RIE x passivation interaction intentionally included?: YES / NO  
If YES, model/design ID: ____________________

---

# 12. F1 / P10-P13 shared detector register

| Detector ID | root | anneal | RIE | passivation | metal | pre-package state | P10 | P11 | P12 | P13 | F1 field derivative | still eligible for package? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |

Incremental detectors required solely for F1: __________  
Default target: zero when existing qualified descendants suffice.

---

# 13. F5 package-build die allocation

Non-HgCdTe surrogate screen complete: YES / NO  
Selected construction family: ____________________

| Package build ID | detector die ID | root/process genealogy | pre-package baseline complete? | package condition/level | post-package P10/P12/P13 | P11 if applicable | independent build? | terminal disposition |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

Independent actual HgCdTe package builds: __________  
HgCdTe dies consumed by F5: __________

Unless qualified reversible rework exists, these numbers are one-for-one.

---

# 14. Holdout register

| Holdout ID | campaign | root | treatment event | why independent? | model frozen before result? | measurement vector | terminal state |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Checks:

- F2 LPE holdout = independent new growth: YES / NO
- F3 holdout independence appropriate to anneal unit: YES / NO
- F4 holdout = independent new chamber treatment: YES / NO
- F5 holdout = independent package assembly: YES / NO

---

# 15. Archive / destructive / contingency register

| Piece ID | root | role | archive / destructive / reserve | reserved decision | destructive method if any | may be reassigned? | terminal disposition |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

No destructive analysis may consume the sole remaining detector bridge/holdout descendant without documented deviation review.

---

# 16. Reserve terms

Do not collapse into one guessed reserve percentage.

| Reserve term | required count/area | empirical basis | confidence target | state |
|---|---:|---|---|---|
| `R_PROCESS` |  |  |  | OPEN |
| `R_METROLOGY` |  |  |  | OPEN |
| `R_LAYOUT` |  |  |  | OPEN |
| `R_HOLDOUT` |  |  |  |  |
| `R_FA` |  |  |  |  |
| `R_POWER` |  |  |  | OPEN |

When a success probability `p` becomes available, attach the binomial/genealogy-aware sizing calculation rather than using an arbitrary multiplier.

---

# 17. Treatment-root confounding audit

| Treatment/campaign | root/block distribution | wafer-position balance | run-order/time alias | source/chamber/ampoule alias | estimable treatment contrast? | action |
|---|---|---|---|---|---|---|
| F3 anneal |  |  |  |  |  |  |
| F4 RIE |  |  |  |  |  |  |
| passivation |  |  |  |  |  |  |
| F5 package |  |  |  |  |  |  |

Reject a plan where treatment is perfectly aliased with root growth or another uncontrolled block.

---

# 18. Material balance

## Independent roots

Available/identified roots: __________  
Required structural roots: __________  
Physically layout-feasible roots: __________  
Uncommitted roots: __________

## Physical descendants

| State | count | total usable area/footprint if known |
|---|---:|---:|
| unsplit parent |  |  |
| material-control |  |  |
| anneal-treatment |  |  |
| RIE witnesses |  |  |
| TLM/LBIC |  |  |
| completed detector |  |  |
| package build |  |  |
| archive |  |  |
| destructive/terminal |  |  |
| uncommitted reserve |  |  |

Physical area sufficiency demonstrated: YES / NO  
Power/yield reserve demonstrated: YES / NO

---

# 19. Anti-pseudoreplication review

- P06 map points counted only as within-growth observations: PASS / FAIL
- sibling coupons not counted as LPE replicates: PASS / FAIL
- co-loaded RIE witnesses not counted as separate chamber runs: PASS / FAIL
- repeated field points not counted as devices: PASS / FAIL
- repeated package cycles not counted as package builds: PASS / FAIL
- no treatment perfectly aliased with root: PASS / FAIL
- one physical run not duplicated as two independent design rows: PASS / FAIL

Reviewer comments: ____________________

---

# 20. P16G disposition

Selected F2 root design frozen: YES / NO  
Stage-0 reuse disposition complete: YES / NO  
All root usable outlines/layouts established: YES / NO  
P05 compatibility branch frozen: YES / NO  
F3 treatment-unit genealogy feasible: YES / NO  
F4 chamber bundle genealogy feasible: YES / NO  
P10-P13/F1 shared detector plan feasible: YES / NO  
F5 die allocation feasible: YES / NO  
Holdouts protected: YES / NO  
Destructive witnesses protected: YES / NO  
Confounding audit passed: YES / NO  
Structural material balance closes: YES / NO  
Yield/power reserve status explicitly open or justified: YES / NO  
EH&S/infrastructure available: YES / NO

Final state:

`P16G-MATERIAL-GENEALOGY-PLAN-READY = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** P16G readiness means the structural material genealogy is feasible. It does not prove P16F empirical campaign readiness, P16E allocation closure, P16A first-build readiness, or P17 release.
