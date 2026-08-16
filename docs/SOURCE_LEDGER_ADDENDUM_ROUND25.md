# Source ledger addendum — Round 25 Mask-1 / wet-mesa lithography

**Date:** 2026-08-16 America/New_York

## Scope

Primary-source recovery for RP-01 Mask-1 photoresist, coating, exposure/development, wet-etch survival, mask bias and resist stripping.

---

## S25-01 — Smith et al. 2001 canonical RP-01

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001). DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

Recovered Mask-1 facts:

- first masking step is wet chemical mesa delineation;
- photolithographic masking used for electrical isolation;
- Mask-1 resist details are not stated in accessible full article text;
- Mask-2 4–5 µm/chlorobenzene process is separately disclosed and must not be transplanted into Mask 1.

**Use:** historical architecture only.

---

## S25-02 — Smith et al. 2000 same-UWA wet mesa

E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *Journal of Electronic Materials* 29, 853–858 (2000). DOI `10.1007/s11664-000-0237-7`.

**Class:** `SAME-UWA-WET-MESA`.

Relevant facts:

- n-type x≈0.31 HgCdTe photoconductors compared wet Br/HBr and H2/CH4 RIE mesas;
- wet devices reached background-limited detector performance in the reported measurement;
- article does not close Mask-1 resist identity/process.

**Use:** establishes same-lineage Br/HBr mesa compatibility and device closure, not resist recipe.

---

## S25-03 — Srivastav et al. 2005

V. Srivastav et al., “Etching of mesa structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005). DOI `10.1007/s11664-005-0203-5`.

**Class:** `PRIMARY-X028-ETCH-COUPLING`.

Recovered lithography-coupling facts:

- etch anisotropy/profile sensitive to photoresist thickness, feature area/geometry and film thickness;
- accelerated etching/trenching observed near photoresist edges;
- high-temperature etching produced ragged sidewalls and attacked photoresist;
- lower-temperature etching improved profile control and preserved photoresist against thermal deterioration/flow;
- exact resist product/thickness/process is not recovered from accessible article text.

**Use:** proves Mask-1 process variables are coupled into P28 etch geometry.

---

## S25-04 — US4686373A Infrared imager

U.S. Patent `US4686373A`, “Infrared imager.”

**Class:** `PRIMARY-HGCDTE-DEEP-WET-MASK / DIFFERENT-DEVICE-AND-CHEMISTRY`.

Explicit first-patterning branch:

- HgCdTe thinned to approximately 12 µm above silicon surface;
- Hunt `180CP` resist;
- spin `4000 rpm / 20 s`;
- dry `60 °C / 3 min`;
- exposed;
- develop `30 s`;
- rinse `15 s`;
- ash `200 W / 30 s`;
- fresh `1/8% bromine-methanol` spray etch until separation trenches clear to epoxy;
- remaining thin epoxy ashed;
- photoresist removed.

Restrictions:

- bonded HgCdTe/Si imager process;
- Br/MeOH rather than Br/HBr/EG;
- spray etch;
- exposure wavelength/dose and developer identity not closed;
- does not identify RP-01 resist.

High value: directly demonstrates a product-identified photoresist process surviving an approximately through-thickness bromine wet etch on HgCdTe of similar thickness scale to RP-01.

---

## S25-05 — CN101740502B deep HgCdTe micro-mesa

Chinese Patent `CN101740502B`, HgCdTe micro-mesa photosensitive-array forming method.

**Class:** `PRIMARY-HGCDTE-HBR-MASK`.

General ranges:

- resist mask thickness `1–6 µm`;
- resist opening `1–8 µm`;
- Br2:HBr **volume ratio** `0.1–1% : 1`;
- etch time `5–150 s`;
- DI-water cleaning after etch;
- acetone resist removal.

Explicit embodiment:

- commercial `AZ4620`;
- resist thickness `3 µm`;
- opening width `5 µm`;
- square mask feature about `45 µm`, center pitch `50 µm`;
- Br2:HBr volume ratio `0.5% : 1`;
- etchant spin-delivery `2000 rpm / 20 s`.

Restrictions:

- different etchant formulation/delivery from P28;
- not RP-01;
- complete resist lithography recipe not disclosed in accessible translation.

High value: strongest recovered product-identified Br2/HBr HgCdTe deep-mesa mask branch.

---

## S25-06 — US5157000A novolak HgCdTe etch mask

U.S. Patent `US5157000A`, “Method for dry etching openings in integrated circuit layers.”

**Class:** `PRIMARY-NOVOLAK-FAMILY`.

Relevant claims:

- photoresist pattern on HgCdTe or ZnS;
- claimed resist may be a `NOVOLAK` composition;
- dry etch followed by bromine/methanol wet finishing;
- photoresist removed afterward.

**Use:** historical family-level compatibility only.

---

## S25-07 — US6657194B2 multispectral HgCdTe mesa

U.S. Patent `US6657194B2`, “Multispectral monolithic infrared focal plane array detectors.”

**Class:** `PRIMARY-HGCDTE-DEEP-WET-MASK / DIFFERENT-DEVICE`.

Relevant facts:

- HgCdTe mesa selectively etched using photolithography;
- protected with `5 µm` thick photoresist;
- `4% bromine in HBr acid` used for etch;
- significant lateral undercut intentionally generated, with sidewall slope around 45° in described structure;
- photoresist subsequently removed with acetone;
- later surface clean included dilute 0.05% bromine/methanol followed by flowing DI water.

Restrictions:

- multispectral MBE heterostructure and intentionally sloped mesa;
- not RP-01 chemistry/geometry;
- no resist identity.

High value: confirms 5-µm photoresist class can be used in a Br2/HBr HgCdTe mesa process and demonstrates why resist/mask geometry couples to final slope/undercut.

---

# Round-25 synthesis

1. **Exact RP-01 Mask-1 resist remains unrecovered.**
2. **AZ4620 is the strongest product-identified Br2/HBr deep-mesa transfer candidate**, but not RP-01 identity and not automatically compatible with the P28 EG-containing formulation.
3. **Hunt 180CP provides the strongest recovered through-thickness historical lithography sequence** on ~12-µm HgCdTe, but uses Br/MeOH spray etching.
4. Primary HgCdTe sources support a broader positive/novolak resist family, but family evidence is not product identity.
5. Srivastav proves that photoresist thickness/geometry and temperature change mesa etch profile; resist qualification must therefore be coupled directly to P28.
6. Resist stripping is part of the surface/passivation handoff and cannot be treated as chemically invisible.

---

# Negative / unresolved searches

Not recovered:

- UWA Mask-1 resist manufacturer/product;
- UWA Mask-1 thickness;
- UWA spin/bake/exposure/developer;
- exact UWA Br/HBr mesa etchant formulation;
- exact UWA Mask-1 strip chemistry;
- resist-selectivity data for Srivastav `2% Br2 / 3:1 EG:HBr`;
- exact Srivastav photoresist product/thickness;
- exact RP-01 mesa outer dimensions/mask bias.

These remain `UNRECOVERED`, not proven absent from theses/lab documentation.
