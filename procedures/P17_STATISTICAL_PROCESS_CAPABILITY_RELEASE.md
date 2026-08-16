# P17 — Statistical process capability, release and change control

**Status:** CONTROLLED QUALIFICATION / RELEASE FRAMEWORK.

## 1. Purpose

Define how repeated RP-01 qualification data are converted into:

- defensible engineering specification limits;
- measurement-system capability;
- statistical process windows;
- run/lot release criteria;
- process capability metrics;
- change-control and requalification rules.

P17 is the bridge between a collection of qualified Pxx procedures and a future end-to-end `REPRODUCIBLE-RELEASE`.

## 2. Central rule: specifications and process spread are different

Do not set acceptance limits by taking the observed mean ± an arbitrary number of standard deviations from a few successful runs.

Engineering specification limits must come from:

- detector physics;
- downstream process compatibility;
- system/performance requirements;
- historical RP-01 reference values where sufficiently defined;
- demonstrated correlation between intermediate material/process metrics and final detector performance.

Only after the specification is independently justified may process capability be evaluated against it.

## 3. NIST statistical/metrology basis

NIST/SEMATECH guidance defines process capability as comparison of a **stable/in-control process** with specification limits.

For an approximately normal stable process, the basic two-sided capability form is

`Cp = (USL - LSL)/(6 s_within)`.

Centering is included through

`Cpk = min[(USL - mean)/(3 s_within), (mean - LSL)/(3 s_within)]`.

Use these only when their assumptions are appropriate.

NIST measurement-process guidance requires characterization of:

- repeatability;
- reproducibility / long-term variability;
- stability/drift;
- bias;
- resolution;
- linearity;
- gauge/operator/configuration effects;
- uncertainty.

A process capability number computed from measurements whose uncertainty is a large fraction of the specification width is not a credible detector-process capability claim.

## 4. No universal Cpk release threshold is inserted here

P17 does **not** hard-code a generic `Cpk >= 1.33`, `1.67`, or other conventional manufacturing rule.

The required capability level depends on:

- detector yield objective;
- cost of false accept/reject;
- downstream sensitivity;
- destructive versus nondestructive measurement;
- whether the output distribution is normal/stationary;
- whether the metric is a screening parameter or a final performance parameter.

A numerical capability requirement may be added only with a documented program/system rationale.

## 5. Measurement system must pass before process capability

For every critical response `Y`, characterize the measurement process before using `Y` for SPC/capability.

Examples:

- P06 thickness / edge / inferred x;
- P05 sheet resistance, Hall density, mobility;
- P01 etch depth/undercut;
- P02 oxide thickness/formation voltage;
- P08 conversion depth / sheet transport;
- P09 TLM contact resistivity;
- P11 responsivity;
- P12 noise ASD / D*;
- P13 bandwidth/time constant.

## 6. Measurement-system study

At minimum characterize:

### Repeatability

Repeated measurements under the same short-term conditions.

Estimate:

`s_repeat`.

### Reproducibility / long-term variation

Repeat across relevant:

- days;
- operators;
- sample remounts;
- instrument startups;
- calibration cycles;
- instrument units where multiple exist.

Estimate long-term components rather than assuming same-day repeatability dominates.

### Bias

Where a traceable/reference artifact exists, estimate systematic measurement bias and uncertainty.

### Resolution

Record actual useful resolution, not merely display digits.

### Linearity

Where applicable, verify response across the full process/specification range.

### Geometry/configuration dependence

Examples include:

- Hall-contact geometry;
- FTIR beam position/incidence;
- profilometer step geometry;
- LBIC illumination side/wavelength;
- TLM contact dimensions;
- noise source impedance/gain configuration.

## 7. Measurement uncertainty versus specification width

For response `Y` with specification width

`W_spec = USL - LSL`,

report the ratio

`r_U = U_Y / W_spec`

using the stated uncertainty convention/coverage.

P17 does not prescribe one universal allowable `r_U`.

The release decision must document how measurement uncertainty affects false accept/reject risk.

Where `r_U` is not small enough for a clear process decision, improve metrology or widen/redefine the engineering specification only if detector physics permits; never hide the issue by ignoring uncertainty.

## 8. Variance hierarchy for HgCdTe processing

Separate at least the following variance scales where the data structure permits:

1. measurement repeatability;
2. within-device / within-site repeatability;
3. within-wafer spatial variation;
4. wafer-to-wafer / run-to-run variation;
5. source-charge / substrate-lot variation;
6. long-term tool drift;
7. operator/setup variation.

A single pooled standard deviation can conceal the dominant physical mechanism.

Use nested or mixed-effects analysis when appropriate.

## 9. Spatial data are not independent replicate runs

P06 may generate 9-point, 5×5 or denser maps.

Do **not** treat every point on one wafer as an independent process replicate when estimating run-to-run capability.

Separate:

- wafer mean;
- within-wafer spatial sigma/range/gradient;
- run-to-run mean variation.

For a mapped variable `Y_ij` at run `i`, site `j`, a useful conceptual model is

`Y_ij = mu + Run_i + Spatial_ij + Measurement_ij`.

Extend with substrate/source/tool effects where needed.

## 10. Core upstream material capability vector

A candidate qualified LPE/anneal process should track at minimum:

`Y_material = {mean thickness, thickness nonuniformity, mean optical x/edge, x/edge nonuniformity, carrier type, n_H/multicarrier state, µ_H, morphology/usable area, lifetime proxy}`.

The process is not capable merely because the mean x is correct.

## 11. Candidate intermediate process capability vectors

### P01 mesa

`Y_mesa = {etch depth, lateral undercut, CD bias, roughness, isolation completeness}`.

### P02 passivation

`Y_pass = {oxide thickness, formation/voltage-time signature, sidewall/perimeter performance, noise/lifetime impact}`.

### P08/P09 contact

`Y_contact = {R_sheet/transport decomposition, d_conv, L_conv, d_etch, rho_c, sweepout metric, noise impact, bandwidth impact}`.

### Final detector

`Y_detector = {R(E,lambda,f), e_n(f), NEP, D*, cutoff/response edge, bandwidth/tau_eff, stability}`.

## 12. Engineering limits shall be correlated to final detector performance

For intermediate variable `X`, avoid choosing a specification solely from historical similarity if final detector performance can establish a more meaningful bound.

Example workflow:

1. deliberately span a controlled range of `X` during qualification;
2. fabricate matched devices;
3. measure final response `Z` such as D*, noise, sweepout, yield;
4. fit a physically/statistically defensible `Z=f(X,other variables)` model;
5. determine the `X` range consistent with detector requirement plus uncertainty;
6. release that range as the engineering limit.

This is especially important for:

- RIE conversion depth;
- TLM rho_c;
- passivation oxide thickness;
- mesa undercut;
- annealed carrier density;
- lifetime.

## 13. Historical RP-01 values are references, not automatic spec limits

Examples:

- thickness `9.5 µm`;
- n `9.8×10^14 cm^-3`;
- µ `4×10^4 cm²/Vs`;
- oxide `80 nm`;
- rho_c `9×10^-4 Ωcm²`;
- g-r plateau `24.5 nV/√Hz`;
- D* `2×10^11 cm Hz^1/2/W`.

These values are valuable reference points.

Unless the paper provides a tolerance/yield distribution or the project establishes detector sensitivity around them, do not reinterpret one historical value as a symmetric production tolerance.

## 14. Stability before capability

Before computing capability indices, establish that the process is statistically stable over the evaluated interval.

Use appropriate control charts/run-order plots for:

- run means;
- within-wafer nonuniformity;
- source-use drift;
- tool-condition variables;
- check standards.

Investigate:

- trends;
- shifts;
- cycles;
- source depletion;
- chamber seasoning;
- calibration drift;
- lot changes.

If the process is drifting, a single `Cp/Cpk` can be misleading.

## 15. Rational subgroup definition

Define subgroups based on actual process physics.

Examples:

- multiple sites on one wafer = spatial subgroup, not independent LPE runs;
- several devices from one die = device-within-wafer subgroup;
- repeated growths from one melt = source-use sequence;
- multiple wafers on separate source charges = run-level subgroup.

The subgroup structure must be stored with the statistical analysis.

## 16. Distribution checks

Do not automatically use normal-theory capability for:

- one-sided defect counts;
- zero-inflated failure metrics;
- lognormal contact/noise quantities;
- censored values below/above instrument limits;
- multimodal distributions caused by hidden process states.

Use transformations, distribution-specific capability, percentile/tolerance methods, or direct yield estimation where appropriate.

Document the model choice.

## 17. One-sided specifications

Many detector/process outputs are inherently one-sided:

- maximum leakage;
- maximum 1/f noise;
- maximum undercut;
- minimum mobility;
- minimum D*;
- minimum breakdown margin.

Use one-sided capability/risk metrics rather than inventing a meaningless symmetric limit.

## 18. Small-sample qualification

Early HgCdTe development may have very few costly runs.

Do not claim mature process capability from a tiny dataset.

For small samples:

- report raw runs;
- confidence intervals on means/variances where meaningful;
- Bayesian/physical-model priors only if explicitly justified;
- prediction/tolerance uncertainty;
- all failure/deviation histories.

Label the state `DEVELOPMENT-CAPABILITY` rather than production capability.

## 19. Minimum evidence for a candidate local process window

Before promoting a variable from `QUAL` to a numerical local process window, require:

1. calibrated/qualified measurement method;
2. repeated experiments spanning the candidate center;
3. evidence of a stable local response;
4. sensitivity to the main control variables;
5. at least one repeat run at the nominal center after the initial DOE;
6. no unresolved confounding with source/substrate/tool state;
7. downstream/final-performance consistency.

The exact number of runs is process/cost dependent and shall be justified rather than universally fixed here.

## 20. Release hierarchy

Use explicit maturity labels:

### `OPEN`

No defensible process value.

### `CANDIDATE-P`

Compatible published process value but not yet local-qualified.

### `LOCAL-QUALIFIED`

Local DOE/metrology demonstrates a reproducible operating region but full long-term capability is not established.

### `PILOT-RELEASE`

Repeated lots/runs under frozen documentation show stability and acceptable risk for controlled pilot fabrication.

### `PRODUCTION-RELEASE`

Measurement system, process stability, capability/yield, change control and final detector performance meet the defined program requirement.

RP-01 as a whole is currently below `PILOT-RELEASE` because multiple historical/app-specific controls remain local-qualification items.

## 21. Process-window representation

Do not reduce a strongly coupled process to independent min/max boxes if interactions are material.

Examples:

- LPE growth: `T × ΔT × time × melt inventory × source-use state`;
- Hg anneal: `T_dwell × time × pHg × cooldown trajectory`;
- RIE: `pressure × gas ratio × self-bias × sample T × semiconductor exposure time`.

Where necessary release a response-surface/allowed-region model rather than independent scalar tolerances.

## 22. Guard bands

When measurement uncertainty and process risk warrant it, define internal action/guard limits tighter than the engineering specification.

The guard-band method must state:

- engineering spec;
- measurement uncertainty;
- risk criterion;
- internal release/action boundary.

Do not silently shrink specifications without documenting the reason.

## 23. Change control / requalification triggers

At minimum require review/requalification after material changes to:

### Upstream

- CdZnTe supplier/lot/specification;
- polarity/miscut;
- final substrate surface process;
- source-element supplier/purity;
- source-synthesis method;
- melt inventory/well geometry;
- boat revision;
- Hg-source geometry;
- furnace/sensor position/calibration;
- growth trajectory;
- anneal source/reservoir/cooldown.

### Frontside

- resist family/developer;
- wet-etch chemistry or bath control;
- anodization electrolyte/cell geometry;
- RIE chamber/reactor/electrode/gas delivery;
- metallization tool/source/rates;
- lift-off method.

### Measurement

- Hall magnet/contact methodology;
- FTIR model/instrument;
- responsivity reference detector;
- preamp/analyzer configuration;
- software/model version used to reduce data.

## 24. Requalification depth should be risk-based

Not every change requires repeating the entire process.

Define impact paths.

Example:

- RIE chamber clean procedure change -> requalify P08 outputs + P09 TLM + selected detector noise/responsivity controls;
- CdZnTe supplier change -> P07/P03/P04 material chain and selected final devices;
- preamp replacement -> P12B measurement system only unless detector loading changes.

Document the rationale.

## 25. Golden/reference artifacts and check standards

Where feasible maintain stable check standards for metrology:

- thickness/step standard;
- optical wavelength/reference detector;
- resistance/noise reference;
- Hall/magnet field check;
- calibrated blackbody/aperture geometry;
- lithography CD standard.

Track check-standard measurements over time to separate tool drift from process drift.

HgCdTe devices themselves may be poor long-term standards if their surface/contacts age; choose artifacts appropriate to each measurement.

## 26. Data architecture

Every result used for capability must retain identifiers linking:

`material lot -> substrate -> source charge -> LPE run -> anneal run -> die/device -> process steps -> measurement instrument/calibration -> analysis version`.

No orphan spreadsheet values.

## 27. Final detector yield

Intermediate capability must eventually be validated against actual detector yield.

Define yield categories explicitly, e.g.:

- material-pass;
- frontside-fabrication-pass;
- contact-pass;
- package-pass;
- detector-electrical-pass;
- optical/noise/performance-pass.

A high final D* on one surviving device is not a high-yield process.

## 28. Failure Pareto / causal feedback

For each failed device/run assign the best-supported failure mechanism:

- material composition/thickness;
- substrate/interface;
- anneal state;
- mesa/passivation;
- RIE/contact;
- metallization;
- package;
- measurement artifact;
- unknown.

Preserve `unknown` rather than forcing classification.

Use failure-mode frequency and correlation to update which process metrics deserve tighter control.

## 29. Future numerical release table

When local data exist, P17 will host or point to a controlled table with columns:

`Metric | Method | Spec/goal | Guard limit | Measurement uncertainty | Mean | Within-run sigma | Run-to-run sigma | Capability/risk metric | N runs/lots | Status | Revision`

No row should be populated from invented or single-paper tolerance estimates.

## 30. Current project implication

The P01–P16/PxxA-E framework now defines what must be measured and how major historical gaps can be locally qualified.

P17 defines what evidence will be required before those local settings become a released process.

The next step toward `REPRODUCIBLE-RELEASE` is therefore **data-driven window closure**, not additional unsupported numerical specificity.