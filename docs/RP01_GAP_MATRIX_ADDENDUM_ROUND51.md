# RP-01 gap-matrix addendum — Round 51 manuscript integration

**Date:** 2026-08-16 America/New_York

## Purpose

Round 51 corrects a structural problem in prior readiness language: absence of a specific laboratory implementation was being allowed to function as if it were an unresolved manuscript-content gap.

A source-traceable process manual can be complete while still requiring an executing laboratory to insert its measured furnace offset, MFC calibration, QCM tooling factor, lithographic dose, bondline geometry, optical view factor, etc.

## New manuscript-state labels

- `MANUSCRIPT-CONTENT-INTEGRATED` — the process step is represented coherently in the integrated manual with its source basis, execution sequence, outputs and acceptance logic.
- `REFERENCE-CENTER-DEFINED` — a literature-grounded first qualification center is stated without mislabeling it as historical identity.
- `LOCAL-EXECUTION-INSTANTIATION-REQUIRED` — one or more quantities physically depend on the executing lab's apparatus/material lot and must be measured before execution.
- `HISTORICAL-IDENTITY-OPEN` — source detail remains unrecovered and limits a literal RP-01 historical-reproduction claim.
- `MANUSCRIPT-CONTRADICTION-OPEN` — incompatible procedure statements remain to be reconciled before final publication.

## Important non-equivalence

`LOCAL-EXECUTION-INSTANTIATION-REQUIRED != MANUSCRIPT-CONTENT-OPEN`.

Similarly:

`MANUSCRIPT-CONTENT-INTEGRATED != TRACEABLE-FIRST-BUILD-READY != HISTORICAL-RP01-REPRODUCED != REPRODUCIBLE-RELEASE`.

The first is a document state. The others are physical/scientific maturity states.

## Round-51 integrated content disposition

| Manual block | Manuscript state | Remaining local/historical boundary |
|---|---|---|
| Reference detector/specification | `MANUSCRIPT-CONTENT-INTEGRATED` | historical measurement temperature/contact-pair details remain open |
| CdZnTe substrate/final surface | `MANUSCRIPT-CONTENT-INTEGRATED`, `REFERENCE-CENTER-DEFINED` | exact RP-01 surface basis/time open; local explicit Br2 recipe required |
| Te-rich LPE | `MANUSCRIPT-CONTENT-INTEGRATED`, `REFERENCE-CENTER-DEFINED` | total charge/boat dimensions/gas/thermal offsets/contact time local |
| As-grown P05/P06 | `MANUSCRIPT-CONTENT-INTEGRATED` | actual Hall/FTIR hardware calibration local |
| Hg anneal | `MANUSCRIPT-CONTENT-INTEGRATED`, `REFERENCE-CENTER-DEFINED` | actual ampoule/Hg inventory/T offsets and final kinetics local |
| Mask 1 | `MANUSCRIPT-CONTENT-INTEGRATED`, `REFERENCE-CENTER-DEFINED` | exact historical resist open; current resist/dose/developer local |
| Wet mesa | `MANUSCRIPT-CONTENT-INTEGRATED`, `REFERENCE-CENTER-DEFINED` | Br2/EG:HBr basis and HBr assay historical-open; local formulation mandatory |
| Anodic oxide | `MANUSCRIPT-CONTENT-INTEGRATED`, `REFERENCE-CENTER-DEFINED` | EG:H2O basis historical-open; cell/A_exposed local |
| Mask 2 | `MANUSCRIPT-CONTENT-INTEGRATED` | resist identity/exposure/developer/chlorobenzene order/lift-off solvent local/historical open |
| RIE | `MANUSCRIPT-CONTENT-INTEGRATED` | direct controller center fixed; reactor physics/MFC split/self-bias/t_clear local |
| Cr/Au | `MANUSCRIPT-CONTENT-INTEGRATED` | 30/270 nm fixed; method/vacuum/rates/tooling factor local |
| TLM/geometry/DC | `MANUSCRIPT-CONTENT-INTEGRATED` | exact historical performance pair open; actual dimensions always measured |
| Singulation | `MANUSCRIPT-CONTENT-INTEGRATED`, `REFERENCE-CENTER-DEFINED` | exact historical method open; local functional edge exclusion required |
| Package | `MANUSCRIPT-CONTENT-INTEGRATED`, `REFERENCE-CENTER-DEFINED` | historical construction open; local thermal/mechanical implementation required |
| Responsivity | `MANUSCRIPT-CONTENT-INTEGRATED` | actual calibrated optical chain local |
| Noise/NEP/D* | `MANUSCRIPT-CONTENT-INTEGRATED` | historical 1-kHz noise implementation open; local PSD chain required |
| Dynamics/lifetime | `MANUSCRIPT-CONTENT-INTEGRATED` | RP-01 lifetime open; local de-embedded measurement required |

## Round-51 manuscript result

`RP01-INTEGRATED-MANUSCRIPT-DRAFT-READY = YES`.

This means the technical process can now be reviewed as one coherent document.

It does **not** promote any physical build/readiness/release state.

## Remaining pre-final-publication gaps

The high-value remaining work is now:

1. contradiction and unit/symbol audit across the integrated manuscript and controlled procedures;
2. consolidated uncertainty/examples appendix;
3. complete bibliography extraction from the source ledger;
4. final process-flow/device figures and equipment schematics where useful;
5. operator checklists/travelers as appendices;
6. adversarial scientific review of the integrated manuscript;
7. final professional typesetting/PDF generation.

Further literature search should be targeted only at a specific manuscript claim or contradiction, not used as an open-ended reason to postpone integration.
