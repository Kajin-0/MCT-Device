# P30 — Te-rich horizontal-slider LPE execution qualification register

**Purpose:** blank run record for P30. Every field that is not measured must be marked `OPEN/NA`; do not backfill from nominal settings.

## A. Run identity

- Run ID:
- Date:
- Operator:
- Boat revision / IDs:
- Furnace / tube ID:
- Growth-solution batch ID:
- Growth-solution aliquot/run number:
- Hg-source batch ID / reuse count:
- Substrate ID / P29 record:
- Target branch / recipe ID:

## B. Substrate and interface

- Material / lot:
- Zn fraction / lattice parameter:
- Plane / polarity:
- Miscut magnitude / azimuth:
- Dimensions:
- Final P29 surface recipe:
- Final removed depth:
- Final roughness / surface-state proxy:
- Final-rinse end time:
- Dry-complete time:
- Boat-load time:
- Furnace/purge start time:
- `Δt_clean→boat`:
- `Δt_clean→process`:

## C. Boat geometry

- Graphite grade / lot:
- Substrate recess L × W × depth:
- Growth-well top dimensions:
- Growth-well bottom dimensions:
- Growth-well depth / calibrated volume:
- Hg-source recess dimensions / volume:
- Plug ID / mass:
- Slider-to-base clearance:
- Cover fit / measured gap if available:
- Moat/groove dimensions:
- Growth overlap area:
- Wipe-off hardware branch:
  - [ ] plain slide-off
  - [ ] CdTe-piece wipe-off well
  - [ ] scribed CdTe apron
  - [ ] other qualified branch
- Wipe-off dimensions / element IDs:
- Actuator ID:
- Position calibration / repeatability:

## D. Growth-solution synthesis genealogy

- Preparation family:
  - [ ] sealed-ampoule synthesized charge
  - [ ] in-situ vapor-transport solution preparation
  - [ ] other qualified branch
- Target `xL`:
- Target `yL`:
- Predicted / measured `TL`:
- Elemental Hg lot / purity / mass:
- Elemental Cd lot / purity / mass:
- Elemental Te lot / purity / mass:
- Total weighed mass:
- Mass closure:
- Ampoule material / ID:
- Evacuation endpoint / pressure:
- Seal method:
- Synthesis `T(t)`:
- Peak T:
- Synthesis hold time:
- Cooling sequence:
- Post-synthesis grinding method:
- Mixing/homogenization method/time:
- Storage history:

## E. Per-run charge inventory

- Empty growth-well/boat reference mass:
- Growth aliquot mass loaded:
- Growth-well fill height / fraction:
- Hg source composition:
- Hg source initial mass:
- Hg source geometry / exposed area:
- Other source wafer(s):
- Pre-run total boat mass where applicable:
- Previous runs on same growth batch:
- Cumulative prior HgCdTe grown:

## F. Gas / atmosphere

### Nitrogen purge
- N2 supplier / purity:
- Purifier / getter:
- Flow:
- Start / stop:
- Total duration:
- O2 endpoint:
- H2O/dew-point endpoint:

### Hydrogen / process gas
- H2 supplier / purity:
- Purifier / getter:
- Flow:
- Start time:
- Pressure:
- Exhaust/backpressure state:
- Measured O2/H2O if available:

## G. Furnace / temperature calibration

- Sensor type / ID:
- Sensor location relative to growth well:
- Calibration date / uncertainty:
- Axial gradient map reference:
- Controller ID:
- Data-acquisition sample interval:

## H. Thermal trajectory

- Predicted/measured `TL`:
- Heat-up start:
- Time first above `TL`:
- Peak T:
- Above-liquidus hold start/end:
- Above-liquidus hold duration:
- Equilibration T:
- Equilibration duration:
- Criterion used to declare equilibrium:
- Cooling mode:
  - [ ] step supercool
  - [ ] slow cooling from liquidus
  - [ ] combination
- Intended supercooling:
- Actual T at first contact:
- Actual `ΔT_SC = TL_actual - T_contact`:
- Cooling rate during contact:
- Full T(t) file / location:

## I. Optional meltback / source-wafer interaction

- Meltback branch used? Y/N
- Meltback solution/source ID:
- Meltback contact start/end:
- T(t):
- Removed-depth witness result:
- Source wafer ID / composition / purpose:

## J. Growth contact

- Slider pre-contact position:
- Contact command time:
- First physical overlap time:
- Full-overlap time:
- Contact T:
- Contact duration:
- Contact-end command:
- Physical separation time:
- Commanded slider speed:
- Measured travel distance/time:
- Acceleration setting:
- Stick-slip / anomaly observed:
- Force/torque trace if available:

## K. Wipe-off / slide-out

- Wipe-off branch ID:
- Separation temperature:
- Slide-out direction:
- Commanded speed:
- Measured speed / travel time:
- Cooling-well arrival time:
- CdTe-piece spacing / condition if used:
- CdTe apron material / scribe pattern if used:
- Scratch/contact event observed:
- Visible melt carryover during motion:
- Reverse migration observed:

## L. Cooldown

- Post-separation thermal program:
- T at cooling-well position:
- Time below Te-rich melt mobility/solidification threshold used by local recipe:
- Atmosphere during cooldown:
- Intentional holds:
- Boat removal T/time:
- Room-temperature unload time:

## M. Post-run mass / source genealogy

- Hg source final mass:
- `Δm_Hg_source`:
- Growth charge residual mass if measurable:
- Wipe-off element final mass if measured:
- Post-run total boat mass:
- Melt reuse decision:
- New source-use count:
- Notes on source crusting/segregation/residue:

## N. Immediate surface inspection

- Whole-layer image ID:
- Usable area:
- Residual melt area fraction:
- Largest residual droplet dimensions:
- Number of residual droplets:
- Pinhole/void density:
- Scratch density / maximum scratch length:
- Terrace morphology:
- Edge exclusion width:
- Hg-evaporation-point signature:
- Other morphology notes:

## O. P06 thickness / composition

- Thickness map file:
- Mean thickness:
- Standard deviation:
- Min / max:
- P–V nonuniformity:
- Optical composition/cutoff map file:
- Mean x / defined edge metric:
- Spatial x variation:
- Target met? Y/N/PARTIAL:

## P. Structural / electrical outcome

- HRXRD result:
- Defect / EPD metric:
- As-grown carrier sign:
- As-grown P05 n/p / mobility:
- Post-P04 carrier sign:
- Post-P04 n / mobility:
- P13 lifetime/proxy:
- Device correlation ID if processed:

## Q. Genealogy / drift analysis

- Run number on same melt:
- Run number on same Hg source:
- Change from prior run in x:
- Change from prior run in thickness:
- Change from prior run in residual-melt fraction:
- Evidence of Hg-loss or depletion drift:
- Source branch disposition:
  - [ ] continue
  - [ ] recondition
  - [ ] discard

## R. Qualification disposition

- P30 apparatus gate: PASS / FAIL / HOLD
- Composition gate: PASS / FAIL / HOLD
- Thickness gate: PASS / FAIL / HOLD
- Wipe-off/morphology gate: PASS / FAIL / HOLD
- Source-stability gate: PASS / FAIL / HOLD
- Electrical/material gate: PASS / FAIL / HOLD
- Final disposition:
- Deviations / failure-analysis record:

## Non-negotiable notes

1. Honeywell `xL=.082/yL=.810/TL=507 °C` does not supply an exact total charge mass.
2. Radhakrishnan `10 g synthesis / ~4.8 g run / 3 g HgTe` belongs to a different composition/boat branch.
3. Harman `1 h at 550 °C`, `450–550 °C`, and `0.25–10 min` are direct historical branch values, not universal setpoints.
4. Honeywell’s ~30-min growth example is a separate patent example; do not average it with Harman.
5. CdTe-piece wipe-off and scribed-apron wipe-off are distinct Honeywell hardware generations.
6. Actual measured T(t), contact time, slider motion and source genealogy control interpretation; nominal settings alone do not release a run.
