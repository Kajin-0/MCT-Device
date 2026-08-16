# P25 — anodic-oxide empirical process window / practical qualification

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert the existing P02/P02A/P02B/P02C native-oxide branch into a practical, literature-grounded passivation procedure for the RP-01 x≈0.30 HgCdTe photoconductor process.

The historical RP-01 paper directly closes only:

- passivant identity: native anodic oxide;
- nominal oxide thickness: approximately `800 Å = 80 nm`;
- process order: mesa definition precedes anodic oxidation; contact windows are subsequently opened through the oxide by the localized CH4/H2 RIE step.

The exact UWA electrolyte, current density, cell geometry, endpoint and rinse are still not published in the recovered RP-01 record.

P25 therefore uses the strongest experimentally disclosed HgCdTe native-oxide process as a **transfer center**, while preserving its non-UWA provenance.

The practical chain is:

`incoming HgCdTe surface -> cell/bath state -> galvanostatic V(t) signature -> physical oxide -> electrical interface -> sidewall/device response -> downstream RIE compatibility`.

P25 supplements rather than replaces P02/P02A/P02B/P02C.

---

# 2. Provenance classes

## `DIRECT-RP01`

Directly reported for the canonical Smith et al. 2001 detector.

## `PRIMARY-TI-PHOTOCONDUCTOR`

Direct HgCdTe photoconductor anodization process disclosed by Texas Instruments in U.S. Patent 3,977,018. This is the strongest executable historical transfer process currently recovered, but it is not proved to be the UWA traveler.

## `PRIMARY-EXPERIMENTAL-HGCDTE`

Direct experimental HgCdTe anodization/passivation paper, but not the exact RP-01 material/process.

## `PRIMARY-X030-CHEMISTRY`

Direct experimental oxide-composition/process study including x≈0.30 material.

## `SAME-UWA-FUNCTIONAL`

Same-UWA photoconductor passivation/device evidence; useful for final electrical-function requirements, not for assigning the anodization bath recipe.

No value may change provenance class by repetition in this repository.

---

# 3. Historical RP-01 target — `DIRECT-RP01`

The canonical detector used:

- native anodic oxide;
- nominal thickness approximately `800 Å = 80 nm`.

The recovered paper does not specify:

- electrolyte;
- bath concentration;
- electrode materials;
- exposed-area definition;
- current density;
- voltage endpoint;
- process time;
- bath temperature;
- agitation;
- post-anodization rinse/dry sequence.

Therefore the following practical process is a local transfer candidate, not a claim of historical UWA identity.

---

# 4. Strongest executable transfer center — Texas Instruments

## 4.1 Preferred bath — `PRIMARY-TI-PHOTOCONDUCTOR`

The TI process discloses a preferred electrolyte of:

- `0.1 M KOH`;
- solvent: `90% ethylene glycol / 10% deionized water`.

The patent also reports substantial electrolyte dependence:

- aqueous KOH above approximately `0.1 M` can produce dark/matte films;
- lower-concentration aqueous KOH gives shiny interference-colored films;
- approximately `0.01–0.05 M` aqueous KOH was useful for more uniform films, but very low-concentration aqueous baths had limited maximum uniform thickness;
- `0.1 M` borax in ethylene glycol was another usable oxide-growth bath;
- replacing much of the water with ethylene glycol changes tellurium-species solubility and permits thicker, more uniform films.

**P25 rule:** bath chemistry is a controlled process variable. Do not treat “KOH anodization” as a complete recipe.

## 4.2 Cell polarity and electrodes — `PRIMARY-TI-PHOTOCONDUCTOR`

The HgCdTe specimen is the **anode**.

The original TI disclosure uses a **carbon-rod cathode**.

Later HgCdTe anodization implementations used alternative counter-electrode arrangements, including platinum, but these are separate apparatus lineages.

For local transfer:

- carbon is the first historically anchored counter-electrode candidate;
- cathode material, exposed area, separation and position shall be fixed and recorded;
- changing cathode geometry or material constitutes a process change until equivalence is demonstrated.

## 4.3 Electrical mode — `PRIMARY-TI-PHOTOCONDUCTOR`

Operate galvanostatically:

- constant current density approximately `0.3 mA/cm²`;
- formation voltage rises during oxide growth;
- preferred endpoint approximately `15 V`;
- typical reported time approximately `2 min`;
- resulting film approximately `800 Å`;
- reported visual endpoint: uniform **deep-blue** film.

These values form the P25 **literature transfer center**:

`0.1 M KOH / 90% EG + 10% DI / 0.30 mA cm^-2 / ~15 V / ~2 min / ~80 nm`.

They are not production limits and are not claimed to be the exact RP-01 UWA recipe.

---

# 5. Independent experimental support for the transfer center

A direct experimental native-oxide C–V study on Hg0.8Cd0.2Te used:

- pre-oxide etch approximately `30–60 s` in `1% Br2 in ethylene glycol`;
- DI-water rinse;
- room-temperature anodization;
- `0.1 M KOH` in `90% ethylene glycol / 10% water`;
- constant current densities approximately `0.2–0.5 mA/cm²`;
- an example native oxide thickness approximately `70 nm`.

This independently validates the bath/current-density family as an experimentally used HgCdTe process.

**Transfer restriction:** the Br2/ethylene-glycol etch is not an RP-01 pre-anodization recipe and shall not be inserted into P01/P02 by default.

---

# 6. Composition-matched x≈0.30 oxide chemistry

Primary experimental work on anodic oxides of n-type Hg1−xCdxTe including `x≈0.30` shows that oxide chemistry/structure depends strongly on:

- electrolyte pH;
- anodic current density;
- aqueous versus ethylene-glycol content.

Reported trends include:

- high-pH conditions favor Cd tellurite-rich oxide chemistry;
- incorporating ethylene glycol reduces tellurite solubility and changes precipitation chemistry;
- Hg-containing tellurite species can be retained more effectively in EG-containing baths;
- resulting film physical properties depend on the electrochemical environment rather than thickness alone.

This establishes a practical rule for RP-01 transfer:

**two nominally 80-nm oxides are not automatically equivalent if bath chemistry, current density or starting surface differ.**

---

# 7. Starting-surface control

The anodization interface inherits the state left by the preceding mesa/surface preparation.

Before P25, record:

- wafer/growth/coupon ID;
- measured composition/optical-edge coordinate;
- active-layer thickness;
- incoming Hall state where available;
- preceding wet chemistry;
- semiconductor depth removed by the last etch;
- final rinse;
- elapsed clean-to-anodization time;
- storage atmosphere during that delay;
- optical/DIC image of the surface;
- mesa sidewall state when present.

Do not transplant the aggressive bulk-HgCdTe surface preparations used in some anodization-mechanism studies to a 9.5-µm LPE layer without separate justification.

---

# 8. Bath preparation record

For every electrolyte batch record:

- batch ID;
- KOH supplier/lot/purity;
- weighed or delivered KOH quantity;
- final concentration calculation;
- ethylene glycol supplier/lot/grade;
- water content specification if known;
- DI-water source/resistivity;
- exact EG:H2O preparation basis used locally;
- preparation order;
- preparation timestamp;
- storage container;
- bath age at use;
- bath temperature;
- whether the bath is fresh, reused or replenished;
- visible contamination/precipitate;
- conductivity/pH if measured and method/calibration.

The historical sources do not fully close reagent grades, ratio convention or shelf-life. These remain local qualification variables.

---

# 9. Cell construction / exposed area

The cell record must contain:

- vessel material and ID;
- HgCdTe electrical-contact method;
- anode lead material/location;
- counter-electrode material;
- counter-electrode exposed dimensions;
- electrode separation;
- relative orientation;
- sample immersion depth;
- total HgCdTe area in electrical contact with electrolyte;
- masking/fixture material;
- whether mesa top, sidewall and backside are exposed;
- agitation state.

The required applied current is

`I = J A_exposed`.

Use the **electrochemically exposed area**, not nominal die area, when calculating current density.

A 10% area error creates a 10% current-density error at fixed current.

---

# 10. Agitation / mass transport

Composition-matched x≈0.30 anodization literature shows an initial dissolution/precipitation stage whose induction behavior changes with mass transport.

Agitation can alter or suppress stable film formation at sufficiently low current density by removing dissolved species from the anode region.

Therefore record explicitly:

- `UNSTIRRED`, `STIRRED`, or another defined state;
- stirrer/rotation method;
- speed if used;
- sample orientation;
- gas bubbles on the specimen;
- any flow across the active surface.

For first RP-01 transfer, use an **unstirred/static bath** unless the selected primary implementation requires otherwise. This is a local transfer choice, not a recovered UWA historical fact.

---

# 11. Galvanostatic run sequence

## 11.1 Pre-run

1. Verify bath identity and temperature.
2. Verify sample ID and incoming-surface record.
3. Determine exposed area.
4. Calculate current required for the selected `J`.
5. Verify current-source calibration and voltage compliance.
6. Verify voltage acquisition zero and polarity.
7. Photograph/document initial specimen surface where practical.

## 11.2 Process

For the first historical transfer center:

- set `J≈0.30 mA/cm²`;
- start simultaneous current/voltage/time acquisition before or at current application;
- maintain the defined static cell condition;
- record `V(t)` continuously or at a cadence adequate to resolve induction and oxide-growth portions;
- use approximately `15 V` and approximately `80 nm` only as expected transfer-center outcomes, not blind stop criteria until the local V(t)-thickness relation has been verified.

## 11.3 Stop record

Record:

- termination basis: voltage, time, charge, operator criterion, or compliance;
- terminal voltage;
- total time;
- total charge;
- charge per exposed area;
- current stability;
- visible bubbles/abnormality;
- final bath temperature.

---

# 12. Voltage-time trace as a process fingerprint

Do not reduce the process record to “0.3 mA/cm² for 2 min.”

Extract from `V(t)`:

- initial voltage;
- induction interval `t_ind`, if present;
- time of sustained voltage rise;
- `dV/dt` over a defined oxide-growth interval;
- terminal voltage;
- excursions/steps/noise;
- time to selected reference voltages;
- integrated charge per area.

An anomalous induction period or V(t) shape is evidence of changed:

- starting surface;
- bath chemistry;
- current density;
- area calculation;
- mass transport;
- contact/fixture state;
- bath contamination/aging.

A coupon that accidentally reaches 80 nm after an abnormal trace should not automatically be treated as process-equivalent.

---

# 13. Post-process rinse/dry

The exact RP-01 and TI production rinse/dry details remain incompletely closed in the current source record.

Therefore P25 requires the local sequence to be explicit and frozen during qualification:

- immediate transfer delay after current termination;
- rinse fluid(s);
- rinse time/volume/agitation;
- drying method;
- delay to inspection/thickness metrology;
- delay to photoresist coating or storage;
- storage environment.

Do not permit operator-specific rinsing/drying to remain undocumented.

---

# 14. Physical oxide qualification

## 14.1 Thickness

Historical target:

`d_ox ≈ 800 Å = 80 nm`.

Measure quantitatively using a qualified technique such as:

- stylus profilometry across a deliberately created oxide step;
- ellipsometry with a documented optical model;
- cross-sectional method on sacrificial samples when necessary.

The TI lineage used profilometry and optical-interference/color observations.

## 14.2 Color

Uniform deep blue is a useful TI-lineage operator indicator for the approximately 800-Å film.

Color is **secondary metrology only** because it depends on:

- illumination spectrum;
- angle;
- oxide optical constants;
- underlying HgCdTe optical properties;
- thickness nonuniformity.

Freeze viewing/illumination conditions if color is used as an in-process visual check.

## 14.3 Uniformity and defects

Record/map:

- mean thickness;
- within-coupon range or standard deviation;
- edge-to-center trend;
- mesa-top versus sidewall observations where accessible;
- pinholes;
- matte regions;
- peeling/cracking;
- stains/residue;
- corner/edge anomalies.

---

# 15. Electrical-interface qualification

The passivation function is not equivalent to physical oxide thickness.

A native-oxide/HgCdTe interface study on x≈0.21 material reported at 77 K scales of approximately:

- fast interface-state density near midgap `~5×10^11 cm^-2 eV^-1`, increasing toward the band edges toward `~10^13 cm^-2 eV^-1`;
- positive fixed oxide charge of order `~6×10^11 cm^-2`;
- flat-band voltage around `-0.5 V` for an approximately 500-Å oxide on n-type material in the reported configuration.

These are **not RP-01 acceptance values**. They establish the order of magnitude and demonstrate that the electrical interface is a measurable independent process output.

Where appropriate, qualification structures should measure one or more of:

- C–V/interface-state behavior;
- surface/channel conductance;
- field-effect response;
- sheet resistance before/after passivation;
- dark I–V;
- low-frequency noise;
- lifetime/perimeter dependence.

---

# 16. Surface accumulation versus responsivity tradeoff

Same-UWA LWIR HgCdTe photoconductor work using a gate-controlled native-oxide/ZnS structure directly demonstrated that suppressing surface recombination by accumulation can also create excessive surface shunting.

For the x≈0.23 device studied:

- optimum surface potential was reported near `50 mV`;
- the floating native-oxide condition corresponded to approximately `72 mV`;
- operation near the optimum increased responsivity by approximately `70%` relative to the floating-gate state.

These numerical values are **not RP-01 x≈0.30 targets**.

The transferable practical conclusion is critical:

**more accumulation is not automatically better passivation.**

P25 release must therefore check the complete detector consequence, not simply maximize positive fixed charge or minimize an inferred surface-recombination parameter.

---

# 17. Mesa-sidewall qualification

P02C remains authoritative for sidewall coverage.

Because RP-01 anodizes after mesa definition, local release must verify that the electrochemical process adequately treats:

- mesa top;
- mesa sidewalls;
- mesa corners/perimeter;

while leaving the later contact windows available for controlled P08 opening.

A planar 80-nm witness does not prove sidewall passivation.

Use perimeter-to-area device comparisons and/or physical cross-sectional evidence as defined in P02C.

---

# 18. P08 compatibility gate

The native oxide is also the layer through which the RP-01 localized CH4/H2 RIE opens the contact region.

For every candidate P25 oxide condition record downstream:

- oxide-clear time under the selected P08 reactor/process;
- residual oxide evidence;
- physical HgCdTe recession after clear;
- n+ conversion state/depth where applicable;
- Cr/Au contact result;
- TLM contact resistivity;
- detector responsivity/noise.

A chemically different 80-nm oxide that requires materially different RIE exposure is not automatically equivalent to the RP-01 passivation/contact stack.

---

# 19. Thermal/storage stability record

Native-oxide prior art and later HgCdTe passivation work show that passivation/electrical-interface properties can evolve with heat and storage.

Do not assign a universal RP-01 bake limit from another architecture.

Instead record during qualification:

- anodization-to-lithography delay;
- storage temperature/atmosphere;
- cumulative room-temperature storage;
- all photoresist prebakes;
- vacuum bakes;
- metallization thermal exposure;
- cryogenic cycles;
- post-aging physical oxide appearance;
- post-aging dark I–V/noise/responsivity where relevant.

Stability is part of passivation release.

---

# 20. Initial empirical qualification matrix

Before optimizing many variables, replicate the literature center and establish metrology.

## Stage A — center replication

Use repeated matched x≈0.30 coupons at:

- `0.1 M KOH`;
- `90% EG / 10% DI water`;
- static bath;
- approximately room temperature, measured;
- `J=0.30 mA/cm²`;
- expected terminal region near `15 V`;
- expected oxide thickness near `80 nm`.

Measure full V(t), charge/area, thickness, color/uniformity and surface/electrical state.

## Stage B — bounded current-density sensitivity

After center reproducibility is known, compare a narrow current-density range supported by direct experimental HgCdTe work, for example the existing P02 qualification levels around `0.2–0.4 mA/cm²`, while holding bath/surface/cell geometry fixed.

Do not release these levels as production bounds merely because they appear in literature.

## Stage C — surface-history sensitivity

Compare controlled, minimally different pre-anodization surface histories that are compatible with the RP-01 LPE layer.

The purpose is to determine whether V(t), oxide thickness, interface behavior or downstream noise are dominated by the incoming surface.

## Stage D — device closure

Fabricate matched devices through P08–P13 and compare:

- dark resistance/I–V;
- responsivity;
- 1/f and g-r noise;
- NEP/D*;
- time response;
- perimeter dependence;
- thermal/storage stability.

---

# 21. Required run record

A P25 run is incomplete without all applicable fields:

### Incoming material
- wafer/coupon ID;
- composition/edge;
- thickness;
- Hall state;
- mesa state;
- last wet process;
- clean-to-anodize delay.

### Bath
- batch ID;
- KOH concentration;
- EG:H2O basis;
- reagent lots;
- age;
- temperature;
- pH/conductivity if measured;
- agitation state.

### Cell
- exposed area;
- anode-contact method;
- cathode material;
- cathode area;
- electrode spacing/orientation;
- immersion depth.

### Electrical process
- current;
- current density;
- V(t) raw file;
- induction time;
- growth slope descriptor;
- terminal voltage;
- duration;
- charge/area;
- compliance events.

### Post process
- rinse/dry;
- color/uniformity;
- oxide thickness map;
- storage history;
- delay to subsequent lithography/RIE.

### Functional closure
- P08 oxide-clear result;
- P09 contact/TLM;
- P10 dark electrical result;
- P11 responsivity;
- P12 noise/NEP/D*;
- P13 time response where required.

---

# 22. Failure signatures and first discriminating checks

| Signature | Competing causes | First discriminating checks |
|---|---|---|
| no sustained voltage rise | current too low; surface dissolution; wrong bath; area error; agitation | verify area/current, bath concentration, agitation, incoming surface; inspect V(t) induction |
| excessively rapid voltage rise | small exposed area; poor electrical contact; depleted/dry region; bath error | recalculate area/J, inspect fixture/contact, repeat with known witness |
| matte/dark film | bath concentration/chemistry; roughening; surface contamination | bath composition/age, DIC, thickness map, fresh-bath repeat |
| strong color gradient | current-density/mass-transport nonuniformity; geometry; bubbles | cell geometry, immersion, bubble record, thickness map |
| correct thickness but high 1/f noise | interface chemistry/state, surface damage, sidewall failure | C–V/field effect, P/A devices, incoming surface comparison |
| good noise but low responsivity | excessive surface accumulation/shunting; contact sweepout; bulk material | field-effect/sheet conductance, P24 contact tests, P10 heating |
| slow or incomplete P08 clear | oxide composition/density differs; thickness high; RIE drift | independent thickness, oxide-clear series, reactor state |
| passivation degrades after bake/storage | interface/oxide instability; contamination; mechanical damage | controlled aging split, physical inspection, repeat electrical metrics |

Use P18 for full root-cause/CAPA handling.

---

# 23. Release logic

P25 may advance to `LOCAL-QUALIFIED` only after:

1. bath/cell/electrical process is fully specified locally;
2. repeated center runs give stable V(t) fingerprints;
3. measured oxide thickness/uniformity meet a detector-derived requirement;
4. electrical interface behavior is stable and acceptable;
5. mesa sidewalls are functionally passivated;
6. P08 oxide clearing remains reproducible;
7. P09 contact performance remains acceptable;
8. P11/P12/P13 devices show acceptable responsivity/noise/time response;
9. thermal/storage history is controlled;
10. repeated independent runs support P17 capability analysis.

The literature center is not itself a production specification.

---

# 24. Remaining empirical recovery targets

Still worth searching before final manual release:

- full Musca/Smith/Dell/Faraone 1998/1999 UWA passivation/contact paper;
- Musca/Siliquini thesis experimental sections;
- exact historical UWA bath/electrode/rinse sequence;
- exact UWA anodization-to-resist delay/storage condition;
- quantitative same-UWA native-oxide interface measurements on x≈0.30 LPE photoconductors.

Until recovered, preserve the transfer provenance.

---

# 25. Principal source lineage

1. Smith et al. 2001 RP-01 canonical photoconductor paper — direct 800-Å native-oxide identity/thickness and downstream process context.
2. Texas Instruments, U.S. Patent 3,977,018 — executable HgCdTe photoconductor anodic-oxide process: KOH/EG-water, galvanostatic current, formation voltage/time, film color/thickness and cell architecture.
3. Direct Hg0.8Cd0.2Te C–V/native-oxide study — independent use of 0.1 M KOH/90% EG/10% water at 0.2–0.5 mA/cm² and room temperature.
4. Direct composition/structure study of anodic oxides on Hg1−xCdxTe including x≈0.30 — electrolyte-pH/current-density/EG dependence.
5. Direct HgCdTe/native-oxide interface study — quantitative interface-state/fixed-charge scales.
6. Same-UWA gate-controlled LWIR photoconductor study — direct functional evidence that native-oxide-induced accumulation can trade surface recombination against shunting/responsivity.
7. P02B x≈0.30 anodic-oxidation mechanism lineage — induction/mass-transport/start-surface dependence.
