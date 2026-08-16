# P08C — UWA LBIC conversion-method lineage and pressure provenance

**Status:** CONTROLLED SOURCE/INTERPRETATION ADDENDUM. Supplements `P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`, `P08A_RIE_GAS_RATIO_PROVENANCE_ADDENDUM.md`, and `P08B_RIE_HALL_DEPTH_COUPLING_ADDENDUM.md`.

## 1. Purpose

Separate the distinct University of Western Australia RIE/LBIC experiments that are often conflated when discussing HgCdTe plasma-induced type conversion, and lock the strongest currently available primary-source pressure values to the correct sample/process branches.

The central rule is:

> A conversion depth, carrier-density result, or pressure from one p-type RIE junction experiment may not be transferred to the RP-01 n-type blocking-contact experiment unless the material state and plasma condition are demonstrably matched.

## 2. Primary UWA p-type LBIC branch — 1997

J. F. Siliquini, J. M. Dell, C. A. Musca, L. Faraone, “Scanning Laser Microscopy of Reactive Ion Etching Induced n-Type Conversion in Vacancy-Doped p-Type HgCdTe,” *Applied Physics Letters* 70, 3443–3445 (1997), DOI `10.1063/1.119159`.

The UWA repository directly states:

- material: vacancy-doped p-type Hg0.69Cd0.31Te;
- RIE pressure: `410 mTorr`;
- gas chemistry: CH4/H2;
- RF power density: `0.4 W/cm²`;
- physical HgCdTe etch depth: approximately `0.2 µm`;
- electrically converted n-type depth: approximately `1.5 µm`.

This is a direct primary demonstration that electrical conversion depth greatly exceeds physical etch depth.

It is **not** the RP-01 n-type blocking-contact depth condition.

## 3. Primary UWA arsenic-doped p-type LBIC branch — 1998

J. F. Siliquini, J. M. Dell, C. A. Musca, E. P. G. Smith, L. Faraone, J. Piotrowski, “Estimation of doping density in HgCdTe p-n junctions using scanning laser microscopy,” *Applied Physics Letters* 72 (1998), DOI `10.1063/1.120642`.

The UWA institutional repository directly states:

- material: extrinsic arsenic-doped p-type Hg0.71Cd0.29Te;
- prior Hg anneal used to eliminate Hg vacancies;
- RIE pressure: `340 mTorr`;
- gas chemistry: CH4/H2;
- RF power density: `0.4 W/cm²`;
- LBIC measured over `80–300 K`;
- effective n-type donor density extracted using SEMICAD DEVICE simulation.

### Pressure-provenance warning

Several secondary/reposted records reproduce the same paper with `390 mTorr` rather than `340 mTorr`.

For controlled project use:

- `340 mTorr` = preferred value because it is given by the UWA institutional primary-paper record;
- `390 mTorr` = secondary transcription/reposting discrepancy;
- do not average the two values or silently substitute 390 mTorr.

If the publisher full text is later acquired, re-audit the experimental section and resolve this discrepancy definitively.

## 4. 1998 JCG characterization branch

J. F. Siliquini, J. M. Dell, C. A. Musca, L. Faraone, J. Piotrowski, “Characterisation of reactive-ion-etching-induced type-conversion in p-type HgCdTe using scanning laser microscopy,” *Journal of Crystal Growth* 184–185, 1219–1222 (1998), DOI `10.1016/S0022-0248(98)80255-8`.

This primary paper explicitly characterizes both lateral and vertical conversion in vacancy- and extrinsically doped p-type HgCdTe around `x≈0.3` using LBIC and modeling over 80–300 K.

Use this paper as a method-lineage anchor for:

- vertical conversion-depth extraction;
- lateral conversion mapping;
- temperature-dependent LBIC interpretation;
- donor-density fitting.

Do not transfer a depth from this p-type branch to RP-01 without matching process/material conditions.

## 5. RP-01 n-type branch remains distinct

RP-01 uses starting **n-type** `x≈0.30` HgCdTe and states:

- Plasma Technology parallel-plate RIE;
- printed chemistry `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- RF power `50 W`;
- process time `60 s`.

RP-01 cites Musca et al. 1998, *Journal of Electronic Materials* 27, 661–667, DOI `10.1007/s11664-998-0032-4`, as prior work indicating an n+ region extending approximately `8 µm` under similar conditions.

The publicly accessible institutional record for that paper confirms:

- mid-wave n-type HgCdTe;
- LBIC maps under multiple wafer-processing conditions;
- simulation of junction depth, temperature and grading effects;
- extraction of n+ depth and lateral extent.

However, the accessible record still does **not** expose the exact pressure/power/time/gas condition tied specifically to the ~8-µm result.

Therefore:

`d_conv ≈ 8 µm` remains `P-OTHER-SOURCE / SIMILAR-CONDITIONS`, not a directly closed RP-01 process-output value.

## 6. Metrology consequence

P08 qualification shall treat these as separate measured outputs:

- physical recession `d_etch`;
- vertical electrical conversion depth `d_conv`;
- lateral conversion distance `L_conv`;
- sheet transport state;
- volumetric density only after an independently justified depth model;
- final TLM contact performance.

The 1997 direct result (`0.2 µm` physical etch vs `~1.5 µm` electrical conversion) is the clearest empirical reason not to infer `d_conv` from surface recession.

## 7. Source hierarchy for disputed values

When numerical values conflict:

1. directly inspected publisher full text;
2. institutional repository record reproducing the paper abstract/metadata;
3. author manuscript/proceedings copy;
4. peer-reviewed review table;
5. secondary indexing/reposting platforms.

Use the highest available level and record discrepancies instead of combining them.

## 8. Remaining RIE archival priorities

1. acquire the complete Musca et al. 1998 JEM paper and recover the exact condition tied to the ~8-µm n-type result;
2. confirm primary individual CH4/H2 MFC values behind RP-01 `CH4/5H2`;
3. recover Plasma Technology reactor electrode area, spacing, RF frequency, self-bias and sample-temperature behavior;
4. determine whether the 50-W RP-01 setting can be converted to a historical power density using the actual powered-electrode area;
5. reconcile the RIE depth model with P08B sheet-density/volume-density coupling.
