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
16. Repeated observations from one melt/source/bath/substrate genealogy are not independent replicates.
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

---

# Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_empirical_lpe_execution_round23.md`

Then, as needed:

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

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND23.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND23.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND22.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND22.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND21.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND21.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND20.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND20.md`
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
- **P30 Te-rich LPE apparatus/charge/contact/wipe-off empirical process window + register**

P24–P30 are deliberately empirical/practical and supplement earlier physics/provenance modules.

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
- exact historical wet chemistry/anodization chemistry open

## Contact-window RIE
- Plasma Technology parallel-plate reactor
- printed `CH4/5H2`
- total `64 sccm`
- `100 mTorr`
- `50 W`
- `60 s`
- exact reactor model/RF/electrode geometry/self-bias/sample T/individual gas flows open

## Converted region / LBIC
- average converted n `~2.0×10^15 cm^-3`
- mobility `~3.3×10^4 cm²/V·s`
- Hall/resistivity at 80/300 K, B to 2 T
- earlier same-lineage ~8-µm n+ conversion under similar conditions
- LBIC square 300×300 µm; Nd:YLF 1.047 µm CW; ~400 mW/cm²; 80 K

Do not combine 2e15 cm^-3 and 8 µm into one directly measured canonical sheet density.

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

# P30 — empirical Te-rich LPE execution state

P30 is now the empirical execution layer for P03/P03A–P03E.

## Honeywell composition and apparatus

Direct Honeywell tie line:

`xL=.082, yL=.810, TL=507 °C -> xS≈.29`, with `xS/xL=3.54`.

Derived source mass fractions:

- Hg `.249738`
- Cd `.012502`
- Te `.737760`

These fractions do **not** establish total charge mass.

Direct Honeywell apparatus family:

- covered graphite base/slider/cover;
- substrate recess;
- plugged growth-solution well;
- auxiliary HgTe or HgTe+Te source;
- Hg-distribution moats/grooves;
- quartz tube;
- N2 purge before heating;
- flowing H2;
- slide well over substrate after thermal equilibration.

Exact boat dimensions, gas flows and RP-01 supplier configuration remain OPEN.

## Direct Honeywell thermal families

Solution is heated above liquidus, then brought below liquidus for growth by:

- step supercooling;
- slow cooling after contact;
- or a combination.

The patent gives an example of ~0.5 h growth. Do not treat this as the canonical x=.29 duration.

## Harman 1980 direct operating scales

Primary Te-rich horizontal-slider branch:

- growth `450–550 °C`;
- growth/contact times `0.25–10 min`;
- typical equilibration `~1 h at 550 °C`;
- source wafers + supercooled solutions + `(111)` substrates for highest-quality layers;
- layer thickness `3–15 µm`.

These are direct branch values, not a single RP-01 recipe.

## Radhakrishnan 2003 source-prep transfer branch

Direct:

- high-purity/high-density graphite slider;
- `15×15×1 mm` CdZnTe recess;
- solution bins + HgTe cavity;
- tightly fitting graphite cover;
- quartz tube with gas/push-pull/TC ports;
- in-situ meltback provision;
- `10 g` growth-compound synthesis;
- `6N` Hg/Cd/Te;
- evacuated quartz ampoule;
- `700 °C / 8 h`;
- grind + thorough mix;
- `~4.8 g` charge/run;
- `3 g HgTe` compensation/run.

Representative branch coordinates are around `z=.049, y=.84`; masses are transfer data only and may not overwrite Honeywell x=.29.

## Alternate in-situ source preparation

Bernardi 1988 demonstrated Hg-vapor transport into a Cd-rich Te melt to prepare the MCT solution in situ. Keep separate from sealed-ampoule source synthesis.

## Thermal-trajectory thickness evidence

Shinohara 1994:

- equilibrium cooling -> `2–4 µm` layers;
- step/supercooling with `15 K` supercooling -> `30–40 µm` layers;
- `x≈.25–.42`.

Therefore record full `T(t)`, actual `DeltaT_SC`, cooling rate and source history.

## Honeywell wipe-off hardware

### US4592304A
- dedicated wipe-off well adjacent to growth well;
- CdTe pieces in vertical slots about `1 mm` apart;
- polycrystalline/unpolished pieces permitted;
- mechanical wiping + surface-tension adhesion + capillary wicking;
- discard after cooldown.

### US4706604A
- later, separate scribed-CdTe-apron generation;
- apron in tandem with substrate;
- diagonal diamond scribes;
- final residual melt directed/retained on apron;
- finite slider clearance is required to avoid scratching;
- patent reports complete/100% wipe-off for described geometry.

Do not combine these two generations into one historical apparatus.

## P30 release chain

`P29 substrate -> source/boat genealogy -> purge/H2 -> above-liquidus hold/equilibration -> measured T(t)/supercool -> slider contact -> measured contact time -> slide-out/wipe-off -> cooldown -> residual-melt/scratch map -> P06 x/d -> P05 transport -> P04 -> P13/device proxy`.

Exact RP-01 total charge, boat dimensions, source synthesis, gas flows, contact duration, slider speed/clearance, wipe-off generation, cooldown and source reuse remain OPEN.

---

# P29 — empirical CdZnTe substrate / LPE-interface state

RP-01 closes only electrically insulating CdZnTe. Exact y(Zn), plane/polarity, miscut, dimensions, supplier, resistivity, impurities, polish and final surface remain OPEN.

Strong x≈0.30 transfer center: `Cd0.96Zn0.04Te`. Historical benchmark study reports representative best substrate `EPD≈5×10^4 cm^-2` and XRD linewidth `≈25 arcsec`; benchmarks only.

Detector-LPE surface transfer branch uses `(111)B`, ~4% Zn, `10×10×1 mm³`, chemical+mechanical polish, `(2–3)% Br2/MeOH` for a few seconds then graphite-boat loading; exact concentration basis/rinse/removed depth/timing remain open.

Direct A/B slider comparison shows polarity affects wetting/residual melt; do not freeze B polarity by convention. Direct dipping-LPE miscut result near `1.2° off (111)` is transfer evidence only.

---

# P28 — empirical wet mesa

Near-x transfer center: nominal `2% Br2 in 3:1 EG:HBr`, 21 °C, `R_V≈2.78 µm/min`, ~±26% variation, `A≈0.63±11%`, best roughness ~2 nm, `Ea≈7.5 kcal/mol`, rate ~doubles/+10 °C.

Percentage basis, EG:HBr basis, HBr assay, agitation and rinse remain OPEN. `9.5/2.78≈3.42 min` is diagnostic only; release from measured depth/profile + isolation.

---

# P27/P26/P25/P24 concise state

- **P27 Mask-2:** historical `4–5 µm -> 80 °C/30 min -> chlorobenzene 30 min -> pattern/develop/water rinse -> RIE -> Cr/Au lift-off`; exact resist/dose/developer/lift-off solvent open.
- **P26 Cr/Au:** direct Cr 30 nm / Au 270 nm / 80-K `rho_c≈9×10^-4 Ω·cm²`; thermal evaporation strongest same-UWA transfer method, not historical proof; Cr rate open; record RIE→metal exposure.
- **P25 anodic oxide:** strongest transfer center 0.1 M KOH in 90% EG/10% DI, ~0.30 mA/cm², ~15 V, ~2 min, ~80 nm; record full V(t), charge/area and downstream state.
- **P24 blocking:** direct 100 mTorr / 64 sccm / 50 W / 60 s / printed CH4/5H2; physical etch depth != electrical conversion depth; release plasma/material -> TLM -> minority blocking -> full detector.

---

# Anneal state — P04/P23

Cooldown is part of Hg anneal. Record `T_sample(t), T_reservoir(t), pHg(t)` and initial state.

State labels:
- `N-LIKE`
- `P-LIKE`
- `TRANSITION-MULTICARRIER`

Never fit one reciprocal-Hall-density model through sign reversal. No unique RP-01 anneal dwell/T/pHg/cooldown is released.

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

# Highest-priority OPEN practical details after Round 23

## Hg anneal — strongest next empirical target

Recover primary values for:

- sealed/open ampoule or boat geometry;
- Hg reservoir form/mass;
- sample-reservoir spacing;
- sample and reservoir temperatures independently;
- pHg equilibrium/calibration method;
- ramp/dwell/cooldown trajectories;
- vacuum/backfill/ambient;
- sample encapsulation/holder material;
- carrier-type/density/mobility outcomes;
- spectral/surface effects.

P23 has the state-boundary physics; it still lacks an executable empirical hardware trajectory.

## LPE remaining

- exact Honeywell/Fermionics boat dimensions;
- x=.29 total charge mass/melt height;
- exact source synthesis;
- gas flows/purity/dew point;
- TC position/calibration;
- exact equilibration/supercooling/contact duration;
- slider speed/clearance;
- wipe-off generation used by supplier;
- cooldown and melt reuse.

## CdZnTe / wet mesa / RIE / metallization / lithography

- exact RP-01 CZT y/face/miscut/final surface;
- exact UWA wet-mesa formulation and concentration basis;
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
- exact Honeywell dimensioned LPE boat drawings/process travelers

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 24: empirical Hg-anneal apparatus / reservoir / pHg / cooldown recovery**.

1. Search primary HgCdTe anneal papers, Honeywell/Fermionics/UWA sources, patents and theses.
2. Recover actual ampoule/boat geometry, Hg charge/reservoir, sample-reservoir spacing, independent temperature histories, pHg method, dwell and cooldown.
3. Keep n↔p conversion/state-boundary evidence separate from one-carrier Hall fits near transition.
4. Connect anneal execution to P05 transport, P06 optical edge/thickness, P13 lifetime and downstream detector noise.
5. Create P31 empirical anneal execution window/traveler only if the primary evidence supports it.
6. Do not invent Hg mass, reservoir temperature, pHg, ramp rate or cooldown.

Do not populate production tolerances without repeated local fabrication data.
