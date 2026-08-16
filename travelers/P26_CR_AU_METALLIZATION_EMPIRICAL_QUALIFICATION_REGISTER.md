# P26 — Cr/Au metallization empirical qualification register

**Status:** BLANK CONTROLLED TRAVELER  
**Use:** one form per P26 metallization/lift-off run and linked TLM/device set.

Do not replace `OPEN` fields with assumed values. Attach raw traces/files by repository path or controlled data-system ID.

---

## A. Run identity

- P26 run ID:
- date:
- operator:
- wafer/coupon/device IDs:
- growth run/source wafer:
- P08 recipe/run ID:
- P14 recipe/run ID:
- P09/P09A parent recipe ID:
- metallization tool ID:
- deposition method:
- qualification branch (`thermal evaporation / e-beam / sputter / other`):
- stated evidence class for method:

---

## B. Incoming material/device state

- HgCdTe x / optical-edge metric:
- active thickness:
- carrier state / P05 reference:
- P08 converted density/sheet state:
- P08 converted depth result:
- P08 physical recess:
- P08 lateral conversion result:
- P08 surface/morphology result:
- anodic oxide thickness outside windows:
- actual contact-window dimensions:
- actual mesa dimensions:
- Mask-2 resist product/recipe:
- measured resist thickness:
- post-RIE resist thickness:
- developed undercut/overhang:
- RIE-survival inspection:
- incoming hold state: PASS / FAIL / CONDITIONAL

---

## C. P08-to-metal time history

Record timestamps with timezone or elapsed-seconds clock.

- `t_RF_off`:
- `t_RIE_vent`:
- `t_sample_out`:
- atmosphere after unload:
- inert container/storage ID if used:
- `t_metal_load`:
- `t_pump_start`:
- `t_base_accept`:
- `t_Cr_start`:
- `t_Cr_end`:
- `t_Au_start`:
- `t_Au_end`:
- `t_vent_after_metal`:
- `t_liftoff_start`:

Derived:

- `Delta t_RIE-Cr`:
- cumulative `Delta t_air`:
- cumulative inert exposure:
- `Delta t_Cr-Au`:
- total metal-deposition-to-lift-off delay:

Any unplanned exposure/event:

---

## D. Pre-metal surface intervention

Baseline P26 expects **none** between released P08 and Cr deposition.

- wet clean performed? YES / NO
- chemistry/concentration/time if YES:
- rinse/dry if YES:
- ion mill performed? YES / NO
- energy/current/dose/time if YES:
- plasma clean? YES / NO
- gas/power/pressure/time if YES:
- UV/ozone or other treatment? YES / NO
- reason for non-baseline intervention:
- separate recipe/change-control ID:
- post-intervention P08 state reverified? YES / NO / N/A

---

## E. Deposition chamber state

- chamber ID:
- pump type:
- chamber clean date/state:
- immediately preceding deposited material/process:
- source-to-sample distance:
- sample tilt/orientation:
- sample rotation/planetary mode:
- holder/carrier material:
- backside mounting method:
- QCM head position:
- witness position(s):
- RGA available? YES / NO
- RGA file:

Pressure:

- pressure at loading:
- base pressure before Cr:
- base-accept criterion:
- Cr deposition pressure mean/range:
- pressure between Cr/Au:
- Au deposition pressure mean/range:
- unexpected pressure excursion:
- pressure trace file:

---

## F. Chromium source and deposition

Historical target thickness: `30 nm` (`DIRECT-RP01`). Historical rate remains `OPEN`.

- Cr supplier:
- lot:
- stated purity:
- source form:
- boat/crucible material:
- source condition/preheat:
- shutter stabilization time:
- QCM material settings:
- QCM tooling factor:
- nominal local rate:
- mean measured rate:
- rate standard deviation/range:
- rate trace file:
- deposition start thickness:
- indicated final thickness:
- shutter-open duration:
- holder T initial:
- holder/sample T max during Cr:
- pressure start/end:
- source spitting/particulates? YES / NO
- other observation:

---

## G. Gold source and deposition

Historical target thickness: `270 nm` (`DIRECT-RP01`). Published transfer-rate anchors exist at 3–12 Å/s but are not RP-01 values.

- Au supplier:
- lot:
- stated purity:
- source form:
- boat/crucible material:
- source condition/preheat:
- QCM material settings:
- QCM tooling factor:
- nominal local rate:
- mean measured rate:
- rate standard deviation/range:
- rate trace file:
- indicated final thickness:
- shutter-open duration:
- holder T at Au start:
- holder/sample T max during Au:
- pressure start/end:
- source spitting/particulates? YES / NO
- other observation:

---

## H. Cr-to-Au interface

- vacuum broken between layers? YES / NO
- if YES, exposure atmosphere/time:
- interval Cr-end to Au-start:
- pressure during interval:
- intentional treatment between layers? YES / NO
- treatment details:

---

## I. Independent film-thickness/witness metrology

### Chromium witness

- method:
- measured thickness:
- uncertainty:
- QCM/witness ratio:
- roughness:
- sheet resistance if measured:

### Gold / final-stack witness

- method:
- measured Au or stack thickness:
- uncertainty:
- QCM/witness ratio:
- roughness:
- sheet resistance if measured:
- adhesion result:
- microscopy/AFM/SEM file:

---

## J. Post-metal thermal history

P26 baseline uses no intentional post-metal anneal.

- intentional anneal? YES / NO
- if YES, separate branch/recipe ID:
- atmosphere:
- sample temperature trace:
- nominal temperature:
- dwell duration:
- ramp/cooldown:
- reason:
- all later thermal events before TLM:

---

## K. Lift-off process

Historical RP-01 lift-off solvent/time/agitation remain `OPEN`.

- solvent product:
- supplier/lot:
- bath/container ID:
- bath temperature:
- immersion start/end:
- time to first visible release:
- total soak time:
- solvent exchanges:
- static/manual agitation/stirring:
- ultrasound used? YES / NO
- ultrasound frequency:
- ultrasound power/setting:
- ultrasound time:
- rinse sequence:
- final rinse:
- dry method:
- mechanical intervention used? YES / NO
- details:

---

## L. Post-lift-off physical inspection

Record actual measured dimensions rather than mask nominal values.

- contact length/width:
- gap series:
- metal CD bias from mask:
- complete unwanted-metal removal? YES / NO
- fencing/stringers:
- edge tearing:
- pad scratches:
- Cr/Au delamination:
- pinholes/voids:
- resist residue:
- particle redeposition:
- mesa damage:
- oxide/passivation damage:
- optical image files:
- SEM/profilometry files:
- physical gate: PASS / FAIL / CONDITIONAL

---

## M. Electrical TLM conditions

- measurement date/time:
- elapsed time since Cr deposition:
- elapsed time since lift-off:
- sample temperature:
- temperature stability:
- optical background condition:
- cold shield? YES / NO
- magnet/light source states relevant to measurement:
- current grid:
- voltage compliance:
- self-heating check:
- current reversal used? YES / NO
- raw I–V file:
- raw pair-resistance file:
- dimensional-metrology file:

---

## N. TLM raw geometry/results

For every pair record:

| Pair | gap measured | contact dimensions | +I resistance | -I resistance | linearity/hysteresis | notes |
|---|---:|---|---:|---:|---|---|
| | | | | | | |

Regression:

- model used:
- weighting:
- slope:
- intercept:
- adjusted R²:
- residual diagnostic:
- sheet resistance:
- contact resistance:
- transfer length:
- `rho_c`:
- standard uncertainty / CI:
- model assumptions valid? YES / NO / CONDITIONAL

Historical comparison:

- RP-01 benchmark `rho_c≈9×10^-4 Ω·cm² at 80 K`;
- result relative to benchmark:

---

## O. Contact uniformity

- number of contacts/pairs passing:
- mean pair/contact metric:
- standard deviation:
- coefficient of variation:
- min/max:
- spatial trend:
- outlier contacts:
- outlier investigation:

---

## P. Aging and thermal-cycle record

| State/cycle | date | elapsed storage | storage T/ambient | test T | pair/TLM metric | rho_c if extracted | visual state | notes |
|---|---|---|---|---:|---|---:|---|---|
| as fabricated | | | | | | | | |
| | | | | | | | | |

- contact drift beyond measurement uncertainty? YES / NO
- delamination/cracking? YES / NO
- I–V changed? YES / NO

---

## Q. Detector correlation, if fabricated

- detector ID:
- measured gap/active area:
- operating T:
- electric field:
- current/power:
- responsivity condition/result:
- noise ASD condition/result:
- 1/f knee:
- g-r plateau:
- NEP:
- D*:
- temporal response / f3dB / tau_eff:
- P10/P11/P12/P13 data paths:
- contact process caused detectable performance penalty? YES / NO / UNRESOLVED

---

## R. Deviations / failure classification

- deviation ID:
- unplanned vacuum excursion:
- source instability:
- sample overheating:
- resist reflow:
- incomplete lift-off:
- high/nonuniform rho_c:
- non-ohmic behavior:
- aging drift:
- noise/performance regression:
- root-cause status:
- P18 record if opened:

---

## S. Run disposition

- physical gate: PASS / FAIL / CONDITIONAL
- TLM gate: PASS / FAIL / CONDITIONAL
- stability gate: PASS / FAIL / CONDITIONAL
- detector gate: PASS / FAIL / CONDITIONAL / NOT TESTED
- overall P26 disposition:
- approved for next DOE stage? YES / NO
- approver/date:

### Evidence statement

- Which values in this run are `DIRECT-RP01` targets?
- Which are transfer-family literature anchors?
- Which are local qualification choices?
- Which fields remain `OPEN`?

