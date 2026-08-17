# Round 57 — targeted metrology closure of the empirical protocol manual

**Date:** 2026-08-16 America/New_York

## Trigger

The Round-56 manual was re-reviewed adversarially. The review confirmed that the Round-55 geometry, anodization and transient blockers were genuinely repaired, but identified three remaining major characterization/release-gate defects:

1. the definition of `10 V/cm` did not distinguish Smith’s historical terminal applied field from a contact-corrected internal field;
2. absolute spectral responsivity did not close the monochromator beam footprint/coupling to the 100×300-µm D1 active gap;
3. the research-gate table required LBIC/blocking evidence but no executable LBIC protocol existed.

Round 57 is a targeted closure, not a broad rewrite.

## 1. Dual electric-field convention

Round 57 freezes two separately reported quantities.

### Historical comparison coordinate

`E_Smith = V_terminal / L_gap`.

For the nominal D1 `L_gap=100 µm`, the canonical Smith-comparison point is:

`E_Smith=10.0 V/cm -> V_terminal=0.100 V`.

### Physics-oriented companion estimate

`E_bulk,est = [V_terminal - I(Rc1,est+Rc2,est)]/L_gap`.

The contact estimate is obtained from Protocol-14 `rho_c`, D1 `R_s`, contact width `W` and contact length `L_c`:

`L_T=sqrt(rho_c/R_s)`

`R_c,est=sqrt(rho_c R_s)/W * coth(L_c/L_T)`.

Because D1 lacks Kelvin voltage-sense contacts, `E_bulk,est` must never be relabeled a directly measured active-region voltage.

Using the RP-like screening values in the manual gives approximately:

- `R_bulk=55.87 ohm`;
- `R_c≈12.95 ohm/contact`;
- `R_terminal≈81.76 ohm`;
- at `V_terminal=0.100 V`, `E_bulk,est≈6.83 V/cm`;
- estimated bulk `10 V/cm` would require about `V_terminal=0.146 V`, corresponding to `E_Smith≈14.6 V/cm`.

The manual therefore preserves direct historical comparability without hiding contact-drop physics.

## 2. Absolute spectral radiant-power geometry

Protocol 18 now uses one canonical mode: **underfilled spectral radiant-power substitution comparison**.

Reference geometry:

- D1 active region: `100 × 300 µm`;
- target beam: `50 µm` 1/e²-equivalent diameter near `4 µm`;
- measured diameter `<=60 µm` at `3.0, 4.0, 4.4, 5.0 µm`;
- centering within `±10 µm` of active-gap center;
- integrated measured probe-beam power inside active rectangle `>=99.0%`;
- reference/DUT axial-plane mismatch `<=0.10 mm`;
- calibrated reference detector must fully capture the underfilled beam and have an applicable spectral radiant-power responsivity certificate/state.

Reference-before -> DUT -> reference-after substitution is retained at every wavelength step. FOV controls angular background/acceptance and is explicitly not used as a substitute for beam-footprint measurement.

If the underfilled/overlap criterion cannot be met, the result cannot be labeled the canonical power-responsivity measurement; use a separately defined irradiance mode.

## 3. LBIC blocking-contact functional qualification

Round 57 creates an explicit process-control witness `W1` and repository procedure `P37`.

Reference state:

- same parent material/anodic oxide and same RIE chamber run as D1/T1;
- central bare `300 × 300 µm` RIE-converted square, with remote metal collectors arranged so the diagnostic square remains optically accessible;
- `80.0 K`;
- `1.047 µm` CW source;
- nominal irradiance `400 mW/cm²`;
- nominal spot `10 µm` 1/e²-equivalent;
- `700 × 700 µm` scan;
- `5 µm` scan pitch;
- zero external bias; virtual-ground current readout.

Quantitative screening rule:

- line scans at y=`−100, −50, 0, +50, +100 µm`;
- estimate off-feature noise `sigma_0`;
- each accepted line must contain both positive and negative lobes with extrema `>=5 sigma_0` in magnitude;
- lobe centers must lie within `50 µm` of the nominal RIE-square boundaries at x=`±150 µm`;
- W1 passes when `>=4/5` lines pass and the 2-D current map shows the same boundary-associated sign reversal.

The default witness keeps oxide intact. A diluted-HCl oxide-strip comparison is allowed only on a duplicate sacrificial W1, never on D1.

This converts the prior statement “TLM alone is insufficient” into an executable functional gate.

## 4. LPE validation nomenclature and independence

The seven-run upstream test is now a **blocked 2² factorial validation screen**, not a classical response surface.

Batch A:

- 497 °C / 3 min;
- 497 °C / 7 min;
- 503 °C / 3 min;
- 503 °C / 7 min;
- 500 °C / 5 min center.

Independent source syntheses B and C each contribute a 500 °C / 5 min center run.

This distinguishes within-source repeatability from source-synthesis/process-block variability. The first-order model estimates T, time and T×time interaction plus center-vs-corner curvature indication. Optional axial points `(494,5)`, `(506,5)`, `(500,1)`, `(500,9)` are a separate second-stage design if a quadratic surface is needed.

## 5. Finite-width TLM

T1 is 500 µm wide while the metal pads are 300 µm wide. Precision `rho_c` extraction therefore no longer assumes a 1-D strip with conductor width equal to contact width.

Round 57 specifies a 2-D sheet/contact model:

- uncovered sheet: `div(G_s grad V)=0`, with `G_s=1/R_s`;
- under equipotential metal: normal current transfer `j_c=(V_m−V_s)/rho_c`;
- mesa sidewalls: insulating boundary;
- measured contact/gap geometry used directly;
- fit `R_s` and `rho_c` jointly or with independently constrained `R_s`;
- archive solver version, mesh and residuals.

The familiar long-contact `L_T=sqrt(rho_c/R_s)` relation remains a consistency check, not the primary precision inversion.

## 6. Other closure repairs

- Wet etch witness is co-patterned, same resist stack/orientation, and co-immersed close to D1 in the same bath.
- FTIR defines `z=0` interface and `z=d` free surface, with `x(z)=x0+g(z/d−0.5)`; optional `s_x` is explicitly a manual unresolved-composition parameter. Real analyses must archive exact coefficient/model files and hashes.
- Singulation separates the source’s `125-mm` saw wording from cutting-wire diameter and supplies a concrete SYN starting mechanics set: 100-µm stainless wire, 5.0 N, 20 m/min, 0.020 mm/min feed, 16-µm BN, 10 wt% slurry.
- Packaging names Dow Corning 3110 RTV as the historical reference adhesive family rather than an unspecified “compliant silicone.”
- Noise requires a stationarity/serial-correlation screen before assigning 128 per-bin DOF; fixed 995–1005-Hz band; record-level 10,000-resample bootstrap for the final band estimator.
- Transient repetition is adaptive: `T_record>=10 tau_slowest`; `T_rep>=T_record+5 tau_slowest`; baseline-recovery gate must pass before averaging.

## Artifact QA

Round-57 review artifacts:

- `RP01_HgCdTe_Empirical_Protocol_Manual_Round57.docx`
- `RP01_HgCdTe_Empirical_Protocol_Manual_Round57.pdf`

QA:

- 41 pages;
- monochrome;
- DOCX accessibility `0 high / 0 medium / 0 low`;
- all 41 DOCX render pages visually inspected;
- all table rows protected against cross-page splitting;
- final PDF: 41 letter-size pages, openable, unencrypted, text-native, no form fields;
- final PDF and the visually inspected LibreOffice PDF are pixel-identical at comparison DPI;
- final PDF separately rendered at 200 dpi.

SHA-256:

- DOCX `162f51b424acc2a5754bf11fb615f5077091a03f57b5b468e93be5c0181f3d1e`;
- PDF `92f5ec2a6a05af22f77add2ed10c5dded36162c79b27b7d1dc51392dce1aaca8`.

## Disposition

`RP01-EMPIRICAL-PROTOCOL-ROUND57-REVIEW-CANDIDATE = YES`.

The document remains a high-detail literature-derived research protocol candidate. It is not an empirically validated integrated fabrication process.