# P27 — Mask-2 photoresist / exposure / developer / lift-off empirical process window

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert the partially closed RP-01 Mask-2 lithography sequence into a practical, literature-grounded qualification procedure without falsely identifying an unrecovered commercial resist.

The direct historical fingerprint is unusually specific:

`4–5 µm resist -> 80 °C / 30 min prebake -> chlorobenzene 30 min -> pattern -> develop -> water rinse -> CH4/H2 RIE -> Cr 30 nm / Au 270 nm -> lift-off`.

P27 keeps those direct anchors fixed during first transfer and uses historical chlorobenzene single-layer lift-off literature plus primary patent examples to constrain the missing resist/exposure/developer/lift-off variables.

P27 supplements P14/P14A and P26.

---

# 2. Evidence classes

## `DIRECT-RP01`

Directly reported in Smith et al. 2001.

## `PRIMARY-CHLOROBENZENE-LIFTOFF`

Primary paper/patent in the historical single-layer positive-diazo/novolak chlorobenzene lift-off lineage.

## `PRIMARY-AZ4000-THICKNESS`

Primary process example establishing thickness/spin/exposure behavior for a named AZ4000-family resist, but not RP-01.

## `MECHANISM-CONSISTENT`

A conclusion supported by the historical lift-off mechanism but not identifying the UWA product.

## `LOCAL-QUAL`

A variable that must be selected by local lithographic qualification.

No product or process value may be relabeled `DIRECT-RP01` without direct UWA/RP-01 evidence.

---

# 3. Direct RP-01 Mask-2 anchors

Directly reported:

- photoresist thickness approximately `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene treatment `30 min`;
- then patterned, developed and rinsed in water;
- resist remains through the CH4/H2 RIE contact-opening/conversion step;
- same resist process supports lift-off of Cr `30 nm` + Au `270 nm`.

Directly **not** reported:

- resist manufacturer/product;
- solids content/dilution;
- dispense volume;
- spin speed/acceleration/time;
- dehydration or adhesion promoter;
- exposure wavelength/dose/tool/contact mode;
- whether chlorobenzene occurred before or after UV exposure within the word `patterned`;
- chlorobenzene temperature/purity/agitation;
- post-soak dry/bake;
- developer product/concentration/time/temperature/agitation;
- final drying method after the water rinse;
- lift-off solvent/time/temperature/agitation;
- quantitative undercut/overhang.

---

# 4. Historical process-family identification

The Hatzakis/IBM single-step optical lift-off lineage explicitly uses **positive AZ-type diazo/novolak photoresist** modified by soaking in chlorobenzene or another aromatic solvent.

The mechanism is differential development:

- chlorobenzene penetrates/modifies a near-surface portion of the resist;
- that layer develops more slowly than the underlying exposed resist;
- the result is a re-entrant/overhanging profile suitable for lift-off.

Historical process-control work identifies strong interactions among:

- residual casting solvent after soft bake;
- exposure;
- chlorobenzene soak time;
- soak temperature;
- chlorobenzene purity/impurities/use history;
- developer strength;
- development time;
- bake conditions.

Useful control observables include:

- film thickness before/after chlorobenzene;
- developed resist height;
- top and bottom opening CDs;
- undercut/overhang;
- post-RIE profile;
- final lift-off yield.

### P27 conclusion

The historical mechanism is strongly consistent with a positive DNQ/diazo-novolak AZ-type family, but **does not uniquely identify the RP-01 commercial resist**.

---

# 5. Candidate-family narrowing from film thickness

The RP-01 single-layer thickness `4–5 µm` is useful discriminating evidence.

## 5.1 AZ4110 — strong chlorobenzene evidence, weak thickness match

A primary fabrication example directly reports:

- positive AZ4110;
- spin `4000 rpm / 30 s`;
- hotplate bake `90 °C / 2 min`;
- UV exposure dose `900 J/m² = 90 mJ/cm²` with exposure of order `10 s`;
- chlorobenzene `28–30 °C / 2 min`;
- developer diluted `1:1` with water;
- develop `60 s`;
- careful water rinse/blow dry;
- resulting resist thickness approximately `1100 nm = 1.1 µm`.

Use: direct proof that AZ4110 supports chlorobenzene-shaped lift-off.

Restriction: this particular single-coat condition is much thinner than RP-01's 4–5 µm layer.

## 5.2 AZ4330 — strong thickness match

A primary process example reports:

- AZ4330, m-cresol-novolak type;
- film thickness approximately `4.3 µm`;
- spin `3500 rpm / 30 s`;
- bake `85 °C / 10 min`;
- exposure `150 mJ/cm²` at `365 nm` using a GCA step-and-repeat tool.

That example uses a different silylation/development process and is **not** a chlorobenzene lift-off recipe.

Use: direct evidence that AZ4330 naturally occupies the correct RP-01 single-coat thickness class.

## 5.3 AZ4400 — direct 4–5 µm thickness class

Primary patents use AZ4400-type positive resist at approximately `4 µm` and `5 µm` film thicknesses in patterned microfabrication processes.

Use: geometric/thickness candidate family only.

Exact chlorobenzene RP-01 compatibility and spin/exposure settings remain unclosed.

## 5.4 AZ4620 — direct 5-µm thickness example

A primary microfabrication example reports a `5 µm` AZ4620 positive-resist layer at `4000 rpm`.

Other primary examples use AZ4620 as a much thicker resist, demonstrating that product/solids/spin conditions strongly affect final thickness.

Use: another thick AZ4000-family candidate.

Restriction: the currently recovered example is much later than RP-01 and does not prove UWA identity.

## 5.5 Candidate-ranking consequence

For local screening:

- **AZ4110** = chlorobenzene mechanism/control reference;
- **AZ4330/AZ4400/AZ4620-class** = stronger single-coat thickness matches;
- any modern equivalent must be verified as a positive DNQ/novolak or otherwise experimentally compatible lift-off resist, not selected by name similarity alone.

This is a screening hierarchy, **not** a historical identification.

---

# 6. Fully quantified chlorobenzene control branch

A primary single-layer lift-off patent provides a useful complete control process on AZ1350J:

- spin `3000 rpm`;
- soft bake `90 °C / 20 min`;
- chlorobenzene `15 min`;
- post-soak bake `90 °C / 10 min`;
- demonstrated resist overhang about `0.4 µm` in that process;
- Cr `200 Å` + Al `9900 Å` deposition;
- acetone lift-off `10 min` with ultrasonic agitation, then fresh acetone for an additional `5 min`.

Its comparative prior-art branch used:

- AZ1350J `4000 rpm`;
- `90 °C / 10 min` soft bake;
- exposure `5.8 s` at `13.6 mW/cm²` = approximately `78.9 mJ/cm²`;
- chlorobenzene `10 min`;
- Shipley Microposit 303A developer `10 s`;
- Cr `200 Å` + Al `9900 Å`;
- acetone + ultrasonics requiring about `8 h` for lift-off.

### P27 use

This control branch proves quantitatively that post-soak bake/profile control can dramatically alter lift-off time and sidewall discontinuity.

Do not transplant AZ1350J, 90 °C bake, 15-min chlorobenzene, acetone ultrasound, or Cr/Al stack into RP-01. Use the branch for process-development controls only.

---

# 7. RP-01 chlorobenzene sequence ambiguity

RP-01 states the resist was prebaked, soaked in chlorobenzene for a further 30 min, **then patterned, developed and rinsed in water**.

A literal reading suggests the chlorobenzene soak may precede exposure/pattern definition.

Historical chlorobenzene processes exist both:

- `soft bake -> exposure -> chlorobenzene -> develop`, and
- `soft bake -> chlorobenzene -> exposure -> develop`.

Therefore P27 shall not silently choose one ordering as historical fact.

## First transfer branches

Where material allows, compare:

- Branch A: `80 °C/30 min -> chlorobenzene 30 min -> expose -> develop`;
- Branch B: `80 °C/30 min -> expose -> chlorobenzene 30 min -> develop`.

All other variables held fixed.

Responses:

- resist thickness loss;
- opening CD;
- undercut/overhang;
- scum;
- RIE survival;
- final metal lift-off.

If a direct UWA source later closes the sequence, retire the nonhistorical branch.

---

# 8. Chlorobenzene bath control

Every P27 run records:

- supplier/lot/grade;
- bath container ID;
- fresh versus reused bath;
- bath age;
- temperature at start/end;
- soak start/end;
- sample orientation;
- agitation/static condition;
- cover/evaporation control;
- visible contamination;
- thickness before soak;
- thickness after soak/dry.

Historical literature shows soak time, temperature and impurity/use state affect penetration/profile. Therefore `30 min chlorobenzene` is incomplete unless bath state is recorded.

Initial RP-01 transfer should use a defined fresh/static bath unless a direct historical source states otherwise.

---

# 9. Spin-coating qualification

Because the resist product is unknown, no historical spin speed can be inferred from the final 4–5 µm thickness.

For each candidate resist:

1. measure incoming viscosity/lot if available;
2. dispense reproducibly;
3. record spin acceleration, speed and duration;
4. inspect edge bead and coverage over mesa topography;
5. bake at the direct RP-01 center `80 °C / 30 min`;
6. measure thickness at multiple positions;
7. select the spin condition that reproducibly centers the **measured** film in the 4–5 µm historical range.

Candidate spin speeds from other products are screening references only.

Do not label `3500 rpm` or `4000 rpm` historical RP-01 values.

---

# 10. Exposure qualification

Historical RP-01 exposure tool/wavelength/dose are open.

Primary diazo/novolak examples in the relevant process family demonstrate doses around:

- `~78.9 mJ/cm²` in one AZ1350J comparison process;
- `90 mJ/cm²` in one AZ4110 chlorobenzene process;
- `150 mJ/cm² at 365 nm` in one 4.3-µm AZ4330 process.

These values show the order of magnitude but are product/process specific.

## P27 local exposure procedure

For each candidate resist/developer pair:

1. characterize the clearing dose on the actual 4–5 µm film after the selected RP-01 bake/chlorobenzene branch;
2. use a dose matrix around that measured clearing transition;
3. measure top/bottom CD, resist height and overhang;
4. retain only doses that open the contact window without losing RIE-mask margin or lift-off profile.

Record:

- aligner/model;
- wavelength/band;
- irradiance calibration;
- exposure mode;
- actual dose;
- mask contact/proximity state;
- sample temperature where relevant.

Do not release exposure from nominal seconds alone.

---

# 11. Developer qualification

The direct RP-01 paper says only `developed and rinsed in water`.

Historical AZ/diazo-novolak lift-off examples use aqueous alkaline developers, including:

- Shipley Microposit 303A in the AZ1350J chlorobenzene lineage;
- diluted aqueous developer in an AZ4110 chlorobenzene example;
- AZ400K/KOH-family development with AZ4000-series resists in other processes.

This strongly supports an aqueous-alkaline developer **family**, but does not identify the UWA product/concentration.

## Local rule

Developer must be product-matched and recorded by:

- product/lot;
- concentrate:diluent ratio;
- DI-water quality;
- bath/puddle temperature;
- fresh/reuse state;
- develop duration;
- agitation;
- endpoint/clearing observation;
- water-rinse duration/method;
- dry method.

The complete P25 anodic oxide is exposed to developer except where protected by resist, so developer compatibility with the oxide/passivated surface must be verified.

---

# 12. Post-develop metrology gate

Before P08, measure on representative devices/witnesses:

- resist thickness remaining;
- top opening CD;
- bottom opening CD;
- undercut per side;
- overhang length if resolvable;
- sidewall angle/profile;
- opening scum/residue;
- edge roughness;
- contact-window alignment;
- across-sample variation.

Primary control metric:

`u = (CD_bottom - CD_top)/2`

with sign convention documented.

Do not prescribe a universal minimum `u` from theory. Release profile must demonstrate actual metal-sidewall discontinuity and clean lift-off of the P26 300-nm stack.

---

# 13. RIE-survival gate

Mask 2 is not a normal lift-off-only resist. It must survive P08:

- CH4/H2;
- 64 sccm total;
- 100 mTorr;
- 50 W;
- 60 s historical center.

On sacrificial profile witnesses measure before and after P08:

- resist thickness;
- thickness loss;
- undercut/overhang;
- top/bottom CD;
- blistering/cracking/reflow/hardening;
- opening residue;
- sidewall deposition/polymer;
- contact-window blockage.

A resist that produces excellent pre-RIE overhang but loses the profile during P08 fails P27.

---

# 14. Metal-deposition/lift-off gate

After P26 Cr/Au deposition on qualification structures:

- verify discontinuity between metal on the substrate and metal on the resist top/sidewall;
- inspect fencing/stringers;
- inspect resist reflow;
- inspect shadowing/CD shrinkage;
- record actual final metal dimensions.

The historical stack is only `0.30 µm` total against `4–5 µm` resist, but thickness ratio alone is not acceptance.

---

# 15. Lift-off solvent qualification

The exact RP-01 lift-off solvent remains unrecovered.

Historical chlorobenzene single-layer lift-off literature includes acetone-based lift-off, including a primary branch using:

- acetone `10 min` + ultrasonic agitation;
- fresh acetone another `5 min`.

Other primary lift-off patents list acetone, NMP and commercial resist removers as possible solvents for positive novolak/diazo systems.

### RP-01 restriction

Do **not** call acetone the historical UWA solvent.

Do not introduce ultrasonic agitation directly on qualified HgCdTe devices without sacrificial validation.

## Initial local solvent screen

On sacrificial structures reproducing the full P14/P08/P26 stack:

1. test a compatible positive-resist solvent/remover beginning with the least mechanically aggressive condition;
2. record time to edge penetration/first release/full release;
3. avoid scraping;
4. inspect metal adhesion, oxide/passivation and mesa edges;
5. if agitation is required, escalate from gentle manual bath motion to controlled ultrasonics only after damage checks.

Every solvent branch receives its own recipe ID.

---

# 16. Candidate screening architecture

## Stage 0 — resist availability/chemistry check

For each candidate:

- verify positive-tone chemistry;
- verify film can reach 4–5 µm in one reproducible coat;
- verify compatibility with chlorobenzene and aqueous development;
- verify supplier processing window.

Do not screen a product solely because its name starts with AZ4xxx.

## Stage 1 — thickness

Determine spin condition yielding measured `4–5 µm` after the direct `80 °C / 30 min` bake.

## Stage 2 — 30-min chlorobenzene and sequence order

Test Branch A/B ordering with full bath control.

## Stage 3 — exposure/developer matrix

Determine clearing/profile window for each candidate at the actual film thickness.

## Stage 4 — P08 survival

Run historical-center RIE on sacrificial profile structures.

## Stage 5 — P26 stack + lift-off

Deposit `30 nm Cr / 270 nm Au`; qualify lift-off.

## Stage 6 — electrical closure

Use final structures for:

- P09/P26 80-K TLM;
- contact uniformity;
- P10 I–V;
- P12 low-frequency noise;
- aging/thermal cycle.

A resist recipe is not released based on clean optical images alone.

---

# 17. Practical candidate table

| Candidate/reference | Direct thickness example | Chlorobenzene evidence | Primary use in P27 |
|---|---:|---|---|
| AZ1350J | not RP-01 matched in recovered example | very strong; complete quantified historical control | profile/lift-off control branch |
| AZ4110 | ~1.1 µm at 4000 rpm/30 s in one example | strong direct chlorobenzene example | mechanism/developer/exposure control |
| AZ4330 | ~4.3 µm at 3500 rpm/30 s | AZ4000 family; exact product-specific CB branch not recovered | strong thickness candidate |
| AZ4400 | direct 4–5 µm examples | exact product-specific CB branch not recovered | strong thickness candidate |
| AZ4620 | direct 5-µm example at 4000 rpm | later AZ4000-family use; exact RP-01-era CB evidence not recovered | thick-resist candidate |

**No row identifies the historical RP-01 product.**

---

# 18. Current release blockers

P27 remains `PRE-RELEASE` until closed:

1. exact historical UWA resist, if recoverable;
2. historical spin program;
3. historical exposure tool/wavelength/dose;
4. chlorobenzene order relative to exposure;
5. chlorobenzene temperature/purity/agitation;
6. post-soak drying/bake;
7. historical developer product/concentration/time;
8. final post-water-rinse dry;
9. quantitative developed profile;
10. RIE-induced profile change;
11. historical lift-off solvent/time/agitation;
12. local selected resist/developer/solvent branch;
13. CD/overhang repeatability;
14. final metal lift-off defect rate;
15. P26 TLM/device performance;
16. P17 repeated-run capability.

---

# 19. Primary-source set used by P27

1. E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. M. Hatzakis, B. J. Canavello, J. M. Shaw, “Single-Step Optical Lift-Off Process,” *IBM Journal of Research and Development* 24, 452–460 (1980), DOI `10.1147/rd.244.0452`.
3. R. M. Halverson, M. W. MacIntyre, W. T. Motsiff, “The Mechanism of Single-Step Liftoff with Chlorobenzene in a Diazo-Type Resist,” *IBM Journal of Research and Development* 26, 590–595 (1982).
4. G. G. Collins, C. W. Halsted, “Process Control of the Chlorobenzene Single-Step Liftoff Process with a Diazo-Type Resist,” *IBM Journal of Research and Development* 26, 596–604 (1982).
5. A. Fathimulla, “Single-step lift-off process using chlorobenzene soak on AZ4000 resists,” *Journal of Vacuum Science & Technology B* 3(1), 25–27 (1985).
6. U.S. Patent `5,654,128`, single-resist-layer chlorobenzene lift-off process; includes quantified AZ1350J examples.
7. U.S. Patent `4,769,343`, single-step chlorobenzene lift-off / AZ-resist process and historical AZ4000/AZ4110 lineage.
8. GB Patent `2,229,005A`, quantified AZ4110 chlorobenzene/developer example.
9. EP Patent `0,410,268B1`, quantified 4.3-µm AZ4330 spin/bake/exposure example.
10. U.S. Patent `6,470,904B1` / related Parylene microvalve lineage, direct AZ4400 4–5-µm film examples.
11. CN Patent `101138663A`, direct 5-µm AZ4620 at 4000-rpm example.

