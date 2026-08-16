# Recovery checkpoint — round 11 failure-analysis integration

**Date:** 2026-08-15 America/New_York

**Purpose:** Fast handoff after adding the failure-analysis/diagnostic layer on top of the P01–P17 process architecture.

## 1. New files

- `procedures/P18_FAILURE_ANALYSIS_DIAGNOSTIC_ATLAS.md`
- `travelers/P18_FAILURE_ANALYSIS_RECORD.md`

## 2. Core diagnostic rule

Do not map one symptom to one cause.

The controlled sequence is:

`observed signature -> competing hypotheses -> discriminating measurements -> most-supported mechanism -> containment/corrective action -> verification`.

Prefer initially:

1. preserved raw-data re-analysis;
2. nondestructive repeat metrology;
3. matched witnesses/controls;
4. spatial-map correlation;
5. reversible T/field/frequency/optical-power sweeps;
6. destructive cross-section/chemistry only after the hypothesis space narrows.

## 3. Upstream signatures covered

P18 includes diagnostic chains for:

- x/edge too red or blue;
- x gradient;
- thickness high/low;
- thickness nonuniformity;
- residual Te-rich melt/wipe-off failure;
- unexpected rough/wavy/terraced morphology;
- low mobility at correct x/n;
- wrong carrier type after anneal;
- nonreproducible carrier density.

Each chain points back to P03/P04/P05/P06/P07 variables and distinguishes metrology artifacts from true process shifts.

## 4. Mesa/passivation signatures

Included:

- incomplete mesa isolation;
- excessive undercut;
- rough sidewalls;
- correct planar oxide thickness but poor detector performance;
- high 1/f after passivation;
- anomalous anodization voltage-time trace.

P02C perimeter sensitivity is used explicitly where sidewall quality is suspected.

## 5. RIE/contact signatures

Included:

- contact-window CD mismatch;
- incomplete oxide clear;
- excessive HgCdTe physical recession;
- acceptable Hall but poor TLM;
- acceptable TLM but strong detector sweepout;
- non-ohmic/high TLM;
- contact degradation after cryogenic cycling.

Important conceptual diagnostic:

`good rho_c + bad sweepout` is evidence that majority-carrier contact quality does not close minority-carrier recombination (`rho_c != S_c`).

## 6. Detector electrical/optical signatures

Included:

- resistance higher/lower than material/geometry expectation;
- responsivity low at low field;
- strong field saturation/rolloff;
- polarity asymmetry;
- detector cutoff inconsistent with P06 material edge.

The cutoff chain explicitly forbids immediately declaring composition error; it checks convention, absorption/thickness, grading and optical calibration.

## 7. Noise/D* signatures

Included:

- white floor above Johnson/detector model;
- 1/f knee much higher than historical reference;
- apparent g-r plateau changes with analyzer settings;
- good R/noise individually but poor D*;
- BLIP only at some biases.

P12B dummy-resistor/Johnson-noise checks are the first-line discriminators for measurement/electronics artifacts.

## 8. Temporal/bandwidth signatures

Included:

- measured bandwidth far too low;
- non-single-pole response;
- lifetime depends on injection amplitude;
- lifetime shortens strongly with field.

P13 external transfer de-embedding and amplitude+phase consistency remain mandatory before assigning intrinsic detector lifetime.

## 9. Packaging signatures

Included:

- bare die passes but package increases noise;
- resistance changes after package bake;
- responsivity falls after packaging with stable R;
- bandwidth falls only after packaging.

Package bakeout remains part of detector thermal history.

## 10. Cross-module chains

P18 includes compact sequences for:

- low D* + high 1/f + low lifetime;
- low D* + good noise but low responsivity;
- low D* + normal responsivity but high white noise;
- correct material metrics but poor final device yield;
- large within-wafer device spread.

These are designed to identify the failing stage before tightening an unrelated process parameter.

## 11. Integration with P17

Every confirmed failure mechanism feeds the P17 capability register:

- failure frequency;
- process module;
- variance/capability impact;
- measurement-system contribution;
- change-control/requalification trigger;
- recurrence after corrective action.

A mature process should show decreasing recurrence of known failure classes, not just improving average D*.

## 12. Blank record

`travelers/P18_FAILURE_ANALYSIS_RECORD.md` captures:

- genealogy;
- observed signature;
- containment;
- hypotheses;
- ordered discriminating tests;
- measurement-artifact audit;
- full process-history audit;
- spatial correlations;
- root cause;
- corrective action;
- requalification;
- verification;
- final disposition.

## 13. Current project state after round 11

The project now has three layers:

1. **P01–P16:** scientific fabrication/measurement methods and end-to-end traveler;
2. **P17:** statistical process release/capability/change control;
3. **P18:** failure diagnosis, containment, corrective action and recurrence tracking.

Historical process values remain open where the literature genuinely does not disclose them, but each high-impact gap now has an explicit local qualification/recovery method.

## 14. Next logical work

The next high-value integration work is to build a **master specification / requirements traceability matrix** linking:

`final detector requirement -> intermediate material/process characteristic -> measurement -> Pxx control -> release/failure response`.

This would answer, for every controlled variable, **why it exists and which final detector property it protects**.

Examples:

- x/edge -> spectral band/cutoff;
- thickness -> absorption/gain/geometry;
- n/µ -> resistance, gain, noise, field distribution;
- passivation -> surface recombination/1/f/lifetime;
- rho_c / blocking contact -> majority contact + sweepout;
- lifetime -> responsivity/bandwidth;
- package capacitance -> bandwidth/readout.

## 15. Recovery order

1. `AGENTS.md`
2. this checkpoint after round 10
3. `procedures/P18_FAILURE_ANALYSIS_DIAGNOSTIC_ATLAS.md`
4. `travelers/P18_FAILURE_ANALYSIS_RECORD.md`
5. P17 for capability/release integration
6. branch-specific Pxx procedures for root-cause investigation.
