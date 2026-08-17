# Integrated manual manuscript

Canonical integrated technical source:

`RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md`

## Current publication direction

- Round 52: integrated technical/source draft.
- Round 53: condensed publication presentation — **REJECTED / SUPERSEDED**.
- Round 54: traveler/SOP-with-fill-fields presentation — **REJECTED / SUPERSEDED**.
- Round 55: hard-number empirical protocol model — important structural advance, but adversarial review found three release-blocking defects.
- Round 56: **ACTIVE ADVERSARIALLY REPAIRED REVIEW CANDIDATE**.

`RP01-EMPIRICAL-PROTOCOL-ROUND56-REVIEW-CANDIDATE = YES`.

Round 56 retains the protocol-paper grammar:

`equipment/materials -> hard-number reference recipe -> numbered procedure -> timing -> expected result -> analysis -> troubleshooting -> evidence note`.

The main body contains no blank traveler fields.

## Round-56 scientific disposition

The three Round-55 blocker defects are repaired in the publication:

1. detector and TLM mask geometries are physically separated (`D1=900×500 µm`, `T1=5000×500 µm`);
2. anodization now specifies an isolated-mesa temporary-contact fixture, wetted-area equation and microampere current scale;
3. transient acquisition now uses 500 MS/s / 2-ns sampling and an adaptive record >=10× the slowest fitted detector pole.

The upstream material section is explicitly labeled a **composite literature-derived upstream material hypothesis**, because Smith et al. purchased their starting Fermionics LPE material rather than disclosing its growth traveler.

Other major repairs include same-bath witness-calibrated mesa timing, explicit FTIR inverse-model controls, Hall-density terminology, D* active-area normalization, anti-alias/PSD confidence controls, self-heating extrapolation, reduced false precision, value-level provenance, and explicit research continuation gates.

See:

- `../docs/RP01_EMPIRICAL_PROTOCOL_REPAIR_ROUND56.md`;
- `../docs/RP01_GAP_MATRIX_ADDENDUM_ROUND56.md`;
- `../docs/SOURCE_LEDGER_ADDENDUM_ROUND56.md`;
- `../research/2026-08-16_checkpoint_after_empirical_protocol_round56.md`.

## Governing evidence rule

- `RP` direct RP-01;
- `SL` same lineage;
- `PT` primary transfer;
- `DER` derived;
- `SYN` explicit synthesized empirical starting implementation.

A hard number is not validated merely because it has literature ancestry. Cross-lineage combinations remain hypotheses until the combined process is empirically tested.

## Physical maturity remains separate

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

## Next publication gate

Perform another adversarial audit of the remaining SYN values and transfer interactions. Preserve concrete starting numbers where defensible, but replace any weak composite value with stronger primary evidence or a better physically justified hard-number experiment. Do not return to blank-field formatting and do not label the document a validated reproducible fabrication manual without empirical execution.
