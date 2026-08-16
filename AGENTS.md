# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** that a competent researcher can execute without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains direct historical anchors, empirical transfer procedures, measurement SOPs, qualification travelers, release/failure architecture and explicit unresolved gaps.

---

# Non-negotiable rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, explicit derivation, or a named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01 evidence, same-lineage evidence, transfer-family evidence, models, derived physics, apparatus calibration and local qualification.
4. Every critical process step requires output metrology and a pass/fail/qualification gate.
5. Preserve negative searches, failed branches, rejected inferences, corrections and source conflicts.
6. Use measured fabricated geometry for field, area and D* normalization.
7. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density, `rho_c` and minority-carrier blocking metrics distinct.
8. Treat passivation, post-RIE exposure, wet-etch surface exposure, metal-interface exposure, anneal cooldown, substrate clean-to-load, LPE source genealogy and packaging as process variables.
9. Measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Engineering specifications come from required detector/material performance; observed process spread does not define passing limits.
11. Failure diagnosis uses competing hypotheses and discriminating tests.
12. Repository scientific procedures do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.
13. Every numerical sensitivity/tolerance must state protected output, input, operating point and evidence class. Proxies may size experiments but cannot release production specifications.
14. A tie-line ratio such as `xS/xL` is not a local derivative `dxS/dxL` when other coordinates vary.
15. A coded DOE result does not create a physical process tolerance.
16. Repeated observations from one melt/source/bath/substrate/anneal-source genealogy are not independent replicates.
17. Never regress reciprocal Hall density through a p/n Hall-sign transition; use signed Hall/tensor information near transition.
18. **Empirical/practical literature first.** Before creating a theoretical placeholder, search primary papers, theses, patents and institutional archives for actual times, temperatures, concentrations, flows, pressures, dimensions, apparatus, metrology settings, outputs and failure observations.
19. Theory connects genuine literature gaps and checks consistency; it does not displace reported process data.
20. A successful historical process condition is not automatically an optimum.
21. Equal anodic-oxide thickness does not imply equal interface state.
22. No undocumented ion mill, wet etch or plasma clean may be inserted between qualified P08 RIE and Cr deposition.
23. Baseline P26 is as-deposited; post-metal anneals from other contact architectures are transfer evidence only.
24. Cryogenic TLM records optical-background/shield state as well as temperature/current.
25. Chlorobenzene constrains Mask-2 to a positive diazo/DNQ-novolak AZ-type lift-off family but does not identify a commercial resist.
26. Preserve RP-01 Mask-2 wording `prebake -> chlorobenzene -> then patterned/developed/water rinse`; do not silently reorder exposure sequence.
27. A generic AZ developer/lift-off solvent is not automatically the RP-01 developer/solvent.
28. **Wet-etch concentration rule:** a percentage without an explicit basis is not an executable formulation. Never guess Srivastav `2% Br2`.
29. Preserve `3:1 EG:HBr` symbolically until its preparation basis is recovered or explicitly defined locally.
30. HBr stock assay is part of wet-etch chemistry.
31. Br2 bath age/open exposure/run order/cumulative etched area/agitation are process variables.
32. **Wet-mesa endpoint rule:** time is an input; measured through-layer isolation is the output.
33. Post-wet-etch air time and surface state are part of the P28→P25 handoff.
34. **CdZnTe rule:** `4% Zn`, `{111}`, B polarity, or “epi-ready” are not direct RP-01 values unless sourced. Record actual lot, lattice/composition, polarity, miscut and final surface.
35. A/B polarity, miscut magnitude and miscut azimuth are separate coordinates.
36. Substrate impurity/ingot genealogy is a fabrication variable; Cu is a high-priority warning analyte for lightly doped LPE HgCdTe.
37. A substrate surface is released from resulting LPE interface/material quality, not AFM roughness or vendor label alone.
38. Clean-to-LPE timing/ambient must be timestamped.
39. **LPE composition is not charge mass.** `xL/yL` defines composition; absolute charge mass requires a defined growth-well geometry/inventory.
40. **Do not average incompatible growth-time branches.** Harman 0.25–10 min and the Honeywell ~30-min patent example remain separate evidence.
41. **Source-preparation branches remain separate.** Sealed-ampoule synthesis and in-situ Hg-vapor solution preparation are not one recipe.
42. **Wipe-off hardware generations remain separate.** CdTe-piece wipe-off and scribed-CdTe-apron wipe-off are distinct Honeywell implementations.
43. Slider clearance, speed, smoothness, contact/separation time and separation temperature are LPE process variables.
44. LPE thermal history is `T(t)`, not a scalar `Tgrowth`. Record actual liquidus estimate, supercooling at contact, cooling rate and cooldown.
45. Hg-source mass/geometry/reuse and growth-melt reuse form a repeated-measures genealogy that must follow run-order composition/thickness data.
46. **Hg anneal is trajectory defined.** A statement such as `250 °C in Hg` is incomplete; retain `T_s(t)`, `T_Hg(t)`, enclosure/source geometry and cooldown.
47. **Isothermal and two-temperature Hg anneals are separate process branches.** `T_Hg≈T_s` and `T_Hg<T_s` can produce different equilibrium carrier states.
48. **Hg saturation is a boundary condition, not a universal gram quantity.** Do not infer reservoir mass from another ampoule volume/geometry.
49. Controller setpoint is not sample or reservoir temperature until spatial/lag calibration demonstrates equivalence.
50. Do not copy multi-day bulk Hg-anneal times onto a ~9.5-µm LPE epilayer; kinetics depend on x, thickness, temperature, pHg and starting defect state.
51. High-temperature dislocation/Te-precipitate conditioning and low-temperature vacancy/stoichiometry control are separate anneal objectives.
52. During two-zone/high-temperature branches, source/sample temperature relation must prevent uncontrolled Hg condensation/deposition/dissolution; cooldown is part of the recipe.
53. A final n-type Hall sign is not sufficient anneal release. Require stable Hall-model validity, optical/thickness preservation and defect/morphology closure.
54. **Mask-1 and Mask-2 are different resist functions.** Do not copy Mask-2's chlorobenzene/lift-off process into Mask 1.
55. **Mask-1 thickness is not a selectivity specification.** Release from measured remaining resist height, edge retreat, pinholes/adhesion and final mesa transfer through the complete P28 etch.
56. AZ4620 is a strong product-identified Br2/HBr deep-mesa transfer candidate, **not** the historical RP-01 resist.
57. Hunt 180CP is a historical deep-through-HgCdTe bromine/methanol transfer branch, not a generic modern substitute family.
58. Changing resist thickness/profile/product changes the P28 dimensional-transfer problem; requalify mask bias and edge trenching unless equivalence is demonstrated.
59. Resist stripping is part of the HgCdTe surface process. Record strip/rinse/dry and timing to P25; acetone from another branch is not historical proof.
60. Do not introduce ultrasonics into Mask-1 strip by default; qualify mechanical/surface damage first.

---

# Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_empirical_mask1_round25.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_empirical_hg_anneal_round24.md`
- `research/2026-08-16_checkpoint_after_empirical_lpe_execution_round23.md`
- `research/2026-08-16_checkpoint_after_empirical_czt_substrate_round22.md`
- `research/2026-08-16_checkpoint_after_empirical_wet_mesa_round21.md`
- `research/2026-08-16_checkpoint_after_empirical_lithography_round20.md`
- `research/2026-08-16_checkpoint_after_empirical_metallization_round19.md`
- `research/2026-08-16_checkpoint_after_empirical_passivation_round18.md`
- `research/2026-08-16_checkpoint_after_empirical_blocking_contact_round17.md`
- `research/2026-08-16_checkpoint_after_hg_anneal_boundary_round16.md`
- `research/2026-08-16_checkpoint_after_information_design_round15.md`
- `research/2026-08-16_checkpoint_after_lpe_jacobian_round14.md`
- `research/2026-08-16_checkpoint_after_analytical_sensitivity_round13.md`

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND25.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND25.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND24.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND24.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND23.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND23.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND22.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND22.md`
- older addenda as needed.

---

# Controlled module set

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP
- P06 FTIR composition/thickness
- P07 CdZnTe substrate + P07A/P07B/P07C
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
- **P32 Mask-1/wet-mesa lithography empirical process window + register**

P24–P32 are deliberately empirical/practical and supplement earlier physics/provenance modules.

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
- Mask 1 = wet chemical mesa delineation before anodic oxide
- exact Mask-1 resist/process remains open
- native anodic oxide `~800 Å = 80 nm`

## Contact-window RIE
- Plasma Technology parallel-plate reactor
- printed `CH4/5H2`
- total `64 sccm`
- `100 mTorr`
- `50 W`
- `60 s`

## Converted region / LBIC
- average converted n `~2.0×10^15 cm^-3`
- mobility `~3.3×10^4 cm²/V·s`
- Hall/resistivity at 80/300 K, B to 2 T
- earlier same-lineage ~8-µm n+ conversion under similar conditions
- LBIC square 300×300 µm; Nd:YLF 1.047 µm CW; ~400 mW/cm²; 80 K

Do not combine 2e15 cm^-3 and 8 µm into one directly measured sheet density.

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
- 80 K
- stated 60° FOV
- spectral response at 1 kHz
- representative noise field 10 V/cm
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz
- high-frequency g-r plateau ~24.5 nV/√Hz
- cutoff ~4.4 µm
- BLIP D* ~`2×10^11 cm Hz^1/2/W` at 4 µm
- quoted QE ~70%

---

# P32 — empirical Mask-1 / wet-mesa lithography state

P32 is now the empirical Mask-1 execution layer for P14/P28/P25.

## Historical state

RP-01 directly closes only:

`photolithographic Mask 1 -> wet chemical mesa delineation -> passivation`.

Exact resist identity, thickness, spin, bake, exposure, developer, post-develop treatment, strip chemistry, mesa outer dimensions and mask bias remain `OPEN-HISTORICAL`.

Mask-2's 4–5 µm/chlorobenzene/lift-off process is a different function and may not be copied into Mask 1.

## Same-UWA function

Same-UWA x≈.31 wet Br/HBr mesa photoconductors achieved background-limited detector performance in the published comparison. This supports the wet-mesa device branch but does not close Mask-1 resist.

## Strong product-identified HBr transfer candidate

CN101740502B deep HgCdTe mesa branch:

- general resist thickness `1–6 µm`;
- general opening `1–8 µm`;
- Br2:HBr explicitly volume-ratio `0.1–1% : 1`;
- etch `5–150 s`;
- DI-water rinse;
- acetone strip.

Explicit embodiment:

- `AZ4620`;
- `3 µm` resist;
- `5 µm` opening;
- ~45-µm square / 50-µm pitch;
- Br2:HBr `0.5% : 1` by volume;
- etchant spin-delivery `2000 rpm / 20 s`.

This is the strongest product-identified Br2/HBr screening candidate. It is **not** RP-01 and does not prove compatibility with P28's EG-containing branch.

## Historical through-HgCdTe lithography branch

US4686373A:

- HgCdTe thinned to ~`12 µm`;
- Hunt `180CP`;
- spin `4000 rpm / 20 s`;
- dry `60 °C / 3 min`;
- expose;
- develop `30 s`;
- rinse `15 s`;
- ash `200 W / 30 s`;
- fresh `1/8% Br2/methanol` spray etch until separation trenches clear to epoxy;
- resist removed after etch.

This is strong deep-wet-mask transfer evidence on a thickness scale comparable to RP-01, but chemistry/device/etch mode differ.

## Novolak family evidence

US5157000A explicitly claims novolak photoresist compatibility in HgCdTe etch processing. Family evidence does not identify RP-01 Mask 1.

## Srivastav coupling

Primary x=.28 mesa work shows:

- profile/anisotropy depends on photoresist thickness and feature geometry;
- faster etching/trenching can occur at resist edges;
- high temperature attacks/deteriorates resist and produces ragged sidewalls;
- lower-temperature processing improves profile control and resist preservation.

Therefore Mask-1 and P28 are one coupled dimensional-transfer process.

## Resist release coordinates

Record and measure:

- `h_PR,0` before etch;
- `h_PR,f` after etch;
- resist thickness loss;
- edge retreat/swelling;
- adhesion/lift/blister/crack state;
- pinhole breakthrough;
- final mesa depth, lateral undercut, top/base CD and isolation.

Do not set production resist thickness from HgCdTe depth alone.

## Mask-bias chain

`CD_mask -> CD_PR -> CD_mesa_top/base`.

Track:

`Delta_CD_lith = CD_PR-CD_mask`

`Delta_CD_wet = CD_top-CD_PR`

`Delta_CD_total = CD_top-CD_mask`.

Do not infer mask bias solely from Srivastav's mean anisotropy.

## Strip / P25 handoff

Acetone is demonstrated in transfer branches but is not historical RP-01 proof.

Record strip chemistry/time/T/agitation/rinse/dry plus:

- `t_etch_to_strip`;
- `t_strip_to_P25`;
- residue/surface result;
- P25 anodization V(t)/charge response.

No default ultrasonics.

## P32 remaining OPEN

- exact UWA Mask-1 resist product/family;
- resist thickness;
- spin/bake;
- exposure wavelength/dose/mode;
- developer;
- strip chemistry;
- UWA Br/HBr resist selectivity;
- RP-01 mesa outer dimensions;
- historical mask bias;
- exact Srivastav resist product/thickness.

---

# P31 — empirical Hg-overpressure anneal state

Historical RP-01 closes final material state but not whether UWA performed the anneal; purchased Fermionics material may already have arrived in the quoted n/µ state.

Strong low-T screening anchor: pseudo-isothermal Hg-rich ~`250 °C / 1 h`, transfer only.

Near-composition Nagahama evidence: `250–300 °C` produced well-behaved n-type layers without apparent composition change; `400 °C` produced detectable interface-region composition change.

Jones distinguishes:

- isothermal `T_Hg≈T_s`;
- two-temperature `T_Hg<T_s`.

Keep separate.

TI two-zone transfer architecture uses long sealed ampoule, sample and elemental-Hg reservoir at opposite ends, independently heated zones. High-temperature defect-control branch is separate from baseline low-temperature vacancy control.

No universal elemental-Hg mass is released. Record source mass/geometry/free area, ampoule free volume, source/sample spacing, `T_s(t)`, `T_Hg(t)`, reconstructed pHg and cooldown.

Bulk multi-day anneals may not be copied onto a ~9.5-µm epilayer.

---

# P30 — empirical Te-rich LPE execution state

Honeywell tie line:

`xL=.082, yL=.810, TL=507 °C -> xS≈.29`.

Derived source mass fractions Hg `.249738`, Cd `.012502`, Te `.737760`. Composition does not establish charge mass.

Direct Honeywell apparatus family:

- covered graphite base/slider/cover;
- substrate recess;
- plugged solution well;
- auxiliary HgTe or HgTe+Te source;
- Hg-distribution grooves;
- quartz tube;
- N2 purge;
- flowing H2;
- slider contact/separation.

Harman branch: growth `450–550 °C`, contact `0.25–10 min`, typical equilibration ~1 h at 550 °C, 3–15 µm layers.

Radhakrishnan 2003 transfer: 6N elements; 10 g source synthesized 700 °C/8 h in evacuated quartz; ground/mixed; ~4.8 g/run; 3 g HgTe/run; 15×15×1 mm substrate recess. Do not overwrite Honeywell x=.29 with these masses.

Honeywell wipe-off generations remain separate: CdTe pieces in ~1-mm-spaced slots vs later scribed-CdTe drainage apron.

---

# P29/P28/P27/P26/P25/P24 concise state

- **P29 CdZnTe:** strong transfer center `Cd0.96Zn0.04Te {111}`; exact RP-01 y/polarity/miscut/final surface open; polarity affects wetting/residual melt.
- **P28 wet mesa:** nominal `2% Br2 in 3:1 EG:HBr`, 21 °C, `R_V≈2.78 µm/min`, ±26%, `A≈0.63`, best roughness ~2 nm; percentage basis/HBr assay/agitation/rinse open; release by measured depth + electrical isolation, not timer.
- **P27 Mask-2:** `4–5 µm -> 80 °C/30 min -> chlorobenzene 30 min -> pattern/develop/water rinse -> RIE -> lift-off`; exact resist/dose/developer/solvent open.
- **P26 Cr/Au:** Cr 30 nm / Au 270 nm / 80-K `rho_c≈9×10^-4 Ω·cm²`; deposition details partly open.
- **P25 anodic oxide:** strongest transfer center 0.1 M KOH, 90% EG/10% DI, ~0.30 mA/cm², ~15 V, ~2 min, ~80 nm; transfer only.
- **P24 blocking contact:** direct 100 mTorr / 64 sccm / 50 W / 60 s / printed CH4/5H2; physical etch depth != electrical conversion depth.

---

# Measurement / release essentials

- P05 Hall: current/field reversal, VdP redundancy, variable field, self-heating check, multicarrier escalation.
- P06 FTIR: Hansen x=.30/80 K gives Eg~0.243684 eV and lambda_Eg~5.0879 µm; not detector cutoff.
- P10: `E=V_active/L_measured`.
- P11: calibrated absolute radiometry/geometry.
- P12: `NEP=e_n/R_v`; `D*=R_v sqrt(A)/e_n`; combine independent noise at PSD level.
- P13: de-embed external transfer functions; use `tau_eff` unless bulk lifetime justified.
- P17: separate measurement/spatial/run/lot/long-term variation; no generic Cpk threshold.
- P18: signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification.
- P19/P20: trace requirements and sensitivities without replacing empirical process data.

---

# Highest-priority OPEN practical details after Round 25

## Hall / Van der Pauw execution — strongest next empirical target

Many fabrication modules now release on P05 electrical state, so practical Hall execution is a high-leverage remaining gap:

- exact UWA/RP-01 Hall test coupon geometry;
- contact metallurgy and preparation;
- contact size/position;
- contact anneal, if any;
- current range/self-heating test;
- field sweep/reversal sequence;
- 80/77-K stabilization;
- magnet calibration;
- voltage offset/polarity convention;
- uncertainty propagation;
- Hall-factor and multicarrier escalation.

Audit P05 first. Build P33 empirical Hall/VdP execution window + traveler only if it materially improves reproducibility.

## Persistent fabrication gaps

- exact RP-01 Mask-1 identity/process and outer mesa mask geometry;
- exact UWA wet-mesa formulation basis;
- exact RP-01 CdZnTe y/face/miscut/final surface;
- exact Honeywell/Fermionics LPE boat dimensions/charge/source synthesis/gas flows/contact time;
- exact supplier/UWA anneal history and local pHg hardware;
- exact Plasma Technology reactor/RF/self-bias/sample T;
- exact metal deposition method/rates/vacuum;
- exact Mask-2 resist/exposure/developer/lift-off solvent;
- practical die attach/interconnect/package materials remain incompletely historical.

---

# Active negative/source-recovery record

Identified but not fully recovered through current routes:

- Vanya Srivastav IISc thesis `G25544.pdf`
- John Kenion White 2005 UWA thesis experimental text
- Ryan Westerhout 2013 UWA thesis experimental text
- Smith et al. 2000 in-situ vacuum processing full experimental text
- Musca/Smith/Dell/Faraone photoconductor contact/passivation proceedings traveler
- exact Honeywell/Fermionics dimensioned LPE travelers
- full Jones et al. anneal experimental tables/geometry through accessible route
- exact Nagahama anneal apparatus/time/reservoir details
- exact UWA Mask-1 lithography traveler
- exact Srivastav resist identity/thickness.

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 26: empirical Hall / Van der Pauw contact + cryogenic measurement execution**.

1. Audit P05 for practical execution gaps before creating another module.
2. Search primary RP-01/UWA HgCdTe Hall papers/theses plus near-x≈.30 primary Hall studies for contact metallurgy, sample geometry, current, field, temperature and sequencing.
3. Distinguish material Hall contacts from device/TLM contacts.
4. Recover contact ohmicity checks and any contact anneal/aging requirements.
5. Recover actual field range, reversal, low/high-field behavior and multicarrier criteria.
6. Define thermal stabilization, self-heating and uncertainty procedures from primary evidence + metrology, not convention.
7. Create P33 empirical Hall/VdP execution window/traveler only if the audit shows material improvement over P05.
8. If P05 is already operationally adequate, pivot in the same round to P15 die attach / wire bond / cryogenic package empirical closure.

Do not populate production tolerances without repeated local fabrication data.
