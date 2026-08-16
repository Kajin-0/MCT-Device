# Checkpoint — after first-qualification-build branch integration Round 40

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round 40 objective

Round 40 followed the documentary-saturation conclusion from Round 39.

Instead of creating another process addendum, it audited all 36 P16A rows and asked:

> What is the strongest **single coherent candidate first qualification build** supported by the controlled literature, and which fields are irreducibly local?

The result is a new integration register:

`travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`.

P16B is not a physical-process SOP and does not replace P16A.

---

## 2. Central result

The repository has passed a significant transition.

For most major fabrication stages, the literature now supports a preferred **process architecture/family** and often a quantitative first-screen center:

- Cd0.96Zn0.04Te `(111)B` substrate family;
- Honeywell covered horizontal-slider LPE topology;
- xL=.082 / yL=.810 / TL=507 °C / xS≈.29 composition center;
- N2 purge -> flowing H2 LPE atmosphere family;
- 250 °C / 1 h / Hg-saturated anneal first screen;
- AZ4620 historical Mask-1 transfer candidate, without assuming modern product equivalence;
- Srivastav `2% Br2 / 3:1 EG:HBr` wet-mesa center with basis kept open;
- TI 0.1-mol-KOH/L anodization center;
- direct RP-01 Mask-2 4–5 µm / 80 °C 30 min / chlorobenzene 30 min functional state;
- candidate CH4:H2=1:5 RIE split with direct 64-sccm total;
- direct Cr 30 nm / Au 270 nm stack with thermal evaporation as the strongest same-UWA method family;
- low-force wire-saw first singulation screen;
- compliant silicone-family first die-attach screen;
- shared ~80-K / 10-V/cm reference state for key detector performance.

The remaining uncertainty is increasingly **local apparatus/material realization**, not lack of a process family.

---

## 3. Selected safe derived quantities

### LPE composition after local Mcharge selection

For the Honeywell composition center:

- `w_Hg=.249740`;
- `w_Cd=.012502`;
- `w_Te=.737758`.

Therefore:

`m_Hg=.249740 Mcharge`  
`m_Cd=.012502 Mcharge`  
`m_Te=.737758 Mcharge`.

The literature does not determine `Mcharge`.

### RIE candidate split

For total 64 sccm and 1:5 CH4:H2:

- `Q_CH4=10.6667 sccm`;
- `Q_H2=53.3333 sccm`.

These remain derived candidate local nominal values, not historical MFC records.

### Anodization KOH inventory

0.1000 mol KOH at 56.1056 g/mol gives:

`5.61056 g` pure KOH per stated 1-L solvent batch.

For assay fraction `a_KOH`:

`m_reagent=5.61056/a_KOH g`.

The 90:10 EG:H2O solvent-basis convention remains unresolved and must be selected explicitly before execution.

---

## 4. Cross-module decisions frozen in P16B

### P29 -> P30

Substrate physical dimensions remain subordinate to actual boat/recess selection. Do not buy a nominal 10×10×1-mm substrate and then force a boat around it merely because one transfer paper used that size.

### P30 -> P31

Use measured as-grown P05/P06 state before anneal. No high-temperature defect-conditioning step is inserted by default.

### P32 -> P28 -> P25

Mask-1, wet etch and anodization are a single surface-state trajectory. The project no longer treats each as independently optimizable.

### P25 -> P27 -> P08

Mask-2 developer/profile must preserve the anodic oxide and survive the actual RIE exposure.

### P08 -> P26

No undocumented interface clean is inserted. RIE-to-Cr elapsed time/atmosphere and Cr-to-Au vacuum history are recorded.

### P26 -> P35 -> P33

Singulation and package construction are detector processes. A completed device cannot inherit deep bulk-CdZnTe saw-damage etches as a generic post-dice clean.

### P10 -> P13

Performance quantities are combined only at matched or explicitly corrected detector ID/contact pair/gap/T/field/package/background state.

---

## 5. Twenty irreducible local identity/calibration groups

P16B identifies the following minimum local set that literature cannot honestly fill:

1. actual CdZnTe supplier/lot and measured crystallographic/material state;
2. executable final pre-LPE surface recipe and clean-to-load realization;
3. dimensioned LPE boat/furnace/tube/actuator;
4. numerical total LPE charge and auxiliary Hg source;
5. actual LPE gas-delivery/purity/pressure instrumentation;
6. calibrated LPE thermal/contact/wipe/cooldown trajectory;
7. FTIR and Hall apparatus/calibration chains;
8. Hg-anneal enclosure/reservoir geometry and measured Ts/THg trajectory;
9. Mask-1 resist/coater/aligner/developer/strip;
10. explicit wet-etch concentration/ratio bases and HBr assay;
11. wet-etch rinse/air/anodization handoff;
12. anodization solvent basis/cell/electrochemical area;
13. Mask-2 resist/developer/exposure/lift-off branch;
14. CH4/H2 gas delivery and calibrated MFCs;
15. RIE reactor/sheath/thermal/chamber-state implementation and oxide clear;
16. Cr/Au deposition tool/vacuum/source/QCM/rate/thermal implementation;
17. CD/TLM/bias/radiometry/noise/temporal metrology tools and transfer functions;
18. singulation tool/protection/clean/street implementation;
19. cryogenic attachment/interconnect/window/shield/vacuum construction;
20. package survival and later process-capability data.

These should be treated as local engineering specification/calibration tasks, not as invitations for endless historical searching.

---

## 6. Files created in Round 40

- `travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND40.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND40.md`
- this checkpoint.

P16A formal row states were deliberately not promoted.

---

## 7. Readiness after Round 40

Formal state remains:

- `TRACEABLE-FIRST-BUILD-READY = NO`;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

The improvement is architectural: the open rows now have one preferred evidence-ranked branch instead of a large uncontrolled option space.

---

# 8. Strongest next action — Round 41

Proceed with a **minimum laboratory capability / implementation specification package** derived from P16B.

The user cannot perform physical experiments in this project, so Round 41 should maximize what can be closed analytically before a future laboratory exists.

Create an integrated capability/specification layer that answers, for each irreducible local group:

1. what apparatus or consumable must exist;
2. what minimum physical capability/range is required by the selected P16B branch;
3. what fields must be specified at procurement/selection time;
4. what calibration is required before HgCdTe material is consumed;
5. what witness/surrogate can be used for non-destructive or non-HgCdTe commissioning where scientifically valid;
6. what values **cannot** be specified until the actual tool is present;
7. what downstream modules accept/reject the capability;
8. what EH&S/facility dependencies exist as separate institutional gates.

Prioritize the critical-path apparatus groups:

- LPE furnace/boat/gas/actuator;
- Hg anneal furnace/ampoule/reservoir;
- FTIR/Hall material metrology;
- lithography tools;
- RIE;
- Cr/Au deposition;
- 77–80-K electrical/optical/noise test infrastructure;
- singulation;
- package/Dewar.

Do **not** shop for a commercial tool or choose a vendor model unless the task later specifically calls for procurement research. First define the physics-based minimum capability envelope.

Suggested artifact:

`docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`

plus a fillable controlled register/traveler if useful.

Round 41 should update source/gap/checkpoint/AGENTS and link back to P16B.