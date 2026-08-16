# P31 — Hg-overpressure anneal apparatus / reservoir / trajectory empirical process window

**Status:** `EMPIRICAL-QUALIFICATION-CANDIDATE` — supplements P04/P04A/P04B/P23; not a released RP-01 anneal recipe.

## 1. Purpose

Convert the Hg-anneal branch from a temperature/time shorthand into a physically reproducible process state:

`{sample, enclosure, Hg source, source/sample geometry, T_s(t), T_Hg(t), p_Hg(t), dwell, cooldown}`

`-> {carrier-state class, Hall tensor state, mobility, optical preservation, morphology, defect state, lifetime/device response}`.

The central rule is:

> `250 °C in Hg` is not a complete anneal specification.

A reproducible anneal requires the actual Hg chemical-potential boundary condition and the complete thermal trajectory.

---

## 2. Evidence classes

- `[P-RP01]` — Smith et al. 2001 reference detector material state.
- `[P-HARMAN]` — Harman US4642142 in-situ Te-rich LPE/anneal lineage.
- `[P-JONES]` — Jones, Quelch, Capper, Gosney, J. Appl. Phys. 53, 9080–9092 (1982), DOI `10.1063/1.330419`.
- `[P-NAG]` — Nagahama, Ohkata, Nishitani, Murotani 1984 LPE/anneal branch.
- `[P-SCHAAKE]` — Schaake/Tregilgas US4481044; Schaake et al. JVST A 3, 143–149 (1985).
- `[P-TREG]` — Tregilgas et al. US5079192 and US5028296.
- `[P-ARCHER]` — Archer/Palfrey mercury self-diffusion work, 1991.
- `[TRANSFER]` — primary process from a different growth/device branch.
- `[D]` — derived or consistency calculation.
- `[CAL]` — apparatus calibration required.
- `[QUAL]` — local qualification required.
- `[OPEN]` — historical/process value unrecovered.

---

## 3. RP-01 target state

Direct material-state reference from RP-01:

- x≈0.30;
- thickness ~9.5 µm;
- n-type;
- electron concentration ~`9.8×10^14 cm^-3`;
- mobility ~`4.0×10^4 cm² V^-1 s^-1`.

These are final-state anchors, not a disclosed historical anneal recipe.

Exact RP-01 anneal apparatus, Hg source, reservoir mass, source/sample temperatures, dwell and cooldown remain `OPEN`.

---

## 4. Empirical architecture families

### 4.1 Closed sealed ampoule — isothermal Hg-saturated branch

Jones et al. explicitly used closed-tube annealing with Hg vapor controlled by a mercury reservoir. In an isothermal anneal the reservoir was held approximately at the HgCdTe temperature. `[P-JONES]`

Observed qualitative result:

- native-defect p-type material can convert to n-type under isothermal Hg-rich conditions.

This is the strongest conceptual match to an RP-01 target that is lightly n-type.

### 4.2 Closed sealed ampoule — two-temperature branch

Jones et al. also used `T_Hg < T_s`. `[P-JONES]`

Observed qualitative result:

- lower Hg chemical potential can produce or control p-type native-acceptor states.

Therefore a two-temperature branch is not interchangeable with an isothermal branch.

### 4.3 In-situ LPE anneal branch

Harman US4642142 describes post-growth in-situ pseudo-isothermal and pseudo-two-zone annealing. A reported pseudo-isothermal example uses approximately:

- sample anneal `250 °C`;
- `1 h`;
- Hg-saturated condition;
- then cooling to room temperature. `[P-HARMAN]`

Use as a direct process-family kinetic anchor, not as the RP-01 recipe.

### 4.4 Two-zone high-temperature/dislocation-control branch

Tregilgas et al. US5079192 uses a long sealed ampoule with:

- HgCdTe sample at one end;
- elemental Hg reservoir remote at the other end;
- two independently controlled furnace zones. `[P-TREG]`

One preferred sequence is:

1. sample near `400 °C`;
2. Hg reservoir `<200 °C` during the first stage to establish lower Hg pressure;
3. approximately `1 h` first-stage anneal;
4. raise Hg reservoir to approximately `390 °C` while sample remains about `400 °C`;
5. approximately `1 h` second stage;
6. then a stoichiometric anneal below `325 °C` for several hours to several days;
7. cool to room temperature. `[P-TREG]`

This branch demonstrates real two-zone hardware and trajectory control. It is not the preferred first RP-01 low-temperature branch because its first objective is dislocation/Te-precipitate control rather than simply reaching `n≈10^15 cm^-3`.

---

## 5. Why reservoir temperature must be logged separately

For an elemental-Hg reservoir in equilibrium with its vapor, `T_Hg` is a pressure-control coordinate.

The sample itself responds to both:

- its own temperature `T_s`, which sets defect/diffusion kinetics and equilibrium boundaries;
- the imposed Hg chemical potential/partial pressure, which depends on the reservoir state and enclosure.

Therefore every run must retain both traces:

`T_s(t)` and `T_Hg(t)`.

A furnace recipe containing only one controller setpoint is scientifically incomplete unless the apparatus is truly isothermal and that equivalence has been calibrated.

---

## 6. Hg source identity and inventory

### 6.1 Permitted empirical source classes

- elemental Hg reservoir;
- HgTe or two-phase Hg-containing source where directly qualified;
- in-situ growth-system Hg source.

Do not interchange source classes under one recipe ID.

### 6.2 Source inventory record

Record:

- source material identity;
- purity;
- supplier/lot;
- starting mass;
- ending mass where safely/measurably feasible;
- reservoir container geometry;
- liquid free-surface area if elemental Hg;
- source-to-sample distance;
- source-zone thermometry location;
- reuse count/history.

The literature located in Round 24 does not disclose a universal elemental-Hg mass required for the RP-01 geometry. Therefore P31 does not assign one.

### 6.3 Saturation condition

A source mass is sufficient only if it maintains the intended vapor boundary condition over the full run. `Enough Hg for saturation` is a functional condition, not a transferable number independent of ampoule free volume, temperature, leakage and condensation surfaces.

---

## 7. Ampoule / enclosure geometry

### 7.1 Minimum closed-tube record

Record for every apparatus revision:

- quartz grade;
- inner diameter;
- total heated length;
- sample-zone length;
- reservoir-zone length;
- sample-to-reservoir axial separation;
- sample holder material and geometry;
- free internal volume;
- sample orientation;
- sample exposed area;
- reservoir container geometry;
- seal method;
- pre-seal evacuation/backfill method;
- leak-check method;
- ampoule reuse status.

No historical RP-01 dimensions have been recovered; all dimensions remain local apparatus coordinates.

### 7.2 Two-zone requirement

For two-temperature work, the furnace shall have separately characterized sample and reservoir zones with known thermal cross-talk.

A nominal `T_s=250 °C`, `T_Hg=230 °C` condition is invalid if the reservoir actually sits at 245 °C because of axial leakage.

Required calibration:

- axial temperature map with empty ampoule;
- axial map with representative loaded ampoule;
- ramp lag in both zones;
- steady-state offset between controller and actual specimen/source positions;
- repeatability after furnace/insulation changes.

---

## 8. Primary low-temperature transfer window

The literature supports a low-temperature native-defect-control regime below ~300 °C.

### 8.1 Harman center

`250 °C / 1 h / Hg-saturated` is a direct primary process-family example. `[P-HARMAN]`

### 8.2 Nagahama near-composition branch

LPE HgCdTe spanning x≈0.17–0.30 was annealed under Hg overpressure from `250–400 °C`. `[P-NAG]`

Observed:

- `250–300 °C`: well-behaved n-type layers without apparent composition change;
- `400 °C`: detectable composition change near the interface.

For first transfer to x≈0.30 RP-01-like material, P31 therefore prioritizes a sub-300 °C branch unless a separate defect-engineering objective justifies higher temperature.

### 8.3 TI low-temperature bulk/process evidence

Texas Instruments process literature uses low-temperature Hg-rich post-anneals around `270 °C`, with time strongly dependent on material thickness and starting defect state; bulk slices may require days. `[P-SCHAAKE/P-TREG]`

This is strong evidence that time cannot be transferred from thick bulk slices to a 9.5-µm LPE layer.

---

## 9. Thickness and kinetics are coupled

Chandra/Schaake/Kinch show that low-temperature Hg annealing rate depends strongly on:

- alloy composition x;
- temperature;
- initial metal-vacancy concentration.

Schaake et al. further report diffusion-front-like behavior at long times, and Archer/Palfrey directly measured Hg diffusion in bulk and LPE material under controlled Hg reservoirs.

Therefore:

`t_required = F(x, T_s, p_Hg, initial defect state, thickness, surface boundary condition)`.

A fixed time such as 1 h, 4 h, 8 h or 16 h is not transferable without measuring the final state.

---

## 10. First local apparatus-qualification sequence

### Stage 0 — cold hardware qualification

Before exposing HgCdTe:

1. calibrate sample-zone thermometry;
2. calibrate reservoir-zone thermometry;
3. map axial gradients;
4. measure cross-zone thermal coupling;
5. qualify ramp/recovery after door/tube disturbances;
6. establish sealed-ampoule handling and leak-testing under institutional EH&S.

### Stage 1 — one-condition repeatability

Use matched x≈0.30 coupons at one literature-anchored screening condition, preferably near:

- `T_s≈250 °C`;
- Hg-saturated/isothermal-like boundary;
- `t≈1 h`.

This is `QUAL`, not a released recipe.

Purpose:

- verify temperature repeatability;
- verify source condition repeatability;
- verify P05/P06 measurement closure;
- establish whether the process moves the starting material into a stable n-like region.

### Stage 2 — time mapping

At fixed apparatus and Hg boundary condition, map time around the first condition.

The P04 screening points 0.5/1/2/4 h remain useful local DOE coordinates, but only `1 h` is directly anchored by Harman. Other levels are qualification choices.

### Stage 3 — sample-temperature mapping

After a useful time region is found, vary `T_s` within the low-temperature feasible region while preserving the Hg boundary condition.

Do not change `T_s`, `T_Hg` and cooldown simultaneously in the first sensitivity fit.

### Stage 4 — Hg chemical-potential mapping

Only after the isothermal-like branch is stable should `T_Hg` be shifted relative to `T_s` to map the carrier-state boundary.

Use P23 state labels rather than reciprocal Hall density through the p/n transition.

---

## 11. Cooldown is a controlled anneal stage

Record the entire path after dwell:

- dwell-end timestamp;
- `T_s(t)`;
- `T_Hg(t)`;
- sample/source temperature difference;
- cooling-rate segments;
- point at which Hg source can no longer maintain intended boundary condition;
- point at which condensation is first possible by the qualified thermodynamic criterion;
- temperature at ampoule removal;
- time to room temperature.

Do not use labels such as `furnace cool`, `slow cool` or `quench` without the trace.

### Condensation warning

Two-zone TI work explicitly keeps the reservoir below the sample during high-temperature stages to avoid Hg depositing on and dissolving the specimen. `[P-TREG]`

P31 therefore requires a defined cooldown/source-temperature relationship; simply shutting both zones off simultaneously is a separate unqualified branch until its trajectory is measured.

---

## 12. Pre-anneal state vector

Every qualification coupon records:

`S0 = {growth run, wafer coordinate, x/edge, thickness, carrier-state class, Hall tensor, R_s, mu where valid, morphology, surface/passivation state, prior thermal history}`.

Matched coupons should be used whenever possible.

Starting p-type versus already n-type material may follow different trajectories; do not pool them as equivalent initial conditions.

---

## 13. Post-anneal measurement vector

Minimum:

1. P05 full Hall/VdP data at declared temperature/field range;
2. signed carrier-state label: `N-LIKE`, `P-LIKE`, or `TRANSITION/MULTICARRIER`;
3. n or p only where the reduction is valid;
4. mobility only where valid;
5. sheet resistance;
6. P06 pre/post edge/composition map;
7. thickness map;
8. DIC/Nomarski surface inspection;
9. Hg/Te deposits or surface alteration;
10. crystal/defect metric on development samples where available;
11. P13 lifetime/device proxy on selected conditions.

RP-01 reference neighborhood:

- `n≈9.8×10^14 cm^-3`;
- `mu≈4.0×10^4 cm²/Vs`.

Do not accept a run merely because it is n-type.

---

## 14. Hall-state interpretation

Near conversion:

`R_H = (p mu_h^2 - n mu_e^2) / {q(p mu_h + n mu_e)^2}`.

The Hall sign boundary is:

`p mu_h^2 = n mu_e^2`.

Therefore the apparent one-carrier density is singular near cancellation.

P31 inherits P23's rule:

- locate the transition using signed Hall/tensor information;
- fit `n_H` and `mu_H` only inside a validated stable n-like region.

---

## 15. Composition-preservation gate

Near-composition LPE evidence shows a warning at 400 °C. `[P-NAG]`

Therefore every development condition receives matched pre/post P06 measurement.

A statistically significant undesired spectral/composition shift excludes the condition even if the Hall target is reached.

For x≈0.30, preserve separately:

- optical edge metric;
- model-derived x;
- measurement temperature;
- measurement repeatability.

Do not convert a detector cutoff directly into growth composition without the appropriate optical model/convention.

---

## 16. Defect / precipitate / dislocation branch

Low-temperature Hg-saturated annealing can annihilate Te precipitates through Hg in-diffusion, but literature also reports dislocation multiplication associated with this transformation for some starting states. `[P-SCHAAKE]`

High-temperature/intermediate anneal branches were developed specifically to reduce this risk.

Therefore during initial local development record, where possible:

- pre/post EPD or equivalent defect metric;
- Te precipitate/inclusion observations;
- morphology changes;
- whether starting P30 material already shows second-phase evidence.

Do not automatically add a 400–600 °C pre-anneal. That is a separate process architecture requiring its own need/benefit demonstration.

---

## 17. Apparatus equivalence rule

Changing any of the following creates a new anneal-apparatus revision requiring equivalence data:

- ampoule ID/diameter/length;
- sample holder;
- sample/reservoir spacing;
- reservoir vessel/free area;
- furnace insulation or zone length;
- thermocouple type/position;
- source identity;
- sealed versus open configuration;
- sample surface/passivation boundary condition.

Same controller setpoints do not prove same `p_Hg(t)` or sample trajectory after a geometry change.

---

## 18. Release vector

Define:

`Y_A = {state class, n_H, mu_H, R_s, optical shift, thickness shift, morphology, defect metric, tau_eff, detector response}`.

A candidate process can become `LOCAL-QUALIFIED` only after:

- stable n-like operation with margin from transition;
- carrier density and mobility in the detector-relevant neighborhood;
- optical/thickness preservation;
- cooldown reproducibility;
- repeatability across independent ampoule/anneal runs;
- repeatability across more than one P30 growth run;
- P11/P12/P13 detector confirmation.

---

## 19. Current strongest first-transfer branch

For practical local qualification, the strongest evidence-supported first branch is:

- sealed or otherwise quantitatively Hg-controlled enclosure;
- independent sample/source thermometry;
- x≈0.30 matched LPE coupons;
- sample near `250 °C`;
- Hg-saturated/isothermal-like condition;
- `~1 h` as the first literature-anchored time point;
- complete controlled cooldown under retained Hg boundary condition;
- P05/P06 closure.

Every phrase above is a qualification center, not a production recipe.

No Hg mass, ampoule dimensions, ramp rate, cooldown rate, or final carrier tolerance is assigned without local data.

---

## 20. Release blockers

1. exact RP-01 historical anneal architecture;
2. exact historical Hg source identity/mass;
3. ampoule/furnace geometry;
4. sample/source distance;
5. direct pHg reconstruction relation for the chosen local source;
6. sample and source thermometry uncertainty;
7. ramp/dwell/cooldown trajectory;
8. local x≈0.30 time constant/state boundary;
9. repeatability across independent runs;
10. optical/interface preservation;
11. defect/dislocation response;
12. final detector bridge.

---

## 21. Primary sources

1. C. L. Jones, M. J. T. Quelch, P. Capper, J. J. G. Gosney, “Effects of annealing on the electrical properties of CdxHg1−xTe,” *J. Appl. Phys.* 53, 9080–9092 (1982), DOI `10.1063/1.330419`.
2. T. C. Harman, US4642142, “Process for making mercury cadmium telluride.”
3. K. Nagahama, R. Ohkata, K. Nishitani, T. Murotani, “LPE growth of Hg1−xCdxTe using conventional slider boat and effects of annealing on properties of the epilayers” (1984).
4. H. F. Schaake, J. H. Tregilgas, US4481044, “High-temperature Hg anneal for HgCdTe.”
5. H. F. Schaake, J. H. Tregilgas, J. D. Beck, M. A. Kinch, B. E. Gnade, “The effect of low temperature annealing on defects, impurities, and electrical properties of (Hg,Cd)Te,” *J. Vac. Sci. Technol. A* 3, 143–149 (1985), DOI `10.1116/1.573186`.
6. J. H. Tregilgas et al., US5079192, “Method of preventing dislocation multiplication of bulk HgCdTe and LPE films during low temperature anneal in Hg vapor.”
7. J. H. Tregilgas, US5028296, “Annealing method.”
8. D. Satish Chandra, H. F. Schaake, M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *J. Electron. Mater.* 32, 810–815 (2003), DOI `10.1007/s11664-003-0075-5`.
