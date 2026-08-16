# Source ledger addendum — Round 39 Mask-2 / Mask-1 lithography documentary-limit audit

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Scope

Round 39 audited the unresolved commercial-photoresist / exposure / developer / strip identity for both RP-01 lithography masks. The objective was to recover direct or same-UWA process identity if possible, while avoiding a redundant P27A/P32A procedure if the existing empirical qualification layers were already complete.

---

## S39-01 — Smith et al. 2001 canonical RP-01 paper

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

Direct Mask-2 fingerprint retained:

- photoresist thickness approximately `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene treatment `30 min`;
- then patterned/developed/water rinsed;
- same resist remains through the localized CH4/H2 RIE;
- same resist supports lift-off of Cr `30 nm` / Au `270 nm`.

Direct Mask-1 information remains limited to photolithographic delineation of the wet-etched mesa process; no commercial resist product or full lithography traveler is named.

Still not direct for either mask:

- resist manufacturer/product/lot/formulation;
- spin speed/acceleration/time;
- exposure tool/wavelength/mode/dose;
- developer identity/concentration/time;
- Mask-1 bake/thickness/strip;
- Mask-2 exact chlorobenzene bath state and exposure ordering beyond the paper wording;
- lift-off solvent/time/agitation.

---

## S39-02 — P14A/P27 repository audit

`procedures/P14A_CHLOROBENZENE_LIFTOFF_LINEAGE_ADDENDUM.md` and `procedures/P27_MASK2_PHOTORESIST_EXPOSURE_DEVELOPER_LIFTOFF_EMPIRICAL_WINDOW.md` were re-read before new writing.

**Result:** P27 is already method-complete for local Mask-2 transfer. It controls:

- product/lot/formulation;
- coating/thickness map;
- direct 80 °C / 30-min RP-01 bake center;
- 30-min chlorobenzene bath state;
- pre- versus post-exposure chlorobenzene branches;
- calibrated exposure/dose matrix;
- product-matched developer;
- CD/undercut/profile metrology;
- P08 plasma survival;
- P26 metal-deposition compatibility;
- lift-off solvent/agitation escalation;
- TLM and detector-function closure.

**Round-39 decision:** do **not** create P27A merely because the historical product remains unknown.

---

## S39-03 — John Kenion White 2005 UWA PhD thesis

John White, *Mid-wave infrared HgCdTe photodiode technology based on plasma induced p-to-n type conversion*, PhD thesis, University of Western Australia, 2005.

Official UWA record identifies a downloadable PDF and confirms direct relevance to UWA HgCdTe RIE fabrication/passivation technology.

**Current retrieval state:** the official PDF path was identified but returned `403 Forbidden` through the present retrieval route.

**Class:** `IDENTIFIED-NOT-RECOVERED`.

Do not infer that the thesis lacks Mask-2 resist/developer/lift-off details. The relevant full experimental text was not available for inspection in Round 39.

---

## S39-04 — same-UWA 1994–2001 fabrication lineage

Official UWA records were rechecked for:

- J. F. Siliquini et al., “Improved device technology for epitaxial Hg1-xCdxTe infrared photoconductor arrays,” *Semiconductor Science and Technology* 9 (1994) 1515–1522, DOI `10.1088/0268-1242/9/8/013`;
- Siliquini/Faraone, “Two-Dimensional Infrared Focal Plane Arrays Based on HgCdTe Photoconductive Detectors,” *Semiconductor Science and Technology* 11 (1996) 1906–1911, DOI `10.1088/0268-1242/11/12/024`;
- Musca/Siliquini/Parish/Dell/Faraone, “A monolithic dual-band HgCdTe infrared detector,” *Journal of Crystal Growth* 184–185 (1998) 1284–1287, DOI `10.1016/S0022-0248(98)80266-2`;
- Smith/Musca/Redfern/Dell/Faraone, “Reactive ion etching for mesa structuring in HgCdTe,” *JVST A* 17 (1999) 2503–2509;
- Smith/Musca/Redfern/Dell/Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *J. Electronic Materials* 29 (2000) 853–858;
- Musca/Smith/Dell/Faraone 1999 contact/passivation proceedings paper.

These establish strong same-laboratory fabrication continuity but the accessible indexed records did not expose a commercial Mask-1 or Mask-2 resist/developer traveler.

**Class:** `SAME-UWA-BIBLIOGRAPHIC / PROCESS-IDENTITY-NOT-RECOVERED`.

---

## S39-05 — Srivastav et al. 2005 wet-mesa primary paper

V. Srivastav et al., “Etching of mesa structures in HgCdTe,” *Journal of Electronic Materials* 34 (2005) 1440–1445, DOI `10.1007/s11664-005-0203-5`.

Author-uploaded full text was re-read through its experimental section.

Directly reported:

- x≈0.28 HgCdTe;
- two photolithographic masks (600-µm linear structures with 50-µm trenches; 2-D mesas separated by 30-µm trenches);
- Br2/HBr/EG etch study;
- photoresist thickness/feature area/HgCdTe thickness affect the measured etch profile/anisotropy;
- edge trenching occurs near photoresist boundaries;
- high-temperature etching attacks/deteriorates photoresist;
- lower temperature improves photoresist preservation/profile control.

Not reported in the recovered primary text:

- resist manufacturer/product;
- resist film thickness used in the experiments;
- spin recipe;
- bake;
- exposure tool/dose;
- developer;
- strip chemistry.

**Class:** `PRIMARY-X028-ETCH-COUPLING`, not product identity.

---

## S39-06 — CN101740502B product-identified HgCdTe Br2/HBr branch

Chinese patent `CN101740502B`, HgCdTe deep micro-mesa photosensitive-array forming method.

Direct embodiment:

- commercial photoresist `AZ4620`;
- resist thickness `3 µm`;
- mask opening width `5 µm`;
- approximately 45-µm square pattern / 50-µm center spacing;
- Br2:HBr defined by volume ratio, example `0.5% : 1`;
- etchant rotational delivery example `2000 rpm / 20 s`;
- DI-water clean;
- acetone photoresist removal.

**Class:** `PRIMARY-HGCDTE-HBR-MASK`.

This remains the strongest recovered product-identified Mask-1 transfer branch, but it is not RP-01 and not the P28 Br2/EG/HBr bath.

---

## S39-07 — current AZ P4620 commercial documentation

Current commercial/vendor documentation for AZ P4620 describes the P4000 positive thick-resist family and a normal AZ P4620 film-thickness range of approximately `5–30 µm`, with common KOH/TMAH developer compatibility.

**Class:** `CURRENT-VENDOR-DOCUMENTATION`.

Important conflict/caution:

- historical/primary CN101740502B embodiment: `AZ4620`, `3 µm`;
- current commercial documentation: normal range approximately `5–30 µm`.

This difference may arise from formulation generation, product grade, thinning, spin conditions, or documentation convention. Round 39 does not resolve which.

**Permanent implication:** a commercial product name repeated across decades is not proof of formulation/process equivalence. A current AZ P4620 lot must be treated as a new local branch and thickness/exposure/development/etch survival must be measured.

---

## S39-08 — P32 repository audit

`procedures/P32_MASK1_WET_MESA_LITHOGRAPHY_EMPIRICAL_PROCESS_WINDOW.md` and its traveler were re-read.

**Result:** P32 is already method-complete. It contains:

- product-identified AZ4620 Br2/HBr transfer candidate;
- Hunt 180CP deep-HgCdTe historical transfer branch;
- thick positive novolak control branch;
- coating/exposure/development qualification;
- P28-coupled resist-survival measurement;
- empirical mask-bias decomposition;
- through-layer isolation endpoint;
- strip and P25 surface-state handoff;
- device-level release criteria.

**Round-39 decision:** do **not** create a redundant P32A.

---

# Round-39 negative-search record

No primary/same-UWA source recovered an exact RP-01:

### Mask 2
- commercial resist identity;
- viscosity/solids/dilution;
- spin recipe;
- exposure tool/wavelength/dose;
- developer product/concentration/time;
- chlorobenzene temperature/grade/agitation;
- exact lift-off solvent/time/agitation.

### Mask 1
- commercial resist identity;
- thickness;
- spin/bake/exposure/developer;
- resist-to-RP01-wet-etch selectivity;
- strip chemistry;
- mask bias or exact mesa-mask dimensions.

These are `NOT-RECOVERED`, not proved absent.

---

# Round-39 source conclusion

The documentary record has reached a practical limit for generic web-accessible UWA lithography searches. The repository already has controlled qualification paths for both masks. Further progress now depends more on **explicit branch selection and actual tool/product instantiation** than on creating additional lithography procedures.
