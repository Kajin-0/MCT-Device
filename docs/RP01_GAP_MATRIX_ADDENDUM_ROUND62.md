# RP-01 gap-matrix addendum — Round 62

**Date:** 2026-08-17 America/New_York  
**Basis:** full-text acquisition after the Round-61 publication artifact.

Round 62 changes a gap only where a recovered full text supplies a stronger consequential coordinate. Historical unknowns remain `OPEN` unless direct/same-lineage documentary evidence actually closes them.

## G62-01 — graphite cleaning transfer branch

Astles et al. provide primary HgCdTe-LPE evidence for POCO DFP-2 graphite that was acid etched, cleaned in boiling DI water for one week, baked at 500 °C, and used with scratch-free hand-polished mating surfaces and shimmed slider rails.

**Action:** historical RP-01 graphite grade/cleaning remains `OPEN`; this route becomes an explicit `PT` qualification branch. Round 61's warning against an *unsupported* acid clean is therefore refined, not discarded.

State: `PT-CLEANING-BRANCH-CLOSED / HISTORICAL-CLEANING-OPEN`.

## G62-02 — Hg compensation requires independent reservoir thermal state

Chiang/Chen demonstrate independently heated Hg reservoirs connected to slider growth regions by quartz two-arm covers; Astles uses separate HgTe delivery paths for solution wells and grown-layer cooldown.

**Action:** whenever a separately controlled reservoir is used, record `T_Hg(t)` separately from `T_growth(t)` plus source mass, exposed area, vapor path/volume and pre/post mass. Source mass alone is insufficient.

State: `HG-CHEMICAL-POTENTIAL-BOUNDARY-STRENGTHENED`.

## G62-03 — Hg-loss metrology can be executed

Astles measured solution mass change using dummy pre-growth thermal cycles and obtained ~0.3 mg/min Hg loss in that apparatus. Chiang reports <0.5-g reservoir consumption per thermal cycle.

**Action:** add dummy-cycle gravimetric Hg-loss qualification before detector-grade growth. Numerical rates remain PT examples, not local limits.

State: `HG-LOSS-METROLOGY-PT-CLOSED / LOCAL-LIMIT-OPEN`.

## G62-04 — wipe clearance and post-separation temperature

Radhakrishnan shows that insufficient wipe clearance can scratch the epilayer; non-smooth slide-out can produce transient meltback/re-growth texture; incomplete wipe leaves dendritic Te-rich residue. In that branch, exposed layers held above ~350 °C after slide-out developed Hg-evaporation points, whereas excessively cool placement could produce HgTe soot.

**Action:** record actual layer/graphite clearance, slide-out time/velocity/force, residual-droplet map, `T_layer(t)` after separation, and time to protected/cool state. The ~350 °C observation is PT branch evidence, not a universal limit.

State: `POST-SEPARATION-THERMAL-MECHANICAL-STATE-EXPLICIT`.

## G62-05 — executable `(111)B` CdZnTe defect screen

Everson et al. validate a B-face etch:

`6 cm³ 48% HF + 24 cm³ HNO3 + 150 cm³ lactic acid`, 2.5 min, room temperature, moderate agitation.

Reported pits are ~10:1 width:depth and correlate with dislocations. Their manufacturing example used `EPD <1×10^5 cm^-2` as a high-quality-area screen.

**Action:** add as a `PT` P29 screening branch. The example EPD threshold is not an RP-01 specification.

State: `B-FACE-EPD-METHOD-PT-CLOSED`.

## G62-06 — room-temperature versus growth-temperature lattice match

Tobin et al. show crosshatch/EPD minima near lattice match and a shift between room-temperature and growth-temperature matching. Tranchart directly supports `y≈0.04` CdZnTe for `x≈0.30` HgCdTe LPE.

**Action:** P29 should preserve both `delta_a_RT` and `delta_a_Tgrowth` or a justified thermal model equivalent.

State: `THERMAL-LATTICE-MATCH-COORDINATE-EXPLICIT`.

## G62-07 — anneal kinetic coordinate

Chandra/Schaake/Kinch show Hg-saturated skin depth approximately proportional to `sqrt(t)` and use `x_B²/t` as a rate coordinate dependent on composition, temperature and starting vacancy/excess-Te state. An x≈0.28 series gave ~1.1-eV activation energy.

**Action:** add `x_B²/t` as a PT response coordinate in P31/P23. Do not derive a universal dwell without starting-state and boundary data.

State: `ANNEAL-KINETIC-COORDINATE-STRENGTHENED`.

## G62-08 — anodization termination mode

Nemirovsky/Kidron used constant-current oxide growth followed by constant-voltage completion and reported improved dielectric/thickness control. Stahle supports the 0.3-mA/cm² KOH/EG/H2O branch; Ngoc/Nha show a 0.2–0.5-mA/cm² range and Pt counter-electrode variant.

**Action:** local anodization qualification should compare termination mode explicitly and record counter-electrode material. Historical electrode spacing/area ratio remains `OPEN`.

State: `ANODIZATION-TERMINATION-PT-CLOSED / CELL-GEOMETRY-OPEN`.

## G62-09 — same-lineage RIE physical state

Siliquini 1997 gives a complete UWA branch: Plasma Technology parallel plate, cathode 18 °C, H2 27 sccm, CH4 5 sccm, 410 mTorr, 0.4 W/cm², printed dc bias 180 V, 60 s, ~0.2-µm physical recession and ~1.5-µm electrical conversion.

**Action:** use as stronger `SL` evidence for P34's measured self-bias/thermal/gas/pressure state. Do not transfer 180 V to the RP-01 100-mTorr/50-W condition.

State: `RIE-SL-PHYSICAL-STATE-STRENGTHENED / RP01-SELF-BIAS-OPEN`.

## G62-10 — LBIC depth calibration

Siliquini used 1.047-µm CW excitation, ~3-µm spot, 2.5-µm scan step, ~5-mm remote-contact spacing and sequential 0.1% Br2/methanol depth stripping. Junction signature disappeared after ~1.6 µm removal.

**Action:** retain as an `SL` `d_conv` calibration lineage while preserving P37's distinct Musca-1998 80-K functional map.

State: `LBIC-DEPTH-CALIBRATION-SL-STRENGTHENED`.

## G62-11 — DC contact resistance does not close contact noise

Beck et al. show strong metal/contact-size-dependent HgCdTe 1/f noise even for electrically usable contacts.

**Action:** P09/P12 should include contact/no-contact or contact-geometry controls when excess 1/f noise appears; low `rho_c` alone is not a low-noise qualification.

State: `CONTACT-NOISE-INDEPENDENT-COORDINATE-EXPLICIT`.

## G62-12 — package thermal conductance becomes identifiable

Bartoli et al. 1976 separate HgCdTe-PC array recovery into short- and long-time bond-layer paths, with example conductance-per-area values ~3.2 and ~0.9 W cm^-2 K^-1.

**Action:** P33/P13 should fit a multi-path thermal response when supported by data and report conductance-per-area or equivalent network parameters. Values are PT, not RP-01/Dow-3110 constants.

State: `PACKAGE-THERMAL-PARAMETERIZATION-STRENGTHENED`.

## G62-13 — FTIR edge/thickness coupling

Gopal explicitly shows the 50%-transmission point depends on layer thickness; Chang demonstrates automated spatial x/thickness mapping with self-consistent optical fitting.

**Action:** Round-57 full-spectrum inversion remains controlling. Scalar edge coordinates remain descriptors/diagnostics, not thickness-independent composition truth.

State: `FTIR-MODEL-DISCIPLINE-STRENGTHENED`.

## Remaining highest-priority OPEN coordinates

- exact RP-01 LPE numerical boat/well/recess dimension stack;
- x≈0.30 melt density/well area/melt depth relation;
- historical Hg-source area/location/vapor geometry;
- historical graphite grade/roughness/clean;
- source-synthesis ampoule geometry/free volume/hot pressure;
- historical wet-etch hydrodynamics;
- historical anodization electrode geometry/solution drop;
- RP-01 RIE model/electrode geometry/RF frequency/self-bias/sample temperature/chamber seasoning;
- historical Cr/Au evaporator source/QCM/sample geometry;
- historical RP-01 package/readout/cryostat thermal state.

## Targeted documentary work still justified

Next acquisition should be narrow: Suh full slider-LPE paper; Shinohara full Hg-loss/wipe-off paper; Honeywell/Fermionics/UWA machine drawings/notebooks; TI anodization-cell records; UWA Plasma Technology run records; original RP-01 evaporator and cryostat/package records. Do not restart a broad literature sweep before these are exhausted.