# Checkpoint — after RIE gas re-audit / anodic-oxide instantiation Round 37

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round 37 objective

Round 37 began with P16A R17:

- determine whether RP-01 `CH4/5H2` could be resolved into direct historical individual MFC values;
- avoid duplicating P08A if the source trail was already exhausted.

After the audit established no primary source upgrade, the round pivoted to P16A R15:

- make the anodic-oxide cell/electrolyte branch materially closer to operator execution;
- recover primary cell/electrolyte details rather than merely repeat the ~80-nm target.

---

## 2. RIE gas conclusion

P08A was already the correct controlled location.

Direct RP-01 remains:

- Plasma Technology parallel-plate;
- `CH4/5H2`;
- total `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`.

The 1999 same-UWA primary branch also continues to print `CH4/5H2` rather than separate MFCs.

The strongest explicit decoding remains the same-lineage 2005 review:

`CH4:H2 = 1:5`.

Derived candidate split from direct 64-sccm total:

- CH4 `10.6667 sccm`;
- H2 `53.3333 sccm`.

Evidence remains:

`DIRECT total + SAME-LINEAGE SECONDARY ratio -> DERIVED candidate individual flows`.

Do not call the individual values direct Smith et al. data.

### Search decision

No new RIE gas module was created. Future agents should not repeat generic `CH4/5H2` searches without a genuinely new source family such as UWA reactor travelers/notebooks/thesis appendices.

---

## 3. Anodic-oxide source advance

The strongest useful new detail came from TI US3977018.

### Direct TI photoconductor branch

Recovered:

- HgCdTe anode;
- carbon-rod cathode;
- plastic-lined stainless tank is permitted;
- constant-current process;
- preferred electrolyte `0.1 M KOH / 90% EG / 10% DI water`;
- patent explicitly states `0.1 mole KOH dissolved in 1 liter` of the 90/10 mixed solvent;
- preferred `J≈0.3 mA/cm²`;
- preferred formation voltage ~`15 V`;
- ~`2 min`;
- ~`800 Å` oxide;
- uniform deep-blue film;
- reproducible formation-voltage/thickness relation reported for the branch.

Still open:

- whether the 90%/10% solvent split means v/v, w/w or another basis.

Therefore do not convert the source statement into `900 mL EG + 100 mL water` and label that historical fact.

### Derived KOH inventory

For a source-defined 0.1000 mol KOH per liter:

`m_KOH,pure = 0.1000 mol × 56.1056 g/mol = 5.61056 g`.

Correct for actual reagent assay in a local recipe.

This calculation does not identify the 90:10 basis.

---

## 4. Separate later cell lineage

US5036376A supplies a concrete later HgCdTe anodization apparatus:

- two-electrode Teflon cell;
- horizontal HgCdTe slice;
- etched tungsten/titanium anode-contact probe;
- circular Pt cathode;
- Teflon/polypropylene tank;
- 0.1 M KOH in 10% water / 90% EG;
- unstirred;
- about room temperature;
- voltage/time recording;
- example 350 µA/cm² on 20×5-mm x≈.20 HgCdTe;
- 15 min -> ~600 Å oxide in that branch.

This is apparatus-transfer evidence, not the same branch as TI's earlier carbon-rod photoconductor process.

Permanent rule:

`TI-CARBON-ROD-PC != TI-LATER-PT-HORIZONTAL-CELL`.

Do not splice their hardware and timing into a fictitious published recipe.

---

## 5. New controlled files

Created:

- `procedures/P25A_ANODIC_OXIDE_CELL_ELECTROLYTE_INSTANTIATION_ADDENDUM.md`
- `travelers/P25A_ANODIC_OXIDE_CELL_ELECTROLYTE_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND37.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND37.md`
- this checkpoint

Updated:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`

AGENTS refresh follows this checkpoint.

---

## 6. P25A control logic

P25A owns:

- explicit local EG:H2O mathematical definition;
- KOH assay/inventory calculation;
- reagent genealogy;
- cell vessel/dimensions;
- anode contact;
- cathode material/geometry;
- actual electrochemically exposed area `A_exposed`;
- `I = J A_exposed` realization;
- bath temperature/agitation;
- raw V(t), induction, charge/area;
- rinse/dry;
- P28->P25 and P25->Mask2/P08 clocks.

P25 remains the broader physical/interface/device qualification method.

### Qualification progression

`LITERATURE-TRANSFER-ONLY`
-> `ELECTROLYTE-MATHEMATICALLY-DEFINED`
-> `CELL-GEOMETRY-DEFINED`
-> `CURRENT-DENSITY-TRACEABLE`
-> `V(T)-FINGERPRINT-REPEATABLE`
-> `OXIDE-THICKNESS-QUALIFIED`
-> `INTERFACE-FUNCTION-QUALIFIED`
-> `P08-COMPATIBLE`
-> `CONTACT/DETECTOR-CORRELATED`
-> `P25-LOCAL-QUALIFIED`.

---

## 7. Readiness state after Round 37

Still:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`

Important rows:

- R15 remains `OPEN-CHOICE`; P25A is a closure method, not a physically selected cell.
- R17 remains blocking; the 1:5 split is a candidate, not direct historical identity or an instantiated gas manifold.
- R18 remains `APPARATUS-NOT-SELECTED`.
- R20 Cr/Au deposition remains `APPARATUS-NOT-SELECTED`.

---

## 8. Same-UWA passivation recovery state

Still identified:

- Musca/Smith/Dell/Faraone 1999 contact/passivation conference paper;
- Musca/Siliquini/Nener/Faraone 1995 LWIR photoconductor passivation paper.

Institutional metadata verifies both records, but the accessible records do not expose the native-anodization traveler.

Record as `NOT-RECOVERED`, not absent.

---

# 9. Strongest next action — Round 38

Proceed with **R20 Cr/Au deposition apparatus / rate / vacuum provenance audit and local instantiation closure**.

Reason:

- direct RP-01 already fixes Cr `30 nm`, Au `270 nm`, Mask-2 context, contact geometry and 80-K `rho_c≈9×10^-4 Ω cm²`;
- the actual deposition method, tool, base pressure, rates, source geometry and thermal history remain unpublished in RP-01;
- same-UWA primary evidence does establish angled thermal evaporation for HgCdTe contact-metal deposition in nearby 1998 fabrication work;
- P26 is already a strong empirical qualification window, so Round 38 should **not duplicate P26**.

Round 38 should:

1. audit P09/P09A/P26 and its register first;
2. search primary UWA papers/theses/proceedings for exact Cr/Au deposition tool, thermal/e-beam method, source boats/crucibles, base pressure, deposition rate, substrate cooling/orientation and lift-off details;
3. distinguish same-UWA thermal evaporation evidence from exact RP-01 identity;
4. re-audit whether the RP-01 proposed load-lock RIE->metal architecture was actually used on reported devices or merely proposed;
5. recover any same-lab quantitative metal deposition rates/pressures from 1997–2005 HgCdTe device papers;
6. do not import angled ion milling or other surface treatment from photovoltaic structures into the RP-01 RIE-contact branch;
7. if historical apparatus/rates remain unavailable, create a focused `P26A` deposition-apparatus/rate/vacuum instantiation addendum + register rather than inventing values;
8. integrate R20 into P16A without marking it closed until an actual laboratory tool/branch is instantiated;
9. update source/gap ledgers, checkpoint and AGENTS.

If the P26 audit shows this exact search has already been exhausted, pivot within Round 38 to R12/R16 lithography product/developer source recovery rather than repeating prior work.
