# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** that a competent researcher can execute without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains direct historical anchors, empirical transfer procedures, measurement SOPs, qualification travelers, release/failure architecture and explicit unresolved gaps.

---

# Non-negotiable rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, an explicit derivation, or a named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01, same-lineage, transfer-family, model, derived, apparatus-calibration and local-qualification evidence.
4. Every critical process step requires output metrology plus a pass/fail/qualification gate.
5. Preserve negative searches, failed branches, rejected inferences, corrections and source conflicts.
6. Use measured fabricated geometry for field, area and D* normalization.
7. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density, `rho_c` and minority-carrier blocking metrics distinct.
8. Treat passivation, post-RIE exposure, wet-etch surface exposure, metal-interface exposure, anneal cooldown, substrate clean-to-load, LPE source genealogy and packaging as process variables.
9. Measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Engineering specifications come from required detector/material performance; observed process spread does not define its own passing limits.
11. Failure diagnosis uses competing hypotheses and discriminating tests.
12. Repository scientific procedures do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.
13. Every numerical sensitivity/tolerance states protected output, input, operating point and evidence class. Proxies may size experiments but cannot release production specifications.
14. A tie-line ratio such as `xS/xL` is not a local derivative `dxS/dxL` when other coordinates change.
15. A coded DOE result does not create a physical process tolerance.
16. Repeated observations from one melt/source/bath/substrate/anneal-source/package genealogy are not independent replicates.
17. Never regress reciprocal Hall density through a p/n Hall-sign transition; use signed Hall/tensor information near transition.
18. **Empirical/practical literature first.** Before creating theoretical placeholders, search primary papers, theses, patents, proceedings and institutional archives for actual times, temperatures, concentrations, flows, pressures, dimensions, apparatus, metrology settings, outputs and failure observations.
19. Theory connects genuine literature gaps and checks consistency; it does not displace reported process data.
20. A successful historical process condition is not automatically an optimum.
21. Equal anodic-oxide thickness does not imply equal interface state.
22. No undocumented ion mill, wet etch or plasma clean may be inserted between qualified P08 RIE and Cr deposition.
23. Baseline P26 is as-deposited; post-metal anneals from other contact architectures are transfer evidence only.
24. Cryogenic TLM records optical-background/shield state as well as temperature/current.
25. Chlorobenzene constrains Mask-2 to a positive diazo/DNQ-novolak AZ-type lift-off family but does not identify a commercial resist.
26. Preserve RP-01 Mask-2 wording `prebake -> chlorobenzene -> then patterned/developed/water rinse`; do not silently reorder the sequence.
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
39. **LPE composition is not charge mass.** `xL/yL` defines composition; absolute charge mass requires defined well geometry/inventory.
40. **Do not average incompatible growth-time branches.** Harman `0.25–10 min` and Honeywell ~30-min patent examples remain separate evidence.
41. **Source-preparation branches remain separate.** Sealed-ampoule source synthesis and in-situ Hg-vapor solution preparation are not one recipe.
42. **Wipe-off hardware generations remain separate.** CdTe-piece wipe-off and scribed-CdTe-apron wipe-off are distinct Honeywell implementations.
43. Slider clearance, speed, smoothness, contact/separation time and separation temperature are LPE process variables.
44. LPE thermal history is `T(t)`, not a scalar `Tgrowth`. Record liquidus estimate, actual supercooling, cooling rate and cooldown.
45. Hg-source mass/geometry/reuse and growth-melt reuse form repeated-measures genealogies.
46. **Hg anneal is trajectory defined.** `250 °C in Hg` is incomplete; retain `T_s(t)`, `T_Hg(t)`, enclosure/source geometry, pHg state and cooldown.
47. **Isothermal and two-temperature Hg anneals are separate process branches.** `T_Hg≈T_s` and `T_Hg<T_s` can establish different carrier states.
48. **Hg saturation is a boundary condition, not a universal gram quantity.**
49. Controller setpoint is not sample/reservoir temperature until calibration and thermal lag are known.
50. Do not copy multi-day bulk Hg-anneal times onto a ~9.5-µm LPE epilayer.
51. High-temperature dislocation/Te-precipitate conditioning and low-temperature vacancy/stoichiometry control are separate anneal objectives.
52. During two-zone/high-temperature anneals, source/sample temperature relation must prevent uncontrolled Hg condensation/deposition/dissolution; cooldown is part of the recipe.
53. A final n-type Hall sign is not sufficient anneal release. Require Hall-model validity, optical/thickness preservation and defect/morphology closure.
54. **Mask-1 and Mask-2 are different resist functions.** Do not copy Mask-2's chlorobenzene/lift-off process into Mask 1.
55. **Mask-1 thickness is not a selectivity specification.** Release from remaining resist height, edge retreat, pinholes/adhesion and final mesa transfer through P28.
56. AZ4620 is a strong product-identified Br2/HBr deep-mesa transfer candidate, **not** the historical RP-01 resist.
57. Hunt 180CP is a historical deep-through-HgCdTe Br2/methanol transfer branch, not a generic modern substitute.
58. Changing resist thickness/profile/product changes P28 dimensional transfer; requalify mask bias and edge trenching unless equivalence is demonstrated.
59. Resist stripping is part of the HgCdTe surface process. Acetone from another branch is not historical proof.
60. Do not introduce ultrasonics into Mask-1 stripping by default.
61. **P05 audit rule:** the existing P05 is the canonical Hall/VdP execution SOP. Do not create a duplicate Hall module unless new evidence materially changes the method.
62. **Die attach is a detector process variable.** Mechanical compliance, CTE match, bondline thermal conductance, cure history and detector electrical/noise stability are coupled outputs.
63. **Adhesive product identity is not a bondline specification.** Measure bondline thickness, coverage, voiding and die tilt.
64. Honeywell 5-g/40-g thermocompression values are controlled experimental transfer data, **not** RP-01 bond setpoints.
65. A packaged HgCdTe photoconductor can have package-generated thermal poles on ms-to-hundreds-ms scales. Do not assign them to intrinsic carrier lifetime without P33/P13 separation.
66. Package thermal history and thermal-cycle count are genealogical process variables. Repeated cycles of one package are not independent package replicates.
67. Do not transplant p-HgCdTe or FPA contact/interconnect metallurgies (In solder, Mo/AuGe, indium bumps, etc.) into the RP-01 Cr/Au contact chain without reopening P26/P24.
68. A package is not released by die shear or wire pull alone; mechanical, electrical/noise, thermal and optical/device gates must all pass.

---

# Current checkpoint — READ THIS FIRST

Latest:

`research/2026-08-16_checkpoint_after_empirical_packaging_round26.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_empirical_mask1_round25.md`
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

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND26.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND26.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND25.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND25.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND24.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND24.md`
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
- P32 Mask-1/wet-mesa lithography empirical process window + register
- **P33 cryogenic die-attach/interconnect/package empirical process window + register**

P24–P33 are empirical/practical supplements to the earlier controlled physics/metrology modules.

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
- exact Mask-1 process open
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
- Hall/resistivity at 80 and 300 K, B to 2 T
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

# Round-26 P05 audit

`procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md` is already adequate as the controlled Hall/VdP execution SOP.

It includes:

- ohmic-contact checks;
- dark/temperature state;
- current/self-heating screening;
- full VdP current reversal/reciprocity;
- numerical consistency gates;
- measured field calibration;
- symmetric B sweep;
- current/field reversal + orthogonal Hall configurations;
- antisymmetrization;
- single-carrier validity checks;
- multicarrier escalation;
- Hall-factor discipline;
- uncertainty and repeatability;
- structured raw-data output.

No separate Hall P33 was created.

Remaining P05 gaps are historical contact identity, historical temperature associated with RP-01 supplier n/µ, final acceptance bands, and any later Hall-factor correction.

---

# P33 — empirical cryogenic package state

P33 is the empirical execution layer for P15 and a required interpretation input to P10/P11/P12/P13.

## Historical RP-01 state

RP-01 does not close:

- singulation/die outline;
- die attach;
- bondline;
- carrier/cold finger;
- wire/ribbon/bond process;
- Dewar/header/window/cold shield;
- vacuum/bake;
- thermal cycling.

All remain `OPEN-HISTORICAL`.

## Honeywell compliant-attachment branch

US4081819A directly identifies glass adhesive as the cause of cryogenic cracking in its epitaxial HgCdTe device experiments and replaces it with silicone rubber.

Named examples:

- Dow Corning 3110 RTV;
- 3112 RTV;
- 3116 RTV.

Controlled 5-K comparison:

- glass / 60-µm abrasion / 40-g thermocompression -> cracked;
- silicone / ~50-µm abrasion / 40 g -> survived;
- silicone / 15-µm abrasion / 5 g -> survived.

Use this as attachment-family/mechanical evidence only. The 5-g/40-g values are not RP-01 bond setpoints.

## Direct HgCdTe photoconductor thermal stack

US4012691A / Bartoli et al. 1975:

`HgCdTe -> epoxy -> Irtran 2 or sapphire -> GE 7031 varnish -> copper heat sink at 77 K`.

Primary result:

- package/construction-dependent recovery on several-ms scale;
- slower recovery on hundreds-ms scale;
- attributed to two thermally resistive bonding layers.

Pulse heating may be optical or electrical, followed by resistance-vs-time recovery.

### P33 consequence

Measure a package thermal kernel / `H_pkg,thermal`. Do not assign slow poles to intrinsic lifetime until package response is separated.

## Thin-device stress / CTE transfer evidence

- US5462882A: thin `5–10 µm` HgCdTe mounted by epoxy to Si can develop slip/microcracks/fracture under thermomechanical mismatch/high-T processing.
- US5365088A: sapphire buffer improves HgCdTe/Si CTE mismatch reliability over repeated cryogenic cycles.

These are FPA transfer branches, not RP-01 construction identities.

## P33 release hierarchy

1. mechanical — cracks/delamination/shift/interconnect;
2. electrical/noise — contact resistance, leakage, 1/f, microphonics;
3. thermal — `R_theta`, transient kernel, self-heating;
4. optical/device — FOV/throughput/responsivity/P13 consistency.

No package is released by mechanical strength alone.

---

# P32/P31/P30 concise state

## P32 Mask-1

Historical resist identity remains open. Strong transfer branches:

- CN101740502B: AZ4620, 3-µm resist example with explicit Br2:HBr volume-ratio deep-mesa process;
- US4686373A: Hunt 180CP `4000 rpm/20 s`, `60 °C/3 min`, develop 30 s, rinse 15 s, ash `200 W/30 s`, then fresh `1/8% Br2/MeOH` through ~12-µm HgCdTe.

Release from actual resist survival + `CD_mask -> CD_PR -> CD_mesa`, not thickness alone.

## P31 Hg anneal

Strong low-T screen: pseudo-isothermal Hg-rich ~250 °C / 1 h, transfer only. Jones isothermal vs two-temperature branches remain separate. No universal Hg mass. Record full sample/source trajectories and cooldown.

## P30 LPE

Honeywell tie line: `xL=.082, yL=.810, TL=507 °C -> xS≈.29`. Composition does not establish charge mass. Honeywell wipe-off generations remain separate. Radhakrishnan 2003 source-synthesis masses are transfer only.

---

# P29–P24 concise state

- **P29 CdZnTe:** strong transfer center `Cd0.96Zn0.04Te {111}`; exact RP-01 y/polarity/miscut/final surface open.
- **P28 wet mesa:** nominal `2% Br2 in 3:1 EG:HBr`, 21 °C, `R_V≈2.78 µm/min`, ±26%, `A≈0.63`; formulation basis/HBr assay/agitation/rinse open; release by measured depth + isolation.
- **P27 Mask-2:** `4–5 µm -> 80 °C/30 min -> chlorobenzene 30 min -> pattern/develop/water rinse -> RIE -> lift-off`; exact resist/dose/developer/solvent open.
- **P26 Cr/Au:** Cr 30 nm / Au 270 nm / 80-K `rho_c≈9×10^-4 Ω·cm²`; exact historical deposition details partly open.
- **P25 anodic oxide:** strongest transfer center 0.1 M KOH, 90% EG/10% DI, ~0.30 mA/cm², ~15 V, ~2 min, ~80 nm; transfer only.
- **P24 blocking contact:** direct 100 mTorr / 64 sccm / 50 W / 60 s / printed CH4/5H2; physical etch depth != electrical conversion depth.

---

# Measurement / release essentials

- P05 Hall: canonical controlled execution SOP; multicarrier escalation near transition.
- P06 FTIR: distinguish bandgap/composition model from empirical detector cutoff.
- P10: `E=V_active/L_measured`; package thermal resistance matters under bias.
- P11: calibrated absolute radiometry and measured package geometry.
- P12: `NEP=e_n/R_v`; `D*=R_v sqrt(A)/e_n`; package/contact noise is a post-assembly gate.
- P13: de-embed source/optics/bias/preamp/cable/instrument **and P33 package thermal response where relevant**.
- P17: separate measurement/spatial/run/lot/long-term variation; no generic Cpk threshold.
- P18: signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification.
- P19/P20: trace requirements and sensitivities without replacing empirical process data.

---

# Highest-priority OPEN practical details after Round 26

## RIE reactor execution — strongest next empirical target

P24 has an empirical blocking-contact response framework, but exact apparatus/plasma-state closure remains weak:

- exact Plasma Technology reactor model;
- RF frequency;
- electrode area/diameter;
- electrode spacing;
- powered/grounded geometry;
- sample mounting and thermal coupling;
- dc self-bias/plasma potential;
- sample temperature during the 60-s treatment;
- base pressure/pump/throttle configuration;
- individual MFC flows/calibration;
- ignition/stabilization sequence;
- chamber clean/seasoning history;
- oxide-clear state;
- physical etch depth versus electrical conversion depth.

Search same-UWA papers/theses and primary HgCdTe CH4/H2 RIE literature first.

If the exact historical reactor cannot be recovered, create P34 as a **reactor-equivalence empirical process window**, using measurable plasma/process-state coordinates rather than fabricated historical hardware values.

## Persistent historical gaps

- exact RP-01 Mask-1 and Mask-2 commercial lithography details;
- exact UWA wet-mesa formulation basis;
- exact RP-01 CdZnTe y/face/miscut/final surface;
- exact Honeywell/Fermionics LPE boat/charge/gas/contact trajectory;
- exact supplier/UWA anneal history;
- exact Cr/Au deposition method/rates/vacuum;
- exact RP-01 package construction.

---

# Active negative/source-recovery record

Identified but not fully recovered through current routes:

- Vanya Srivastav IISc thesis `G25544.pdf` full process text;
- John Kenion White 2005 UWA thesis experimental text;
- Ryan Westerhout 2013 UWA thesis experimental text;
- Smith et al. 2000 in-situ vacuum processing full experimental text;
- Musca/Smith/Dell/Faraone photoconductor contact/passivation proceedings traveler;
- exact Honeywell/Fermionics LPE travelers;
- exact UWA Mask-1 traveler;
- full Siliquini–Faraone 1996 package details through current accessible route;
- exact epoxy identity in the NRL/Bartoli HgCdTe photoconductor stack;
- exact RP-01 die attach/interconnect/Dewar traveler.

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 27: empirical P08 RIE reactor / plasma-state / oxide-clear execution closure**.

1. Search same-UWA HgCdTe RIE papers, theses and proceedings for Plasma Technology reactor identity, RF frequency, electrode geometry/spacing, self-bias and sample temperature.
2. Search primary near-x HgCdTe CH4/H2 RIE process studies for pressure/power-density/sample-temperature dependencies and physical etch rates.
3. Recover chamber base pressure, pump/throttle, MFC calibration, ignition/stabilization and chamber-conditioning details where published.
4. Separate oxide removal from HgCdTe physical etch and from electrical conversion depth.
5. Preserve direct RP-01 center `64 sccm / 100 mTorr / 50 W / 60 s / CH4/5H2` without inventing the missing gas split or electrode area.
6. Create P34 only if it materially adds an executable **reactor-equivalence** qualification layer to P08/P24.

Do not populate production tolerances without repeated local fabrication data.
