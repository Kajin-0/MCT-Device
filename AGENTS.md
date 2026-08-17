# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 57  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce a source-traceable **empirical protocol manual** for HgCdTe photoconductor fabrication and characterization. The publication should read as a hard-number experimental methods monograph: materials/equipment, concrete reference recipe, numbered procedure, timing, expected result, analysis, troubleshooting, and value-level evidence. Do not revert to blank-field traveler formatting.

Canonical downstream historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_EMPIRICAL_PROTOCOL_METROLOGY_CLOSURE_ROUND57.md`.
2. `research/2026-08-16_checkpoint_after_empirical_protocol_round57.md`.
3. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND57.md` and `docs/SOURCE_LEDGER_ADDENDUM_ROUND57.md`.
4. `procedures/P37_LBIC_BLOCKING_CONTACT_FUNCTIONAL_QUALIFICATION.md`.
5. `analysis/ftir/ROUND57_FTIR_MODEL_SPECIFICATION.md`.
6. The detailed P01–P36A procedures/calculations and Round-56 records remain underlying evidence history.

## Current publication state

- `RP01-EMPIRICAL-PROTOCOL-ROUND57-REVIEW-CANDIDATE = YES`.
- `ROUND56-REVIEW-METROLOGY-BLOCKERS-CLOSED-IN-PUBLICATION = YES`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

Round 57 is a targeted metrology-closure revision of the hard-number protocol candidate. It is not a claim of end-to-end empirical validation.

## Evidence codes

- `RP` — direct Smith/RP-01 evidence;
- `SL` — same-lineage evidence;
- `PT` — primary transfer evidence;
- `DER` — derived quantity;
- `SYN` — explicit synthesized empirical starting choice.

`SYN` is concrete and falsifiable, but never historical identity or demonstrated process capability.

## Round-57 major closures

### Electric field: historical comparison and physics correction are separate

D1 has only two detector contacts, so a contact-free active-region voltage is not directly sensed.

Report both:

`E_Smith = V_terminal / L_gap`

for direct comparison to Smith’s applied-field convention, and

`E_bulk,est = [V_terminal - I(Rc1,est+Rc2,est)] / L_gap`

as a contact-corrected internal-field estimate.

Estimate each contact with the finite-contact TLM relation

`L_T = sqrt(rho_c/R_s)`

`R_c,est = sqrt(rho_c R_s)/W * coth(L_c/L_T)`.

For the nominal 100-µm gap, the canonical historical point remains `E_Smith=10 V/cm -> V_terminal=0.100 V`. With the RP-like screening values, this corresponds to `E_bulk,est≈6.83 V/cm`; a true bulk 10 V/cm estimate would require about `0.146 V` terminal. These are consistency calculations, not measured D1 Kelvin voltages.

### Absolute responsivity: one canonical underfilled radiant-power mode

Protocol 18 now freezes a spectral radiant-power substitution-comparator mode:

- D1 active gap: `100 × 300 µm`;
- target probe-beam diameter: `50 µm` 1/e²-equivalent near 4 µm;
- measured diameter must be `<=60 µm` at 3.0, 4.0, 4.4 and 5.0 µm;
- beam center within `±10 µm` of active-gap center;
- integrated measured beam power inside the active gap `>=99.0%`;
- reference/DUT image-plane mismatch `<=0.10 mm`;
- reference detector must have applicable spectral radiant-power responsivity calibration and fully capture the underfilled beam.

If the overlap/underfill condition is not met, the result may not be labeled the canonical absolute power responsivity; use a separately defined irradiance-mode method.

### Functional blocking: executable LBIC witness protocol

A new `W1` process-control witness is introduced. It shares parent material, anodic oxide and the same RIE chamber run with D1/T1, but is sacrificial/diagnostic so D1 passivation is not stripped.

Reference LBIC state:

- `80.0 K`;
- `1.047 µm` CW excitation;
- `400 mW/cm²`;
- nominal `10 µm` 1/e² spot;
- `700 × 700 µm` scan;
- `5 µm` pitch;
- zero external bias with virtual-ground current readout;
- five line scans at y=`−100, −50, 0, +50, +100 µm`.

A line passes only when both positive and negative lobes exceed `5 sigma_0` and their centers lie within `50 µm` of the nominal ±150-µm RIE boundaries. W1 passes at `>=4/5` lines plus a consistent 2-D bipolar map. TLM alone remains insufficient evidence of minority-carrier blocking.

## Secondary Round-57 repairs

- LPE matrix is named a **blocked 2² factorial validation screen**, not a response surface. Four corners + center in source batch A; independent 500 °C/5-min centers from source batches B and C. Optional axial points are a separate second stage if quadratic curvature is needed.
- Wet-mesa witness is co-patterned/geometrically representative, uses the same AZ4620 stack and orientation, and is co-immersed near D1 in the same bath.
- FTIR coordinates are defined: z=0 at HgCdTe/CdZnTe interface, z=d at free surface; `x(z)=x0+g(z/d−0.5)`, so `g=x_surface−x_interface`. Optional `s_x` is explicitly a manual Gaussian unresolved-composition parameter, not claimed as Hougen notation. Exact implementation/coefficient files and hashes must be archived with real data.
- T1 precision rho_c extraction uses a finite-width 2-D sheet/contact model rather than assuming conductor width equals 300-µm contact width. The long-contact expression is retained only as a consistency check.
- Singulation now distinguishes the source’s ambiguous `125-mm` saw wording from the actual cutting-wire diameter. Round-57 starting implementation: 100-µm stainless wire, 5.0-N tension, 20 m/min wire speed, 0.020 mm/min feed, 16-µm BN, 10-wt% BN/DI slurry, cuts parallel to mask axes.
- Packaging names Dow Corning 3110 RTV as the historical reference silicone family. A modern substitute is a separate recipe/equivalence problem.
- Noise uses 64 non-overlapping records only after stationarity/serial-correlation screening; fixed 995–1005-Hz ASD band; final band-estimator CI from a 10,000-resample record-level bootstrap rather than pretending adjacent Hann bins add independent chi-square DOF.
- Transient repetition now adapts with record length: `T_record>=10 tau_slowest`, `T_rep>=T_record+5 tau_slowest`, with explicit baseline-recovery verification.

## Stable geometry and direct downstream anchors

- `D1`: `900 × 500 µm`; two `300 × 300 µm` contacts; `100 µm` reference gap.
- `T1`: `5000 × 500 µm`; nine `300 × 300 µm` contacts; gaps `50,100,...,400 µm`.
- RP-comparison `A_Dstar = L_gap W_active = 100 µm × 300 µm = 3.00e-4 cm²` nominal.
- RIE direct controller state remains printed `CH4/5H2`, total `64 sccm`, `100 mTorr`, `50 W`, `60 s`; individual 10.7/53.3-sccm values are interpretive DER/SYN nominal setpoints.
- Cr/Au direct stack remains `30/270 nm`.
- Detector comparison state retains `80 K`, Smith terminal-field coordinate, stated `60° FOV`, and 1-kHz spectral modulation.
- `24.5 nV/sqrt(Hz)` is the high-frequency g-r level, not an automatic 1-kHz noise value.

## Upstream-material status

Protocols 1–7 remain explicitly a **COMPOSITE LITERATURE-DERIVED UPSTREAM MATERIAL HYPOTHESIS**. Smith purchased the starting Fermionics LPE material; the repository’s LPE/anneal route is a testable synthesis of separate primary lineages, not an RP-01 historical growth reconstruction.

## Round-57 artifact QA

Review artifacts:

- `RP01_HgCdTe_Empirical_Protocol_Manual_Round57.docx`
- `RP01_HgCdTe_Empirical_Protocol_Manual_Round57.pdf`

Final state:

- 41 pages;
- monochrome, text-native;
- no fillable PDF form fields;
- DOCX accessibility audit `0 high / 0 medium / 0 low`;
- all 41 DOCX-render pages visually inspected;
- final PDF: 41 letter-size pages, openable, unencrypted, not scanned, zero form fields;
- final PDF render is pixel-identical to the inspected LibreOffice render at the comparison DPI;
- final PDF independently rendered at 200 dpi.

SHA-256:

- DOCX `162f51b424acc2a5754bf11fb615f5077091a03f57b5b468e93be5c0181f3d1e`.
- PDF `92f5ec2a6a05af22f77add2ed10c5dded36162c79b27b7d1dc51392dce1aaca8`.

## Immediate next work

Do not reopen the Round-57 field, absolute-power, or LBIC definitions unless new primary evidence invalidates them. The next adversarial pass should focus on the remaining `SYN` process values and on whether any reference implementation combines incompatible process lineages. Preserve the recipe format and hard numbers; strengthen weak choices rather than reverting to blanks.