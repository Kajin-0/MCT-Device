# Research checkpoint — after empirical cryogenic packaging Round 26

**Date:** 2026-08-16 America/New_York

## Completed this round

1. Audited `P05_HALL_VDP_MATERIAL_METROLOGY.md` before creating any new Hall documentation.
2. Determined P05 is already operationally mature and creating a separate empirical Hall module would be redundant.
3. Pivoted the round to the unresolved P15 cryogenic packaging branch.
4. Recovered primary Honeywell HgCdTe cryogenic attachment evidence and direct U.S. Navy HgCdTe photoconductor thermal-stack evidence.
5. Added P33 empirical package execution window.
6. Added a blank P33 qualification register.
7. Added Round-26 source and gap ledgers.

---

## P05 audit conclusion

P05 already includes the execution requirements needed for process-development measurements:

- contact-ohmicity checks;
- current/self-heating screening;
- van der Pauw reversal/reciprocity;
- measured field calibration;
- symmetric field sweep;
- field/current antisymmetrization;
- single-carrier validity;
- multicarrier escalation;
- Hall-factor discipline;
- uncertainty/repeatability;
- raw-data record.

Do not create P33 Hall merely to continue numbering.

Remaining P05 items are true closure items:

- historical RP-01 Hall-contact recipe;
- exact source measurement temperature for the supplier n/µ values;
- final production acceptance bands;
- Hall-factor model if a physical-density correction is later required.

---

## P33 primary empirical result

The package is now treated as part of the detector transfer function.

### Honeywell attachment evidence

US4081819A directly demonstrates that cryogenic cracking of epitaxial HgCdTe devices can be dominated by the bonding layer.

Named compliant attachment examples:

- Dow Corning 3110 RTV silicone;
- 3112 RTV silicone;
- 3116 RTV silicone.

In the source's controlled 5-K experiment, glass adhesive cracked while two silicone-attached branches did not, despite different air-abrasion depths and thermocompression pressures.

The 5-g/40-g values are experiment conditions, not RP-01 bonding setpoints.

### Direct photoconductor thermal evidence

US4012691A / Bartoli et al. describe:

`HgCdTe -> epoxy -> Irtran 2 or sapphire -> GE 7031 varnish -> copper heat sink at 77 K`.

They directly find construction-dependent recovery on:

- several-ms scale;
- hundreds-ms scale;

and attribute the two scales to thermally resistive bonding layers.

Therefore package thermal response must be measured and separated from intrinsic P13 detector response.

### Thin-device stress evidence

US5462882A documents thermomechanical defects in thin 5–10-µm HgCdTe/epoxy/Si stacks under thermal processing/cooldown.

US5365088A demonstrates sapphire as a CTE/thermal-mechanical buffer in HgCdTe/Si hybrids and documents repeated cryogenic-cycle reliability as a real architecture problem.

---

## Permanent process interpretation

Attachment selection is a multi-objective detector optimization:

`attachment compliance <-> thermal conductance <-> vacuum/cure compatibility <-> detector electrical/noise stability`.

A mechanically strong package can be thermally or electrically unacceptable.

A compliant package can survive cooldown yet create excessive self-heating or slow thermal poles.

P33 therefore measures:

- bondline thickness/voiding;
- CTE/carrier construction;
- cryogenic mechanical state;
- electrical/noise pre/post state;
- package thermal resistance;
- thermal impulse/recovery kernel;
- optical geometry;
- thermal-cycle genealogy.

---

## Files created

- `procedures/P33_CRYOGENIC_DIE_ATTACH_INTERCONNECT_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P33_CRYOGENIC_PACKAGE_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND26.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND26.md`
- this checkpoint

---

## Historical gaps still open

- exact RP-01 die singulation and die outline;
- exact adhesive/carrier;
- exact bondline;
- exact wire/ribbon metallurgy;
- bond method/setpoints;
- cold finger/header/Dewar;
- aperture/window/filter;
- vacuum and package bake;
- thermal-cycle history.

Same-Honeywell and NRL constructions remain transfer evidence, not historical RP-01 reconstruction.

---

## Strongest next empirical round

### Round 27 — P08 RIE reactor execution / plasma-state closure

P24 provides the empirical blocking-contact response framework, but major apparatus variables remain open:

- exact Plasma Technology reactor model;
- RF frequency;
- electrode diameter/area;
- electrode spacing;
- powered/grounded electrode configuration;
- sample mounting/thermal coupling;
- self-bias / dc bias;
- sample temperature during the 60-s exposure;
- base pressure and pump configuration;
- MFC calibration and individual CH4/H2 flows;
- ignition/stabilization sequence;
- oxide-clear state;
- chamber seasoning/clean history;
- endpoint/physical etch depth versus electrical conversion depth.

Search same-UWA theses/papers and primary Plasma Technology-era HgCdTe RIE literature before defining any reactor transfer recipe.

If exact apparatus values remain unrecovered, build P34 as a **reactor-equivalence empirical qualification window**, not a fabricated historical reactor specification.

---

## Continuity rule

Before future theoretical expansion, continue closing the practical empirical gaps that determine whether a competent researcher can actually reproduce the detector.
