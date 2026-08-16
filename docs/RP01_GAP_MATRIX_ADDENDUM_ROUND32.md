# RP-01 gap matrix addendum — Round 32: FTIR / composition / thickness / cutoff

**Date:** 2026-08-16 America/New_York

| Gap | Current state after Round 32 | Evidence / control | Release path |
|---|---|---|---|
| Was FTIR used for RP-01 starting-material x? | `OPEN-HISTORICAL` | RP-01 states x≈0.30 but does not disclose method | Recover supplier/UWA material traveler, thesis, lab record or contemporaneous paper |
| Source of RP-01 9.5-µm thickness | `OPEN-HISTORICAL` | Direct thickness value only | Recover supplier certificate or UWA material characterization record |
| Exact RP-01 FTIR model/hardware | `OPEN-HISTORICAL` | No direct instrument statement | Archive/source recovery |
| FTIR source/beamsplitter/detector | `OPEN-HISTORICAL` | Strong transfer examples exist, not RP-01 | Use local qualified state until direct evidence recovered |
| FTIR path purge/vacuum | `OPEN-HISTORICAL` | Evacuated Bruker branch exists in primary HgCdTe work | Local qualification; do not assign historically |
| RP-01 spectral range/resolution/coadds | `OPEN-HISTORICAL` | None recovered | Local method qualification |
| Historical spatial mapping | `OPEN-HISTORICAL` | No RP-01 map recovered | P06A map register defines local coordinates |
| Mapping apparatus execution | `TRANSFER-CLOSED` | Chang 2005: Centaur µs + Nicolet 870, x-y stage ~1 µm, 100-µm mapping aperture | Validate equivalent local spatial footprint/stage registration |
| Aperture equals spatial resolution? | `REJECTED-INFERENCE` | Optical footprint/diffraction/stage state are additional variables | Measure projected footprint and registration uncertainty |
| LPE/CdZnTe FTIR composition + fringe thickness workflow | `TRANSFER-CLOSED` | Murthy 2009: Bruker IFS66v/S, 300 K, Te-rich horizontal-slider LPE/CdZnTe, fringe thickness | Reproduce locally with calibrated optical model |
| Full-spectrum LPE transmission model | `PRIMARY-LINEAGE-CLOSED` | Hougen 1989 | Freeze model/optical constants/software version after validation |
| 50% transmission composition metric | `PRIMARY-LINEAGE-CLOSED` | Gopal et al. 1992 | Keep as traceable QC descriptor, not sole composition estimator |
| Gopal 1992 thickness validity interval | `SOURCE-CONFLICT` | index renders 10–30 mm; author/profile summary gives µm-scale range | Recover/check primary PDF line before freezing interval |
| Hansen Eg(x,T) equation | `PRIMARY-CLOSED` | Hansen et al. 1982 | Use for declared consistency/mapping only |
| Hansen 0.013-eV standard error interpretation | `CLOSED` | global empirical fit error, not FTIR repeatability | Separate model systematic and measurement repeatability |
| x=.30 versus 4.4-µm RP-01 cutoff inconsistency | `DERIVED-CONSISTENCY-CLOSED` | at 80 K x=.30 -> 5.0879 µm bandgap-equivalent; 4.4 µm -> Hansen-equivalent x≈.3241 | Do not force equality; correlate material and device data empirically |
| Exact RP-01 detector cutoff convention | `OPEN-HISTORICAL` | paper states 4.4 µm without formal criterion | Recover raw Figure-6 data/method or define local detector-cutoff convention |
| FTIR optical thickness versus physical thickness | `LOCAL-QUAL-REQUIRED` | fringe/full-fit method is established | Cross-calibrate d_FTIR against profilometry/cross-section over expected thickness range |
| CdZnTe/interface influence on fringes | `TRANSFER-CLOSED` | primary work shows Hg in-diffusion/interface defects can reduce transmission/remove fringes | Treat fringe loss as material/interface diagnostic until excluded |
| Pre/post Hg-anneal optical shift means composition change? | `REJECTED-INFERENCE` | doping/defect/Fermi/surface/interface changes can alter edge | Match P05 Hall, P31 anneal genealogy and P06 spectral-model state |
| Final P06-to-P11 detector correlation | `OPEN-LOCAL` | conceptual relationship defined; no local devices measured | Link known P06 coordinates/material genealogy to P11 spectral response |

## Highest-value remaining historical retrieval

1. Supplier/UWA material certificate or thesis identifying how `x≈0.30` and `9.5 µm` were measured.
2. Direct FTIR/instrument details from the late-1990s UWA HgCdTe characterization lineage.
3. Formal definition/raw data behind RP-01 `4.4 µm` detector cutoff.
4. Primary PDF of Gopal et al. 1992 to close the thickness-range unit conflict.
5. Any same-wafer material map that can be tied to the Figure-3/5/6/7 device.

## Release implication

P06 remains the canonical operator SOP. P06A is the empirical apparatus/model/cutoff transfer layer. A future material lot is not released by a single inferred x; release must preserve the joint state:

`{raw spectrum, defined edge metric, x_opt/model, d_FTIR, d_physical calibration, spatial coordinate, substrate/interface state, anneal genealogy}`.
