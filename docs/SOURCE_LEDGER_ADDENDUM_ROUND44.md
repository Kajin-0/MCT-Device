# Source ledger addendum — Round 44 empirical-Jacobian / information-optimal DOE architecture

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Scope

Round 44 did not reopen saturated historical process searches. It used the controlled repository evidence and Round-43 uncertainty results to design the next empirical-information layer.

New controlled artifacts:

- `calculations/RP01_EMPIRICAL_JACOBIAN_INFORMATION_DESIGN.md`;
- `procedures/P22A_MULTI_SUBSYSTEM_INFORMATION_OPTIMAL_JACOBIAN_PROGRAM.md`;
- `travelers/P16F_EMPIRICAL_JACOBIAN_INFORMATION_REGISTER.md`.

No physical experiment was performed. No empirical coefficient was invented.

---

## S44-01 — Round-43 uncertainty/allocation basis

Controlled sources:

- `calculations/RP01_FIRST_BUILD_UNCERTAINTY_BUDGET.md`;
- `procedures/P20A_FIRST_BUILD_UNCERTAINTY_REQUIREMENTS_ALLOCATION_ADDENDUM.md`;
- `travelers/P16E_FIRST_BUILD_UNCERTAINTY_ALLOCATION_REGISTER.md`.

Round-44 use:

- identified the highest-value missing empirical derivatives;
- retained covariance/common-path rules;
- treated detector-decision uncertainty rather than process-coefficient count as the ultimate experiment objective.

Key inherited open terms:

- canonical `s_R,E`, `s_n,E`;
- LPE process -> material state;
- anneal trajectory -> transport/lifetime state;
- RIE/passivation -> blocking/noise/responsivity/dynamics;
- package construction -> thermal/dynamic/noise state.

**Class:** `CONTROLLED-ANALYTICAL-INPUT`.

---

## S44-02 — P21 LPE empirical-Jacobian architecture

Controlled source:

`procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`.

Retained principles:

- independent LPE growth is the process experimental unit;
- P06 map points are within-growth observations;
- factors include actual xL/yL, measured local supercooling, contact time, inventory/source-use and Hg-loss state;
- morphology defines a feasible region;
- P06-to-P11 bridge is required before detector spectral tolerances can be allocated;
- holdout confirmation is required for `EMPIRICAL-VERIFIED` status.

Round-44 addition:

- a 9-growth Jacobian-first axial option may be considered for the three-factor `{xL,yL,DeltaT_SC}` local slope problem when interactions/curvature are not required;
- this does not replace P22 BBD/FCCCD when interactions or curvature matter.

The 9-run count is a structural design result (`2k+3` for `k=3` plus three centers), not a power-based recommendation.

---

## S44-03 — P22 information-optimal DOE architecture

Controlled source:

`procedures/P22_INFORMATION_OPTIMAL_DOE_PLANNING.md`.

Retained:

- coded factor scaling from physical resolvability and same-regime limits;
- full-rank design requirement;
- D-information candidate score;
- 15-run BBD and 17-run FCCCD P21 Stage-1 candidates;
- 11-run two-factor face-centered P21 Stage-2 design;
- source-use mixed/repeated-measures structure;
- holdout and derivative-status promotion.

Round-44 additions derived from the same information-matrix framework:

- c-optimal criterion for one protected coefficient/linear combination;
- weighted A/trace criterion for a protected vector;
- expected detector-decision variance reduction as the preferred criterion when the downstream P20 Jacobian exists;
- general axial first-order design `n=2k+r`.

**Class:** `DERIVED-INFORMATION-DESIGN`.

---

## S44-04 — symmetric derivative-resolution derivation

For

`g_hat=[y(+)-y(-)]/(2 Delta u)`

with `m` independent plus/minus pairs and equal residual SD `sigma`, Round 44 derives:

`SE(g_hat)=sigma/[sqrt(2m) Delta u]`.

Define

`eta=|g|Delta u/sigma`.

Using the existing P22 planning convention of two-sided alpha=.05 and target power=.80 with a normal approximation:

`eta_min≈1.981/sqrt(m)`.

Values retained in the calculation:

- m=1 -> 1.981;
- m=2 -> 1.401;
- m=3 -> 1.144;
- m=4 -> 0.991.

These are DOE sizing scales only.

**Class:** `DERIVED-STATISTICAL-DESIGN-CHECK`.

---

## S44-05 — paired/correlated contrast derivation

Round 44 derives for a matched plus/minus pair:

`Var(g_hat)=[Var(y+)+Var(y-)-2Cov(y+,y-)]/(4 Delta u^2)`.

Use:

- canonical field sweeps on one detector;
- paired before/after package comparisons;
- matched material blocks where appropriate.

This formalizes why pairing must be retained rather than discarded in an iid analysis.

**Class:** `IDENTITY / DERIVED-COVARIANCE`.

---

## S44-06 — canonical electric-field derivative design

Controlled process/metrology sources:

- P10 DC bias/self-heating;
- P11 responsivity;
- P12 noise/D*;
- Round-43 gap/field covariance result.

Round-44 controlled normalized coordinate:

`z_E=ln(E/E0)` with canonical `E0=10 V/cm`.

For multiplicatively symmetric field points:

`E-=E0 exp(-h)`

`E+=E0 exp(+h)`

estimate

`s_y,E≈[ln y(E+)-ln y(E-)]/(2h)`.

Required outputs:

- `s_R,E`;
- `s_n,E`;
- `s_D,E=s_R,E-s_n,E`;
- thermal/hysteresis diagnostics.

No numerical `h` is assigned because it depends on local measurement precision and same-regime/sweepout/heating limits.

**Class:** `CONTROLLED-DESIGN / PHYSICAL-RANGE-OPEN`.

---

## S44-07 — P23 anneal state-boundary information

Controlled source:

`procedures/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_QUALIFICATION.md`.

Retained:

- carrier sign transition is a classification/state boundary;
- transition/multicarrier region must not be forced into one-carrier regression;
- local continuous Jacobian is fitted only inside stable n-like state;
- complete initial material state and cooldown trajectory are controlled.

Round-44 mathematical addition:

for a logistic-style classifier, Bernoulli Fisher information for the linear predictor is proportional to

`p(1-p)`,

which is maximized at `p=.5`.

Therefore boundary-localization coupons have highest classification information near the uncertain transition, subject to P23 optical/morphology feasibility.

This does not mean those same points are suitable for continuous `n_H/mu_H` derivatives.

**Class:** `DERIVED-CLASSIFIER-INFORMATION`.

---

## S44-08 — P24/P25 blocking-contact/passivation integration

Controlled sources:

- P24 blocking-contact empirical window;
- P34 RIE reactor equivalence;
- P25/P25A anodization;
- P10/P11/P12/P13 detector measurements.

Retained empirical facts:

- direct RP-01 RIE center: total 64 sccm, 100 mTorr, 50 W, 60 s;
- same-lineage 1:5 candidate gas interpretation remains a candidate, not historical individual MFC evidence;
- converted transport/depth depends on reactor state;
- physical etch depth is not electrical conversion depth;
- pressure/temperature/energy state matter;
- `rho_c` is not minority blocking strength.

Round-44 design decision:

- first freeze the P25/passivation/downstream process while mapping RIE;
- regress against measured physical state (self-bias/sheath, temperature, `t_clear`, `t_sem`, converted sheet/depth), not only controller setpoints;
- use a `2k+3` Jacobian-first structural option when `k` independently controlled factors exist, followed by targeted interaction augmentation;
- map passivation/surface state as a separate sequential subcampaign rather than exploding one giant factorial.

No numerical RIE perturbation ranges are released.

---

## S44-09 — P33 package integration

Controlled source:

`procedures/P33_CRYOGENIC_DIE_ATTACH_INTERCONNECT_EMPIRICAL_PROCESS_WINDOW.md`.

Retained:

- package thermal poles can be several ms and hundreds of ms in primary HgCdTe photoconductor evidence;
- compliant attachment reduces cryogenic fracture risk in Honeywell evidence;
- bondline thickness/coverage/voiding and carrier construction are first-class thermal variables;
- pre/post detector measurements are required to isolate package-induced effects.

Round-44 design decision:

- surrogate-screen discrete package families first;
- freeze one family before estimating continuous Jacobians;
- use measured bondline/void/tilt state;
- treat independent package build as process unit;
- repeated pulses/cycles on one package are repeated measures, not independent package replicates;
- use paired pre/post detector response when possible.

---

## S44-10 — evidence promotion architecture

New controlled progression:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`.

This extends P21/P22/P23 terminology across all empirical-Jacobian blocks.

A derivative is not P20/P16E allocation-eligible merely because it is statistically estimable.

---

## S44-11 — new P16F integration state

New register:

`travelers/P16F_EMPIRICAL_JACOBIAN_INFORMATION_REGISTER.md`.

New state:

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`.

Meaning:

- experimental units/factors/responses are defined;
- Stage-0 local variance exists;
- physical perturbation ranges are resolution-verified and same-regime;
- rank/conditioning pass;
- genealogy/material plan exists;
- holdouts/stopping criteria are frozen.

Current:

`NO / NOT PHYSICALLY INSTANTIATED`.

P16F is a campaign-readiness state, not empirical verification or project release.

---

## Round-44 source conclusion

No new literature number was required to make progress.

The dominant remaining uncertainty is now demonstrably **local empirical information** rather than documentary process-family identity.

Further generic searching does not substitute for:

- actual independent-run variance;
- actual factor actuation/metrology;
- local response surfaces;
- classifier boundaries;
- matched detector descendants;
- package-build data.
