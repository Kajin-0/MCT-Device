# Source ledger addendum — round 14 LPE Jacobian / requirements allocation

**Date:** 2026-08-16 America/New_York

This addendum records the primary sources used to formalize the P03/P06 empirical Jacobian campaign. No new historical RP-01 setpoint is promoted in this round.

## S-R14-01 — Bowers-Schmit Honeywell Te-rich tie-line table

**Class:** Primary patent / same upstream Honeywell process family  
**Citation:** J. E. Bowers and J. L. Schmit, U.S. Patent 4,317,689, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution” (1982).

**Directly used facts:**

- Te-rich horizontal-slider HgCdTe growth under a covered graphite boat;
- HgTe/HgTe+Te auxiliary Hg source concept;
- growth near 500 C after taking the source above liquidus and then below liquidus;
- step cooling, slow cooling or combination allowed;
- tie-line table:
  - xL=.100, yL=.825, TL=508 C -> xS=.40;
  - xL=.095, yL=.820, TL=508 C -> xS=.37;
  - xL=.082, yL=.810, TL=507 C -> xS=.29;
  - xL=.060, yL=.800, TL=510 C -> xS=.22;
  - xL=.050, yL=.800, TL=499 C -> xS=.195.

**Round-14 derived diagnostic:** adjacent directional secants around xL=.082 give apparent `Delta xS/Delta xL` values about 6.154 on the upper side, 3.182 on the lower side and 4.286 across the two adjacent rows. These are not partial derivatives because yL and TL change simultaneously.

**Restriction:** the tabulated `xS/xL=3.54` at the candidate row is a ratio, not a locally measured derivative.

**Files:**

- `calculations/RP01_LPE_TO_SPECTRAL_JACOBIAN_FRAMEWORK.md`
- `procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`

## S-R14-02 — Sanz-Maudes et al. finite-liquid / Hg-loss HgCdTe LPE model

**Class:** Primary-A / HgCdTe Te-rich slider-LPE theory validated against experiment  
**Citation:** J. Sanz-Maudes, J. Sangrador, T. Rodriguez, A. Pernichi, C. Gonzalez, “Numerical simulation of the growth of HgCdTe layers by liquid phase epitaxy from Te-rich solutions: The effect of liquid dimensions and mercury loss,” *Journal of Crystal Growth* 106, 303-317 (1990).  
**DOI:** `10.1016/0022-0248(90)90076-W`.

**Direct abstract-level findings used:**

- diffusion-based model of Te-rich slider HgCdTe LPE;
- includes density changes, Hg loss, moving interface and finite liquid dimensions;
- treats step cooling, ramp cooling and supercooling;
- short-time no-Hg-leak behavior is broadly consistent with diffusion-limited LPE theory except for composition profile;
- beyond a characteristic time related to liquid thickness, growth rate decreases because the finite liquid reservoir matters;
- Hg loss drives grown material toward higher Cd composition;
- Hg-loss effect can be especially pronounced in step-cooling/supercooling cases with small cooling rates;
- known liquid dimensions and Hg-loss flux are required inputs for meaningful simulation.

**Round-14 use:** motivates explicit control/recording of effective liquid depth, source-use/depletion and Hg-loss state and the model-conditioning coordinate `Fo_L=D_eff t/h_liquid^2`.

**Restriction:** no numerical `D_eff`, finite-liquid threshold or Hg-loss flux is transplanted without full local validation.

## S-R14-03 — Harman Te-rich phase/growth study

**Class:** Primary-A / HgCdTe Te-rich horizontal-slider LPE  
**Citation:** T. C. Harman, Te-rich Hg-Cd-Te liquidus/solidus and horizontal-slider LPE study, *Journal of Electronic Materials* 9 (1980).  
**DOI:** `10.1007/BF02822728`.

**Previously controlled role:**

- measured Te-rich liquidus isotherms over a broad temperature range;
- horizontal-slider growth under flowing hydrogen;
- source/supercooling/substrate state materially affect growth;
- order-hour source equilibration benchmark in Harman's different apparatus.

**Round-14 role:** reinforces that a validated ternary equilibrium model can support the Jacobian campaign, but does not supply independent local partial derivatives for the Honeywell xL=.082/yL=.810 apparatus.

## S-R14-04 — Jovic et al. composition-profile model

**Class:** Primary-A / Te-rich HgCdTe LPE model + experiment  
**Citation:** V. Jovic, Z. Djuric, Z. Jaksic, W. M. Popovic, “Composition profiles of (Hg,Cd)Te liquid phase epitaxy layers grown from Te-rich solution,” *Journal of Crystal Growth* 143, 176-183 (1994).  
**DOI:** `10.1016/0022-0248(94)90053-1`.

**Direct abstract-level role:** for layers with x<=0.3, composition profiles arise from non-constant-temperature crystallization of the ternary solid solution and interdiffusion between substrate and growing layer; the model applies to step cooling, supercooling and equilibrium cooling.

**Round-14 implication:** mean x alone is insufficient. P21 preserves depth/composition-gradient information from P06 when identifiable and does not assume one scalar composition fully defines detector spectral response.

## S-R14-05 — general LPE growth-process caution

**Class:** Primary review/theory in *Journal of Crystal Growth*  
**Citation:** “The physical processes occurring during liquid phase epitaxial growth,” *Journal of Crystal Growth* 27, 35-48 (1974), DOI `10.1016/S0022-0248(74)80048-5`.

**Role:** diffusion models can predict growth-rate/time behavior in appropriate regimes, but hydrodynamics, thermal/solutal fields, interface kinetics and morphology complicate universal transfer of a single time law.

**Round-14 restriction:** P21 therefore does not pre-impose `d proportional t`, `sqrt(t)` or `t^(3/2)` over the entire local HgCdTe process range.

## Round-14 central conclusions

1. The next missing object is a local multivariable Jacobian, not another isolated recipe number.
2. The Honeywell table cannot independently identify `partial xS/partial xL`, `partial xS/partial yL` or `partial xS/partial T`.
3. Finite-liquid geometry and Hg loss must be explicit state variables in any transferable local response model.
4. Material response must retain composition/thickness spatial and depth-profile information before it is connected to P11 detector cutoff.
5. No production tolerance is released in this round.
