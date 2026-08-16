# P03E — Te-rich LPE liquidus, equilibration and thermal-metrology qualification

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. Supplements P03/P03A/P03B/P03C/P03D.

## 1. Purpose

Replace the vague instruction “equilibrate the x≈0.30 Te-rich source, then grow near 500 °C” with a measurable apparatus-specific criterion based on:

- actual source liquidus;
- temperature-sensor calibration;
- spatial thermal field;
- hold-time convergence;
- source homogenization state;
- resulting solid composition/thickness sensitivity.

The historical composition-matched anchor remains:

`xL=.082, yL=.810, TL=507 °C -> historical xS≈.29`.

The historical Honeywell patent does not state an exact equilibration duration for this row.

## 2. Historical/direct Honeywell thermal statements

Bowers–Schmit US4317689A directly states that:

- the covered graphite boat is heated near `500 °C`;
- growth begins after equilibration;
- the source must initially be raised above its liquidus temperature;
- growth then occurs below liquidus;
- step supercooling, slow cooling from liquidus, or a combination may be used;
- for the xL=.082/yL=.810 source, the tabulated liquidus is `507 °C`.

What remains historically open:

- exact temperature above liquidus used for equilibration;
- exact hold duration;
- allowed sensor offset/gradient;
- exact cooling ramp/supercooling trajectory for the xS=.29 case.

## 3. Why nominal charge temperature is insufficient

A primary HgCdTe LPE metrology patent, US4474640 (“In situ differential thermal analysis for HgCdTe LPE”), was developed specifically because the **actual melt composition can differ from the original charge** due to Hg transport/distillation and other process effects.

The method measures the actual HgCdTe melt temperature while differentially sensing latent-heat transformations against a neutral reference body.

Key principle:

> Identify the liquidus of the actual melt rather than assuming the nominal phase-diagram value is exactly realized in the apparatus.

The patent's numerical melt example is not the RP-01/Honeywell x=.29 composition and its dipping process is a different apparatus branch. Use the measurement principle, not its recipe.

## 4. Heating liquidus versus cooling transition

The DTA patent shows large hysteresis/supercooling can occur on cooling.

Accordingly:

- use the **heating transformation/liquidus** as the preferred equilibrium liquidus measurement;
- do not define `TL` from an arbitrary cooling exotherm unless the supercooling behavior has been calibrated;
- record heating and cooling traces separately.

The local process shall distinguish:

- `TL,heat` — liquidus identified during heating;
- `Tnuc,cool` — observed cooling/nucleation transformation;
- `ΔT_hyst = TL,heat - Tnuc,cool`.

Do not treat `ΔT_hyst` as intended growth supercooling.

## 5. Candidate liquidus-measurement routes

At least one of the following shall be qualified.

### Route A — in-situ differential thermal measurement

Use differential thermometry/DTA on the actual or representative source charge with:

- temperature sensor coupled to source/reactor;
- neutral/reference body;
- controlled heating/cooling rate;
- recorded differential signal versus source temperature.

### Route B — sacrificial matched-charge DTA

If the production slider cannot accommodate DTA, synthesize a matched source aliquot from the same source lot and measure liquidus in a calibrated sacrificial vessel.

Transfer uncertainty must include:

- vessel geometry difference;
- Hg chemical-potential difference;
- atmosphere difference;
- sensor placement.

### Route C — growth-response inference

If DTA is unavailable, determine an operational liquidus neighborhood from a controlled series of growth/no-growth or meltback/growth transitions combined with P06 composition data.

This is weaker evidence and requires more qualification runs.

## 6. Temperature sensor calibration

Before source/process qualification record:

- sensor type/alloy;
- wire diameter;
- junction construction;
- readout instrument;
- reference-junction compensation;
- calibration date/method;
- calibration points spanning the LPE range;
- fit/correction function;
- expanded/standard uncertainty.

A controller display alone is not a traceable growth temperature.

## 7. Growth-zone spatial thermal map

Map the temperature field over at least the volume spanning:

- full source well;
- substrate recess/contact region;
- Hg-source region where relevant.

Measure or validate:

- axial gradient;
- transverse gradient;
- source-to-substrate temperature difference;
- steady-state drift;
- transient lag during ramps.

The mapping method can use calibrated dummy assemblies/sensors where direct multi-sensor production operation is impractical.

Record the exact boat revision and furnace position because geometry changes can invalidate the map.

## 8. Sensor-to-melt offset

Define:

`ΔT_sensor-melt = T_melt - T_sensor`.

Estimate this offset and uncertainty under representative:

- source mass/inventory;
- boat geometry;
- gas flow;
- furnace ramp/hold state.

Do not assume the nearby thermocouple equals liquid temperature during ramps.

## 9. Independent equilibration benchmark

Harman 1980, DOI `10.1007/BF02822728`, reports a **typical growth-solution equilibration time of approximately 1 h at 550 °C** in a different Te-rich horizontal-slider process.

This is evidence that equilibration can require an order-hour hold in Te-rich HgCdTe LPE.

It is **not** the historical xL=.082/yL=.810 Honeywell hold condition.

Use it only to size an initial local hold-time experiment.

## 10. Hold-time convergence experiment

For a new source-preparation/boat configuration, establish equilibration by convergence rather than by copying one published hold time.

At fixed:

- source lot/composition;
- melt inventory;
- Hg-source configuration;
- above-liquidus temperature;
- gas flow;
- boat/furnace position;

compare multiple hold durations spanning below and above the expected equilibration time.

A practical initial design may include at least three hold durations with the longest approximately twice the shortest, centered in the order-hour regime suggested by Te-rich LPE literature. Exact values are `QUAL`, not historical setpoints.

For each hold condition perform the same P03B growth and measure:

- source thermal signature/liquidus where possible;
- layer mean x;
- x uniformity;
- thickness/growth rate;
- morphology;
- post-anneal mobility.

## 11. Equilibration acceptance criterion

A source is operationally equilibrated when increasing hold duration no longer produces a statistically meaningful systematic change in the relevant output vector:

`Y_eq = {TL, mean x, x uniformity, thickness/growth rate, morphology, post-anneal mobility}`.

The exact numerical equivalence margin must be based on:

- measurement uncertainty;
- allowed RP-01 material-state window;
- run-to-run process capability.

Do not define equilibrium only as “temperature stopped changing.”

## 12. Source homogenization interaction

P03C source synthesis/homogenization and P03E in-boat equilibration are separate stages.

A pre-synthesized charge can still require in-boat homogenization/equilibration after:

- remelting;
- Hg exchange with the auxiliary source;
- partial source reuse/depletion;
- temperature gradients.

Record source-use index and prior thermal history for every P03E dataset.

## 13. Actual liquidus versus nominal 507 °C

For the historical composition, `507 °C` is the strongest published tie-line value.

Locally, define:

`δTL = TL,measured - 507 °C`.

A nonzero `δTL` is diagnostic, not automatically a reason to force the controller to 507 °C.

Investigate:

- weighing/composition error;
- Hg loss or chemical-potential mismatch;
- source contamination;
- incomplete homogenization;
- sensor/calibration offset;
- phase-diagram/model difference.

Use P06 grown-layer composition to discriminate causes.

## 14. Growth-supercooling definition

After a local liquidus is established, define process supercooling from the **measured local liquidus**:

`ΔT_SC = TL,measured - T_contact/start`.

Do not automatically use `507 °C - controller setpoint` if the actual source liquidus or sensor offset differs.

P03B shall store both nominal and corrected/local `ΔT_SC`.

## 15. Temperature sensitivity experiment

At a fixed source lot/inventory and growth-time condition, perturb the local growth/contact temperature over a small bounded range around the candidate center.

Measure:

- `∂x/∂T` locally;
- `∂d/∂T` locally;
- morphology sensitivity;
- wipe-off sensitivity.

Do not infer a universal derivative from the five Honeywell tie-line rows because each row has a different liquid composition as well as liquidus temperature.

## 16. Derive the required temperature uncertainty from the material budget

Let the allowed contribution of temperature uncertainty to solid-composition error be `u_x,T`.

For a locally measured sensitivity `S_xT = |∂x/∂T|`, require approximately:

`u_T <= u_x,T / S_xT`

within the locally linear region.

Similarly, for thickness:

`u_T <= u_d,T / |∂d/∂T|`.

Choose the tighter requirement and include:

- calibration uncertainty;
- spatial gradient;
- sensor-to-melt offset uncertainty;
- temporal controller variation.

This replaces arbitrary goals such as “hold ±0.01 °C” unless the sensitivity analysis actually demands them.

## 17. Thermal uncertainty budget

At minimum combine contributions from:

- sensor calibration;
- readout resolution/noise;
- reference-junction compensation;
- source-to-sensor offset;
- axial/transverse gradient;
- temporal drift;
- ramp lag;
- run-to-run furnace placement.

Report a combined standard uncertainty and, where needed, expanded uncertainty.

## 18. Cooling/ramp qualification

The historical Honeywell process permits:

- step supercooling;
- slow cooling after contact;
- combination.

P03B must therefore record the complete `T(t)` trace, not only start/end setpoints.

For a released trajectory record:

- rate above liquidus;
- hold temperature/time;
- approach rate to liquidus;
- intended supercooling at contact;
- post-contact cooling rate;
- separation/wipe-off temperature.

## 19. Nucleation/excess-supercooling guard

Primary DTA/LPE literature warns that excessive supercooling can produce heterogeneous nucleation and loss of composition control.

Local qualification must therefore inspect for:

- particles/secondary nucleation;
- rough/non-epitaxial deposits;
- abrupt morphology changes;
- unexpected depletion;
- abnormal thermal transformations.

Do not improve growth rate by increasing supercooling without requalifying morphology/x/depletion.

## 20. Production equilibration release

The final traveler may use a fixed hold time only after demonstrating that it sits safely beyond the local convergence time with adequate margin for:

- source-lot variation;
- source reuse;
- charge mass variation;
- furnace loading variation.

The traveler shall specify both:

- minimum qualified equilibration time; and
- measured/allowed thermal state before growth.

A timer alone is not the release gate.

## 21. Historical closure status

Historical x≈0.30 Honeywell:

- tie-line liquidus 507 °C: `CLOSED-P`;
- heating above liquidus then growth below: `CLOSED-P`;
- exact equilibration duration/overtemperature/ramp: `OPEN`.

P03E is the controlled local path to close these variables without inventing historical precision.