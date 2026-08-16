# P21 — LPE Jacobian qualification register

**Status:** BLANK CONTROLLED DEVELOPMENT REGISTER  
**Use with:** `procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`

## A. Campaign identity

- Campaign ID:
- Date range:
- Operator(s):
- Boat revision:
- Furnace/tube position revision:
- Substrate class/lot:
- P07C surface-prep route/version:
- Source-preparation route/version:
- Auxiliary-Hg architecture/version:
- Thermal trajectory family:
- Wipe-off route/version:
- P06 instrument/method/model version:
- P04/P05 route version if used:
- P11 detector spectral method/version if used:

## B. Frozen geometry/state

- Substrate dimensions:
- Growth-contact area:
- Well dimensions:
- Effective liquid-depth definition:
- Nominal liquid inventory:
- Free liquid surface area:
- Sensor locations:
- Sensor-to-melt correction version:
- Atmosphere sequence:
- Source-use/depletion coordinate definition:
- Hg-loss state/proxy definition:

## C. Metrology qualification

### Balance / delivered mass

- Balance ID:
- Calibration date:
- Repeatability near Hg mass:
- Repeatability near Cd mass:
- Repeatability near Te mass:
- Transfer-loss estimate:
- Reconstructed xL uncertainty:
- Reconstructed yL uncertainty:

### Liquidus / thermal

- TL_actual method:
- Calibration/reference:
- TL_actual standard uncertainty:
- T_contact standard uncertainty:
- covariance/correlation treatment:
- DeltaT_SC uncertainty:

### P06

- repeated-reference specimen ID:
- x_opt repeatability:
- edge-metric repeatability:
- thickness repeatability:
- spatial registration uncertainty:
- model systematic uncertainty statement:

## D. DOE block definition

- Stage: 0 / 1 / 2 / 3 / 4
- Factor coding/scaling version:
- Center point:
- Planned factor ranges:
- Planned run order/randomization:
- Center-run IDs:
- Holdout-run IDs:
- Exclusion rule version:

## E. Per-growth record

| Field | Value |
|---|---|
| Growth ID | |
| Source lot | |
| Source-use index | |
| Actual m_Hg | |
| Actual m_Cd | |
| Actual m_Te | |
| Reconstructed xL | |
| Reconstructed yL | |
| Initial liquid mass | |
| Effective h_liquid | |
| TL_actual | |
| T_contact | |
| DeltaT_SC | |
| Contact start time | |
| Separation time | |
| t_contact | |
| Thermal trace file | |
| Hg-source state | |
| Hg-loss proxy/state | |
| Substrate ID/position | |
| Wipe-off state | |
| P06 dataset | |
| P05 dataset if used | |
| P11 dataset if used | |
| Inclusion status | |
| Exclusion/review reason | |

## F. P06/material responses

- mean x_opt:
- sigma_x:
- x min/max:
- longitudinal x gradient:
- transverse x gradient:
- edge metric mean:
- edge metric spread:
- mean thickness:
- sigma_d:
- thickness min/max:
- longitudinal thickness gradient:
- transverse thickness gradient:
- composition-gradient fit parameter(s):
- P06 fit residual/QC:
- morphology class:
- residual-melt metric:
- usable-area fraction:

## G. Dimensionless/state diagnostics

Where justified:

- `epsilon_m = m_epilayer/M_liquid,initial`:
- `D_eff` source/model:
- `Fo_L = D_eff t_contact/h_liquid^2`:
- `ell_D/h_liquid`:
- `f_Hg` or calibrated Hg-loss coordinate:

If a value is unavailable, record `OPEN`; do not invent it.

## H. Model fit record

For each response:

- response name:
- model equation/version:
- factor set:
- coefficient table:
- coefficient covariance:
- residual standard deviation:
- lack-of-fit result:
- condition number / collinearity diagnostic:
- influential-run diagnostic:
- local valid range:
- holdout prediction error:
- disposition: PRELIMINARY / VERIFIED / REJECTED

## I. Jacobian table

| Output | Input | Dimensional derivative | Normalized sensitivity | Standard uncertainty / CI | Operating point | Valid range | Evidence class |
|---|---|---:|---:|---:|---|---|---|
| | | | | | | | |

Allowed evidence states:

- EMPIRICAL-REQUIRED
- EMPIRICAL-PRELIMINARY
- EMPIRICAL-VERIFIED
- MODEL-CONDITIONAL
- IDENTITY

## J. P06-to-P11 bridge

- Matched wafer/die coordinate map version:
- Detector process branch:
- Detector temperature:
- Detector edge/cutoff convention:
- P11 dataset IDs:
- model `lambda_det = F(x_opt,d,gradient,...)`:
- `partial lambda_det/partial x_opt`:
- `partial lambda_det/partial d`:
- other retained derivatives:
- covariance/model uncertainty:
- holdout verification:
- disposition:

## K. P20 handoff

- Detector spectral requirement ID:
- Allowed spectral variation/uncertainty:
- Jacobian version:
- process covariance version:
- model uncertainty contribution:
- measurement uncertainty contribution:
- proposed backward allocations:
- allocation status: OPEN / PRELIMINARY / VERIFIED
- P17 promotion authorized? YES / NO

## L. Negative results / boundary observations

Record every failed or regime-changing run:

- growth ID:
- observed signature:
- suspected mechanisms:
- discriminating evidence:
- whether retained for P18 boundary/failure analysis:

## M. Campaign conclusion

- Robust center candidate:
- Feasible morphology region:
- dominant sensitivities:
- dominant uncertainty contributions:
- unresolved interactions:
- next experiment:
- files/checkpoints updated:
