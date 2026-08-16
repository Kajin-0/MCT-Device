# RP-01 sample genealogy / material-allocation calculation

**Status:** CONTROLLED DERIVED CALCULATION / ROUND 45  
**Date:** 2026-08-16 America/New_York  
**Use with:** P21, P22/P22A, P23, P24/P25, P33/P35, P05/P06/P10-P13, P16F/P16G.

## 1. Purpose

Convert the Round-44 empirical-campaign architecture into a quantitative genealogy/material-accounting framework without inventing:

- actual HgCdTe inventory;
- coupon dimensions;
- wafer/coupon yield;
- power-based final replication;
- destructive-analysis burden;
- process-failure reserve.

The calculation distinguishes four quantities that must not be conflated:

1. **independent experimental units** needed for model identifiability;
2. **physical descendant pieces** consumed from those units;
3. **usable material area/footprint** needed to place those descendants;
4. **statistical reserve** needed after yield/variance are known.

A single LPE growth can generate many descendant coupons/dies, but those descendants do not become independent LPE replicates.

---

# 2. Genealogy notation

Use the following node types.

- `G[g]` — independent LPE growth/root material unit.
- `M[g]` — intact as-grown HgCdTe/CdZnTe parent after P03 and P06 map.
- `C[g,r]` — coupon/region `r` cut from growth `g`.
- `A[g,r,a]` — coupon after one irreversible Hg-anneal history `a`.
- `R[g,r,a,q]` — coupon/structure after one RIE treatment/chamber run `q`.
- `D[g,...,d]` — completed detector die.
- `P[g,...,p]` — packaged detector build.
- `X[g,...,x]` — destructive cross-section/failure-analysis witness.

A genealogy edge represents physical descent, not statistical independence.

Example:

`G -> M --P06--> M -> split -> {C_Hall, C_anneal, C_device, C_archive}`.

The correct branch point is the **latest common state before an irreversible treatment**.

---

# 3. Measurement/process consumption classes

## `OBSERVATIONAL-ND`

Normally does not consume or intentionally alter the specimen state.

Examples:

- P06 FTIR transmission mapping;
- calibrated optical microscopy;
- non-contact dimensional/surface metrology where qualified.

P06 is explicitly non-destructive and should therefore be performed on the intact parent before subdivision whenever geometry permits.

## `CONDITIONALLY-ND`

Measurement can reuse the same specimen only while self-heating, optical injection, bias history, contamination and handling are demonstrated negligible/reversible.

Examples:

- P10 DC/bias;
- P11 calibrated responsivity;
- P12 noise;
- P13 low-injection temporal/frequency response.

These four measurements should preferentially share one completed detector and matched state.

## `PROCESS-ALTERING`

Creates a new irreversible process state even if the specimen remains physically intact.

Examples:

- Hg anneal;
- wet mesa;
- anodization/passivation;
- RIE conversion;
- Cr/Au deposition/lift-off;
- package attach/interconnect.

## `GEOMETRY-CONSUMING`

Consumes parent geometry or creates independent pieces.

Examples:

- couponing;
- singulation/dicing;
- cleaving.

## `DESTRUCTIVE`

Specimen cannot remain a detector descendant afterwards.

Examples where applicable:

- destructive cross-section;
- destructive composition/depth analysis;
- destructive pull/shear or failure-analysis sectioning.

### P05 special rule

P05 electrical acquisition itself need not destroy a Hall coupon, but the required four-contact van-der-Pauw specimen/contact preparation changes the surface/geometry state. Therefore a P05 coupon is **not automatically reusable as a detector or anneal descendant**. Same-coupon reuse is allowed only after the Hall-contact process is demonstrated compatible with the later process history.

Default genealogy accounting therefore treats P05 as a dedicated material-control branch.

---

# 4. Delayed-differentiation rule

To conserve scarce HgCdTe and maximize matching:

> Delay physical splitting until immediately before descendants require different irreversible histories.

Examples:

- perform P06 on one intact grown parent before cutting Hall/device/anneal pieces;
- anneal one sufficiently large parent coupon first, then split it into post-anneal Hall and detector descendants if geometry/process compatibility allows;
- for one RIE chamber treatment, co-load sibling structures needed for Hall/LBIC/TLM/device outputs and treat them as one treatment bundle, not independent chamber replicates;
- perform P10-P13 on one completed detector before package if fixture geometry permits, then repeat selected measurements on the same detector after package.

This preserves common-mode covariance while minimizing physical material use.

---

# 5. F1 field-derivative campaign material demand

Round 44 defines repeated field states on one completed detector.

For one detector:

`E_- -> E_0 -> E_+` (with counterbalanced/repeated centers)

can identify an **individual-device** local field slope.

Therefore:

- mathematical physical-device floor for one within-device slope: `N_D,F1 = 1`;
- mathematical floor to estimate a between-device slope variance component: `N_D,F1 >= 2`;
- statistically credible/power-based device count: `OPEN`.

F1 normally requires **zero incremental HgCdTe devices** when suitable completed detector descendants already exist from F4/F5 or first-build qualification.

Do not create a separate F1 lot solely because the field points are numerous; field points are repeated measures, not independent detector units.

---

# 6. F2 LPE structural growth counts

The following counts are design-matrix counts of **independent growths**.

| F2 design branch | fitted independent growths `N_fit` | current P21 holdout policy | minimum validated-growth count if Stage-0 centers are reusable |
|---|---:|---:|---:|
| 3-factor Jacobian-first axial + 3 centers | 9 | >=3 held-out growths | >=12 |
| 3-factor BBD + 3 centers | 15 | >=3 | >=18 |
| 3-factor FCCCD + 3 centers | 17 | >=3 | >=20 |
| 2-factor Stage-2 quadratic | 11 | >=3 | >=14 |

The P21 holdout set currently includes at least:

1. center confirmation;
2. interior combined perturbation;
3. feasible near-margin confirmation.

These counts do **not** include nonreusable pilot/Stage-0 growths.

Define:

`N_G,F2,total = N_fit + N_holdout,new + N_stage0,nonreusable`.

Stage-0 center growths may be reused as model centers only if:

- the apparatus/process block is unchanged;
- their center state is exactly the frozen design center;
- acquisition/model versions remain compatible;
- inclusion was not selectively decided from response outcome;
- the adaptive design record explicitly carries them into the information matrix.

Otherwise they remain pilot data and are additional material.

### Row reuse across F2 submodels

One physical growth may contribute to more than one fitted model when its realized state is legitimately a row in each design.

It still counts as **one independent growth**, not two.

Therefore separate Stage-1/Stage-2 run counts shall not be blindly added until overlapping center/axial states are reconciled in one master design matrix.

---

# 7. F2 descendant pieces do not equal growth count

Every F2 growth requires P06 material response, but P06 consumes no additional piece when performed before splitting.

Only selected growths need downstream descendants for the P06->P11 detector bridge.

For each selected bridge growth `g`, define roles:

- `H_g` — material-control/P05 descendant;
- `D_g` — detector descendant for P10-P13;
- `A_g` — archive/reference descendant, optional but recommended;
- `X_g` — destructive depth/FA witness only when justified.

Under the conservative default that P05 contact preparation is not downstream-compatible, a selected bridge growth needs at least two physically distinct descendant roles:

`{H_g, D_g}`.

This is a **piece-role requirement**, not an independent-growth requirement.

If a qualified same-specimen Hall/device route is later demonstrated, the role count may be reduced under change control.

---

# 8. F3 anneal campaign material equation

Every unique irreversible anneal history consumes a distinct treatment specimen/history.

Define:

- `N_B` = boundary/classifier treatment histories;
- `N_J` = stable n-like local-Jacobian treatment histories;
- `N_H` = held-out anneal histories;
- `N_C` = dedicated control/reference histories;
- `N_X` = destructive validation histories.

Then

`N_treat,F3 = N_B + N_J + N_H + N_C + N_X`.

The boundary component `N_B` remains sequential/information-driven and has no justified fixed total before data exist.

### Continuous n-like Jacobian structural option

If `k_A` continuous anneal descriptors are estimated with a first-order axial design plus three centers:

`N_J,fit = 2 k_A + 3`.

For the currently contemplated four descriptors

`{T_dwell, t_dwell, Hg-source/chemical-potential coordinate, cooldown coordinate}`

this gives a **structural fitted-design size of 11 treatment histories**.

This does not include boundary search, holdouts or power-based replication.

### Matching strategy

A treatment history can be applied to one sufficiently large parent coupon and subdivided *after* anneal into:

- post-anneal P05 material-control coupon;
- detector-fabrication descendant;
- optional archive/destructive witness.

This is preferable to annealing all descendants separately when the objective is a common anneal history.

However, P23 requires pre-state information. Two branches are allowed:

1. `SAME-COUPON-PRESTATE` — only if Hall contacts/prestate measurements are proven compatible with anneal and later processing;
2. `MATCHED-SIBLING-PRESTATE` — conservative default: a neighboring sibling supplies the P05 pre-state while the treatment parent remains contact-free.

The second branch consumes more physical material but protects process validity.

---

# 9. F4 RIE/passivation treatment bundles

Round 44 gives the Jacobian-first RIE structural design:

`N_Q,fit = 2 k_R + 3`

where `k_R` is the number of **independently controllable RIE treatment factors**.

For `k_R=4`,

`N_Q,fit = 11` independent chamber treatments.

Add:

`N_Q,total = 2 k_R + 3 + N_Q,holdout + N_Q,stage0,nonreusable + N_Q,stability`.

No numerical value is assigned to the latter terms yet.

### Treatment-bundle principle

The independent unit is the **chamber treatment/run**, not each coupon co-loaded in that run.

One treatment bundle may contain sibling structures for:

- oxide-clear/recession witness;
- variable-field Hall / converted sheet-state witness;
- LBIC/depth/lateral-conversion structure;
- TLM/contact structure;
- completed detector descendant.

These structures increase material footprint but not independent treatment count.

### Staged detector descendants

It is not automatically efficient to fabricate a complete detector for every early RIE treatment.

Recommended staged logic:

1. all treatment runs acquire plasma/process-state + minimum material-state witnesses;
2. detector descendants are fabricated for the center, high-information contrasts and explicit holdouts selected by P16E/P16F;
3. once actuator->material-state response is established, expand detector descendants only where needed to identify material-state->device response.

This avoids spending full detector fabrication on RIE states already shown to be irrelevant or infeasible.

### Passivation

Passivation/oxide/sidewall state is a separate treatment block. Do not create an uncontrolled full RIE x passivation factorial solely to reuse material.

Use matched sibling descendants from selected RIE states and preserve the two-stage genealogy.

---

# 10. F5 package material demand

Surrogate package screening can use non-HgCdTe materials and therefore has

`N_HgCdTe,F5,surrogate = 0`.

Once one construction family is selected, each actual independent package build requires one completed detector die unless a separately qualified reversible package/rework route exists.

Thus:

`N_D,F5 = N_package_builds`.

Repeated thermal pulses or repeated thermal cycles on one package are within-build observations and do not increase independent package-build count.

### Bondline-thickness model structure

- linear thickness effect: at least two distinct thickness states are needed for rank;
- curvature: at least three distinct thickness states are needed;
- independent build variance/power: additional replicate builds remain `OPEN`.

Do not call three packages a sufficient statistical release sample merely because three levels identify curvature.

### Paired reuse

One detector die should preferentially provide:

`pre-package P10/P12/P13 -> package build -> post-package P10/P12/P13`

and P11 where optical geometry permits.

This gives paired change estimates and consumes one detector, not two.

---

# 11. Cross-campaign sharing means totals are not additive

Program material shall be represented as a DAG, not

`N_total = N_F1 + N_F2 + N_F3 + N_F4 + N_F5`.

Examples:

- F1 uses completed detector descendants from F4/F5;
- F3 coupons may descend from selected F2 growths;
- F4 incoming material may descend from annealed F2/F3 parents;
- F5 uses detector descendants already fabricated for F4/device bridge work;
- P10-P13 share the same detector.

Therefore the independent-growth count satisfies only a lower-bound relation such as

`N_G,program >= N_G,F2,unique`

when all downstream material can physically be allocated from those F2 roots.

Under the current P21 holdout policy, conditional lower bounds are therefore:

- Jacobian-first F2 branch: `>=12` independent growth roots;
- BBD F2 branch: `>=18`;
- FCCCD F2 branch: `>=20`;
- Stage-2-only branch: `>=14`.

These are **independent-growth structural lower bounds only**. They are not claims that the entire program can physically fit on that amount of grown area.

Additional growths are required whenever descendant footprint, yield, blocking, holdout independence, or material-state matching cannot be satisfied by those roots.

---

# 12. Physical area feasibility

For parent growth `g`, define the usable polygon after excluding unusable edge/morphology regions:

`Omega_usable,g`.

For every planned descendant role `r`, define a required layout polygon including:

- active coupon/die footprint;
- cut street;
- kerf uncertainty;
- functional edge exclusion from P35;
- handling/fixture margin;
- orientation constraint.

Call this expanded polygon `Omega_r+`.

The exact CAD/layout feasibility condition is

`area(union_r Omega_r+) <= area(Omega_usable,g)`

with all polygons non-overlapping and satisfying crystallographic/orientation constraints.

A scalar area sum alone is insufficient when packing/orientation matters.

### No current numeric area budget

Round 45 cannot assign a numerical material-area requirement because the following are still local/open:

- actual grown usable outline;
- Hall coupon footprint/contact geometry;
- detector die outline;
- cut street/kerf;
- P35 functional edge exclusion;
- LBIC/TLM/witness layouts;
- package handling dimensions.

These become P16G fields.

---

# 13. Statistical reserve after yield exists

Structural design count is not production/material reserve.

If a required descendant role has independent success probability `p` and at least `r` successful descendants are needed, then for `n` planned descendants

`Pr(K>=r) = 1 - sum_{k=0}^{r-1} C(n,k) p^k (1-p)^(n-k)`.

Once empirical `p` exists, choose `n` to satisfy the declared confidence/yield objective.

Do not assign `p` from intuition.

For a multi-stage path with stage yields `p_s`,

`p_path = product_s p_s`

only under a justified independence model. Correlated wafer/process failures require genealogy-aware empirical estimation.

Therefore Round 45 records:

- `N_structural`;
- `N_holdout`;
- `N_archive`;
- `N_destructive`;
- `N_failure_reserve`;
- `N_power_replication`

as separate terms.

Only `N_structural` is partly closed analytically today.

---

# 14. Independence hierarchy

Permanent rules:

1. multiple P06 map points on one growth are not independent growths;
2. multiple coupons from one growth are not independent LPE replicates;
3. multiple annealed sibling coupons can be independent anneal treatment histories but share a growth block;
4. multiple coupons in one RIE chamber run are within-run witnesses, not independent RIE treatments;
5. multiple field points on one detector are repeated measures;
6. repeated P10-P13 acquisitions on one device are measurement repeats;
7. repeated pulses/cycles on one package are within-package observations;
8. separate package assemblies are independent package-build units even when blocked by common growth, subject to package-fixture/tool genealogy.

Every model shall analyze at the correct unit level.

---

# 15. Treatment balance across upstream roots

Material conservation must not create complete confounding.

Bad design example:

- all low anneal states from Growth A;
- all high anneal states from Growth B.

This aliases treatment with growth.

Where multiple upstream roots are available, distribute downstream treatment levels across roots/wafer positions so that:

- treatment contrasts occur within blocks where possible;
- growth/position can be estimated or conditioned out;
- one treatment is not perfectly aliased with one material root.

The same rule applies to RIE/passivation/package branches.

---

# 16. Archive and destructive witnesses

An archive piece is scientifically useful but is not automatically part of the strict identifiability floor.

Recommended archive priority:

- candidate process center;
- each major upstream material block;
- anomalous/failure states of high diagnostic value.

Destructive witnesses shall be created deliberately before consuming a detector-capable descendant.

No destructive cross-section or chemical depth analysis shall be taken from the only remaining bridge/holdout descendant unless the decision value exceeds the loss and is documented.

---

# 17. Minimum genealogy metadata

Every physical descendant must retain:

- root growth ID;
- parent piece ID;
- wafer/growth coordinate/orientation;
- split/singulation timestamp and method;
- all irreversible process histories in order;
- co-treatment/chamber/ampoule/package-build IDs;
- measurement-state IDs;
- whether it is fit, center, holdout, archive, reserve or failure-analysis material;
- whether it remains eligible for detector fabrication;
- current physical dimensions/remaining area;
- terminal disposition.

No descendant may be relabeled an independent root because it was physically separated.

---

# 18. Round-45 controlled conclusions

1. P06 should normally precede subdivision because it is non-destructive.
2. P05 requires dedicated-role accounting unless Hall-contact compatibility with later processing is proven.
3. P10-P13 should share one completed detector state where measurement loading is qualified.
4. F1 generally adds no HgCdTe consumption once suitable completed devices exist.
5. F2 validated structural growth floors are branch-dependent: 12/18/20/14 under the current three-holdout policy and reusable Stage-0-center assumption.
6. F3 unique anneal histories consume unique treatment specimens; a 4-factor n-like first-order axial fit would structurally use 11 fit histories, but boundary search/holdout/power remain open.
7. F4 has `2k_R+3` fitted chamber-treatment structural size; co-loaded coupons are treatment-bundle witnesses, not independent runs.
8. F5 actual package builds consume one detector die each; surrogate package screening consumes no HgCdTe.
9. Cross-campaign material totals must be calculated from the genealogy DAG, not by adding campaign sample counts.
10. Physical grown-area requirement remains open until actual layout/kerf/edge-exclusion footprints are frozen.
11. Yield/failure/power reserve remains open until empirical data exist.

Round 45 therefore closes the **accounting architecture and branch-specific structural counts**, not the final amount of HgCdTe that must be procured or grown.
