# P25A — anodic-oxide cell / electrolyte / current-density instantiation addendum

**Status:** CONTROLLED EMPIRICAL CLOSURE METHOD / PRE-FIRST-BUILD  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Close the specific P16A R15 execution gap without mislabeling a transfer-family anodization recipe as the unpublished UWA/RP-01 process.

P25 already controls oxide growth, voltage-time fingerprints, physical thickness, interface response and downstream device qualification. P25A adds the missing **apparatus and electrolyte-instantiation layer** needed to turn the strongest published transfer evidence into a numerically defined local branch:

`published anodization lineage -> explicit electrolyte mathematics -> cell branch -> measured electrochemical area -> selected J -> I=J A_exposed -> V(t)/Q/A -> oxide thickness/interface -> P08/P09/P12 closure -> LOCAL-BRANCH-FROZEN`.

P25A does not replace P02/P02A/P02B/P02C/P25. It does not claim recovery of the historical UWA anodization traveler.

---

## 2. Evidence classes

### `DIRECT-RP01`
Smith et al. 2001 canonical detector paper.

### `PRIMARY-TI-PC-3977018`
Catagnus and Baker, Texas Instruments, US 3,977,018, photoconductive HgCdTe native anodic oxide.

### `PRIMARY-TI-LATER-CELL-5036376`
Later Texas Instruments HgCdTe anodization apparatus disclosed in US 5,036,376. This is strong cell-construction transfer evidence but is not the same photoconductor process generation.

### `PRIMARY-X030-MECHANISM`
Janousek/Carscallen x≈0.30 anodic-oxidation mechanism lineage already controlled in P02B.

### `PRIMARY-HGCDTE-TRANSFER`
Other directly reported HgCdTe anodization processes useful for sensitivity/replication context.

### `LOCAL-DEFINED`
A local cell/electrolyte branch whose mathematics, materials and hardware are fully explicit but not yet qualified.

### `LOCAL-QUAL`
A locally defined branch that has passed the applicable P25 physical/interface/downstream gates.

### `OPEN-HISTORICAL`
A parameter not recovered for the UWA/RP-01 process.

---

## 3. Historical RP-01 boundary

RP-01 directly closes only:

- passivant: native anodic oxide;
- nominal oxide thickness: approximately `800 Å = 80 nm`;
- process order: wet mesa -> anodic oxide -> Mask-2/contact-window opening -> localized CH4/H2 RIE -> Cr/Au.

Still `OPEN-HISTORICAL`:

- electrolyte identity/concentration;
- EG/water ratio, if used;
- cell vessel and electrode materials;
- anode-contact geometry;
- counter-electrode geometry;
- electrochemically exposed area;
- current density;
- absolute current;
- endpoint voltage/time/charge;
- bath temperature/agitation;
- rinse/dry;
- P28-to-P25 and P25-to-Mask-2 clocks.

The same-UWA Musca/Smith/Dell/Faraone 1999 contact/passivation paper is bibliographically identified, but no executable anodization recipe has been recovered from accessible text.

---

## 4. Strongest photoconductor transfer branch — TI US3977018

US3977018 is directly about HgCdTe **photoconductive** detector passivation and is therefore the principal apparatus/process transfer center retained by P25.

### 4.1 Direct electrolyte definition

The patent directly gives a preferred electrolyte family as:

`0.1 M KOH / 90% ethylene glycol / 10% deionized water`.

It further states that for thick, uniform oxide growth:

`0.1 mole KOH is dissolved in 1 liter of 90% ethylene glycol / 10% deionized water`.

This closes two points that must remain separate:

1. the KOH inventory is explicitly tied to `0.1 mol per liter` of the stated mixed solvent;
2. the recovered text still does **not** explicitly say whether the `90% / 10%` solvent proportion is `v/v`, `w/w`, or another basis.

Therefore:

`KOH molarity definition = PRIMARY-TI-PC-CLOSED`  
`EG:H2O 90:10 preparation basis = OPEN-HISTORICAL`.

### 4.2 Derived KOH mass — arithmetic only

Using `M_KOH = 56.1056 g/mol`, an ideal 1.000-L batch at 0.1000 mol/L contains:

`m_KOH,pure = 5.61056 g`.

For a reagent with certified mass fraction/assay `a_KOH`:

`m_KOH,reagent = 5.61056 g / a_KOH`

for the corresponding 1-L nominal branch, provided the local recipe defines how the final liter is established.

This is `DERIVED` arithmetic from the patent molar inventory, not an RP-01 value.

### 4.3 Direct TI photoconductor cell/process anchors

US3977018 directly specifies:

- HgCdTe specimen is the anode;
- carbon rod is the cathode;
- electrolyte tank may be plastic-lined stainless steel;
- constant-current operation;
- preferred current density about `0.3 mA/cm²`;
- preferred formation voltage about `15 V`;
- preferred duration about `2 min`;
- preferred resulting oxide approximately `800 Å`;
- preferred film appearance uniform deep blue;
- voltage increases as the oxide grows because impedance increases;
- oxide thickness/formation-voltage relationship was reported reproducible for the preferred electrolyte family.

These form branch identity:

`P25A-TI-PC-CARBON-TRANSFER`.

They are not `DIRECT-RP01`.

### 4.4 Important restriction on the 2-min value

The same primary disclosure shows electrolyte-dependent electrochemistry and film dissolution. Therefore `~2 min` is not a universal endpoint.

P25/P25A release shall use the complete state vector:

`{J, I, A_exposed, V(t), Q/A, bath state, film thickness, film uniformity, interface state}`.

A run is not accepted solely because 2 min elapsed.

---

## 5. Later explicit horizontal-cell apparatus — TI US5036376A

US5036376A supplies unusually concrete cell architecture:

- two-electrode Teflon cell;
- HgCdTe slice horizontal;
- cleaned HgCdTe surface as anode;
- anode contact by etched tungsten or titanium probe;
- circular platinum cathode;
- tank may be Teflon or polypropylene;
- example electrolyte `0.1 M KOH in 10% water / 90% ethylene glycol`;
- electrolyte not stirred;
- bath about room temperature;
- constant-current supply;
- voltage and anodization time recorded continuously;
- example 20 mm × 5 mm slice;
- example current density about `350 µA/cm²`;
- example x≈0.20 material, 15 min -> approximately 600 Å oxide.

Branch identity:

`P25A-TI-LATER-PT-HORIZONTAL-TRANSFER`.

### Critical restriction

Do **not** combine:

- the US3977018 carbon-rod cathode;
- the US5036376 circular Pt cathode;
- one patent's contact geometry;
- another patent's duration/thickness;

and describe the result as a published recipe.

Cathode material/geometry, anode-contact topology and sample orientation are cell coordinates requiring either one-source branch fidelity or explicit local qualification.

---

## 6. Why P25A does not prescribe the historical 90:10 mixing operation

The primary TI photoconductor patent specifies 90% EG / 10% DI water but the recovered text does not label the ratio basis.

Therefore a local executable recipe must choose and name one mathematical branch, for example:

### `P25A-LOCAL-VV-*`

`V_EG / V_solvent = 0.900`  
`V_H2O / V_solvent = 0.100`

with the final electrolyte-volume convention stated explicitly.

### `P25A-LOCAL-WW-*`

`m_EG / m_solvent = 0.900`  
`m_H2O / m_solvent = 0.100`.

These are different local chemistries. Neither may be relabeled as the original TI or UWA preparation basis unless source evidence closes that identity.

### Required local electrolyte record

For any branch record:

- KOH supplier/product/lot;
- KOH certified assay and basis;
- EG supplier/product/lot/purity/water specification;
- DI-water source/resistivity;
- chosen EG:H2O mathematical definition;
- actual delivered masses/volumes;
- method establishing final batch mass/volume;
- calculated KOH molarity;
- measured conductivity/pH where useful and method;
- preparation order;
- preparation temperature;
- batch age/storage/reuse.

---

## 7. Cell branch must be frozen before first device run

A local P25A branch shall have a dimensioned cell record containing:

### Vessel
- material;
- inner dimensions;
- bath volume;
- liquid depth;
- cover state;
- temperature measurement location.

### Anode/specimen
- HgCdTe ID and orientation;
- horizontal/vertical/other orientation;
- exposed top area;
- exposed sidewall area;
- exposed backside area;
- masked area;
- total electrochemically exposed area `A_exposed`;
- area determination method and uncertainty;
- electrical-contact material;
- contact location;
- contact area exposed to electrolyte or isolated from it.

### Cathode
- material;
- geometry;
- dimensions;
- exposed area;
- anode-cathode separation;
- relative orientation/alignment.

### Fixture
- holder material;
- masking material;
- chemical compatibility;
- bubble-trapping risk;
- photograph/drawing revision.

A generic statement such as `two-electrode KOH cell` is not sufficient for `LOCAL-BRANCH-FROZEN`.

---

## 8. Current density requires electrochemical area

For a selected current density `J`:

`I_command = J × A_exposed`.

`A_exposed` is the semiconductor area participating in the electrolyte/electrode process, not automatically die footprint or mesa-top area.

Record:

- nominal area;
- measured dimensions;
- sidewall/backside inclusion rule;
- masking leakage/creep;
- uncertainty in `A_exposed`;
- resulting uncertainty in `J` at fixed current.

At fixed current, a 10% error in electrochemical area creates a 10% error in nominal current density.

The current-source setpoint is therefore not portable without the cell/area definition.

---

## 9. First local qualification center

Where no institution-specific prior HgCdTe anodization branch exists, the strongest literature-grounded **qualification center** is the TI photoconductor branch:

- electrolyte family: `0.1 M KOH / 90% EG / 10% DI water`;
- HgCdTe as anode;
- carbon counter-electrode candidate if following the TI-PC branch;
- static/unstirred condition as a controlled local starting state, while preserving source-specific agitation evidence;
- recorded room/bath temperature;
- `J ≈ 0.30 mA/cm²`;
- continuous `V(t)` acquisition;
- expected transfer-center formation voltage near `15 V`;
- independent oxide-thickness target near `80 nm`;
- deep-blue/uniform color only as an auxiliary observable.

This is `LOCAL-QUALIFICATION-CENTER / PRIMARY-TI-PC-ANCHORED`, not RP-01 historical identity.

### Do not release from controller resemblance

The local branch must demonstrate:

1. repeatable `V(t)` fingerprint;
2. oxide thickness/uniformity;
3. acceptable starting-surface dependence / P28 handoff;
4. electrical/interface behavior;
5. P08 oxide-clear compatibility;
6. P09 contact/TLM compatibility;
7. P10/P12 detector electrical/noise behavior;
8. stability through relevant processing/thermal history.

---

## 10. Required V(t) and charge observables

For every qualification run retain the raw voltage trace and derive:

- `V0`;
- induction time `t_ind`, if present;
- criterion used for `t_ind`;
- time to reference voltages;
- growth-region `dV/dt` over a defined interval;
- terminal voltage;
- current stability;
- total time;
- `Q = ∫I dt`;
- `Q/A_exposed`;
- voltage excursions/noise;
- compliance events.

The x≈0.30 Janousek/Carscallen lineage shows that the induction/dissolution-precipitation stage depends on current density, mass transport and starting surface. Therefore an anomalous early V(t) trajectory is process information, not a nuisance to be discarded.

---

## 11. P28 -> P25 surface-state handoff

P28A establishes that wet-etch completion does not uniquely define the starting surface for anodization.

P25A therefore requires the following clocks and surface coordinates:

- P28 immersion end;
- first quench/rinse start;
- rinse end;
- dry completion;
- cumulative air exposure;
- storage atmosphere;
- P25 immersion time;
- current-on time.

Define:

`t_etch->P25 = t_current-on,P25 - t_etch-end,P28`.

Retain intermediate state information rather than recording only the scalar interval if the surface experiences different liquids/ambient/storage conditions.

No maximum allowed delay is released until P25 V(t), oxide/interface and detector outputs are correlated with that trajectory.

---

## 12. Post-anodization handoff

The exact RP-01 rinse/dry and oxide-to-Mask-2 clock remain `OPEN-HISTORICAL`.

A local branch must explicitly freeze:

- current-off to rinse delay;
- rinse chemistry/sequence;
- dry method;
- post-dry atmosphere/storage;
- time to thickness/interface metrology;
- time to Mask-2 processing;
- time to P08 exposure where relevant.

Do not import buffered-HF, sulfide-conversion, ZnS or other later passivation operations into RP-01 unless the controlled branch explicitly calls for them. RP-01's canonical passivant remains the native anodic oxide.

---

## 13. Qualification ladder

Use the following state progression:

1. `LITERATURE-TRANSFER-ONLY`
2. `ELECTROLYTE-MATHEMATICALLY-DEFINED`
3. `CELL-GEOMETRY-DEFINED`
4. `CURRENT-DENSITY-TRACEABLE`
5. `V(T)-FINGERPRINT-REPEATABLE`
6. `OXIDE-THICKNESS-QUALIFIED`
7. `INTERFACE-FUNCTION-QUALIFIED`
8. `P08-COMPATIBLE`
9. `CONTACT/DETECTOR-CORRELATED`
10. `P25-LOCAL-QUALIFIED`

Only after steps 2–4 are complete may P16A R15 be considered for `LOCAL-BRANCH-FROZEN` first-build execution status. Later stages are required for process release.

---

## 14. P16A readiness consequence

Round 37 closes a **methodological and source-definition gap**, not the physical implementation gap.

Current project state remains:

`R15 = OPEN-CHOICE`.

To move R15 to `LOCAL-BRANCH-FROZEN`, an actual laboratory must instantiate at minimum:

- electrolyte branch and ratio basis;
- reagent products/lots/assays;
- cell/vessel revision;
- anode-contact method;
- cathode material/geometry;
- measured `A_exposed`;
- selected `J` and current;
- bath temperature/agitation state;
- endpoint/V(t)/charge recording;
- rinse/dry/handoff branch.

P25A existing in the repository is not itself evidence that those choices have been made.

---

## 15. Source/recovery state after Round 37

### Directly useful primary sources

1. P. C. Catagnus and C. T. Baker, Texas Instruments, US3977018, *Passivation of mercury cadmium telluride semiconductor surfaces by anodic oxidation*.
2. US5036376A, *Passivation oxide conversion*, for explicit later HgCdTe horizontal-cell apparatus transfer.
3. Janousek/Carscallen x≈0.30 anodic-oxidation lineage already controlled by P02B.

### Same-UWA historical identity

Still identified but recipe not recovered:

- Musca, Smith, Dell, Faraone, 1999, *Performance and stability of HgCdTe photoconductive devices: A study of contact and passivation technology*;
- Musca, Siliquini, Nener, Faraone, 1995, *Passivation and Surface Effects in Long Wavelength Infrared HgCdTe Photoconductors*.

`NOT-RECOVERED != NONEXISTENT`.

---

## 16. Safety / facility hold point

P25A defines scientific process variables and provenance. KOH, HgCdTe/Cd/Hg-containing waste, electrical equipment and solvent handling require institution-specific chemical-hygiene, waste, ventilation, PPE and electrical-safety controls. No repository process setting overrides local EH&S approval.
