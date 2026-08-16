# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** executable by a competent researcher without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repo contains direct historical anchors, empirical transfer procedures, controlled metrology, qualification registers, gap/source ledgers, negative-search records and explicit unresolved history.

---

# Non-negotiable scientific/provenance rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, an explicit derivation or named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01, same-lineage, transfer-family, model, derived, apparatus-calibration and local-qualification evidence.
4. Every critical process step requires outcome metrology plus a pass/fail/qualification gate.
5. Preserve negative searches, rejected inferences, failed branches, corrections and source conflicts.
6. Use measured fabricated geometry for electric field, active area and `D*` normalization.
7. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density, `rho_c` and minority-carrier blocking metrics distinct.
8. Process history includes passivation exposure, wet-etch surface state, RIE chamber state, post-RIE age, metal-interface exposure, LPE source genealogy, anneal cooldown, substrate clean-to-load, package and thermal-cycle history.
9. Measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Specifications derive from downstream material/device requirements, not observed process spread.
11. Failure diagnosis: signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification.
12. Repository procedures do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S.
13. Every numerical sensitivity/tolerance states protected output, input, operating point and evidence class. Proxies may size experiments but cannot release production specifications.
14. `xS/xL` is not `dxS/dxL` when other equilibrium coordinates change.
15. Coded DOE coordinates do not create physical tolerances.
16. Repeated observations from one melt/source/bath/substrate/anneal-source/chamber/package genealogy are not iid independent replicates.
17. Never regress reciprocal Hall density through a p/n sign transition; use signed Hall/tensor information near transition.
18. **Empirical/practical literature first.** Before theoretical placeholders, search primary papers, theses, patents, proceedings and institutional archives for real process/apparatus numbers and outcomes.
19. Theory checks consistency and bridges genuine gaps; it does not displace empirical process data.
20. A successful historical center is not automatically an optimum.
21. Equal anodic-oxide thickness does not imply equal interface state.
22. No undocumented ion mill, wet etch or plasma clean may be inserted between qualified P08 RIE and Cr deposition.
23. Baseline P26 is as-deposited; post-metal anneals from other architectures are transfer evidence only.
24. Cryogenic TLM records optical-background/shield state as well as temperature/current.
25. Chlorobenzene constrains Mask-2 to a positive diazo/DNQ-novolak lift-off family but does not identify a commercial resist.
26. Preserve RP-01 Mask-2 ordering `prebake -> chlorobenzene -> patterned/developed/water rinse`; do not silently reorder.
27. Generic developer or lift-off solvent is not historical proof.
28. **Wet-etch percentage without basis is not executable.** Never guess the basis of Srivastav `2% Br2`.
29. Preserve `3:1 EG:HBr` symbolically until preparation basis is recovered or locally defined.
30. HBr stock assay and wet-etch bath genealogy are process variables.
31. **Wet-mesa endpoint:** time is input; measured through-layer isolation is output.
32. Post-wet-etch air time/surface state belongs to the P28->P25 handoff.
33. **CdZnTe vendor label is not interface specification.** Record composition/lattice state, plane, polarity, miscut, defects and final surface.
34. A/B polarity, miscut magnitude and azimuth are separate coordinates.
35. Substrate impurity/ingot genealogy follows epilayer/device; Cu remains a high-priority warning analyte.
36. Release substrate surface from resulting LPE interface/material quality, not roughness/vendor label alone.
37. Clean-to-LPE interval/ambient must be timestamped.
38. **LPE composition is not charge mass.** Absolute inventory requires defined well geometry/mass.
39. Do not average incompatible growth-time/source-preparation/wipe-off branches.
40. Slider clearance/speed/smoothness/contact/separation temperature are LPE variables.
41. LPE thermal history is `T(t)`, not scalar `Tgrowth`.
42. Hg-source mass/geometry/reuse and melt reuse are genealogical repeated measures.
43. **Hg anneal is trajectory-defined:** retain `T_s(t)`, `T_Hg(t)`, source geometry/pHg state and cooldown.
44. Isothermal `T_Hg≈T_s` and two-temperature `T_Hg<T_s` anneals are separate branches.
45. Hg saturation is a boundary condition, not a universal gram quantity.
46. Controller setpoint is not sample/reservoir temperature until calibrated.
47. Do not copy multi-day bulk anneals onto a ~9.5-µm epilayer.
48. High-T defect/precipitate conditioning and low-T stoichiometry control are separate objectives.
49. Final n-type Hall sign alone does not release anneal.
50. **Mask-1 and Mask-2 are different resist functions.**
51. Mask-1 thickness is not selectivity; release from surviving profile and final mesa transfer.
52. AZ4620/Br2:HBr and Hunt 180CP/Br2-methanol are transfer branches, not RP-01 resist identity.
53. Resist-product/profile changes reopen dimensional transfer/mask bias.
54. Resist stripping is part of HgCdTe surface processing; no default ultrasonics.
55. **P05 audit rule:** P05 is the canonical Hall/VdP execution SOP; do not duplicate it without materially new evidence.
56. **Die attach is a detector variable.** Mechanical compliance, CTE, bondline thermal conductance, cure and electrical/noise state are coupled.
57. Adhesive identity is not bondline specification; measure thickness/coverage/voiding/tilt.
58. Package thermal poles can occur on ms-to-hundreds-ms scales; do not call slow P13 poles intrinsic lifetime without P33 separation.
59. Thermal-cycle genealogy is not independent replication.
60. Do not transplant p-HgCdTe/FPA interconnect metallurgy into RP-01 Cr/Au without reopening P26/P24.
61. A package is not released by die shear/wire pull alone.
62. **RIE watts are not an ion-energy coordinate.** Record dc self-bias or calibrated sheath/ion-energy proxy for reactor transfer.
63. **RIE physical depth is not electrical conversion depth.** Keep `d_etch`, `d_conv`, `L_conv` separate.
64. **Separate oxide clear from semiconductor exposure:** `t_sem=t_RF-t_clear` only after actual P25 oxide clear is measured.
65. Same-era Plasma Technology RIE80 evidence does not prove RP-01 used RIE80/13.56 MHz.
66. Do not infer RP-01 electrode area from `50 W / 0.4 W cm^-2`.
67. RIE chamber clean/seasoning/loading history is a process genealogy.
68. Preserve P29 crystallography into P34 because CH4/H2 HgCdTe etch rate/morphology is orientation-dependent.
69. Matching `64 sccm / 100 mTorr / 50 W / 60 s` alone is **not reactor equivalence**.
70. **P11 audit rule:** P11 is the canonical absolute-radiometry SOP; use lineage/transfer addenda rather than duplicate top-level methods.
71. Same-UWA Optronics use establishes measurement-lineage continuity, not exact historical bench identity.
72. **A stated FOV angle is not radiometric geometry.** Record apertures, separations, offsets, window/shield geometry and view factor.
73. RP-01 `60° FOV` as a 60° full cone is a photon-flux consistency inference, not documentary proof.
74. **Blackbody controller/contact temperature is not radiance temperature.**
75. HgCdTe PC responsivity linearity is qualified versus actual irradiance/background, not total power alone.
76. P11 responsivity and P12 noise combine into `D*` only at matched/corrected T, field, package/window, FOV/background, area and frequency state.
77. Optronics `735D` remains a historical lead only; do not assign it to RP-01 without primary closure.
78. **P12 audit rule:** P12/P12B are the canonical PSD/analyzer methods; use P12C for historical state identity.
79. Figures 3/5/6/7 are the same physical RP-01 detector, but exact performance contact pair/gap is `OPEN-HISTORICAL`.
80. RP-01 Figure 5 directly states 80 K, 10 V/cm and 60° FOV; do not relabel it optically blocked.
81. **Do not substitute 24.5 nV/sqrtHz for 1-kHz noise.** The 1-kHz signal frequency is below the ~3-kHz historical 1/f knee.
82. Historical Figure-5 knee is the intersection of low-frequency 1/f trend and high-frequency g-r level; keep it distinct from -3-dB/Lorentzian corners.
83. Analyzer display output is not detector-terminal ASD until bias/load transfer, preamp gain/noise/loading, analyzer normalization and ENBW/window processing are calibrated.
84. Background-illumination fluctuations are a possible HgCdTe PC noise source; record background stability during PSD acquisition.
85. **P10 audit rule:** P10 is the canonical DC-field/self-heating SOP; Round 30 adds P10A historical/network transfer rather than another top-level method.
86. **RP-01 field is directly a contact-to-contact voltage-bias coordinate.** Use `E=V_contact/L_active`.
87. Source-supply voltage is not detector field unless all intervening drops are demonstrated negligible or corrected.
88. Same physical detector does not identify which one of the 50–400-µm contact gaps was active.
89. P10's `~1.79 mA` at 10 V/cm is `DERIVED-CONSISTENCY`, not historical current.
90. Later UWA bias-capable low-noise voltage-preamp evidence is lineage/transfer only; it does not prove the 2001 circuit.
91. Bias/load resistor noise must be propagated through the actual network before P12 subtraction.
92. AC coupling/bias-tee transfer must be measured across 1 kHz and the noise-analysis band.
93. Equal peak field under pulsed and DC bias does not imply equal thermal state.
94. P11/P12 joint `D*` requires electrical-state identity or explicit correction in addition to optical/thermal identity.
95. Do not infer historical voltage-source stiffness, series resistor, battery bias, pulse scheme or preamp input impedance from a plausible circuit.

---

# Current checkpoint — READ THIS FIRST

Latest:

`research/2026-08-16_checkpoint_after_bias_network_round30.md`

Then as needed:

- `research/2026-08-16_checkpoint_after_noise_chain_round29.md`
- `research/2026-08-16_checkpoint_after_radiometry_round28.md`
- `research/2026-08-16_checkpoint_after_rie_reactor_equivalence_round27.md`
- `research/2026-08-16_checkpoint_after_empirical_packaging_round26.md`
- older checkpoints for the detailed process genealogy.

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND30.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND30.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND29.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND29.md`
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
- **P10 DC bias/self-heating + P10A UWA bias/load-network lineage/transfer + register**
- P11 absolute radiometry/responsivity + P11A Optronics lineage/transfer + register
- P12 noise/PSD/NEP/D* + P12A preamp lineage + P12B analyzer transfer + P12C state identity + register
- P13 temporal/frequency response + P13A
- P14 lithography/CD + P14A
- P15 cryogenic package
- P16 master end-to-end traveler
- P17 statistical release/capability
- P18 failure analysis/CAPA
- P19 requirements traceability
- P20 analytical sensitivity / requirements allocation
- P21 LPE response surface / empirical Jacobian
- P22 information-optimal DOE
- P23 Hg-anneal state boundary / local Jacobian
- P24 blocking-contact empirical window + register
- P25 anodic-oxide empirical window + register
- P26 Cr/Au metallization/lift-off empirical window + register
- P27 Mask-2 empirical window + register
- P28 wet-mesa empirical window + register
- P29 CdZnTe/final-surface empirical window + register
- P30 Te-rich LPE apparatus/charge/contact/wipe-off empirical window + register
- P31 Hg-overpressure anneal apparatus/reservoir/trajectory empirical window + register
- P32 Mask-1/wet-mesa lithography empirical window + register
- P33 cryogenic die-attach/interconnect/package empirical window + register
- P34 CH4/H2 RIE reactor-equivalence empirical window + register

No new top-level module was created in Rounds 28–30 because P11, P12 and P10 were already method-complete; lineage/state-transfer addenda were the correct missing layer.

---

# Canonical RP-01 direct anchors — do not drift

## Material / fabrication

- LPE n-HgCdTe on electrically insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `mu=4.0×10^4 cm²/V·s`
- active thickness `9.5 µm`
- supplier n/µ measurement temperature undisclosed
- native anodic oxide `~800 Å = 80 nm`
- RIE: Plasma Technology parallel-plate; printed `CH4/5H2`; total 64 sccm; 100 mTorr; 50 W; 60 s
- converted average n `~2.0×10^15 cm^-3`; mobility `~3.3×10^4 cm²/V·s`
- Cr 30 nm / Au 270 nm
- nine 300×300-µm contacts; gaps 50–400 µm in 50-µm increments
- `rho_c≈9×10^-4 Ω cm²` at 80 K

Do not combine the reported average converted n with the separate ~8-µm conversion-depth lineage into one direct sheet density.

## Detector / radiometry / noise

- Optronics Laboratories Spectral Response Measurement System
- ~80 K
- stated 60° FOV
- responsivity/spectral response chopped at 1 kHz
- Figure-3 applied field explicitly means voltage bias between contacts
- Figure-3 field sweep roughly 0–50 V/cm
- Figures 5–7 performance state at 10 V/cm
- Figures 3/5/6/7 same physical detector
- exact contact pair/gap remains open
- cutoff ~4.4 µm
- BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm
- quoted 300-K/60° photon flux ~`1×10^15 cm^-2 s^-1`
- quoted QE ~70%
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz by trend intersection
- high-frequency g-r level ~24.5 nV/sqrtHz
- exact 1-kHz noise/bandwidth convention used for published D* remains open

---

# P10A — current bias/load-network state

## Direct closure

RP-01 defines the applied field through **voltage bias between the detector contacts**:

`E = V_contact-contact / L_active`.

The supply/load topology remains unknown.

## Same-UWA transfer lineage

Hatch et al. 2011, DOI `10.1063/1.3540655`, directly describes a low-noise **voltage** preamplifier specifically designed so bias voltage could be applied to the photoconductor. It cites J. F. Siliquini's 1995 UWA PhD thesis for the preamplifier.

Direct transfer details include just-below-1-kHz chopping, fields 5–80 V/cm, and a 250-mV bias mapped to 9.2 or 8.6 V/cm for two different device geometries.

This is UWA lineage evidence, not proof of the 2001 circuit.

## Power/duty transfer lineage

Siliquini/Faraone 1996–1997 UWA photoconductor-array work treats power dissipation as a device constraint; the vertical-PC analysis uses pulsed bias in a different architecture. Therefore local thermal qualification records duty/pulse width/repetition/settling, but RP-01 is **not** assumed pulse biased.

## Controlled local transfer

Record and calibrate:

`Y_bias={contact_pair,L,W,V_source,V_contact,I,E,P_det,R_static,R_diff,H_sig(f),H_noise(f),Z_pre(f),source_noise,T_proxy,H_pkg,thermal,duty,polarity,sweepout_metric}`.

At 1 kHz, explicitly measure small-signal transfer. Propagate load/source resistor and preamp noise through the actual circuit.

## P11/P12 electrical-state identity

Allowed joint-D* dispositions:

- `STATE-ELECTRICALLY-IDENTICAL`
- `CORRECTED-TO-COMMON-ELECTRICAL-STATE`
- `INCOMPATIBLE — DO NOT CALCULATE JOINT D*`

## Remaining OPEN

- exact Figure-3/5/6/7 contact pair/gap
- 2001 bias-source model/topology
- series/load resistor and temperature
- detector current/R at 10 V/cm
- detector-voltage sense method
- preamp input impedance/gain/coupling
- exact P11/P12 topology identity
- Siliquini 1995 thesis full schematic.

---

# P12C / P11A / P34 / P33 concise state

## P12C noise

Same device for Figs 3/5/6/7; Figure 5 is 80 K / 10 V/cm / 60° FOV. Do not use 24.5 nV/sqrtHz automatically at 1 kHz. HP35665A exact span/lines/window/averaging remain open. Background fluctuations are a possible low-frequency source.

## P11A radiometry

Same-UWA Optronics lineage is real but exact bench identity remains open. 60° full-cone interpretation is a Planck-flux consistency check only. Absolute blackbody work uses radiance temperature, actual aperture/view factor and transmission.

## P34 RIE

Direct controller center remains 64 sccm / 100 mTorr / 50 W / 60 s / CH4/5H2; transfer requires self-bias/sheath proxy, sample T(t), oxide-clear time, physical etch, electrical conversion and downstream contact/blocking/noise closure.

## P33 package

Compliant attachment can reduce cryogenic cracking; package bond layers can create ms-to-hundreds-ms thermal response. Measure `H_pkg,thermal` before assigning slow temporal poles to carrier lifetime.

---

# Persistent fabrication/process OPEN items

- exact RP-01 Mask-1/Mask-2 commercial lithography details
- exact UWA wet-mesa formulation basis/HBr assay
- exact RP-01 CdZnTe composition/face/polarity/miscut/final surface
- exact Honeywell/Fermionics LPE boat/charge/gas/contact trajectory
- exact supplier/UWA anneal history
- exact Cr/Au deposition hardware/rates/vacuum
- exact RP-01 package construction
- exact Plasma Technology RIE hardware/self-bias/sample temperature
- exact RP-01 Optronics optical bench/calibration chain
- exact RP-01 bias/load/preamp circuit

---

# Active source-recovery record

Identified but not fully recovered:

- Vanya Srivastav IISc thesis `G25544.pdf`
- John Kenion White 2005 UWA thesis full experimental text
- Ryan Westerhout 2013 UWA thesis full experimental text
- **J. F. Siliquini 1995 UWA PhD thesis — highest-value P10/P12 electronics target**
- Smith et al. 2000 in-situ vacuum processing full text
- exact Honeywell/Fermionics LPE travelers
- exact UWA Mask-1 traveler
- exact RP-01 package traveler
- 1989 SPIE Optronics/low-background-radiometry full text
- exact RP-01 Optronics calibration records
- exact Figure-5 HP35665A acquisition record/raw data
- original Figure-3/5/6/7 device notebook identifying contact pair/current/resistance.

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 31: P13 temporal-response apparatus / source / package de-embedding audit**.

1. Audit `procedures/P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md` and `procedures/P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md` first.
2. Re-read P33 package thermal evidence because package poles can masquerade as detector lifetime.
3. Search primary same-UWA HgCdTe papers/theses/proceedings for transient source wavelength/type, optical pulse/chopper waveform, rise/fall time, field/bias topology, preamp bandwidth/coupling, oscilloscope/analyzer and data-reduction method.
4. Determine whether any historical “lifetime” quantity was inferred from optical transient, frequency response, noise or another method.
5. Separate `H_source`, `H_optics`, `H_detector`, `H_bias`, `H_preamp`, `H_cable`, `H_instrument` and `H_pkg,thermal`.
6. Never call a slow pole intrinsic carrier lifetime until package/readout/source contributions are experimentally excluded or de-embedded.
7. Create a new top-level module only if P13 is genuinely method-incomplete; otherwise create a lineage/de-embedding addendum + traveler.
8. Continue source-recovery for Siliquini 1995 in parallel only when a concrete archival route appears.

Do not populate production tolerances without repeated local fabrication data.
