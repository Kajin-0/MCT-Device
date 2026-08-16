# P07A — CdZnTe final pre-LPE surface-preparation addendum

**Status:** CONTROLLED TRANSFER-CANDIDATE UPDATE to `P07_CZT_SUBSTRATE_QUALIFICATION.md`.

## 1. Problem

P07 closes how the CdZnTe substrate should be characterized, but the exact final surface-preparation sequence used by the RP-01/Honeywell x≈0.30 LPE lineage remains unresolved.

This addendum records the strongest detector-oriented LPE surface-preparation candidate recovered so far without falsely promoting it into the RP-01 historical recipe.

## 2. Primary detector/LPE transfer source

A published HgCdTe detector-process source from the Military University of Technology reports:

- CdZnTe substrate composition around 4 mol% Zn;
- orientation `(111)B`;
- dimensions approximately `10 × 10 × 1 mm`;
- chemical and mechanical polishing before the final etch;
- final etch in approximately `2–3% bromine in methanol`;
- exposure for **a few seconds**;
- immediate loading into the graphite LPE boat after surface preparation.

The same source uses Te-rich LPE for long-wave HgCdTe active layers around x≈0.20–0.22.

### Evidence status

This is:

`CANDIDATE-P / LPE-CZT-SURFACE-PREP / DIFFERENT-COMPOSITION-BRANCH`.

It is not evidence that the Honeywell x≈0.30 or Fermionics RP-01 material used exactly 2–3% Br2/MeOH for the same time.

## 3. Why this candidate is physically relevant

A Br2/methanol final etch is widely used to:

- remove mechanically damaged near-surface CdZnTe;
- remove native contamination/oxide;
- expose a fresh surface immediately before epitaxy.

However, bromine/methanol treatment can also:

- alter surface stoichiometry;
- expose Te precipitates or polishing inclusions;
- leave a surface condition that evolves with air exposure.

Therefore concentration, removed depth and clean-to-load delay are coupled process variables.

## 4. Supporting substrate-characterization evidence

Modern CdZnTe substrate studies show that Br:methanol surface preparation can reveal pre-existing near-surface features such as Te precipitates and residual silica polishing particles. This reinforces the P07 rule that a visually smooth as-received substrate is not necessarily a clean epitaxy-ready surface.

Do not treat a post-etch increase in visible nanoscale features automatically as damage created by the etch; qualification should distinguish newly exposed substrate defects from etch-generated morphology.

## 5. Initial local qualification structure

For RP-01-compatible x≈0.30 material, qualify final pre-LPE surface treatment as a DOE rather than adopting the LWIR recipe unchanged.

### Candidate center family

Use Br2/methanol chemistry in the detector-LPE literature as a starting family.

Variables to qualify:

- bromine concentration;
- solution preparation basis;
- bath temperature;
- immersion time;
- agitation;
- substrate orientation/face;
- methanol rinse sequence;
- any DI-water rinse, if used;
- dry method;
- clean-to-load elapsed time.

### Mandatory outputs

Measure/record:

- surface roughness before/after;
- optical/DIC surface image;
- particle/precipitate density;
- removed thickness/depth where possible;
- XPS/surface chemistry on development coupons if available;
- resulting LPE nucleation/morphology;
- interface impurity/defect evidence;
- P05/P06 material state after growth.

The winning surface process is the one that gives the best **grown interface and epilayer**, not simply the lowest roughness immediately after wet etch.

## 6. Clean-to-load clock

The exact RP-01 limit remains `[QUAL]`, but P16 must continue to record:

`Δt_clean→load`.

A released process should set a maximum interval only after post-growth interface/morphology/electrical data show the sensitivity to delay.

## 7. What remains open

Still not recovered for the exact x≈0.30 Honeywell/Fermionics lineage:

- final substrate chemistry;
- bromine concentration;
- removed depth;
- rinse sequence;
- dry method;
- maximum air exposure before load;
- whether an in-situ meltback followed the ex-situ clean;
- exact A/B face and miscut used for the historical RP-01 starting material.

Therefore this addendum narrows the transfer candidate but does **not** close the P07 historical recipe.
