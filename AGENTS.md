# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 52  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce the final source-traceable HgCdTe photodetector fabrication and characterization procedure paper/booklet. The user wants the finished technical manual, not open-ended repository/software infrastructure work.

Canonical historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

Primary manuscript:

`manuscript/RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md`

Current manuscript version: Draft 0.2 / Round 52.

Latest technical review:

`docs/RP01_MANUSCRIPT_TECHNICAL_REVIEW_ROUND52.md`

Latest checkpoint:

`research/2026-08-16_checkpoint_after_manuscript_adversarial_review_round52.md`

Latest gap/source addenda:

- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND52.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND52.md`

For older continuity, then read Round51 and earlier checkpoints only as needed.

## Current document maturity

- `RP01-INTEGRATED-MANUSCRIPT-DRAFT-READY = YES`.
- `RP01-MANUSCRIPT-ADVERSARIAL-REVIEW-PASSED = YES`.

These are manuscript states only.

Physical maturity remains separate:

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

Do not resume open-ended security/provenance/software work unless it directly blocks the final fabrication manual.

## Round-52 permanent corrections

### 1. Title/claim

Do not call the current process `reproducible fabrication` as a demonstrated state. The manuscript title is now source-traceable **qualification** fabrication/characterization. Reproducible release requires P17 evidence.

### 2. Reference center versus executable branch

Permanent relation:

`REF-CENTER != EXECUTABLE-LOCAL-SETPOINT`.

Before any irreversible physical operation, all required local material/reagent/tool/geometry/setpoint/endpoint fields must be instantiated in the current traveler and the relevant P36/P36A acceptance evidence must exist. Blank/TBD/`appropriate`/undefined-% instructions fail preflight.

The manuscript may be complete as a qualification document while an unspecified future laboratory remains uninstantiated.

### 3. P36/P36A are part of the manual architecture

Use:

- P36 for tool/subsystem IQ, OQ, surrogate PQ and HgCdTe-residual qualification;
- P36A for mass, dimensional, lithography, wet-chemistry and anodization acceptance.

Surrogate competence does not prove HgCdTe equivalence.

### 4. RIE converted density is depth-coupled

RP-01 direct:

- `n_conv≈2.0e15 cm^-3`, averaged over converted thickness;
- `mu≈3.3e4 cm²/Vs`.

Do not treat the volumetric density as independent of `d_conv`.

Report at least:

`{R_s,N_s,mu_H,d_conv,L_conv,d_etch,rho_c,blocking_response}`

and derive:

`n_conv=N_s/d_conv`

only after `d_conv` is independently justified.

The same-lineage ~8-µm conversion-depth scale is conditional context, not a proven RP-01 reduction thickness.

### 5. RP-01 performance figures are one representative device

P12C closes Figures 3/5/6/7 as the same representative device. Exact contact pair remains open.

New D* closure should lock:

`{device,contact pair,gap,width,T,E,package,FOV/background,loading,frequency convention}`

unless an explicit measured correction is applied.

### 6. 60° FOV remains angularly ambiguous

RP-01 says 60° FOV but does not document full cone vs half-angle or physical aperture geometry.

A 60° full cone / 30° half-angle is a derived photon-flux consistency interpretation only. New work must record physical geometry and state the angle convention explicitly.

### 7. D* area convention

Define:

- `A_Dstar` = detector normalization area;
- optical beam/aperture/irradiance geometry separately.

They need not be the same physical area. If a common area coordinate enters incident-power derivation and D* normalization, retain covariance.

`gamma_A = partial ln(P_inc)/partial ln(A_Dstar)`

`S_Dstar,A = 0.5 - gamma_A`.

### 8. Noise warning remains permanent

`24.5 nV/sqrt(Hz)` is the high-frequency g-r level. It is not automatically the 1-kHz detector noise because the reported knee is ~3 kHz.

## Evidence discipline

Never invent a missing value.

Use these classes consistently:

- direct RP-01;
- same-UWA/same-lineage;
- primary transfer;
- derived;
- reference qualification center;
- local calibration/qualification;
- historical identity open.

Repetition does not promote evidence class. `Not recovered` does not mean absent.

## Current reference route

1. Substrate: insulating CdZnTe; first transfer center Cd0.96Zn0.04Te (111)B; exact RP-01 Zn/polarity/miscut open.
2. Final substrate surface: brief 2–3% Br2/methanol transfer family; concentration basis/time/rinse/clean-to-load locally explicit.
3. LPE topology: covered Honeywell-derived graphite horizontal slider with auxiliary Hg source and one defined wipe-off architecture.
4. LPE center: xL=.082, yL=.810, TL=507 °C, xS≈.29.
5. Authoritative mass fractions: Hg=.2497382358, Cd=.01250164993, Te=.7377601143 using Hg=200.59, Cd=112.414, Te=127.60 g/mol.
6. Atmosphere: N2 purge -> H2; actual flows/gas quality local.
7. LPE first screen: measured contact state near 500 °C (~7 K nominal supercooling) as REF-CENTER; absolute charge, gas, thermometry, contact time, wipe and cooldown must be locally instantiated first.
8. As-grown: P06 FTIR spatial map + P05 Hall/VdP.
9. Hg anneal: first center ~250 °C / 1 h / Hg-saturated isothermal-like; release by post-anneal P05/P06.
10. Mask 1: thick positive novolak/DNQ family; AZ4620 strongest product-identified Br2/HBr screening candidate, not historical identity.
11. Wet mesa: nominal 2% Br2 in 3:1 EG:HBr near 21 °C; ~2.78 µm/min, anisotropy~.63, best roughness~2 nm transfer data; exact formulation basis/HBr assay local.
12. Anodic oxide: RP-01 ~80 nm; TI-PC center 0.1 M KOH in stated 90% EG/10% DI, HgCdTe anode/carbon cathode, J~0.30 mA/cm², ~15 V, ~2 min; accept from V(t), Q/A, thickness/interface/device response.
13. Mask 2 direct: 4–5 µm, 80 °C/30 min prebake, chlorobenzene 30 min, then pattern/develop/water rinse. Product/exposure/developer/order/lift-off local.
14. RIE direct: Plasma Technology parallel plate, CH4/5H2, 64 sccm total, 100 mTorr, 50 W, 60 s. Candidate 1:5 -> 10.6667/53.3333 sccm only as interpretive transfer.
15. RIE equivalence: self-bias/sheath proxy, sample T, chamber state, t_clear/t_sem, physical recession, sheet transport, d_conv/L_conv, LBIC/TLM/blocking response. `50 W != reactor equivalence`.
16. Metal: Cr/Au 30/270 nm direct; thermal evaporation first same-UWA method-family transfer; vacuum/rates/QCM/sample heating local.
17. TLM: nine ~300×300-µm contacts, gaps 50–400 µm in 50-µm increments; rho_c~9e-4 ohm cm² at 80 K.
18. P10: canonical 80 K, 10 V/cm; nominal ideal current ~1.79 mA; active V 0.05–0.40 V across 50–400-µm gaps.
19. Singulation: low-force CdZnTe-compatible wire-saw family first screen; qualify functional edge exclusion.
20. Package: compliant silicone-family first screen; package thermal response mandatory because ms-to-hundreds-ms poles can masquerade as detector dynamics.
21. Responsivity: 80 K, 10 V/cm, 1 kHz, stated 60° FOV; calibrated comparator/reference detector preferred; physical view geometry required.
22. Noise/D*: 1/f knee ~3 kHz; high-f g-r ASD ~24.5 nV/sqrtHz; use same-device/state noise at the declared D* frequency.
23. Dynamics: no direct RP-01 lifetime curve; de-embed source/optics/bias/preamp/cable/instrument/package and validate any one-pole interpretation.

## Known housekeeping discrepancy

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md` is numerically authoritative. One P30A section still shows older ppm-scale rounded mass fractions. Never let P30A's old rounded triplet override the calculation module or Draft 0.2. Fix in a later housekeeping pass if convenient.

## Immediate next work — Round 53

Continue toward the finished booklet, not another broad research loop:

1. compile the complete bibliography from the controlled source ledger;
2. create compact uncertainty/example-calculation appendix;
3. create publication-quality process-flow/LPE/anneal/RIE/radiometry figures;
4. extract operator checklists/travelers into appendices;
5. normalize symbols, units and index;
6. typeset the final professional PDF/booklet;
7. perform final editorial/visual adversarial review.

Targeted source recovery is allowed only where it materially improves a specific final-manuscript claim.