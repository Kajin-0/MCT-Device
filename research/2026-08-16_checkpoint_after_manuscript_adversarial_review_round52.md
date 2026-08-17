# Checkpoint after integrated-manuscript adversarial review — Round 52

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Purpose of Round 52

Perform an adversarial scientific/procedural review of the integrated Draft 0.1 manuscript against the controlled procedure and calculation set, then incorporate the important corrections into Draft 0.2. This round deliberately avoided another infrastructure/security branch.

## Primary result

The reference process architecture survived review. No major physical-process reversal was required.

The review instead found seven important manuscript-control defects:

1. title overclaimed reproducibility;
2. reference qualification centers could be read as executable setpoints before local instantiation;
3. P36/P36A commissioning architecture was omitted from the integrated crosswalk;
4. RIE `2.0e15 cm^-3` converted density was not explicit enough about its conversion-depth coupling;
5. stated 60° FOV needed explicit full-angle/half-angle uncertainty;
6. D* area wording incorrectly pushed detector normalization area and optical power geometry toward physical identity;
7. same-device identity of RP-01 Figures 3/5/6/7 was not used strongly enough in the D* closure rule.

All seven are corrected in Draft 0.2.

## Draft 0.2 key changes

### Claim discipline

Title changed to:

`Source-Traceable Qualification Fabrication and Characterization of an x≈0.30 HgCdTe Photoconductor`.

`Reproducible` is reserved for a later demonstrated local process under P17.

### Irreversible-step preflight

New permanent rule:

`REF-CENTER != EXECUTABLE-LOCAL-SETPOINT`.

Before an irreversible step, the traveler must close all required local material, reagent, geometry, tool, setpoint, calibration, endpoint, genealogy, P36/P36A and EH&S fields. `TBD`, `appropriate`, undefined `%`, and generic `typical` instructions fail preflight.

### P36/P36A integration

The manuscript now explicitly invokes:

- P36 for laboratory subsystem IQ/OQ/surrogate-PQ/HgCdTe residual acceptance;
- P36A for mass, dimensional, lithography, wet-chemistry and anodization acceptance.

### RIE converted state

Permanent controlled interpretation:

`n_conv = N_s/d_conv`

only after `d_conv` is independently justified.

Blocking-contact state vector is at least:

`{R_s,N_s,mu_H,d_conv,L_conv,d_etch,rho_c,blocking_response}`.

The RP-01 `2.0e15 cm^-3` result is direct but depth-coupled because it was averaged over converted thickness.

### Radiometric FOV

Historical state remains `stated 60° FOV`.

A 60° full cone / 30° half-angle is retained only as a derived consistency interpretation that agrees with the published background-photon-flux scale. New work must record physical aperture/view-factor geometry and the angular convention.

### D* area convention

Draft 0.2 distinguishes:

- `A_Dstar` — detector normalization area;
- optical beam/aperture/irradiance geometry used for `P_inc`.

They need not be physically identical. Shared area coordinates require covariance.

`gamma_A = partial ln(P_inc)/partial ln(A_Dstar)`

and:

`S_Dstar,A = 0.5 - gamma_A`.

### Same-device D* state

P12C closes that RP-01 Figures 3/5/6/7 are the same representative device. New D* closure therefore locks:

`{device,contact pair,gap,width,T,E,package,FOV/background,loading,frequency convention}`

unless an explicit measured correction is applied.

### Noise warning retained

`24.5 nV/sqrt(Hz)` remains the high-frequency g-r level, not an allowed automatic substitution for the 1-kHz noise because the reported knee is about 3 kHz.

## Numerical review

No substantive regression found in:

- authoritative LPE mass fractions;
- 250 °C / 1 h anneal reference center;
- wet-mesa transfer rate/anisotropy warning;
- 0.1 M KOH / ~0.3 mA cm^-2 anodization reference architecture;
- 64 sccm / 100 mTorr / 50 W / 60 s RIE direct controller state;
- Cr/Au 30/270 nm;
- 10 V/cm active-voltage table;
- NEP/D* equations;
- PSD-level electronics subtraction;
- one-pole frequency/time relation under its stated validation conditions.

## Known internal housekeeping issue

P30A still contains an older ppm-scale rounded LPE mass-fraction triplet in one section. The authoritative calculation is:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`;

with Hg=200.59, Cd=112.414, Te=127.60 g/mol.

Draft 0.2 uses the authoritative values. A later housekeeping pass may repair P30A wording; it does not block the manuscript because the numerical authority is explicit.

## New manuscript maturity state

`RP01-MANUSCRIPT-ADVERSARIAL-REVIEW-PASSED = YES`.

This is a document state only.

Physical states remain unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

## Next work

Round 53 should continue directly toward the finished booklet rather than reopen broad process research. Recommended priority:

1. build the full bibliography from the controlled source ledger;
2. create a compact uncertainty/example-calculation appendix;
3. create publication-quality process schematics and flow figures;
4. extract operator checklists/travelers into appendices;
5. normalize symbols/units/index;
6. typeset the professional PDF/booklet and perform final editorial/visual review.

Targeted source recovery is justified only when it materially resolves a claim in the final manual.