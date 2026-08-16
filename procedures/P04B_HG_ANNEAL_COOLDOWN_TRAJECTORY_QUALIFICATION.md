# P04B — Hg-rich anneal cooldown-trajectory qualification

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. Supplements P04/P04A.

## 1. Purpose

Treat the entire post-growth Hg-rich thermal path—including cooldown—as a state-defining process variable for x≈0.30 HgCdTe.

The release target is not merely “n-type after anneal.” The local process must reproducibly reach a detector-compatible final state while preserving:

- alloy composition / spectral edge;
- active-layer thickness;
- morphology;
- electron mobility;
- low carrier concentration;
- spatial uniformity;
- subsequent device performance.

The final material state is therefore written schematically as

`State_final = F(T(t), pHg(t), t_dwell, source geometry, initial defect state, cooldown trajectory)`.

## 2. Direct experimental proof that cooldown matters

Z. Kawazu, S. Ochi, T. Sonoda, S. Takamiya, “Effect of Cooling Procedure After Annealing on Electrical Properties of Cd0.2Hg0.8Te Epitaxial Films Grown by Liquid Phase Epitaxy,” *Journal of Electronic Materials* 24(9), 1113–1117 (1995), DOI `10.1007/BF02653061`.

The direct published experiment used:

- LPE `Cd0.2Hg0.8Te`;
- Hg-rich annealing over `260–350 °C`;
- dwell `8 h`;
- fixed Hg vapor pressure;
- two cooldown modes:
  - quench;
  - gradual cooling over approximately `200 min`.

Reported outcome:

- quenched samples showed strong anneal-temperature dependence and a p→n transition near 300 °C;
- gradually cooled samples were n-type across the tested anneal-temperature range;
- electrical properties depended strongly on cooling procedure;
- interpretation: Hg-vacancy annihilation continues during gradual cooling because Hg diffusion remains sufficiently rapid.

### Use restriction

This source is `x=0.20`, not RP-01 `x≈0.30`.

Therefore:

- `8 h` is **not** an RP-01 dwell;
- `200 min` is **not** an RP-01 cooldown;
- the 260–350 °C matrix is **not** a production window for RP-01.

The transferable result is the **causal role of cooldown trajectory**.

## 3. Diffusion-scale consistency check [D]

Kawazu et al. estimate the Hg diffusion coefficient during the relevant cooldown process as greater than approximately

`D_Hg > 1×10^-9 cm²/s`.

Using the lower-bound value only as an illustrative scale:

For `t = 200 min = 1.2×10^4 s`,

`L_D ≈ sqrt(D t) > sqrt(1×10^-9 × 1.2×10^4) cm`

so

`L_D > 3.46×10^-3 cm ≈ 34.6 µm`.

That length exceeds the RP-01 active-layer thickness of 9.5 µm.

Conversely, using

`t ≈ L²/D`

for `L=9.5 µm = 9.5×10^-4 cm` and `D=1×10^-9 cm²/s` gives

`t ≈ 9.0×10^2 s ≈ 15 min`.

These are **not RP-01 anneal/cooldown times**. They only demonstrate that, at diffusion coefficients of this order, a 9.5-µm film can remain chemically/defect-state active during a realistic cooldown interval.

Because `D_Hg` depends on composition and temperature, the local x≈0.30 trajectory must be measured/qualified independently.

## 4. Composition-matched temperature bounds

Nagahama et al. report Te-rich LPE HgCdTe with approximately `x=0.17–0.30` and Hg-overpressure annealing from 250–400 °C.

Key composition-relevant observations already incorporated into P04/P04A:

- 250–300 °C produced well-behaved n-type layers without obvious composition change;
- ~400 °C produced an interface-region composition change.

Therefore the local x≈0.30 state-mapping program should remain centered in the low-temperature native-defect-control regime unless new direct evidence justifies otherwise.

The exact dwell and Hg chemical potential remain local qualification variables.

## 5. Independent low-background carrier-density benchmark

Astles, Shaw, Blackmore, Hall, “Improved control of composition and electrical properties of liquid phase epitaxial (CdHg)Te layers,” *Journal of Crystal Growth* 117, 213–217 (1992), DOI `10.1016/0022-0248(92)90747-7`, reports:

- Te-rich slider LPE at ~460 °C;
- very low Hg-loss rate (~0.3 mg/min) using powdered HgTe source;
- excellent composition/thickness reproducibility;
- undoped background carrier concentration after Hg-rich annealing as low as `n≈(6–8)×10^13 cm^-3`.

The exact x/anneal path is not established as RP-01-compatible in the accessible abstract.

Use this only as evidence that **sub-10^14 cm^-3 n-type background states are physically achievable in Te-rich LPE HgCdTe after Hg-rich vacancy removal**, not as an RP-01 setpoint.

## 6. Anneal trajectory variables

Every P04/P04B run shall record the complete temperature and Hg-chemical-potential history.

At minimum:

### Sample temperature trajectory

- ramp from room temperature to dwell;
- dwell temperature;
- dwell time;
- start of cooldown;
- cooldown rate versus temperature;
- any holds/plateaus;
- temperature at which Hg source and sample cease to be chemically coupled;
- final room-temperature arrival.

### Hg chemical-potential / reservoir trajectory

Record:

- Hg source identity;
- reservoir/source temperature versus time;
- sample/source temperature difference;
- estimated or measured Hg vapor pressure where possible;
- whether cooling is isothermal, pseudo-isothermal or two-temperature;
- valve/open-tube/closed-tube state;
- point at which reservoir is isolated or becomes ineffective.

The phrase “Hg-rich cooldown” is insufficient without the source/temperature path.

## 7. Cooldown-mode qualification axes

The local development matrix should explicitly compare at least two distinct cooldown behaviors after a matched dwell:

1. **rapid cooldown / quench-like condition** within apparatus capability;
2. **controlled gradual cooldown** under maintained Hg-rich conditions.

A third intermediate ramp is preferred if material inventory permits.

The exact durations/rates are locally selected and must not be copied from Kawazu's x=.20 process.

## 8. Matched-coupon design

Use matched coupons from the same epilayer or immediately adjacent wafer regions to separate cooldown effects from growth/material variation.

For a given dwell condition:

- coupon A -> rapid cooldown;
- coupon B -> gradual cooldown;
- optional coupon C -> intermediate cooldown.

Keep fixed:

- pre-anneal material state;
- sample geometry/thickness;
- anneal furnace position;
- Hg source condition;
- dwell T/time;
- measurement method.

## 9. Pre/post metrology

For every cooldown condition obtain, where practical, the same-coordinate pre/post data.

### P06 optical/composition

- full spectrum;
- edge metric;
- inferred x/model result;
- thickness/fringes;
- spatial map.

### P05 electrical

- carrier sign;
- Hall density / multicarrier state;
- mobility;
- sheet resistance;
- temperature of measurement.

### Morphology

- DIC/optical inspection;
- surface defect/precipitate change;
- interface damage where cross-sectional methods are justified.

### P13/device proxy where material allows

- effective lifetime;
- matched photoconductor response/noise after fabrication.

## 10. Cooldown-state acceptance vector

Define

`Y_cool = {carrier sign, n_H/multicarrier state, µ_H, optical x/edge, thickness, morphology, lifetime}`.

A cooldown trajectory is acceptable only if `Y_cool` is reproducible and satisfies the complete RP-01 material-state interface.

Do not accept based only on carrier sign.

## 11. Targeting the RP-01 low-density n state

RP-01 historical starting-material anchors are:

- n-type;
- `n≈9.8×10^14 cm^-3`;
- `µ≈4.0×10^4 cm²/V·s`;
- thickness `9.5 µm`;
- nominal `x≈0.30`.

Because the historical temperature of the supplier Hall values is unknown, the local acceptance procedure shall report its own measurement temperature explicitly rather than forcing numerical equality at an assumed 80 K.

The target should initially be treated as a **reference neighborhood** and refined once local Hall-vs-temperature data establish an apples-to-apples comparison.

## 12. Dwell versus cooldown identifiability

A final Hall state after one arbitrary dwell/cooldown pair cannot determine which stage controlled the result.

Therefore develop the process in stages:

### Stage A — dwell sensitivity

At one controlled cooldown trajectory, vary dwell time/T/Hg chemical potential.

### Stage B — cooldown sensitivity

At one stable dwell condition, vary cooldown trajectory.

### Stage C — interaction

Only after main effects are understood, evaluate limited dwell × cooldown interaction points.

This prevents confounding.

## 13. Two-temperature / isothermal distinction

Primary annealing literature on HgCdTe with `x≈0.17–0.31` shows that:

- isothermal Hg-reservoir/sample conditions can drive native-defect p-type material toward n-type;
- lower-reservoir-temperature/two-temperature conditions can drive or preserve p-type states depending on system geometry/pressure;
- Hg vapor pressure can control either equilibrium defect concentration, kinetics, or both.

Therefore P04B must preserve the **sample temperature and reservoir temperature as separate recorded variables**.

Do not characterize an anneal solely by sample temperature.

## 14. Cooldown endpoint

Define a chemically meaningful cooldown endpoint rather than “room temperature.”

Possible local criterion:

- sample temperature below which Hg-vacancy redistribution during the remaining cooldown is negligible compared with process uncertainty.

This endpoint must be justified from kinetics/literature/local data.

Until closed, continue recording the full trajectory to room temperature.

## 15. Thermal lag / actual sample temperature

The sample may not follow furnace controller temperature during rapid cooling.

Qualify:

- sample-to-furnace lag;
- reservoir-to-sample lag;
- spatial gradient;
- repeatability.

Use a calibrated dummy/sample thermometry study if direct device-wafer thermometry is impractical.

The released cooling rate shall refer to **actual or calibrated sample temperature**, not just furnace setpoint slew rate.

## 16. Composition-preservation gate

A cooldown that achieves the desired Hall state but causes a statistically significant unwanted P06 composition/edge shift fails.

This is especially important because higher-temperature anneal branches can alter the HgCdTe composition near interfaces.

## 17. Mobility/lifetime gate

A low carrier density reached by creating compensating damage/impurities is not equivalent to clean low-density n-type material.

Therefore require acceptable:

- electron mobility;
- lifetime/device proxy;
- spatial uniformity.

Use Astles' low-background n-type result only as proof of physical feasibility, not as a universal carrier-density goal.

## 18. Repeated-run capability

Before freezing a cooldown trajectory, demonstrate reproducibility over:

- multiple coupons;
- multiple anneal runs;
- at least two source/material lots where feasible.

Track:

- mean n_H;
- run-to-run sigma;
- mobility;
- optical-edge shift;
- failure rate.

## 19. Release rule

A local Hg anneal may be labeled `RP01-MATERIAL-STATE-QUALIFIED` only when the complete trajectory is frozen and demonstrates repeatable final:

`{carrier type, Hall/multicarrier state, mobility, optical x/edge, thickness, morphology, lifetime/device proxy}`.

The final traveler must include:

- dwell T/time;
- Hg reservoir/source state;
- pHg model/measurement basis;
- ramp rates;
- cooldown trajectory;
- endpoint criterion;
- metrology result.

“250 °C for 1 h” or any other dwell-only shorthand is not a complete anneal recipe.

## 20. Historical closure state

The exact RP-01/Fermionics anneal and cooldown remain `OPEN`.

P04B provides the controlled local path to close the missing cooldown/trajectory dimension without transplanting source-specific x=.20 numbers.