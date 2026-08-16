# P16F — empirical-Jacobian / information-optimal campaign register

**Status:** CONTROLLED PRE-EXPERIMENT REGISTER / ROUND 44  
**Date:** 2026-08-16 America/New_York  
**Use with:** P20/P20A, P21, P22/P22A, P23, P24, P25, P33, P16E.

## 1. Purpose

Provide the future laboratory fill-in record for converting `EMPIRICAL-JACOBIAN-REQUIRED` gaps into identifiable, information-efficient experimental campaigns.

This register is not a fabrication traveler and does not authorize HgCdTe processing by itself.

Program state:

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = YES / NO`.

Current repository state: `NO / NOT PHYSICALLY INSTANTIATED`.

---

# 2. Program header

Laboratory/facility: ____________________  
Responsible engineer/statistician: ____________________  
P16F revision: ____________________  
P16E revision: ____________________  
P22A revision: ____________________  
Date opened: ____________________  
Protected detector requirement(s): ____________________

---

# 3. Universal campaign-design record

Complete one block for every campaign F1–F5.

## Requirement / decision

P19/P16E requirement ID: ____________________  
Protected metric: ____________________  
Operating condition: ____________________  
Numerical decision limit/uncertainty target: ____________________  
Current dominant uncertainty contribution: ____________________

## Experimental unit

Independent treatment unit: ____________________  
Within-unit repeated/spatial observations: ____________________  
Blocking/genealogy variable: ____________________  
Hard-to-change/sequential variable: ____________________

## Stage-0 variance

| Response | Measurement repeatability | within-unit variation | independent-unit SD | drift term | dataset ID |
|---|---:|---:|---:|---:|---|
|  |  |  |  |  |  |

## Model / design

Model formula: ____________________  
Independent units `n`: __________  
Coefficients `p`: __________  
Rank: __________  
Residual df: __________  
Conditioning diagnostic: __________  
Information criterion: D / c / A / classifier / decision variance / other: __________  
Protected coefficient/combination `c`: ____________________

## Perturbation-resolution check

For each factor:

| Factor | center | half-range | metrology uncertainty | expected protected contrast | `eta=|g|Delta/sigma` | required `eta_min` | same-regime? | status |
|---|---:|---:|---:|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |  |  |

## Holdout / stopping

Holdout state(s): ____________________  
Model discrepancy check: ____________________  
Stopping criterion: ____________________  
Failure/invalidation rule: ____________________

---

# 4. F1 — canonical field-derivative campaign

### Requirement link

Round-43 need:

- `s_R,E`;
- `s_n,E`;
- `s_D,E=s_R,E-s_n,E`;
- gap/field covariance in D*.

Detector IDs: ____________________  
Contact pair/gap: ____________________  
Package state: ____________________

`E0 = 10 V/cm` canonical comparison.

Selected multiplicative half-range `h`: ____________________  
`E_- = E0 exp(-h)`: ____________________  
`E_+ = E0 exp(+h)`: ____________________

### Resolution inputs

P11 `ln R_v` repeatability: ____________________  
P12 `ln e_n` repeatability: ____________________  
P10 field uncertainty: ____________________  
Temperature/self-heating repeatability: ____________________

### Sequence

Counterbalanced order: ____________________  
Center repeats: ____________________  
Bias polarity: ____________________  
Optical/background state: ____________________

### Results

`s_R,E`: ____________________ ± ____________________  
`s_n,E`: ____________________ ± ____________________  
`s_D,E`: ____________________ ± ____________________  
Device-to-device slope variance: ____________________  
Curvature test: PASS / HOLD / FAIL  
Heating/hysteresis test: PASS / HOLD / FAIL  
Interior holdout prediction: PASS / HOLD / FAIL

Evidence state: ____________________

---

# 5. F2 — P21 LPE campaign

Boat/source/process block ID: ____________________  
Growth is the independent unit: CONFIRMED / NO

### Immediate design objective

- [ ] Jacobian-only
- [ ] first-order + interactions
- [ ] local quadratic
- [ ] source-use mixed/repeated measures

### Stage-0

Independent center growths: ____________________  
P06 repeatability: ____________________  
Independent-growth variance: ____________________  
`TL_actual` uncertainty: ____________________  
Morphology feasible region defined: YES / NO

### Factor block

| Factor/state | center | half-range | independently controllable? | measured-state method | same-regime evidence |
|---|---:|---:|---|---|---|
| `xL` |  |  |  |  |  |
| `yL` |  |  |  |  |  |
| `DeltaT_SC` |  |  |  |  |  |
| `t_contact` |  |  |  |  |  |
| inventory/depth |  |  |  |  |  |
| source-use |  |  | sequential |  |  |

### Design selection

- [ ] 9-run Jacobian-first axial option (`xL,yL,DeltaT_SC` + 3 centers)
- [ ] 15-run BBD candidate
- [ ] 17-run FCCCD candidate
- [ ] P22 Stage-2 11-run 2-factor quadratic candidate
- [ ] constrained/sequential custom design

Exact run matrix ID: ____________________  
Rank/conditioning: ____________________  
Information criterion: ____________________

### Responses

P06 x/thickness/uniformity: ____________________  
Morphology/yield: ____________________  
P05 selected descendants: ____________________  
P11 detector descendants: ____________________

P06→P11 bridge state: ____________________

Holdout: ____________________  
Evidence state: ____________________

---

# 6. F3 — P23 anneal boundary / n-like Jacobian

Growth/wafer blocks: ____________________  
Coupon matching strategy: ____________________  
Complete pre-state available: YES / NO

### Boundary factors/state descriptors

| Descriptor | center/range | metrology | independently identifiable? | notes |
|---|---|---|---|---|
| sample dwell T |  |  |  |  |
| dwell time |  |  |  |  |
| Hg-source / chemical-potential proxy |  |  |  |  |
| cooldown descriptor |  |  |  |  |
| initial state | measured covariate |  |  |  |

Initial classifier design ID: ____________________  
Classifier model: ____________________  
Transition/multicarrier definition: ____________________

### Active boundary selection

Candidate list/version: ____________________  
Boundary-information score: ____________________  
Feasible-region exclusions: ____________________  
Selected next coupon/state: ____________________

### Boundary result

Candidate-center signed margin: ____________________  
Boundary-normal uncertainty: ____________________  
Transition-zone width: ____________________  
Sufficient for state/yield decision? YES / NO

### N-like local response

`d log10(n_H)/d factors`: ____________________  
`d mu_H/d factors`: ____________________  
Optical-preservation Jacobian: ____________________  
P13/P11/P12 detector bridge: ____________________

Holdout: ____________________  
Evidence state: ____________________

---

# 7. F4 — blocking-contact / passivation campaign

Incoming material block: ____________________  
P25 passivation baseline revision: ____________________  
Mask-2 revision: ____________________  
Cr/Au revision: ____________________  
Detector/package/test state: ____________________

### RIE actuators and measured state

| Coordinate | actuator or measured state? | center | half-range | metrology | independent? |
|---|---|---:|---:|---|---|
| CH4 flow |  |  |  |  |  |
| H2 flow |  |  |  |  |  |
| pressure |  |  |  |  |  |
| forward RF power |  |  |  |  |  |
| reflected RF | measured |  |  |  |  |
| self-bias/sheath proxy | measured |  |  |  |  |
| sample T |  |  |  |  |  |
| total plasma time |  |  |  |  |  |
| `t_clear` | measured |  |  |  |  |
| `t_sem` | derived/measured |  |  |  |  |
| chamber genealogy | block/covariate |  |  |  |  |

Number of independently controlled RIE factors `k`: __________  
Jacobian-first structural size `2k+3`: __________  
Actual selected design: ____________________  
Rank/conditioning: ____________________

### RIE state responses

- physical etch depth: ____________________
- converted sheet state: ____________________
- `d_conv`: ____________________
- `L_conv`: ____________________
- `rho_c`: ____________________
- LBIC/junction signature: ____________________

### Detector vector responses

- sweepout `R_v(E)`: ____________________
- `e_n(f,E)`: ____________________
- `tau_eff/f3dB`: ____________________
- `D*`: ____________________

### Interaction augmentation

Residual/physics-motivated interactions: ____________________  
Additional combined states: ____________________

### Passivation subcampaign

Independent surface-state coordinates: ____________________  
Mesa→oxide handoff control: ____________________  
Oxide→Mask2 handoff control: ____________________  
1/f/lifetime/responsivity responses: ____________________

Matched detector holdout: ____________________  
Evidence state: ____________________

---

# 8. F5 — package thermal/dynamic campaign

Surrogate-screen revision: ____________________  
Selected carrier family: ____________________  
Selected adhesive family: ____________________  
Selected interconnect family: ____________________  
Window/shield/vacuum revision: ____________________

### Continuous measured coordinates

| Coordinate | levels/range | measurement method | build-to-build SD | status |
|---|---|---|---:|---|
| bondline thickness |  |  |  |  |
| coverage/void fraction |  |  |  |  |
| die tilt |  |  |  |  |
| other |  |  |  |  |

Independent package builds: ____________________  
Repeated pulses/cycles per build: ____________________

### Paired pre-package baseline

P10: ____________________  
P12: ____________________  
P13: ____________________  
Other: ____________________

### Package responses

`R_theta,eff`: ____________________  
Thermal kernel/poles: ____________________  
Bias-induced `DeltaT`: ____________________  
Noise/microphonics shift: ____________________  
Raw vs de-embedded P13 response: ____________________  
Mechanical/interconnect survival: ____________________

Curvature tested?: YES / NO  
Holdout package: ____________________  
Evidence state: ____________________

---

# 9. Cross-campaign descendant allocation

| Upstream state ID | P05 | P06 | P10 | P11 | P12 | P13 | package state | genealogy complete? |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Do not combine detector metrics from unmatched descendants without an explicit correction model.

---

# 10. Next-run information log

| Campaign | candidate state | information criterion | expected decision-variance reduction | material/cost burden | confounding risk | feasible? | surrogate substitute? | selected? |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

---

# 11. Evidence promotion log

| Derivative/boundary | prior state | new state | local valid range | uncertainty | holdout ID/result | detector bridge | P20/P16E eligible? |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Allowed progression:

`EMPIRICAL-REQUIRED -> DESIGN-IDENTIFIED -> DESIGN-RESOLUTION-VERIFIED -> EMPIRICAL-PRELIMINARY -> EMPIRICAL-VERIFIED -> DETECTOR-BRIDGED -> ALLOCATION-ELIGIBLE`.

---

# 12. P16F disposition

All campaign experimental units defined: YES / NO  
Stage-0 variance available for active campaigns: YES / NO  
Physical perturbation ranges resolution-verified: YES / NO  
Model rank/conditioning passed: YES / NO  
Genealogy/material plan feasible: YES / NO  
Holdouts defined: YES / NO  
Stopping rules defined: YES / NO  
EH&S/infrastructure available: YES / NO

Final state:

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** P16F readiness does not imply empirical verification, P16E completion, P16A readiness or P17 release.