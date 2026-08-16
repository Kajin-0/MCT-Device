# Recovery checkpoint — round 15 P21 information-optimal DOE planning

**Date:** 2026-08-16 America/New_York

**Purpose:** Fast handoff after analytically designing the P21 LPE Jacobian campaign in coded coordinates.

Read after `AGENTS.md` and the round-14 checkpoint.

---

## 1. New files

Round 15 adds:

- `calculations/RP01_P21_CODED_DOE_INFORMATION_DESIGN.md`
- `procedures/P22_INFORMATION_OPTIMAL_DOE_PLANNING.md`
- `travelers/P22_DOE_INFORMATION_REGISTER.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND15.md`
- this checkpoint.

No new historical HgCdTe fabrication setpoint is claimed.

The round closes experimental-design mathematics, not physical perturbation magnitudes.

---

## 2. Core coded model

For physical factor `u_i`, candidate center `u_i0`, and half-range `Delta u_i`, use

`z_i=(u_i-u_i0)/Delta u_i`.

At center, for a local quadratic model,

`partial y/partial u_i = beta_i/Delta u_i`.

Thus DOE identifiability and coefficient precision can be studied before `Delta u_i` is fixed.

Physical half-ranges remain OPEN until Stage-0 run variance + same-regime bounds exist.

---

## 3. Fisher-information basis

For independent homoscedastic response error:

`Cov(beta_hat)=sigma^2 (X^T X)^-1`.

Round 15 uses:

- matrix rank;
- `kappa(X^T X)` under a frozen coded basis;
- coefficient SE multipliers;
- internal D-information index
  `I_D=det[(X^T X)/n]^(1/p)`.

The D index is only compared among designs using the same model-column definition.

---

## 4. Critical rank-deficiency result

For a 3-factor full quadratic, p=10.

`2^3 factorial + 3 centers` has:

- n=11;
- rank=8;
- therefore cannot identify the three separate quadratic terms.

For a 2-factor full quadratic, p=6.

`2^2 factorial + 3 centers` has:

- n=7;
- rank=5;
- likewise deficient.

Continuity rule:

**center points do not de-alias individual quadratic terms in a two-level factorial.**

Axial/edge information is required for curvature.

---

## 5. Stage-1 design comparison

Factors:

`{xL,yL,DeltaT_SC}`.

### 17-run face-centered CCD + 3 centers

- rank 10;
- residual df 7;
- `kappa(X^T X)=19.70`;
- `I_D=0.41297`;
- linear SE multiplier `0.3162 sigma`;
- interaction `0.3536 sigma`;
- quadratic `0.6109 sigma`.

Strength:

- best current default for local Jacobian + interaction precision.

Risk:

- requires all eight triple-extreme corners.

### 15-run Box-Behnken + 3 centers

- rank 10;
- residual df 5;
- `kappa=17.97`;
- `I_D=0.36643`;
- linear SE `0.3536 sigma`;
- interaction `0.5000 sigma`;
- quadratic `0.5204 sigma`.

Its internal D-information index is ~88.7% of the FCCCD value under the same coded basis.

Strength:

- two fewer growths;
- avoids all-three-factor extreme corners;
- somewhat better individual quadratic coefficient precision.

Selection rule:

- FCCCD if cube corners remain safely inside the same growth/morphology regime;
- BBD if triple-extreme states are risky.

Do not choose by generic DOE preference.

---

## 6. Stage-2 design

Factors:

`{DeltaT_SC,t_contact}`.

Full quadratic requires p=6.

Default 11-run face-centered CCD:

- 4 corners;
- 4 axis points;
- 3 centers;
- rank 6;
- residual df 5;
- `kappa=9.50`;
- `I_D=0.42835`;
- linear SE `0.4082 sigma`;
- interaction `0.5000 sigma`;
- quadratic `0.6283 sigma`.

Physical scaling remains OPEN.

---

## 7. Derivative-resolution result

Define the standardized center-to-edge linear effect

`eta=|partial y/partial u| Delta u / sigma_y = |beta|/sigma_y`.

For two-sided alpha=.05 and target power=.80, the one-block approximate linear resolution scales are:

- Stage-1 FCCCD: `eta_min≈1.034`;
- Stage-1 BBD: `eta_min≈1.242`;
- Stage-2 FCCCD: `eta_min≈1.435`.

Approximate interaction/quadratic one-block scales:

- Stage-1 FCCCD: interaction 1.156, quadratic 1.998;
- Stage-1 BBD: interaction 1.757, quadratic 1.829;
- Stage-2 FCCCD: interaction 1.757, quadratic 2.208.

This means one DOE block cannot resolve arbitrarily tiny effects.

Perturbation half-range should be selected so the minimum scientifically important response is large enough relative to independent-run sigma while remaining inside the same physical regime.

---

## 8. Replication effect

Approximate 80%-power linear eta minima for complete design replication:

| design | 1 block | 2 blocks | 3 blocks |
|---|---:|---:|---:|
| Stage-1 BBD | 1.242 | 0.736 | 0.588 |
| Stage-1 FCCCD | 1.034 | 0.653 | 0.524 |
| Stage-2 FCCCD | 1.435 | 0.862 | 0.685 |

These are planning values, not requirements.

Center-only replication does not improve all slope terms; informative off-center growths are required for derivative precision.

---

## 9. Sequential next-growth criterion

For current weighted information matrix

`M=X^T W X`

and admissible candidate model row `x_c` with weight `w_c`, define

`q_c=w_c x_c^T M^-1 x_c`.

Matrix determinant lemma:

`det(M+w_c x_c x_c^T)=det(M)(1+q_c)`.

Therefore `q_c` is the exact one-run D-information increment under the assumed linear model/error structure.

Use only after filtering candidates through:

- morphology feasible region;
- same-regime physics;
- apparatus constraints;
- genealogy/source-use constraints;
- variance weighting.

Do not allow pure algebraic D-optimality to select a physically invalid extreme.

---

## 10. Stage-3 source-use structure

Source-use is sequential, not randomized.

Natural units:

- source charge = independent genealogy / whole plot;
- melt depth/inventory = whole-plot treatment if fixed by charge;
- source-use state = repeated within-charge coordinate;
- Hg-loss state = separate measured covariate.

To support quadratic depth and use effects, structural floor:

- 3 depth levels;
- >=2 independent charges per depth;
- >=3 selected use states per charge;
- >=6 source genealogies / 18 selected growth states.

This is not a power-based final sample size.

Three charges per depth is stronger if resources permit.

Use a mixed model/random charge effect or equivalent covariance analysis.

Never treat repeated use of one charge as independent replication of depth/inventory.

---

## 11. Center-run rule

Center runs are useful for:

- independent center variance;
- drift;
- intercept;
- curvature support.

They do not replace off-center information.

Three centers remain a planning default only.

Distribute them through chronological sequence rather than clustering all centers together when drift detection matters.

---

## 12. Current open physical quantities

Round 15 intentionally leaves OPEN:

- Stage-1 physical `Delta xL`;
- `Delta yL`;
- `DeltaT_SC` scale;
- Stage-2 contact-time perturbation;
- melt-depth levels;
- selected source-use states;
- Hg-loss perturbation;
- independent-run sigma by response;
- exact morphology feasible region.

These require P21 Stage 0 or apparatus-specific evidence.

---

## 13. P22 controlled method

`procedures/P22_INFORMATION_OPTIMAL_DOE_PLANNING.md` operationalizes:

- coded scaling;
- rank gate;
- candidate design selection;
- derivative-resolution gate;
- adaptive D-information selection;
- randomization/blocking;
- Stage-3 repeated-measures genealogy;
- holdout validation;
- derivative maturity promotion.

Use `travelers/P22_DOE_INFORMATION_REGISTER.md` for each stage/revision.

---

## 14. Next logical branch

The P21 experiment is now sufficiently designed analytically that further progress requires actual Stage-0 apparatus/run variance or a concrete apparatus specification.

Therefore the strongest next purely analytical branch is the second P20 high-value Jacobian:

**P04/P05/P13 anneal trajectory -> final carrier state/mobility/lifetime.**

Target mapping:

`{T_sample(t),T_reservoir(t),pHg(t),dwell,cooldown,initial x/n/state}`

`-> {carrier sign,n_H/multicarrier,mu_H,tau_eff,optical edge preservation}`.

Important warning:

This mapping can cross p/n conversion boundaries, so it cannot be treated as one global linear Jacobian. The next round should build a state/classification + local-continuous sensitivity framework rather than force a derivative through the conversion boundary.
