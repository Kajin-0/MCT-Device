# Round 55 — empirical protocol / hard-number recipe rebuild

**Date:** 2026-08-16 America/New_York  
**Base technical corpus:** Draft 0.2 plus P01–P36/P36A and calculation modules

## Why Round 54 was superseded

The Round-54 procedural rebuild was technically richer than Round 53 but still used the wrong publication grammar. It emphasized traveler fields, local blanks, and GO/HOLD release logic. The user clarified that the desired artifact is a new kind of **empirical protocol paper/manual**: each process should give a concrete hard-number recipe and direct step-by-step procedure, with analysis and troubleshooting where needed.

Round 55 therefore treats forms/travelers as ancillary rather than primary content.

## Publication model

Each of 20 process/measurement protocols now uses the same compact structure:

1. objective;
2. starting state;
3. equipment and materials;
4. hard-number reference recipe;
5. direct numbered procedure;
6. timing;
7. expected result;
8. analysis and critical empirical notes;
9. troubleshooting;
10. evidence note.

The document is monochrome, text/table dominant, and intentionally avoids decorative diagrams.

## No blank-field rule

The main document contains no fill-in-the-blank traveler fields.

For a missing historical parameter:

- use a direct value when published;
- derive a value when the calculation is unambiguous;
- otherwise choose one concrete empirical starting value from the most compatible primary evidence and label it `SYN`;
- preserve a short evidence note explaining the limitation.

This produces a falsifiable empirical recipe without claiming the chosen composite is historical fact.

## Evidence codes

- `RP` — direct Smith et al. RP-01.
- `SL` — same-lineage process/method.
- `PT` — primary transfer experiment/patent.
- `DER` — calculated from stated inputs.
- `SYN` — explicit synthesized empirical starting value.

## Protocol coverage

20 protocols span substrate selection and preparation, Te-rich source synthesis and horizontal-slider LPE, FTIR/Hall, Hg anneal, both lithography masks, wet mesa, native anodic oxide, RIE blocking contacts, Cr/Au, cryogenic TLM, singulation, compliant packaging, DC characterization, absolute responsivity, noise/NEP/D*, and transient/frequency response.

## Representative hard-number synthesis

### LPE charge

Target composition remains `xL=.082, yL=.810` with authoritative mass fractions from the controlled calculation module. Round 55 adopts `4.8000 g` as the explicit source-solution charge because a primary modified horizontal-slider HgCdTe process reports approximately 4.8 g per growth run. Applying the target composition gives:

- Hg `1.198744 g`;
- Cd `0.060008 g`;
- Te `3.541249 g`.

This is `PT + DER + SYN`, not historical RP-01/Honeywell charge-mass evidence.

### Wet mesa

The primary x≈0.28 HgCdTe branch supports 2% Br2 in 3:1 EG:HBr at ~21 °C and ~2.78 µm/min. Round 55 explicitly fixes the ambiguous preparation to 100.0 mL total, 2.00 mL Br2 + 73.50 mL EG + 24.50 mL HBr, and a 4.00-min initial etch. The 4-min time gives 11.12 µm nominal depth versus a 9.5-µm active layer before rate uncertainty.

### Native anodic oxide

The manual fixes an executable transfer branch of 0.100 M KOH, 900 mL EG + 100 mL DI water, carbon cathode, HgCdTe anode, 0.300 mA/cm², 120 s, with expected ~15 V / ~80 nm / deep-blue film.

### RIE and metal

Direct RP-01 RIE values are preserved. Individual CH4/H2 flows are explicitly calculated from a 1:5 interpretation and labeled DER/SYN. Cr/Au thicknesses remain direct; method/rates/vacuum/timing/lift-off choices are separately coded by evidence class.

## Formatting basis

The procedural grammar follows the useful parts of established protocol/SOP practice: the experimental procedure is a direct numbered sequence, critical notes appear beside the relevant process, troubleshooting is explicit, and expected results/data analysis are stated. Round 55 intentionally removes the traveler-like local-entry presentation that dominated Round 54.

## QA result

Final review artifact:

- 34 pages;
- monochrome;
- no fillable fields;
- no decorative figures;
- DOCX visually inspected page-by-page after repairing a stranded appendix row;
- accessibility audit `0 high / 0 medium / 0 low`;
- PDF openable, unencrypted, text-native, 34 letter-size pages;
- final PDF independently rendered at 200 dpi.

Artifact hashes:

- DOCX `ee697bced13152e65eed1ce1bf53ed35977bfd96cf922143a5fed6fcd0e8d764`;
- PDF `f3d8256f653befac45a0b2c7316aaba95d55cb9b93015e0741d966a8242abe57`.

## Disposition

`RP01-EMPIRICAL-PROTOCOL-CANDIDATE-READY = YES`.

This is a publication/reference-implementation state only. It does not establish end-to-end empirical validation of the composite recipe, historical reproduction, or production release.
