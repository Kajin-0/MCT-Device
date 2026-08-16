# P22B — first-build descendant genealogy and HgCdTe material-allocation planning

**Status:** CONTROLLED PRE-EXPERIMENT PLANNING METHOD / ROUND 45  
**Date:** 2026-08-16 America/New_York  
**Use with:** P21, P22/P22A, P23, P24/P25, P33/P35, P05/P06/P10-P13, P16F/P16G.

## 1. Purpose

Design the physical sample genealogy that allows the Round-44 empirical-Jacobian campaigns to execute with minimum HgCdTe consumption while preserving:

- correct experimental-unit independence;
- matched-descendant covariance;
- holdout integrity;
- destructive-analysis reserve;
- process-state traceability;
- physical layout/edge-exclusion feasibility.

P22B does not prescribe actual coupon dimensions, material inventory or final sample size before a real laboratory/tool/material state exists.

---

# 2. Planning principle

The program is a directed acyclic genealogy graph, not a flat sample list.

`growth -> material map -> split -> irreversible treatment branches -> device descendants -> package descendants`.

The core conservation rule is:

> Split at the latest common process state compatible with all intended descendants.

The core statistics rule is:

> Physical descendants inherit their parent genealogy; physical separation does not create upstream statistical independence.

---

# 3. Required sample-role labels

Every planned piece receives exactly one current primary role plus optional secondary measurement roles.

- `ROOT-GROWTH` — independent P03 LPE experimental unit.
- `PARENT-MATERIAL` — intact grown material before branch split.
- `MATERIAL-CONTROL` — P05/Hall or other transport coupon.
- `ANNEAL-TREATMENT` — one irreversible P23 anneal history.
- `RIE-STATE-WITNESS` — Hall/LBIC/depth/recession witness associated with one chamber treatment.
- `TLM-CONTACT-WITNESS` — contact-specific structure.
- `DETECTOR-BRIDGE` — completed detector intended for P10-P13/P11/P12 bridge.
- `PACKAGE-BUILD` — detector committed to one P33/F5 package construction.
- `HOLDOUT` — specimen excluded from model fitting until prediction is frozen.
- `ARCHIVE` — retained reference material.
- `DESTRUCTIVE-FA` — specimen explicitly allocated for destructive analysis.
- `CONTINGENCY-RESERVE` — uncommitted material held against a stated future risk.

A specimen may change role only by logged disposition.

---

# 4. Measurement compatibility matrix

Use the following default until local qualification changes it.

| Operation | Consumption class | Can precede another use on same specimen? | Default genealogy treatment |
|---|---|---|---|
| P06 FTIR map | OBSERVATIONAL-ND | yes | run on intact parent before split |
| optical/CD microscopy | OBSERVATIONAL-ND | yes | shared |
| P05 Hall acquisition with already-qualified contacts | CONDITIONALLY-ND | yes | shared only inside Hall branch |
| P05 contact fabrication | PROCESS-ALTERING | not assumed | dedicated material-control branch |
| P10 DC/bias | CONDITIONALLY-ND | yes if heating/reversibility gate passes | same detector as P11-P13 |
| P11 responsivity | CONDITIONALLY-ND | yes if optical loading linear/reversible | same detector |
| P12 noise | CONDITIONALLY-ND | yes | same detector |
| P13 temporal/frequency | CONDITIONALLY-ND | yes if low-injection/thermal gate passes | same detector |
| Hg anneal | PROCESS-ALTERING | creates new state | branch point before anneal |
| wet mesa/anodization/RIE/metal | PROCESS-ALTERING | creates new state | branch before different process variants |
| singulation | GEOMETRY-CONSUMING | yes on descendants | exact parent-child IDs mandatory |
| package attach/interconnect | PROCESS-ALTERING | not assumed reversible | one die committed per package build |
| cross-section/destructive depth/FA | DESTRUCTIVE | no | dedicated terminal branch |

Any deviation from this matrix requires a local compatibility record.

---

# 5. Root-growth allocation

For each F2 design, first freeze the required independent-growth rows.

Current structural fitted-design options:

- F2 Jacobian-first: 9 growths;
- F2 BBD: 15 growths;
- F2 FCCCD: 17 growths;
- P22 Stage-2 quadratic: 11 growths.

Current P21 validation policy adds at least three held-out growth states.

Therefore the branch-specific validated-growth lower bounds are:

- 12;
- 18;
- 20;
- 14;

respectively, only when eligible Stage-0 center growths are reused rather than discarded as pilots.

These are **root-count lower bounds**, not physical-area sufficiency claims.

### Stage-0 reuse gate

Before reusing a pilot center as a formal design center, confirm:

- same boat/source/process revision;
- same intended center;
- same P06 method/model version or validated equivalence;
- no response-based selective inclusion;
- preserved raw data/genealogy;
- design matrix updated prospectively.

Otherwise assign `PILOT-NONREUSABLE`.

---

# 6. Root material mapping before consumption

For each root growth:

1. assign root ID before removal from the growth apparatus;
2. record full P03/P30 process history;
3. map usable outline/morphology;
4. perform P06 map on intact material where geometry permits;
5. register physical coordinate system and crystal orientation;
6. create a preliminary CAD descendant layout;
7. identify proposed cut streets/edge exclusions;
8. only then release the parent for subdivision.

This preserves the strongest possible material-state map before geometry is consumed.

---

# 7. Descendant-layout feasibility

For every parent define:

- usable polygon;
- excluded edge/morphology zones;
- coordinate system;
- growth/slider direction;
- crystallographic orientation;
- minimum handling margin.

For every descendant define the expanded footprint including:

- active piece geometry;
- cut street;
- kerf/wander allowance;
- P35 functional edge-exclusion allowance;
- fixture/mounting allowance;
- orientation requirement.

A layout is accepted only after a CAD/polygon packing check shows all descendant footprints fit without overlap inside the usable parent.

Do not infer feasibility from nominal area alone.

---

# 8. F2 material-response genealogy

The immediate P21 response can be obtained from the intact P06-mapped parent. Therefore do not automatically dice every F2 growth into full detector sets.

Classify each F2 growth after material-response acquisition:

- `FIT-MATERIAL-ONLY`;
- `FIT-BRIDGE-SELECTED`;
- `HOLDOUT-MATERIAL-ONLY`;
- `HOLDOUT-BRIDGE-SELECTED`;
- `MORPHOLOGY-FAIL/BOUNDARY`;
- `ARCHIVE`.

Only bridge-selected roots proceed to detector descendants unless later information value justifies more.

For every bridge-selected root, reserve enough compatible material for at least:

- a material-control branch;
- a detector branch.

Archive/destructive branches are separate allocations.

---

# 9. F3 anneal genealogy

## 9.1 Treatment experimental unit

Each unique anneal trajectory/history is an independent **anneal treatment history** only when independently executed or otherwise justified by the furnace/ampoule experimental-unit definition.

Multiple pieces in one sealed ampoule that experience the same thermal/Hg history are within-treatment specimens, not automatically independent anneal runs.

Record:

- ampoule/run ID;
- sample-zone positions;
- sibling/root IDs;
- T_s(t), T_Hg(t);
- source state;
- cooldown history.

## 9.2 Conservative pre-state branch

Until Hall-contact compatibility with anneal is qualified:

- use P06 on the actual treatment parent;
- use one matched sibling/root-region for detailed P05 pre-state where necessary;
- keep the treatment parent contact-free;
- after anneal, split the treated parent into post-anneal Hall and detector descendants if material permits.

This avoids contaminating the anneal chemistry with an unqualified Hall contact process.

## 9.3 Boundary and n-like allocations

Keep three separate pools:

- classifier/boundary pool;
- stable n-like Jacobian pool;
- held-out validation pool.

Do not consume every boundary sample into full detector fabrication. Detector descendants are highest value near:

- the selected robust n-like center;
- a controlled margin challenge;
- one or more states needed to bridge Hall state to P11/P12/P13.

---

# 10. F4 RIE treatment bundles

The chamber run/treatment is the default independent RIE unit.

A single chamber run may deliberately co-process a **bundle** containing:

1. oxide-clear/recession witness;
2. converted-sheet/Hall witness;
3. LBIC/depth/lateral structure;
4. TLM/contact witness;
5. detector structure(s).

All bundle members share the chamber-run ID and are within-run descendants.

### Minimum-structure versus full detector burden

The Jacobian-first RIE fit requires `2k_R+3` independent chamber treatments. That does not imply `2k_R+3` completed detectors are required initially.

Use staged allocation:

- Stage R1: process-state witness on every treatment;
- Stage R2: detector fabrication on selected informative treatment states;
- Stage R3: independent held-out detector state(s).

This minimizes full-stack consumption while retaining the actuator->state->device chain.

### Chamber-position effect

If multiple pieces are co-loaded, map chamber position. Within-run spatial variation is a separate variance component and shall not be mistaken for independent treatment replication.

---

# 11. Passivation/sidewall branch

The P25/passivation study should branch from a frozen incoming RIE/material state.

Allocate matched sibling devices/coupons to the selected surface/passivation treatments.

Avoid a large cross-product design until Round-44 information analysis shows the RIE x passivation interaction materially affects the protected detector decision.

Every surface-state descendant retains both upstream RIE treatment and passivation treatment IDs.

---

# 12. P10-P13 detector sharing

A completed detector that remains within low-injection/self-heating/reversibility gates should carry a common measurement sequence rather than be split into separate detectors for each metric.

Preferred common detector record:

1. geometry/CD and package state;
2. P10 low-field/DC/self-heating qualification;
3. P11 responsivity/spectral response;
4. P12 noise under the matched state;
5. P13 dynamic response;
6. repeat critical P10 baseline to detect measurement-induced drift.

The exact order may be adjusted to protect the most sensitive measurement, but one device should normally produce the matched P10-P13 state required by the repository.

### F1 reuse

Run the F1 field-derivative sequence on one or more of these already-completed detectors.

No separate F1 material allocation is required unless existing descendants cannot support the canonical state.

---

# 13. F5 package genealogy

Before package commit, record the detector's pre-package baseline.

Then:

`D_pre -> package build P -> D/P_post`.

The same physical die provides the paired comparison.

Each independent package build consumes one detector die. A package cannot be counted twice as two independent builds because it experienced multiple cooldown cycles or was remounted in the same construction.

Use non-HgCdTe surrogates for family screening before committing real detector dies.

---

# 14. Holdout integrity

Every campaign holdout must be labeled before outcome inspection where practicable.

A holdout may share an upstream root with fit specimens when the statistical question permits blocked validation, but it may not share the exact irreversible treatment event whose reproducibility is under test if that would destroy independence.

Examples:

- a held-out F2 LPE state requires a new independent growth;
- a held-out RIE chamber treatment requires a new chamber run;
- a held-out package build requires a new package assembly;
- an interior F1 field holdout may be a new field point on the same device when validating local interpolation, because detector is the experimental unit and field is repeated measure.

---

# 15. Destructive-analysis policy

Before any destructive measurement:

1. verify a dedicated `DESTRUCTIVE-FA` descendant exists;
2. confirm it is not the only remaining holdout/detector-bridge specimen;
3. document expected decision value;
4. record exact pre-destruction state;
5. preserve images/data and terminal disposition.

If no dedicated destructive witness exists, destructive analysis requires explicit deviation review.

---

# 16. Contingency reserve policy

Do not use an arbitrary percentage reserve.

Separate reserve causes:

- `R_PROCESS` — process failure;
- `R_METROLOGY` — unusable measurement/contact/fixture;
- `R_LAYOUT` — unusable area/kerf/edge damage;
- `R_HOLDOUT` — independent confirmation;
- `R_FA` — destructive diagnostic;
- `R_POWER` — additional independent units required after variance estimation.

Until yield/variance data exist, these remain explicit open terms rather than one guessed multiplier.

When empirical success probabilities exist, use the binomial or a genealogy-aware correlated-yield model to size the reserve at a declared confidence.

---

# 17. Material-conservation optimization objective

For a candidate genealogy plan `G`, define conceptually

`J_material = C_growth N_growth + C_area A_consumed + C_detector N_full_detector + C_package N_package + C_destructive N_destructive`

subject to:

- design rank/conditioning;
- information target;
- holdout requirements;
- treatment independence;
- layout feasibility;
- morphology/physics feasibility;
- EH&S/infrastructure constraints.

The coefficients are not assigned numerically until real material/tool costs exist.

The purpose is to make explicit that a plan minimizing number of coupons may still waste more high-value detector descendants than a slightly larger material-control campaign.

---

# 18. Anti-pseudoreplication checks

Before approving a plan answer:

1. Are map points being counted as growth replicates? If yes, reject.
2. Are sibling coupons being counted as independent LPE runs? Reject.
3. Are co-loaded RIE coupons being counted as independent chamber treatments? Reject.
4. Are repeated field points being counted as independent devices? Reject.
5. Are repeated thermal cycles being counted as independent package builds? Reject.
6. Is treatment perfectly aliased with root growth/wafer position? Redesign/block.
7. Has a single physical run been duplicated in two design matrices as if two independent observations? Correct the information matrix.

---

# 19. Required P16G outputs

Before `P16G-MATERIAL-GENEALOGY-PLAN-READY = YES`, the future laboratory must provide:

- selected F2 design and root count;
- actual parent dimensions/usable polygons;
- planned descendant layout/CAD for each root class;
- sample-role tree;
- P05 compatibility branch;
- F3 ampoule/treatment-unit definition;
- F4 chamber-treatment bundle definition;
- detector-sharing plan for P10-P13/F1;
- package-build die allocation;
- holdout IDs;
- destructive witness IDs;
- reserve categories;
- proof no treatment is unintentionally confounded with root genealogy;
- current terminal material balance.

---

# 20. Promotion rule

P22B/P16G can close a material plan structurally before empirical yield is known, but only as:

`STRUCTURAL-GENEALOGY-READY`.

It shall not be promoted to:

- statistically powered campaign;
- process capability;
- yield release;
- first-build ready;

until P16F/P16E/P17 requirements are met.
