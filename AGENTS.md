# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 58  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce an **exhaustive research-fabrication protocol** for HgCdTe photoconductor fabrication and characterization: a hybrid of a scientific methods monograph, an SOP, and a process-development laboratory reference. The document should preserve essentially every experimentally useful detail that can be recovered, derived, or defensibly synthesized.

The dominant question on every protocol page is:

> What exactly does the researcher do, with what material, tool, geometry, quantity, timing, measurement, calculation, and acceptance criterion?

Explanatory physics is included when it improves execution or interpretation, but execution remains primary. Do not revert to blank-field traveler formatting or condensed review-article prose.

Canonical downstream historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_LATEX_TYPESETTING_ROUND58.md` — current presentation/type-system state.
2. `research/2026-08-16_checkpoint_after_latex_protocol_round58.md` — latest checkpoint.
3. Round-57 scientific closure records remain controlling for the scientific content:
   - `docs/RP01_EMPIRICAL_PROTOCOL_METROLOGY_CLOSURE_ROUND57.md`;
   - `procedures/P37_LBIC_BLOCKING_CONTACT_FUNCTIONAL_QUALIFICATION.md`;
   - `analysis/ftir/ROUND57_FTIR_MODEL_SPECIFICATION.md`.
4. Detailed P01–P37 procedures, calculations and source ledger remain the technical evidence corpus.

## Current publication state

- `RP01-EXHAUSTIVE-EMPIRICAL-PROTOCOL-ROUND58-LATEX-CANDIDATE = YES`.
- Round 58 is a **presentation and mathematical-typesetting revision of the Round-57 scientific state**.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

## Round-58 document concept

The preferred label is **exhaustive research-fabrication protocol**. It is intentionally not forced into a conventional publication or manufacturing-SOP template.

Each process remains self-contained and follows approximately:

`physical objective -> starting state -> equipment/materials -> hard-number reference recipe -> numbered procedure -> timing -> expected result -> analysis/process notes -> troubleshooting -> evidence/transfer limits`.

The document may explain why a setpoint matters, derive equations, and discuss uncertainty, but it must never become less explicit because of that explanation.

## Round-58 typography and layout

The active presentation layer is native LaTeX rather than DOCX-generated math/prose.

Key design rules:

- monochrome technical-reference aesthetic;
- TeX Gyre Pagella serif body, restrained sans-serif headings, proper mathematical font;
- real LaTeX mathematics for symbols, equations and derivations;
- `siunitx`-style unit treatment and `mhchem` chemistry notation;
- booktabs-style tables instead of spreadsheet grids;
- each major protocol begins on a fresh page;
- running headers/footers and a real contents hierarchy;
- no decorative graphics, dashboard cards, colored traveler fields or form-style blank boxes;
- equations are displayed/aligned when they carry analytical meaning rather than written as code-like text strings.

Representative notation now appears as mathematical objects, e.g. `x_L`, `T_L`, `rho_c`, `R_v(lambda)`, `D*`, `E_Smith`, `E_bulk,est`, rather than literal prose strings.

## Scientific state inherited from Round 57

Do not reopen these closures without stronger contrary evidence:

- D1 detector and T1 TLM geometries are separate and physically closed.
- Native-oxide anodization includes an explicit isolated-mesa anode/contact geometry and microampere current calculation.
- Transient sampling uses 500 MS/s / 2-ns sampling with adaptive record and repetition periods.
- Protocols 1–7 remain a **COMPOSITE LITERATURE-DERIVED UPSTREAM MATERIAL HYPOTHESIS**, not an RP-01 historical growth reconstruction.
- Mesa etch is geometry-matched witness calibrated.
- FTIR uses an explicit full-spectrum inverse-model specification with archived model/coefficient hashes when real data are generated.
- Hall reports Hall quantities and separates weak-field one-carrier reduction from higher-field diagnostic behavior.
- The detector measurement reports both Smith-style terminal field and separately labeled contact-corrected bulk-field estimate.
- Absolute responsivity uses a defined underfilled spectral radiant-power comparator geometry.
- TLM alone does not prove blocking; P37/W1 LBIC is the functional blocking-contact witness gate.
- `A_Dstar` is the inter-contact optical area for direct RP comparison; do not substitute mesa area.
- The historical 1-kHz spectral / ~3-kHz noise-knee ambiguity is preserved rather than silently repaired.

Evidence codes remain `RP`, `SL`, `PT`, `DER`, `SYN`. A `SYN` hard number is a concrete empirical starting hypothesis, not validated process capability.

## Round-58 artifact state

Review artifacts:

- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round58.pdf`
- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round58.tex`

Final PDF state:

- 59 physical pages;
- letter size;
- text-native, openable and unencrypted;
- no XFA/form fields;
- full page-by-page visual inspection completed through 59 pages after final pagination repairs;
- no remaining overfull/underfull LaTeX box warnings in the release compile.

SHA-256:

- PDF `07a367efa3dbd378733d40170a98fe37591560e2cd0241995b946be4cfabfb18`;
- TeX `1aecca413df24ddb545b9e5c8bc1e14afc8d26e80fe14ca5eeea59c530e3889f`.

The TeX source is a conversation review artifact for Round 58; repository Markdown/procedure/calculation files remain the controlled scientific evidence corpus.

## Immediate next work

Use Round 58 as the preferred presentation model. Future technical work should attack remaining `SYN` process values and cross-lineage compatibility, not revert the typography or protocol grammar. Any new scientific correction should be integrated into the LaTeX protocol while preserving the exhaustive-research-reference concept.