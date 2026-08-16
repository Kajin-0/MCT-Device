# 2026-08-15 — LPE wipe-off and Hg-anneal closure

## Scope

This research pass targeted two open interfaces in RP-01 upstream material preparation:

1. how to remove residual Te-rich growth solution reproducibly after horizontal-slider LPE;
2. how to convert as-grown Te-rich material to the low-density n-type state required by RP-01.

---

# A. Growth-solution wipe-off

## A1. Correct primary patent

The high-value Honeywell wipe-off source is:

**U.S. Patent 4,592,304**, “Apparatus for liquid phase epitaxy of mercury cadmium telluride.”

A previously noted identifier `US4706604` was incorrect for this purpose.

## A2. Mechanical architecture

The patent adds a dedicated wipe-off well adjacent to the growth-solution well in the movable graphite slider.

The wipe-off well contains loose, unpolished polycrystalline CdTe pieces held in vertical slots approximately **1 mm apart**.

The pieces are a sliding fit and rest naturally against the upper surface of the graphite base. After LPE growth, slider translation carries them across the epilayer.

Residual growth solution is removed by three mechanisms explicitly identified by the source:

1. mechanical wiping;
2. surface-tension adhesion between CdTe and the Te-rich growth liquid;
3. capillary wicking into the gap between adjacent CdTe pieces.

The wipe-off well is maintained under the same Hg-rich environment supplied by the HgTe reservoir. The CdTe wipe pieces are discarded after cooldown.

## A3. Why this matters

Residual Te-rich droplets are not cosmetic. Related LPE literature reports that frozen residual solution reduces usable area and produces strain and detector-quality degradation.

The patent therefore converts “wipe off the melt” from an operator-dependent act into a dedicated mechanical process module.

## A4. Variables still open

The patent does not close:

- slider translation velocity;
- contact force of the loose CdTe pieces;
- exact CdTe piece thickness/height/width;
- number of pieces beyond the illustrated arrangement;
- acceptable wear/reuse criterion for the graphite slots;
- allowed scratch density;
- optimum temperature at wipe crossing;
- residual-droplet acceptance threshold.

These remain apparatus qualification variables.

## A5. Proposed metrology

For each wipe-off qualification run record:

- slider translation speed;
- sample temperature at growth termination;
- number and spacing of CdTe wipers;
- wiper material lot and dimensions;
- whole-wafer bright-field image before any cleaning;
- residual droplet count;
- total residual-droplet area fraction;
- maximum residual-droplet diameter;
- scratch count/length;
- Nomarski surface map;
- post-process usable-area fraction.

A production slider speed should be selected by minimizing residual melt while avoiding mechanical damage; it should not be guessed from an unrelated actuator.

---

# B. Hg-overpressure anneal

## B1. Strongest exact process anchor found

T. C. Harman, U.S. Patent 4,642,142, “Process for making mercury cadmium telluride,” provides a fully explicit pressure-controlled LPE/anneal framework.

The patent treats sample temperature and Hg chemical potential/partial pressure as coupled thermodynamic process variables.

Key primary anchors:

- HgCdTe annealing generally in the **200–300 °C** range;
- Hg partial pressure broadly **0.1–250 Torr**, selected according to desired stoichiometric defect state;
- pseudo-isothermal Hg-saturated example at **250 °C for 1 h**, then cool to room temperature;
- in the specific process, post-anneal carrier concentrations were typically in the **low 10^16 cm^-3** range.

## B2. Critical inference for RP-01

The 250 °C/1 h condition is scientifically valuable because it is an exact primary-source kinetic anchor, but it **does not meet RP-01 electrically by itself**.

RP-01 starting material requires approximately:

- n=9.8×10^14 cm^-3;
- µe=4.0×10^4 cm²/V·s.

Therefore the manual must never say “anneal at 250 °C for 1 h and the material is done.” Instead, 250 °C/1 h becomes the center point of a transfer experiment whose output is verified by Hall measurements.

## B3. Additional exact LPE-process information from Harman patent

The same patent reports:

- growth solution / Hg-source temperatures must be held within <1 °C, preferably <0.2 °C, in composition-sensitive operation;
- growth-solution temperature range about 425–550 °C, preferably 425–500 °C;
- source-wafer equilibration approximately 0.5–2 h, with ~60 min typical;
- charge heated about 3 °C above liquidus in the described saturation sequence;
- growth initiated at supercooling typically **2–10 °C**;
- substrate contact time broadly **10 s–30 min**, preferably **1–20 min**;
- growth thickness is time dependent.

These values belong to Harman's pressure-controlled process and must not be silently substituted into the Bowers–Schmit xL=0.082/yL=0.810 Honeywell composition branch. They are useful independent bounds and qualification anchors.

## B4. Composition dependence of anneal kinetics

Chandra, Schaake, and Kinch (JEM 2003, DOI `10.1007/s11664-003-0075-5`) show that low-temperature annealing kinetics depend on alloy composition, vacancy concentration, and temperature, with annealing slowing as x increases over the studied range.

This is a direct reason not to use an x≈0.20 anneal time as the fixed process time for x≈0.30 RP-01 material.

## B5. High-temperature warning

Nagahama et al. report that Hg-overpressure treatment at 250–300 °C can convert x≤0.30 LPE material to well-behaved n-type without apparent composition change, while 400 °C produces a measurable composition change near the interface.

For RP-01, the initial native-defect-control qualification window should therefore stay below 300 °C unless a separate high-temperature objective is deliberately introduced.

## B6. Anneal process control principle

The controlled output must be the tuple

`(carrier sign, n, mobility, x/cutoff, thickness, morphology, defect state)`

not just `temperature × time`.

Any released production anneal must include:

- sample-temperature trace;
- Hg-source/pressure trace or reconstructable proxy;
- ramp and cooldown;
- pre/post Hall;
- pre/post spectral/composition map;
- pre/post morphology;
- repeatability across multiple LPE runs.

## B7. New controlled module

Created:

`procedures/P04_HG_ANNEAL_QUALIFICATION.md`

It uses 250 °C/1 h as a primary-source screening anchor but explicitly requires a time/temperature/Hg-chemical-potential DOE to approach the RP-01 final carrier state.

---

# C. Immediate next questions

1. Can the full Schmit–Hager–Wood 1982 x≈0.30 LPE experimental section be recovered to reconcile its exact growth time/thermal profile with the Bowers–Schmit tie line?
2. Can full Nagahama 1984 bibliographic/method data be recovered, especially anneal duration and Hg-source arrangement?
3. Can a primary x≈0.30 anneal data set be found whose final electron density lies near 10^15 cm^-3 rather than 10^16 cm^-3?
4. Can slider translation speed or dimensional details be recovered from a related Honeywell wipe-off patent/paper?
5. What Hall measurement protocol was used by RP-01/Fermionics for the reported n and mobility, and at what measurement temperature?

---

# D. Primary sources

1. U.S. Patent 4,592,304, “Apparatus for liquid phase epitaxy of mercury cadmium telluride.”
2. T. C. Harman, U.S. Patent 4,642,142, “Process for making mercury cadmium telluride.”
3. C. L. Jones, M. J. T. Quelch, P. Capper, J. J. G. Gosney, “Effects of annealing on the electrical properties of CdxHg1−xTe,” *J. Appl. Phys.* 53, 9080–9092 (1982), DOI `10.1063/1.330419`.
4. D. Satish Chandra, H. F. Schaake, M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *J. Electron. Mater.* 32, 810–815 (2003), DOI `10.1007/s11664-003-0075-5`.
5. K. Nagahama, R. Ohkata, K. Nishitani, T. Murotani, “LPE growth of Hg1−xCdxTe using conventional slider boat and effects of annealing on properties of the epilayers” (1984; full bibliographic metadata still unresolved).
