# RP-01 gap matrix addendum — round 16 Hg-anneal state-boundary / Jacobian

**Date:** 2026-08-16 America/New_York

This addendum records the remaining gaps after formalizing P23.

---

## 1. Gap matrix

| ID | Missing quantity / closure | Why it matters | Current evidence | Required closure path | Status |
|---|---|---|---|---|---|
| R16-G01 | exact RP-01/Fermionics Hg-anneal traveler | historical reproduction | process family only | direct historical source recovery or explicit local qualification | OPEN |
| R16-G02 | local p/transition/n boundary in anneal-history space | prevents process distribution crossing carrier-state transition | qualitative literature + P23 framework | matched-coupon boundary-mapping DOE | EMPIRICAL-REQUIRED |
| R16-G03 | transition/multicarrier-zone width | one-carrier `n_H` is unstable near sign reversal | P05 physics + two-carrier identity | repeated P05 tensor measurements + process repeats | EMPIRICAL-REQUIRED |
| R16-G04 | `partial log10(n_H)/partial T_dwell` in stable n-like region | temperature tolerance allocation | none local | P23 local DOE + holdout | EMPIRICAL-REQUIRED |
| R16-G05 | `partial log10(n_H)/partial t_dwell` | dwell-time tolerance / equilibrium margin | none local | P23 local DOE + saturation test | EMPIRICAL-REQUIRED |
| R16-G06 | `partial log10(n_H)/partial pHg or muHg` | source-zone / pressure tolerance | Jones proves causal role, no local slope | calibrated source-state perturbation | EMPIRICAL-REQUIRED |
| R16-G07 | mobility Jacobian versus anneal variables | low n with poor mobility is not acceptable | literature shows separate mobility kinetics | P23 local DOE | EMPIRICAL-REQUIRED |
| R16-G08 | actual diffusion/relaxation model for x≈.30 LPE branch | trajectory compression / cooldown prediction | activated-diffusion evidence only | fit/validate full-trajectory data | MODEL-OPEN |
| R16-G09 | `D_eff(T,x,state)` or equivalent kinetic parameter | compute `Theta_D` quantitatively | cross-family values only | local direct/indirect kinetic inference | EMPIRICAL-REQUIRED |
| R16-G10 | surface/substrate boundary condition for defect transport | changes first diffusion eigenmode by order-unity factors | physically unresolved | compare model predictions / depth profiling / process evidence | MODEL-OPEN |
| R16-G11 | fraction of state evolution occurring during cooldown | complete trajectory release | Kawazu proves causal role in x=.20 | matched dwell / varied cooldown | EMPIRICAL-REQUIRED |
| R16-G12 | point below which remaining cooldown is chemically negligible | defines meaningful anneal endpoint | no x=.30 local criterion | kinetic model + trajectory experiments | OPEN |
| R16-G13 | initial-state dependence | same anneal may not erase growth history | expected physically | matched coupons + multiple growth states | EMPIRICAL-REQUIRED |
| R16-G14 | pre/post P06 optical/interface preservation boundary | avoid obtaining correct Hall state by damaging composition/interface | high-T warnings exist | matched P06 maps / interface metrics | LOCAL-SPEC-OPEN |
| R16-G15 | P05 state -> P13 lifetime relation | anneal must improve detector-relevant state, not Hall alone | no local mapping | matched anneal material -> frozen devices | EMPIRICAL-REQUIRED |
| R16-G16 | P05/P13 state -> P11/P12/D* relation | determines detector-optimal n/mu/lifetime neighborhood | no local mapping | matched devices + performance correlation | EMPIRICAL-REQUIRED |
| R16-G17 | historical supplier n/mu measurement temperature | direct RP-01 numerical comparison | source omission | historical source recovery; otherwise define local 80-K spec | OPEN |
| R16-G18 | P20 detector-level material-state budget | needed before process tolerance exists | historical values are references only | define reproduction/performance requirement | LOCAL-SPEC-OPEN |
| R16-G19 | state-boundary safety margin requirement | prevents yield loss from transition overlap | framework exists, no requirement | P20/P17 allocation based on yield/performance | LOCAL-SPEC-OPEN |
| R16-G20 | anneal process covariance `Sigma_a` | boundary and output uncertainty propagation | no repeated local process | P17-compatible repeated runs | EMPIRICAL-REQUIRED |

---

## 2. New analytical closure achieved in round 16

### 2.1 Hall-sign boundary is mobility weighted

For a two-carrier low-field model,

`R_H = (p mu_h^2 - n mu_e^2)/{q(p mu_h+n mu_e)^2}`.

Therefore

`R_H=0 <=> p mu_h^2=n mu_e^2`.

This closes the conceptual error that a Hall sign reversal necessarily corresponds to `p=n`.

### 2.2 Apparent Hall density is singular at the transition

`N_H,app = 1/(q|R_H|)`

and thus diverges as the Hall numerator tends to zero.

This closes the modeling question: **do not fit one global `log10(n_H)` response surface through p→n conversion.**

### 2.3 Anneal model is hybrid

Required model object is now

`{state boundary g(a)=0, transition uncertainty, J_n,a, J_p,a}`

rather than one global Jacobian.

### 2.4 Non-isothermal diffusion exposure

For a model diffusivity `D[T(t)]`, define

`Theta_D = integral D[T(t)]/L^2 dt`.

This provides a physically meaningful trajectory descriptor for dwell/cooldown comparison while keeping its evidence class `MODEL-CONDITIONAL`.

### 2.5 Boundary-condition uncertainty retained

The slowest diffusion-mode time scale is

`tau_D=L^2/(lambda_1^2 D)`

with `lambda_1` determined by physical boundary conditions. P23 explicitly refuses to choose a one-sided or two-sided coefficient without evidence.

---

## 3. Priority order

The strongest closure sequence is:

1. qualify P05/P06/thermal/source-state metrology;
2. locate local n/p transition/multicarrier region;
3. choose candidate n-like center with margin to that boundary;
4. estimate local n-like n/mu Jacobian;
5. quantify cooldown contribution and initial-state dependence;
6. connect annealed material to P13 lifetime;
7. connect material/lifetime to P11/P12 D*;
8. allocate numerical anneal tolerances through P20;
9. establish capability through P17.

---

## 4. Do-not-infer list

Until the above gaps close, do not infer:

- that `250 C / 1 h` is the RP-01/Fermionics anneal;
- that a 77-K one-carrier Hall number equals true vacancy concentration;
- that Hall sign reversal means `n=p`;
- that very large apparent Hall density near sign reversal means physically large carrier density;
- that one diffusion coefficient from x=.20 or MBE material applies to x≈.30 LPE;
- that dwell alone determines final state;
- that an equal `T*t` product makes two trajectories equivalent;
- that reaching the historical n value while degrading mobility/lifetime is acceptable;
- that a state-boundary classifier contour has zero physical uncertainty;
- that observed process spread defines the release limits.
