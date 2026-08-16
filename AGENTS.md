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
8. Treat passivation, post-RIE exposure, wet-etch surface exposure, metal-interface exposure, LPE source genealogy, anneal cooldown, substrate clean-to-load, RIE chamber state, packaging and thermal-cycle history as process variables.
9. Measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Specifications derive from downstream material/device performance, not observed process spread.
11. Failure diagnosis: signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification.
12. Repository procedures do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S.
13. Numerical sensitivities/tolerances state protected output, input, operating point and evidence class. Proxies may size experiments but cannot release production specifications.
14. `xS/xL` is not `dxS/dxL` when other equilibrium coordinates vary.
15. Coded DOE coordinates do not create physical process tolerances.
16. Repeated observations from one melt/source/bath/substrate/anneal-source/chamber/package genealogy are not iid replicates.
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

---

# Current checkpoint — READ THIS FIRST

Latest:

`research/2026-08-16_checkpoint_after_ftir_composition_thickness_round32.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_temporal_deembedding_round31.md`
- `research/2026-08-16_checkpoint_after_bias_network_round30.md`
- `research/2026-08-16_checkpoint_after_noise_chain_round29.md`
- `research/2026-08-16_checkpoint_after_radiometry_round28.md`
- `research/2026-08-16_checkpoint_after_rie_reactor_equivalence_round27.md`
- `research/2026-08-16_checkpoint_after_empirical_packaging_round26.md`
- older checkpoints for detailed fabrication genealogy.

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND32.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND32.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND31.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND31.md`
- older addenda as needed.

---

# Controlled module set

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP
- **P06 FTIR composition/thickness + P06A FTIR apparatus/model/cutoff lineage + register**
- P07 CdZnTe + P07A/P07B/P07C
- P08 RIE blocking contact + P08A–P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating + P10A bias/load transfer + register
- P11 absolute radiometry/responsivity + P11A Optronics transfer + register
- P12 noise/PSD/NEP/D* + P12A preamp lineage + P12B analyzer transfer + P12C state identity + register
- P13 temporal/frequency response + P13A detailed UWA TPCD apparatus/de-embedding + register
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

No new top-level module was created in Rounds 28–32 because P11/P12/P10/P13/P06 were already method-complete; the missing layer was historical lineage/state/apparatus/model transfer.

---

# Canonical RP-01 direct anchors — do not drift

## Material / fabrication

- LPE n-HgCdTe on electrically insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `mu=4.0×10^4 cm²/V·s`
- active thickness `9.5 µm`
- supplier n/µ measurement temperature undisclosed
- **method used historically to obtain x≈0.30 and 9.5 µm is OPEN**
- native anodic oxide `~800 Å = 80 nm`
- RIE: Plasma Technology parallel-plate; printed `CH4/5H2`; total 64 sccm; 100 mTorr; 50 W; 60 s
- converted average n `~2.0×10^15 cm^-3`; mobility `~3.3×10^4 cm²/V·s`
- Cr 30 nm / Au 270 nm
- nine 300×300-µm contacts; gaps 50–400 µm in 50-µm increments
- `rho_c≈9×10^-4 Ω cm²` at 80 K

Do not combine average converted n with the separate ~8-µm conversion-depth lineage into one direct sheet density.

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
- detector cutoff stated ~4.4 µm; **exact cutoff criterion remains OPEN**
- BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm
- quoted 300-K/60° photon flux ~`1×10^15 cm^-2 s^-1`
- quoted QE ~70%
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz by trend intersection
- high-frequency g-r level ~24.5 nV/sqrtHz
- exact 1-kHz noise/bandwidth convention for historical D* remains open
- no recovered direct RP-01 lifetime or frequency-response curve.

---

# Current measurement-state layers

## P06/P06A FTIR / material optical state

P06 remains the canonical operator SOP. P06A adds empirical apparatus/model provenance and a qualification register.

Permanent measurement vector:

`{d_physical, d_FTIR, lambda_50T/lambda_T-int, Eg,opt, x_opt, lambda_det,c}`

with explicit definitions and no automatic equality.

Strong apparatus-transfer examples:

- Chang et al. 2005: Thermo Nicolet Centaur µs IR microscope + Nicolet 870 FTIR + computerized x-y stage; ~1-µm stated stage precision; ~100-µm mapping aperture; automated x/thickness maps.
- Murthy et al. 2009: Te-rich horizontal-slider LPE HgCdTe/Cd0.96Zn0.04Te; Bruker IFS 66v/S; composition from 300-K IR absorption and thickness from interference fringes.
- Yue et al. 2019: Bruker IFS 66v/S + KBr beamsplitter + LN2 HgCdTe detector + evacuated path.

These are transfer branches, not RP-01 bench identity.

Hansen consistency only: x=.300 at 80 K gives band-gap-equivalent 5.0879 µm; the 4.4-µm detector cutoff would correspond to Hansen-equivalent x≈.3241 if one intentionally made the `hc/lambda` substitution. This mismatch is a warning against conflation, not a corrected historical composition.

## P10A bias/load

Historical field target is contact voltage divided by active gap. Exact bias-source/load/preamp circuit remains open. Local transfer measures `V_source`, `V_contact`, I, E, P, static/differential R, `H_sig(f)`, `H_noise(f)`, `Z_pre(f)`, source noise and package thermal state.

## P11A radiometry

Same-UWA Optronics lineage is real; exact model/calibration chain remains open. 60° full-cone interpretation is a Planck-flux consistency check only. Absolute work uses radiance temperature, actual aperture/view factor and transmission.

## P12C noise

Same physical detector for Figs 3/5/6/7; Figure 5 is 80 K / 10 V/cm / 60° FOV. Do not use 24.5 nV/sqrtHz automatically at 1 kHz. HP35665A exact span/lines/window/averaging remain open.

## P13/P13A temporal

RP-01 `tau/f_3dB` open. Strongest same-UWA method branch is Rajaduray 1998: 1.047 µm / 25 ns / 1 kHz / 77 K vacuum / low current bias / AC-coupled amplifier / HP54522A / 500×20-ns samples / 128 averages. Local release requires source waveform, injection-level, bias/readout, package thermal, fit-model and time-frequency consistency gates.

## P33 package

HgCdTe PC bonding layers can create several-ms and hundreds-ms thermal recovery. Measure package thermal kernel before assigning slow detector poles.

## P34 RIE

Direct controller center remains 64 sccm / 100 mTorr / 50 W / 60 s / CH4/5H2. Transfer requires self-bias/sheath proxy, sample T(t), oxide-clear, physical etch, electrical conversion and downstream contact/blocking/noise closure.

---

# Persistent fabrication/process OPEN items

- exact RP-01 Mask-1/Mask-2 commercial lithography details
- exact UWA wet-mesa formulation basis/HBr assay
- exact RP-01 CdZnTe composition/face/polarity/miscut/final surface
- exact Honeywell/Fermionics LPE boat/charge/gas/contact trajectory
- exact supplier/UWA anneal history
- exact Cr/Au deposition hardware/rates/vacuum
- exact RP-01 singulation/die-separation method and edge-clean state
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
- J. F. Siliquini 1995 UWA PhD thesis — highest-value P10/P12 electronics target
- Redfern/Musca/Smith/Dell/Faraone 1999 TPCD conference full experimental text
- exact Rajaduray AC amplifier/Keithley/laser-energy setup records
- Smith et al. 2000 in-situ vacuum processing full text
- exact Honeywell/Fermionics LPE travelers
- exact UWA Mask-1 traveler
- exact RP-01 package traveler
- exact RP-01 singulation/dicing traveler
- 1989 SPIE Optronics/low-background-radiometry full text
- exact RP-01 Optronics calibration records
- exact Figure-5 HP35665A raw/acquisition record
- original Figure-3/5/6/7 device notebook identifying contact pair/current/resistance
- supplier/UWA material certificate or notebook identifying how `x≈0.30` and `9.5 µm` were measured
- primary PDF line for Gopal et al. 1992 thickness-range unit conflict.

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 33: singulation / dicing / die-edge damage / package-ready die preparation**.

This appears to be a genuine end-to-end fabrication gap rather than another already-complete metrology method.

1. Audit `procedures/P15_DIE_ATTACH_INTERCONNECT_CRYOGENIC_PACKAGE_QUALIFICATION.md`, `procedures/P33_CRYOGENIC_DIE_ATTACH_INTERCONNECT_EMPIRICAL_PROCESS_WINDOW.md`, `procedures/P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`, and relevant P18 failure records.
2. Search primary HgCdTe/CdZnTe detector papers, patents, theses and institutional process records for saw, scribe/cleave, lap or other die-separation methods.
3. Recover blade/grit/thickness, spindle/feed/depth, coolant, protective coating/tape, street/kerf, chipping/subsurface-damage and cleaning parameters where primary evidence exists.
4. Treat dicing coolant/cleaner/residue as a detector surface/process variable; do not introduce a cleaning chemistry because it is standard for Si/GaAs.
5. Record edge-to-active-region exclusion, chip/crack metrics, contamination/particle state, die pickup/handling and post-singulation storage.
6. Require pre/post-singulation electrical/noise/optical checks on qualification units and cryogenic survival before package release.
7. Separate mechanical die yield from detector-performance yield; an intact die can still have dicing-induced electrical/noise degradation.
8. Create a new empirical top-level module only if the audit confirms no existing controlled singulation procedure; current repo state strongly suggests this is missing.

Do not populate production tolerances without repeated local fabrication data.
