# Source ledger addendum — Round 29 noise-chain / analyzer-state recovery

**Date:** 2026-08-16

**Scope:** RP-01 Figure-5 noise state, same-device linkage to responsivity/detectivity, UWA low-noise preamplifier lineage, HP35665A analyzer capability, and background-fluctuation noise evidence.

Evidence classes follow the repository-wide provenance rules.

---

## R29-S1 — Smith et al. 2001 canonical RP-01 article

**Reference**

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Evidence class:** `DIRECT-RP01 / PRIMARY`.

### Directly recovered for Round 29

The complete article text/captions establish:

- Figure 5 is an **averaged noise-voltage spectrum** for a typical detector;
- Figure-5 conditions include `T=80 K`, `E=10 V/cm`, and stated `60° FOV`;
- the chain is low-noise preamplifier -> HP35665A spectrum analyzer;
- low-frequency behavior is identified as `1/f` noise;
- the high-frequency generation-recombination noise level is approximately `24.5 nV/sqrt(Hz)`;
- the graphical intersection of the low-frequency `1/f` trend and high-frequency g-r trend gives a knee near `3 kHz`;
- Figures 3, 5, 6 and 7 are tied to the **same detector/device** in the performance discussion;
- spectral responsivity/detectivity state uses `80 K`, `10 V/cm`, stated `60° FOV` and `1 kHz` optical chopping;
- the device structure includes nine `300 x 300 µm` contacts with 50-µm-increment spacings, but the exact contact pair used for Figures 3/5/6/7 is not identified in the recovered text;
- Figure-7 `D*` is about `2.0e11 cm sqrt(Hz)/W` at 4 µm.

### Critical direct/non-direct boundary

Direct evidence now closes that Figure 5 itself had stated `60° FOV` and that the main performance figures refer to the same physical device.

It does **not** close:

- exact active gap/contact pair;
- exact physical aperture defining 60°;
- exact background radiance/temperature during the Figure-5 acquisition;
- preamplifier circuit/gain/noise;
- HP35665A span/window/line count/averaging;
- exact noise frequency/value used in the Figure-7 `D*` reduction.

### Important rejected inference

Because `1 kHz < 3 kHz`, do not infer that the `24.5 nV/sqrt(Hz)` high-frequency plateau is the noise used for the 1-kHz spectral `D*`.

---

## R29-S2 — Keysight 35665A Operators Guide

**Reference**

Keysight/HP, *35665A Dynamic Signal Analyzer Operators Guide*, publication `35665-90026`, Sep. 1991.

Official legacy manual page/file supplied by Keysight.

**Evidence class:** `OFFICIAL-INSTRUMENT / PRIMARY`.

### Relevance

Positive model documentation for the exact analyzer family named by RP-01.

It establishes an authoritative path for reconstructing the analyzer's PSD/spectrum/window/averaging implementation.

### What was not recovered

No historical Figure-5 instrument state was found. The manual cannot identify which settings UWA selected in 2001.

---

## R29-S3 — Keysight 35665A Concepts Guide

**Reference**

Keysight/HP, *35665A Dynamic Signal Analyzer Concepts Guide*, publication `35665-90028`, Sep. 1991.

**Evidence class:** `OFFICIAL-INSTRUMENT / PRIMARY`.

### Official capability relevant to transfer

Keysight's official 35665A documentation/product record identifies capabilities including:

- linear spectrum;
- power spectral density;
- cross spectrum;
- frequency response;
- time waveform/correlation functions;
- up to 102.4-kHz one-channel bandwidth;
- up to 51.2-kHz two-channel bandwidth;
- selectable 100/200/400/800 lines of resolution.

These prove capability only; they are not historical Figure-5 settings.

---

## R29-S4 — Hatch et al. 2011 UWA preamplifier lineage

**Reference**

S. D. Hatch, C. A. Musca, C. R. Becker, J. M. Dell, L. Faraone, “Photoresponse in photoconductor devices fabricated from HgTe-HgCdTe superlattices,” *Applied Physics Letters* 98, 043505 (2011), DOI `10.1063/1.3540655`.

**Evidence class:** `SAME-UWA-LINEAGE / PRIMARY`.

### Directly relevant experimental facts

Later UWA photoconductor work reports:

- Optronic Laboratories spectral-response system;
- continuous-flow cryostat with ZnSe window;
- a low-noise **voltage preamplifier designed to permit bias application**;
- chopping just below 1 kHz;
- citation to J. F. Siliquini's 1995 UWA PhD thesis for the preamplifier.

### Provenance limit

This supports a persistent UWA functional readout architecture but does not prove the exact circuit remained unchanged from 1995 through RP-01 in 2001 and later work in 2011.

---

## R29-S5 — Siliquini 1995 UWA thesis

**Reference state**

J. F. Siliquini, PhD thesis, University of Western Australia, 1995.

**Evidence class:** `ARCHIVAL-TARGET / IDENTIFIED-BY-CITATION`.

Later UWA work cites this thesis specifically for the custom low-noise bias-capable photoconductor preamplifier.

The current project has not recovered the full thesis, title/call number, schematic or circuit parameters.

**Priority extraction if acquired:** schematic, component values, bias topology, gain, input noise, source-resistance range, bandwidth, coupling, power supply, shielding/grounding, and analyzer interface.

---

## R29-S6 — Siliquini et al. 1995 near-composition photoconductor performance

**Reference**

J. F. Siliquini, C. A. Musca, B. Nener, L. Faraone, “Temperature Dependence of Hg0.68Cd0.32Te Infrared Photoconductor Performance,” *IEEE Transactions on Electron Devices* 42(8), 1441–1448 (1995), DOI `10.1109/16.398658`.

**Evidence class:** `SAME-UWA / NEAR-COMPOSITION / PRIMARY`.

### Relevance

Near-RP01 MWIR n-HgCdTe photoconductor performance/noise lineage:

- x≈0.32;
- ~250 x 250 µm² detector scale;
- ~4.6-µm cutoff at 80 K;
- experimental responsivity/noise versus temperature;
- passivation and BLIP performance context.

No exact RP-01 electronics settings are transferred from this source.

---

## R29-S7 — Jozwikowski et al. 2003 background-fluctuation noise

**Reference**

K. Jozwikowski, R. Sewell, C. A. Musca, J. M. Dell, L. Faraone, “Noise modeling in HgCdTe heterostructure devices,” *Journal of Applied Physics* 94(10), 6541–6548 (2003), DOI `10.1063/1.1619198`.

**Evidence class:** `SAME-UWA / PRIMARY`.

### Direct relevance

The reported fluctuation model includes spectral intensity from:

- temperature fluctuations;
- **background-illumination fluctuations**;
- thermal generation-recombination fluctuations including Auger, radiative and Shockley-Read-Hall processes;
- carrier-mobility fluctuations.

The model was compared with measured MWIR HgCdTe photoconductor noise spectra over a wide temperature range.

### P12 implication

Nominal FOV is insufficient to characterize a noise run. Warm-background stability can contribute to the measured noise spectrum and must be recorded/controlled during P12 transfer.

---

# Round-29 provenance conclusions

1. `DIRECT`: RP-01 Figure 5 is at 80 K, 10 V/cm and stated 60° FOV.
2. `DIRECT`: Figures 3/5/6/7 correspond to the same physical detector.
3. `OPEN`: exact contact pair/gap for that detector's performance data.
4. `OPEN`: exact historical preamplifier circuit and complete bias/load network.
5. `OPEN`: exact HP35665A Figure-5 acquisition settings.
6. `OPEN`: exact detector-noise quantity/frequency convention entering Figure-7 `D*`.
7. `REJECTED`: substituting the 24.5-nV/sqrtHz high-frequency plateau for 1-kHz noise solely because spectral responsivity was chopped at 1 kHz.
8. `SAME-UWA`: background-illumination fluctuations are a legitimate HgCdTe photoconductor noise contribution and must be part of the optical-state record.
9. `OFFICIAL-INSTRUMENT`: the 35665A manuals provide the correct local interpretation/calibration framework but cannot back-fill missing historical settings.
