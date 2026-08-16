# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** executable by a competent researcher without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains direct historical anchors, empirical transfer procedures, metrology SOPs, qualification travelers, failure/release architecture, negative-search records and explicit unresolved gaps.

---

# Non-negotiable scientific/provenance rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, explicit derivation, or a named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01, same-lineage, transfer-family, model, derived, apparatus-calibration and local-qualification evidence.
4. Every critical process step needs output metrology and a pass/fail/qualification gate.
5. Preserve negative searches, failed branches, rejected inferences, corrections and source conflicts.
6. Use measured fabricated geometry for field, active area and `D*` normalization.
7. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density, `rho_c` and minority-carrier blocking metrics distinct.
8. Treat passivation, post-RIE exposure, wet-etch surface exposure, metal-interface exposure, anneal cooldown, substrate clean-to-load, LPE source genealogy, RIE chamber state and packaging as process variables.
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
61. **P05 audit rule:** P05 is the canonical Hall/VdP execution SOP; do not duplicate it without materially new method evidence.
62. **Die attach is a detector variable.** Mechanical compliance, CTE, bondline thermal conductance, cure and noise/electrical state are coupled.
63. Adhesive product identity is not a bondline specification; measure thickness/coverage/voiding/tilt.
64. Honeywell 5-g/40-g thermocompression values are transfer experiment values, not RP-01 setpoints.
65. Package-generated thermal poles can occur on ms-to-hundreds-ms scales; do not assign them to intrinsic lifetime without P33/P13 separation.
66. Thermal-cycle genealogy is not independent replication.
67. Do not transplant p-HgCdTe/FPA interconnect metallurgies into the RP-01 Cr/Au chain without reopening P26/P24.
68. A package is not released by die shear/wire pull alone.
69. **RIE watts are not an ion-energy coordinate.** Record dc self-bias or another calibrated sheath/ion-energy proxy for reactor transfer.
70. **RIE physical depth is not electrical conversion depth.** Keep `d_etch`, `d_conv` and `L_conv` separate.
71. **Separate oxide clear from semiconductor exposure:** `t_sem=t_RF-t_clear` only after local `t_clear` is measured.
72. Same-era Plasma Technology RIE80 evidence does not prove RP-01 used RIE80 or 13.56 MHz.
73. Do not infer RP-01 electrode area from `50 W / 0.4 W cm^-2`.
74. RIE chamber clean/seasoning/loading history is a genealogy variable.
75. Preserve P29 plane/polarity into P34 because CH4/H2 HgCdTe etch rate/morphology is orientation-dependent.
76. Matching `64 sccm / 100 mTorr / 50 W / 60 s` alone is **not reactor equivalence**.
77. **P11 audit rule:** P11 is the canonical absolute-radiometry SOP; do not create a duplicate top-level module without materially new method evidence.
78. Same-UWA Optronics use establishes measurement-lineage continuity, not exact historical bench identity/configuration.
79. **A stated FOV angle is not a radiometric geometry.** Record physical apertures, separations, offsets, window/shield geometry and view factor.
80. RP-01 `60° FOV` as a 60° full cone is a photon-flux consistency inference, not documentary proof.
81. **Blackbody controller/contact temperature is not radiance temperature.**
82. HgCdTe photoconductor responsivity linearity is qualified versus actual irradiance/background, not total power alone.
83. P11 responsivity and P12 noise may be combined into `D*` only when temperature, field, package/window, FOV/background, active area and frequency conventions match or are explicitly corrected.
84. Optronics `735D` remains a historical lead only; do not assign it to RP-01 without primary documentary closure.
85. **P12 audit rule:** P12/P12B are already the canonical noise/PSD/analyzer metrology methods; Round 29 adds P12C historical-state closure rather than a duplicate top-level noise module.
86. **Same-device identity does not close active geometry.** RP-01 Figures 3/5/6/7 are the same physical detector, but the exact contact pair/gap remains `OPEN-HISTORICAL`.
87. RP-01 Figure 5 directly states `80 K`, `10 V/cm`, and `60° FOV`; do not relabel the published noise spectrum as optically blocked. The exact radiance/aperture behind that FOV remains open.
88. **Do not substitute the 24.5-nV/sqrtHz high-frequency g-r plateau for 1-kHz noise.** RP-01's `1 kHz` signal frequency lies below the reported `~3 kHz` 1/f knee; historical Figure-7 noise convention remains open.
89. For historical Figure-5 comparison, the knee is the intersection of the low-frequency 1/f trend and high-frequency g-r level. Keep it distinct from a -3-dB or Lorentzian corner.
90. Analyzer display output is not detector-terminal ASD until bias/load transfer, preamplifier gain/noise/loading, analyzer normalization and ENBW/window processing are calibrated.
91. Same-UWA HgCdTe noise work explicitly includes background-illumination fluctuations; record background stability during noise spectra and do not automatically label background-driven low-frequency noise as intrinsic detector 1/f.

---

# Current checkpoint — READ THIS FIRST

Latest:

`research/2026-08-16_checkpoint_after_noise_chain_round29.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_radiometry_round28.md`
- `research/2026-08-16_checkpoint_after_rie_reactor_equivalence_round27.md`
- `research/2026-08-16_checkpoint_after_empirical_packaging_round26.md`
- `research/2026-08-16_checkpoint_after_empirical_mask1_round25.md`
- `research/2026-08-16_checkpoint_after_empirical_hg_anneal_round24.md`
- `research/2026-08-16_checkpoint_after_empirical_lpe_execution_round23.md`
- older checkpoints as needed.

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND29.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND29.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND28.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND28.md`
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
- P11 absolute radiometry/responsivity + P11A Optronics lineage/transfer + register
- **P12 noise/PSD/NEP/D* + P12A preamplifier lineage + P12B analyzer transfer + P12C RP-01 state identity + register**
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
- P34 CH4/H2 RIE reactor-equivalence empirical process window + register

P24–P34 are empirical execution layers. P11A and P12C are lineage/state-transfer addenda because the underlying P11/P12 metrology SOPs were already operationally complete. No P35/P36 was created in Rounds 28–29.

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

## Mask-2 / metal / contact geometry
- resist ~4–5 µm
- prebake 80 °C / 30 min
- chlorobenzene 30 min
- pattern/develop/water rinse
- Cr 30 nm / Au 270 nm
- nine 300×300-µm contacts
- gaps 50–400 µm in 50-µm increments
- `rho_c≈9×10^-4 Ω·cm²` at 80 K

## Detector / radiometry / noise benchmark
- ~80 K
- Optronics Laboratories Spectral Response Measurement System
- stated `60° FOV`
- responsivity/spectral response chopped at `1 kHz`
- spectral responsivity / `D*` state at `10 V/cm`
- cutoff ~4.4 µm
- BLIP `D* ~2×10^11 cm Hz^1/2/W` at 4 µm
- quoted 300-K/60° background flux ~`1×10^15 photons cm^-2 s^-1`
- quoted QE ~70%
- noise chain: low-noise preamp + HP35665A
- Figure-5 noise state: **same performance device, 80 K, 10 V/cm, stated 60° FOV**
- `1/f` knee ~3 kHz by trend intersection
- high-frequency g-r level ~24.5 nV/sqrtHz
- Figures 3/5/6/7 are the **same physical detector**
- exact performance contact pair/gap remains open
- exact noise value used for Figure-7 `D*` remains open

---

# P12C — current noise-chain state

## Direct state closure

Historical performance coupling:

`Fig3 field response -> Fig5 noise -> Fig6 spectral response -> Fig7 D* = same detector`.

Figure 5 directly closes `80 K / 10 V/cm / stated 60° FOV / low-noise preamp / HP35665A`.

Do not infer the active gap from the nine-contact spacing list.

## 1-kHz ambiguity

`f_sig=1 kHz` and `f_k≈3 kHz`, so the high-frequency `24.5 nV/sqrtHz` plateau cannot automatically be inserted into the 1-kHz `D*` calculation.

Local default:

`D*(lambda,1kHz)=R_v(lambda,1kHz)*sqrt(A)/e_det(1kHz)`

under matched detector/background/loading state.

## Historical knee

For RP-01 comparison use the intersection of the fitted/drawn 1/f trend and high-frequency g-r level. Report any modern breakpoint or Lorentzian corner separately.

## UWA preamp lineage

Hatch et al. 2011 directly describes a bias-capable low-noise voltage preamplifier and cites J. F. Siliquini's 1995 UWA PhD thesis for it. This is the highest-value archival electronics target. Exact identity with the 2001 preamp remains unproven.

## HP35665A

Official manuals:

- Operators Guide `35665-90026` (Sep. 1991)
- Concepts Guide `35665-90028` (Sep. 1991)

Official capability includes linear spectrum, PSD, cross spectrum, frequency response, time waveform/correlation, 102.4-kHz single-channel bandwidth, 51.2-kHz dual-channel bandwidth and 100/200/400/800 resolution lines.

These are capability facts, **not Figure-5 settings**.

## Background-noise coordinate

Jozwikowski et al. 2003 same-UWA HgCdTe work includes fluctuations of background illumination as a modeled/measured noise source. Record background/source stability during P12 runs.

## Controlled output

`Y_NOISE={device_ID,contact_pair,T,E,I,P,FOV/background,Z_d(f),G(f),analyzer_state,e_det(f),alpha,f_k,hist,e_GR,e_n(1kHz),A,D*_closure}`.

Before `D*`, complete the P12C P11/P12 state-identity matrix.

## Remaining OPEN

- exact contact pair/gap for the same Figure-3/5/6/7 detector;
- exact 2001 preamp circuit/gain/noise;
- bias/load/coupling network;
- exact HP35665A span/lines/window/averaging/scaling;
- exact Figure-5 background radiance beyond `60° FOV`;
- exact noise frequency/value/bandwidth used for Figure-7 `D*`;
- Siliquini 1995 thesis full text/schematic.

---

# Other current empirical states — concise recovery map

## P11A radiometry

Same-UWA Optronics lineage is real but exact RP-01 bench identity remains open. 60° full-cone interpretation is a Planck-flux consistency inference only. Absolute blackbody work uses calibrated radiance temperature, aperture/view factor and package transmission. P11/P12 states must match for `D*`.

## P34 RIE reactor equivalence

Direct controller center remains `64 sccm / 100 mTorr / 50 W / 60 s / CH4/5H2`; transfer release requires measured self-bias/sheath proxy, sample `T(t)`, oxide-clear time, physical etch, sheet state, electrical conversion depth/lateral spread, TLM and blocking/noise closure.

## P33 cryogenic package

Compliant attachment can prevent cryogenic cracking; bonding layers can introduce ms-to-hundreds-ms thermal poles. Measure package thermal kernel before assigning slow P13 poles to intrinsic lifetime.

## P32 Mask-1

Historical identity open. AZ4620/Br2:HBr and Hunt 180CP/Br2-methanol are transfer branches. Release from actual mask survival and `CD_mask -> CD_PR -> CD_mesa`.

## P31 Hg anneal

Low-T screening anchor ~250 °C/1 h under Hg-rich/pseudo-isothermal transfer branch; isothermal and two-temperature routes distinct. No universal Hg reservoir mass.

## P30 LPE

Honeywell tie line `xL=.082,yL=.810,TL=507 °C -> xS≈.29`; composition does not determine total charge. Wipe-off generations remain distinct.

## P29–P24

- P29 CdZnTe: exact RP-01 y/polarity/miscut/final surface open.
- P28 wet mesa: nominal `2% Br2 in 3:1 EG:HBr`, 21 °C, `R_V≈2.78 µm/min`, ±26%, `A≈0.63`; formulation basis/HBr assay/rinse open.
- P27 Mask-2: 4–5 µm / 80 °C 30 min / chlorobenzene 30 min anchors; exact commercial resist/exposure/developer/strip open.
- P26 Cr/Au: 30 nm / 270 nm, `rho_c≈9e-4 Ω cm²` at 80 K; exact deposition details partly open.
- P25 anodic oxide: strongest transfer center 0.1 M KOH, 90% EG/10% DI, ~0.30 mA/cm², ~15 V, ~2 min, ~80 nm; transfer only.
- P24 blocking: direct controller center preserved; P34 controls reactor equivalence.

---

# Measurement / release essentials

- P05 Hall: canonical execution SOP; VdP redundancy, current/field reversal, variable field, self-heating, multicarrier escalation.
- P06 FTIR: composition/bandgap model is not detector cutoff.
- P10: `E=V_active/L_measured`; electrical loading and package thermal resistance matter.
- P11/P11A: calibrated radiometry, measured FOV/reference-plane geometry, irradiance/background linearity.
- P12/P12C: `NEP=e_n/R_v`; `D*=R_v sqrt(A)/e_n`; independent noises combine/subtract at PSD level; matched state required.
- P13: de-embed source/optics/bias/preamp/cable/instrument and P33 package thermal response.
- P17: separate measurement/spatial/run/lot/long-term variation; no generic Cpk threshold.
- P18: preserve negative/failed runs and competing mechanisms.
- P19/P20: trace final requirements/sensitivities without replacing empirical process data.

---

# Highest-priority OPEN practical details after Round 29

## Bias/load/self-heating historical execution — strongest next target

Audit P10 first. The remaining noise uncertainty now lies heavily in the electrical network between detector and preamplifier.

Priority recovery:

- exact UWA/RP-01 detector bias-source topology;
- load/series resistor values and temperature;
- where detector voltage was sensed;
- AC-coupling/bias-tee topology;
- preamplifier input impedance/loading;
- detector differential resistance/current at 10 V/cm;
- same Figure-3/5/6/7 contact pair/gap;
- actual active-region voltage versus source voltage;
- how the responsivity and noise readout shared or differed in bias electronics;
- Siliquini thesis schematic/electronics details.

If P10 is already operator-complete, create only a lineage/bias-network transfer addendum + register rather than a duplicate top-level procedure.

Alternative if no new bias evidence is recoverable: audit P13/P13A and close historical transient/source/readout apparatus while explicitly separating intrinsic detector response from P33 package thermal poles.

## Persistent historical fabrication gaps

- exact RP-01 Mask-1/Mask-2 commercial lithography details;
- exact UWA wet-mesa formulation basis;
- exact RP-01 CdZnTe y/face/miscut/final surface;
- exact Honeywell/Fermionics LPE boat/charge/gas/contact trajectory;
- exact supplier/UWA anneal history;
- exact Cr/Au deposition method/rates/vacuum;
- exact RP-01 package construction;
- exact Plasma Technology RIE hardware/self-bias/sample temperature;
- exact RP-01 Optronics optical bench/calibration chain.

---

# Active source-recovery record

Identified but not fully recovered:

- Vanya Srivastav IISc thesis `G25544.pdf` full process text;
- John Kenion White 2005 UWA thesis full experimental text — current repository PDF route returned 403;
- Ryan Westerhout 2013 UWA thesis experimental text;
- **J. F. Siliquini 1995 UWA PhD thesis — highest-value P10/P12 electronics target**;
- Smith et al. 2000 in-situ vacuum processing full experimental text;
- Musca/Smith/Dell/Faraone photoconductor contact/passivation traveler;
- exact Honeywell/Fermionics LPE travelers;
- exact UWA Mask-1 traveler;
- exact RP-01 die attach/interconnect/Dewar traveler;
- 1989 SPIE Optronics/low-background-radiometry full primary text;
- exact RP-01 Optronics calibration records;
- exact RP-01 Figure-5 analyzer state/raw data.

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 30: audit/reconstruct P10 bias-source / load-network / active-field execution**.

1. Audit `procedures/P10_DEVICE_DC_BIAS_SELF_HEATING.md` before creating anything new.
2. Search RP-01, same-UWA photoconductor papers, theses and proceedings for the bias circuit, load resistor, preamp input, coupling and detector resistance/current.
3. Prioritize Siliquini 1995 thesis acquisition/references because P12A directly ties it to the bias-capable low-noise preamp.
4. Preserve `E=V_active/L_measured`; never infer active field from supply voltage alone.
5. Tie any recovered circuit to the same Figure-3/5/6/7 detector state without guessing the contact gap.
6. Determine detector-terminal noise/signal transfer through the bias network and how it interacts with P12B.
7. If P10 is already operator-complete, create a P10 lineage/transfer addendum + traveler rather than a duplicate top-level module.
8. If evidence cannot advance P10 materially, pivot in the same round to P13 temporal-response apparatus recovery.

Do not populate production tolerances without repeated local fabrication data.
