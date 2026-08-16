# Research checkpoint — after sample genealogy / material allocation Round 45

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 45 began from the Round-44 conclusion that the missing empirical-Jacobian campaigns were now designed at the level of experimental units, information criteria and structural design sizes, but the project still lacked a physically coherent answer to:

> How should scarce HgCdTe material descend through those campaigns without pseudoreplication, unnecessary duplicate devices, destroyed holdouts or hidden geometry shortfalls?

Round 45 therefore built a sample-genealogy/material-allocation layer.

No physical material inventory was assumed. No yield was invented. No power-based final sample size was assigned.

---

# 2. New controlled artifacts

Created:

- `calculations/RP01_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION.md`;
- `procedures/P22B_FIRST_BUILD_DESCENDANT_GENEALOGY_MATERIAL_ALLOCATION.md`;
- `travelers/P16G_SAMPLE_GENEALOGY_MATERIAL_ALLOCATION_REGISTER.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND45.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND45.md`;
- this checkpoint.

AGENTS is refreshed at the end of the round.

---

# 3. New integration concept — P16G

P16A-P16G now separate seven questions:

1. **P16A:** is a complete first build executable without undocumented irreversible choices?
2. **P16B:** which evidence-ranked process branch should be pursued?
3. **P16C:** does a real laboratory have the required physical capability?
4. **P16D:** has that infrastructure passed controlled IQ/OQ/surrogate commissioning?
5. **P16E:** are measurement/control uncertainties and requirements adequately allocated?
6. **P16F:** are the missing empirical-Jacobian campaigns identifiable and physically ready?
7. **P16G:** can the required physical material be allocated through those campaigns with correct genealogy, holdouts, layout and experimental-unit independence?

New state:

`P16G-MATERIAL-GENEALOGY-PLAN-READY`.

Current:

`NO / NOT PHYSICALLY INSTANTIATED`.

P16G feeds the P16F genealogy/material-feasibility gate. It is not an empirical result or release state.

---

# 4. Major result 1 — four different material counts must remain separate

Round 45 separates:

1. independent process units;
2. physical descendant pieces;
3. usable material area/packing;
4. yield/power/failure reserve.

A program can have enough independent growths statistically while still lack enough physical area for Hall, LBIC, TLM, detectors, package builds, holdouts and destructive witnesses.

Conversely, one large growth can produce many pieces but still contributes only one LPE experimental unit.

This distinction is now permanent.

---

# 5. Major result 2 — the program is a genealogy DAG, not a sum of campaign counts

Round 45 rejects:

`N_program = N_F1 + N_F2 + N_F3 + N_F4 + N_F5`.

The physically correct representation is a directed acyclic graph:

`growth -> intact mapped material -> branch treatments -> detector descendants -> package descendants`.

Important sharing:

- F1 can use completed detector descendants already fabricated for F4/F5/device-bridge work;
- F3 can consume selected descendants from F2 material roots;
- F4 can consume selected annealed material descendants;
- P10/P11/P12/P13 can share one completed detector state;
- F5 can use the same detector after its pre-package baseline.

Therefore campaign counts are not additive.

---

# 6. Major result 3 — delayed differentiation conserves material and improves matching

Permanent rule:

> Split a parent at the latest common state before descendants require different irreversible histories.

Examples:

- perform P06 on intact as-grown material before cutting;
- where process geometry allows, anneal one large parent and split post-anneal Hall/device descendants afterward;
- co-load RIE witness structures and detector structures in one treatment bundle;
- measure P10-P13 on one completed detector;
- measure pre-package detector state before committing that same die to F5.

This reduces material consumption and preserves common-mode covariance.

---

# 7. P06 versus P05 genealogy consequence

P06 is explicitly non-destructive transmission metrology. It should normally measure the intact parent before subdivision.

P05 is different.

The Hall acquisition itself need not destroy a specimen, but the required van-der-Pauw contact preparation changes the surface/geometry state and the exact contact process remains local.

Therefore the conservative current branch is:

`P06 intact parent -> split -> dedicated P05 material-control descendant + contact-free process/device descendant`.

Same-specimen Hall->anneal or Hall->device reuse remains possible only after local compatibility qualification.

This prevents a material-conservation shortcut from silently changing the process under study.

---

# 8. F1 incremental material demand

F1 field-response points are repeated measures on a completed detector.

Structural consequences:

- one detector is enough to estimate a within-device local field slope;
- at least two devices are mathematically needed to begin estimating a between-device slope variance component;
- statistically credible device count remains power/variance dependent.

Most importantly:

**F1 normally adds zero incremental HgCdTe devices once suitable completed F4/F5/device-bridge descendants exist.**

This is a conservation result, not a claim that one detector is enough for process release.

---

# 9. F2 validated structural root-count lower bounds

Existing design sizes:

- Jacobian-first F2 axial: 9 fitted growths;
- BBD: 15;
- FCCCD: 17;
- two-factor Stage-2 quadratic: 11.

P21 currently requires at least three independent held-out growth states.

Under the explicit assumption that Stage-0 center growths are eligible for reuse as formal center rows, Round 45 derives:

| F2 branch | Fit growths | Holdouts | Conditional independent-growth root floor |
|---|---:|---:|---:|
| Jacobian-first | 9 | 3 | >=12 |
| BBD | 15 | 3 | >=18 |
| FCCCD | 17 | 3 | >=20 |
| Stage-2 | 11 | 3 | >=14 |

These are the first quantitative **program-root structural lower bounds**.

They do not mean the full qualification program physically fits on 12/18/20/14 grown pieces.

Additional roots may be required for:

- nonreusable pilots;
- physical area shortage;
- failed/poor-morphology growths;
- downstream blocking;
- independent power replication;
- source-history designs.

---

# 10. Stage-0 reuse now controlled

A pilot/center growth can count as a formal model center only if:

- apparatus/process revision is unchanged;
- the physical center matches the frozen design center;
- metrology/model versions remain compatible;
- the sample was not selectively included because its response looked favorable;
- raw data/genealogy are retained;
- the design information matrix carries the observation prospectively.

Otherwise it remains `PILOT-NONREUSABLE` and adds to the total root demand.

---

# 11. F3 anneal structural accounting

Round 45 defines:

`N_treat,F3 = N_B + N_J + N_H + N_C + N_X`.

For a first-order axial fit of `k_A` stable n-like continuous anneal descriptors with three centers:

`N_J,fit = 2 k_A + 3`.

For the current four-descriptor concept:

`N_J,fit = 11` treatment histories.

This number excludes:

- active carrier-boundary search;
- holdouts;
- controls;
- destructive validation;
- power replication.

Round 45 also freezes an important unit issue: multiple pieces co-loaded in one ampoule and experiencing one common thermal/Hg trajectory are not automatically independent anneal-run replicates.

---

# 12. F4 treatment-bundle architecture

Round 44 gives the fitted chamber-treatment count:

`N_Q,fit = 2 k_R + 3`.

At four independent RIE factors this is 11 chamber treatments.

Round 45 now separates the treatment count from physical witness count.

One chamber run may contain sibling structures for:

- oxide clear/recession;
- Hall converted sheet state;
- LBIC conversion depth/lateral extent;
- TLM/contact response;
- detector response.

Those are one treatment bundle, not five independent RIE runs.

The number and area of structures in the bundle remain physical-layout quantities.

---

# 13. Full detectors should not automatically be fabricated for every early RIE state

A staged material strategy is now controlled:

1. obtain minimum process/material-state witnesses for every RIE treatment;
2. fabricate full detector descendants at the center, high-information contrasts and held-out states selected by decision value;
3. expand detector-bearing states only when needed to identify the material-state -> detector-performance map.

This prevents expensive full device processing on treatment states already demonstrated to be irrelevant, unstable or outside the feasible region.

---

# 14. P10-P13/F1 detector sharing

Where loading/heating is qualified as reversible, the preferred detector chain is:

`P10 -> P11 -> P12 -> P13 -> verification baseline`

on the same physical device and matched state.

This directly supports the Round-43 covariance/common-path logic and avoids assembling D* or lifetime claims from unmatched descendants.

F1 is then run on one or more of these same detectors.

---

# 15. F5 package accounting

Non-HgCdTe surrogate family screening consumes zero HgCdTe detector dies.

For actual packages:

`N_HgCdTe dies = N_independent package builds`

unless a separately qualified reversible package/rework route exists.

The same die supplies:

`pre-package baseline -> package -> post-package response`.

Repeated cycles and pulses are within-package observations and do not increase independent package-build count.

---

# 16. Physical material-area requirement remains intentionally open

A final material-area number cannot yet be produced because several local geometric inputs remain unresolved:

- actual grown usable outline;
- Hall coupon dimensions;
- detector die outline;
- LBIC/TLM witness footprints;
- cut streets;
- kerf/wander;
- P35 functional edge exclusion;
- handling/fixture margin;
- crystallographic/orientation constraints.

Round 45 therefore specifies a CAD/polygon packing problem.

For parent `g`:

`Omega_usable,g` = measured usable region.

For every descendant `r`:

`Omega_r+` = active footprint plus process/kerf/edge/handling margins.

Require all `Omega_r+` to fit non-overlapping inside `Omega_usable,g`.

Scalar area alone is not enough.

---

# 17. Reserve is no longer an arbitrary percentage

Round 45 separates reserve into:

- process failure;
- metrology/contact/fixture failure;
- layout/singulation loss;
- holdouts;
- destructive failure analysis;
- power-based replication.

Once an empirical independent success probability `p` and required successes `r` exist:

`Pr(K>=r)=1-sum_{k=0}^{r-1} C(n,k)p^k(1-p)^(n-k)`.

This can size `n` at a declared confidence.

No `p` or confidence target exists yet, so no reserve multiplier is released.

Correlated wafer/process failures will require genealogy-aware modeling instead of an independent binomial.

---

# 18. Experimental-unit hierarchy reinforced

Permanent Round-45 rules:

- map points are not growth replicates;
- sibling coupons are not LPE replicates;
- separate anneal histories may be treatment units while remaining blocked by common growth;
- co-loaded RIE coupons are within-treatment witnesses;
- field points are repeated detector measurements;
- repeated P10-P13 measurements are measurement repeats;
- package cycles are repeated measures, not package builds.

This removes a major path to pseudoreplication from the remaining development program.

---

# 19. Material conservation cannot create treatment confounding

A material-efficient plan is invalid if treatment becomes aliased with root material.

Example prohibited pattern:

- all low-temperature anneals on Growth A;
- all high-temperature anneals on Growth B.

The treatment effect would be inseparable from growth effect.

P16G therefore contains an explicit treatment-root/wafer-position/time confounding audit for F3/F4/passivation/F5.

---

# 20. P16G closure state

Current:

`P16G-MATERIAL-GENEALOGY-PLAN-READY = NO / NOT PHYSICALLY INSTANTIATED`.

To become YES the future lab must at minimum identify actual roots, choose the F2 branch, freeze pilot reuse, demonstrate descendant CAD packing, freeze P05 compatibility strategy, define anneal/RIE experimental units, protect holdouts and destructive witnesses, allocate detector/package descendants and pass the confounding audit.

---

# 21. Project maturity after Round 45

Unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`
- `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16G-MATERIAL-GENEALOGY-PLAN-READY = NO / NOT PHYSICALLY INSTANTIATED`

Strategic state:

**branch-selected + capability-specified + acceptance-specified + uncertainty architecture defined + information-optimal empirical campaigns designed + sample genealogy/material accounting designed + not physically instantiated**.

---

# 22. Strongest next analytical work — Round 46

The next useful layer is not another generic DOE or material-count estimate.

Build a **campaign execution / material-release control plan** that determines when a descendant is allowed to advance to an expensive or irreversible downstream step.

Round 46 should define:

1. chronological stage sequence across P16C/D/E/F/G;
2. go/hold/stop gates after surrogate commissioning, Stage-0 variance, F2 material response, F3 state boundary and F4 material-state response;
3. material-release gates before full detector fabrication and before packaging;
4. run-order randomization/blocking subject to source-use, ampoule and chamber constraints;
5. dynamic holdout/reserve release rules;
6. decision rules for whether another upstream run has greater information value than consuming an existing descendant downstream;
7. failure/deviation routes into P18 without destroying remaining holdout material.

This would turn the current design architecture into a controlled development campaign sequence while still avoiding invented physical results.
