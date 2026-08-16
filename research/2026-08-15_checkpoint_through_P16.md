# Research checkpoint — through P16

**Timestamp:** 2026-08-15 America/New_York  
**Purpose:** exact takeover point after completing P13 temporal response, P14 lithography/geometry, P15 packaging, and P16 master integration.

## Current project status

The first canonical reference process remains RP-01: the Smith–Winchester–Musca–Dell–Faraone 2001 n-type MWIR HgCdTe photoconductor process.

The project now contains controlled procedure/qualification modules for the entire path from substrate through final detector performance:

- P01 wet mesa
- P02 anodic oxide
- P03 x≈0.30 Te-rich LPE
- P04 Hg anneal
- P05 Hall/VdP
- P06 FTIR composition/thickness
- P07 CdZnTe substrate
- P08 RIE blocking contact
- P09 Cr/Au + TLM
- P10 device DC bias/self-heating
- P11 absolute spectral responsivity/radiometry
- P12 noise/NEP/D*
- P13 temporal response/lifetime/bandwidth
- P14 lithography/mask geometry/CD
- P15 cryogenic package/interconnect
- P16 master end-to-end traveler

No end-to-end `REPRODUCIBLE-RELEASE` exists. Several process variables remain literature-open or require local apparatus qualification.

## New P13 findings

Same-UWA transient-lifetime source identified:

D. A. Redfern, C. A. Musca, E. P. G. Smith, J. M. Dell, L. Faraone, “On the Transient Photoconductive Decay Technique for Lifetime Extraction in HgCdTe,” IEEE conference proceedings, published 1999, pp. 275–278.

This is especially valuable because it overlaps the RP-01 team.

P13 rules:

- de-embed source/modulator + readout before detector bandwidth extraction;
- require amplitude and phase agreement before accepting a one-pole tau;
- call the result `tau_eff` unless a physical model justifies bulk lifetime;
- verify low-injection linearity;
- track fit window in transient decay;
- measure versus field to expose sweepout/contact/heating effects;
- test whether the canonical 1-kHz condition is actually on the low-frequency plateau.

Kruse 1965 <=100-ns 77-K HgCdTe PC response is only a broad historical benchmark, not an RP-01 value.

## New P14 findings

Direct RP-01 geometry:

- nine contacts;
- each 300×300 µm;
- eight adjacent gaps 50,100,...,400 µm;
- same structure used for TLM and PC performance evaluation.

Derived sequential contact-string extent if arranged linearly = 4.5 mm.

The paper explicitly states that Figures 6 and 7 use the **same device** as Figures 3 and 5. Thus 4-µm responsivity vs field, noise spectrum, spectral responsivity and spectral D* are one historical device. Missing identifier = which contact pair/gap.

P14 dimensional chain:

`CD_mask → CD_resist → CD_mesa → CD_RIE_open → CD_n+ → CD_metal → actual gap/area`.

General chlorobenzene lift-off sources:

- Hatzakis–Canavello–Shaw 1980, DOI `10.1147/rd.244.0452`;
- Collins–Halsted 1982.

They establish lift-off profile mechanism/control, not RP-01 resist identity.

Tempting 50-µm historical-gap inference remains **OPEN**. A 300×50-µm active area plus Rλ~4×10^5 V/W and e_n=24.5 nV/√Hz yields D*~2×10^11, but exact graph value/noise convention/active width are insufficiently closed.

## New P15 findings

RP-01 does not disclose mechanical package construction.

Do not invent:

- singulation;
- die attach;
- cold finger;
- wire material/diameter/bond method;
- window/aperture/shield;
- vacuum/bake.

P15 qualifies package by pre/post device state, mechanical stability and optical definition.

Useful external mechanical framework:

- current MIL-STD-883 Part 2 mechanical tests;
- Method 2011 bond pull;
- Method 2019 die shear.

Do not choose numerical limits until construction/wire/die attach are known.

UWA vacuum-baking work on HgCdTe photodiodes is used only to enforce the principle that packaging thermal history can modify HgCdTe device state; no numerical bake recipe is transferred.

## New P16 integration structure

Master genealogy:

`SOURCE LOT → LPE CHARGE → GROWTH RUN → WAFER → COUPON/DIE → DEVICE → CONTACT PAIR → DATASET`.

Main phases:

A. facility/material/substrate readiness  
B. charge + LPE  
C. as-grown P05/P06 state  
D. Hg anneal + repeat P05/P06  
E. Mask1/P01/P02/Mask2/P08/P09/P14/TLM  
F. bare-die P10 and optional optical/noise/dynamic baseline  
G. P15 package/interconnect  
H. final P11/P12/P13 characterization

Key elapsed-time clocks explicitly added:

- substrate final clean → LPE load;
- growth → first metrology;
- anneal → metrology;
- mesa etch → passivation;
- anodization → Mask2;
- Mask2 development → RIE;
- RIE → Cr deposition;
- Au → lift-off;
- lift-off → first electrical test;
- singulation clean → die attach;
- die attach → wire bond;
- package pump/bake → first cold test.

Rework must remain visible in genealogy. Repeat anneal, etch, passivation, plasma, metal, bake and wire-bond operations are not assumed benign.

## Current highest-impact blockers

### Upstream

- exact final CdZnTe face/miscut and surface preparation;
- final boat/growth-well geometry and total charge mass;
- x≈0.30 source synthesis/homogenization;
- exact equilibration/supercooling/cooling/growth-time calibration;
- wipe-off slider speed/contact mechanics;
- Hg anneal time/pHg/cooldown needed for final target Hall state.

### Frontside

- exact basis of “2% Br2” and final post-etch rinse;
- exact UWA anodization recipe or completed local transfer;
- Mask1/Mask2 resist identity, spin, dose, developer;
- exact individual CH4/H2 flows represented by `CH4/5H2`;
- exact source conditions for ~8-µm electrical conversion depth;
- metal deposition base pressure/rates/substrate T;
- RIE-to-metal allowable delay;
- lift-off solvent/time/agitation.

### Device/package/measurement

- historical typical-device contact pair/gap;
- historical package details;
- historical low-noise preamp/gain and analyzer RBW/ENBW;
- exact noise convention used for historical Figure-7 D*;
- statistical release/yield limits once actual devices exist.

## Files created/updated in this work block

- `procedures/P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md`
- `research/2026-08-15_p13_temporal_response.md`
- `research/2026-08-15_checkpoint_through_P13.md`
- `docs/SOURCE_LEDGER_ADDENDUM_P13_P14.md`
- `procedures/P14_LITHOGRAPHY_MASK_GEOMETRY_CD_QUALIFICATION.md`
- `research/2026-08-15_p14_lithography_geometry.md`
- `procedures/P15_DIE_ATTACH_INTERCONNECT_CRYOGENIC_PACKAGE_QUALIFICATION.md`
- `research/2026-08-15_p15_packaging.md`
- `procedures/P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`
- refreshed `AGENTS.md` through P16.

## Recommended next action

Create a practical blank traveler under `travelers/` from P16, then resume targeted primary-source recovery rather than adding another device architecture.

Priority source recovery order:

1. exact `CH4/5H2` gas split / RIE reactor details;
2. exact Mask1/Mask2 resist/exposure/developer lineage;
3. full Schmit–Hager–Wood x≈0.30 LPE experimental section;
4. exact final substrate preparation;
5. exact UWA native anodization recipe;
6. metal deposition/lift-off conditions;
7. historical typical-device geometry / package / preamp.

Keep updating the repo after each meaningful result; do not leave new conclusions only in chat.
