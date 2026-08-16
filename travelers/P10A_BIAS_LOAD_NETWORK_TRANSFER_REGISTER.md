# P10A — Bias/load-network transfer qualification register

**Status:** `CONTROLLED-QUALIFICATION-REGISTER`

Use with:

- `procedures/P10_DEVICE_DC_BIAS_SELF_HEATING.md`
- `procedures/P10A_UWA_BIAS_LOAD_NETWORK_LINEAGE_TRANSFER_ADDENDUM.md`
- P11/P11A radiometry
- P12/P12A/P12B/P12C noise and D*
- P33 package thermal qualification

Do not populate historical unknowns by inference.

---

## A. Device identity

- Run ID:
- Date/time:
- Operator:
- Wafer ID:
- Device ID:
- Package ID:
- Contact pair IDs:
- Nominal gap:
- Measured active gap `L_active`:
- Measured active width `W_active`:
- HgCdTe thickness:
- Active-area convention:
- Geometry metrology file/reference:

Historical-RP01 comparison status:
- [ ] same physical detector identity known locally
- [ ] exact historical Figure-3/5/6/7 contact pair remains OPEN

---

## B. Thermal / optical state

- Cold-finger controller setpoint:
- Measured mount temperature:
- Detector temperature proxy/method:
- Vacuum/exchange-gas state:
- Window/filter:
- FOV geometry:
- Background source/radiance state:
- Chopper/modulator state:
- P33 package thermal calibration version:
- `H_pkg,thermal` reference:

---

## C. Complete bias/readout schematic

Attach schematic filename/version:

Bias mode:
- [ ] stiff voltage source
- [ ] resistor-biased voltage source
- [ ] current source
- [ ] pulsed voltage
- [ ] other: ______

Bias source:
- Manufacturer/model:
- Serial:
- Calibration date:
- Range:
- Compliance:
- Nominal output impedance:
- Measured output impedance if characterized:
- Output filter:
- Ground/isolation state:

Network elements:

| Ref | Function | Nominal | Measured | Temperature | Uncertainty | Notes |
|---|---|---:|---:|---:|---:|---|
| | series/load R | | | | | |
| | bias R | | | | | |
| | coupling C | | | | | |
| | bypass C | | | | | |
| | protection | | | | | |
| | cable/wiring | | | | | |

Preamplifier:
- Model/custom circuit ID:
- Gain setting:
- Input topology:
- Input impedance `Z_pre(f)` calibration file:
- Coupling mode:
- Gain transfer `G_pre(f)` file:
- Input voltage-noise model:
- Input current-noise model:

Downstream instrument:
- Lock-in/analyzer model:
- Input impedance:
- Coupling:
- Measurement configuration/version:

---

## D. Detector-terminal voltage calibration

Method:
- [ ] direct high-Z sensing across selected contacts
- [ ] four-terminal sense
- [ ] reconstructed from calibrated network
- [ ] other: ______

For reconstructed voltage:

`V_contact = V_source - I R_series - V_other`

Record correction terms and uncertainty.

| Point | V_source | V_contact | I | E=V_contact/L | P_det=V_contact*I | T/proxy | Polarity |
|---:|---:|---:|---:|---:|---:|---:|---|
| 0 | | | | | | | |
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |

Canonical 10-V/cm point:
- Required `V_contact`:
- Measured `V_contact`:
- Measured E:
- Measured current:
- Detector power:
- Static resistance:
- Differential resistance:
- Field uncertainty:

Gate:
- [ ] PASS — detector-terminal field directly demonstrated
- [ ] CONDITIONAL — corrected field with acceptable uncertainty
- [ ] FAIL — source voltage used without adequate drop correction

---

## E. Low-field I–V / load-line gate

Acquisition file:
- Field range:
- Positive/negative sweep:
- Dwell per point:
- Return-to-zero points:

Fit/results:
- low-field conductance:
- intercept:
- residual metric:
- polarity asymmetry:
- hysteresis:
- detector resistance at 10 V/cm:

Network load-line file:
- [ ] measured source-side I–V
- [ ] measured detector-terminal I–V
- [ ] nonlinear detector load line used if required

Disposition:
- [ ] PASS
- [ ] REVIEW
- [ ] FAIL

---

## F. Small-signal transfer calibration

Purpose: determine how detector-terminal signal appears at P11/P12 measurement node.

Calibration method:
- injected signal amplitude:
- injection source impedance:
- detector-equivalent impedance:
- frequency grid:

Transfer:

`H_sig(f) = V_meas(f)/V_detector-equivalent(f)`

- file:
- `|H_sig(1 kHz)|`:
- phase at 1 kHz:
- uncertainty:
- high-pass pole(s):
- low-pass pole(s):
- resonances/artifacts:

Signal quantity reported by P11:
- [ ] detector-terminal equivalent voltage
- [ ] preamp-input voltage
- [ ] load voltage
- [ ] amplified output corrected by calibrated transfer
- [ ] other

Gate:
- [ ] PASS
- [ ] REVIEW
- [ ] FAIL

---

## G. Bias-source / network noise qualification

Required states:

| State | Configuration | ASD/PSD file | 1 kHz value | Notes |
|---|---|---|---:|---|
| B0 | preamp input terminated | | | |
| B1 | detector-equivalent resistor, source off | | | |
| B2 | detector-equivalent resistor, source on | | | |
| B3 | actual bias/load network | | | |
| B4 | alternate low-noise source if available | | | |

Record:
- bias resistor Johnson contribution propagated through network:
- source broadband noise:
- 50/60-Hz components:
- regulator/reference spurs:
- drift:
- P12B calibration reference:

Gate:
- [ ] source/network noise acceptably below detector-noise target
- [ ] correction possible with acceptable uncertainty
- [ ] electronics-limited — detector result cannot be released

---

## H. AC-coupling / bias-tee gate

- AC-coupling present? yes/no
- topology:
- component values:
- measured amplitude transfer file:
- measured phase transfer file:
- attenuation at 1 kHz:
- phase at 1 kHz:
- transfer across 100 Hz–10 kHz or actual analysis band:
- settling/recovery after bias change:

Gate:
- [ ] PASS — calibrated/flat or corrected
- [ ] FAIL — unknown frequency-dependent attenuation

---

## I. Self-heating / duty-cycle experiment

Fields tested:
- canonical 10 V/cm: yes/no
- higher-field sweepout region: yes/no

| Condition | Peak E | Duty | Pulse width | Repetition | I | P_peak | P_avg | T/proxy change | Responsivity | Noise metric |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| short pulse | | | | | | | | | | |
| low duty | | | | | | | | | | |
| medium duty | | | | | | | | | | |
| DC | | 100% | | | | | | | | |

Thermal results:
- thermal settling time:
- recovery time:
- inferred/measured `Delta T` at 10 V/cm:
- `R_theta` if valid:
- package thermal-kernel version:

Interpretation:
- [ ] no measurable thermal effect within uncertainty
- [ ] thermal contribution identified and corrected/limited
- [ ] thermal state invalidates nominal field comparison

---

## J. Sweepout versus heating discrimination

At field(s) where responsivity departs from low-field linearity:

- field:
- normalized sweepout metric `S(E)`:
- response versus duty cycle:
- response versus polarity:
- detector T/proxy:
- post-bias recovery:
- contact/RIE lineage:

Disposition:
- [ ] consistent with sweepout at controlled thermal state
- [ ] heating contributes materially
- [ ] both mechanisms plausible
- [ ] unresolved

Do not classify from one DC field sweep alone.

---

## K. P11 / P12 electrical-state identity

| Coordinate | P11 responsivity state | P12 noise state | Match/correction |
|---|---|---|---|
| Device ID | | | |
| Contact pair | | | |
| L_active | | | |
| V_contact | | | |
| Electric field | | | |
| Detector current | | | |
| Detector power | | | |
| Static/differential R | | | |
| Bias topology | | | |
| Load/source R | | | |
| Preamp loading | | | |
| Thermal state | | | |
| Package/window | | | |
| FOV/background | | | |
| Signal-frequency convention | | | |

Final state:
- [ ] `STATE-ELECTRICALLY-IDENTICAL`
- [ ] `CORRECTED-TO-COMMON-ELECTRICAL-STATE`
- [ ] `INCOMPATIBLE — DO NOT CALCULATE JOINT D*`

---

## L. Historical RP-01 comparison record

Directly closed:
- [ ] field means voltage bias between contacts / active gap
- [ ] Figure-3 field sweep approximately 0–50 V/cm
- [ ] Figures 5–7 canonical field 10 V/cm
- [ ] Figures 3/5/6/7 same physical device

Still OPEN unless new source attached:
- [ ] contact pair/gap
- [ ] historical bias-source model
- [ ] source/load resistance
- [ ] detector current at 10 V/cm
- [ ] detector R at 10 V/cm
- [ ] preamp input impedance
- [ ] coupling network
- [ ] P11/P12 exact topology identity
- [ ] exact 1995 thesis preamplifier schematic

New source/provenance notes:

---

## M. Final output vector

Populate:

`Y_bias = {contact_pair, L, W, V_source, V_contact, I, E, P_det, R_static, R_diff, H_sig(f), H_noise(f), Z_pre(f), source_noise, T_detector_proxy, H_pkg,thermal, duty, polarity, sweepout_metric}`

Release disposition:
- [ ] PASS for local P10/P11/P12 use
- [ ] CONDITIONAL
- [ ] FAIL

Reviewer:
- Date:
- Notes:
