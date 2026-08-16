# P32 — Mask-1 wet-mesa lithography empirical process window

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Turn the RP-01 Mask-1 mesa-delineation step into an empirically bounded lithography process without manufacturing a historical resist identity that the canonical paper does not disclose.

RP-01 directly establishes:

- Mask 1 is the first photolithographic masking step;
- it defines wet-chemical mesa delineation of the n-HgCdTe detector elements;
- the starting active layer is approximately 9.5 µm thick;
- mesa isolation precedes anodic-oxide passivation.

P32 controls the coupled chain:

`incoming HgCdTe surface -> resist coat/bake -> exposure/development -> developed resist geometry -> P28 bromine-based wet etch -> resist survival/edge retreat -> final mesa CD/profile/isolation -> resist strip -> surface-state handoff to P25`.

P32 supplements P14 and P28. It does not claim to reconstruct an unpublished UWA/Fermionics Mask-1 traveler.

---

## 2. Evidence classes

### `DIRECT-RP01`
Directly stated by Smith et al. 2001.

### `PRIMARY-HGCDTE-DEEP-WET-MASK`
Primary patent/process evidence where photoresist is explicitly used to mask a through/deep HgCdTe wet etch.

### `PRIMARY-HGCDTE-HBR-MASK`
Primary HgCdTe process evidence specifically using photoresist with Br2/HBr chemistry.

### `PRIMARY-NOVOLAK-FAMILY`
Primary HgCdTe process evidence establishing novolak photoresist compatibility with HgCdTe etch processing without identifying RP-01 Mask-1.

### `PRIMARY-X028-ETCH-COUPLING`
Srivastav et al. 2005 x=0.28 wet-mesa evidence showing that photoresist parameters affect the etched profile and that higher etch temperature attacks/deteriorates photoresist.

### `LOCAL-QUAL`
Locally measured transfer process.

No transfer resist identity may be relabeled `DIRECT-RP01`.

---

## 3. Historical RP-01 state

The canonical 2001 paper shows the sequence:

`starting n-HgCdTe on insulating substrate -> wet chemical mesa delineation etch (Mask 1) -> photoresist removal / passivation -> anodic oxide`.

The recovered article does **not** state for Mask 1:

- photoresist manufacturer/product;
- positive/negative tone;
- film thickness;
- spin speed/acceleration/time;
- dehydration or adhesion promoter;
- bake temperature/time;
- exposure wavelength/mode/dose;
- developer identity/concentration/time;
- post-develop bake/ash;
- strip solvent/time;
- resist-to-etch selectivity;
- mask bias;
- final mesa outer dimensions.

All remain `OPEN-HISTORICAL`.

Do not copy the RP-01 Mask-2 `4–5 µm / 80 °C 30 min / chlorobenzene 30 min` process into Mask 1. Mask 2 serves RIE + metal lift-off and is a different functional resist process.

---

## 4. Same-UWA wet-mesa requirement

Smith et al. 2000 directly demonstrate that n-type x≈0.31 HgCdTe photoconductors fabricated using bromine/HBr wet chemical mesa etching can reach background-limited detector performance under the reported measurement condition.

This closes the **mesa chemistry family and device function**, but not the Mask-1 resist recipe.

P32 therefore preserves bromine/HBr compatibility as the first chemical requirement for any candidate resist while keeping the exact UWA resist identity open.

---

## 5. Strong primary transfer branch A — deep HgCdTe patterning with Hunt 180CP

U.S. Patent 4,686,373 describes an HgCdTe infrared-imager process with an unusually explicit first patterning step.

The HgCdTe had been thinned to approximately 12 µm above the silicon processor surface before patterning.

The process states:

- resist: `180CP`, Hunt;
- spin: `4000 rpm / 20 s`;
- dry/bake: `60 °C / 3 min`;
- exposure: performed, but wavelength/dose/mode not stated in the accessible text;
- development: `30 s`;
- rinse: `15 s`;
- ash: `200 W / 30 s`;
- etch: fresh `1/8% bromine-methanol`, spray etched until separation trenches cleared to the underlying epoxy;
- residual thin epoxy was plasma ashed;
- photoresist was then removed.

### Evidence interpretation

This is strong `PRIMARY-HGCDTE-DEEP-WET-MASK` evidence that a conventional positive-resist-type photolithographic film could protect HgCdTe during an approximately through-thickness bromine wet etch on material of similar thickness scale to RP-01.

### Restrictions

It is not RP-01 because:

- device architecture is a bonded imager, not the UWA photoconductor;
- etchant is bromine/methanol rather than bromine/HBr/EG;
- spray etching differs from the P28 immersion/controlled-wet branch;
- 180CP historical product identity does not establish availability or equivalence today;
- exposure and developer identities are not fully disclosed.

Do not adopt 180CP as the production resist solely because this historical branch succeeded.

---

## 6. Strong primary transfer branch B — AZ4620 with Br2/HBr deep mesas

CN101740502B describes HgCdTe deep-micro-mesa formation using a photoresist mask and Br2/HBr chemistry.

General disclosed ranges:

- photoresist masking-film thickness: `1–6 µm`;
- resist opening width: `1–8 µm`;
- Br2:HBr etchant explicitly defined by **volume ratio** over `0.1–1% : 1`;
- etch time `5–150 s`;
- post-etch DI-water cleaning;
- acetone removal of the photoresist.

One explicit embodiment states:

- commercial resist `AZ4620`;
- resist thickness `3 µm`;
- opening width `5 µm`;
- square mask feature approximately `45 µm` with 50-µm center-to-center spacing;
- Br2:HBr volume ratio `0.5% : 1`;
- etchant delivered by a spin-coating-like operation at `2000 rpm / 20 s`.

### Evidence interpretation

This is the strongest recovered **product-identified** `PRIMARY-HGCDTE-HBR-MASK` branch.

It directly demonstrates that AZ4620 at a 3-µm film thickness can participate in a Br2/HBr HgCdTe deep-mesa process.

### Restrictions

It does not prove compatibility with the P28 `2% Br2 in 3:1 EG:HBr` transfer chemistry, because:

- P28 has a different bromine concentration convention and includes EG;
- the patent uses a rotating small-volume etchant delivery geometry rather than the Srivastav bath;
- etch duration and mesa depth are process-specific;
- resist soft-bake, exposure and developer conditions for the embodiment are not completely specified in the accessible text.

AZ4620 is therefore a strong **screening candidate**, not the historical RP-01 resist.

---

## 7. Novolak-family support

U.S. Patent 5,157,000 describes HgCdTe/ZnS etch processing with a photoresist mask and explicitly identifies a `NOVOLAK` photoresist composition as suitable in the claimed process. The process combines dry etching followed by bromine/methanol wet finishing.

This supports the broad historical compatibility of novolak-family resists with HgCdTe processing, but it does not identify Mask 1 or establish resistance to P28 chemistry.

### P32 consequence

The first local candidate set should stay within well-characterized thick positive novolak/DNQ-style resist families unless direct empirical screening provides a reason to expand.

Do not infer that Mask 1 and Mask 2 used the same commercial resist.

---

## 8. Srivastav coupling: photoresist is part of the etch physics

The x=0.28 Srivastav mesa study states that the measured anisotropy/profile is sensitive to parameters including:

- photoresist thickness;
- feature area/geometry;
- HgCdTe film thickness.

The study also observed:

- faster etching near photoresist edges / trenching;
- sidewall transport effects;
- high-temperature conditions producing ragged edges/sidewalls;
- high-temperature etchant attacking the photoresist;
- lower-temperature etching preserving the photoresist better and improving profile control.

Therefore the Mask-1 resist is **not** an independent upstream layer whose only criterion is chemical survival.

The coupled response is:

`{resist thickness, resist profile, feature geometry, etchant chemistry, bath T, agitation, etch time}`

`-> {resist loss, edge retreat, R_V, R_L, trenching, mesa-top CD, mesa-base CD, sidewall profile}`.

Any change to the resist process invalidates a previously established P28 mask-bias calibration until equivalence is demonstrated.

---

## 9. Required Mask-1 candidate characterization before etching

For every candidate resist/process record:

- manufacturer/product;
- chemistry/family where documented;
- lot and expiry;
- viscosity/product grade;
- substrate surface history and delay from prior process;
- dehydration step, if any;
- adhesion promoter, if any;
- dispense volume/method;
- spin speed;
- acceleration;
- spin time;
- edge-bead handling;
- soft-bake method, temperature and time;
- film thickness at multiple locations;
- exposure tool/wavelength/mode;
- calibrated dose;
- post-exposure treatment, if any;
- developer identity/concentration;
- develop time/agitation;
- rinse identity/time;
- post-develop dry/bake/ash;
- developed opening CD and resist mesa CD;
- residual scum;
- pinholes;
- adhesion defects;
- sidewall/profile metric.

A resist process may not enter P28 qualification on appearance alone.

---

## 10. Resist-thickness selection principle

The historical RP-01 Mask-1 thickness remains open.

Do not set thickness by a generic rule such as `resist thickness >= HgCdTe thickness`.

The wet etchant attacks primarily the exposed HgCdTe and may chemically/physically degrade the resist at a very different rate. What matters is the **remaining intact mask geometry through the full etch**.

For each candidate define:

- `h_PR,0` — developed resist thickness before wet etch;
- `h_PR,f` — remaining resist thickness immediately after wet etch;
- `Delta h_PR = h_PR,0 - h_PR,f`;
- `Delta CD_PR` — lateral edge retreat/swelling of the resist;
- pinhole/blister/lift fraction.

A nominal selectivity may be reported as

`S_PR = d_HgCdTe / Delta h_PR`

only when `Delta h_PR` is measured reliably and the resist does not fail by delamination, swelling, cracking or edge lift.

A high numerical `S_PR` does not pass a resist that loses adhesion or CD integrity.

---

## 11. First local candidate hierarchy

### Branch 1 — product-identified HBr-compatible screening candidate

`AZ4620` is the strongest recovered product-identified first screening candidate because primary HgCdTe deep-mesa evidence explicitly uses it with Br2/HBr.

Initial local processing conditions for AZ4620 must follow the current manufacturer technical data for coating/exposure/development **only after independently verifying that the resulting film thickness/profile meets P32 requirements**. Manufacturer values are not historical RP-01 values.

### Branch 2 — thick positive novolak control

Use one additional currently available, well-characterized thick positive novolak/DNQ-style resist as a control branch selected for the target film-thickness range and chemical compatibility.

This branch must receive its own recipe ID.

### Historical control — 180CP

The Hunt 180CP process is retained as historical evidence and may be reproduced only if authentic material/process documentation is available. Do not substitute a similarly named current resist and call it equivalent.

---

## 12. Exposure/development qualification

For each candidate resist, perform a dose/development matrix on a geometry that includes:

- large protected mesa areas representative of RP-01;
- trenches/lines at the expected mesa-edge scale;
- smaller diagnostic openings;
- isolated and dense features.

Measure before wet etching:

- developed CD;
- resist thickness;
- edge slope/profile;
- scum/residue;
- adhesion;
- pinhole density.

Do not choose exposure/development solely from nominal mask CD. The winning condition is the one that remains dimensionally stable through P28.

---

## 13. Etch-survival qualification

P32 and P28 shall be qualified together.

For each resist condition, expose matched coupons to the actual locally defined P28 etchant branch and record:

- bath temperature;
- bath age/genealogy;
- agitation;
- actual exposure time;
- resist thickness before/after;
- resist edge position before/after;
- swelling/softening;
- cracking/crazing;
- blistering/lifting;
- pinholes;
- discoloration;
- mesa depth;
- lateral undercut;
- trenching at mask edges;
- sidewall profile.

Because Srivastav directly observed stronger photoresist attack at elevated temperature, temperature qualification shall include resist-survival response, not only HgCdTe etch rate.

---

## 14. Mask bias must be empirical

Let:

- `CD_mask` = mask design dimension;
- `CD_PR` = developed resist dimension;
- `CD_top` = final mesa-top dimension;
- `CD_base` = final mesa-base dimension where measurable.

Define transfer terms with a documented sign convention:

`Delta_CD_lith = CD_PR - CD_mask`

`Delta_CD_wet = CD_top - CD_PR`

`Delta_CD_total = CD_top - CD_mask`.

For approximately symmetric lateral retreat, a first-order design correction may use half the measured total width change per edge, but **only after the local geometry confirms symmetry**.

Do not derive final Mask-1 bias from Srivastav's mean anisotropy alone. Anisotropy, edge trenching and resist retreat are geometry/process dependent.

---

## 15. Through-layer endpoint remains a P28 electrical gate

P32 does not replace the P28 mesa endpoint rule.

The RP-01 active layer is approximately 9.5 µm, but the Mask-1 etch passes only when:

- measured incoming local HgCdTe thickness is known;
- measured etch depth crosses the conducting layer robustly;
- final mesa-to-mesa electrical isolation passes;
- resist remains intact through the required overetch;
- lateral undercut/profile remain acceptable.

A resist process that survives a nominal calculated time but fails before the electrical-isolation endpoint is not qualified.

---

## 16. Resist strip is a surface process

The historical RP-01 Mask-1 strip is open.

Primary transfer processes demonstrate that acetone is used to remove photoresist after some HgCdTe mesa processes, while other process families simply state that the resist is removed.

Do not infer acetone as RP-01 historical practice.

For every local strip branch record:

- strip chemistry;
- grade/lot;
- bath temperature;
- immersion/spray duration;
- agitation/ultrasonics state;
- rinse sequence;
- dry method;
- elapsed time from P28 etch end to resist removal;
- elapsed time from strip/rinse completion to P25 anodization;
- optical/DIC surface result;
- residue metric where available.

No ultrasonics may be introduced by default. Mechanical damage/delamination must be qualified first.

---

## 17. Post-strip surface-state gate

Mask-1 removal occurs immediately upstream of native anodic-oxide passivation in the RP-01 sequence.

Therefore P32 shall hand off to P25/P28 with:

- final mesa depth and profile;
- electrical isolation result;
- final mesa top/base dimensions;
- sidewall condition;
- resist-residue inspection;
- strip/rinse/dry history;
- `t_etch_to_strip`;
- `t_strip_to_P25`;
- ambient/storage condition.

A visually clean resist strip is insufficient if it causes a changed P25 anodization signature or degraded detector surface state.

---

## 18. Required local qualification responses

For each candidate resist recipe evaluate at minimum:

### Lithography
- film-thickness mean/uniformity;
- developed CD error;
- pinhole/adhesion defect density;
- developed profile.

### Wet-etch survival
- remaining resist thickness;
- edge retreat;
- swelling/lift/crack fraction;
- breakthrough/pinhole attack.

### Mesa transfer
- vertical etch depth;
- lateral undercut;
- anisotropy;
- edge trenching;
- top/base CD;
- sidewall roughness/profile;
- electrical isolation.

### Strip/passivation handoff
- residue/surface metric;
- P25 anodization `V(t)`/charge response;
- post-passivation leakage/surface behavior where measurable.

### Device closure
- final active geometry;
- P10 field normalization geometry;
- P11/P12 responsivity/noise/D* on representative devices.

---

## 19. Failure modes

Preserve and classify:

- poor initial wetting/coating on HgCdTe;
- pinholes;
- incomplete development/scum;
- overdevelopment/edge loss;
- resist lift in HBr/Br2 chemistry;
- swelling/softening;
- thermal flow;
- bromine attack;
- mask-edge trenching;
- asymmetric undercut;
- resist breakthrough before isolation;
- excessive mask bias requirement;
- strip residue;
- strip-induced surface damage;
- altered P25 anodization behavior;
- post-passivation leakage/noise degradation.

Do not discard failed resist/process branches from the development record.

---

## 20. Release rule

A Mask-1 process can become `LOCAL-QUALIFIED` only when one explicit resist/lithography/strip branch demonstrates across independent etch batches/material runs:

1. reproducible coating and developed geometry;
2. complete survival through the required P28 through-layer etch and qualified overetch;
3. bounded edge retreat and mask bias;
4. acceptable mesa top/base geometry and sidewall state;
5. electrical isolation;
6. clean/reproducible resist removal;
7. stable P25 passivation handoff;
8. no unacceptable detector-performance penalty.

Historical identity may remain `OPEN` even after a local process is qualified.

---

## 21. Primary references

1. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *Journal of Electronic Materials* 29, 853–858 (2000), DOI `10.1007/s11664-000-0237-7`.
3. V. Srivastav et al., “Etching of mesa structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005), DOI `10.1007/s11664-005-0203-5`.
4. U.S. Patent `US4686373A`, “Infrared imager.”
5. Chinese Patent `CN101740502B`, HgCdTe micro-mesa photosensitive-array forming method.
6. U.S. Patent `US5157000A`, “Method for dry etching openings in integrated circuit layers.”
7. U.S. Patent `US6657194B2`, “Multispectral monolithic infrared focal plane array detectors.”

---

## 22. Current unresolved items

Still `OPEN-HISTORICAL` for RP-01 Mask 1:

- resist manufacturer/product/family;
- resist thickness;
- spin process;
- bake;
- exposure tool/wavelength/dose;
- developer;
- post-develop treatment;
- exact mesa mask dimensions;
- resist-to-UWA Br2/HBr selectivity;
- resist-strip chemistry;
- mask bias;
- etch-to-strip and strip-to-anodization timing.

P32 closes a defensible empirical qualification path without inventing any of these values.
