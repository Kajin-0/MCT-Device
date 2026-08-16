# P16C — minimum laboratory capability implementation register

**Status:** CONTROLLED PRE-BUILD IMPLEMENTATION REGISTER / ROUND 41  
**Date:** 2026-08-16 America/New_York  
**Use with:** `docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`, P16A, P16B.

## 1. Purpose

Provide the fill-in record a future laboratory must complete to demonstrate that the P16B candidate branch has actual physical infrastructure behind it.

P16C does not change any P16A row automatically.

Allowed capability states:

- `NOT-INSTANTIATED`
- `IDENTIFIED-NOT-CALIBRATED`
- `SURROGATE-COMMISSIONED`
- `LOCAL-CALIBRATED`
- `HGCDTE-QUALIFICATION-PENDING`
- `HGCDTE-QUALIFIED`
- `EH&S-BLOCKED`
- `NOT-REQUIRED-FOR-SELECTED-BRANCH`

Project-level maturity remains separately controlled by P16A/P17.

---

# 2. Register header

Laboratory/facility: ____________________  
Responsible engineer: ____________________  
P16C revision: ____________________  
P16B revision/commit: ____________________  
P16A register revision: ____________________  
Date opened: ____________________  
Intended first-build branch ID: ____________________

---

# 3. Global calibration / genealogy infrastructure

| ID | Capability | Actual implementation | Calibration/traceability ID | State | P16A dependency |
|---|---|---|---|---|---|
| G01 | raw-data/versioned storage |  |  | NOT-INSTANTIATED | R35 |
| G02 | instrument calibration registry |  |  | NOT-INSTANTIATED | R35 |
| G03 | sample genealogy IDs |  |  | NOT-INSTANTIATED | R35 |
| G04 | deviation/nonconformance control |  |  | NOT-INSTANTIATED | R35 |
| G05 | timestamp synchronization / handoff clocks |  |  | NOT-INSTANTIATED | R14/R20/R35 |

---

# 4. C01 — source weighing / mass accounting

Actual balance(s): ____________________  
Calibration range: ____________________  
Readability: ____________________  
Measured repeatability at expected Cd mass: ____________________  
Measured linearity/bias: ____________________  
Current selected `M_charge`: ____________________ (`LOCAL-BLANK` until P30A capacity is closed)

Controlled mass-fraction convention:

- Hg `0.2497382358`
- Cd `0.01250164993`
- Te `0.7377601143`

State: ____________________  
Supports P16A: R01/R05.

---

# 5. C02 — LPE system

## Tool identity

Furnace/tube ID: ____________________  
Boat revision: ____________________  
Slider/actuator ID: ____________________  
N2 gas train ID: ____________________  
H2 gas train ID: ____________________

## HARD-MINIMUM evidence

| Item | Required evidence | Actual | State |
|---|---|---|---|
| process-region thermal coverage | calibrated around ~495–520 °C engineering envelope |  |  |
| local 507 °C tie-line neighborhood measurable | yes |  |  |
| above-liquidus operation demonstrated | yes |  |  |
| N2 purge -> H2 process sequence possible | yes |  |  |
| growth-well/recess/plug geometry dimensioned | yes |  |  |
| room-temperature well volume measured | yes |  |  |
| hot slider motion/position repeatability measured | yes |  |  |
| source/substrate-region thermal map | yes |  |  |
| MFC/flow calibration | gas-specific |  |  |
| pressure/backpressure state defined | if applicable |  |  |

## Local blanks remaining after surrogate commissioning

`M_charge`: __________  
Hg/HgTe source inventory: __________  
`TL_local`: __________  
above-liquidus hold: __________  
`DeltaT_SC`: __________  
`t_contact`: __________  
cooling rate: __________  
separation/wipe trajectory: __________

State: ____________________  
Supports P16A: R04/R05/R06/R07.

---

# 6. C03 — Hg anneal system

Anneal enclosure/ampoule revision: ____________________  
Sample-zone sensor: ____________________  
Hg-reservoir-zone sensor: ____________________  
Hg source/reservoir geometry: ____________________  
Seal/leak method: ____________________

| Item | Required capability | Actual | State |
|---|---|---|---|
| sample temperature | stable around 250 °C first screen |  |  |
| mapping range | at least ~250–300 °C engineering region |  |  |
| `T_s(t)` logging | required |  |  |
| `T_Hg(t)` logging | required |  |  |
| loaded thermal map / cross-talk | required |  |  |
| cooldown trace | required |  |  |

Hg inventory: __________  
First-screen branch: `~250 °C / ~1 h / Hg-saturated-isothermal-like`  
Local released dwell/cooldown: __________

State: ____________________  
Supports P16A: R10/R11.

---

# 7. C04 — FTIR station

Instrument/model: ____________________  
Source/beamsplitter/detector: ____________________  
Mapping stage: ____________________  
Independent thickness method: ____________________

| Requirement | Current minimum | Actual | State |
|---|---:|---|---|
| spectral coverage | ~500–5000 cm^-1 |  |  |
| qualification resolution | <=4 cm^-1 unless sensitivity validates coarser |  |  |
| minimum map | 9 points |  |  |
| preferred development map | 5x5+ where geometry permits |  |  |
| physical thickness range | expected ~5–15 µm |  |  |
| wavenumber calibration | required |  |  |
| purge/vacuum path control | required where atmospheric artifacts matter |  |  |

Model/software version: ____________________  
Repeatability: ____________________  
Spot/aperture size: ____________________

State: ____________________  
Supports P16A: R08 and pre/post-anneal gates.

---

# 8. C05 — Hall/VdP station

Magnet: ____________________  
Field probe: ____________________  
Cryostat/stage: ____________________  
Current source: ____________________  
Voltage readout/switching: ____________________

| Requirement | Minimum / preferred | Actual | State |
|---|---|---|---|
| field | HARD-MINIMUM >= +/-0.50 T |  |  |
| extended field | preferred up to ~+/-2 T |  |  |
| temperature | ~80 K and 300 K |  |  |
| current reversal | required |  |  |
| field reversal | required |  |  |
| measured B at sample | required |  |  |
| detector/sample dark enclosure | required |  |  |

Initial P05 field grid support: ____________________  
Hall standard/surrogate verification: ____________________

State: ____________________  
Supports P16A: R09 and P31 outcome qualification.

---

# 9. C06 — lithography / wet chemistry / anodization

Spin coater: ____________________  
Bake tool(s): ____________________  
Aligner/exposure: ____________________  
Film-thickness metrology: ____________________  
CD/profile metrology: ____________________  
Wet-chemistry station: ____________________  
Anodization current source/logger: ____________________

## Mask-2 direct-state capability

- 4–5 µm film: __________
- 80 °C / 30 min bake calibration: __________
- chlorobenzene 30-min controlled bath: __________
- measured exposure dose: __________
- developer identity/basis: __________
- post-RIE profile measurement: __________
- 300-nm-stack lift-off capability: __________

## Wet-mesa local definition

Br2 percentage basis: __________  
EG:HBr ratio basis: __________  
HBr stock assay: __________  
Bath temperature control around ~21 °C: __________  
Etch-depth/profile method: __________  
P28->P25 handoff clock: __________

## Anodization

Cell revision: __________  
Cathode material/geometry: __________  
`A_exposed`: __________ cm²  
Selected `J`: __________ mA/cm²  
Calculated `I=J A_exposed`: __________ mA  
Voltage logger range/compliance: __________  
`V(t)` logging: __________  
Oxide-thickness method near 80 nm: __________

State: ____________________  
Supports P16A: R12/R13/R14/R15/R16.

---

# 10. C07 — RIE

Tool/model/revision: ____________________  
RF frequency: ____________________  
Powered-electrode geometry: ____________________  
Pressure gauge: ____________________  
CH4 MFC: ____________________  
H2 MFC: ____________________  
Self-bias/sheath diagnostic: ____________________  
Sample-temperature method: ____________________

Direct controller center support:

- total flow 64 sccm: __________
- candidate CH4 10.6667 sccm: __________
- candidate H2 53.3333 sccm: __________
- pressure 100 mTorr: __________
- forward RF power 50 W: __________
- 60-s timed exposure: __________
- reflected-power logging: __________
- self-bias logging: __________
- chamber clean/season genealogy: __________

Oxide-clear calibration `t_clear`: __________  
Semiconductor exposure `t_sem`: __________

State: ____________________  
Supports P16A: R17/R18.

---

# 11. C08 — Cr/Au deposition

Tool/revision: ____________________  
Method family: ____________________  
Pump/gauge chain: ____________________  
Cr source hardware: ____________________  
Au source hardware: ____________________  
QCM/head/controller: ____________________  
Independent witness method: ____________________

| Requirement | Direct/candidate value | Actual | State |
|---|---:|---|---|
| Cr thickness | 30 nm |  |  |
| Au thickness | 270 nm |  |  |
| Cr tooling factor | separate calibration required |  |  |
| Au tooling factor | separate calibration required |  |  |
| base/deposition pressure logging | required, no preassigned numeric spec |  |  |
| sample thermal proxy | required |  |  |
| RIE->Cr timestamps/atmosphere | required |  |  |
| Cr->Au vacuum history | required |  |  |

Selected Cr rate: __________  
Selected Au rate: __________  
Local base-pressure criterion: __________

State: ____________________  
Supports P16A: R19/R20.

---

# 12. C09 — integrated 77–80 K detector station

Cryostat/Dewar: ____________________  
Temperature sensor/controller: ____________________  
Bias/load network: ____________________  
Low-noise preamp: ____________________  
Spectrum analyzer/digitizer: ____________________  
Monochromator/source: ____________________  
Reference detector: ____________________  
Chopper/modulator: ____________________  
Fast optical source/reference detector: ____________________

## Shared detector state

Device: __________  
Contact pair: __________  
Measured L/W/t: __________  
Package revision: __________  
Temperature: __________  
Electric field: __________  
Background/FOV geometry: __________  
Window/filter: __________  
Load network: __________

## DC/bias

- stable ~80 K: __________
- 10 V/cm canonical point: __________
- safe characterization toward ~50 V/cm where qualified: __________
- active-region voltage measurement: __________
- current/power/self-heating proxy: __________

## Radiometry

- useful MWIR + beyond-edge coverage, first-build ~2–6 µm envelope: __________
- 4 µm calibrated point: __________
- through/beyond ~4.4 µm edge: __________
- 1-kHz chopping: __________
- wavelength calibration: __________
- reference-detector traceability: __________
- view-factor/aperture geometry: __________

## Noise

- calibrated 100 Hz–10 kHz historical-band coverage: __________
- below-100-Hz extension: __________
- above-10-kHz extension: __________
- electronics-floor ASD: __________ nV/sqrtHz
- complex gain/impedance calibration: __________
- FFT/window/ENBW validation: __________
- Johnson-noise validation: __________

If PSD budget fraction `beta` is selected: __________  
Derived floor target `24.5*sqrt(beta)`: __________ nV/sqrtHz.

## Temporal

- 10–100 Hz low-end where practical: __________
- 1 kHz / 10 kHz / 100 kHz / 1 MHz support: __________
- extension to >=5–10x observed f3dB: __________
- source complex transfer: __________
- electrical transfer: __________
- package thermal kernel: __________
- pulse capability, if used: __________

State: ____________________  
Supports P16A: R22/R23/R24/R25/R26/R27.

---

# 13. C10 — singulation

Tool/method: ____________________  
Selected first-screen family: ____________________  
Support/protection: ____________________  
Abrasive/slurry: ____________________  
Street geometry: ____________________  
Kerf/wander measurement: ____________________  
Edge inspection: ____________________  
Subsurface-damage method/proxy: ____________________  
Clean/release sequence: ____________________

Compatibility of completed oxide/Cr/Au stack demonstrated: __________  
Pre/post electrical/noise/responsivity comparison available: __________

State: ____________________  
Supports P16A: R28/R29.

---

# 14. C11 — package / Dewar / interconnect

Carrier/cold finger: ____________________  
Die attach product/lot: ____________________  
Bondline measurement: ____________________  
Interconnect wire/ribbon: ____________________  
Bonder/tool: ____________________  
Vacuum/purge system: ____________________  
Window/filter: ____________________  
Aperture/shield geometry: ____________________

| Requirement | Actual | State |
|---|---|---|
| repeatable 77–80 K operation |  |  |
| bondline thickness/coverage/void record |  |  |
| interconnect resistance/noise check |  |  |
| measured package thermal response |  |  |
| measured optical geometry/transmission |  |  |
| pressure/pump/bake/cooldown record |  |  |
| repeated thermal-cycle capability |  |  |

State: ____________________  
Supports P16A: R30/R31/R32/R33/R34.

---

# 15. C12 — auxiliary metrology/access

Record whether capability is in-house, shared facility or external service.

| Capability | Implementation | Availability/turnaround | Calibration/traceability | State |
|---|---|---|---|---|
| optical CD/dimensional microscopy |  |  |  |  |
| profilometry / step thickness |  |  |  |  |
| oxide thickness |  |  |  |  |
| metal witness thickness |  |  |  |  |
| surface/profile roughness |  |  |  |  |
| edge/subsurface inspection |  |  |  |  |
| gas-flow calibration |  |  |  |  |
| pressure-gauge calibration |  |  |  |  |
| thermometer calibration |  |  |  |  |
| magnetic-field calibration |  |  |  |  |
| wavelength/radiometric calibration |  |  |  |  |

---

# 16. EH&S / facility authorization register

| Hazard/capability | Institutional authorization/control | State |
|---|---|---|
| Hg / Hg-containing waste |  |  |
| Cd/HgCdTe/CdZnTe contamination |  |  |
| Br2 / HBr wet chemistry |  |  |
| H2 gas |  |  |
| CH4 gas |  |  |
| high-temperature sealed ampoule |  |  |
| chlorobenzene/solvents |  |  |
| RF plasma/vacuum |  |  |
| cryogens |  |  |

Any `EH&S-BLOCKED` state prevents physical execution regardless of scientific readiness.

---

# 17. P16C disposition

Mandatory first-build capabilities instantiated: YES / NO  
All required surrogate commissioning complete: YES / NO  
All critical calibration records current: YES / NO  
All HgCdTe-only blanks clearly identified: YES / NO  
EH&S/facility authorized: YES / NO  
P16A mapping reviewed: YES / NO

Final P16C state:

`P16C-INFRASTRUCTURE-READY = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** `P16C-INFRASTRUCTURE-READY = YES` does not itself set `TRACEABLE-FIRST-BUILD-READY = YES`.
