# Source ledger addendum — Round 22 empirical CdZnTe substrate / final-surface recovery

**Date:** 2026-08-16 America/New_York  
**Scope:** P07/P07A/P07B/P07C/P29 substrate composition, orientation/polarity/miscut, crystal quality, impurity genealogy and final pre-LPE surface.

This round prioritizes primary LPE and substrate literature. Transfer-family values are not upgraded into the historical RP-01 substrate specification.

---

## R22-S1 — canonical RP-01 detector paper

E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16 (2001) 455–462, DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

Directly supports:

- LPE-grown n-HgCdTe;
- electrically insulating CdZnTe substrate;
- nominal HgCdTe x≈0.30;
- active-layer thickness 9.5 µm.

Does not expose exact substrate Zn fraction, face/polarity, miscut, substrate dimensions, supplier, impurity specification, polish or final clean.

---

## R22-S2 — Cd0.96Zn0.04Te crystalline-quality comparison for x≈0.30 LPE

Primary *Journal of Crystal Growth* study (1994), “Study of crystalline quality of CdTe, CdZnTe and CdMnTe substrates used for liquid phase epitaxy of Cd0.7Hg0.3Te.”

**Class:** `PRIMARY-LPE-X030 / PRIMARY-SUBSTRATE-QUALITY`.

Recovered direct result:

- Cd0.96Zn0.04Te was included specifically as an HgCdTe LPE substrate;
- representative best substrate material had etch-pit density approximately `5×10^4 cm^-2`;
- X-ray rocking-curve linewidth approximately `25 arcsec`;
- Cd0.7Hg0.3Te layers grown on Cd0.96Zn0.04Te had better crystalline quality than comparable layers on CdTe in that study.

**Use:** strong empirical support for ~4 mol% Zn as a transfer composition and for XRD/EPD as incoming substrate metrics.

**Restriction:** not an RP-01 Zn or XRD/EPD acceptance specification.

---

## R22-S3 — Kubiak et al. detector-oriented Te-rich LPE substrate preparation

L. Kubiak et al., “Status of HgCdTe photodiodes at the Military University of Technology,” *Opto-Electronics Review* 11(3) (2003) 211–226.

**Class:** `PRIMARY-LPE-TRANSFER`.

Recovered practical process details:

- `(111)B` CdZnTe;
- `4% Zn`;
- substrate dimensions `10×10×1 mm^3`;
- chemically and mechanically polished;
- final etch with `(2–3)% bromine-methanol`;
- exposure for `a few seconds`;
- substrate then loaded into the graphite boat;
- Te-rich LPE used for HgCdTe base layers x≈0.20–0.22.

The same source also states that the graphite boat was acid-cleaned and analytical examination found no Fe, Cu, Ni or Na in the machined graphite, reinforcing contamination control in the growth chain.

**Use:** strongest current operator-level final-surface transfer branch for detector LPE.

**Restrictions:** different HgCdTe composition/device architecture; currently recovered text does not define Br2 percentage basis, exact seconds, rinse/dry or clean-to-load time.

---

## R22-S4 — Gawron/Rogalski LPE epi-ready substrate branch

J. Gawron and A. Rogalski, “HgCdTe buried multi-junction photodiodes fabricated by the liquid phase epitaxy,” *Infrared Physics & Technology* 43 (2002) 157–163, DOI `10.1016/S1350-4495(02)00135-4`.

**Class:** `PRIMARY-LPE-TRANSFER`.

Recovered:

- Cd0.96Zn0.04Te substrate family;
- `(111)B` orientation;
- epi-ready polished substrate surfaces;
- direct use for HgCdTe LPE detector structures.

**Use:** independent detector-LPE support for the 4%-Zn/(111)B transfer center.

**Restriction:** “epi-ready” does not reveal the vendor polish/final-clean traveler and is not itself a reproducible surface specification.

---

## R22-S5 — Huo et al. A/B polarity comparison in slider LPE

Q. Huo et al., “Effect of polarity of CdZnTe substrate on slider liquid phase epitaxy of HgCdTe,” *Journal of Infrared and Millimeter Waves* 42(1) (2023) 1–7, DOI `10.11972/j.issn.1001-9014.2023.01.001`.

**Class:** `PRIMARY-POLARITY-TRANSFER`.

Direct experimental results:

- slider LPE on `(111)A` and conventional `(111)B` CdZnTe;
- HgCdTe composition and thickness on A were comparable to B in the investigated process;
- melt/film contact angle `(111)A = 50±2°`;
- melt/film contact angle `(111)B = 30±2°`;
- HgCdTe grown on `(111)A` had XRD FWHM `33.1 arcsec`;
- A-face growth substantially reduced residual melt droplets without reported reduction in crystal quality.

**Use:** direct proof that polarity is a wetting/morphology process variable in slider LPE.

**Restriction:** does not identify historical RP-01 polarity or establish universal A-face superiority.

---

## R22-S6 — vicinal-plane LPE experiment

“Growth of Hg1−xCdxTe liquid phase epitaxial films on vicinal planes,” *Journal of Crystal Growth* 169 (1996) 480–484, DOI `10.1016/S0022-0248(96)00418-6`.

**Class:** `PRIMARY-MISCUT-TRANSFER`.

Direct result:

- dipping LPE on substrates with several misoriented facets;
- epilayers near `1.2° off (111)` had better crystal quality and fewer Te precipitates than other tilted substrates in that experiment.

**Use:** establishes low-degree miscut as a real LPE factor.

**Restriction:** dipping process and substrate implementation differ from RP-01 slider/horizontal process; `1.2°` is not a setpoint for P29.

---

## R22-S7 — Tower et al. substrate impurity study

Tower et al., “CdZnTe Substrate Impurities and Their Effects on Liquid Phase Epitaxy HgCdTe,” *Journal of Electronic Materials* (1995).

**Class:** `PRIMARY-SUBSTRATE-IMPURITY`.

Recovered conclusion:

- impurities in CdZnTe/CdTe substrates can influence LPE HgCdTe;
- Cu contamination specifically degraded electrical/device properties of lightly doped LPE material;
- anomalous carrier-type behavior correlated with certain substrate ingots.

**Use:** makes substrate lot/impurity genealogy a mandatory process record, with Cu a high-priority analyte.

**Restriction:** no universally transferable RP-01 Cu concentration limit was recovered.

---

## R22-S8 — explicit CdZnTe preparation in a primary MBE branch

Primary *Journal of Crystal Growth* study on HgCdTe MBE using Cd0.96Zn0.04Te `(211)B` substrates.

**Class:** `PRIMARY-SURFACE-METHOD-TRANSFER / MBE`.

Direct details:

- nominally undoped p-Cd0.96Zn0.04Te `(211)B`;
- substrate resistivity approximately `10^5 Ω·cm`;
- sequential degrease in trichloroethylene, acetone and methanol at `60 °C for 15 min`;
- `0.5% Br2/methanol` etch for `60 s`;
- methanol rinse.

**Use:** demonstrates the level of explicit surface-history control appropriate to CdZnTe epitaxy and provides a semi-insulating resistivity scale.

**Restriction:** MBE, `(211)B`, different x/device branch. Do not import this recipe into P03 LPE.

---

## R22-S9 — modern CdZnTe/HgCdTe LPE overview with x≈0.30

Primary *Journal of Crystal Growth* 2020 article, “HgCdTe/CdZnTe LPE epitaxial layers: From material growth to applications in devices,” DOI `10.1016/j.jcrysgro.2019.125295`.

**Class:** `PRIMARY-LPE-X030-BROAD`.

Recovered scope:

- LPE HgCdTe/CdZnTe epiwafers include x≈0.21 and x≈0.30;
- CdZnTe y≈0.04 is part of the mature device-oriented LPE substrate family.

**Use:** supports continued relevance of approximately 4% Zn in x≈0.30 LPE.

**Restriction:** broad process article; no RP-01 historical identity inferred.

---

## R22-S10 — same-UWA modern substrate family, MBE only

Modern UWA HgCdTe work uses Cd0.96Zn0.04Te B-oriented substrates, including `(211)B` MBE structures.

**Class:** `SAME-UWA-TRANSFER / MBE`.

**Use:** same-laboratory-family confirmation that high-quality 4%-Zn CdZnTe remains a relevant substrate platform.

**Restriction:** MBE `(211)B` must not be transplanted into the RP-01 LPE face specification.

---

# Miscut-source audit / conflict handling

Older secondary summaries report differing preferred miscut values, ranging from near-nominal `(111)` to low-degree offcuts. Because those precise statements were not recovered directly from the cited original process papers in this round, they are not used as P29 numerical anchors.

The only direct numerical miscut result promoted in Round 22 is the `~1.2° off (111)` result from the 1996 primary vicinal dipping-LPE paper, and it remains transfer-only.

Historical RP-01 miscut magnitude and azimuth remain `OPEN`.

---

# Negative search / still unrecovered

Round 22 did not recover direct RP-01 values for:

1. CdZnTe Zn fraction;
2. substrate plane/polarity;
3. miscut magnitude/azimuth;
4. supplier/ingot;
5. substrate dimensions/thickness;
6. resistivity;
7. XRD/EPD/inclusion acceptance limits;
8. trace-impurity limits;
9. mechanical polish traveler;
10. final substrate chemistry;
11. final Br2 concentration basis;
12. exact final-etch duration;
13. rinse/dry;
14. final removed depth;
15. clean-to-load limit;
16. whether an in-situ substrate meltback erased or modified the ex-situ final surface.

This means **not recovered**, not absent.

---

# Round-22 consequence

The substrate branch can now be treated empirically without guessing a historical face:

`lot/ingot -> measured y/lattice state -> verified plane/polarity/miscut -> XRD/EPD/inclusions/impurities -> mechanical genealogy -> mathematically defined final surface recipe -> removed depth/roughness/chemistry -> clean-to-load clock -> P03 wetting/wipe-off -> epilayer XRD/x/d/transport -> device correlation`.

The strongest first-transfer center is a high-quality Cd0.96Zn0.04Te `{111}` substrate family, with `(111)B` strongly represented historically, while A/B polarity should remain a controlled qualification coordinate because direct slider-LPE data show significant wetting/residual-melt differences.
