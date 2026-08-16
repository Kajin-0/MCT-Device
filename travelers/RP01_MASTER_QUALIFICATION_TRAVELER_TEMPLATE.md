# RP-01 master qualification traveler — blank template

**Traveler ID:** ____________________  
**Revision:** ____________________  
**Date opened:** ____________________  
**Lead operator/researcher:** ____________________

> This is a blank execution record for the controlled qualification flow in `procedures/P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`. It is not a substitute for the detailed P01–P15 procedures.

## Status legend

`NOT STARTED / IN PROCESS / HOLD-DATA / HOLD-REVIEW / PASS / PASS-CONDITIONAL / FAIL / SCRAPPED / REWORK AUTHORIZED`

---

# 0. Process configuration

- RP-01 process revision: ____________________
- P01–P16 revisions: ____________________
- source-ledger revision/addenda: ____________________
- target x: ____________________
- target HgCdTe thickness: ____________________
- target Hall state / measurement T: ____________________
- target device/contact geometry: ____________________
- intended operating T: ____________________
- pre-approved deviations: ____________________

**Configuration status:** ____________________

---

# A. Facility / incoming material / substrate

## A0 Calibration and authorization readiness

| Item | Equipment/record ID | Due/current? | Status | Initial/date |
|---|---|---|---|---|
| Balance | | | | |
| Furnace thermometry | | | | |
| Gas MFCs | | | | |
| Pressure/vacuum gauges | | | | |
| Hall B-field / thermometry | | | | |
| FTIR | | | | |
| RIE | | | | |
| QCM/metal thickness | | | | |
| Lithography dose/spin/hotplate | | | | |
| Cryogenic thermometry | | | | |
| Electrical/noise chain | | | | |
| EHS/facility authorization | | | | |

**Gate A0:** ____________________

## A1 Source-material lots

| Material | Lot ID | Supplier | Purity | CoA ref | Received/open date | PASS? |
|---|---|---|---|---|---|---|
| Hg | | | | | | |
| Cd | | | | | | |
| Te | | | | | | |

## A2 CdZnTe substrate — P07

- Substrate ID: ____________________
- Dimensions/thickness: ____________________
- Zn/lattice mismatch metric: ____________________
- A/B polarity: ____________________
- Miscut magnitude/azimuth: ____________________
- HRXRD metric: ____________________
- EPD/dislocation metric: ____________________
- IR inclusion/precipitate map ref: ____________________
- Trace impurity data ref: ____________________
- Resistivity/leakage: ____________________
- Surface roughness/polish: ____________________
- Micrograph/data refs: ____________________

**Gate A2:** ____________________

---

# B. Charge preparation / LPE — P03

## B0 Boat / growth-well configuration

- Boat ID/revision: ____________________
- Growth-well dimensions: ____________________
- Melt depth/volume: ____________________
- Substrate recess: ____________________
- Hg source geometry: ____________________
- Cover configuration: ____________________
- Wipe-off configuration: ____________________
- Temperature-sensor positions: ____________________
- Previous run/clean state: ____________________

**Gate B0:** ____________________

## B1 Charge

- Charge ID: ____________________
- Total target mass M: ____________________

| Element | Target mass | Actual mass | Balance ID | Uncertainty |
|---|---:|---:|---|---|
| Hg | | | | |
| Cd | | | | |
| Te | | | | |

- Calculated actual xL: ____________________
- Calculated actual yL: ____________________
- Deviation from target: ____________________
- Calculation file ref: ____________________

**Gate B1:** ____________________

## B2 Charge synthesis

- Ampoule/container ID: ____________________
- Loading sequence: ____________________
- Vacuum/backfill: ____________________
- Temperature-time program ref: ____________________
- Rocking/agitation: ____________________
- Cooldown: ____________________
- Final state/inspection: ____________________

**Gate B2:** ____________________

## B3 Final substrate clean/load

- Surface-prep recipe/revision: ____________________
- Start/end time: ____________________
- Rinse/dry: ____________________
- Inspection: ____________________
- LPE load time: ____________________
- `Δt_clean→load`: ____________________

**Gate B3:** ____________________

## B4 Atmosphere/equilibration

- N2 purge: ____________________
- H2 flow: ____________________
- Residual O2/H2O if measured: ____________________
- Pressure: ____________________
- Hg source ID/mass/T: ____________________
- Temperature trace ref: ____________________
- Equilibration interval: ____________________
- Equilibrium criterion: ____________________

**Gate B4:** ____________________

## B5 Growth

- LPE run ID: ____________________
- Contact time: ____________________
- T at contact: ____________________
- Supercooling/trajectory: ____________________
- Growth duration: ____________________
- Full trace ref: ____________________
- Excursions: ____________________

**Gate B5:** ____________________

## B6 Termination / wipe-off

- Separation time/T: ____________________
- Slider speed/direction: ____________________
- Wiper config: ____________________
- Residual melt: ____________________
- Scratch/damage: ____________________

**Gate B6:** ____________________

---

# C. As-grown material gate — P05/P06

## C1 Morphology

- Whole-wafer image ref: ____________________
- Droplets/pinholes/voids: ____________________
- Cracks/scratches: ____________________
- Usable-area map: ____________________

**Gate C1:** ____________________

## C2 FTIR/thickness — P06

- Dataset: ____________________
- Map pattern: ____________________
- Mean thickness: ____________________
- Thickness range/nonuniformity: ____________________
- Edge metric: ____________________
- Inferred x/model: ____________________
- Composition/edge range: ____________________

**Gate C2:** ____________________

## C3 Hall/VdP — P05

- Coupon ID: ____________________
- T: ____________________
- B grid: ____________________
- VdP consistency: ____________________
- Carrier sign: ____________________
- `n_H/p_H`: ____________________
- `µ_H`: ____________________
- Multicarrier flag/model: ____________________

**Gate C3:** ____________________

---

# D. Hg anneal — P04

## D1 Setup

- Sample/coupon IDs: ____________________
- Reactor/ampoule: ____________________
- Hg source: ____________________
- Geometry: ____________________
- pHg/chemical-potential method: ____________________

## D2 Run

- Ramp: ____________________
- Sample T: ____________________
- Hg source T / pHg proxy: ____________________
- Soak time: ____________________
- Cooldown: ____________________
- Trace ref: ____________________

## D3 Post-anneal P06

- Dataset: ____________________
- Δ thickness: ____________________
- Δ edge/x: ____________________

**Gate D3:** ____________________

## D4 Post-anneal P05

- T: ____________________
- Carrier sign: ____________________
- `n_H`: ____________________
- `µ_H`: ____________________
- Model/linearity: ____________________

**Gate D4:** ____________________

---

# E. Device fabrication

## E1 Mask 1 — P14

- Resist/lot: ____________________
- Spin: ____________________
- Thickness: ____________________
- Bake: ____________________
- Mask ID/rev: ____________________
- Exposure: ____________________
- Develop: ____________________
- CD map ref: ____________________

**Gate E1:** ____________________

## E2 Wet mesa — P01

- Etchant composition + concentration basis: ____________________
- Reagent lots: ____________________
- Bath T: ____________________
- Time/agitation: ____________________
- Rinse/quench: ____________________
- Depth: ____________________
- Undercut/CD: ____________________
- Surface/sidewall: ____________________

**Gate E2:** ____________________

## E3 Anodic oxide — P02

- Electrolyte: ____________________
- T: ____________________
- J: ____________________
- V(t) dataset: ____________________
- Endpoint/time: ____________________
- Rinse/dry: ____________________
- Measured oxide thickness: ____________________

**Gate E3:** ____________________

## E4 Mask 2 — P14

- Resist/lot: ____________________
- Spin/thickness: ____________________
- Prebake: ____________________
- Chlorobenzene soak: ____________________
- Exposure: ____________________
- Development: ____________________
- Opening CD: ____________________
- Overhang/profile metric: ____________________
- Mask1 overlay: ____________________

**Gate E4:** ____________________

## E5 RIE — P08

- Tool ID: ____________________
- CH4 actual flow: ____________________
- H2 actual flow: ____________________
- Total flow: ____________________
- Pressure: ____________________
- RF frequency/power: ____________________
- Self-bias: ____________________
- Sample T: ____________________
- Time: ____________________
- Oxide-clear result: ____________________
- HgCdTe recession: ____________________
- n+ Hall/LBIC witness: ____________________
- Conversion depth/lateral extent: ____________________

**Gate E5:** ____________________

## E6 RIE → metal clock

- RIE off: ____________________
- Vent/ambient exposure: ____________________
- Metal tool load: ____________________
- Cr deposition start: ____________________
- `Δt_RIE→Cr`: ____________________

**Gate E6:** ____________________

## E7 Cr/Au — P09

- Tool/method: ____________________
- Base pressure: ____________________
- Cr rate/thickness: ____________________
- Au rate/thickness: ____________________
- QCM/witness ref: ____________________
- Substrate T: ____________________

**Gate E7:** ____________________

## E8 Lift-off

- Solvent: ____________________
- T/time/agitation: ____________________
- Rinse/dry: ____________________
- Inspection: ____________________

**Gate E8:** ____________________

## E9 Final geometry — P14

| Device | Contact pair | Pad W/L | Actual gap | Active width | Active area | Mesa dims | PASS? |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Gate E9:** ____________________

## E10 TLM — P09

- Dataset: ____________________
- T: ____________________
- Fit range/R²: ____________________
- `ρc`: ____________________
- I–V linearity: ____________________

**Gate E10:** ____________________

---

# F. Bare-die baseline — P10–P13

## F1 P10 electrical

- Device/contact pair: ____________________
- T: ____________________
- Gap: ____________________
- Safe E range: ____________________
- I/V/P at canonical field: ____________________
- Self-heating: ____________________
- Sweepout: ____________________

**Gate F1:** ____________________

## F2 Optional pre-package optical/noise/dynamic

- P11 dataset: ____________________
- P12 dataset: ____________________
- P13 dataset: ____________________

---

# G. Package / interconnect — P15

## G1 Singulation

- Tool/process: ____________________
- Final die dimensions: ____________________
- Edge damage: ____________________

**Gate G1:** ____________________

## G2 Die attach

- Carrier/cold finger: ____________________
- Attach material/lot: ____________________
- Bondline: ____________________
- Cure/T history: ____________________
- Position/tilt: ____________________

**Gate G2:** ____________________

## G3 Wire bond

- Wire material/diameter: ____________________
- Bonder/tool/program: ____________________
- Force/ultrasonic/time/stage T: ____________________
- Bond map: ____________________
- Pull-test coupon ref: ____________________

**Gate G3:** ____________________

## G4 Optical/vacuum assembly

- Window/filter: ____________________
- Aperture/shield geometry: ____________________
- Calculated FOV: ____________________
- Vacuum/pump/bake: ____________________
- Sensor location/calibration: ____________________

**Gate G4:** ____________________

## G5 Cryogenic package qualification

- Cooldown trace: ____________________
- Post-package P10 comparison: ____________________
- P12 comparison: ____________________
- P11 comparison: ____________________
- P13 comparison: ____________________
- Thermal-cycle record: ____________________

**Gate G5:** ____________________

---

# H. Final performance

## H1 P11 absolute spectral responsivity

- Dataset: ____________________
- Optical calibration ref: ____________________
- T/E/f/background/FOV: ____________________
- `Rλ` summary: ____________________

## H2 P12 noise / NEP / D*

- Dataset: ____________________
- Noise signal frequency: ____________________
- ASD/PSD/ENBW: ____________________
- Electronics floor: ____________________
- Active area: ____________________
- NEP: ____________________
- D*: ____________________
- 1/f knee / g-r level: ____________________

## H3 P13 temporal response

- Dataset: ____________________
- De-embedding refs: ____________________
- `f_3dB`: ____________________
- `tau_eff`: ____________________
- One-pole valid? ____________________
- 1-kHz attenuation: ____________________

---

# Deviations / holds / rework

| No. | Step | Intended | Actual/deviation | Physical concern | Extra metrology | Disposition/approval |
|---|---|---|---|---|---|---|
| | | | | | | |

---

# Elapsed-time control table

| Interval | Start | End | Δt | Current limit | PASS? |
|---|---|---|---|---|---|
| substrate clean → LPE load | | | | | |
| growth → first metrology | | | | | |
| anneal → metrology | | | | | |
| mesa etch → passivation | | | | | |
| anodization → Mask2 | | | | | |
| Mask2 develop → RIE | | | | | |
| RIE → Cr | | | | | |
| Au → lift-off | | | | | |
| lift-off → electrical test | | | | | |
| singulation clean → attach | | | | | |
| attach → wire bond | | | | | |
| pump/bake → cold test | | | | | |

---

# Final disposition

- [ ] QUALIFICATION RUN — COMPLETE
- [ ] QUALIFICATION RUN — FAILED
- [ ] LOCAL PROCESS QUALIFIED
- [ ] REWORK REQUIRED
- [ ] SCRAPPED
- [ ] REPRODUCIBLE-RELEASE — only if P16 release rule is satisfied

**Reviewer:** ____________________  
**Date:** ____________________

**Comments / unresolved items:**

__________________________________________________________________

__________________________________________________________________
