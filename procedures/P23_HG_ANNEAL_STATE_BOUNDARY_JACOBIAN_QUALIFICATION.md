# P23 — Hg-anneal state-boundary / local-Jacobian qualification

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD / PRE-SPECIFICATION  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Identify the local transformation

`{T_sample(t), T_Hg(t), pHg(t), dwell, cooldown, initial material state}`

into

`{carrier-state class, Hall/multicarrier state, mobility, optical preservation, tau_eff/device proxy}`

for the selected x≈0.30 RP-01 material branch.

P23 is the second dedicated empirical-Jacobian module under P20.

Its central rule is that p-to-n conversion is a **state boundary**. The process must therefore be modeled as:

`state-boundary classifier + local continuous response surface inside each stable state region`,

not as one polynomial for `n_H` across the transition.

No unique RP-01 dwell, temperature, Hg pressure or cooldown trajectory is claimed.

---

## 2. Required internal references

Read before executing P23:

- P04 Hg anneal qualification;
- P04A x≈0.30 state-mapping DOE;
- P04B cooldown-trajectory qualification;
- P05 Hall/VdP metrology;
- P06 FTIR composition/thickness mapping;
- P13 temporal response/lifetime;
- P20 requirements allocation;
- P22 information-optimal DOE planning;
- `calculations/RP01_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN.md`.

P23 does not replace P04/P04A/P04B. It converts their process physics into an identifiable sensitivity/boundary architecture.

---

## 3. State labels

Every annealed sample receives one of three transport-state labels at each declared measurement temperature:

### `N-LIKE`

- signed low-field Hall response is n-like with its stated uncertainty excluding zero;
- P05 single-carrier validity checks pass over the declared fit range;
- no unresolved sign reversal/curvature invalidates the label.

### `P-LIKE`

Same logic with p-like sign.

### `TRANSITION/MULTICARRIER`

Use this label when:

- Hall sign is unresolved within uncertainty;
- Hall sign changes with field or temperature;
- Hall curvature is material;
- magnetoresistance indicates unresolved parallel/multiple channels;
- P05 single-carrier gates fail.

Do not force an ambiguous specimen into n or p for regression convenience.

---

## 4. Why `log10(n_H)` cannot be the global response

In the two-carrier low-field model,

`R_H = (p mu_h^2 - n mu_e^2) / {q[p mu_h + n mu_e]^2}`.

The Hall-sign boundary is therefore

`p mu_h^2 = n mu_e^2`.

The apparent one-carrier Hall density

`1/(q|R_H|)`

diverges as the numerator approaches zero.

Therefore:

- use signed Hall slope/coefficient/tensor information for boundary identification;
- use `log10(n_H)` only inside a verified n-like one-carrier region;
- use multicarrier/tensor models where required;
- preserve temperature and field range with every state label.

This rule prevents a mathematical singularity from being mistaken for a physical carrier-density excursion.

---

## 5. Process-history representation

The complete anneal remains trajectory defined:

`A(t) = {T_s(t), T_Hg(t), pHg(t), enclosure/source state}`.

For local DOE/modeling, reduce the trajectory only to descriptors that are physically and metrologically controlled.

Candidate descriptors include:

- dwell sample temperature;
- dwell duration;
- Hg source/reservoir temperature;
- reconstructed/qualified Hg partial pressure or chemical-potential proxy;
- cooldown exposure descriptor(s);
- sample/source temperature offset trajectory;
- initial Hall state;
- initial optical x/edge;
- epilayer thickness;
- surface/passivation state.

Do not use vague categorical labels such as `Hg-rich` or `slow cool` as numerical factors unless their physical trajectories are also retained.

---

## 6. Stage 0 — metrology and initial-state qualification

Before mapping an anneal boundary:

1. qualify sample and Hg-source temperature calibration/lag;
2. qualify the source-state / pHg reconstruction method;
3. qualify P05 repeatability and field range;
4. quantify P06 pre/post edge/thickness repeatability;
5. define matched-coupon/wafer-coordinate strategy;
6. establish independent anneal-run variance at one nominal condition where possible;
7. preserve the complete pre-anneal state vector.

Required pre-state:

`S0 = {wafer coordinate, x_opt/edge, thickness, Hall tensor state, carrier class, mu_H where valid, R_s, morphology, prior thermal history}`.

A sample without adequate `S0` is not suitable for quantitative anneal sensitivity estimation.

---

## 7. Stage 1 — find the carrier-state boundary efficiently

The first objective is not to fit precise `n_H`; it is to locate the transition region in process-history space.

Use a bounded, physically safe candidate region inherited from P04/P04A/P04B.

### 7.1 Initial coarse support

Choose coded support sufficient to test the dominant axes:

- dwell temperature;
- dwell duration;
- Hg chemical-potential/source coordinate;
- one defined cooldown coordinate.

Use P22 to reject rank-deficient/confounded designs.

### 7.2 Boundary bracketing

When two otherwise comparable conditions produce stable opposite carrier-state labels, the boundary lies between them in the chosen process coordinate only if other trajectory variables are matched.

Use additional points to narrow the boundary while retaining matched initial states.

### 7.3 Active information rule

After an initial classifier exists, candidate points should be scored for a combination of:

- high classification uncertainty / proximity to the boundary;
- reduction in parameter/posterior uncertainty;
- physical feasibility;
- optical/morphology safety;
- independence from previously sampled initial states.

Do not spend most growth/anneal samples far inside already certain p-like or n-like regions while the boundary remains poorly located.

### 7.4 Transition zone

Maintain an explicit transition/multicarrier zone around the boundary. Its width is set by:

- Hall/metrology uncertainty;
- run-to-run process variation;
- multicarrier onset;
- model uncertainty.

Do not reduce the zone to zero merely because a classifier produces a sharp mathematical contour.

---

## 8. Stage 2 — local n-like response surface

After a candidate RP-01 anneal center lies safely inside the n-like region, identify local continuous responses.

Primary n-like outputs:

- `log10(n_H)` at the declared measurement condition;
- `mu_H`;
- `R_s`;
- P06 edge/x shift;
- P06 thickness shift;
- morphology/interface metrics.

Candidate local process descriptors:

- `T_dwell`;
- `t_dwell`;
- `pHg/muHg` proxy;
- cooldown descriptor(s).

Use P22 coded-response-surface rules.

Begin with the smallest model supported by the data:

`y = beta0 + sum beta_i z_i + selected interactions + selected curvature`.

A coefficient becomes a process derivative only when:

- design rank/conditioning is adequate;
- factor variation is independently identifiable;
- holdout predictions are acceptable;
- the fitted region remains entirely inside the same carrier-state/morphology regime.

---

## 9. Stage 3 — dwell versus cooldown decomposition

P04B establishes that cooldown can materially alter the final state.

P23 therefore separates:

1. dwell contribution;
2. cooldown contribution;
3. dwell × cooldown interaction.

### 9.1 Diffusion-exposure diagnostic

Where a validated or screening diffusivity model is available, calculate

`Theta_D = integral D[T_s(t)] / L^2 dt`

and

`f_cool,D = Theta_D,cool / Theta_D,total`.

Use this as a trajectory descriptor/model diagnostic only.

Do not promote it to a complete state variable until the model predicts held-out anneal results.

### 9.2 Reduced relaxation diagnostic

For responses showing monotone saturation, test

`y(t)=y_eq + [y0-y_eq] exp(-t/tau_y)`

under fixed conditions.

Estimate separate `tau_y` for separate outputs where justified.

Do not assume Hall density, mobility, optical state and lifetime equilibrate with one common time constant.

### 9.3 Cooldown as moving-equilibrium path

A cooldown is not merely extra dwell at lower temperature because both kinetics and the equilibrium defect condition can change with `T_s(t)` and `pHg(t)`.

A scalar equivalent-time transformation is allowed only after validation against full trajectory data.

---

## 10. Stage 4 — initial-state dependence

Repeat selected anneal conditions on matched material spanning controlled pre-state differences, such as:

- nearby coupons from one growth;
- different LPE runs with matched P06 state;
- controlled differences in starting Hall/defect state.

Model

`S_final = F(anneal descriptors, S_initial)`.

If the same anneal trajectory gives systematically different final states from different initial conditions, the final traveler must either:

- constrain the incoming P03/P04 material state; or
- include a measured initial-state correction/branch.

Do not hide initial-state dependence inside residual variance.

---

## 11. Stage 5 — P05/P13 detector bridge

A material anneal is not fully qualified by Hall state alone.

Selected material from the n-like response surface shall proceed through a frozen detector process.

Correlate P05/P06 state with:

- P13 `tau_eff` / intrinsic transfer function;
- P11 responsivity;
- P12 noise / D*;
- P10 bias/self-heating behavior where relevant.

The target is a local detector-performance map

`P_detector = G(n_H, mu_H, optical state, tau_eff, ...)`.

This determines whether the historical `~9.8e14 cm^-3` / `~4e4 cm^2/Vs` neighborhood is actually the best local reproduction target under explicitly stated measurement conditions.

---

## 12. State-boundary margin as a process requirement

A selected process center shall have a quantified margin to the undesired/ambiguous carrier-state boundary.

Let the boundary be represented by a signed classifier response `g(a)` with desired n-like region `g<0` under the chosen convention.

For small process perturbations,

`delta g ≈ grad(g)^T delta a`.

If process covariance is `Sigma_a`, then local boundary-normal variance is approximately

`u_g^2 = grad(g)^T Sigma_a grad(g)`

plus model/classification uncertainty.

A candidate center is not robust if the expected process distribution substantially overlaps the transition region.

No universal sigma-margin is imposed here; P20/P17 shall set the release confidence based on detector/yield requirements.

---

## 13. Optical/morphology feasible region

Define

`Omega_A = {anneal histories that preserve required P06 optical state, thickness, morphology/interface quality and detector compatibility}`.

The state boundary and response surface shall only be used inside `Omega_A`.

Any condition that reaches the target Hall state but causes unacceptable:

- composition/edge shift;
- interface redistribution;
- thickness change;
- surface voiding/degradation;
- precipitate/dislocation damage;

is excluded from the feasible process region.

---

## 14. Holdout confirmation

Before promoting any anneal derivative or boundary model:

1. reserve process histories not used in fitting;
2. predict carrier-state class and continuous n-like outputs;
3. compare predicted versus measured state with uncertainty;
4. include at least one point near the intended process-center margin and one point challenging the boundary model;
5. repeat across independent anneal runs/material where possible.

A model that interpolates its training coupons but fails held-out trajectories remains `EMPIRICAL-PRELIMINARY`.

---

## 15. Evidence-state promotion

Use the following labels:

- `EMPIRICAL-REQUIRED` — no local derivative/boundary estimate yet;
- `EMPIRICAL-PRELIMINARY` — fitted but not independently confirmed;
- `EMPIRICAL-VERIFIED` — holdout-confirmed inside stated local range;
- `LOCAL-QUALIFIED` — integrated into a material-state process with metrology and detector confirmation;
- `RELEASED` — P17 capability/release completed.

Do not promote a cross-process literature kinetic constant directly to `EMPIRICAL-VERIFIED`.

---

## 16. Required run record

For each anneal record:

- sample/coupon ID and wafer coordinate;
- growth/source provenance;
- complete pre-anneal P05/P06 state;
- surface/passivation state;
- furnace/ampoule/chamber revision;
- sample thermometry ID/calibration;
- Hg-source ID/mass/geometry;
- `T_s(t)` raw/calibrated trace;
- `T_Hg(t)` raw/calibrated trace;
- `pHg(t)` or reconstruction/proxy version;
- dwell definition/time;
- cooldown trajectory;
- point where Hg chemical coupling changes/ends;
- post-anneal P05 raw tensor/Hall sweep;
- carrier-state label;
- n_H/mu_H only where valid;
- P06 pre/post optical/thickness result;
- morphology/interface result;
- P13/P11/P12 downstream result where applicable;
- DOE coded coordinates/model version;
- inclusion/exclusion/failure disposition.

---

## 17. Failure / invalidation conditions

Do not silently pool a run into the local Jacobian when:

- sample temperature trajectory is not known adequately;
- Hg-source/chemical-potential state is unresolved;
- the sample leaves the intended carrier-state region;
- Hall curvature/multicarrier behavior invalidates one-carrier reduction;
- pre-state is missing or materially mismatched;
- optical composition/interface shifts beyond the feasible region;
- surface/passivation state changes the Hg-exchange boundary condition;
- the anneal apparatus geometry/revision changes;
- uncontrolled quench/source isolation occurs;
- specimen damage compromises Hall/optical metrology.

Preserve such runs under P18 as boundary/failure information.

---

## 18. Current release blockers

P23 remains pre-specification until:

1. local carrier-state boundary is mapped with uncertainty;
2. transition/multicarrier zone is characterized;
3. candidate center lies safely inside the desired n-like feasible region;
4. P05 measurement repeatability/model validity is quantified;
5. local n-like `n_H/mu_H` Jacobian is holdout confirmed;
6. cooldown contribution is measured and modeled adequately;
7. initial-state dependence is bounded or incorporated;
8. optical/interface preservation is demonstrated;
9. P13/P11/P12 detector bridge is established;
10. a detector-level material-state requirement is defined;
11. P20 converts that requirement into process-state margins/tolerances;
12. P17 demonstrates capability.

---

## 19. Literature / provenance boundary

Primary and near-primary evidence supports:

- isothermal/Hg-rich conditions tending to convert native-defect p-type material toward n-type;
- Hg chemical potential as an independent state variable;
- strong x/T/vacancy dependence of low-temperature anneal kinetics;
- cooldown as a causal part of final electrical state;
- incomplete metal-vacancy ionization complicating 77-K electrical interpretation for x above about 0.26.

A 2023 x≈0.29 MBE nitrogen-anneal study additionally demonstrates, in a different process family, separate exponential-like equilibration of carrier concentration and mobility and strong cooling-time dependence.

These sources support the P23 model architecture. They do **not** supply the RP-01 process constants.

---

## 20. Next integration after P23

Once P23 is established analytically, the next highest-value unresolved branch is the blocking-contact response:

`{RIE converted profile, depth, sheet state, contact geometry}`

`-> {minority-carrier sweepout, R_v, e_n, tau_eff, D*}`.

That branch should reuse the same P20/P22 philosophy: identify state boundaries/constraints first, then local Jacobians, then requirement allocation.
