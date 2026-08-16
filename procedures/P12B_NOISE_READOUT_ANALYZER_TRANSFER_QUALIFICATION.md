# P12B — detector-noise readout / analyzer transfer qualification

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. Historical RP-01 preamplifier and HP35665A settings remain open; this procedure defines a traceable detector-referred noise measurement that can reproduce the physical quantity without guessing those settings.

## 1. Purpose

Qualify the complete electrical chain used to measure RP-01-type HgCdTe photoconductor noise:

`biased detector -> bias/readout network -> low-noise preamplifier -> dynamic signal/spectrum analyzer`.

The procedure must establish detector-referred voltage-noise spectral density and its uncertainty while separating:

- detector noise;
- bias-network noise;
- preamplifier voltage/current noise;
- gain/frequency-response effects;
- analyzer input noise;
- FFT/window/averaging normalization.

## 2. Historical RP-01 anchor

Direct RP-01 noise condition:

- detector temperature `80 K`;
- electric field `10 V/cm`;
- low-noise preamplifier;
- HP35665A spectrum analyser;
- plotted result described as an **averaged noise-voltage spectrum**;
- 1/f knee approximately `3 kHz`;
- generation–recombination plateau approximately `24.5 nV/√Hz`.

The historical preamp model/circuit, gain, RBW/ENBW/window and averaging count are not stated.

Therefore these values remain historical performance anchors, not enough information to reproduce the exact instrument setup.

## 3. Official HP35665A capability

Keysight's official legacy documentation identifies the HP/Agilent 35665A as a two-channel dynamic signal analyzer capable of measurements including:

- linear spectrum;
- power spectral density;
- cross spectrum;
- frequency response;
- time waveform/correlation functions.

Official product information gives:

- up to `102.4 kHz` single-channel analysis bandwidth;
- up to `51.2 kHz` dual-channel bandwidth;
- selectable `100, 200, 400, 800` lines of resolution.

This confirms that the instrument class is fully capable of direct PSD/frequency-response characterization, but it does not recover the specific settings used in Figure 5.

## 4. Core reporting quantity

The preferred detector noise result is detector-terminal voltage ASD:

`e_det(f) = sqrt(S_v,det(f))` in `V/√Hz`.

Do not derive an ASD by dividing arbitrary displayed RMS volts by `sqrt(RBW)` unless the analyzer's actual noise-equivalent bandwidth and processing convention are known.

Preferred approaches are:

1. instrument-reported PSD/ASD with independent calibration verification; or
2. raw time-domain acquisition + documented FFT/window normalization.

## 5. Complete chain model

For a linear voltage preamplifier, measured analyzer-input PSD can be represented as

`S_meas(f) = |G(f)|² [ S_det,loaded(f) + S_pre,in(f; Z_s) + S_bias,in(f) ] + S_an,in(f)`

where:

- `G(f)` = complex preamplifier/readout gain;
- `S_det,loaded` = detector noise after electrical loading by bias/readout network;
- `S_pre,in(f;Z_s)` = preamp input-referred noise for actual source impedance;
- `S_bias,in` = bias-network equivalent input noise;
- `S_an,in` = analyzer input contribution.

Detector PSD is obtained by subtracting **independent PSD contributions**, never ASDs linearly:

`S_det = S_total - S_electronics`

only where independence/linearity assumptions are justified.

Then

`e_det = sqrt(max(S_det,0))`.

## 6. Detector-equivalent source-impedance calibration

Preamplifier noise depends on source impedance through voltage noise, current noise and Johnson noise.

Therefore electronics-floor characterization shall include at least:

1. input short / near-zero source impedance;
2. one or more precision resistors bracketing the detector's operating differential resistance;
3. the actual bias-network configuration;
4. preferably a cryogenic/dummy detector-equivalent impedance when capacitance/parasitics are important.

For each resistance calculate expected Johnson ASD:

`e_J = sqrt(4 k_B T R)`

using the resistor's actual temperature.

The measured increase versus resistance is an end-to-end calibration of the readout/noise normalization.

## 7. Gain calibration

Measure `G(f)` over a range broader than the detector-noise band.

Preferred method:

- inject a calibrated low-level AC voltage through a source impedance equivalent to the detector;
- sweep frequency logarithmically;
- record analyzer input/output ratio and phase;
- repeat at every preamplifier gain setting used for detector data.

Required outputs:

- gain magnitude;
- phase;
- -3 dB points;
- high-pass/AC-coupling pole(s);
- gain flatness across the 1/f and g-r analysis band;
- uncertainty.

A nominal front-panel gain is insufficient.

## 8. Bias-network loading calibration

The detector is biased while noise is measured. The bias circuit can alter both operating field and measured noise.

Record/model:

- bias source;
- series/load resistor(s);
- coupling capacitor(s);
- bypass/filter components;
- detector differential resistance;
- input impedance of the preamp;
- cable capacitance.

Calculate/measure the transfer from intrinsic detector-terminal noise to preamplifier input.

If the readout does not have effectively infinite input impedance, report the loading correction explicitly.

## 9. Analyzer PSD normalization calibration

Regardless of whether an HP35665A or a modern equivalent is used, verify the selected PSD/ASD display mode with a traceable white-noise source or resistor noise.

Recommended calibration:

1. connect a precision resistor of known R and measured T through the actual input chain;
2. predict Johnson PSD `4kTR`;
3. acquire spectra using the intended analyzer settings;
4. compare measured detector-referred PSD to theory over the flat band;
5. repeat for at least two resistance values;
6. document residual normalization error versus frequency.

This simultaneously catches errors in gain, ENBW/window scaling and units.

## 10. FFT/window/ENBW record

Every noise dataset must record:

- measurement type (`PSD`, spectrum, ASD, etc.);
- time-record length or frequency span;
- number of FFT lines / frequency-bin spacing;
- window type;
- analyzer definition of PSD/ASD;
- equivalent noise bandwidth if needed for the selected mode;
- overlap;
- averaging type;
- averaging count;
- linear versus logarithmic averaging;
- detector/peak/RMS processing if applicable.

Do not state only “RBW.” FFT analyzers couple window and record length to effective noise bandwidth.

## 11. Averaging qualification

An averaged spectrum is not fully specified by average count alone.

During method qualification:

- compare multiple averaging counts;
- verify that mean PSD is stable while statistical scatter decreases as expected;
- distinguish power/PSD averaging from magnitude/voltage averaging;
- preserve enough independent records to estimate uncertainty/confidence intervals.

Averaging must not suppress genuine intermittent/nonstationary detector noise without being reported.

## 12. Stationarity check

Before reporting a PSD, acquire time-domain records long enough to detect:

- drift;
- burst noise;
- microphonics;
- intermittent contact noise;
- environmental line pickup;
- bias instability.

If the process is nonstationary, report time-resolved/statistical behavior rather than treating one averaged PSD as complete.

## 13. Environmental line rejection

Identify and annotate narrow spectral components due to:

- mains frequency/harmonics;
- pump/compressor vibration;
- chopper/modulator leakage;
- digital clocks;
- RF interference.

Do not interpolate through these bins silently when fitting 1/f or g-r noise.

The detector-noise fit region and excluded bands must be saved with the analysis.

## 14. Electronics floor subtraction rule

Acquire electronics-floor spectra under the same:

- gain;
- analyzer settings;
- source impedance state;
- bias network;
- cable configuration;
- shielding/grounding;

as the detector measurement.

Subtract only in PSD:

`S_detector = S_total - S_floor`.

If `S_total/S_floor` is too close to unity for stable subtraction, report an upper bound / electronics-limited result rather than a negative or highly uncertain detector PSD.

## 15. Two-channel cross-spectrum option

The HP35665A supports two-channel/cross-spectrum measurements. A modern or legacy two-channel implementation may be used to suppress uncorrelated amplifier noise if two independent preamplifier channels can observe the same detector voltage without materially loading it.

This is a **local enhancement**, not a claim about RP-01.

If used:

- independently characterize each channel;
- verify negligible cross-talk;
- retain complex cross-spectrum;
- quantify convergence versus number of averages;
- ensure both channels see the same detector operating state.

## 16. Required operating-condition lock to P10/P11/P12

For a reported RP-01-like detector spectrum record:

- detector ID;
- T;
- measured active gap;
- active-region field;
- detector current/power;
- optical/background/FOV state;
- packaging/cryostat state;
- preamp gain/configuration;
- analyzer configuration.

For D*, evaluate detector noise at the same signal frequency used for responsivity unless an alternate convention is explicitly declared.

## 17. Historical 1-kHz ambiguity remains

RP-01 reports:

- responsivity chopping at `1 kHz`;
- 1/f knee near `3 kHz`;
- g-r white/plateau level near `24.5 nV/√Hz`.

Therefore 1 kHz lies below the reported knee.

Do not insert the 24.5-nV/√Hz high-frequency plateau into the 1-kHz spectral D* calculation unless the historical authors' convention is recovered or a figure-data reconstruction demonstrates it.

For new measurements, directly measure `e_n(1 kHz)` under the same operating state as `R(1 kHz)`.

## 18. Minimum calibration acceptance

Before detector data are considered traceable, demonstrate:

- gain calibration residual within the local uncertainty budget over the analysis band;
- Johnson-noise test agrees with prediction within combined uncertainty;
- analyzer PSD normalization is frequency-independent over a white-noise reference band;
- electronics floor is sufficiently below detector noise over the bands used for detector fitting, or the electronics limitation is explicitly reported;
- repeated spectra are statistically consistent for a stationary reference source.

Numerical percentage thresholds should be frozen after instrument uncertainty and target D* precision are defined.

## 19. Historical acquisition target

The highest-value archival item remains:

`J. F. Siliquini, Ph.D. thesis, University of Western Australia, 1995`.

Later UWA work cites this thesis specifically for the custom bias-capable low-noise voltage preamplifier.

If acquired, compare the historical circuit against the local P12B chain and determine whether exact historical transfer can be recreated.

## 20. Release conclusion

The historical RP-01 electronics cannot yet be reproduced controller-for-controller.

The **physical noise measurement can**, however, be made more traceably than the original paper specifies by calibrating the complete detector/readout/analyzer chain and storing all PSD-processing parameters.

P12B is therefore the preferred local route until the Siliquini thesis or an equivalent UWA electronics source is recovered.
