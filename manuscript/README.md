# Integrated manual manuscript

Canonical integrated technical source:

`RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md`

## Current publication direction

- Round 52: integrated technical/source draft.
- Round 53: condensed booklet — rejected.
- Round 54: traveler/SOP-with-fill-fields — rejected.
- Round 55: first hard-number empirical-protocol model; major defects found.
- Round 56: adversarial scientific repair.
- Round 57: targeted metrology closure; controlling scientific/metrology baseline.
- Round 58: native-LaTeX presentation rebuild.
- Round 59: **ACTIVE OPERATOR-COMPLETENESS / MATHEMATICAL-TYPESETTING CANDIDATE**.

`RP01-EXHAUSTIVE-EMPIRICAL-PROTOCOL-ROUND59-OPERATOR-CANDIDATE = YES`.

## What Round 59 is

Round 59 preserves the document class established in Round 58: an **exhaustive research-fabrication protocol** rather than a conventional paper or factory traveler.

Its goal is to combine:

- publication-level analytical clarity;
- SOP-level executable sequencing;
- process-development-notebook completeness;
- explicit evidence/transfer classification;
- professional mathematical typesetting.

The protocol grammar remains:

`objective -> starting state -> equipment/materials -> hard-number reference recipe -> numbered procedure -> timing -> expected result -> analysis -> troubleshooting -> evidence/transfer limits`.

The main body contains no blank traveler fields.

## Round-59 changes

### Complete mathematical cleanup

Round 59 removes residual ASCII/pseudo-code mathematics from prose, tables, gates and appendices. Symbols, inequalities, tolerances, units and equations now use native LaTeX consistently.

A targeted residual-pattern scan after the final build returned no matches for the code-like notation patterns identified during the Round-58 review.

### Operator-question audit

The main protocols were audited against deeper procedure modules to answer more of the questions a competent researcher would ask while standing at the tool.

New explicit SYN reference details include:

- guarded substrate leakage/isolation measurement;
- source-synthesis leak/vacuum/ramp/cooldown requirements;
- LPE purge endpoints, gas-flow scaling, thermometry and slider actuation;
- complete first Mask-1 spin/exposure/developer implementation;
- complete first Mask-2 spin/exposure/developer/undercut implementation;
- RIE carrier placement and reactor-equivalence screening;
- thermal-evaporation source distance, sample rotation and cooldown;
- package seat flatness, bondline, tilt, wire and pull-test screens;
- lock-in settling/stability/uncertainty targets for absolute responsivity.

These new values remain `SYN` research starting coordinates unless a different evidence class is stated.

### Explicit apparatus closure instead of invented values

Where a number cannot responsibly be recovered or synthesized, the manual no longer hides the problem behind phrases such as “use the qualified method.” Appendix C lists the exact drawing/calibration/qualification record required to close the coordinate.

Examples include:

- source-synthesis ampoule geometry and pressure/temperature qualification;
- Honeywell-derived boat dimensions, well volumes, clearances and thermal map;
- tool-specific lithography calibration;
- RIE electrode/carrier/self-bias/thermal state;
- QCM/source/holder geometry for metallization;
- package adhesive/carrier/wire-bond construction;
- optical train/reference-detector implementation;
- noise/transient analog-chain and analysis-code identity.

This is an explicit research-gap list, not a fill-in form.

## Scientific state inherited from Round 57

Round 59 does not overturn the established scientific/metrology closures:

- D1/T1 geometry separation;
- explicit anodization current/contact geometry;
- 500-MS/s transient acquisition with adaptive record/repetition period;
- upstream LPE branch explicitly treated as a composite literature-derived hypothesis;
- witness-calibrated mesa etch;
- explicit FTIR inverse model;
- Hall-density/mobility terminology and weak-field-first analysis;
- dual Smith-terminal/contact-corrected field reporting;
- underfilled absolute radiant-power comparator geometry;
- P37/W1 LBIC functional blocking witness;
- finite-width TLM treatment;
- inter-contact D* area convention;
- preserved 1-kHz/~3-kHz historical noise ambiguity.

Evidence codes remain `RP`, `SL`, `PT`, `DER`, `SYN`.

## Round-59 review artifact

- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round59.pdf`
- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round59.tex`

QA:

- 62 physical PDF pages;
- letter size;
- text-native, openable and unencrypted;
- no form/XFA fields;
- all fonts embedded;
- all 62 final pages visually inspected after the final pagination correction;
- no remaining overfull/underfull LaTeX box warnings;
- the intermediate nearly blank anodization evidence page was removed by consolidating its evidence into the preceding protocol section.

SHA-256:

- PDF `bb51def36f7fdc8c25d595c8789286dd112938664adb0d96f5605141615d71ee`;
- TeX `352c170cca4c42d0bdeaea91878aa79e7020cdc12199ce69179ca81437dcc11b`.

See:

- `../docs/RP01_OPERATOR_COMPLETENESS_LATEX_ROUND59.md`;
- `../docs/RP01_GAP_MATRIX_ADDENDUM_ROUND59.md`;
- `../docs/SOURCE_LEDGER_ADDENDUM_ROUND59.md`;
- `../research/2026-08-17_checkpoint_after_operator_completeness_round59.md`;
- Round-57 scientific/metrology records for controlling background.

## Physical maturity remains separate

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

## Next gate

Use the Round-59 LaTeX/operator model as the preferred presentation layer. Future revisions should adversarially test the new `SYN` execution coordinates and close the explicit apparatus-coordinate appendix from stronger primary evidence or actual local metrology. Do not regress to vague operator prose, blank fields, or code-like mathematics.
