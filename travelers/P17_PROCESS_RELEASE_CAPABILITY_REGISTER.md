# P17 — Process release / capability register

**Status:** BLANK CONTROLLED TEMPLATE

**Purpose:** Populate only with locally measured/qualified data. Do not fill missing limits from generic semiconductor conventions.

## A. Program / dataset identity

- Process revision:
- Device reference process:
- Analysis revision:
- Date range:
- Number of independent LPE runs:
- Number of source charges:
- Number of substrate lots:
- Number of anneal runs:
- Number of fabricated devices:
- Number of packaged devices:
- Operators:
- Tools/furnaces/reactors included:

## B. Measurement-system qualification register

| Metric | Measurement method | Instrument/configuration | Repeatability | Long-term/reproducibility | Bias/reference result | Resolution | Linearity/configuration check | Standard/expanded uncertainty | Status |
|---|---|---|---:|---:|---:|---:|---|---:|---|
| P06 thickness |  |  |  |  |  |  |  |  | OPEN |
| P06 optical edge/x |  |  |  |  |  |  |  |  | OPEN |
| P05 sheet resistance |  |  |  |  |  |  |  |  | OPEN |
| P05 Hall density |  |  |  |  |  |  |  |  | OPEN |
| P05 mobility |  |  |  |  |  |  |  |  | OPEN |
| P01 etch depth |  |  |  |  |  |  |  |  | OPEN |
| P01 undercut/CD |  |  |  |  |  |  |  |  | OPEN |
| P02 oxide thickness |  |  |  |  |  |  |  |  | OPEN |
| P08 conversion depth |  |  |  |  |  |  |  |  | OPEN |
| P09 TLM rho_c |  |  |  |  |  |  |  |  | OPEN |
| P11 responsivity |  |  |  |  |  |  |  |  | OPEN |
| P12 noise ASD |  |  |  |  |  |  |  |  | OPEN |
| P13 f_3dB/tau_eff |  |  |  |  |  |  |  |  | OPEN |

## C. Engineering specification register

| Metric | Physics/performance rationale | Nominal/target | LSL | USL | One/two-sided | Historical reference | Local detector correlation | Specification status |
|---|---|---:|---:|---:|---|---|---|---|
| Layer thickness |  |  |  |  |  | RP-01 9.5 µm |  | OPEN |
| Optical x/edge |  |  |  |  |  | RP-01 x≈0.30 / device cutoff ~4.4 µm |  | OPEN |
| Carrier type |  |  |  |  |  | RP-01 n-type |  | OPEN |
| Hall density |  |  |  |  |  | RP-01 supplier 9.8e14 cm^-3, T unstated |  | OPEN |
| Mobility |  |  |  |  |  | RP-01 supplier 4e4 cm²/Vs |  | OPEN |
| Mesa depth |  |  |  |  |  | through 9.5-µm active layer required |  | OPEN |
| Mesa undercut |  |  |  |  |  | none published |  | OPEN |
| Oxide thickness |  |  |  |  |  | RP-01 ~80 nm |  | OPEN |
| Contact rho_c |  |  |  |  |  | RP-01 ~9e-4 Ωcm² at80K |  | OPEN |
| Responsivity |  |  |  |  |  | RP-01 reference curves |  | OPEN |
| Noise ASD at signal f |  |  |  |  |  | historical 24.5 nV/√Hz g-r plateau, not necessarily 1kHz |  | OPEN |
| D* |  |  |  |  |  | RP-01 ~2e11 cm√Hz/W at4µm |  | OPEN |
| Bandwidth/tau |  |  |  |  |  | no RP-01 value |  | OPEN |

## D. Variance-component register

| Metric | Measurement variance | Within-wafer spatial variance | Run-to-run variance | Source-charge/lot variance | Long-term tool variance | Dominant component | Analysis method/revision |
|---|---:|---:|---:|---:|---:|---|---|
| Thickness |  |  |  |  |  |  |  |
| Optical x/edge |  |  |  |  |  |  |  |
| Hall density |  |  |  |  |  |  |  |
| Mobility |  |  |  |  |  |  |  |
| rho_c |  |  |  |  |  |  |  |
| Responsivity |  |  |  |  |  |  |  |
| Noise ASD |  |  |  |  |  |  |  |
| D* |  |  |  |  |  |  |  |

## E. Capability / risk register

| Metric | Stable/in-control? | Distribution/model | Mean | Within sigma | Overall sigma | Cp / one-sided analogue | Cpk / one-sided analogue | Uncertainty/spec-width ratio | Runs/lots | Decision |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Thickness |  |  |  |  |  |  |  |  |  | OPEN |
| Optical x/edge |  |  |  |  |  |  |  |  |  | OPEN |
| Hall density |  |  |  |  |  |  |  |  |  | OPEN |
| Mobility |  |  |  |  |  |  |  |  |  | OPEN |
| rho_c |  |  |  |  |  |  |  |  |  | OPEN |
| Responsivity |  |  |  |  |  |  |  |  |  | OPEN |
| Noise ASD |  |  |  |  |  |  |  |  |  | OPEN |
| D* |  |  |  |  |  |  |  |  |  | OPEN |

## F. Coupled process windows

### F1. LPE window

Model/revision:

`{source state, melt inventory, TL, ΔT_SC, T(t), growth time, source-use index} -> {thickness, x, morphology}`

Released allowed region:

- Source-preparation revision:
- Melt-inventory range:
- Measured TL range:
- ΔT_SC range:
- Growth-time range / response model:
- Maximum source-use/depletion state:
- Temperature uncertainty requirement:
- Status: OPEN

### F2. Hg anneal window

Model/revision:

`{initial state, T_dwell, time, T_reservoir/pHg, cooldown trajectory} -> {carrier type,n_H,µ_H,x/lambda,thickness,lifetime}`

Released allowed region:

- Dwell T:
- Dwell time:
- Reservoir condition:
- pHg model:
- Cooldown trajectory:
- Endpoint criterion:
- Status: OPEN

### F3. RIE/contact window

Model/revision:

`{gas ratio, pressure, self-bias/ion proxy, sample T, post-clear exposure} -> {d_etch,transport,d_conv,L_conv,rho_c,sweepout/noise}`

Released allowed region:

- Gas ratio:
- Pressure:
- Self-bias/ion proxy:
- Sample T:
- Semiconductor exposure time after oxide clear:
- TLM/contact gate:
- Functional detector gate:
- Status: OPEN

## G. Yield register

| Yield stage | Numerator | Denominator | Yield | Confidence/uncertainty method | Dominant failure classes | Revision |
|---|---:|---:|---:|---|---|---|
| Substrate/material pass |  |  |  |  |  |  |
| LPE/anneal material pass |  |  |  |  |  |  |
| Frontside fabrication pass |  |  |  |  |  |  |
| Contact/TLM pass |  |  |  |  |  |  |
| Bare-die detector pass |  |  |  |  |  |  |
| Package pass |  |  |  |  |  |  |
| Full performance pass |  |  |  |  |  |  |

## H. Change-control register

| Change ID | Date | Changed item | Old revision | New revision | Physics/risk path | Required requalification | Results | Approved/rejected |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## I. Failure Pareto register

| Failure class | Count | Fraction | Evidence quality | Likely process module | Corrective action | Verification result |
|---|---:|---:|---|---|---|---|
| Material x/thickness |  |  |  |  |  |  |
| Substrate/interface |  |  |  |  |  |  |
| Anneal state |  |  |  |  |  |  |
| Mesa/passivation |  |  |  |  |  |  |
| RIE/contact |  |  |  |  |  |  |
| Metallization/lift-off |  |  |  |  |  |  |
| Packaging |  |  |  |  |  |  |
| Measurement artifact |  |  |  |  |  |  |
| Unknown |  |  |  |  |  |  |

## J. Release signoff

- Measurement-system state:
- Process-stability state:
- Intermediate process capability state:
- Final detector yield/performance state:
- Open deviations:
- Release maturity (`OPEN`, `LOCAL-QUALIFIED`, `PILOT-RELEASE`, `PRODUCTION-RELEASE`):
- Approved revision:
- Reviewer(s):
- Date:
