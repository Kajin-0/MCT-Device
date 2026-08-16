# P20 — requirements allocation / sensitivity register

**Status:** BLANK CONTROLLED TEMPLATE  
**Purpose:** Record detector-derived numerical allocations before promoting intermediate specifications into P17.

Do not populate a tolerance because it is historical, conventional, or equal to observed process spread.

---

# A. Analysis identity

- Allocation record ID:
- Date:
- Analyst/reviewer:
- RP-01/process revision:
- P19 revision:
- P20 revision:
- Calculation/model revision(s):
- Dataset revision(s):

---

# B. Final detector/system requirement

- P19 requirement ID:
- Requirement maturity (`HISTORICAL-REFERENCE`, `PHYSICS-REQUIREMENT`, `LOCAL-SPEC-OPEN`, `LOCAL-QUALIFIED`, `RELEASED`):
- Final metric:
- Target:
- Lower/upper limit or allowed uncertainty:
- One-sided/two-sided:
- Physical rationale/system consequence:

## Operating condition

- Detector temperature:
- Electric field / bias condition:
- Wavelength:
- Signal/modulation frequency:
- Background/FOV:
- Active-area convention:
- Package/readout state:
- Other fixed conditions:

**Requirement definition complete?** ____________________

---

# C. Measurement equation

Write the exact equation or response model used to connect intermediate metrics to the final requirement.

Equation/model:

__________________________________________________________________

Assumptions/domain:

__________________________________________________________________

Known limitations/model discrepancy:

__________________________________________________________________

---

# D. Sensitivity register

| Input variable | Pxx source/control | Operating point | Dimensional derivative `J` | Normalized sensitivity `S` | Evidence class | Source/model revision | Sign/physical interpretation |
|---|---|---:|---:|---:|---|---|---|
|  |  |  |  |  |  |  |  |

Allowed evidence classes:

- `IDENTITY`
- `MODEL-CONDITIONAL`
- `PROXY-CONDITIONAL`
- `EMPIRICAL-REQUIRED`

A `PROXY-CONDITIONAL` row cannot directly support a released tolerance.

---

# E. Input metrology / current variation state

| Input | Measurement method | Standard/expanded uncertainty | Current process variation | Variance level (measurement/spatial/run/lot/tool) | Correlated with | Status |
|---|---|---:|---:|---|---|---|
|  |  |  |  |  |  |  |

---

# F. Covariance / interaction register

| Variable pair / interaction | Physical reason | Evidence | Included in model? | Method | Result/status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Examples requiring explicit consideration where applicable:

- n / mobility Hall covariance;
- active gap / area image-calibration covariance;
- source composition / actual liquidus;
- anneal sample T / Hg-reservoir state;
- detector temperature / responsivity / noise;
- RIE converted depth / sheet transport;
- blocking strength / lifetime / bandwidth.

---

# G. Requirement-budget allocation

## G1. Worst-case bounded allocation, if used

Final allowed relative budget:

`b_y = ____________________`

Check:

`sum |S_i| b_i = ____________________`

PASS / HOLD / FAIL: ____________________

| Input | Proposed relative band `b_i` | `|S_i| b_i` contribution | Rationale | Achievable? |
|---|---:|---:|---|---|
|  |  |  |  |  |

## G2. Standard-uncertainty/covariance allocation, if used

Final allowed standard uncertainty:

`u_y = ____________________`

Calculated:

`u_y^2 = J Sigma J^T = ____________________`

Coverage/expanded uncertainty convention:

____________________

| Input | Standard uncertainty | Sensitivity | Variance contribution | Fraction of total |
|---|---:|---:|---:|---:|
|  |  |  |  |  |

---

# H. Missing empirical Jacobian plan

For every `EMPIRICAL-REQUIRED` row:

| Input/output block | DOE/model required | Levels/range | Independent runs | Witness/control | Primary response | Interaction terms | Destructive? | Status |
|---|---|---|---:|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Do not substitute map points from one wafer for independent process-run replication.

---

# I. Model validation

- Center-point repeatability:
- Perturbation range tested:
- Local linearity adequate?:
- Residual structure:
- Higher-order/interaction terms significant?:
- Holdout/confirmation data:
- Model uncertainty:
- Model extrapolation prohibited outside:

**Sensitivity status after validation:** ____________________

---

# J. Proposed intermediate specifications

| Intermediate metric | Nominal/target | LSL | USL | One/two-sided | Pxx owner | Detector requirement protected | Evidence basis | Spec maturity |
|---|---:|---:|---:|---|---|---|---|---|
|  |  |  |  |  |  |  |  | `LOCAL-SPEC-OPEN` |

A proposed intermediate specification shall remain `LOCAL-SPEC-OPEN` until detector-level verification and P17 promotion criteria are satisfied.

---

# K. Metrology adequacy check

For each proposed intermediate specification:

| Metric | Spec width / decision margin | Measurement uncertainty | Uncertainty/spec ratio | False-accept/reject concern | Required metrology improvement | Status |
|---|---:|---:|---:|---|---|---|
|  |  |  |  |  |  |  |

---

# L. Detector-level verification

- Verification run/device genealogy:
- Intermediate metric deliberately varied/observed:
- Final detector metric measured:
- Predicted change:
- Observed change:
- Agreement within uncertainty?:
- Failure mechanisms/confounders:
- P18 record if discrepant:

**Does the intermediate metric demonstrably protect the stated requirement?** ____________________

---

# M. P17 promotion decision

- Engineering specification ready for P17?:
- Measurement system qualified?:
- Stable process data available?:
- P17 register row(s):
- Change-control triggers defined?:
- Release maturity:
- Reviewer approval:
- Date:

---

# N. Open items

1. ________________________________________________
2. ________________________________________________
3. ________________________________________________

---

# O. Final disposition

- [ ] ANALYTICAL ONLY — no numerical intermediate specification released
- [ ] EMPIRICAL JACOBIAN REQUIRED
- [ ] LOCAL ALLOCATION DEFINED
- [ ] DETECTOR-LEVEL VERIFIED
- [ ] READY FOR P17 CAPABILITY EVALUATION
- [ ] REJECTED / MODEL INVALID

Comments:

__________________________________________________________________

__________________________________________________________________
