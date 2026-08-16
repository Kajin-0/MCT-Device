# P13A — Transient / frequency-response de-embedding qualification register

**Status:** `CONTROLLED-QUALIFICATION-REGISTER`

Use with:

- `procedures/P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md`
- `procedures/P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md`
- P10/P10A bias/load qualification
- P33 package thermal qualification
- P11/P12 when testing 1-kHz dynamic attenuation

Do not use this register to manufacture a historical RP-01 lifetime. RP-01 `tau` and `f_3dB` remain open.

---

## A. Device / package identity

- Run ID:
- Date/time:
- Operator:
- Wafer ID:
- Device ID:
- Package ID:
- Contact pair:
- Measured gap `L_active`:
- Active width:
- HgCdTe thickness:
- Composition / optical-edge record:
- Passivation state:
- Package-attach genealogy:
- Window/filter:
- FOV/background:

---

## B. Thermal state

- Cold-finger setpoint:
- Measured mount temperature:
- Detector temperature/proxy:
- Sensor location:
- Vacuum/exchange gas:
- Pre-run thermal soak:
- P33 thermal-kernel version:
- Measured/qualified `H_pkg,thermal` file:
- Package thermal settling/recovery times:

Gate:
- [ ] package response negligible in carrier-analysis band
- [ ] package response explicitly de-embedded/modelled
- [ ] package contamination unresolved

---

## C. Optical source identity and waveform

- Source make/model:
- Wavelength / spectrum:
- Modulation mode:
  - [ ] sinusoidal
  - [ ] square/chopped
  - [ ] optical pulse
  - [ ] other
- Drive electronics:
- Commanded repetition/frequency:
- Measured repetition/frequency:
- Commanded pulse width:
- Measured optical pulse FWHM:
- Measured rise time:
- Measured fall time:
- Trigger/reference channel:
- Trigger jitter:
- Pulse-to-pulse stability:
- Optical reference detector:
- Reference detector bandwidth/calibration:
- Spot diameter/profile:
- Beam position:
- Incident pulse energy / modulated power:
- Transmission/absorbed-fraction model:
- Estimated excited depth/volume:

Source waveform file:

Gate:
- [ ] source sufficiently faster than claimed detector response
- [ ] source deconvolved with validated uncertainty
- [ ] source-limited — intrinsic detector value not releasable

---

## D. Historical 1998 UWA comparison fields

Complete only for a lineage comparison; do not force local values to match.

Direct Rajaduray branch:

- wavelength `1.047 µm`
- repetition `1 kHz`
- pulse duration `25 ns`
- ~77 K / vacuum
- Keithley variable-current source
- low bias to suppress sweepout
- one analyzed sample state `-1.05 V`
- AC-coupled voltage amplifier
- HP54522A
- typical 128 waveform averages
- 500 points at 20 ns spacing

Local match/difference notes:

---

## E. Injection-level qualification

### E1. Excitation series

| Level | Incident power/energy | Absorbed estimate | Spot/volume | Estimated `Delta n` or `Delta p` | `Delta n/n0` or equivalent | Peak signal | Fitted tau | Shape change? |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |

### E2. Small-signal disposition

- [ ] waveform shape invariant as excitation is reduced
- [ ] fitted tau invariant within uncertainty
- [ ] harmonic/compression test passed if frequency-domain
- [ ] excess-carrier estimate supports low injection
- [ ] injection state uncertain
- [ ] high-injection behavior observed

Disposition:
- [ ] `LOW-INJECTION-QUALIFIED`
- [ ] `HIGH-INJECTION`
- [ ] `INJECTION-STATE-UNRESOLVED`

No intrinsic low-injection lifetime may be released from the last two states.

---

## F. Bias/load state — P10A handoff

- Bias source:
- Bias mode:
- `V_source`:
- `V_contact`:
- Detector current:
- Field `E=V_contact/L_active`:
- Detector power:
- Static resistance:
- Differential resistance:
- Duty/pulse history:
- P10A run/reference:
- Low-field state used for lifetime branch:
- Higher-field state(s) used for sweepout branch:

### Bias-independence test

| Field | V_contact | I | P | tau/metric | Waveform shape | T/proxy | Notes |
|---:|---:|---:|---:|---:|---|---:|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Gate:
- [ ] low-field tau invariant to further bias reduction
- [ ] field dependence intentionally retained as sweepout/transport result
- [ ] field/sweepout contamination unresolved

---

## G. Readout / AC-coupling transfer

- Amplifier make/model/circuit ID:
- Input impedance `Z_in(f)`:
- Gain `G(f)` calibration:
- Voltage/current noise:
- AC coupling present? yes/no
- Coupling components:
- Measured high-pass pole(s):
- Measured low-pass pole(s):
- Cable/termination:
- Detector-equivalent source impedance used for calibration:

Readout transfer file:

Gate:
- [ ] transfer flat/negligible over analysis band
- [ ] transfer explicitly deconvolved
- [ ] electrical-chain limited / unresolved

---

## H. Acquisition instrument

- Instrument model/serial:
- Input range:
- Coupling:
- Termination:
- Analog bandwidth limit/filter:
- Sample rate:
- Time step:
- Record length:
- Number of points:
- Pre-trigger/trigger delay:
- Trigger source/level:
- Averaging type:
- Average count:
- Acquisition mode:
- Firmware/software version:
- Calibration date:

Raw acquisition file(s):

---

## I. Time-domain transient reduction

### I1. Raw and corrected waveform

- raw DUT waveform:
- optical reference waveform:
- baseline interval:
- source/electrical/package correction method:
- corrected waveform file:

### I2. Fit windows

| Model | Start time | End time | Parameters | RMS/weighted residual | Structured residual? | Notes |
|---|---:|---:|---|---:|---|---|
| single exponential | | | | | | |
| double exponential | | | | | | |
| diffusion/recombination model | | | | | | |
| trap/interface model | | | | | | |
| other | | | | | | |

### I3. Fit-window stability

Repeat selected model with reasonable start/end perturbations.

- tau/parameter spread:
- conclusion:

Gate:
- [ ] stable
- [ ] fit-window-sensitive
- [ ] no defensible scalar tau

---

## J. Frequency-domain response

- Source/reference complex transfer file:
- Measured DUT complex response file:
- External electrical transfer file:
- Package-thermal correction/reference:
- De-embedded `H_det(f)` file:

One-pole test:
- amplitude-derived tau:
- phase-derived tau:
- `f_3dB`:
- fit range:
- residual result:

Higher-order test:
- model:
- time constants/poles:
- physical assignment status:

Gate:
- [ ] one-pole validated by amplitude + phase
- [ ] multi-component response
- [ ] externally limited

---

## K. Time/frequency consistency

- `tau_decay`:
- `tau_freq=1/(2pi f_3dB)` if valid:
- phase-derived tau:
- combined uncertainties:

Disposition:
- [ ] mutually consistent single-pole behavior
- [ ] disagreement explained by validated physical model
- [ ] disagreement unresolved — do not report intrinsic lifetime

---

## L. Wavelength dependence

| Wavelength | Absorption-depth model | Injection | Field | tau/response | Notes |
|---:|---|---|---:|---:|---|
| | | | | | |
| | | | | | |
| | | | | | |

Special check:
- [ ] 1.047-µm near-surface decay not automatically equated to ~4-µm detector response

---

## M. Package thermal discrimination

If a slow pole/component exists:

| Test | Change | Slow-component amplitude | Slow tau | Fast tau | Interpretation |
|---|---|---:|---:|---:|---|
| optical energy | | | | | |
| pulse duration | | | | | |
| electrical Joule pulse | | | | | |
| bias duty | | | | | |
| package/attach branch | | | | | |

- P33 thermal match:
- package temperature/resistance proxy correlation:

Disposition:
- [ ] slow component package-thermal
- [ ] package contribution negligible
- [ ] mixed/uncertain

---

## N. Interface/trap / multicomponent check

Look for:

- delayed peak;
- sign reversal;
- long tail;
- bias-dependent transient shape;
- surface/passivation dependence;
- spatial dependence;
- non-exponential residual structure.

Observed:

Interpretation:
- [ ] no material trap signature resolved
- [ ] `TRAP/MULTICOMPONENT`
- [ ] unresolved

Do not assign a delayed/slow component to bulk lifetime by default.

---

## O. 1-kHz P11/P12 dynamic-attenuation gate

- De-embedded `|H_det(1 kHz)|`:
- Low-frequency plateau normalization:
- Ratio `|H_det(1kHz)|/|H_det(0)|`:
- Uncertainty:

Disposition:
- [ ] negligible attenuation within uncertainty
- [ ] measurable attenuation; P11/P12 must report/correct
- [ ] not established

---

## P. Final temporal-result classification

Select all that apply:

- [ ] `SOURCE-LIMITED`
- [ ] `ELECTRICAL-LIMITED`
- [ ] `PACKAGE-THERMAL-CONTAMINATED`
- [ ] `HIGH-INJECTION`
- [ ] `TRAP/MULTICOMPONENT`
- [ ] `SWEEPOUT/TRANSPORT-CONTAMINATED`
- [ ] `EFFECTIVE-ONLY`
- [ ] `ONE-POLE-DEVICE-RESPONSE-QUALIFIED`
- [ ] `BULK-LIFETIME-JUSTIFIED`

If `BULK-LIFETIME-JUSTIFIED`, document the physical basis separately:

---

## Q. Reported output vector

Populate as applicable:

`Y_time={device,package,contact_pair,T,E,I,P,wavelength,injection_state,source_waveform,H_readout,H_pkg,thermal,H_det(f),f_3dB,tau_decay,tau_phase,tau_eff,model,fit_window,trap_state,sweepout_state,1kHz_attenuation,classification}`.

Release:
- [ ] PASS for qualified effective temporal response
- [ ] PASS for bulk-lifetime interpretation
- [ ] CONDITIONAL / descriptive only
- [ ] FAIL / externally limited

Reviewer:
- Date:
- Notes:
