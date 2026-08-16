# RP-01 gap matrix addendum — Round 45 sample genealogy / material allocation

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 45 converts the Round-44 empirical-campaign designs into a physical genealogy/material plan and identifies which sample-count questions are analytically closed versus still dependent on actual material geometry, local compatibility, yield and power.

No readiness row is promoted by this addendum.

---

# 2. New gap states

Use the following Round-45 gap/state labels where applicable:

- `STRUCTURAL-COUNT-DERIVED` — independent-unit design count follows from a frozen model/design assumption.
- `ROOT-INVENTORY-OPEN` — actual independent material roots available are unknown.
- `DESCENDANT-FOOTPRINT-OPEN` — physical coupon/die/witness dimensions or layout are not frozen.
- `PHYSICAL-AREA-OPEN` — structural count exists but usable parent area/packing has not been demonstrated.
- `P05-DOWNSTREAM-COMPATIBILITY-OPEN` — Hall-contact/sample state has not been qualified for later anneal/device processing.
- `TREATMENT-UNIT-DEFINITION-OPEN` — physical experimental unit for ampoule/chamber/bundle still requires local definition.
- `TREATMENT-BUNDLE-LAYOUT-OPEN` — required within-run witness/device structures are not physically allocated.
- `SINGULATION-EDGE-EXCLUSION-OPEN` — local `d_release`/kerf/street geometry not frozen.
- `HOLDOUT-MATERIAL-OPEN` — independent confirmation material is not yet physically protected.
- `DESTRUCTIVE-WITNESS-OPEN` — destructive analysis has no dedicated descendant.
- `TREATMENT-ROOT-CONFOUNDING-OPEN` — treatment assignment is not yet proven separable from root/position/time blocks.
- `STATISTICAL-RESERVE-OPEN` — yield/failure reserve cannot be sized yet.
- `POWER-REPLICATION-OPEN` — independent-unit count required by effect size/variance remains unknown.
- `STRUCTURAL-GENEALOGY-READY` — physical genealogy and structural sample allocation are feasible, without implying powered/released status.

---

# 3. F2 LPE root-count gaps

## Closed structurally

Under the current model/design choices:

| Design | Fit roots | P21 minimum holdouts | Conditional structural root floor | State |
|---|---:|---:|---:|---|
| Jacobian-first axial | 9 | 3 | 12 | STRUCTURAL-COUNT-DERIVED |
| BBD | 15 | 3 | 18 | STRUCTURAL-COUNT-DERIVED |
| FCCCD | 17 | 3 | 20 | STRUCTURAL-COUNT-DERIVED |
| Stage-2 2-factor quadratic | 11 | 3 | 14 | STRUCTURAL-COUNT-DERIVED |

### Conditions

These floors assume eligible Stage-0 center growths are reused in the fitted design rather than consumed as nonreusable pilots.

## Still open

- selected design branch;
- actual Stage-0 reuse eligibility;
- usable material outline per root;
- physical descendant packing;
- source/morphology failure rate;
- statistically powered root count;
- source-history/split-plot expansion;
- whether downstream descendants can all be supplied from selected roots.

States:

`ROOT-INVENTORY-OPEN`, `PHYSICAL-AREA-OPEN`, `POWER-REPLICATION-OPEN`.

---

# 4. P06 genealogy gap

P06 is non-destructive and can normally measure the intact parent before subdivision.

The **method is closed** as a genealogy strategy.

Still open:

- whether the future instrument beam/stage can map the actual as-grown parent without prior cutting;
- actual coordinate-registration uncertainty after later subdivision.

This does not create a material-consumption gap unless real geometry prevents intact-parent mapping.

---

# 5. P05 compatibility gap

Current conservative branch:

`intact parent/P06 -> split -> dedicated P05 material-control descendant + contact-free process/device descendants`.

Why open:

- exact Hall contact material/process remains local;
- contact preparation changes specimen state;
- compatibility with later Hg anneal/RIE/device processing is not demonstrated.

Required closure evidence:

1. freeze Hall contact process;
2. compare treated versus untouched matched specimens through the intended later process;
3. show no material effect on optical/Hall/device response beyond allocated uncertainty;
4. define contact removal/retention if reuse is intended.

State:

`P05-DOWNSTREAM-COMPATIBILITY-OPEN`.

Until closed, P05 consumes a dedicated descendant role.

---

# 6. F3 anneal material gaps

## Structural relation closed

`N_treat,F3 = N_B + N_J + N_H + N_C + N_X`.

For a four-factor first-order n-like axial fit:

`N_J,fit = 11` treatment histories.

## Open

- number of active boundary-search histories `N_B`;
- exact anneal experimental unit: independently sealed ampoule/run versus another qualified definition;
- number of specimens per ampoule;
- between-position effects inside one ampoule;
- pre-state branch material burden;
- held-out history count beyond current minimum logic;
- detector bridge descendant count;
- power/variance replication.

States:

- `TREATMENT-UNIT-DEFINITION-OPEN`;
- `DESCENDANT-FOOTPRINT-OPEN`;
- `HOLDOUT-MATERIAL-OPEN`;
- `POWER-REPLICATION-OPEN`.

### Anti-confounding risk

Anneal states must not be assigned so that one treatment level occurs only on one LPE root/wafer region.

Current state:

`TREATMENT-ROOT-CONFOUNDING-OPEN` until an actual assignment exists.

---

# 7. F4 RIE material gaps

## Structural count closed

For `k_R` independently controlled RIE factors:

`N_Q,fit = 2 k_R + 3`.

For `k_R=4`, fitted chamber-treatment structure is 11.

## Treatment bundle not yet physically closed

Every important RIE treatment may require multiple within-run structures:

- oxide-clear/physical-recession witness;
- Hall/converted-sheet-state coupon;
- LBIC/depth/lateral conversion structure;
- TLM/contact structure;
- detector descendant(s).

The precise number/area depends on actual structure geometry and whether methods can be combined on one piece without altering the response.

State:

`TREATMENT-BUNDLE-LAYOUT-OPEN`.

## Detector burden remains open

Round 45 explicitly does not require complete detector fabrication for every early RIE treatment. The number of detector-bearing states is an information-value decision after material-state results.

State:

`POWER-REPLICATION-OPEN / DETECTOR-DESCENDANT-COUNT-OPEN`.

---

# 8. Passivation branch gap

P25/passivation should branch from a frozen incoming RIE/material state using sibling descendants.

Open:

- number and geometry of sibling devices/coupons per surface state;
- whether RIE x passivation interaction is large enough to justify cross-product treatment states;
- process-state compatibility with later metal/device testing.

Do not inflate material counts by assuming a full factorial before interaction information exists.

---

# 9. P10-P13/F1 material gaps

## Structural sharing rule closed

One completed detector may supply matched P10/P11/P12/P13 and F1 field-response data when all measurements are qualified as reversible/low-loading.

F1 therefore has a conditional incremental material floor of zero once suitable detector descendants exist.

## Open

- final number of independent detector descendants needed to estimate between-device variance;
- whether one measurement causes persistent thermal/optical/electrical state change;
- exact pre-package versus post-package measurement order;
- device failure rate.

States:

`POWER-REPLICATION-OPEN`, `STATISTICAL-RESERVE-OPEN`.

---

# 10. F5 package material gaps

## Closed structurally

- non-HgCdTe surrogate package-family screening: zero HgCdTe dies;
- one actual independent package build consumes one completed detector die absent qualified reversible rework;
- repeated thermal cycles/pulses are not independent package builds;
- >=3 distinct bondline thickness levels are needed to identify quadratic curvature in thickness.

## Open

- number of independent builds per level;
- package-build yield;
- number of holdout package builds;
- actual die outline/package fixture footprint;
- availability of matched detector descendants.

States:

`POWER-REPLICATION-OPEN`, `STATISTICAL-RESERVE-OPEN`, `DESCENDANT-FOOTPRINT-OPEN`.

---

# 11. Singulation / edge-exclusion gap

P35 establishes the qualification method but no local final edge exclusion exists.

Before material packing can close, required local values include:

- selected singulation method;
- kerf/wander distribution;
- `d_functional`;
- released `d_release` including uncertainty/margin;
- handling/fixture margin;
- die orientation.

State:

`SINGULATION-EDGE-EXCLUSION-OPEN`.

This can make nominal area calculations materially optimistic, so no final area budget is released in Round 45.

---

# 12. Holdout protection gap

Round 45 distinguishes model-fit material from true held-out confirmation material.

Required physical closure:

- F2 LPE holdouts must be new independent growths;
- F3 holdout independence must match the actual anneal experimental-unit definition;
- F4 RIE holdouts must be independent chamber treatments;
- F5 package holdouts must be independent package builds;
- F1 interpolation holdout may be a new within-device field state when the validation question is local response interpolation.

Until IDs/material are reserved:

`HOLDOUT-MATERIAL-OPEN`.

---

# 13. Destructive-witness gap

Depth profiling, cross-sectioning or failure analysis can permanently terminate a descendant.

Round 45 requires a dedicated destructive role before execution.

Until physical descendants are reserved:

`DESTRUCTIVE-WITNESS-OPEN`.

A destructive method is not allowed to consume the sole remaining detector bridge/holdout by default.

---

# 14. Physical area / packing gap

Material feasibility requires actual expanded descendant polygons, not only counts.

Open inputs:

- usable parent outline;
- Hall coupon dimensions;
- LBIC/TLM/test-structure dimensions;
- detector die dimensions;
- package handling allowance;
- streets/kerf/wander;
- P35 release exclusion;
- crystallographic orientation.

State:

`DESCENDANT-FOOTPRINT-OPEN` + `PHYSICAL-AREA-OPEN`.

Closure method:

CAD/polygon packing inside each measured usable parent.

---

# 15. Reserve/yield gap

No physical yield data exist.

Therefore no justified reserve percentage exists.

Round 45 freezes separate reserve categories:

- process failure;
- metrology failure;
- layout/singulation loss;
- holdout allocation;
- destructive FA;
- power-based replication.

State:

`STATISTICAL-RESERVE-OPEN` + `POWER-REPLICATION-OPEN`.

Once empirical success probability and confidence objective exist, use a binomial or genealogy-aware correlated model.

---

# 16. P16G closure map

`P16G-MATERIAL-GENEALOGY-PLAN-READY = YES` requires at minimum:

1. F2 root design selected;
2. Stage-0 reuse decisions frozen;
3. actual root inventory identified;
4. usable outlines and descendant CAD packing pass;
5. P05 reuse/dedicated branch frozen;
6. anneal experimental unit and treatment assignment frozen;
7. RIE treatment-bundle layout frozen;
8. P10-P13/F1 shared detector allocation frozen;
9. actual package die allocation frozen;
10. holdouts protected;
11. destructive witnesses protected;
12. treatment-root confounding audit passes;
13. structural material balance closes;
14. reserve/power terms explicitly open or empirically justified.

Current:

`P16G-MATERIAL-GENEALOGY-PLAN-READY = NO / NOT PHYSICALLY INSTANTIATED`.

---

# 17. Maturity status

Round 45 changes no project maturity state.

A structural genealogy plan is not:

- physical material availability;
- P16F campaign readiness;
- empirical verification;
- P16E allocation completion;
- P16A first-build readiness;
- P17 release.
