# P30A — absolute LPE charge / apparatus calibration register

**Status:** CONTROLLED PRE-EXECUTION / QUALIFICATION REGISTER  
**Date:** 2026-08-16 America/New_York

Use with `procedures/P30A_LPE_ABSOLUTE_CHARGE_APPARATUS_CALIBRATION_ADDENDUM.md` and `travelers/P30_LPE_EXECUTION_EMPIRICAL_QUALIFICATION_REGISTER.md`.

Every unmeasured field shall be marked `OPEN`, `NA`, or `NOT-MEASURED`. Do not substitute a nominal drawing or another laboratory's value.

---

## A. Calibration branch identity

- P30A revision:
- Calibration ID:
- Date:
- Responsible researcher:
- Facility:
- Intended P30 branch:
- Historical/transfer classification:
- Boat revision:
- Furnace/tube revision:
- Actuator revision:
- Target material branch:
  - [ ] Honeywell-derived xL=.082/yL=.810 local branch
  - [ ] other explicitly defined branch
- Related P29 substrate branch:
- Related P03C source-synthesis branch:

---

## B. Boat dimensional metrology

### Base/stator
- Material/grade/lot:
- Overall L × W × H:
- Datum definition:
- Flatness:
- Surface condition:

### Substrate recess
- Length:
- Width:
- Depth:
- Corner geometry:
- Substrate top plane relative to datum:
- Measurement method:
- Measurement uncertainty:

### Growth well
- Well ID:
- Top opening dimensions:
- Bottom opening dimensions:
- Depth:
- Taper/profile:
- Plug/cap ID:
- Plug intrusion depth:
- Calculated plug displacement volume:
- `V_well,geom`:
- `u(V_well)`:
- Independent capacity check:

### Hg-source recess / vapor distribution
- Source recess L × W × depth:
- Source recess volume:
- Top moat/groove dimensions:
- Bottom moat/groove dimensions:
- Connecting channel dimensions:
- Cover gap/fit:

### Slider / overlap / wipe region
- Slider L × W × H:
- Slider-to-base clearance:
- Parallelism/flatness:
- Growth-well-to-substrate overlap area:
- Cooling/wipe well geometry:
- Actuator stroke:
- Indexed positions:
- Room-temperature position repeatability:

Dimensional report/file:

---

## C. Geometric capacity calculation

- Calculation version:
- `V_well,geom`:
- Plug displacement:
- Net geometric volume:
- Assumed/qualified unusable/freeboard region:
- Candidate `V_hot,usable` model:
- Evidence class for hot-volume correction:
- Uncertainty:

### Explicit check
- [ ] No charge mass was derived by substrate-area scaling alone.
- [ ] Radhakrishnan ~4.8-g value is retained only as transfer evidence.
- [ ] Honeywell x=.29 tie line was not treated as an absolute mass.

---

## D. Furnace / thermometry calibration

- Furnace ID:
- Quartz tube ID/ID/OD where controlled:
- Boat axial reference position:
- Controller ID:
- Controller sensor:
- Growth-region sensor ID/type:
- Sensor location relative to growth well:
- Substrate-region sensor/proxy:
- Calibration date:
- Calibration uncertainty:
- Static axial map file:
- Static transverse map file:
- Controller-to-growth-well offset:
- Dynamic lag during heat-up:
- Dynamic lag during cool-down:
- Data logging interval:

### Local liquidus / melting verification
- Target composition:
- Published tie-line `TL`:
- Local observation/method:
- Local liquidus proxy/result:
- Uncertainty:

---

## E. Hot mechanical calibration

- Process atmosphere used:
- Calibration temperature range:
- Slider command speed(s):
- Measured travel time(s):
- Position repeatability at temperature:
- Stick-slip observed:
- Force/torque/current proxy:
- Cover/slider interference:
- Hot clearance observation/measurement:
- Wipe/cooling-well transition time:
- Abnormal events:

Hot-mechanical calibration disposition: PASS / FAIL / HOLD

---

## F. Candidate absolute growth-charge inventory

Candidate inventory values shall be numerical before material loading.

| Candidate ID | `M_charge` | Basis from measured geometry/capacity | Evidence class | Approved for trial? |
|---|---:|---|---|---|
| LOW | | | | |
| CENTER | | | | |
| HIGH | | | | |
| OTHER | | | | |

### Selected first trial
- Candidate ID:
- Selected `M_charge`:
- Selection rationale:
- Engineering reviewer:

---

## G. xL=.082 / yL=.810 charge calculation

For the current project atomic-weight convention:

- `w_Hg = 0.249740`
- `w_Cd = 0.012502`
- `w_Te = 0.737758`

For selected `M_charge`:

- target Hg mass:
- target Cd mass:
- target Te mass:
- target total:

Actual weighing:

- balance ID/calibration:
- Hg lot/purity/actual mass:
- Cd lot/purity/actual mass:
- Te lot/purity/actual mass:
- actual total:
- mass closure:
- recomputed actual Hg mole fraction:
- recomputed actual Cd mole fraction:
- recomputed actual Te mole fraction:
- realized `xL`:
- realized `yL`:
- propagated weighing uncertainty:

---

## H. Source-synthesis genealogy

- P03C branch ID:
- Ampoule ID/material:
- Evacuation endpoint:
- Synthesis peak T:
- Hold time:
- T(t) file:
- Cooldown:
- Grinding/comminution:
- Mixing/homogenization:
- Storage:
- Batch final mass:
- Batch ID:

---

## I. Auxiliary Hg/HgTe source inventory

- Source chemistry/form:
- Source lot/batch:
- Initial mass:
- Recess geometry:
- Exposed area:
- Source temperature/proxy:
- Source run/reuse count before trial:
- Final mass:
- `Δm_source`:
- Condensation/transport observations:

### Explicit check
- [ ] Auxiliary source mass is recorded independently from `M_charge`.
- [ ] The Radhakrishnan 3-g HgTe datum was not promoted to a universal source mass.

---

## J. Atmosphere branch

### Nitrogen purge
- Gas grade/source:
- Purifier/getter:
- Flow:
- Pressure:
- Start/stop:
- Duration:
- O2 endpoint/method:
- H2O/dew-point endpoint/method:

### Process H2 / selected process gas
- Gas grade/source:
- Purifier/getter:
- Flow:
- Pressure/backpressure:
- Start/stop:
- O2/H2O monitoring:

Atmosphere branch revision:

---

## K. Above-liquidus equilibration

- Predicted/published `TL`:
- Local `TL`/proxy:
- Heat-up start:
- Time first above liquidus:
- Peak T:
- Above-liquidus hold start/end:
- Hold duration:
- Evidence used to declare equilibrium:
- Melt appearance/state observation if available:
- Thermal file:

---

## L. Candidate contact-trajectory matrix

Do not average incompatible literature branches. Record physical values.

| Trial ID | `M_charge` | `T_contact` | `ΔT_SC` | cooling rate | `t_contact` | separation T | wipe branch | source-use index |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

DOE/planning document:

---

## M. Physical contact / actuator data per trial

- Trial ID:
- Pre-contact slider position:
- Contact command time:
- First physical overlap:
- Full-overlap time:
- Actual contact duration:
- Contact-end command:
- Physical separation time:
- Commanded travel:
- Measured travel time/speed:
- Stick-slip/anomaly:
- Full `T_solution(t)` file:
- Full `T_substrate(t)` or proxy file:

---

## N. Wipe-off and cooldown

- Wipe branch:
  - [ ] CdTe-piece well
  - [ ] scribed CdTe apron
  - [ ] local branch
- Wipe element IDs/geometry:
- Piece spacing/scribe pattern where relevant:
- Separation temperature:
- Slide-out direction:
- Measured slide-out time/speed:
- Cooling-well arrival time:
- Residual liquid migration observed:
- Scratch/contact event:
- Cooldown program:
- Atmosphere through cooldown:
- Boat removal T/time:
- Unload time:

---

## O. Post-run mass accounting

- Growth solution loaded:
- Accessible residual growth solution:
- Wipe element pre/post mass:
- Hg-source initial/final mass:
- Boat pre/post mass:
- Known material recovered:
- Known material lost:
- Unmeasured/unknown mass pathways:
- Reported mass-closure residual:
- Is residual physically interpretable? Y/N/PARTIAL

Do not force a closed mass balance if evaporation/films/residue are not measured.

---

## P. Material outcomes

### Morphology
- Whole-layer image:
- Usable area:
- Residual melt area fraction:
- Largest droplet:
- Pinhole/void density:
- Scratch density:
- Terrace state:
- Edge-loss width:

### P06/P06A
- Thickness map:
- Mean thickness:
- Spatial sigma/range:
- Mean optical edge/x metric:
- Spatial x variation:
- Target ~9.5 µm approached? Y/N/PARTIAL
- Target x≈.30 approached? Y/N/PARTIAL

### Electrical/material
- As-grown P05 state:
- Post-anneal P05 state:
- Mobility:
- Additional structural data:

---

## Q. Source-use / repeatability

- Growth batch reuse index:
- Hg-source reuse index:
- Repeat-center trial ID:
- Change in liquidus/proxy:
- Change in x mean:
- Change in x spatial variation:
- Change in thickness mean:
- Change in thickness spatial variation:
- Change in morphology/residual melt:
- Change in Hg-source mass loss:

---

## R. Branch-freeze decision

### P16A R04 hardware
- Dimensioned specific boat selected? Y/N
- Calibrated well volume? Y/N
- Thermometry attached? Y/N
- Hot actuator/position state qualified? Y/N
- Proposed state: APPARATUS-NOT-SELECTED / LOCAL-BRANCH-FROZEN

### P16A R05 absolute charge
- Numerical `M_charge` selected? Y/N
- Actual source masses defined? Y/N
- Auxiliary Hg source separately defined? Y/N
- Proposed state: OPEN-CHOICE / LOCAL-BRANCH-FROZEN

### P16A R06 atmosphere
- Gas identities/flows/pressure/purge fully defined? Y/N
- Monitoring/calibration defined? Y/N
- Proposed state: OPEN-CHOICE / LOCAL-BRANCH-FROZEN

### P16A R07 trajectory
- T(t) defined? Y/N
- Contact criterion/time defined? Y/N
- Wipe/separation defined? Y/N
- Cooldown defined? Y/N
- P06/P05 evidence attached? Y/N
- Repeat-center evidence attached? Y/N
- Proposed state: OPEN-CHOICE / LOCAL-BRANCH-FROZEN

### Final P30A disposition
- [ ] METHOD DEFINED — APPARATUS NOT YET SELECTED
- [ ] APPARATUS CALIBRATED — MATERIAL TRIALS OPEN
- [ ] MATERIAL BRACKET IN PROGRESS
- [ ] LOCAL P30/P30A BRANCH FROZEN FOR QUALIFICATION BUILD
- [ ] FAIL / REDESIGN

Reviewer:
Date:
Revision:

---

## Permanent note

No field in this register may be completed by taking the Radhakrishnan `~4.8 g` charge, Honeywell substrate size, or another source's charge and scaling it only by area. Absolute charge is released for the **measured local boat and trajectory**.