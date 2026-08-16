# AGENTS.md — MCT-Device continuity record

## Mission

Develop an extremely detailed, source-traceable procedure for fabricating and characterizing HgCdTe photodetectors. The endpoint is a booklet/manual plus process travelers that specify measurements, metrics, times, equipment, machinery, tolerances, calibration requirements, acceptance criteria, failure modes, and provenance sufficiently well that a competent researcher can reproduce the process without relying on undocumented tribal knowledge.

## Non-negotiable research rules

1. **Do not fabricate missing numbers.** A blank or `[OPEN]`/`[QUAL]` requirement is preferable to a plausible but untraceable setpoint.
2. **Do not splice process families casually.** HgCdTe composition, substrate orientation, melt chemistry, Hg chemical potential, passivation, etch history, doping, and thermal history are coupled.
3. **Primary literature first.** Books/reviews are excellent maps, but process-critical numbers should be traced to original experimental sources wherever possible.
4. **Separate published observation, derived physics, apparatus calibration, and proposed qualification experiments.**
5. **Preserve negative results and rejected branches.** Record why an apparently useful process was not adopted.
6. **Every critical process step needs metrology.** A setpoint without measurement confirming the resulting material/device state is insufficient.
7. **Every process module needs a gate.** State what must be true before the sample advances.
8. **Safety is part of reproducibility.** Hg, Cd-containing material, Br2/HBr/KOH chemistry, vacuum systems, high temperatures, methane/hydrogen plasmas, cryogens, and electrical systems require institution-approved EH&S procedures and apparatus-specific risk assessment. Repository procedures are scientific process specifications, not operating authorization.

## Reference process RP-01

The first downstream reference process is:

> E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, and L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001). DOI `10.1088/0268-1242/16/6/306`.

RP-01 was selected because actual n-type HgCdTe photoconductors were fabricated and measured and the paper gives unusually strong downstream process anchors.

### RP-01 material state

- LPE-grown HgCdTe on insulating CdZnTe `[P]`.
- x≈0.30, n-type `[P]`.
- carrier density 9.8×10^14 cm^-3 `[P]`.
- electron mobility 4.0×10^4 cm² V^-1 s^-1 `[P]`.
- experimental device-layer thickness 9.5 µm `[P]`.

### RP-01 RIE/contact anchors

- parallel-plate Plasma Technology reactor `[P]`.
- CH4/5H2 gas mixture `[P]`.
- total flow 64 sccm `[P]`.
- chamber pressure 100 mTorr `[P]`.
- RF power 50 W `[P]`.
- process time 1 min `[P]`.
- RIE-converted carrier density 2.0×10^15 cm^-3 `[P]`.
- RIE-converted mobility 3.3×10^4 cm² V^-1 s^-1 `[P]`.
- older same-lineage work reports deep RIE-induced conversion; do not equate those depth values with a directly measured RP-01 depth without source matching.

### RP-01 lithography/passivation/metallization anchors

- photoresist thickness ~4–5 µm `[P]`.
- prebake 80 °C, 30 min `[P]`.
- chlorobenzene soak 30 min `[P]`.
- anodic oxide 800 Å `[P]`.
- Cr 300 Å `[P]`.
- Au 2700 Å `[P]`.
- resist identity, exposure dose, developer, deposition rate/base pressure, lift-off solvent, and RIE-to-metal transfer delay remain open.

### RP-01 TLM anchors

- nine contacts `[P]`.
- each 300 µm × 300 µm `[P]`.
- first spacing 50 µm, successive spacing increment 50 µm `[P]`.
- 80 K specific contact resistivity 9×10^-4 Ω cm² `[P]`.

### RP-01 detector-characterization anchors

- Optronics Laboratories Spectral Response Measurement System `[P]`.
- detector temperature 80 K `[P]`.
- field of view 60° `[P]`.
- chopping frequency 1 kHz `[P]`.
- representative noise field 10 V/cm `[P]`.
- HP35665A spectrum analyzer with low-noise preamplifier `[P]`.
- 1/f knee ~3 kHz `[P]`.
- g-r noise ~24.5 nV/√Hz `[P]`.
- measured spectral cutoff 4.4 µm `[P]`.
- BLIP D* 2.0×10^11 cm Hz^1/2 W^-1 at 4 µm `[P]`.
- reported 300 K/60° background photon flux 1.0×10^15 cm^-2 s^-1 `[P]`.
- reported quantum efficiency 70% `[P]`.

## Current process architecture

The working RP-01 process architecture is now:

1. qualify semi-insulating CdZnTe substrate;
2. grow x≈0.30 HgCdTe by Te-rich horizontal-slider LPE;
3. qualify post-growth Hg-overpressure treatment to reach the RP-01 n-type electrical state;
4. wet-chemical mesa isolation;
5. native anodic-oxide passivation;
6. contact-window lithography;
7. localized CH4/H2 RIE under contact regions only;
8. Cr/Au metallization and lift-off;
9. TLM/contact QC;
10. packaging/interconnection;
11. electrical, spectral, noise, temporal and absolute-performance characterization.

This is a controlled architecture, not yet a released manufacturing traveler.

## Mesa-isolation decision

Same-UWA-lineage detector work closes the architectural choice: retain **wet mesa isolation** and use RIE only locally where its n+ conversion is intentional.

Key source:

E. P. G. Smith et al., “H2-based dry plasma etching for mesa structuring of HgCdTe,” *J. Electron. Mater.* 29, 853–858 (2000), DOI `10.1007/s11664-000-0237-7`.

The x≈0.31 n-HgCdTe detector comparison showed much higher D* for wet bromine/HBr mesa processing than for blanket H2/CH4 dry-mesa processing. Do not “modernize” RP-01 into an all-dry process without defining a new reference process.

### Wet-mesa quantitative transfer source

V. Srivastav et al., *J. Electron. Mater.* 34, 1440–1445 (2005), DOI `10.1007/s11664-005-0203-5`, reports on x=0.28 HgCdTe:

- selected 2% Br2 in 3:1 EG:HBr;
- 21 °C mean vertical etch rate 2.78 µm/min;
- ~±26% rate variation;
- anisotropy ~0.63 ±11%;
- best reported RMS roughness around 2 nm;
- process temperatures 5–50 °C;
- rate approximately doubles per +10 °C;
- lower temperature improves dimensional control.

**Release blocker:** accessible primary text does not unambiguously define the concentration basis of “2% Br2.” Do not invent it.

Controlled module: `procedures/P01_WET_MESA_QUALIFICATION.md`.

## Passivation branch

RP-01 directly closes the target film as 800 Å native anodic oxide but not its formation recipe.

A strong historical qualification candidate from a Texas Instruments primary process disclosure uses:

- 0.1 M KOH;
- 90% ethylene glycol / 10% deionized water;
- constant current ~0.3 mA/cm²;
- formation endpoint ~15 V;
- ~2 min;
- resulting oxide ~800 Å.

Independent primary HgCdTe work supports the same electrolyte family and a 0.2–0.5 mA/cm² constant-current regime.

**Do not call this the exact UWA recipe.** It remains a transfer/qualification candidate until the UWA lineage is recovered or local x≈0.30 qualification closes thickness, electrical/interface behavior, and compatibility with the contact-window RIE.

Controlled module: `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`.

## Upstream LPE branch — major closure achieved 2026-08-15

### Corrected key source

DOI `10.1016/0022-0248(82)90468-7` is:

J. L. Schmit, R. J. Hager, and R. A. Wood, “Liquid phase epitaxy of Hg1−xCdxTe,” *Journal of Crystal Growth* 56, 485–489 (1982).

It was previously mislabeled as “Tung et al.” Correct that attribution everywhere. The paper explicitly reports Te-rich atmospheric-pressure horizontal-slider growth of solid x=0.2, 0.3, and 0.4 material.

### Composition-matched tie line

J. E. Bowers and J. L. Schmit, U.S. Patent 4,317,689 (1982), in the same Honeywell/Schmit Te-rich slider lineage, provides the strongest explicit composition anchor found so far:

- liquid metal Cd fraction `xL=0.082` `[P]`;
- liquid Te fraction `yL=0.810` `[P]`;
- liquidus `TL=507 °C` `[P]`;
- grown solid `xS=0.29` `[P]`;
- `k=xS/xL=3.54` `[P]`.

For `(Hg_(1−xL)Cd_xL)_(1−yL)Te_yL`, derived elemental mole fractions are:

- Hg 0.17442 `[D]`;
- Cd 0.01558 `[D]`;
- Te 0.81000 `[D]`.

Derived mass fractions are:

- Hg 0.249738 `[D]`;
- Cd 0.012502 `[D]`;
- Te 0.737760 `[D]`.

For total charge mass `M`, use `mHg=0.249738M`, `mCd=0.012502M`, `mTe=0.737760M`; **M is still OPEN/CAL** because melt depth and solute inventory depend on the actual boat geometry.

### LPE apparatus/process architecture now supported

Bowers–Schmit demonstrates:

- covered graphite horizontal-slider boat;
- separate HgTe or HgTe+Te Hg-vapor source;
- Hg-distribution groove/moat geometry;
- quartz furnace tube;
- nitrogen purge before heating;
- flowing H2 during processing;
- heating the charge above liquidus before growth below liquidus;
- operation near 500 °C for the relevant process family.

For the xS=0.29 tie line, growth near 500 °C corresponds to a derived center-point supercooling `ΔT≈7 °C`; treat this as a qualification center point, not a released setpoint.

### Radhakrishnan source — engineering module, not composition module

J. K. Radhakrishnan, S. Sitharaman, S. C. Gupta, *J. Crystal Growth* 252, 79–86 (2003), DOI `10.1016/S0022-0248(02)02530-7`, gives useful apparatus/process detail:

- high-purity/high-density graphite slider;
- 15×15×1 mm CdZnTe recess;
- quartz tube with stainless-steel end flanges;
- gas-flow/push-pull/thermocouple ports;
- 6N Cd/Te/Hg;
- 700 °C for 8 h evacuated-ampoule charge synthesis;
- ~4.8 g per growth run;
- 3 g HgTe compensation;
- in-situ meltback;
- improved wipe-off geometry.

Its typical composition branch is around x≈0.20. **Never combine its 4.8-g charge or 3-g HgTe number with the Bowers–Schmit xL=0.082/yL=0.810 formulation and present that as a published x≈0.30 recipe.**

### Substrate branch

Tranchart et al., *J. Crystal Growth* 72, 468–473 (1985), support CdZnTe around y≈0.04 for x≈0.30 Te-rich LPE material and detector arrays. Separate primary lattice-match work gives an optimum near 2.9 mol% ZnTe for Hg0.7Cd0.3Te.

Therefore:

- CdZnTe substrate family is closed;
- exact production Zn fraction is not a universal number;
- release the substrate specification from measured lattice mismatch, orientation and material quality.

### Electrical-state problem

As-grown Te-rich LPE material may be p-type because of Hg vacancies. Nagahama et al. report x≈0.17–0.30 material and Hg-overpressure annealing from 250–400 °C; 250–300 °C produced well-behaved n-type material without the apparent composition change seen at 400 °C.

This makes low-temperature Hg-overpressure treatment the leading bridge to the RP-01 target n≈9.8×10^14 cm^-3, but anneal time, Hg chemical-potential control, geometry, cooldown and final x≈0.30 n/µ remain open.

Controlled upstream module: `procedures/P03_LPE_X030_QUALIFICATION.md`.

Research reconciliation record: `research/2026-08-15_lpe_process_reconciliation.md`.

## Current controlled qualification modules

1. `procedures/P01_WET_MESA_QUALIFICATION.md`
2. `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`
3. `procedures/P03_LPE_X030_QUALIFICATION.md`

All three are qualification modules, **not released production travelers**.

## Highest-priority open variables

### Upstream material

- full Schmit–Hager–Wood 1982 experimental details;
- exact CdZnTe orientation/miscut and measured mismatch target;
- substrate cleaning/polishing process;
- selected boat dimensions/well volume and total charge mass;
- exact x≈0.30 charge synthesis/homogenization protocol;
- N2 purge/H2 flow/purity criteria;
- equilibrium hold criterion;
- exact supercooling/cooling trajectory;
- growth-time/thickness calibration to 9.5 µm;
- slider velocity/wipe-off mechanics;
- post-growth Hg anneal time/source/cooldown required to hit n≈9.8×10^14 cm^-3 and µ≈4.0×10^4 cm²/V·s.

### Downstream device

- exact RP-01 active detector dimensions;
- Mask-1 resist/exposure/develop process;
- Br2 concentration basis and post-etch rinse;
- exact UWA 800 Å anodization recipe or complete local qualification of the historical candidate;
- Mask-2 resist identity/exposure/develop;
- RIE electrode geometry, self-bias, sample temperature and conversion depth;
- Cr/Au deposition method/base pressure/rates and RIE-to-metal delay;
- lift-off process;
- die attach and wire-bond metallurgy;
- full responsivity/noise calibration chain including preamplifier, RBW/ENBW, averaging and electronics-floor subtraction.

## Most natural next work

1. Recover the full Schmit–Hager–Wood x≈0.30 LPE experimental section or equivalent same-lineage primary detail.
2. Recover full Tranchart CdZnTe substrate preparation/growth details.
3. Recover complete Nagahama anneal metadata and especially time, Hg source/pressure arrangement and cooldown.
4. Audit the Honeywell wipe-off/slider-termination patent lineage for translation geometry/speed and melt-removal control.
5. Build `P04_HG_ANNEAL_QUALIFICATION.md` once the anneal parameters are sufficiently closed.
6. Continue RIE-depth, lithography, metallization and measurement-chain closure in parallel.
7. Maintain dated research logs for accepted, rejected and unresolved branches.
