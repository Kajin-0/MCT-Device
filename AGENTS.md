# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual that a competent researcher can reproduce without undocumented tribal knowledge.

Canonical first process: **RP-01**, Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository now contains the control architecture from substrate/material preparation through detector characterization, statistical release, failure analysis, requirements traceability, analytical/numerical requirements allocation, empirical-Jacobian qualification, information-optimal DOE planning, and the first hybrid state-boundary/local-Jacobian model for Hg annealing.

## Non-negotiable rules

1. Never invent a missing number. Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, or explicit derivation.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct publication, derived physics, apparatus calibration and local qualification.
4. Every critical step needs outcome metrology and a pass/fail gate.
5. Preserve negative searches, rejected inferences, corrections and source conflicts.
6. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density and measured geometry distinct.
7. Keep majority-carrier contact resistivity `rho_c` distinct from minority-carrier contact recombination velocity `S_c`.
8. Use measured fabricated geometry for field/area/D* normalization.
9. Treat passivation, post-RIE exposure, thermal cooldown and packaging as detector-process variables.
10. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
11. Specifications come from physics/performance; observed process spread does not define its own passing limits.
12. Failure diagnosis uses competing hypotheses and discriminating tests; never force one cause from one symptom.
13. Every controlled process variable should trace forward to a final detector requirement.
14. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.
15. Every numerical sensitivity or allocated tolerance must state the protected output, input variable, operating point and evidence class. `PROXY-CONDITIONAL` relations may size experiments but cannot release production specifications.
16. A tabulated equilibrium ratio such as `xS/xL` is not a local derivative `dxS/dxL`; directional secants from tie-line tables are not independent partial derivatives when other composition/temperature coordinates change simultaneously.
17. A coded DOE result does not create a physical process tolerance. Physical perturbation magnitudes require independent-run variance, apparatus control and same-regime/morphology bounds.
18. Repeated observations from one source genealogy are not independent process replicates. Source-use is sequential and must be analyzed at the correct hierarchical/repeated-measures level.
19. Never regress reciprocal Hall density through a p/n Hall-sign transition. In a multicarrier transition, apparent `1/(q|R_H|)` is singular; use signed Hall/tensor information for the boundary and local `n_H/mu_H` derivatives only inside a verified stable carrier-state region.
20. Anneal tolerances must satisfy both the detector/material performance budget and margin to the carrier-state transition/multicarrier zone. The tighter constraint controls.

## Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_hg_anneal_boundary_round16.md`

Then read:

- `research/2026-08-16_checkpoint_after_information_design_round15.md`;
- `research/2026-08-16_checkpoint_after_lpe_jacobian_round14.md`;
- `research/2026-08-16_checkpoint_after_analytical_sensitivity_round13.md`.

Current integration files:

- `procedures/P17_STATISTICAL_PROCESS_CAPABILITY_RELEASE.md`
- `travelers/P17_PROCESS_RELEASE_CAPABILITY_REGISTER.md`
- `procedures/P18_FAILURE_ANALYSIS_DIAGNOSTIC_ATLAS.md`
- `travelers/P18_FAILURE_ANALYSIS_RECORD.md`
- `procedures/P19_REQUIREMENTS_TRACEABILITY_MATRIX.md`
- `procedures/P20_ANALYTICAL_SENSITIVITY_REQUIREMENTS_ALLOCATION.md`
- `calculations/RP01_FIRST_ORDER_SENSITIVITY_MATRIX.md`
- `travelers/P20_REQUIREMENTS_ALLOCATION_REGISTER.md`
- `procedures/P21_LPE_RESPONSE_SURFACE_JACOBIAN_QUALIFICATION.md`
- `calculations/RP01_LPE_TO_SPECTRAL_JACOBIAN_FRAMEWORK.md`
- `travelers/P21_LPE_JACOBIAN_QUALIFICATION_REGISTER.md`
- `procedures/P22_INFORMATION_OPTIMAL_DOE_PLANNING.md`
- `calculations/RP01_P21_CODED_DOE_INFORMATION_DESIGN.md`
- `travelers/P22_DOE_INFORMATION_REGISTER.md`
- `procedures/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_QUALIFICATION.md`
- `calculations/RP01_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN.md`
- `travelers/P23_HG_ANNEAL_STATE_BOUNDARY_JACOBIAN_REGISTER.md`

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND14.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND14.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND15.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND16.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND16.md`

For older provenance also read round-9/8/7/6 source and gap addenda.

## Controlled module set

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP
- P06 FTIR composition/thickness
- P07 CdZnTe + P07A/P07B/P07C
- P08 RIE blocking contact + P08A–P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating
- P11 absolute radiometry
- P12 noise/PSD/NEP/D* + P12A/P12B
- P13 temporal response + P13A
- P14 lithography/CD + P14A
- P15 cryogenic package
- P16 master end-to-end traveler + blank traveler
- P17 statistical process capability/release + blank register
- P18 failure-analysis diagnostic atlas + blank failure record
- P19 requirements / physics / process traceability matrix
- P20 analytical sensitivity / numerical requirements allocation + blank allocation register
- P21 LPE response-surface / empirical-Jacobian qualification + blank qualification register
- P22 information-optimal DOE planning + blank information register
- **P23 Hg-anneal state-boundary / local-Jacobian qualification + blank register**.

## Direct RP-01 anchors — do not drift

### Material

- LPE n-HgCdTe on insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `µ=4.0×10^4 cm²/V·s`
- thickness `9.5 µm`
- supplier n/µ measurement temperature not stated.

### Contact-window RIE

- Plasma Technology parallel-plate reactor
- printed `CH4/5H2`
- total `64 sccm`
- `100 mTorr`
- `50 W`
- `60 s`
- converted density `~2.0×10^15 cm^-3`, explicitly averaged over converted thickness
- mobility `~3.3×10^4 cm²/V·s`.

P08A secondary same-lineage evidence supports `CH4:H2=1:5`; conditional split 10.6667/53.3333 sccm. Not direct historical MFC closure.

P08B: if `d_conv≈8 µm`, conditional `N_s≈1.6×10^12 cm^-2`. Use sheet/multicarrier state plus independently measured depth.

### Mask-2/passivation/metal

- resist ~`4–5 µm`
- prebake `80 °C / 30 min`
- chlorobenzene `30 min`
- pattern/develop/water rinse
- anodic oxide `800 Å`
- Cr `300 Å`
- Au `2700 Å`.

### Geometry/TLM

- nine 300×300-µm contacts
- adjacent gaps 50–400 µm in 50-µm increments
- 80-K `rho_c≈9×10^-4 Ω·cm²`
- Figures 3/5/6/7 same device
- exact selected contact pair/gap remains `OPEN` and is not uniquely invertible from published D*/noise/responsivity.

### Detector benchmark

- 80 K
- stated 60° FOV
- spectral response at 1 kHz
- representative noise field 10 V/cm
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz
- g-r plateau ~24.5 nV/√Hz
- cutoff ~4.4 µm
- BLIP D* ~`2.0×10^11 cm Hz^1/2 W^-1` at 4 µm
- QE ~70%.

Do not assume 24.5 nV/√Hz is the historical 1-kHz noise used in the spectral D* curve.

## Current material/process state

Historical Honeywell tie line:

`xL=.082, yL=.810, TL=507 °C -> historical xS≈.29`.

Derived source mass fractions Hg `.249738`, Cd `.012502`, Te `.737760`.

Historical source synthesis, charge mass/well volume, exact substrate face, final clean and exact anneal trajectory remain undisclosed, but all now have explicit local qualification paths.

### P03C/D/E

- source prep: mass closure/homogenization/material output;
- melt inventory/depletion: dimensioned geometry, source-use and Hg-loss state;
- liquidus/equilibration: actual `TL,heat`, local `ΔT_SC`, sensor/melt offset, spatial thermal field and convergence;
- temperature uncertainty derived from local process sensitivity.

### P07B/C

- select face/miscut from morphology/x/thickness/crystal quality/mobility/lifetime;
- final surface released by removed depth, morphology/chemistry proxy and clean-to-load history, not etch time alone.

### P04/P04A/P04B/P23

Cooldown is part of the Hg-stoichiometry process. Record `T_sample(t),T_reservoir(t),pHg(t)` and accept on `{carrier state,n_H/multicarrier,µ_H,optical x/edge,thickness,morphology,lifetime}`.

P23 adds the hybrid anneal model:

- first locate the `P-LIKE / TRANSITION-MULTICARRIER / N-LIKE` boundary using signed Hall/tensor information;
- only inside a verified stable n-like region fit continuous `log10(n_H)`, `mu_H`, optical and lifetime sensitivities;
- preserve initial-state dependence;
- require margin to the state boundary in addition to detector-performance tolerance.

## RIE/blocking-contact state

P08C/D/E govern source separation, reactor equivalence and multicarrier transport. The `50 W / 0.4 W cm^-2` electrode-area inference is rejected.

P08F/G require detector-level sweepout suppression without unacceptable noise/bandwidth penalty. `rho_c != S_c`.

## Frontside/passivation state

P01 x=.28 wet-mesa source: nominal 2% Br2 in3:1 EG:HBr, ~2.78 µm/min at21 °C; full primary text still does not define percentage basis.

P02 exact UWA traveler open. TI-family candidate: 0.1 M KOH /90% EG+10% DI, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å; x≈.30 lineage confirms strong surface-state/mass-transfer dependence.

P02C requires sidewall/perimeter passivation verification.

P09 historical Cr/Au 30/270 nm direct; vacuum/rates/RIE-to-metal delay locally qualified in P09A.

P14 exact resist/developer remains open; chlorobenzene supports a positive-resist undercut/lift-off mechanism class, not a product identity.

## Measurement state

P05 requires variable-field escalation when Hall curvature/sign changes/MR invalidate a one-carrier reduction. Near anneal conversion, signed Hall/tensor data are primary; reciprocal apparent Hall density is not.

P12A: later UWA work cites J. F. Siliquini's 1995 UWA PhD thesis for a custom bias-capable low-noise preamp. P12B closes local gain/noise/PSD/ENBW calibration independent of the missing historical circuit.

P13 bulk-lifetime interpretation requires low-field/bias-independence and external transfer de-embedding.

## P17 — statistical release

Engineering specification limits come from detector physics/performance, not observed process spread.

Before capability claims characterize measurement repeatability, long-term variation, stability, bias, resolution, linearity, configuration dependence and uncertainty.

Separate:

`measurement -> within-wafer spatial -> run-to-run -> source/substrate lot -> long-term tool/operator`.

P17 does not impose a generic Cpk threshold. Current end-to-end process remains below `PILOT-RELEASE` because no local repeated fabrication dataset exists.

## P18 — failure analysis

Diagnostic rule:

`signature -> competing mechanisms -> discriminating tests -> root cause -> containment/corrective action -> verification`.

Prefer raw-data reanalysis and nondestructive/reversible tests before destructive analysis. Every confirmed failure feeds P17 variance/yield/change-control records.

## P19 — requirements traceability

P19 links:

`final detector requirement -> physical characteristic -> intermediate metric -> controlling Pxx process -> P17 release -> P18 failure response`.

Requirement maturity labels:

- `HISTORICAL-REFERENCE`
- `PHYSICS-REQUIREMENT`
- `LOCAL-SPEC-OPEN`
- `LOCAL-QUALIFIED`
- `RELEASED`.

## P20 — analytical sensitivity / requirements allocation

P20 separates numerical derivatives into:

- `IDENTITY`;
- `MODEL-CONDITIONAL`;
- `PROXY-CONDITIONAL`;
- `EMPIRICAL-REQUIRED`.

Key first-order results:

### D*/NEP

`D*=R_v sqrt(A)/e_n` gives exact normalized sensitivities:

- responsivity `+1`;
- detector noise ASD `-1`;
- area `+0.5`.

### Bias/self-heating

Uniform one-carrier screening gives `P_J ∝ E^2`, so field has normalized Joule-power sensitivity `+2`.

### Composition proxy

At `x=.30, T=80 K`, Hansen gives

`partial lambda_Eg/partial x≈-33.05 um/x`,

or about `-33.1 nm` per `+0.001` x.

This is **not** detector-cutoff sensitivity. The needed production derivative is `partial lambda_response/partial x_P06`.

### 300-K background-model sensitivity

For the existing ideal 60-degree-full-cone / 4.4-um-step model:

- flux changes about `4.03%/K` near 300 K;
- about `2.06% per 0.01 um` of effective long-wave boundary;
- about `3.0% per 1 degree` of full cone angle around 60 degrees.

Therefore precision BLIP verification should use calibrated source radiance, measured spectral weighting and physical aperture/view factor rather than scalar historical shorthand.

### Bandwidth

For a validated one-pole response, `S_f3dB,tau=-1`.

To make 1 kHz lie within 1% amplitude of the low-frequency plateau requires `f_3dB >7.02 kHz` under that one-pole model. This is a model criterion, not an RP-01 bandwidth specification.

## P21 — P03/P06 empirical Jacobian

P21 formalizes the first high-value empirical block:

`{xL,yL,TL_actual,DeltaT_SC,t_contact,h_liquid/inventory,source-use,Hg-loss state}`

`-> {x_opt,thickness,uniformity,optical edge,morphology}`.

### Honeywell derivative warning

Around the candidate xL=.082/yL=.810 row, the adjacent historical directional `Delta xS/Delta xL` secants are about:

- 6.154 on the upper side;
- 3.182 on the lower side;
- 4.286 across both adjacent rows.

The tabulated ratio at the candidate row is 3.54.

Because yL and TL also change across these rows, none of these numbers is an independent `partial xS/partial xL`. Their spread only demonstrates why a local multivariable response must be measured.

### Actual supercooling

`DeltaT_SC = TL_actual - T_contact`.

Retain covariance between TL_actual and T_contact when propagating uncertainty.

### Finite-liquid state

P21 introduces the model-conditioning coordinate

`Fo_L = D_eff t_contact / h_liquid^2`

and extraction loading

`epsilon_m = m_epilayer/M_liquid,initial`.

`Fo_L=1` is **not** a released threshold; `D_eff` and the finite-reservoir transition require local validation.

### Hg-loss distinction

Track cumulative/qualified Hg-loss state separately from source-use/solute extraction. Do not use run index as if it uniquely identifies the physical mechanism.

### Sequential DOE

- Stage 0: metrology + center-run variance;
- Stage 1: `{xL,yL,DeltaT_SC}` source/phase block;
- Stage 2: `{DeltaT_SC,t_contact}` kinetic block;
- Stage 3: `{h_liquid/inventory,source-use}` finite-reservoir block with Hg loss tracked separately;
- Stage 4: holdout confirmation.

### Detector spectral bridge

Matched P06/P11 data must establish

`lambda_det = F(x_opt,d,composition_gradient,edge_metric,...)`

under a fixed detector process, temperature and cutoff convention.

Do not substitute Hansen `lambda_Eg` for this relation.

### Robust-center rule

Choose the final LPE center inside a morphology/yield feasible region and prefer lower sensitivity to realistic process covariance, not merely an exact 9.5-um/x target crossing.

No balance, temperature, timing, melt-mass or source-use tolerance is released yet.

## P22 — information-optimal P21 design

P22 closes the coded experimental-design mathematics for the first empirical Jacobian.

### Rank rule

For a full local quadratic:

- 3 factors require 10 coefficients;
- `2^3 + centers` remains rank 8 and cannot identify separate quadratic terms;
- 2 factors require 6 coefficients;
- `2^2 + centers` remains rank 5.

Center points do not de-alias individual quadratic terms.

### Stage-1 candidates

**17-run face-centered CCD + 3 centers**:

- rank 10;
- residual df 7;
- `kappa(X^T X)≈19.70`;
- internal `I_D≈0.41297`;
- linear SE multiplier `0.3162 sigma`;
- interaction `0.3536 sigma`;
- quadratic `0.6109 sigma`.

**15-run Box-Behnken + 3 centers**:

- rank 10;
- residual df 5;
- `kappa≈17.97`;
- `I_D≈0.36643`;
- linear `0.3536 sigma`;
- interaction `0.5000 sigma`;
- quadratic `0.5204 sigma`.

BBD internal D-information is about 88.7% of the FCCCD value under the same coded model basis, uses two fewer runs and avoids triple-extreme states.

Use FCCCD when cube corners are physically feasible and derivative precision dominates. Use BBD when triple extremes threaten morphology/same-regime validity.

### Stage-2 candidate

11-run 2-factor face-centered CCD + 3 centers:

- rank 6;
- residual df 5;
- `kappa≈9.50`;
- internal `I_D≈0.42835`;
- linear SE `0.4082 sigma`;
- interaction `0.5000 sigma`;
- quadratic `0.6283 sigma`.

### Derivative resolution

Define

`eta=|partial y/partial u| Delta u / sigma_y`.

One-block approximate alpha=.05 / 80%-power linear resolution:

- Stage-1 FCCCD `eta_min≈1.034`;
- Stage-1 BBD `≈1.242`;
- Stage-2 FCCCD `≈1.435`.

Thus physical perturbations must be large enough to generate resolvable response relative to independent-run sigma, while remaining inside the same physical regime.

### Sequential next-run criterion

For `M=X^T W X`, candidate row `x_c` and weight `w_c`:

`q_c=w_c x_c^T M^-1 x_c`.

Adding that run multiplies the information determinant by `1+q_c` under the assumed model. Use this only after filtering candidates through morphology, apparatus and genealogy constraints.

### Stage-3 genealogy rule

Source-use is sequential/repeated measures.

Structural floor for quadratic depth/use support:

- 3 depth levels;
- at least 2 independent charges per depth;
- at least 3 selected use states per charge;
- at least 6 independent source genealogies / 18 selected growth states.

This is a structural identifiability floor, not a power-based final sample size.

Use mixed/repeated-measures analysis. Repeated growths from one charge are not independent replicates of the depth factor.

Physical perturbation magnitudes remain OPEN.

## P23 — Hg-anneal state boundary / local Jacobian

P23 formalizes the second high-value empirical block:

`{T_s(t),T_Hg(t),pHg(t),dwell,cooldown,initial state}`

`-> {carrier-state class,n_H/multicarrier,mu_H,optical preservation,tau_eff}`.

### Hall-transition singularity

For the low-field two-carrier model:

`R_H=(p mu_h^2-n mu_e^2)/{q(p mu_h+n mu_e)^2}`.

Thus Hall sign changes at

`p mu_h^2=n mu_e^2`,

not `p=n`.

The reciprocal apparent Hall density `1/(q|R_H|)` diverges at the sign-cancellation boundary. This is a model/measurement singularity, not a physical carrier-density divergence.

### Transport-state labels

Use:

- `N-LIKE`;
- `P-LIKE`;
- `TRANSITION/MULTICARRIER`.

Boundary identification uses signed Hall slope/coefficient plus P05 curvature/MR/field/temperature checks. Never force an ambiguous transition specimen into one-carrier `n_H` regression.

### Hybrid model

The correct local object is

`{g(a)=0, transition uncertainty, J_n,a, J_p,a}`.

`log10(n_H)` and `mu_H` derivatives are estimated only inside a verified stable n-like region.

### Non-isothermal diffusion exposure

P23 introduces the model-conditioning coordinate

`Theta_D = integral D[T(t)]/L^2 dt`.

For Arrhenius diffusion,

`D=D0 exp[-E_a/(kT)]`.

This allows ramp/dwell/cooldown contributions to be compared without reducing the process to `T*t`. It remains `MODEL-CONDITIONAL` until validated locally.

Late-time slab relaxation is

`Delta c_bar/Delta c_bar0 ~ exp[-lambda_1^2 Theta_D]`,

with the factor `lambda_1` depending on the physical boundary conditions. One-sided versus two-sided simple slab models differ by a factor of four in characteristic time, so no precise coefficient is assumed without evidence.

### Cooldown fraction

`f_cool,D = Theta_D,cool/Theta_D,total`

is a diagnostic for kinetic exposure, not a release criterion. Cooldown can also move the equilibrium state, so equal diffusion exposure does not guarantee equal final material state.

### Boundary margin

For boundary response `g(a)` and process covariance `Sigma_a`:

`u_g^2 ~= grad(g)^T Sigma_a grad(g)`

plus model/classification uncertainty.

The selected anneal center must have adequate margin to the transition zone as well as meeting detector/material performance budgets.

### Downstream bridge

Selected annealed material must establish

`anneal trajectory -> P05/P06 material state -> P13 lifetime -> P11/P12 responsivity/noise/D*`.

Do not optimize Hall density independently of mobility, lifetime or detector performance.

No anneal tolerance or unique RP-01 dwell/temperature/pHg/cooldown is released yet.

## Current architecture

The repository now has eight integrated layers:

1. **P01–P16:** fabrication/material/device methods + end-to-end traveler;
2. **P17:** statistical process release/capability/change control;
3. **P18:** failure diagnosis/corrective action;
4. **P19:** final-requirement-to-process traceability;
5. **P20:** analytical/empirical sensitivity and numerical requirements allocation;
6. **P21:** local response-surface/Jacobian identification for the first high-value P03/P06 block;
7. **P22:** coded/Fisher-information experimental-design optimization;
8. **P23:** hybrid carrier-state-boundary + within-state Jacobian for Hg annealing.

Most numerical fabrication tolerances remain `LOCAL-SPEC-OPEN` because no repeated local LPE/anneal/device dataset exists yet.

## Next logical work

The P21/P22 LPE block and P23 anneal block are now analytically structured. Both require local data before numerical process tolerances can be released.

Strongest next purely analytical branch:

1. build the **P08/P10/P12/P13 blocking-contact response model**;
2. map
   `{RIE converted profile/depth, sheet transport state, lateral conversion, contact geometry, surface damage}`
   into
   `{minority-carrier sweepout boundary condition, responsivity, noise, tau_eff, D*}`;
3. derive a minimal diffusion/recombination/contact model using an effective minority-carrier surface/contact recombination velocity `S_c`;
4. prove analytically which combinations of `S_c`, diffusion length, contact spacing and bulk lifetime are identifiable from responsivity + temporal-response data;
5. preserve the rule `rho_c != S_c` — TLM majority-carrier contact resistivity cannot release the minority-carrier boundary condition;
6. then use P20/P22 to allocate blocking-contact process requirements.

Do not populate production capability/tolerance numbers without local repeated-device data.