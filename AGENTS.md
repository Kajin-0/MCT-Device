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
51. High-temperature dislocation/Te-precipitate conditioning and low-temperature vacancy/stoichiometry control are separate anneal objectives and must not be collapsed into one undocumented step.
52. During two-zone/high-temperature branches, source/sample temperature relation must prevent uncontrolled Hg condensation/deposition/dissolution; the cooldown relation is part of the recipe.
53. A final n-type Hall sign is not sufficient anneal release. Require stable Hall-model validity, optical/thickness preservation and defect/morphology closure.

---

# Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_empirical_hg_anneal_round24.md`

Then, as needed:

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

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND24.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND24.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND23.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND23.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND22.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND22.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND21.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND21.md`
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
- **P31 Hg-overpressure anneal apparatus/reservoir/trajectory empirical process window + register**

P24–P31 are deliberately empirical/practical and supplement earlier physics/provenance modules.

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
- wet chemical mesa before anodic oxide
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

# P31 — empirical Hg-overpressure anneal state

P31 is the empirical apparatus/execution layer for P04/P04A/P04B/P23.

## Historical RP-01 status

RP-01 closes the final material state but does not publicly close the anneal execution. It may also be possible that the purchased Fermionics material arrived already in the quoted n/µ state; this historical branch remains `OPEN`.

## Strongest low-temperature first-transfer branch

Harman primary process-family example:

- pseudo-isothermal/Hg-saturated;
- sample ~`250 °C`;
- ~`1 h`;
- then cooldown.

This is a **screening anchor only**.

Nagahama near-composition x≈0.17–0.30 LPE evidence:

- Hg-overpressure annealing `250–400 °C`;
- `250–300 °C` -> well-behaved n-type layers without apparent composition change;
- `400 °C` -> detectable interface-region composition change.

Therefore first x≈0.30 local stoichiometry work remains below 300 °C unless a separate defect-control objective is justified.

## Jones isothermal/two-temperature distinction

Jones et al. directly use Hg reservoirs in closed/open tube systems:

- isothermal: `T_Hg≈T_s`, favors p→n native-defect conversion;
- two-temperature: `T_Hg<T_s`, lower Hg chemical potential and different native-acceptor equilibrium.

Do not treat these as one recipe.

## Concrete two-zone hardware transfer branch

US5079192:

- long sealed ampoule;
- LPE HgCdTe sample at one end;
- sufficient elemental Hg reservoir at remote end;
- two independently heated zones.

Preferred high-T/dislocation-control example:

- sample ~400 °C;
- reservoir initially <200 °C;
- ~1 h;
- reservoir then ~390 °C while sample remains ~400 °C;
- ~1 h;
- subsequent stoichiometric anneal <325 °C for hours–days;
- cooldown to room T.

This proves architecture/trajectory mechanics but is **not** the baseline RP-01 low-T recipe.

## Condensation/dissolution rule

The TI two-zone branch deliberately keeps Hg source colder than the sample during part of the trajectory to prevent Hg depositing on/dissolving the specimen. Therefore P31 records source/sample temperatures through cooldown, not merely during dwell.

## Hg inventory

No universal elemental-Hg mass has been recovered. “Sufficient Hg for saturation” depends on ampoule volume, reservoir free area, temperature, condensation surfaces, leakage and duration.

P31 records source mass/geometry/reuse but does not release a gram value.

## Time/thickness state

Bulk TI low-temperature examples around 270 °C can require `3–7 days`; Harman's epitaxial branch uses ~1 h. Chandra/Schaake/Kinch show kinetics depend strongly on x/T/starting vacancy concentration. Therefore:

`t_required = F(x,T_s,pHg,S_initial,thickness,surface boundary)`.

Do not transfer bulk times to the ~9.5-µm epilayer.

## P31 required run chain

`P30/P05/P06 starting state`

`-> enclosure/ampoule revision`

`-> Hg source identity/mass/geometry`

`-> calibrated T_s(t), T_Hg(t)`

`-> reconstructed/qualified pHg state`

`-> dwell`

`-> controlled source-coupled cooldown`

`-> P05 signed Hall/tensor state`

`-> P06 same-site optical/thickness`

`-> morphology/defect state`

`-> P13/P11/P12 detector bridge`.

Near p/n conversion use P23 labels `N-LIKE / P-LIKE / TRANSITION-MULTICARRIER`; never force reciprocal Hall density through cancellation.

## P31 remaining OPEN

- exact RP-01 historical anneal/no-anneal supplier state;
- exact local ampoule dimensions/free volume;
- exact Hg reservoir mass/area;
- sample/source spacing;
- local pHg reconstruction relation;
- sample/source thermometry uncertainty;
- ramp/cooldown trajectory;
- local x≈0.30 time dependence and boundary margin;
- defect/dislocation response;
- detector-level optimum.

---

# P30 — empirical Te-rich LPE execution state

Direct Honeywell tie line:

`xL=.082, yL=.810, TL=507 °C -> xS≈.29`; derived source mass fractions Hg `.249738`, Cd `.012502`, Te `.737760`.

Composition does not establish total charge mass.

Direct Honeywell apparatus family:
- covered graphite base/slider/cover;
- substrate recess;
- plugged growth-solution well;
- auxiliary HgTe or HgTe+Te source;
- Hg-distribution grooves;
- quartz tube;
- N2 purge before heating;
- flowing H2;
- slider contact/separation.

Harman branch:
- growth `450–550 °C`;
- contact `0.25–10 min`;
- typical equilibration `~1 h at 550 °C`;
- 3–15 µm layers.

Radhakrishnan 2003 transfer:
- 6N Hg/Cd/Te;
- 10 g synthesized at 700 °C / 8 h in evacuated quartz;
- ground/mixed;
- ~4.8 g/run;
- 3 g HgTe/run;
- 15×15×1 mm substrate recess.

Do not overwrite Honeywell x=.29 with these masses.

Honeywell wipe-off generations:
- CdTe pieces in ~1-mm-spaced slots;
- later scribed-CdTe drainage apron.

Keep separate.

---

# P29/P28/P27/P26/P25/P24 concise state

- **P29 CdZnTe:** strong transfer center `Cd0.96Zn0.04Te {111}`; exact RP-01 y/polarity/miscut/final surface open; polarity affects wetting/residual melt.
- **P28 wet mesa:** nominal `2% Br2 in 3:1 EG:HBr`, 21 °C, `R_V≈2.78 µm/min`, ±26%, `A≈0.63`, best roughness ~2 nm; percentage basis/HBr assay/agitation/rinse open; release by measured depth + electrical isolation, not timer.
- **P27 Mask-2:** `4–5 µm -> 80 °C/30 min -> chlorobenzene 30 min -> pattern/develop/water rinse -> RIE -> lift-off`; exact resist/dose/developer/solvent open.
- **P26 Cr/Au:** Cr 30 nm / Au 270 nm / 80-K `rho_c≈9×10^-4 Ω·cm²`; deposition details remain partly open.
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

# Highest-priority OPEN practical details after Round 24

## Mask-1 / wet-mesa lithography — strongest next empirical target

P28 chemistry is substantially improved, but actual Mask-1 execution remains weak:

- historical resist identity;
- resist thickness needed to survive through-mesa wet etch;
- spin/bake;
- exposure tool/wavelength/dose;
- developer;
- wet-etch resist selectivity/swelling/edge retreat;
- strip solvent/time;
- effect of sidewall undercut and mask bias on final active geometry;
- resist-to-Br2/EG/HBr compatibility.

Recover primary UWA/near-x HgCdTe wet-mesa lithography evidence and create P32 only if supported.

## Hg anneal remaining

- exact RP-01 supplier anneal history;
- ampoule/reservoir geometry and Hg mass;
- pHg relation;
- x≈0.30 local time/cooldown state boundary;
- defect response.

## LPE remaining

- exact Honeywell/Fermionics boat dimensions;
- x=.29 total charge mass/melt height;
- source synthesis;
- gas flows/purity/dew point;
- exact contact time/slider speed/clearance;
- supplier wipe-off generation and reuse history.

## Other persistent gaps

- exact RP-01 CdZnTe y/face/miscut/final surface;
- exact UWA wet-mesa formulation basis;
- exact Plasma Technology reactor/RF/self-bias/sample T;
- exact metal deposition method/rates/vacuum;
- exact Mask-2 resist/exposure/developer/lift-off solvent.

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

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 25: empirical Mask-1 / wet-mesa lithography / resist-selectivity recovery**.

1. Search primary HgCdTe photoconductor/mesa papers, theses, patents and process records for Mask-1 resist, thickness, bake, exposure, developer and strip.
2. Prioritize Br2/HBr/EG and related bromine wet-etch compatibility/selectivity with positive photoresists.
3. Recover actual mask bias/undercut/sidewall/CD data near deep (~9.5 µm) HgCdTe mesa etches.
4. Keep lithography process-family evidence separate from Mask-2 chlorobenzene lift-off.
5. Build P32 empirical Mask-1/wet-mesa resist window + traveler if evidence supports it.
6. If primary Mask-1 recovery fails, pivot to another empirical gap rather than inventing resist values.

Do not populate production tolerances without repeated local fabrication data.
