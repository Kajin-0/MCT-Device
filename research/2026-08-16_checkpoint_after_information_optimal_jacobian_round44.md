# Research checkpoint — after empirical-Jacobian / information-optimal DOE architecture Round 44

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 44 began from the Round-43 conclusion that uncertainty propagation was now substantially defined, but the dominant remaining terms were empirical process-to-material/device Jacobians.

Objective:

> Design the smallest scientifically identifiable experimental campaigns that can close those Jacobians, using expected reduction in final detector-decision uncertainty rather than generic factorial completeness.

No physical experiment was performed. No empirical coefficient was fabricated. No vendor/tool was selected.

---

# 2. New controlled artifacts

Created:

- `calculations/RP01_EMPIRICAL_JACOBIAN_INFORMATION_DESIGN.md`;
- `procedures/P22A_MULTI_SUBSYSTEM_INFORMATION_OPTIMAL_JACOBIAN_PROGRAM.md`;
- `travelers/P16F_EMPIRICAL_JACOBIAN_INFORMATION_REGISTER.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND44.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND44.md`;
- this checkpoint.

AGENTS is refreshed at the end of the round.

---

# 3. New integration concept — P16F

P16A–P16F now separate six questions:

1. **P16A:** is one complete build executable without undocumented irreversible choices?
2. **P16B:** which evidence-ranked candidate process branch should be pursued?
3. **P16C:** does a real laboratory possess the required physical capability?
4. **P16D:** has that infrastructure passed controlled IQ/OQ/surrogate commissioning?
5. **P16E:** are measurement/control uncertainties and requirements adequately allocated?
6. **P16F:** are the missing empirical-Jacobian campaigns themselves physically ready, identifiable and information-justified?

New state:

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`.

Current:

`NO / NOT PHYSICALLY INSTANTIATED`.

P16F readiness is not empirical verification and is not P17 release.

---

# 4. New empirical evidence progression

Round 44 generalizes the P21/P22/P23 empirical states across all missing Jacobian blocks:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`.

Current process-to-device blocks reach at most `DESIGN-IDENTIFIED` because no local data exist.

---

# 5. Major result 1 — perturbation size derives from information, not convention

For a symmetric local derivative

`g_hat=[y(+)-y(-)]/(2 Delta u)`

with residual independent-unit SD `sigma` and `m` independent plus/minus pairs:

`SE(g_hat)=sigma/[sqrt(2m) Delta u]`.

Define

`eta=|g|Delta u/sigma`.

Using the existing P22 planning convention alpha=.05 and target power=.80 with normal approximation:

`eta_min≈1.981/sqrt(m)`.

Therefore:

- one pair needs a protected half-range response about 1.98 residual SD;
- two pairs ~1.40 SD;
- three pairs ~1.14 SD;
- four pairs ~0.99 SD.

This does not define a physical factor range. The range must also remain inside the same process regime.

Permanent rule:

`information lower bound <= Delta u <= physics/same-regime upper bound`.

If no overlap exists, improve metrology/stability or change the experiment.

---

# 6. Major result 2 — paired covariance is useful information

For matched plus/minus states:

`Var(g_hat)=[Var(y+)+Var(y-)-2Cov(y+,y-)]/(4 Delta u^2)`.

This formalizes the value of:

- repeated field sweeps on the same detector;
- neighboring matched anneal coupons;
- paired detector pre/post package measurements.

Do not destroy this advantage by reducing paired data as iid observations.

---

# 7. Major result 3 — D-optimality is not always the scientifically optimal target

P22 already uses D-information to estimate a broad coefficient set.

Round 44 adds:

### c-optimality

For protected combination

`theta=c^T beta`,

minimize

`c^T M^-1 c`.

Use when P16E cares primarily about one detector-relevant derivative/direction.

### weighted A/trace

Use for a protected vector of several quantities.

### decision-variance reduction

When a downstream P20 Jacobian exists, prefer the run expected to reduce final detector-decision variance most.

This is potentially more efficient than maximizing information about coefficients that do not affect the final detector requirement materially.

---

# 8. Campaign F1 — canonical field derivatives

Round 43 requires

`s_R,E = partial ln R_v/partial ln E`

and

`s_n,E = partial ln e_n/partial ln E`.

Round 44 defines multiplicatively symmetric field support around

`E0=10 V/cm`:

`E-=E0 exp(-h)`

`E+=E0 exp(+h)`.

Then

`s_y,E≈[ln y(E+)-ln y(E-)]/(2h)`.

A counterbalanced center/minus/center/plus/center structure is used to expose drift/hysteresis.

No numerical `h` is released before actual P10/P11/P12 precision, heating and sweepout reversibility are known.

This campaign is analytically highest value because it can close a direct Round-43 gap with no new upstream fabrication once qualified detectors exist.

---

# 9. Campaign F2 — LPE information design

P21/P22 remain authoritative.

Round 44 adds a lower-run Jacobian-first option when the current objective is strictly first-order local slopes.

For `{xL,yL,DeltaT_SC}`:

- six axial off-center growths;
- three distributed centers;
- total `n=9` independent growths.

This option cannot identify interactions or quadratic curvature.

If those are required, use existing P22:

- BBD `n=15`;
- FCCCD `n=17`;
- Stage-2 2-factor quadratic `n=11`.

The correct design is selected from detector-relevant information need, morphology feasibility and expected variance—not lowest run count alone.

---

# 10. Campaign F3 — anneal boundary information

P23's carrier-sign transition is a classification problem.

For logistic-style classifier probability `p`, Bernoulli information scales as

`p(1-p)`

and is maximum at `p=.5`.

Therefore new boundary-localization coupons should challenge uncertain feasible boundary states rather than repeat already certain p-like/n-like states.

Important separation:

- boundary points identify the classifier;
- safe n-like points identify continuous `n_H/mu_H` derivatives.

Do not use transition/multicarrier data in a one-carrier slope fit.

---

# 11. Campaign F4 — blocking-contact/passivation vector response

The design now explicitly separates:

`actuator settings -> measured plasma/surface state -> detector response`.

RIE measured physical coordinates include:

- flow/pressure;
- self-bias/sheath proxy;
- reflected power;
- sample thermal state;
- oxide clear `t_clear`;
- semiconductor exposure `t_sem`;
- converted sheet/depth/lateral state.

A generic Jacobian-first design for `k` independently controllable factors plus three centers has

`n=2k+3`.

For four independent factors the structural size is 11 chamber treatments.

This is not a final sample-size recommendation.

Interactions are augmented sequentially.

P25/passivation is then mapped as a separate surface-state block rather than creating one giant RIE×oxide factorial.

Final multiresponse target includes:

- sweepout;
- `R_v`;
- `e_n`;
- `tau/f3dB`;
- `D*`;
- contact metrics.

`rho_c` alone remains insufficient.

---

# 12. Campaign F5 — package thermal/dynamic response

Round 44 formalizes:

1. non-HgCdTe surrogate screen for package-family feasibility;
2. freeze one discrete construction family;
3. estimate continuous package-state effects from measured bondline/coverage/void/tilt;
4. use independent package build as experimental unit;
5. use paired pre/post detector measurements where possible;
6. separate repeated pulse/cycle data from independent package-build variance.

If bondline thickness curvature is to be fitted, at least three distinct qualified thickness levels are structurally required. Actual replicate count remains power/variance dependent.

---

# 13. Experimental-unit hierarchy now frozen

For initial empirical campaigns:

- field sweep -> completed detector is independent device unit; field points are repeated measures;
- LPE -> independent growth;
- anneal -> independently treated coupon/history with growth/wafer blocking;
- RIE -> independent chamber treatment;
- package -> independent package build.

This prevents pseudoreplication across the entire remaining development program.

---

# 14. Cross-campaign descendant rule

Scarce HgCdTe should be planned as a genealogy tree.

Selected upstream states should reserve descendants for matched:

- P05;
- P06;
- P10;
- P11;
- P12;
- P13.

This is more informative than generating unrelated datasets at every stage because covariance and material state remain traceable.

---

# 15. Sequential stopping rule

A stage stops when:

- its uncertainty is small enough that it cannot materially change the protected detector decision;
- local model/interaction checks pass;
- holdout prediction passes;
- further runs have low expected decision-value relative to material cost.

A stage must be redesigned if:

- perturbation leaves the intended regime;
- effect is unresolvable over feasible range;
- design becomes rank deficient/confounded;
- actual physical state cannot be measured;
- genealogy aliases treatment with source/run/time.

---

# 16. What Round 44 closes

Round 44 closes:

- how to choose local perturbation size after Stage-0 variance;
- how to use paired covariance;
- how to select D/c/A/decision-focused information criteria;
- experimental units for the five high-value campaigns;
- Jacobian-first low-run structural options;
- anneal boundary active-learning principle;
- RIE/passivation sequential design architecture;
- package surrogate→actual staged design;
- empirical evidence-promotion ladder;
- P16F campaign-readiness register.

---

# 17. What remains open

Still physically open:

- actual Stage-0 variances;
- actual feasible perturbation ranges;
- real design matrices after tool constraints;
- all empirical derivative values;
- all classifier boundaries;
- all holdout results;
- detector descendants;
- empirical P20/P16E allocations;
- P17 capability/yield.

---

# 18. Project maturity after Round 44

Unchanged:

`TRACEABLE-FIRST-BUILD-READY = NO`

`HISTORICAL-RP01-REPRODUCED = NO`

`REPRODUCIBLE-RELEASE = NO`

`P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`

`P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`

`P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO / NOT PHYSICALLY INSTANTIATED`

Strategic state:

**branch-selected + capability-specified + acceptance-specified + uncertainty-allocated analytically + information-optimal empirical campaigns designed + not physically instantiated**.

---

# 19. Strongest next analytical work — Round 45

The next bottleneck is no longer “what experiment should be run?” at a high level.

The highest-value analytical work is to build a **first-build descendant/genealogy and material-allocation plan** that determines how many wafers/coupons/devices each empirical campaign would consume, which measurements can share descendants, which steps are destructive, and how to preserve independent experimental units while minimizing HgCdTe consumption.

Round 45 should therefore construct:

- sample genealogy graph;
- coupon/device split strategy;
- destructive/non-destructive measurement map;
- minimum structural sample inventory under the candidate DOE branches;
- shared-descendant plan across P05/P06/P10–P13;
- contingency reserve for failures/holdouts;
- explicit distinction between structural minimum and power-based final sample size.

Do not invent material availability or yield.