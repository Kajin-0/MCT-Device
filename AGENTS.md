# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** that a competent researcher can execute without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains direct historical anchors, practical transfer procedures, empirical process windows, measurement SOPs, release/failure architecture, and explicit unresolved gaps.

---

# Non-negotiable rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, explicit derivation, or a named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01 publication, same-lineage evidence, transfer-family evidence, model values, derived physics, apparatus calibration and local qualification.
4. Every critical process step requires output metrology and a pass/fail or qualification gate.
5. Preserve negative searches, failed branches, rejected inferences, corrections and source conflicts.
6. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density and measured geometry distinct.
7. Keep majority-carrier contact resistivity `rho_c` distinct from minority-carrier contact recombination/effective loss boundary `S_c`.
8. Use measured fabricated geometry for field, area and D* normalization.
9. Treat passivation, post-RIE elapsed time/thermal exposure, metal-interface exposure, anneal cooldown and packaging as detector-process variables.
10. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
11. Engineering specifications come from required detector/material performance; observed process spread does not define its own passing limits.
12. Failure diagnosis uses competing hypotheses and discriminating tests; never force one cause from one symptom.
13. Every controlled process variable should trace forward to a detector requirement.
14. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.
15. Every numerical sensitivity/tolerance must state protected output, input variable, operating point and evidence class. Proxy relations may size an experiment but cannot release a production specification.
16. A tabulated equilibrium ratio such as `xS/xL` is not a differential `dxS/dxL` when other phase coordinates vary.
17. A coded DOE result does not create a physical process tolerance. Physical perturbations require metrology/run variance, apparatus capability and same-regime bounds.
18. Repeated observations from one melt/source genealogy are not independent process replicates.
19. Never regress reciprocal Hall density through a p/n Hall-sign transition. Near transition use signed Hall/tensor information and multicarrier analysis.
20. Anneal tolerances must satisfy both detector/material-performance budget and margin to the carrier-state transition zone.
21. **Empirical/practical literature first.** Before creating another theoretical placeholder, search primary papers, theses, patents and institutional repositories for actual times, temperatures, flows, pressures, concentrations, dimensions, apparatus, metrology settings, output values and failure observations.
22. Theory connects genuine literature gaps, checks consistency and allocates requirements; it does not displace experimentally reported process information.
23. A successful historical process condition is not automatically an optimum. Preserve author statements identifying unoptimized variables.
24. For anodic passivation, equal oxide thickness does not imply equal interface state. Record chemistry, starting surface, cell geometry, current density, full `V(t)`, charge/area, oxide metrology and downstream device response.
25. Color is secondary oxide metrology only.
26. For metal contacts, **RIE-to-metal time/atmosphere and pre-metal surface intervention are process variables**. No undocumented ion mill, wet etch or plasma clean may be inserted between the qualified P08 surface and Cr deposition.
27. A published post-metal anneal from another HgCdTe contact architecture is not an RP-01 anneal. Baseline P26 is as-deposited unless direct evidence or local qualification supports otherwise.
28. Cryogenic TLM must record optical-background/shield state as well as temperature/current because HgCdTe background carriers can bias low-temperature contact extraction.

---

# Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_empirical_metallization_round19.md`

Then read, in descending order as needed:

- `research/2026-08-16_checkpoint_after_empirical_passivation_round18.md`
- `research/2026-08-16_checkpoint_after_empirical_blocking_contact_round17.md`
- `research/2026-08-16_checkpoint_after_hg_anneal_boundary_round16.md`
- `research/2026-08-16_checkpoint_after_information_design_round15.md`
- `research/2026-08-16_checkpoint_after_lpe_jacobian_round14.md`
- `research/2026-08-16_checkpoint_after_analytical_sensitivity_round13.md`

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND19.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND19.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND18.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND18.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND17.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND17.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND16.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND16.md`
- round-14/15 and older round-6/7/8/9 provenance/gap files as needed.

---

# Controlled module set

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP material metrology
- P06 FTIR composition/thickness mapping
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
- **P26 Cr/Au metallization/lift-off empirical process window + register**

P24–P26 are deliberately empirical/practical and supplement the earlier physics/provenance modules rather than replacing them.

---

# Canonical RP-01 direct anchors — do not drift

## Material

- LPE n-HgCdTe on electrically insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `mu=4.0×10^4 cm²/V·s`
- active thickness `9.5 µm`
- supplier n/mu measurement temperature remains undisclosed

## Native anodic oxide

- native anodic oxide
- nominal thickness `~800 Å = 80 nm`
- formed after mesa definition and before Mask-2/RIE
- exact historical bath/current/cell/endpoint/rinse remain open

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

- converted average electron density `~2.0×10^15 cm^-3`, averaged over converted thickness
- mobility `~3.3×10^4 cm²/V·s`
- Hall/resistivity at `80 K` and `300 K`
- variable magnetic field to `2 T`

Earlier same-lineage n-type work cited by RP-01:

- approximately `8 µm` n+ conversion under similar RIE conditions

Do not combine 2e15 cm^-3 and 8 µm and call the resulting sheet density one directly measured RP-01 quantity.

## RP-01 LBIC apparatus

- patterned RIE test square `300×300 µm`
- Waterloo Scientific scanning laser microscope
- Nd:YLF laser
- `1.047 µm`
- CW
- approximately `400 mW/cm²`
- `80 K`

## Mask-2 / metal / TLM

- resist `~4–5 µm`
- prebake `80 °C / 30 min`
- chlorobenzene `30 min`
- pattern/develop/water rinse
- same resist remains through RIE and metal lift-off
- Cr `300 Å = 30 nm`
- Au `2700 Å = 270 nm`
- nine `300×300-µm` contacts
- adjacent gaps `50–400 µm` in 50-µm increments
- 80-K `rho_c≈9×10^-4 Ω·cm²`

## Detector benchmark

- 80 K
- stated 60° FOV
- spectral response at 1 kHz
- responsivity-vs-field comparison near 4 µm
- representative noise field 10 V/cm
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz
- high-frequency g-r plateau ~24.5 nV/√Hz
- cutoff ~4.4 µm
- BLIP D* ~`2.0×10^11 cm Hz^1/2 W^-1` at 4 µm
- quoted QE ~70%

Do not use the high-frequency 24.5-nV/√Hz plateau as the historical 1-kHz noise automatically.

---

# P26 — empirical Cr/Au metallization/lift-off state

P26 is now the controlling empirical front end for the P09/P14A metal-contact branch.

## What is direct versus still open

Direct historical:

- Cr 30 nm
- Au 270 nm
- chlorobenzene-shaped 4–5-µm Mask-2 resist is suitable for lift-off after RIE
- 80-K `rho_c≈9×10^-4 Ω·cm²`

Still not recovered directly:

- deposition method/tool
- base/process pressure
- Cr rate
- Au rate
- source purity/boat/crucible
- sample temperature
- actual RIE-to-Cr delay
- whether canonical Cr→Au had a vacuum break
- lift-off solvent/time/temp/agitation/rinse/dry

## Thermal evaporation is the strongest current transfer method

Same-UWA 1998 HgCdTe detector work directly used **angled thermal evaporation** for contact-metal deposition.

Modern UWA HgCdTe photoconductors directly use Cr/Au `10/200 nm` by thermal evaporation and demonstrate linear/symmetric I–V.

Therefore thermal evaporation is the preferred **local first-transfer method** if compatible equipment exists, but it is not historical RP-01 proof.

## Direct RP-01 load-lock nuance

Smith et al. explicitly identify connecting the RIE chamber to the metal-deposition system through a load lock as a beneficial vacuum-processing architecture.

Classification:

`DIRECT-RP01-PROPOSED-ARCHITECTURE`.

Do not claim the measured historical devices were necessarily transferred in vacuum.

## RIE-to-metal timing is mandatory

P26 records:

- `t_RF_off`
- RIE vent/unload
- metal load/pumpdown
- `t_Cr_start`
- `t_Cr_end`
- `t_Au_start/end`
- total and actual air/inert exposure
- metal-to-lift-off delay

A 2026 x≈0.30 LPE HgCdTe interface study used about 10 min air exposure after deoxidation as a representative pre-metal state and directly found Te-oxide/contaminant evolution at the buried interface. Its oxide numbers are transfer-only, but the timing conclusion is physical.

## No undocumented pre-metal reset

Other HgCdTe contacts deliberately use 500-eV Ar ion milling and/or short Br2/HBr cleans before metal. Those are contact-engineering operations, not neutral cleaning.

RP-01 baseline:

`qualified P08 RIE surface -> controlled transfer -> Cr`.

Any added wet clean, ion mill or plasma clean becomes a separate branch requiring remeasurement of P08 conversion + TLM + detector outputs.

## Au empirical rate scale

Primary HgCdTe Au studies report:

- 3 Å/s
- 6 Å/s
- 10 Å/s
- 12 Å/s

across thermal/e-beam p-HgCdTe branches.

Use these only as practical experiment-sizing anchors.

**Cr rate remains OPEN. Do not copy the Au rate to Cr.**

## Post-metal thermal history

A primary x≈0.29 p-HgCdTe Au study reported:

- as-deposited `rho_c=2.73×10^-3 Ω·cm²`
- air anneal `80 °C / 2 h`
- post-anneal `rho_c=7.11×10^-4 Ω·cm²`

This proves thermal history can materially change contact resistance in that branch. It is not an RP-01 anneal.

P26 baseline is **as-deposited / no intentional post-metal anneal**. Any anneal requires its own recipe ID and detector requalification.

## Cryogenic TLM background state

Other primary HgCdTe TLM work demonstrates that background-generated carriers can distort low-temperature contact extraction.

P26 records optical background/cold-shield state, temperature, current and self-heating with every cryogenic TLM dataset.

## P26 local sequence

1. P08 passes and P14 resist profile survives RIE.
2. Shortest controlled P08→metal transfer baseline.
3. No undocumented surface reset.
4. Log chamber state/base/process pressure.
5. Deposit calibrated 30-nm Cr.
6. Remain under vacuum through Au when practical; record any break.
7. Deposit calibrated 270-nm Au.
8. Record rate and sample-temperature histories.
9. No baseline post-metal anneal.
10. Execute sacrificially qualified lift-off.
11. Inspect actual metal CDs/gaps and defects.
12. Measure dark 80-K TLM with optical-background state recorded.
13. Compare with historical rho_c scale.
14. Age/thermal-cycle selected structures.
15. Close with P10–P13 detector metrics.

---

# P25 — empirical native anodic-oxide/passivation state

Strongest executable transfer center is the TI HgCdTe photoconductor anodization process:

- HgCdTe anode
- carbon-rod cathode
- `0.1 M KOH`
- `90% EG / 10% DI water`
- galvanostatic
- ~`0.30 mA/cm²`
- ~`15 V`
- ~`2 min`
- ~`800 Å = 80 nm`
- uniform deep-blue appearance

This is a transfer center, not the historical UWA recipe.

P25 records bath composition/age, exposed area, electrode geometry, bath temperature/agitation, full `V(t)`, induction time, dV/dt, charge/area and independent oxide thickness.

Equal ~80-nm oxide does not imply equal interface chemistry/fixed charge/recombination/noise.

P02C sidewall/passivation and P08/P09/P12 downstream closure remain mandatory.

---

# P24 — empirical blocking-contact state

Key practical evidence:

- p-x≈0.31 transfer branch: ~0.2-µm physical etch produced ~1.5-µm electrical conversion under its RIE condition -> `d_etch != d_conv`.
- x≈0.29 UWA LBIC branch used 340 mTorr / CH4-H2 / 0.4 W cm^-2; some public snippets conflict at ~390 mTorr, so preserve the institutional 340-mTorr value plus conflict.
- plasma conversion/depth in x≈0.30 transfer work is especially sensitive to pressure and temperature; RIE/ICP power also matters.
- plasma-induced state can relax/thermally reverse in other branches; record RIE-to-Hall/LBIC/metal delay, storage T and later thermal events.
- RP-01 authors explicitly say the historical blocking contact was not optimized; n+ density and junction depth remain optimization variables.

P24 release hierarchy:

1. plasma/material state
2. majority contact/TLM
3. minority blocking via responsivity-vs-field
4. full detector noise/D*/bandwidth/stability

No contact process is released on TLM alone.

---

# LPE state — P03/P21/P22

Historical Honeywell tie line:

`xL=.082, yL=.810, TL=507 °C -> historical xS≈.29`.

Derived source mass fractions:

- Hg `.249738`
- Cd `.012502`
- Te `.737760`

`xS/xL=3.54` is not `dxS/dxL`.

P03E uses actual supercooling:

`DeltaT_SC = TL_actual - T_contact`.

P21 maps growth coordinates/history into `{x_opt, thickness, uniformity, optical edge, morphology}`. P22 provides coded/Fisher-information DOE planning. No balance/temperature/time tolerance is released without local data.

---

# Anneal state — P04/P23

Cooldown is part of the anneal. Record:

`T_sample(t), T_reservoir(t), pHg(t)`.

Use final measured state:

`{carrier state, n_H/multicarrier, mu_H, optical x/edge, thickness, morphology, lifetime/device proxy}`.

P23 labels:

- `N-LIKE`
- `P-LIKE`
- `TRANSITION/MULTICARRIER`

Two-carrier low-field Hall:

`R_H=(p mu_h²-n mu_e²)/{q(p mu_h+n mu_e)²}`.

Hall sign reversal is not p=n; apparent reciprocal Hall density is singular near cancellation. Never fit one global log-density response through conversion.

No unique RP-01 anneal dwell/T/pHg/cooldown is released.

---

# Substrate / wet mesa / surface

- CdZnTe is the correct substrate family.
- Exact RP-01 Zn fraction/orientation/miscut/final-surface history remain qualification variables.
- P07C releases final surface by removed depth + morphology/chemistry proxy + clean-to-load + resulting interface quality.

Near-x wet-mesa transfer branch:

- nominal 2% Br2 in 3:1 EG:HBr
- ~2.78 µm/min at 21 °C
- anisotropy ~0.63
- roughness ~2 nm
- rate variation ~±26%
- percentage basis of “2% Br2” remains undefined in the source

Do not guess wt%, vol%, or wt/vol.

---

# Measurement state

## Hall — P05

Use current reversal, field reversal, van der Pauw redundancy, variable field and current-linearity/self-heating checks. Escalate to multicarrier/QMSA when curvature/sign changes/MR invalidate one-carrier interpretation.

RP-01 screening consistency:

- rho ~0.159 Ω·cm
- Rs ~168 Ω/sq for 9.5 µm
- |RH| ~6.37×10^3 cm³/C

## FTIR — P06

At x=.30, 80 K, Hansen gives Eg~0.243684 eV and lambda_Eg~5.0879 µm. This is not the detector's ~4.4-µm measured cutoff.

## Bias — P10

Use measured gap/active voltage: `E=V_active/L_measured`. Track self-heating separately.

## Radiometry — P11

Use calibrated radiance/transfer detector and physical aperture/view factor. Historical 300-K/4.4-µm-step/60° full-cone reconstruction gives ~1.12e15 photons cm^-2 s^-1, only a consistency reconstruction.

## Noise — P12

`NEP=e_n/R_v`; `D*=R_v sqrt(A)/e_n`. Subtract independent contributions at PSD level.

## Temporal — P13

`H_meas=H_source H_optics H_detector H_bias H_preamp H_cable H_instrument`.

De-embed before calling a rolloff detector bandwidth. Use `tau_eff` unless bulk-lifetime interpretation is justified.

---

# P17/P18/P19/P20 architecture

P17: separate measurement -> spatial -> run -> lot -> long-term tool/operator. No generic Cpk threshold. End-to-end process remains below `PILOT-RELEASE` without repeated local fabrication data.

P18: `signature -> competing mechanisms -> discriminating tests -> root cause -> containment/CAPA -> verification`.

P19: trace `final requirement -> physical characteristic -> intermediate metric -> process -> P17 release -> P18 response`.

P20 evidence classes: `IDENTITY`, `MODEL-CONDITIONAL`, `PROXY-CONDITIONAL`, `EMPIRICAL-REQUIRED`. Analytical results support but do not replace empirical process data.

---

# Highest-priority OPEN practical details after Round 19

## P14 lithography / Mask-2 — strongest next empirical target

Direct RP-01 gives thickness/bake/chlorobenzene but not:

- resist manufacturer/product/formulation
- dilution/solids
- spin speed/time/acceleration
- exposure tool/wavelength/dose/contact/proximity mode
- mask polarity/details
- developer manufacturer/product/concentration
- development time/temperature/agitation
- exact chlorobenzene grade/temperature/agitation
- final lift-off solvent/time/temp/agitation/rinse/dry

These should trigger a literature/thesis/patent recovery pass before arbitrary local values.

## P26 metallization

Still search for exact historical:

- deposition method/tool
- base/process pressure
- Cr/Au rates
- source purity/hardware
- sample temperature
- RIE-to-Cr delay
- Cr-to-Au vacuum state
- lift-off solvent/time/agitation/rinse/dry

High-priority sources remain the full 2000 same-UWA in-situ-vacuum paper, full 1999 contact/passivation proceedings paper, and RP-01-era UWA theses/process appendices.

## Blocking contact

- exact Plasma Technology reactor model/RF frequency/electrode geometry/self-bias/sample T
- oxide-clear time
- canonical physical recession
- exact process tied to ~8-µm n+ depth
- canonical n(z)/lateral conversion
- RP-01 post-RIE stability

## Native oxide

- exact UWA bath/current/cell/rinse
- pre-anodization clean
- bath convention/reagent grades
- local V(t)/Q/A/thickness capability
- electrical/interface/noise release metrics

## Other

- exact CdZnTe face/miscut/final clean
- complete Hg anneal architecture/trajectory
- full LPE source synthesis/charge mass/well geometry/growth trajectory
- mesa etch percentage basis/end-point closure

---

# Active negative/source-recovery record

Not yet recovered through current public routes:

- full John Kenion White 2005 UWA thesis experimental text
- full Ryan Westerhout 2013 UWA thesis experimental text
- full Smith et al. 2000 “Dry plasma technology for in-situ vacuum processing…” experimental text
- full Musca/Smith/Dell/Faraone 1999 photoconductor contact/passivation proceedings experimental traveler
- historical Cr/Au deposition/lift-off operating details

“Not recovered” does not mean absent.

---

# Next logical work

Continue the user-requested empirical/practical sequence with **Round 20: exact P14 photoresist / exposure / developer / lift-off recovery**.

1. Search RP-01-era UWA papers, theses, proceedings and historical chlorobenzene single-layer lift-off literature.
2. Recover actual positive-resist products capable of 4–5 µm films, spin curves, 80 °C bake behavior, chlorobenzene timing/order, exposure doses, developers, development times and lift-off solvents where primary sources disclose them.
3. Keep direct RP-01 fingerprint fixed: `4–5 µm / 80 °C 30 min / chlorobenzene 30 min / pattern-develop-water rinse / RIE survival / 30+270 nm metal lift-off`.
4. Do not identify a commercial resist merely because it is historically plausible.
5. Create a P27 empirical lithography/lift-off process window and traveler if the literature supports useful practical branches.
6. Use theory only after primary empirical recovery is exhausted.

Do not populate production tolerances without local repeated-device data.
