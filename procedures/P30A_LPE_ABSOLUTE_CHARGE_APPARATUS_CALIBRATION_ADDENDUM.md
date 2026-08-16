# P30A — absolute LPE charge / apparatus-capacity / contact-trajectory calibration addendum

**Status:** CONTROLLED EMPIRICAL CLOSURE METHOD / PRE-FIRST-BUILD  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Close the specific execution gap identified by P16A rows R04–R07 without inventing a Honeywell/Fermionics charge mass.

P30 already defines the horizontal-slider process variables. P30A defines how an actual laboratory shall convert the published composition/architecture evidence into a **numerically frozen local apparatus branch**:

`measured boat geometry -> usable hot melt volume -> selected absolute charge -> measured liquidus/thermal field -> substrate contact trajectory -> wipe/separation -> P06/P05 outputs -> repeatability -> LOCAL-BRANCH-FROZEN`.

P30A does **not** claim recovery of the historical RP-01 or Fermionics growth traveler.

---

## 2. Evidence boundary established in Round 35

### 2.1 Direct Honeywell geometry is real but not dimensioned

Bowers and Schmit, US4317689A / US4366771A, directly establish a covered graphite horizontal-slider architecture including:

- graphite base with a substrate recess;
- movable graphite slider/carrier;
- two through-wells in the more preferred embodiment;
- through-wells described as somewhat tapered, with smaller lower openings;
- graphite plug/cap for the growth-solution well;
- separate shallow Hg-source recess;
- Hg-distribution moats/grooves above and below the slider;
- close-fitting graphite cover;
- recessed regions associated with the growth wells generally corresponding in size to the substrate recess;
- quartz-tube furnace;
- nitrogen purge followed by flowing hydrogen;
- growth-solution heating above liquidus followed by growth below liquidus.

For the composition-matched row near RP-01:

- `xL = 0.082`;
- `yL = 0.810`;
- `TL = 507 °C`;
- `xS ≈ 0.29`.

**Round-35 source audit result:** the recovered primary patent text does not provide a numerical well depth, well volume, boat dimension, substrate-recess dimension, or absolute growth-charge mass for this x≈0.29 branch.

Therefore:

`DIRECT-HONEYWELL-GEOMETRY != DIRECT-HONEYWELL-DIMENSIONS`  
`DIRECT-HONEYWELL-COMPOSITION != DIRECT-HONEYWELL-CHARGE-MASS`.

### 2.2 Quantitative Te-rich transfer apparatus exists, but it is a different branch

Radhakrishnan, Sitharaman and Gupta, *Journal of Crystal Growth* 252 (2003) 79–86, DOI `10.1016/S0022-0248(02)02530-7`, report a modified slider process with:

- `15 mm × 15 mm × 1 mm` CdZnTe substrates;
- about `10 g` synthesized growth compound;
- about `4.8 g` growth charge used per run;
- `3 g` HgTe reservoir per run;
- 6N starting elements;
- evacuated-quartz synthesis at `700 °C / 8 h`.

These values establish a physically real Te-rich LPE apparatus/mass scale. They do **not** define the Honeywell xL=.082/yL=.810 mass and shall not be rescaled by substrate area.

### 2.3 Harman trajectory data strengthen calibration, not mass closure

Harman's Te-rich LPE work and MIT patent provide quantitative growth-trajectory transfer evidence, including:

- supercooling in roughly the `2–10 °C` range in represented branches;
- contact/growth times spanning seconds to tens of minutes depending on branch;
- slow-cooling and step-supercooling variants;
- measured thickness changes with time/cooling trajectory;
- examples on `4 × 10 mm` and `8 × 8 mm` substrates.

The same sources do not provide a universal solution-mass-per-area rule.

### 2.4 Fermionics is material lineage, not recovered process identity

Same-era UWA work explicitly identifies Fermionics-supplied LPE HgCdTe/CdZnTe material. This supports vendor/material genealogy. No recovered primary Fermionics traveler has yet supplied the internal boat dimensions, growth charge, Hg-source mass, or exact contact/cooldown trajectory used for RP-01 material.

---

## 3. Non-negotiable separation of apparatus coordinates

P30A shall keep these quantities independent:

- `V_well,geom` — room-temperature geometric well volume;
- `V_plug` — volume displaced by any plug/cap intrusion;
- `V_hot,usable` — locally qualified hot usable solution volume;
- `M_charge` — absolute loaded growth-solution mass;
- `h_melt` — melt depth/meniscus state under process temperature;
- `A_overlap` — actual solution/substrate overlap area;
- `M_Hg,res` — separate Hg/HgTe auxiliary-source inventory;
- `T_solution(t)` — actual solution-region thermal history;
- `T_sub(t)` — substrate-region thermal history;
- `t_contact` — physical solution/substrate contact interval;
- `X_source-use` — source/reuse genealogy.

Do not replace any of these with another because two runs have the same nominal composition.

---

## 4. Prohibited scaling shortcut

The following is **not** an approved charge calculation:

`M_new = M_reference × A_sub,new / A_sub,reference`.

Area scaling is invalid unless all relevant geometric and thermofluid coordinates are independently shown equivalent, including at minimum:

- well depth/shape;
- melt depth/meniscus;
- substrate-to-well clearance;
- free surface area;
- Hg-loss path;
- overlap/contact geometry;
- thermal gradients;
- source depletion fraction.

Primary finite-dimension LPE modeling also shows that liquid dimensions and Hg-loss boundary conditions affect growth behavior; substrate area alone is not a sufficient scale coordinate.

---

# 5. Stage A — freeze and measure the local boat

Before any composition-sensitive growth run, assign a permanent boat revision and create a dimensioned drawing.

Measure and record:

- graphite grade/supplier/lot;
- base L/W/H;
- slider L/W/H;
- cover L/W/H;
- substrate recess L/W/depth;
- substrate top-plane height relative to base datum;
- each growth-well top opening L/W or diameter;
- each growth-well bottom opening L/W or diameter;
- taper/profile;
- well depth;
- plug geometry and insertion depth;
- auxiliary Hg-source recess L/W/depth;
- top and bottom moat/groove dimensions;
- channel dimensions connecting Hg-source region to moats;
- cover-to-slider gap/fit;
- slider-to-base clearance;
- overlap area at each indexed slider position;
- wipe-off/cooling-well geometry;
- actuator stroke;
- position repeatability;
- flatness/parallelism of base and slider.

### 5.1 Geometric volume

Calculate `V_well,geom` from the measured drawing, including taper and plug displacement.

Report:

`V_well,geom ± u(V_well)`.

Do not infer volume from a nominal drill/end-mill size alone.

### 5.2 Dimensional witness

Retain one of:

- coordinate-metrology report;
- calibrated optical/mechanical dimensional report;
- mass/volume capacity calibration with a chemically compatible room-temperature surrogate;
- equivalent traceable method.

A surrogate may calibrate geometry/capacity only; it does not prove molten-HgCdTe wetting or hot meniscus behavior.

---

# 6. Stage B — hot mechanical and thermal apparatus calibration

Before consuming qualification HgCdTe source material, characterize the apparatus under the selected process atmosphere as far as facility safety permits.

Record:

- furnace/tube/boat axial position;
- controller/sensor IDs;
- sensor locations relative to growth well and substrate;
- static axial and transverse temperature map;
- controller-to-boat temperature offset;
- temperature lag during representative ramp/cool trajectories;
- slider travel time at temperature;
- position repeatability at temperature;
- stick-slip/force anomalies;
- slider/base clearance change where measurable;
- cover/slider motion interference;
- cooling-well transition timing.

### 6.1 Required thermal distinction

`T_controller != T_growth_solution` until calibrated.

P30/P03E shall use the calibrated solution-region temperature or explicitly stated proxy with uncertainty.

### 6.2 Honeywell trajectory constraint

For the Honeywell-derived branch, the growth solution shall first be demonstrated to reach a state above its measured/local liquidus before the below-liquidus contact trajectory is initiated.

The published `TL=507 °C` is the equilibrium tie-line anchor for xL=.082/yL=.810. It is not a substitute for local thermometry calibration or an observed local melting/liquidus check.

---

# 7. Stage C — composition calculation after absolute mass is selected

Once a candidate local total charge mass `M_charge` is selected from the measured apparatus-capacity study, calculate target elemental masses from the xL=.082/yL=.810 composition.

Using current project atomic-weight convention, the derived mass fractions are approximately:

- `w_Hg = 0.249740`;
- `w_Cd = 0.012502`;
- `w_Te = 0.737758`.

Therefore:

`m_Hg,target = 0.249740 M_charge`

`m_Cd,target = 0.012502 M_charge`

`m_Te,target = 0.737758 M_charge`.

These equations define masses **after `M_charge` has been locally selected**. They do not determine `M_charge`.

Record target and actual masses to full balance resolution and recompute the realized mole fractions from the actual weighed masses.

### 7.1 No premature Cd rounding

Because Cd is the smallest mass component in this tie-line representation, preserve full balance resolution through the charge calculation and sensitivity analysis.

---

# 8. Stage D — establish a local inventory bracket

P30A intentionally does not prescribe a universal gram value.

Before the first material run, the qualification engineer shall define a **numerical candidate inventory bracket** from:

1. measured `V_well,geom` and plug displacement;
2. verified containment/freeboard at process temperature;
3. substrate overlap geometry;
4. actuator/wipe-off clearance;
5. the selected Te-rich solution density model or measured material-volume relation, with evidence class;
6. primary transfer evidence only as a plausibility check.

The actual candidate masses must be written into the P30A traveler **before** the run.

A run is not `TRACEABLE-FIRST-BUILD-READY` while the traveler still contains an operator instruction such as “fill well appropriately.”

### 8.1 Coded DOE is not a released setpoint

Low/center/high or coded inventory coordinates may be used for development, but the physical masses must be explicitly recorded. Coded coordinates do not become a production tolerance.

---

# 9. Stage E — Hg-source inventory is independent

The auxiliary Hg/HgTe source is not part of `M_charge`.

Record separately:

- source chemistry/form;
- initial mass;
- source recess geometry;
- exposed source area;
- source temperature or calibrated proxy;
- run/reuse count;
- final mass;
- `Δm_source`;
- growth-solution mass change;
- evidence of condensation or unintended transport.

The Radhakrishnan `3 g HgTe` value is a transfer datum only. Honeywell's patent-level ~0.1-atm Hg-vapor discussion does not identify a universal source mass.

---

# 10. Stage F — first-contact / thickness calibration

The first local thickness study shall not assume that a published time transfers directly.

Preserve distinct literature branches:

- Honeywell general apparatus example: growth may continue about `30 min`;
- Harman 1980 experimental branch: approximately `0.25–10 min` with `3–15 µm` layers over represented conditions;
- Harman/MIT Hg-pressure-controlled branch: seconds-to-30-min contact windows with thickness strongly dependent on cooling/supercooling;
- Shinohara 1994: equilibrium cooling produced `2–4 µm`, while `15 K` supercooling/step cooling produced `30–40 µm` in its branch.

These values demonstrate trajectory sensitivity; they are not averaged into one recipe.

For the local branch, record and vary only physically defined coordinates:

- actual `T_contact`;
- `ΔT_SC = TL_local - T_contact`;
- cooling rate during contact;
- physical `t_contact`;
- `M_charge`;
- source-use index;
- actual separation temperature.

Measure P06 thickness and composition at registered positions after every run.

---

# 11. Stage G — mass balance and source-use closure

For every qualification run, measure where feasible:

`M_loaded_growth`

`M_residual_growth`

`M_Hg,res,initial`

`M_Hg,res,final`

`M_wipeoff_gain`

`M_boat_pre/post`.

Define a mass-closure residual only from quantities actually measured. Do not force a closed balance when evaporation, retained films or inaccessible residue are not measured.

Track versus source-use index:

- liquidus shift;
- layer mean x/edge;
- x spatial variation;
- mean thickness;
- thickness spatial variation;
- residual melt fraction;
- Hg-source loss;
- morphology.

A reused melt is a sequential genealogy, not an independent replicate.

---

# 12. Stage H — wipe-off and separation qualification

Choose one hardware branch and keep it distinct:

1. Honeywell CdTe-piece wipe-off well;
2. Honeywell scribed CdTe apron;
3. another explicitly local branch.

For every run record:

- physical separation temperature;
- slide direction;
- commanded and measured travel time/speed;
- stick-slip;
- slider clearance/flatness state;
- wipe element identity/geometry;
- post-run residual melt area fraction;
- largest droplet;
- scratch/void/pinhole metrics.

Do not change wipe hardware while using the same process-revision label.

---

# 13. Minimum response vector for freezing a local P30 branch

A local branch is judged on:

`Y_LPE = {x_mean, x_spatial, d_mean, d_spatial, morphology, residual_melt, pinholes/voids, scratches, liquidus stability, source mass loss, as-grown Hall state, post-anneal Hall compatibility}`.

A visually smooth film is insufficient.

The x/thickness map must retain physical coordinates so later P05/P11/device data can be tied to material genealogy.

---

# 14. P16A closure criteria for R04–R07

P30A provides the closure route but does not automatically change the project state.

### R04 — LPE boat/well/source hardware

Can move from `APPARATUS-NOT-SELECTED` to `LOCAL-BRANCH-FROZEN` only when:

- a specific boat/furnace/tube/actuator revision is selected;
- dimensioned geometry exists;
- well volume and clearances are measured;
- thermometry/position calibration is attached.

### R05 — absolute LPE charge inventory

Can move from `OPEN-CHOICE` to `LOCAL-BRANCH-FROZEN` only when:

- a numerical `M_charge` is selected for that boat;
- actual elemental/compound masses are specified;
- auxiliary Hg-source inventory is specified independently;
- mass/load genealogy is traceable.

### R06 — LPE atmosphere

Can move to `LOCAL-BRANCH-FROZEN` only when:

- gas identities, purities, flows/pressure and purge/process sequence are explicit;
- actual instrumentation/monitoring and acceptance method are named.

### R07 — thermal/contact/wipe/cooldown trajectory

Can move to `LOCAL-BRANCH-FROZEN` only when:

- local liquidus/temperature proxy is calibrated;
- numerical T(t), contact criterion/time and separation trajectory are specified;
- wipe hardware/motion is selected;
- cooldown is specified through unload-safe state;
- P06/P05 qualification evidence supports the selected branch.

Until those records exist, the project remains not `TRACEABLE-FIRST-BUILD-READY` even though the method for closing the gap is now defined.

---

# 15. Historical identity status after Round 35

Still `OPEN-HISTORICAL`:

- Fermionics/Honeywell boat dimensions used for the RP-01 material;
- absolute x≈0.30 growth-charge mass;
- Hg-source mass;
- exact N2/H2 flows;
- exact solution/substrate thermocouple geometry;
- exact equilibration duration;
- exact 9.5-µm contact/cooling trajectory;
- exact wipe-off hardware generation;
- exact cooldown.

These gaps block a literal historical-process claim but do not prevent a future explicitly labeled local P30/P30A branch from becoming executable.

---

# 16. Primary sources retained

- R. C. Bowers, J. L. Schmit, US4317689A, “Liquid phase epitaxial growth of mercury cadmium telluride.”
- R. C. Bowers, J. L. Schmit, US4366771A, divisional continuation.
- R. J. Hager / Honeywell, US4592304A, CdTe-piece wipe-off architecture.
- R. J. Hager / Honeywell, US4706604A, scribed-apron wipe-off architecture.
- T. C. Harman, *J. Electron. Mater.* 9 (1980), DOI `10.1007/BF02822728`.
- T. C. Harman, *J. Electron. Mater.* 10 (1981), DOI `10.1007/BF02661192`.
- T. C. Harman / MIT, US4642142A, Hg-pressure-controlled Te-rich LPE apparatus/trajectory evidence.
- J. K. Radhakrishnan, S. Sitharaman, S. C. Gupta, *J. Cryst. Growth* 252 (2003) 79–86, DOI `10.1016/S0022-0248(02)02530-7`.
- M. Shinohara et al., *J. Cryst. Growth* 141 (1994) 352–356, DOI `10.1016/0022-0248(94)90237-2`.

---

## Permanent Round-35 rule

**Absolute LPE charge is an apparatus coordinate.**

A composition tie line, substrate area, or another laboratory's charge mass does not determine the grams to load into a new horizontal-slider boat. The local charge becomes executable only after boat geometry/capacity, thermal state, contact trajectory and material outcomes are jointly calibrated.