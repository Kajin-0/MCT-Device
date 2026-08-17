# Source-ledger addendum — Round 57 metrology closure

**Date:** 2026-08-16 America/New_York

## Governing rule

Round 57 preserves the distinction between source ancestry and combined-process validity. New hard-number metrology coordinates are explicit reference implementations or source-derived comparison conventions; they are not historical facts unless coded `RP`/`SL`/`PT` appropriately.

## Smith et al. 2001 — field convention

Round 57 records the historical comparison coordinate as:

`E_Smith=V_terminal/L_gap`.

Use: direct comparison to the published “applied electric field” convention associated with voltage bias between the planar contacts.

Transfer delta: Round 57 additionally reports a contact-corrected `E_bulk,est`; this is a derived companion coordinate, not a Smith measurement.

## Musca et al. / Smith LBIC lineage

Primary/same-UWA-lineage functional evidence:

- C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.
- Smith et al. 2001 discuss the associated 300×300-µm RIE regions and LBIC validation.

Round-57 anchors:

- `1.047 µm` CW excitation;
- approximately `400 mW/cm²`;
- `80 K`;
- `300 × 300 µm` RIE feature;
- bipolar LBIC spatial signature as functional n+/n evidence.

Transfer delta: the exact scan pitch, spot diameter and numerical acceptance statistic are not direct RP-01 values. Round 57 defines `10 µm` nominal spot, `5 µm` pitch and a 5-sigma/4-of-5-line screen as `SYN` research criteria on a sacrificial W1 witness.

Important passivation rule: Smith’s illustrated diagnostic included an oxide-stripped state using diluted HCl, but similar bipolar behavior was reported with/without oxide. Round 57 therefore keeps D1 intact and permits oxide stripping only on a duplicate sacrificial W1.

## NIST infrared comparator lineage

Authoritative metrology sources used for Protocol 18 include:

- A. L. Migdall and G. P. Eppeldauer, NIST SP 250-42, *Spectroradiometric Detector Measurements: Part III—Infrared Detectors* (1998), DOI `10.6028/NIST.SP.250-42`;
- NIST infrared spectral comparator facility publications describing both spectral radiant-power and irradiance response modes;
- G. P. Eppeldauer and M. Racz, InSb working-standard radiometer calibration work in which known-area apertures are underfilled by the monochromator output beam.

Round-57 use:

- canonical mode is spectral radiant-power comparison with an underfilled D1 active gap;
- beam profile/position is treated as part of the calibration state;
- reference and DUT must be measured in compatible image-plane geometry.

Transfer delta: NIST does not prescribe a 50/60-µm beam for D1. Those dimensions, ±10-µm centering, >=99% active-gap overlap and <=0.10-mm plane mismatch are Round-57 `SYN` engineering criteria sized to the 100-µm narrow dimension of the D1 active region.

## Finite-width TLM model

Direct RP-01 geometry remains nine 300×300-µm contacts with gaps 50–400 µm. Round 57 does not invent a new historical contact geometry.

The 500-µm T1 mesa width is a synthesized geometry that creates finite-width spreading because pads are 300 µm wide. The 2-D sheet/contact PDE is therefore a Round-57 analysis method, not a source claim. Archive the exact solver, mesh and boundary implementation with real reductions.

## CdZnTe singulation source wording

Primary source:

S. S. Yoo, G. Jennings, P. A. Montano, “CdZnTe Array Detectors for Synchrotron Radiation Applications,” *Journal of Synchrotron Radiation* 5, 1332–1336 (1998), DOI `10.1107/S0909049598007237`.

The source literally reports a `125 mm-diameter stainless-steel wire saw` and `16 µm BN slurry`, with roughly one hour per full cut. The 125-mm dimension is preserved as source wording but is not treated as the actual wire thickness.

Round-57 transfer implementation:

- actual cutting wire `100 µm` diameter stainless steel;
- tension `5.0 N`;
- wire speed `20 m/min`;
- feed `0.020 mm/min`;
- `16 µm` BN;
- `10 wt%` BN in DI water.

All of those mechanics beyond the 16-µm abrasive family are `SYN` starting choices requiring empirical cutting-damage qualification.

## FTIR parameter definitions

Hougen 1989 remains the preferred LPE transmission-model lineage. Round 57 adds publication-level definitions without claiming they are original Hougen symbols:

- z=0: HgCdTe/CdZnTe interface;
- z=d: HgCdTe free surface;
- `x(z)=x0+g(z/d−0.5)`;
- `g=x_surface−x_interface`;
- optional `s_x`: Gaussian unresolved composition-distribution standard deviation used only if justified by residual structure.

The symbol `s_x` is explicitly a Round-57 manual parameter, not attributed to Hougen. A real analysis is reproducible only if the exact code/model coefficient files, version and SHA-256 are stored with the dataset.

## Permanent restrictions reinforced

- `E_bulk,est` is not a directly sensed D1 bulk voltage.
- FOV is not beam diameter.
- absolute `V/W` requires a closed spatial-coupling definition.
- good TLM does not prove minority-carrier blocking.
- an LBIC research screen is not a production criterion until correlated with detector outcomes.
- non-overlapping PSD records are not automatically statistically independent.
- `SYN` values remain synthesized starting coordinates, not source facts or validated optima.