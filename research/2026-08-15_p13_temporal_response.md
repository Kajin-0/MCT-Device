# P13 research record — temporal response / lifetime / bandwidth

**Date:** 2026-08-15 America/New_York

## Purpose

Close the dynamic-response measurement architecture for RP-01 without confusing detector lifetime with source, amplifier, RC, trap or transport poles.

## Primary literature findings

### Kruse 1965

P. W. Kruse, “Photon Effects in Hg1−xCdxTe,” *Applied Optics* 4, 687–692 (1965), DOI `10.1364/AO.4.000687`.

- HgCdTe photoconductive response-time measurements at 77 K were reported no greater than ~10^-7 s for the devices studied.
- This is a broad HgCdTe PC historical benchmark only; it is not RP-01-specific.

For an ideal one-pole response, tau=100 ns corresponds to f_3dB≈1.59 MHz.

Derived plausibility check at 1 kHz for tau=100 ns:

- normalized magnitude ≈0.999999803;
- attenuation ≈−1.71×10^-6 dB;
- phase ≈−0.036°.

Therefore a 1-kHz responsivity point would be essentially unattenuated for such a detector. This does **not** prove RP-01 has tau≤100 ns because RP-01 itself does not publish a dynamic measurement.

### Recombination in CdHgTe photodetectors, 1978

*Solid-State Electronics* 21, 1475–1480, DOI `10.1016/0038-1101(78)90228-9`.

- Carrier lifetime is a major determinant of PC detector behavior.
- Dominant recombination mechanism varies with composition/band gap.
- Photoconductive decay was used experimentally.

### HgCdTe anodic-oxide/interface transient work, 2004

*Journal of Crystal Growth* 265, 530–536, DOI `10.1016/j.jcrysgro.2004.02.082`.

- Transient PC decay can show structure associated with surface/interface traps and bias.
- A single exponential must not be assumed a priori.

### High-injection lifetime characterization, 1992

OSA meeting paper, “Lifetime characterization of n-type HgCdTe under high excess carrier density conditions.”

- High excess-carrier injection can produce non-exponential decay.
- P13 therefore requires a small-signal optical-linearity gate before interpreting tau.

### MWIR HgCdTe photoconductor lifetime example, 2021

DOI `10.1088/1361-6641/abea6d`.

- Room-temperature x≈0.325 HgCdTe(100) photoconductor, 5.3-µm active layer.
- Reported time constant ~8.52 µs after excluding an initially distorted portion of the waveform.
- This is a useful fit-window methodological example, not a numerical RP-01 target.

## Core P13 decisions

1. Measured response is a product of source/optics/detector/bias/readout/instrument transfer functions.
2. Detector response must be de-embedded before quoting f_3dB or tau.
3. Amplitude and phase are both required for frequency-domain model validation.
4. For a one-pole detector:
   - H=1/(1+i2πfτ)
   - f_3dB=1/(2πτ)
   - phase=−atan(2πfτ)
5. Use tau=1/(2πf_3dB) only after amplitude and phase support the same one-pole model.
6. A fitted detector time constant is called `tau_eff` unless a physical model justifies identifying it with bulk minority-carrier lifetime.
7. Time-domain transient fits must state the exact fit window and avoid source-pulse/amplifier/high-injection distortion.
8. Low-injection response linearity must be demonstrated by optical-amplitude scaling.
9. Repeat dynamic response versus electric field to distinguish recombination-dominated behavior from sweepout/transport/heating effects.
10. P13 must explicitly determine whether 1 kHz lies on the low-frequency detector plateau before P11/P12 interpret the historical 1-kHz operating point as dynamically unattenuated.

## New procedure

`procedures/P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md`

## Major unresolved RP-01-specific variables

- no historical RP-01 f_3dB currently identified;
- no historical RP-01 tau currently identified;
- exact RP-01 high-frequency readout architecture not published;
- exact dynamic optical source/modulator not published because the 2001 paper only states 1-kHz chopping for spectral responsivity;
- numerical temporal-response production acceptance limits require actual reconstructed-device statistics.

## Next strongest branch after P13

The remaining large end-to-end fabrication holes are now increasingly concentrated in:

- exact lithography/mask processing (resist identity, exposure/developer, mask dimensions);
- die attach / wire-bond / package / cold-finger interface;
- final master process traveler and cross-module acceptance gates.

Before packaging, prioritize recovery of same-UWA/Faraone lithography details if possible because mask geometry and contact spacing feed directly into P10/P11/P12/P13 normalization.
