# Source ledger addendum — Round 27 — RIE reactor equivalence

**Date:** 2026-08-16 America/New_York

## Purpose

Record the primary evidence used to convert the RP-01 CH4/H2 RIE step from a controller-only recipe into a reactor-equivalence qualification.

---

## S27-01 — canonical RP-01 blocking-contact process

**Source:** E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, *Semiconductor Science and Technology* 16, 455–462 (2001). DOI `10.1088/0268-1242/16/6/306`.

**Evidence class:** `DIRECT-RP01`.

**Extracted process anchors:**

- Plasma Technology parallel-plate reactor;
- printed `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- RF power `50 W`;
- RF-on time `60 s`.

**Use:** canonical controller center.

**Not closed:** reactor model, RF frequency, electrode geometry, self-bias, sample temperature, base pressure, exact individual MFC flows, chamber state.

---

## S27-02 — UWA mesa structuring / same-lineage plasma response

**Source:** E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “Reactive ion etching for mesa structuring in HgCdTe,” *Journal of Vacuum Science & Technology A* 17, 2503–2509 (1999). DOI `10.1116/1.581988`.

**Evidence class:** `SAME-UWA-RIE`.

**Extracted:**

- `400 mTorr`;
- `CH4/5H2`;
- `0.4 W cm^-2`;
- p→n conversion in p-HgCdTe;
- n+ doping in n-HgCdTe;
- anisotropic mesa profile.

**Use:** proves same-lab plasma damage/conversion response and a separate pressure/power-density branch.

**Restriction:** do not combine its 0.4 W/cm² with RP-01 50 W to infer historical electrode area.

---

## S27-03 — direct physical-depth vs electrical-depth separation

**Source:** J. F. Siliquini, J. M. Dell, C. A. Musca, L. Faraone, *Applied Physics Letters* 70, 3443–3445 (1997). DOI `10.1063/1.119159`.

**Evidence class:** `SAME-UWA-RIE`.

**Extracted:**

- vacancy-doped p-type x≈0.31 HgCdTe;
- `410 mTorr`;
- `CH4/H2`;
- `0.4 W cm^-2`;
- physical etch depth ~`0.2 µm`;
- electrical n-type conversion extending ~`1.5 µm`.

**Use:** permanent proof that `d_etch != d_conv`.

---

## S27-04 — arsenic-doped x≈0.29 conversion branch

**Source:** J. F. Siliquini et al., *Applied Physics Letters* 72 (1998). DOI `10.1063/1.120642`.

**Evidence class:** `SAME-UWA-RIE`.

**Extracted:**

- extrinsic As-doped p-type x≈0.29 HgCdTe after Hg anneal;
- `340 mTorr`;
- `CH4/H2`;
- `0.4 W cm^-2`;
- LBIC/model-based effective converted doping analysis from 80–300 K.

**Use:** reinforces dependence on starting material/defect state and validates LBIC as conversion metrology.

---

## S27-05 — UWA 90-W conversion / Hg-anneal recovery branch

**Source:** E. P. G. Smith et al., *Journal of Applied Physics* 83, 5555–5557 (1998). DOI `10.1063/1.367389`.

**Evidence class:** `SAME-UWA-RIE`.

**Extracted:**

- x≈0.31 extrinsically doped p-HgCdTe;
- RIE `400 mTorr`, `CH4/H2`, `90 W`;
- p→n conversion;
- subsequent sealed-tube Hg anneal `200 °C / 17 h` removed the converted region in that experiment.

**Use:** another distinct UWA power convention and proof that plasma-induced state interacts with subsequent thermal/Hg history.

---

## S27-06 — Semu et al. self-bias / temperature / gas-ratio evidence

**Source:** A. Semu, L. Montelius, P. Leech, D. Jamieson, P. Silverberg, “Novel CH4/H2 metalorganic reactive ion etching of Hg1-xCdxTe,” *Applied Physics Letters* 59, 1752–1754 (1991). DOI `10.1063/1.106418`.

**Evidence class:** `PRIMARY-HGCDTE-RIE-TRANSFER`.

**Extracted:**

General parametric condition:

- total flow `85 sccm`;
- pressure `20 mTorr`;
- temperature `35 °C`;
- RF power `150 W`;
- dc bias `-360` to `-440 V`.

Explicit example:

- CH4 `15 sccm`;
- H2 `70 sccm`;
- pressure `20 mTorr`;
- RF `150 W`;
- dc bias `-390 V`;
- temperature `35 °C`.

Additional direct observations:

- etch rate depends on CH4:H2 ratio;
- laser interferometry used for in-situ rate/endpoint;
- sidewalls/surfaces were rough under the high RF-induced dc-bias condition;
- authors explicitly linked roughness to high dc bias.

**Use:** establishes self-bias and sample temperature as first-class reactor-transfer variables.

**Restriction:** different reactor/material/growth branch; no numerical self-bias target transferred to RP-01.

---

## S27-07 — Elkind & Orloff chemistry/orientation response

**Source:** J. L. Elkind, G. J. Orloff, “Reactive ion etching of HgCdTe with methane and hydrogen,” *Journal of Vacuum Science & Technology A* 10, 1106–1112 (1992). DOI `10.1116/1.578210`.

**Evidence class:** `PRIMARY-HGCDTE-RIE-TRANSFER`.

**Extracted from primary abstract/record:**

- H2-only RIE gave Cd-rich residue and rough surface;
- methane addition around the studied ~25% level produced smoother surfaces/deeper vias;
- strong crystallographic orientation dependence;
- short-time etch-rate ordering `(111)B > (100) > (111)A`;
- `(111)A` surface smoother than `(111)B` or `(100)` under the compared conditions.

**Use:** crystallographic orientation/polarity must remain in RIE genealogy; gas ratio materially changes chemistry/residue.

---

## S27-08 — same-era Plasma Technology RIE80 hardware-family evidence

**Source:** primary 2001 *Microelectronic Engineering* study, “Effects of pressure and capping layer thickness on sub-micron T-gate recess etching of GaAs p-HEMTs by SiCl4/SiF4/O2 reactive ion etch.”

**Evidence class:** `PRIMARY-PLASMA-TECH-FAMILY`.

**Extracted:**

- Plasma Technology RIE80;
- lower electrode driven at `13.56 MHz`;
- chamber base pressure below `0.5 mTorr`;
- platform temperature controlled; `40 °C` used in that experiment.

**Use:** demonstrates concrete same-manufacturer parallel-plate architecture fields relevant to a historical-equipment reconstruction.

**Critical restriction:** does not prove RP-01 used RIE80, 13.56 MHz, <0.5 mTorr base pressure, or 40 °C.

---

## S27-09 — White 2005 UWA thesis

**Source:** John Kenion White, “Mid-wave infrared HgCdTe photodiode technology based on plasma induced p-to-n type conversion,” PhD thesis, UWA (2005).

**Evidence class:** `PRIMARY-UWA-THESIS-IDENTIFIED / FULL-TEXT-NOT-RECOVERED`.

**Recovered:** repository record and downloadable-file identity.

**Access issue:** UWA current repository PDF route returned HTTP 403 through the available retrieval path.

**Use:** high-priority future source recovery because it is likely to contain practical reactor and processing details.

**Do not infer inaccessible details.**

---

# Round 27 source conclusions

1. The direct RP-01 controller center remains intact.
2. No primary evidence recovered the exact RP-01 reactor model, RF frequency, electrode geometry, self-bias or sample temperature.
3. Primary HgCdTe data directly demonstrate that gas ratio, dc self-bias, temperature, crystallographic orientation and starting material state affect RIE outcomes.
4. Same-manufacturer hardware evidence makes 13.56-MHz lower-electrode RIE80 architecture plausible as a comparison branch only.
5. Reactor equivalence must therefore be released from measured plasma/thermal/material outcomes, not from watts/pressure/flow/time alone.
