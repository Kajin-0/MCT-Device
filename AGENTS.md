# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** executable by a competent researcher without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains direct historical anchors, empirical transfer procedures, controlled metrology, qualification registers, source/gap ledgers, negative-search records and explicit unresolved history.

---

# Non-negotiable scientific/provenance rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, explicit derivation, or a named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01, same-lineage, transfer-family, model, derived, apparatus-calibration and local-qualification evidence.
4. Every critical process step requires outcome metrology and a pass/fail/qualification gate.
5. Preserve negative searches, failed branches, rejected inferences, corrections and source conflicts.
6. Use measured fabricated geometry for field, active area and `D*` normalization.
7. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density, `rho_c` and minority-carrier blocking metrics distinct.
8. Treat passivation, post-RIE exposure, wet-etch surface exposure, metal-interface exposure, LPE source genealogy, anneal cooldown, substrate clean-to-load, RIE chamber state, packaging, singulation and thermal-cycle history as process variables.
9. Measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Specifications derive from downstream material/device performance, not observed process spread.
11. Failure diagnosis: signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification.
12. Repository procedures do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S.
13. Numerical sensitivities/tolerances state protected output, input, operating point and evidence class. Proxies may size experiments but cannot release production specifications.
14. `xS/xL` is not `dxS/dxL` when other equilibrium coordinates vary.
15. Coded DOE coordinates do not create physical process tolerances.
16. Repeated observations from one melt/source/bath/substrate/anneal-source/chamber/package/tool genealogy are not iid replicates.
17. Never regress reciprocal Hall density through a p/n Hall-sign transition; use signed Hall/tensor information near transition.
18. **Empirical/practical literature first.** Before theoretical placeholders, search primary papers, theses, patents, proceedings and institutional archives for actual process/apparatus values and outcomes.
19. Theory checks consistency and bridges genuine gaps; it does not displace empirical process data.
20. A successful historical process center is not automatically an optimum.
21. Equal anodic-oxide thickness does not imply equal interface state.
22. No undocumented ion mill, wet etch or plasma clean may be inserted between qualified P08 RIE and Cr deposition.
23. Baseline P26 is as-deposited; post-metal anneals from other contact architectures are transfer evidence only.
24. Cryogenic TLM records optical-background/shield state as well as temperature/current.
25. Chlorobenzene constrains Mask-2 to a positive diazo/DNQ-novolak lift-off family but does not identify a resist product.
26. Preserve RP-01 Mask-2 order `prebake -> chlorobenzene -> patterned/developed/water rinse`; do not silently reorder it.
27. Generic developer or lift-off solvent is not historical proof.
28. **Wet-etch percentage without basis is not executable.** Never guess Srivastav `2% Br2` basis.
29. Preserve `3:1 EG:HBr` symbolically until preparation basis is recovered or locally defined; HBr assay and bath genealogy are separate controls.
30. **Wet-mesa endpoint:** time is input; measured through-layer isolation is output.
31. Post-wet-etch air time/surface state belongs to the P28->P25 handoff.
32. **CdZnTe vendor label is not interface specification.** Record composition/lattice state, plane, polarity, miscut, defects and final surface.
33. A/B polarity, miscut magnitude and azimuth are separate coordinates.
34. Substrate impurity/ingot genealogy follows epilayer/device; Cu remains a high-priority warning analyte.
35. Release substrate surface from resulting LPE interface/material quality, not vendor label/roughness alone.
36. Clean-to-LPE interval/ambient must be timestamped.
37. **LPE composition is not charge mass.** Absolute inventory requires defined well geometry/mass.
38. Do not average incompatible growth-time, source-preparation or wipe-off branches.
39. Slider clearance/speed/smoothness/contact/separation temperature are LPE variables.
40. LPE thermal history is `T(t)`, not scalar `Tgrowth`; source/reuse is genealogy.
41. **Hg anneal is trajectory-defined:** retain `T_s(t)`, `T_Hg(t)`, source geometry/pHg state and cooldown.
42. Isothermal `T_Hg≈T_s` and two-temperature `T_Hg<T_s` anneals are separate branches.
43. Hg saturation is a boundary condition, not a universal gram quantity.
44. Controller setpoint is not sample/reservoir temperature until calibrated.
45. Do not copy multi-day bulk anneals onto a ~9.5-µm epilayer.
46. High-T defect/precipitate conditioning and low-T stoichiometry control are separate objectives.
47. Final n-type Hall sign alone does not release anneal.
48. **Mask-1 and Mask-2 are different resist functions.** Mask-1 releases from surviving profile/final mesa transfer, not thickness alone.
49. AZ4620/Br2:HBr and Hunt 180CP/Br2-methanol are transfer branches, not RP-01 resist identity.
50. Resist-product/profile changes reopen dimensional transfer/mask bias; resist stripping is part of HgCdTe surface processing; no default ultrasonics.
51. **P05 audit rule:** P05 is the canonical Hall/VdP SOP; do not duplicate it without materially new evidence.
52. **Die attach is a detector variable.** Compliance, CTE, bondline thermal conductance, cure and electrical/noise state are coupled.
53. Adhesive identity is not bondline specification; measure thickness/coverage/voiding/tilt.
54. Package thermal poles can occur on ms-to-hundreds-ms scales; do not call slow P13 poles intrinsic lifetime without P33 separation.
55. Thermal-cycle genealogy is not independent replication; package release is mechanical + electrical/noise + thermal + optical.
56. **RIE watts are not ion energy.** Record dc self-bias or calibrated sheath/ion-energy proxy for transfer.
57. **RIE physical depth is not electrical conversion depth.** Keep `d_etch`, `d_conv`, `L_conv` separate.
58. Separate oxide clear from semiconductor exposure: `t_sem=t_RF-t_clear` only after local clear is measured.
59. Same-era Plasma Technology RIE80 evidence does not prove RP-01 used RIE80/13.56 MHz; do not infer electrode area from `50 W/0.4 W cm^-2`.
60. RIE chamber clean/season/loading history is genealogy; preserve P29 crystallography into P34.
61. Matching `64 sccm / 100 mTorr / 50 W / 60 s` alone is **not reactor equivalence**.
62. **P11 audit rule:** P11 is the canonical absolute-radiometry SOP; use lineage/transfer addenda rather than duplicate methods.
63. Same-UWA Optronics use establishes measurement-lineage continuity, not exact bench identity.
64. **FOV angle is not radiometric geometry.** Record apertures, separations, offsets, window/shield and view factor.
65. RP-01 `60° FOV` as a 60° full cone is a photon-flux consistency inference, not documentary proof.
66. **Blackbody contact/controller temperature is not radiance temperature.**
67. HgCdTe PC responsivity linearity is qualified versus actual irradiance/background, not total power alone.
68. P11/P12 combine into `D*` only at matched/corrected T, field, package/window, FOV/background, area and frequency state.
69. Optronics `735D` remains a lead only; do not assign it to RP-01 without primary closure.
70. **P12 audit rule:** P12/P12B are canonical PSD/analyzer methods; P12C controls historical state identity.
71. Figures 3/5/6/7 are the same physical RP-01 detector, but exact performance contact pair/gap is `OPEN-HISTORICAL`.
72. Figure 5 directly states 80 K, 10 V/cm and 60° FOV; do not relabel it optically blocked.
73. **Do not substitute 24.5 nV/sqrtHz for 1-kHz noise.** 1 kHz is below the historical ~3-kHz 1/f knee.
74. Historical Figure-5 knee is the intersection of low-frequency 1/f trend and high-frequency g-r level; keep it distinct from -3-dB/Lorentzian corners.
75. Analyzer display output is not detector-terminal ASD until bias/load transfer, preamp gain/noise/loading, normalization and ENBW/window processing are calibrated.
76. Background-illumination fluctuations can be HgCdTe-PC noise sources; record background stability during PSD acquisition.
77. **P10 audit rule:** P10 is canonical DC-field/self-heating; P10A supplies historical/network transfer.
78. **RP-01 field is a contact-to-contact voltage-bias coordinate:** `E=V_contact/L_active`.
79. Supply voltage is not detector field unless intervening drops are negligible/corrected.
80. Same physical detector does not identify which 50–400-µm gap was active; P10's ~1.79 mA is derived consistency only.
81. Later UWA bias-capable low-noise voltage-preamp evidence is transfer lineage, not proof of the 2001 circuit.
82. Bias/load resistor noise must be propagated through the actual network; AC coupling/bias-tee transfer must be measured.
83. Equal peak field under pulsed/DC bias does not imply equal thermal state.
84. Joint `D*` requires electrical-state identity/correction as well as optical/thermal identity.
85. Do not infer historical source stiffness, series resistor, battery bias, pulse scheme or preamp input impedance from a plausible circuit.
86. **P13 audit rule:** P13 is the canonical temporal/frequency-response SOP; Round 31 corrects/extends P13 and P13A rather than creating a duplicate top-level method.
87. **Historical RP-01 `tau` and `f_3dB` are currently OPEN.** A 1-kHz chopped measurement is not a lifetime or bandwidth measurement.
88. Temporal interpretation must include source, optics, bias, preamp, cable, instrument and **P33 package thermal response**; a slow pole is not intrinsic carrier lifetime until these are excluded/de-embedded.
89. **Low average optical power does not prove low injection.** The 1998 UWA TPCD branch itself estimates localized initial excitation can approach high-level injection.
90. A `25 ns` pulse is a source condition, not proof of a 25-ns detector response or small-signal lifetime.
91. The direct 1998 UWA same-lab TPCD branch is `1.047 µm / 25 ns / 1 kHz / ~77 K vacuum / Keithley variable-current source / low bias / AC-coupled amplifier / HP54522A / 500 points at 20 ns / 128 averages typical`.
92. Those 1998 values are **same-UWA method evidence, not RP-01 detector setpoints**. In particular `-1.05 V` is not an RP-01 field.
93. `1.047 µm` near-surface TPCD and ~4-µm RP-01 detector response are not automatically the same temporal observable.
94. AC-coupled transient readout requires measured high-pass transfer with detector-equivalent impedance.
95. HP54522A datasheet capability is not historical acquisition configuration beyond values directly stated in the thesis.
96. A one-exponential fit is not a bulk-lifetime proof; require residual/model/fit-window/injection/field/package checks and time-frequency consistency.
97. Pal 2001 and Gopal 2004 interface-trap papers are **non-UWA transfer evidence**; preserve correct attribution.
98. HgCdTe-PC package recovery of several ms and hundreds ms from Bartoli 1975 cannot be labeled carrier lifetime without package discrimination.
99. Redfern/Musca/Smith/Dell/Faraone 1999 TPCD conference paper is identified but full experimental text remains unrecovered.
100. `BULK-LIFETIME-JUSTIFIED` is a terminal evidence classification in P13A, not the default name for a fitted decay.
101. **P06 audit rule:** P06 is the canonical FTIR/transmission SOP; Round 32 adds P06A apparatus/model/cutoff transfer rather than a duplicate top-level method.
102. **Keep physical thickness, FTIR optical thickness, optical edge, optical bandgap/composition and detector cutoff distinct:** `d_physical != d_FTIR`, and neither `lambda_edge` nor `hc/Eg` is automatically `lambda_det,c`.
103. RP-01's `x≈0.30` and `9.5 µm` are direct reported material descriptors, but the measurement methods are `OPEN-HISTORICAL`; do not claim they were obtained by FTIR without documentary evidence.
104. Hansen's ~`0.013 eV` is the standard error of the global empirical `Eg(x,T)` fit, not local FTIR repeatability, spatial-map precision or detector-cutoff uncertainty.
105. **The Round-32 Hansen comparison is `DERIVED-CONSISTENCY` only:** at 80 K `x=.300 -> Eg=.243684 eV -> lambda_g,eq=5.0879 µm`; `4.4 µm -> 0.281782 eV -> x_Hansen,eq≈.3241`. Never back-fill `x=.3241` as the measured RP-01 composition.
106. **FTIR aperture setting is not sample spatial resolution.** Measure/bound projected footprint, wavelength-dependent diffraction/blur, stage repeatability/backlash and physical coordinate registration.
107. Preserve the Gopal 1992 thickness-range unit conflict until the primary paper line is checked; do not silently repair indexed `mm` text into `µm` in a controlled source record.
108. Weak/absent HgCdTe/CdZnTe interference fringes can reflect interface degradation, Hg in-diffusion, scattering, free-carrier absorption or stack complexity; do not automatically classify them as instrument failure.
109. A pre/post-anneal optical-edge shift is not automatically a composition shift. Check P05 Hall state, defects/free carriers, surface/interface state, map registration and P31 trajectory before changing x.
110. Surface preparation from an optical transfer paper, including a Br2/methanol premeasurement treatment, is part of that experiment's sample state and is not automatically an RP-01 P06 preparation step.
111. Full-spectrum composition/thickness fitting must freeze optical constants, absorption model, substrate model and software/version; do not allow hidden coefficient/model drift between wafers.
112. `DEVICE-CORRELATED` optical metrology requires a traceable material-coordinate/genealogy link from P06/P06A to P11 detector spectral response; adjacent or nominally similar material is not the same physical state.
113. **P35 is the controlled empirical singulation layer.** P15 remains the package framework; P35 owns finished-device separation/tool/protection/clean/edge-damage qualification.
114. Historical RP-01 singulation method, die outline, tool and edge exclusion remain `OPEN-HISTORICAL`; conventional HgCdTe diamond-saw use in another source does not prove UWA used it.
115. **Visible dicing damage is not the same as functional or subsurface damage.** Preserve `d_visible`, `d_functional`, and locally released `d_release` separately.
116. HgCdTe array transfer data showing roughly `9–19 µm` mechanical-saw and `0–6 µm` excimer no-measured-degradation clearances are architecture-specific transfer evidence, not RP-01 edge rules.
117. **No visible chip does not prove no subsurface damage.** Bulk-CdZnTe manufacturing evidence shows saw-damage depths can greatly exceed visible edge defects.
118. Deep bromine saw-damage-removal etches from bulk CdZnTe are **not** a completed-RP-01 post-dice clean. A ~9.5-µm HgCdTe active layer plus oxide/RIE/Cr-Au cannot inherit `5% Br/methanol / 5 min` or ~100-µm removal logic without a separate material-removal qualification.
119. The Yoo 1998 `125-mm stainless wire / 16-µm BN slurry / ~1-h cut / wax + photoresist protection` branch is direct finished-CdZnTe transfer evidence, not an RP-01 recipe.
120. **Laser/non-contact does not mean chemically inert.** Excimer ablation can change II–VI stoichiometry; a laser P35 branch must qualify near-edge chemistry/redeposition as well as chipping and detector function.
121. Protection polymers, temporary wax/tape, slurry/coolant and release solvents are detector-process variables after final metal/passivation; no generic semiconductor clean is inserted by default.
122. Scribe/cleave inherits P29 crystallographic plane/polarity/miscut and defect genealogy; rectangular die cannot be assumed to cleave equivalently in two orthogonal directions.
123. Tool age/dressing/wire condition and coolant/slurry genealogy are repeated-measures process variables.
124. P35 has two release stages: `SINGULATION-ROOM-TEMP-QUALIFIED`, then final `RP01-SINGULATION-QUALIFIED` only after P33 cryogenic edge-survival feedback.

---

# Current checkpoint — READ THIS FIRST

Latest:

`research/2026-08-16_checkpoint_after_singulation_round33.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_ftir_composition_thickness_round32.md`
- `research/2026-08-16_checkpoint_after_temporal_deembedding_round31.md`
- `research/2026-08-16_checkpoint_after_bias_network_round30.md`
- `research/2026-08-16_checkpoint_after_noise_chain_round29.md`
- `research/2026-08-16_checkpoint_after_radiometry_round28.md`
- older checkpoints for detailed fabrication genealogy.

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND33.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND33.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND32.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND32.md`
- older addenda as needed.

---

# Controlled module set

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP
- P06 FTIR composition/thickness + P06A FTIR apparatus/model/cutoff lineage + register
- P07 CdZnTe + P07A/P07B/P07C
- P08 RIE blocking contact + P08A–P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating + P10A bias/load transfer + register
- P11 absolute radiometry/responsivity + P11A Optronics transfer + register
- P12 noise/PSD/NEP/D* + P12A preamp lineage + P12B analyzer transfer + P12C state identity + register
- P13 temporal/frequency response + P13A detailed UWA TPCD apparatus/de-embedding + register
- P14 lithography/CD + P14A
- P15 cryogenic package framework
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
- **P35 HgCdTe/CdZnTe singulation/die-edge empirical process window + register**

Rounds 28–32 did not require new top-level modules because their base SOPs were already method-complete. Round 33 **did** identify a genuine fabrication execution gap and created P35.

---

# Canonical RP-01 direct anchors — do not drift

## Material / fabrication

- LPE n-HgCdTe on electrically insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `mu=4.0×10^4 cm²/V·s`
- active thickness `9.5 µm`
- supplier n/µ measurement temperature undisclosed
- method used historically to obtain x≈0.30 and 9.5 µm is OPEN
- native anodic oxide `~800 Å = 80 nm`
- RIE: Plasma Technology parallel-plate; printed `CH4/5H2`; total 64 sccm; 100 mTorr; 50 W; 60 s
- converted average n `~2.0×10^15 cm^-3`; mobility `~3.3×10^4 cm²/V·s`
- Cr 30 nm / Au 270 nm
- nine 300×300-µm contacts; gaps 50–400 µm in 50-µm increments
- `rho_c≈9×10^-4 Ω cm²` at 80 K
- **singulation method/final die outline/edge exclusion OPEN**

## Detector / radiometry / noise

- Optronics Laboratories Spectral Response Measurement System
- ~80 K
- stated 60° FOV
- responsivity/spectral response chopped at 1 kHz
- Figure-3 field explicitly means voltage bias between contacts
- Figure-3 sweep roughly 0–50 V/cm
- Figures 5–7 at 10 V/cm
- Figures 3/5/6/7 same physical detector
- exact contact pair/gap remains open
- detector cutoff stated ~4.4 µm; exact cutoff criterion remains OPEN
- BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm
- quoted 300-K/60° photon flux ~`1×10^15 cm^-2 s^-1`
- quoted QE ~70%
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz by trend intersection
- high-frequency g-r level ~24.5 nV/sqrtHz
- exact 1-kHz noise/bandwidth convention for historical D* remains open
- no recovered direct RP-01 lifetime or frequency-response curve.

---

# Current empirical-state summary

## P06/P06A FTIR

Keep `{d_physical,d_FTIR,lambda_edge,Eg/x_opt,lambda_det,c}` distinct. At 80 K, Hansen x=.300 gives `lambda_g,eq=5.0879 µm`; treating 4.4 µm as `hc/Eg` would give Hansen-equivalent x≈.3241. This is a consistency warning only.

## P10A/P11A/P12C/P13A

- field uses measured contact voltage / measured active gap;
- radiometry requires real view factor/radiance state;
- 24.5 nV/sqrtHz is not automatically 1-kHz noise;
- RP-01 lifetime/f3dB remain open;
- package thermal poles must be excluded from detector lifetime.

## P33 package

Package attachment/interconnect/thermal response is device physics. P35 now hands a room-temperature-qualified singulated die into P33 and receives cryogenic edge-survival feedback.

## P34 RIE

Direct controller center remains `64 sccm / 100 mTorr / 50 W / 60 s / CH4/5H2`; reactor equivalence requires measured plasma/sheath/thermal/chamber and physical/electrical outputs.

## P35 singulation

Historical RP-01 method remains open.

Strong transfer branches:

- Rockwell HgCdTe: conventional diamond-grit saw problems and excimer edge-performance branch;
- Yoo 1998 finished CdZnTe: graphite/wax + photoresist protection + 125-mm stainless wire + 16-µm BN slurry + ~1 h/cut;
- Szeles 2006 CdZnTe: hidden saw damage may require ~100 µm removal even after low-damage wire saw; blade damage can be deeper;
- Rockwell II–VI laser: ablation can change stoichiometry.

These are transfer evidence only. P35 releases the actual finished HgCdTe/CdZnTe stack using mechanical + subsurface + electrical/noise + cryogenic outputs.

---

# Persistent highest-value OPEN items

- exact RP-01 Mask-1/Mask-2 commercial lithography details
- exact UWA wet-mesa formulation basis/HBr assay
- exact RP-01 CdZnTe composition/face/polarity/miscut/final surface
- exact Honeywell/Fermionics LPE boat/charge/gas/contact trajectory
- exact supplier/UWA anneal history
- exact Cr/Au deposition hardware/rates/vacuum
- exact RP-01 singulation/die outline/street/protection/clean
- exact RP-01 package construction
- exact Plasma Technology RIE hardware/self-bias/sample temperature
- exact RP-01 Optronics optical bench/calibration chain
- exact RP-01 bias/load/preamp circuit
- exact RP-01 temporal response/lifetime
- exact historical method behind `x≈0.30` and `9.5 µm`
- exact detector cutoff convention for `4.4 µm`.

---

# Active source-recovery record

Identified but not fully recovered:

- Vanya Srivastav IISc thesis `G25544.pdf`
- John Kenion White 2005 UWA thesis full experimental text
- Ryan Westerhout 2013 UWA thesis experimental text
- J. F. Siliquini 1995 UWA PhD thesis
- Redfern/Musca/Smith/Dell/Faraone 1999 TPCD conference full experimental text
- Smith et al. 2000 in-situ vacuum processing full text
- exact Honeywell/Fermionics LPE travelers
- exact UWA Mask-1 traveler
- exact RP-01 package traveler
- **exact RP-01 singulation/dicing traveler / mask-layout street drawing**
- exact RP-01 Optronics calibration records
- exact Figure-5 HP35665A raw/acquisition record
- original Figure-3/5/6/7 device notebook identifying contact pair/current/resistance
- supplier/UWA material certificate identifying how `x≈0.30` and `9.5 µm` were measured
- primary PDF line for Gopal et al. 1992 thickness-range unit conflict.

Same-UWA public repository searches in Round 33 identified neighboring device papers but did not recover an executable singulation traveler. “Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 34: P16 end-to-end first-build / reproducibility / release-readiness audit**.

The major fabrication chain now has empirical execution layers through singulation and package handoff. Do not create another process module reflexively.

Round 34 should:

1. audit every P16 phase against the latest P24–P35 empirical modules and travelers;
2. update/reconcile P16's generic references where newer empirical modules own execution, especially P35 for STEP G1;
3. classify every remaining unresolved variable as one of:
   - `HISTORICAL-IDENTITY-ONLY` — unknown historical detail not required to execute a scientifically traceable local equivalent;
   - `EXECUTION-BLOCKER` — cannot perform the step without defining/qualifying it;
   - `RELEASE-BLOCKER` — a build can be attempted but cannot be accepted without closure;
   - `LOCAL-QUALIFIABLE` — can be replaced by explicit empirical qualification without claiming UWA historical identity;
4. create a first-build readiness matrix by phase and process state;
5. identify missing cross-module handoff data and travelers;
6. distinguish three claims rigorously:
   - `TRACEABLE-FIRST-BUILD-READY`;
   - `HISTORICAL-RP01-REPRODUCED`;
   - final `REPRODUCIBLE-RELEASE`;
7. do not let historical-identity gaps unnecessarily block a local scientifically controlled build, but do not erase them;
8. preserve all empirical provenance and negative searches in the audit.

The likely goal of Round 34 is to determine the **minimum remaining closure set before a competent laboratory could execute the first fully traceable fabrication run from substrate through packaged detector**.
