# P04 — Hg-overpressure stoichiometry anneal qualification for RP-01 material

**Status:** `QUALIFICATION-CANDIDATE` — NOT a released production anneal.

**Purpose:** Convert Te-rich LPE HgCdTe into the low-density n-type electrical state required by RP-01 while preserving alloy composition, layer thickness, morphology, crystal quality, and subsequent detector performance.

**RP-01 final-state reference:**

- nominal alloy composition: x≈0.30;
- layer thickness: ~9.5 µm;
- conductivity: n-type;
- electron concentration: ~9.8×10^14 cm^-3;
- electron mobility: ~4.0×10^4 cm² V^-1 s^-1.

The anneal is controlled by the **final measured material state**, not by temperature/time alone.

---

## 1. Why this is a separate process module

Te-rich LPE HgCdTe is commonly p-type as grown because the growth/thermal history can leave a high concentration of Hg-vacancy acceptors. The post-growth Hg-rich anneal changes the native-defect population and can convert this material to n-type.

The same operation can also:

- alter carrier concentration by orders of magnitude;
- alter compensation;
- redistribute or annihilate native defects;
- alter Te precipitates;
- multiply or rearrange dislocations under some conditions;
- change alloy composition if the temperature/chemical potential is inappropriate;
- change the electrical interpretation of Hall measurements.

Therefore annealing is a controlled material-state transformation, not a generic furnace bake.

---

## 2. Primary-source anchors

### 2.1 Harman pressure-controlled LPE/anneal process

T. C. Harman, U.S. Patent 4,642,142, “Process for making mercury cadmium telluride,” gives a primary process description in which a HgCdTe epilayer is annealed under controlled Hg vapor after LPE.

Published process anchors include:

- general anneal-temperature range: approximately 200–300 °C;
- Hg partial-pressure range: approximately 0.1–250 Torr;
- pressure selected according to the desired stoichiometric defect state;
- pseudo-isothermal Hg-saturated anneal example: 250 °C for 1 h, followed by cooling to room temperature;
- sample temperature and Hg pressure are both treated as state variables;
- the patent's in-situ-annealed layers typically had carrier concentrations in the low 10^16 cm^-3 range.

**Compatibility warning:** This establishes a credible anneal architecture and a kinetic anchor, but its reported electrical endpoint is roughly an order of magnitude above the RP-01 target. Therefore `250 °C / 1 h` is not automatically the RP-01 production anneal.

### 2.2 Nagahama–Ohkata–Nishitani–Murotani 1984 branch

Primary experimental work on LPE Hg1−xCdxTe spanning approximately x=0.17–0.30 reports:

- as-grown p-type layers;
- Hg-overpressure annealing over 250–400 °C;
- 400 °C produced detectable compositional change near the interface;
- 250–300 °C produced well-behaved n-type layers without apparent compositional change.

This is directly relevant to x≈0.30 RP-01-like material but the exact anneal time, Hg-source configuration, cooldown and final carrier concentration/mobility remain to be recovered.

### 2.3 Jones–Quelch–Capper–Gosney 1982 defect-control study

C. L. Jones, M. J. T. Quelch, P. Capper, and J. J. G. Gosney, “Effects of annealing on the electrical properties of CdxHg1−xTe,” *Journal of Applied Physics* 53, 9080–9092 (1982), DOI `10.1063/1.330419`, investigated approximately x=0.17–0.31 material using both closed-tube and open-tube methods.

The study distinguishes:

- **isothermal anneal:** Hg reservoir temperature approximately equal to HgCdTe temperature;
- **two-temperature anneal:** Hg reservoir held below the HgCdTe temperature.

The primary result relevant to RP-01 is that isothermal Hg-rich treatment converts native-defect-controlled p-type material to n-type, while lower Hg chemical potential can establish p-type material. This confirms that Hg partial pressure is a required controlled variable, not simply an ambient label.

### 2.4 Chandra–Schaake–Kinch 2003 kinetics

D. Satish Chandra, H. F. Schaake, and M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *Journal of Electronic Materials* 32, 810–815 (2003), DOI `10.1007/s11664-003-0075-5`, shows that low-temperature annealing kinetics depend strongly on:

- vacancy concentration;
- alloy composition x;
- temperature.

The annealing rate decreases as CdTe mole fraction increases over the studied range. Therefore an anneal time transferred from x≈0.20 material cannot be assumed correct for x≈0.30.

---

## 3. Controlled variables

A released anneal traveler must explicitly control or measure all of the following.

### Sample variables

- wafer/coupon ID;
- growth-run ID;
- x/composition map before anneal;
- thickness map before anneal;
- pre-anneal carrier type;
- pre-anneal carrier concentration;
- pre-anneal Hall mobility;
- surface morphology;
- starting defect/dislocation metric where available.

### Thermal variables

- sample temperature `T_s`;
- Hg reservoir/source temperature `T_Hg` if a separate source zone is used;
- ramp rate to anneal;
- soak time;
- temperature stability during soak;
- spatial temperature uniformity over the sample;
- cooldown trajectory;
- temperature at which Hg chemical potential is reduced/removed, if applicable.

### Chemical-potential variables

- Hg source type: elemental Hg, HgTe, or other qualified source;
- source mass/area;
- source temperature;
- chamber free volume;
- open-tube vs closed-tube configuration;
- carrier gas if open-tube;
- Hg partial pressure or a thermodynamically justified proxy;
- leakage/flow condition;
- position of source relative to sample.

### Metrology variables

- thermocouple/reference type;
- thermocouple location;
- calibration date;
- pressure measurement method where used;
- Hall measurement temperature and magnetic field;
- FTIR/spectral mapping convention;
- thickness method;
- surface/crystal-quality method.

---

## 4. Anneal architecture options

Two architectures are scientifically defensible and must be treated as separate qualified recipes.

### 4.1 Isothermal Hg-saturated route

Concept:

- establish a Hg chemical potential near the Hg-rich/isothermal boundary for the sample temperature;
- anneal the material until Hg vacancies/native acceptors are sufficiently reduced;
- maintain the Hg-rich condition during the relevant high-temperature portion of cooldown.

Primary-source anchor:

- Harman gives a typical 250 °C, 1 h pseudo-isothermal treatment.

Expected qualitative outcome:

- p-to-n conversion is favored.

### 4.2 Two-temperature route

Concept:

- sample at `T_s`;
- separate Hg reservoir at `T_Hg < T_s`;
- Hg pressure therefore lower than the isothermal saturation condition.

This route can intentionally establish a different native-defect equilibrium and must not be interchanged with the isothermal route.

For RP-01, the initial qualification program should prioritize the Hg-rich/isothermal branch because the required final state is n-type.

---

## 5. Initial temperature window

Primary sources support the following working interpretation:

- 250–300 °C: strong candidate window for p-to-n conversion with lower risk of composition change;
- ~400 °C: explicit literature warning for composition alteration in the Nagahama branch;
- <300 °C: standard low-temperature native-defect-control regime.

Accordingly, the first RP-01 transfer DOE should remain below 300 °C unless a separate, justified high-temperature objective is introduced.

### Initial center point

`T_s = 250 °C`, `t = 1 h`, Hg-rich/isothermal-like condition

is a valid **screening center point** because it is directly anchored by the Harman process.

It is not a released recipe because Harman's corresponding material typically ended in the low-10^16 cm^-3 regime rather than RP-01's ~10^15 cm^-3 regime.

---

## 6. Temperature-control requirement

Harman's LPE process emphasizes temperature control within <1 °C and preferably ~0.2 °C in composition-sensitive portions of the process. The anneal module shall initially adopt comparably rigorous temperature logging until its own sensitivity study establishes a justified tolerance.

Required qualification measurements:

- traceable temperature-sensor calibration;
- sample-zone axial/radial temperature map;
- source-zone map if a two-zone arrangement is used;
- logged `T_s(t)` and `T_Hg(t)`;
- maximum deviation from target during the soak;
- thermal lag between furnace controller and sample fixture.

Do not infer sample temperature from controller setpoint alone.

---

## 7. Hg partial-pressure control

Harman gives a broad primary process range of approximately 0.1–250 Torr Hg partial pressure for 200–300 °C annealing, with the selected pressure dependent on the desired stoichiometric defect state.

This range is **not** a recipe window to sweep blindly. For RP-01, the selected Hg chemical potential must be tied to a defined thermodynamic state and verified by the resulting electrical properties.

### Preferred qualification hierarchy

1. control both sample and Hg-source temperatures;
2. calculate expected Hg vapor pressure from a documented Hg source relation;
3. independently verify furnace-zone temperature calibration;
4. maintain a reproducible sample/source geometry;
5. use Hall electrical state as the process outcome metric.

The final traveler must record either measured Hg partial pressure or sufficient calibrated source-temperature/geometry information to reconstruct it.

---

## 8. Pre-anneal characterization gate

Before annealing, each qualification sample must have:

- composition/cutoff value at defined positions;
- thickness;
- Hall carrier sign;
- Hall carrier concentration;
- Hall mobility;
- optical/Nomarski morphology images;
- sample dimensions and orientation;
- wafer-position provenance.

Where sample area permits, divide a growth run into matched coupons so several anneal conditions are compared against essentially identical starting material.

---

## 9. Initial qualification DOE

The objective is to find an anneal condition that reaches the RP-01 electrical state while preserving composition.

### Stage A — time dependence at 250 °C

At a fixed, reproducibly Hg-rich condition, investigate at least:

- 0.5 h;
- 1 h;
- 2 h;
- 4 h.

`1 h` is the Harman primary-source anchor. The additional times are qualification points, not published RP-01 values.

For each time measure post-anneal:

- carrier sign;
- `n` or `p`;
- mobility;
- composition/cutoff;
- thickness;
- morphology.

### Stage B — temperature dependence

After identifying a useful time region, compare approximately:

- 225 °C;
- 250 °C;
- 275 °C.

These are proposed DOE levels within the established sub-300 °C defect-control regime. They are not all claimed as literature-optimum conditions.

### Stage C — Hg chemical-potential dependence

At fixed sample temperature/time, vary the Hg-source condition narrowly around the selected Hg-rich state to quantify sensitivity of final carrier concentration.

Do not change sample temperature and Hg chemical potential simultaneously in the first sensitivity experiment.

### Stage D — repeatability

Repeat the selected nominal condition on multiple matched coupons and then across multiple LPE runs.

---

## 10. Primary response variables

The principal response is not merely “became n-type.” Record:

1. `n_77K` or other explicitly selected reference-temperature carrier concentration;
2. `µe_77K`;
3. carrier sign versus temperature where feasible;
4. composition/cutoff shift;
5. thickness change;
6. surface morphology change;
7. defect/dislocation metric change;
8. spatial uniformity of electrical state.

Target electrical reference:

`n ≈ 9.8×10^14 cm^-3`

`µe ≈ 4.0×10^4 cm² V^-1 s^-1`

from RP-01.

Production tolerance must be established from detector-performance sensitivity and process capability; it is not yet assigned.

---

## 11. Composition-preservation gate

Because 400 °C annealing produced interface-region composition changes in the Nagahama branch, every qualification anneal must compare pre/post composition using the same calibrated method.

At minimum:

- identical FTIR/spectral positions before and after;
- explicitly defined wavelength/cutoff metric;
- convert to x only with a stated model and temperature;
- report measurement repeatability separately from observed shift.

A statistically significant composition shift is a process failure unless deliberately designed and modeled.

---

## 12. Hall measurement gate

A nominal anneal is not accepted without Hall verification.

The Hall SOP must eventually specify:

- Van der Pauw geometry;
- sample thickness used in reduction;
- contact metal/method;
- current magnitude and polarity reversal;
- magnetic field magnitude and reversal;
- temperature stabilization time;
- field/current sequencing;
- offset cancellation;
- single-carrier versus multicarrier interpretation rule;
- uncertainty propagation.

For x≈0.30 material, care is required because partial ionization/compensation can complicate interpretation. If Hall coefficient changes sign or shows strong field dependence, a simple one-carrier reduction must not be forced without justification.

---

## 13. Cooldown is part of the anneal

The final defect population can depend on the path through temperature–Hg chemical-potential space, not solely the soak point.

Therefore record:

- time at end of soak;
- sample cooling rate;
- Hg-source cooling rate;
- whether source/sample remain approximately isothermal;
- temperature at which Hg supply is isolated or depleted;
- time to <100 °C;
- final removal temperature.

A production process must reproduce this path within defined tolerance.

---

## 14. Candidate acceptance logic

A qualification coupon passes only if all required conditions are met:

- n-type final conduction;
- carrier density approaching the RP-01 target rather than merely “low” or “n-type”;
- mobility compatible with the RP-01 target;
- no statistically significant unwanted composition shift;
- no unacceptable thickness change;
- no macroscopic Hg/Te deposits or surface degradation;
- no unacceptable crystal-quality degradation;
- repeatability demonstrated on independent coupons/runs.

The final numerical acceptance bands remain `OPEN/QUAL` until device-performance sensitivity and process capability are quantified.

---

## 15. Failure modes

Log explicitly:

- remains p-type;
- converts to n-type but carrier density too high;
- anomalously low mobility;
- mixed or non-single-carrier Hall behavior;
- composition/cutoff shift;
- interface grading increase;
- Te/Hg precipitate or surface deposits;
- increased dislocation/etch-pit density;
- cracking, delamination, or substrate damage;
- nonuniform electrical conversion;
- large run-to-run dependence on source history;
- cooldown-dependent result;
- measurable Hg-source depletion inconsistent with the assumed chemical potential.

---

## 16. Safety hold point

This process uses Hg-containing semiconductor material, elevated temperatures, and a controlled Hg vapor environment; candidate architectures may also use H2 carrier gas or sealed quartz systems. Execution requires institution-approved toxic-metal, mercury-vapor, furnace, pressure/vacuum, hydrogen, exhaust, spill, monitoring, and hazardous-waste procedures. The scientific setpoints in this file are not an operating authorization.

---

## 17. Release blockers

P04 remains `QUALIFICATION-CANDIDATE` until all of the following are closed:

1. exact selected anneal architecture: in-situ/open-tube vs sealed/closed-tube;
2. Hg source identity and geometry;
3. sample/source temperature calibration;
4. quantitative Hg chemical-potential/pressure control method;
5. full temperature ramp and cooldown;
6. process time that reproducibly gives the RP-01 carrier-density target;
7. final mobility capability;
8. pre/post composition-shift limit;
9. spatial electrical-uniformity metric;
10. repeatability across growth runs;
11. Hall SOP and uncertainty budget;
12. detector-level confirmation that the selected material state reproduces expected responsivity/noise behavior.

---

## 18. Primary references

1. T. C. Harman, “Process for making mercury cadmium telluride,” U.S. Patent 4,642,142 (1987; priority 1982-05-19).
2. C. L. Jones, M. J. T. Quelch, P. Capper, J. J. G. Gosney, “Effects of annealing on the electrical properties of CdxHg1−xTe,” *Journal of Applied Physics* 53, 9080–9092 (1982), DOI `10.1063/1.330419`.
3. K. Nagahama, R. Ohkata, K. Nishitani, T. Murotani, “LPE growth of Hg1−xCdxTe using conventional slider boat and effects of annealing on properties of the epilayers” (1984; full journal metadata still being verified).
4. D. Satish Chandra, H. F. Schaake, M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *Journal of Electronic Materials* 32, 810–815 (2003), DOI `10.1007/s11664-003-0075-5`.
5. E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
