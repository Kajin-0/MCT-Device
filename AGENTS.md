# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** executable by a competent researcher without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains direct historical anchors, empirical transfer procedures, metrology SOPs, qualification travelers, failure/release architecture and explicit unresolved gaps.

---

# Non-negotiable scientific/provenance rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, explicit derivation, or a named evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct RP-01, same-lineage, transfer-family, model, derived, apparatus-calibration and local-qualification evidence.
4. Every critical process step needs output metrology and a pass/fail/qualification gate.
5. Preserve negative searches, failed branches, rejected inferences, corrections and source conflicts.
6. Use measured fabricated geometry for field, active area and D* normalization.
7. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density, `rho_c` and minority-carrier blocking metrics distinct.
8. Treat passivation, post-RIE exposure, wet-etch surface exposure, metal-interface exposure, anneal cooldown, substrate clean-to-load, LPE source genealogy, chamber state and packaging as process variables.
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
61. **P05 audit rule:** P05 is already the canonical Hall/VdP execution SOP; do not duplicate it without materially new method evidence.
62. **Die attach is a detector variable.** Mechanical compliance, CTE, bondline thermal conductance, cure and noise/electrical state are coupled.
63. Adhesive product identity is not a bondline specification; measure thickness/coverage/voiding/tilt.
64. Honeywell 5-g/40-g thermocompression values are transfer experiment values, not RP-01 setpoints.
65. Package-generated thermal poles can occur on ms-to-hundreds-ms scales; do not assign them to intrinsic lifetime without P33/P13 separation.
66. Thermal-cycle genealogy is not independent replication.
67. Do not transplant p-HgCdTe/FPA interconnect metallurgies into the RP-01 Cr/Au chain without reopening P26/P24.
68. A package is not released by die shear/wire pull alone.
69. **RIE watts are not an ion-energy coordinate.** Record measured dc self-bias or another calibrated sheath/ion-energy proxy for reactor transfer.
70. **RIE physical depth is not electrical conversion depth.** Keep `d_etch`, `d_conv` and `L_conv` separate.
71. **Separate oxide clear from semiconductor exposure:** `t_sem = t_RF - t_clear` only after local `t_clear` is measured.
72. A same-era Plasma Technology RIE80 using 13.56 MHz does not prove RP-01 used RIE80 or 13.56 MHz.
73. Do not infer RP-01 electrode area from `50 W / 0.4 W cm^-2`.
74. RIE chamber clean/seasoning/loading history is a genealogy variable; pre/post-clean runs are not iid replicates.
75. Preserve P29 crystallographic plane/polarity into P34 because primary CH4/H2 HgCdTe data show orientation-dependent etch rate/morphology.
76. Matching `64 sccm / 100 mTorr / 50 W / 60 s` alone is **not reactor equivalence**.
77. **P11 audit rule:** P11 is the canonical absolute-radiometry SOP; do not create a duplicate top-level module unless new evidence materially changes the method.
78. Same-UWA use of an Optronics Laboratories Spectral Response Measurement System establishes measurement-lineage continuity, not exact historical instrument identity/configuration.
79. **A stated FOV angle is not a radiometric geometry.** Record physical aperture radii/areas, separations, offsets, window/shield geometry and the resulting view factor.
80. The provisional interpretation of RP-01 `60° FOV` as a 60° full cone is a consistency inference from the quoted 300-K photon flux, not documentary proof.
81. **Blackbody controller/contact temperature is not radiance temperature.** Absolute background calibration requires calibrated radiance or radiance temperature plus emissivity/geometry/transmission uncertainty.
82. For photoconductive HgCdTe, responsivity linearity must be qualified versus actual irradiance and background state; equal total radiant power with different spot area/background is not automatically equivalent.
83. P11 responsivity and P12 noise may be combined into D* only when temperature, electric field, package/window state, FOV/background, active-area convention and frequency convention are matched or explicitly corrected.
84. Optronics model `735D` remains a historical lead only; do not assign it to RP-01 until primary documentary evidence closes the identity.

---

# Current checkpoint — READ THIS FIRST

Latest:

`research/2026-08-16_checkpoint_after_radiometry_round28.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_rie_reactor_equivalence_round27.md`
- `research/2026-08-16_checkpoint_after_empirical_packaging_round26.md`
- `research/2026-08-16_checkpoint_after_empirical_mask1_round25.md`
- `research/2026-08-16_checkpoint_after_empirical_hg_anneal_round24.md`
- `research/2026-08-16_checkpoint_after_empirical_lpe_execution_round23.md`
- `research/2026-08-16_checkpoint_after_empirical_czt_substrate_round22.md`
- `research/2026-08-16_checkpoint_after_empirical_wet_mesa_round21.md`
- older checkpoints as needed.

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND28.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND28.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND27.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND27.md`
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
- P11 absolute radiometry/responsivity + **P11A UWA Optronics lineage/transfer addendum + register**
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
- P31 Hg-overpressure anneal apparatus/reservoir/trajectory empirical process window + register
- P32 Mask-1/wet-mesa lithography empirical process window + register
- P33 cryogenic die-attach/interconnect/package empirical process window + register
- P34 CH4/H2 RIE reactor-equivalence empirical process window + register

P24–P34 are empirical/practical execution layers supplementing earlier physics/metrology modules. P11A is a lineage/transfer addendum because P11 itself was already operationally complete; **no P35 was created in Round 28**.

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

## Mask-2 / metal / TLM
- resist ~4–5 µm
- prebake 80 °C / 30 min
- chlorobenzene 30 min
- pattern/develop/water rinse
- Cr 30 nm / Au 270 nm
- nine 300×300-µm contacts
- gaps 50–400 µm in 50-µm increments
- `rho_c≈9×10^-4 Ω·cm²` at 80 K

## Detector / radiometry benchmark
- ~80 K
- Optronics Laboratories Spectral Response Measurement System
- stated 60° FOV
- responsivity/spectral response chopped at 1 kHz
- single-wavelength responsivity near 4 µm versus field
- spectral responsivity / D* state at 10 V/cm
- cutoff ~4.4 µm
- BLIP D* ~`2×10^11 cm Hz^1/2/W` at 4 µm
- quoted 300-K/60° background photon flux ~`1×10^15 photons cm^-2 s^-1`
- quoted QE ~70%
- noise lineage: low-noise preamp + HP35665A, 1/f knee ~3 kHz, high-frequency g-r plateau ~24.5 nV/sqrt(Hz)

---

# P11A — radiometry lineage / transfer state

## Same-UWA measurement lineage

Parish et al. 1997 independently reports an Optronics Laboratories Spectral Response Measurement System used for HgCdTe photoconductor responsivity measurements at:

- 1-kHz chopping;
- 80 K;
- approximately 3–12 µm spectral range;
- 10 V/cm in the published spectral-response figure.

This is strong same-UWA lineage evidence. It does **not** identify the exact RP-01 Optronics model, calibration detector, slit/bandpass, FOV geometry or signal convention.

## FOV consistency

The existing Planck check gives strong internal consistency for interpreting RP-01 `60°` as a **full cone** (`30°` half-angle): the idealized 300-K photon flux through a 4.4-µm step response is close to the quoted `1e15 cm^-2 s^-1`.

For a simple circular stop:

`a/z = tan(30°) = 0.57735`.

Ordinary cone solid angle:

`Omega = 2*pi*(1-cos 30°) ≈ 0.84179 sr`.

Lambertian projected angular integral:

`pi*sin^2(30°) = pi/4 ≈ 0.78540 sr`.

These define a geometry family, **not historical dimensions**.

## Blackbody transfer rule

Absolute background calibration records calibrated radiance/radiance temperature, effective emissivity, aperture geometry, exact view factor, package transmission and uncertainty. Contact/controller temperature alone is insufficient.

## Photoconductor linearity/background rule

Primary HgCdTe detector metrology shows PC-HgCdTe nonlinearity can depend on irradiance, and background fluctuations can couple through detector nonlinearity into apparent responsivity drift. Local qualification therefore varies irradiance at the actual beam size/background and monitors background-dependent repeatability.

## D* state matching

For local release:

`D* = R_v sqrt(A) / e_n`

may combine P11/P11A and P12 only when the relevant temperature, field, package/window, FOV/background, area and frequency conventions match or are explicitly corrected.

## OL-735D lead

A 1989 SPIE item is repeatedly indexed as an Optronics `735D` / pyroelectric-reference / broadband-blackbody architecture. Full primary text remains unrecovered. Status: `SECONDARY-LEAD / PRIMARY-FULL-TEXT-NOT-RECOVERED`.

Never write “RP-01 used an OL-735D” without documentary closure.

## Historical optical blockers

Still open:

- exact Optronics model;
- source and monochromator configuration;
- gratings/slits/bandpass;
- wavelength calibration;
- order-sorting filters;
- reference detector and absolute calibration chain;
- physical 60° aperture/cold-shield dimensions;
- window/filter transmission;
- chopper duty/waveform;
- responsivity preamplifier/lock-in chain;
- RMS/peak/fundamental convention;
- beam diameter/profile;
- active-area convention;
- historical 4.4-µm cutoff definition;
- exact area/noise/background conventions used for published D*.

---

# P34/P33/P32/P31/P30 concise state

## P34 RIE reactor equivalence

Direct RP-01 controller center is preserved, but transfer release requires measured self-bias/sheath proxy, sample `T(t)`, oxide-clear time, physical etch, sheet state, electrical conversion depth/lateral spread, TLM and blocking/noise closure. Historical model/RF/electrode geometry/self-bias/sample temperature remain open.

## P33 cryogenic package

Honeywell primary evidence shows compliant silicone attachment prevented cooldown cracking in its HgCdTe experiments; NRL/Bartoli photoconductor construction shows bonding layers can create several-ms and hundreds-ms thermal recovery components. Measure package thermal kernel before assigning slow P13 poles to carrier lifetime.

## P32 Mask-1

Historical identity remains open. Strong transfer branches: AZ4620/Br2:HBr and Hunt 180CP/Br2-methanol. Release from actual resist survival plus `CD_mask -> CD_PR -> CD_mesa`, not nominal thickness.

## P31 Hg anneal

Low-T screening anchor ~250 °C/1 h under Hg-rich/pseudo-isothermal transfer branch; isothermal and two-temperature routes remain distinct. No universal Hg reservoir mass.

## P30 LPE

Honeywell tie line `xL=.082, yL=.810, TL=507 °C -> xS≈.29`; composition does not determine total charge. Wipe-off hardware generations remain distinct.

---

# P29–P24 concise state

- **P29 CdZnTe:** strong transfer center `Cd0.96Zn0.04Te {111}`; exact RP-01 y/polarity/miscut/final surface open.
- **P28 wet mesa:** nominal `2% Br2 in 3:1 EG:HBr`, 21 °C, `R_V≈2.78 µm/min`, ±26%, `A≈0.63`; formulation basis/HBr assay/agitation/rinse open; release by measured depth + isolation.
- **P27 Mask-2:** direct 4–5 µm / 80 °C 30 min / chlorobenzene 30 min anchors; exact resist/dose/developer/lift-off solvent open.
- **P26 Cr/Au:** 30 nm Cr / 270 nm Au / `rho_c≈9×10^-4 Ω·cm²` at 80 K; exact deposition hardware/rates partly open.
- **P25 anodic oxide:** strongest transfer center 0.1 M KOH, 90% EG/10% DI, ~0.30 mA/cm², ~15 V, ~2 min, ~80 nm; transfer only.
- **P24 blocking contact:** direct RP-01 controller center preserved; P34 controls reactor equivalence.

---

# Measurement / release essentials

- P05 Hall: canonical execution SOP; current/field reversal, VdP redundancy, variable field, self-heating, multicarrier escalation.
- P06 FTIR: distinguish composition/bandgap model from detector cutoff.
- P10: `E=V_active/L_measured`; package thermal resistance matters under bias.
- P11/P11A: calibrated absolute radiometry, measured reference-plane/FOV geometry, irradiance/background linearity and matched P12 state.
- P12: `NEP=e_n/R_v`; `D*=R_v sqrt(A)/e_n`; combine independent noise at PSD level.
- P13: de-embed source/optics/detector/bias/preamp/cable/instrument and P33 package thermal response where relevant.
- P17: separate measurement/spatial/run/lot/long-term variation; no generic Cpk threshold.
- P18: preserve negative/failed runs and competing mechanisms.
- P19/P20: trace final requirements and sensitivities without replacing empirical process data.

---

# Highest-priority OPEN practical details after Round 28

## P12 noise / analyzer / background state — strongest next empirical target

Audit `P12`, `P12A`, and `P12B` before creating any new top-level module.

Priority historical/empirical recovery:

- exact UWA low-noise preamplifier circuit/model used for RP-01;
- HP35665A input range/coupling/window/FFT span/lines/averaging;
- ASD/PSD normalization and analyzer ENBW/bin-width convention;
- exact detector contact pair/active geometry tied to the published Figure-5 noise trace;
- bias-source/load topology and bias-resistor contribution;
- optical-background/FOV state during noise measurement;
- whether the 60° FOV was filled by a 300-K scene during the PSD measurement or merely quoted as detector environment;
- calibration from analyzer input back to detector-terminal V/sqrt(Hz);
- preamp gain/bandwidth/input-noise/loading;
- matched P11/P12 temperature, field, area, package and background for D* closure.

If P12/P12A/P12B are already operator-complete, create only a lineage/transfer addendum analogous to P11A rather than duplicate documentation.

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

Identified but not fully recovered through current routes:

- Vanya Srivastav IISc thesis `G25544.pdf` full process text;
- John Kenion White 2005 UWA thesis full experimental text — current repository PDF route returns 403;
- Ryan Westerhout 2013 UWA thesis experimental text;
- Smith et al. 2000 in-situ vacuum processing full experimental text;
- Musca/Smith/Dell/Faraone photoconductor contact/passivation traveler;
- exact Honeywell/Fermionics LPE travelers;
- exact UWA Mask-1 traveler;
- exact RP-01 die attach/interconnect/Dewar traveler;
- 1989 SPIE “Relative Spectral Response And Low Background Radiometric Detector Measurements” full primary text;
- exact RP-01 Optronics system traveler / calibration records.

“Not recovered” does not mean absent.

---

# Next logical work

Proceed with **Round 29: audit and empirical reconstruction of P12 noise / preamplifier / HP35665A / optical-background state**.

1. Audit `procedures/P12_NOISE_PSD_NEP_DETECTIVITY.md`, `P12A_UWA_PREAMPLIFIER_LINEAGE_ADDENDUM.md`, and `P12B_NOISE_READOUT_ANALYZER_TRANSFER_QUALIFICATION.md` first.
2. Search same-UWA HgCdTe photoconductor papers, proceedings and theses for the low-noise preamplifier and HP35665A settings.
3. Recover bias/load topology and detector-terminal noise calibration.
4. Determine the actual FOV/background state during the published PSD measurement.
5. Keep analyzer bin width, window ENBW, PSD and ASD definitions separate.
6. Tie the noise trace to the actual fabricated contact pair/active geometry where possible.
7. Require matched P11/P12 state before recomputing the historical D* benchmark.
8. Create a new top-level module only if the audit demonstrates a real execution gap; otherwise create a lineage/transfer addendum.

Do not populate production tolerances without repeated local fabrication data.
