# RP-01 gap-matrix addendum — source-recovery round 9

**Date:** 2026-08-15 America/New_York

This addendum records the liquidus/equilibration, final CdZnTe surface and Hg-anneal cooldown overrides introduced after round 8.

| Module | Variable / evidence required | Current status | Round-9 interpretation |
|---|---|---|---|
| LPE thermal | historical tie-line liquidus | CLOSED-P | xL=.082/yL=.810 historical TL=507 °C. |
| LPE thermal | actual local liquidus | CONTROLLED-QUAL | P03E requires measuring/inferring the actual melt liquidus; nominal charge/controller value is not sufficient. |
| LPE thermal | heating vs cooling transformation | CONTROLLED-QUAL | Prefer heating liquidus for equilibrium reference; record cooling nucleation/hysteresis separately because supercooling can be large. |
| LPE thermal | exact Honeywell equilibration duration | OPEN | No exact hold recovered for xS=.29 branch. Harman ~1 h at 550 °C is independent benchmark only. |
| LPE thermal | equilibration release criterion | CONTROLLED-QUAL | P03E uses hold-time convergence of `{TL, mean x, x uniformity, thickness/growth rate, morphology, mobility}` rather than timer alone. |
| LPE thermal | sensor calibration / melt offset | CONTROLLED-QUAL | Calibrate sensor/readout, map source-to-sensor offset and spatial gradients. |
| LPE thermal | temperature uncertainty | CONTROLLED-QUAL | Derive required uT from locally measured `∂x/∂T` and `∂d/∂T`, not arbitrary controller stability. |
| LPE thermal | local supercooling definition | CONTROLLED-QUAL | `ΔT_SC = TL,measured - T_contact`; retain nominal and corrected values. |
| Substrate prep | final Br2/methanol family | CANDIDATE-P / QUAL | Brief 2–3% Br2/MeOH immediately before boat loading is LPE-supported in a different x≈.20–.22 branch; not historical RP-01. |
| Substrate prep | removal depth | CONTROLLED-QUAL | P07C requires measured chemical-removal depth rather than time alone. |
| Substrate prep | final surface roughness/topography | CONTROLLED-QUAL | AFM/DIC/pit-wave metrics required; concentration/time can change pitting/waviness. |
| Substrate prep | final chemical state | CONTROLLED-QUAL | Br-MeOH leaves Te-enriched CdZnTe; qualification should establish a stable chemistry proxy where possible. |
| Substrate prep | rinse/dry | OPEN / CONTROLLED-QUAL | Historical sequence unknown; local sequence released by resulting LPE interface/material quality. |
| Substrate prep | clean-to-load delay | CONTROLLED-QUAL | P07C requires timestamped final-prep→boat/furnace path and DOE for maximum allowed delay. |
| Substrate prep | face dependence | CONTROLLED-QUAL | Final treatment must be requalified on selected P07B polarity/miscut; do not assume identical etch behavior. |
| Post-growth anneal | cooldown trajectory | CONTROLLED-QUAL | P04B makes cooldown a state-defining variable; Kawazu x=.20 directly proves quench vs gradual cooling changes final carrier state. |
| Post-growth anneal | sample/reservoir T trajectories | CONTROLLED-QUAL | Record separately; Jones x=.17–.31 shows isothermal vs two-temperature conditions can drive opposite carrier-type outcomes. |
| Post-growth anneal | fixed Hg vapor pressure / pHg path | PARTIAL / QUAL | Hg chemical potential controls equilibrium and/or time to equilibrium depending apparatus; local reservoir model/measurement required. |
| Post-growth anneal | historical RP-01 cooldown | OPEN | No Fermionics/RP-01 cooldown recovered. |
| Post-growth anneal | x=.20 8 h / 200 min numbers | NONTRANSFER | Kawazu source-specific values. Use only as causal cooldown evidence. |
| Post-growth anneal | diffusion-scale implication | CLOSED-D / NONRELEASE | Using D_Hg≈1e-9 cm²/s lower-bound scale gives ~35 µm in 200 min and ~15 min across 9.5 µm; illustrates cooldown relevance only. |
| Post-growth anneal | final state gate | CONTROLLED-QUAL | `Y_cool={carrier sign,nH/multicarrier,µH,optical x/edge,thickness,morphology,lifetime}`. |
| Post-growth anneal | dwell/cooldown identifiability | CONTROLLED-QUAL | P04B stages dwell sensitivity, cooldown sensitivity, then limited interaction DOE. |
| Post-growth anneal | low-background n feasibility | CANDIDATE-P / NONTARGET | Astles et al. shows 6–8e13 cm^-3 after Hg-rich anneal in Te-rich LPE branch; proof of feasibility, not RP-01 target. |

## Round-9 control rule

The upstream/post-growth material process must carry full state histories:

`source composition/inventory -> actual liquidus + T(t) -> substrate surface state + clean-to-load -> growth -> Hg anneal T_sample(t), T_reservoir(t), pHg(t) -> P05/P06/P13 state`.

A nominal controller temperature, etch time or anneal dwell is not sufficient for release when the material output depends on the full trajectory.

## Governing files

- `procedures/P03E_LPE_LIQUIDUS_EQUILIBRATION_THERMAL_METROLOGY.md`
- `procedures/P07C_CZT_FINAL_SURFACE_CLEAN_TO_LOAD_QUALIFICATION.md`
- `procedures/P04B_HG_ANNEAL_COOLDOWN_TRAJECTORY_QUALIFICATION.md`
- P03/P03B/P03C/P03D/P04/P04A/P07/P07A/P07B/P05/P06/P13.
