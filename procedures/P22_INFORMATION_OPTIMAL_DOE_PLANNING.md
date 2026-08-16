# P22 — information-optimal DOE planning for P21 LPE Jacobian qualification

**Status:** CONTROLLED ANALYTICAL / PRE-EXPERIMENT PLANNING METHOD  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert the P21 empirical-Jacobian problem into a controlled experimental-design plan that maximizes information per independent growth while preserving physical identifiability, morphology feasibility and genealogy.

P22 is intentionally apparatus-scale-free at this stage.

It controls:

- coded factor definitions;
- required model rank;
- candidate design selection;
- center replication;
- derivative-resolution planning;
- sequential Fisher/D-optimal run selection;
- drift/randomization/blocking;
- source-use repeated-measures structure;
- holdout confirmation.

P22 does **not** authorize real perturbation magnitudes until P21 Stage 0 establishes metrology, independent-run variance and same-regime bounds.

Detailed calculations are in:

`calculations/RP01_P21_CODED_DOE_INFORMATION_DESIGN.md`.

---

## 2. Inputs required before planning a stage

For every factor provide:

- physical variable name;
- process meaning;
- candidate center;
- whether it is freely randomized, hard-to-change, sequential or merely observed;
- lower/upper same-regime bounds if known;
- metrology uncertainty;
- apparatus actuation resolution;
- expected sign/magnitude of response if any;
- known coupling to other factors.

For every response provide:

- response name/units;
- measurement method/version;
- measurement repeatability;
- independent-run variance estimate when available;
- downstream P20 requirement relevance;
- morphology/yield status if categorical or bounded.

Do not design around a nominal factor that is not actually measured. Example: use corrected `DeltaT_SC`, not controller setpoint alone.

---

## 3. Coded variables

For continuous factor `u_i`, define

`z_i=(u_i-u_i0)/Delta u_i`.

The coded design interval is initially `[-1,+1]`.

`Delta u_i` is not arbitrary. It must satisfy both:

### lower information bound

The expected scientifically important response across `Delta u_i` must be resolvable above measurement + independent-run noise.

### upper physics bound

The interval must remain inside the same physical regime and morphology feasible region.

If no interval satisfies both, the response cannot be estimated reliably with the current apparatus/metrology/model and the limiting subsystem must be improved first.

---

## 4. Model hierarchy

Use the smallest model justified by the scientific question.

### Jacobian-only model

`y=beta0+sum beta_i z_i+error`.

Use when the only immediate objective is local first derivatives and prior evidence shows curvature/interactions negligible over the selected region.

### first-order + interaction model

`y=beta0+sum beta_i z_i+sum beta_ij z_i z_j+error`.

Use when coupled factors such as supercooling/time or xL/yL are expected to interact.

### local quadratic model

`y=beta0+sum beta_i z_i+sum beta_ij z_i z_j+sum beta_ii z_i^2+error`.

Use when centering/robustness/curvature matter.

Do not fit the full quadratic automatically if the number of independent growths cannot support it.

---

## 5. Rank gate before any run is accepted as a planned design

Construct the exact model matrix `X` for the proposed run list.

Require:

`rank(X)=p`.

Also report:

- `n`;
- residual degrees of freedom `n-p`;
- `kappa(X^T X)` under the frozen coding/model basis;
- diagonal of `(X^T X)^-1`;
- determinant/information metric.

### Explicit rejected pattern

For a full quadratic response:

- `2^3` factorial + centers is rank deficient for 3 factors;
- `2^2` factorial + centers is rank deficient for 2 factors.

Center replication alone does not identify separate quadratic coefficients.

---

## 6. P21 Stage-1 default candidate designs

Factors:

`{xL,yL,DeltaT_SC}`.

### Option A — face-centered CCD

- 8 cube corners;
- 6 axis/face points;
- 3 centers;
- `n=17`.

Use when the entire coded cube is confirmed to lie inside the same growth/morphology regime.

Primary advantage:

- stronger linear/Jacobian and interaction precision.

Primary risk:

- all-three-extreme corner states may be physically undesirable.

### Option B — Box-Behnken + 3 centers

- 12 two-factor edge-midpoint states;
- 3 centers;
- `n=15`.

Use when simultaneous extremes of all three factors should be avoided.

Primary advantages:

- fewer runs;
- no triple-extreme corners;
- good curvature identification.

Primary cost:

- weaker linear/interaction precision than the 17-run FCCCD.

### Selection gate

The choice is based on:

1. morphology/same-regime feasibility;
2. protected derivative priorities from P20;
3. expected independent-run sigma;
4. material/run cost.

Do not choose by generic DOE convention.

---

## 7. P21 Stage-2 default design

Factors:

`{DeltaT_SC,t_contact}`.

For the full local quadratic, use the face-centered 2-factor design:

- four corners;
- four axis points;
- three center replicates;
- `n=11`.

This is full rank for

`{1,z1,z2,z1z2,z1^2,z2^2}`.

If morphology excludes one or more support points, redesign using the constrained sequential method rather than silently deleting a point.

---

## 8. Center-run placement

Center runs are not all to be performed consecutively unless a specific stability study requires it.

Distribute them across the chronological sequence to expose:

- furnace drift;
- source conditioning;
- operator/calendar drift;
- P06 drift.

For example, one center may be placed early, one near mid-campaign and one late, subject to source genealogy constraints.

Randomization/blocking should preserve the ability to detect time drift.

---

## 9. Independent-run versus spatial replicate rule

One LPE growth is the independent process experimental unit for Stage 1/2 material-response estimation.

Multiple P06 locations on one layer are:

- spatial observations within one growth;
- not independent growth replicates.

Use hierarchical variance decomposition:

`measurement -> within-growth spatial -> independent-growth`.

The DOE information matrix for process coefficients shall not count each map point as an independent process row.

Spatial maps can enter as response summaries or through an explicit hierarchical model.

---

## 10. Derivative-resolution gate

For response `y`, factor `u`, coded half-range `Delta u`, independent-run residual standard deviation `sigma_y`, and derivative `g=partial y/partial u`:

`eta = |g| Delta u / sigma_y`.

Before freezing the physical perturbation, calculate the design-specific minimum resolvable standardized effect using the chosen alpha/power and coefficient SE multiplier.

Round-15 default planning values use:

- two-sided alpha `0.05`;
- target power `0.80`.

The detailed one-block scales are in the calculation file.

If the expected important `eta` is well below the design's resolution:

- enlarge the factor half-range if physics permits;
- improve measurement/run stability;
- replicate the design or strategically add information-rich runs;
- reduce the fitted model dimension if scientifically justified.

Do not pretend a statistically unresolved slope is a precise process derivative.

---

## 11. Sequential information-optimal next-run rule

After valid data exist, form the current weighted information matrix

`M=X^T W X`.

For every physically admissible candidate state `c`, calculate model row `x_c` and expected inverse-variance weight `w_c`.

Score:

`q_c = w_c x_c^T M^-1 x_c`.

By the matrix determinant lemma, the D-information multiplier from adding that run is

`1+q_c`.

Select the highest-information candidate only after applying the physics/genealogy constraints below.

### Exclude candidates that

- are outside `Omega_feasible`;
- cross a known growth-regime boundary;
- cannot be realized/calibrated accurately;
- confound source-use with calendar drift irreparably;
- violate frozen apparatus/process-family assumptions;
- duplicate existing points without a deliberate pure-error objective.

The highest algebraic `q_c` is not automatically the highest scientific-value run.

---

## 12. Information-priority weighting from P20

P21 produces multiple responses, but P20 identifies which outputs most strongly control the final detector requirement.

Therefore adaptive run selection should prioritize information reduction in responses such as:

- `x_opt` / optical edge;
- thickness where absorption sensitivity is material;
- spatial composition uniformity;
- material-to-detector spectral bridge.

A run that greatly improves a low-priority morphology scalar but contributes little to the dominant spectral uncertainty should not necessarily displace a run that better identifies the protected Jacobian, provided morphology constraints remain satisfied.

Document the weighting rationale.

---

## 13. Stage-3 genealogy / repeated-measures design

Stage 3 cannot be planned as ordinary iid rows because source-use is sequential.

### Experimental units

- source charge/genealogy = independent whole-plot unit;
- selected liquid depth/inventory = whole-plot treatment when fixed by charge;
- source-use state = within-charge repeated sequential coordinate;
- Hg-loss proxy = separately measured covariate/state.

### Minimum structural support

To estimate quadratic depth and source-use effects requires at least three levels of each.

To separate depth from independent charge-to-charge variation requires multiple independent charges at each depth.

Initial structural floor:

- 3 depth levels;
- at least 2 independent source charges per depth;
- at least 3 selected use states per charge.

This corresponds to at least 6 independent source genealogies and 18 selected growth states.

This is not a power-based final recommendation.

Three independent charges per depth is scientifically stronger for whole-plot variance estimation when resources permit.

### Statistical model

Use a mixed model or covariance-equivalent analysis, for example:

`y = fixed(depth,use,depth*use,quadratic terms) + random(charge) + error`.

Add random slope/source-history structure only if data support it.

Do not treat repeated source-use observations as independent replicates of the depth factor.

---

## 14. Source-use versus Hg-loss separation

Run order/source-use, extraction fraction and Hg loss are distinct coordinates.

P22 requires recording:

- use index;
- cumulative growth/contact time;
- `epsilon_m` extraction/loading proxy;
- `f_Hg` or alternate calibrated Hg-loss proxy where available;
- liquidus shift;
- thermal history.

If source-use and Hg-loss cannot be separately identified statistically, report a combined state variable rather than unstable partial coefficients.

---

## 15. Randomization and blocking

### Freely randomized factors

Randomize run order where the physical process permits.

### Hard-to-change factors

Use blocks/split-plot structure and analyze at the correct experimental-unit level.

### Sequential factors

Preserve chronological order by definition, but interleave independent source genealogies where practical so time drift is not perfectly aliased with source-use.

### Instrument drift

Use stable reference specimens / P06 QC checks throughout the campaign.

---

## 16. Holdout and model-validation plan

Reserve confirmation states outside the model-fit dataset.

At minimum include:

- center confirmation;
- one interior combined perturbation;
- one feasible near-margin state when scientifically appropriate.

For each holdout compare observed vs predicted:

- mean response;
- prediction interval;
- morphology state;
- spatial uniformity.

A high-rank, high-determinant model that fails holdout prediction is not accepted.

---

## 17. Promotion of derivative status

A P21 derivative is promoted through:

1. `EMPIRICAL-REQUIRED` — no data;
2. `EMPIRICAL-PRELIMINARY` — estimable coefficient with adequate rank but no independent holdout validation;
3. `EMPIRICAL-VERIFIED` — holdout prediction and residual/model checks passed over stated local range;
4. handed to P20 for requirement allocation;
5. only after detector-level confirmation and P17 capability may the resulting tolerance become `LOCAL-QUALIFIED`/`RELEASED`.

Do not promote based only on p-value.

---

## 18. Required design-review outputs before execution

Each proposed P21 stage shall have a frozen design record containing:

- factor list and coding equations;
- physical center and half-ranges or `OPEN` state;
- candidate set;
- morphology/physics exclusions;
- model formula;
- exact run matrix;
- rank;
- condition number;
- coefficient SE multipliers;
- residual df;
- expected independent-run sigma;
- standardized derivative-resolution target;
- randomization/blocking schedule;
- genealogy plan;
- holdout plan;
- response priorities;
- PASS/REVISE disposition.

Use `travelers/P22_DOE_INFORMATION_REGISTER.md`.

---

## 19. Current release blockers

P22 remains pre-experiment until:

1. Stage-0 independent-run variance exists for the selected apparatus;
2. P06 repeatability is quantified;
3. same-regime/morphology bounds are known well enough to scale coded factors;
4. local source/thermal controls can realize the planned perturbations;
5. Stage-1 candidate design passes physics review;
6. source genealogy/material availability supports the independent-run requirement;
7. P20 defines which material-response derivatives have highest information value.

---

## 20. Main controlled conclusions

- Full quadratic curvature cannot be recovered from a two-level factorial plus centers alone.
- The default Stage-1 choice is conditional: FCCCD for derivative precision, BBD when triple-extreme states are undesirable.
- Stage-2 default is an 11-run face-centered quadratic design.
- Center runs are for pure error/drift/curvature support, not substitutes for off-center derivative information.
- Perturbation size is determined jointly by statistical resolvability and physical validity.
- Adaptive next-growth choice uses exact Fisher-information increment subject to `Omega_feasible`.
- Stage-3 source-use data require independent source genealogies and mixed/repeated-measures analysis.
- No coded design result creates a real LPE recipe tolerance.
