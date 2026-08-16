# P13A — UWA same-lineage transient-decay experimental addendum

**Status:** SAME-LAB / THESIS-LEVEL PROCESS EVIDENCE. Supplements `P13_TEMPORAL_RESPONSE_FREQUENCY_LIFETIME_BANDWIDTH.md`.

## 1. Purpose

Record direct UWA experimental details from a 1998 honours thesis supervised by John M. Dell, with acknowledged assistance from David Redfern and E. P. G. Smith, that materially support the P13 operating-condition and sweepout-control logic for n-type x≈0.30 HgCdTe.

## 2. Source

Ramesh Rajaduray, *Investigation of Spatial Characterisation Techniques in Semiconductors*, Bachelor of Engineering (Honours) thesis, Department of Electrical and Electronic Engineering, University of Western Australia, 1998. Supervisor: Dr John M. Dell.

The thesis explicitly acknowledges experimental assistance/advice from David Redfern and Ed Smith and support from Lorenzo Faraone. This places the work in the immediate UWA detector-characterisation lineage surrounding RP-01.

## 3. Material / sample state

The transient-photoconductive-decay experiments used:

- LPE-grown n-type HgCdTe top layer;
- nominal `x≈0.30`;
- wider-bandgap buffer/substrate below the active layer;
- wet-etched test region using Br2/HBr;
- indium contacts pressed onto opposite ends of the sample;
- measurements at approximately `77 K` under vacuum.

The thesis sample is not asserted to be the RP-01 wafer and its buffer/substrate details are not fully identified. Treat this as same-laboratory methodology evidence, not a direct RP-01 device recipe.

## 4. Instrumentation disclosed

The thesis gives the following experimental hardware classes/details:

- Keithley variable-current source for detector bias;
- HP54522A digital oscilloscope for transient acquisition;
- PC-controlled acquisition;
- liquid-nitrogen cooling / cryostat operation;
- pulsed optical excitation for transient photoconductive decay;
- vacuum measurement environment.

These are useful historical UWA metrology anchors. P13 remains instrument-transferable and does not require these exact legacy models.

## 5. High-value field/sweepout statement

The thesis explicitly states that detector/sample bias was kept **small** so that excess photogenerated carriers would not be swept toward the contacts, which are regions of substantially higher recombination.

This directly supports the P13 rule that an apparent decay constant or bandwidth may become field dependent because carrier sweepout/contact recombination changes the effective response.

Therefore, for any lifetime-oriented P13 measurement:

1. establish a low-field condition where the extracted transient is insensitive to further bias reduction within uncertainty;
2. measure the same sample at higher fields separately as a transport/sweepout study;
3. do not call a high-field fitted decay constant a bulk minority-carrier lifetime without a model separating drift/contact effects.

## 6. Spatial-lifetime mapping details relevant to P13

The thesis demonstrates that lifetime extraction can vary with elapsed time and spatial region because diffusion and recombination redistribute excess carriers after excitation. It also reports that a single-exponential description does not necessarily capture all local physics.

This reinforces the following P13 controls:

- retain the raw transient;
- document the fit window;
- test fit-window stability;
- test injection-level dependence;
- compare time-domain and frequency-domain estimates where possible;
- use `tau_eff` unless a bulk-lifetime interpretation is independently justified.

## 7. Numerical values from the thesis — NOT RP-01 acceptance targets

The thesis reports representative x≈0.30 sample lifetime/surface-recombination analyses and spatial variations. These values are specific to its sample and analysis method and must not be imported as RP-01 production limits.

The value of this source to RP-01 is primarily the experimental architecture and explicit sweepout-control logic.

## 8. Provenance classification

- UWA same-laboratory experimental thesis: `[PRIMARY-THESIS / SAME-LAB]`.
- RP-01 historical device condition: **not** established by this thesis.
- P13 field-control rationale: materially strengthened.

## 9. Release implication

P13 should require a **bias-independence check in the low-field lifetime regime** before a measured transient time constant is interpreted as a material lifetime. A separate field-dependent dataset should then quantify sweepout/contact effects.
