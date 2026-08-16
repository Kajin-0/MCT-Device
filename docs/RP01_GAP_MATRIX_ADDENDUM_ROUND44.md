# RP-01 gap matrix addendum — Round 44 empirical-Jacobian / information-optimal DOE architecture

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Purpose

Update the controlled gap state after introducing a unified information-optimal empirical-Jacobian program.

Round 44 closes **how the missing Jacobians should be learned**, but does not close any Jacobian numerically because no local physical data exist.

---

# G44-01 — canonical field derivatives

Required:

- `s_R,E = partial ln R_v / partial ln E`;
- `s_n,E = partial ln e_n / partial ln E`;
- `s_D,E = s_R,E - s_n,E` near 80 K / 10 V/cm.

Prior state:

`EMPIRICAL-JACOBIAN-REQUIRED`.

Round-44 state:

`DESIGN-IDENTIFIED / PHYSICAL-RANGE-OPEN`.

Closed analytically:

- use multiplicatively symmetric field perturbation;
- retain repeated-measures covariance;
- counterbalance order;
- measure self-heating/hysteresis;
- hold out an interior field point.

Still open:

- perturbation half-range `h`;
- device-to-device slope variance;
- actual slope values;
- curvature/sweepout boundary at the selected local device state.

Blocking impact:

- prevents final Round-43 gap/field D* uncertainty allocation.

---

# G44-02 — LPE local Jacobian

Required mapping:

`{xL,yL,TL,DeltaT_SC,t_contact,inventory,source-use,Hg-loss}`

`-> {x_opt,d,uniformity,morphology}`

and matched P06/P11 detector bridge.

Prior:

P21/P22 architecture defined; local apparatus/variance/factor ranges absent.

Round-44 state:

`DESIGN-IDENTIFIED / STAGE0-DATA-OPEN`.

New option:

- 9-growth three-factor Jacobian-first axial design when only first-order `{xL,yL,DeltaT_SC}` slopes are required and interaction/curvature assumptions pass.

Existing alternatives retained:

- 15-run BBD;
- 17-run FCCCD;
- 11-run two-factor Stage-2 quadratic;
- mixed/repeated Stage-3 source-use design.

Still open:

- independent center-growth variance;
- actual physical half-ranges;
- same-regime/morphology feasible region;
- local factor independence;
- empirical coefficients/covariance;
- holdout prediction;
- P06→P11 bridge.

Blocking impact:

- no detector-derived LPE mass/thermal/time tolerance can be released.

---

# G44-03 — Hg anneal state boundary

Required:

- classifier for P-LIKE / N-LIKE / TRANSITION-MULTICARRIER;
- boundary uncertainty;
- stable n-like local Jacobian;
- cooldown/initial-state dependence;
- detector bridge.

Round-44 state:

`DESIGN-IDENTIFIED / CLASSIFIER-DATA-OPEN`.

Closed analytically:

- boundary information is highest near uncertain class probability;
- continuous one-carrier derivatives must be estimated separately inside stable n-like state;
- matched pre-state/growth blocking required.

Still open:

- local boundary location;
- transition-zone width;
- candidate-center margin;
- n-like `n_H/mu_H` derivatives;
- cooldown interaction;
- detector-level performance derivative.

Blocking impact:

- no robust anneal process margin can be allocated.

---

# G44-04 — RIE physical-state Jacobian

Required mapping:

`{gas/pressure/sheath/thermal/exposure/chamber state}`

`-> {sheet transport,dconv,Lconv,rho_c,sweepout,R_v,e_n,tau,D*}`.

Round-44 state:

`DESIGN-IDENTIFIED / INDEPENDENT-FACTOR-SET-OPEN`.

Closed analytically:

- distinguish actuator from measured physical state;
- preserve `t_clear` versus `t_sem`;
- use independent RIE chamber execution as process unit;
- permit `2k+3` Jacobian-first structural design for `k` independently controllable factors plus three centers;
- add interactions sequentially from physics/residual evidence;
- optimize detector vector response rather than `rho_c` alone.

Still open:

- actual reactor factor independence;
- physical perturbation ranges;
- Stage-0 run variance;
- conversion-depth/sheath/thermal metrology;
- detector descendants;
- empirical state-to-performance Jacobian.

Blocking impact:

- RIE controller center remains a candidate historical starting point, not an optimized/released blocking-contact specification.

---

# G44-05 — passivation/sidewall Jacobian

Required mapping:

`{mesa/oxide/surface-state trajectory}`

`-> {1/f,R_v,tau,D*}`.

Round-44 state:

`DESIGN-IDENTIFIED / PHYSICAL-STATE-COORDINATES-OPEN`.

Closed architecture:

- freeze RIE center before passivation subcampaign where practical;
- use actual electrochemical/surface-state coordinates;
- do not treat dependent `I`, `J`, `A_exposed` as independent factors;
- control mesa→oxide and oxide→Mask2 handoffs.

Still open:

- local chemistry/electrochemical branch;
- quantitative oxide/interface state;
- variance;
- factor ranges;
- empirical noise/lifetime/responsivity derivatives.

---

# G44-06 — package thermal/dynamic Jacobian

Required mapping:

`{attachment/bondline/carrier/interconnect/vacuum state}`

`-> {R_theta,H_pkg,DeltaT,noise,P13 apparent response}`.

Round-44 state:

`DESIGN-IDENTIFIED / PACKAGE-BUILD-DATA-OPEN`.

Closed architecture:

- surrogate-screen construction families first;
- freeze a discrete construction family before continuous slope estimation;
- use measured bondline/coverage/void/tilt coordinates;
- independent package build is process unit;
- use paired detector pre/post data where possible;
- repeated pulses/cycles are not independent package builds.

Still open:

- actual package family/product;
- feasible bondline range;
- package-build variance;
- thermal/noise/dynamic derivatives;
- detector/package interaction.

Blocking impact:

- no final separation of intrinsic P13 detector pole from package thermal response.

---

# G44-07 — perturbation-size selection

Prior issue:

process factor ranges could be chosen by convention or historical spread.

Round-44 controlled rule:

For symmetric derivative estimation,

`SE(g)=sigma/[sqrt(2m)Delta u]`.

Planning effect criterion at alpha=.05 / power=.80:

`eta_min≈1.981/sqrt(m)`

with

`eta=|g|Delta u/sigma`.

State:

`ANALYTICAL-METHOD-CLOSED / LOCAL-SIGMA-OPEN`.

This closes the method but not any physical `Delta u` because `sigma` and same-regime bounds are local.

---

# G44-08 — information criterion

Prior default:

P22 D-optimal determinant increment.

Round-44 extension:

- c-optimal protected combination;
- weighted A/trace protected vector;
- final detector-decision variance reduction when downstream Jacobian exists.

State:

`ANALYTICAL-METHOD-CLOSED / REQUIREMENT-WEIGHTS-OPEN`.

A future campaign must declare the criterion and protected combination before adaptive run selection.

---

# G44-09 — experimental-unit/genealogy ambiguity

Round-44 closes the conceptual rule:

- detector = unit for repeated field sweep;
- growth = unit for LPE;
- anneal coupon/history = treatment unit, with growth/wafer blocks;
- chamber treatment = unit for RIE;
- package build = unit for package process.

State:

`ARCHITECTURE-CLOSED / PHYSICAL-GENEALOGY-OPEN`.

Actual IDs, blocks and descendant allocation remain local.

---

# G44-10 — empirical evidence promotion

New progression:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`.

State:

`CONTROLLED`.

No current empirical process derivative advances beyond `DESIGN-IDENTIFIED` because no local physical dataset exists.

---

# G44-11 — P16F campaign readiness

New integration state:

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`.

Current:

`NO / NOT PHYSICALLY INSTANTIATED`.

To become YES, active campaigns require:

- experimental unit defined;
- Stage-0 independent-unit variance;
- resolution-verified physical perturbations;
- rank/conditioning pass;
- genealogy/material plan;
- holdout;
- stopping rule;
- infrastructure/EH&S readiness.

P16F YES would not imply any derivative is `EMPIRICAL-VERIFIED`.

---

# Round-44 maturity disposition

Unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO`;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`;
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`;
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`;
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`;
- `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO / NOT PHYSICALLY INSTANTIATED`.

Round 44 materially closes **experimental design architecture**, not physical process state.