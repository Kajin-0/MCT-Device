# Recovery checkpoint — round 10 statistical release framework

**Date:** 2026-08-15 America/New_York

**Purpose:** Fast handoff after converting the P01–P16 qualification architecture into an explicit statistical process-release framework.

## 1. New files

- `procedures/P17_STATISTICAL_PROCESS_CAPABILITY_RELEASE.md`
- `travelers/P17_PROCESS_RELEASE_CAPABILITY_REGISTER.md`

Round 10 is not primarily a source-recovery round. It defines what evidence will be required before local qualified settings become a released manufacturing process.

## 2. Core statistical rule

Engineering specification limits are **not** generated from observed process spread.

Specifications come from:

- detector physics;
- downstream compatibility;
- final detector/system performance;
- defensible historical reference values where appropriate;
- deliberate intermediate-metric versus final-device correlation.

Only after the specification is independently justified may process capability be calculated against it.

## 3. NIST process-capability basis

NIST/SEMATECH process-capability guidance treats capability as comparison of a stable/in-control process with engineering specification limits.

For an approximately normal stable process:

`Cp = (USL-LSL)/(6 s_within)`

and

`Cpk = min[(USL-mean)/(3 s_within),(mean-LSL)/(3 s_within)]`.

P17 does **not** impose a generic Cpk ≥1.33/1.67 rule. A required capability level must be tied to the program's yield/risk requirements.

## 4. Measurement system comes first

Before a metric is used for process capability, characterize its measurement system for:

- repeatability;
- long-term/reproducibility variation;
- stability/drift;
- bias;
- resolution;
- linearity;
- geometry/configuration effects;
- uncertainty.

This applies to P05/P06 material metrology and all critical frontside/device metrics.

## 5. Measurement uncertainty versus specification width

For metric `Y` define:

`r_U = U_Y/(USL-LSL)`

for a two-sided specification using an explicitly stated uncertainty convention.

P17 does not set one universal allowed `r_U`; the project must document false-accept/false-reject risk and improve metrology when uncertainty is too large for a defensible decision.

## 6. Variance hierarchy

Separate where possible:

1. measurement repeatability;
2. within-wafer spatial variation;
3. run-to-run variation;
4. source-charge/substrate-lot variation;
5. long-term tool drift;
6. operator/setup effects.

Do not use map points from one wafer as independent LPE-run replicates.

Conceptual mapped-data model:

`Y_ij = mu + Run_i + Spatial_ij + Measurement_ij`.

Extend with lot/source/tool random effects where justified.

## 7. Core process capability vectors

### Material

`Y_material={mean thickness,thickness nonuniformity,mean optical x/edge,x/edge nonuniformity,carrier type,n_H/multicarrier,µ_H,morphology/usable area,lifetime proxy}`.

### Mesa

`Y_mesa={etch depth,lateral undercut,CD bias,roughness,isolation completeness}`.

### Passivation

`Y_pass={oxide thickness,formation/voltage-time signature,sidewall/perimeter behavior,noise/lifetime impact}`.

### RIE/contact

`Y_contact={sheet/multicarrier state,d_conv,L_conv,d_etch,rho_c,sweepout metric,noise impact,bandwidth impact}`.

### Detector

`Y_detector={R(E,lambda,f),e_n(f),NEP,D*,cutoff,response bandwidth/tau,stability}`.

## 8. Coupled process windows

Do not release strongly coupled physics as independent min/max boxes when interactions are material.

Examples:

### LPE

`{source state,melt inventory,TL,ΔT_SC,T(t),growth time,source-use state} -> {thickness,x,morphology}`.

### Hg anneal

`{initial state,T_dwell,time,pHg/T_reservoir,cooldown trajectory} -> {carrier type,n_H,µ_H,x/thickness,lifetime}`.

### RIE

`{gas ratio,pressure,self-bias/sample T,post-clear exposure} -> {d_etch,transport,d_conv,L_conv,rho_c,sweepout/noise}`.

A response-surface/allowed-region release may be more correct than scalar tolerances.

## 9. Release maturity labels

P17 defines:

- `OPEN`
- `CANDIDATE-P`
- `LOCAL-QUALIFIED`
- `PILOT-RELEASE`
- `PRODUCTION-RELEASE`.

The current end-to-end RP-01 reconstruction remains below `PILOT-RELEASE` because no local repeated fabrication dataset exists yet.

## 10. Change control

Requalification is triggered by process-relevant changes including:

- substrate supplier/face/surface process;
- source-element lot/synthesis method;
- LPE boat/melt inventory/furnace calibration;
- anneal source/reservoir/cooldown;
- wet-etch/passivation chemistry;
- RIE chamber/electrode/gas delivery;
- metallization/lift-off;
- metrology hardware/model/software changes.

Requalification depth should follow the physical impact path rather than automatically repeating everything.

## 11. Blank capability register

`travelers/P17_PROCESS_RELEASE_CAPABILITY_REGISTER.md` contains empty registers for:

- measurement-system capability;
- engineering specifications;
- variance components;
- capability/risk metrics;
- LPE/anneal/RIE coupled windows;
- yield stages;
- change control;
- failure Pareto;
- final release signoff.

Do not populate missing numerical tolerances from generic semiconductor manufacturing rules.

## 12. Next logical module

The next integration layer should be a **failure-analysis / diagnostic atlas** linking observable signatures to candidate modules and discriminating measurements.

The goal is not a list of guesses; each entry should contain:

`observed signature -> plausible mechanisms -> quickest discriminating test -> affected Pxx module -> required containment/requalification`.

Examples include:

- cutoff/x drift;
- thickness gradient;
- p-type after anneal;
- low mobility at correct n;
- excessive mesa undercut;
- high 1/f after passivation;
- TLM high rho_c;
- responsivity sweepout;
- noise plateau mismatch;
- bandwidth unexpectedly low;
- package-induced noise or drift.

## 13. Recovery order

1. `AGENTS.md`
2. this checkpoint after round 9
3. `procedures/P17_STATISTICAL_PROCESS_CAPABILITY_RELEASE.md`
4. `travelers/P17_PROCESS_RELEASE_CAPABILITY_REGISTER.md`
5. branch-specific Pxx modules for actual process-window generation.
