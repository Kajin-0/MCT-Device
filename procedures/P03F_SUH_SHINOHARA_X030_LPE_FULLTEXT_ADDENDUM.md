# P03F — Suh/Shinohara x≈0.30 LPE full-text addendum

**Status:** PRIMARY-TRANSFER QUALIFICATION ADDENDUM. Supplements P03B/P03C/P03D/P03E and P30. Not an RP-01 historical traveler.

## Purpose

Freeze the two strongest newly recovered empirical constraints on the x≈0.30 horizontal-slider LPE problem: (1) Hg-vapor conductance/solution-mass control from Suh et al. 1992 and (2) numerical wipe clearance/thermal-wipe coupling from Shinohara et al. 1994.

The historical Honeywell/Fermionics geometry remains unrecovered. This document provides qualification branches, not historical identity.

## Suh near-x≈0.30 liquid/source branch

For nominal Hg0.7Cd0.3Te growth, Suh reports a Te-rich liquid with elemental mole fractions `Hg=0.158, Cd=0.012, Te=0.830`. Equivalent Round-61 notation (`DER`): `xL≈0.0706`, `yL=0.830`. Reported growth range: approximately `500–489 °C`.

Source preparation in that branch:

- elemental Hg/Cd/Te;
- vacuum-sealed quartz;
- `700 °C / 12 h`;
- water quench;
- about `2.5 g` solution per LPE run.

Use this as an independent PT neighborhood around the Honeywell `xL=.082/yL=.810/TL=507 °C` center. Do not average the two compositions or call either the Fermionics/RP-01 liquid without direct evidence.

## Suh Hg-vapor throttle

Suh's boat places a conical graphite button over the solution well between HgTe and solution vapor spaces. With a central hole, the reported gas-phase argument gives

`J_Hg,in ∝ D (P_HgTe - P_solution) d_hole^2 / t_button`.

External loss is independently affected by slider/body clearance. For nominal x≈0.30 material, approximately `2 mm` hole diameter drove net solution-weight change close to zero in the published apparatus.

Required local geometry record:

- `d_hole`, `t_button`, button/body clearance;
- solution-well and HgTe-well geometry;
- solution-to-button vapor volume;
- slider/body clearance and cover fit;
- Hg-source exposed area/mass;
- process pressure/gas state;
- pre/post solution and Hg-source mass.

The local release objective is not the literal 2-mm dimension. It is minimized `|Delta m_solution|` over the qualified thermal cycle while maintaining correct x, thickness and morphology.

## Suh near-liquidus thermal branch

Reported sequence:

- homogenize ~20 °C above liquidus;
- initial rapid cool;
- slow cool at ~0.3 °C/min;
- contact ~1 °C below liquidus;
- grow ~30 min while ramping temperature;
- separate and cool rapidly.

This validates the P03E state `{TL,heat, DeltaT_contact, dT/dt, t_contact}` but does not replace the Round-61 SYN factorial center.

Published x≈0.30 capability benchmark: mean `x≈0.304`, run-to-run `sigma_x≈0.003`, within-layer variation `~±0.002`, interface width `~2–3 µm`, mirror-like/terraced surfaces. Use only as PT comparison metrics.

## Shinohara source-mass trajectory

Reported apparatus/process state:

- conventional graphite slider with HgTe reservoir;
- quartz tube `100 mm ID`;
- H2 `1 atm`, `0.5 L/min`;
- source `746 K`, melting point `727 K`;
- growth start after ~130 min;
- growth period 30 min;
- HgTe reservoir 2-g and 3-g branches.

The source and reservoir were weighed. The source can first gain Hg and later lose it, so P03D/P30 shall distinguish conceptually `m_solution,load`, `m_solution,growth-start`, `m_solution,post-growth`, `m_Hg-source,load` and `m_Hg-source,post`. When continuous weighing is impossible, use sacrificial dummy cycles stopped at selected times.

## Shinohara numerical wipe-clearance branch

For x≈0.31 sample CZT4:

- `(111) Cd0.97Zn0.03Te`, 10×10×1 mm;
- equilibrium cooling (`DeltaT=0`);
- cooling rate `0.15 K/min`;
- complete wipe over 10×10 mm;
- slider-bottom/substrate-surface clearance `~20 µm`;
- clearance variation `<~5 µm` identified as important;
- layer thickness `~4 µm`;
- interdiffusion width `~2 µm`;
- x≈0.31;
- slightly terraced/specular surface.

Another equilibrium-cooling branch used `20–25 µm` clearance.

P30 shall therefore distinguish `clearance_RP01=OPEN` from `clearance_Shinohara_PT≈20 µm`; 20–25 µm is an observed PT range, not a universal optimum.

## Wipe/thickness coupling

Shinohara reports equilibrium cooling producing `2–4 µm` layers and best wipe behavior, while 15-K supercooling/step cooling produced `30–41 µm` layers. RP-01 target thickness is ~`9.5 µm`.

Minimum response vector for local qualification:

`Y={d_layer, x_mean, sigma_x, residual_melt_fraction, max_droplet, scratch_density, terrace_metric}`.

Minimum controlled factor set:

`X={DeltaT_contact, dT/dt, t_contact, clearance, wipe_geometry, Hg-transfer state}`.

Do not freeze a wipe clearance from a 4-µm layer and assume it remains valid at 9.5 µm without checking epilayer/slider separation.

## Growth-window Hg-loss gate

Shinohara reports approximately `0.014 g` source-liquid mass loss during the growth window despite Hg-vapor supply. On the ~2-g source scale this is roughly `7e-3` fractional mass change.

This is not a release threshold. It demonstrates that sub-percent source-mass change can be compositionally consequential. Correlate source/Hg-reservoir mass change with P06 x/cutoff before tuning temperature.

## Recommended qualification sequence

1. Freeze one boat/CAD revision and measure all vapor/wipe geometry.
2. Run sacrificial mass-balance cycles to map solution/Hg-source mass change versus time.
3. If a Suh-like button is adopted, screen throttle conductance around one defined center while keeping vapor geometry fixed.
4. Confirm actual liquidus by P03E.
5. Map slider clearance/flatness/recess flushness on dummy mechanics before detector-grade material.
6. On material runs, determine clearance at slide-out from recess/substrate/epilayer geometry.
7. Treat thermal trajectory and wipe clearance jointly; record residual melt and scratch metrics.
8. Fit x/thickness only after Hg mass balance is included in the run state.
9. Retain every value as PT/SYN unless direct RP-01/Fermionics records are recovered.

## Explicit non-promotions

- 2-mm button hole != RP-01 button hole.
- 20-µm wipe clearance != RP-01 clearance.
- 700 °C/12 h != RP-01 source synthesis.
- 0.15 K/min equilibrium cooling != RP-01 growth ramp.
- x≈0.304 ±0.003 != RP-01 acceptance criterion.
- 0.014-g loss != acceptable local loss limit.