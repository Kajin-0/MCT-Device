# Source ledger addendum — Round 20 empirical Mask-2 lithography / lift-off recovery

**Date:** 2026-08-16 America/New_York  
**Scope:** P14/P14A/P27 resist-family identification, chlorobenzene process control, exposure/development, lift-off.

This addendum records what is recovered and what is still unresolved. It does not identify the RP-01 resist by analogy.

---

## R20-S1 — canonical RP-01 detector paper

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16 (2001) 455–462. DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

Direct Mask-2 facts:

- resist approximately `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene soak `30 min`;
- then patterned, developed and rinsed in water;
- resist is suitable as P08 RIE mask;
- same resist process enables lift-off of Cr `300 Å` / Au `2700 Å`.

Still absent:

- product/manufacturer;
- spin program;
- exposure tool/dose;
- chlorobenzene temperature/purity/agitation/order relative to exposure;
- developer identity/concentration/time;
- post-develop dry;
- lift-off solvent/time/agitation.

---

## R20-S2 — Hatzakis/Canavello/Shaw 1980 single-step optical lift-off

M. Hatzakis, B. J. Canavello, J. M. Shaw, “Single-Step Optical Lift-Off Process,” *IBM Journal of Research and Development* 24 (1980) 452–460. DOI `10.1147/rd.244.0452`.

**Class:** `PRIMARY-CHLOROBENZENE-LIFTOFF`.

Direct/general process result:

- UV exposure with a single layer of positive AZ-type resist;
- chlorobenzene/toluene/benzene soak can be applied before or after exposure;
- resulting differential development produces lift-off overhang;
- soak time/temperature behave consistently with a diffusion-controlled profile modification.

Use: establishes process mechanism and permits both soak-order branches.

Restriction: no RP-01 product identification.

---

## R20-S3 — Halverson/MacIntyre/Motsiff 1982 mechanism paper

R. M. Halverson, M. W. MacIntyre, W. T. Motsiff, “The Mechanism of Single-Step Liftoff with Chlorobenzene in a Diazo-Type Resist,” *IBM Journal of Research and Development* 26 (1982) 590–595.

**Class:** `PRIMARY-CHLOROBENZENE-MECHANISM`.

Direct process-family conclusion:

- chlorobenzene-penetrated near-surface resist develops more slowly than underlying bulk resist;
- diazo/novolak-type positive resist architecture supports re-entrant lift-off profile formation.

Use: mechanism only.

---

## R20-S4 — Collins/Halsted 1982 process-control paper

G. G. Collins, C. W. Halsted, “Process Control of the Chlorobenzene Single-Step Liftoff Process with a Diazo-Type Resist,” *IBM Journal of Research and Development* 26 (1982) 596–604.

**Class:** `PRIMARY-CHLOROBENZENE-PROCESS-CONTROL`.

Recovered process-control conclusions through publisher/bibliographic record and primary patent citations:

- exposure, chlorobenzene soak, development and post-application bake interact;
- linewidth, overhang and resist height are useful process-state observables;
- film-thickness loss during chlorobenzene treatment can be used as a soak-control observable;
- manufacturing reproducibility depends on controlling bake/soak/exposure/development rather than treating them independently.

Use: direct justification for P27 full profile metrology.

---

## R20-S5 — Fathimulla 1985 AZ4000 chlorobenzene lift-off

A. Fathimulla, “Single-step lift-off process using chlorobenzene soak on AZ4000 resists,” *Journal of Vacuum Science & Technology B* 3(1) (1985) 25–27.

**Class:** `PRIMARY-AZ4000-CHLOROBENZENE`.

Recovered through publisher-indexed bibliographic record and contemporaneous primary patent description:

- chlorobenzene single-layer lift-off specifically demonstrated on AZ4000 resists;
- AZ4110 is explicitly named in the associated historical description;
- thick overhang / vertical-wall structure was demonstrated;
- UV hardening was used in the AZ4110 lineage to improve thermal stability under hot metal deposition.

Restriction: full experimental parameter table was not recovered in the current public route; do not invent exact spin/developer values from this paper.

---

## R20-S6 — U.S. Patent 5,654,128 quantified AZ1350J control process

**Class:** `PRIMARY-CHLOROBENZENE-LIFTOFF / QUANTITATIVE`.

Direct example:

- AZ1350J;
- spin `3000 rpm`;
- soft bake `90 °C / 20 min`;
- chlorobenzene `15 min`;
- post-soak bake `90 °C / 10 min`;
- overhang about `0.4 µm` in reported example;
- Cr `200 Å` + Al `9900 Å`;
- acetone `10 min` + ultrasonic agitation, then fresh acetone additional `5 min` for complete lift-off.

Comparative prior-art branch:

- AZ1350J `4000 rpm`;
- `90 °C / 10 min` soft bake;
- exposure `5.8 s` at `13.6 mW/cm²` = derived `78.9 mJ/cm²`;
- chlorobenzene `10 min`;
- Shipley Microposit 303A `10 s`;
- same ~1-µm metal stack;
- acetone/ultrasonic lift-off required approximately `8 h`.

Use: strong process-control example showing impact of profile conditioning on lift-off.

Restriction: different substrate/resist/metal; not RP-01 recipe.

---

## R20-S7 — GB 2,229,005A quantified AZ4110 chlorobenzene process

**Class:** `PRIMARY-AZ4110-CHLOROBENZENE`.

Direct process:

- positive AZ4110;
- `4000 rpm / 30 s`;
- `90 °C / 2 min` hotplate bake;
- UV dose `900 J/m² = 90 mJ/cm²`;
- exposure of order `10 s`;
- chlorobenzene `28–30 °C / 2 min`;
- aqueous developer at `1:1` dilution;
- `60 s` development;
- water rinse/blow dry;
- resulting film approximately `1.1 µm`.

Use: direct chlorobenzene/developer/exposure example for AZ4110.

Restriction: thickness far below RP-01 4–5 µm under this coating condition.

---

## R20-S8 — EP 0,410,268B1 quantified AZ4330 thickness/exposure

**Class:** `PRIMARY-AZ4000-THICKNESS`.

Direct process example:

- m-cresol-novolak AZ4330;
- film approximately `4.3 µm`;
- spin `3500 rpm / 30 s`;
- bake `85 °C / 10 min`;
- exposure `150 mJ/cm²` at `365 nm` with GCA step-and-repeat tool.

The example subsequently uses a silylation process and is not a chlorobenzene lift-off recipe.

Use: strong geometric/thickness match only.

---

## R20-S9 — AZ4400 4–5-µm primary patent examples

U.S. Patent `6,470,904B1` and related microvalve patent lineage.

**Class:** `PRIMARY-AZ4000-THICKNESS`.

Directly describes AZ4400-type resist layers at approximately `4 µm` and `5 µm` in patterned microfabrication.

Use: confirms AZ4400 resides in RP-01 thickness class.

Restriction: no recovered product-specific chlorobenzene sequence or RP-01 identification.

---

## R20-S10 — AZ4620 5-µm primary example

CN Patent `101138663A`.

**Class:** `PRIMARY-AZ4000-THICKNESS / LATE`.

Direct example:

- AZ4620 positive photoresist;
- approximately `5 µm` film;
- `4000 rpm` spin condition;
- exposure/development in a separate microfabrication architecture.

Use: thick-resist screening candidate.

Restriction: much later process and not direct chlorobenzene single-layer evidence.

---

## R20-S11 — U.S. Patent 4,769,343 historical AZ single-step lift-off summary

**Class:** `PRIMARY-HISTORICAL-LIFTOFF`.

Directly summarizes:

- Hatzakis single-layer chlorobenzene method;
- Fathimulla AZ4000/AZ4110 branch;
- diazo-oxide / phenolic-resin positive-resist chemistry;
- bake/exposure/chlorobenzene/development sequence dependence.

Its own preferred device process uses additional deep-UV/thermal-flow steps and is not RP-01.

Use: historical family linkage only.

---

# Negative search / unresolved identification

Round 20 did **not** recover a UWA/RP-01 source naming:

1. resist manufacturer/product;
2. spin speed/time;
3. exposure wavelength/dose/tool;
4. developer product/concentration/time;
5. chlorobenzene temperature/purity/agitation;
6. post-soak bake/dry;
7. lift-off solvent/time/agitation.

Targeted UWA searches for `AZ4110`, `AZ4000`, `chlorobenzene`, `photoresist`, and the RP-01 author names did not expose an indexed UWA record containing those missing process details.

This is negative search evidence only.

---

# Round-20 source consequence

The process family can be narrowed substantially without pretending identity:

- historical chlorobenzene lift-off = positive diazo/novolak AZ-type family;
- AZ4110 = strong direct chlorobenzene reference but weak single-coat thickness match under one quantified condition;
- AZ4330/AZ4400/AZ4620-class products = much stronger direct 4–5-µm thickness matches;
- exact RP-01 product remains open;
- direct RP-01 bake/chlorobenzene duration are stronger anchors than any transfer spin/dose/developer number;
- exposure/developer must be qualified jointly with chlorobenzene order/profile and RIE survival;
- acetone is a documented historical chlorobenzene-lift-off solvent candidate but is not proven as the RP-01 lift-off solvent.

P27 therefore gives an executable empirical screening route without upgrading candidate products to historical facts.
