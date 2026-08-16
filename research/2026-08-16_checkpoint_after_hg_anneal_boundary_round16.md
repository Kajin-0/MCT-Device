# Recovery checkpoint — round 16 Hg-anneal state boundary / Jacobian

**Date:** 2026-08-16 America/New_York

**Purpose:** Fast handoff after formalizing the second high-value empirical P20 block.

Read after `AGENTS.md`, then round-15 and round-14 checkpoints for P22/P21 context.

---

## 1. New files

Round 16 adds:

- `calculations/RP01_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN.md`
- `procedures/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_QUALIFICATION.md`
- `travelers/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND16.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND16.md`
- this checkpoint.

No new historical RP-01/Fermionics anneal setpoint is claimed.

---

## 2. Main conceptual result

The anneal mapping is not one globally differentiable response surface.

Correct architecture:

`anneal trajectory -> carrier-state boundary/class -> local continuous response inside stable region -> detector performance`.

The process-history input is

`{T_s(t),T_Hg(t),pHg(t),dwell,cooldown,initial state}`.

The output includes

`{carrier class, Hall/multicarrier state, mu_H,optical preservation,tau_eff}`.

---

## 3. Two-carrier Hall boundary

For the classical low-field two-carrier model,

`R_H = (p mu_h^2 - n mu_e^2) / {q(p mu_h+n mu_e)^2}`.

Therefore Hall sign changes at

`p mu_h^2 = n mu_e^2`,

not `p=n`.

Because electron and hole mobilities can differ greatly, Hall sign is mobility weighted.

---

## 4. Apparent Hall-density singularity

The one-carrier apparent Hall-density magnitude is

`N_H,app=1/(q|R_H|)`.

Thus it diverges as `R_H->0` even though physical carrier populations remain finite.

Permanent rule:

**Never regress `log10(n_H)` through the p/n Hall-sign transition.**

Boundary identification uses signed Hall/tensor information.

`log10(n_H)` and `mu_H` are local responses only inside a verified single-carrier n-like region.

---

## 5. Three transport-state labels

P23 uses:

- `N-LIKE`;
- `P-LIKE`;
- `TRANSITION/MULTICARRIER`.

Do not force ambiguous Hall data into a binary p/n label.

State classification must retain:

- measurement temperature;
- field range;
- uncertainty;
- Hall curvature;
- MR;
- P05 single-carrier validity result.

---

## 6. Hybrid mathematical object

Near the transition the correct process model is

`{g(a)=0, transition uncertainty, J_n,a, J_p,a}`,

where:

- `g(a)=0` is the carrier-state boundary;
- `J_n,a` is the local Jacobian inside stable n-like material;
- `J_p,a` is the analogous p-like object if needed.

There is no meaningful single derivative of reciprocal Hall density through `g=0`.

---

## 7. Boundary margin / covariance

A process center must have margin to the transition zone.

For local boundary response `g(a)`:

`delta g ~= grad(g)^T delta a`.

With process covariance `Sigma_a`:

`u_g^2 ~= grad(g)^T Sigma_a grad(g)`

plus classifier/model uncertainty.

Thus P20 must impose both:

1. detector/material performance error budget;
2. state-boundary margin constraint.

The tighter constraint controls the eventual tolerance.

---

## 8. Non-isothermal diffusion exposure

Round 16 introduces

`Theta_D = integral D[T(t)]/L^2 dt`.

For Arrhenius

`D=D0 exp[-E_a/(kT)]`.

At constant T:

`Theta_D=D(T)t/L^2`.

Use this to compare ramp/dwell/cooldown contributions only after choosing a justified diffusion model.

Define

`f_cool,D = Theta_D,cool/Theta_D,total`.

This is a model diagnostic, not a release criterion.

---

## 9. Diffusion boundary-condition factor remains open

Late-time 1-D slab relaxation can be represented

`Delta c_bar(t)/Delta c_bar(0) ~ exp[-lambda_1^2 Theta_D]`.

Examples:

- two fixed-concentration surfaces: `lambda_1=pi`;
- one fixed surface + one no-flux surface: `lambda_1=pi/2`.

Hence characteristic time differs by a factor of 4 between these simple cases.

Do not use a precise `L^2/D` coefficient until the actual epilayer boundary condition is established.

---

## 10. Moving-equilibrium model

For a scalar state variable:

`dy/dt=[y_eq(T,pHg,...)-y]/tau_y(T,pHg,...)`.

Under constant conditions:

`y=y_eq+(y0-y_eq)exp(-t/tau_y)`.

Different outputs may have different `tau_y`.

A 2023 x≈.29 MBE nitrogen-anneal paper gives cross-family evidence that carrier concentration and mobility can approach equilibrium with distinct kinetics and that cooling time changes the final electrical state.

Restriction: no reported value from that branch is transferred to RP-01.

---

## 11. P23 sequential architecture

### Stage 0

Qualify:

- thermometry/lag;
- pHg/source-state reconstruction;
- P05 repeatability/multicarrier capability;
- P06 pre/post repeatability;
- matched initial-state strategy.

### Stage 1

Locate the p/transition/n boundary using signed Hall/tensor information and information-efficient boundary sampling.

### Stage 2

Choose a candidate center safely inside n-like material and estimate local derivatives of:

- `log10(n_H)`;
- `mu_H`;
- `R_s`;
- optical edge/x preservation.

### Stage 3

Decompose dwell, cooldown and their interaction. Test diffusion exposure / relaxation models only as model candidates.

### Stage 4

Measure initial-state dependence.

### Stage 5

Carry selected annealed material through frozen device processing and correlate P05/P06 state with P13/P11/P12 outputs.

---

## 12. New source added

`docs/SOURCE_LEDGER_ADDENDUM_ROUND16.md` adds/re-emphasizes:

- Jones et al. 1982, DOI `10.1063/1.330419`;
- Kawazu et al. 1995, DOI `10.1007/BF02653061`;
- Chandra/Schaake/Kinch 2003, DOI `10.1007/s11664-003-0075-5`;
- Jin et al. 2023, DOI `10.1088/2053-1591/acdf40` as DIFFERENT-PROCESS-FAMILY model evidence only.

---

## 13. Highest-priority remaining anneal gaps

See `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND16.md`.

Highest priority:

1. local state boundary and transition-zone width;
2. local n-like `n_H/mu_H` Jacobian;
3. cooldown contribution;
4. initial-state dependence;
5. diffusion/relaxation model if it improves prediction;
6. P05 state -> P13 lifetime;
7. P05/P13 -> responsivity/noise/D*;
8. detector-defined material-state budget;
9. P20 tolerance allocation;
10. P17 capability.

---

## 14. Next logical work

The next strongest theoretical/analytical branch is the P08 blocking-contact response block:

`{RIE converted depth/profile, sheet state, lateral conversion, contact geometry, surface damage}`

`-> {minority-carrier boundary condition / sweepout, responsivity, noise, tau_eff, D*}`.

The central expected difficulty is again a hidden state variable:

- `rho_c` controls majority-carrier electrical contact quality;
- minority-carrier contact recombination/sweepout is governed by a different boundary condition, often represented by an effective `S_c`;
- `rho_c != S_c`.

A useful next round should derive a minimal photoconductor diffusion/recombination model showing how contact recombination velocity and geometry alter effective lifetime/responsivity/bandwidth, identify dimensionless groups, and define which quantities P08F must measure to invert the boundary condition without pretending TLM provides it.
