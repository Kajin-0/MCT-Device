# P03G - Honeywell / semiclosed-slider full-text LPE addendum

**Status:** `PT` PROCESS-FAMILY EVIDENCE. Supplements P03/P03A-P03F/P30/P30A.

## 1. Purpose

Integrate Schmit-Hager-Wood 1982 and Nemirovsky et al. 1982 without converting either branch into a synthetic RP-01 recipe.

## 2. Honeywell 1982 branch

Directly reported apparatus/process state:

- high-purity graphite horizontal slider;
- horizontal quartz tube;
- flowing high-purity H2 at atmospheric pressure;
- externally temperature-regulated furnace;
- push-rod slider actuation;
- previously compounded/homogenized Te-rich solution;
- polished (111) CdTe substrates, 1 mm thick, typically 1 x 1 cm or 2 x 3 cm;
- charge heated above its liquidus, typically near 500 C;
- furnace lowered below liquidus before contact;
- solution translated over substrate;
- growth is isothermal and driven by supercooling;
- solution translated away at the end of the chosen growth time.

Process-family behavior:

- Te fraction y approximately 0.8;
- usual growth times ~1-20 min for layers up to about 30 um;
- thickness up to ~50 um reported;
- initial growth rate several um/min, falling substantially after approximately 15 min;
- run-to-run x control demonstrated;
- strong within-layer composition uniformity demonstrated.

### Transfer rule

These values strengthen the Honeywell topology and process-control family. They do **not** close:

- well diameter/depth/volume;
- total source charge mass;
- H2 flow in sccm;
- slider clearance;
- slider velocity;
- exact x=.29 growth supercooling/time;
- wipe hardware;
- source reuse history.

## 3. Nemirovsky 1982 semiclosed branch

Directly reported process-family coordinates:

- semiclosed graphite slider;
- HgTe reservoir approximately 4.5 g;
- growth solution approximately 3.5 g;
- cover/groove vapor communication between reservoir and solution region;
- reservoir replaced every run;
- growth solution reused for several, approximately five, runs;
- typical reservoir mass decrease approximately 20% over a 2-3 h cycle near 460 C;
- substrate size approximately 12 x 14 mm.

Reported thermal branch:

- equilibration approximately 463 C;
- about 5 C supercooling;
- growth approximately 458 -> 455 C;
- cooling approximately 0.25 C/min;
- approximately 10-um layer in 15 min.

The source also reports a pre-load branch with 0.3-um Al2O3 polishing followed by 10% Br2/methanol for 10-15 s immediately before loading.

### Critical observation: pre-contact vapor exposure

The work observed deposition/crystallites on substrates during the equilibration environment even before intentional solution contact. Therefore substrate state during equilibration cannot be treated as automatically unchanged.

## 4. New traveler fields

For every local x approximately .30 LPE run add/retain:

- `solution_use_number`;
- `Hg_source_use_number`;
- `m_Hg_source_pre`, `m_Hg_source_post`;
- `m_solution_pre`, `m_solution_post`;
- `substrate_position_during_equilibration`;
- `substrate_vapor_exposure_time`;
- precontact witness result where used;
- whether deliberate melt-back occurred;
- melt-back duration/thermal state;
- post-run morphology associated with source-use number.

## 5. Qualification experiment

Before source reuse is allowed, execute a source-age study at fixed nominal growth state. At minimum compare early and later source-use numbers while recording:

- solution and Hg-source mass change;
- actual liquidus/thermal trace;
- mean x and x map;
- thickness and thickness map;
- residual melt/morphology;
- post-anneal Hall state.

Do not pool source-use numbers if drift is observable.

## 6. Evidence limits

- Honeywell 1982 is `PT` because it is upstream Honeywell process-family evidence, not the Smith/RP-01 fabrication paper.
- Nemirovsky 1982 is `PT` from another laboratory.
- Neither paper closes historical Fermionics source genealogy, machine dimensions or the exact recipe used for the RP-01 starting material.