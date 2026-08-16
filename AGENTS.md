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
8. Treat passivation, post-RIE exposure, wet-etch surface exposure, metal-interface exposure, anneal cooldown, substrate clean-to-load and packaging as process variables.
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
26. Preserve RP-01 Mask-2 wording `prebake -> chlorobenzene -> then patterned/developed/water rinse`; do not silently reorder the exposure sequence.
27. A generic AZ developer/lift-off solvent is not automatically the RP-01 developer/solvent.
28. **Wet-etch concentration rule:** a percentage without an explicit basis is not an executable formulation. Never guess the basis of Srivastav `2% Br2` or convert it to reagent quantities.
29. Preserve `3:1 EG:HBr` symbolically until its preparation basis is recovered or explicitly defined in a local recipe.
30. HBr stock assay is part of the wet-etch chemistry.
31. Br2 bath age/open exposure/run order/cumulative etched area/agitation are process variables.
32. **Wet-mesa endpoint rule:** time is an input; measured through-layer isolation is the output.
33. Post-wet-etch air time and surface state are part of the P28→P25 passivation handoff.
34. **CdZnTe substrate rule:** `4% Zn`, `{111}`, B polarity, or “epi-ready” are not direct RP-01 values unless sourced. Record actual substrate lot, lattice/composition, polarity, miscut and final surface.
35. **Polarity and miscut are separate coordinates.** `(111)` alone is incomplete; record A/B polarity, miscut magnitude and azimuth separately.
36. Substrate impurity/ingot genealogy is a fabrication variable. Cu is a high-priority warning analyte for lightly doped LPE HgCdTe.
37. A final substrate surface is released from the resulting LPE interface/material quality, not AFM roughness or vendor polish label alone.
38. Clean-to-LPE timing/ambient must be timestamped. Do not assume an “immediate load” statement supplies a reproducible numerical maximum.

---

# Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_empirical_czt_substrate_round22.md`

Then, as needed:

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

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND22.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND22.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND21.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND21.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND20.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND20.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND19.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND19.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND18.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND18.md`
- older provenance/gap addenda as needed.

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
- **P29 CdZnTe substrate/final-surface empirical process window + register**

P24–P29 are deliberately empirical/practical and supplement the earlier physics/provenance modules.

---

# Canonical RP-01 direct anchors — do not drift

## Material

- LPE n-HgCdTe on electrically insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `mu=4.0×10^4 cm²/V·s`
- active thickness `9.5 µm`
- supplier n/mu measurement temperature remains undisclosed

## Mesa/passivation

- wet chemical mesa before anodic oxide
- native anodic oxide `~800 Å = 80 nm`
- exact historical wet chemistry and anodization chemistry remain open

## Contact-window RIE

- Plasma Technology parallel-plate reactor
- printed `CH4/5H2`
- total `64 sccm`
- `100 mTorr`
- `50 W`
- `60 s`

Historical reactor model/RF frequency/electrode geometry/self-bias/sample temperature/individual gas flows remain open.

## Converted region

- average converted electron density `~2.0×10^15 cm^-3`
- mobility `~3.3×10^4 cm²/V·s`
- Hall/resistivity at 80 K and 300 K, B to 2 T
- earlier same-lineage ~8-µm n+ conversion under similar RIE conditions

Do not combine the 2e15 cm^-3 and 8 µm into one directly measured canonical sheet density.

## LBIC

- 300×300-µm RIE square
- Waterloo Scientific scanning laser microscope
- Nd:YLF 1.047 µm CW
- ~400 mW/cm²
- 80 K

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

# P29 — empirical CdZnTe substrate / LPE-interface state

P29 is the empirical control layer for P07/P07A/P07B/P07C.

## Historical state

RP-01 directly closes only **electrically insulating CdZnTe**. Exact y(Zn), plane/polarity, miscut, dimensions, supplier, resistivity, crystal-quality limits, impurities, polish and final surface remain `OPEN`.

## Strongest composition transfer center

Primary x≈0.30 LPE literature strongly supports `Cd0.96Zn0.04Te`.

A primary 1994 comparison reported representative best Cd0.96Zn0.04Te substrate metrics:

- `EPD≈5×10^4 cm^-2`
- XRD rocking-curve linewidth `≈25 arcsec`

and better x≈0.30 HgCdTe crystalline quality than on CdTe in that experiment.

These are benchmarks, not P29 limits.

## Strong detector-LPE final-surface branch

Kubiak et al. report:

- `(111)B` CdZnTe, 4% Zn
- 10×10×1 mm³
- chemical + mechanical polish
- `(2–3)% Br2-methanol`
- `a few seconds`
- then graphite-boat loading

for a Te-rich detector LPE branch.

This is a practical transfer family, not RP-01 historical closure. Percentage basis, exact seconds, rinse/dry, removed depth and clean-to-load interval remain unresolved.

## Polarity is an active growth coordinate

Direct 2023 slider-LPE A/B comparison:

- comparable x/thickness on A and B
- melt/film contact angle `(111)A = 50±2°`
- `(111)B = 30±2°`
- A-grown layer FWHM `33.1 arcsec`
- A face strongly reduced residual melt droplets in that process

Therefore evaluate:

`polarity -> wetting -> residual melt -> wipe-off -> morphology`.

Do not freeze B polarity by convention.

## Miscut

A direct 1996 dipping-LPE study found improved crystal quality/fewer Te precipitates near `1.2° off (111)`.

This proves miscut matters but does not supply a slider-LPE or RP-01 setpoint. Historical magnitude and azimuth remain OPEN.

## Impurity genealogy

Primary substrate/LPE work shows substrate contamination, especially Cu, can degrade lightly doped HgCdTe electrical/device behavior.

Record lot/ingot genealogy and Cu/Fe/Ni/Na or equivalent impurity information where available. No universal impurity limit is released.

## “Epi-ready” rule

Vendor “epi-ready” is not a complete process state. Retain certificate and independently record/measure orientation/polarity/miscut, crystal quality, surface morphology and clean-to-load history.

## P29 practical chain

`lot/ingot -> y/lattice state -> plane/polarity/miscut -> XRD/EPD/inclusions -> impurities -> electrical isolation -> mechanical genealogy -> explicit final surface recipe -> removed depth/roughness/chemistry -> clean-to-load -> P03 wetting/wipe-off -> epilayer XRD/x/d/transport -> device proxy`.

The first local transfer family should be high-quality `Cd0.96Zn0.04Te {111}` if available, while polarity and miscut remain qualification coordinates.

---

# P28 — empirical wet mesa

Near-x primary transfer center:

- nominal `2% Br2 in 3:1 EG:HBr`
- 21 °C
- `R_V≈2.78 µm/min`
- ~±26% rate variation
- `A≈0.63±11%`
- roughness best ~2 nm
- `Ea≈7.5 kcal/mol`
- rate ~doubles per +10 °C

Percentage basis, EG:HBr physical preparation basis, HBr stock assay, agitation and rinse remain OPEN.

`9.5/2.78≈3.42 min` is diagnostic only; P28 releases from measured depth/profile + electrical isolation.

Record bath genealogy and etch→P25 surface exposure.

---

# P27 — empirical Mask-2 lithography

Historical fingerprint:

`4–5 µm resist -> 80 °C/30 min -> chlorobenzene 30 min -> pattern/develop/water rinse -> RIE -> Cr/Au lift-off`.

Chlorobenzene supports positive diazo/DNQ-novolak AZ family, not exact product identity. Exposure dose/developer/lift-off solvent remain OPEN.

---

# P26 — empirical Cr/Au

Direct: Cr 30 nm / Au 270 nm / 80-K `rho_c≈9×10^-4 Ω·cm²`.

Thermal evaporation is strongest same-UWA transfer method, not direct RP-01 proof. Au screening scales exist at 3/6/10/12 Å/s; Cr rate remains OPEN.

Record RIE→Cr exposure, no undocumented surface reset, baseline no intentional post-metal anneal, and optical-background state during cryogenic TLM.

---

# P25 — empirical native anodic oxide

Strongest executable transfer center:

- HgCdTe anode / carbon-rod cathode
- 0.1 M KOH
- 90% EG / 10% DI water
- ~0.30 mA/cm² galvanostatic
- ~15 V
- ~2 min
- ~80 nm oxide

Transfer only. Record full V(t), charge/area, cell/bath state, physical oxide and downstream electrical/device state.

---

# P24 — empirical blocking contact

Canonical center:

- 100 mTorr / 64 sccm / 50 W / 60 s / printed CH4/5H2
- converted n ~2e15 cm^-3
- mobility ~3.3e4 cm²/Vs

Physical etch depth != electrical conversion depth. Post-RIE state can age/thermally relax. Historical contact was not optimized.

Release: plasma/material -> TLM -> minority blocking -> full detector.

---

# LPE / anneal state

Honeywell tie line retained:

`xL=.082, yL=.810, TL=507 °C -> xS≈.29`.

Derived source mass fractions Hg `.249738`, Cd `.012502`, Te `.737760`.

`xS/xL=3.54` is not a derivative.

P03E uses `DeltaT_SC = TL_actual - T_contact`; P21/P22 map process coordinates empirically. No tolerance from tie-line ratios alone.

P04/P23: cooldown is part of Hg anneal. Record `T_sample(t), T_reservoir(t), pHg(t)`. State labels N-LIKE / P-LIKE / TRANSITION-MULTICARRIER. Never fit one Hall-density model through sign reversal.

---

# Measurement / release essentials

- P05 Hall: current/field reversal, VdP redundancy, variable field, self-heating check; multicarrier escalation when required.
- P06 FTIR: Hansen x=.30/80 K gives Eg~0.243684 eV and lambda_Eg~5.0879 µm; not the detector cutoff.
- P10: `E=V_active/L_measured`.
- P11: calibrated absolute radiometry/geometry.
- P12: `NEP=e_n/R_v`; `D*=R_v sqrt(A)/e_n`; combine independent noise at PSD level.
- P13: de-embed external transfer functions; use `tau_eff` unless bulk lifetime is justified.
- P17: separate measurement/spatial/run/lot/long-term variation; no generic Cpk threshold.
- P18: signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification.
- P19/P20: trace requirements and sensitivities, but do not replace empirical process data.

---

# Highest-priority OPEN practical details after Round 22

## LPE apparatus/source/growth — strongest next empirical target

Recover primary values for:

- graphite boat and well geometry
- substrate dimensions/orientation within boat
- source-wafer identity/preparation
- total charge mass/inventory
- source synthesis/homogenization
- saturation/equilibration determination
- Hg-loss handling
- supercooling/contact trajectory
- growth duration
- decant/wipe-off mechanics
- cooldown
- melt/source reuse and depletion history

## CdZnTe

- exact RP-01 y(Zn), face/polarity/miscut
- supplier/ingot/resistivity
- crystal-quality and impurity limits
- historical polish/final etch/rinse/dry
- removed depth
- clean-to-growth limit
- in-situ meltback state

## Wet mesa

- exact UWA formulation
- Srivastav percentage/ratio bases
- HBr assay, mixing/agitation, rinse/dry
- local x≈0.30 rate/isolation capability

## Anneal / RIE / metallization / lithography

- RP-01 Hg reservoir/apparatus/trajectory
- exact Plasma Technology reactor/RF/self-bias/sample T
- exact metal deposition method/rates/vacuum
- exact Mask-2 resist/exposure/developer/lift-off solvent

---

# Active negative/source-recovery record

Identified but not fully recovered through current routes:

- Vanya Srivastav IISc thesis `G25544.pdf`
- John Kenion White 2005 UWA thesis experimental text
- Ryan Westerhout 2013 UWA thesis experimental text
- Smith et al. 2000 in-situ vacuum processing full experimental text
- Musca/Smith/Dell/Faraone photoconductor contact/passivation proceedings traveler
- original historical LPE papers behind several secondary miscut claims

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 23: empirical P03 LPE apparatus / source synthesis / charge inventory / contact / wipe-off recovery**.

1. Search Honeywell/SBRC/Harman and related Te-rich horizontal-slider primary papers, patents, theses and proceedings.
2. Recover actual graphite boat/well dimensions, charge masses, source synthesis, homogenization/equilibration times, substrate placement, temperature trajectory, growth contact time, decant/wipe-off and cooling.
3. Separate direct x≈0.30 horizontal-slider evidence from other-x/dipping/Hg-rich branches.
4. Preserve the known Honeywell tie-line as thermodynamic composition evidence, not an operator traveler by itself.
5. Build P30 empirical LPE apparatus/growth traveler if enough primary process detail can be recovered.
6. Do not invent charge mass, well volume, source-wafer dimensions or timing if the source remains silent.

Do not populate production tolerances without repeated local fabrication data.
