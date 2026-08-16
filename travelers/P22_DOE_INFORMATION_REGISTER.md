# P22 DOE information / identifiability register

**Status:** BLANK CONTROLLED PLANNING RECORD

Use one record per P21 experimental-design stage or major adaptive redesign.

---

## A. Campaign identity

- campaign ID:
- P21 stage:
- date/revision:
- apparatus/boat revision:
- source-preparation route/lot class:
- substrate class/P07C route:
- P06 method/model version:
- analyst/operator:

---

## B. Protected responses / P20 priority

| Response | Units | P20 protected requirement | Priority weight | Measurement repeatability | Independent-run sigma | Status |
|---|---|---|---:|---:|---:|---|
| | | | | | | |

Morphology/yield hard constraints:

- 

---

## C. Factors and coding

| Factor | Physical variable | Role | Center `u0` | Half-range `Delta u` | Coded range | metrology uncertainty | randomization class | Same-regime evidence |
|---|---|---|---:|---:|---|---:|---|---|
| z1 | | | | | [-1,+1] | | | |
| z2 | | | | | [-1,+1] | | | |
| z3 | | | | | [-1,+1] | | | |

Randomization class examples:

- freely randomized;
- hard-to-change / block;
- sequential state;
- measured covariate only.

Any physical half-range still OPEN?

- [ ] yes
- [ ] no

Reason / closure needed:

- 

---

## D. Candidate model

Model family:

- [ ] Jacobian-only linear
- [ ] linear + interactions
- [ ] full local quadratic
- [ ] mixed/repeated-measures
- [ ] other:

Exact model terms:

` `

Number of coefficients `p`:

- 

Physics rationale for each interaction/curvature term:

- 

Terms deliberately excluded:

- 

---

## E. Candidate design support

Design family:

- [ ] Stage-1 FCCCD
- [ ] Stage-1 Box-Behnken
- [ ] Stage-2 FCCCD
- [ ] constrained D-optimal
- [ ] Stage-3 mixed/repeated-measures
- [ ] custom

Number of planned independent growths:

- 

Number of center replicates:

- 

Number of independent source genealogies:

- 

Candidate states excluded by morphology/physics:

| Candidate state | reason excluded |
|---|---|
| | |

---

## F. Exact coded run matrix

| Planned run ID | z1 | z2 | z3 | center? | genealogy/block | planned chronological slot | holdout? |
|---|---:|---:|---:|---|---|---:|---|
| | | | | | | | |

Do not count P06 map locations as independent process rows.

---

## G. Information diagnostics

- `n =`
- `p =`
- residual df `n-p =`
- `rank(X) =`
- full rank? [ ] yes [ ] no
- `kappa(X^T X) =`
- internal `I_D = det[(X^T X)/n]^(1/p) =`

Coefficient SE multipliers `sqrt(diag[(X^T X)^-1])`:

| coefficient | multiplier |
|---|---:|
| intercept | |
| z1 | |
| z2 | |
| z3 | |
| interaction(s) | |
| quadratic(s) | |

Conditioning/aliasing review:

- 

PASS rank gate?

- [ ] PASS
- [ ] REVISE

---

## H. Derivative-resolution planning

Planning test:

- alpha:
- target power:
- residual df:
- required noncentrality:

For each protected derivative:

| response | factor | minimum important physical derivative | independent-run sigma | `Delta u` | standardized `eta=|g|Delta u/sigma` | design `eta_min` | resolvable? |
|---|---|---:|---:|---:|---:|---:|---|
| | | | | | | | |

If not resolvable, planned action:

- [ ] enlarge same-regime half-range
- [ ] improve metrology/stability
- [ ] add independent growths
- [ ] reduce model dimension with physics justification
- [ ] do not attempt derivative yet

---

## I. Randomization / blocking / drift plan

Freely randomized order:

- 

Hard-to-change blocks:

- 

Sequential constraints:

- 

Center/reference placement through chronological sequence:

- 

P06 reference/QC schedule:

- 

Potential calendar/source-use aliasing and mitigation:

- 

---

## J. Stage-3 genealogy structure, if applicable

Depth/inventory levels:

- 

Independent source charges per level:

- 

Selected source-use states per charge:

- 

Hg-loss proxy:

- 

Cumulative extraction proxy:

- 

Proposed random effects / covariance structure:

- 

Repeated observations incorrectly being treated as iid?

- [ ] no
- [ ] REVIEW

---

## K. Sequential next-run information log

Current model version:

- 

Current information matrix version:

- 

| Candidate | feasible? | expected variance/weight | `q=x^T M^-1 x * w` | P20 response value | selected? | reason |
|---|---|---:|---:|---:|---|---|
| | | | | | | |

If highest-q candidate was not selected, document physical/scientific reason.

---

## L. Holdout plan

Reserved holdout states:

| holdout ID | coded state | reason | protected outputs |
|---|---|---|---|
| | | | |

Holdout states used in model fitting accidentally?

- [ ] no
- [ ] INVALIDATE/REPLAN

---

## M. Pre-execution disposition

- [ ] PASS — design is identifiable and physically admissible
- [ ] CONDITIONAL — unresolved item below
- [ ] REVISE — design not executable/identifiable

Open items:

1. 
2. 
3. 

Approval/review note:

- 

---

## N. Post-stage update

After data are acquired record:

- fitted model version;
- coefficient covariance;
- residual sigma;
- lack-of-fit result;
- holdout prediction result;
- updated `Omega_feasible`;
- derivative status: `EMPIRICAL-PRELIMINARY` / `EMPIRICAL-VERIFIED`;
- next highest-information candidate(s);
- handoff to P20 allocation register.
