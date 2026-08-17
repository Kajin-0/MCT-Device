# RP-01 gap-matrix addendum — Round 63

**Date:** 2026-08-17 America/New_York  
**Basis:** full-text recovery of Suh 1992 and Shinohara 1994 after Round 62.

Round 63 affects only the upstream Te-rich horizontal-slider LPE evidence state. It does not change RP-01 downstream fabrication evidence or Round-57 metrology definitions.

## G63-01 — independent near-x≈0.30 Te-rich liquid branch

Suh reports nominal Hg0.7Cd0.3Te growth from a Te-rich solution with elemental mole fractions approximately `Hg0.158 Cd0.012 Te0.830`, corresponding to `xL≈0.0706, yL=0.830` in the Round-61 notation, with a reported growth-temperature range of about 500–489 °C.

**Action:** preserve the Honeywell `xL=.082/yL=.810/TL=507 °C -> xS≈.29` center, but add Suh as an independent PT empirical neighborhood. Do not average the compositions.

State: `X030-INDEPENDENT-LIQUID-BRANCH-PT-CLOSED`.

## G63-02 — x≈0.30 source synthesis has an independent 700 °C branch

Suh compounds growth solutions in vacuum-sealed quartz at `700 °C / 12 h`, water quenches them, and uses about `2.5 g` solution per run. Round 61/62 already had a `700 °C / 8 h` Radhakrishnan branch.

**Action:** 700 °C becomes independently supported across two Te-rich slider-LPE branches, one explicitly x≈0.30. Dwell remains apparatus/source-preparation qualification, not a historical RP-01 constant.

State: `SYNTHESIS-TEMPERATURE-PT-STRENGTHENED / DWELL-HISTORICAL-OPEN`.

## G63-03 — Hg compensation geometry becomes a measured vapor conductance

Suh places a conical graphite button between the HgTe and solution vapor spaces. For the x≈0.30 branch, a central hole of about `2 mm` diameter produced near-zero net solution-weight change in that apparatus. The model scales influx approximately with `d_hole^2/t_button`, while external Hg loss depends separately on slider/body gap.

**Action:** add button/throttle geometry and solution-mass trajectory as first-class PT coordinates. Local objective is `Delta m_solution≈0`, not literal reproduction of the 2-mm hole.

State: `HG-VAPOR-CONDUCTANCE-GEOMETRY-PT-CLOSED / RP01-GEOMETRY-OPEN`.

## G63-04 — numerical wipe clearance exists as a relevant PT branch

Shinohara's x≈0.31 CZT4 equilibrium-cooling branch achieved complete wiping across 10×10 mm with about `20 µm` slider-bottom/substrate-surface clearance. A second branch used `20–25 µm`. The authors identify clearance variation below about `5 µm` as important for large-area specular wiping.

**Action:** revise the Round-61 statement that no relevant quantitative clearance is available. Historical RP-01 clearance remains OPEN; a 20-µm PT branch now exists and can seed local mechanics qualification.

State: `WIPE-CLEARANCE-PT-BRANCH-CLOSED / HISTORICAL-CLEARANCE-OPEN`.

## G63-05 — source mass must be treated as a trajectory

Shinohara explicitly weighs source and reservoir materials and shows that the source can first gain Hg from the reservoir and later lose Hg. The growth starts after approximately 130 min in that branch.

**Action:** distinguish `m_source(load)`, `m_source(growth-start)` and `m_source(post-growth)` conceptually. Where direct in-situ weighing is impossible, use sacrificial time-point/dummy cycles to establish the trajectory.

State: `SOURCE-MASS-TRAJECTORY-EXPLICIT`.

## G63-06 — growth-window Hg loss is large enough to bias composition

Shinohara reports approximately `0.014 g` source-liquid loss during a 30-min growth period despite Hg-vapor compensation, roughly 0.7% on the ~2-g source scale.

**Action:** require `Delta m_source` and `Delta m_Hg-source` to be correlated with FTIR composition. Do not interpret x drift as a temperature-only effect until mass balance is closed.

State: `HG-LOSS-COMPOSITION-COUPLING-STRENGTHENED`.

## G63-07 — wipe quality and thickness are coupled responses

Shinohara finds:

- equilibrium cooling from melting point: ~2–4 µm layers and best wiping;
- 15-K supercooling/step cooling: ~30–41 µm layers.

The complete-wipe x≈0.31 CZT4 branch at 0.15 K/min produced ~4 µm, not the RP-01 ~9.5-µm target.

**Action:** optimize `DeltaT_contact`, cooling rate, contact time, clearance and wipe geometry jointly. Do not optimize wipe in a thickness-blind experiment.

State: `WIPE-THICKNESS-COUPLING-EXPLICIT`.

## G63-08 — near-liquidus x≈0.30 growth branch

Suh homogenizes about 20 °C above liquidus, then cools and contacts at approximately 1 °C below liquidus, continuing growth about 30 min at ~0.3 °C/min.

**Action:** retain as a PT branch validating P03E's use of measured liquidus and contact offset. It does not replace the Round-61 497/500/503 °C SYN factorial design.

State: `NEAR-LIQUIDUS-CONTACT-PT-STRENGTHENED`.

## G63-09 — composition-control capability benchmark

Suh's x≈0.30 branch reports mean x≈0.304, run-to-run sigma≈0.003 and within-layer variation about ±0.002; interface width is about 2–3 µm.

**Action:** preserve as a PT benchmark demonstrating what Hg-loss-controlled slider LPE achieved in a published apparatus. Do not convert it to an RP-01 or local acceptance specification.

State: `X030-REPEATABILITY-BENCHMARK-PT-ADDED`.

## Remaining highest-priority LPE OPEN coordinates

- exact RP-01/Fermionics machine drawing and complete numerical dimension stack;
- historical slider/base/epilayer clearance;
- historical Hg-vapor throttle/button geometry, if any;
- growth-well area/depth and actual melt depth;
- historical Hg-source area/location/vapor geometry;
- exact historical graphite grade/finish/clean;
- source-synthesis ampoule geometry/free volume/hot pressure;
- historical source-synthesis route/dwell/mixing;
- historical growth contact temperature/time/cooling trajectory;
- wipe hardware generation and actuation dynamics;
- source reuse/depletion history.

## Search disposition

The two highest-value paper targets identified at the end of Round 62 are now recovered. Further work should prioritize archival apparatus records and local instrumented qualification, not another broad literature sweep.