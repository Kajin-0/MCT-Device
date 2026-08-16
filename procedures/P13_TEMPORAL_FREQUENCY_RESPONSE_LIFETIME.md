# P13 — temporal response / frequency response / lifetime / bandwidth

**Status:** `CONTROLLED-QUALIFICATION-METROLOGY` — temporal measurement/de-embedding is operator-defined; RP-01 itself does not publish a detector lifetime or frequency-response curve, and several historical apparatus details remain open.

## 1. Purpose

Measure the dynamic response of an RP-01-type HgCdTe photoconductor while separating intrinsic detector dynamics from source modulation, optical-path response, detector bias/load network, package thermal response, preamplifier, cabling and acquisition-instrument response.

Determine, when justified:

- normalized complex detector response `H_det(f)`;
- detector phase response;
- `f_3dB`;
- time-domain rise/fall/decay constants;
- whether one-pole behavior is adequate;
- effective detector time constant `tau_eff`;
- whether `tau_eff` can legitimately be called minority-carrier lifetime;
- field dependence / sweepout contribution;
- injection-level dependence;
- surface/interface trapping signatures;
- package/thermal poles distinct from electronic-carrier response.

Do **not** fold temporal response into conventional `D*` unless a separately defined generalized performance metric is introduced.

---

## 2. Provenance / physical basis

### P13-S1 — Kruse 1965 historical HgCdTe PC benchmark

P. W. Kruse, “Photon Effects in Hg1−xCdxTe,” *Applied Optics* 4, 687–692 (1965), DOI `10.1364/AO.4.000687`.

Photoconductive response-time measurements at 77 K were reported no greater than about `10^-7 s` for the detectors studied. This is a broad historical benchmark, not an RP-01-specific time constant.

### P13-S2 — HgCdTe recombination work

“Recombination in cadmium mercury telluride photodetectors,” *Solid-State Electronics* 21, 1475–1480 (1978), DOI `10.1016/0038-1101(78)90228-9`.

Primary HgCdTe work showing carrier lifetime as a key performance variable and using photoconductive decay experimentally. It is not an RP-01 recipe.

### P13-S3 — interface-trap transient behavior — **non-UWA transfer source**

V. Gopal, N. Devi, R. Pal, V. Kumar, “Study of the traps at a mercury cadmium telluride–anodic oxide interface using a transient photoconductive decay technique,” *Journal of Crystal Growth* 265, 530–536 (2004), DOI `10.1016/j.jcrysgro.2004.02.082`.

This source was previously mislabeled in P13 as Musca/Faraone lineage. **Correction:** it is not a UWA source. It remains valuable primary transfer evidence because it shows bias-dependent, non-simple transient photoconductive behavior associated with HgCdTe/anodic-oxide interface trapping.

Related primary paper:

R. Pal et al., “Study of interface traps from transient photoconductive decay measurements in passivated HgCdTe,” *Journal of Electronic Materials* 30, 103–108 (2001), DOI `10.1007/s11664-001-0108-x`.

This paper reports delayed peaks in PC decays attributed to interface electron/hole trapping. Therefore an arbitrary transient cannot be assumed to be a single exponential.

### P13-S4 — high-injection warning

Historical and later HgCdTe transient-lifetime literature shows that decay can depart from a simple exponential under high excess-carrier injection. Low-injection/small-signal operation must therefore be demonstrated when the intended quantity is a linear lifetime/transfer function.

### P13-S5 — modern HgCdTe fit-window warning

Modern MWIR HgCdTe transient work has shown that an initially distorted portion may need to be excluded before fitting a decay constant. This is methodological transfer evidence only; no numerical lifetime from another device is an RP-01 target.

### P13-S6 — **same-UWA 1998 transient-photoconductive-decay apparatus**

R. Rajaduray, *Investigation of Spatial Characterisation Techniques in Semiconductors*, B.E. (Honours) thesis, Department of Electrical and Electronic Engineering, University of Western Australia, 1998. Supervisor: J. M. Dell. DOI/archive copy `10.13140/RG.2.2.29365.47848`.

The thesis directly documents an n-type `x≈0.30` HgCdTe transient-photoconductive-decay branch in the same UWA laboratory lineage and acknowledges assistance from D. Redfern and E. P. G. Smith.

Direct experimental anchors recovered:

- Waterloo Scientific scanning laser microscope;
- laser wavelength `1.047 µm`;
- pulsed operation at `1 kHz` repetition frequency;
- pulse duration `25 ns`;
- optical power deliberately kept low to avoid damage;
- approximately `77 K`, under vacuum;
- liquid-N2 cooling/cold-finger/cryostat arrangement;
- sample biased with a **Keithley variable-current source**;
- bias deliberately kept small to reduce sweepout to high-recombination contacts;
- analyzed sample bias reported as `-1.05 V`;
- photoconductive voltage change amplified using an **AC-coupled amplifier**;
- HP54522A digital oscilloscope, remotely controlled by PC;
- typical scan coordinate used `128` waveform averages;
- each stored decay contained `500` voltage samples at `20 ns` spacing;
- analysis was performed in Matlab;
- the thesis compared a non-exponential diffusion/recombination solution with a single exponential and found the non-exponential model gave the better fit for the analyzed spatial-lifetime data.

These values are direct for the Rajaduray thesis branch, **not** direct RP-01 lifetime setpoints.

### P13-S7 — package thermal response can masquerade as detector response

F. J. Bartoli, L. Esterowitz, M. R. Kruer, R. E. Allen, “Thermal recovery processes in laser irradiated HgCdTe (PC) detectors,” *Applied Optics* 14, 2499–2507 (1975), DOI `10.1364/AO.14.002499`.

Direct HgCdTe photoconductor result:

- thermal recovery strongly depends on detector construction;
- one recovery component occurs on the order of several milliseconds;
- another occurs on the order of hundreds of milliseconds;
- the two time scales were attributed to two thermally resistive bonding layers;
- signal magnitude/shape depended on irradiation power density and duration.

This is the primary basis for requiring P33 package-thermal de-embedding in P13.

---

## 3. Core rule: detector dynamics must be de-embedded

The measured complex response is generally

`H_meas(f) = H_source(f) H_optics(f) H_detector(f) H_bias(f) H_preamp(f) H_cable(f) H_instrument(f) H_pkg,thermal(f)`

where `H_pkg,thermal` is included whenever optical/electrical excitation or detector bias produces a measurable thermal response in the acquisition band.

For clarity, define

`H_external(f) = H_source H_optics H_bias H_preamp H_cable H_instrument`

and treat the package thermal channel separately when it is additive/coupled rather than a simple multiplicative LTI block.

Only calculate

`H_detector = H_meas / H_external`

when the selected representation is physically valid and the external transfer has been measured with adequate SNR and phase reference.

A measured `-3 dB` point is **not** detector bandwidth when a source, coupling network, preamplifier, cable, instrument or package thermal mechanism has comparable response.

---

## 4. Apparatus classes required for a released measurement

Document equivalents of:

1. cryostat/cold finger capable of stable operation near the target detector temperature;
2. temperature sensor sufficiently coupled/placed to bound detector temperature;
3. P10/P10A calibrated DC bias/load network;
4. in-band optical source with controlled small-signal modulation or pulses;
5. optical attenuation/source-current control;
6. fast reference photodetector for source waveform/complex modulation calibration;
7. modulation/pulse driver and trigger distribution;
8. low-noise readout whose complex transfer and source-impedance dependence are calibrated;
9. lock-in/network analyzer/digitizer/oscilloscope appropriate to the selected method;
10. calibrated cables/terminations;
11. optical beam monitor/reference path when drift matters;
12. P33 package-thermal characterization or a demonstrated reason it is negligible in the analyzed time/frequency region.

Legacy UWA apparatus identity is useful provenance but exact legacy instruments are not required for local transfer when the physical quantities are calibrated.

---

## 5. Operating-state record

Every dataset stores:

- device/wafer/package ID;
- selected contact pair;
- measured active width/gap/thickness;
- detector temperature and sensor location;
- P10A `V_contact`, `E`, current and power;
- bias topology/duty/pulse history;
- optical wavelength/spectrum;
- mean optical irradiance and modulated/pulse fluence where applicable;
- spot size/profile and position;
- modulation depth or pulse width/energy;
- background/FOV state;
- package window/filter state;
- preamplifier gain/load/input impedance;
- cable/termination;
- source modulation method;
- acquisition sample rate, record length, bandwidth and averaging;
- P33 package thermal state / thermal-kernel version.

Changing field, optical injection, package state, temperature, background or readout topology creates a new dynamic operating state.

---

## 6. Injection-level gate — stronger than “low laser power”

A source can be low in average power yet produce high localized excess-carrier density in a short pulse.

The Rajaduray 1998 thesis is an important same-UWA warning. For its analyzed sample it estimated:

- layer dimensions used in the calculation approximately `1 cm × 0.5 cm × 17 µm`;
- total equilibrium electron count approximately `4.25×10^11` in that volume;
- a representative transient signal of `0.17 V` at `-1.05 V` bias was mapped to about `8.2×10^10` generated carriers;
- because those carriers were generated in a much smaller illuminated volume, the thesis concluded that the local initial state could approach **high-level injection**, where Auger recombination becomes important.

Therefore P13 does not accept “power was low” as a small-signal proof.

### Required gate

At one low test frequency or in repeated pulse-decay acquisition:

1. hold T, field and geometry fixed;
2. vary modulation amplitude/pulse fluence over at least three levels;
3. verify waveform shape and fitted time constant are invariant as excitation is reduced;
4. inspect harmonic content/compression in frequency-domain work;
5. where material parameters permit, estimate `Delta n/n0` or `Delta p/p0` using absorbed photon density and excited volume.

If lifetime/shape changes with injection level, report the injection dependence and do not collapse the result into one intrinsic lifetime.

---

## 7. Source and optical-transfer qualification

### Frequency-domain source

Measure source/reference complex modulation response:

`H_source,opt(f) = V_ref(f)/V_drive(f)`.

The reference detector bandwidth should comfortably exceed the test band or have its own calibrated response included.

### Time-domain source

Measure the actual optical pulse at the DUT reference plane whenever possible.

Record:

- wavelength;
- pulse FWHM and rise/fall time;
- repetition rate;
- pulse-to-pulse amplitude stability;
- trigger timing/jitter;
- spot geometry;
- pulse energy/fluence or calibrated relative level.

A commanded electrical pulse is not proof of the optical waveform.

### Historical UWA branch

The Rajaduray branch provides direct values `1.047 µm`, `1 kHz`, `25 ns`; exact laser model/pulse-energy calibration and source rise/fall remain open in the recovered text. Do not invent them.

---

## 8. Bias/readout transfer qualification

Use P10A and P12B principles to measure the transfer between intrinsic detector electrical response and the recorded node.

Record:

- contact pair and active field;
- source/load network;
- detector static and differential impedance;
- AC-coupling pole(s);
- preamp gain/phase and input impedance;
- cable/termination transfer;
- oscilloscope/analyzer input state.

For an AC-coupled historical-style transient readout, a slow decay can be distorted by the high-pass network. The amplifier transfer must therefore be measured with a detector-equivalent source impedance.

The Rajaduray thesis proves that **AC coupling was present** in that UWA branch; it does not disclose the recovered capacitor/resistor values or amplifier model. Those remain `OPEN-HISTORICAL`.

---

## 9. Frequency-domain sweep

### Qualification grid

Begin wide enough to identify low-frequency thermal/high-pass effects and the first detector rolloff:

- ~10–100 Hz where source/readout allow;
- include 1 kHz;
- extend through 10 kHz, 100 kHz, 1 MHz;
- continue to at least 5–10× the observed detector `f_3dB` where external hardware permits.

This is a project qualification grid, not a historical RP-01 sweep.

Kruse's broad `<=10^-7 s` historical PC response-time benchmark would correspond to a first-order `f_3dB >= ~1.59 MHz`, but this is **not** an RP-01 acceptance criterion.

### Acquisition

At each frequency store reference amplitude/phase, DUT amplitude/phase, detector current/power/T and repeatability statistics.

Normalize only after external de-embedding.

---

## 10. One-pole model test

For

`H_1(f)=1/(1+i2πf tau)`

`|H_1|=1/sqrt(1+(2πf tau)^2)`

`phi=-atan(2πf tau)`

and

`f_3dB=1/(2πtau)`.

A one-pole fit is accepted only when:

- amplitude and phase support the same `tau`;
- residuals show no systematic second-pole/zero structure;
- `tau` is stable to reasonable fit-window/range changes;
- external transfer uncertainty is sufficiently smaller than the resolved detector feature;
- excitation-amplitude reduction does not change the fitted pole;
- package thermal response is negligible in the fitted range or separately modeled/de-embedded.

Otherwise report `tau_eff` descriptively or use a higher-order/physical model.

---

## 11. Multi-pole interpretation

A diagnostic two-pole model is

`H_2(f)=1/[(1+i2πf tau_1)(1+i2πf tau_2)]`.

Do not assign pole identities merely by ordering their time constants.

Possible remaining mechanisms after external electrical/source calibration include:

- bulk recombination;
- surface recombination;
- interface trapping/de-trapping;
- transport/sweepout;
- contact recombination;
- spatially nonuniform generation/field;
- residual device RC;
- package/bondline thermal response.

The Gopal/Pal interface-trap papers prove that delayed/non-exponential PC structure can be real semiconductor-interface physics. The Bartoli HgCdTe PC paper proves that slow assembly/bondline recovery can also be real. Distinguishing them requires discriminating experiments, not curve-labeling.

---

## 12. Time-domain transient method

Use an optical pulse whose measured waveform is sufficiently short relative to the carrier/process time scale being estimated.

For an ideal one-exponential decay after excitation ends:

`V(t)=V0 exp(-t/tau)+V_offset`.

### Fit-window rule

Do not force the fit to begin at the optical pulse edge when the early response contains:

- finite source-pulse tail;
- high-injection/Auger behavior;
- amplifier overload/recovery;
- ringing;
- bandwidth limitation;
- trapping or delayed release;
- contact/sweepout transient;
- mixed spatial diffusion modes.

Store the fit start/end and demonstrate stability to reasonable perturbation.

### Same-UWA historical branch

The 1998 UWA implementation provides a concrete acquisition example:

- `25 ns` optical pulse at `1.047 µm`;
- `1 kHz` repetition;
- HP54522A acquisition;
- 500 points spaced `20 ns` -> nominal stored record of about `10 µs` across 500 intervals/points, depending on endpoint convention;
- typically 128 waveform averages per coordinate;
- non-exponential and single-exponential models were both tested; the non-exponential model performed better for the analyzed spatial-lifetime dataset.

Do **not** automatically reuse the 20-ns/500-point/128-average settings. They are historical same-UWA anchors. A local setup chooses sampling and record length from the expected dynamics and independently characterized instrumentation.

---

## 13. HP54522A historical instrument state

Official Keysight legacy documentation identifies the HP54522A as a two-channel digitizing oscilloscope with:

- 500-MHz analog bandwidth;
- up to 2 GSa/s sample rate;
- 32-k acquisition memory/channel;
- sequential single-shot capability.

These are instrument capabilities, **not proof of the Rajaduray acquisition settings beyond the settings explicitly stated in the thesis**.

The thesis itself directly closes the stored transient spacing/count (`20 ns`, 500 points) and averaging (`128` typical), but the following remain open:

- input range;
- coupling/termination at the oscilloscope;
- trigger level and delay;
- vertical scaling;
- acquisition mode;
- scope firmware/version;
- any internal filtering.

Local reproduction shall calibrate the complete impulse/step response regardless of instrument model.

---

## 14. Package thermal separation

P33 is mandatory context whenever a P13 waveform contains millisecond or slower structure, or when optical/bias energy could heat the detector assembly.

Bartoli et al. show that HgCdTe PC packages can produce:

- several-millisecond recovery;
- hundred-millisecond recovery;
- dependence on optical power density and irradiation duration;
- time constants associated with bonding layers rather than carrier recombination.

### Required discriminating tests

Where a slow component is observed:

1. vary optical pulse energy/irradiation duration at fixed carrier-sensitive conditions;
2. compare optical heating with electrical Joule-heating impulse where possible;
3. vary bias duty at fixed peak field;
4. compare package temperature/resistance proxy response;
5. use P33 `H_pkg,thermal` or thermal impulse kernel;
6. repeat after package/attach changes where available.

A pole that follows package/heating variables must not be labeled intrinsic carrier lifetime.

Timescale separation is useful but not sufficient by itself.

---

## 15. Rise-time / first-order bandwidth relation

For a validated first-order step response:

`t_10-90 = tau ln(9) ≈ 2.1972 tau`

`tau=t_10-90/ln(9)`

`f_3dB≈0.3497/t_10-90`.

Do not use these formulas for a multi-pole or source-limited waveform.

---

## 16. Lifetime terminology

In general

`tau_eff != tau_bulk`.

Use:

- `tau_eff` — measured effective device time constant;
- `tau_decay` — fitted time-domain decay constant;
- `tau_freq` — frequency-domain equivalent only after validated model;
- `tau_bulk` — only when bulk minority-carrier lifetime interpretation is independently justified;
- `tau_surface/interface` — only from a model/experiment capable of separating that contribution;
- `tau_pkg,thermal` — package/thermal time scale.

Do not call a measured decay “lifetime” solely because it is exponential.

---

## 17. Field dependence / sweepout test

Repeat at multiple fields within the P10/P10A self-heating-safe region.

Include:

- a low-field lifetime-oriented state;
- the RP-01 detector-performance benchmark near 10 V/cm where relevant;
- a higher safe field where justified.

For each state record low-frequency responsivity, `f_3dB`, `tau_eff`, phase, current/power/T, duty and noise where available.

### Same-UWA historical lesson

The Rajaduray thesis intentionally reduced bias to prevent photocarriers being swept into high-recombination contacts. This directly validates a P13 requirement: before interpreting a decay as material lifetime, reduce field until the fitted decay is invariant within uncertainty or explicitly model transport/contact loss.

The thesis branch's `-1.05 V` value is sample-geometry-specific and **must not** be converted into an RP-01 field without its actual active geometry.

---

## 18. Wavelength dependence

Repeat at more than one in-band wavelength where practical because absorption depth changes spatial weighting of surface/bulk/contact transport.

The UWA transient branch used `1.047 µm`, which is a strong near-surface excitation for `x≈0.30` HgCdTe at 77 K. It therefore should not be assumed to weight the active volume identically to a 4-µm RP-01 signal.

A 1.047-µm transient lifetime and a 4-µm detector-response time are related diagnostics, not automatically identical observables.

---

## 19. Temperature dependence

Repeat selected measurements around the intended operating temperature.

Temperature dependence helps discriminate recombination, interface trapping, mobility/transport and thermal artifacts. Do not infer activation energies without adequate range/model.

---

## 20. Time/frequency-domain consistency

When both methods are available compare:

`tau_freq = 1/(2π f_3dB)`

with `tau_decay` and phase-derived `tau`.

A strong single-pole detector should agree within combined uncertainty. Disagreement is diagnostic and must not be averaged away.

---

## 21. Coupling to P11/P12

P11/P12 use the historical 1-kHz signal condition.

P13 must establish whether 1 kHz lies on the low-frequency detector-response plateau after source/electrical/package correction.

If

`|H_det(1 kHz)|/|H_det(f->0)| ≈ 1`

within uncertainty, dynamic attenuation at 1 kHz is negligible.

Otherwise P11/P12 must state that the 1-kHz responsivity/D* includes temporal attenuation.

P13 does not alter the P12 rule that responsivity and noise be compared at the same signal frequency and state.

---

## 22. Required plots

Every released P13 dataset should include where applicable:

1. measured and source-reference transient;
2. de-embedded normalized amplitude vs log frequency;
3. de-embedded phase vs log frequency;
4. model overlay and residuals;
5. `f_3dB` indication;
6. `tau_eff` vs field;
7. waveform/time constant vs injection level;
8. corrected time-domain decay with fit window marked;
9. package thermal impulse/recovery trace or a documented negligible-package gate;
10. time/frequency consistency comparison.

---

## 23. Required raw-data fields

- device/wafer/package/contact-pair ID;
- date/operator;
- optical source ID, wavelength, pulse/modulation state;
- measured source waveform/reference detector;
- pulse width/repetition/fluence or modulation depth;
- beam spot/profile/location;
- detector T;
- P10A `V_contact`, E, I, P and duty;
- background/FOV/window;
- frequency or transient time base;
- preamp gain/phase/input impedance calibration;
- AC-coupling/bias-network transfer;
- cable/termination;
- instrument model/serial/range/coupling;
- sample rate, record length, averaging;
- P33 package thermal-kernel reference;
- raw waveforms/complex response;
- fit model/version/window;
- residuals/statistical metrics;
- uncertainty components.

---

## 24. Failure modes / red flags

Do not release intrinsic lifetime/bandwidth when unresolved:

- observed pole coincides with source, AC-coupling, preamp, cable or instrument response;
- package thermal pole is not measured/excluded;
- response or fitted tau depends materially on optical injection level;
- local pulse creates high-level injection while a low-injection lifetime is claimed;
- amplitude and phase imply incompatible tau;
- detector temperature changes with bias/frequency/duty;
- transient is fit through source pulse or amplifier overload;
- delayed/trap peaks or multi-exponential structure are ignored;
- cable ringing/reflections contaminate response;
- low-frequency normalization lies inside a high-pass or thermal transient;
- bandwidth is quoted without source-reference normalization;
- 1.047-µm near-surface decay is automatically relabeled as 4-µm detector response;
- `-1.05 V` from the Rajaduray sample is imported as an RP-01 field/setpoint.

---

## 25. Current RP-01 historical status

The RP-01 2001 paper specifies a 1-kHz chopped spectral-response condition but does not publish a detector frequency-response curve or directly measured RP-01 lifetime/time constant in the audited text.

Therefore:

- historical RP-01 `tau` = `OPEN`;
- historical RP-01 `f_3dB` = `OPEN`;
- exact RP-01 transient apparatus = `NOT REPORTED`;
- same-UWA 1998 `x≈0.30` transient apparatus is now strongly documented and is the best historical methodology branch;
- the 1999 Redfern/Musca/Smith/Dell/Faraone conference paper is positively identified but full experimental text remains unrecovered through current routes;
- Kruse response time remains a broad benchmark only.

P13 shall generate/qualify the temporal behavior of a reconstructed RP-01 device rather than fabricate a historical value.

---

## 26. Release blockers / future qualification

Before production-like release define from actual detector data:

- minimum required `f_3dB`;
- maximum dynamic attenuation at 1 kHz;
- accepted disagreement among amplitude-, phase- and transient-derived tau;
- injection-level range for linear operation;
- field range before sweepout/heating changes `tau_eff`;
- package-thermal separation criterion;
- repeatability across remounts/devices/days.

Historical source-recovery priorities:

1. full Redfern et al. 1999 conference paper;
2. any UWA transient apparatus drawing/software referenced by Rajaduray;
3. exact laser model and pulse-energy/spot calibration;
4. Keithley current-source model/current setting and sample contact geometry;
5. AC-coupled amplifier circuit/gain/bandwidth;
6. original HP54522A setup/trigger/termination;
7. any RP-01-device transient measurement not yet indexed.

No numerical production tolerances are released until repeated local data exist.
