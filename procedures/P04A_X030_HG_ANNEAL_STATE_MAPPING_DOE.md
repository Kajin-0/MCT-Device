# P04A — x≈0.30 Hg-overpressure anneal state-mapping DOE

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. The low-temperature Hg-rich anneal branch is literature-supported, but the exact RP-01 time / Hg chemical potential / cooldown path is not published.

## 1. Purpose

Map post-growth anneal variables into the final HgCdTe material state required by RP-01.

The controlled endpoint is not an anneal temperature/time pair. The endpoint is the measured state vector:

`S_final = {carrier sign, n_H / multicarrier state, µ_H, optical edge/x, thickness, morphology, spatial uniformity}`.

The RP-01 historical material target is approximately:

- n-type;
- supplier density `9.8×10^14 cm^-3`;
- supplier mobility `4.0×10^4 cm²/V·s`;
- nominal `x≈0.30`;
- thickness `9.5 µm`.

The temperature at which the supplier n/µ values were measured is unknown, so local qualification must report measurement temperature explicitly.

## 2. Literature anchors

### Composition-matched Nagahama branch

Nagahama, Ohkata, Nishitani and Murotani report Te-rich slider-LPE HgCdTe spanning approximately `x=0.17–0.30`.

Direct abstract-level findings:

- CdTe `(111)A` substrate;
- conventional slider boat;
- open-tube H2 process;
- as-grown material p-type;
- Hg-overpressure annealing studied from `250–400 °C`;
- `250–300 °C` gives well-behaved n-type material without apparent composition change;
- `400 °C` produces compositional change near the interface.

The public source record does not currently expose the exact dwell time, Hg-source geometry/pressure, or cooldown sequence associated with those results.

### Harman process anchor

A separate primary Hg-rich anneal process gives:

- broad anneal region approximately `200–300 °C`;
- Hg partial pressure roughly `0.1–250 Torr`, chosen according to target defect state;
- example pseudo-isothermal Hg-saturated treatment near `250 °C / 1 h`.

That example generally yields material in the low `10^16 cm^-3` range rather than the RP-01 `~10^15 cm^-3` state. Therefore it is a kinetic/process screening anchor, not a target recipe.

### Kinetic warning for x≈0.30

Low-temperature HgCdTe annealing studies show that defect-equilibration kinetics depend strongly on:

- Cd fraction `x`;
- vacancy concentration;
- anneal temperature;
- Hg chemical potential.

The rate decreases with increasing x over the relevant regime, so a time valid for x≈0.20 cannot be assumed valid for x≈0.30.

For x≳0.26, incomplete ionization of metal vacancies at 77 K can also complicate interpretation of defect concentration from low-temperature Hall data alone.

## 3. Core rule

Do not release a production anneal solely as:

`T = ... ; time = ...`.

The process must also specify:

- Hg source / chemical-potential control;
- sample/source temperature relationship;
- chamber/ampoule geometry;
- ramp history;
- dwell definition;
- cooldown path;
- final measured electrical + optical state.

Two anneals with the same sample temperature/time but different Hg source temperature or cooldown may not produce the same defect population.

## 4. Prerequisite pre-anneal state

Every P04A sample/coupon must have a pre-anneal record containing:

- source wafer/run ID;
- P03/P03B growth condition;
- spatial location on wafer;
- thickness map/value;
- optical edge / inferred x at matched coordinate;
- carrier sign;
- Hall density/mobility or multicarrier result at defined temperature(s);
- sheet resistance;
- surface morphology;
- any prior thermal treatment.

Without the pre-state, the anneal response cannot be interpreted quantitatively.

## 5. Coupon strategy

Whenever wafer area permits, use matched coupons from nearby positions on the same LPE wafer for anneal mapping.

Reason:

- LPE composition/thickness vary spatially;
- comparing unrelated wafers confounds growth variation with anneal response.

Record coupon orientation and exact wafer coordinates so pre/post FTIR/Hall trends can be compared spatially.

## 6. Anneal apparatus variables to record

### Sample zone

- sample temperature sensor type/location;
- sample-zone calibrated temperature;
- axial/radial temperature uniformity;
- heating ramp;
- dwell start criterion;
- dwell duration;
- cooling trajectory.

### Hg source / chemical potential

Depending on apparatus architecture, record:

- Hg/HgTe source material and lot;
- source mass/area;
- source-zone temperature;
- source-to-sample spacing;
- ampoule/chamber free volume;
- calculated/measured Hg partial pressure or defined saturation state;
- source depletion / pre-post mass where measurable.

### Atmosphere / enclosure

- sealed / flowing / semi-closed architecture;
- base vacuum/purge procedure as applicable;
- pressure measurement if applicable;
- ampoule/chamber ID;
- contamination/previous-run history.

## 7. Qualification center and bounds

A rational initial local screen is centered near the literature-supported low-temperature Hg-rich region rather than 400 °C.

Use `250 °C / ~1 h` only as a **literature screening center** because:

- 250 °C lies in the composition-preserving region reported for x≤0.30;
- a separate Hg-saturated primary process explicitly uses about 250 °C / 1 h;
- that independent process does not produce the RP-01 carrier density and therefore cannot be accepted without state measurements.

The initial DOE should bracket:

- temperature within the literature-supported low-temperature region below the 400 °C composition-change warning;
- dwell time around the 1-h screening scale;
- at least two Hg chemical-potential/source conditions if the apparatus can vary them reproducibly.

Exact local levels must be assigned recipe IDs and reported as qualification values, not historical RP-01 setpoints.

## 8. Stage A — time response at fixed T and Hg condition

At one selected center temperature / source condition:

- use at least three dwell times spanning under-treated through near-equilibrated behavior;
- replicate the center time;
- keep ramp/cooldown identical.

For every coupon measure post-anneal:

- carrier sign;
- Hall sheet/volume state with measurement temperature;
- mobility;
- full variable-field behavior during qualification;
- FTIR optical edge/x;
- thickness;
- morphology.

Plot state variables versus dwell time.

Do not assume a plateau has been reached from one apparently successful point.

## 9. Stage B — temperature response

After a useful time range is found, repeat at multiple temperatures within the composition-preserving low-temperature regime.

Determine:

- time required to approach the target n-type state;
- mobility evolution;
- optical composition stability;
- morphology/interface changes.

Higher temperature is not automatically better even when it accelerates equilibration; it may increase interdiffusion/composition change.

## 10. Stage C — Hg chemical-potential response

At a selected temperature/time, vary the Hg chemical-potential control within the safe/calibrated apparatus range.

The variable may be implemented by:

- controlled Hg-source temperature;
- saturated/unsaturated source condition;
- another validated two-zone method.

Record the physical quantity used to define the condition. Do not use labels such as “Hg rich” without source-temperature/pressure information.

Measure the same final state vector after every split.

## 11. Stage D — cooldown-path sensitivity

The final defect state can be frozen in during cooldown rather than defined solely at dwell temperature.

Compare at least two controlled cooldown trajectories after otherwise identical dwell conditions if preliminary data indicate cooldown sensitivity.

Record:

- sample temperature versus time;
- Hg source temperature versus time;
- point where source/sample chemical-potential control changes;
- time to key temperature landmarks.

Do not quench or slow-cool by convention; qualify the path.

## 12. Hall measurement strategy

Use P05 variable-field methods.

At minimum report:

- one detector-relevant cryogenic temperature near 77–80 K;
- an additional temperature where defect ionization/multicarrier interpretation is less ambiguous, where practical.

Because x≈0.30 can show incomplete vacancy ionization at 77 K, do not infer native-defect concentration from one low-temperature one-carrier Hall value alone.

The primary production outcome may still be the detector-relevant 80-K transport state, but defect-physics interpretation needs additional evidence.

## 13. Optical composition-preservation gate

For each coupon compare P06 data before and after anneal at matched coordinates.

Report:

- edge shift;
- model-inferred `Δx`;
- thickness shift;
- fringe/profile change;
- spatial nonuniformity change.

Any statistically significant composition shift not required by the target process is a failure mode.

The 400 °C Nagahama result is an explicit warning that interface-region composition change can occur at higher anneal temperature.

## 14. Mobility as a separate outcome

Reaching `n_H≈10^15 cm^-3` is not enough.

Monitor whether mobility remains consistent with a high-quality n-type epilayer and the RP-01 historical scale `~4×10^4 cm²/V·s`.

A low carrier density accompanied by severe mobility degradation may indicate:

- contamination;
- compensation;
- extended defects;
- surface/multicarrier artifacts;
- thermal damage.

Do not tune n independently of µ.

## 15. Response-surface representation

Within the local qualified range, model key outputs as functions of:

`Y = f(T_anneal, t_dwell, μ_Hg/p_Hg, cooldown, pre_state)`.

Important responses:

- carrier sign;
- log10(n_H);
- µ_H;
- optical x/edge;
- thickness;
- sheet resistance.

Because anneal kinetics can be nonlinear and asymptotic, simple linear fits may be inadequate. Use models only over the experimentally supported region.

## 16. Equilibrium / saturation test

A candidate condition should not be called “equilibrated” unless extending dwell time produces no material change beyond measurement/process uncertainty in:

- carrier sign/density;
- mobility;
- optical composition.

If the state continues to drift with time, the selected dwell is kinetic, not equilibrium-defined, and production timing tolerance must reflect that sensitivity.

## 17. Deriving time/temperature tolerances

Once local sensitivity is measured, derive equipment tolerances from the allowed material-state budget.

For example, if

`S_nt = ∂log10(n_H)/∂t`

near the selected center and allowable log-density variation is `u_n`, require approximately

`u_t <= u_n / |S_nt|`.

Analogously use derivatives with temperature and Hg chemical potential.

Do not assign arbitrary ±time or ±temperature specifications before measuring state sensitivity.

## 18. Candidate release condition

A local P04 anneal may advance toward release only when:

- post-anneal material is reproducibly n-type;
- detector-relevant Hall state is centered near the required range;
- mobility remains acceptable;
- optical composition/thickness are preserved;
- run-to-run variability is measured;
- cooldown dependence is understood/controlled;
- Hg source/chemical-potential condition is reproducible;
- downstream detector fabrication gives stable P10–P13 performance.

Numerical n/µ acceptance windows must be frozen only after resolving the historical supplier-measurement-temperature ambiguity or defining a new local detector-relevant material specification.

## 19. Failure modes to preserve

Record explicitly:

- remains p-type;
- over-converts to excessively high n;
- mobility degrades;
- optical edge/composition shifts;
- interface grading appears;
- surface morphology changes;
- spatial nonuniformity increases;
- result depends strongly on cooldown;
- Hg-source condition is unstable/depleted;
- multicarrier Hall prevents simple state extraction.

Failed states are essential for mapping the process window.

## 20. Historical conclusion

The literature strongly supports the low-temperature Hg-overpressure **process family** for converting Te-rich LPE HgCdTe up to x≈0.30 to n-type material without the high-temperature interface-composition change seen near 400 °C.

It does **not** close a unique RP-01 dwell time / Hg pressure / cooldown sequence.

Therefore the correct route is controlled state mapping and a measurement-defined endpoint, not adoption of 250 °C / 1 h as if it were the original Fermionics recipe.
