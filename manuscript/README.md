# Integrated manual manuscript

Canonical integrated technical source:

`RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md`

## Current publication direction

- Round 52: integrated technical/source draft.
- Round 53: condensed publication presentation — **REJECTED / SUPERSEDED**.
- Round 54: traveler/SOP-with-fill-fields presentation — **REJECTED / SUPERSEDED**.
- Round 55: first hard-number empirical-protocol model; critical defects found.
- Round 56: adversarial repair of geometry, anodization and transient design.
- Round 57: **ACTIVE TARGETED METROLOGY-CLOSURE REVIEW CANDIDATE**.

`RP01-EMPIRICAL-PROTOCOL-ROUND57-REVIEW-CANDIDATE = YES`.

The active publication grammar remains:

`equipment/materials -> hard-number reference recipe -> numbered procedure -> timing -> expected result -> analysis -> troubleshooting -> evidence note`.

No blank traveler fields in the main document.

## Round-57 closure

Round 57 repairs the remaining major characterization/release-gate findings from the Round-56 adversarial re-review:

1. **electric field** — report both Smith-style terminal applied field `E_Smith=V_terminal/L_gap` and a separately labeled TLM-derived contact-corrected `E_bulk,est`;
2. **absolute optical power** — canonical Protocol 18 is an underfilled spectral radiant-power comparator measurement with measured beam profile, <=60-µm 1/e²-equivalent diameter at specified wavelengths, ±10-µm centering and >=99% power overlap inside the 100×300-µm D1 active gap;
3. **functional blocking** — new Protocol 14A / repository P37 supplies an executable LBIC witness test at 80 K, 1.047 µm, ~400 mW/cm² with quantitative bipolar-map criteria.

Secondary repairs include a blocked 2² LPE validation screen across independent source syntheses, geometry-matched wet-etch witness, mathematically defined FTIR depth/gradient coordinates and archived model hashes, finite-width 2-D TLM reduction, explicit wire-saw mechanics, stationarity-tested noise statistics and adaptive transient repetition period.

See:

- `../docs/RP01_EMPIRICAL_PROTOCOL_METROLOGY_CLOSURE_ROUND57.md`;
- `../docs/RP01_GAP_MATRIX_ADDENDUM_ROUND57.md`;
- `../docs/SOURCE_LEDGER_ADDENDUM_ROUND57.md`;
- `../procedures/P37_LBIC_BLOCKING_CONTACT_FUNCTIONAL_QUALIFICATION.md`;
- `../analysis/ftir/ROUND57_FTIR_MODEL_SPECIFICATION.md`;
- `../research/2026-08-16_checkpoint_after_empirical_protocol_round57.md`.

## Evidence rule

- `RP` direct RP-01;
- `SL` same lineage;
- `PT` primary transfer;
- `DER` derived;
- `SYN` explicit synthesized empirical starting implementation.

A hard number remains a hypothesis until the combined process state is experimentally demonstrated. Cross-lineage ancestry is not process validation.

## Physical maturity remains separate

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

## Round-57 artifact state

Review artifact: 41-page monochrome empirical protocol manual.

QA:

- DOCX accessibility `0 high / 0 medium / 0 low`;
- all 41 DOCX-render pages visually inspected;
- final PDF 41 letter-size pages, text-native, openable, unencrypted, zero form fields;
- final PDF render pixel-identical to the inspected LibreOffice PDF at comparison DPI and independently rendered at 200 dpi.

SHA-256:

- DOCX `162f51b424acc2a5754bf11fb615f5077091a03f57b5b468e93be5c0181f3d1e`;
- PDF `92f5ec2a6a05af22f77add2ed10c5dded36162c79b27b7d1dc51392dce1aaca8`.

## Next gate

Continue adversarial review of remaining `SYN` process settings and cross-lineage interactions. Do not undo the dual-field convention, underfilled absolute-power geometry, or LBIC witness gate without stronger contrary primary evidence.