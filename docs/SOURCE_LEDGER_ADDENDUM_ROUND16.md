# Source ledger addendum — round 16 Hg-anneal state-boundary / Jacobian

**Date:** 2026-08-16 America/New_York

This addendum records the sources used to formalize P23. It does not close the historical RP-01/Fermionics anneal recipe.

---

## S-R16-01 — Jones et al. 1982: Hg chemical potential and carrier-state control

**Class:** Primary-A  
**Citation:** C. L. Jones, M. J. T. Quelch, P. Capper, J. J. G. Gosney, “Effects of annealing on the electrical properties of CdxHg1−xTe,” *Journal of Applied Physics* 53, 9080–9092 (1982).  
**DOI:** `10.1063/1.330419`

### Relevant direct findings

For approximately x=0.17–0.31 HgCdTe:

- both closed-tube and open-tube annealing were investigated;
- Hg vapor pressure was controlled using a reservoir;
- isothermal reservoir/sample conditions convert native-defect p-type material toward n-type;
- two-temperature conditions can produce/retain p-type states;
- Hg vapor pressure can control final acceptor state and/or time to equilibrium depending on architecture.

### Round-16 use

This source supports treating:

`{T_sample, T_Hg/pHg}`

as independent state variables and supports the existence of an anneal-state boundary in temperature–Hg-chemical-potential space.

### Restriction

The paper does not provide the RP-01/Fermionics x≈0.30 production traveler. No numerical pressure/temperature boundary is transferred directly into P23.

---

## S-R16-02 — Kawazu et al. 1995: cooldown is causal

**Class:** Primary-A  
**Citation:** Z. Kawazu, S. Ochi, T. Sonoda, S. Takamiya, “Effect of Cooling Procedure After Annealing on Electrical Properties of Cd0.2Hg0.8Te Epitaxial Films Grown by Liquid Phase Epitaxy,” *Journal of Electronic Materials* 24, 1113–1117 (1995).  
**DOI:** `10.1007/BF02653061`

### Direct experimental branch

- LPE x=0.20 HgCdTe;
- Hg-rich anneal;
- quench versus gradual cooldown;
- final electrical properties depended strongly on cooling procedure.

### Round-16 use

Supports the P23 rule:

`State_final != F(dwell point only)`.

Cooldown must remain part of the controlled `T_sample(t),pHg(t)` trajectory.

### Restriction

The published x=.20 dwell/cooldown durations and temperatures are not transferred as x≈.30 RP-01 values.

---

## S-R16-03 — Chandra, Schaake, Kinch 2003: composition-dependent activated anneal kinetics

**Class:** Primary-A  
**Citation:** D. Satish Chandra, H. F. Schaake, M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *Journal of Electronic Materials* 32, 810–815 (2003).  
**DOI:** `10.1007/s11664-003-0075-5`

### Direct abstract-level findings

The low-temperature anneal kinetics were investigated as functions of:

- vacancy concentration;
- CdTe mole fraction x;
- temperature.

The reported annealing rate decreases with increasing x over approximately x=0.15–0.5 and resembles a composition-dependent activated-diffusion process.

The work also explicitly warns that incomplete ionization of metal vacancies at 77 K introduces electrical-measurement ambiguity for x above approximately 0.26.

### Round-16 use

Supports:

- keeping x in the kinetic model;
- using Arrhenius/diffusion exposure only as `MODEL-CONDITIONAL`;
- not transferring x=.20 time scales into x≈.30;
- not interpreting one low-temperature Hall number as exact vacancy concentration.

### Restriction

No activation coefficient or kinetic constant from this work is promoted into the RP-01 local model without validation.

---

## S-R16-04 — Jin et al. 2023: separate electrical-state relaxation and cooling dependence

**Class:** Primary-A / DIFFERENT-PROCESS-FAMILY  
**Citation:** D. Jin, S. Zhou, L. Chen, C. Lin, L. He, “Impact of nitrogen annealing on the electrical properties of HgCdTe epitaxial films,” *Materials Research Express* 10, 076302 (2023).  
**DOI:** `10.1088/2053-1591/acdf40`

### Direct branch

- MBE-grown HgCdTe;
- average x≈0.29;
- epilayer approximately 4–6 µm;
- CdTe passivation;
- nitrogen annealing rather than the intended RP-01 Hg-rich anneal.

The study reports:

- carrier concentration evolving toward an anneal-condition-dependent equilibrium;
- mobility also evolving toward equilibrium with a separate characteristic response;
- cooling duration materially affecting carrier concentration and mobility;
- an Arrhenius-type equilibrium analysis with a fitted activation energy of 0.63 eV under the nitrogen-anneal branch.

### Round-16 use

This is valuable **model-architecture evidence** because it demonstrates near-composition-matched HgCdTe can require more than one electrical-state time constant and that cooling remains active.

It supports testing reduced models such as

`y(t)=y_eq+[y0-y_eq]exp(-t/tau_y)`

separately for each observable.

### Restrictions

- MBE, not the RP-01 LPE lineage;
- nitrogen, not the intended controlled Hg-rich chemical-potential branch;
- passivated surface/boundary condition differs;
- `0.63 eV` is **not** assigned as the RP-01 Hg-diffusion/anneal activation energy;
- no reported time constant becomes an RP-01 setpoint.

---

## S-R16-05 — P05 two-/multicarrier transport framework

**Class:** Controlled internal measurement framework backed by same-lineage HgCdTe variable-field literature.

P05 requires:

- current and field reversal;
- symmetric field sweeps;
- Hall linearity checks;
- magnetoresistance review;
- multicarrier escalation when curvature/sign changes occur.

### Round-16 analytical consequence

For the standard low-field two-carrier model,

`R_H = (p mu_h^2 - n mu_e^2) / {q[p mu_h+n mu_e]^2}`.

Therefore the Hall-sign boundary is mobility weighted:

`p mu_h^2 = n mu_e^2`.

This is the reason P23 models the boundary using signed Hall/tensor quantities rather than apparent reciprocal Hall density.

---

## Round-16 central conclusions

1. **Carrier conversion is a boundary problem.** A global `log10(n_H)` regression across p→n is invalid because apparent one-carrier Hall density becomes singular near Hall-sign cancellation.
2. **Hg chemical potential is independent of sample temperature.** Preserve sample and reservoir/source trajectories separately.
3. **Cooldown is part of the anneal.** Use full trajectories, with diffusion/relaxation exposure as model diagnostics rather than assuming inert cooldown.
4. **Kinetic constants are composition/process-family dependent.** Cross-family constants may motivate models but do not become RP-01 setpoints.
5. **Different observables can equilibrate differently.** Hall density, mobility, optical state and lifetime must not be forced into one time constant.
6. **P20 allocation requires both a performance-error budget and a state-boundary margin.** The tighter constraint controls the eventual process tolerance.
