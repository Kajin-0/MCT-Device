# Source ledger addendum — Round 45 sample genealogy / material allocation

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`  
**Round classification:** `DERIVED-INTERNAL-CONTROL`

## 1. Scope

Round 45 does not introduce a new historical HgCdTe process source family and does not claim new RP-01 documentary closure.

Its purpose is to derive a controlled sample-genealogy/material-allocation architecture from already controlled process, metrology, DOE, singulation and packaging modules.

No vendor search was performed. No material inventory, yield, wafer area or power-based sample size was invented.

---

# 2. New controlled artifacts

Round 45 adds:

- `calculations/RP01_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION.md`;
- `procedures/P22B_FIRST_BUILD_DESCENDANT_GENEALOGY_MATERIAL_ALLOCATION.md`;
- `travelers/P16G_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION_REGISTER.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND45.md`;
- this source-ledger addendum;
- `research/2026-08-16_checkpoint_after_sample_genealogy_round45.md`.

AGENTS is refreshed separately.

---

# 3. Evidence basis — F2 LPE root counts

## Controlled internal sources

- P21 LPE response-surface/Jacobian qualification;
- P22 information-optimal DOE planning;
- P22A multi-subsystem Jacobian program;
- Round-44 empirical-Jacobian calculation/checkpoint.

## Derived Round-45 result

Current fitted-design root counts remain:

- 9 independent growths for the Jacobian-first axial F2 option;
- 15 for BBD;
- 17 for FCCCD;
- 11 for the two-factor Stage-2 quadratic option.

P21 additionally requires at least three held-out growth states:

- center confirmation;
- one interior combined perturbation;
- one feasible near-margin confirmation.

Therefore, under the explicit assumption that eligible Stage-0 center runs are reused inside the formal fitted design, Round 45 derives validated independent-growth structural lower bounds:

- `9+3 = 12`;
- `15+3 = 18`;
- `17+3 = 20`;
- `11+3 = 14`.

### Evidence class

`DERIVED-INTERNAL / STRUCTURAL-COUNT`

### Restriction

These values are not:

- wafer procurement counts;
- physical-area requirements;
- production sample sizes;
- power-based replication;
- yield reserves.

If Stage-0 runs are nonreusable pilots, additional independent roots are required.

---

# 4. P06 consumption classification

## Controlled source

`procedures/P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md` explicitly defines P06 as non-destructive infrared transmission metrology and recommends material measurement before device patterning.

## Round-45 inference

P06 should normally be performed on the intact grown parent before subdivision when beam/sample geometry permits.

### Evidence class

`DERIVED-INTERNAL-WORKFLOW`.

This is a material-conservation/genealogy rule, not an RP-01 historical process claim.

---

# 5. P05 consumption classification

## Controlled source

`procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md` requires a van-der-Pauw specimen with four perimeter contacts and states that the exact contact fabrication process remains qualification dependent.

## Round-45 inference

The Hall electrical acquisition itself need not physically destroy the sample, but Hall contact fabrication changes the specimen surface/geometry state. Therefore P05 is conservatively treated as a dedicated material-control branch until same-specimen compatibility with subsequent Hg anneal or detector fabrication is demonstrated.

### Evidence class

`DERIVED-INTERNAL-WORKFLOW / CONSERVATIVE-COMPATIBILITY`.

Round 45 does not assert that same-specimen reuse is impossible. It makes it a controlled compatibility qualification instead of an undocumented assumption.

---

# 6. P10-P13 shared detector rule

## Controlled sources

- P10 DC/bias/self-heating;
- P11 absolute spectral responsivity;
- P12 noise/NEP/D*;
- P13 temporal/frequency response;
- P16/P16B/P16E matched-state requirements;
- Round-43 covariance results;
- Round-44 F1 field-derivative architecture.

## Derived result

When low-injection, self-heating, optical-loading and reversibility gates pass, the same completed detector should preferentially provide the matched P10/P11/P12/P13 state.

The F1 field-derivative campaign can therefore normally use those same completed detector descendants rather than requiring a separate detector lot.

### Evidence class

`DERIVED-INTERNAL-WORKFLOW / COVARIANCE-PRESERVING`.

No minimum statistically credible number of devices is released.

---

# 7. F3 anneal genealogy

## Controlled sources

- P04/P04A/P04B;
- P23 state-boundary/Jacobian qualification;
- P05/P06;
- P22A F3 architecture.

## Derived result

Every distinct irreversible anneal history requires its own treated specimen/history at the relevant anneal experimental-unit level.

Round 45 defines:

`N_treat,F3 = N_B + N_J + N_H + N_C + N_X`,

where:

- `N_B` = classifier/boundary histories;
- `N_J` = stable n-like Jacobian histories;
- `N_H` = holdouts;
- `N_C` = controls;
- `N_X` = destructive validation histories.

For a first-order axial local model with `k_A` independently controlled continuous anneal descriptors plus three centers:

`N_J,fit = 2 k_A + 3`.

For the current four-descriptor concept this gives 11 fitted treatment histories.

### Evidence class

`DERIVED-INTERNAL / STRUCTURAL-COUNT`.

Boundary search, holdouts, variance/power replication and physical coupon footprint remain open.

### Additional experimental-unit caution

Multiple pieces co-loaded in one ampoule/run and subjected to the same thermal/Hg history are not automatically independent anneal-run replicates. The actual ampoule/run experimental-unit definition must be frozen locally.

---

# 8. F4 RIE treatment bundles

## Controlled sources

- P08/P08A-P08G;
- P24 blocking-contact empirical process window;
- P34 reactor equivalence;
- P22A F4 architecture.

## Derived result

For `k_R` independently controllable RIE factors, the Round-44 Jacobian-first fitted-design structure is:

`N_Q,fit = 2 k_R + 3` independent chamber treatments.

For four factors:

`N_Q,fit = 11`.

One chamber treatment may include co-loaded sibling structures for:

- oxide-clear/recession;
- Hall/converted sheet state;
- LBIC/depth/lateral conversion;
- TLM/contact response;
- completed detector response.

These are **within-treatment witnesses**, not independent RIE treatments.

### Evidence class

`DERIVED-INTERNAL / EXPERIMENTAL-UNIT-CONTROL`.

No claim is made that 11 chamber treatments are statistically sufficient or that 11 complete detectors must be fabricated.

---

# 9. F5 package genealogy

## Controlled sources

- P15;
- P33 cryogenic package empirical window;
- P22A F5 architecture.

## Derived result

Non-HgCdTe surrogate package-family screening consumes zero HgCdTe detector dies.

After a construction family is selected, one independent actual package build consumes one completed detector die unless a separately qualified reversible/rework route exists.

Repeated thermal pulses/cycles on the same package are within-build observations, not independent package builds.

### Evidence class

`DERIVED-INTERNAL / EXPERIMENTAL-UNIT-CONTROL`.

---

# 10. Singulation/layout evidence

## Controlled source

P35 establishes that:

- singulation is a genuine process operation;
- visible kerf/chipping does not bound functional/subsurface damage;
- `d_visible`, `d_functional` and `d_release` must remain distinct;
- cut street, kerf, protection/support and post-cut effects must be qualified.

## Round-45 consequence

Material area cannot be calculated from nominal die area alone.

Each descendant layout footprint must include:

- active specimen footprint;
- cut street;
- kerf/wander uncertainty;
- functional edge exclusion;
- fixture/handling margin;
- required orientation.

Packing must be checked on the actual usable parent geometry.

### Evidence class

`DERIVED-INTERNAL-WORKFLOW`.

No numerical `d_release`, kerf or die outline is created by Round 45.

---

# 11. Genealogy-DAG non-additivity

Round 45 formalizes that campaign material counts cannot be added naively.

Examples:

- F1 can reuse F4/F5 detector descendants;
- F3 can use selected descendants of F2 growths;
- F4 can use material from the selected F2/F3 states;
- F5 can package detector descendants already used for pre-package P10-P13;
- P10-P13 can share one detector.

Thus:

`N_program != N_F1 + N_F2 + N_F3 + N_F4 + N_F5`.

### Evidence class

`DERIVED-INTERNAL / GENEALOGY-ACCOUNTING`.

The program must be represented as a directed acyclic graph with physical parent-child relationships and correct experimental-unit labels.

---

# 12. Physical area equation

For parent root `g`, define usable region `Omega_usable,g`.

For descendant roles `r`, define expanded non-overlapping layout polygons `Omega_r+`.

A necessary layout condition is:

`area(union_r Omega_r+) <= area(Omega_usable,g)`

plus geometry/orientation/packing feasibility.

### Evidence class

`DERIVED-INTERNAL / GEOMETRIC-CONTROL`.

This is not sufficient by scalar area alone; actual CAD/polygon packing remains required.

---

# 13. Statistical reserve equation

Once an empirical independent success probability `p` exists and at least `r` successful descendants are required, Round 45 records:

`Pr(K>=r)=1-sum_{k=0}^{r-1} C(n,k) p^k (1-p)^(n-k)`.

This is the appropriate basic independent-binomial sizing relation.

Correlated root/process failures require a genealogy-aware model instead.

### Evidence class

`IDENTITY / STATISTICAL-DESIGN`.

No `p`, confidence target or reserve multiplier is assigned in Round 45.

---

# 14. New Round-45 state

Round 45 introduces:

`P16G-MATERIAL-GENEALOGY-PLAN-READY`.

Current:

`NO / NOT PHYSICALLY INSTANTIATED`.

P16G closes only structural genealogy/material feasibility. It does not imply P16F empirical readiness, P16E allocation completion, P16A first-build readiness or P17 release.

---

# 15. No new external documentary claims

Round 45 performs no new historical-source search and makes no new claim about:

- exact RP-01 wafer size;
- exact RP-01 die outline;
- singulation method;
- material yield;
- number of devices produced;
- experimental sample count;
- Hall coupon reuse;
- package rework.

Those remain governed by prior source ledgers and local qualification.
