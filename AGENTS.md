# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** that a competent researcher can execute without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains direct historical anchors, empirical transfer procedures, measurement SOPs, release/failure architecture, and explicit unresolved gaps.

---

# Non-negotiable rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, explicit derivation, or a named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01 publication, same-lineage evidence, transfer-family evidence, model values, derived physics, apparatus calibration and local qualification.
4. Every critical process step requires output metrology and a pass/fail/qualification gate.
5. Preserve negative searches, failed branches, rejected inferences, corrections and source conflicts.
6. Use measured fabricated geometry for field, area and D* normalization.
7. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density, `rho_c` and minority-carrier blocking metrics distinct.
8. Treat passivation, post-RIE elapsed time/thermal exposure, metal-interface exposure, wet-etch surface exposure, anneal cooldown and packaging as process variables.
9. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Engineering specifications come from required detector/material performance; observed process spread does not define its own passing limits.
11. Failure diagnosis uses competing hypotheses and discriminating tests; never force one cause from one symptom.
12. Repository scientific procedures do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.
13. Every numerical sensitivity/tolerance must state protected output, input, operating point and evidence class. Proxy relations may size experiments but cannot release production specifications.
14. A tie-line ratio such as `xS/xL` is not a local derivative `dxS/dxL` when other coordinates vary.
15. A coded DOE result does not create a physical process tolerance.
16. Repeated observations from one melt/source/bath genealogy are not independent replicates.
17. Never regress reciprocal Hall density through a p/n Hall-sign transition; use signed Hall/tensor information near transition.
18. **Empirical/practical literature first.** Before creating a theoretical placeholder, search primary papers, theses, patents and institutional archives for actual times, temperatures, concentrations, flows, pressures, dimensions, apparatus, metrology settings, outputs and failure observations.
19. Theory connects genuine literature gaps and checks consistency; it does not displace experimentally reported process information.
20. A successful historical process condition is not automatically an optimum.
21. Equal anodic-oxide thickness does not imply equal interface state; record chemistry, surface, cell, current, full `V(t)`, charge/area, oxide metrology and detector response.
22. No undocumented ion mill, wet etch or plasma clean may be inserted between qualified P08 RIE and Cr deposition.
23. Baseline P26 is as-deposited; post-metal anneals from other contact architectures are transfer evidence only.
24. Cryogenic TLM records optical-background/shield state as well as temperature/current.
25. **Mask-2 identity rule:** chlorobenzene constrains the historical process to a positive diazo/DNQ-novolak AZ-type lift-off family, but it does not identify a commercial resist.
26. **Mask-2 sequence rule:** preserve RP-01 wording `prebake -> chlorobenzene -> then patterned/developed/water rinse`; carry alternative exposure-order branches until direct UWA evidence closes it.
27. A developer/lift-off solvent used in generic historical AZ processing is not automatically the RP-01 developer/lift-off solvent.
28. **Wet-etch concentration rule:** a percentage without an explicit basis is not an executable formulation. Primary HgCdTe literature uses both weight and volume conventions; never guess the basis of Srivastav `2% Br2` or convert it into reagent quantities.
29. Preserve source notation `3:1 EG:HBr` symbolically until its physical preparation basis is recovered or a new local recipe defines one explicitly.
30. HBr stock assay is part of the wet-etch chemistry. Do not assume a commercial concentration such as 48 wt% unless the selected local recipe explicitly uses that certified product.
31. Br2 bath age, open-vessel exposure, run order, cumulative etched area and agitation are process variables because the primary study identifies volatility/mass transport as important.
32. **Wet-mesa endpoint rule:** time is an input; physical through-layer isolation is the output. A timer alone cannot release a mesa.
33. Post-wet-etch air time and surface state are part of the P28→P25 passivation handoff.

---

# Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_empirical_wet_mesa_round21.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_empirical_lithography_round20.md`
- `research/2026-08-16_checkpoint_after_empirical_metallization_round19.md`
- `research/2026-08-16_checkpoint_after_empirical_passivation_round18.md`
- `research/2026-08-16_checkpoint_after_empirical_blocking_contact_round17.md`
- `research/2026-08-16_checkpoint_after_hg_anneal_boundary_round16.md`
- `research/2026-08-16_checkpoint_after_information_design_round15.md`
- `research/2026-08-16_checkpoint_after_lpe_jacobian_round14.md`
- `research/2026-08-16_checkpoint_after_analytical_sensitivity_round13.md`

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND21.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND21.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND20.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND20.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND19.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND19.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND18.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND18.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND17.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND17.md`
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
- P27 Mask-2 photoresist/exposure/developer/lift-off empirical process window + register
- **P28 wet-mesa empirical process window + register**

P24–P28 are deliberately empirical/practical and supplement earlier physics/provenance modules.

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

Historical reactor model/RF frequency/electrode area-spacing/self-bias/sample temperature/individual gas flows remain open.

P08A same-lineage evidence supports `CH4:H2=1:5`; derived 10.6667/53.3333-sccm split is a local candidate, not direct historical MFC closure.

## Converted region

Direct RP-01:

- average converted electron density `~2.0×10^15 cm^-3`, explicitly averaged over converted thickness
- mobility `~3.3×10^4 cm²/V·s`
- Hall/resistivity at `80 K` and `300 K`
- variable B to `2 T`

Earlier same-lineage n-type work cited by RP-01:

- ~`8 µm` n+ conversion under similar conditions

Do not combine 2e15 cm^-3 and 8 µm and call the derived sheet density directly measured RP-01 data.

## RP-01 LBIC apparatus

- patterned RIE test square `300×300 µm`
- Waterloo Scientific scanning laser microscope
- Nd:YLF `1.047 µm`, CW
- ~`400 mW/cm²`
- `80 K`

## Mask-2 / metal / TLM

- resist `~4–5 µm`
- prebake `80 °C / 30 min`
- chlorobenzene `30 min`
- pattern/develop/water rinse
- same resist remains through RIE and lift-off
- Cr `30 nm`
- Au `270 nm`
- nine `300×300-µm` contacts
- gaps `50–400 µm` in 50-µm increments
- 80-K `rho_c≈9×10^-4 Ω·cm²`

## Detector benchmark

- 80 K
- stated 60° FOV
- spectral response at 1 kHz
- responsivity-vs-field near 4 µm
- representative noise field 10 V/cm
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz
- high-frequency g-r plateau ~24.5 nV/√Hz
- response cutoff ~4.4 µm
- BLIP D* ~`2.0×10^11 cm Hz^1/2 W^-1` at 4 µm
- quoted QE ~70%

Do not use the 24.5-nV/√Hz high-frequency plateau automatically as historical 1-kHz noise.

---

# P28 — empirical wet-mesa state

P28 is now the empirical control layer for P01/P01A.

## Same-UWA functional evidence

Smith et al. 2000 directly compared n-type x=0.31 HgCdTe photoconductors made with wet bromine/HBr mesas versus H2/CH4 RIE mesas.

Reported wet branch:

- background-limited under the reported condition
- `D_lambda*≈2.5×10^11 cm Hz^1/2 W^-1` at 80 K / 3 µm / stated 60° FOV

Dry branch in same comparison:

- ~`1.0×10^10`.

Same-UWA LBIC work found no significant electrical-property modification for chemically etched material relative to strong RIE-induced modification.

This supports wet mesa selection but does not recover the exact UWA recipe.

## Srivastav x=0.28 quantitative transfer center

Primary selected notation:

`2% Br2 in 3:1 EG:HBr`

with figure caption `2% Br2 + 75% EG + 25% HBr`.

Direct outputs:

- reference T `21 °C`
- mean `R_V≈2.78 µm/min`
- rate variation ~`±26%`
- `A≈0.63`, ~`±11%`
- `A=1-R_L/R_V`
- roughness ~2–7 nm, best ~2 nm
- `Ea≈7.5 kcal/mol`
- rate ~doubles per +10 °C over tested regime
- lower-T etch improves geometry/resist preservation
- 10 °C SEM example has better feature control than 21 °C example

Source test geometry:

- ~600-µm lines / 50-µm trenches
- 2D mesas / 30-µm trenches

Source starting preparation included a nominal 0.1% Br2/methanol / 1 min free etch, but that percentage basis is also unclosed and the bulk-preparation sequence is not automatically transferable to the 9.5-µm RP-01 epilayer.

## Formulation ambiguity is proven real

Primary HgCdTe literature includes:

- explicit `0.1% (w/w) Br:HBr` — Leech/Gwynn/Kibel 1989;
- explicit volume-ratio Br2:HBr — CN101740502B;
- explicit `(V/V)` bromine/methanol — US4436580A.

Therefore never guess the basis of Srivastav `2%`.

Also preserve `3:1 EG:HBr` without converting it to mL until the preparation basis is recovered or explicitly defined locally.

HBr stock assay is separately OPEN.

## Local formulation rule

If historical closure fails, create a new explicit local recipe, e.g. a branch whose bromine concentration and EG:HBr ratio are mathematically defined by mass or volume and whose HBr stock assay is recorded.

A local branch is **not** the exact Srivastav formulation even if its nominal number is 2%.

## Bath genealogy

Every batch records:

- reagent lots/assays
- explicit concentration definitions
- mixing order
- vessel and cover/seal state
- preparation time
- bath temperature
- bath age/open time
- run order
- cumulative etched area
- bath reuse state

Br2 evaporation is directly identified as a drift mechanism.

Multiple coupons from one bath are not independent bath replicates.

## Agitation

Primary source says agitation assists transport of reaction products in the viscous bath, but actual published agitation method/rate is not recovered.

Agitation changes require new rate calibration.

## Endpoint

`9.5/2.78≈3.42 min` is diagnostic only.

Using source ±26% rate spread gives ~2.71–4.62 min just to span nominal 9.5-µm removal before overetch/transfer differences.

P28 releases from:

- measured incoming local HgCdTe thickness
- measured etch depth
- lateral undercut/profile
- electrical mesa-to-mesa isolation
- qualified minimum overetch only after substrate-interface crossing

No generic overetch fraction is released.

## Rinse/quench

Exact matched rinse remains OPEN.

Other primary branches use different sequences (DI-water rinse for one Br2/HBr process; solvent-specific quench for Br/methanol/DMF), proving the rinse is chemistry-specific.

Do not silently import DI water, methanol or acetone as historical P28 practice.

## Surface/passivation handoff

Br-based HgCdTe surface studies show elemental-Te/oxide and surface-recombination evolution with air exposure in other chemistries.

Record:

- etch/rinse/dry timestamps
- atmosphere/storage
- `t_etch_to_P25`
- surface witness data
- P25 anodization `V(t)`/induction signature

P28 is not released on mesa depth alone.

---

# P27 — empirical Mask-2 lithography state

Historical fingerprint:

`4–5 µm resist -> 80 °C/30 min -> chlorobenzene 30 min -> pattern/develop/water rinse -> RIE -> 30 nm Cr + 270 nm Au lift-off`.

Chlorobenzene strongly supports positive diazo/DNQ-novolak AZ-type process family, but exact commercial resist remains OPEN.

Thickness evidence makes thicker AZ4000-family members more geometrically consistent than a thin AZ4110 example, while AZ1350J/AZ4110 remain strong mechanism/control branches.

Historical exposure dose/developer/lift-off solvent remain OPEN. Generic acetone/ultrasound is transfer evidence only.

---

# P26 — empirical Cr/Au state

Direct:

- Cr 30 nm / Au 270 nm
- 80-K `rho_c≈9×10^-4 Ω·cm²`

Thermal evaporation is strongest same-UWA transfer method, not direct RP-01 proof.

Primary HgCdTe Au studies provide 3/6/10/12 Å/s screening scales; **Cr rate remains OPEN**.

Record RIE→Cr time/air exposure. No undocumented surface reset. Baseline as-deposited/no intentional post-metal anneal.

Cryogenic TLM records optical background/shield state.

---

# P25 — empirical native anodic oxide

Strongest executable transfer center from TI HgCdTe photoconductor patent:

- HgCdTe anode
- carbon-rod cathode
- `0.1 M KOH`
- `90% EG / 10% DI water`
- galvanostatic
- ~`0.30 mA/cm²`
- ~`15 V`
- ~`2 min`
- ~`80 nm`
- uniform deep-blue appearance

This is transfer-family, not historical UWA identity.

Record full `V(t)`, induction, dV/dt, charge/area, bath/cell state, physical oxide and electrical/device outcome. P02C sidewall closure remains mandatory.

---

# P24 — empirical blocking contact

Key direct RP-01 center:

- 100 mTorr / 64 sccm / 50 W / 60 s / printed CH4/5H2
- average converted n ~2e15 cm^-3
- mobility ~3.3e4 cm²/Vs

Same/transfer evidence proves physical etch depth != electrical conversion depth and that post-RIE state can age/thermally relax.

Historical contact was not optimized; n+ density/depth remain optimization variables.

Release hierarchy:

1. plasma/material
2. majority contact/TLM
3. minority blocking via responsivity/field
4. full detector noise/D*/bandwidth/stability

---

# LPE state — P03/P21/P22

Historical Honeywell tie line:

`xL=.082, yL=.810, TL=507 °C -> xS≈.29`.

Derived source mass fractions:

- Hg `.249738`
- Cd `.012502`
- Te `.737760`

`xS/xL=3.54` is not `dxS/dxL`.

P03E: `DeltaT_SC = TL_actual - T_contact`.

P21 maps actual process coordinates/history to composition/thickness/morphology. P22 provides rank/information DOE planning. No physical tolerance is released from coded design or tie-line ratio alone.

---

# Anneal state — P04/P23

Cooldown is part of anneal. Record `T_sample(t), T_reservoir(t), pHg(t)` and initial state.

State labels:

- `N-LIKE`
- `P-LIKE`
- `TRANSITION/MULTICARRIER`

Two-carrier Hall:

`R_H=(p mu_h²-n mu_e²)/{q(p mu_h+n mu_e)²}`.

Hall sign reversal is not p=n; apparent reciprocal Hall density diverges near cancellation. Never fit one global Hall-density response through conversion.

No unique RP-01 anneal dwell/T/pHg/cooldown is released.

---

# Measurement / release essentials

P05 Hall: current/field reversal, VdP redundancy, variable field, self-heating check; multicarrier escalation when needed.

P06 FTIR: Hansen x=.30/80 K gives Eg~0.243684 eV and lambda_Eg~5.0879 µm; this is not the ~4.4-µm detector cutoff.

P10: use measured gap and active voltage `E=V_active/L_measured`.

P11: absolute responsivity through calibrated radiometry/geometry.

P12: `NEP=e_n/R_v`; `D*=R_v sqrt(A)/e_n`; subtract independent contributions at PSD level.

P13: de-embed `H_source H_optics H_bias H_preamp H_cable H_instrument`; use `tau_eff` unless bulk-lifetime interpretation is justified.

P17: separate measurement/spatial/run/lot/long-term variation; no generic Cpk threshold.

P18: `signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification`.

P19: trace final detector requirement to physical characteristic/intermediate metric/process/release/failure response.

P20 analytical sensitivities support experiment design; they do not replace empirical process data.

---

# Highest-priority OPEN practical details after Round 21

## Wet mesa

- exact UWA RP-01 wet formulation
- Srivastav 2% basis
- 3:1 EG:HBr preparation basis
- HBr stock assay
- mixing order
- reported agitation method/rate
- matched rinse/quench/dry
- local x≈0.30 rate/anisotropy
- minimum robust through-layer overetch
- electrical-isolation limit
- maximum clean-to-P25 exposure

Primary recovery target: Vanya Srivastav IISc thesis `G25544.pdf`, whose institutional record is found but full experimental text has not been recovered through the current accessible route.

## CdZnTe substrate / LPE interface

- exact RP-01 Zn fraction
- crystallographic face/orientation
- miscut
- final polish/etch/clean
- clean-to-growth interval
- surface roughness/chemistry acceptance

## Anneal

- exact RP-01 apparatus geometry
- Hg reservoir charge/geometry
- sample/reservoir thermal trajectories
- pHg coordinate
- cooldown

## RIE/contact/lithography

- exact Plasma Technology reactor model/RF/self-bias/sample T
- exact RIE oxide-clear time
- exact historical metal deposition method/rates/vacuum
- exact Mask-2 resist/exposure/developer/lift-off solvent

## LPE

- source synthesis details
- actual charge mass/well geometry
- growth contact time/supercooling process sensitivity
- source-use/depletion history

---

# Active negative/source-recovery record

Identified but not fully recovered through current routes:

- Vanya Srivastav IISc thesis `G25544.pdf`
- John Kenion White 2005 UWA thesis full experimental text
- Ryan Westerhout 2013 UWA thesis full experimental text
- Smith et al. 2000 “Dry plasma technology for in-situ vacuum processing…” full experimental text
- Musca/Smith/Dell/Faraone photoconductor contact/passivation proceedings traveler

“Not recovered” does not mean absent.

---

# Next logical work

Continue empirical/practical source recovery. Strongest next candidate:

## Round 22 — CdZnTe substrate face/orientation/final-surface closure

1. Search primary RP-01/UWA/Honeywell LPE papers, theses and patents for CdZnTe Zn fraction, face/orientation, miscut, polishing, final chemical preparation and clean-to-growth sequence.
2. Separate bulk-substrate specification from final surface state.
3. Recover actual surface roughness/etch/polish numbers where primary sources disclose them.
4. Connect the released substrate surface to P03 LPE morphology/interface quality rather than accepting a vendor label alone.
5. Create a P29 empirical substrate/final-surface window and traveler if the evidence supports it.

If source recovery for P07 is poor, pivot in the same round to primary Hg-anneal apparatus/reservoir literature rather than inventing substrate values.

Do not populate production tolerances without local repeated-device data.
