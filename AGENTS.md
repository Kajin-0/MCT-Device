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
8. Treat passivation, post-RIE elapsed time/thermal exposure, metal-interface exposure, anneal cooldown and packaging as process variables.
9. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Engineering specifications come from required detector/material performance; observed process spread does not define its own passing limits.
11. Failure diagnosis uses competing hypotheses and discriminating tests; never force one cause from one symptom.
12. Repository scientific procedures do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.
13. Every numerical sensitivity/tolerance must state protected output, input, operating point and evidence class. Proxy relations may size experiments but cannot release production specifications.
14. A tie-line ratio such as `xS/xL` is not a local derivative `dxS/dxL` when other coordinates vary.
15. A coded DOE result does not create a physical process tolerance.
16. Repeated observations from one melt/source genealogy are not independent replicates.
17. Never regress reciprocal Hall density through a p/n Hall-sign transition; use signed Hall/tensor information near transition.
18. **Empirical/practical literature first.** Before creating a theoretical placeholder, search primary papers, theses, patents and institutional archives for actual times, temperatures, concentrations, flows, pressures, dimensions, apparatus, metrology settings, outputs and failure observations.
19. Theory connects genuine literature gaps and checks consistency; it does not displace experimentally reported process information.
20. A successful historical process condition is not automatically an optimum.
21. Equal anodic-oxide thickness does not imply equal interface state; record chemistry, surface, cell, current, full `V(t)`, charge/area, oxide metrology and detector response.
22. No undocumented ion mill, wet etch or plasma clean may be inserted between qualified P08 RIE and Cr deposition.
23. Baseline P26 is as-deposited; post-metal anneals from other contact architectures are transfer evidence only.
24. Cryogenic TLM records optical-background/shield state as well as temperature/current.
25. **Mask-2 identity rule:** chlorobenzene strongly constrains the historical process to a positive diazo/DNQ-novolak AZ-type lift-off family, but it does not identify a commercial resist. Candidate-family consistency is not historical identity.
26. **Mask-2 sequence rule:** preserve the RP-01 wording `prebake -> chlorobenzene -> then patterned/developed/water rinse`. Do not silently move the chlorobenzene step relative to exposure; carry both sequence branches until direct UWA evidence closes it.
27. A developer/lift-off solvent used in generic historical AZ processing is not automatically the RP-01 developer/lift-off solvent.

---

# Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_empirical_lithography_round20.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_empirical_metallization_round19.md`
- `research/2026-08-16_checkpoint_after_empirical_passivation_round18.md`
- `research/2026-08-16_checkpoint_after_empirical_blocking_contact_round17.md`
- `research/2026-08-16_checkpoint_after_hg_anneal_boundary_round16.md`
- `research/2026-08-16_checkpoint_after_information_design_round15.md`
- `research/2026-08-16_checkpoint_after_lpe_jacobian_round14.md`
- `research/2026-08-16_checkpoint_after_analytical_sensitivity_round13.md`

Latest source/gap addenda:

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
- P07 CdZnTe + P07A/P07B/P07C
- P08 RIE blocking contact + P08A–P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating
- P11 absolute radiometry/responsivity
- P12 noise/PSD/NEP/D* + P12A/P12B
- P13 temporal response + P13A
- P14 lithography/CD + P14A
- P15 cryogenic package
- P16 master end-to-end traveler
- P17 statistical release/capability
- P18 failure analysis/CAPA
- P19 requirements traceability
- P20 analytical sensitivity / allocation
- P21 LPE empirical Jacobian
- P22 information-optimal DOE planning
- P23 Hg-anneal state boundary / local Jacobian
- P24 blocking-contact empirical process window + register
- P25 anodic-oxide empirical process window + register
- P26 Cr/Au metallization/lift-off empirical process window + register
- **P27 Mask-2 photoresist/exposure/developer/lift-off empirical process window + register**

P24–P27 are deliberately empirical/practical.

---

# Canonical RP-01 anchors — do not drift

## Material

- LPE n-HgCdTe on insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `mu=4.0×10^4 cm²/V·s`
- active thickness `9.5 µm`
- supplier n/mu measurement temperature undisclosed

## Native oxide

- native anodic oxide
- `~800 Å = 80 nm`
- exact historical bath/current/cell/endpoint/rinse remain open

## RIE

- Plasma Technology parallel-plate
- printed `CH4/5H2`
- `64 sccm` total
- `100 mTorr`
- `50 W`
- `60 s`
- converted average `n≈2.0×10^15 cm^-3`
- converted `mu≈3.3×10^4 cm²/V·s`
- Hall/resistivity at 80 K and 300 K, variable field to 2 T
- earlier similar-condition n-type work: ~8-µm conversion depth; do not combine with the density as one direct canonical measurement

RP-01 LBIC:

- 300×300-µm patterned RIE region
- Waterloo Scientific scanning laser microscope
- Nd:YLF 1.047 µm CW
- ~400 mW/cm²
- 80 K

## Mask-2 / metal / TLM

- resist `~4–5 µm`
- prebake `80 °C / 30 min`
- chlorobenzene `30 min`
- then patterned/developed/water rinse
- same resist survives RIE and supports metal lift-off
- Cr `30 nm`
- Au `270 nm`
- nine `300×300-µm` contacts
- gaps 50–400 µm in 50-µm increments
- 80-K `rho_c≈9×10^-4 Ω·cm²`

## Detector benchmark

- 80 K
- stated 60° FOV
- spectral response at 1 kHz
- representative noise field 10 V/cm
- 1/f knee ~3 kHz
- high-frequency g-r plateau ~24.5 nV/√Hz
- cutoff ~4.4 µm
- BLIP D* ~`2×10^11 cm Hz^1/2 W^-1` at 4 µm
- quoted QE ~70%

Do not use the 24.5-nV/√Hz high-frequency plateau as the historical 1-kHz noise automatically.

---

# P27 — empirical Mask-2 state

## Process-family conclusion

Historical chlorobenzene single-layer lift-off literature establishes a **positive AZ-type diazo/DNQ-novolak** process family using aromatic-solvent treatment to create a re-entrant profile by differential development.

This substantially narrows chemistry, but the RP-01 commercial resist remains `OPEN`.

## Candidate hierarchy

### AZ4110

Strong direct chlorobenzene reference. One quantified primary example:

- 4000 rpm / 30 s
- 90 °C / 2 min bake
- 90 mJ/cm²
- chlorobenzene 28–30 °C / 2 min
- aqueous developer diluted 1:1
- 60 s development
- ~1.1-µm film

Use as chlorobenzene/exposure/developer control; thickness is poor match to RP-01 in this example.

### AZ4330

Primary example:

- ~4.3 µm
- 3500 rpm / 30 s
- 85 °C / 10 min
- 150 mJ/cm² at 365 nm

Strong thickness match, but the example is not a chlorobenzene process.

### AZ4400 / AZ4620

Primary examples establish ~4–5-µm film capability; product-specific RP-01-style chlorobenzene recipes remain unrecovered.

Therefore:

- AZ1350J/AZ4110 lineage = strong chlorobenzene-control reference;
- AZ4330/AZ4400/AZ4620 class = stronger 4–5-µm thickness candidates;
- **none is identified as RP-01**.

## Quantified chlorobenzene control branch

Primary AZ1350J example:

- 3000 rpm
- 90 °C / 20 min bake
- chlorobenzene 15 min
- 90 °C / 10 min post-soak bake
- ~0.4-µm overhang in that process
- acetone 10 min + ultrasonics, then fresh acetone 5 min

Comparative branch:

- 4000 rpm
- 90 °C / 10 min
- ~78.9 mJ/cm² exposure
- chlorobenzene 10 min
- Microposit 303A developer 10 s
- ~8 h acetone/ultrasonic lift-off for its ~1-µm Cr/Al stack

Use as process-control evidence only; do not transplant values into RP-01.

## Chlorobenzene sequence ambiguity

Carry two qualification branches until direct UWA evidence closes ordering:

A. `80 °C/30 min -> CB 30 min -> expose -> develop`

B. `80 °C/30 min -> expose -> CB 30 min -> develop`

Compare film loss, CD, undercut, scum, P08 survival and P26 lift-off.

## Exposure/developer status

Related primary examples give useful dose scales (~79, 90, 150 mJ/cm²), not an RP-01 dose.

Aqueous alkaline developer family is mechanism-consistent; exact UWA product/dilution/time remain open.

P27 requires a product-specific dose/development matrix on the actual 4–5-µm film after the chosen RP-01 bake/CB branch.

## Chlorobenzene bath control

Record grade/lot, fresh/reused state, age, temperature, agitation, exact time, sample orientation and resist thickness before/after soak. `30 min` alone is not an adequate process record.

## RIE + lift-off gate

A Mask-2 candidate must retain measurable undercut/profile after P08 and cleanly lift off the actual P26 30/270-nm Cr/Au stack.

Exact historical lift-off solvent remains open. Acetone is transfer-lineage evidence only. Do not baseline ultrasonics on qualified HgCdTe without sacrificial damage validation.

---

# P26 — empirical Cr/Au state

- thermal evaporation is the strongest current same-UWA transfer method but not historical RP-01 proof;
- RP-01 directly proposes load-lock-connected RIE/metal vacuum processing as advantageous, but canonical execution is unproved;
- record complete RIE-to-Cr timing/atmosphere;
- no undocumented pre-metal surface reset;
- Au transfer studies give 3–12 Å/s real HgCdTe rate scales; Cr rate remains open;
- baseline no intentional post-metal anneal;
- cryogenic TLM records optical-background/shield state;
- full P26 sequence ends in TLM, aging, responsivity/noise/time-response closure.

---

# P25 — empirical native oxide state

Strongest executable transfer center:

- HgCdTe anode / carbon cathode
- 0.1 M KOH
- 90% EG / 10% DI water
- galvanostatic ~0.30 mA/cm²
- ~15 V
- ~2 min
- ~80 nm

Not historical UWA identity. Record full bath/cell state, `V(t)`, induction, charge/area, thickness, interface/sidewall and detector outcomes.

---

# P24 — empirical blocking-contact state

- physical etch depth and electrical conversion depth are distinct;
- local transfer must measure oxide clear, recession, sheet transport, LBIC vertical/lateral conversion, TLM and detector sweepout/noise;
- pressure/sample temperature are high-priority plasma-transfer coordinates;
- post-RIE storage/thermal history must be recorded;
- historical RP-01 contact was successful but explicitly not optimized;
- no process is released on TLM alone.

---

# LPE / anneal continuity

Historical Honeywell tie line: `xL=.082, yL=.810, TL=507 °C -> xS≈.29`; derived source mass fractions Hg .249738 / Cd .012502 / Te .737760. `xS/xL=3.54` is not `dxS/dxL`.

P03E actual supercooling: `DeltaT_SC=TL_actual-T_contact`.

P21/P22 govern empirical growth Jacobian + DOE; physical tolerances remain local-data dependent.

P23 anneal uses signed Hall state labels `N-LIKE / P-LIKE / TRANSITION-MULTICARRIER`, records `T_sample(t), T_reservoir(t), pHg(t)` and treats cooldown as part of the process. No unique RP-01 anneal traveler is released.

---

# Highest-priority OPEN practical details after Round 20

## P01 wet mesa — next empirical target

Near-composition empirical branch currently has:

- x≈0.28
- nominal `2% Br2` in `3:1 ethylene glycol:HBr`
- rate ~`2.78 µm/min` at 21 °C
- anisotropy ~`0.63`
- roughness ~`2 nm`
- ~±26% rate variation
- activation energy ~`7.5 kcal/mol`
- rate approximately doubles per +10 °C in reported range

Critical unresolved item: **the source does not define the percentage basis of “2% Br2.”**

Round 21 should search original/same-author papers, theses, cited formulation lineage and patents for:

- wt%, vol%, wt/vol or other basis;
- HBr concentration/reagent grades;
- mixing order;
- bath volume/sample area;
- agitation/orientation;
- temperature-control method;
- rinse/quench/dry;
- endpoint/overetch;
- etch-depth and sidewall metrology;
- post-etch surface chemistry.

Do not use `9.5 µm / 2.78 µm/min ≈ 3.42 min` as a setpoint; it is diagnostic only.

## Other major historical gaps

- exact P27 UWA resist/exposure/developer/lift-off solvent
- exact P26 deposition tool/vacuum/Cr-Au rates
- exact P08 reactor geometry/self-bias/sample temperature/oxide-clear time
- exact P25 UWA anodization traveler
- exact CdZnTe face/miscut/final clean
- complete Hg anneal trajectory
- full LPE source synthesis/charge mass/well geometry/growth trajectory

These gaps trigger literature recovery first.

---

# Active source-recovery / negative record

Not recovered through current public routes:

- full John Kenion White 2005 UWA thesis experimental text
- full Ryan Westerhout 2013 UWA thesis experimental text
- full Smith et al. 2000 in-situ vacuum-processing experimental text
- full Musca/Smith/Dell/Faraone 1999 contact/passivation proceedings traveler
- UWA document naming RP-01 photoresist/developer/lift-off solvent
- exact historical Cr/Au deposition operating details

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 21: empirical P01 wet-mesa chemistry / endpoint / rinse recovery**.

Keep the near-x published rate/morphology data separate from the still-unknown exact solution preparation. Recover primary numbers before proposing a local recipe. If the percent basis remains unrecoverable, define multiple chemically explicit candidate formulations rather than silently selecting one meaning of “2%.”

Do not populate production tolerances without repeated local data.
