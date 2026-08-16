# Source ledger addendum — source-recovery / qualification round 4

**Date:** 2026-08-15 America/New_York

This addendum records the literature and process conclusions used to build P14A, P09A, P03B and P04A after round 3.

## S-R4-01 — RP-01 full text re-audit for Mask-2 lift-off fingerprint

**Class:** Primary-A  
**Source:** E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Direct Mask-2 anchors:**

- photoresist `~4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene treatment `30 min`;
- then pattern/develop/water rinse;
- same resist retained through CH4/H2 RIE and metal lift-off;
- Cr `300 Å` / Au `2700 Å`.

**Negative result:** repeated UWA/process-lineage searches still do not identify the resist manufacturer/product, spin condition, UV dose, developer, development time, historical lift-off solvent/time, or metal deposition vacuum/rates.

## S-R4-02 — historical chlorobenzene single-layer lift-off mechanism

**Class:** Primary/Patent process lineage.

Historical single-layer optical lift-off literature and patents citing Hatzakis/IBM work establish:

- chlorobenzene treatment is a positive-resist profile-modification method;
- relevant resist class is diazo/diazide-sensitized novolak positive photoresist;
- chlorobenzene-modified near-surface resist dissolves more slowly during development, generating undercut/overhang suitable for lift-off;
- overhang/profile depend on soft-bake solvent content, soak duration/temperature, developer strength/temperature, chlorobenzene purity/water content, exposure sequence and resist formulation.

Representative historical products such as AZ1350J, AZ4000/AZ4110 and Shipley products appear in unrelated implementations.

**Use restriction:** no recovered source identifies one of those products as RP-01. Do not assign a commercial resist name historically.

**Procedure:** `procedures/P14A_CHLOROBENZENE_LIFTOFF_LINEAGE_ADDENDUM.md`.

## S-R4-03 — UWA RIE photovoltaic-device passivation branch

**Class:** Primary-A / Same-lab, different architecture.  
**Citation:** M. H. Rais et al., “HgCdTe photovoltaic detectors fabricated using a new junction formation technology,” *Microelectronics Journal* 31(7), 545–551 (2000), DOI `10.1016/S0026-2692(00)00028-8`.

**Relevant direct process principle:**

- LPE p-HgCdTe on CdZnTe;
- CH4/H2 RIE type conversion through windows in a ZnS layer;
- ZnS layer served as both RIE mask and permanent passivant;
- authors emphasize avoiding exposure of the converted junction to atmosphere;
- no high-temperature post-junction anneal.

**Use restriction:** this is a p-to-n photovoltaic branch, not RP-01 n-type photoconductor contact processing. Do not transplant ZnS mask/passivation or its device geometry into RP-01. Use only as same-lab evidence that post-RIE surface/passivation history is electrically important.

## S-R4-04 — Dell et al. 2001 passivant bake stability

**Class:** Primary-A / Same-lab, different architecture.  
**Citation:** J. M. Dell et al., “RIE induced n-on-p junction HgCdTe photodiodes: effects of passivant technology on bake stability,” *Proc. SPIE* 4454, 106–115 (2001), DOI `10.1117/12.448166`.

**Relevant direct conclusion:** x≈0.3 RIE-induced junction stability depends strongly on passivant technology during 80 °C bake; ZnS, CdTe and dual-layer approaches show different stability behavior.

**Use restriction:** reinforces passivation/thermal-history coupling but does not close RP-01 anodic-oxide recipe.

## S-R4-05 — modern UWA-compatible HgCdTe Cr/Au thermal evaporation

**Class:** Primary-A / same institution, modern different architecture.

Modern UWA-associated HgCdTe photoconductor work explicitly deposits Cr/Au by thermal evaporation.

**Role:** supports thermal evaporation as a locally compatible Cr/Au candidate technique.

**Restriction:** no historical 2001 UWA base pressure/rate/tool is recovered; modern numbers are not RP-01 setpoints.

**Procedure:** `procedures/P09A_CR_AU_DEPOSITION_TRANSFER_DOE.md`.

## S-R4-06 — Schmit–Hager–Wood / Wood–Hager Honeywell LPE lineage

**Class:** Primary-A.

Key sources:

- J. L. Schmit, R. J. Hager, R. A. Wood, “Liquid phase epitaxy of Hg1−xCdxTe,” *J. Crystal Growth* 56, 485–489 (1982), DOI `10.1016/0022-0248(82)90468-7`;
- R. A. Wood, R. J. Hager, “Horizontal slider LPE of (Hg,Cd)Te” (1983; complete DOI/full experimental thickness-time table still not recovered publicly).

**Direct/abstract-level high-value findings:**

- atmospheric-pressure horizontal-slider Te-rich LPE;
- controlled x=0.2, 0.3, 0.4 in Schmit–Hager–Wood;
- 2×3-cm substrate capability;
- Wood–Hager reports layer-to-layer composition reproducibility `σx≈0.002` and good across-layer uniformity.

**Negative result:** public indexing still does not provide a composition-matched 9.5-µm thickness versus time/supercooling table.

## S-R4-07 — Harman thickness / supercooling evidence

**Class:** Primary-A.

Same broad Te-rich horizontal-slider family demonstrates:

- thickness ranges from a few micrometers to tens of micrometers;
- thickness changes with both degree of supercooling and growth/contact time;
- process times vary substantially with apparatus/thermal trajectory.

**Implication:** literature time alone cannot close the RP-01 9.5-µm schedule.

**Procedure:** `procedures/P03B_X030_GROWTH_TIME_SUPERCOOLING_CALIBRATION.md`.

## S-R4-08 — Nagahama et al. x≤0.30 anneal branch

**Class:** Primary-A / abstract-level method.

**Citation lead:** K. Nagahama, R. Ohkata, K. Nishitani, T. Murotani, “LPE growth of Hg1−xCdxTe using conventional slider boat and effects of annealing on properties of the epilayers” (1984; full journal metadata/dwell details still need archival closure).

**Direct abstract-level anchors:**

- `x≈0.17–0.30`;
- CdTe `(111)A`;
- conventional slider/open-tube H2 growth;
- as-grown p-type;
- Hg-overpressure anneal `250–400 °C`;
- `250–300 °C` yields well-behaved n-type material without apparent composition change;
- `400 °C` produces interface-region composition change.

**Negative result:** public source does not expose exact dwell, Hg-source condition or cooldown.

## S-R4-09 — Harman / Chandra anneal controls

**Class:** Primary-B + Primary-A.

- Harman process source gives broad ~200–300 °C, Hg partial pressure ~0.1–250 Torr, and a ~250 °C / 1 h screening example but generally higher final carrier density than RP-01.
- Chandra/Schaake/Kinch show low-temperature anneal kinetics depend strongly on x, vacancy concentration and T; kinetics slow with increasing x; x≳0.26 complicates vacancy inference from 77-K Hall alone.

**Implication:** P04 must be released by final Hall + optical state rather than a transplanted time/temperature pair.

**Procedure:** `procedures/P04A_X030_HG_ANNEAL_STATE_MAPPING_DOE.md`.

## Round-4 source conclusion

Four areas have reached a practical archival source ceiling:

1. exact RP-01 positive-resist product/developer;
2. historical Cr/Au vacuum/rates/RIE-to-metal delay;
3. composition-matched 9.5-µm LPE time/supercooling relation;
4. exact x≈0.30 Hg-overpressure anneal dwell/source/cooldown.

The correct next step for these fields is controlled local qualification, not insertion of generic semiconductor-fab numbers.
