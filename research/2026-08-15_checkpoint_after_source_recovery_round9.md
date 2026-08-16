# Recovery checkpoint — source-recovery round 9

**Date:** 2026-08-15 America/New_York

**Purpose:** Fast handoff after liquidus/equilibration, final CdZnTe surface-state and Hg-anneal cooldown research. Read after `AGENTS.md` and round-8 checkpoint.

## 1. New controlled files

Round 9 added:

- `procedures/P03E_LPE_LIQUIDUS_EQUILIBRATION_THERMAL_METROLOGY.md`
- `procedures/P07C_CZT_FINAL_SURFACE_CLEAN_TO_LOAD_QUALIFICATION.md`
- `procedures/P04B_HG_ANNEAL_COOLDOWN_TRAJECTORY_QUALIFICATION.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND9.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND9.md`

## 2. P03E — actual liquidus, not controller folklore

Historical Honeywell composition remains:

`xL=.082, yL=.810, TL=507 °C -> xS≈.29`.

Bowers–Schmit says heat above liquidus, then grow below liquidus, but does not specify the exact equilibration hold/overtemperature/ramp for the x=.29 row.

A primary HgCdTe LPE in-situ DTA patent demonstrates why the **actual melt's liquidus** should be measured/verified rather than blindly equated to the nominal phase-diagram value: Hg transport/distillation and apparatus history can shift the actual source state.

P03E therefore distinguishes:

- `TL,heat` = heating liquidus/equilibrium reference;
- `Tnuc,cool` = cooling/nucleation transformation;
- `ΔT_hyst = TL,heat - Tnuc,cool`;
- intended growth supercooling `ΔT_SC = TL,measured - T_contact`.

Cooling transformations can be strongly supercooled and are not used as the equilibrium liquidus without calibration.

## 3. P03E equilibration is convergence-based

Harman's independent Te-rich slider process reports a typical ~1 h equilibration at 550 °C. This is used only as an order-hour benchmark for the local hold-time experiment.

The Honeywell x=.29 hold remains historically open.

P03E defines equilibration by convergence of:

`Y_eq={TL,mean x,x uniformity,thickness/growth rate,morphology,post-anneal mobility}`.

A fixed timer may be used in production only after the local convergence time and margin are demonstrated.

## 4. P03E temperature tolerance is sensitivity-derived

Before release, locally measure:

- `∂x/∂T`;
- `∂d/∂T`;
- sensor calibration uncertainty;
- source-to-sensor offset;
- spatial gradients;
- temporal drift/ramp lag.

Then derive allowed temperature uncertainty from the material budget, e.g.

`u_T <= u_x,T / |∂x/∂T|`.

Do not impose arbitrary ±0.01 °C control unless the measured process sensitivity actually requires it.

## 5. P07C — final substrate preparation is an output state

The exact RP-01/Fermionics CdZnTe final surface process remains open.

Best LPE-specific transfer branch:

- `(111)B` CdZnTe;
- chemical + mechanical polish;
- final `2–3% Br2/methanol` treatment;
- only a few seconds;
- immediate graphite-boat loading;
- different x≈.20–.22 HgCdTe branch.

Do not transplant that concentration/time historically.

Independent CdZnTe surface studies confirm:

- Br-MeOH removes polishing damage;
- treatment can leave a Te-rich surface;
- concentration/time alter pitting/waviness/roughness;
- favorable conditions in radiation-detector studies are not LPE recipes.

P07C therefore releases on:

`Y_surface={removed depth,roughness,pit/wave density,chemical-state proxy,t_CTL,epilayer morphology,interface defect,mobility,lifetime}`.

## 6. P07C clean-to-load clock

Record timestamps for:

- end final rinse;
- dry complete;
- boat load;
- furnace/tube insertion or purge start.

Qualify maximum clean-to-load delay by deliberately varying delay and measuring resulting LPE interface/material quality.

Changing P07B polarity/miscut requires P07C requalification unless equivalence is shown.

If an in-situ meltback is used, final chemical prep and meltback removed depth must be qualified jointly.

## 7. P04B — cooldown is part of the anneal

Kawazu/Ochi/Sonoda/Takamiya 1995, DOI `10.1007/BF02653061`, directly shows in LPE Cd0.2Hg0.8Te that final electrical properties depend strongly on cooldown after an Hg-rich anneal.

Source-specific experiment:

- 260–350 °C;
- 8 h;
- fixed Hg vapor pressure;
- quench vs gradual ~200-min cooldown.

Quenched samples showed anneal-T-dependent p→n behavior; gradually cooled samples were n-type across the tested range.

These numerical conditions are **not transferred to x≈.30 RP-01**.

Transferable conclusion: defect equilibration continues during cooldown and the final state depends on the complete thermal/Hg trajectory.

## 8. Diffusion-scale check — illustrative only

Kawazu estimates `D_Hg >~1×10^-9 cm²/s` during the relevant regime.

At the lower-bound value:

- `sqrt(D×200 min) >~34.6 µm`;
- `L²/D` for 9.5 µm is ~902 s ≈15 min.

This demonstrates that a 9.5-µm layer can plausibly remain defect-state active during cooldown.

It is **not** a recommended RP-01 cooldown time. D varies with x and temperature.

## 9. Sample/reservoir temperatures must remain separate

Jones/Quelch/Capper/Gosney, *JAP* 53, 9080–9092, DOI `10.1063/1.330419`, covers x≈.17–.31 and distinguishes:

- isothermal sample/Hg-reservoir anneals -> native-defect p to n;
- lower-reservoir-temperature/two-temperature closed-tube anneals -> n to p with acceptor state controlled by T/pHg;
- two-temperature open-tube anneals -> n to p, with Hg pressure affecting time to equilibrium in the studied range.

Therefore P04B logs:

`T_sample(t), T_reservoir(t), pHg(t)`

through dwell and cooldown.

Do not label an anneal only by sample temperature.

## 10. Very low background n is physically feasible, but not the RP-01 target

Astles/Shaw/Blackmore/Hall 1992, DOI `10.1016/0022-0248(92)90747-7`, reports a Te-rich LPE process with:

- Hg loss ~0.3 mg/min;
- strong composition/thickness reproducibility;
- undoped background n after Hg-rich anneal `~6–8×10^13 cm^-3`.

Use this only as evidence that low-background n material is physically achievable after Hg-vacancy removal. Exact x/anneal branch is not established as RP-01 compatible from accessible data.

## 11. Composition dependence remains critical

Chandra/Schaake/Kinch 2003, DOI `10.1007/s11664-003-0075-5`, shows low-T anneal kinetics depend strongly on x, vacancy concentration and temperature and slow as Cd fraction rises.

For x≳.26, incomplete metal-vacancy ionization at 77 K complicates purely electrical defect-state inference.

Thus the x=.20 Kawazu cooldown kinetics cannot be used numerically for x≈.30.

P04/P04B must use P05 + P06 together.

## 12. Material-state chain after round 9

The upstream/post-growth controlled chain is now:

`P07/P07A/P07B/P07C substrate -> P03C source -> P03D inventory/depletion -> P03E liquidus/equilibration/T field -> P03B growth trajectory -> wipe-off -> P06 as-grown map -> P04/P04A/P04B Hg-rich state trajectory -> P05/P06/P13 final material gate`.

## 13. Highest-value remaining upstream work

Historical values still open:

1. exact Honeywell source synthesis;
2. exact charge mass/well dimensions;
3. exact RP-01 CdZnTe face/miscut/final clean;
4. exact x=.29 Honeywell hold/ramp;
5. exact Fermionics Hg anneal/cooldown.

All now have controlled local qualification routes.

The next high-value task is no longer another generic archival search. It is to define **statistical process capability / release criteria** that turn these qualification procedures into an actual process window once local data exist.

## 14. Recovery order

1. `AGENTS.md`
2. this checkpoint after round 8
3. `docs/SOURCE_LEDGER_ADDENDUM_ROUND9.md`
4. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND9.md`
5. P03E/P07C/P04B
6. prior P03/P04/P07 files for broader context.
