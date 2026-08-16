# Source ledger addendum — Round 32: FTIR composition / thickness / cutoff closure

**Date:** 2026-08-16 America/New_York

## Scope

Empirical audit of P06 and recovery of practical HgCdTe infrared-transmission apparatus, composition/thickness extraction methods, optical-edge definitions, model provenance, and the relationship to the RP-01 detector cutoff.

---

## S32-01 — Smith et al. 2001 — canonical RP-01

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

Recovered/reconfirmed:

- material described as LPE n-HgCdTe, approximately `x≈0.30`;
- active thickness `9.5 µm`;
- detector spectral response at `80 K`, `10 V/cm`, stated `60° FOV`, `1 kHz`;
- detector cutoff stated as `4.4 µm`;
- same detector used for field response/noise/spectral response/D* performance figures.

Not disclosed:

- FTIR material metrology;
- how `x≈0.30` was measured;
- how `9.5 µm` was measured;
- the formal spectral-response cutoff convention used for `4.4 µm`.

**Use:** historical performance/material anchor only. Do not invent an FTIR traveler from it.

---

## S32-02 — Hansen, Schmit, Casselman 1982

G. L. Hansen, J. L. Schmit, T. N. Casselman, “Energy gap versus alloy composition and temperature in Hg1−xCdxTe,” *Journal of Applied Physics* 53, 7099–7101 (1982), DOI `10.1063/1.330018`.

**Class:** `PRIMARY-HGCDTE-BANDGAP`.

Direct:

`Eg = -0.302 + 1.93x - 0.810x^2 + 0.832x^3 + 5.35e-4 T(1-2x)` eV.

- based on data from 22 studies;
- stated valid over full composition range and approximately 4.2–300 K;
- standard error of estimate ~0.013 eV.

**Permanent interpretation:** 0.013 eV is the empirical fit standard error, not local FTIR repeatability or a detector-cutoff uncertainty.

Derived RP-01 consistency:

- x=.300, 80 K -> Eg=.243684 eV -> bandgap-equivalent 5.0879 µm;
- 4.4 µm -> hc/lambda=.281782 eV -> Hansen-equivalent x≈.3241 at 80 K.

**Use:** consistency/model mapping only; never equate undefined detector cutoff with exact x.

---

## S32-03 — Hougen 1989

C. A. Hougen, “Model for infrared absorption and transmission of liquid-phase epitaxy HgCdTe,” *Journal of Applied Physics* 66, 3763–3766 (1989), DOI `10.1063/1.344038`.

**Class:** `PRIMARY-HGCDTE-LPE-OPTICAL`.

**Use:** primary full-transmission-model lineage for LPE HgCdTe. Supports P06 preference for full-spectrum optical modeling instead of one-point cutoff-to-x conversion.

Historical RP-01 apparatus identity: not established.

---

## S32-04 — Gopal, Ashokan, Dhar 1992

V. Gopal, R. Ashokan, V. Dhar, “Compositional characterization of HgCdTe epilayers by infrared transmission,” *Infrared Physics* 33, 39–45 (1992), DOI `10.1016/0020-0891(92)90053-V`.

**Class:** `PRIMARY-HGCDTE-LPE-OPTICAL / METHOD`.

Direct/indexed conclusions:

- room-temperature transmission;
- HgCdTe in approximately 0.2<x<0.3;
- 50%-transmission frequency and zero-intercept/cut-on metric correlated to x;
- disagreement between the two x estimates used as a qualitative indicator of compositional nonuniformity.

### Source conflict

Current ScienceDirect index text renders the thickness interval as `10–30 mm`, inconsistent with the epilayer context. An author/profile summary describes micrometre-scale material and approximately `20–30 µm`.

Status: `SOURCE-UNIT-CONFLICT / PRIMARY-PDF-LINE-NOT-YET-CHECKED`.

Do not freeze the exact validity interval until the primary paper line is inspected.

---

## S32-05 — Chu et al. 1994

J. H. Chu, B. Li, K. Liu, D. Tang, “Empirical rule of intrinsic absorption spectroscopy in Hg1−xCdxTe,” *Journal of Applied Physics* 75, 1234–1235 (1994), DOI `10.1063/1.356464`.

**Class:** `PRIMARY-HGCDTE-ABSORPTION-MODEL`.

Direct:

- measured intrinsic absorption spectra over x approximately 0.170–0.443;
- empirical Kane-region absorption relation;
- beta composition/temperature dependence given for 300 K and 77 K;
- empirical result compared with Kane-model calculations.

**Use:** candidate absorption-model lineage; model/version must be frozen and validated locally.

---

## S32-06 — Chang et al. 2005 — automated IR microscope mapping

Y. Chang, G. Badano, E. Jiang, J. W. Garland, J. Zhao, C. H. Grein, S. Sivananthan, “Composition and thickness distribution of HgCdTe molecular beam epitaxy wafers by infrared microscope mapping,” *Journal of Crystal Growth* 277, 78–84 (2005), DOI `10.1016/j.jcrysgro.2005.01.051`.

**Class:** `PRIMARY-HGCDTE-MAPPING-TRANSFER`.

Author-uploaded primary text recovers:

- Thermo Nicolet Centaur µs IR microscope;
- Thermo Nicolet 870 FTIR;
- computerized x-y translation stage;
- stated position precision ~1 µm;
- adjustable aperture down to ~25 µm at 10-µm wavelength;
- 100-µm aperture selected for mapping throughput/SNR;
- automatic transmissivity-curve fitting;
- composition from intrinsic absorption edge;
- thickness from interference-pattern fitting below intrinsic absorption region.

Example CdZnTe-substrate map:

- x mean ~0.2182;
- σx ~0.0006;
- thickness mean ~7.84 µm;
- σd ~0.03 µm.

**Use:** quantitative apparatus/mapping template only. Numerical uniformities are not RP-01 process specifications.

---

## S32-07 — Murthy et al. 2009 — LPE/CdZnTe/FTIR transfer branch

O. V. S. N. Murthy, V. Venkataraman, R. K. Sharma, I. Vurgaftman, J. R. Meyer, “Multicarrier conduction and Boltzmann transport analysis of heavy hole mobility in HgCdTe near room temperature,” *Journal of Applied Physics* 106, 113708 (2009), DOI `10.1063/1.3266015`.

**Class:** `PRIMARY-HGCDTE-LPE-OPTICAL / APPARATUS-TRANSFER`.

Direct relevant branch:

- LPE HgCdTe sample on Cd0.96Zn0.04Te;
- Te-rich horizontal-slider growth;
- in-situ Te-saturation anneal ~230 °C;
- composition from IR absorption at 300 K;
- Bruker IFS 66v/S FTIR;
- LPE sample x=0.200;
- 34-µm layer thickness estimated from FTIR interference fringes.

**Use:** strong proof of practical room-temperature FTIR composition + fringe-thickness workflow on a Te-rich horizontal-slider LPE/CdZnTe branch.

Not RP-01 apparatus identity.

---

## S32-08 — Yue et al. 2019 — evacuated FTIR optical branch

F.-Y. Yue et al., “Optical characterization of defects in narrow-gap HgCdTe for infrared detector applications,” *Chinese Physics B* 28, 017104 (2019), DOI `10.1088/1674-1056/28/1/017104`.

**Class:** `PRIMARY-HGCDTE-OPTICAL-TRANSFER`.

Direct apparatus details:

- Bruker IFS 66v/S;
- KBr beamsplitter;
- LN2-cooled HgCdTe detector;
- spectrometer evacuated to suppress atmospheric absorption.

The source also used quick `1% Br2/methanol` treatment before its optical experiment.

**Rule:** do not import that surface treatment into RP-01 P06 automatically; it is experiment-specific surface-state preparation.

The paper emphasizes that defects/doping/Fermi-level state can influence the optical band-edge interpretation.

---

## S32-09 — interface/fringe degradation evidence

Primary Journal of Crystal Growth work on HgCdTe/CdZnTe reports that high substrate dislocation density/Hg in-diffusion correlates with low below-gap FTIR transmission and loss of interference fringes.

DOI `10.1016/j.jcrysgro.2006.09.056`.

**Class:** `PRIMARY-HGCDTE-INTERFACE-OPTICAL-TRANSFER`.

**Use:** absence of fringes is not automatically an instrument problem; it can be a material/interface diagnostic.

---

# Negative / unresolved searches

Not recovered this round:

- a direct RP-01/UWA statement that the supplier x≈0.30 was obtained by FTIR;
- a direct RP-01/UWA measurement method for 9.5-µm thickness;
- exact RP-01 material spectrometer/model;
- exact RP-01 material map/grid;
- exact 4.4-µm detector cutoff convention;
- primary PDF line resolving the Gopal 1992 thickness-range unit conflict.

“Not recovered” does not mean nonexistent.

---

# Round-32 scientific conclusions

1. P06 is already operator-capable; no duplicate top-level module is warranted.
2. P06A supplies empirical apparatus/model lineage and a controlled transfer register.
3. `d_physical`, `d_FTIR`, `Eg/x_opt`, optical-edge metrics and detector cutoff are permanently separate quantities.
4. `x=.30 -> 5.09 µm bandgap-equivalent at 80 K` and `4.4 µm -> x≈.3241 Hansen-equivalent` is a consistency comparison only.
5. A 100-µm microscope aperture is not automatically 100-µm spatial resolution.
6. Hansen's 0.013-eV global fit error is not local FTIR uncertainty.
7. Defect/doping/interface state can shift/deform optical spectra without a true alloy-composition change.
8. Loss of interference fringes can be a material/interface signature, not merely poor instrument SNR.
