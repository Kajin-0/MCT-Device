# Source ledger addendum — Round 18 empirical anodic-oxide/passivation recovery

**Date:** 2026-08-16 America/New_York  
**Scope:** P02/P25 native anodic oxide and passivation; continued P24 source recovery.

This addendum records what was actually recovered, what evidence class it supports, and what remains inaccessible. It does not upgrade transfer-family values into RP-01 historical values.

---

## R18-S1 — canonical RP-01 detector paper

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16 (2001) 455–462. DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

Directly supports for P02/P25:

- native anodic oxide used on the detector;
- nominal thickness approximately `800 Å = 80 nm`;
- anodization occurred after mesa definition and before Mask-2 contact opening/RIE;
- residual oxide could later be stripped in diluted HCl during an LBIC diagnostic without removing the RIE-induced electrical signature.

Does **not** expose:

- anodization bath;
- electrode material/geometry;
- current density;
- endpoint voltage;
- time;
- rinse/dry sequence.

Historical traveler remains open.

---

## R18-S2 — Texas Instruments native anodic oxide patent

Texas Instruments Incorporated, U.S. Patent `3,977,018`, “Passivation of mercury cadmium telluride semiconductor surfaces by anodic oxidation.”

**Class:** `PRIMARY-TI-PHOTOCONDUCTOR`.

Recovered practical process information:

- HgCdTe specimen is the anode;
- carbon-rod cathode;
- preferred electrolyte `0.1 M KOH` in `90% ethylene glycol / 10% deionized water`;
- galvanostatic constant-current operation;
- preferred current density approximately `0.3 mA/cm²`;
- preferred formation-voltage region approximately `15 V`;
- approximately `2 min` reported formation time;
- approximately `800 Å` oxide;
- visual film described as uniform deep blue;
- oxide thickness evaluated using profilometry and optical-interference/color methods;
- voltage rises reproducibly as the oxide/solution impedance evolves;
- bath composition materially affects film appearance/uniformity/thickness capability.

Additional bath observations retained qualitatively:

- overly concentrated aqueous KOH may produce dark/matte films;
- lower-concentration aqueous KOH can produce shiny interference-colored films;
- borax/ethylene-glycol and KOH/EG-water are distinct useful process families.

**Use:** strongest executable transfer center currently available for RP-01-like 80-nm native oxide.

**Restriction:** not evidence that UWA used this exact recipe.

---

## R18-S3 — experimental Hg0.8Cd0.2Te native-oxide C–V study

Primary experimental paper indexed as “The interface characteristics of passivity anodic oxide films on Hg0.8Cd0.2Te by C–V measurements.”

**Class:** `PRIMARY-EXPERIMENTAL-HGCDTE`.

Recovered experimental details:

- Hg0.8Cd0.2Te;
- pre-anodization etch approximately `30–60 s` in `1% Br2 in ethylene glycol`;
- DI-water rinse;
- room-temperature anodization;
- standard electrolyte `0.1 M KOH / 90% ethylene glycol / 10% H2O`;
- constant current density range approximately `0.2–0.5 mA/cm²`;
- example oxide thickness approximately `70 nm`;
- C–V interface characterization at 10 kHz on an n-type example.

**Use:** independently validates the bath/current-density family experimentally.

**Restriction:** different composition and surface-prep branch; its Br2/EG etch is not imported into RP-01.

---

## R18-S4 — anodic-oxide composition/structure including x≈0.30

Primary article indexed as “Composition and structure of anodic oxide films on Hg1−xCdxTe.”

**Class:** `PRIMARY-X030-CHEMISTRY`.

Recovered scope/results:

- includes n-type x≈0.20 and x≈0.30 HgCdTe;
- galvanostatic anodization;
- oxide composition/structure depends strongly on electrolyte pH and anodic current density;
- high-pH chemistry favors Cd tellurite-rich films;
- replacement of aqueous solvent by ethylene glycol changes tellurite solubility/precipitation and can improve film physical properties.

**Use:** direct evidence that film chemistry is an independent output; equal thickness does not imply an equivalent interface.

No exact RP-01 executable recipe is claimed from this source.

---

## R18-S5 — native HgCdTe oxide interface electrical study

Primary article: “The interface between Hg1−xCdxTe and its native oxide,” *Solid-State Electronics* 22 (1979) 831–837. DOI `10.1016/0038-1101(79)90049-2`.

**Class:** `PRIMARY-EXPERIMENTAL-HGCDTE`.

For x≈0.21 material, reported 77-K electrical-interface scales include approximately:

- fast interface-state density `~5×10^11 cm^-2 eV^-1` near midgap, rising toward the band edges toward `~10^13 cm^-2 eV^-1`;
- positive fixed oxide charge of order `~6×10^11 cm^-2`;
- flat-band voltage of order `-0.5 V` for an approximately 500-Å oxide on the reported n-type sample.

**Use:** establishes measurable interface-output scale and motivates C–V/field-effect qualification.

**Restriction:** these are not RP-01 acceptance specifications.

---

## R18-S6 — same-UWA gate-controlled photoconductor passivation

J. F. Siliquini and L. Faraone, “A Gate-Controlled HgCdTe Long Wavelength Infrared Photoconductive Detector,” *Semiconductor Science and Technology* 12 (1997), DOI `10.1088/0268-1242/12/8/014`.

**Class:** `SAME-UWA-FUNCTIONAL`.

Recovered direct functional result for x≈0.23 LWIR photoconductor architecture:

- native oxide/ZnS gate/passivation structure;
- surface accumulation suppresses surface recombination but excessive accumulation produces surface shunting;
- reported optimum surface potential approximately `50 mV`;
- floating native-oxide state approximately `72 mV`;
- operation near optimum produced approximately `70%` greater responsivity than the floating-gate state.

**Use:** direct same-UWA evidence that passivation cannot be optimized by oxide thickness or accumulation alone.

**Restriction:** different x, band and gate stack; numbers are not RP-01 targets.

---

## R18-S7 — P02B x≈0.30 anodic-oxidation mechanism lineage

B. K. Janousek and R. C. Carscallen, 1982 HgCdTe anodic-oxidation work, including “The mechanism of (Hg,Cd)Te anodic oxidation,” *Journal of Applied Physics* 53, 1720–1726, plus same-author x=0.30 anodic-oxidation work.

**Class:** `PRIMARY-X030-MECHANISM` for primary conclusions; detailed numbers recovered from later technical synthesis remain secondary-attributed unless re-read in the primary article.

Important process conclusions already controlled in P02B/P25:

- initial dissolution/precipitation stage;
- induction time can depend strongly on current density/mass transport;
- stirring can suppress film formation at low current density;
- starting surface affects later oxide/interface state;
- pH controls oxide solubility/formation behavior.

**Use:** establishes V(t), induction time, agitation and starting surface as mandatory process variables.

---

## R18-S8 — later oxide-to-sulfide conversion patent lineage

U.S. Patent `5,036,376`, “Passivation oxide conversion.”

**Class:** `PRIMARY-PATENT-TRANSFER-OTHER`.

Recovered anodization apparatus/process example:

- two-electrode Teflon cell;
- HgCdTe horizontal;
- sample anode contacted by W/Ti probe;
- circular Pt cathode;
- `0.1 M KOH / 90% EG / 10% water`;
- room temperature;
- unstirred;
- constant current;
- example approximately `350 µA/cm²`, `15 min`, yielding approximately `600 Å` oxide before subsequent sulfide conversion.

**Use:** confirms later apparatus variants and importance of explicitly fixing counter-electrode/cell geometry.

**Restriction:** do not merge the Pt cathode or 15-min example with the TI 800-Å photoconductor recipe.

---

## R18-S9 — anodic fluoro-oxide patent lineage

U.S. Patent `4,961,829`.

**Class:** `PRIMARY-PATENT-ALTERNATE-PASSIVATION`.

Reported alternate electrolyte family includes KF/EG or KF+KOH/EG-water and current densities roughly `0.05–0.5 mA/cm²`; example x≈0.213 processing can produce approximately 600-Å fluoro-oxide.

**Use:** historical alternate passivation branch and stability context only.

**Restriction:** not native anodic-oxide RP-01.

---

## R18-S10 — John K. White UWA PhD thesis record

John Kenion White, 2005, UWA thesis, “Mid-wave infrared HgCdTe photodiode technology based on plasma induced p-to-n type conversion.”

**Class:** `SAME-UWA-THESIS-BIBLIOGRAPHIC / PARTIAL-ABSTRACT`.

Accessible institutional record establishes:

- H2/CH4 plasma-induced p→n conversion photodiode technology;
- double-layer ZnS on CdTe passivation branch compatible with RIE junctions;
- devices reportedly survived vacuum bake near `80 °C / 175 h` with negligible degradation in zero-bias `R0A` in that photodiode architecture.

Direct thesis PDF URL was identified but returned access/403 in the current retrieval path.

**Use:** alternate UWA passivation/stability branch and future source-recovery target.

**Restriction:** not RP-01 native oxide recipe; do not transfer 80 °C/175 h as a native-oxide qualification requirement.

---

## R18-S11 — Ryan Westerhout UWA PhD thesis record

Ryan Westerhout, 2013, UWA thesis, “A study of passivation, dark current and 1/f noise in mid-wave infrared HgCdTe photovoltaic detectors.”

**Class:** `SAME-UWA-THESIS-BIBLIOGRAPHIC / PARTIAL-ABSTRACT`.

Institutional record identifies a UWA photodiode passivation branch using MBE CdTe and thermally evaporated ZnS, with investigation of ZnS gate-insulator stability and SiN alternatives.

Direct thesis PDF URL was identified but returned access/403 in the current retrieval path.

**Use:** alternate-passivation/noise/stability context only.

---

## R18-S12 — same-UWA dry plasma conference source

E. P. G. Smith et al., “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors,” 2000 conference record; IEEE document identifier `939185`.

**Class:** `SAME-UWA-BIBLIOGRAPHIC / FULL-TEXT-OPEN`.

This is highly relevant to P24 because it may contain reactor/load-lock/vacuum-transfer details missing from RP-01.

Current search recovered bibliographic identity but not full experimental text.

**Action:** keep as an active source-recovery target; do not infer reactor geometry or vacuum conditions from title/abstract alone.

---

# Negative/recovery record

The following remain unrecovered despite targeted searching:

1. exact UWA/RP-01 anodization bath/current/cell/rinse;
2. full Musca/Smith/Dell/Faraone same-laboratory photoconductor passivation/contact proceedings paper;
3. direct thesis experimental sections that may contain RP-01-era oxide/RIE travelers;
4. full White 2005 thesis through the currently accessible institutional PDF endpoint;
5. full Westerhout 2013 thesis through the currently accessible institutional PDF endpoint;
6. full 2000 “Dry plasma technology…” paper.

This is **negative search evidence only**. It does not establish that the information is absent from the underlying documents or archives.

---

# Round-18 source consequence

The native-oxide process is now empirically much stronger than a generic candidate:

- exact RP-01 film identity/thickness are direct;
- an executable historical HgCdTe photoconductor process produces the same nominal 800-Å thickness using 0.1 M KOH/90% EG/10% DI, 0.3 mA/cm², ~15 V and ~2 min;
- experimental HgCdTe work independently validates the same bath/current-density family;
- x≈0.30 chemistry/mechanism sources prove that pH/current density/agitation/start surface affect film chemistry and induction;
- same-UWA functional work proves that the electrical surface state can trade recombination reduction against shunting.

What remains open is historical UWA identity and local process capability—not whether an executable, physically credible empirical transfer process exists.
