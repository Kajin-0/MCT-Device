# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 51  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce the final source-traceable HgCdTe photodetector fabrication and characterization procedure paper/booklet. The user wants to review the finished technical manual, not repository/software infrastructure work.

Canonical historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

Primary current manuscript:

`manuscript/RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md`

Latest checkpoint:

`research/2026-08-16_checkpoint_after_manuscript_integration_round51.md`

Then, for detailed history:

- `research/2026-08-16_checkpoint_after_deployment_security_round50.md` — ancillary infrastructure history only;
- `research/2026-08-16_checkpoint_after_operational_provenance_round49.md`;
- `research/2026-08-16_checkpoint_after_digital_provenance_round48.md`;
- `research/2026-08-16_checkpoint_after_control_system_dry_run_round47.md`;
- `research/2026-08-16_checkpoint_after_sequential_material_release_round46.md`;
- `research/2026-08-16_checkpoint_after_sample_genealogy_round45.md`;
- `research/2026-08-16_checkpoint_after_information_optimal_jacobian_round44.md`;
- `research/2026-08-16_checkpoint_after_uncertainty_allocation_round43.md`.

Latest manuscript gap distinction:

`docs/RP01_GAP_MATRIX_ADDENDUM_ROUND51.md`.

## Critical Round-51 direction change

Do not resume open-ended security/provenance/software work unless it directly blocks the final fabrication manual.

Permanent distinction:

`LOCAL-EXECUTION-INSTANTIATION-REQUIRED != MANUSCRIPT-CONTENT-OPEN`.

An unspecified future lab will necessarily have local values for furnace offsets, MFC calibration, QCM tooling factor, resist exposure dose, bondline geometry, optical view factor, etc. The manual must identify those variables and define how to qualify them; it must not postpone manuscript completion until a real lab exists and must never invent universal numbers.

New document state:

`RP01-INTEGRATED-MANUSCRIPT-DRAFT-READY = YES`.

This is not a physical process maturity label.

## Physical maturity remains separate

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated lab.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.
- repository logic/provenance/security states from Rounds 47–50 may remain recorded but are ancillary to the manual.

## Evidence discipline

Never invent a missing value.

Use these conceptual classes consistently:

- direct RP-01;
- same-UWA/same-lineage;
- primary transfer;
- derived;
- reference qualification center;
- local calibration/qualification;
- historical identity open.

Repetition does not promote evidence class. “Not recovered” does not mean absent.

## Integrated Draft 0.1 reference route

1. **Substrate:** insulating CdZnTe; first transfer center Cd0.96Zn0.04Te (111)B; exact RP-01 Zn fraction/polarity/miscut open.
2. **Final substrate surface:** strongest Te-rich LPE transfer family uses brief 2–3% Br2/methanol; concentration basis/time/rinse/clean-to-load must be locally explicit.
3. **LPE topology:** covered Honeywell-derived graphite horizontal slider with Hg source/containment and defined wipe-off architecture.
4. **LPE composition center:** xL=.082, yL=.810, TL=507 °C, xS≈.29.
5. **Authoritative mass fractions:** Hg=.2497382358, Cd=.01250164993, Te=.7377601143 using Hg=200.59, Cd=112.414, Te=127.60 g/mol.
6. **Atmosphere:** N2 purge -> H2; actual flows/gas quality local.
7. **First LPE contact screen:** near 500 °C (~7 K nominal supercooling) as a reference center; actual contact time selected from measured thickness/morphology, not imported blindly.
8. **As-grown material:** P06 FTIR spatial map + P05 Hall/VdP.
9. **Hg anneal:** first center ~250 °C / 1 h / Hg-saturated isothermal-like; release by post-anneal P05/P06, not “n-type” alone.
10. **Mask 1:** thick positive novolak/DNQ family; AZ4620 strongest product-identified Br2/HBr screening candidate, not historical identity.
11. **Wet mesa:** reference center nominal 2% Br2 in 3:1 EG:HBr near 21 °C; Rv~2.78 µm/min transfer datum, anisotropy~.63, best roughness~2 nm; formulation basis/HBr assay unresolved and must be locally defined/calibrated.
12. **Anodic oxide:** RP-01 ~80 nm; reference TI-PC center 0.1 M KOH in stated 90% EG/10% DI, HgCdTe anode/carbon cathode, J~0.30 mA/cm², ~15 V, ~2 min, deep-blue auxiliary indicator; solvent-ratio basis local; accept using V(t), Q/A, physical thickness/interface/downstream data.
13. **Mask 2 direct:** 4–5 µm resist, 80 °C/30 min prebake, chlorobenzene 30 min, then pattern/develop/water rinse. Resist product/exposure/developer/chlorobenzene order/lift-off local.
14. **RIE direct:** Plasma Technology parallel plate, CH4/5H2, total 64 sccm, 100 mTorr, 50 W, 60 s. Candidate 1:5 interpretation -> 10.6667 CH4 / 53.3333 H2 sccm, explicitly not direct MFC history.
15. **RIE equivalence:** self-bias/ion-energy proxy, sample T, chamber state, oxide-clear time t_clear, semiconductor exposure t_sem, physical recession, electrical conversion/LBIC/TLM/blocking response. `50 W != reactor equivalence`.
16. **RIE converted reference:** n~2.0e15 cm^-3, mu~3.3e4 cm²/Vs.
17. **Metal:** Cr/Au 30/270 nm direct; thermal evaporation first same-UWA method-family transfer. Vacuum/rates/QCM/sample heating are local.
18. **TLM:** nine ~300×300 µm contacts, gaps 50–400 µm in 50-µm increments; rho_c~9e-4 ohm cm² at 80 K.
19. **P10 electrical:** canonical 80 K, E=10 V/cm; nominal ideal current ~1.79 mA; active V 0.05–0.40 V across 50–400 µm gaps. Measured active voltage/gap control E.
20. **Singulation:** low-force CdZnTe-compatible wire-saw family first screen; exact historical RP-01 method open; qualify functional edge exclusion.
21. **Package:** compliant silicone-family first screen from direct HgCdTe cryogenic evidence; package thermal response must be measured because ms-to-hundreds-ms poles can masquerade as detector dynamics.
22. **Responsivity:** canonical T=80 K, E=10 V/cm, 1-kHz modulation, nominal 60° FOV; calibrated comparator/reference detector preferred.
23. **Noise/D*:** historical 1/f knee ~3 kHz and high-f g-r ASD ~24.5 nV/sqrtHz. 24.5 nV/sqrtHz is not automatically the 1-kHz noise. `D*=R_v sqrt(A)/e_n` at the same state.
24. **Dynamics:** no direct RP-01 lifetime curve. De-embed source/optics/bias/preamp/cable/instrument/package; one-pole only if amplitude+phase+injection/fit checks support it.

## Key permanent cautions

- detector response cutoff ~4.4 µm != Hansen band-gap-equivalent wavelength (~5.09 µm for x=.30 at 80 K);
- physical RIE etch depth != electrical conversion depth;
- TLM rho_c does not prove minority-carrier blocking;
- apparent one-carrier Hall density near p/n transition can be meaningless;
- wet-etch timing cannot replace measured depth/isolation;
- anodization elapsed time cannot replace V(t)/Q/A/thickness/interface state;
- forward RIE watts cannot replace measured plasma/sheath/thermal state;
- package thermal poles cannot be called minority-carrier lifetime without discrimination;
- active-area convention and optical-power convention must match in D*.

## Immediate next work — Round 52

Perform an adversarial technical review of the **integrated manuscript**, not another infrastructure round.

Tasks:

1. compare Draft 0.1 line-by-line against P01–P35 and calculations;
2. flag any unsupported, contradictory, or overly prescriptive statement;
3. verify every important number/equation/evidence label;
4. normalize units/symbols/terminology;
5. identify any true remaining operator ambiguity that the manuscript itself can close;
6. create uncertainty/example-calculation appendix;
7. compile complete bibliography from the controlled source ledger;
8. revise manuscript to Draft 0.2;
9. only after technical closure, create final figures/layout and professional PDF/booklet.

The user ultimately wants the finished procedure paper/booklet to review as a whole.
