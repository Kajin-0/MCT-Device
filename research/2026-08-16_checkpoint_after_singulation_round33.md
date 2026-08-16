# Research checkpoint — after Round 33 singulation / die-edge closure

**Date:** 2026-08-16 America/New_York

## Executive state

Round 33 identified and closed a real documentation/process-architecture gap between completed frontside detector fabrication and P33 packaging.

Before this round:

- P15 contained only a generic singulation qualification placeholder;
- P16 STEP G1 referred to P15 without an empirical execution window;
- P33 assumed an already-singulated/clean die;
- P18 had no dedicated singulation failure branch.

Round 33 therefore created a new controlled fabrication module:

- `procedures/P35_HGCDTE_CZT_SINGULATION_DIE_EDGE_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P35_SINGULATION_DIE_EDGE_EMPIRICAL_QUALIFICATION_REGISTER.md`

This is the first new top-level empirical process module since P34.

---

# 1. Historical RP-01 status

The audited Smith et al. 2001 paper does not disclose an executable singulation traveler.

Still `OPEN-HISTORICAL`:

- method: blade / wire / scribe-cleave / laser;
- final die outline;
- cut streets;
- edge exclusion;
- tool model/settings;
- temporary support/protection;
- coolant/slurry;
- post-cut clean;
- edge-damage acceptance.

Do not backfill these values from another II–VI process.

---

# 2. Strongest HgCdTe-specific dicing evidence

Rockwell US5214261 directly discusses dicing HgCdTe detector arrays.

It identifies diamond-grit blade saw dicing as the conventional branch of the period and specifically records problems with:

- chipping/fracturing;
- local friction heat;
- electrical-component degradation;
- dimensional accuracy/buttable edges.

Its excimer branch demonstrates that functional detector degradation can be mapped versus distance from diced edge.

The patent's tested architecture gives approximate no-measured-degradation distance ranges of:

- mechanical saw: about `9–19 µm`;
- excimer: about `0–6 µm`.

These are **transfer data only** and are not P35 exclusion values because the patented device is a sapphire/CdTe/HgCdTe array rather than LPE HgCdTe/CdZnTe RP-01.

Permanent new distinction:

`d_visible != d_functional != d_release`.

---

# 3. Strongest finished-CdZnTe execution branch

Yoo, Jennings and Montano 1998 provide a concrete singulation process on an already metallized CdZnTe detector array:

- sample about `1×1 cm`;
- low-melting-point wax to graphite support;
- whole-surface photoresist protection;
- `125 mm` stainless-steel wire saw;
- `16 µm` boron-nitride slurry;
- extremely slow cut, approximately `1 h` per complete cut;
- subsequent wall-damage treatment and cleaning.

This is the strongest current practical low-force wire-saw branch.

It is **not** an RP-01 recipe.

In particular, its subsequent `5% Br/methanol / 5 min` wall etch must not be transplanted onto a completed ~9.5-µm HgCdTe photoconductor with anodic oxide, RIE contact conversion and Cr/Au.

---

# 4. Subsurface damage is now a first-class process variable

Szeles et al. 2006 describe production CdZnTe detector fabrication where even low-damage wire-saw processing was followed by approximately `100 µm` material removal to eliminate surface/subsurface saw damage; blade slicing/dicing was described as requiring several hundred micrometres in that bulk-crystal flow.

These depths are not applicable removal allowances for RP-01.

Their value is the warning:

**visible chips/roughness do not bound subsurface damage.**

P35 therefore requires a destructive or validated non-destructive subsurface-damage study during branch qualification.

---

# 5. Laser branch has a different failure axis

US5018164 shows that excimer ablation of II–VI material can change residual surface stoichiometry as a function of fluence/pulse history.

Therefore:

`low mechanical force != zero device damage`.

A P35 laser branch must qualify:

- geometry/chipping;
- redeposition;
- near-edge Hg/Cd/Te state where practical;
- passivation/metal damage;
- detector electrical/noise/responsivity state.

No CdTe fluence value from the patent is an HgCdTe P35 setting.

---

# 6. P35 process architecture

Candidate branches:

A. precision abrasive blade saw;  
B. low-force wire saw;  
C. scribe/cleave;  
D. laser/excimer.

Scribe/cleave inherits P29 plane/polarity/miscut and defect state.

Controlled input vector:

`X_SING={method,tool/revision,crystal orientation,street/protection/support,abrasive-or-laser state,motion state,coolant/slurry,pass sequence,tool age/conditioning,clean/release,handling}`.

Controlled output vector:

`Y_SING={kerf,width/position accuracy,die dimensions/squareness,front/back chips,crack depth/length,subsurface damage,edge roughness/taper,residue,passivation/metal damage,Delta_R/I-V,Delta_noise,Delta_responsivity,cryogenic survival}`.

---

# 7. Two-stage P35 release

### Stage 1

`SINGULATION-ROOM-TEMP-QUALIFIED`

Requires:

- protection/support compatibility;
- dimensional/edge inspection;
- clean/residue control;
- subsurface-damage evidence appropriate to current qualification stage;
- functional electrical/noise preservation;
- safe handoff to P33.

### Stage 2

`RP01-SINGULATION-QUALIFIED`

Requires P33 package/cooldown feedback:

- no chip/crack propagation;
- no fracture initiated at cut edge;
- no correlated electrical/noise/responsivity loss.

Thus room-temperature appearance alone cannot release singulation.

---

# 8. New permanent rules

1. Singulation is a detector fabrication process, not neutral handling.
2. Exact RP-01 singulation remains open.
3. No visible chip does not prove no subsurface damage.
4. Preserve visible, functional and released edge-exclusion distances separately.
5. Deep Br saw-damage removal from bulk CdZnTe is not a finished-RP-01 clean.
6. Protection/support materials are process variables and need completed-stack compatibility.
7. Tool age/dressing/wire state is genealogy.
8. Coolant/slurry chemistry/age/exposure is genealogy.
9. Laser separation requires chemistry/stoichiometry qualification in addition to mechanical qualification.
10. Scribe/cleave requires P29 crystallographic inheritance.
11. P35 must feed forward to P33 thermal-cycle survival.
12. Functional pre/post noise/responsivity can reveal edge damage that optical inspection misses.

---

# 9. Negative search / source recovery

Same-UWA searches across publicly indexed UWA repository records did not recover an executable dicing/singulation traveler.

Potential high-value archival sources remain:

- Siliquini 1995 thesis;
- White 2005 thesis;
- Westerhout 2013 thesis;
- Musca/Smith/Dell/Faraone internal photoconductor process records;
- Fermionics material/die delivery documentation;
- original device mask/layout/package notebook.

Not recovered does not mean nonexistent.

---

# 10. Files created in Round 33

- `procedures/P35_HGCDTE_CZT_SINGULATION_DIE_EDGE_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P35_SINGULATION_DIE_EDGE_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND33.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND33.md`
- `research/2026-08-16_checkpoint_after_singulation_round33.md`

`AGENTS.md` must be refreshed after this checkpoint.

---

# 11. Strongest next action

Proceed with **Round 34: end-to-end P16 reproducibility / release-readiness audit** rather than immediately inventing another process module.

The process now contains empirical execution layers for the major fabrication bottlenecks through singulation and package handoff. The next useful question is:

**Which remaining OPEN variables actually prevent a competent laboratory from attempting a traceable first local build, and which are historical-identity gaps that can legitimately be replaced by explicit local qualification?**

Round 34 should:

1. audit every P16 phase against the latest P24–P35 empirical layers;
2. classify each unresolved item as:
   - `HISTORICAL-IDENTITY-ONLY`,
   - `EXECUTION-BLOCKER`,
   - `RELEASE-BLOCKER`,
   - `LOCAL-QUALIFIABLE`;
3. update P16 references so P35 owns singulation execution;
4. identify missing travelers/data fields;
5. generate a first-build readiness matrix;
6. distinguish `TRACEABLE-FIRST-BUILD-READY` from `HISTORICAL-RP01-REPRODUCED` and from final `REPRODUCIBLE-RELEASE`.
