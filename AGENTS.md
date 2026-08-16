# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** executable by a competent researcher without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains direct historical anchors, empirical transfer procedures, metrology SOPs, qualification travelers, failure/release architecture and explicit unresolved gaps.

---

# Non-negotiable scientific/provenance rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, explicit derivation, or a named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01, same-lineage, transfer-family, model, derived, apparatus-calibration and local-qualification evidence.
4. Every critical process step needs output metrology and a pass/fail/qualification gate.
5. Preserve negative searches, failed branches, rejected inferences, corrections and source conflicts.
6. Use measured fabricated geometry for field, active area and D* normalization.
7. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density, `rho_c` and minority-carrier blocking metrics distinct.
8. Treat passivation, post-RIE exposure, wet-etch surface exposure, metal-interface exposure, anneal cooldown, substrate clean-to-load, LPE source genealogy, chamber state and packaging as process variables.
9. Measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Specifications derive from required material/device performance, not observed process spread.
11. Failure diagnosis: signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification.
12. Repository procedures do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S.
13. Every numerical sensitivity/tolerance states protected output, input, operating point and evidence class. Proxies may size experiments but cannot release production specifications.
14. A tie-line ratio such as `xS/xL` is not `dxS/dxL` when other coordinates vary.
15. Coded DOE coordinates do not create physical tolerances.
16. Repeated observations from one melt/source/bath/substrate/anneal-source/chamber/package genealogy are not iid independent replicates.
17. Never regress reciprocal Hall density through a p/n Hall-sign transition; use signed Hall/tensor information near transition.
18. **Empirical/practical literature first.** Before theoretical placeholders, search primary papers, theses, patents, proceedings and institutional archives for real times, temperatures, concentrations, flows, pressures, dimensions, apparatus, metrology settings and outcomes.
19. Theory connects genuine gaps and checks consistency; it does not displace published process data.
20. A successful historical center is not automatically an optimum.
21. Equal anodic-oxide thickness does not imply equal interface state.
22. No undocumented ion mill, wet etch or plasma clean may be inserted between qualified P08 RIE and Cr deposition.
23. Baseline P26 is as-deposited; post-metal anneals from other contact architectures are transfer evidence only.
24. Cryogenic TLM records optical-background/shield state as well as temperature/current.
25. Chlorobenzene constrains Mask-2 to a positive diazo/DNQ-novolak lift-off family but does not identify a resist product.
26. Preserve RP-01 Mask-2 ordering `prebake -> chlorobenzene -> then patterned/developed/water rinse`; do not silently reorder it.
27. A generic developer or lift-off solvent is not automatically historical RP-01 practice.
28. **Wet-etch percentage without basis is not an executable formulation.** Never guess the basis of Srivastav `2% Br2`.
29. Preserve `3:1 EG:HBr` symbolically until preparation basis is recovered or locally defined.
30. HBr stock assay is part of wet-etch chemistry.
31. Br2 bath age/open exposure/run order/cumulative area/agitation are process variables.
32. **Wet-mesa endpoint:** time is an input; measured through-layer isolation is the output.
33. Post-wet-etch air time/surface state are part of the P28->P25 handoff.
34. **CdZnTe vendor label is not interface specification.** Record actual composition/lattice state, plane, polarity, miscut, defects and final surface.
35. A/B polarity, miscut magnitude and azimuth are separate coordinates.
36. Substrate impurity/ingot genealogy follows the epilayer/device; Cu is a high-priority warning analyte.
37. Release substrate surface from resulting LPE interface/material quality, not AFM roughness alone.
38. Clean-to-LPE interval/ambient must be timestamped.
39. **LPE composition is not charge mass.** Absolute inventory requires defined well geometry/mass.
40. Do not average incompatible Harman/Honeywell growth-time branches.
41. Sealed-ampoule source synthesis and in-situ Hg-vapor preparation remain separate branches.
42. CdTe-piece wipe-off and scribed-CdTe-apron wipe-off are separate Honeywell hardware generations.
43. Slider clearance/speed/smoothness/contact/separation temperature are LPE variables.
44. LPE thermal history is `T(t)`, not scalar `Tgrowth`.
45. Hg-source mass/geometry/reuse and melt reuse are repeated-measures genealogies.
46. **Hg anneal is trajectory-defined:** retain `T_s(t)`, `T_Hg(t)`, pHg/source geometry and cooldown.
47. Isothermal `T_Hg≈T_s` and two-temperature `T_Hg<T_s` anneals are separate branches.
48. Hg saturation is a boundary condition, not a universal gram quantity.
49. Controller setpoint is not sample/reservoir temperature until calibrated.
50. Do not copy multi-day bulk anneals onto a ~9.5-µm epilayer.
51. High-T defect/precipitate conditioning and low-T stoichiometry control are separate objectives.
52. Two-zone cooldown relation is part of the anneal recipe.
53. Final n-type Hall sign alone does not release an anneal.
54. **Mask-1 and Mask-2 are different resist functions.**
55. Mask-1 thickness is not a selectivity specification; release from surviving profile and final mesa transfer.
56. AZ4620 is a strong Br2/HBr product-identified transfer candidate, not historical RP-01 identity.
57. Hunt 180CP is a historical deep-through-HgCdTe Br2/methanol branch, not a generic substitute.
58. Resist-product/profile changes reopen P28 dimensional transfer/mask bias.
59. Resist stripping is part of HgCdTe surface processing; acetone from another branch is not historical proof.
60. No default ultrasonics for Mask-1 stripping.
61. **P05 audit rule:** P05 is already the canonical Hall/VdP execution SOP; do not duplicate it without materially new method evidence.
62. **Die attach is a detector variable.** Mechanical compliance, CTE, bondline thermal conductance, cure and noise/electrical state are coupled.
63. Adhesive product identity is not a bondline specification; measure thickness/coverage/voiding/tilt.
64. Honeywell 5-g/40-g thermocompression values are transfer experiment values, not RP-01 setpoints.
65. Package-generated thermal poles can occur on ms-to-hundreds-ms scales; do not assign them to intrinsic lifetime without P33/P13 separation.
66. Thermal-cycle genealogy is not independent replication.
67. Do not transplant p-HgCdTe/FPA interconnect metallurgies into the RP-01 Cr/Au chain without reopening P26/P24.
68. A package is not released by die shear/wire pull alone.
69. **RIE watts are not an ion-energy coordinate.** Record measured dc self-bias or another calibrated sheath/ion-energy proxy for reactor transfer.
70. **RIE physical depth is not electrical conversion depth.** Keep `d_etch`, `d_conv` and `L_conv` separate.
71. **Separate oxide clear from semiconductor exposure:** `t_sem = t_RF - t_clear` only after local `t_clear` is measured.
72. A same-era Plasma Technology RIE80 using 13.56 MHz does not prove RP-01 used RIE80 or 13.56 MHz.
73. Do not infer RP-01 electrode area from `50 W / 0.4 W cm^-2`.
74. RIE chamber clean/seasoning/loading history is a genealogy variable; pre/post-clean runs are not iid replicates.
75. Preserve P29 crystallographic plane/polarity into P34 because primary CH4/H2 HgCdTe data show orientation-dependent etch rate/morphology.
76. Matching `64 sccm / 100 mTorr / 50 W / 60 s` alone is **not reactor equivalence**.

---

# Current checkpoint — READ THIS FIRST

Latest:

`research/2026-08-16_checkpoint_after_rie_reactor_equivalence_round27.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_empirical_packaging_round26.md`
- `research/2026-08-16_checkpoint_after_empirical_mask1_round25.md`
- `research/2026-08-16_checkpoint_after_empirical_hg_anneal_round24.md`
- `research/2026-08-16_checkpoint_after_empirical_lpe_execution_round23.md`
- `research/2026-08-16_checkpoint_after_empirical_czt_substrate_round22.md`
- `research/2026-08-16_checkpoint_after_empirical_wet_mesa_round21.md`
- `research/2026-08-16_checkpoint_after_empirical_lithography_round20.md`
- older checkpoints as needed.

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND27.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND27.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND26.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND26.md`
- older addenda as needed.

---

# Controlled module set

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP
- P06 FTIR composition/thickness
- P07 CdZnTe + P07A/P07B/P07C
- P08 RIE blocking contact + P08A–P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating
- P11 absolute radiometry/responsivity
- P12 noise/PSD/NEP/D* + P12A/P12B
- P13 temporal/frequency response + P13A
- P14 lithography/CD + P14A
- P15 cryogenic package
- P16 master end-to-end traveler
- P17 statistical process capability/release
- P18 failure-analysis/CAPA
- P19 requirements traceability
- P20 analytical sensitivity / requirements allocation
- P21 LPE response-surface / empirical Jacobian
- P22 information-optimal DOE planning
- P23 Hg-anneal state-boundary / local Jacobian
- P24 blocking-contact empirical process window + register
- P25 anodic-oxide empirical process window + register
- P26 Cr/Au metallization/lift-off empirical process window + register
- P27 Mask-2 lithography/lift-off empirical process window + register
- P28 wet-mesa empirical process window + register
- P29 CdZnTe substrate/final-surface empirical process window + register
- P30 Te-rich LPE apparatus/charge/contact/wipe-off empirical process window + register
- P31 Hg-overpressure anneal apparatus/reservoir/trajectory empirical process window + register
- P32 Mask-1/wet-mesa lithography empirical process window + register
- P33 cryogenic die-attach/interconnect/package empirical process window + register
- **P34 CH4/H2 RIE reactor-equivalence empirical process window + register**

P24–P34 are empirical/practical execution layers that supplement earlier physics/metrology modules.

---

# Canonical RP-01 direct anchors — do not drift

## Material
- LPE n-HgCdTe on electrically insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `mu=4.0×10^4 cm²/V·s`
- active thickness `9.5 µm`
- supplier n/mu measurement temperature undisclosed

## Mesa/passivation
- Mask 1 wet chemical mesa delineation before anodic oxide
- native anodic oxide `~800 Å = 80 nm`

## RIE blocking-contact center
- Plasma Technology parallel-plate reactor
- printed `CH4/5H2`
- total `64 sccm`
- `100 mTorr`
- `50 W`
- `60 s`

## Converted region / LBIC
- average converted n `~2.0×10^15 cm^-3`
- mobility `~3.3×10^4 cm²/V·s`
- Hall/resistivity at 80 and 300 K, B to 2 T
- earlier same-lineage ~8-µm n+ conversion under similar conditions
- LBIC square 300×300 µm; Nd:YLF 1.047 µm CW; ~400 mW/cm²; 80 K

Do not combine `2e15 cm^-3` and `8 µm` into one directly measured sheet density.

## Mask-2 / metal / TLM
- resist ~4–5 µm
- prebake 80 °C / 30 min
- chlorobenzene 30 min
- pattern/develop/water rinse
- Cr 30 nm / Au 270 nm
- nine 300×300-µm contacts
- gaps 50–400 µm in 50-µm increments
- `rho_c≈9×10^-4 Ω·cm²` at 80 K

## Detector benchmark
- ~80 K
- stated 60° FOV
- spectral response at 1 kHz
- representative field 10 V/cm
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz
- high-frequency g-r plateau ~24.5 nV/√Hz
- cutoff ~4.4 µm
- BLIP D* ~`2×10^11 cm Hz^1/2/W` at 4 µm
- quoted QE ~70%

---

# P34 — empirical RIE reactor-equivalence state

P34 is now the apparatus/execution layer for P08/P08D/P24.

## Historical state

Direct controller center is closed, but exact historical reactor state remains open:

- model;
- RF frequency;
- powered/grounded area;
- electrode spacing;
- sample holder/loading;
- base pressure;
- pump/throttle;
- individual MFC values;
- chamber clean/season;
- self-bias;
- sample temperature;
- oxide-clear time.

## Same-UWA branches

Keep these separate:

- 1999 mesa branch: `400 mTorr / CH4/5H2 / 0.4 W cm^-2`;
- 1997 vacancy-p x≈.31: `410 mTorr / CH4-H2 / 0.4 W cm^-2`, `d_etch≈0.2 µm`, `d_conv≈1.5 µm`;
- 1998 As-p x≈.29: `340 mTorr / CH4-H2 / 0.4 W cm^-2`;
- 1998 anneal-recovery branch: `400 mTorr / CH4-H2 / 90 W`.

Do not average or splice them into RP-01.

## Semu 1991 direct HgCdTe transfer evidence

Primary CH4/H2 RIE branch:

- total `85 sccm`;
- `20 mTorr`;
- `35 °C`;
- `150 W`;
- dc bias roughly `-360` to `-440 V`.

Explicit example: `15 sccm CH4 / 70 sccm H2 / 20 mTorr / 150 W / -390 V / 35 °C`.

The authors directly associated rough etched surfaces with high RF-induced dc bias and showed gas-ratio dependence of etch rate.

### Consequence

Every local transfer run records self-bias or calibrated ion-energy proxy.

## Elkind/Orloff orientation evidence

CH4/H2 HgCdTe RIE showed strong orientation dependence; short-time rate ordering `(111)B > (100) > (111)A`, with `(111)A` smoother in the reported comparison. Preserve P29 crystallography in RIE records.

## Same-manufacturer hardware-family evidence

A same-era Plasma Technology RIE80 primary publication reports a 13.56-MHz lower powered electrode, base pressure below 0.5 mTorr and platform temperature control.

**Transfer-only:** none of those values is historical RP-01 proof.

## Oxide-clear separation

Define locally:

`t_sem = t_RF - t_clear`.

Measure `t_clear` on the actual P25 oxide. Do not assume all 60 s modifies exposed HgCdTe.

## Reactor-equivalence release vector

`Y_RIE = {t_clear, self_bias(t), T_sample(t), d_etch, morphology, sheet_state, d_conv, L_conv, rho_c, blocking_response, detector_noise_delta}`.

Release only after repeated independent chamber-state preparations reproduce a stable vector and downstream P26/P09/P08F/device closure.

## White 2005 thesis

John Kenion White's UWA thesis has been positively identified; current PDF retrieval returned HTTP 403. Treat as `IDENTIFIED / FULL-TEXT-NOT-RECOVERED`, not as absent evidence.

---

# P33/P32/P31/P30 concise state

## P33 cryogenic package

Honeywell primary evidence shows compliant silicone attachment prevented cooldown cracking in its HgCdTe experiments; NRL/Bartoli photoconductor construction shows bonding layers can create several-ms and hundreds-ms thermal recovery components. Measure package thermal kernel before assigning slow P13 poles to carrier lifetime.

## P32 Mask-1

Historical identity remains open. Strong transfer branches: AZ4620/Br2:HBr and Hunt 180CP/Br2-methanol. Release from actual resist survival plus `CD_mask -> CD_PR -> CD_mesa`, not nominal thickness.

## P31 Hg anneal

Low-T screening anchor ~250 °C/1 h under Hg-rich/pseudo-isothermal transfer branch; isothermal and two-temperature routes remain distinct. No universal Hg reservoir mass.

## P30 LPE

Honeywell tie line `xL=.082, yL=.810, TL=507 °C -> xS≈.29`; composition does not determine total charge. Wipe-off hardware generations remain distinct.

---

# P29–P24 concise state

- **P29 CdZnTe:** strong transfer center `Cd0.96Zn0.04Te {111}`; exact RP-01 y/polarity/miscut/final surface open.
- **P28 wet mesa:** nominal `2% Br2 in 3:1 EG:HBr`, 21 °C, `R_V≈2.78 µm/min`, ±26%, `A≈0.63`; formulation basis/HBr assay/agitation/rinse open; release by measured depth + isolation.
- **P27 Mask-2:** direct 4–5 µm / 80 °C 30 min / chlorobenzene 30 min anchors; exact resist/dose/developer/lift-off solvent open.
- **P26 Cr/Au:** 30 nm Cr / 270 nm Au / `rho_c≈9×10^-4 Ω·cm²` at 80 K; exact deposition hardware/rates partly open.
- **P25 anodic oxide:** strongest transfer center 0.1 M KOH, 90% EG/10% DI, ~0.30 mA/cm², ~15 V, ~2 min, ~80 nm; transfer only.
- **P24 blocking contact:** direct RP-01 controller center preserved; P34 now controls reactor equivalence.

---

# Measurement / release essentials

- P05 Hall: canonical execution SOP; current/field reversal, VdP redundancy, variable field, self-heating, multicarrier escalation.
- P06 FTIR: distinguish composition/bandgap model from detector cutoff.
- P10: `E=V_active/L_measured`; package thermal resistance matters under bias.
- P11: calibrated absolute radiometry and measured package/reference-plane geometry.
- P12: `NEP=e_n/R_v`; `D*=R_v sqrt(A)/e_n`; combine independent noise at PSD level.
- P13: de-embed source/optics/detector/bias/preamp/cable/instrument and P33 package thermal response where relevant.
- P17: separate measurement/spatial/run/lot/long-term variation; no generic Cpk threshold.
- P18: preserve negative/failed runs and competing mechanisms.
- P19/P20: trace final requirements and sensitivities without replacing empirical process data.

---

# Highest-priority OPEN practical details after Round 27

## Absolute radiometry / FOV apparatus — strongest next empirical target

Audit P11 first. If it is already operator-complete, do not create duplicate documentation.

Priority historical/empirical recovery:

- exact RP-01 blackbody/source type and temperature calibration;
- source aperture dimensions;
- source-to-detector distance;
- whether stated 60° FOV is defined by cold shield, room-temperature aperture, optics or another geometry;
- window/filter material, transmission and temperature;
- chopper geometry/frequency/reference phase;
- monochromator/filter spectral bandwidth where used;
- reference detector/calibration chain;
- radiometric reference plane;
- background-subtraction sequence;
- optical throughput/vignetting;
- exact active detector/contact pair tied to published responsivity/D* curves.

P33 now controls package optical geometry, making P11 the natural downstream closure for the historical BLIP/D* benchmark.

## Persistent historical gaps

- exact RP-01 Mask-1/Mask-2 commercial lithography details;
- exact UWA wet-mesa formulation basis;
- exact RP-01 CdZnTe y/face/miscut/final surface;
- exact Honeywell/Fermionics LPE boat/charge/gas/contact trajectory;
- exact supplier/UWA anneal history;
- exact Cr/Au deposition method/rates/vacuum;
- exact RP-01 package construction;
- exact Plasma Technology RIE hardware/self-bias/sample temperature.

---

# Active source-recovery record

Identified but not fully recovered through current routes:

- Vanya Srivastav IISc thesis `G25544.pdf` full process text;
- John Kenion White 2005 UWA thesis full experimental text — current repository PDF route returns 403;
- Ryan Westerhout 2013 UWA thesis experimental text;
- Smith et al. 2000 in-situ vacuum processing full experimental text;
- Musca/Smith/Dell/Faraone photoconductor contact/passivation traveler;
- exact Honeywell/Fermionics LPE travelers;
- exact UWA Mask-1 traveler;
- exact RP-01 die attach/interconnect/Dewar traveler.

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 28: audit and empirical reconstruction of P11 absolute radiometry / blackbody / FOV apparatus**.

1. Audit `procedures/P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md` first.
2. Search canonical RP-01 and same-UWA photoconductor papers/proceedings/theses for the actual blackbody, optical train, apertures, FOV definition, chopper, filters/monochromator and reference detector.
3. Recover calibration temperatures, distances and dimensions before deriving flux.
4. Distinguish geometric FOV from effective radiometric throughput.
5. Tie D* to the actual fabricated active area/contact pair and the noise frequency used.
6. Preserve the existing ~`1.12×10^15 photons cm^-2 s^-1` 300-K/4.4-µm/60° consistency calculation as a **derived check**, not historical apparatus proof.
7. Create P35 only if the audit shows a material execution/provenance gap.

Do not populate production tolerances without repeated local fabrication data.
