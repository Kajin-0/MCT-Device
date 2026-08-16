# RP-01 gap matrix addendum — round 15 information-optimal DOE planning

**Date:** 2026-08-16 America/New_York

Round 15 does not add a historical fabrication recipe. It closes the **experimental-design architecture** needed to estimate P21 Jacobians efficiently and records which quantities still prevent physical execution or tolerance release.

---

## G15-01 — Stage-1 coded design family

**State:** PARTIALLY CLOSED / DESIGN FAMILY IDENTIFIED

Closed analytically:

- full quadratic three-factor model has 10 coefficients;
- `2^3 + center` is rank deficient for individual quadratic terms;
- 17-run face-centered CCD is full rank and has stronger first-order/interaction precision;
- 15-run Box-Behnken + 3 centers is full rank, uses two fewer runs and avoids all-three-factor extreme corners.

Still OPEN:

- whether all FCCCD cube corners remain in the same physical/morphology regime;
- physical scaling for `Delta xL`, `Delta yL`, `DeltaT_SC`;
- Stage-0 independent-run sigma.

Closure path:

P21 Stage 0 + P22 physics review.

---

## G15-02 — Stage-2 coded kinetic design

**State:** CODED STRUCTURE CLOSED / PHYSICAL SCALING OPEN

Closed analytically:

- full quadratic two-factor model has 6 coefficients;
- `2^2 + center` is rank deficient;
- 11-run face-centered CCD + 3 centers is full rank with adequate algebraic conditioning.

OPEN:

- actual `DeltaT_SC` half-range;
- actual contact-time half-range;
- whether all corner/axis states remain inside the same growth regime;
- independent-run response variance.

---

## G15-03 — derivative-resolution / power planning

**State:** METHOD CLOSED / INPUT VARIANCE OPEN

Round-15 result:

For a coded linear coefficient,

`eta = |partial y/partial u| Delta u / sigma_y`.

One-block approximate 80%-power, alpha=.05 resolution scales:

- Stage-1 FCCCD linear `eta_min≈1.03`;
- Stage-1 BBD linear `eta_min≈1.24`;
- Stage-2 FCCCD linear `eta_min≈1.44`.

These are standardized planning scales, not process tolerances.

OPEN:

- actual response sigma by output;
- minimum scientifically important physical derivative;
- physical half-ranges.

---

## G15-04 — sequential next-growth selection

**State:** ANALYTICAL RULE CLOSED / CANDIDATE SET OPEN

For current information matrix `M` and candidate model row `x_c`, use

`q_c = w_c x_c^T M^-1 x_c`.

By the matrix determinant lemma, adding the candidate multiplies D-information determinant by `1+q_c`.

OPEN:

- physically admissible candidate set;
- response-dependent variance weights;
- P20 multiresponse information weights.

---

## G15-05 — Stage-3 source-use design

**State:** STRUCTURAL MODEL IDENTIFIED / SAMPLE SIZE OPEN

Closed conceptually:

- source-use is sequential and not freely randomized;
- source charge is the independent genealogy/whole-plot unit;
- liquid depth/inventory may be a hard-to-change whole-plot treatment;
- source-use is a within-charge repeated coordinate;
- Hg-loss proxy remains a separate covariate/state.

Structural floor for quadratic depth/use support:

- 3 depth levels;
- >=2 independent charges per depth;
- >=3 selected use states per charge;
- at least 6 independent source genealogies / 18 selected growth states.

This is not a power-based recommendation.

OPEN:

- physical depth levels;
- use-state spacing;
- charge-to-charge variance;
- within-charge correlation / random-effect structure;
- material/resource feasibility.

---

## G15-06 — center-run replication

**State:** ROLE CLOSED / COUNT LOCALLY QUALIFIED

Round-15 conclusion:

Center points improve pure-error, intercept and curvature support but do not substitute for off-center derivative information.

Three centers are a planning default, not a released requirement.

OPEN:

- required center count after observed center-run variance/drift;
- chronological placement under actual source genealogy constraints.

---

## G15-07 — morphology-constrained DOE

**State:** METHOD CLOSED / FEASIBLE SET OPEN

Candidate support points must be filtered through

`Omega_feasible`.

If a standard FCCCD/BBD point is excluded, the design must be re-optimized; simply deleting a point may destroy rank or precision.

OPEN:

- actual same-regime/morphology boundary around the candidate center.

---

## G15-08 — multiresponse information weighting

**State:** OPEN

One growth yields multiple outputs:

`{x_opt,d,edge,spatial metrics,morphology,...}`.

P20 must determine which response uncertainties dominate the final detector spectral requirement before a multiresponse information objective can be frozen.

Closure path:

P20 requirement allocation + Stage-0 response covariance.

---

## G15-09 — holdout confirmation allocation

**State:** STRUCTURE CLOSED / EXACT POINTS OPEN

P22 requires holdout combinations not used in model fitting.

At minimum plan:

- center confirmation;
- one interior combined perturbation;
- one feasible near-margin point where scientifically appropriate.

Exact states remain OPEN until coded ranges and morphology bounds are known.

---

## G15-10 — physical perturbation magnitudes

**State:** OPEN BY DESIGN

Round 15 intentionally does **not** assign:

- `Delta xL`;
- `Delta yL`;
- `DeltaT_SC` in C/K;
- contact-time seconds/minutes;
- melt-depth mm;
- source-use run indices;
- Hg-loss perturbation.

They are selected only after:

1. Stage-0 metrology/run variance;
2. minimum important derivative scale;
3. same-regime/morphology bounds;
4. apparatus resolution/control;
5. source genealogy feasibility.

---

## Round-15 conclusion

The P21 experimental problem is no longer under-specified at the **design-mathematics** level.

The remaining uncertainty is now properly localized to physical scaling, variance and feasibility rather than experimental-design structure.

Next analytical block after P22 should move to P04/P05/P13 anneal-trajectory sensitivity unless additional P21 synthetic optimization is needed for a specific apparatus candidate.
