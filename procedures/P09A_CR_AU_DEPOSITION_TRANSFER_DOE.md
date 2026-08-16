# P09A — Cr/Au deposition and RIE-to-metal transfer qualification DOE

**Status:** CONTROLLED LOCAL TRANSFER METHOD. Historical RP-01 deposition pressure/rates/tool remain `OPEN`; this procedure defines how to establish a reproducible local Cr/Au process without inventing those missing historical numbers.

## 1. Purpose

Qualify the deposition portion of the RP-01 contact stack while preserving the directly published layer thicknesses:

- Cr `30 nm`;
- Au `270 nm`.

The local process must demonstrate that vacuum history, deposition kinetics and time after P08 RIE do not degrade:

- adhesion;
- contact geometry;
- TLM contact resistivity;
- I–V linearity;
- cryogenic stability;
- detector low-frequency noise.

## 2. Historical closure status

Direct RP-01 closes:

- RIE-modified n+ contact region;
- Cr/Au material stack;
- Cr thickness 30 nm;
- Au thickness 270 nm;
- 80-K specific contact resistivity approximately `9×10^-4 Ω·cm²` after the complete contact process.

Still not recovered:

- deposition method/tool;
- base pressure;
- pressure during Cr and Au deposition;
- Cr rate;
- Au rate;
- source-to-sample geometry;
- substrate temperature;
- whether vacuum was broken between Cr and Au;
- actual time between RIE and metal deposition;
- exact lift-off conditions.

Later UWA HgCdTe work demonstrates thermal evaporation of Cr/Au as a workable HgCdTe contact method, but that is a different detector/process branch. Thermal evaporation is therefore a **candidate local deposition method**, not historical proof for RP-01.

## 3. Core transfer principle

Do not optimize deposition by film appearance alone.

The controlled response vector is:

`Y = {rho_c(80 K), TLM fit quality, I-V symmetry/linearity, adhesion, metal CD, roughness, cryogenic drift, 1/f-noise impact}`.

A process is acceptable only if the contact electrical state and detector performance are stable.

## 4. Keep the historical stack fixed during first transfer

During the first transfer DOE, hold nominal final thicknesses fixed at:

- Cr `30 nm`;
- Au `270 nm`.

Do not vary adhesion-metal thickness, cap-metal thickness and vacuum variables simultaneously. If the historical stack cannot meet performance after deposition-variable optimization, any thickness change becomes a separate process branch.

## 5. Qualification hardware requirements

The local deposition system must provide/log:

- deposition method and tool ID;
- chamber base pressure versus time;
- pressure during each metal layer;
- source material lot/purity;
- source/crucible/boat identity and conditioning state;
- source-to-sample distance and orientation;
- sample fixture/carrier;
- substrate-temperature proxy or direct measurement;
- thickness/rate monitor (preferably QCM) with calibration history;
- shutter timing;
- Cr and Au rate versus time;
- final indicated thickness;
- witness coupon position;
- chamber cleaning/previous-process history.

## 6. Thickness-monitor calibration

Before contact DOE:

1. deposit Cr-only witness films at the intended geometry;
2. compare QCM indicated thickness with an independent thickness method;
3. establish tooling factor / calibration correction;
4. repeat for Au;
5. verify calibration at thicknesses bracketing the RP-01 targets.

Suitable independent methods include:

- stylus step profilometry;
- calibrated ellipsometry where optical constants permit;
- X-ray reflectometry;
- cross-sectional microscopy for periodic validation.

Record calibration uncertainty separately for Cr and Au.

## 7. RIE-to-metal exposure clock

P08 creates a chemically/electrically modified HgCdTe contact surface. Atmospheric exposure and reoxidation/adsorption can change the interface before metal deposition.

Define timestamps:

- `t_RF_off`;
- `t_RIE_vent`;
- `t_sample_out`;
- `t_metal_load`;
- `t_pump_start`;
- `t_base_accept`;
- `t_Cr_start`.

Define the principal delay:

`Δt_RIE-metal = t_Cr_start - t_RF_off`.

Also record actual atmospheric exposure separately:

`Δt_air = t_metal_load - t_sample_out`.

The historical values are unknown. Local qualification must determine an allowable maximum rather than choose one by convention.

## 8. Stage A — shortest-delay baseline

Create the best physically achievable local baseline:

- complete P08 under the selected nominal RIE condition;
- minimize handling/air exposure using the actual facility workflow;
- pump to the cleanest routinely reproducible deposition condition;
- deposit 30 nm Cr then 270 nm Au without an intentional delay;
- record every timestamp and pressure/rate trace.

This baseline defines the local `minimum practical delay`, not a historical RP-01 value.

Use at least matched TLM structures and witness films.

## 9. Stage B — delay sensitivity

After the shortest-delay baseline is reproducible, introduce controlled delays spanning the realistic process window.

The DOE should include:

- shortest practical delay;
- one intermediate delay representative of ordinary wafer handling;
- one deliberately extended delay large enough to detect contact degradation if oxidation/adsorption is important.

Exact time values must be selected from local workflow capability and accelerated-screening practicality and recorded as local DOE values, not historical values.

At each delay measure:

- TLM `rho_c` at 80 K;
- sheet resistance / fit intercept and slope;
- I–V symmetry and low-field linearity;
- optical/SEM edge morphology;
- contact adhesion;
- post-cycle stability.

If `rho_c` or variability grows monotonically with delay, release a maximum transfer delay with statistical margin.

## 10. Stage C — deposition-pressure sensitivity

Do not specify an arbitrary universal base pressure. Instead first characterize the actual deposition tool:

- clean/routinely attainable base-pressure distribution;
- pressure rise during Cr;
- pressure rise during Au;
- residual-gas or outgassing behavior if RGA is available.

Then intentionally compare at least:

1. the best routinely achievable clean-vacuum condition;
2. a controlled poorer-vacuum condition still within tool/facility operating rules.

The goal is to measure the sensitivity of contact outcome to deposition environment and to define a **local maximum allowed pressure**, not to match an unsupported historical number.

Do not introduce reactive contamination intentionally if doing so would violate equipment contamination rules; a naturally higher-pressure operating condition or controlled waiting/outgassing state is sufficient.

## 11. Stage D — Cr deposition-rate sensitivity

Cr is the first metal contacting the RIE-modified surface and is therefore the higher-priority kinetic variable.

After pressure and transfer-delay baselines are stable, compare at least three Cr rate settings within the calibrated stable operating range of the actual source/tool:

- low;
- center/nominal local operating point;
- high.

Keep final Cr thickness `30 nm` fixed.

Record:

- rate transient after shutter opening;
- mean and standard deviation of rate;
- substrate-temperature rise;
- film roughness/continuity;
- TLM outcome.

Do not choose the production rate solely from shortest run time or smoothest witness film; electrical contact performance controls.

## 12. Stage E — Au deposition-rate sensitivity

Repeat a bounded rate study for Au while keeping:

- selected Cr process fixed;
- total Au thickness `270 nm` fixed.

Monitor for:

- resist heating/reflow;
- sidewall metal bridging;
- film stress/peeling;
- surface roughness;
- lift-off quality;
- TLM stability.

Because Au is much thicker than Cr in RP-01, its deposition time and radiative/thermal loading can dominate photoresist profile degradation even if the Cr/HgCdTe interface determines contact chemistry.

## 13. Stage F — substrate thermal-budget measurement

Do not assume the wafer stays at room temperature during 300-nm total metal deposition.

Establish a sample-temperature calibration using:

- a dummy sample with embedded/attached thermometry where possible;
- fixture/chuck temperature;
- calibrated thermal model when direct measurement is impossible.

Record maximum temperature and thermal exposure time for each Cr/Au run.

Correlate with:

- chlorobenzene-derived resist-profile stability;
- lift-off quality;
- contact electrical performance;
- detector/passivation drift.

## 14. Cr-to-Au interface control

Preferred qualification baseline is sequential Cr and Au deposition **without breaking vacuum** where the selected tool permits it.

If the tool requires a vacuum break between metals, that is a distinct process branch and must be qualified separately.

Record:

- end-Cr timestamp;
- start-Au timestamp;
- pressure/history during any interval;
- sample exposure state.

## 15. Witness-film characterization

For each DOE run use witness coupons to measure, as appropriate:

- Cr/Au thickness;
- sheet resistance;
- surface roughness;
- adhesion;
- optical/SEM morphology;
- film continuity;
- stress/warpage for sufficiently large witness substrates.

Witness data are process diagnostics. They do not replace TLM on HgCdTe.

## 16. Contact-electrical acceptance

The historical performance anchor remains:

`rho_c ≈ 9×10^-4 Ω·cm² at 80 K`.

During qualification report:

- all raw TLM pair resistances;
- measured spacings/CDs;
- regression slope/intercept;
- extracted sheet resistance;
- transfer length if model-valid;
- specific contact resistivity;
- confidence interval/fit residual;
- device-to-device and run-to-run variation.

A local process should reproduce the historical order of magnitude with stable, ohmic behavior before production limits are frozen.

The final acceptance window must be established statistically from local data; do not equate one successful sample with process capability.

## 17. Cryogenic and aging gate

For selected process conditions:

1. measure TLM/I–V at room temperature if informative;
2. cool to 80 K and measure;
3. warm to room temperature;
4. repeat multiple thermal cycles;
5. remeasure after controlled storage/aging.

Track:

- `rho_c` drift;
- I–V asymmetry;
- open contacts;
- delamination/cracking;
- contact-area morphology.

## 18. Detector-noise correlation

Once TLM passes, fabricate matched photoconductor devices and use P12 to compare:

- low-frequency 1/f noise;
- g-r plateau;
- responsivity at the same field/frequency;
- D*.

A contact process with low static `rho_c` but increased excess noise is not equivalent to RP-01 performance.

## 19. Factor-selection discipline

Do not vary simultaneously:

- RIE plasma condition;
- RIE-to-metal delay;
- base pressure;
- Cr rate;
- Au rate;
- resist/lift-off recipe.

First freeze P08/P14 enough to make P09 interpretable, then vary deposition factors sequentially or with a statistically designed factorial/response-surface plan.

If a multivariate DOE is used, include sufficient center-point replication to estimate process noise.

## 20. Release record

The eventual local P09 release must specify:

- deposition tool/method;
- base-pressure acceptance;
- maximum pressure during Cr/Au;
- QCM calibration/tooling factors;
- Cr rate and tolerance;
- Au rate and tolerance;
- substrate-temperature limit;
- maximum `Δt_RIE-metal` and `Δt_air`;
- Cr-to-Au vacuum-break rule;
- final thickness tolerances;
- P14 resist/lift-off recipe ID;
- TLM acceptance distribution;
- thermal-cycle stability;
- P12 detector-noise correlation.

Until these are established, P09 remains a controlled transfer procedure rather than a historical recipe reconstruction.
