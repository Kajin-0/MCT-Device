# RP-01 Hg-anneal state-boundary / local-Jacobian framework

**Status:** CONTROLLED DERIVED CALCULATION / PRE-SPECIFICATION  
**Date:** 2026-08-16 America/New_York

## Purpose

Formalize the second high-value empirical block under P20:

`{T_sample(t), T_Hg(t), pHg(t), dwell, cooldown, initial material state}`

`-> {transport state, n_H / multicarrier state, mu_H, tau_eff, optical-edge preservation}`.

The key distinction is that p-type to n-type conversion is a **state-boundary problem**, not one globally differentiable regression problem.

This document separates:

1. the carrier-state boundary;
2. local continuous sensitivities inside a validated n-like or p-like region;
3. non-isothermal diffusion/relaxation exposure during dwell + cooldown;
4. measurement singularities near Hall-sign reversal;
5. the later P20 tolerance-allocation interface.

No RP-01 anneal temperature, dwell, Hg pressure, cooldown rate, or carrier-density tolerance is released here.

---

# 1. Process-input and state vectors

Define the anneal-history input as a trajectory-valued object

`u_A = {T_s(t), T_Hg(t), pHg(t), enclosure/source geometry, t_dwell, cooldown(t), initial state, layer thickness}`.

For local finite-dimensional response-surface work, use controlled descriptors only after the trajectory representation is frozen, for example:

`z_A = {T_dwell, t_dwell, muHg_or_pHg, cooldown descriptor(s), initial-state descriptor(s)}`.

The latent material state may include

`q = {c_VHg(z), c_interstitial(z), defect complexes, precipitate state, residual donors/acceptors, compensation, surface/interface state}`.

The measured response vector is

`m_A = {R_s(T), R_H(B,T), Hall curvature, MR(B,T), n_H/p_H where valid, mu_H, optical edge, thickness, tau_eff, morphology}`.

P23 shall not claim that any one measured Hall number uniquely equals a microscopic Hg-vacancy concentration.

---

# 2. Charge-neutrality boundary versus measured Hall boundary

A schematic charge-neutrality relation is

`p + N_D^+ = n + N_A^- + 2[V_Hg^{2-}] + ...`

where the ellipsis includes other charged defects/complexes and the actual ionization state depends on measurement temperature and Fermi level.

A simple net-doping sign can therefore be useful only inside a validated single-carrier/extrinsic regime.

The experimentally observed Hall-sign boundary is more subtle when electrons and holes coexist.

For the standard low-field two-carrier model,

`rho_0 = 1 / [q(n mu_e + p mu_h)]`

and

`R_H = (p mu_h^2 - n mu_e^2) / {q[n mu_e + p mu_h]^2}`.

Therefore the low-field Hall sign changes when

`p mu_h^2 = n mu_e^2`,

not when `p=n`.

Because electron mobility can greatly exceed hole mobility in HgCdTe, a Hall-sign boundary can occur far from equal electron and hole populations.

**Evidence class:** `MODEL-CONDITIONAL` — exact inside the classical two-carrier low-field model.

---

# 3. Apparent Hall-density singularity

The one-carrier apparent Hall-density magnitude is

`N_H,app = 1/(q |R_H|)`.

Under the two-carrier expression,

`N_H,app = (n mu_e + p mu_h)^2 / |p mu_h^2 - n mu_e^2|`.

Thus

`N_H,app -> infinity`

as

`p mu_h^2 - n mu_e^2 -> 0`.

This divergence is a **measurement-model singularity**, not a physical divergence in carrier population.

Consequences:

1. do not regress `log10(n_H)` continuously across the p/n transition;
2. do not interpret a huge apparent Hall density near sign reversal as a microscopic defect concentration;
3. near the transition, retain the raw conductivity/resistivity tensor and Hall slope/curvature;
4. use P05 multicarrier escalation when curvature/sign changes/MR demand it;
5. estimate local `n_H`/`mu_H` Jacobians only after a robust single-carrier n-like region is established.

This is a non-negotiable P23 continuity rule.

---

# 4. Carrier-state classification variable

Use the signed low-field Hall coefficient or slope as the first transport classifier, but never alone.

Define, for a declared low-field fit range,

`H_s = dV_H/dB`

or equivalently the signed `R_H` after geometry/current reduction.

A qualification state may be labeled:

- `N-LIKE`: Hall sign is n-like with uncertainty excluding zero and P05 single-carrier checks pass;
- `P-LIKE`: Hall sign is p-like with uncertainty excluding zero and P05 single-carrier checks pass;
- `TRANSITION/MULTICARRIER`: Hall sign is statistically unresolved, changes with B/T, or the P05 single-carrier checks fail.

The confidence rule is a metrology/classification rule, not a detector material specification.

For boundary modeling, define a continuous signed response such as

`g_H = R_H,low-field`

or a suitably scaled signed Hall slope.

The empirical carrier-state boundary is

`g_H(u_A) = 0`

with an explicit uncertainty band and multicarrier exclusion/transition zone.

Do not fit the boundary using the reciprocal `1/R_H`.

---

# 5. Hybrid model architecture

P23 uses two linked model classes.

## 5.1 Classification / boundary model

Estimate the process-history surface separating stable n-like from p-like/transition states.

Generic representation:

`g(u_A)=0`.

Candidate methods after data exist:

- signed-response regression on `R_H` or Hall slope;
- logistic/probit classifier for n-like probability;
- Gaussian-process classification if nonlinearity warrants it;
- physically constrained classifier with separate multicarrier state.

The method must preserve uncertainty and may not hide unresolved transition states inside a forced binary label.

## 5.2 Local continuous model inside the n-like region

Only after selecting a process center safely inside the n-like region may P23 estimate local derivatives such as

`partial log10(n_H)/partial T_dwell`,

`partial log10(n_H)/partial t_dwell`,

`partial log10(n_H)/partial muHg`,

`partial mu_H/partial T_dwell`,

`partial tau_eff/partial T_dwell`,

and cooldown sensitivities.

These derivatives are `EMPIRICAL-REQUIRED` until independently confirmed.

The valid local domain must not cross the state boundary or a multicarrier regime.

---

# 6. General defect-transport equation

A schematic one-dimensional native-defect field `c(z,t)` may be represented as

`partial c/partial t = partial/partial z [D(T,x,c,...) partial c/partial z] + R(c,T,pHg,x,...)`.

Boundary conditions are set by the actual surface/passivation/Hg chemical potential, and the substrate-side condition may differ from the free surface.

This equation is not yet a released predictive model. Its role is to prevent invalid collapse of the anneal to one scalar `time x temperature` number.

The process can be:

- diffusion limited;
- reaction/defect-complex limited;
- boundary-chemical-potential limited;
- coupled.

Which regime applies must be established locally.

---

# 7. Non-isothermal diffusion exposure

If, as a screening model, defect redistribution is governed by a diffusivity `D(T)` that is spatially uniform at each instant, define the accumulated dimensionless diffusion exposure

`Theta_D = integral D[T(t)] / L^2 dt`.

Here `L` is the relevant redistribution thickness, initially the active epilayer thickness only if that is physically justified.

For Arrhenius diffusivity

`D(T) = D0 exp[-E_a/(k_B T)]`,

`Theta_D = (D0/L^2) integral exp[-E_a/(k_B T(t))] dt`.

This integral gives a mathematically correct way, **inside the Arrhenius diffusion model**, to compare dwell and cooldown thermal histories.

At constant T,

`Theta_D = D(T)t/L^2`.

Then

`partial ln(Theta_D)/partial ln(t) = +1`

and

`partial ln D/partial T = E_a/(k_B T^2)`.

The latter shows why a narrow temperature error can have large kinetic leverage when the activated barrier is appreciable.

**Evidence class:** `MODEL-CONDITIONAL`.

No activation energy from a different HgCdTe process branch is transferred into RP-01 as a production constant.

---

# 8. First diffusion-mode relaxation factor

For a constant-equilibrium, 1-D slab diffusion problem, the late-time solution is dominated by the slowest eigenmode.

Write generically

`Delta c_bar(t)/Delta c_bar(0) ~ exp[-lambda_1^2 Theta_D]`.

The eigenvalue depends on boundary conditions.

Examples:

- two fixed-concentration surfaces: `lambda_1 = pi`, giving `tau_D = L^2/(pi^2 D)`;
- one fixed-concentration surface and one blocking/no-flux surface: `lambda_1 = pi/2`, giving `tau_D = 4L^2/(pi^2 D)`.

Because an epilayer on a substrate is not automatically a two-sided diffusion slab, P23 shall not choose the factor of 1 versus 4 without validating the physical boundary condition.

This refines the rough `L^2/D` scaling used in P04B while preserving its role as an order-of-magnitude check.

**Evidence class:** `MODEL-CONDITIONAL`.

---

# 9. Cooldown contribution fraction

Inside the same diffusion-exposure model, decompose

`Theta_D,total = Theta_D,ramp + Theta_D,dwell + Theta_D,cool`.

Define

`f_cool,D = Theta_D,cool / Theta_D,total`.

Interpretation:

- `f_cool,D << 1`: cooldown is kinetically small under the chosen diffusion model;
- appreciable `f_cool,D`: cooldown cannot be treated as inert;
- `f_cool,D` by itself does not determine the final defect state because the equilibrium boundary condition may also move during cooling.

This gives P04B a quantitative trajectory diagnostic without declaring a universal cooldown rate.

---

# 10. Moving-equilibrium / first-order relaxation model

A separate reduced model for a scalar material-state observable `y` is

`dy/dt = [y_eq(T,pHg,x,...) - y]/tau_y(T,pHg,x,...)`.

For constant conditions,

`y(t)=y_eq + [y(0)-y_eq] exp(-t/tau_y)`.

For time-varying conditions, both `y_eq` and `tau_y` can move throughout cooldown.

This model is useful for:

- testing whether an observable has approached a plateau;
- separating equilibrium value from kinetic time constant;
- demonstrating why carrier density and mobility need not share one time constant.

A 2023 x≈0.29 MBE nitrogen-anneal study reports exponential approaches of carrier concentration and mobility toward anneal-condition-dependent equilibria and finds that cooling duration materially changes the electrical state. This is strong **cross-process model evidence**, not an Hg-rich LPE RP-01 recipe.

**Evidence class:** `MODEL-CONDITIONAL / DIFFERENT-PROCESS-FAMILY`.

---

# 11. No universal time-temperature equivalence

Two anneal trajectories with equal

`T_dwell x t_dwell`

or equal conventional thermal budget need not be equivalent because:

1. `D(T)` is nonlinear/activated;
2. `pHg` or Hg chemical potential changes the equilibrium defect state;
3. sample and Hg reservoir temperatures can follow different trajectories;
4. cooldown can continue defect redistribution;
5. different observables can have different time constants;
6. passivation/surface conditions can change boundary exchange;
7. precipitate/defect-complex evolution can add separate kinetics.

Therefore the full `T_s(t), T_Hg(t), pHg(t)` trajectory remains the primary process record.

---

# 12. Initial-state dependence

The final state is not expected to be a function of anneal history alone.

Write

`m_final = F(u_A, m_initial, q_initial)`.

At minimum preserve pre-anneal:

- P06 `x_opt`, edge and thickness;
- P05 carrier sign/Hall tensor state/mobility;
- growth-run/wafer coordinate;
- any prior thermal exposure;
- surface/passivation state;
- morphology.

Matched-coupon comparisons are therefore substantially more informative than unrelated-wafer comparisons.

---

# 13. Optical-preservation constraint

The anneal optimization is constrained by

`Delta lambda_edge`, `Delta x_opt`, `Delta d`, morphology/interface state.

A condition that achieves the desired n-like transport state but causes an unwanted composition/interface shift is outside the feasible region.

Define

`Omega_A = {anneal histories: transport target reachable AND optical/morphology gates pass}`.

The carrier-state boundary and local Jacobian are meaningful only inside this feasible domain.

---

# 14. Lifetime/device bridge

After material-state mapping, selected matched material shall proceed through a frozen downstream detector process so P13 can establish

`tau_eff = G(annealed material state, E, T_detector, interfaces, contacts, ...)`.

Do not assume that lower Hall density automatically increases detector lifetime or D*.

The anneal output must ultimately be judged against downstream:

- responsivity;
- noise;
- `tau_eff` / intrinsic bandwidth;
- D*;
- stability.

Thus the later chain is

`anneal trajectory -> material state -> detector dynamics/performance`.

---

# 15. P20 Jacobian structure

Inside a verified n-like local region, define material-state vector

`m_n = {log10(n_H), mu_H, R_s, tau_eff, lambda_edge, ...}`

and process descriptor vector

`a = {T_dwell, t_dwell, muHg/pHg, cooldown descriptors, initial-state descriptors}`.

The local anneal Jacobian is

`J_n,a = partial m_n / partial a`.

Near the state boundary, replace this with a hybrid object:

`{boundary surface g(a)=0, transition uncertainty, within-state Jacobians J_n,a and J_p,a}`.

There is no physically defensible single derivative of `log10(n_H)` through the boundary.

---

# 16. Tolerance-allocation consequence

P20 may convert an allowed material-state budget into a process tolerance only when:

1. the selected center is safely inside the desired state region;
2. the local derivative is experimentally verified;
3. the allowed perturbation does not cross `g(a)=0` or leave `Omega_A`;
4. trajectory/metrology covariance is included;
5. detector-level sensitivity to the resulting material state is known.

Therefore any anneal tolerance must satisfy both

`performance/error budget`

and

`state-boundary margin`.

The tighter constraint wins.

---

# 17. Highest-value unresolved quantities

1. local boundary location in `{T_dwell,t_dwell,pHg/cooldown,initial state}`;
2. local n-like derivatives of `log10(n_H)` and `mu_H`;
3. actual trajectory-dependent `D_eff` or reduced kinetic model, if useful;
4. cooldown contribution to final state;
5. relation between P05 transport state and P13 `tau_eff`;
6. detector-level optimum n/mu/lifetime region;
7. optical/interface-preservation boundary;
8. source/passivation dependence of Hg exchange.

All remain `EMPIRICAL-REQUIRED` unless explicitly promoted by later data.

---

# 18. Sources / internal interfaces

- P04 `HG_ANNEAL_QUALIFICATION`.
- P04A `X030_HG_ANNEAL_STATE_MAPPING_DOE`.
- P04B `HG_ANNEAL_COOLDOWN_TRAJECTORY_QUALIFICATION`.
- P05 `HALL_VDP_MATERIAL_METROLOGY`.
- P06 `FTIR_COMPOSITION_THICKNESS_MAPPING`.
- P13 `TEMPORAL_FREQUENCY_RESPONSE_LIFETIME`.
- P20 `ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION`.
- Jones et al., *J. Appl. Phys.* 53, 9080–9092 (1982), DOI `10.1063/1.330419`.
- Kawazu et al., *J. Electron. Mater.* 24, 1113–1117 (1995), DOI `10.1007/BF02653061`.
- Chandra, Schaake, Kinch, *J. Electron. Mater.* 32, 810–815 (2003), DOI `10.1007/s11664-003-0075-5`.
- D. Jin et al., *Materials Research Express* 10, 076302 (2023), DOI `10.1088/2053-1591/acdf40` — different MBE/nitrogen process family; model/kinetic evidence only.
