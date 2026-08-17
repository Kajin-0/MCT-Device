# Reproducible Fabrication and Characterization of an x≈0.30 HgCdTe Photoconductor

## Source-traceable process manual based on the Smith et al. RP-01 architecture

**Integrated manuscript draft:** 0.1  
**Continuity round:** 51  
**Date:** 2026-08-16 America/New_York  
**Status:** `INTEGRATED-MANUSCRIPT-DRAFT — REFERENCE/QUALIFICATION PROCESS`  
**Physical maturity:** not a production release; not a claim of literal historical reproduction.

---

## Abstract

This manual consolidates a source-traceable process for fabricating and characterizing an approximately x=0.30 HgCdTe photoconductive infrared detector on insulating CdZnTe, using the two-mask blocking-contact architecture reported by Smith et al. (2001). The historical paper directly fixes several important device and process quantities—approximately 9.5 µm active-layer thickness, native anodic oxide near 80 nm, a 4–5 µm Mask-2 photoresist layer with an 80 °C/30 min prebake and 30 min chlorobenzene treatment, a CH4/H2 reactive-ion-etch step at 64 sccm total flow, 100 mTorr, 50 W and 60 s, Cr/Au metallization of 30/270 nm, a nine-contact 300×300 µm test structure with 50–400 µm gaps, and detector characterization near 80 K and 10 V/cm. The historical publication does not disclose a complete starting-material growth traveler, Hg-overpressure anneal recipe, wet-mesa formulation, anodization cell construction, photoresist identities, RIE reactor physics, deposition apparatus, singulation method, package construction, or full metrology implementations.

The present manual therefore distinguishes three classes of instructions throughout: **historically fixed values**, **literature-grounded reference qualification centers**, and **apparatus-dependent quantities that must be measured locally before irreversible processing**. The objective is not to manufacture missing historical facts. It is to give a competent laboratory a coherent, executable qualification route in which every remaining local variable is explicitly identified, measured, recorded, and accepted by a stated physical criterion. Historical identity and local reproducibility are treated as separate claims.

---

# 1. Scope and claims

## 1.1 Device being reproduced functionally

The reference device is an n-type HgCdTe photoconductor grown by Te-rich liquid-phase epitaxy (LPE) on an electrically insulating CdZnTe substrate. The nominal alloy composition is approximately x=0.30, corresponding to a mid-wave infrared detector response. The reference layer thickness is approximately 9.5 µm. Localized CH4/H2 RIE is used through contact openings to create a more highly n-type near-contact region intended to suppress minority-carrier surface/contact recombination while retaining a simple two-mask photoconductor geometry.

The final detector is characterized using measured contact geometry, detector temperature, active electric field, optical background, modulation frequency, responsivity, detector-referred noise, and temporal/frequency response.

## 1.2 What this manual can claim

A laboratory that follows this document can generate one of three scientifically distinct outcomes:

1. **Reference qualification build:** follows the fixed RP-01 values where known and the explicitly identified transfer/qualification branches where history is incomplete.
2. **Local reproducible process:** after apparatus-specific windows, measurement systems, repeatability, change control, and detector acceptance criteria are established locally.
3. **Historical RP-01 reproduction:** only if the historically critical identities that remain open are independently recovered or otherwise demonstrated.

A working detector produced with a local LPE boat, modern resist, different evaporator, or local package is not automatically a literal reproduction of the 2001 fabrication traveler. Conversely, such substitutions do not prevent a scientifically rigorous and reproducible local process when they are labeled and qualified.

## 1.3 Evidence labels used in this manual

- **[RP01]** — directly reported by Smith et al. (2001).
- **[SAME-LINEAGE]** — directly reported by UWA/Faraone-group work closely related to the reference device/process.
- **[PRIMARY-TRANSFER]** — primary experimental literature or patent from a different but physically relevant HgCdTe/CdZnTe process family.
- **[DERIVED]** — arithmetic or physics calculation from stated quantities.
- **[REF-CENTER]** — literature-grounded first qualification center; not a historical RP-01 setpoint unless separately marked [RP01].
- **[LOCAL-CAL]** — apparatus-dependent quantity that must be measured/calibrated on the executing laboratory's hardware.
- **[LOCAL-QUAL]** — local branch or tolerance that must be qualified empirically before routine use.
- **[OPEN-HIST]** — historically unrecovered. Do not infer from generic semiconductor practice.

---

# 2. Reference detector specification

## 2.1 Starting material and final-device anchors

| Quantity | Reference value | Evidence / use |
|---|---:|---|
| HgCdTe alloy composition | x≈0.30 | [RP01] nominal starting material |
| Active-layer thickness | ≈9.5 µm | [RP01] |
| Starting conductivity | n-type | [RP01] |
| Electron concentration | ≈9.8×10^14 cm^-3 | [RP01] supplier value; measurement temperature not disclosed |
| Electron mobility | ≈4.0×10^4 cm²/V·s | [RP01] supplier value; measurement temperature not disclosed |
| Substrate | electrically insulating CdZnTe | [RP01] |
| Native anodic oxide | ≈800 Å = 80 nm | [RP01] |
| RIE-converted electron density | ≈2.0×10^15 cm^-3 | [RP01] measured converted material |
| RIE-converted mobility | ≈3.3×10^4 cm²/V·s | [RP01] |
| Cr thickness | 300 Å = 30 nm | [RP01] |
| Au thickness | 2700 Å = 270 nm | [RP01] |
| Contact size | ≈300×300 µm | [RP01] |
| Contact gaps | 50–400 µm in 50-µm increments | [RP01] |
| Specific contact resistivity | ≈9×10^-4 Ω·cm² at 80 K | [RP01] TLM result |
| Canonical detector temperature | 80 K | [RP01] characterization state |
| Canonical electric field | 10 V/cm | [RP01] noise/spectral state |
| Spectral modulation frequency | 1 kHz | [RP01] |
| Nominal FOV | 60° | [RP01]; exact physical aperture geometry must still be measured locally |
| Detector-response cutoff | ≈4.4 µm | [RP01]; exact cutoff convention not recovered |
| D* near 4 µm | ≈2×10^11 Jones | [RP01] |
| Quantum efficiency | ≈70% | [RP01] |
| 300-K/60° background photon flux | ≈1×10^15 cm^-2 s^-1 | [RP01] |
| 1/f knee | ≈3 kHz | [RP01] typical device |
| High-frequency g-r noise ASD | ≈24.5 nV/√Hz | [RP01]; do not use as the 1-kHz noise without evidence |

## 2.2 Useful electrical consistency quantities

Using n=9.8×10^14 cm^-3, µ=4.0×10^4 cm²/V·s, q as the elementary charge, and the one-carrier Hall-factor-one approximation:

`rho = 1/(q n mu) ≈ 0.15922 ohm·cm`  [DERIVED]

For t=9.5 µm:

`R_sheet = rho/t ≈ 167.60 ohm/square`  [DERIVED]

The one-carrier Hall coefficient magnitude is:

`|R_H| = 1/(q n) ≈ 6.369×10^3 cm^3/C`  [DERIVED]

For W≈300 µm and E=10 V/cm, ideal uniform bulk current is approximately:

`I ≈ E W t / rho ≈ 1.79 mA`  [DERIVED]

This is an instrument-sizing check, not a published detector current.

---

# 3. Safety, facility, and execution boundary

Hg, Cd-containing materials, bromine, concentrated HBr, hydrogen, methane, vacuum systems, RF plasma systems, high-temperature sealed ampoules, organic solvents, cryogens, and metal-deposition systems require the executing institution's formal EH&S controls. This manual does not substitute for local chemical hygiene, hazardous-gas, pressure-vessel, pyrophoric/flammable-gas, vacuum, cryogenic, or waste-management procedures.

Before physical execution, the laboratory shall identify and approve:

- Hg/Cd containment, exposure monitoring, spill response, and waste streams;
- Br2/HBr-compatible hood, storage, secondary containment, and neutralization/waste route;
- H2/CH4 gas cabinets, leak detection, purge/interlock system, and exhaust;
- sealed-ampoule and hot-zone handling controls;
- RIE RF/high-voltage and vacuum safety;
- metal-deposition source and vacuum-system safety;
- solvent/chlorobenzene controls;
- LN2/cryostat oxygen-deficiency and pressure-relief controls.

No process value in this manual constitutes authorization to operate hazardous equipment.

---

# 4. End-to-end process flow

The recommended reference qualification route is:

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

At every irreversible step, record material genealogy, procedure revision, actual setpoints/traces, deviations, and the corresponding acceptance measurement.

---

# 5. CdZnTe substrate and final pre-LPE surface

## 5.1 Reference substrate family

RP-01 specifies only an insulating CdZnTe substrate. The strongest current near-composition LPE transfer center is **Cd0.96Zn0.04Te, (111)B**. Use this as the first qualification substrate family unless the executing laboratory has stronger matched evidence. [PRIMARY-TRANSFER / REF-CENTER]

Do not label 4% Zn, (111)B polarity, any particular miscut, or any substrate dimensions as direct RP-01 facts.

## 5.2 Incoming qualification record

Record for each substrate:

- supplier, lot/ingot, nominal Cd/Zn/Te composition;
- measured lattice parameter or independently verified Zn fraction where available;
- surface plane and A/B polarity;
- miscut magnitude and azimuth;
- substrate dimensions/thickness;
- electrical-isolation/resistivity information;
- HRXRD rocking curve and curve shape;
- IR inclusion/precipitate map;
- EPD or equivalent defect metric on representative material;
- trace impurities where available, especially electrically active contaminants such as Cu;
- polish history, roughness, scratches, chips, warp/flatness.

Historical values near EPD~5×10^4 cm^-2 and ~25 arcsec rocking-curve width are transfer reference scales, not released limits.

## 5.3 Final surface family

The strongest practical Te-rich LPE transfer source uses a brief **2–3% Br2 in methanol** treatment on (111)B CdZnTe followed by rapid loading into the graphite boat. [PRIMARY-TRANSFER]

The source does not close:

- whether the bromine percentage is w/w, w/v, v/v, or another convention;
- exact exposure time beyond “a few seconds”;
- bath temperature/agitation;
- rinse/dry sequence;
- removed depth;
- maximum clean-to-load delay.

### Required local instantiation

Create an unambiguous local recipe ID, for example `CZT-BRMEOH-VV-*` or `CZT-BRMEOH-WW-*`, and mathematically define the bromine concentration. Record reagent lots, bath temperature/age, sample area, immersion time, agitation, rinse, dry, removed depth, roughness, and all timestamps.

Define:

`Delta t_clean-load = t_boat_load - t_final_etch_end`.

No universal maximum is assigned. The executing laboratory must qualify the allowed delay by downstream LPE morphology, interface quality, P06 spatial uniformity, and P05 transport.

## 5.4 Substrate acceptance before LPE

Proceed only when:

- identity/orientation/polarity are unambiguous;
- no crack or inclusion intersects the intended active region;
- electrical isolation is adequate for the intended device geometry;
- the selected final-surface recipe was executed exactly under its local ID;
- no visible residue/particle/surface damage remains;
- clean-to-load history is recorded.

---

# 6. Te-rich horizontal-slider LPE growth

## 6.1 Composition center

Use the Honeywell x≈0.29 tie-line center:

`x_L = 0.082`  
`y_L = 0.810`  
`T_L = 507 °C`  
`x_S ≈ 0.29`.

For `(Hg_(1-xL) Cd_xL)_(1-yL) Te_yL`, the derived elemental mass fractions are:

- `w_Hg = 0.2497382358`
- `w_Cd = 0.01250164993`
- `w_Te = 0.7377601143`.

Use atomic weights Hg=200.59, Cd=112.414, Te=127.60 g/mol. [DERIVED]

For any locally established total growth-charge mass `M_charge`:

`m_Hg = 0.2497382358 M_charge`

`m_Cd = 0.01250164993 M_charge`

`m_Te = 0.7377601143 M_charge`.

**Do not infer `M_charge` by scaling another laboratory's substrate area or published 4.8-g charge.** Total charge is determined by the actual well volume, fill height, melt depth, overlap area, containment geometry, source depletion, and handling margin. [LOCAL-CAL]

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
- controlled slider actuation for contact and separation;
- one defined residual-melt wipe-off architecture.

Two Honeywell-derived wipe-off families are acceptable development branches, but do not combine them under one recipe:

1. CdTe pieces retained in a dedicated wipe-off well;
2. scribed CdTe apron adjacent to the growth substrate.

Record complete boat dimensions, graphite grade, clearances, recess depth, well dimensions/volume, overlap, Hg-source geometry, cover fit, actuator travel, and measured position repeatability. [LOCAL-CAL]

## 6.3 Source synthesis

The exact x≈0.30 historical synthesis schedule is unrecovered. A practical Te-rich slider transfer branch demonstrates:

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
5. heat/equilibrate above or near the liquidus as defined by the selected branch;
6. supercool or cool to the intended contact state;
7. translate melt over substrate.

N2 flow/time, H2 flow, gas purity/dew point/O2 criterion, furnace offsets, axial gradient, and actual melt temperature are [LOCAL-CAL]. Controller display temperature is not assumed equal to melt temperature.

Calibrate the loaded boat temperature at the actual substrate/melt region before HgCdTe qualification. Record the complete `T(t)` trace.

## 6.5 First qualification thermal/contact center

Use `T_L=507 °C` as the liquidus tie-line anchor. A **500 °C first-contact state**, corresponding nominally to about 7 K supercooling, is a reasonable [REF-CENTER], not a historical release condition.

Published Te-rich LPE evidence brackets growth contact over roughly 0.25–10 min in one direct branch; a Honeywell example extends to about 30 min. Do not average these into one fictitious historical time.

### Recommended first local development sequence

1. establish a stable loaded-boat thermal map;
2. hold above the chosen liquidus sufficiently to obtain a repeatable solution state;
3. cool to the first contact center near 500 °C;
4. execute a short-to-intermediate contact time chosen from the published seconds-to-minutes scale;
5. separate with measured slider motion;
6. execute the selected wipe-off operation;
7. cool under the recorded H2/controlled atmosphere trajectory.

The precise contact time is set by measured thickness and morphology, not by literature resemblance.

## 6.6 Required LPE outputs

After every growth run record:

- whole-surface image and usable-area map;
- residual melt/droplet area;
- pinholes/voids/scratches/terraces;
- P06 thickness/composition map;
- HRXRD/defect metric where available;
- matched P05 transport coupon;
- charge/source mass history and source-use number.

The target is an approximately x=0.30, ~9.5-µm usable layer with sufficiently uniform morphology and transport to enter anneal/device fabrication. Do not accept a run solely because its center-point optical edge appears correct.

---

# 7. As-grown material metrology

## 7.1 FTIR mapping

Use nondestructive IR transmission on the intact parent piece before subdivision where practical.

Recommended qualification capability:

- spectral range approximately 500–5000 cm^-1 or wider as needed;
- spectral resolution ≤4 cm^-1 for qualification work;
- minimum 9-point spatial map; 5×5 preferred where sample size permits;
- background/reference acquisition with instrument state recorded;
- full-spectrum fitting preferred over single-edge-point interpretation;
- independent physical thickness cross-check.

The Hansen relation for x=0.30 at 80 K gives a band-gap-equivalent wavelength near 5.09 µm. This is **not** the same quantity as the reported ~4.4-µm detector response cutoff. Do not use detector cutoff and band-gap wavelength interchangeably.

Report the spectral edge definition used. `lambda_50` may be retained as a QC descriptor but is not a universal composition identity.

## 7.2 Hall / van der Pauw

Use a dedicated material-control descendant unless the laboratory has demonstrated that Hall contacts and processing are compatible with subsequent device fabrication.

For initial qualification:

- four small perimeter ohmic contacts;
- symmetric current/field reversals;
- nominal currents 10, 30, and 100 µA with self-heating checks;
- initial B grid: 0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T;
- extend toward ±2 T where available for multicarrier discrimination;
- 80 K mandatory for the first direct comparison; 300 K recommended.

Use antisymmetrized Hall voltage and van-der-Pauw reciprocity checks. A practical redundancy gate is:

- ≤3% discrepancy: pass;
- 3–5%: conditional/review;
- >5%: fail/repeat or escalate.

Near p/n conversion, do not force a one-carrier density through a Hall-sign cancellation region. Classify the state as `N-LIKE`, `P-LIKE`, or `TRANSITION/MULTICARRIER` and use variable-field tensor analysis where required.

---

# 8. Hg-overpressure anneal

## 8.1 Objective

Drive the as-grown layer into a stable lightly n-type state while preserving optical composition, thickness, morphology, and detector-relevant lifetime/interface behavior.

The final target neighborhood is the RP-01 material state:

- n-type;
- n≈9.8×10^14 cm^-3;
- µ≈4.0×10^4 cm²/V·s;
- x≈0.30;
- thickness ≈9.5 µm.

The supplier measurement temperature for the historical n and µ values is unknown, so local comparison shall always state the measurement temperature.

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

Near-composition LPE evidence supports 250–300 °C as a useful n-type conversion region without apparent composition change, while ~400 °C can produce interface-region composition changes. Therefore begin below 300 °C unless a separate objective justifies a higher-temperature branch.

## 8.4 Anneal qualification sequence

1. Measure pre-anneal P05/P06 state at registered locations.
2. Run the 250 °C/1 h Hg-rich center.
3. Cool under a recorded boundary condition; do not simply label “furnace cool.”
4. Repeat P05 and P06.
5. If the state is stable n-like but materially above/below the desired carrier-density region, map time at fixed `T_s`/Hg boundary before changing multiple coordinates.
6. Useful local time-screen coordinates are 0.5, 1, 2, and 4 h; only 1 h is the cited direct reference center.
7. After time sensitivity is known, map `T_s`; only then map Hg chemical potential (`T_Hg` relative to `T_s`) if required.

## 8.5 Anneal acceptance

A condition is retained only when:

- Hall state is stably n-like under an appropriate transport model;
- density/mobility are in the selected local target region;
- P06 shows no unacceptable optical/composition shift;
- surface morphology is preserved;
- no Hg/Te deposit or handling damage invalidates the surface;
- repeated matched coupons show a consistent response.

“n-type” alone is insufficient.

---

# 9. Mask 1 and wet mesa isolation

## 9.1 Mask-1 resist strategy

RP-01 does not identify the Mask-1 resist. Do not copy the Mask-2 chlorobenzene process into Mask 1.

The strongest product-identified Br2/HBr HgCdTe transfer candidate is **AZ4620**, demonstrated at 3 µm in another deep HgCdTe mesa process. A thick positive novolak/DNQ-family resist is therefore the recommended first screening family. [REF-CENTER]

The actual spin speed, thickness, exposure dose, developer, bake, and strip are [LOCAL-QUAL] and shall be selected from measured resist performance on the actual HgCdTe topography/etch chemistry.

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

`nominal 2% Br2 in 3:1 EG:HBr` at approximately 21 °C.

Measured transfer behavior at/near 21 °C includes:

- vertical rate ≈2.78 µm/min;
- run/process variation of order ±26%;
- anisotropy `A = 1 - R_L/R_V ≈ 0.63` with ~±11% variation;
- best reported RMS roughness near 2 nm;
- etch rate approximately doubles for each +10 °C over the studied range;
- lower temperature improves geometric/photoresist control.

These are [PRIMARY-TRANSFER], not x=0.30 RP-01 specifications.

## 9.3 Formulation ambiguity — mandatory local definition

The primary source does **not** define the basis of “2% Br2,” the mathematical preparation basis of 3:1 EG:HBr, or the HBr stock assay. Therefore the executing laboratory shall create an explicit local recipe, for example:

- `MESA-WW-*`: bromine mass fraction explicitly defined;
- `MESA-VV-*`: bromine volume fraction explicitly defined;
- another branch with a complete mathematical definition.

Record Br2/EG/HBr supplier, lot, purity/assay, delivered masses/volumes, vessel, batch age, temperature, open time, agitation, sample loading, and reuse history.

Do **not** write “2% Br2” on a traveler without its definition.

## 9.4 Etch-rate calibration before device etch

Before etching a detector wafer/piece through the active layer:

1. prepare matched witness coupons with the actual Mask-1 process;
2. measure starting thickness/topography;
3. execute at least three short etch times spanning the expected range;
4. measure vertical depth, lateral undercut, resist loss/retreat, roughness and profile;
5. determine the current local `R_V`, `R_L`, and mask bias;
6. use electrical isolation as the final through-layer criterion, not nominal time alone.

At a transfer rate of 2.78 µm/min, removing 9.5 µm would nominally require ~3.4 min [DERIVED], but **this value must not be used as an uncalibrated device etch time** because local formulation, agitation, temperature, resist geometry, and run-to-run variation can materially shift the rate.

## 9.5 Mesa endpoint and handoff

Record actual bath temperature, time, agitation, depth, top/base CD, undercut, sidewall morphology, isolation resistance/leakage, rinse/quench/dry, and the clock to anodization.

Proceed only when the mesa is electrically isolated, passivation-ready, and within the locally qualified geometry window.

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

The primary disclosure explicitly specifies 0.1 mole KOH per 1 L of the stated mixed solvent. With pure KOH molecular weight 56.1056 g/mol:

`m_KOH,pure = 5.61056 g per 1.000 L nominal electrolyte`  [DERIVED]

Correct for certified reagent assay `a`:

`m_KOH,reagent = 5.61056/a`.

The historical 90:10 EG/water basis is not explicitly stated as v/v or w/w. A local recipe shall define one basis mathematically and retain that identity throughout qualification.

## 10.3 Cell/current calculation

Measure the electrochemically exposed semiconductor area `A_exposed`, including the laboratory's explicit rule for exposed sidewalls/backside.

For selected current density `J`:

`I_command = J A_exposed`.

At the reference center:

`J ≈ 0.30 mA/cm²`.

Do not reuse an absolute current from another sample geometry.

## 10.4 Required anodization record

Record:

- electrolyte recipe/batch/age;
- vessel and cell geometry;
- anode-contact material/location;
- carbon cathode geometry/separation for the TI-PC branch;
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
- ~80-nm physical oxide target within the local metrology/acceptance window;
- good coverage/uniformity;
- acceptable interface/electrical state;
- compatible RIE oxide clearing;
- compatible TLM/contact and detector noise.

---

# 11. Mask 2: RIE/contact-window and lift-off resist

## 11.1 Direct historical fingerprint

Keep the following fixed for first RP-01-oriented transfer:

- resist thickness: **4–5 µm** [RP01];
- prebake: **80 °C / 30 min** [RP01];
- chlorobenzene treatment: **30 min** [RP01];
- then pattern, develop, water rinse [RP01];
- resist remains for RIE and subsequent Cr/Au lift-off.

The commercial resist, exposure dose/tool, developer, exact chlorobenzene sequence relative to exposure, and lift-off solvent are [OPEN-HIST].

## 11.2 Candidate resist hierarchy

The historical chlorobenzene mechanism strongly supports a positive DNQ/diazo-novolak AZ-type family.

Useful candidate evidence:

- AZ4110: direct chlorobenzene lift-off mechanism evidence but typically thinner in the cited branch;
- AZ4330/AZ4400/AZ4620 class: direct 4–5-µm thickness evidence in other processes.

The preferred local choice is a currently available positive resist that reproducibly yields a measured 4–5 µm film and a re-entrant profile after the RP-01 bake/chlorobenzene fingerprint. Product identity is a local transfer choice, not a historical claim.

## 11.3 Chlorobenzene order ambiguity

RP-01 wording can be read literally as:

`bake -> chlorobenzene -> pattern/expose -> develop`,

but historical chlorobenzene lift-off processes also use:

`bake -> expose -> chlorobenzene -> develop`.

If direct source closure is unavailable, compare both branches on witnesses while holding other variables fixed. Retain the branch giving stable 4–5 µm thickness, clean contact-window opening, sufficient RIE mask survival, measurable undercut/overhang, and clean 300-nm total-metal lift-off.

## 11.4 Exposure/development

Do not adopt an exposure dose from another resist. Determine clearing/exposure response on the actual 4–5 µm film after the chosen bake/chlorobenzene sequence. Use a dose/development matrix and measure:

- resist height;
- top/bottom opening CD;
- undercut/overhang;
- scum;
- oxide damage/compatibility;
- alignment to Mask 1.

Developer shall be product-matched, aqueous-alkaline where appropriate, with product/lot/concentration/time/temperature/agitation and water-rinse method recorded.

---

# 12. CH4/H2 RIE blocking-contact formation

## 12.1 Direct controller recipe

The canonical RP-01 RIE condition is:

- parallel-plate Plasma Technology reactor;
- gas notation `CH4/5H2`;
- total flow **64 sccm**;
- pressure **100 mTorr**;
- forward RF power **50 W**;
- RF time **60 s**.

These are [RP01].

If `CH4/5H2` is interpreted as a 1:5 flow ratio, the corresponding candidate flows are:

- CH4 = `64/6 = 10.6667 sccm`;
- H2 = `5×64/6 = 53.3333 sccm`.

This split is **[SAME-LINEAGE/INTERPRETIVE-CANDIDATE]**, not a directly stated RP-01 MFC setting. The local process traveler must state the actual adopted gas realization explicitly.

## 12.2 Reactor-equivalence rule

Matching 50 W, 100 mTorr, and 64 sccm is not sufficient to establish the same plasma. Record/calibrate:

- reactor/electrode geometry and RF frequency;
- sample holder/loading;
- CH4/H2 MFC IDs/ranges/calibration;
- base pressure and pressure-gauge state;
- chamber clean/season history;
- forward/reflected power;
- measured dc self-bias or a qualified ion-energy/sheath proxy;
- chuck/sample thermal state;
- pressure trace;
- actual gas ratio/total flow.

Forward RF power is an actuator, not a portable ion-energy coordinate.

## 12.3 Oxide clear versus semiconductor exposure

Define experimentally:

- `t_clear` = time required to clear the actual ~80-nm P25 oxide;
- `t_sem = t_RF - t_clear` = time of direct HgCdTe plasma exposure.

Determine `t_clear` on matched anodized witnesses by short-time calibration. Do not assume the full 60 s acts directly on HgCdTe.

## 12.4 Physical and electrical outputs

Keep distinct:

- `d_etch` = physical recession;
- `d_conv` = vertical electrical conversion depth;
- `L_conv` = lateral conversion extent.

Same-UWA work directly demonstrates that electrical conversion can extend much deeper than the physical etch. Therefore never infer conversion depth from profilometry alone.

Required qualification outputs include:

- oxide clear/recession;
- surface roughness/morphology;
- sheet resistance/conductance;
- Hall state on dedicated witnesses;
- LBIC or validated equivalent for conversion extent;
- TLM contact response after metallization;
- minority-carrier blocking functional response;
- detector resistance/noise change.

A direct RP-01 converted-state reference is n≈2.0×10^15 cm^-3 and µ≈3.3×10^4 cm²/V·s.

The historical TLM target is rho_c≈9×10^-4 Ω·cm² at 80 K.

## 12.5 LBIC reference validation branch

Same-lineage validation used a patterned ~300×300 µm RIE region, 1.047-µm Nd:YLF CW illumination around 400 mW/cm², and 80-K measurements to reveal the bipolar boundary response. These values are a validation reference branch, not mandatory production test settings.

---

# 13. RIE-to-metal transfer and Cr/Au deposition

## 13.1 Surface-transfer clock

The default baseline is:

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

No universal maximum is assigned; qualify the interval by TLM, interface stability, and detector performance.

## 13.2 Deposition method

RP-01 does not state the deposition method. Thermal evaporation is the strongest same-UWA method-family transfer candidate and is the preferred first local branch. E-beam or sputtered branches are permissible but require separate qualification because bombardment, heating, stress, and directionality differ.

## 13.3 Film stack

Deposit, without intentional interlayer oxidation:

1. **30 nm Cr** [RP01];
2. **270 nm Au** [RP01].

Remain under vacuum between layers if the tool permits.

Record:

- tool/method/chamber ID;
- base/process pressure;
- source material/purity/boat/crucible;
- QCM crystal/calibration/tooling factor;
- Cr and Au rates and times;
- indicated and independent witness thickness;
- holder/sample temperature;
- source-to-sample geometry/angle/rotation;
- abnormal events.

Do not invent an RP-01 base pressure or Cr deposition rate. Published HgCdTe Au rates of ~0.3–1.2 nm/s are useful screening scales only; select rates inside the stable calibrated regime of the actual tool and qualify contact response.

## 13.4 Thermal budget

Use the first transfer as **as-deposited, no intentional post-metal anneal**. Record actual holder/sample heating during deposition. Any post-metal anneal is a new process branch because Hg loss, interdiffusion, contact resistance, and resist/lift-off behavior can change.

## 13.5 Lift-off

The historical lift-off solvent/time/agitation are unrecovered. Choose a solvent/process compatible with the selected positive resist and Cr/Au stack. Prefer soaking and low-mechanical-force removal; ultrasonication is not a default because it can damage fragile HgCdTe/passivation/contact edges.

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
- optical aperture overlap where relevant.

Use these measured values, not mask CAD, in field and D* calculations.

## 14.2 TLM

Use the nine-contact geometry with approximately 300×300 µm contacts and gaps 50–400 µm in 50-µm steps.

At the defined temperature/background and low enough excitation to remain ohmic:

1. acquire bidirectional I–V for each adjacent/selected gap;
2. extract resistance using a consistent regression interval;
3. plot total resistance versus gap/geometry term;
4. obtain sheet and contact terms with uncertainty/residual analysis;
5. report specific contact resistivity with the exact TLM convention used.

Reference benchmark:

`rho_c ≈ 9×10^-4 ohm·cm² at 80 K` [RP01].

TLM is a majority-contact metric. It does **not** by itself prove the minority-carrier blocking function of the RIE region; retain LBIC or equivalent functional evidence.

---

# 15. Bare-device electrical qualification

## 15.1 Canonical operating field

At 80 K, use the measured active-region voltage and gap:

`E = V_active/L`.

For 10 V/cm, required active voltages are:

- 50 µm gap: 0.050 V;
- 100 µm: 0.100 V;
- 150 µm: 0.150 V;
- 200 µm: 0.200 V;
- 250 µm: 0.250 V;
- 300 µm: 0.300 V;
- 350 µm: 0.350 V;
- 400 µm: 0.400 V.

Correct source voltage for lead/contact/series drops where material.

## 15.2 Dark I–V and self-heating

At stabilized ~80 K:

1. acquire symmetric positive/negative low-field sweeps from zero through the intended operating range;
2. record active voltage, current, detector/mount temperature, and power;
3. periodically return to zero to expose drift/hysteresis;
4. establish the approximately ohmic low-field region;
5. characterize field-dependent resistance/sweepout behavior;
6. establish a self-heating criterion using a calibrated local temperature proxy.

Joule power:

`P_J = V_active I`.

A universal allowable mW limit is not assigned because package thermal resistance is construction-specific.

Preferred local temperature checks include near-zero-power `R(T)` calibration and/or a sufficiently coupled temperature sensor. Use short-pulse versus DC comparison where useful.

---

# 16. Singulation

## 16.1 Historical status

RP-01 does not disclose the singulation method or die outline. The first qualification route should therefore use a low-force, CdZnTe-compatible method and treat singulation as an actual process step rather than neutral handling.

## 16.2 Preferred first branch

A low-force **wire-saw family** is the strongest directly documented CdZnTe detector transfer branch. Primary evidence includes metallized CdZnTe protected with photoresist, mounted with low-melting wax on graphite, cut extremely slowly using a stainless-steel wire and 16-µm BN abrasive slurry. These details are [PRIMARY-TRANSFER], not a ready-made RP-01 recipe.

Do not automatically use the associated strong post-cut 5% Br/methanol/5-min damage-removal etch on a completed RP-01 device; it could destroy/alter the 9.5-µm active layer, passivation, and contacts.

## 16.3 Qualification method

Define and record:

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

- `d_visible` = geometric distance to visible damage;
- `d_functional` = minimum distance shown not to measurably degrade detector function;
- `d_release` = locally released exclusion including uncertainty/margin.

Visible edge quality alone is insufficient.

---

# 17. Cryogenic die attach, interconnect, and package

## 17.1 Historical status

The RP-01 paper does not disclose die attach, carrier, wire, aperture, window, vacuum, or package construction. Package hardware is therefore a local transfer architecture, not a historical process claim.

## 17.2 First attachment branch

Use a **compliant silicone-family** attachment as the first cryogenic mechanical screen because direct Honeywell HgCdTe evidence showed brittle/glass attachment cracking on deep cooldown while silicone-rubber attachment survived. The historical Dow Corning product names are evidence of the material family, not procurement instructions for an obsolete formulation.

A low-outgassing epoxy can be screened as a second branch, but must be treated separately.

## 17.3 Required package record

Record:

- singulated die geometry/edge state;
- carrier/cold-finger material, dimensions, CTE and thermal data source;
- attachment product/lot/mix ratio;
- dispense quantity;
- bondline thickness/coverage/voiding;
- placement force/tilt;
- cure T/time/atmosphere/trajectory;
- wire/ribbon material/diameter;
- bonder/tool/mode/force/ultrasonic/time/stage temperature;
- aperture, window/filter, shield and physical FOV geometry;
- vacuum/purge/bake history;
- temperature sensor position.

## 17.4 Package thermal response

Package/bondline thermal poles can occur on millisecond to hundreds-of-milliseconds scales in HgCdTe photoconductor assemblies. Therefore characterize the package thermal response near operating temperature using short optical or electrical heating pulses.

Do not attribute a slow P13 transient to minority-carrier lifetime until package thermal response has been evaluated.

## 17.5 Cryogenic acceptance

After assembly and defined thermal cycles, repeat selected:

- dark resistance/I–V;
- contact/lead resistance;
- P12 noise;
- P11 responsivity;
- P13 dynamic/thermal response;
- edge/crack and bond inspection.

Reject or requalify any package that introduces unacceptable mechanical damage, excess noise, optical loss, electrical drift, or thermal pole into the detector measurement band.

---

# 18. Absolute spectral responsivity

## 18.1 Canonical RP-01 comparison state

Use:

- T = 80 K;
- E = 10 V/cm;
- nominal 60° FOV, implemented by measured physical geometry;
- modulation/chopping frequency = 1 kHz;
- spectral region covering the full response and cutoff (~4.4 µm historical response edge).

## 18.2 Measurement architecture

Preferred modern method: substitution/comparison to a calibrated IR transfer detector in the same optical reference plane.

For calibrated reference responsivity `R_ref(lambda)` and detector-terminal-equivalent reference and DUT signals:

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
- detector current/power/temperature.

Use the same modulation and signal-amplitude convention for reference and DUT whenever possible so waveform factors cancel.

## 18.3 Spectral safeguards

- use order-sorting filters;
- test stray light beyond cutoff;
- purge/evacuate important H2O/CO2 path lengths;
- do not quote cutoff more precisely than wavelength calibration and edge-definition uncertainty;
- do not equate a detector-response cutoff to the Hansen band-gap-equivalent wavelength.

---

# 19. Noise, NEP, and specific detectivity

## 19.1 Canonical comparison state

For RP-01 comparison:

- T=80 K;
- E=10 V/cm;
- same contact pair/geometry as responsivity;
- same FOV/background state;
- evaluate detector noise at the signal frequency used in responsivity, especially 1 kHz for the canonical spectral measurement.

The historical ~24.5 nV/√Hz value is the reported high-frequency/g-r noise level. Since 1 kHz lies below the ~3-kHz 1/f knee, **do not substitute 24.5 nV/√Hz as the 1-kHz noise unless the measurement actually establishes that value at 1 kHz.**

## 19.2 PSD/ASD definitions

Voltage-noise PSD:

`S_v(f)` in V²/Hz.

ASD:

`e_n(f)=sqrt(S_v(f))` in V/√Hz.

Integrated noise:

`V_rms = sqrt(integral S_v(f) df)`.

For locally white noise through ENBW `B`:

`V_rms ≈ e_n sqrt(B)`.

Record FFT/window/ENBW or analyzer normalization so displayed line amplitude is never confused with ASD.

## 19.3 Electronics subtraction

When independent and correctly referred to the same input node:

`S_det = S_meas - S_elec`

`e_det = sqrt(e_meas^2 - e_elec^2)`.

Do not subtract ASDs linearly. If electronics noise is a large fraction of measured noise, propagate the resulting subtraction uncertainty rather than reporting an artificially precise detector floor.

Validate the chain using known resistor Johnson noise:

`e_J = sqrt(4 k_B T R)`.

## 19.4 NEP and D*

At the same wavelength, frequency, field, temperature, background and active-area convention:

`NEP(lambda,f) = e_det(f)/R_v(lambda,f)`.

`D*(lambda,f) = R_v(lambda,f) sqrt(A) / e_det(f)`.

Equivalently:

`D* = sqrt(A)/NEP`.

If responsivity and noise share the same calibrated linear gain path, common gain uncertainty can cancel algebraically; document the correlation rather than double-counting the gain uncertainty.

The area `A` must be the same physical optical/detector-area convention used to define incident power. Do not mix a nominal mask area with a different illuminated/aperture area.

## 19.5 Noise diagnostics

Report separately:

- fitted 1/f exponent;
- 1/f knee by the stated intersection convention;
- high-frequency/g-r plateau ASD;
- narrowband interference lines;
- bias dependence;
- blocked versus background-loaded states;
- stationarity/drift.

Historical comparison targets are roughly 3 kHz knee and 24.5 nV/√Hz high-frequency g-r level.

---

# 20. Temporal/frequency response and lifetime

## 20.1 Historical boundary

RP-01 does not publish a direct detector lifetime/frequency-response curve. Do not infer lifetime from the fact that spectral measurements used 1 kHz.

Same-UWA x≈0.30 transient-photoconductive work provides a useful historical measurement branch:

- 1.047 µm pulsed laser;
- 25 ns optical pulses;
- 1 kHz repetition;
- ~77 K under vacuum;
- AC-coupled amplification;
- HP54522A oscilloscope;
- typically 128 waveform averages;
- 500 samples at 20 ns spacing;
- non-exponential diffusion/recombination model outperformed a single exponential in the analyzed data.

These are measurement-history anchors, not RP-01 lifetime targets.

## 20.2 De-embedding

In frequency domain:

`H_meas = H_source H_optics H_detector H_bias H_preamp H_cable H_instrument H_pkg,thermal`

where the package thermal mechanism may require a coupled/additive representation rather than a simple multiplicative factor.

Only report detector `f_3dB` after source, electronics, cabling/instrument, and package effects are shown negligible or are measured and de-embedded.

## 20.3 Small-signal/injection gate

At fixed T/E/geometry, acquire at least three decreasing optical modulation or pulse levels. The inferred time constant/waveform must converge as excitation is reduced before it can be interpreted as a small-signal material/device quantity.

A 25-ns source pulse corresponds to a rough one-pole rise-time bandwidth scale ~0.35/25 ns ≈14 MHz [DERIVED]. This is only an apparatus-sizing check and does not establish detector bandwidth.

## 20.4 One-pole model

For:

`H(f)=1/(1+i 2 pi f tau)`

`|H|=1/sqrt(1+(2 pi f tau)^2)`

`phi=-atan(2 pi f tau)`

`f_3dB=1/(2 pi tau)`.

Accept a one-pole interpretation only when amplitude and phase give the same tau, residuals are structureless, fit-window dependence is small, injection level does not change tau, and package/electronics response is not limiting.

Otherwise report an effective time constant or higher-order model rather than forcing the result to “minority-carrier lifetime.”

---

# 21. Acceptance matrix for a qualification build

The following are **qualification-build gates**, not production capability indices.

| Stage | Required evidence before advance |
|---|---|
| Substrate | identity/polarity/defect/surface genealogy complete; no critical crack/inclusion; local final-surface branch executed |
| LPE | usable continuous layer; P06 x/thickness map and morphology within selected development region; genealogy complete |
| As-grown material | P05 carrier-state baseline + P06 registered map complete |
| Anneal | stable n-like state under valid transport model; acceptable n/µ region; optical composition/thickness preserved |
| Mask 1 | measured resist thickness/CD/profile; no pinhole/adhesion failure |
| Wet mesa | measured through-layer isolation; acceptable depth/undercut/profile; no uncontrolled chemistry basis |
| Oxide | repeatable V(t)/Q/A; ~80-nm target physically verified; interface/device compatibility |
| Mask 2 | measured 4–5 µm film; clean opening; sufficient re-entrant profile; oxide compatibility |
| RIE | actual gas/plasma/thermal state recorded; oxide clear known; electrical conversion/blocking witness accepted |
| Cr/Au | 30/270 nm physically verified; clean lift-off; no uncontrolled RIE-to-metal treatment |
| Contact | TLM/IV accepted; target neighborhood includes rho_c~9×10^-4 Ω·cm² at 80 K |
| Bare detector | stable near-ohmic low-field operation; safe E/P_J region established |
| Singulation | no unacceptable visible/subsurface/functional edge damage |
| Package | cryogenic mechanical/electrical/noise/thermal acceptance passed |
| Responsivity | traceable spectral calibration at declared T/E/f/FOV/geometry |
| Noise/D* | detector-referred PSD/ASD normalized correctly; electronics separated; same-state R and noise |
| Dynamics | external/package transfer bounded/de-embedded; injection dependence checked |

No row should be converted into a numerical production tolerance until repeated local data justify one.

---

# 22. Apparatus-dependent quantities that must be instantiated locally

These are not manuscript omissions. They are coordinates that physically depend on the executing hardware/material lot.

## 22.1 LPE

- boat dimensions, well volume, fill height and total charge mass;
- furnace-controller-to-melt temperature offsets/gradients;
- N2/H2 flow and gas-quality criteria;
- exact contact interval giving the required thickness;
- slider speed/clearance/wipe geometry;
- Hg-source mass sufficient for the local enclosure and depletion history.

## 22.2 Anneal

- ampoule free volume and source/sample geometry;
- sample and reservoir thermometry offsets;
- Hg inventory sufficient for the local boundary condition;
- actual cooldown trajectory;
- time/temperature needed for the starting defect state.

## 22.3 Lithography/wet chemistry

- exact mathematical Br2 formulation basis;
- HBr stock assay;
- agitation and measured etch rate;
- Mask-1 resist/product/process;
- Mask-2 resist product, spin, exposure, developer, chlorobenzene order, lift-off solvent;
- oxide EG/water ratio basis and cell dimensions.

## 22.4 RIE

- exact CH4/H2 local gas realization;
- MFC calibration;
- RF frequency/electrode geometry;
- self-bias/ion-energy proxy;
- sample temperature;
- chamber seasoning;
- oxide-clear time.

## 22.5 Metallization

- deposition method/tool;
- base/process vacuum;
- Cr/Au rate;
- QCM tooling factor;
- sample thermal load;
- allowable RIE-to-Cr delay.

## 22.6 Singulation/package

- exact cutting tool/abrasive/feed/support/protection;
- released functional edge exclusion;
- attachment product/bondline/cure;
- wire-bond parameters;
- cold-shield/window/aperture geometry;
- package thermal transfer.

## 22.7 Metrology

- Hall magnet/current/voltage/temp implementation;
- FTIR reference, footprint, spectral resolution and reduction version;
- calibrated radiometric reference detector/monochromator geometry;
- preamplifier/analyzer transfer and ENBW convention;
- dynamic-source/electronics/package transfer functions.

A competent laboratory completes these fields by calibration/qualification, not by searching for a universal number that does not exist.

---

# 23. Minimum run traveler/data package

A complete qualification build shall preserve:

1. source-material and substrate genealogy;
2. final CdZnTe surface recipe and clean-to-load times;
3. exact LPE charge calculation and actual masses;
4. boat revision, source inventory, gas and full growth T(t);
5. as-grown P05/P06 data;
6. full anneal T_s(t), T_Hg(t), source history and post-anneal P05/P06;
7. Mask-1 resist/exposure/develop data;
8. wet-etch formulation mathematics, bath genealogy, depth/CD/isolation;
9. anodization cell/electrolyte/A_exposed/I/V(t)/Q/A/thickness;
10. Mask-2 thickness, bake, chlorobenzene branch, exposure/developer/profile;
11. RIE MFC/plasma/pressure/self-bias/temperature/t_clear/t_sem/witness data;
12. RIE-to-Cr timestamps;
13. Cr/Au source/vacuum/rate/QCM/witness thickness and lift-off inspection;
14. final geometry/contact map and TLM;
15. P10 bare-device DC/self-heating data;
16. pre-singulation optical/noise/dynamic baseline where feasible;
17. singulation process/edge/subsurface/functional disposition;
18. package construction, bondline, interconnect, optical geometry and thermal response;
19. final P11 absolute responsivity files;
20. final P12 raw PSD/ASD, electronics calibration, NEP and D* reduction;
21. final P13 raw transient/frequency data and de-embedding;
22. uncertainties, deviations, rework and nonconformances;
23. final comparison against RP-01 anchors.

A scientifically useful run with missing items may be reported, but it is not a complete reproducibility record.

---

# 24. Troubleshooting logic

## 24.1 Layer composition/thickness wrong

Check, in order:

- charge mass calculation and actual Cd weighing;
- actual melt temperature/liquidus offset;
- contact supercooling and T(t);
- source age/depletion/Hg loss;
- contact time;
- spatial temperature/overlap/wipe behavior.

Do not compensate a thermometry error by silently changing charge composition.

## 24.2 Residual melt / rough LPE surface

Check:

- substrate polarity/wetting;
- slider clearance and flatness;
- wipe-off element geometry/contact;
- separation speed/stick-slip;
- thermal trajectory at separation;
- Hg-source/solution history.

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
- temperature sensor placement.

Recalibrate etch rate after any chemistry/agitation/resist change.

## 24.5 Oxide thickness or V(t) drifts

Check:

- electrolyte preparation basis/age;
- KOH assay;
- A_exposed/current-density calculation;
- cathode/anode geometry;
- starting wet-etch surface and air-exposure clock;
- bath temperature;
- film dissolution during/after formation.

## 24.6 High contact resistance

Separate:

- RIE electrical conversion failure;
- oxide not fully cleared;
- long/uncontrolled RIE-to-metal delay;
- contaminated/oxidized interface;
- wrong Cr thickness/poor film continuity;
- TLM fitting/geometry error.

Do not introduce an ion mill/wet clean without treating it as a new contact process.

## 24.7 Excess 1/f noise

Check:

- detector bias/self-heating;
- contact/TLM state;
- passivation/interface history;
- package/interconnect stress/microphonics;
- readout electronics floor/loading;
- optical background;
- actual signal frequency relative to knee.

## 24.8 Apparent slow lifetime

Check package thermal recovery, AC-coupling/high-pass response, source pulse tail, preamplifier recovery, injection level, and interface trapping before attributing the pole to bulk recombination.

---

# 25. Historical gaps that remain deliberately open

The following do not prevent this manual from being used as a reference/qualification process, but they prevent an unqualified claim of literal historical identity:

- exact RP-01 CdZnTe Zn fraction, plane/polarity/miscut and final surface recipe;
- exact Fermionics/UWA LPE boat dimensions, charge mass, source synthesis, gas flows, contact/wipe/cooldown;
- exact RP-01 Hg anneal apparatus/source/trajectory;
- exact Mask-1 resist/process and wet-mesa chemistry;
- exact UWA anodization electrolyte/cell/current program;
- exact Mask-2 resist product/exposure/developer/chlorobenzene ordering/lift-off solvent;
- exact Plasma Technology reactor model, RF frequency, electrode geometry, self-bias, sample temperature and individual MFC settings;
- exact RP-01 deposition method, base pressure, rates, QCM factors and RIE-to-metal air break;
- exact historical contact pair/gap used for each performance curve;
- exact 4.4-µm cutoff convention;
- exact Optronics spectral-system configuration and reference chain;
- exact low-noise preamplifier and HP35665A settings;
- exact 1-kHz noise convention used in the published D* curve;
- exact singulation method/die outline;
- exact package/interconnect/optical construction;
- direct RP-01 lifetime/frequency-response result.

“Not recovered” is not equivalent to “did not exist.”

---

# 26. Reference-source crosswalk

The integrated procedure is based principally on the following controlled source families already audited in the repository:

1. Smith et al. 2001 — canonical RP-01 photoconductor process/performance.
2. Hansen, Schmit, Casselman 1982 — HgCdTe band gap versus composition/temperature.
3. Harman 1980 — Te-rich LPE growth/liquidus/process behavior.
4. Schmit, Hager, Wood 1982 — Te-rich LPE including x≈0.30.
5. Radhakrishnan, Sitharaman, Gupta 2003 — executable horizontal-slider/source-preparation details.
6. Bowers & Schmit / Honeywell — xL=.082, yL=.810, TL=507 °C tie line and Hg-containment architecture.
7. Hager & Wood / Honeywell — residual-melt wipe-off architectures.
8. Tranchart et al. — CdZnTe near 4% Zn for x≈0.30 LPE.
9. Nagahama et al., Harman, Jones et al., Chandra/Schaake/Kinch — Hg-rich anneal process/defect control.
10. Smith et al. 2000 — same-UWA wet-mesa detector evidence.
11. Srivastav et al. 2005 — quantitative Br2/EG/HBr mesa process behavior.
12. Texas Instruments US3977018 — HgCdTe photoconductor anodic-oxide branch.
13. Musca/Siliquini/Smith/Faraone UWA RIE studies — electrical conversion/LBIC/process physics.
14. Semu et al.; Elkind & Orloff — CH4/H2 RIE self-bias, chemistry, morphology/orientation effects.
15. same-UWA HgCdTe metallization work plus primary HgCdTe contact studies — deposition-method/interface transfer.
16. van der Pauw/NIST Hall guidance and Tsen et al. — transport metrology/multicarrier control.
17. Hougen 1989 — HgCdTe transmission/composition/thickness modeling.
18. NIST-style spectral comparator principles — absolute responsivity traceability.
19. Bartoli et al. and related HgCdTe PC package thermal work — package thermal de-embedding.
20. UWA transient-photoconductive-decay work — historical same-lineage dynamic measurement branch.

The controlled repository source ledger remains authoritative for complete bibliographic metadata, evidence class, and transfer restrictions.

---

# 27. Internal procedure crosswalk

For detailed travelers, derivations, uncertainty budgets, and qualification experiments use:

- P29 / P07 family — CdZnTe substrate/final surface;
- P30 / P03 family — LPE growth;
- P05 — Hall/VdP;
- P06/P06A — FTIR composition/thickness;
- P31 / P04/P23 — Hg anneal;
- P32 / P14 — Mask 1;
- P28/P28A / P01 — wet mesa;
- P25/P25A / P02 — anodic oxide;
- P27 / P14A — Mask 2/lift-off resist;
- P34 / P08/P24 — RIE blocking contact;
- P26/P26A / P09 — Cr/Au and TLM;
- P10/P10A — DC field/self-heating;
- P35 — singulation;
- P33/P15 — package/interconnect;
- P11/P11A — absolute responsivity;
- P12/P12B/P12C — noise/NEP/D*;
- P13/P13A — dynamics/lifetime;
- P16 — master traveler;
- P18 — deviations/failure analysis;
- P20/P20A — uncertainty propagation.

---

# 28. Current manuscript status

This Draft 0.1 establishes one coherent reference/qualification route from substrate through final detector characterization. The principal remaining work before issuing a polished final booklet is editorial and integration work rather than another open-ended search for universal apparatus setpoints:

1. add figures/schematics and compact process-flow diagrams;
2. convert the internal procedure crosswalk into appendices/checklists;
3. normalize symbols, units and evidence labels across chapters;
4. integrate full uncertainty tables and example calculations;
5. compile the complete reference list from the controlled source ledger;
6. perform an adversarial technical review for contradictions, unsafe ambiguities, and unsupported claims;
7. typeset the final document as a professional PDF/booklet.

The absence of a specific laboratory's furnace offsets, MFC calibration, QCM tooling factor, resist dose, bondline thickness, or optical view factor is **not** treated as a manuscript-content failure. Those are explicitly defined local instantiation fields whose acceptance methods are now part of the procedure.
