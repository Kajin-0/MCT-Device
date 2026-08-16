# 2026-08-15 — RP-01 upstream LPE process reconciliation

## Objective

Identify a primary-source Te-rich LPE process that can plausibly generate the RP-01 starting material:

- n-type Hg1−xCdxTe;
- x≈0.30;
- approximately 9.5 µm active-layer thickness;
- electrically insulating CdZnTe substrate;
- electron concentration approximately 9.8×10^14 cm^-3;
- electron mobility approximately 4.0×10^4 cm² V^-1 s^-1.

The main research constraint is to avoid constructing a process by silently combining individually valid but mutually incompatible recipes.

---

## 1. Correction to the source ledger

The Journal of Crystal Growth paper with DOI `10.1016/0022-0248(82)90468-7` is:

J. L. Schmit, R. J. Hager, and R. A. Wood, “Liquid phase epitaxy of Hg1−xCdxTe,” *Journal of Crystal Growth* 56, 485–489 (1982).

It was previously mislabeled in the project ledger as “Tung et al. 1982.” That attribution is incorrect and must be corrected.

The paper reports atmospheric-pressure horizontal-slider growth from Te-rich liquid and explicitly includes solids with x=0.2, 0.3, and 0.4.

---

## 2. High-value primary process source: Bowers–Schmit Hg containment patent

**Source:** J. E. Bowers and J. L. Schmit, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution,” U.S. Patent 4,317,689 (1982), priority 1980-07-18.

This source is especially valuable because it belongs to the same Honeywell/Schmit Te-rich horizontal-slider lineage as the 1982 x=0.2/0.3/0.4 paper and gives explicit liquid/solid tie-line parameters.

### 2.1 Apparatus architecture

The source describes:

- open-tube LPE at atmospheric pressure;
- a graphite slider/carrier, graphite base/stator, and graphite cover;
- one or more through-wells for growth solution;
- a substrate recess in the base;
- a plug over the growth-solution well;
- a shallow well containing an Hg source, nominally HgTe or HgTe+Te;
- Hg-vapor-distribution grooves/moats surrounding the growth wells and lower slider surface;
- a quartz furnace tube;
- nitrogen purge before heating;
- flowing H2 during equilibration/growth.

The purpose of the secondary HgTe source is to establish an Hg vapor pressure approximately equal to that over the Te-rich growth solution, thereby suppressing Hg loss from both growth solution and grown material.

At approximately 500 °C the source reports an Hg partial pressure near 0.1 atm for the relevant Te-rich solutions.

### 2.2 Thermal sequence stated by the source

The source explicitly requires:

1. the growth solution to be heated above its liquidus temperature;
2. growth to occur below the liquidus temperature;
3. growth to be initiated by translating the slider so the molten charge contacts the substrate.

It permits either:

- step supercooling before substrate contact;
- contact near liquidus followed by slow cooling below liquidus;
- a combination of both.

The described example operates near 500 °C and notes that growth may continue for approximately 0.5 h; that 0.5-h value is an apparatus/process example and must **not** be interpreted as the production time for a 9.5 µm RP-01 layer.

---

## 3. Exact tie-line nearest RP-01 composition

The patent tabulates five source-solution/solid pairs. The one closest to RP-01 is:

- source-solution metal Cd fraction: `x_L = 0.082`;
- source-solution Te fraction: `y_L = 0.810`;
- source liquidus temperature: `T_L = 507 °C`;
- grown-solid Cd fraction: `x_S = 0.29`;
- ratio `k = x_S/x_L = 3.54`.

This is currently the strongest explicit composition anchor for the RP-01 upstream process.

### 3.1 Composition interpretation

The liquid is written

`(Hg_(1−x_L) Cd_(x_L))_(1−y_L) Te_(y_L)`.

For `x_L=0.082`, `y_L=0.810`:

- elemental mole fraction Hg = `(1−0.082)(1−0.810) = 0.17442`;
- elemental mole fraction Cd = `0.082(1−0.810) = 0.01558`;
- elemental mole fraction Te = `0.81000`.

These sum to 1.00000.

Using atomic weights Hg=200.59, Cd=112.414, Te=127.60 g/mol, the corresponding **derived mass fractions** are approximately:

- Hg: 0.249738;
- Cd: 0.012502;
- Te: 0.737760.

These mass fractions are a `[D]` conversion of the published molar formulation, not independently published charge masses.

### 3.2 Critical restriction on charge mass

Do **not** combine the Radhakrishnan 4.8-g charge mass with the Honeywell x_L=0.082, y_L=0.810 formulation and call it a published recipe.

Radhakrishnan's 4.8-g charge belongs to a different modified-slider apparatus and typical melt chemistry. Charge mass controls melt depth, thermal mass, solute inventory, depletion, and hydrodynamics. The RP-01 candidate charge mass must therefore be determined from the selected boat/well geometry and qualified experimentally.

---

## 4. CdZnTe substrate compatibility

RP-01 explicitly used electrically insulating CdZnTe under the LPE HgCdTe.

Tranchart, Latorre, Foucher, and Le Gouge, *J. Crystal Growth* 72, 468–473 (1985), report Cd1−yZnyTe with y≈0.04 as a substrate developed to closely match x≈0.30 HgCdTe and report improved-quality Te-rich LPE HgCdTe layers used in 3–5 µm detector arrays.

This strongly supports CdZnTe as the substrate family for the RP-01-compatible x≈0.30 branch.

### Important lattice-match nuance

A separate 1985/1986 primary lattice-matching study reports an optimum ZnTe fraction of about 2.9% for Hg0.7Cd0.3Te. Therefore, “4% Zn is exactly lattice matched to x=0.30” must not be treated as a universal exact number without specifying temperature, lattice-parameter calibration, composition convention, and source.

For the controlled manual:

- `CdZnTe` substrate family is closed by RP-01;
- a nominal Zn fraction around a few percent is strongly supported;
- the **exact released Zn fraction must be defined from measured lattice mismatch**, not copied as an unqualified universal constant.

---

## 5. Radhakrishnan modified-slider source: apparatus module, not composition module

Radhakrishnan, Sitharaman, and Gupta (2003), DOI `10.1016/S0022-0248(02)02530-7`, gives unusually useful apparatus and charge-handling detail:

- high-purity/high-density graphite slider boat;
- base + moving plate + solution-bin block + tightly fitting graphite cover;
- recess for a 15 mm × 15 mm × 1 mm CdZnTe substrate;
- horizontal quartz tube with stainless-steel end flanges;
- ports for gas flow, push-pull rod, and thermocouple;
- 6N elemental Cd, Te, Hg;
- 10-g synthesized batches;
- synthesis in evacuated quartz ampoules at 700 °C for 8 h;
- synthesized material ground and thoroughly mixed;
- ~4.8 g loaded per growth run;
- 3 g HgTe used for Hg-loss compensation;
- in-situ substrate meltback;
- modified geometry designed for clean solution wipe-off.

Its typical melt is `(Hg_(1−z)Cd_z)_(1−y)Te_y` with `z≈0.049`, `y≈0.84`, and the associated Radhakrishnan material branch is around x≈0.20. Therefore it is not the composition source for RP-01 x≈0.30.

**Use:** apparatus architecture, Hg-loss-control concepts, meltback concept, surface-morphology failure modes, and candidate synthesis methodology.

**Do not use without qualification:** 4.8-g charge, 3-g HgTe mass, or exact melt formulation as direct RP-01 x≈0.30 values.

---

## 6. Broad process-window constraints from Harman

T. C. Harman, *J. Electron. Mater.* (1980), DOI `10.1007/BF02822728`, reports:

- Te-rich liquidus isotherms from 425–600 °C;
- horizontal-slider growth under flowing H2;
- solid x spanning about 0.1–0.8;
- growth temperatures approximately 450–550 °C;
- growth times approximately 0.25–10 min;
- typical equilibration about 1 h at 550 °C;
- highest-quality layers using source wafers, supercooled solutions, and (111)-oriented substrates;
- layer thicknesses about 3–15 µm.

These are useful physical/process bounds, but they do not define the exact RP-01 recipe.

---

## 7. Electrical-state problem: as-grown Te-rich material is commonly p-type

A recurring result in the Te-rich LPE literature is that as-grown material is often Hg-vacancy p-type.

Nagahama, Ohkata, Nishitani, and Murotani (1984) report:

- x spanning 0.17–0.30;
- CdTe (111)A substrates;
- conventional slider boat;
- open-tube H2-flow system;
- as-grown p-type material;
- Hg-overpressure annealing studied from 250–400 °C;
- 400 °C caused detectable compositional change near the interface;
- 250–300 °C converted material to well-behaved n-type without apparent compositional change.

This is directly relevant to RP-01 because RP-01 requires low-density n-type material.

However, the abstract-level evidence does **not** yet close:

- anneal time;
- Hg source/reservoir geometry;
- cool-down rate;
- resulting n for x≈0.30;
- resulting mobility;
- reproducibility near the specific RP-01 target 9.8×10^14 cm^-3.

Therefore the post-growth anneal remains a separate qualification module, not a guessed fixed recipe.

---

## 8. Candidate process architecture now supported

The most defensible RP-01-compatible upstream architecture is currently:

1. qualified semi-insulating CdZnTe substrate with lattice mismatch measured against target x≈0.30 HgCdTe;
2. Te-rich horizontal-slider LPE;
3. covered graphite boat with an independent HgTe/HgTe+Te vapor source to suppress Hg depletion;
4. target source-solution composition initially centered on the Bowers–Schmit tie line `x_L=0.082`, `y_L=0.810`;
5. source liquidus reference `T_L≈507 °C`;
6. controlled supercooling/growth below liquidus near 500 °C;
7. growth terminated by slider translation/wipe-off;
8. thickness/composition immediately mapped;
9. Hg-overpressure post-growth anneal qualified in the low-temperature regime to reach the target n-type electrical state without shifting x;
10. Hall, FTIR, thickness, morphology, and crystal-quality gates before device fabrication.

Items 1–10 define a coherent **process architecture**, not yet a production traveler.

---

## 9. What is now closed vs open

### Strongly closed / primary-source anchored

- Te-rich horizontal-slider process can grow x≈0.30 HgCdTe.
- Explicit x≈0.29 tie line: x_L=0.082, y_L=0.810, T_L=507 °C.
- Source-limited Hg loss is a critical variable.
- HgTe/HgTe+Te auxiliary source in a covered slider is a demonstrated control strategy.
- Growth must proceed below the liquidus after heating above it.
- CdZnTe is a demonstrated compatible substrate family for x≈0.30 HgCdTe.
- Low-temperature Hg-overpressure annealing is a demonstrated path for converting as-grown Te-rich LPE material toward n-type electrical behavior.

### Still open / qualification required

- exact CZT Zn fraction and orientation for RP-01;
- substrate cleaning/polishing sequence;
- target boat well dimensions and charge mass;
- synthesis procedure for the x_L=0.082, y_L=0.810 source charge;
- exact equilibration temperature/time for that charge in the selected boat;
- exact supercooling ΔT;
- cooling rate;
- growth/contact time required for 9.5 µm;
- slider translation speed and wipe-off mechanics;
- thickness uniformity capability;
- target composition uniformity capability;
- Hg anneal time/geometry/cooldown required for n≈9.8×10^14 cm^-3;
- final mobility/lifetime acceptance windows.

---

## 10. Next highest-value source targets

1. Obtain full experimental details of Schmit–Hager–Wood 1982 and Wood–Hager 1983 horizontal-slider papers.
2. Recover full Tranchart et al. 1985 CdZnTe/x≈0.30 LPE experimental section.
3. Recover Nagahama et al. 1984 annealing time/pressure/cooling details.
4. Audit the Honeywell wipe-off apparatus patent (US4706604) for slider velocity/geometry and melt-removal control.
5. Build a controlled LPE qualification module using only the quantities that are now actually closed.
