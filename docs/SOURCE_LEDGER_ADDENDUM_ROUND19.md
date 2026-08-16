# Source ledger addendum — Round 19 empirical Cr/Au metallization and lift-off recovery

**Date:** 2026-08-16 America/New_York  
**Scope:** P09/P09A/P14A/P26 Cr/Au deposition, pre-metal interface state, lift-off, TLM and stability.

This addendum records recovered empirical evidence and restrictions. It does not convert transfer-family metallization conditions into the historical RP-01 traveler.

---

## R19-S1 — canonical RP-01 two-mask detector paper

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16 (2001) 455–462. DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01` plus one `DIRECT-RP01-PROPOSED-ARCHITECTURE` item.

Direct metallization/process facts:

- Mask-2 photoresist approximately `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene soak `30 min`;
- pattern/develop/water rinse;
- same mask survives RIE and is suitable for lift-off of `Cr 300 Å / Au 2700 Å`;
- Cr target `30 nm`;
- Au target `270 nm`;
- nine `300×300-µm` contacts with 50-µm-increment spacing;
- 80-K TLM result `rho_c≈9×10^-4 Ω·cm²`;
- RIE/passivation/metal are self-aligned in the two-mask process.

The paper explicitly says the vacuum-processing capability created by connecting the RIE chamber via a load lock to a metal-deposition system is advantageous.

**Classification of load-lock statement:** `DIRECT-RP01-PROPOSED-ARCHITECTURE`. It is a stated design/process advantage, not proof that every experimental device was transferred in vacuum.

Still absent from the paper:

- metal-deposition method;
- tool model;
- base/process pressure;
- Cr rate;
- Au rate;
- sample temperature during deposition;
- source purity/hardware;
- actual RIE-to-Cr delay;
- lift-off solvent/time/agitation/rinse/dry.

---

## R19-S2 — same-UWA in-situ vacuum processing conference paper

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors,” Proc. 2000 International Semiconducting and Insulating Materials Conference (SIMC-XI), pp. 318–321, IEEE document `939185`.

**Class:** `SAME-UWA-BIBLIOGRAPHIC / PARTIAL-ACCESS`.

Recovered:

- exact title/authors/year/page range/document identity;
- same RP-01 team and explicit in-situ-vacuum-processing focus.

Current public retrieval still did not expose a sufficiently complete experimental section to close:

- deposition tool;
- load-lock vacuum levels;
- transfer time;
- metal rates.

**Action:** retain as high-priority source-recovery target.

---

## R19-S3 — same-UWA 1998 HgCdTe detector thermal-evaporation method

Same-UWA HgCdTe heterostructure detector papers:

- J. Piotrowski et al./C. Musca et al., *Semiconductor Science and Technology* 13 (1998) 1209–1214, DOI `10.1088/0268-1242/13/10/025`;
- C. Musca et al., *Journal of Electronic Materials* 27 (1998) 740–746, DOI `10.1007/s11664-998-0046-y`.

**Class:** `SAME-UWA-METHOD`.

Directly recovered:

- fabricated HgCdTe detector structures used **angled thermal evaporation for contact metal deposition**.

**Use:** establishes thermal evaporation as a real same-laboratory HgCdTe contact-deposition method in the immediate RP-01 era.

**Restriction:** different photovoltaic/heterostructure device family; no direct proof that RP-01 Cr/Au used the same tool/method/rates.

---

## R19-S4 — modern UWA Cr/Au thermal evaporation on HgCdTe

S. Ma et al., “Damage-free lift-off of epitaxial HgCdTe thin films for future curved infrared imaging array applications,” *Infrared Physics & Technology* 151 (2025) 106073. DOI `10.1016/j.infrared.2025.106073`.

**Class:** `SAME-UWA-METHOD / MODERN`.

Direct practical details:

- HgCdTe photoconductor;
- Cr/Au `10/200 nm`;
- deposited by **thermal evaporation**;
- shadow-mask patterning;
- photodetection area approximately `180×1260 µm²`;
- dark I–V tested from `-2 to +2 V` using Keithley 4200A-SCS;
- device performance evaluated at 77 K.

**Use:** modern same-UWA confirmation that Cr/Au thermal evaporation is a workable HgCdTe photoconductor metallization method.

**Restriction:** different HgCdTe material, no anodic passivation, different stack/geometry; no RP-01 historical-rate inference.

---

## R19-S5 — modern UWA Cr/Au thermal evaporation / 77–300 K I–V

W. Pan et al., “Van der Waals Epitaxy of HgCdTe Thin Films for Flexible Infrared Optoelectronics,” *Advanced Materials Interfaces* (2023), DOI `10.1002/admi.202201932`.

**Class:** `SAME-UWA-METHOD / MODERN`.

Directly recovered:

- Cr/Au `10/200 nm` deposited by thermal evaporation on HgCdTe;
- ohmic nature supported by linear, symmetric dark I–V;
- measurements over approximately `77–300 K` and `-1 to +1 V`.

**Use:** additional method/functional evidence for local thermal-evaporation transfer.

**Restriction:** different MBE/mica/CdTe-capped material architecture and Cr/Au thicknesses.

---

## R19-S6 — LPE p-HgCdTe Au thermal-evaporation rate study

V. S. Meena et al., “Structural, compositional, morphological and electrical characteristics of thermally evaporated Au Ohmic Contact on p-type HgCdTe substrate for possible infrared detectors,” *Optical Materials* 141 (2023) 113943. DOI `10.1016/j.optmat.2023.113943`.

**Class:** `PRIMARY-X029-AU-TRANSFER`.

Recovered practical information:

- p-HgCdTe LPE on CdZnTe(111), x≈0.29;
- Au deposited by thermal evaporation;
- explicit Au rate conditions `3 Å/s` and `10 Å/s`;
- TLM as-deposited `rho_c = 2.73×10^-3 Ω·cm²`;
- `80 °C / 2 h` anneal in air reduced `rho_c` to `7.11×10^-4 Ω·cm²` in this contact branch;
- optimized Au RMS roughness `4.19 ± 0.02 nm`.

**Use:** gives a real HgCdTe thermal-Au rate scale and direct evidence that post-metal thermal history can substantially change contact resistance.

**Restrictions:** p-type, single-Au contact, different interface physics and likely different film thickness; none of these rates/anneal values is an RP-01 setting.

---

## R19-S7 — x≈0.30 p-HgCdTe buried-interface study

A. Colas Reuillon et al., “Electrical and Physicochemical Study of the Metal/p-HgCdTe Interface for MCT-Based Infrared Detectors,” *Journal of Electronic Materials* 55 (2026) 6638–6646. DOI `10.1007/s11664-026-12909-8`.

**Class:** `PRIMARY-X030-INTERFACE-TRANSFER`.

Recovered direct details:

- 9-µm Hg0.7Cd0.3Te LPE on CdZnTe;
- prepared p-type surface region for the study;
- standard wet etch before metal deposition;
- 10-nm metal layer by sputtering for physicochemical characterization;
- 120-nm metal for TLM samples using lift-off;
- HAXPES/ToF-SIMS interface study;
- one surface state intentionally included **~10 min air exposure after deoxidation** to represent just-before-metallization condition;
- model-estimated Te-oxide thickness roughly 0.9 nm as-prepared, 0.3 nm after deoxidation/pre-metal, and apparent ~1.6 nm after metallization under homogeneous-interface assumptions;
- post-metal oxide quantification/origin explicitly remains uncertain;
- F/O/C/N and oxygen-related interface contaminants observed by ToF-SIMS.

**Use:** direct evidence that clean-to-metal timing/surface oxide/contamination are physical contact-process variables on x≈0.30 HgCdTe.

**Restriction:** p-type/high-doping/sputtered contact branch; oxide numbers are not RP-01 limits.

---

## R19-S8 — n-HgCdTe Ti/Pt/Au contact process

V. Srivastav, R. Pal, B. L. Sharma, V. Mittal, V. Gopal, H. P. Vyas, “Electrical properties of titanium-HgCdTe contacts,” *Journal of Electronic Materials* 34 (2005) 225–231. DOI `10.1007/s11664-005-0208-0`.

**Class:** `PRIMARY-HGCDTE-CONTACT-TRANSFER`.

Direct practical details:

- n-type bulk HgCdTe, x≈0.20;
- material thinned to ~10 µm for test structures;
- 300-Å anodic oxide; CdTe 500 Å thermally evaporated; ZnS 2500 Å in interpad region by thermal evaporation/lift-off;
- before contact metal: `500 eV` Ar ion mill creating n+ surface;
- fresh `0.05% Br2 + HBr` treatment for `2 s`;
- Ti/Pt/Au `300/300/4500 Å` by DC sputtering;
- contacts defined by lift-off;
- low substrate-temperature deposition used to limit Hg out-diffusion;
- specific contact resistance order `10^-4 Ω·cm²` in the qualified measurement architecture;
- cryogenic TLM was sensitive to optical background and required cold-shield consideration;
- long-duration `60 °C / 15 day` air heat treatment changed cryogenic contact properties.

**Use:** demonstrates the importance of explicit surface reset, substrate thermal budget, optical-background control during TLM and aging.

**Restriction:** do not transplant the 500-eV mill, 0.05% Br2/HBr or Ti/Pt/Au stack into RP-01. P08 intentionally creates the RP-01 n+ contact state already.

---

## R19-S9 — 2026 thermal versus e-beam Au on p-HgCdTe

S. K. Gaur et al., “Experimental study of the nanoscale gold Ohmic Contact's for prospective infrared detectors on a p-type HgCdTe,” *Optics Communications* 604 (2026) 132846. DOI `10.1016/j.optcom.2025.132846`.

**Class:** `PRIMARY-AU-METHOD-RATE-TRANSFER`.

Recovered:

- p-HgCdTe LPE near x≈0.30;
- thermal- and e-beam-evaporated Au compared;
- rate conditions `6 Å/s` and `12 Å/s` for both methods;
- e-beam films showed different microstructural/roughness behavior and somewhat lower TLM contact resistivity in the studied p-type branch;
- reported optimized TLM rho_c approximately `7.3×10^-3 Ω·cm²` for e-beam versus `1.1×10^-2 Ω·cm²` for thermal Au.

**Use:** reinforces method/rate dependence and supplies an additional real Au rate scale.

**Restriction:** p-type Au-only branch, much higher rho_c than RP-01 n+/n Cr/Au; not a recipe candidate by numerical matching.

---

## R19-S10 — Cr/p-Hg0.72Cd0.28Te contact study

F. Sizov et al., “Electrical characterization of Cr/p-Hg1−xCdxTe (x=0.28,1.0) contacts using LTLM: contact resistance and current transport mechanism,” *Applied Physics A* 131 (2025) 722; preprint lineage arXiv:2411.01003.

**Class:** `PRIMARY-CR-INTERFACE-TRANSFER`.

Recovered direct/author-preprint information:

- Cr film deposited at room temperature under vacuum on p-Hg0.72Cd0.28Te;
- LTLM measured at 77 and 300 K;
- Cr/p-HgCdTe `rho_c` approximately `0.15 Ω·cm²` at 77 K and `0.029 Ω·cm²` at 300 K;
- authors discuss Cr oxide and element diffusion as possible contributors to the relatively high contact resistance.

**Use:** failure/interface-chemistry evidence for direct Cr/HgCdTe contact.

**Restriction:** p-type, no RIE n+ region, much larger rho_c than canonical RP-01; not a numerical transfer target.

---

# Negative search / still-open evidence

Round-19 searching still did **not** recover the following direct RP-01 values:

1. deposition method used on the canonical measured devices;
2. metal deposition tool/model;
3. base pressure;
4. Cr deposition rate;
5. Au deposition rate;
6. source purity/boat/crucible;
7. sample temperature during Cr/Au;
8. actual RIE-to-Cr air/vacuum delay;
9. exact lift-off solvent;
10. lift-off time/temperature/agitation;
11. post-lift-off rinse/dry;
12. explicit statement of whether canonical Cr and Au were deposited without vacuum break.

The same-UWA 2000 in-situ-vacuum paper and older dissertations/proceedings remain likely source-recovery targets.

This negative result means **not recovered**, not absent.

---

# Round-19 source consequence

P26 can now be substantially more empirical than P09/P09A alone:

- the historical Cr/Au thickness/TLM outcome and Mask-2 process are direct;
- thermal evaporation is a real same-UWA HgCdTe contact method both near the RP-01 era and in modern UWA work;
- published HgCdTe Au deposition rates give a practical 3–12 Å/s empirical scale for screening, without closing RP-01;
- x≈0.30 interface measurements demonstrate oxidation/contamination evolution over practical pre-metal timing;
- direct HgCdTe contact papers show that deliberate ion milling/wet surface reset, substrate heating and background illumination can materially change or complicate contact behavior;
- post-metal heat treatment can change rho_c and therefore must be a recorded variable.

The remaining problem is no longer lack of a practical local qualification route. It is exact historical identity plus local statistical capability.
