# RP-01 P21 coded DOE / Fisher-information design

**Status:** CONTROLLED DERIVED CALCULATION / PRE-EXPERIMENT DESIGN  
**Date:** 2026-08-16 America/New_York

## Purpose

Design the P21 LPE Jacobian-identification campaign in **coded coordinates** before any apparatus-specific perturbation magnitudes are selected.

This file determines:

- which candidate run structures are identifiable;
- which are rank deficient;
- relative Fisher-information content under a common coded model;
- coefficient/derivative standard-error multipliers;
- approximate standardized effect sizes resolvable at selected power;
- how sequential D-optimal growth selection can be performed after data begin to accumulate;
- why source-use/depletion requires a repeated-measures / whole-plot treatment rather than ordinary independent-run regression.

It does **not** assign real values for `Delta xL`, `Delta yL`, `DeltaT_SC`, contact time, melt depth, source-use limit, or Hg-loss perturbation.

---

# 1. Coded-factor definition

For a continuous process factor `u_i` with candidate center `u_i0` and selected half-range `Delta u_i`, define

`z_i = (u_i-u_i0)/Delta u_i`.

Thus the coded center is `z_i=0` and the nominal local design boundary is `z_i=+/-1`.

The physical half-range remains `OPEN` until P21 verifies that:

- the perturbation is resolvable above metrology/run noise;
- the complete interval remains in the same physical epitaxial-growth regime;
- morphology/yield remain feasible;
- apparatus control can realize the perturbation reproducibly.

For a local quadratic response model in coded variables,

`y = beta0 + sum beta_i z_i + sum beta_ij z_i z_j + sum beta_ii z_i^2 + error`.

At the coded center,

`partial y/partial u_i = beta_i/Delta u_i`.

Therefore

`SE(partial y/partial u_i) = SE(beta_i)/Delta u_i`.

This is the formal reason the design can be optimized before physical scaling is fixed.

---

# 2. Fisher-information framework

For homoscedastic independent run error with variance `sigma^2`,

`Cov(beta_hat) = sigma^2 (X^T X)^-1`.

The information matrix is proportional to

`M = X^T X / sigma^2`.

The following diagnostics are used in this file.

## Rank

A design is identifiable only when

`rank(X) = p`,

where `p` is the number of fitted coefficients.

## Condition number

`kappa(X^T X)` is used as a same-parameterization collinearity/conditioning diagnostic.

Do not compare condition numbers across differently scaled model columns without reparameterizing first.

## Generalized D-information index

For designs using the same coded model basis, define

`I_D = det[(X^T X)/n]^(1/p)`.

Higher is better for generalized coefficient-volume information under that fixed basis.

This is an internal comparison index, not a universal D-efficiency percentage.

## Coefficient standard-error multiplier

For coefficient `beta_j`, define

`c_j = sqrt([(X^T X)^-1]_jj)`

so

`SE(beta_j) = c_j sigma`.

These multipliers are especially useful because a center-to-edge standardized linear effect is

`eta_j = |beta_j|/sigma = |partial y/partial u_j| Delta u_j / sigma`.

---

# 3. Stage 1 model — source/phase block

P21 Stage 1 perturbs three coded factors:

- `z1`: actual `xL` coordinate;
- `z2`: actual `yL` coordinate;
- `z3`: corrected `DeltaT_SC` coordinate.

A full local quadratic model has 10 coefficients:

`{1,z1,z2,z3,z1z2,z1z3,z2z3,z1^2,z2^2,z3^2}`.

Thus `p=10`.

## 3.1 Rejected design: 2^3 factorial + center replication

Eight cube corners plus three center runs gives `n=11` but

`rank(X)=8 < 10`.

Reason: on every factorial corner, `z1^2=z2^2=z3^2=1`; at the center all three are zero. Center replication separates a common curvature direction from the intercept but cannot identify the three individual quadratic coefficients.

**Continuity rule:** center points do not de-alias individual quadratic terms in a two-level factorial.

## 3.2 Face-centered central composite design (FCCCD)

Support:

- 8 factorial corners `(+-1,+-1,+-1)`;
- 6 face-axis points `(+-1,0,0),(0,+-1,0),(0,0,+-1)`;
- 3 center replicates.

Total:

`n=17`, `p=10`, residual df `=7`.

Calculated design diagnostics:

- `rank=10`;
- `kappa(X^T X)=19.70`;
- `I_D=0.41297`;
- linear-coefficient SE multiplier `0.3162 sigma`;
- two-factor-interaction SE multiplier `0.3536 sigma`;
- quadratic-coefficient SE multiplier `0.6109 sigma`;
- intercept SE multiplier `0.4279 sigma`.

Interpretation:

- strong linear/Jacobian information;
- strong interaction information;
- weaker quadratic precision than the Box-Behnken candidate below;
- requires all eight simultaneous three-factor extremes, which may conflict with the P21 morphology feasible-region constraint.

## 3.3 Three-factor Box-Behnken design (BBD)

Support:

- 12 edge-midpoint points where two factors are at `+/-1` and the third is 0;
- 3 center replicates.

Total:

`n=15`, `p=10`, residual df `=5`.

Calculated diagnostics:

- `rank=10`;
- `kappa(X^T X)=17.97`;
- `I_D=0.36643`;
- linear-coefficient SE multiplier `0.3536 sigma`;
- two-factor-interaction SE multiplier `0.5000 sigma`;
- quadratic-coefficient SE multiplier `0.5204 sigma`;
- intercept SE multiplier `0.5774 sigma`.

Interpretation:

- two fewer runs than FCCCD;
- avoids all-three-factors-at-extreme corners;
- slightly better individual quadratic-coefficient precision in this coding;
- weaker linear and interaction precision;
- its `I_D` is about `0.36643/0.41297 = 0.887` of the FCCCD internal information index under the same model basis.

## 3.4 Stage-1 selection rule

Use **FCCCD** when:

- the primary objective is precise local Jacobian / first-order and interaction estimation;
- simultaneous corner perturbations are known to remain in the same growth/morphology regime.

Use **BBD** when:

- triple-extreme combinations are physically risky or likely to leave `Omega_feasible`;
- two fewer growths materially reduce cost;
- curvature information is important;
- modest loss of linear/interaction precision is acceptable.

If P21 excludes some BBD/FCCCD support points after morphology/physics screening, do not manually delete them and retain the same model. Re-optimize the design over the surviving candidate set using the sequential/constrained D-optimal rule in Section 8.

---

# 4. Stage 2 model — supercooling/contact-time kinetic block

Use two coded factors:

- `z1 = DeltaT_SC`;
- `z2 = t_contact`.

Full local quadratic model:

`{1,z1,z2,z1z2,z1^2,z2^2}`,

so `p=6`.

## 4.1 Rejected design: 2^2 factorial + center replication

Four corners plus three centers gives `n=7` but

`rank(X)=5 < 6`.

Again, the two individual quadratic terms remain aliased.

## 4.2 Face-centered CCD with three centers

Support:

- 4 corners `(+-1,+-1)`;
- 4 face-axis points `(+-1,0),(0,+-1)`;
- 3 centers.

Total:

`n=11`, `p=6`, residual df `=5`.

Calculated diagnostics:

- `rank=6`;
- `kappa(X^T X)=9.50`;
- `I_D=0.42835`;
- linear-coefficient SE multiplier `0.4082 sigma`;
- interaction SE multiplier `0.5000 sigma`;
- quadratic SE multiplier `0.6283 sigma`;
- intercept SE multiplier `0.5130 sigma`.

This is the default coded Stage-2 support if all nine unique locations of the `{-1,0,+1}^2` grid are feasible.

---

# 5. Why three center runs are a useful initial default

Center replication serves several functions:

- independent center-run variance estimate;
- pure-error/lack-of-fit separation when the design has repeated support;
- sensitivity to process drift at the nominal state;
- better intercept/quadratic separation.

It does **not** improve every coefficient equally.

For example, in the symmetric Stage-1 BBD, increasing centers from 1 to 7 leaves the linear and interaction SE multipliers unchanged at approximately `0.3536 sigma` and `0.5000 sigma`, while improving intercept/quadratic precision.

Thus center replication should not be used as a substitute for informative off-center growths when the goal is to estimate first derivatives.

Three center runs are an initial planning default, not a production requirement.

---

# 6. Standardized derivative-resolution planning

For a coefficient test under the local model,

`T = beta_hat_j / SE(beta_hat_j)`.

For planning, define

`eta_j = |beta_j|/sigma`.

For a coded linear term,

`eta = |partial y/partial u| Delta u / sigma`.

This is the response change from center to one coded edge measured in units of independent-run residual sigma.

A two-sided alpha=0.05, power=0.80 t-test requires a noncentrality that depends on residual degrees of freedom. Approximate required values for the designs below are:

- df=5: `lambda_req≈3.514`;
- df=7: `lambda_req≈3.270`.

Therefore a one-block Stage-1/2 campaign has the following approximate 80%-power standardized detectability limits.

| Design | residual df | linear `eta_min` | interaction `|beta_ij|/sigma` | quadratic `|beta_ii|/sigma` |
|---|---:|---:|---:|---:|
| Stage-1 BBD + 3 centers | 5 | 1.242 | 1.757 | 1.829 |
| Stage-1 FCCCD + 3 centers | 7 | 1.034 | 1.156 | 1.998 |
| Stage-2 FCCCD + 3 centers | 5 | 1.435 | 1.757 | 2.208 |

Interpretation example:

For the Stage-1 FCCCD, a linear derivative whose center-to-edge response is only `0.5 sigma` is unlikely to be resolved reliably in one 17-run block. A response around `1.0 sigma` across the half-range is near the one-block detection scale.

These values are planning calculations, not acceptance criteria.

## Replication effect

Replicating the complete design approximately scales coefficient SE as `1/sqrt(r)` while also increasing residual degrees of freedom.

Approximate 80%-power linear `eta_min` values are:

| Design | one block | two complete blocks | three complete blocks |
|---|---:|---:|---:|
| Stage-1 BBD | 1.242 | 0.736 | 0.588 |
| Stage-1 FCCCD | 1.034 | 0.653 | 0.524 |
| Stage-2 FCCCD | 1.435 | 0.862 | 0.685 |

This table gives a direct design rule:

**select the coded perturbation half-range so the scientifically important response is expected to exceed the resolvable standardized effect, rather than selecting tiny perturbations first and discovering afterward that the derivative is buried in run variance.**

Absolute half-ranges remain OPEN.

---

# 7. Converting standardized resolution to a physical derivative requirement

Suppose the process derivative of interest is

`g_i = partial y/partial u_i`

and the coded half-range is `Delta u_i`.

Then

`beta_i = g_i Delta u_i`.

For an intended minimum physically important derivative `g_min`, require approximately

`|g_min| Delta u_i / sigma_y >= eta_min`.

Thus

`Delta u_i >= eta_min sigma_y / |g_min|`.

This does **not** mean the range should simply be made large. P21 also imposes the upper constraints:

- remain within the same physical response regime;
- remain inside morphology/yield feasibility;
- avoid type/state transitions not represented by the model;
- maintain source/material traceability;
- remain within apparatus controllability.

The usable design range is therefore bounded from below by information resolution and from above by physics/model validity.

---

# 8. Sequential constrained D-optimal selection

After any set of valid independent growths, let the current information matrix be

`M = X^T W X`

with `W` containing inverse-variance weights when justified.

For a candidate independent run with model row vector `x_c` and scalar weight `w_c`, the matrix determinant lemma gives

`det(M + w_c x_c x_c^T) = det(M) [1 + w_c x_c^T M^-1 x_c]`.

Therefore the candidate that maximizes

`q_c = w_c x_c^T M^-1 x_c`

provides the largest one-run increase in D-information under the assumed model.

This gives a rigorous **next-growth information score**.

### Candidate-set restrictions

Before evaluating `q_c`, exclude candidate states that violate:

- known morphology/yield feasibility;
- apparatus bounds;
- source-composition constraints;
- same-regime assumptions;
- thermal/safety constraints;
- duplicate runs that add negligible information unless replication is deliberately needed for variance estimation.

### Weighted/heteroscedastic case

If a candidate condition is expected to have larger response uncertainty, assign smaller `w_c=1/sigma_c^2` rather than treating all support points as equally informative.

Do not use D-optimality to favor a mathematically extreme point that is physically likely to produce a different growth mechanism.

---

# 9. Multiresponse design

P21 measures several responses from the same growth:

`{x_opt,d,edge,spatial metrics,morphology,...}`.

If the same design matrix applies to multiple continuous responses, one growth can inform several Jacobians simultaneously.

However response noise/correlation differ.

For response vector `y`, retain the response covariance matrix rather than treating all outputs as independent.

A practical multiresponse design score can combine normalized information gains for the protected responses with weights derived from P20 requirements.

Do not optimize only thickness information if composition/spectral uncertainty dominates the downstream detector requirement.

---

# 10. Stage 3 is not an ordinary factorial — source-use is hard to randomize

P21 Stage 3 includes:

- effective liquid depth/inventory;
- source-use/depletion state;
- Hg-loss state/proxy.

Source-use is **sequential state**, not a freely randomized factor. Later-use observations exist only after earlier source histories have occurred.

Likewise, a selected melt depth may be fixed for an entire source charge.

The natural experimental structure is therefore repeated-measures / split-plot-like:

- independent source charge = whole plot / genealogy unit;
- inventory/depth = whole-plot treatment where fixed by charge;
- source-use index = within-charge sequential coordinate;
- Hg-loss proxy = measured time-varying covariate, not automatically synonymous with source-use.

## Minimum support logic

To estimate linear + quadratic depth response, at least three distinct depth levels are required.

To estimate linear + quadratic source-use response, at least three separated use states are required.

But one source charge per depth is insufficient to estimate independent whole-plot run variation separately from depth effect.

A minimal credible planning structure is therefore at least:

- 3 depth levels;
- >=2 independent source charges per depth;
- >=3 measured source-use states per charge;

which implies at least 6 independent charges and 18 measured growth states if every selected use state produces a measured growth.

This is a **structural identifiability floor**, not the recommended final sample size.

With only two charges per depth, whole-plot variance and quadratic depth response remain weakly estimated. Three independent charges per depth (9 charges / 27 selected growth states) is a stronger initial planning structure when material cost permits.

Absolute depth levels and source-use indices remain OPEN.

## Intraclass-correlation warning

Repeated growths from one charge are correlated.

For `m` repeated observations with approximate intraclass correlation `rho`, the usual cluster effective-sample-size relation

`m_eff = m / [1 + (m-1) rho]`

illustrates why three growths from one charge do not supply the same information about a whole-plot depth effect as three independent source charges.

Use a mixed model/random charge effect or an equivalent covariance model for Stage 3.

---

# 11. Run order / drift protection

Within stages where randomization is physically possible, randomize or block run order.

Where source-use imposes sequence, record the sequence explicitly and use independent fresh-source genealogies to separate:

- source-use/depletion;
- furnace/calendar drift;
- operator drift;
- instrument drift.

Include repeated center/standard states distributed through the campaign rather than running all centers consecutively at the beginning.

A design can have excellent algebraic D-information and still be scientifically confounded by chronological drift.

---

# 12. Holdout prediction requirement

P21 already requires holdout confirmation.

DOE optimization does not remove this requirement.

At least one or more process combinations inside the intended operating region shall remain outside the fit dataset and be used to test predicted:

- mean composition/edge;
- thickness;
- relevant interactions;
- morphology feasibility.

If holdout residuals exceed the model prediction interval systematically, the model class or local region is inadequate even if `X^T X` is well conditioned.

---

# 13. Recommended coded planning sequence

## Stage 0

Estimate:

- P06 measurement repeatability;
- independent nominal-center growth variance;
- feasible coded-factor bounds.

## Stage 1

Default candidate:

- FCCCD + 3 centers if cube corners are physically feasible;
- BBD + 3 centers if triple-extreme combinations are undesirable.

## Stage 2

Default candidate:

- 2-factor face-centered CCD + 3 centers.

## Stage 3

Use:

- mixed/repeated-measures design across independent source charges;
- never ordinary iid regression on sequential source-use points.

## Adaptive continuation

After each stage:

1. fit the simplest physically adequate model;
2. inspect rank/condition/covariance/residuals;
3. evaluate candidate next runs using `q_c=x_c^T M^-1 x_c` with variance weighting;
4. constrain candidates to `Omega_feasible`;
5. add runs for information or pure-error resolution as needed;
6. preserve a holdout set.

---

# 14. Main conclusions

1. A two-level factorial plus centers is insufficient for the full quadratic P21 models.
2. Stage-1 FCCCD provides stronger first-order/interaction precision than the 15-run BBD, but BBD avoids three-factor extremes and uses two fewer growths.
3. Stage-2 requires axial/face points; the 11-run face-centered CCD is a clean full-rank starting structure.
4. Center replication improves pure-error/intercept/curvature information but cannot replace off-center information for derivative estimation.
5. One-block derivative resolution is not arbitrarily fine: the important center-to-edge response should generally be of order the independent-run sigma or larger for the proposed Stage-1 designs.
6. Candidate half-ranges should be chosen jointly from information resolution and physical-regime limits.
7. Sequential D-optimal selection can choose later growths by exact incremental information gain once a valid model/candidate region exists.
8. Stage-3 source-use data are clustered/sequential and require multiple independent source genealogies; repeated uses of one charge are not independent replicates.
9. None of these design calculations authorizes an apparatus tolerance or historical process setpoint.

---

## Provenance

All numerical design diagnostics in this file are derived from standard linear-model/Fisher-information algebra applied to the explicitly stated coded design matrices. No new HgCdTe process literature value is introduced.

This calculation supplements:

- `procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`;
- `calculations/RP01_LPE_TO_SPECTRAL_JACOBIAN_FRAMEWORK.md`;
- `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`.
