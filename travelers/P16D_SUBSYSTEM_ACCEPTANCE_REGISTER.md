# P16D — subsystem commissioning / acceptance register

**Status:** CONTROLLED PRE-BUILD ACCEPTANCE REGISTER / ROUND 42  
**Date:** 2026-08-16 America/New_York  
**Use with:** P36 and P16C.

## 1. Purpose

Provide the fill-in evidence register for future subsystem acceptance before HgCdTe process qualification.

P16D records whether each physical subsystem has passed:

`IQ -> OQ -> surrogate PQ -> HgCdTe residual qualification`.

P16D does not automatically change P16A readiness.

Allowed states:

- `AT-NOT-STARTED`
- `AT-IQ-PASS`
- `AT-OQ-PASS`
- `AT-SURROGATE-PQ-PASS`
- `AT-HGCDTE-RESIDUAL-PENDING`
- `AT-HGCDTE-PASS`
- `AT-CONDITIONAL`
- `AT-FAIL`
- `AT-EH&S-BLOCKED`
- `AT-NOT-APPLICABLE`

---

# 2. Register header

Laboratory/facility: ____________________  
Responsible engineer: ____________________  
P16D revision: ____________________  
P36 revision/commit: ____________________  
P16C revision/commit: ____________________  
P16B branch revision: ____________________  
Date opened: ____________________

---

# 3. Acceptance summary

| Subsystem | IQ | OQ | Surrogate PQ | HgCdTe residual | Overall state | Raw-data ID |
|---|---|---|---|---|---|---|
| LPE furnace/boat/gas/actuator |  |  |  |  | AT-NOT-STARTED |  |
| Hg anneal |  |  |  |  | AT-NOT-STARTED |  |
| FTIR |  |  |  |  | AT-NOT-STARTED |  |
| Hall/VdP |  |  |  |  | AT-NOT-STARTED |  |
| RIE |  |  |  |  | AT-NOT-STARTED |  |
| Cr/Au deposition |  |  |  |  | AT-NOT-STARTED |  |
| integrated 77–80 K detector station |  |  |  |  | AT-NOT-STARTED |  |
| singulation |  |  |  |  | AT-NOT-STARTED |  |
| package/Dewar/interconnect |  |  |  |  | AT-NOT-STARTED |  |

---

# 4. AT-LPE register

Tool/furnace ID: ____________________  
Boat revision: ____________________  
Slider/actuator ID: ____________________  
N2 train: ____________________  
H2 train: ____________________

## AT-LPE-01 geometry/capacity

Dimensioned drawing ID: ____________________  
`V_well,geom`: ____________________ ± ____________________  
Plug displacement: ____________________  
Substrate overlap geometry: ____________________  
Method/calibration ID: ____________________  
State: ____________________

## AT-LPE-02 hot motion

Temperature range tested: ____________________  
Position repeatability: ____________________  
Transit/contact timing uncertainty: ____________________  
Stick-slip/interference observed: YES / NO  
Raw-data ID: ____________________  
State: ____________________

## AT-LPE-03 thermal map

Sensor IDs/calibration: ____________________  
Range mapped: ____________________  
Controller-to-source correction: ____________________  
Controller-to-substrate correction: ____________________  
Source-substrate offset: ____________________  
Axial/transverse gradients: ____________________  
`U_DeltaT`: ____________________  
Can intended minimum `DeltaT_SC` be resolved: YES / NO  
State: ____________________

## AT-LPE-04 gases

N2 calibration ID: ____________________  
H2 calibration ID: ____________________  
Selected process flows: ____________________ (`LOCAL-BLANK` until branch frozen)  
Pressure/backpressure method: ____________________  
Sequence/interlock test: ____________________  
State: ____________________

## AT-LPE-05 synchronized logging

Temperature/gas/actuator clocks synchronized: YES / NO  
Timestamp uncertainty: ____________________  
Reconstructed dummy sequence reviewed: YES / NO  
State: ____________________

## AT-LPE-06 residual HgCdTe gates

- `TL_local`: ____________________
- `M_charge`: ____________________
- auxiliary Hg source: ____________________
- equilibration convergence: ____________________
- growth response: ____________________
- P06/P05 response: ____________________

Overall AT-LPE state: ____________________

---

# 5. AT-ANN register

Enclosure/ampoule revision: ____________________  
Furnace/zone IDs: ____________________  
Sample sensor: ____________________  
Reservoir sensor: ____________________

## AT-ANN-01 geometry

Sample/source positions dimensioned: YES / NO  
Free-volume/fixture record: ____________________  
State: ____________________

## AT-ANN-02 dual-temperature map

Range: ____________________  
`T_s` correction/uncertainty: ____________________  
`T_Hg` correction/uncertainty: ____________________  
Zone cross-talk: ____________________  
Cooldown response: ____________________  
State: ____________________

## AT-ANN-03 one-hour dummy dwell

Setpoint: ____________________  
Measured mean `T_s`: ____________________  
Measured mean `T_Hg`: ____________________  
Drift/stability: ____________________  
Timing uncertainty: ____________________  
State: ____________________

## AT-ANN-04 enclosure integrity

Method: ____________________  
Facility criterion: ____________________  
Result: ____________________  
State: ____________________

## AT-ANN-05 residual Hg/HgCdTe gates

Hg inventory/source state: ____________________  
P05/P06/P23 evidence: ____________________  
Released dwell/cooldown: ____________________

Overall AT-ANN state: ____________________

---

# 6. AT-FTIR register

Instrument/configuration: ____________________  
Calibration ID: ____________________

| Test | Requirement | Result | State |
|---|---|---|---|
| AT-FTIR-01 coverage | ~500–5000 cm^-1 |  |  |
| AT-FTIR-01 resolution | <=4 cm^-1 unless justified otherwise |  |  |
| AT-FTIR-02 baseline/repeatability | quantified |  |  |
| AT-FTIR-03 mapping | >=9-point geometry |  |  |
| AT-FTIR-03 stage registration | quantified |  |  |
| AT-FTIR-04 thickness reference | independent ~5–15 µm capability |  |  |

Beam/aperture footprint: ____________________  
Purge/vacuum state: ____________________  
Model/software version: ____________________  
HgCdTe optical-model validation: ____________________

Overall AT-FTIR state: ____________________

---

# 7. AT-HALL register

Magnet/probe: ____________________  
Cryostat: ____________________  
Current/voltage/switching chain: ____________________

## Field grid verification

| Nominal B (T) | Measured B | Uncertainty | +/− symmetry | State |
|---:|---:|---:|---|---|
| 0 |  |  |  |  |
| +0.01 |  |  |  |  |
| -0.01 |  |  |  |  |
| +0.025 |  |  |  |  |
| -0.025 |  |  |  |  |
| +0.05 |  |  |  |  |
| -0.05 |  |  |  |  |
| +0.10 |  |  |  |  |
| -0.10 |  |  |  |  |
| +0.20 |  |  |  |  |
| -0.20 |  |  |  |  |
| +0.50 |  |  |  |  |
| -0.50 |  |  |  |  |

Current-reversal PQ: ____________________  
Voltage-chain PQ: ____________________  
~80 K calibration: ____________________  
300 K calibration: ____________________  
Hall-reference result: ____________________  
HgCdTe residual result: ____________________

Overall AT-HALL state: ____________________

---

# 8. AT-RIE register

Tool/revision: ____________________  
RF frequency/electrode geometry: ____________________  
CH4 MFC: ____________________  
H2 MFC: ____________________  
Pressure gauge: ____________________  
Self-bias/sheath diagnostic: ____________________

## Gas/pressure/controller center

| Coordinate | Target/candidate | Measured/corrected | Uncertainty | State |
|---|---:|---:|---:|---|
| CH4 | 10.6667 sccm |  |  |  |
| H2 | 53.3333 sccm |  |  |  |
| total | 64 sccm |  |  |  |
| pressure | 100 mTorr |  |  |  |
| forward power | 50 W |  |  |  |
| time | 60 s |  |  |  |

Reflected power trace: ____________________  
Self-bias/sheath trace: ____________________  
Sample thermal surrogate result: ____________________  
Chamber clean/season state: ____________________  
Run-to-run repeatability: ____________________  
Actual P25 oxide `t_clear`: ____________________ (`HGCDTE-REQUIRED`)  
`t_sem`: ____________________  
HgCdTe conversion/blocking/TLM evidence: ____________________

Overall AT-RIE state: ____________________

---

# 9. AT-MET register

Tool/revision: ____________________  
Vacuum/gauge chain: ____________________  
Cr source/QCM geometry: ____________________  
Au source/QCM geometry: ____________________

## Cr calibration

Nominal: 30 nm  
QCM tooling/density settings: ____________________  
Independent witness method: ____________________  
Runs/raw data: ____________________  
Local correction/uncertainty: ____________________

## Au calibration

Nominal: 270 nm  
QCM tooling/density settings: ____________________  
Independent witness method: ____________________  
Runs/raw data: ____________________  
Local correction/uncertainty: ____________________

Sequential Cr->Au vacuum history demonstrated: YES / NO  
Pumpdown/deposition pressure trace: ____________________  
Sample thermal proxy: ____________________  
RIE->Cr handoff timing method: ____________________  
HgCdTe TLM/lift-off/contact result: ____________________

Overall AT-MET state: ____________________

---

# 10. AT-DET register

Cryostat/Dewar: ____________________  
Temperature chain: ____________________  
Bias/load network: ____________________  
Radiometry chain: ____________________  
Noise chain: ____________________  
Temporal chain: ____________________

## AT-DET-01 cryogenic state

Dummy package: ____________________  
Temperature range/stability: ____________________  
Vacuum/purge state: ____________________  
Cooldown/warmup repeatability: ____________________  
State: ____________________

## AT-DET-02 DC/bias network

Dummy loads: ____________________  
Voltage calibration: ____________________  
Current calibration: ____________________  
Load calibration: ____________________  
Terminal-voltage transfer: ____________________  
Protection/current limiting: ____________________  
State: ____________________

## AT-DET-03 radiometry

Coverage: ____________________  
4-µm calibration: ____________________  
Beyond-4.4-µm coverage: ____________________  
Wavelength calibration: ____________________  
Reference detector: ____________________  
Aperture/view-factor geometry: ____________________  
State: ____________________

## AT-DET-04 modulation

1-kHz frequency accuracy: ____________________  
Waveform/duty: ____________________  
Reference phase: ____________________  
Waveform correction factor: ____________________  
State: ____________________

## AT-DET-05 electronics noise floor

Frequency range: ____________________  
Termination/load states: ____________________  
Electronics ASD/PSD: ____________________  
Selected PSD allocation `beta`: ____________________  
Derived design target: ____________________  
Complex gain/impedance calibration: ____________________  
FFT/window/ENBW validation: ____________________  
State: ____________________

## AT-DET-06 Johnson validation

| R | T | Predicted ASD/PSD | Measured | Combined uncertainty | Pass |
|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

State: ____________________

## AT-DET-07 temporal transfer

| Frequency | Source transfer | Electrical transfer | Reference transfer | State |
|---:|---|---|---|---|
| 1 kHz |  |  |  |  |
| 10 kHz |  |  |  |  |
| 100 kHz |  |  |  |  |
| 1 MHz |  |  |  |  |

Low-frequency extension: ____________________  
High-frequency extension: ____________________  
Pulse branch/BW if used: ____________________  
State: ____________________

## AT-DET-08 package thermal kernel

Dummy thermal stimulus: ____________________  
Measured kernel/poles: ____________________  
Repeatability: ____________________  
State: ____________________

## AT-DET-09 matched-state genealogy

Synthetic/dummy end-to-end state ID: ____________________  
All P10–P13 metadata fields recovered without inference: YES / NO  
State: ____________________

## AT-DET-10 HgCdTe residual

Device/contact/package state: ____________________  
P10 result: ____________________  
P11 result: ____________________  
P12 result: ____________________  
P13 result: ____________________

Overall AT-DET state: ____________________

---

# 11. AT-SING register

Tool/method: ____________________  
Support/protection: ____________________  
Consumable/slurry: ____________________

Surrogate material: ____________________  
Cut path/street: ____________________  
Kerf: ____________________  
Wander: ____________________  
Visible edge damage: ____________________  
Subsurface proxy: ____________________  
Clean/release sequence: ____________________  
Witness compatibility: ____________________  
CdZnTe/HgCdTe residual evidence: ____________________

Overall AT-SING state: ____________________

---

# 12. AT-PKG register

Carrier/cold finger: ____________________  
Candidate compliant attach family/product: ____________________  
Interconnect: ____________________  
Window/filter/shield: ____________________  
Vacuum/pump system: ____________________

Dummy package ID: ____________________  
Bondline thickness/coverage: ____________________  
Thermal resistance/kernel: ____________________  
Thermal-cycle count/conditions: ____________________  
Interconnect resistance/integrity: ____________________  
Microphonics/noise check: ____________________  
Aperture/window geometry: ____________________  
Spectral transmission: ____________________  
Vacuum/bake/cooldown trace: ____________________  
HgCdTe completed-package residual evidence: ____________________

Overall AT-PKG state: ____________________

---

# 13. Requalification trigger register

| Subsystem | Trigger observed | Date | Affected tests | Result/new state |
|---|---|---|---|---|
| LPE |  |  |  |  |
| anneal |  |  |  |  |
| FTIR |  |  |  |  |
| Hall |  |  |  |  |
| RIE |  |  |  |  |
| Cr/Au |  |  |  |  |
| detector station |  |  |  |  |
| singulation |  |  |  |  |
| package/Dewar |  |  |  |  |

---

# 14. P16D disposition

All mandatory subsystem IQ complete: YES / NO  
All mandatory OQ complete: YES / NO  
All possible surrogate PQ complete: YES / NO  
All remaining HgCdTe residual tests explicitly identified: YES / NO  
All calibration/uncertainty records linked: YES / NO  
All critical requalification triggers defined: YES / NO  
EH&S/facility authorization current: YES / NO

P16D overall state:

`P16D-SURROGATE-COMMISSIONING-COMPLETE = YES / NO`

Reviewer: ____________________  
Date: ____________________

**Reminder:** this state is not `TRACEABLE-FIRST-BUILD-READY`, `HISTORICAL-RP01-REPRODUCED`, or `REPRODUCIBLE-RELEASE`.