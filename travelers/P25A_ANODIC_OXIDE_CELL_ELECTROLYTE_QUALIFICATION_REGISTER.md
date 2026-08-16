# P25A — anodic-oxide cell / electrolyte instantiation qualification register

**Status:** BLANK CONTROLLED PRE-FIRST-BUILD RECORD  
**Use with:** P02/P02A/P02B/P02C/P25/P25A and P16A

This register defines the **physical and mathematical anodization branch**. It does not replace the larger P25 run/outcome register.

Do not back-fill unknown historical values. Use `OPEN`, `N/A`, `NOT-MEASURED`, or the actual local value.

---

## A. Branch identity

- P25A branch ID:
- revision:
- date:
- operator/author:
- intended evidence class:
  - [ ] `P25A-TI-PC-CARBON-TRANSFER`
  - [ ] `P25A-TI-LATER-PT-HORIZONTAL-TRANSFER`
  - [ ] `P25A-LOCAL-VV-*`
  - [ ] `P25A-LOCAL-WW-*`
  - [ ] other explicit local branch
- P25 run/register linked:
- P28/P28A incoming-surface record linked:
- deviation/change-control ID:

Historical-identity claim being made? YES / NO  
If YES, documentary basis:

---

## B. Electrolyte mathematical definition

### KOH
- target molarity:
- target final electrolyte amount/volume definition:
- KOH molar mass used:
- required pure-KOH moles:
- required pure-KOH mass:
- reagent assay/certified fraction:
- assay basis:
- corrected reagent mass:
- final calculated molarity:

### EG / water carrier
- published notation being transferred:
- chosen local basis:
  - [ ] volume fraction
  - [ ] mass fraction
  - [ ] other, specify
- explicit mathematical definition:
- target EG fraction:
- target H2O fraction:
- final-solvent denominator definition:
- final-electrolyte denominator definition:

### Actual preparation
- actual KOH delivered mass:
- actual EG delivered mass:
- actual EG delivered volume:
- actual DI-water mass:
- actual DI-water volume:
- actual final mass:
- actual final volume, if measured/defined:
- calculation worksheet/data path:

**Gate B:** concentration mathematics complete and unambiguous? PASS / FAIL

---

## C. Reagent genealogy

### KOH
- supplier:
- product/catalog:
- lot:
- grade:
- certified assay:
- certificate reference:
- storage/open date:

### Ethylene glycol
- supplier:
- product/catalog:
- lot:
- grade/purity:
- water specification:
- certificate reference:
- storage/open date:

### DI water
- source/system:
- resistivity/conductivity:
- measurement time:
- TOC/other specification if controlled:

### Bath preparation
- vessel ID/material:
- reagent addition order:
- preparation start/end:
- solution temperature during/after preparation:
- mixing method/time:
- visible precipitate/contamination:
- pH method/result:
- conductivity method/result:
- storage container/state:
- bath age at use:
- fresh/reused/replenished:

**Gate C:** reagent/bath genealogy complete? PASS / FAIL

---

## D. Cell architecture

### Vessel
- material:
- internal dimensions:
- nominal bath volume:
- actual bath volume:
- liquid depth:
- cover state:
- cell drawing/photo ID:

### HgCdTe anode
- material/coupon ID:
- nominal/measured x:
- L/W/thickness:
- orientation in cell:
- top-surface exposed area:
- sidewall exposed area:
- backside exposed area:
- masked area:
- total `A_exposed`:
- area measurement method:
- uncertainty in `A_exposed`:
- anode contact material:
- anode contact geometry/location:
- anode contact exposed to electrolyte? YES / NO / PARTIAL
- contact isolation method:

### Cathode
- material:
- branch provenance:
- shape:
- dimensions:
- exposed cathode area:
- anode-cathode separation:
- relative orientation:
- alignment/position tolerance:

### Fixture
- holder material:
- mask/seal material:
- compatibility reference:
- bubble-trapping inspection:
- leakage/creep test result:

**Gate D:** cell is dimensioned and branch-specific? PASS / FAIL

---

## E. Temperature / mass transport

- bath temperature sensor ID:
- calibration date/uncertainty:
- sensor location:
- target bath temperature:
- actual pre-run bath temperature:
- actual post-run bath temperature:
- ambient temperature:
- agitation state:
  - [ ] unstirred/static
  - [ ] stirred
  - [ ] holder motion
  - [ ] other
- agitation equipment/setting:
- sample orientation:
- bubble-removal rule:
- observed convection/flow anomaly:

**Gate E:** thermal/mass-transport state reproducibly defined? PASS / FAIL

---

## F. Electrical realization

- constant-current source make/model/ID:
- calibration date/result:
- voltage logger/DMM/DAQ:
- voltage measurement reference points:
- acquisition interval/rate:
- compliance voltage:
- selected `J_target`:
- `A_exposed` used:
- calculated `I_command = J_target A_exposed`:
- commanded current:
- measured current mean:
- measured current min/max:
- current uncertainty:
- resulting measured/estimated J:
- polarity check:

**Gate F:** current density is traceable to measured area? PASS / FAIL

---

## G. Process trajectory

- sample immersion time:
- current-on time:
- initial voltage `V0`:
- induction definition:
- measured `t_ind`:
- time to 5 V:
- time to 10 V:
- time to 15 V:
- defined growth-region fit interval:
- `dV/dt`:
- terminal voltage:
- terminal criterion:
  - [ ] voltage
  - [ ] time
  - [ ] charge/area
  - [ ] combined criterion
  - [ ] other
- current-off time:
- total process duration:
- integrated charge Q:
- `Q/A_exposed`:
- compliance events:
- gas/bubble events:
- raw V(t) path:
- raw I(t) path:

**Gate G:** full electrical trajectory recorded? PASS / FAIL

---

## H. Immediate post-process handling

- current-off -> first-rinse delay:
- rinse 1 identity/duration/state:
- rinse 2 identity/duration/state:
- further rinse:
- dry method:
- dry-complete time:
- film appearance/color:
- uniformity/stain/pinhole note:
- standardized image ID:
- post-process storage atmosphere:
- time to P25 physical metrology:
- time to Mask-2:
- time to P08:

**Gate H:** post-anodization trajectory explicit? PASS / FAIL

---

## I. P28 -> P25 incoming-surface clock

- P28 etch-end time:
- quench/rinse sequence ID:
- dry-complete time:
- storage atmosphere:
- cumulative air exposure estimate:
- P25 bath-immersion time:
- P25 current-on time:
- calculated `t_etch->P25`:
- incoming surface-image/metrology reference:

---

## J. Physical oxide result — link to P25

- oxide thickness method:
- thickness map/data path:
- mean thickness:
- standard deviation/range:
- target comparison:
- color/thickness correlation status:
- top-surface morphology:
- mesa-sidewall coverage:
- abnormal dissolution/matte region:

P25 physical oxide gate: PASS / FAIL / HOLD

---

## K. Interface / downstream result — link to P25

- P25 interface/electrical result ID:
- P08 oxide-clear result:
- P08 converted-region result:
- P09 TLM/contact result:
- P10 dark electrical result:
- P12 noise result:
- stability/aging result:

P25 interface/function gate: PASS / FAIL / HOLD  
P08 compatibility gate: PASS / FAIL / HOLD  
Detector/contact correlation gate: PASS / FAIL / HOLD / NOT-TESTED

---

## L. Branch classification

Select highest supported state only:

- [ ] `LITERATURE-TRANSFER-ONLY`
- [ ] `ELECTROLYTE-MATHEMATICALLY-DEFINED`
- [ ] `CELL-GEOMETRY-DEFINED`
- [ ] `CURRENT-DENSITY-TRACEABLE`
- [ ] `V(T)-FINGERPRINT-REPEATABLE`
- [ ] `OXIDE-THICKNESS-QUALIFIED`
- [ ] `INTERFACE-FUNCTION-QUALIFIED`
- [ ] `P08-COMPATIBLE`
- [ ] `CONTACT/DETECTOR-CORRELATED`
- [ ] `P25-LOCAL-QUALIFIED`

Can P16A R15 be changed to `LOCAL-BRANCH-FROZEN`? YES / NO

If YES, identify exact frozen branch/revision and justify that sections B–H are complete:

Can this branch be called historical RP-01? YES / NO

If YES, direct historical evidence:

Reviewer/date:
