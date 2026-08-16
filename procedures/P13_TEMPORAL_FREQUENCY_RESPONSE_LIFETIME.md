# P13 — temporal response / frequency response / lifetime / bandwidth

**Status:** CONTROLLED QUALIFICATION METHOD — not yet a production release criterion.

## 1. Purpose

Measure the dynamic response of an RP-01-type HgCdTe photoconductor while separating intrinsic detector dynamics from source modulation, optical-path modulation, bias network, preamplifier, cabling, lock-in/analyzer and digitizer response.

The method must determine, when justified:

- normalized amplitude response |H_det(f)|;
- detector phase response phi_det(f);
- -3 dB frequency f_3dB;
- rise/fall or transient decay constants;
- whether a one-pole model is adequate;
- effective detector time constant tau_eff;
- whether tau_eff can legitimately be interpreted as an excess-carrier lifetime;
- field dependence of temporal response and evidence for transit/sweepout effects;
- evidence for multiple recombination/trapping/interface time scales.

Do **not** fold temporal response into conventional D* unless a separately defined generalized metric is introduced.

---

## 2. Provenance / physical basis

### P13-S1 — Kruse 1965

P. W. Kruse, “Photon Effects in Hg1−xCdxTe,” *Applied Optics* 4, 687–692 (1965), DOI `10.1364/AO.4.000687`.

Primary historical HgCdTe detector study. Photoconductive response-time measurements at 77 K were reported no greater than about 10^-7 s for the devices studied. This is a broad historical benchmark, not an RP-01-specific time constant.

### P13-S2 — Elliott et al. 1978 recombination study

“Recombination in cadmium mercury telluride photodetectors,” *Solid-State Electronics* 21, 1475–1480 (1978), DOI `10.1016/0038-1101(78)90228-9`.

Shows that carrier lifetime is a central determinant of HgCdTe detector performance and that dominant recombination mechanisms vary with band gap/composition; photoconductive decay was used experimentally.

### P13-S3 — Musca/Faraone lineage: interface/trap transient behavior

“Study of the traps at a mercury cadmium telluride–anodic oxide interface using a transient photoconductive decay technique,” *Journal of Crystal Growth* 265, 530–536 (2004), DOI `10.1016/j.jcrysgro.2004.02.082`.

Demonstrates that HgCdTe transient photoconductive decay can contain non-simple behavior associated with surface/interface traps and bias conditions. The transient response therefore cannot be assumed to be a single exponential a priori.

### P13-S4 — high-injection HgCdTe lifetime work

“Lifetime characterization of n-type HgCdTe under high excess carrier density conditions,” OSA technical meeting paper (1992).

Reports departures from exponential decay under high excess-carrier injection. Low-injection conditions are therefore mandatory if the aim is a small-signal linear transfer function/lifetime.

### P13-S5 — modern MWIR HgCdTe PC lifetime example

“Minority carrier lifetime in HgCdTe(100) epilayers and their potential application to background radiation limited MWIR photodiodes,” *Semiconductor Science and Technology* (2021), DOI `10.1088/1361-6641/abea6d`.

A room-temperature HgCdTe(100) photoconductor with x≈0.325 and 5.3-µm active layer was measured by transient optical excitation; an approximately 8.52-µs decay constant was obtained after excluding the initially distorted portion. This is a useful methodological example showing that the fit window matters; it is not a numerical RP-01 target.

---

## 3. Core rule: detector response must be de-embedded

The measured complex transfer function is generally

`H_meas(f) = H_source(f) H_optics(f) H_detector(f) H_bias(f) H_preamp(f) H_cable(f) H_instrument(f)`.

Therefore

`H_detector(f) = H_meas(f) / H_external(f)`

only where the external transfer function is independently measured with adequate signal-to-noise ratio and phase reference.

A measured -3 dB point is **not** a detector bandwidth if an external element has comparable bandwidth.

---

## 4. Required apparatus classes

The released setup must include or document equivalents of:

1. cryostat/cold finger capable of holding the RP-01 detector near 80 K;
2. temperature sensor mounted sufficiently close to the detector to bound detector temperature;
3. stable DC bias source and bias network from P10;
4. in-band optical source with controllable small-signal modulation;
5. optical attenuator set or source-current control for injection-linearity checks;
6. reference photodetector with calibrated bandwidth substantially above the test range;
7. function generator / RF source / modulation driver;
8. low-noise wideband preamplifier or transimpedance/voltage readout whose transfer function can be calibrated;
9. lock-in amplifier, network analyzer, spectrum analyzer, digitizer or equivalent complex-response instrument;
10. calibrated oscilloscope/digitizer for transient measurements where used;
11. calibrated cabling/terminations appropriate to the selected bandwidth;
12. optical beam monitoring method or beamsplitter/reference channel when source drift is non-negligible.

Specific instrument models are not released yet because P13 is intended to be apparatus-transferable.

---

## 5. Operating condition to record

Every temporal-response dataset must carry:

- device ID;
- active width and measured contact gap;
- active-layer thickness;
- detector temperature;
- active-region electric field `E` from P10;
- detector current and dissipated power;
- optical wavelength or source spectrum;
- mean optical irradiance/power at detector;
- modulation depth;
- background/FOV state;
- preamplifier gain and load configuration;
- cable/termination configuration;
- source modulation method;
- frequency grid;
- acquisition bandwidth/integration time/averaging.

Changing E, optical power, or temperature defines a new dynamic operating condition.

---

## 6. Low-injection linearity gate

Before extracting a transfer function, verify small-signal operation.

At one low frequency well below all suspected poles:

1. hold detector T and E fixed;
2. vary modulated optical amplitude over at least 3 levels spanning a practical factor of at least ~4 in modulation amplitude;
3. record fundamental detector response amplitude;
4. fit response versus modulation amplitude;
5. examine harmonics if available.

Pass condition for qualification:

- no statistically significant compression within the selected operating region;
- normalized transfer-function shape is unchanged, within uncertainty, when modulation amplitude is reduced.

If apparent lifetime/bandwidth depends on injection level, report this dependence explicitly; do not quote one “carrier lifetime” without excitation state.

---

## 7. External optical-modulation transfer function

### 7.1 Preferred method

Place a reference detector in the same optical plane as the HgCdTe device, or use a simultaneous reference arm whose relative path transfer has been calibrated.

The reference detector bandwidth should preferably exceed the highest test frequency by at least one decade. If that is not practical, its own complex transfer function must be known and included in the de-embedding model.

Measure

`H_opt,meas(f) = V_ref(f) / V_drive(f)`.

This captures modulator/source rolloff and phase delay.

### 7.2 Chopper warning

A mechanical chopper is appropriate for low-frequency responsivity but is generally unsuitable for determining MHz-class intrinsic photoconductor bandwidth. P13 therefore allows a different modulation source than P11/P12, provided detector operating state and optical wavelength/power are explicitly recorded.

---

## 8. Electrical-chain transfer function

Determine the complex transfer of the detector readout independently.

Preferred approaches:

- calibrated small-signal electrical injection at the detector/readout input with an equivalent detector impedance;
- full two-port/network characterization where appropriate;
- reference photodetector substitution through the same readout path when electrically compatible.

Record:

- preamp gain versus f;
- phase versus f;
- input/output loading;
- any AC-coupling high-pass pole;
- cable/termination response;
- instrument anti-alias or demodulator filters.

A nominal manufacturer bandwidth is insufficient for de-embedding unless independently verified over the actual gain/load setting.

---

## 9. Frequency-domain sweep

### 9.1 Qualification grid

For RP-01 process development, begin with a logarithmic sweep broad enough to identify both low-frequency artifacts and the first intrinsic rolloff.

Initial project grid:

- start near 10–100 Hz if the source/readout permits;
- include the historical 1-kHz operating point;
- extend through at least 10 kHz, 100 kHz, 1 MHz;
- continue to at least 5–10 times the observed detector f_3dB when external instrumentation permits.

This is a qualification grid, not a published RP-01 frequency sweep.

Historical context from Kruse 1965 (<=10^-7 s at 77 K for studied HgCdTe PCs) corresponds, for a one-pole system, to

`f_3dB >= 1/(2 pi 100 ns) ≈ 1.59 MHz`.

Treat this only as a broad plausibility benchmark, not as an RP-01 acceptance value.

### 9.2 Acquire complex response

At each frequency record:

- source/reference amplitude and phase;
- detector output amplitude and phase;
- detector DC current and temperature;
- repeat/uncertainty metric.

Normalize the detector response to the low-frequency plateau only after external de-embedding.

---

## 10. One-pole model test

For a first-order detector response,

`H_1(f) = 1 / (1 + i 2 pi f tau)`.

Then

`|H_1(f)| = 1 / sqrt(1 + (2 pi f tau)^2)`

and

`phi_1(f) = -atan(2 pi f tau)`.

The -3 dB frequency is

`f_3dB = 1/(2 pi tau)`.

### 10.1 Acceptance before calling tau a one-pole time constant

A one-pole fit is allowed only when:

- amplitude and phase are simultaneously consistent with the same tau over the fitted range;
- residuals do not show systematic curvature indicating another pole/zero;
- extracted tau is stable when the fit range is changed reasonably;
- the external-chain de-embedding uncertainty is small enough that the detector pole is resolved;
- tau is independent of small-signal modulation amplitude within the selected linear regime.

If these conditions fail, report `tau_eff` only as a descriptive fitted parameter or use a higher-order/physical model.

---

## 11. Two-pole / multi-pole model

A common diagnostic model is

`H_2(f) = 1 / [(1 + i 2 pi f tau_1)(1 + i 2 pi f tau_2)]`.

Do not automatically identify tau_1 and tau_2 with “detector lifetime” and “electronics lifetime.” External electronics should already have been de-embedded. Remaining poles may arise from:

- bulk excess-carrier recombination;
- surface/interface recombination/trapping;
- transit or sweepout;
- spatially nonuniform field/photogeneration;
- contact-region dynamics;
- thermal response;
- residual parasitic RC effects not captured by the calibration model.

Model selection should use both physical plausibility and residual improvement, not only a lower least-squares error.

---

## 12. Time-domain transient method

Use a pulsed optical source with pulse width/rise time substantially shorter than the expected detector response.

Measure the optical pulse waveform with the reference detector and deconvolve/instrument-correct when necessary.

For an ideal single exponential decay after the excitation ends,

`V(t) = V0 exp(-t/tau) + V_offset`.

### Fit-window rule

Do not force the fit to begin at the pulse edge if the early waveform is distorted by:

- source pulse tail;
- amplifier recovery/saturation;
- high-injection recombination;
- ringing;
- bandwidth limitation;
- trap-related transient structure.

Record the exact fit window and demonstrate fit stability to reasonable changes in its start/end times.

The 2021 HgCdTe MWIR study explicitly excluded an initially distorted portion before obtaining its reported decay constant; P13 adopts this as a methodological warning rather than copying its numerical lifetime.

---

## 13. Relation between rise time and one-pole bandwidth

For an ideal first-order step response, 10–90% rise time is

`t_10-90 = tau ln(9) ≈ 2.1972 tau`.

Therefore

`tau = t_10-90 / ln(9)`

and

`f_3dB ≈ 0.3497 / t_10-90`.

Use these relations only for a validated first-order response.

---

## 14. Lifetime versus effective device time constant

Even when a single detector pole exists,

`tau_eff != tau_bulk`

in general.

The measured effective time constant can include surface recombination, contact recombination, trapping, carrier transport and spatial device effects. Only call tau_eff a **minority-carrier lifetime** when device geometry, injection regime and physical model justify that identification.

Use terminology:

- `tau_eff` — measured effective detector time constant;
- `tau_decay` — time-domain fitted decay constant;
- `tau_bulk` — bulk excess-carrier lifetime only when independently justified;
- `tau_surface/interface` — only from a model/experiment capable of separating the surface contribution.

---

## 15. Field dependence / sweepout test

RP-01 is a biased photoconductor. Repeat the frequency-response measurement at several electric fields within the P10 self-heating-safe region.

At minimum include:

- low field;
- the historical benchmark near 10 V/cm;
- one higher safe field if P10 allows it.

For each field record:

- low-frequency responsivity;
- f_3dB;
- tau_eff;
- phase fit;
- detector current and power;
- self-heating indicator;
- P12 noise at the relevant signal frequency when available.

Interpretation:

- field-independent tau with field-dependent gain may support a recombination-dominated time scale;
- systematic shortening of tau with field can indicate transport/sweepout or field-modified recombination/contact behavior;
- apparent bandwidth increase accompanied by measurable heating must not be labeled intrinsic sweepout without thermal correction.

---

## 16. Wavelength dependence

Where practical, repeat temporal response at more than one wavelength within the active band.

Reason: absorption depth and photogeneration profile vary with wavelength and can alter the spatial weighting of bulk, surface and contact transport.

A wavelength-independent response is useful evidence for a lumped effective model but is not required a priori.

---

## 17. Temperature dependence

During material/device qualification, repeat at multiple temperatures around the intended 80-K operating point where apparatus permits.

Record actual detector T and thermal stability.

Temperature dependence can help distinguish:

- recombination-limited behavior;
- trap/interface activation;
- mobility/transport effects;
- thermal/readout artifacts.

Do not infer an activation energy unless the temperature range and model support it.

---

## 18. Consistency between time and frequency domains

When both methods are available, compare:

`tau_freq = 1/(2 pi f_3dB)`

against

`tau_decay`

and against phase-derived tau.

A strong single-pole detector should give mutually consistent values within combined uncertainty.

Disagreement is diagnostic and must be investigated rather than averaged away.

---

## 19. Coupling to P11/P12

P11 spectral responsivity and P12 noise/detectivity use a 1-kHz historical benchmark.

P13 must explicitly determine whether 1 kHz lies on the low-frequency responsivity plateau.

If

`|H_det(1 kHz)| / |H_det(f->0)| ≈ 1`

within measurement uncertainty, then the 1-kHz responsivity is not materially attenuated by detector bandwidth.

If not, P11/P12 results must state that the reported 1-kHz responsivity/D* includes dynamic attenuation.

P13 does **not** alter the P12 rule that responsivity and noise must be compared at the same signal frequency.

---

## 20. Required plots

Every released P13 dataset should contain at least:

1. de-embedded normalized amplitude versus log frequency;
2. de-embedded phase versus log frequency;
3. selected model fit overlaid on both;
4. fit residuals;
5. f_3dB indication;
6. tau_eff versus electric field;
7. low-frequency response versus optical modulation amplitude (linearity gate);
8. if time-domain data exist: corrected transient with fit window explicitly marked.

---

## 21. Required raw-data fields

- sample/device ID;
- date/operator;
- optical source ID and wavelength/spectrum;
- source driver settings;
- reference detector ID/calibration/bandwidth;
- optical attenuation state;
- detector T;
- field E and measured V_active;
- detector current/power;
- frequency;
- reference amplitude/phase;
- detector amplitude/phase;
- preamp gain/phase calibration reference;
- cable/termination state;
- averaging/integration settings;
- transient sampling rate and record length where applicable;
- all fit model/version/parameter values;
- residual/statistical metrics;
- uncertainty components.

---

## 22. Failure modes / red flags

Do not release a lifetime/bandwidth value when any of the following is unresolved:

- observed pole coincides with preamplifier or modulator bandwidth;
- response depends strongly on optical modulation amplitude in the alleged small-signal regime;
- phase and amplitude imply incompatible tau values;
- detector temperature changes materially with frequency/bias condition;
- transient waveform is fit through source-pulse or amplifier saturation;
- multiple exponential components are visually/systematically present but ignored;
- cable reflections/ringing contaminate the measurement;
- low-frequency normalization is itself inside a high-pass or thermal transient region;
- bandwidth is quoted from output amplitude without source-reference normalization.

---

## 23. Current RP-01 historical status

The RP-01 2001 paper specifies a 1-kHz chopped spectral-response condition but does not, in the currently audited text, publish a detector frequency-response curve or a directly measured RP-01 lifetime/time constant.

Therefore:

- no historical RP-01 `tau` is currently closed;
- no historical RP-01 `f_3dB` is currently closed;
- Kruse’s <=10^-7-s 77-K result is only a broad HgCdTe PC historical benchmark;
- P13 will generate the temporal benchmark for a reconstructed RP-01 device rather than fabricate one from unrelated material.

---

## 24. Release criteria still to be established

After actual RP-01-compatible devices are measured, the project must define numerical process acceptance windows for:

- minimum detector f_3dB;
- maximum allowable spread across devices/wafer;
- allowed mismatch between amplitude-, phase- and transient-derived tau;
- allowed field dependence before sweepout/heating investigation is required;
- maximum dynamic attenuation at the canonical 1-kHz P11/P12 condition.

These remain `[QUAL]` until device statistics exist.
