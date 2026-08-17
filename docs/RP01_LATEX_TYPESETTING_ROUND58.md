# Round 58 — LaTeX typesetting and protocol-document redesign

**Date:** 2026-08-16 America/New_York  
**Scientific baseline:** Round 57

## Trigger

The user judged the Round-57 scientific content much stronger than its presentation. The document still looked like a generated technical handout and many equations/symbols were written as code-like prose rather than real mathematical notation.

The user then clarified that the desired artifact should not be forced to imitate a conventional publication. The target is a new hybrid: an **exhaustive research-fabrication protocol** combining the explanatory rigor of a methods paper, the directness of an SOP, and the completeness of an internal process-development notebook.

Round 58 therefore changes the presentation/type system while preserving the Round-57 scientific state.

## Document design rule

The dominant question is:

> What exactly does the researcher do, with what material, tool, geometry, quantity, timing, measurement, calculation, and acceptance criterion?

Explanatory physics and uncertainty are included when they make the protocol more executable or interpretable, but they do not replace numbered execution.

## LaTeX presentation layer

Round 58 uses native LaTeX rather than a DOCX-first layout.

Key choices:

- `scrreprt`, 10-pt, letter paper, one-sided;
- TeX Gyre Pagella body type;
- TeX Gyre Heros headings;
- `newtxmath` mathematical typography;
- `siunitx`, `mhchem`, `amsmath`, `mathtools`;
- `booktabs`, `longtable`, `tabularx` for technical tables;
- monochrome only;
- restrained protocol title frames and thin rules;
- running headers/footers;
- every major protocol begins on a new page;
- contents depth deliberately limited so navigation remains useful rather than becoming a multi-page index of every subheading.

Tables no longer use spreadsheet-style boxed grids. Recipe and troubleshooting tables are formatted as technical reference tables with minimal rules.

## Mathematical conversion

Round 58 explicitly converts important analysis from literal text strings to mathematical objects and displayed derivations.

Examples include:

- FTIR depth/composition model `x(z)`, gradient definition and weighted `chi^2` objective;
- wet-etch overetch and witness-rate timing equations;
- anodization charge density and KOH mass;
- Hg vapor inventory consistency calculation;
- Smith terminal-field and contact-corrected bulk-field equations;
- TLM transfer-length/contact-resistance relations;
- absolute spectral substitution-comparator responsivity equation;
- NEP and specific-detectivity equations;
- transient sampling, adaptive record/repetition timing and conditional one-pole `f_3dB` mapping.

Appendix A is reformatted as a genuine analytical reference with aligned equations rather than prose calculations.

## Protocol grammar retained

Each protocol remains approximately:

1. objective;
2. starting state;
3. equipment and materials;
4. hard-number reference recipe;
5. numbered procedure;
6. timing;
7. expected empirical outcome;
8. analysis/process notes;
9. troubleshooting;
10. evidence basis/transfer limits.

This is intentionally more explanatory than a production SOP but more executable than a journal Methods section.

## Scientific content unchanged in authority

Round 58 does not promote any `SYN` value to validated process knowledge. Round-57 scientific closures remain controlling, including:

- D1/T1 geometry;
- isolated-mesa anodization fixture;
- composite upstream LPE hypothesis;
- geometry-matched wet-mesa witness calibration;
- FTIR inverse model and archive requirements;
- dual field convention;
- underfilled absolute-radiometry geometry;
- P37/W1 LBIC blocking-contact witness;
- finite-width TLM;
- D* active-area convention;
- stationarity-aware noise statistics;
- adaptive transient timing.

## Layout QA

The first LaTeX builds intentionally allowed more space rather than forcing the 41-page Round-57 layout. Intermediate builds reached 62 pages while mathematical and table problems were corrected.

Specific pagination/type repairs included:

- reduced TOC depth to remove multi-page navigation clutter;
- removal of an isolated Part-I status page;
- folding protocol evidence notes into analysis where a forced page caused an evidence-only orphan;
- reworking Appendix-B troubleshooting columns rather than shrinking type;
- fixing protocol tables so rows do not split awkwardly across pages;
- compacting the absolute-responsivity troubleshooting section to eliminate a one-row spill page;
- correcting closing status language to Round 58;
- removing remaining overfull/underfull box warnings.

Final release state:

- 59 physical pages;
- all 59 release pages visually inspected via rendered contact sheets;
- letter size;
- text-native PDF;
- openable, unencrypted;
- no XFA/form fields;
- no remaining LaTeX overfull/underfull box warnings.

## Artifact hashes

- PDF SHA-256: `07a367efa3dbd378733d40170a98fe37591560e2cd0241995b946be4cfabfb18`.
- TeX SHA-256: `1aecca413df24ddb545b9e5c8bc1e14afc8d26e80fe14ca5eeea59c530e3889f`.

## Disposition

`RP01-EXHAUSTIVE-EMPIRICAL-PROTOCOL-ROUND58-LATEX-CANDIDATE = YES`.

This is a presentation/mathematical-typesetting state, not an empirical process-release state. The next scientific work should continue adversarial review of remaining `SYN` process values and cross-lineage compatibility while retaining this document architecture.