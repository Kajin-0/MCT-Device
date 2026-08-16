# Checkpoint after Round 35 — LPE absolute apparatus / charge / trajectory closure

**Date:** 2026-08-16 America/New_York

## Current project state

Round 34 established that P16A rows R04–R07 are among the highest-impact blockers to a traceable first build:

- R04 actual LPE boat/well/source hardware;
- R05 absolute growth charge;
- R06 atmosphere;
- R07 thermal/contact/wipe/cooldown trajectory.

Round 35 investigated whether primary historical literature could close these rows directly.

## Main result

It could not close the historical absolute scale.

Honeywell primary patents now support a stronger and more detailed apparatus topology than previously summarized, including tapered through-wells, substrate-sized recessed regions, plugged growth-solution well, separate Hg-source recess, top/bottom Hg moats and close cover. However, no numerical boat/well dimensions or x≈.29 charge mass were recovered.

The x≈.29 equilibrium anchor remains direct:

- `xL=.082`;
- `yL=.810`;
- `TL=507 °C`;
- `xS≈.29`.

This defines composition, not inventory.

## Strong quantitative transfer evidence retained

### Radhakrishnan 2003

Different modified-slider branch:

- 15×15×1-mm CdZnTe;
- ~10-g synthesized source batch;
- ~4.8-g growth charge/run;
- 3-g HgTe reservoir;
- 6N elements;
- 700°C/8-h synthesis.

Use only as apparatus/mass-scale evidence. Do not area-scale it into the Honeywell branch.

### Harman branches

The 1980 and 1981 Harman papers are now explicitly kept distinct.

Harman/MIT patent data give useful examples connecting:

- supercooling;
- cooling rate;
- contact time;
- substrate size;
- final thickness.

Examples include a ~7-µm film after ~1 min under one trajectory and ~30–33-µm films after ~30 min under a different slow-cooling branch. These demonstrate trajectory sensitivity but do not provide a universal solution mass.

### Fermionics lineage

Same-era UWA work confirms Fermionics-supplied LPE HgCdTe/CdZnTe material. No Fermionics internal process traveler was recovered.

Permanent distinction:

`FERMIONICS MATERIAL PROVENANCE != FERMIONICS PROCESS RECIPE`.

## New controlled closure method

Created:

- `procedures/P30A_LPE_ABSOLUTE_CHARGE_APPARATUS_CALIBRATION_ADDENDUM.md`
- `travelers/P30A_LPE_ABSOLUTE_CHARGE_APPARATUS_CALIBRATION_REGISTER.md`

P30A defines:

1. dimensioned local boat/cover/slider/substrate-recess/well/source/wipe geometry;
2. calibrated geometric well volume and uncertainty;
3. hot thermal/mechanical calibration;
4. numerical local candidate inventory bracket;
5. xL=.082/yL=.810 elemental mass calculation after `M_charge` selection;
6. independent auxiliary Hg-source inventory;
7. gas/purge branch;
8. local liquidus/thermometry calibration;
9. contact/cooling/wipe trajectory matrix;
10. post-run mass balance and source-use genealogy;
11. P06 thickness/x and P05 electrical outcome closure;
12. criteria for moving P16A R04–R07 to `LOCAL-BRANCH-FROZEN`.

## New permanent rule

**Absolute LPE charge is an apparatus coordinate.**

Do not infer it from:

- xL/yL;
- substrate area alone;
- another laboratory's grams;
- a substrate-size ratio.

The local charge becomes executable only after the measured boat geometry/capacity and thermal/contact process are qualified.

## P16A state after Round 35

Still:

`TRACEABLE-FIRST-BUILD-READY = NO`.

R04 remains `APPARATUS-NOT-SELECTED`.

R05–R07 remain `OPEN-CHOICE`.

This is intentional. P30A defines how to close them; no actual laboratory hardware/grams/flows/trajectory have been supplied or qualified.

## Files created/updated in Round 35

Created:

- `procedures/P30A_LPE_ABSOLUTE_CHARGE_APPARATUS_CALIBRATION_ADDENDUM.md`
- `travelers/P30A_LPE_ABSOLUTE_CHARGE_APPARATUS_CALIBRATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND35.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND35.md`
- this checkpoint.

Updated:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`.

## Negative searches to preserve

- No dimensional Honeywell x≈.29 boat drawing recovered from the audited patents.
- No absolute Honeywell x≈.29 growth-charge mass recovered.
- No universal Honeywell Hg-source mass recovered.
- No exact Honeywell N2/H2 flow values recovered.
- No Fermionics internal LPE traveler recovered from same-era UWA/Fermionics lineage searches.
- Harman quantitative trajectory records did not recover a universal growth-solution gram loading.

Do not repeat these searches and then silently fill the missing fields from the Radhakrishnan branch.

## Strongest next action

Proceed with **Round 36: wet-mesa etchant preparation-basis recovery**, centered on P16A R13.

Priority:

1. recover Vanya Srivastav IISc thesis `G25544.pdf` or another primary full-text route;
2. identify the exact source underlying `2% Br2` and `3:1 EG:HBr`;
3. determine percentage basis;
4. determine EG:HBr preparation basis;
5. recover HBr stock assay/concentration;
6. recover mixing order, bath volume/temperature/agitation;
7. recover rinse/quench/dry sequence;
8. preserve near-x≈.3 etch-rate evidence separately from recipe identity;
9. if primary recovery still fails, define a P28A local chemistry-definition/qualification route rather than guessing the historical basis.

This is a more source-recoverable execution blocker than the laboratory-specific absolute LPE charge and should be attacked before another generic process module is added.