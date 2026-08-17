# Round-63 controlled PDF release manifest

**Date:** 2026-08-17 America/New_York

## Artifact identity

- Filename: `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round63.pdf`
- Physical pages: `82`
- Page size: US Letter (`612 × 792 pt`)
- SHA-256: `95b698db8c0c0f2d85da708c21b9f3298886d6f207f1aa6ebe20c9899f03297c`
- Openable/encrypted: openable, not encrypted
- Forms/XFA: none
- Fonts: embedded in the generated Round-63 material; baseline body retains the released Round-61 font state

## Controlled-document construction

The original Round-61 TeX source is not currently present in the repository. The Round-63 artifact therefore uses an audit-preserving controlled construction:

1. three-page Round-63 publication/evidence front matter;
2. the released 74-page Round-61 PDF body, visually unchanged;
3. five-page controlled Round-62/63 evidence supplement and supersession map.

The extracted final pages corresponding to the 74-page Round-61 body were rendered against the supplied Round-61 baseline at 100 dpi using the project PDF diff tool. Result:

- pages compared: `74`;
- changed pages: `0`;
- pixel change: `0%` on every compared page.

This verifies that the baseline body was not accidentally restyled or altered during Round-63 assembly.

## Source identities

The Round-63 targeted source hashes are recorded separately in:

`research/2026-08-17_round63_targeted_lpe_source_sha256_manifest.md`.

## Distribution note

The generated PDF is delivered as the controlled Round-63 review artifact. Publisher source PDFs are not redistributed by the repository.