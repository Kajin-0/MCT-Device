# Checkpoint — after Cr/Au deposition apparatus / provenance Round 38

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round 38 objective

Close as much of P16A R20 as primary literature permits without duplicating P09/P09A/P26 or inventing a historical metal-deposition recipe.

Targeted coordinates:

- deposition method;
- tool/source hardware;
- base/process pressure;
- Cr/Au rates;
- QCM/thickness calibration;
- source/sample geometry;
- substrate thermal state;
- actual RIE-to-metal load-lock use;
- Cr-to-Au vacuum history;
- lift-off details.

---

## 2. Main historical result

The RP-01 paper directly closes:

- Cr `30 nm`;
- Au `270 nm`;
- Mask-2 lift-off compatibility;
- TLM geometry;
- `rho_c≈9×10^-4 Ω·cm²` at 80 K.

It does **not** identify the deposition method, apparatus, rates, pressure, source geometry, sample temperature or lift-off chemistry.

Therefore the historical deposition traveler remains `OPEN-HISTORICAL`.

---

## 3. Same-UWA method-family result

Two 1998 UWA HgCdTe photovoltaic papers explicitly state that contact metal was deposited by **angled thermal evaporation**.

This is close in laboratory lineage and time to RP-01.

Correct evidence upgrade:

`thermal evaporation = strongest SAME-UWA method-family candidate`.

Incorrect inference:

`RP-01 Cr/Au was angled-thermally evaporated`.

The 1998 devices differ in material/growth/doping/contact geometry, and their angle is itself a designed geometry variable.

---

## 4. RP-01 load-lock interpretation corrected/frozen

RP-01 describes a vacuum-processing capability obtained by allowing the RIE chamber to be connected via a load lock to the metal-deposition system and identifies that architecture as beneficial.

The recovered experimental text does not state that the reported experimental devices actually used that connected load-lock path.

Permanent evidence class:

`DIRECT-RP01-PROPOSED-ARCHITECTURE`.

Do not claim zero historical air exposure.

---

## 5. Same-team bridge sources

Still identified but detailed process text not recovered:

1. Musca/Smith/Dell/Faraone 1999, “Performance and stability of HgCdTe photoconductive devices: A study of contact and passivation technology.”
2. Smith/Winchester/Musca/Dell/Faraone 2000, “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors,” SIMC-XI, pp. 318–321.

These remain high-value archival targets but should not be repeatedly rediscovered through generic searches.

State:

`IDENTIFIED / BIBLIOGRAPHICALLY CLOSED / EXPERIMENTAL TRAVELER NOT RECOVERED`.

---

## 6. Documentary limit after Round 38

No primary UWA source recovered exact RP-01:

- evaporator/deposition method;
- tool model;
- Cr boat/source;
- Au boat/source;
- source/sample distance;
- deposition angle;
- Cr rate;
- Au rate;
- base pressure;
- process pressure;
- QCM/tooling factor;
- wafer temperature;
- actual load-lock use on measured devices;
- Cr-to-Au vacuum-break state;
- lift-off solvent/time/agitation.

Do not substitute common cleanroom practice for those values.

---

## 7. New controlled layer

Created:

- `procedures/P26A_CR_AU_DEPOSITION_APPARATUS_INSTANTIATION_ADDENDUM.md`
- `travelers/P26A_CR_AU_DEPOSITION_APPARATUS_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND38.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND38.md`
- this checkpoint.

Updated:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`.

AGENTS refresh follows.

---

## 8. P26A purpose

P26 already records each metallization run and its physical/electrical results.

P26A instead creates a **master apparatus revision** and freezes:

`X_dep = {tool/revision, chamber/pumps/gauges, source stations, source hardware/materials, source-sample geometry, holder/thermal contact, rotation/tilt, QCM geometry/tooling factors, pressure state, rate branches, thermal calibration, RIE transfer, Cr-Au vacuum history}`.

This prevents the operator from selecting unstated equipment conditions at run time.

---

## 9. P26A qualification states

1. `METHOD-FAMILY-SELECTED`
2. `TOOL-REVISION-DEFINED`
3. `VACUUM-CHAIN-DEFINED`
4. `SOURCE-HARDWARE-DEFINED`
5. `GEOMETRY-DEFINED`
6. `THICKNESS-METROLOGY-QUALIFIED`
7. `THERMAL-LOAD-CALIBRATED`
8. `RIE-CR-HANDOFF-DEFINED`
9. `CR-AU-SEQUENCE-DEFINED`
10. `P26-APPARATUS-READY`
11. `P26-LOCAL-QUALIFIED`

`P26-APPARATUS-READY` means the tool can execute a controlled qualification run without hidden equipment choices.

`P26-LOCAL-QUALIFIED` additionally requires P26 outcome gates.

---

## 10. Thickness and rate rules

Direct targets stay fixed for first transfer:

- Cr `30 nm`;
- Au `270 nm`.

Cr and Au require separate QCM/witness calibration unless empirical data justify a shared tooling factor.

Historical Cr and Au rates remain open.

Several-Å/s Au rates in other primary HgCdTe contact studies remain transfer-scale evidence only.

Never copy the Au rate to Cr.

---

## 11. Thermal-load rule

A 300-nm total metal deposition can heat the HgCdTe/CdZnTe/resist assembly.

P26A requires a dummy/surrogate thermal calibration for the actual source/sample/holder geometry when direct wafer thermometry is unavailable.

Keep:

- holder temperature;
- sample/proxy temperature;
- sensor lag/uncertainty

separate.

No intentional post-metal anneal belongs to the baseline unless separately qualified.

---

## 12. Readiness state after Round 38

Still:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`

Specific rows:

- R20 remains `APPARATUS-NOT-SELECTED`.
- R21 remains `OPEN-CHOICE`.

P26A is a closure method, not a filled apparatus specification.

R20 may move to `LOCAL-BRANCH-FROZEN` only after an actual laboratory P26A register reaches `P26-APPARATUS-READY` and all first-build coordinates are under change control.

---

# 13. Strongest next action — Round 39

Proceed with **P16A R16 / Mask-2 resist, exposure, developer, chlorobenzene and lift-off historical/transfer closure**.

Reason:

- RP-01 has an unusually restrictive process fingerprint: `4–5 µm resist -> 80 °C / 30 min prebake -> chlorobenzene 30 min -> pattern/develop/water rinse -> CH4/H2 RIE -> 30/270-nm Cr/Au -> lift-off`;
- P27 already identifies positive DNQ/novolak chlorobenzene-lift-off families and candidate thick AZ families;
- product/exposure/developer identity may still be recoverable through UWA theses, 1990s Australian microfabrication papers, process appendices or same-lab device papers;
- R16 remains a true execution blocker because a product/exposure/developer branch is not frozen.

Round 39 should:

1. audit P14/P14A/P27 and P27 register before searching;
2. search UWA theses/papers/proceedings from the Smith/Musca/Siliquini/Dell/Faraone fabrication lineage for resist manufacturer/product, spin conditions, exposure tool/dose, developer, chlorobenzene ordering/temperature and lift-off solvent;
3. exploit the unusual `4–5 µm + 80 °C/30 min + chlorobenzene 30 min` fingerprint rather than generic HgCdTe lithography searches;
4. distinguish exact UWA evidence from historical chlorobenzene-lift-off transfer families;
5. determine whether RP-01 wording places chlorobenzene before or after UV exposure and whether same-lab text resolves `patterned`;
6. do not identify AZ4330/AZ4400/AZ4620 merely by thickness match;
7. if product identity remains open, create a P27A local resist/developer/exposure instantiation layer only if it adds something materially different from the existing P27 run register;
8. update R16 only when a real local branch is physically/product-wise frozen;
9. keep R21 lift-off coupled to P27/P26; do not invent acetone/NMP/ultrasonics;
10. record negative searches and prevent repeated candidate-name guessing.

**Pivot rule:** if P27 already contains a complete local instantiation framework and no new primary UWA evidence is recovered, do not create a redundant P27A. Pivot to R12/Mask-1 product/process closure and use the same empirical-first discipline.
