# Source-Traceable Qualification Fabrication and Characterization of an x≈0.30 HgCdTe Photoconductor

## Reference process manual based on the Smith et al. RP-01 architecture

**Integrated manuscript draft:** 0.2  
**Continuity round:** 52  
**Date:** 2026-08-16 America/New_York  
**Status:** `TECHNICALLY-REVIEWED INTEGRATED MANUSCRIPT DRAFT — REFERENCE/QUALIFICATION PROCESS`  
**Physical maturity:** not a production release; not a claim of literal historical reproduction; not a declaration that an unspecified laboratory is ready to execute the process.

---

## Abstract

This manual consolidates a source-traceable qualification route for fabricating and characterizing an approximately x=0.30 HgCdTe photoconductive infrared detector on electrically insulating CdZnTe, using the two-mask blocking-contact architecture reported by Smith et al. (2001). The historical paper directly fixes several important device and process quantities—approximately 9.5 µm active-layer thickness, native anodic oxide near 80 nm, a 4–5 µm Mask-2 photoresist layer with an 80 °C/30 min prebake and 30 min chlorobenzene treatment, a CH4/H2 reactive-ion-etch step at 64 sccm total flow, 100 mTorr, 50 W and 60 s, Cr/Au metallization of 30/270 nm, a nine-contact 300×300 µm test structure with 50–400 µm gaps, and detector characterization near 80 K and 10 V/cm. The historical publication does not disclose a complete starting-material growth traveler, Hg-overpressure anneal recipe, wet-mesa formulation, anodization cell construction, photoresist identities, RIE reactor physics, deposition apparatus, singulation method, package construction, or full metrology implementations.

The manual therefore distinguishes four operational classes throughout: **historically fixed values**, **literature-grounded reference qualification centers**, **apparatus/material-dependent quantities that must be instantiated locally**, and **historical-identity details that remain unrecovered**. A reference center is not an executable setpoint by itself. Before an irreversible operation, all required local fields for that operation must be numerically or operationally closed on the executing hardware, the applicable measurement/commissioning gate must be satisfied, and the process traveler must contain no blank or ambiguous instruction. The objective is not to manufacture missing historical facts. It is to provide a coherent qualification-development route that becomes executable when the identified local instantiation and commissioning gates are closed. Historical identity, local execution readiness, and reproducible release are treated as separate claims.

---

# 1. Scope, claims, and execution semantics

## 1.1 Device being reproduced functionally

The reference device is an n-type HgCdTe photoconductor grown by Te-rich liquid-phase epitaxy (LPE) on an electrically insulating CdZnTe substrate. The nominal alloy composition is approximately x=0.30 and the reference active-layer thickness is approximately 9.5 µm. Localized CH4/H2 RIE through contact openings creates a more highly n-type near-contact region intended to reduce minority-carrier loss at the contacts while retaining a two-mask photoconductor geometry.

The completed detector is characterized using measured contact geometry, detector temperature, active-region electric field, optical background, modulation frequency, responsivity, detector-referred noise, and temporal/frequency response.

## 1.2 Claims that must remain distinct

A laboratory using this document can ultimately generate three scientifically different outcomes:

1. **Reference qualification build** — fixed RP-01 quantities are used where known and explicitly labeled transfer/qualification branches are used where historical details are incomplete.
2. **Local reproducible process** — apparatus-specific windows, measurement systems, repeatability, numerical acceptance criteria, change control, detector performance and yield are demonstrated locally.
3. **Historical RP-01 reproduction** — historically critical identities being claimed are independently recovered or otherwise demonstrated, and local substitutions are not silently represented as historical.

A working detector fabricated with a local LPE boat, modern resist, different evaporator, or locally designed package is not automatically a literal reproduction of the 2001 fabrication traveler. Conversely, a clearly identified substitution does not prevent a rigorous local process from becoming reproducible.

## 1.3 Evidence labels

- **[RP01]** — directly reported by Smith et al. (2001).
- **[SAME-LINEAGE]** — directly reported by UWA/Faraone-group work closely related to the reference device/process.
- **[PRIMARY-TRANSFER]** — primary experimental literature or patent from a different but physically relevant HgCdTe/CdZnTe process family.
- **[DERIVED]** — arithmetic or physics calculation from stated quantities and assumptions.
- **[REF-CENTER]** — literature-grounded first qualification center; not a historical RP-01 setpoint unless separately marked [RP01].
- **[LOCAL-CAL]** — apparatus-dependent physical quantity that must be measured/calibrated on the executing hardware.
- **[LOCAL-QUAL]** — local branch, endpoint, or tolerance that must be qualified empirically before routine use.
- **[OPEN-HIST]** — historically unrecovered. Do not infer from generic semiconductor practice.

Repetition does not promote an evidence class.

## 1.4 Irreversible-step preflight rule

A `[REF-CENTER]` is a development coordinate, not permission to execute an irreversible operation.

Before any irreversible process step, the current traveler shall contain, where applicable:

- material/sample/device identity and genealogy;
- procedure and branch revision;
- named reagent/material products and lots;
- mathematically unambiguous concentration/ratio definitions;
- actual apparatus/tool identity and configuration;
- numerical local setpoints or operational endpoints;
- current calibration/acceptance records for the measurements controlling that decision;
- required P36/P36A subsystem acceptance state;
- required upstream measurement gate;
- applicable institutional EH&S authorization;
- planned disposition if an endpoint or process state is missed.

The following are **not executable instructions**:

- `TBD`;
- `appropriate flow`;
- `sufficient Hg` without a defined local functional criterion;
- `standard developer`;
- `typical vacuum`;
- an undefined `%` or liquid ratio;
- a controller setpoint substituted for an uncalibrated physical process temperature;
- a literature center copied into the traveler while a required local apparatus coordinate remains blank.

If a required field remains open, the material is held. The manual may be complete as a qualification document while an unspecified future laboratory remains physically uninstantiated.

## 1.5 Laboratory commissioning hierarchy

The executing laboratory should use P36/P36A to separate:

1. **IQ** — tool identity/configuration/installation;
2. **OQ** — calibrated control/measurement over the required physical envelope;
3. **surrogate PQ** — end-to-end apparatus performance on non-HgCdTe standards/dummies where scientifically meaningful;
4. **HgCdTe residual qualification** — material-specific response that cannot be established with a surrogate.

Surrogate competence does not prove HgCdTe process equivalence.

---

# 2. Reference detector specification

## 2.1 Starting-material and detector anchors

| Quantity | Reference value | Evidence / use |
|---|---:|---|
| HgCdTe alloy composition | x≈0.30 | [RP01] nominal starting material |
| Active-layer thickness | ≈9.5 µm | [RP01] |
| Starting conductivity | n-type | [RP01] |
| Electron concentration | ≈9.8×10^14 cm^-3 | [RP01] supplier value; measurement temperature not disclosed |
| Electron mobility | ≈4.0×10^4 cm²/V·s | [RP01] supplier value; measurement temperature not disclosed |
| Substrate | electrically insulating CdZnTe | [RP01] |
| Native anodic oxide | ≈800 Å = 80 nm | [RP01] |
| RIE-converted electron density | ≈2.0×10^15 cm^-3 | [RP01], explicitly averaged over the converted thickness; depth-coupled quantity |
| RIE-converted mobility | ≈3.3×10^4 cm²/V·s | [RP01] converted-state transport result |
| Cr thickness | 300 Å = 30 nm | [RP01] |
| Au thickness | 2700 Å = 270 nm | [RP01] |
| Contact size | ≈300×300 µm | [RP01] |
| Contact gaps | 50–400 µm in 50-µm increments | [RP01] |
| Specific contact resistivity | ≈9×10^-4 Ω·cm² at 80 K | [RP01] TLM result |
| Canonical detector temperature | 80 K | [RP01] characterization state |
| Canonical electric field | 10 V/cm | [RP01] noise/spectral state |
| Spectral modulation frequency | 1 kHz | [RP01] |
| Stated FOV | 60° | [RP01]; full-angle vs half-angle and physical aperture geometry remain open |
| Detector-response cutoff | ≈4.4 µm | [RP01]; exact cutoff convention not recovered |
| D* near 4 µm | ≈2×10^11 Jones | [RP01] |
| Quantum efficiency | ≈70% | [RP01] |
| 300-K/60° background photon flux | ≈1×10^15 cm^-2 s^-1 | [RP01] |
| 1/f knee | ≈3 kHz | [RP01] representative device |
| High-frequency g-r noise ASD | ≈24.5 nV/√Hz | [RP01]; not automatically the 1-kHz noise |

RP-01 Figures 3, 5, 6 and 7 are tied to the **same representative device**. The exact contact pair/gap used for those performance figures remains [OPEN-HIST]. New measurements should therefore preserve same-device/contact/state identity across responsivity, noise and D* wherever physically possible.

## 2.2 Useful electrical consistency quantities

Using `n=9.8×10^14 cm^-3`, `mu=4.0×10^4 cm²/V·s`, elementary charge `q`, and a one-carrier Hall-factor-one screening model:

`rho = 1/(q n mu) ≈ 0.15922 ohm·cm`  [DERIVED]

For `t=9.5 µm`:

`R_sheet = rho/t ≈ 167.60 ohm/square`  [DERIVED]

The one-carrier Hall coefficient magnitude is:

`|R_H| = 1/(q n) ≈ 6.369×10^3 cm^3/C`  [DERIVED]

For `W≈300 µm` and `E=10 V/cm`, ideal uniform bulk current is approximately:

`I ≈ E W t / rho ≈ 1.79 mA`  [DERIVED]

These quantities are consistency/instrument-sizing checks, not directly published detector operating currents or release tolerances.

---

# 3. Safety, facility, and execution boundary

Hg, Cd-containing materials, bromine, concentrated HBr, hydrogen, methane, vacuum systems, RF plasma systems, high-temperature sealed ampoules, organic solvents including chlorobenzene, cryogens, and metal-deposition systems require the executing institution's formal EH&S controls. This manual does not substitute for local chemical-hygiene, hazardous-gas, pressure-vessel, flammable-gas, vacuum, cryogenic, electrical/RF, or waste-management procedures.

Before physical execution, the laboratory shall identify and approve:

- Hg/Cd containment, exposure monitoring, spill response, and waste streams;
- Br2/HBr-compatible hood, storage, secondary containment, and waste route;
- H2/CH4 gas cabinets, leak detection, purge/interlock system, and exhaust;
- sealed-ampoule and hot-zone handling controls;
- RIE RF/high-voltage and vacuum safety;
- metal-deposition source and vacuum-system safety;
- chlorobenzene/solvent controls;
- LN2/cryostat oxygen-deficiency and pressure-relief controls.

No process value in this manual constitutes authorization to operate hazardous equipment.

---

# 4. End-to-end process flow

The reference qualification sequence is:

`CdZnTe receipt/qualification`
`-> final pre-LPE surface`
`-> Te-rich x≈0.30 LPE`
`-> as-grown FTIR + Hall`
`-> Hg-rich low-temperature anneal`
`-> post-anneal FTIR + Hall`
`-> Mask 1`
`-> wet mesa isolation`
`-> native anodic oxide`
`-> Mask 2 + chlorobenzene profile`
`-> localized CH4/H2 RIE`
`-> Cr/Au deposition`
`-> lift-off + dimensional/TLM verification`
`-> bare-device DC/optical/noise/dynamic baseline`
`-> singulation`
`-> die attach/interconnect/optical package`
`-> cryogenic package verification`
`-> final responsivity/noise/D*/temporal characterization`.

At every irreversible edge, apply Section 1.4. Record material genealogy, procedure revision, local instantiated branch, actual traces/setpoints, deviations, and the corresponding measurement gate.

---

# 5. CdZnTe substrate and final pre-LPE surface

## 5.1 Reference substrate family

RP-01 specifies only an insulating CdZnTe substrate. The strongest current near-composition LPE transfer center is **Cd0.96Zn0.04Te, (111)B**. This is the preferred first screening family when no stronger matched local evidence exists. [PRIMARY-TRANSFER / REF-CENTER]

Do not label 4% Zn, (111)B polarity, any particular miscut, or any substrate dimensions as direct RP-01 facts.

## 5.2 Incoming qualification record

Record for each substrate:

- supplier, lot/ingot, nominal Cd/Zn/Te composition;
- composition certificate and method;
- measured lattice parameter or independently verified Zn fraction where available;
- surface plane and A/B polarity;
- miscut magnitude and azimuth;
- dimensions/thickness;
- electrical-isolation/resistivity information;
- HRXRD rocking curve and curve shape;
- IR inclusion/precipitate map;
- EPD or equivalent defect metric on representative material;
- trace impurities where available, especially electrically active contaminants such as Cu;
- polish history, roughness, scratches, chips, warp/flatness.

Historical scales near `EPD~5×10^4 cm^-2` and `~25 arcsec` rocking-curve width are transfer references, not released limits.

## 5.3 Final-surface family

The strongest practical Te-rich LPE transfer source uses a brief **2–3% Br2 in methanol** treatment on (111)B CdZnTe followed by rapid loading into the graphite boat. [PRIMARY-TRANSFER]

The recovered source does not close:

- bromine percentage basis;
- exact exposure time beyond `a few seconds`;
- bath temperature/agitation;
- rinse/dry sequence;
- removed depth;
- maximum clean-to-load delay.

### Required local instantiation

Create an unambiguous local recipe ID, for example `CZT-BRMEOH-VV-*` or `CZT-BRMEOH-WW-*`, and mathematically define the bromine concentration. Record reagent lots, bath temperature/age, sample area, immersion time, agitation, rinse, dry, removed depth, roughness, and all timestamps.

Define:

`Delta t_clean-load = t_boat_load - t_final_etch_end`.

No universal maximum is assigned. Qualify the allowed delay by downstream LPE morphology/interface quality, P06 spatial uniformity, and P05 transport.

## 5.4 Substrate acceptance before LPE

Proceed only when:

- identity/orientation/polarity are unambiguous;
- no crack or inclusion intersects the intended active region;
- electrical isolation is adequate for the intended device geometry;
- the selected final-surface recipe is fully defined and executed under its local ID;
- no visible residue/particle/surface damage remains;
- clean-to-load history is recorded;
- the supporting wet-chemistry/dimensional metrology capability satisfies the applicable P36A gate.

---

# 6. Te-rich horizontal-slider LPE growth

## 6.1 Composition center

Use the Honeywell x≈0.29 tie-line center:

`x_L = 0.082`  
`y_L = 0.810`  
`T_L = 507 °C`  
`x_S ≈ 0.29`.

For `(Hg_(1-xL) Cd_xL)_(1-yL) Te_yL`, the authoritative project mass fractions are:

- `w_Hg = 0.2497382358`
- `w_Cd = 0.01250164993`
- `w_Te = 0.7377601143`.

Use atomic weights Hg=200.59, Cd=112.414, Te=127.60 g/mol. [DERIVED]

For any **locally established** total growth-charge mass `M_charge`:

`m_Hg = 0.2497382358 M_charge`

`m_Cd = 0.01250164993 M_charge`

`m_Te = 0.7377601143 M_charge`.

Recalculate realized `x_L` and `y_L` from the actual weighed masses. Preserve full balance resolution, especially for Cd.

**Do not infer `M_charge` by substrate-area scaling or by copying another laboratory's ~4.8-g charge.** Total charge is an apparatus coordinate determined by measured well geometry, usable hot volume/meniscus, overlap, freeboard, containment, source depletion, and wipe/separation behavior. [LOCAL-CAL]

## 6.2 Boat/furnace architecture

Use a covered high-purity graphite horizontal-slider architecture derived from the Honeywell lineage:

- base/stator with substrate recess;
- moving slider/carrier;
- capped Te-rich growth-solution well;
- auxiliary Hg-containing source recess;
- close graphite cover;
- Hg-distribution grooves/moats around the growth region;
- horizontal quartz furnace tube;
- N2 purge followed by flowing H2;
- controlled slider actuation for contact/separation;
- one defined residual-melt wipe-off architecture.

Two Honeywell-derived wipe-off families may be qualified separately:

1. CdTe pieces retained in a dedicated wipe-off well;
2. scribed CdTe apron adjacent to the growth substrate.

Do not merge them under one recipe identity.

Record complete boat dimensions, graphite grade, clearances, recess depth, well dimensions/volume, overlap, plug displacement, Hg-source geometry, cover fit, actuator travel, hot-motion behavior, and position repeatability. [LOCAL-CAL]

## 6.3 Source synthesis

The exact x≈0.30 historical source-synthesis schedule is unrecovered. A practical Te-rich slider transfer branch demonstrates:

- 6N elemental starting materials;
- sealed evacuated quartz ampoule synthesis;
- 700 °C for 8 h;
- post-synthesis grinding and mixing.

Those conditions are [PRIMARY-TRANSFER], not direct RP-01.

For a local xL=.082/yL=.810 branch, define and freeze:

- elemental purities/lots;
- total synthesis batch mass;
- loading order;
- ampoule material/volume;
- evacuation/backfill state;
- ramp/soak trajectory;
- agitation/rocking if used;
- cooldown;
- comminution/mixing;
- aliquot mass placed in each growth well;
- auxiliary Hg-source identity/mass/geometry;
- source reuse count.

## 6.4 Atmosphere and thermal calibration

The direct Honeywell sequence is:

1. load substrate, growth charge, auxiliary Hg source, cap and cover;
2. place boat in the quartz tube;
3. thoroughly purge with N2;
4. establish H2 flow;
5. heat/equilibrate above or near liquidus according to the selected local branch;
6. cool/supercool to the intended contact state;
7. translate melt over the substrate.

N2 flow/time, H2 flow, gas purity/dew point/O2 criterion, furnace offsets, axial/transverse gradients, and actual solution/substrate temperatures are [LOCAL-CAL]. Controller display temperature is not assumed equal to melt temperature.

P36 AT-LPE commissioning shall establish geometry, hot motion, thermal field, gas delivery and synchronized data capture before a local branch is called executable.

## 6.5 First qualification thermal/contact center

Use `T_L=507 °C` as the tie-line anchor. A **500 °C measured contact-region state**, corresponding nominally to about 7 K supercooling, is a useful [REF-CENTER], not a historical release condition.

Published Te-rich LPE evidence brackets contact times over roughly 0.25–10 min in one experimental family; a Honeywell apparatus example extends to about 30 min. These are separate branches and shall not be averaged into a fictitious historical time.

### Mandatory local values before an LPE run

Before first irreversible contact, the traveler shall contain at minimum:

- boat revision and measured well/overlap geometry;
- absolute `M_charge` and actual elemental masses;
- auxiliary Hg-source identity/inventory;
- actual N2/H2 flow states and gas-quality criteria;
- corrected solution/substrate temperature measurement method;
- above-liquidus/equilibration criterion;
- selected contact temperature/supercooling;
- numerical contact-time coordinate or explicit measured endpoint;
- selected wipe-off branch;
- separation/cooldown trajectory;
- abort/hold criteria.

`500 °C / literature seconds-to-minutes` without these fields is not an executable recipe.

## 6.6 Required LPE outputs

After every growth run record:

- whole-surface image and usable-area map;
- residual melt/droplet area;
- pinholes/voids/scratches/terraces;
- P06 thickness/composition map;
- HRXRD/defect metric where available;
- matched P05 transport coupon;
- charge/source mass history and source-use number.

The qualification objective is an approximately x=0.30, ~9.5-µm usable layer with sufficiently uniform morphology and transport to enter anneal/device fabrication. Do not accept a run solely because one optical edge point appears correct.

---

# 7. As-grown material metrology

## 7.1 FTIR mapping

Use nondestructive IR transmission on the intact parent piece before subdivision where practical.

Recommended qualification capability:

- spectral range approximately 500–5000 cm^-1 or wider as needed;
- spectral resolution ≤4 cm^-1 for qualification work unless sensitivity analysis justifies otherwise;
- minimum 9-point spatial map; 5×5 preferred where sample size permits;
- background/reference acquisition with instrument state recorded;
- full-spectrum fitting preferred over single-edge-point interpretation;
- independent physical thickness cross-check.

The Hansen relation for x=0.30 at 80 K gives a band-gap-equivalent wavelength near 5.09 µm. This is **not** the same quantity as the reported ~4.4-µm detector-response cutoff. Do not use detector cutoff and band-gap wavelength interchangeably.

Report the spectral-edge definition used. `lambda_50` may be a QC descriptor but is not a universal composition identity.

P36 AT-FTIR shall establish spectral calibration, photometric repeatability, map registration and an independent thickness reference.

## 7.2 Hall / van der Pauw

Use a dedicated material-control descendant unless Hall contacts and processing have been demonstrated compatible with subsequent device fabrication.

For initial qualification:

- four small perimeter ohmic contacts;
- symmetric current/field reversals;
- nominal currents 10, 30, and 100 µA with self-heating checks;
- initial B grid: 0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T;
- extend toward ±2 T where available for multicarrier discrimination;
- 80 K mandatory for the first direct comparison; 300 K recommended.

Use antisymmetrized Hall voltage and van-der-Pauw reciprocity/reversal checks. A practical project redundancy gate is:

- ≤3% discrepancy: pass;
- 3–5%: conditional/review;
- >5%: fail/repeat or escalate.

Near p/n conversion, do not force a one-carrier density through a Hall-sign cancellation region. Classify `N-LIKE`, `P-LIKE`, or `TRANSITION/MULTICARRIER` and use variable-field tensor/multicarrier analysis where required.

---

# 8. Hg-overpressure anneal

## 8.1 Objective

Drive the as-grown layer into a stable lightly n-type state while preserving optical composition, thickness, morphology, and detector-relevant lifetime/interface behavior.

The reference neighborhood is:

- n-type;
- n≈9.8×10^14 cm^-3;
- µ≈4.0×10^4 cm²/V·s;
- x≈0.30;
- thickness ≈9.5 µm.

The supplier measurement temperature for the historical n and µ values is unknown, so every local comparison shall state measurement temperature and transport model.

## 8.2 Preferred first anneal architecture

Use a sealed or otherwise controlled Hg-rich enclosure in which sample temperature `T_s(t)` and Hg-reservoir/source temperature `T_Hg(t)` are independently known. A true isothermal Hg-saturated branch is acceptable if equivalence between sample and reservoir state is calibrated.

Record:

- ampoule/enclosure dimensions and free volume;
- sample/source positions;
- Hg source identity, purity, mass, geometry, reuse history;
- evacuation/backfill and leak-check method;
- sample and reservoir thermometry;
- full `T_s(t)` and `T_Hg(t)`;
- dwell, cooldown, and condensation-control trajectory.

`250 °C in Hg` is not a complete recipe without the boundary condition and thermal path.

## 8.3 First qualification center

Use approximately:

- `T_s ≈ 250 °C`;
- Hg-saturated, isothermal-like boundary;
- `t ≈ 1 h`.

This is [REF-CENTER] anchored by primary low-temperature Hg-rich anneal evidence, not direct RP-01 history.

Near-composition LPE evidence supports 250–300 °C as a useful n-type conversion region without apparent composition change, while ~400 °C can produce interface-region composition changes. Begin below 300 °C unless a separate defect-engineering objective justifies otherwise.

## 8.4 Anneal qualification sequence

1. Measure pre-anneal P05/P06 state at registered locations.
2. Execute the selected fully instantiated local branch near the 250 °C/1 h Hg-rich center.
3. Cool under a recorded boundary condition; do not use `furnace cool` as the only description.
4. Repeat P05 and P06.
5. If stably n-like but materially above/below the desired carrier-state region, map time at fixed `T_s`/Hg boundary before changing multiple coordinates.
6. Useful local time-screen coordinates are 0.5, 1, 2, and 4 h; only 1 h is the direct reference center.
7. After time sensitivity is known, map `T_s`; only then map Hg chemical potential (`T_Hg` relative to `T_s`) if required.

P36 AT-ANN shall establish enclosure geometry, dual-temperature mapping, dwell stability and enclosure integrity before the branch is treated as executable.

## 8.5 Anneal acceptance

Retain a condition only when:

- Hall state is stably n-like under a valid transport model;
- density/mobility lie in the selected local target region;
- P06 shows no unacceptable optical/composition shift;
- surface morphology is preserved;
- no Hg/Te deposit or handling damage invalidates the surface;
- repeated matched coupons show a consistent response.

`n-type` alone is insufficient.

---

# 9. Mask 1 and wet mesa isolation

## 9.1 Mask-1 resist strategy

RP-01 does not identify the Mask-1 resist. Do not copy the Mask-2 chlorobenzene process into Mask 1.

The strongest product-identified Br2/HBr HgCdTe transfer candidate is **AZ4620**, demonstrated at 3 µm in another deep HgCdTe mesa process. A thick positive novolak/DNQ-family resist is therefore the first screening family. [REF-CENTER]

The actual product, spin, thickness, exposure dose, developer, bake, strip and mask bias are [LOCAL-QUAL].

Before etch record:

- resist product/lot;
- dispense/spin acceleration/speed/time;
- measured thickness map;
- bake;
- exposure tool/wavelength/dose;
- developer identity/concentration/time;
- developed CD/profile;
- pinholes/scum/adhesion.

## 9.2 Wet-etch chemistry reference center

The strongest quantitative near-composition transfer is:

`nominal 2% Br2 in 3:1 EG:HBr` near approximately 21 °C.

Transfer behavior at/near 21 °C includes:

- vertical rate ≈2.78 µm/min;
- run/process variation of order ±26%;
- anisotropy `A = 1 - R_L/R_V ≈ 0.63` with ~±11% variation;
- best reported RMS roughness near 2 nm;
- etch rate approximately doubling for each +10 °C over the studied regime;
- lower-temperature etching improving geometric/photoresist control.

These are [PRIMARY-TRANSFER], not x=0.30 RP-01 specifications.

## 9.3 Formulation ambiguity — mandatory local definition

The primary source does **not** close:

- the basis of `2% Br2`;
- the mathematical preparation basis of `3:1 EG:HBr`;
- HBr stock assay;
- actual historical agitation.

The executing laboratory shall create an explicit local recipe, such as:

- `MESA-WW-*`: bromine mass fraction explicitly defined;
- `MESA-VV-*`: bromine volume fraction explicitly defined;
- another branch with a complete mathematical definition.

Record Br2/EG/HBr supplier, lot, purity/assay, delivered masses/volumes, vessel, batch age, temperature, open time, agitation, sample loading, and reuse history.

Do **not** write `2% Br2` on a traveler without its definition. P36A AT-WET-01 makes this a pre-execution gate.

## 9.4 Etch-rate calibration before device etch

Before etching detector material through the active layer:

1. prepare matched witnesses using the actual Mask-1 process;
2. measure starting thickness/topography;
3. execute several short etch times spanning the expected range;
4. measure vertical depth, lateral undercut, resist loss/retreat, roughness and profile;
5. determine current local `R_V`, `R_L`, and mask bias;
6. use electrical isolation and measured geometry as the final endpoint, not nominal time alone.

At the transfer rate of 2.78 µm/min, 9.5 µm corresponds to about 3.4 min [DERIVED], but **3.4 min is not an uncalibrated device etch recipe**.

## 9.5 Mesa endpoint and handoff

Record actual bath temperature, time, agitation, depth, top/base CD, undercut, sidewall morphology, isolation resistance/leakage, rinse/quench/dry, and the clock to anodization.

Proceed only when the mesa is electrically isolated, passivation-ready, and inside the locally qualified geometry/interface window.

---

# 10. Native anodic-oxide passivation

## 10.1 Historical target

RP-01 uses a native anodic oxide approximately **80 nm** thick after wet mesa delineation. [RP01]

The strongest photoconductor-specific transfer branch uses:

- `0.1 M KOH` in stated `90% ethylene glycol / 10% DI water`;
- HgCdTe as anode;
- carbon-rod cathode;
- constant current density ≈0.30 mA/cm²;
- formation voltage near 15 V;
- duration near 2 min;
- oxide near 800 Å;
- uniform deep-blue film as an auxiliary visual indicator.

This is [PRIMARY-TRANSFER / REF-CENTER], not the recovered UWA recipe.

## 10.2 Electrolyte definition

The primary disclosure specifies 0.1 mole KOH per 1 L of the stated mixed solvent. With pure KOH molecular weight 56.1056 g/mol:

`m_KOH,pure = 5.61056 g per 1.000 L nominal branch`  [DERIVED]

For certified KOH assay `a`:

`m_KOH,reagent = 5.61056/a`.

The recovered text does not explicitly close whether the 90:10 EG/water ratio is v/v or w/w. A local recipe shall define one basis mathematically and preserve that identity.

P36A AT-ANO-01 treats an undefined solvent-ratio basis as a failed preflight state.

## 10.3 Cell/current calculation

Measure electrochemically exposed semiconductor area `A_exposed`, including the explicit rule for exposed sidewalls/backside.

For selected current density `J`:

`I_command = J A_exposed`.

Reference center:

`J ≈ 0.30 mA/cm²`.

Do not reuse an absolute current from another sample geometry.

## 10.4 Required anodization record

Record:

- electrolyte recipe/batch/age;
- vessel and cell geometry;
- anode-contact material/location;
- carbon cathode geometry/separation for the TI-PC transfer branch;
- bath temperature/agitation state;
- `A_exposed` and uncertainty;
- commanded/measured current;
- continuous `V(t)`;
- total time;
- `Q = integral I dt` and `Q/A_exposed`;
- film color/uniformity;
- independent oxide thickness;
- rinse/dry;
- wet-etch-to-anodization and anodization-to-Mask2 clocks.

## 10.5 Acceptance

Do not accept solely at 2 min or 15 V. Retain a local branch only when it gives:

- repeatable `V(t)` fingerprint;
- ~80-nm physical oxide target inside the local metrology/acceptance window;
- good coverage/uniformity;
- acceptable interface/electrical state;
- compatible RIE oxide clearing;
- compatible TLM/contact response;
- acceptable detector electrical/noise behavior.

---

# 11. Mask 2: RIE/contact-window and lift-off resist

## 11.1 Direct historical fingerprint

Keep the following fixed for first RP-01-oriented transfer:

- resist thickness: **4–5 µm** [RP01];
- prebake: **80 °C / 30 min** [RP01];
- chlorobenzene treatment: **30 min** [RP01];
- then pattern, develop, water rinse [RP01];
- resist remains through RIE and subsequent Cr/Au deposition/lift-off.

Commercial resist, exposure dose/tool, developer, exact chlorobenzene sequence relative to exposure, and lift-off solvent are [OPEN-HIST].

## 11.2 Candidate resist hierarchy

Historical chlorobenzene lift-off evidence strongly supports a positive DNQ/diazo-novolak AZ-type process family.

Useful candidate evidence:

- AZ4110: direct chlorobenzene mechanism evidence but thinner in the cited branch;
- AZ4330/AZ4400/AZ4620 class: direct 4–5-µm thickness evidence in other processes.

The preferred local choice is a currently available positive resist that reproducibly gives a measured 4–5 µm film and a suitable re-entrant profile after the selected RP-01 bake/chlorobenzene branch. Product identity is a local transfer choice, not a historical claim.

## 11.3 Chlorobenzene-order ambiguity

RP-01 wording can be read as:

`bake -> chlorobenzene -> pattern/expose -> develop`,

while historical chlorobenzene lift-off processes also use:

`bake -> expose -> chlorobenzene -> develop`.

If direct source closure remains unavailable, compare both branches on witnesses while holding other variables fixed. Retain the branch giving stable film thickness, clean contact-window opening, RIE-mask survival, sufficient undercut/overhang, and clean 300-nm-total metal lift-off.

Do not label the winning local branch as the historical ordering.

## 11.4 Exposure/development

Determine clearing/exposure response on the actual 4–5 µm film after the chosen bake/chlorobenzene sequence. Use a dose/development matrix and measure:

- resist height;
- top/bottom opening CD;
- undercut/overhang;
- scum;
- oxide compatibility;
- alignment to Mask 1.

Developer shall be product-matched, with product/lot/concentration/time/temperature/agitation and water-rinse method recorded. P36A AT-LITH establishes coating, bake, solvent-treatment, dose and development/profile acceptance before HgCdTe residual qualification.

---

# 12. CH4/H2 RIE blocking-contact formation

## 12.1 Direct controller recipe

Canonical RP-01 RIE condition:

- parallel-plate Plasma Technology reactor;
- gas notation `CH4/5H2`;
- total flow **64 sccm**;
- pressure **100 mTorr**;
- forward RF power **50 W**;
- RF time **60 s**.

These are [RP01].

If `CH4/5H2` is interpreted as a 1:5 flow ratio, candidate individual flows are:

- CH4 = `64/6 = 10.6667 sccm`;
- H2 = `5×64/6 = 53.3333 sccm`.

This split is an interpretive/same-lineage candidate, not a directly stated RP-01 pair of MFC settings. The local traveler shall state the actual adopted gas realization explicitly.

## 12.2 Reactor-equivalence rule

Matching 50 W, 100 mTorr, 64 sccm, and 60 s does not establish equivalent ion energy, flux, plasma density, wall chemistry, residence time, or sample temperature.

Record/calibrate:

- reactor/electrode geometry and RF frequency;
- sample holder/loading;
- CH4/H2 MFC IDs/ranges/calibration;
- base pressure and pressure-gauge state;
- chamber clean/season history;
- forward/reflected power;
- measured dc self-bias or qualified sheath/ion-energy proxy;
- chuck/sample thermal state;
- pressure trace;
- actual gas ratio/total flow.

Forward RF power is an actuator, not a portable ion-energy coordinate.

## 12.3 Oxide clear versus semiconductor exposure

Define experimentally:

- `t_clear` = time required to clear the actual ~80-nm oxide under the local plasma;
- `t_sem = t_RF - t_clear` = direct HgCdTe plasma-exposure time after oxide clear.

Determine `t_clear` on matched anodized witnesses by a short-time calibration. Do not assume all 60 s acts directly on HgCdTe.

## 12.4 Physical, sheet-transport and conversion-depth outputs

Keep distinct:

- `d_etch` — physical HgCdTe recession;
- `N_s` — Hall sheet carrier density when a valid sheet reduction exists;
- `mu_H` — Hall mobility under the selected transport model;
- `d_conv` — independently measured/inferred vertical electrical conversion depth;
- `L_conv` — lateral conversion extent;
- `n_conv = N_s/d_conv` — derived volumetric density only after `d_conv` is justified.

RP-01 reports `n_conv≈2.0×10^15 cm^-3` **averaged over the converted thickness** and `mu≈3.3×10^4 cm²/V·s`. The volume density is therefore depth-coupled; it is not an independent reactor target.

A same-lineage approximately 8-µm conversion-depth result exists under similar conditions, but the exact linkage to the RP-01 volume-density reduction remains historically open. Do not assume `d_conv=8 µm` for a new reactor without measurement.

The controlled blocking-contact state vector shall include at least:

`{R_s, N_s, mu_H, d_conv, L_conv, d_etch, rho_c, blocking_response}`.

Do not tune the plasma solely to reproduce `2.0×10^15 cm^-3`.

If the modified layer and underlying epilayer conduct in parallel, a one-layer Hall reduction may be invalid. Retain variable-field Hall/magnetoresistance and escalate to a multicarrier/multilayer treatment where required.

## 12.5 Functional qualification

Required qualification outputs include:

- oxide clear/recession;
- surface roughness/morphology;
- sheet resistance/conductance;
- variable-field Hall state on dedicated witnesses;
- LBIC or validated equivalent for conversion extent;
- TLM contact response after metallization;
- minority-carrier blocking functional response;
- detector resistance/noise change.

Historical TLM reference:

`rho_c≈9×10^-4 ohm·cm² at 80 K` [RP01].

TLM is a majority-contact metric and does not prove minority-carrier blocking by itself.

## 12.6 LBIC reference validation branch

Same-lineage validation used a patterned ~300×300 µm RIE region, 1.047-µm Nd:YLF CW illumination around 400 mW/cm², and 80-K measurements to reveal a bipolar boundary signature. These values are a validation-reference branch, not mandatory production test settings.

---

# 13. RIE-to-metal transfer and Cr/Au deposition

## 13.1 Surface-transfer clock

Default baseline:

`RIE -> controlled transfer -> Cr deposition`

with no undocumented wet clean, ion mill, UV ozone, or additional plasma clean.

Record:

- RF-off time;
- vent/sample-out time;
- atmosphere and cumulative air exposure;
- metal-tool load/pump start;
- base-accept time;
- Cr start.

Define:

`Delta t_RIE-Cr = t_Cr_start - t_RF_off`.

No universal maximum is assigned; qualify the interval by TLM, interface stability, converted-layer preservation, and detector response.

## 13.2 Deposition method

RP-01 does not state the deposition method. Thermal evaporation is the strongest same-UWA method-family transfer candidate and the preferred first local branch. E-beam or sputtered branches are permissible but separate because bombardment, heating, stress, residual-gas interaction and directionality differ.

## 13.3 Film stack

Deposit, without intentional interlayer oxidation:

1. **30 nm Cr** [RP01];
2. **270 nm Au** [RP01].

Remain under vacuum between layers where the chosen tool permits.

Record:

- tool/method/chamber ID;
- base/process pressure;
- source material/purity/boat/crucible;
- QCM crystal/calibration/tooling factor;
- separate Cr and Au rates/times;
- indicated and independent witness thickness;
- holder/sample temperature;
- source-to-sample geometry/angle/rotation;
- abnormal events.

Do not invent an RP-01 base pressure or Cr rate. Published HgCdTe Au rates around 0.3–1.2 nm/s are screening scales only.

## 13.4 Thermal budget

Use the first transfer as **as-deposited, no intentional post-metal anneal** unless a separate branch is justified. Record actual holder/sample heating. Any post-metal anneal is a new branch requiring remeasurement of contact/interface and detector outputs.

## 13.5 Lift-off

Historical lift-off solvent/time/agitation are unrecovered. Choose a process compatible with the selected resist and Cr/Au stack. Prefer soaking/low mechanical force during initial qualification; ultrasonication is not a default because fragile passivation/contact edges may be damaged.

Accept only when microscopy shows:

- no metal bridges;
- no fencing/ears/flakes;
- no pad delamination;
- no passivation damage;
- clean opening dimensions;
- intact contact pads.

---

# 14. Final geometry and contact-quality verification

## 14.1 Dimensional metrology

For each contact pair record:

- contact IDs;
- actual pad width/length;
- actual gap at multiple positions;
- active conducting width;
- mesa dimensions;
- alignment/clearance;
- optical-aperture overlap where relevant.

Use measured values, not mask CAD, in field and D* calculations. P36A AT-DIM shall establish the lateral/vertical metrology needed at the relevant scales.

## 14.2 TLM

Use the nine-contact geometry with approximately 300×300 µm contacts and gaps 50–400 µm in 50-µm steps.

At the declared temperature/background and low enough excitation to remain ohmic:

1. acquire bidirectional I–V for selected gaps;
2. extract resistance using a consistent regression interval;
3. regress total resistance versus gap/geometry term;
4. obtain sheet/contact terms with uncertainty and residual analysis;
5. report specific contact resistivity with the exact TLM convention.

Reference benchmark:

`rho_c ≈ 9×10^-4 ohm·cm² at 80 K` [RP01].

Retain separate blocking-contact functional evidence.

---

# 15. Bare-device electrical qualification

## 15.1 Canonical operating field

At 80 K, calculate electric field from measured active-region voltage and measured gap:

`E = V_active/L`.

For 10 V/cm, active-voltage targets are:

- 50 µm gap: 0.050 V;
- 100 µm: 0.100 V;
- 150 µm: 0.150 V;
- 200 µm: 0.200 V;
- 250 µm: 0.250 V;
- 300 µm: 0.300 V;
- 350 µm: 0.350 V;
- 400 µm: 0.400 V.

Correct source voltage for lead/contact/series drops when material.

## 15.2 Dark I–V and self-heating

At stabilized ~80 K:

1. acquire symmetric positive/negative low-field sweeps from zero through the intended operating region;
2. record active voltage, current, detector/mount temperature, and power;
3. periodically return to zero to expose drift/hysteresis;
4. establish the approximately ohmic low-field region;
5. characterize field-dependent resistance/sweepout behavior;
6. establish a self-heating criterion using a calibrated local temperature proxy.

Joule power:

`P_J = V_active I`.

A universal allowable mW limit is not assigned because thermal resistance is construction-specific.

Preferred checks include near-zero-power `R(T)` calibration, sufficiently coupled thermometry, and pulse/DC comparison where useful.

---

# 16. Singulation

## 16.1 Historical status

RP-01 does not disclose singulation method or die outline. Treat singulation as a material/device process, not neutral handling.

## 16.2 Preferred first branch

A low-force **wire-saw family** is the strongest directly documented CdZnTe detector transfer branch. Primary evidence includes metallized CdZnTe protected with photoresist, mounted with low-melting wax on graphite, and cut very slowly with stainless-steel wire plus 16-µm BN abrasive slurry. These are [PRIMARY-TRANSFER], not a ready-made RP-01 recipe.

Do not automatically use the associated strong post-cut 5% Br/methanol/5-min damage-removal etch on a completed RP-01-like device; it could materially alter the 9.5-µm active layer, oxide, and contacts.

## 16.3 Qualification method

Define/record:

- die/street geometry and crystal orientation;
- support/protection material;
- tool/wire/blade identity;
- abrasive/coolant;
- motion/feed/pass state;
- tool age/conditioning;
- kerf/position error;
- cleaning/release sequence;
- edge chips/cracks;
- subsurface-damage evidence on witnesses;
- pre/post resistance, noise, and responsivity on selected qualification devices.

Define separately:

- `d_visible` — geometric distance to visible damage;
- `d_functional` — minimum distance shown not to measurably degrade detector function;
- `d_release` — locally released exclusion including uncertainty/margin.

Visible edge quality alone is insufficient.

---

# 17. Cryogenic die attach, interconnect, and package

## 17.1 Historical status

RP-01 does not disclose die attach, carrier, wire, aperture, window, vacuum, or package construction. Package hardware is a local transfer architecture, not a historical process claim.

## 17.2 First attachment branch

Use a **compliant silicone-family** attachment as the first cryogenic mechanical screen because direct HgCdTe evidence showed brittle/glass attachment cracking on deep cooldown while silicone-rubber attachment survived. Historical product names identify the material family, not a modern procurement instruction.

A low-outgassing epoxy may be screened as a separate branch.

## 17.3 Required package record

Record:

- singulated die geometry/edge state;
- carrier/cold-finger material, dimensions, CTE and thermal-data source;
- attachment product/lot/mix ratio;
- dispense quantity;
- bondline thickness/coverage/voiding;
- placement force/tilt;
- cure T/time/atmosphere/trajectory;
- wire/ribbon material/diameter;
- bonder/tool/mode/force/ultrasonic/time/stage temperature;
- aperture, window/filter, shield and physical FOV geometry;
- vacuum/purge/bake history;
- temperature-sensor position.

## 17.4 Package thermal response

Package/bondline thermal poles can occur on millisecond-to-hundreds-of-milliseconds scales in HgCdTe photoconductor assemblies. Characterize package thermal response near operating temperature using a qualified short optical or electrical heating perturbation.

Do not attribute a slow P13 transient to minority-carrier lifetime until package thermal response has been evaluated.

## 17.5 Cryogenic acceptance

After assembly and defined thermal cycles, repeat selected:

- dark resistance/I–V;
- contact/lead resistance;
- P12 noise;
- P11 responsivity;
- P13 dynamic/thermal response;
- edge/crack and bond inspection.

Reject/requalify a package that introduces unacceptable mechanical damage, excess noise, optical loss, electrical drift, or a thermal pole that corrupts the intended measurement band.

---

# 18. Absolute spectral responsivity and optical state

## 18.1 Canonical RP-01 comparison state

Direct historical coordinates:

- T = 80 K;
- E = 10 V/cm;
- stated FOV = 60°;
- modulation/chopping frequency = 1 kHz;
- spectral region covering the full response and the ~4.4-µm reported response edge.

The historical 60° label does **not** document full-angle versus half-angle or the physical aperture dimensions. A 60° full cone (30° half-angle) is consistent with the quoted 300-K photon-flux scale in the current radiometric consistency model, but that is [DERIVED / CONSISTENCY], not historical proof.

For a new measurement:

- preserve `stated 60° FOV` as the historical comparison label;
- separately define the actual aperture/shield/window/source geometry;
- calculate or measure the view factor/projected solid angle;
- state explicitly whether any quoted angle is full cone, half-angle or another convention.

Do not silently replace the historical state with `exact 30° half-angle`.

## 18.2 Measurement architecture

Preferred modern method: substitution/comparison to a calibrated IR transfer detector in the same defined optical reference plane.

For calibrated reference responsivity `R_ref(lambda)` and detector-terminal-equivalent signals:

`P_inc(lambda) = V_ref(lambda)/R_ref(lambda)`

`R_DUT(lambda) = V_DUT(lambda)/P_inc(lambda)`

or:

`R_DUT(lambda) = [V_DUT/V_ref] R_ref(lambda)`

when modulation waveform, frequency, beam geometry, and signal conventions are compatible.

Record:

- source/monochromator/grating/slits/order filters;
- wavelength calibration and residual;
- spectral bandwidth/line shape;
- purge/vacuum state;
- reference detector/certificate;
- reference/DUT positioning and aperture;
- beam map/uniformity;
- chopper waveform/duty/frequency;
- lock-in harmonic, phase, RMS/peak convention;
- gain/filter transfer;
- detector current/power/temperature;
- window/filter/package transmission state.

Use the same modulation and signal-amplitude convention for reference and DUT whenever possible so waveform factors cancel.

## 18.3 Spectral safeguards

- use order-sorting filters;
- test stray light beyond cutoff;
- purge/evacuate important H2O/CO2 path lengths;
- characterize signal linearity at the actual irradiance/background state;
- do not quote cutoff more precisely than wavelength calibration and edge-definition uncertainty;
- do not equate detector-response cutoff to the Hansen band-gap-equivalent wavelength.

---

# 19. Noise, NEP, and specific detectivity

## 19.1 Canonical comparison state and same-device rule

For direct RP-01 comparison:

- T=80 K;
- E=10 V/cm;
- stated 60° FOV/background state;
- same representative device for the performance chain;
- evaluate detector noise at the declared D* frequency, especially 1 kHz for the canonical spectral measurement.

P12C closes that RP-01 Figures 3, 5, 6 and 7 correspond to the same representative detector. Therefore a new D* closure should lock, at minimum:

`{device, contact pair, measured gap, measured width, T, E, package, FOV/background, loading, frequency convention}`

between responsivity and noise measurements, unless a measured correction is explicitly applied.

`same wafer/process` is not a substitute for `same device/state`.

The historical ~24.5 nV/√Hz value is the reported high-frequency/g-r level. Since 1 kHz is below the ~3-kHz 1/f knee, **do not substitute 24.5 nV/√Hz as the 1-kHz noise unless evidence establishes that convention/value at 1 kHz.**

## 19.2 PSD/ASD definitions

Voltage-noise PSD:

`S_v(f)` in V²/Hz.

ASD:

`e_n(f)=sqrt(S_v(f))` in V/√Hz.

Integrated RMS noise:

`V_rms = sqrt(integral S_v(f) df)`.

For locally white noise through equivalent noise bandwidth `B`:

`V_rms ≈ e_n sqrt(B)`.

Record FFT/window/ENBW or analyzer normalization so a displayed line amplitude is never confused with ASD.

Historical knee comparison remains the intersection of the low-frequency 1/f trend and the high-frequency g-r level; do not silently replace that with a -3-dB or Lorentzian-corner definition.

## 19.3 Electronics subtraction

When independent and referred to the same input node:

`S_det = S_meas - S_elec`

`e_det = sqrt(e_meas^2 - e_elec^2)`.

Do not subtract ASDs linearly. If electronics noise is a large fraction of measured noise, propagate the subtraction conditioning/uncertainty.

Validate the electrical chain with known resistor Johnson noise where the source-impedance model is applicable:

`e_J = sqrt(4 k_B T R)`.

Do not subtract a Johnson term blindly from a biased nonequilibrium detector.

## 19.4 NEP and D* — explicit area/power convention

At the same wavelength, frequency, field, temperature, background, loading and package state:

`NEP(lambda,f) = e_det(f)/R_v(lambda,f)`.

Define explicitly:

- `A_Dstar` — detector normalization area used in the D* definition;
- `P_inc` — optical power incident under the stated radiometric geometry;
- any aperture/beam/irradiance area used to derive `P_inc`.

Then:

`D*(lambda,f) = R_v(lambda,f) sqrt(A_Dstar) / e_det(f)`

and:

`D* = sqrt(A_Dstar)/NEP`.

`A_Dstar` and the optical beam/aperture area need **not** be literally the same physical area if the measurement equation defines them separately. What is prohibited is silently mixing conventions.

If incident power is derived from irradiance using a geometry/area that is shared or correlated with `A_Dstar`, retain that covariance. Define:

`gamma_A = partial ln(P_inc)/partial ln(A_Dstar)`

under the stated measurement convention. The first-order D* sensitivity to that area coordinate is:

`S_Dstar,A = 0.5 - gamma_A`.

Thus the familiar `+0.5` area exponent applies only when `P_inc` is independent of the same area coordinate.

If responsivity and noise share the same calibrated linear gain path at the same frequency/loading, common gain uncertainty may cancel; document the correlation rather than double-counting it.

## 19.5 Noise diagnostics

Report separately:

- fitted 1/f exponent;
- historical-comparison knee;
- high-frequency/g-r plateau ASD;
- detector ASD at the D* frequency;
- narrowband interference lines;
- bias dependence;
- blocked versus background-loaded states;
- stationarity/drift;
- background-temperature/aperture stability where relevant.

Historical comparison targets are roughly 3 kHz knee and 24.5 nV/√Hz high-frequency g-r level.

---

# 20. Temporal/frequency response and lifetime

## 20.1 Historical boundary

RP-01 does not publish a direct detector lifetime/frequency-response curve. Do not infer lifetime from the use of 1-kHz optical chopping.

Same-UWA x≈0.30 transient-photoconductive work provides a historical measurement branch:

- 1.047 µm pulsed laser;
- 25 ns optical pulses;
- 1 kHz repetition;
- ~77 K under vacuum;
- AC-coupled amplification;
- HP54522A oscilloscope;
- typically 128 waveform averages;
- 500 samples at 20 ns spacing;
- non-exponential diffusion/recombination model outperforming a single exponential for the analyzed dataset.

These are measurement-lineage anchors, not RP-01 lifetime targets.

## 20.2 De-embedding

In a simple multiplicative frequency-domain representation:

`H_meas = H_source H_optics H_detector H_bias H_preamp H_cable H_instrument`

Package thermal behavior may require a separate coupled/additive model rather than being forced into a multiplicative block.

Only report detector `f_3dB` after source, bias/readout, cabling/instrument and package effects are shown negligible or measured/de-embedded with adequate uncertainty.

## 20.3 Small-signal/injection gate

At fixed T/E/geometry, acquire at least three decreasing optical modulation or pulse levels. Inferred waveform/time constant should converge as excitation is reduced before interpretation as a small-signal device/material quantity.

A 25-ns source pulse corresponds to a rough one-pole rise-time bandwidth scale:

`0.35/25 ns ≈ 14 MHz` [DERIVED].

This is an apparatus-sizing check only.

## 20.4 One-pole model

For:

`H(f)=1/(1+i 2 pi f tau)`

`|H|=1/sqrt(1+(2 pi f tau)^2)`

`phi=-atan(2 pi f tau)`

`f_3dB=1/(2 pi tau)`.

Accept a one-pole interpretation only when:

- amplitude and phase support the same `tau`;
- residuals are not systematically structured;
- fit-window/range changes do not materially shift the pole;
- decreasing injection does not change the inferred small-signal pole;
- external electrical/source response is not limiting;
- package thermal response is negligible in the fitted band or separately modeled.

Otherwise report `tau_eff` or a higher-order/physical model rather than forcing the result to `minority-carrier lifetime`.

---

# 21. Qualification-build acceptance matrix

These are qualification gates, not production capability indices.

| Stage | Required evidence before advance |
|---|---|
| Preflight | all step-specific local fields instantiated; applicable P36/P36A commissioning evidence current; genealogy and EH&S authorization complete |
| Substrate | identity/polarity/defect/surface genealogy complete; no critical crack/inclusion; local final-surface branch executed |
| LPE | absolute charge/thermal/gas/contact/wipe branch instantiated; usable continuous layer; P06 x/thickness map and morphology in selected development region; genealogy complete |
| As-grown material | P05 carrier-state baseline + P06 registered map complete |
| Anneal | actual `T_s(t)`/`T_Hg(t)` branch instantiated; stable n-like state under valid transport model; acceptable material region; optical composition/thickness preserved |
| Mask 1 | named resist branch; measured thickness/CD/profile; no pinhole/adhesion failure |
| Wet mesa | chemistry basis unambiguous; local rate/profile calibration; measured through-layer isolation; acceptable depth/undercut/profile |
| Oxide | electrolyte basis/cell/area defined; repeatable V(t)/Q/A; ~80-nm target physically verified; interface/device compatibility |
| Mask 2 | measured 4–5 µm film; direct bake/chlorobenzene fingerprint retained; clean opening; sufficient re-entrant profile; oxide compatibility |
| RIE | gas/plasma/thermal state recorded; oxide clear known; sheet/depth conversion state and blocking witness accepted |
| Cr/Au | 30/270 nm physically verified; clean lift-off; no uncontrolled RIE-to-metal treatment |
| Contact | TLM/IV accepted; reference neighborhood includes rho_c~9×10^-4 Ω·cm² at 80 K; blocking function separately verified |
| Bare detector | stable near-ohmic low-field operation; safe E/P_J region established |
| Singulation | no unacceptable visible/subsurface/functional edge damage |
| Package | cryogenic mechanical/electrical/noise/thermal acceptance passed |
| Responsivity | traceable spectral calibration at declared device/contact/T/E/f/FOV/geometry |
| Noise/D* | same-device/state identity or explicit correction; detector-referred PSD/ASD normalized correctly; electronics/background effects bounded |
| Dynamics | external/package transfer bounded/de-embedded; injection dependence checked |

No row becomes a numerical production tolerance until repeated local data and requirements justify one.

---

# 22. Local instantiation and commissioning coordinates

These are not manuscript omissions; they physically depend on the executing hardware/material lot. They are nevertheless **mandatory traveler fields before the relevant irreversible operation**.

## 22.1 LPE

- boat dimensions, well volume, fill/meniscus state and total charge mass;
- furnace-controller-to-solution/substrate temperature offsets/gradients;
- N2/H2 flow and gas-quality criteria;
- above-liquidus/equilibration criterion;
- exact contact interval/trajectory giving required thickness;
- slider speed/clearance/wipe geometry;
- auxiliary Hg-source inventory and reuse/depletion rule.

Use P36 AT-LPE and P30/P30A.

## 22.2 Anneal

- ampoule free volume and source/sample geometry;
- sample/reservoir thermometry offsets;
- Hg inventory/source state sufficient for the local boundary condition;
- actual dwell and cooldown trajectory;
- time/temperature needed for the measured starting defect state.

Use P36 AT-ANN and P31/P23.

## 22.3 Lithography/wet chemistry

- exact mathematical Br2 formulation basis;
- HBr stock assay;
- agitation and measured etch rate;
- Mask-1 resist/product/process;
- Mask-2 resist product, spin, exposure, developer, chlorobenzene order, lift-off solvent;
- anodization EG/water ratio basis and cell dimensions.

Use P36A AT-LITH/AT-WET/AT-ANO.

## 22.4 RIE

- exact CH4/H2 local gas realization;
- MFC calibration;
- RF frequency/electrode geometry;
- self-bias/ion-energy proxy;
- sample temperature;
- chamber seasoning;
- oxide-clear time;
- conversion-depth/sheet-state measurement method.

Use P36 RIE acceptance and P34/P08/P24.

## 22.5 Metallization

- deposition method/tool;
- base/process vacuum state;
- Cr/Au rates;
- QCM tooling factor and independent witness calibration;
- sample thermal load;
- allowable RIE-to-Cr delay.

Use P36 deposition acceptance and P26/P26A.

## 22.6 Singulation/package

- cutting tool/abrasive/feed/support/protection;
- released functional edge exclusion;
- attachment product/bondline/cure;
- wire-bond parameters;
- cold-shield/window/aperture geometry;
- package thermal transfer.

Use P35/P33/P36.

## 22.7 Metrology

- Hall magnet/current/voltage/temp implementation;
- FTIR reference/footprint/resolution/reduction version;
- calibrated radiometric reference detector/monochromator geometry;
- preamplifier/analyzer transfer and ENBW convention;
- dynamic-source/electronics/package transfer functions;
- dimensional/thickness metrology appropriate to the feature scale.

Use P36/P36A.

A competent laboratory closes these values through calibration/qualification rather than by searching for a universal number that does not physically exist.

---

# 23. Minimum run traveler/data package

A complete qualification build shall preserve:

1. source-material and substrate genealogy;
2. P36/P36A preflight/commissioning evidence applicable to the executed steps;
3. final CdZnTe surface recipe and clean-to-load times;
4. exact LPE charge calculation and actual masses;
5. boat revision, source inventory, gas and full growth T(t);
6. as-grown P05/P06 data;
7. full anneal `T_s(t)`, `T_Hg(t)`, source history and post-anneal P05/P06;
8. Mask-1 resist/exposure/develop data;
9. wet-etch formulation mathematics, bath genealogy, depth/CD/isolation;
10. anodization cell/electrolyte/A_exposed/I/V(t)/Q/A/thickness;
11. Mask-2 thickness, bake, chlorobenzene branch, exposure/developer/profile;
12. RIE MFC/plasma/pressure/self-bias/temperature/t_clear/t_sem/sheet/depth/witness data;
13. RIE-to-Cr timestamps;
14. Cr/Au source/vacuum/rate/QCM/witness thickness and lift-off inspection;
15. final geometry/contact map and TLM;
16. P10 bare-device DC/self-heating data;
17. pre-singulation optical/noise/dynamic baseline where feasible;
18. singulation process/edge/subsurface/functional disposition;
19. package construction, bondline, interconnect, optical geometry and thermal response;
20. final P11 absolute responsivity files;
21. final P12 raw PSD/ASD, electronics calibration, NEP and D* reduction including area/power convention and state identity;
22. final P13 raw transient/frequency data and de-embedding;
23. uncertainties, deviations, rework and nonconformances;
24. final comparison against RP-01 anchors.

A scientifically useful run with missing items may be reported, but it is not a complete reproducibility record.

---

# 24. Troubleshooting logic

## 24.1 Layer composition/thickness wrong

Check, in order:

- actual charge masses/composition reconstruction, especially Cd;
- measured melt/liquidus temperature and calibration;
- contact supercooling and T(t);
- source age/depletion/Hg loss;
- contact time/cooling trajectory;
- spatial temperature/overlap/wipe behavior.

Do not compensate a thermometry error by silently changing charge composition.

## 24.2 Residual melt / rough LPE surface

Check:

- substrate polarity/wetting;
- slider clearance/flatness;
- wipe-off geometry/contact;
- separation speed/stick-slip;
- thermal trajectory at separation;
- source/solution history.

## 24.3 Anneal reaches n-type but poor mobility

Check:

- whether Hall reduction is valid or multicarrier;
- starting defect state;
- Hg boundary condition and cooldown;
- composition shift/surface alteration;
- substrate impurity genealogy;
- excessive thermal history.

## 24.4 Wet mesa profile/etch rate drifts

Check:

- explicit Br2 formulation and HBr assay;
- bath age/open time and temperature;
- agitation/mass transport;
- resist thickness/edge retreat;
- sample loading/area;
- temperature-sensor placement.

Recalibrate after chemistry/agitation/resist changes.

## 24.5 Oxide thickness or V(t) drifts

Check:

- electrolyte preparation basis/age;
- KOH assay;
- A_exposed/current-density calculation;
- cathode/anode geometry;
- starting wet-etch surface and air-exposure clock;
- bath temperature;
- film dissolution during/after formation.

## 24.6 High contact resistance or weak blocking behavior

Separate:

- RIE electrical conversion failure;
- conversion-depth/sheet-state mismatch;
- oxide not fully cleared;
- long/uncontrolled RIE-to-metal delay;
- contaminated/oxidized interface;
- wrong Cr thickness/poor film continuity;
- TLM fitting/geometry error;
- majority contact quality from minority blocking function.

Do not introduce an ion mill/wet clean without treating it as a new contact process.

## 24.7 Excess 1/f noise

Check:

- detector bias/self-heating;
- contact/TLM/blocking state;
- passivation/interface history;
- package/interconnect stress/microphonics;
- readout electronics floor/loading;
- optical background and background fluctuations;
- actual signal frequency relative to knee.

## 24.8 Apparent slow lifetime

Check package thermal recovery, AC-coupling/high-pass response, source pulse tail, preamplifier recovery, injection level, and interface trapping before attributing the pole to bulk recombination.

---

# 25. Historical gaps deliberately left open

The following do not prevent this document from functioning as a reference/qualification manual, but they prevent an unqualified claim of literal historical identity:

- exact RP-01 CdZnTe Zn fraction, plane/polarity/miscut and final surface recipe;
- exact Fermionics/UWA LPE boat dimensions, charge mass, source synthesis, gas flows, contact/wipe/cooldown;
- exact RP-01 Hg anneal apparatus/source/trajectory;
- exact Mask-1 resist/process and wet-mesa chemistry;
- exact UWA anodization electrolyte/cell/current program;
- exact Mask-2 resist product/exposure/developer/chlorobenzene ordering/lift-off solvent;
- exact Plasma Technology reactor model, RF frequency, electrode geometry, self-bias, sample temperature and individual MFC settings;
- exact converted-depth value used in the RP-01 volumetric Hall reduction;
- exact RP-01 deposition method, base pressure, rates, QCM factors and RIE-to-metal air break;
- exact historical contact pair/gap used for Figures 3/5/6/7;
- exact 4.4-µm cutoff convention;
- exact 60° FOV angular convention and physical geometry;
- exact Optronics spectral-system configuration and reference chain;
- exact low-noise preamplifier and HP35665A settings;
- exact 1-kHz noise convention used in the published D* curve;
- exact singulation method/die outline;
- exact package/interconnect/optical construction;
- direct RP-01 lifetime/frequency-response result.

`Not recovered` is not equivalent to `did not exist`.

---

# 26. Reference-source crosswalk

The integrated procedure is based principally on the following controlled source families already audited in the repository:

1. Smith et al. 2001 — canonical RP-01 photoconductor process/performance.
2. Hansen, Schmit, Casselman 1982 — HgCdTe band gap versus composition/temperature.
3. Harman 1980 — Te-rich LPE growth/liquidus/process behavior.
4. Schmit, Hager, Wood 1982 — Te-rich LPE including x≈0.30.
5. Radhakrishnan, Sitharaman, Gupta 2003 — horizontal-slider/source-preparation details.
6. Bowers & Schmit / Honeywell — xL=.082, yL=.810, TL=507 °C tie line and Hg-containment architecture.
7. Hager & Wood / Honeywell — residual-melt wipe-off architectures.
8. Tranchart et al. and related primary substrate work — CdZnTe near 4% Zn for x≈0.30 LPE.
9. Nagahama et al., Harman, Jones et al., Chandra/Schaake/Kinch — Hg-rich anneal/defect control.
10. Smith et al. 2000 — same-UWA wet-mesa detector evidence.
11. Srivastav et al. 2005 — quantitative Br2/EG/HBr mesa behavior.
12. Texas Instruments US3977018 and related anodization disclosures — HgCdTe photoconductor native-oxide branch.
13. Musca/Siliquini/Smith/Faraone UWA RIE studies — electrical conversion/LBIC/process physics.
14. Semu et al.; Elkind & Orloff — CH4/H2 RIE self-bias, chemistry, morphology/orientation effects.
15. same-UWA HgCdTe metallization work plus primary HgCdTe contact studies — deposition/interface transfer.
16. van der Pauw/NIST Hall guidance and Tsen et al. — transport metrology/multicarrier control.
17. Hougen 1989 — HgCdTe transmission/composition/thickness modeling.
18. NIST-style spectral comparator and low-background radiometry principles — absolute responsivity/view-factor traceability.
19. Bartoli et al. and related HgCdTe PC package thermal work — package thermal de-embedding.
20. UWA transient-photoconductive-decay work — same-lineage dynamic measurement branch.

The controlled repository source ledger remains authoritative for complete bibliographic metadata, evidence class, and transfer restrictions.

---

# 27. Internal procedure crosswalk

For detailed travelers, derivations, uncertainty budgets, and qualification experiments use:

- P29 / P07 family — CdZnTe substrate/final surface;
- P30/P30A / P03 family — LPE apparatus, absolute charge, thermal/contact/wipe-off;
- P05 — Hall/VdP;
- P06/P06A — FTIR composition/thickness;
- P31 / P04/P23 — Hg anneal;
- P32 / P14 — Mask 1;
- P28/P28A / P01 — wet mesa;
- P25/P25A / P02 — anodic oxide;
- P27 / P14A — Mask 2/lift-off resist;
- P34 / P08/P08B/P24 — RIE reactor equivalence, depth/sheet state and blocking contact;
- P26/P26A / P09 — Cr/Au and TLM;
- P10/P10A — DC field/self-heating;
- P35 — singulation;
- P33/P15 — package/interconnect;
- P11/P11A — absolute responsivity/FOV/radiometry;
- P12/P12B/P12C — noise/NEP/D*, same-device/state identity;
- P13/P13A — dynamics/lifetime;
- P16/P16A — master traveler and first-build readiness architecture;
- P17 — reproducible-release/statistical capability layer;
- P18 — deviations/failure analysis;
- P20/P20A — uncertainty propagation/requirements allocation;
- **P36 — laboratory subsystem IQ/OQ/surrogate-PQ/HgCdTe residual acceptance**;
- **P36A — mass, dimensional, lithography, wet-chemistry and anodization commissioning/acceptance**.

P36/P36A do not make an unspecified laboratory ready. They define what evidence a real laboratory must produce before a local branch is trusted.

---

# 28. Round-52 technical-review disposition

Draft 0.2 incorporates the adversarial-review corrections recorded in `docs/RP01_MANUSCRIPT_TECHNICAL_REVIEW_ROUND52.md`.

Key corrected points are:

- the title no longer claims reproducibility before P17 evidence exists;
- an irreversible-step preflight rule now separates a literature center from an executable local branch;
- P36/P36A are integrated into the main manual;
- RIE volumetric carrier density is explicitly coupled to conversion depth and sheet transport;
- RP-01 Figures 3/5/6/7 same-device identity is incorporated into D* closure;
- 60° FOV full-angle/half-angle ambiguity is preserved rather than hidden;
- D* detector normalization area is separated from optical beam/aperture geometry and covariance is retained where shared;
- the 24.5-nV/√Hz high-frequency g-r level remains prohibited as an automatic 1-kHz substitution;
- authoritative LPE mass fractions remain those in `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`.

Document state:

`RP01-MANUSCRIPT-ADVERSARIAL-REVIEW-PASSED = YES`.

This is a manuscript-quality state only.

## Remaining work before a finished booklet

1. compile the complete bibliography from the controlled source ledger;
2. add a compact uncertainty/example-calculation appendix;
3. create process-flow, LPE, anneal, RIE/contact and radiometry figures/schematics;
4. extract operator checklists/travelers into appendices;
5. normalize the final symbol/unit/index system;
6. typeset the professional PDF/booklet;
7. perform a final editorial/visual adversarial review.

The absence of a specific future laboratory's furnace offsets, MFC calibration, QCM tooling factor, resist exposure dose, package bondline dimensions, or optical view factor is **not** a manuscript-content failure. Those values are explicitly identified local-instantiation coordinates whose acceptance methods are controlled by the detailed procedures.