# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 54  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce a source-traceable HgCdTe photodetector fabrication and characterization **bench procedure**, not a condensed review article. The deliverable must expose the detailed P01–P36 procedure corpus as operator-facing SOP modules with equipment/materials, local fill-in fields, numbered actions, in-process measurements, acceptance gates, and retained records.

Canonical historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `manuscript/RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md` — technical Draft 0.2 / Round 52.
2. `docs/RP01_MANUSCRIPT_TECHNICAL_REVIEW_ROUND52.md` — scientific/claim corrections.
3. `docs/RP01_PROCEDURAL_REBUILD_REVIEW_ROUND54.md` — active publication-format disposition.
4. `research/2026-08-16_checkpoint_after_procedural_rebuild_round54.md` — latest checkpoint.
5. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND54.md` and `docs/SOURCE_LEDGER_ADDENDUM_ROUND54.md`.
6. Round-53 publication records only as **rejected presentation history**.

## Current document maturity

- `RP01-INTEGRATED-MANUSCRIPT-DRAFT-READY = YES`.
- `RP01-MANUSCRIPT-ADVERSARIAL-REVIEW-PASSED = YES`.
- `ROUND53-PUBLICATION-PRESENTATION-ACCEPTED = NO`.
- `RP01-PROCEDURAL-MANUAL-CORRECTIVE-CANDIDATE-READY = YES`.

The Round-54 state means a substantially rebuilt operator-facing review candidate exists. It is not yet the final issued manual.

Physical maturity remains unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

## Round-54 corrective artifact

The Round-53 22-page booklet was rejected by the user because it was over-condensed, visually weak, insufficiently procedural, and omitted too much operator detail from the controlled source corpus.

Round 54 rebuilt the publication candidate from P01–P36/P36A rather than merely restyling Round 53.

Current review artifact:

- 47 pages;
- 17 sequential SOP modules;
- 9 engineering schematics tied to apparatus/geometry/measurement logic;
- explicit equipment/materials and incoming-state blocks;
- yellow `MUST FILL BEFORE EXECUTION` local-coordinate fields;
- numbered operator actions;
- in-process measurement requirements;
- `GO / HOLD / REWORK / STOP` gates;
- failure-isolation logic;
- worked calculations/uncertainty template;
- operator release checklists;
- symbols/units and controlled bibliography.

Artifact hashes:

- DOCX SHA-256 `399e51aa26046acfde1de283ce690e23f4dbdef9f293ea534e5478f65ce823e2`.
- PDF SHA-256 `a4d27a11471dfad35a79d60727d0d71c847e26d2b6268209501f30b39ecdeaac`.

QA:

- DOCX rendered and visually inspected through all 47 pages after final edits;
- DOCX accessibility audit: `0 high / 0 medium / 0 low` findings after safe fixes;
- PDF inspector/preflight: 47 pages, letter size, openable, unencrypted, text-native;
- PDF independently rendered at 200 dpi through all 47 pages.

The binary files remain conversation review artifacts; Markdown/procedure/calculation files remain controlled technical source of truth until final issue.

## Permanent control rules

### Execution semantics

`REF-CENTER != EXECUTABLE-LOCAL-SETPOINT`.

Before irreversible execution, all required local material/reagent/tool/geometry/setpoint/endpoint fields must be instantiated and relevant P36/P36A acceptance, genealogy, and EH&S authorization must exist. `TBD`, undefined `%`, `appropriate`, and uncalibrated controller values fail preflight.

### Evidence discipline

Never invent missing values. Keep direct RP-01, same-lineage, primary transfer, derived, reference center, local calibration/qualification, and historical-open evidence distinct. Repetition does not promote evidence class. `Not recovered` does not mean absent.

### LPE numerical authority

`xL=.082, yL=.810, TL=507 °C, xS≈.29`.

Using Hg=200.59, Cd=112.414, Te=127.60 g/mol:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

`M_charge` is apparatus dependent. Do not area-scale another laboratory's charge.

### RIE authority

Direct controller state: parallel-plate Plasma Technology reactor, `CH4/5H2`, total `64 sccm`, `100 mTorr`, `50 W`, `60 s`.

Candidate 1:5 split `10.6667/53.3333 sccm` is interpretive transfer only.

Permanent:

- `50 W != reactor equivalence`;
- `d_etch != d_conv` and lateral `L_conv` is separate;
- report sheet state and independently justified conversion depth;
- `n_conv=N_s/d_conv` only after `d_conv` closure;
- TLM does not by itself prove minority-carrier blocking.

### Detector-performance authority

RP-01 Figures 3/5/6/7 are the same representative detector; exact contact pair remains open.

New D* closure locks `{device, contact pair, gap, width, T, E, package, FOV/background, loading, frequency convention}` unless an explicit measured correction is applied.

The stated `60° FOV` remains historically ambiguous as full versus half angle. `A_Dstar` is defined separately from optical power geometry; preserve covariance when a coordinate is shared.

`24.5 nV/sqrt(Hz)` is the high-frequency g-r level and is not automatically the 1-kHz detector noise because the reported knee is ~3 kHz.

### Dynamics/package authority

No direct RP-01 lifetime curve exists. De-embed source/readout/cable/instrument and evaluate package thermal transfer before assigning a slow pole to minority-carrier lifetime.

## Immediate next work

Use the Round-54 artifact as the active review candidate. Next work should be a **line-by-line scientific/operator audit of this procedural version**, repairing any stage that still omits an operator-critical control or misrepresents evidence. Do not force brevity. Do not return to the Round-53 overview layout. Final issue should occur only after that audit and user acceptance.
