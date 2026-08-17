# AGENTS.md - MCT-Device continuity record

**Current continuity round:** 64  
**Date:** 2026-08-17 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Produce an **Exhaustive Empirical Fabrication Protocol (EEFP)** for HgCdTe photoconductor fabrication and characterization: a literature-derived scientific methods monograph with SOP-level specificity, explicit metrology, failure response and evidence provenance.

The project is not a claim that a composite process has already been reproduced in one laboratory. Never assign undocumented historical values merely to remove blanks.

Canonical downstream anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455-462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_SAME_LINEAGE_RIE_PASSIVATION_CLOSURE_ROUND64.md`
2. `research/2026-08-17_checkpoint_after_same_lineage_rie_passivation_round64.md`
3. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND64.md`
4. `docs/SOURCE_LEDGER_ADDENDUM_ROUND64.md`
5. `procedures/P08H_UWA_RIE_LBIC_FULLTEXT_CLOSURE_ADDENDUM.md`
6. `procedures/P25B_PHOTOCONDUCTOR_PASSIVATION_SHUNT_NOISE_ADDENDUM.md`
7. `procedures/P03G_HONEYWELL_TECHNION_SLIDER_LPE_FULLTEXT_ADDENDUM.md`
8. `procedures/P26B_AU_HGCDTE_INTERFACE_CHEMISTRY_ADDENDUM.md`
9. Round-63 targeted LPE layer:
   - `docs/RP01_TARGETED_LPE_CLOSURE_ROUND63.md`
   - `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND63.md`
   - `docs/SOURCE_LEDGER_ADDENDUM_ROUND63.md`
   - `procedures/P03F_SUH_SHINOHARA_X030_LPE_FULLTEXT_ADDENDUM.md`
10. Round-62 full-text layer and Round-61 consequential-coordinate closure remain controlling where later rounds do not supersede them.
11. Round-57 metrology definitions remain controlling unless explicitly superseded.

## Current publication / maturity state

- Released visual baseline body: **Round 61, 74 pages**.
- `ROUND62-FULLTEXT-EVIDENCE-INTEGRATION = COMPLETE`.
- `ROUND63-TARGETED-LPE-CLOSURE = COMPLETE`.
- `ROUND64-SAME-LINEAGE-RIE-PASSIVATION-CLOSURE = COMPLETE`.
- Round-64 controlled PDF preserves the prior controlled body and appends explicit Round-64 supersession material because the original Round-61 TeX is not present in the repository.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `END-TO-END-EMPIRICALLY-VALIDATED = NO`.

No new physical HgCdTe experiment was performed in Round 62-64.

## Evidence vocabulary

Use exactly:

- `RP` - direct Smith/RP-01 evidence.
- `SL` - same UWA/Faraone/Dell/Smith process-lineage primary evidence.
- `PT` - primary transfer evidence from another apparatus/laboratory or official source.
- `DER` - transparent derivation.
- `SYN` - explicit local implementation synthesized from evidence/physics.
- `OPEN` - consequential coordinate for which no defensible historical value is presently supported.

`OPEN` is valid. A related paper may close a `PT` or `SL` branch while historical RP-01 identity remains OPEN.

# Round-64 controlling findings

## 1. Same-UWA RIE physical state is substantially stronger

Smith 1999 supplies a Plasma Technology branch at 400 mTorr, 0.4 W/cm2, 30 sccm total, cathode 16 C and printed 180-V dc bias. This is `SL`, not the direct RP-01 100-mTorr/50-W/64-sccm/60-s state.

RP-01 reactor model, RF frequency, electrode areas/spacing, matching-network state, self-bias and actual sample temperature remain OPEN.

## 2. The approximately 8-um same-lineage conversion result now has a process state

Musca 1998 reports x=.31 Fermionics n-type material exposed at:

`H2 27 sccm / CH4 5 sccm / 430 mTorr / 0.4 W cm^-2 / cathode 18 C / ~200 V dc / 30 s`

with only ~0.075-um physical material removal but an LBIC/etchback electrical n+/n signature extending to about 8 um.

State: `SL-8UM-CONVERSION-BRANCH-CLOSED / RP01-CONVERSION-DEPTH-OPEN`.

Do not average this result with much shallower UWA conversion branches.

## 3. Photoresist profile is a first-class RIE coordinate

Musca 1998 demonstrates electrical conversion beneath nominally masked regions where the resist becomes thin/tapered near an edge. RIE travelers must therefore record measured resist thickness/profile, not only mask CAD dimensions.

## 4. RIE-converted material is electrically multilayered

Antoszewski 2000 and Nguyen 2002 resolve a thin lower-mobility surface-electron population and a deeper high-mobility converted region. One-carrier Hall values are effective scalars unless field dependence supports a single-carrier model. Use field-dependent Hall/QMSA or equivalent resolved analysis for physical conversion-depth/doping claims.

## 5. Plasma thermal and post-bake history matter

White 2001 distinguishes a cooled stage from actual sample temperature and supports multiple hydrogen-related populations. Post-RIE 80-100 C bake histories can redistribute mobile hydrogen. Record stage setpoint, actual/estimated sample temperature and every post-RIE thermal step.

## 6. Hg anneal recovery is an SL diagnostic branch

Smith 1998/1999 show a 200 C / 17 h sealed-Hg treatment restoring p-type electrical state after particular RIE conditions. Use as mechanistic/recovery evidence, not an RP-01 repair recipe.

## 7. Mesa RIE can severely degrade a photoconductor

Smith 2000 uses Fermionics x=.31 n-type PCs and shows long mesa plasma exposure can greatly reduce responsivity, effective lifetime and D* while increasing noise, even when cutoff and DC resistance remain similar.

Any expanded RIE area/dose requires a detector-level gate including responsivity, lifetime/dynamics, full noise spectrum and D*.

Important provenance point: the paper literally prints `H2/5CH4` for its 70-min branch. Preserve the literal notation; do not normalize it to match neighboring UWA papers.

## 8. LBIC absolute depth requires calibration/model support

Musca 1999 shows LBIC depth response depends on doping, wavelength, illumination direction, geometry and diffusion length. Bipolar LBIC proves an electrical boundary but does not uniquely determine absolute depth without calibration/model/destructive cross-check.

## 9. Passivation is a coupled electrical state

Pal 1999 demonstrates the competing effects of accumulation: lower surface recombination can increase effective lifetime while the accumulation layer creates surface shunting that can reduce responsivity.

Bhan 2004 shows surface-shunt resistance at anodic-oxide interfaces can contribute to photoconductor noise.

Schoolar 1982 on x=.30 material shows anodic-oxide/interface charge has visible-light, field and time memory; low-temperature recovery can be extremely slow. Record illumination/bias history and dark-rest time before interface or detector comparisons.

Passivation development therefore tracks, where measurable:

`{d_ox, Qss, Dit, Rsh_surface, tau_eff, Rv, noise}`.

## 10. Honeywell slider evidence remains PT but stronger

Schmit/Hager/Wood 1982 confirms the Honeywell atmospheric-pressure Te-rich horizontal slider, high-purity graphite, quartz tube, flowing H2, push-rod actuation, isothermal supercooling growth and 1-20-min typical growth-time region for <=~30-um layers.

Nemirovsky 1982 adds a separate semiclosed PT branch with explicit HgTe-reservoir depletion, solution reuse and substrate exposure during equilibration.

Neither paper closes the Fermionics/RP-01 machine drawing or exact x=.30 growth traveler.

## 11. Au/HgCdTe interface chemistry is not inert

Davis 1984 shows strong Te redistribution and band-bending changes during Au deposition on cleaved p-HgCdTe. This supports strict metallization-state recording but does not provide RP-01 Cr/Au-on-RIE-n+ setpoints.

# Major historical OPEN coordinates after Round 64

Still OPEN:

- exact RP-01/Fermionics LPE machine drawing and full numerical dimension stack;
- historical slider/epilayer clearance, well area/depth, melt depth and Hg-source vapor geometry;
- exact historical source-synthesis ampoule/free-volume/hot-pressure state;
- RP-01 RIE reactor model, RF frequency, electrode geometry, matching network, self-bias, actual sample temperature and chamber seasoning;
- exact RP-01 electrical conversion depth/lateral spread for the direct blocking-contact exposure;
- historical anodization electrode geometry/solution drop;
- historical Cr/Au evaporator/QCM/source geometry;
- original RP-01 cryostat/package/readout thermal state.

# Next work

Do not restart broad paper mining. Highest-value targets are archival/apparatus records:

1. exact UWA Plasma Technology run sheet/manual for the RP-01 exposure;
2. electrode dimensions/spacing, RF/matching-network state, measured self-bias and actual sample temperature;
3. Honeywell/Fermionics machine drawings and x=.30 source/growth travelers;
4. original anodization-cell drawings;
5. RP-01 Cr/Au evaporator/QCM geometry;
6. original cryostat/package/readout records.

Exact byte identities for the Round-64 paper set are in `research/2026-08-17_round64_source_sha256_manifest.md`.