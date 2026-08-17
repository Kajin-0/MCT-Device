# MCT-Device

A source-controlled effort to build an **Exhaustive Empirical Fabrication Protocol (EEFP)** for HgCdTe (MCT) infrared photodetectors, centered on a fully traceable research implementation of the Smith–Winchester–Musca–Dell–Faraone RP-01 photoconductor architecture.

## Objective

The target is not a generic literature review and not a document made to look complete by filling every blank with a number. Every consequential operation is classified by material state, apparatus geometry, thermal/chemical/electrical history, metrology, uncertainty, failure response and evidence provenance.

A process is not reproducible merely because every field contains a number. Values from different HgCdTe laboratories must not be combined as if they were one historical recipe.

## Reference architecture

RP-01 is anchored to:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

The reconstructed route is:

`CdZnTe qualification -> surface preparation -> Te-rich horizontal-slider LPE -> FTIR/Hall -> Hg-rich anneal -> lithography -> wet mesa -> native oxide -> RIE blocking contacts -> Cr/Au -> TLM/LBIC -> singulation/package -> DC/responsivity/noise/dynamics`.

## Current maturity

- Released visual baseline body: **Round 61**, 74 pages.
- Current evidence/continuity layer: **Round 63**.
- `ROUND62-FULLTEXT-EVIDENCE-INTEGRATION = COMPLETE`.
- `ROUND63-TARGETED-LPE-CLOSURE = COMPLETE`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `END-TO-END-EMPIRICALLY-VALIDATED = NO`.

The negative states are deliberate. The repository contains extensive executable procedures and qualification logic, but the composite process has not been executed end-to-end in one laboratory.

## Evidence vocabulary

- **RP** — direct Smith/RP-01 evidence.
- **SL** — same UWA/Faraone/Dell/Smith process-lineage primary evidence.
- **PT** — primary transfer evidence from another apparatus/laboratory or official source.
- **DER** — transparent derivation.
- **SYN** — explicit local implementation synthesized from evidence/physics.
- **OPEN** — consequential coordinate for which no defensible number is presently supported.

`OPEN` is a valid scientific state. A modern local experiment can establish local `SYN`; it cannot retroactively establish historical identity.

## Read first

1. `AGENTS.md`
2. `docs/RP01_TARGETED_LPE_CLOSURE_ROUND63.md`
3. `research/2026-08-17_checkpoint_after_targeted_lpe_closure_round63.md`
4. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND63.md`
5. `docs/SOURCE_LEDGER_ADDENDUM_ROUND63.md`
6. `procedures/P03F_SUH_SHINOHARA_X030_LPE_FULLTEXT_ADDENDUM.md`
7. Round-62 and Round-61 closure documents.
8. Round-57 metrology specifications and detailed P01–P37 procedures.

## Round-63 LPE closure

Round 62 identified Suh 1992 and Shinohara 1994 as the final high-value paper-level LPE targets. Both are now recovered.

### Suh 1992

Adds an independent x≈0.30 Te-rich growth branch:

- solution approximately `Hg0.158Cd0.012Te0.830` (`xL≈0.0706, yL=.830`);
- growth about `500–489 °C`;
- source synthesis `700 °C / 12 h` in vacuum-sealed quartz, water quenched;
- ~2.5-g run solution;
- graphite vapor-throttle button between solution and HgTe wells;
- ~2-mm central-hole PT branch for near-zero solution-mass change at x≈0.30;
- contact ~1 °C below liquidus and ~0.3 °C/min thermal ramp;
- published x≈0.304, run-to-run sigma≈0.003 and spatial variation ~±0.002.

The 2-mm dimension is apparatus-specific PT evidence, not an RP-01 historical dimension.

### Shinohara 1994

Adds the strongest numerical wipe geometry yet recovered:

- x≈0.31 equilibrium-cooling branch;
- 10×10×1-mm Cd0.97Zn0.03Te substrate;
- 0.15 K/min;
- complete 10×10-mm wipe;
- ~20-µm slider-bottom/substrate-surface clearance;
- 20–25-µm observed equilibrium-branch range;
- <~5-µm clearance-variation warning;
- ~4-µm layer, ~2-µm interdiffusion region.

It also directly measures Hg source/reservoir mass behavior and reports ~0.014-g source-liquid loss during a 30-min growth branch despite Hg-vapor supply.

Historical RP-01/Fermionics clearance remains OPEN; a relevant numerical PT branch now exists.

## Round-62 evidence retained

Round 62 reviewed nineteen full papers and strengthened:

- graphite cleaning/slider mechanics (Astles);
- Hg reservoir thermochemical control (Chiang/Chen);
- slide-out/post-separation morphology (Radhakrishnan/Parker);
- CdZnTe defect and lattice-match screening (Everson/Tobin/Tranchart/Bruder);
- Hg-rich anneal kinetics (Chandra/Schaake/Kinch);
- anodic oxide electrical/process state (Stahle/Nemirovsky/Ngoc);
- same-UWA RIE/LBIC physical state (Siliquini);
- contact noise (Beck);
- HgCdTe-PC package thermal conductance (Bartoli);
- FTIR mapping/inversion discipline (Gopal/Chang).

## Remaining documentary frontier

The major remaining unknowns are now mostly archival/apparatus-specific:

- exact RP-01/Fermionics LPE machine drawing and numerical dimension stack;
- historical slider/base/epilayer clearance and Hg-vapor throttle geometry;
- historical well area/melt depth and Hg-source vapor geometry;
- source-synthesis ampoule geometry/free volume/hot pressure and exact historical preparation route;
- historical anodization electrode geometry;
- RP-01 RIE reactor/electrode/RF/self-bias/thermal/chamber state;
- historical Cr/Au evaporator geometry;
- original RP-01 cryostat/package/readout implementation.

Do not close these by analogy.

## Search disposition

Another broad literature sweep is not recommended. Highest-value future work is archival recovery or deliberate local qualification.

## Source-file provenance

Publisher PDFs are not redistributed in the repository. Exact reviewed byte identities are recorded in:

- `research/2026-08-17_round62_source_acquisition_sha256_manifest.md`
- `research/2026-08-17_round63_targeted_lpe_source_sha256_manifest.md`

so future legally obtained copies can be verified against the exact sources used for evidence extraction.