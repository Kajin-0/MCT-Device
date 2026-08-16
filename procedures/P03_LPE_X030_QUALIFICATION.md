# P03 — Te-rich horizontal-slider LPE qualification for x≈0.30 HgCdTe

**Status:** `QUALIFICATION-CANDIDATE` — NOT a released production recipe.

**Target interface:** produce an HgCdTe epilayer that can enter RP-01 downstream fabrication.

**Nominal material target:**

- Hg1−xCdxTe with x≈0.30;
- n-type after post-growth stoichiometry treatment;
- final active-layer thickness near 9.5 µm;
- electrically insulating CdZnTe substrate;
- final electron concentration near 9.8×10^14 cm^-3;
- final electron mobility near 4.0×10^4 cm² V^-1 s^-1.

This module intentionally separates **growth composition**, **growth thickness**, and **post-growth electrical-state control**. A wafer does not pass merely because its cutoff is correct.

---

## 1. Provenance codes

- `[P-SHW]` — Schmit, Hager, Wood 1982 x=0.2/0.3/0.4 Te-rich horizontal-slider LPE.
- `[P-BS]` — Bowers–Schmit U.S. Patent 4,317,689, same Honeywell Te-rich slider lineage.
- `[P-RSG]` — Radhakrishnan, Sitharaman, Gupta 2003 modified horizontal-slider source.
- `[P-H]` — Harman 1980 Te-rich liquidus/growth study.
- `[P-T]` — Tranchart et al. 1985 CdZnTe/x≈0.30 substrate-growth source.
- `[P-N]` — Nagahama et al. 1984 Hg-overpressure annealing source.
- `[P-RP01]` — Smith et al. 2001 reference detector process.
- `[D]` — derived from primary-source numbers.
- `[CAL]` — apparatus calibration required.
- `[QUAL]` — local transfer qualification required.
- `[OPEN]` — process-critical information not yet closed.

---

## 2. Material target and mandatory release gates

A grown/annealed wafer may proceed to device fabrication only after all of the following are measured:

1. HgCdTe thickness map;
2. spectral/composition map;
3. carrier type;
4. electron concentration;
5. electron mobility;
6. surface-defect/melt-residue inspection;
7. crystal-quality metric;
8. substrate/epilayer integrity.

The reference values from RP-01 are:

- nominal x≈0.30 `[P-RP01]`;
- layer thickness 9.5 µm `[P-RP01]`;
- n=9.8×10^14 cm^-3 `[P-RP01]`;
- µe=4.0×10^4 cm² V^-1 s^-1 `[P-RP01]`.

These are **reference material-state targets**, not proof that the original Fermionics material was grown by the exact process described below.

---

## 3. Selected growth family

The current candidate is Te-rich atmospheric-pressure horizontal-slider LPE because:

- Schmit–Hager–Wood directly report controlled growth of solid x=0.2, 0.3, and 0.4 using this process family `[P-SHW]`;
- the Bowers–Schmit apparatus source gives an explicit liquid composition yielding xS=0.29 `[P-BS]`;
- CdZnTe is the substrate family used by RP-01 and was demonstrated for improved x≈0.30 Te-rich LPE material `[P-T]`.

No other growth family should be substituted into RP-01 without creating a separate reference process ID.

---

## 4. Candidate growth-liquid composition

The Bowers–Schmit source tabulates the following liquid/solid tie line:

- liquid metal Cd fraction: `xL = 0.082` `[P-BS]`;
- liquid Te fraction: `yL = 0.810` `[P-BS]`;
- liquidus temperature: `TL = 507 °C` `[P-BS]`;
- resulting solid Cd fraction: `xS = 0.29` `[P-BS]`;
- `k = xS/xL = 3.54` `[P-BS]`.

The growth solution is therefore written

`(Hg0.918 Cd0.082)0.190 Te0.810`.

### 4.1 Elemental mole fractions `[D]`

- Hg = 0.17442
- Cd = 0.01558
- Te = 0.81000

### 4.2 Derived mass fractions `[D]`

Using Hg=200.59, Cd=112.414, Te=127.60 g/mol:

- Hg mass fraction = 0.249738
- Cd mass fraction = 0.012502
- Te mass fraction = 0.737760

For a selected total charge mass `M`:

- `m_Hg = 0.249738 M`
- `m_Cd = 0.012502 M`
- `m_Te = 0.737760 M`

**Important:** `M` is deliberately not assigned yet. Charge mass/melt depth is an apparatus variable and must be selected from the released growth-well geometry and depletion study. `[OPEN/CAL]`

### 4.3 Charge-preparation hold point

The selected total charge must be accepted only after:

- balance calibration is current;
- each element lot/purity is recorded;
- weighed masses are recorded individually;
- mass closure is calculated;
- final normalized composition is recomputed from actual weighed masses;
- the deviation from target xL/yL is recorded.

Numerical weighing tolerances will be released after a sensitivity analysis maps weighing uncertainty into predicted xS/cutoff uncertainty.

---

## 5. Source-material purity

Radhakrishnan et al. used 6N elemental Cd, Te, and Hg for their horizontal-slider LPE charge preparation. `[P-RSG]`

This is a strong candidate incoming-purity floor for qualification, but it is not directly established as the Honeywell xL=0.082/yL=0.810 source specification. `[QUAL]`

Required lot records:

- supplier;
- lot number;
- nominal purity;
- metallic-impurity certificate where available;
- received mass;
- storage history;
- container opening date.

---

## 6. Substrate

### 6.1 Material family

- electrically insulating CdZnTe `[P-RP01]`.

### 6.2 Composition

Tranchart et al. report Cd1−yZnyTe around y≈0.04 as a substrate used to match/improve x≈0.30 Te-rich LPE material. `[P-T]`

A separate primary lattice-matching study gives an optimum ZnTe mole fraction near 0.029 for Hg0.7Cd0.3Te.

Therefore the production substrate specification must be based on **measured lattice mismatch**, not the statement “4% Zn exactly matches x=0.30.” `[QUAL]`

### 6.3 Orientation

Highest-quality Te-rich slider growth is repeatedly associated with {111}-family substrates in the primary literature. `[P-H]`

The exact RP-01 substrate face/orientation and allowed miscut remain `[OPEN]`.

### 6.4 Incoming substrate measurements

Before LPE qualification, record at minimum:

- dimensions and thickness;
- surface orientation and miscut;
- Zn composition/lattice parameter;
- TTV/warp/bow if the substrate size warrants it;
- IR-transmission microscopy map;
- precipitate/inclusion map;
- dislocation/etch-pit metric where available;
- surface roughness;
- optical micrograph of the growth face.

No substrate may be labeled RP-01-compatible solely from supplier nominal composition.

---

## 7. Slider/furnace architecture

### 7.1 Minimum functional architecture `[P-BS]`

The candidate system requires:

- graphite base/stator with substrate recess;
- graphite movable slider/carrier;
- covered growth-solution well;
- graphite cover;
- separate Hg-supplying source under the cover;
- vapor-distribution grooves/moats or equivalent contained-Hg geometry;
- quartz furnace tube;
- actuator/push-pull mechanism for substrate/solution contact and separation;
- temperature measurement near the growth zone;
- N2 purge capability;
- controlled H2 process-gas capability.

### 7.2 Radhakrishnan process-development geometry `[P-RSG]`

A later modified-slider implementation used:

- high-purity/high-density graphite;
- a 15 mm × 15 mm × 1 mm CdZnTe substrate recess;
- solution bins;
- a dedicated HgTe cavity;
- tightly fitting graphite cover;
- quartz tube with stainless-steel flanges;
- gas-flow, push-pull-rod, and thermocouple ports;
- in-situ substrate meltback;
- geometry intended to improve post-growth wipe-off.

These are useful engineering features, but dimensions outside the stated substrate recess are not yet released for RP-01.

---

## 8. Mercury-loss control

The Bowers–Schmit process uses an auxiliary Hg source of:

- HgTe; or
- HgTe + Te.

`[P-BS]`

The source reports that the Hg vapor pressure over the relevant Te-rich solution is about 0.1 atm near 500 °C and uses the auxiliary source to maintain a comparable local Hg vapor pressure around the growth charge. `[P-BS]`

Radhakrishnan et al. independently used 3 g HgTe per run in their different modified-slider process. `[P-RSG]`

**Do not transfer “3 g HgTe” directly into the Honeywell x≈0.30 boat.** Required Hg-source mass depends on source geometry, free volume, leakage, flow, run duration, and source area. `[QUAL]`

### Qualification metric

A released process must demonstrate that repeated runs do not show a systematic liquidus/composition drift attributable to Hg depletion. This should be tested by:

- pre/post Hg-source mass where practicable;
- run-order versus xS/cutoff regression;
- repeated-growth composition reproducibility;
- inspection for Hg-loss-associated surface features.

---

## 9. Atmosphere sequence

The Bowers–Schmit apparatus source states:

1. assemble/load the covered graphite boat;
2. thoroughly purge with nitrogen before heating;
3. establish flowing H2;
4. heat/equilibrate the growth system;
5. perform growth under the controlled Hg-containing covered environment.

`[P-BS]`

**OPEN/CAL variables:**

- N2 purge flow and duration;
- residual O2/H2O criterion;
- H2 flow rate;
- tube pressure drop;
- exhaust configuration;
- gas purity;
- purifier specification.

These may not be invented from unrelated furnaces.

---

## 10. Thermal sequence

### 10.1 Published liquidus anchor

For xL=0.082, yL=0.810:

`TL = 507 °C`. `[P-BS]`

### 10.2 Published process principle

The growth solution is first heated **above TL** and then brought below TL for epitaxial growth. `[P-BS]`

The source allows:

- step supercooling;
- slow cooling after contact;
- a combination.

### 10.3 500 °C candidate point

The Honeywell source describes growth near 500 °C. For this tie line:

`ΔT = TL − Tgrowth ≈ 507 − 500 = 7 °C`. `[D from P-BS]`

This makes `Tgrowth≈500 °C`, `ΔT≈7 °C` a legitimate **qualification center point**, not yet a production setpoint.

### 10.4 Temperature metrology

Before any qualification run:

- calibrate the growth-zone thermocouple/sensor against a traceable reference;
- map axial temperature gradient over the full solution/substrate length;
- measure controller stability over a duration longer than the complete equilibration + growth sequence;
- record temperature versus time for every run.

A numerical temperature-uniformity/uncertainty requirement will be released after composition sensitivity to temperature has been quantified for this tie-line region.

---

## 11. Equilibration

Harman reports a typical Te-rich growth-solution equilibration time of approximately 1 h at 550 °C in his process. `[P-H]`

The exact equilibration temperature/time for the xL=0.082, yL=0.810 charge in the selected covered boat is not closed. `[OPEN]`

The qualification program must establish equilibrium by showing that extending the hold does not materially change:

- resulting xS/cutoff;
- thickness/growth rate;
- run-to-run reproducibility.

Do not simply copy “1 h at 550 °C” into the x≈0.30 production traveler.

---

## 12. Substrate meltback / interface preparation

Radhakrishnan et al. incorporated in-situ meltback immediately before growth to remove the contaminated substrate/epilayer interface region. `[P-RSG]`

This is a strong candidate module because interface impurity accumulation is a known LPE problem.

However, the exact meltback solution composition, time, temperature, and removed thickness for an RP-01 x≈0.30 CdZnTe substrate are not yet closed. `[OPEN]`

No meltback process should be released until its removed depth and effect on substrate morphology are measured.

---

## 13. Growth initiation

After the selected supercooling/thermal condition is reached:

- translate the slider so the molten growth charge contacts the prepared substrate `[P-BS]`;
- record contact timestamp;
- continue the programmed thermal trajectory;
- record full temperature trace.

The exact translation speed is `[OPEN/CAL]`.

---

## 14. Growth duration and thickness

The Honeywell patent gives an example where growth may continue for about 0.5 h, while Harman reports 0.25–10 min growth durations for 3–15 µm layers in a different process. `[P-BS/P-H]`

This divergence is precisely why a fixed time cannot be imported from the literature.

RP-01 requires approximately 9.5 µm final material thickness. `[P-RP01]`

### Required local calibration

For the selected boat and thermal program, measure thickness versus contact time at fixed charge composition and thermal condition.

At least three distinct times should bracket 9.5 µm, with multiple coupons/runs at the center point.

Fit a local relation

`t_layer = f(t_growth, ΔT, thermal trajectory, charge history)`

only over the experimentally supported region.

Production time may be released only after:

- mean target thickness is centered near 9.5 µm;
- across-wafer uniformity is quantified;
- run-to-run standard deviation is known;
- composition is simultaneously within target.

---

## 15. Growth termination / wipe-off

Growth is terminated by separating the substrate from the growth liquid via slider motion. `[P-BS]`

Radhakrishnan et al. emphasize that poor wipe-off produces residual melt droplets, strain, unusable area, pinholes/voids, and other morphology defects. `[P-RSG]`

Required qualification variables:

- translation direction;
- translation speed;
- temperature at separation;
- substrate/solution overlap geometry;
- final solution drainage path;
- residual-droplet count/area.

These remain `[OPEN/CAL]` until the selected boat is characterized.

---

## 16. Immediate post-growth metrology

Every qualification wafer must receive, before post-growth annealing:

### 16.1 Surface inspection

- whole-wafer bright-field image;
- Nomarski/DIC inspection;
- map of residual melt droplets;
- map of pinholes/voids;
- scratch/terrace documentation;
- edge exclusion recorded explicitly.

### 16.2 Thickness

Map thickness at a defined grid. The released manual must eventually specify:

- instrument;
- calibration standard;
- grid coordinates;
- repeatability;
- wafer mean;
- min/max;
- 1σ;
- peak-to-valley nonuniformity.

### 16.3 Composition / spectral response

Measure an FTIR transmission or equivalent composition/cutoff map at corresponding positions.

Report the wavelength convention explicitly; do not use “cutoff” without definition.

### 16.4 Electrical state

Measure a companion Hall/Van der Pauw coupon before annealing to establish whether the layer is p- or n-type and its carrier density/mobility.

---

## 17. Post-growth Hg-overpressure anneal interface

Te-rich LPE material may be p-type as grown because of Hg vacancies.

Nagahama et al. demonstrate that Hg-overpressure annealing in the 250–300 °C range can produce n-type layers without the compositional change observed at 400 °C. `[P-N]`

This supports a separate low-temperature anneal qualification module.

The following remain open and must **not** be guessed here:

- anneal time;
- Hg reservoir mass/activity;
- sealed/open configuration;
- temperature ramp;
- cool-down;
- target equilibrium/quench condition;
- resulting n and µ at x≈0.30.

The LPE wafer is not RP-01-compatible until this electrical-state module is passed.

---

## 18. Final material acceptance targets

The following are initial RP-01 reference targets, not statistical production tolerances:

- composition: x≈0.30;
- thickness: ~9.5 µm;
- conductivity: n-type;
- n: ~9.8×10^14 cm^-3;
- µe: ~4.0×10^4 cm² V^-1 s^-1.

Production acceptance windows require process-capability data.

At minimum, each released material lot must report:

- x/cutoff mean and spatial spread;
- thickness mean and spatial spread;
- Hall n and µ at stated temperature;
- surface defect density/usable area;
- substrate lot/orientation/Zn metric;
- full growth thermal trace;
- charge lot and actual weighed composition;
- anneal record.

---

## 19. Initial qualification experiment structure

The first scientifically useful DOE should **not** vary every parameter simultaneously.

### Stage A — reproduce composition

Hold:

- xL=0.082;
- yL=0.810;
- selected boat/well geometry;
- substrate family;
- Hg-loss-control geometry.

Investigate a narrow thermal/supercooling range around the 500 °C / TL=507 °C literature point and measure xS spatially.

### Stage B — calibrate thickness

After composition stability is established, vary contact/growth time to bracket 9.5 µm while holding composition/thermal variables fixed.

### Stage C — qualify electrical-state anneal

Use matched coupons from a single growth run to map Hg-overpressure anneal condition to:

- carrier type;
- n;
- mobility;
- spectral/cutoff shift;
- surface morphology.

### Stage D — repeatability

Run the nominal process repeatedly with new charges/substrates to estimate run-to-run composition, thickness, and electrical-state capability.

---

## 20. Major failure modes

Log at least:

- Hg depletion / liquidus drift;
- solid composition outside target;
- vertical/lateral composition gradient;
- thickness outside target;
- excessive terracing;
- residual melt droplets;
- substrate sticking/breakage;
- pinholes/voids;
- slider scratches;
- nonuniform wipe-off;
- interface contamination;
- incorrect post-growth carrier type;
- carrier density too high;
- mobility degradation;
- anneal-induced composition shift;
- substrate/epilayer cracking or delamination.

---

## 21. Safety hold point

This qualification involves elemental Hg/Cd/Te, HgTe, high-temperature quartz/graphite assemblies, hydrogen, mercury vapor, and potentially sealed ampoules. The scientific variables in this file are not an operating authorization. A laboratory must separately establish institution-approved controls for toxic-metal exposure, Hg-vapor monitoring/containment, pyrophoric/flammable-gas systems, furnace interlocks, purge verification, pressure/vacuum integrity, ampoule handling, exhaust treatment, and hazardous waste before execution.

---

## 22. Release blockers

P03 remains `QUALIFICATION-CANDIDATE` until the following are closed:

1. exact CdZnTe composition/orientation/miscut specification;
2. substrate cleaning/polishing process;
3. selected boat dimensions and growth-well volume;
4. total growth-charge mass;
5. exact synthesis/homogenization protocol for xL=0.082/yL=0.810;
6. N2/H2 purity/flow/purge criteria;
7. Hg-source geometry/mass qualification;
8. equilibrium hold condition;
9. exact ΔT/cooling trajectory;
10. substrate-contact translation speed;
11. growth time for 9.5 µm;
12. wipe-off mechanics;
13. composition/thickness acceptance windows;
14. post-growth n-type anneal recipe;
15. final statistical material-property acceptance limits.

---

## 23. Primary references

1. J. L. Schmit, R. J. Hager, R. A. Wood, “Liquid phase epitaxy of Hg1−xCdxTe,” *Journal of Crystal Growth* 56, 485–489 (1982), DOI `10.1016/0022-0248(82)90468-7`.
2. J. E. Bowers, J. L. Schmit, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution,” U.S. Patent 4,317,689 (1982).
3. T. C. Harman, “Liquidus isotherms, solidus lines and LPE growth in the Te-rich corner of the Hg-Cd-Te system,” *Journal of Electronic Materials* 9 (1980), DOI `10.1007/BF02822728`.
4. J. C. Tranchart, B. Latorre, C. Foucher, Y. Le Gouge, “LPE growth of Hg1−xCdxTe on Cd1−yZnyTe substrates,” *Journal of Crystal Growth* 72, 468–473 (1985).
5. J. K. Radhakrishnan, S. Sitharaman, S. C. Gupta, “Liquid phase epitaxial growth of HgCdTe using a modified horizontal slider,” *Journal of Crystal Growth* 252, 79–86 (2003), DOI `10.1016/S0022-0248(02)02530-7`.
6. K. Nagahama, R. Ohkata, K. Nishitani, T. Murotani, “LPE growth of Hg1−xCdxTe using conventional slider boat and effects of annealing on properties of the epilayers” (1984 primary experimental paper; complete bibliographic metadata still to be verified in the source ledger).
7. E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
