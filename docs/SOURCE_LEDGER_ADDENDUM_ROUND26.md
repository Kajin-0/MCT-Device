# Source ledger addendum — Round 26

**Date:** 2026-08-16 America/New_York  
**Scope:** P05 audit + empirical HgCdTe cryogenic die attach / interconnect / package execution.

---

## R26-S01 — RP-01 canonical detector process

E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

**Use this round:** establishes detector operation near 80 K but does not close singulation, die attach, wire/interconnect, cold finger, Dewar/window, vacuum or thermal-cycle construction.

**Do not infer:** package identity from operating temperature alone.

---

## R26-S02 — Honeywell cryogenic HgCdTe attachment patent

T. T. S. Wong, Honeywell Inc., US4081819A, “Mercury cadmium telluride device,” filed 17 Jan 1977, published 28 Mar 1978.

Primary URL: `https://patents.google.com/patent/US4081819A/en`

**Class:** `PRIMARY-HONEYWELL-HGCDTE-PACKAGING`.

**Direct process/experiment anchors:**

- epitaxial HgCdTe devices on a first crystalline substrate;
- first substrate bonded to a second substrate/flat pack/Dewar structure;
- detector operation typically 77 K or below;
- prior glass adhesive caused cryogenic cracking;
- silicone rubber attachment solved cracking in reported experiments;
- named examples: Dow Corning 3110, 3112, 3116 RTV silicone rubbers;
- source thermal-conductivity threshold printed as approximately `5.0×10^-4` in the patent's units;
- controlled comparison:
  - glass adhesive / 60-µm abrasion / 40-g thermocompression -> cracked at 5 K;
  - silicone / ~50-µm abrasion / 40 g -> no crack;
  - silicone / 15-µm abrasion / 5 g -> no crack.

**Use:** proves attachment material/compliance/thermal transport can dominate cryogenic fracture in HgCdTe.

**Restrictions:**

- not RP-01 package identity;
- 5 g and 40 g are experimental thermocompression conditions, not released bond-force setpoints;
- do not reinterpret the source's unusual thermal-conductivity units without a dedicated reconstruction.

---

## R26-S03 — U.S. Navy direct HgCdTe photoconductor thermal-stack patent

US4012691A, “Determination of thermal impedances of bonding layers in infrared photoconductors,” filed 8 Apr 1976, published 15 Mar 1977.

Primary URL: `https://patents.google.com/patent/US4012691`

**Class:** `PRIMARY-HGCDTE-PC-THERMAL`.

**Direct construction:**

`HgCdTe crystal -> epoxy -> Irtran 2 or sapphire -> GE 7031 varnish -> copper heat sink`.

- heat sink held at 77 K for HgCdTe photoconductor measurement;
- conductors fused to detector electrodes;
- laser pulse or electrical pulse may heat the detector;
- resistance recovery is measured to reconstruct thermal behavior;
- epoxy and varnish are thermally resistive and vary between detectors;
- two recovery scales: several milliseconds and hundreds of milliseconds;
- source attributes the two scales to the two thermally resistive bonding layers.

**Use:** package thermal impedance is a measured detector-performance variable and can contaminate apparent temporal response/self-heating.

**Restriction:** exact epoxy identity not disclosed in the recovered patent text.

---

## R26-S04 — Bartoli et al. primary photoconductor thermal paper

F. J. Bartoli, L. Esterowitz, M. R. Kruer, R. E. Allen, “Thermal recovery processes in laser irradiated HgCdTe (PC) detectors,” *Applied Optics* 14, 2499–2507 (1975), DOI `10.1364/AO.14.002499`.

Primary publisher record: `https://opg.optica.org/ao/abstract.cfm?uri=ao-14-10-2499`

**Class:** `PRIMARY-HGCDTE-PC-THERMAL`.

**Direct findings available from publisher abstract/table record:**

- thermal recovery is highly sensitive to detector construction;
- initial recovery on several-ms scale;
- remainder on hundreds-ms scale;
- relative amplitudes and shapes depend on power density and irradiation time;
- two recovery times arise from two thermally resistive bonding layers;
- one-dimensional thermal model agrees with experiment over the studied pulse regime.

**Use:** independent primary-paper support for the P33 thermal-impulse qualification requirement.

---

## R26-S05 — thin-HgCdTe/epoxy thermal mismatch warning

US5462882A, “Masked radiant anneal diffusion method.”

Primary URL: `https://patents.google.com/patent/US5462882`

**Class:** `PRIMARY-HGCDTE-HYBRID-TRANSFER`.

**Direct relevant statements:**

- thin HgCdTe structures can develop dislocations, slip lines, microcracks and fractures when mounted to thermally mismatched materials;
- discussion explicitly includes thin HgCdTe about `5–10 µm` mounted by low-outgassing epoxy to silicon;
- high-temperature processing can harden/alter epoxy and increase cooldown stress;
- devices ultimately operate near 77 K.

**Use:** near-RP-01 thickness-scale warning that package cure/bake and carrier CTE are detector-process variables.

**Restriction:** FPA/high-temperature interdiffusion architecture, not RP-01 packaging.

---

## R26-S06 — HgCdTe/Si thermal-mechanical buffer

US5365088A, Santa Barbara Research Center, “Thermal/mechanical buffer for HgCdTe/Si direct hybridization.”

Primary URL: `https://patents.google.com/patent/US5365088A/en`

**Class:** `PRIMARY-HGCDTE-HYBRID-TRANSFER`.

**Direct relevant findings:**

- direct HgCdTe/Si hybrids suffer reliability problems from CTE mismatch under repeated ambient-to-~78-K cycling;
- failure can occur in HgCdTe and indium interconnects;
- sapphire is used as a thermal/mechanical buffer because its CTE is closer to HgCdTe while offering electrical isolation and useful thermal conduction.

**Use:** establishes carrier/substrate CTE and thermal-cycle history as package variables.

**Restriction:** FPA hybrid architecture, not a single RP-01 photoconductor package.

---

## R26-S07 — same-UWA array context

J. F. Siliquini, L. Faraone, “Two-Dimensional Infrared Focal Plane Arrays Based on HgCdTe Photoconductive Detectors,” *Semiconductor Science and Technology* 11, 1906–1911 (1996), DOI `10.1088/0268-1242/11/12/024`.

Institutional primary metadata: UWA Research Repository.

**Class:** `SAME-UWA-DEVICE-CONTEXT`.

**Direct accessible result:**

- n-type epitaxial HgCdTe photoconductor array with n+ blocking contacts;
- 3×3 format experimentally demonstrated;
- all elements reported BLIP at 80 K.

**Use:** confirms same-UWA photoconductor technology operates in a packaged/cryogenic array context.

**Restriction:** accessible repository record does not close package traveler details.

---

# P05 audit outcome

File audited: `procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md`.

P05 already includes:

- Hall-contact ohmicity verification;
- dark/thermal environment control;
- 80-K and 300-K measurement branches;
- current/self-heating screening;
- full van der Pauw reversal/reciprocity sequence;
- numerical 3%/5% VdP consistency gates;
- measured magnetic-field calibration/orientation;
- symmetric field sweeps;
- current + field reversal and orthogonal Hall configurations;
- antisymmetrization;
- one-carrier validity tests;
- multicarrier escalation;
- Hall-factor reporting discipline;
- uncertainty and repeatability;
- structured raw-data record.

**Round-26 decision:** no new Hall module was created. A P33 Hall document would have duplicated controlled content. Remaining P05 gaps are primarily historical Hall-contact identity, final production acceptance limits and process-specific Hall-factor closure.

---

# Negative / unresolved searches retained

Not recovered this round:

- exact RP-01 singulation/package/adhesive/interconnect/Dewar traveler;
- exact package details from the full Siliquini–Faraone 1996 article through accessible institutional text;
- exact epoxy identity in US4012691A/Bartoli thermal stack;
- exact RP-01 wire/ribbon metallurgy and bond setpoints;
- exact RP-01 cold-shield/window geometry;
- exact RP-01 vacuum/bake history.

“Not recovered” does not mean absent.
