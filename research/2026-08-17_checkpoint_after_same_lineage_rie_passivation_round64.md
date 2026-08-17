# Research checkpoint - Round 64 same-lineage RIE/passivation closure

**Date:** 2026-08-17 America/New_York  
**State:** documentary evidence strengthened; no new physical HgCdTe fabrication run.

## Completed

Fifteen supplied full papers were audited against Round 63. Controlling records:

1. `docs/RP01_SAME_LINEAGE_RIE_PASSIVATION_CLOSURE_ROUND64.md`
2. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND64.md`
3. `docs/SOURCE_LEDGER_ADDENDUM_ROUND64.md`
4. `procedures/P03G_HONEYWELL_TECHNION_SLIDER_LPE_FULLTEXT_ADDENDUM.md`
5. `procedures/P08H_UWA_RIE_LBIC_FULLTEXT_CLOSURE_ADDENDUM.md`
6. `procedures/P25B_PHOTOCONDUCTOR_PASSIVATION_SHUNT_NOISE_ADDENDUM.md`
7. `procedures/P26B_AU_HGCDTE_INTERFACE_CHEMISTRY_ADDENDUM.md`
8. `research/2026-08-17_round64_source_sha256_manifest.md`

## Highest-value recoveries

### UWA RIE/LBIC

- Smith 1999 supplies a Plasma Technology physical-state branch: 400 mTorr, 0.4 W/cm2, 30 sccm total, 16 C cathode and printed 180-V dc bias.
- Musca 1998 closes the process state associated with a very deep same-lineage electrical-conversion observation: H2 27 / CH4 5 sccm, 430 mTorr, 0.4 W/cm2, 18 C cathode, ~200-V dc bias, 30 s, ~0.075-um physical recession, with LBIC/etchback junction signature to about 8 um.
- Musca 1998 also shows tapered/thin resist can permit plasma-induced electrical conversion beneath nominally masked material. Resist thickness/profile is now a first-class RIE coordinate.
- Antoszewski 2000 and Nguyen 2002 resolve a low-mobility surface-electron layer and a deeper high-mobility converted region. One-carrier Hall values are insufficient for rigorous RIE-depth claims.
- White 2001 supports multiple hydrogen-related conversion mechanisms and makes post-RIE bake history consequential.
- Smith 1998 demonstrates a 200 C / 17 h sealed-Hg recovery branch after particular RIE conditions.
- Smith 2000 directly demonstrates that long mesa RIE can severely reduce PC responsivity, lifetime, noise and D* while cutoff and DC resistance remain similar.
- Musca 1999 shows LBIC absolute depth requires calibration/modeling because the signal depends on junction doping, wavelength, geometry and diffusion length.

### LPE

- Schmit/Hager/Wood 1982 strongly confirms the Honeywell Te-rich atmospheric-pressure horizontal-slider process family and its isothermal supercooling/time control.
- Nemirovsky 1982 adds a quantified semiclosed HgTe-reservoir/source-reuse branch and shows substrate state can change during equilibration before melt contact.

### Passivation/noise

- Pal 1999 demonstrates the tradeoff between reduced surface recombination and increased surface shunting in a gated HgCdTe photoconductor.
- Schoolar 1982 on x=.30 material shows anodic-oxide charge has light/bias/time history, including very long low-temperature recovery.
- Bhan 2004 requires a surface-shunt/noise contribution to fit HgCdTe-PC measurements; surface shunts are therefore a candidate detector-noise pathway, not merely a DC-resistance issue.

### Metallization

- Davis 1984 shows Au deposition can drive Te redistribution and band-bending changes at HgCdTe surfaces. P26 interface-state/vacuum/thermal/QCM controls remain justified even though the paper is not the RP-01 Cr/Au interface.

## Critical non-promotions

- RP-01 RIE self-bias, electrode geometry, RF frequency and actual sample temperature remain OPEN.
- The ~8-um Musca-1998 conversion depth is an SL branch, not the RP-01 conversion depth.
- Do not average the wide range of UWA conversion depths into a synthetic universal value.
- Smith-2000 literally prints `H2/5CH4`; preserve that notation rather than editorially changing it to match neighboring papers.
- White-2001's 15 C stage is not a measured wafer temperature.
- 200 C / 17 h sealed-Hg recovery is not a universal repair recipe.
- Pal/Bhan/Schoolar numerical interface values are PT, not RP-01 acceptance limits.
- Davis Au-on-cleaved-p-HgCdTe does not define Cr/Au deposition setpoints for the RIE-converted n+ contact region.

## Current maturity

- `ROUND64-SAME-LINEAGE-RIE-PASSIVATION-CLOSURE = COMPLETE`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `END-TO-END-EMPIRICALLY-VALIDATED = NO`.

## Next documentary targets

Do not restart broad literature mining. Highest-value targets are now archival/apparatus-specific:

1. exact UWA Plasma Technology run sheet/manual for the RP-01 exposure;
2. electrode areas/spacing, RF frequency, matching network, self-bias and actual sample-temperature state;
3. Honeywell/Fermionics machine drawings and source/growth travelers;
4. original anodization-cell geometry;
5. RP-01 Cr/Au evaporator/QCM geometry;
6. original cryostat/package/readout records.