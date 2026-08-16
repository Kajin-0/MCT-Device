# Recovery checkpoint — measurement-chain round 5

**Date:** 2026-08-15 America/New_York  
**Current checkpoint:** yes, after round 4.

Round 5 focused on the historical RP-01 detector-noise/readout chain and on whether the exact active contact gap for Figures 3/5/6/7 could be recovered analytically.

## 1. Historical RP-01 noise chain — direct facts

Smith et al. 2001 state that Figure 5 is an **averaged noise-voltage spectrum** measured:

- at `80 K`;
- at `10 V/cm`;
- through a **low-noise pre-amplifier**;
- using an `HP35665A` spectrum analyser.

Historical results:

- 1/f knee ~`3 kHz`;
- high-frequency g-r noise level ~`24.5 nV/√Hz`.

The paper does **not** state:

- preamp model/schematic;
- gain;
- input voltage/current noise;
- source loading;
- bias topology;
- preamp bandwidth;
- analyzer span/window/RBW/ENBW;
- averaging mode/count.

No electronics citation is attached directly to Figure 5.

## 2. Same-UWA custom preamplifier lineage recovered — P12A

High-value source:

S. D. Hatch et al., “Photoresponse in photoconductor devices fabricated from HgTe-HgCdTe superlattices,” *Applied Physics Letters* 98, 043505 (2011), DOI `10.1063/1.3540655`.

Direct method statement:

- Optronic Laboratories spectral-response system;
- continuous-flow cryostat / ZnSe window;
- detector output connected to a **low-noise voltage preamplifier specifically designed so that detector bias could be applied**;
- chopping just below 1 kHz;
- reference for the preamplifier: **J. F. Siliquini, Ph.D. thesis, University of Western Australia, 1995**.

This is the strongest historical electronics lineage found so far.

Relevant near-composition device paper:

J. F. Siliquini, C. A. Musca, B. Nener, L. Faraone, “Temperature Dependence of Hg0.68Cd0.32Te Infrared Photoconductor Performance,” *IEEE Trans. Electron Devices* 42(8), 1441–1448 (1995), DOI `10.1109/16.398658`.

Direct abstract/index anchors:

- n-type x=.32;
- 250×250-µm² detector;
- cutoff ~4.6 µm at 80 K;
- measured responsivity/noise voltage 80–300 K;
- anodic oxide/ZnS;
- BLIP D* at 4 µm.

Publicly accessible material still does not expose the preamp circuit.

Created/updated:

- `procedures/P12A_UWA_PREAMPLIFIER_LINEAGE_ADDENDUM.md`.

## 3. Siliquini 1995 thesis is now an actionable archival target

Recovered identity:

- **John Frank Siliquini / J. F. Siliquini**;
- PhD, University of Western Australia;
- year 1995;
- later UWA APL paper cites the thesis specifically for the custom bias-capable photoconductor preamplifier.

The thesis title/call number has not surfaced through ordinary public web search.

Current official UWA Library guidance states:

- most pre-2017 UWA Masters/PhD theses are held as print copies;
- older theses can be found through OneSearch;
- stored print theses can be requested;
- external researchers/libraries can inquire about scanned PDF thesis copies through UWA thesis/document-delivery services.

Thus the thesis is no longer a vague citation. It has a defined acquisition route.

If acquired, extract:

- thesis title/catalog ID;
- full preamp schematic;
- bias network;
- component values;
- gain/bandwidth;
- voltage/current noise;
- input impedance/source-resistance range;
- coupling/high-pass poles;
- shielding/grounding;
- noise calibration;
- spectrum-analyzer settings.

## 4. Official HP35665A capability — analyzer side partially closed

Official Keysight legacy documentation confirms the 35665A supports:

- linear spectrum;
- power spectral density;
- cross-spectrum;
- frequency response;
- up to 102.4-kHz single-channel analysis bandwidth;
- up to 51.2-kHz dual-channel bandwidth;
- 100/200/400/800 FFT lines.

This proves the historical analyzer class is capable of direct PSD and transfer measurements.

It does **not** recover the exact Figure-5 window/RBW/ENBW/averaging configuration.

## 5. P12B — local noise-chain transfer qualification created

Rather than guess historical electronics settings, P12B now defines a traceable local method.

Key controls:

- measure complex preamp gain `G(f)` using calibrated low-level injection and detector-equivalent source impedance;
- characterize electronics noise for input short and precision resistors bracketing detector resistance;
- verify full-chain PSD normalization against Johnson noise `4kTR`;
- model/measure bias-network loading;
- record FFT lines, record length/span, window, ENBW, overlap, averaging type/count;
- retain time records to test stationarity/burst/microphonic behavior;
- subtract independent electronics noise at the **PSD level**, not ASD;
- permit two-channel cross-spectrum as a local enhancement if loading/cross-talk are qualified;
- measure detector noise directly at 1 kHz when computing new 1-kHz D*.

Created:

- `procedures/P12B_NOISE_READOUT_ANALYZER_TRANSFER_QUALIFICATION.md`.

## 6. Historical 1-kHz D* ambiguity remains

RP-01 reports:

- spectral responsivity at 1 kHz;
- 1/f knee ~3 kHz;
- g-r plateau ~24.5 nV/√Hz.

Therefore 1 kHz is below the knee.

Do not assume `24.5 nV/√Hz` was the exact noise used for the historical spectral D* curve.

For new measurements, use `R_lambda(1 kHz)` and directly measured `e_n(1 kHz)` under the same detector condition.

## 7. Exact historical active gap — inference audit completed

Direct geometry:

- nine contacts;
- each 300×300 µm;
- adjacent gaps 50,100,...,400 µm;
- Figures 3/5/6/7 use the same detector.

If full 300-µm contact width defines active width, candidate rectangular active areas are:

- 50-µm gap → 0.015 mm²;
- ...
- 400-µm gap → 0.120 mm².

However the gap cannot be uniquely inferred from D* because:

`D* = R sqrt(A) / e_n`

and the exact historical 1-kHz noise value is not closed.

Conditional use of the 24.5-nV/√Hz g-r floor would require 4-µm responsivity from roughly:

- `4.00×10^5 V/W` for 50 µm gap;
- down to `1.41×10^5 V/W` for 400 µm gap,

but this assumption is not historically justified because 1 kHz lies below the 3-kHz knee.

Equation (1) also contains unknown/geometry-dependent detector resistance and effective lifetime, so responsivity-vs-field cannot independently close gap.

Conclusion:

**exact contact pair remains OPEN.**

Do not assign 50, 100 or another gap by plausibility.

Created:

- `research/2026-08-15_rp01_active_gap_inference_audit.md`.

## 8. Repository synchronization completed

Created/updated:

- `procedures/P12A_UWA_PREAMPLIFIER_LINEAGE_ADDENDUM.md`;
- `procedures/P12B_NOISE_READOUT_ANALYZER_TRANSFER_QUALIFICATION.md`;
- `research/2026-08-15_rp01_active_gap_inference_audit.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND5.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND5.md`;
- this checkpoint.

## 9. Highest-impact blockers after round 5

### Historical measurement

1. acquire Siliquini 1995 UWA PhD thesis / preamp circuit;
2. recover exact HP35665A Figure-5 settings if thesis/lab records contain them;
3. recover original mask/layout or log identifying Figure-3/5/6/7 contact pair.

### RIE/frontside

4. primary CH4:H2 MFC ratio;
5. exact Musca-1998 plasma conditions for ~8-µm conversion;
6. exact resist product/exposure/developer;
7. exact UWA anodization traveler/rinse/dry;
8. P01 Br2 percentage basis.

### Upstream

9. exact source synthesis/homogenization;
10. final CdZnTe polarity/miscut/surface prep;
11. historical LPE schedule and anneal condition, with P03B/P04A local recovery paths already defined.

## 10. Recommended next work

Highest-value next paths:

1. trace the Siliquini 1995 IEEE/SPIE publications for any reproduced circuit or thesis title/catalog clue;
2. search same-UWA instrumentation papers/citations for detector preamp schematic independent of thesis;
3. move to exact source synthesis/homogenization if measurement-chain archives remain inaccessible;
4. define local P01/P02 chemistry DOEs now that source ceilings are documented;
5. refresh `AGENTS.md` to point to round 5.

## 11. Recovery order

Read:

1. `AGENTS.md`;
2. through-P16 checkpoint;
3. rounds 1–4;
4. **this round-5 checkpoint**;
5. round-5 source/gap addenda;
6. P12/P12A/P12B and active-gap audit;
7. relevant branch-specific procedures.
