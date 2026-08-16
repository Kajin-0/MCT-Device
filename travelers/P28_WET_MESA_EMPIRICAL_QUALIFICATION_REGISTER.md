# P28 — wet-mesa empirical qualification register

**Status:** BLANK CONTROLLED TRAVELER  
**Use:** one register per etchant batch / process run genealogy. Attach raw data by controlled path or data-system ID.

Do not enter reagent quantities for a literature formulation whose percentage/ratio basis is still undefined. A local executable recipe must have an explicit concentration definition and recipe ID.

---

## A. Run identity

- P28 run ID:
- date:
- operator:
- wafer/coupon IDs:
- growth/anneal lot:
- Mask-1 recipe ID:
- etchant recipe ID:
- evidence class (`DIRECT-RP01 / SAME-UWA / PRIMARY-X028 / LOCAL-QUAL`):
- batch ID:
- run-order position within batch:

---

## B. Incoming material state

- nominal/measured x:
- P06 optical-edge/composition result:
- HgCdTe thickness map / local thickness:
- carrier type:
- Hall n/p:
- mobility:
- substrate ID/type:
- incoming surface history:
- elapsed time since prior wet/thermal process:
- pre-etch Nomarski images:
- pre-etch roughness:
- other surface metrology:

---

## C. Mask-1 state

- resist product/lot:
- adhesion treatment:
- dispense:
- spin speed/time/acceleration:
- soft bake:
- measured resist thickness map:
- mask ID/revision:
- exposure tool/wavelength/dose/mode:
- developer/product/concentration/time/T/agitation:
- rinse/dry:
- developed trench/mesa CDs:
- resist defects:
- Mask-1 gate: PASS / FAIL / CONDITIONAL

---

## D. Etchant formulation definition

### Published notation being tested

- nominal Br2 notation:
- published EG:HBr notation:
- source:

### Local executable definition

- bromine concentration basis (`w/w`, `v/v`, `w/v`, molarity, other):
- mathematical definition:
- EG:HBr mixing basis (`mass`, `volume`, other):
- mathematical definition:
- target final batch quantity:

### Reagents

**Br2**
- supplier:
- product/lot:
- purity/assay:
- bottle open date/storage:
- actual delivered mass/volume:

**Ethylene glycol**
- supplier:
- product/lot:
- purity/water specification:
- actual delivered mass/volume:

**HBr**
- supplier:
- product/lot:
- certified stock assay:
- concentration basis:
- density if used in preparation calculation:
- actual delivered mass/volume:
- bottle open date/storage:

- final measured batch mass:
- final measured batch volume if defined/measured:
- formulation calculation file/path:

---

## E. Mixing / vessel genealogy

- vessel material/ID:
- vessel nominal volume:
- cover/seal configuration:
- reagent-addition order:
- mixing method:
- mixing duration:
- preparation start:
- preparation end:
- peak/initial temperature after mixing:
- temperature when ready for use:
- visible phase/gas/color observations:
- institution-approved chemistry procedure ID:
- batch release for qualification: PASS / FAIL

Optional:

- vessel + bath mass immediately after preparation:
- analytical free-Br2 proxy/method:
- analytical result:

---

## F. Bath state before each coupon/device

| Sample | run order | bath age | cumulative open time | bath T before | bath T after | bath volume/proxy | cumulative etched area | prior deviations |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| | | | | | | | | |

- temperature sensor ID/calibration:
- ambient cleanroom T/RH:
- bath cover state between samples:

---

## G. Agitation / sample geometry

- agitation mode (`static / holder motion / stir / other`):
- agitation rate/settings:
- stir bar/impeller geometry if used:
- sample holder material/ID:
- sample orientation:
- immersion depth:
- distance from vessel walls/bottom:
- exposed HgCdTe area:
- masked/backside areas:
- introduction/removal motion:

Any agitation or geometry change from prior calibration? YES / NO

---

## H. Etch timing

For each sample:

- immersion start:
- immersion end:
- actual immersion time:
- endpoint method:
- endpoint indication/time:
- interruptions? YES / NO
- interruption details:
- visible evolution/bubbles/color:

**Do not disposition a device from time alone.**

---

## I. Quench / rinse / dry

- local rinse recipe ID:
- immediate quench medium:
- quench duration:
- first rinse medium:
- first rinse duration/flow:
- subsequent rinses:
- final rinse:
- dry method:
- etch end timestamp:
- quench/rinse end timestamp:
- dry timestamp:
- visible residue after dry:

This sequence is `LOCAL-QUAL` unless direct UWA/Srivastav closure is recovered.

---

## J. Vertical depth metrology

- instrument/model:
- calibration date:
- stylus/probe settings:
- measurement locations:

| Location | incoming HgCdTe thickness | measured etch depth | uncertainty | substrate crossed? | notes |
|---|---:|---:|---:|---|---|
| | | | | | |

- mean depth:
- standard deviation:
- range:
- inferred local `R_V` only if valid:
- regression/data file:

---

## K. Lateral / geometry metrology

- microscope/SEM model:
- calibration:
- nominal mask CD:
- pre-etch resist CD:

| Feature | depth/time | top mesa CD | base/trench CD | undercut side 1 | undercut side 2 | edge/corner note |
|---|---:|---:|---:|---:|---:|---|
| | | | | | | |

- `R_L` definition used:
- calculated `R_L`:
- anisotropy `A=1-R_L/R_V`:
- uncertainty:
- sidewall angle reported? YES / NO
- if YES, measurement method (do not derive from A unless profile model validated):

---

## L. Surface/profile gate

- RMS roughness method:
- roughness result:
- trench-floor morphology:
- edge trenching/notching:
- convex floor:
- ragged sidewall:
- resist attack/lift:
- residual HgCdTe:
- CdZnTe surface attack:
- Nomarski image path:
- SEM/AFM/profilometry path:
- physical gate: PASS / FAIL / CONDITIONAL

---

## M. Electrical isolation / material preservation

- measurement T:
- mesa-to-mesa isolation structure:
- bias/current condition:
- isolation resistance/leakage:
- measurement uncertainty:
- complete electrical isolation? YES / NO / CONDITIONAL
- companion pre/post Hall comparison:
- LBIC/spatial result if used:
- anomalous electrical modification? YES / NO
- electrical gate: PASS / FAIL / CONDITIONAL

---

## N. Through-layer / overetch state

- local incoming `d_HgCdTe,in`:
- measured `d_etch`:
- `d_over=d_etch-d_HgCdTe,in` if valid:
- substrate-interface crossing evidence:
- electrical isolation corroborates crossing? YES / NO
- lateral-loss consequence:
- overetch disposition:

No generic overetch fraction is released.

---

## O. Post-etch surface / P25 handoff

- atmosphere after dry:
- storage container:
- storage temperature:
- surface analysis witness ID:
- ellipsometry/XPS/AES/AFM result:
- `t_etch_to_P25`:
- P25 run ID:
- P25 anodization induction time / V(t) signature:
- P25 oxide thickness/result:
- anomalous passivation response? YES / NO

---

## P. Bath-aging / run-order reduction

For a sequential batch study attach plots/tables of:

- `R_V` vs bath age;
- `R_V` vs run order;
- `R_V` vs cumulative etched area;
- `R_L/A` vs same coordinates;
- roughness vs same coordinates;
- optional analytical Br2 proxy vs time.

- detectable drift? YES / NO
- candidate maximum bath age/use condition:
- evidence/uncertainty:

Do not count multiple samples from one etchant batch as independent batch replicates.

---

## Q. Downstream device closure, if fabricated

- P25 passivation gate:
- P08/P09 contact gate:
- P10 dark I–V/self-heating:
- P11 responsivity:
- P12 noise/NEP/D*:
- P13 tau_eff/bandwidth:
- mesa/perimeter dependence:
- detector regression attributable to P28? YES / NO / UNRESOLVED
- data paths:

---

## R. Deviations / failure classification

- concentration/preparation deviation:
- temperature deviation:
- bath-age deviation:
- agitation deviation:
- etch-time deviation:
- rinse/quench deviation:
- depth nonuniformity:
- excessive undercut:
- resist attack:
- incomplete isolation:
- surface residue/roughness:
- anomalous P25 response:
- electrical performance regression:
- P18 record opened? YES / NO
- P18 ID:

---

## S. Run disposition

- formulation genealogy complete: PASS / FAIL
- depth/profile gate: PASS / FAIL / CONDITIONAL
- electrical isolation gate: PASS / FAIL / CONDITIONAL
- surface/P25 handoff gate: PASS / FAIL / CONDITIONAL
- detector gate: PASS / FAIL / CONDITIONAL / NOT TESTED
- overall P28 disposition:
- approved for next qualification stage? YES / NO
- approver/date:

### Provenance statement

- Which entries are `DIRECT-RP01`?
- Which are `SAME-UWA`?
- Which are `PRIMARY-X028-MESA`?
- Which are `PRIMARY-CONVENTION/SURFACE-TRANSFER`?
- Which are explicit `LOCAL-QUAL` choices?
- Which remain `OPEN`?
