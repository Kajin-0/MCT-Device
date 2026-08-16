# Source ledger addendum — source-recovery / measurement-chain round 5

**Date:** 2026-08-15 America/New_York

This addendum records the sources used to reconstruct the historical UWA photoconductor noise/readout lineage and to define the local P12B calibration route.

## S-R5-01 — Smith et al. 2001 RP-01 noise measurement re-audit

**Class:** Primary-A  
**Citation:** E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Direct noise-chain anchors:**

- Figure 5 is an **averaged noise-voltage spectrum**;
- detector `80 K`;
- electric field `10 V/cm`;
- low-noise pre-amplifier;
- `HP35665A` spectrum analyser;
- 1/f knee ~`3 kHz`;
- high-frequency g-r noise level ~`24.5 nV/√Hz`.

**Negative result:** the paper does not disclose preamp circuit/model/gain/input noise/loading or HP35665A span/window/RBW/ENBW/averaging count. No electronics citation is attached directly to the Figure-5 sentence.

## S-R5-02 — Hatch et al. 2011 UWA photoconductor measurement lineage

**Class:** Primary-A / same institution and photoconductor measurement lineage.  
**Citation:** S. D. Hatch et al., “Photoresponse in photoconductor devices fabricated from HgTe-HgCdTe superlattices,” *Applied Physics Letters* 98, 043505 (2011), DOI `10.1063/1.3540655`.

**Direct method details:**

- Optronic Laboratories spectral-response measurement system;
- detector mounted in continuous-flow cryostat with ZnSe window;
- output connected to a **low-noise voltage preamplifier specifically designed so a bias voltage could be applied to the device**;
- chopping just below 1 kHz;
- reference for this custom preamp is **J. F. Siliquini, Ph.D. thesis, University of Western Australia, 1995**.

**Role:** strongest recovered same-UWA evidence for the custom bias-capable low-noise preamplifier architecture behind the photoconductor measurement tradition.

## S-R5-03 — Siliquini et al. 1995 composition-matched photoconductor performance

**Class:** Primary-A  
**Citation:** J. F. Siliquini, C. A. Musca, B. Nener, L. Faraone, “Temperature Dependence of Hg0.68Cd0.32Te Infrared Photoconductor Performance,” *IEEE Transactions on Electron Devices* 42(8), 1441–1448 (1995), DOI `10.1109/16.398658`.

**Direct abstract/index anchors:**

- n-type `x=0.32` HgCdTe;
- detector area `250×250 µm²`;
- cutoff ~4.6 µm at 80 K;
- experimental responsivity/noise voltage over 80–300 K;
- anodic oxide/ZnS frontside passivation;
- BLIP D* `3.8×10^11 cm Hz^1/2 W^-1` at 4 µm up to ~180 K under stated background/FOV conditions.

**Negative result:** public full text/circuit description not recovered in this round. This source plus the thesis citation remains the closest pre-RP-01 measurement lineage.

## S-R5-04 — J. F. Siliquini UWA PhD thesis, 1995

**Class:** Primary-Thesis / actionable archival source.

**Known identity:**

- author: John Frank Siliquini / J. F. Siliquini;
- PhD, University of Western Australia, 1995;
- later UWA APL paper cites this thesis specifically for the custom bias-capable low-noise photoconductor preamplifier.

**Current digital status:** thesis title/call number/full text did not surface through ordinary public web/repository searches.

**Acquisition path:** current UWA Library guidance states most pre-2017 UWA Masters/PhD theses are held as print copies and can be found/requested via OneSearch or storage-request services; external researchers/libraries may request scanned thesis copies.

**Highest-value extraction target if acquired:** complete preamp schematic, bias network, component values, gain/bandwidth/input noise, source-resistance range, shielding, calibration method, analyzer settings.

## S-R5-05 — official HP/Keysight 35665A documentation

**Class:** Official-Instrumentation / primary manufacturer documentation.

**Sources:** Keysight legacy product page and 35665A Concepts/Operators Guides (1991).

**Official capability anchors:**

- two-channel dynamic signal analyzer;
- linear spectrum;
- power spectral density;
- cross-spectrum;
- frequency response;
- single-channel analysis bandwidth up to `102.4 kHz`;
- dual-channel up to `51.2 kHz`;
- selectable `100, 200, 400, 800` lines of resolution.

**Role:** proves the analyzer class can directly support PSD and transfer-function measurements. Does not recover the specific Figure-5 window/averaging configuration.

**Procedure:** `procedures/P12B_NOISE_READOUT_ANALYZER_TRANSFER_QUALIFICATION.md`.

## S-R5-06 — 2025 UWA HgCdSe detector-characterization continuity

**Class:** Primary-A / same institution, modern different material branch.  
**Citation:** Z. Zhang et al., “MBE Growth of High-Quality HgCdSe for Infrared Detector Applications,” *Materials* 18, 3676 (2025), DOI `10.3390/ma18153676`.

**Relevant continuity:** later UWA detector characterization still uses Optronic Laboratories spectral-response instrumentation and HP35665A-class noise-spectrum measurement.

**Use restriction:** modern HgCdSe apparatus/settings are not RP-01 historical settings. This source only corroborates instrumentation lineage.

## S-R5-07 — active-gap inference audit using RP-01 scalar data

**Class:** Derived audit from Primary-A RP-01 data.

The exact contact pair/gap for Figures 3/5/6/7 cannot be uniquely inferred because:

- candidate gaps are 50–400 µm;
- width/contact dimension is 300 µm;
- D* depends on `R_lambda sqrt(A)/e_n`;
- the exact `e_n(1 kHz)` used in the spectral D* calculation is not stated;
- 24.5 nV/√Hz is the high-frequency g-r level while the responsivity signal is at 1 kHz below the 3-kHz 1/f knee;
- device resistance/effective lifetime for the selected pair are not fully stated.

**Research note:** `research/2026-08-15_rp01_active_gap_inference_audit.md`.

## Round-5 source conclusion

The historical measurement architecture is now narrowed to a custom UWA bias-capable low-noise voltage preamplifier feeding an HP35665A-class analyzer, with the Siliquini 1995 thesis as the key archival source. Exact historical circuit/RBW/averaging remain open.

A locally traceable noise measurement is nevertheless possible and preferable to guessing the historical settings. P12B defines gain/noise/source-impedance/PSD-normalization calibration explicitly.
