# P12A — UWA low-noise preamplifier lineage and archival-source addendum

**Status:** HISTORICAL LINEAGE PARTIALLY CLOSED / EXACT CIRCUIT STILL OPEN. Supplements `P12_NOISE_PSD_NEP_DETECTIVITY.md`.

## 1. Purpose

Record the strongest recovered evidence for the low-noise bias-capable preamplifier architecture used in the University of Western Australia HgCdTe photoconductor characterization lineage and distinguish that evidence from the still-missing exact RP-01 preamplifier circuit/gain/noise specification.

## 2. Direct RP-01 measurement statement

Smith et al. 2001 directly state that the representative detector noise spectrum was measured:

- at `80 K`;
- at applied field `10 V/cm`;
- using a **low-noise pre-amplifier**;
- followed by an `HP35665A` spectrum analyser;
- the plotted result was an **averaged noise-voltage spectrum**.

The paper does not state:

- preamplifier manufacturer/model;
- circuit topology;
- voltage gain;
- input voltage noise;
- input current noise;
- input impedance/loading;
- bias-injection topology;
- preamplifier bandwidth;
- AC/DC coupling;
- overload/recovery behavior;
- HP35665A frequency span/RBW/ENBW/window/averaging settings.

No electronics citation is attached directly to the Figure-5 sentence.

## 3. Same-UWA preamplifier lineage recovered

S. D. Hatch et al., “Photoresponse in photoconductor devices fabricated from HgTe-HgCdTe superlattices,” *Applied Physics Letters* 98, 043505 (2011), uses the same broad UWA photoconductor characterization tradition.

The paper directly states that:

- lateral photoconductors were measured in an Optronic Laboratories spectral response measurement system;
- devices were mounted in a continuous-flow cryostat with ZnSe window;
- detector output was connected to a **low-noise voltage preamplifier specifically designed so that a bias voltage could be applied to the device**;
- measurements were made at a chopping frequency just below `1 kHz`;
- the cited source for this custom preamplifier is **J. F. Siliquini, Ph.D. thesis, University of Western Australia, 1995**.

This is the strongest recovered evidence that the historical UWA HgCdTe photoconductor readout was not simply an arbitrary commercial voltage amplifier: it was a custom bias-capable low-noise detector preamplifier documented in Siliquini's thesis.

## 4. Archival source status

The 1995 Siliquini thesis has not been recovered as a public full-text digital source through normal web/index searches.

Recovered facts:

- author: **John Frank Siliquini / J. F. Siliquini**;
- institution: University of Western Australia;
- PhD year: `1995`;
- later UWA APL work cites the thesis specifically for the low-noise bias-capable photoconductor preamplifier.

### 4.1 Current official UWA acquisition path

Current UWA Library guidance makes this an actionable archival source:

- UWA states that **most pre-2017 Masters and PhD theses are held as print copies**;
- older theses can be located through UWA `OneSearch` even when there is no repository PDF;
- UWA users can request a stored print thesis for consultation;
- non-UWA users can use the Library's Store Request route to consult stored material;
- libraries/institutions and external researchers can inquire about obtaining a **scanned PDF copy** of a UWA thesis through the Library's thesis/document-delivery service.

Therefore the acquisition record should use at minimum:

`Author: John Frank Siliquini`

`Institution: University of Western Australia`

`Degree: PhD`

`Year: 1995`

`Known citation role: custom low-noise bias-capable HgCdTe photoconductor voltage preamplifier`.

The thesis title/call number remains `OPEN` because it has not surfaced through public web indexing.

This is now classified as an **actionable archival acquisition target**, not an unidentified reference.

### Acquisition goal

If/when the thesis is obtained, extract at minimum:

- thesis title and permanent catalog identifier;
- schematic;
- component values;
- detector bias topology;
- input stage device/op-amp/transistor;
- supply rails;
- gain settings;
- frequency response;
- input/output impedance;
- input voltage/current noise;
- shielding/grounding;
- detector/source-resistance range;
- coupling capacitors/high-pass poles;
- noise calibration method;
- any spectrum-analyzer settings.

Update P12A immediately after acquisition.

## 5. Relevant same-lineage 1995 device paper

J. F. Siliquini, C. A. Musca, B. Nener, L. Faraone, “Temperature Dependence of Hg0.68Cd0.32Te Infrared Photoconductor Performance,” *IEEE Transactions on Electron Devices* 42(8), 1441–1448 (1995), DOI `10.1109/16.398658`.

This source is especially relevant because:

- n-type `x=0.32` HgCdTe is compositionally close to RP-01;
- detector area is `250×250 µm²`;
- cutoff is ~`4.6 µm` at 80 K;
- experimental responsivity and noise voltage are reported over 80–300 K;
- anodic-oxide/ZnS passivation is used;
- BLIP D* is reported at 4 µm.

Publicly accessible abstract/index text does not expose the preamplifier schematic or analyzer settings.

Do not assume that the exact 1995 preamp was unchanged in RP-01, but this paper/thesis pair is the best historical electronics lineage currently identified.

## 6. Later UWA instrumentation continuity

Later UWA photoconductor/material papers continue to use:

- Optronic Laboratories detector spectral-response systems;
- cryogenic detector measurement;
- measured noise spectra using HP dynamic signal/spectrum analyzers, including HP35665A in later work.

Official Keysight documentation for the legacy 35665A confirms that the analyzer class supports linear spectrum, power spectral density, cross-spectrum and frequency-response measurements, with up to 102.4-kHz single-channel analysis bandwidth and selectable FFT line resolution. This is enough to define a rigorous local analyzer calibration, but it does not recover the exact Figure-5 settings.

This supports continuity of the **measurement architecture**, but it does not prove identical gain/RBW/preamp settings across decades.

## 7. Functional architecture inferred at evidence-safe level

The historical/same-UWA evidence supports the following functional blocks:

`detector + DC bias network -> custom low-noise voltage preamplifier -> spectrum/dynamic-signal analyzer`

and, for chopped optical responsivity:

`biased detector -> low-noise preamplifier -> phase-sensitive/measurement instrumentation`.

What is **not** yet known is the internal preamp transfer function.

Accordingly, future RP-01 reproduction must measure the local readout transfer function independently rather than matching only the label “low-noise preamplifier.”

## 8. Historical-noise interpretation rule

Because the RP-01 Figure-5 spectrum is measured after a preamplifier,

`S_out(f) = |G_pre(f)|² S_detector_loaded(f) + S_pre,out(f) + S_analyzer,in_equiv(f)`.

Therefore detector-referred noise requires:

1. complex/real gain `G_pre(f)` over the frequency range;
2. preamplifier self-noise under the actual source impedance/loading;
3. analyzer contribution;
4. detector loading/bias-network transfer.

A flat nominal preamplifier gain or manufacturer broadband noise number is insufficient.

## 9. Release implication

Until the Siliquini thesis/circuit is recovered, the historical preamplifier is `OPEN`.

RP-01 reproduction shall instead use a locally characterized bias-capable low-noise readout whose:

- gain;
- phase;
- input noise;
- source-impedance dependence;
- bandwidth;
- bias-network loading;
- analyzer normalization

are measured and stored with every detector-noise result.

The local circuit may differ from the historical UWA preamp as long as detector-referred noise and responsivity are traceable and the circuit does not alter detector operating state.

See `P12B_NOISE_READOUT_ANALYZER_TRANSFER_QUALIFICATION.md` for the local calibration route.
