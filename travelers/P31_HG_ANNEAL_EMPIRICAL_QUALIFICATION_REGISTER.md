# P31 — Hg-overpressure anneal empirical qualification register

**Status:** blank controlled traveler. One record per anneal run/ampoule.

## A. Run identity

- P31 run ID:
- date/time:
- operator:
- furnace/tool ID:
- furnace revision:
- ampoule/enclosure ID:
- enclosure architecture: `SEALED-ISOTHERMAL / SEALED-TWO-ZONE / IN-SITU / OPEN-TUBE / OTHER`
- recipe/version:
- linked P30 growth run:
- linked P29 substrate lot:
- linked P04/P23 DOE condition:

## B. Starting specimen state

- coupon/wafer ID:
- wafer coordinate:
- dimensions:
- thickness of HgCdTe:
- nominal/measured x:
- optical edge metric and convention:
- P05 pre-anneal carrier-state label:
- Hall measurement T:
- Hall B range:
- signed RH/slope:
- n/p where valid:
- mobility where valid:
- sheet resistance:
- Hall curvature/multicarrier flag:
- surface/passivation state:
- pre-anneal morphology images:
- defect/EPD/precipitate metric:
- prior thermal history:

## C. Hg source / reservoir

- source class: `ELEMENTAL-HG / HgTe / OTHER`
- supplier:
- lot:
- purity:
- initial source mass:
- final source mass:
- source mass uncertainty:
- source vessel material:
- source vessel dimensions:
- estimated free surface area:
- source reuse count:
- prior source thermal cycles:

## D. Ampoule / enclosure geometry

- quartz/material grade:
- ID:
- OD:
- total internal length:
- sample-zone length:
- reservoir-zone length:
- sample-to-reservoir axial spacing:
- free internal volume:
- sample holder material:
- sample orientation:
- exposed sample area:
- reservoir orientation:
- seal method:
- evacuation/backfill procedure ID:
- terminal pressure before seal if measured:
- leak test result:

## E. Thermometry

### Sample zone
- sensor ID/type:
- calibration date:
- sensor location relative to sample:
- controller channel:
- controller-to-sample correction:
- uncertainty:

### Hg zone
- sensor ID/type:
- calibration date:
- sensor location relative to reservoir:
- controller channel:
- controller-to-source correction:
- uncertainty:

### Furnace map
- most recent axial-map ID:
- loaded/unloaded map:
- sample-zone gradient:
- Hg-zone gradient:
- cross-zone coupling note:

## F. Thermal / Hg trajectory

Record raw traces as attachments and summarize:

- start ambient T:
- ramp start:
- target sample T:
- target Hg-source T:
- actual mean sample T during dwell:
- actual sample T range:
- actual mean Hg T during dwell:
- actual Hg T range:
- mean `T_s - T_Hg`:
- dwell start definition:
- dwell start time:
- dwell end time:
- dwell duration:
- reconstructed pHg relation/version:
- reconstructed pHg during dwell:
- pHg uncertainty / evidence class:
- isothermal-like saturation evidence:
- visible/recorded Hg condensation event: Y/N
- specimen dissolution/deposition concern: Y/N

## G. Cooldown

- cooldown start:
- sample cooling method:
- reservoir cooling method:
- `T_s(t)` file:
- `T_Hg(t)` file:
- max/min `T_s-T_Hg` during cooldown:
- time to 200 °C:
- time to 100 °C:
- source-coupling end criterion:
- source-coupling end time/T:
- ampoule removal T:
- room-temperature time:
- uncontrolled interruption/quench: Y/N

## H. Post-run enclosure/source observations

- ampoule integrity:
- Hg location after run:
- wall condensation map/photo:
- specimen deposits:
- specimen attack/dissolution:
- source mass loss:
- unexpected residue:

## I. Post-anneal P05 state

- Hall measurement date:
- measurement T:
- B range:
- signed low-field Hall response:
- curvature:
- magnetoresistance:
- carrier-state label: `N-LIKE / P-LIKE / TRANSITION-MULTICARRIER`
- n/p where valid:
- mobility where valid:
- sheet resistance:
- one-carrier validity disposition:

## J. P06 optical / thickness closure

- pre/post same coordinates verified: Y/N
- pre edge metric:
- post edge metric:
- edge shift:
- repeatability/uncertainty:
- model-derived x pre:
- model-derived x post:
- thickness pre:
- thickness post:
- thickness shift:
- composition-preservation disposition:

## K. Morphology / defect closure

- whole-sample image:
- DIC/Nomarski:
- Hg/Te deposit evidence:
- pits/voids:
- cracks/delamination:
- EPD/defect metric pre:
- EPD/defect metric post:
- precipitate observation:

## L. Downstream detector bridge

Where applicable:

- P13 tau_eff:
- P11 responsivity:
- P12 noise/D*:
- P10 bias/self-heating result:
- detector/process ID:

## M. Statistical / genealogy fields

- matched-coupon group:
- independent ampoule run number:
- independent P30 growth-run number:
- Hg-source genealogy group:
- furnace revision group:
- include in P23 boundary model: Y/N
- include in n-like local Jacobian: Y/N
- exclusion reason:

## N. Disposition

- `FAIL-HARDWARE`
- `FAIL-THERMAL-TRACE`
- `FAIL-HG-BOUNDARY`
- `P-LIKE`
- `TRANSITION-MULTICARRIER`
- `N-LIKE-OUTSIDE-TARGET`
- `N-LIKE-CANDIDATE`
- `FAIL-OPTICAL-SHIFT`
- `FAIL-MORPHOLOGY/DEFECT`
- `LOCAL-QUALIFICATION-CANDIDATE`

Reviewer:
Date:
Notes:
