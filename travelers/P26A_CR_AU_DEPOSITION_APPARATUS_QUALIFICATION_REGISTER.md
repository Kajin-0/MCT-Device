# P26A — Cr/Au deposition apparatus / vacuum / thermal-state qualification register

**Status:** BLANK CONTROLLED APPARATUS RECORD  
**Use with:** P09/P09A/P26/P26A/P27/P08/P17

Complete once per frozen apparatus/process revision and update through formal change control. This register defines whether a metallization branch is apparatus-ready; individual process runs remain recorded in the P26 register.

Do not populate `OPEN` fields with presumed semiconductor-industry values.

---

## A. Branch identity

- P26A branch ID:
- revision:
- date:
- owner/operator:
- deposition method (`THERMAL-EVAP / E-BEAM / SPUTTER / OTHER`):
- evidence class for method:
- intended first-build stack: `Cr 30 nm / Au 270 nm`:
- linked P26 recipe/revision:
- linked P27 Mask-2/lift-off recipe:
- linked P08 RIE branch:
- change-control record:

Qualification state:

- [ ] METHOD-FAMILY-SELECTED
- [ ] TOOL-REVISION-DEFINED
- [ ] VACUUM-CHAIN-DEFINED
- [ ] SOURCE-HARDWARE-DEFINED
- [ ] GEOMETRY-DEFINED
- [ ] THICKNESS-METROLOGY-QUALIFIED
- [ ] THERMAL-LOAD-CALIBRATED
- [ ] RIE-CR-HANDOFF-DEFINED
- [ ] CR-AU-SEQUENCE-DEFINED
- [ ] P26-APPARATUS-READY
- [ ] P26-LOCAL-QUALIFIED

---

## B. Tool/chamber identity

- manufacturer:
- model:
- serial / local asset ID:
- chamber ID:
- chamber revision/liner:
- number of source stations:
- source-station map:
- shutter architecture:
- sample-stage/holder ID:
- nominal sample capacity:
- chamber clean method/revision:
- chamber seasoning/preconditioning rule:
- immediately disallowed prior materials/processes:
- equipment drawing/photo reference:

---

## C. Vacuum chain

- roughing pump type/model:
- high-vacuum pump type/model:
- isolation/throttle architecture:
- base-pressure gauge type/model:
- gauge location:
- gauge range:
- gauge calibration date/result:
- deposition-pressure gauge type/model/location:
- gas correction relevant?:
- RGA model/location if present:
- standard pumpdown procedure:
- normal clean base-pressure distribution/reference data:
- selected qualification base-accept criterion:
- basis for criterion (`LOCAL-CAPABILITY / P26-DATA / OTHER`):
- pressure logging cadence:
- raw baseline pumpdown file:
- leak/outgassing acceptance method:

Historical RP-01 base pressure remains `OPEN`; state explicitly that the local criterion is not a historical value:

---

## D. Cr source station

- source-station ID:
- heating/deposition mechanism:
- boat/crucible/hearth material:
- boat/crucible geometry/part number:
- Cr source supplier/product:
- Cr lot:
- purity:
- source form:
- nominal source charge:
- conditioning/preheat sequence:
- shutter/source stabilization sequence:
- recharge/reuse rule:
- source-to-sample distance:
- source line-of-sight angle to sample normal:
- known masking/shield geometry:
- source spitting/particulate screening method:
- photo/drawing reference:

---

## E. Au source station

- source-station ID:
- heating/deposition mechanism:
- boat/crucible/hearth material:
- boat/crucible geometry/part number:
- Au source supplier/product:
- Au lot:
- purity:
- source form:
- nominal source charge:
- conditioning/preheat sequence:
- shutter/source stabilization sequence:
- recharge/reuse rule:
- source-to-sample distance:
- source line-of-sight angle to sample normal:
- known masking/shield geometry:
- source spitting/particulate screening method:
- photo/drawing reference:

---

## F. Sample holder / flux geometry

- holder/carrier material:
- holder dimensions:
- sample attachment/clamping method:
- backside thermal contact:
- wafer/coupon orientation:
- fixed tilt angle:
- rotation enabled?:
- rotation speed/range if used:
- planetary motion if used:
- sample center coordinates relative to source:
- maximum radial offset used:
- witness-coupon coordinates:
- QCM coordinates relative to source/sample:
- geometry drawing/reference:

### Geometry qualification

- P27 developed resist top CD:
- P27 developed resist bottom CD:
- measured undercut/overhang:
- deposition-angle compatibility coupon ID:
- fencing/bridging result:
- final metal CD bias:
- geometry gate `PASS/FAIL/OPEN`:

---

## G. QCM / thickness monitor — Cr

- controller/model:
- sensor/head ID:
- crystal type/frequency:
- sensor position:
- Cr material setting/density/acoustic setting:
- current tooling factor:
- calibration witness IDs:
- QCM-indicated thicknesses:
- independent method:
- independently measured thicknesses:
- QCM/witness ratios:
- mean correction/tooling result:
- uncertainty:
- repeatability:
- calibration valid date/run range:
- qualification gate `PASS/FAIL/OPEN`:

---

## H. QCM / thickness monitor — Au

- controller/model:
- sensor/head ID:
- crystal type/frequency:
- sensor position:
- Au material setting/density/acoustic setting:
- current tooling factor:
- calibration witness IDs:
- QCM-indicated thicknesses:
- independent method:
- independently measured thicknesses:
- QCM/witness ratios:
- mean correction/tooling result:
- uncertainty:
- repeatability:
- calibration valid date/run range:
- qualification gate `PASS/FAIL/OPEN`:

Cr and Au use one common tooling factor? `YES/NO`:
If YES, provide empirical justification rather than assumption:

---

## I. Selected Cr rate branch

Historical RP-01 rate: `OPEN`.

- P26 DOE/reference runs:
- tested low rate:
- tested center rate:
- tested high rate:
- selected nominal local rate:
- selected allowed variation:
- rate monitor update cadence:
- typical stabilization time before shutter:
- typical shutter-open time for 30 nm:
- pressure range during selected Cr deposition:
- TLM/contact response supporting selection:
- adhesion/morphology response:
- selected state `LOCAL-CANDIDATE / LOCAL-QUALIFIED`:

---

## J. Selected Au rate branch

Historical RP-01 rate: `OPEN`.

- P26 DOE/reference runs:
- tested low rate:
- tested center rate:
- tested high rate:
- selected nominal local rate:
- selected allowed variation:
- typical stabilization time before shutter:
- typical shutter-open time for 270 nm:
- pressure range during selected Au deposition:
- lift-off/thermal response supporting selection:
- selected state `LOCAL-CANDIDATE / LOCAL-QUALIFIED`:

Published transfer-rate values are not RP-01 rates; state any transfer source used only for screening:

---

## K. Thermal-load calibration

- dummy/surrogate ID:
- substrate/thermal-mass similarity to HgCdTe/CdZnTe:
- holder configuration:
- resist/surrogate present?:
- temperature sensor type/location:
- sensor calibration:
- rate/source-power history used:
- Cr deposition duration:
- Au deposition duration:
- holder T initial:
- sample/proxy T initial:
- peak T during Cr:
- peak T during Au:
- time above locally monitored temperature landmarks:
- post-Au cooldown time to vent criterion:
- sensor lag/uncertainty:
- thermal trace file:
- selected thermal hold criterion:
- qualification gate `PASS/FAIL/OPEN`:

Do not relabel holder temperature as exact wafer temperature unless validated.

---

## L. RIE-to-Cr transfer branch

- transfer class (`VACUUM / INERT / AIR / OTHER`):
- physical path description:
- connected load lock? `YES/NO`:
- RIE and deposition tools physically integrated? `YES/NO`:
- transfer container if inert:
- atmosphere specification:
- maximum ordinary handling distance/time:
- P26 delay DOE run IDs:
- selected maximum `Delta t_RIE-Cr`:
- selected maximum cumulative `Delta t_air`:
- timestamp method/resolution:
- required operator log fields:
- branch basis (`LOCAL-QUAL` or other):

Historical statement:
- does this branch claim actual RP-01 load-lock use? `NO` unless new direct evidence is attached.

---

## M. Pre-metal surface branch

Baseline should be `NONE` after qualified P08.

- intermediate wet clean:
- ion mill:
- plasma clean:
- UV/ozone:
- other:
- baseline = no intervention? `YES/NO`:

If any intervention is selected:
- separate recipe ID:
- reason:
- P08 converted-state requalification:
- TLM data:
- detector/noise correlation:

---

## N. Cr-to-Au sequence

- same vacuum cycle? `YES/NO`:
- Cr source end timestamp logging required?:
- Au source start timestamp logging required?:
- nominal/maximum Cr-to-Au interval:
- pressure acceptance between layers:
- source-switch operation:
- required sample cooling between layers:
- vacuum break if unavoidable:
- atmosphere/time if broken:
- treatment between Cr/Au:
- sequence state `LOCAL-DEFINED / LOCAL-QUALIFIED / OPEN`:

No historical RP-01 no-break claim is made unless new source attached:

---

## O. First-build nominal branch table

| Coordinate | Frozen local value/branch | Evidence | Calibration / run ID |
|---|---|---|---|
| deposition method | | | |
| tool/revision | | | |
| base-accept rule | | | |
| Cr source hardware | | | |
| Au source hardware | | | |
| source/sample geometry | | | |
| QCM Cr tooling/cal | | | |
| QCM Au tooling/cal | | | |
| Cr target thickness | `30 nm DIRECT-RP01` | DIRECT-RP01 | |
| Au target thickness | `270 nm DIRECT-RP01` | DIRECT-RP01 | |
| Cr rate | | LOCAL | |
| Au rate | | LOCAL | |
| thermal hold criterion | | LOCAL | |
| RIE-to-Cr branch | | LOCAL | |
| maximum RIE-to-Cr delay | | LOCAL | |
| maximum air exposure | | LOCAL | |
| Cr-to-Au vacuum rule | | LOCAL | |
| linked lift-off recipe | | LOCAL | |

Any blank mandatory row prevents `P26-APPARATUS-READY`.

---

## P. Linked P26 outcome closure

- P26 qualification runs:
- actual Cr thickness distribution:
- actual Au thickness distribution:
- post-lift-off physical gate:
- 80-K TLM result:
- historical rho_c comparison:
- contact-to-contact spread:
- I–V symmetry/linearity:
- thermal-cycle result:
- aging result:
- P12 noise correlation:
- detector functional correlation:
- P26-LOCAL-QUALIFIED? `YES/NO/HOLD`:

---

## Q. Readiness disposition

- method family selected? `YES/NO`:
- actual tool revision frozen? `YES/NO`:
- vacuum chain calibrated/frozen? `YES/NO`:
- Cr and Au source hardware frozen? `YES/NO`:
- geometry frozen? `YES/NO`:
- separate Cr/Au thickness calibration valid? `YES/NO`:
- initial rate branches frozen? `YES/NO`:
- thermal load calibrated? `YES/NO`:
- RIE-to-Cr handoff frozen? `YES/NO`:
- Cr-to-Au sequence frozen? `YES/NO`:
- linked lift-off branch frozen? `YES/NO`:

`P26-APPARATUS-READY = YES / NO`

`P26-LOCAL-QUALIFIED = YES / NO / NOT-YET`

Can P16A R20 be moved to `LOCAL-BRANCH-FROZEN`? `YES / NO`

Reviewer:
Date:
Rationale:
