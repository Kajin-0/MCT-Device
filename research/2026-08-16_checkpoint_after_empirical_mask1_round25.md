# Checkpoint — after empirical Mask-1 / wet-mesa lithography Round 25

**Date:** 2026-08-16 America/New_York

## Repo state advanced

New controlled empirical module:

- `procedures/P32_MASK1_WET_MESA_LITHOGRAPHY_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P32_MASK1_WET_MESA_LITHOGRAPHY_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND25.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND25.md`

P32 supplements P14 and P28.

---

## Main scientific/process conclusion

The exact RP-01 Mask-1 resist recipe is still not recovered.

However, primary HgCdTe process literature now provides enough concrete empirical evidence to stop treating Mask 1 as a generic lithography placeholder.

The recovered evidence establishes:

1. same-UWA x≈0.31 Br/HBr wet mesas can support background-limited photoconductor performance;
2. a product-identified historical resist process (Hunt 180CP) protected approximately 12-µm-class HgCdTe during a through-thickness bromine/methanol separation etch;
3. a product-identified AZ4620 branch directly masks deep HgCdTe mesas in Br2/HBr chemistry;
4. 3-µm and 5-µm resist-thickness examples exist in primary Br2/HBr HgCdTe mesa processes;
5. novolak photoresist family compatibility is explicitly supported in primary HgCdTe processing;
6. Srivastav x=.28 shows photoresist thickness/geometry and etch temperature influence anisotropy, edge trenching and resist survival.

Therefore P32 is a coupled lithography/etch/passivation qualification problem, not a stand-alone exposure recipe.

---

## Strongest product-identified HBr candidate

`AZ4620` is now the strongest recovered product-identified **Br2/HBr deep-mesa transfer candidate**.

Primary patent embodiment:

- AZ4620;
- 3 µm mask thickness;
- 5 µm mask opening;
- Br2:HBr = 0.5%:1 by explicit volume ratio;
- etchant spin delivery 2000 rpm / 20 s;
- DI-water post-etch clean;
- acetone resist strip.

Restrictions:

- different device geometry;
- different etchant formulation and delivery from P28;
- no proof of compatibility with nominal 2% Br2 / 3:1 EG:HBr;
- not historical RP-01 identity.

Use: first local screening candidate only.

---

## Deep through-HgCdTe historical lithography branch

US4686373A provides:

- HgCdTe thinned to ~12 µm;
- Hunt 180CP;
- 4000 rpm / 20 s;
- 60 °C / 3 min dry;
- exposed;
- 30 s develop;
- 15 s rinse;
- 200 W / 30 s ash;
- fresh 1/8% Br2/methanol spray etch until separation trenches clear to epoxy;
- resist removal after etch.

This is strong proof of a conventional photoresist mask surviving a bromine wet etch through HgCdTe on essentially the same thickness scale as RP-01's 9.5-µm layer.

Do not transfer the process as RP-01 because chemistry/device/etch mode differ.

---

## Resist thickness evidence

Primary Br2/HBr mesa sources include:

- general 1–6 µm photoresist masking-film range;
- AZ4620 embodiment at 3 µm;
- a separate multispectral HgCdTe mesa process at 5 µm resist with 4% Br2/HBr.

These numbers are evidence that micron-class positive resist can survive HgCdTe HBr-based mesa processing.

They do **not** define P32's final thickness.

Release requires actual:

`h_PR,0 -> h_PR,f + edge-retreat + adhesion/pinhole state`

through the locally selected P28 chemistry.

---

## Srivastav coupling retained

Primary x=.28 article states/profile data support:

- sensitivity to photoresist thickness and feature geometry;
- faster local etching/trenching at resist edges;
- high-T resist attack;
- high-T ragged sidewalls;
- lower-T improved profile control and photoresist preservation.

Therefore changing Mask-1 resist/process invalidates a P28 dimensional transfer calibration until equivalence is demonstrated.

---

## Mask-bias model

P32 now requires direct measurement of:

- `CD_mask`;
- `CD_PR` after develop;
- `CD_top` after P28;
- `CD_base` where measurable.

With:

- `Delta_CD_lith = CD_PR-CD_mask`;
- `Delta_CD_wet = CD_top-CD_PR`;
- `Delta_CD_total = CD_top-CD_mask`.

No mask bias is derived solely from the source anisotropy value.

---

## Resist strip / P25 handoff

Acetone is directly used in some primary HgCdTe mesa branches, but exact RP-01 strip remains open.

P32 records:

- strip chemistry and lot;
- temperature/time/agitation;
- rinse/dry;
- `t_etch_to_strip`;
- `t_strip_to_P25`;
- residue/surface inspection;
- P25 anodization response.

Ultrasonics remain prohibited by default until mechanical-damage equivalence is demonstrated.

---

## Historical gaps after Round 25

Still unrecovered:

- UWA Mask-1 resist identity;
- UWA Mask-1 thickness;
- spin/bake;
- exposure wavelength/dose/mode;
- developer;
- post-develop treatment;
- resist strip;
- exact UWA Br/HBr formulation;
- final RP-01 mesa outer dimensions;
- UWA mask bias;
- exact Srivastav resist product/thickness;
- direct resist-selectivity number in Srivastav's selected chemistry.

These remain `OPEN-HISTORICAL`, not proven unavailable in theses/lab records.

---

## Strongest next empirical round

Proceed with **Round 26: P05 Hall / Van der Pauw contact fabrication and cryogenic measurement execution**.

Reason:

Many process modules now release on Hall-derived electrical state, but the practical P05 contact fabrication, sample geometry, ohmic verification, cryostat/magnet wiring, current range, field sweep, thermal stabilization and uncertainty path remain critical to reproducibility.

Priority recovery:

1. direct RP-01/UWA Hall test structure/contact metallurgy for the n-HgCdTe and RIE-converted material;
2. Au/In/indium/soldered or evaporated contact practices in primary x≈.30 HgCdTe Hall studies;
3. actual Van der Pauw coupon dimensions and contact size/location;
4. contact anneal, if any;
5. current magnitude and self-heating criterion;
6. field range and sweep/reversal sequence;
7. 80/77 K temperature stabilization;
8. magnet calibration and Hall-voltage polarity convention;
9. resistivity and Hall uncertainty propagation;
10. multicarrier escalation and Hall-factor limitations.

Create P33 empirical Hall/VdP execution window/traveler if primary evidence is sufficient.

Alternative if P05 is already adequately executable after audit: pivot to P15 die attach / wire bond / cryogenic package empirical materials and geometry.
