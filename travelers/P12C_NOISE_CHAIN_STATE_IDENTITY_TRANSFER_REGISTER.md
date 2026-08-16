# P12C — Noise-chain / state-identity transfer register

**Use with:** P10, P11/P11A, P12/P12A/P12B/P12C, P33.

**Purpose:** Preserve the complete device/electrical/optical/analyzer state required to compare a local HgCdTe photoconductor noise spectrum with RP-01 and to combine that spectrum with responsivity in a defensible `D*` calculation.

Do not mark fields “same as prior” unless the referenced record ID is explicit and immutable.

---

## A. Record identity

- Noise run ID:
- Date/time:
- Operator:
- Device ID:
- Wafer/growth lot:
- Fabrication traveler revision:
- Package ID:
- P10 record ID:
- P11/P11A responsivity record ID intended for `D*` closure:
- P33 package record ID:
- Analysis script/notebook/version:
- Raw-data archive location/hash:

---

## B. Historical comparison target

Target branch:

- [ ] RP-01 Figure-5 noise spectrum
- [ ] RP-01 Figure-7 `D*` closure
- [ ] local process qualification only
- [ ] other: ______

Direct RP-01 target state to preserve where applicable:

- same physical device as Figures 3/5/6/7: `YES` for historical source
- `T = 80 K`
- `E = 10 V/cm`
- stated `60° FOV`
- low-noise preamplifier
- HP35665A analyzer
- historical knee `~3 kHz`
- high-frequency g-r level `~24.5 nV/sqrt(Hz)`

Historical unknowns must remain explicit:

- exact contact pair/gap: `OPEN-HISTORICAL`
- exact preamp circuit/gain: `OPEN-HISTORICAL`
- exact HP35665A span/window/lines/averaging: `OPEN-HISTORICAL`
- exact noise quantity used for Figure-7 `D*`: `OPEN-HISTORICAL`

---

## C. Device geometry / contact-pair identity

- Selected contact pair:
- Contact labels:
- Measured active gap `L` (µm):
- Gap measurement method:
- Gap uncertainty:
- Measured active width `W` (µm):
- Width uncertainty:
- Active area convention:
- Calculated `A` (cm²):
- Optical aperture smaller than device active area? Y/N:
- If yes, optical-power/area treatment:
- Contact metallization state/age:
- Any alternate contact pairs measured on same device:

**Gate C:** `PASS / REVIEW / FAIL`

Reason:

---

## D. Thermal / package state

- Cryostat/dewar ID:
- Package/carrier ID:
- Detector temperature sensor ID:
- Sensor position relative to detector:
- Controller setpoint:
- Measured detector-representative T (K):
- T stability over noise acquisition:
- Vacuum/exchange-gas state:
- Window material/ID:
- Filter(s):
- Cold-shield state:
- Package thermal-history/cycle count:
- P33 thermal-kernel status:

**Gate D:** `PASS / REVIEW / FAIL`

---

## E. Optical background / FOV state

Do not reduce this section to the label `60°`.

- Historical comparison nominal FOV: `60°`
- Local FOV full/half-angle convention:
- Limiting aperture/cold-stop ID:
- Aperture diameter/radius:
- Detector-to-aperture distance:
- Measured/calculated view factor:
- Source/background description:
- Background/source temperature:
- Radiance-temperature calibration status:
- Window/filter transmission record ID:
- Vignetting/throughput verification:
- Chopper/modulator present during noise run? Y/N:
- Chopper frequency if present:
- Chopper stopped/open/closed state:
- Background monitor detector/sensor:
- Background stability metric over run:
- Ambient thermal drift:
- Pump/compressor optical-coupling state:

Historical note: RP-01 Figure 5 directly states `60° FOV`; exact aperture geometry and exact source radiance during that run remain open.

**Gate E:** `PASS / REVIEW / FAIL`

---

## F. DC bias / load network

- Bias source manufacturer/model:
- Battery/isolated/mains-powered:
- Nominal source voltage:
- Series/load resistor values:
- Resistor measured values/temperature:
- Coupling capacitor(s):
- Bypass/filter components:
- Bias tee/network diagram file:
- Cable type/length/capacitance:
- Preamplifier input impedance:
- Detector operating resistance/differential resistance:
- Measured active-region voltage:
- Active field `E` (V/cm):
- Detector current:
- Detector electrical power:
- P10 self-heating gate:
- Bias polarity:
- Ground/reference node:
- Measured transfer from intrinsic detector-terminal voltage to preamp input:

**Gate F:** `PASS / REVIEW / FAIL`

---

## G. Preamplifier state

- Preamplifier ID:
- Historical UWA circuit? `YES / NO / UNKNOWN`
- Topology:
- Power supply:
- Gain setting:
- Measured complex gain calibration ID:
- `|G(1 kHz)|`:
- Gain flatness over analysis band:
- Low-frequency pole(s):
- High-frequency pole(s):
- Input voltage-noise ASD characterization:
- Input current-noise ASD characterization:
- Source-impedance dependence test ID:
- Input offset/bias behavior:
- Overload margin during run:
- Shield/chassis connection:

**Gate G:** `PASS / REVIEW / FAIL`

---

## H. Analyzer state

- Analyzer manufacturer/model:
- Serial:
- Firmware/revision:
- If HP35665A, manual revision used:
- Measurement type (`PSD`, linear spectrum, etc.):
- Input channel:
- Input range:
- Input coupling:
- Input impedance:
- Frequency span/start-stop:
- Number of lines:
- Bin spacing:
- Time-record length:
- Window:
- Window ENBW factor:
- Effective ENBW per displayed line:
- Averaging type:
- Number of averages:
- Overlap:
- Anti-alias state:
- Detector/RMS/peak processing setting:
- Units/scaling mode:
- Analyzer self-calibration status/date:
- Raw time capture retained? Y/N:

**Gate H:** `PASS / REVIEW / FAIL`

---

## I. End-to-end normalization checks

### I1 — input short / electronics floor

- Run ID:
- Source impedance:
- Measured input-referred PSD/ASD:
- Narrow spectral artifacts:

### I2 — Johnson-noise reference 1

- R:
- T:
- Predicted `sqrt(4kTR)`:
- Measured ASD:
- Difference (%):

### I3 — Johnson-noise reference 2

- R:
- T:
- Predicted ASD:
- Measured ASD:
- Difference (%):

### I4 — span/line-count invariance

Configurations compared:

- Config A:
- Config B:
- Recovered white ASD A:
- Recovered white ASD B:
- Difference:

### I5 — gain injection

- Calibration signal:
- Source impedance:
- Frequency range:
- Residual versus fitted `G(f)`:

**Gate I:** `PASS / REVIEW / FAIL`

---

## J. Detector noise acquisition states

Acquire/identify as applicable.

### N0 — electronics floor

- Raw file:
- Conditions:

### N1 — detector connected, zero/near-zero bias

- Raw file:
- T/background:

### N2 — biased, optically blocked/cold-background

- Raw file:
- T/E/background:

### N3 — biased, RP-01-like stated-FOV background

- Raw file:
- T:
- E:
- FOV:
- source/background state:

### N4 — bias/background sweep

- Raw file(s):
- Factor levels:

---

## K. Stationarity / artifact record

- Number of individual records:
- Record duration:
- Detector-current drift:
- Temperature drift:
- Background/source drift:
- Burst/random-telegraph events:
- 50/60-Hz lines:
- harmonics:
- pump/compressor lines:
- chopper lines:
- digital/RF lines:
- microphonic stress test result:
- excluded frequency bins/ranges and justification:

**Gate K:** `PASS / REVIEW / FAIL`

---

## L. Reduction outputs

Store PSD before ASD.

- Raw analyzer output file:
- Detector-terminal-referred `S_meas(f)`:
- Electronics/bias-chain `S_floor(f)`:
- Corrected detector `S_det(f)`:
- Corrected detector `e_det(f)`:
- floor-subtraction uncertainty:

### 1/f branch

- fit range:
- fitted exponent `alpha`:
- coefficient:

### RP-01 historical knee

- low-frequency trend definition:
- high-frequency plateau definition:
- intersection `f_k,hist`:
- uncertainty:

### High-frequency g-r level

- plateau fit range:
- `e_GR` (nV/sqrtHz):
- uncertainty:

### Signal-frequency noise

- declared signal frequency:
- band/weighting around signal frequency:
- `e_det(1 kHz)` if applicable:
- uncertainty:

**Never set `e_det(1 kHz)=24.5 nV/sqrtHz` solely because 24.5 nV/sqrtHz is the published high-frequency plateau.**

---

## M. P11/P12 `D*` state-identity matrix

Compare noise and responsivity datasets explicitly.

| Coordinate | P11/P11A responsivity | P12C noise | Match? |
|---|---|---|---|
| physical device | | | |
| contact pair | | | |
| active gap/area | | | |
| detector T | | | |
| active E | | | |
| detector current/power | | | |
| package/window/filter | | | |
| FOV/aperture | | | |
| source/background | | | |
| electrical loading | | | |
| signal/noise frequency convention | | | |

Disposition:

- [ ] state-identical
- [ ] corrected to common state with documented model
- [ ] incompatible; do not calculate joint `D*`

---

## N. NEP / `D*` closure

- `R_v(4 µm, f_sig)`:
- responsivity uncertainty:
- `e_det(f_sig)`:
- noise uncertainty:
- active area `A`:
- area uncertainty:
- `NEP = e_det/R_v`:
- `D* = R_v sqrt(A)/e_det`:
- expanded uncertainty / coverage factor:
- historical comparison result:

If an alternate historical convention is tested, state it separately:

- convention:
- evidence:
- resulting `D*`:

---

## O. BLIP/background test

- Background varied? Y/N:
- Method (temperature/aperture/etc.):
- Photon/radiant flux calibration record:
- Noise versus background result:
- Responsivity versus background result:
- Background-fluctuation monitor result:
- Evidence that g-r/background noise dominates:
- BLIP disposition: `SUPPORTED / NOT SUPPORTED / INCONCLUSIVE`

---

## P. Final disposition

### Historical-state closure

- same-device chain Figures 3/5/6/7 preserved: Y/N
- 80 K state matched: Y/N
- 10 V/cm matched: Y/N
- stated 60° FOV matched/translated: Y/N
- active contact pair recovered historically: Y/N
- historical preamp recovered: Y/N
- historical analyzer settings recovered: Y/N
- historical D* noise convention recovered: Y/N

### Local metrology closure

- bias/load transfer calibrated: Y/N
- preamp gain/noise calibrated: Y/N
- PSD normalization validated: Y/N
- electronics floor controlled: Y/N
- background stability characterized: Y/N
- P11/P12 state identity passed: Y/N

Final status:

`HISTORICAL-EXACT / HISTORICAL-PARTIAL + TRACEABLE-TRANSFER / TRANSFER-QUALIFIED / REVIEW / FAIL`

Reviewer:

Date:

Notes/deviations:
