# P34 qualification traveler — CH4/H2 RIE reactor equivalence

**Status:** BLANK CONTROLLED REGISTER / PRE-RELEASE

## A. Run identity

- Run ID:
- Date/time:
- Operator:
- Reactor manufacturer/model/serial:
- Reactor revision/configuration ID:
- Chamber-state genealogy ID:
- Sample/coupon ID:
- Wafer/lot/P29 genealogy:
- Starting carrier state / P05 reference:
- Starting oxide/P25 batch:

## B. Hardware geometry

- RF frequency:
- Powered electrode material/diameter/area:
- Grounded electrode/chamber area or best estimate:
- Electrode spacing:
- Sample radial/azimuthal position:
- Carrier/holder material and dimensions:
- Total loaded area:
- Exposed HgCdTe area:
- Matching-network model/revision:

## C. Vacuum/chamber state

- Pump type/model:
- Throttle/control mode:
- Pressure gauge type/location/range:
- Gauge calibration date:
- Base pressure before gas:
- Pumpdown duration:
- Prior chamber chemistry:
- Time/plasma-hours since clean:
- Clean recipe ID:
- Seasoning recipe ID:
- Dummy load / carrier state:
- Visual wall/coating state:

## D. Gas state

### CH4
- Supplier/grade/lot:
- MFC model/range:
- Calibration date/correction:
- Commanded flow:
- Verified/qualified flow:

### H2
- Supplier/grade/lot:
- MFC model/range:
- Calibration date/correction:
- Commanded flow:
- Verified/qualified flow:

- Actual CH4:H2 ratio:
- Total flow:
- Gas stabilization time before RF:

## E. RF / plasma record

- Commanded forward power:
- Actual forward-power trace file:
- Reflected-power trace file:
- Matching settings:
- DC self-bias trace file:
- Mean/median self-bias during stable interval:
- Plasma ignition timestamp:
- Stable-plasma timestamp:
- RF-off timestamp:
- Optical emission / plasma diagnostic file if available:

## F. Pressure record

- Pressure setpoint:
- Actual process-pressure trace file:
- Mean stable pressure:
- Pressure standard deviation/range:
- Throttle position trace if available:

## G. Thermal record

- Chuck/electrode setpoint:
- Temperature sensor/proxy ID:
- Sample mounting/thermal-contact method:
- Starting sample temperature:
- Temperature trace file:
- Peak temperature during RF:
- Temperature at RF-off:
- Temperature at vent:
- Cooldown interval before vent:

## H. Oxide-clear calibration

- Oxide type/batch:
- Initial physical oxide thickness:
- Calibration method:
- `t_clear`:
- Uncertainty/repeatability:
- Full RF time `t_RF`:
- Semiconductor exposure `t_sem = t_RF - t_clear`:
- Oxide-clear evidence file:

## I. Physical etch outcome

- Pre/post step metrology method:
- HgCdTe physical recession `d_etch`:
- Uncertainty:
- Surface RMS / morphology metric:
- Sidewall/profile observations:
- Polymer/residue state:
- Cracks/pits/particulate:

## J. Electrical conversion outcome

- Sheet resistance/conductance:
- P05 Hall/multicarrier record ID:
- Hall sign/state:
- Sheet carrier density if justified:
- Hall mobility/model:
- LBIC record ID:
- Electrical conversion depth `d_conv`:
- Lateral conversion `L_conv`:
- Conversion-depth model/version:

## K. Contact / blocking closure

- RIE-to-metal elapsed time:
- P26/P09 metal/TLM lot:
- `rho_c` at stated T/background:
- P08F blocking-response record:
- Device I-V change versus matched control:
- P12 noise change versus matched control:
- P11 responsivity change if measured:

## L. Reactor-equivalence vector

Record:

`Y_RIE = {t_clear, self_bias, T_sample, d_etch, morphology, sheet_state, d_conv, L_conv, rho_c, blocking_response, detector_noise_delta}`

- Comparison reference run(s):
- Repeated independent chamber preparations represented? YES / NO
- Controller-setpoint match only? YES / NO
- Outcome-vector stability demonstrated? YES / NO
- Disposition:
  - DEVELOPMENT
  - PARTIAL-EQUIVALENCE
  - RP01-RIE-TRANSFER-QUALIFIED
  - FAIL / INVESTIGATE

## M. Deviations / observations

- Unexpected ignition behavior:
- Self-bias excursion:
- Temperature excursion:
- Pressure instability:
- Chamber-state anomaly:
- MFC anomaly:
- Residue/polymer anomaly:
- Physical/electrical depth mismatch:
- Corrective action / next discriminating run:

## N. Permanent traveler rules

1. Never release the run from `50 W / 100 mTorr / 64 sccm / 60 s` alone.
2. Record measured self-bias or another calibrated ion-energy proxy.
3. Record actual sample thermal state or validated proxy.
4. Distinguish `t_RF`, `t_clear` and `t_sem`.
5. Distinguish `d_etch`, `d_conv` and `L_conv`.
6. Do not infer historical electrode area from the 0.4-W/cm² same-UWA branch.
7. A chamber clean/seasoning change creates a new genealogy branch until equivalence is shown.
8. Do not combine volumetric converted density with an assumed conversion depth.
9. Preserve crystallographic face/polarity in the sample genealogy.
10. Final transfer requires contact/blocking/device closure, not morphology alone.
