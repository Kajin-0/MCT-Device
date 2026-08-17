# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 53  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce the final source-traceable HgCdTe photodetector fabrication and characterization procedure paper/booklet. Prioritize the finished manual over new infrastructure work.

Canonical historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `manuscript/RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md` — technical Draft 0.2 / Round 52.
2. `docs/RP01_MANUSCRIPT_TECHNICAL_REVIEW_ROUND52.md` — adversarial technical corrections.
3. `docs/RP01_PUBLICATION_ASSEMBLY_REVIEW_ROUND53.md` — publication/render disposition.
4. `research/2026-08-16_checkpoint_after_publication_assembly_round53.md` — latest checkpoint.
5. `docs/SOURCE_LEDGER_ADDENDUM_ROUND53.md` — publication bibliography policy.

## Current manuscript/document maturity

- `RP01-INTEGRATED-MANUSCRIPT-DRAFT-READY = YES`.
- `RP01-MANUSCRIPT-ADVERSARIAL-REVIEW-PASSED = YES`.
- `RP01-PUBLICATION-ASSEMBLY-CANDIDATE-READY = YES`.

These are document states only.

Physical maturity remains:

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

## Round-53 publication candidate

A 22-page professional DOCX/PDF candidate was produced and visually QA'd. It contains:

- claim/execution hierarchy;
- reference detector table;
- process flow from CdZnTe receipt through final characterization;
- five deterministic engineering schematics;
- qualification/local-instantiation matrices;
- ten worked calculations/uncertainty examples;
- six operator release checklists;
- symbol/unit/reporting conventions;
- controlled numbered bibliography;
- deliberately open historical identities.

Artifact hashes at render gate:

- PDF SHA-256 `63b03f0d6303071eeda52bfdd673d8f840a1ab7eff50453d02cf2e7e60ddadb3`.
- DOCX SHA-256 `5f9441141badbcb78714bf8eb2766640cdee47aa07612e450456476dea2b188c`.

The conversation artifacts are review copies; repository Markdown/procedures/calculations remain technical source of truth until final issue.

## Permanent control rules

### Reference center versus execution

`REF-CENTER != EXECUTABLE-LOCAL-SETPOINT`.

Before irreversible execution, all required local material/reagent/tool/geometry/setpoint/endpoint fields must be instantiated and relevant P36/P36A acceptance + genealogy + EH&S authorization must exist.

### Evidence discipline

Never invent missing values. Keep direct RP-01, same-lineage, primary transfer, derived, reference center, local calibration/qualification and historical-open evidence distinct. Repetition does not promote evidence class. `Not recovered` does not mean absent.

### LPE authority

Tie-line center:

`xL=.082, yL=.810, TL=507 °C, xS≈.29`.

Authoritative mass convention:

- Hg 200.59 g/mol;
- Cd 112.414 g/mol;
- Te 127.60 g/mol;
- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

`M_charge` is apparatus dependent. Do not area-scale another laboratory's charge.

### RIE authority

Direct controller state:

`CH4/5H2, 64 sccm total, 100 mTorr, 50 W, 60 s`, parallel-plate Plasma Technology reactor.

Candidate 1:5 split -> `10.6667/53.3333 sccm` is interpretive transfer only.

Permanent:

- `50 W != reactor equivalence`;
- physical recession `d_etch != d_conv`;
- report sheet state and independently justified conversion depth;
- `n_conv=N_s/d_conv` only after `d_conv` closure;
- TLM does not by itself prove minority-carrier blocking.

### Detector comparison authority

RP-01 Figures 3/5/6/7 are the same representative detector; exact contact pair remains open.

New D* closure locks:

`{device, contact pair, gap, width, T, E, package, FOV/background, loading, frequency convention}`

unless a measured correction is explicitly applied.

60° FOV remains historically ambiguous as full versus half angle; physical geometry must be recorded.

Define `A_Dstar` separately from optical power geometry; retain covariance when shared.

`24.5 nV/sqrt(Hz)` is the high-frequency g-r level and is not automatically the 1-kHz detector noise because the reported knee is ~3 kHz.

### Dynamics/package authority

No direct RP-01 lifetime curve exists. De-embed source/readout/cable/instrument and evaluate package thermal transfer before calling a slow pole minority-carrier lifetime.

## Known housekeeping item

One section of P30A still carries an older ppm-scale rounded mass-fraction triplet. `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md` and Draft 0.2 are authoritative. Repair P30A in a later text-cleanup commit; do not let it override the calculation module.

## Immediate next work — Round 54

Do a **content-density/final editorial adversarial audit**, not a broad new research loop:

1. compare the 22-page publication candidate against Draft 0.2 and P01–P36A;
2. identify any operator-critical information lost by condensation;
3. expand only where omission changes a decision, endpoint, evidence class, calculation convention or acceptance gate;
4. optionally repair P30A's known rounded-value wording;
5. freeze bibliography/captions/symbol usage;
6. render and preflight the final-layout candidate again;
7. only then consider a final issued booklet state.

Targeted source recovery is allowed only when a specific final-booklet claim materially requires it.