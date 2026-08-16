# Source ledger addendum — source-recovery round 9

**Date:** 2026-08-15 America/New_York

This addendum records the thermal-equilibration, final-substrate-surface and Hg-anneal/cooldown sources promoted during round 9.

## S-R9-01 — in-situ DTA / actual-melt liquidus method

**Class:** Primary-B / HgCdTe LPE metrology  
**Citation:** U.S. Patent 4,474,640, “In situ differential thermal analysis for HgCdTe liquid phase epitaxy.”

**Role:** Primary metrology basis for P03E.

**Key transferable principle:** the actual melt composition/liquidus can differ from the nominal charge because Hg transport/distillation and apparatus history modify the liquid. The method uses differential thermal sensing of the actual HgCdTe melt against a neutral reference to identify thermal transformations.

**Important interpretation:**

- use the heating transformation/liquidus as the preferred equilibrium liquidus reference;
- cooling transformations can show strong supercooling/hysteresis;
- do not equate a cooling nucleation event with the thermodynamic liquidus;
- the patent's numerical recipe is a different HgCdTe LPE branch and is not transplanted into RP-01.

**Procedure:** `procedures/P03E_LPE_LIQUIDUS_EQUILIBRATION_THERMAL_METROLOGY.md`.

## S-R9-02 — Harman 1980 Te-rich equilibration benchmark

**Class:** Primary-A  
**Citation:** T. C. Harman, “Liquidus isotherms, solidus lines and LPE growth in the Te-rich corner of the Hg-Cd-Te system,” *Journal of Electronic Materials* 9 (1980).  
**DOI:** `10.1007/BF02822728`

**Round-9 role:** provides an independent Te-rich horizontal-slider benchmark of approximately 1 h equilibration at 550 °C in Harman's process.

**Restriction:** not the xL=.082/yL=.810 Honeywell hold condition. Use only to size an order-hour local convergence experiment.

## S-R9-03 — CdZnTe final-surface LPE branch

**Class:** Primary/near-primary LPE transfer branch  
**Role:** strongest current LPE-specific final-surface candidate for P07C.

**Recovered process family:**

- `(111)B` CdZnTe;
- chemical + mechanical polish;
- final `2–3% Br2/methanol` treatment;
- exposure for only a few seconds;
- loading into the graphite boat immediately afterward;
- resulting HgCdTe branch around x≈0.20–0.22.

**Restriction:** different composition branch. The concentration/time are not promoted to historical RP-01 setpoints.

## S-R9-04 — Bensouici et al. 2010 — CdZnTe surface chemistry/roughness

**Class:** Primary-A / surface physics  
**Citation:** A. Bensouici et al., “Study of effects of polishing and etching processes on Cd1−xZnxTe surface quality,” *Journal of Crystal Growth* 312, 2098–2102 (2010).  
**DOI:** `10.1016/j.jcrysgro.2010.03.045`

**Role:** independent CdZnTe surface-state evidence.

**Key findings used in P07C:**

- Br-methanol removes polishing damage and modifies surface morphology;
- a 2% Br-MeOH / 30 s condition was favored among that study's tested radiation-detector surface treatments;
- treatment produces Te enrichment.

**Restriction:** radiation-detector surface study, not HgCdTe LPE recipe. Use for output metrology/physics only.

## S-R9-05 — Zheng et al. 2011 — CdZnTe surface preparation

**Class:** Primary-A / surface physics  
**Citation:** Q. Zheng et al., “Influence of surface preparation on CdZnTe nuclear radiation detectors,” *Applied Surface Science* 257, 8742–8746 (2011).  
**DOI:** `10.1016/j.apsusc.2011.05.098`

**Role:** shows Br-methanol generally improves CdZnTe surface quality compared with other alcohol solvents, while concentration changes can move morphology between pitting and wavy behavior and leave a Te-rich surface.

**Restriction:** not an LPE recipe.

## S-R9-06 — Kawazu et al. 1995 — cooldown controls final HgCdTe electrical state

**Class:** Primary-A  
**Citation:** Z. Kawazu, S. Ochi, T. Sonoda, S. Takamiya, “Effect of Cooling Procedure After Annealing on Electrical Properties of Cd0.2Hg0.8Te Epitaxial Films Grown by Liquid Phase Epitaxy,” *Journal of Electronic Materials* 24(9), 1113–1117 (1995).  
**DOI:** `10.1007/BF02653061`

**Direct experimental conditions:**

- LPE Cd0.2Hg0.8Te;
- Hg-rich anneal, 260–350 °C;
- 8 h dwell;
- fixed Hg vapor pressure;
- quench versus gradual cooling over about 200 min.

**Direct result:** final electrical properties depend strongly on cooldown procedure. Quenched samples show strong anneal-temperature dependence and p→n conversion near 300 °C, while gradually cooled samples were n-type across the tested temperature range.

**Interpretation:** Hg-vacancy annihilation continues during gradual cooling because Hg diffusion remains rapid enough.

**Restriction:** x=.20 and specific apparatus. Do not transplant 8 h or 200 min into RP-01.

**Procedure:** `procedures/P04B_HG_ANNEAL_COOLDOWN_TRAJECTORY_QUALIFICATION.md`.

## S-R9-07 — Jones, Quelch, Capper, Gosney — isothermal/two-temperature annealing

**Class:** Primary-A  
**Citation:** C. L. Jones, M. J. T. Quelch, P. Capper, J. J. G. Gosney, “Effects of annealing on the electrical properties of CdxHg1−xTe,” *Journal of Applied Physics* 53, 9080–9092 (1982).  
**DOI:** `10.1063/1.330419`

**Composition range:** approximately x=0.17–0.31.

**Key findings:**

- both closed-tube and open-tube anneals studied;
- Hg vapor pressure controlled with a Hg reservoir;
- isothermal sample/reservoir conditions convert native-defect p-type material to n-type;
- lower-reservoir-temperature/two-temperature closed-tube anneals can convert n-type to p-type, with acceptor concentration controlled by sample T and Hg pressure;
- two-temperature open-tube anneals also produce n→p behavior; in the reported range Hg pressure strongly affects the time to reach equilibrium even where final acceptor concentration is comparatively pressure-insensitive.

**Role:** primary reason to log sample temperature and Hg-reservoir temperature separately throughout dwell/cooldown.

## S-R9-08 — Astles et al. 1992 — very low background n after Hg-rich anneal

**Class:** Primary-A  
**Citation:** M. G. Astles, N. Shaw, G. Blackmore, R. Hall, “Improved control of composition and electrical properties of liquid phase epitaxial (CdHg)Te layers,” *Journal of Crystal Growth* 117, 213–217 (1992).  
**DOI:** `10.1016/0022-0248(92)90747-7`

**Direct abstract-level results:**

- Te-rich LPE at ~460 °C;
- powdered HgTe Hg source;
- Hg loss ~0.3 mg/min;
- absorption-edge reproducibility ±0.15 µm;
- thickness reproducibility ±1 µm for ~20-µm layers;
- depth-composition gradient `(2–4)×10^-4 x/µm`;
- undoped background carrier concentration after Hg-rich anneal `n≈(6–8)×10^13 cm^-3`.

**Role:** evidence that very low background n-type states are physically achievable after Hg-rich vacancy removal in Te-rich LPE material.

**Restriction:** exact x/anneal path not established as RP-01-compatible from accessible abstract; do not use 6–8e13 as RP-01 target.

## S-R9-09 — Chandra, Schaake, Kinch 2003 — x-dependent low-T anneal kinetics

**Class:** Primary-A  
**Citation:** D. Satish Chandra, H. F. Schaake, M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *Journal of Electronic Materials* 32, 810–815 (2003).  
**DOI:** `10.1007/s11664-003-0075-5`

**Role:** reinforces that low-temperature anneal kinetics depend strongly on x, vacancy concentration and T and slow with increasing Cd fraction. For x≳0.26, incomplete metal-vacancy ionization at 77 K complicates purely electrical inference of defect state.

**Round-9 implication:** Kawazu x=.20 diffusion/cooldown time scales are illustrative only; local x≈.30 kinetics must be qualified.

## Round-9 derived diffusion scale [D]

Using Kawazu's stated `D_Hg >~1×10^-9 cm²/s` as a lower-bound illustrative scale:

- 200 min gives `sqrt(Dt) >~34.6 µm`;
- 9.5-µm diffusion time `L²/D` at 1e-9 cm²/s is ~902 s ≈15 min.

These are not production times. They demonstrate only that cooldown can remain chemically active across a 9.5-µm RP-01-like layer.

## Round-9 central conclusions

1. P03 growth temperature must be referenced to the **actual local liquidus**, not only nominal 507 °C/controller temperature.
2. P07 final substrate preparation is controlled by removed depth + final surface state + clean-to-load history, not Br2 concentration/time alone.
3. P04 anneal cooldown is a thermodynamic/kinetic process stage; sample and reservoir temperature trajectories must be recorded separately.
4. Final material acceptance remains multivariate: Hall/multicarrier + FTIR/x/thickness + morphology + lifetime/device proxy.
