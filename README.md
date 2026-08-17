# MCT-Device

A source-controlled effort to build an **Exhaustive Empirical Fabrication Protocol (EEFP)** for HgCdTe (MCT) infrared photodetectors, centered on a fully traceable research implementation of the Smith–Winchester–Musca–Dell–Faraone RP-01 photoconductor architecture.

## Objective

The target is not a generic literature review and not a document made to look complete by filling every blank with a number.

The repository is intended to state, for every consequential operation:

- incoming material and surface state;
- apparatus topology and physically relevant geometry;
- chemistry, atmosphere, pressure, flow and thermal history;
- electrical/plasma state where applicable;
- setpoints, times and trajectories with evidence classification;
- metrology before/after the operation;
- equations and uncertainty treatment;
- acceptance, rejection and escalation logic;
- failure mechanisms and diagnostics;
- raw-data/provenance requirements;
- which coordinates are historical, transferred, derived, synthesized locally, or still genuinely unknown.

A process is not reproducible merely because every field contains a number. Parameters from different HgCdTe laboratories or apparatuses must not be combined as if they were one historical recipe.

## Current reference architecture

**RP-01** is anchored to:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

The present project reconstructs the complete research path around that device:

`CdZnTe qualification -> final substrate surface -> Te-rich horizontal-slider LPE -> FTIR/Hall -> Hg-rich low-temperature anneal -> FTIR/Hall -> Mask 1 -> wet mesa -> native anodic oxide -> Mask 2 -> localized CH4/H2 RIE -> Cr/Au -> TLM/LBIC -> bare-device characterization -> singulation -> cryogenic package -> absolute responsivity/noise/D*/dynamics`.

## Current maturity

- Current typeset EEFP artifact: **Round 61**, 74 pages.
- Current repository continuity/evidence layer: **Round 62**.
- `ROUND62-FULLTEXT-EVIDENCE-INTEGRATION = COMPLETE`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `END-TO-END-EMPIRICALLY-VALIDATED = NO`.

The negative states are deliberate. The repository now contains extensive procedures, qualification experiments, apparatus-state definitions, travelers, analytical sensitivity/DOE machinery and digital provenance controls, but no claim is made that the composite process has already been executed end-to-end in one laboratory.

## Evidence vocabulary

Current publication-layer evidence states are:

- **RP** — directly reported for the Smith/RP-01 reference process.
- **SL** — same UWA/Faraone/Dell/Smith process-lineage primary evidence.
- **PT** — primary transfer evidence from another laboratory/apparatus or an official technical source.
- **DER** — transparent derivation from better-established inputs.
- **SYN** — explicit locally executable implementation synthesized from evidence and physics.
- **OPEN** — experimentally consequential coordinate for which no defensible numerical value is presently supported.

`OPEN` is a valid scientific state. A modern local experiment can establish a local `SYN` implementation; it cannot retroactively prove what a historical laboratory used.

## Read first

For the current project state:

1. `AGENTS.md`
2. `docs/RP01_FULLTEXT_SOURCE_ACQUISITION_ROUND62.md`
3. `research/2026-08-17_checkpoint_after_fulltext_source_acquisition_round62.md`
4. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND62.md`
5. `docs/SOURCE_LEDGER_ADDENDUM_ROUND62.md`
6. `docs/RP01_CONSEQUENTIAL_COORDINATE_CLOSURE_ROUND61.md`
7. Round-57 metrology closure documents and the detailed P01–P37 procedures.

## Repository structure

- `AGENTS.md` — current continuity state and operating rules.
- `docs/` — architecture, evidence/gap ledgers, round-specific closure reviews, minimum-lab capability and provenance specifications.
- `procedures/` — P01–P37 process, metrology, qualification, DOE and integration modules.
- `travelers/` — executable qualification registers and end-to-end genealogy/traveler structures.
- `calculations/` — sensitivity, uncertainty, Jacobian, material-allocation and physics calculations.
- `analysis/` — controlled analysis specifications such as FTIR inversion.
- `research/` — dated checkpoints, source-recovery records, rejected inferences and handoffs.
- `provenance/`, `schemas/`, `tools/` — machine-readable provenance model, validation and reference transactional implementation.

## Current documentary frontier

Round 62 reviewed nineteen recovered full papers. The strongest new evidence includes:

- a real HgCdTe-LPE graphite cleaning/slider branch from Astles et al.;
- independently heated Hg-reservoir slider architectures from Chiang/Chen;
- direct slide-out/wipe/post-separation morphology evidence from Radhakrishnan;
- an executable `(111)B` CdZnTe defect-screening branch from Everson;
- room-temperature versus growth-temperature lattice-match evidence from Tobin;
- diffusion-like Hg-rich anneal scaling from Chandra/Schaake/Kinch;
- galvanostatic-to-constant-voltage anodization evidence from Nemirovsky/Kidron;
- a complete same-UWA RIE/LBIC physical state from Siliquini;
- quantitative HgCdTe-PC bond-layer thermal conductance from Bartoli.

These strengthen `PT`/`SL` evidence without closing the remaining historical apparatus gaps.

## Highest-priority remaining OPEN coordinates

The most consequential remaining documentary unknowns include:

- exact RP-01 LPE boat/well/recess numerical geometry;
- x≈0.30 melt depth/geometry relation;
- historical Hg-source exposed area/location/vapor volume;
- historical graphite grade/roughness/exact clean;
- source-synthesis ampoule geometry/free volume/hot pressure;
- historical anodization electrode geometry and solution-voltage drop;
- RP-01 RIE model/electrode geometry/RF frequency/self-bias/sample temperature/chamber seasoning;
- historical Cr/Au evaporator source/QCM/sample geometry;
- original RP-01 cryostat/package/readout thermal implementation.

Do not close these by analogy.

## Next documentary targets

The next source-acquisition pass should be narrow rather than broad:

1. Suh et al. full slider-LPE composition-control paper.
2. Shinohara et al. full Hg-loss compensation/wipe-off paper.
3. Honeywell/Fermionics/UWA machine drawings and laboratory notebooks.
4. TI anodization-cell records.
5. UWA Plasma Technology run sheets/manuals.
6. Original RP-01 evaporator/QCM and cryostat/package records.

## Source-file provenance

Publisher PDFs used in Round 62 are not redistributed in this repository. Their exact reviewed byte identities are recorded in:

`research/2026-08-17_round62_source_acquisition_sha256_manifest.md`

so a future legally obtained copy can be checked against the source used for the evidence extraction.