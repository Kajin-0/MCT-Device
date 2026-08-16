# Checkpoint — after Mask-2 / Mask-1 lithography documentary-limit Round 39

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round 39 objective

Round 39 began with P16A R16 / Mask-2 because RP-01 provides an unusually restrictive process fingerprint but omits the commercial resist/developer/lift-off identities.

The round was explicitly instructed to avoid a redundant P27A if P14A/P27 already contained a complete local closure method.

After Mask-2 reached its current documentary limit, the round followed the recorded pivot to P16A R12 / Mask-1.

---

## 2. Mask-2 audit result

Direct RP-01 fingerprint remains:

`4–5 µm resist -> 80 °C / 30 min prebake -> chlorobenzene 30 min -> patterned/developed/water rinse -> CH4/H2 RIE -> Cr 30 nm / Au 270 nm -> lift-off`.

Still not recovered:

- resist manufacturer/product;
- solids/viscosity/dilution;
- spin speed/acceleration/time;
- exposure tool/wavelength/mode/dose;
- developer product/concentration/time;
- chlorobenzene bath temperature/purity/agitation;
- exact exposure/chlorobenzene ordering beyond the wording of RP-01;
- lift-off solvent/time/agitation.

### P27 completeness decision

P14A/P27 and the P27 traveler already control all variables needed to instantiate a local branch:

- product/lot;
- coating/thickness;
- RP-01 bake/chlorobenzene centers;
- ordering branch;
- dose/developer matrix;
- developed profile/undercut;
- P08 survival;
- P26 metal compatibility;
- lift-off;
- TLM/device closure.

Therefore **no P27A was created**.

This is a deliberate anti-duplication decision, not a claim that R16 is closed.

R16 remains `OPEN-CHOICE`.

---

## 3. John White thesis archival lead

Official UWA repository record:

John White, *Mid-wave infrared HgCdTe photodiode technology based on plasma induced p-to-n type conversion*, PhD, 2005.

The official record exposes a PDF download link and the thesis is directly relevant to UWA HgCdTe RIE/passivation device processing.

The current PDF request returns `403 Forbidden` through the available retrieval route.

State:

`IDENTIFIED-NOT-RECOVERED`.

Do not conclude the thesis lacks photoresist/developer/lift-off details.

---

## 4. Mask-1 audit result

P32 was audited after the Mask-2 pivot.

Direct RP-01 gives only the function:

- Mask 1 photolithographically delineates the wet-etched detector mesa;
- mesa isolation precedes anodic oxide.

Exact UWA Mask-1 resist/lithography/strip remains unpublished in the recovered RP-01 record.

### Srivastav primary text

The full author-uploaded 2005 Srivastav paper was re-read through the experimental procedure.

It directly states:

- two photolithographic masks were used;
- 600-µm linear features / 50-µm trenches in one mask;
- 2-D mesas / 30-µm trenches in the other;
- photoresist thickness, feature area and HgCdTe film thickness influence profile/anisotropy;
- edge trenching occurs near photoresist boundaries;
- elevated etch temperature attacks/deteriorates photoresist;
- lower temperature improves resist survival/profile control.

It does **not** identify:

- resist product;
- resist thickness actually used;
- spin/bake;
- exposure;
- developer;
- strip.

Thus Srivastav cannot close R12 product identity.

---

## 5. Product-identified transfer branch retained

`CN101740502B` remains the strongest product-identified HgCdTe Br2/HBr Mask-1 transfer branch:

- commercial `AZ4620`;
- resist `3 µm`;
- 5-µm opening;
- Br2:HBr explicit volume-ratio family;
- example 0.5%:1;
- DI-water clean;
- acetone strip.

This is useful product/chemistry-family evidence but not RP-01 and not P28's Br2/EG/HBr bath.

---

## 6. Current-product continuity warning

Current commercial/vendor documentation for AZ P4620 places the product in a normal thickness range of roughly `5–30 µm`, whereas the older primary HgCdTe patent explicitly used `3 µm` AZ4620.

Round 39 does not know whether the difference reflects:

- formulation generation;
- product grade;
- dilution;
- spin conditions;
- documentation convention;
- or another process difference.

Permanent consequence:

`same commercial name != demonstrated formulation/process equivalence across decades`.

A current AZ P4620 lot must be treated as a new local branch, not as literal reproduction of the patent embodiment.

---

## 7. P32 completeness decision

P32 already controls:

- product/lot selection;
- coating/exposure/development;
- AZ4620 Br2/HBr transfer candidate;
- Hunt 180CP historical deep-HgCdTe transfer;
- thick positive novolak control;
- P28-coupled resist survival;
- empirical lithographic + wet-etch mask bias;
- through-layer/isolation endpoint;
- resist strip;
- P25 surface-state handoff;
- detector-level closure.

Therefore **no P32A was created**.

R12 remains `OPEN-CHOICE`.

---

## 8. Round-39 controlled files

Created:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND39.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND39.md`
- this checkpoint.

No new physical-process procedure was created because P27 and P32 already cover the required local qualification states.

The absence of a new procedure is itself a controlled conclusion: procedure proliferation would not close the remaining branch-selection problem.

---

## 9. Readiness state after Round 39

No readiness row is promoted merely by this source audit.

Important states remain:

- R12 Mask-1 = `OPEN-CHOICE`;
- R16 Mask-2 = `OPEN-CHOICE`;
- R21 lift-off = `OPEN-CHOICE`;
- R20 metallization apparatus = `APPARATUS-NOT-SELECTED`;
- R13 wet-mesa chemistry = `UNDEFINED-BASIS`.

Overall:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`.

---

## 10. Documentary-saturation conclusion

Rounds 35–39 have exposed an important project transition.

For many first-build blockers, the repository now has a scientifically controlled **closure method**, but the row remains open because no actual laboratory branch/tool/product has been selected.

Examples:

- P30A -> actual LPE apparatus/charge branch still absent;
- P28A -> actual wet chemistry definition still absent;
- P25A -> actual anodization cell/electrolyte still absent;
- P26A -> actual metallization tool still absent;
- P27/P32 -> actual commercial resist/tool/developer branches still absent;
- P34 -> actual RIE reactor/gas manifold still absent.

Continuing to create another addendum for every unresolved historical number would now produce paperwork rather than execution closure.

---

# 11. Strongest next action — Round 40

Proceed with **first-qualification-build branch integration / documentary saturation audit**.

Goal:

Convert the 36-row P16A readiness register from a list of independent open choices into a single coherent **literature-defined candidate first-build branch matrix**.

Round 40 should:

1. audit all 36 P16A rows and classify each unresolved coordinate as one of:
   - `DIRECT-RP01-EXECUTABLE`;
   - `PUBLISHED-TRANSFER-CENTER-AVAILABLE`;
   - `LOCAL-TOOL-IDENTITY-REQUIRED`;
   - `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`;
   - `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`;
   - `HISTORICAL-IDENTITY-ONLY`;
2. for each `PUBLISHED-TRANSFER-CENTER-AVAILABLE` row, choose one defensible **candidate first-build branch** from already controlled literature, with source/provenance and exact numerical values where the source genuinely gives them;
3. never promote a candidate transfer value to historical RP-01 identity;
4. never invent tool-specific values such as actual furnace gradients, MFC calibration, QCM tooling factors, sample temperatures, vacuum base pressure or optical view factors;
5. explicitly identify the smallest set of coordinates that cannot be specified from literature and therefore require a real laboratory identity/calibration;
6. build a master `FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER` or equivalent integration file rather than another physical-process SOP;
7. check cross-module compatibility: P28->P25 surface state, P25->P27, P27->P08, P08->P26, P26->P35/P33, and P10–P13 shared detector state;
8. calculate any safe arithmetic consequences only after a branch is selected and label them `DERIVED`;
9. preserve all readiness states unless the selection is truly sufficient under P16A definitions;
10. update checkpoint/source/gap/AGENTS.

The purpose is to move from **“we know how a future lab would close every row”** toward **“here is the strongest coherent first qualification build that the published record supports, and here are the irreducible laboratory-specific blanks.”**
