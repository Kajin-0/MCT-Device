# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 55  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce a source-traceable **empirical protocol manual** for HgCdTe photoconductor fabrication and characterization. The preferred publication model is neither a condensed review nor a manufacturing traveler. Each process should read like a highly explicit experimental recipe: hard numbers, equipment/materials, direct numbered actions, expected results, compact analysis, troubleshooting, and source/evidence basis.

Canonical historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_EMPIRICAL_PROTOCOL_REBUILD_ROUND55.md` — active publication-format disposition.
2. `research/2026-08-16_checkpoint_after_empirical_protocol_round55.md` — latest checkpoint.
3. `manuscript/RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md` — technical Draft 0.2 / Round 52.
4. Detailed `procedures/P01...P36A` and calculation modules remain the technical evidence corpus.
5. Round-53 and Round-54 records are retained as rejected/superseded presentation history.

## Current document maturity

- `RP01-INTEGRATED-MANUSCRIPT-DRAFT-READY = YES`.
- `RP01-MANUSCRIPT-ADVERSARIAL-REVIEW-PASSED = YES`.
- `ROUND53-PUBLICATION-PRESENTATION-ACCEPTED = NO`.
- `ROUND54-TRAVELER-SOP-PRESENTATION-ACCEPTED = NO`.
- `RP01-EMPIRICAL-PROTOCOL-CANDIDATE-READY = YES`.

Round 55 is the first publication candidate built around the user's requested empirical-protocol model. It is still a review candidate, not a claim of end-to-end laboratory validation.

Physical maturity remains unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

## Round-55 publication model

The main body contains **no fill-in-the-blank fields** and no form-style release matrix. It contains 20 self-contained protocols covering:

1. CdZnTe substrate selection;
2. final CdZnTe pre-LPE surface;
3. Te-rich source synthesis;
4. horizontal-slider LPE;
5. FTIR composition/thickness;
6. Hall/Van der Pauw;
7. Hg-saturated anneal;
8. Mask-1 lithography;
9. wet mesa etch;
10. anodic oxide;
11. Mask-2 chlorobenzene lift-off lithography;
12. CH4/H2 RIE blocking-contact conversion;
13. Cr/Au thermal evaporation and lift-off;
14. cryogenic TLM/contact resistivity;
15. singulation;
16. compliant cryogenic die attach/interconnect;
17. DC I-V/resistance/self-heating;
18. absolute spectral voltage responsivity;
19. noise PSD/NEP/D*;
20. transient/frequency response.

Each protocol follows:

`objective -> starting state -> equipment/materials -> hard-number recipe -> numbered procedure -> timing -> expected result -> empirical analysis -> troubleshooting -> evidence note`.

Publication formatting is monochrome and deliberately resembles a technical protocol/methods monograph rather than a dashboard or traveler.

## Evidence codes used in Round 55

- `RP` — direct Smith et al. RP-01 value.
- `SL` — same-lineage value/method.
- `PT` — primary transfer experiment or patent.
- `DER` — derived from stated inputs.
- `SYN` — explicit hard-number empirical starting choice synthesized from compatible evidence when the exact historical value is not published.

`SYN` is **not** a promotion of evidence class and not a claim of historical identity. Its purpose is to eliminate unwritten laboratory knowledge and give a concrete, falsifiable starting recipe.

## Representative Round-55 synthesized reference values

- LPE: 4.8000-g charge at target `xL=.082, yL=.810`: Hg `1.198744 g`, Cd `0.060008 g`, Te `3.541249 g`; 3.000-g HgTe reservoir; 515 °C / 60 min equilibration; 500 °C contact; 5.0-min growth contact.
- Wet mesa: 100.0 mL = 2.00 mL Br2 + 73.50 mL EG + 24.50 mL HBr; 21 °C; 4.00 min.
- Anodization: 0.100 M KOH in explicit 900 mL EG + 100 mL DI water; 0.300 mA/cm²; 120 s; expected ~15 V / ~80 nm.
- RIE: direct total 64 sccm / 100 mTorr / 50 W / 60 s with explicit 1:5 interpretation `10.6667/53.3333 sccm` marked DER/SYN.
- Metallization: thermal evaporation; Cr 30 nm / Au 270 nm; explicit synthesized vacuum/rate/transfer/lift-off reference values.

These numbers are intended as one coherent empirical starting implementation, not a claim that the composite sequence has already been validated end-to-end.

## Round-55 artifact and QA

Review artifacts:

- `RP01_HgCdTe_Empirical_Protocol_Manual_Round55.docx`
- `RP01_HgCdTe_Empirical_Protocol_Manual_Round55.pdf`

Final render:

- 34 pages;
- monochrome;
- no fillable PDF form fields;
- DOCX page-by-page visual review completed after pagination repair;
- DOCX accessibility audit: `0 high / 0 medium / 0 low` findings;
- PDF inspector/preflight: 34 pages, letter size, text-native, openable, unencrypted;
- PDF independently rendered at 200 dpi and checked against the DOCX render.

SHA-256:

- DOCX `ee697bced13152e65eed1ce1bf53ed35977bfd96cf922143a5fed6fcd0e8d764`.
- PDF `f3d8256f653befac45a0b2c7316aaba95d55cb9b93015e0741d966a8242abe57`.

The binary files are conversation review artifacts. Repository procedures/calculations remain the underlying technical evidence corpus until a final issue is frozen.

## Permanent scientific rules

### LPE authority

`xL=.082, yL=.810, TL=507 °C, xS≈.29` with Hg/Cd/Te mass fractions:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

Do not relabel the Round-55 4.8000-g absolute charge as a historical Honeywell/RP-01 charge. It is a synthesized reference implementation using a primary horizontal-slider charge-mass scale.

### RIE authority

Direct controller state: parallel-plate Plasma Technology reactor, `CH4/5H2`, total `64 sccm`, `100 mTorr`, `50 W`, `60 s`.

Permanent:

- `50 W != reactor equivalence`;
- `d_etch != d_conv` and `L_conv` is separate;
- `n_conv=N_s/d_conv` only after independent depth closure;
- TLM does not prove minority-carrier blocking.

### Detector-performance authority

RP-01 Figures 3/5/6/7 are the same representative detector. A new D* result should preserve same device/contact pair/geometry/T/E/package/FOV/loading/frequency state wherever possible.

`24.5 nV/sqrt(Hz)` is the high-frequency g-r level, not automatically the 1-kHz noise because the historical 1/f knee is ~3 kHz.

### Dynamics/package authority

No direct RP-01 lifetime curve exists. Source/readout and package thermal poles must be discriminated before assigning a time constant to carrier lifetime.

## Immediate next work

Use Round 55 as the active review candidate. The next improvement should be a **recipe-by-recipe adversarial scientific audit** of the chosen `SYN` hard numbers and combinations, especially values that combine two process lineages. Replace a SYN value only when better primary evidence or stronger physical analysis justifies a more defensible concrete starting value. Do not revert to blank-field/traveler formatting.
