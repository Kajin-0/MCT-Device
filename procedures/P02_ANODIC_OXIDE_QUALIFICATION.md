# P02 — HgCdTe native anodic-oxide qualification

**Status:** `QUALIFICATION-CANDIDATE` — NOT yet released as the exact RP-01 anodization recipe.

**Purpose:** Establish and qualify an anodically grown native oxide on n-type x≈0.30 HgCdTe with a target thickness of approximately 800 Å (80 nm), matching the passivation thickness used in RP-01.

## 1. RP-01 requirement

Smith et al. 2001 explicitly report experimental devices passivated with **800 Å of anodic oxide** before CH4/H2 RIE contact-window opening and Cr/Au metallization. `[P-RP01]`

The paper also states that anodic oxide is a standard HgCdTe photoconductor passivant and discusses positive fixed charge that promotes n-type surface accumulation and reduced surface recombination/1/f noise. `[P-RP01]`

However, RP-01 does not disclose the electrolyte composition, anodization current density, formation voltage, time, electrode geometry, or post-anodization rinse. Those variables therefore require an independently sourced and experimentally qualified process.

## 2. Strongest current process candidate

A Texas Instruments primary process disclosure for HgCdTe photoconductive material reports a preferred anodization condition using:

- electrolyte: **0.1 M KOH** in **90% ethylene glycol / 10% deionized water**; `[P-TI]`
- control mode: **constant current**; `[P-TI]`
- current density: approximately **0.3 mA/cm²**; `[P-TI]`
- formation voltage endpoint: approximately **15 V**; `[P-TI]`
- reported formation time: approximately **2 min**; `[P-TI]`
- resulting film: approximately **800 Å**, visually described as uniform deep blue. `[P-TI]`

The same disclosure reports that oxide thickness was verified using stylus profilometry on delineated oxide structures and optical interference methods. `[P-TI]`

This thickness is numerically identical to RP-01's reported 800 Å passivation thickness, making the process a strong candidate but **not proof that UWA used the identical anodization conditions**.

## 3. Independent experimental support

A later primary experimental study of native oxides on x=0.20 HgCdTe reports:

- standard electrolyte: **0.1 M KOH in 90% ethylene glycol / 10% H2O**; `[P-CV]`
- room-temperature anodization; `[P-CV]`
- constant current density range: **0.2–0.5 mA/cm²**; `[P-CV]`
- example native oxide thickness: **70 nm** on n-type material. `[P-CV]`

This independently supports the electrolyte family and constant-current regime, although the alloy composition and exact target thickness differ from RP-01.

## 4. Why constant-current control is preferred for qualification

The TI disclosure reports reproducible voltage rise as oxide impedance increases during constant-current anodization. `[P-TI]`

Therefore the complete voltage-versus-time trace is a valuable process signature and must be logged for every qualification run.

A simple timer-only process is not sufficient for release because oxide growth depends on:

- actual exposed HgCdTe area;
- electrolyte composition and temperature;
- electrode geometry;
- current-density accuracy;
- surface preparation;
- material composition and electrical state.

## 5. Material state for transfer qualification

Target material:

- n-type HgCdTe;
- x≈0.30;
- epilayer thickness nominally 9.5 µm;
- target incoming carrier density 9.8×10^14 cm^-3;
- target incoming electron mobility 4.0×10^4 cm² V^-1 s^-1.

All qualification coupons should be taken from material representative of the RP-01 wafer or a deliberately matched process-control wafer.

## 6. Candidate electrolyte specification

Candidate electrolyte:

\[
0.1~\mathrm{mol/L~KOH}
\]

in a solvent mixture consisting of:

\[
90\%~\text{ethylene glycol} + 10\%~\text{deionized water}.
\]

`[P-TI/P-CV]`

### Variables still requiring explicit release definition

- whether the 90:10 solvent proportion is prepared by volume, mass, or another convention `[OPEN]`;
- KOH purity grade `[OPEN]`;
- ethylene-glycol purity/water content `[OPEN]`;
- DI-water resistivity specification `[OPEN]`;
- electrolyte aging/storage limit `[OPEN]`;
- preparation order and exotherm control `[OPEN/EH&S]`;
- bath volume per exposed HgCdTe area `[OPEN/CAL]`.

The primary sources establish the chemical family and molarity but not every manufacturing-control variable required for exact replication.

## 7. Candidate electrical setpoints

Initial qualification reference:

- control mode: constant current `[P-TI]`;
- current density: **0.30 mA/cm²** `[P-TI]`;
- formation voltage target: **~15 V** `[P-TI]`;
- approximate expected time to 800 Å: **~2 min** `[P-TI]`.

These are **qualification targets, not production acceptance limits**.

The current supplied to a particular exposed area is:

\[
I = J A_{\rm exposed}.
\]

Thus the exposed semiconductor area must be measured or defined by fixture geometry before anodization. `[D]`

Example only: an exposed area of 1.00 cm² at 0.30 mA/cm² requires 0.30 mA total current. `[D]`

## 8. Required anodization apparatus features

The qualification setup must provide:

1. constant-current regulation with recorded calibration;
2. simultaneous voltage measurement;
3. continuous or sufficiently sampled voltage-time logging;
4. known electrically exposed HgCdTe area;
5. reproducible sample immersion depth and orientation;
6. reproducible counter-electrode material, area, separation, and orientation `[OPEN]`;
7. bath-temperature measurement;
8. chemically compatible vessel and fixture;
9. electrical isolation of non-process surfaces where required;
10. current compliance sufficient to allow the formation voltage to rise through the expected range.

The exact counter-electrode material and geometry remain release blockers until closed by a primary source or a controlled local qualification.

## 9. Pre-anodization surface gate

Anodization is interface-sensitive. The sample must not enter this step unless the preceding mesa/surface preparation has a defined surface-state acceptance gate.

At minimum record:

- final wet chemistry used before anodization;
- elapsed air exposure between last clean/etch and immersion;
- Nomarski surface image;
- surface roughness on representative coupons;
- optional ellipsometric reference values;
- pre-process Hall properties on a companion coupon.

The exact RP-01 pre-anodization rinse/clean remains `[OPEN]`.

## 10. Qualification run record

For each anodization coupon, record:

- coupon ID and wafer position;
- x/composition metric;
- n and mobility from material-control coupon;
- exposed area;
- electrolyte batch ID and preparation timestamp;
- KOH molarity;
- EG/H2O ratio;
- bath temperature before and after processing;
- applied current;
- calculated current density;
- voltage at start;
- voltage-time trace;
- time to 15 V, if reached;
- final voltage;
- total anodization time;
- visual film color/uniformity;
- post-process rinse and drying sequence;
- measured film thickness at multiple positions.

## 11. Thickness metrology

Target thickness:

\[
800~\text{Å}=80~\text{nm}.
\]

RP-01 states 800 Å. `[P-RP01]`

The candidate TI process reports approximately 800 Å at ~0.3 mA/cm², ~15 V, ~2 min. `[P-TI]`

Thickness must be independently measured rather than inferred solely from color or formation voltage.

Preferred qualification methods:

- stylus profilometry across a deliberately delineated oxide step;
- spectroscopic or single-wavelength ellipsometry with an appropriate optical model;
- optical interference/color only as a secondary rapid indicator after calibration.

## 12. Electrical/passivation qualification metrics

Thickness alone is insufficient. A transferred native oxide must also be shown not to degrade the detector surface.

Qualification should include, where practical:

1. surface leakage or suitable test-structure measurement;
2. low-frequency noise comparison on devices fabricated with the candidate oxide;
3. stability after repeated thermal cycling to the intended detector operating temperature;
4. oxide adhesion/integrity after Mask-2 lithography;
5. reproducible RIE opening behavior through the ~80 nm oxide;
6. preservation of detector responsivity and 1/f-noise performance relative to the RP-01 benchmark.

## 13. Proposed initial DOE

The first transfer study should keep electrolyte composition fixed and investigate current density around the historical operating point.

Suggested current-density levels:

- 0.20 mA/cm²;
- 0.30 mA/cm²;
- 0.40 mA/cm².

These values lie within the 0.2–0.5 mA/cm² primary experimental range and bracket the TI 0.3 mA/cm² condition. `[P-TI/P-CV/QUAL]`

For each condition, measure:

- voltage-time curve;
- final thickness;
- thickness nonuniformity;
- visual uniformity;
- surface morphology;
- compatibility with subsequent photoresist/RIE processing.

Use multiple matched coupons per condition to estimate reproducibility before setting control limits.

## 14. Preliminary acceptance concept

No numerical production control limits are released yet. A successful candidate must demonstrate:

- mean oxide thickness centered near 80 nm;
- low across-coupon thickness nonuniformity;
- repeatable voltage-time signatures;
- no gross pinholes, matte regions, peeling, or visibly nonuniform coloration;
- no unacceptable surface/electrical degradation;
- clean patterning/opening in the subsequent RIE module;
- detector noise/responsivity performance compatible with the RP-01 objective.

Statistical limits must be based on actual process capability data, not guessed from the literature.

## 15. Important distinction: color is not the final metrology

The TI process associates a uniform deep-blue appearance with ~800 Å oxide. `[P-TI]`

This is useful as an operator-level process indicator but must not replace calibrated thickness measurement. Color depends on illumination, optical stack, viewing angle, and oxide optical constants.

## 16. Failure modes to log

- formation voltage does not rise reproducibly;
- excessive early voltage rise;
- current-compliance saturation;
- local gas evolution/roughening;
- matte/nonuniform oxide;
- large thickness gradient;
- pinholes;
- delamination or damage during lithography;
- anomalous RIE opening time;
- increased 1/f noise;
- degraded responsivity or lifetime;
- post-cycle instability.

## 17. Safety hold point

KOH is strongly caustic; ethylene glycol is toxic; HgCdTe contains mercury and cadmium. The anodization fixture is also an electrically driven wet-chemical process. Execution requires an institution-approved chemical-hygiene procedure, SDS review, compatible PPE, splash/containment controls, hazardous-waste routing for Hg/Cd-containing liquids and solids, and electrical isolation appropriate to the bath. This scientific qualification document does not replace local EH&S procedures.

## 18. Release blockers

This module remains `QUALIFICATION-CANDIDATE` until the following are closed:

1. exact UWA/RP-01 anodization lineage, if recoverable;
2. solvent-ratio preparation basis;
3. reagent grades;
4. counter-electrode material/geometry;
5. sample electrical-contact method;
6. bath temperature control tolerance;
7. agitation/no-agitation rule;
8. exact post-anodization rinse/dry sequence;
9. x≈0.30 thickness-versus-charge/voltage calibration;
10. oxide-thickness acceptance window;
11. electrical/passivation acceptance metrics;
12. compatibility with the released RIE contact-opening module.

## 19. Primary sources

1. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. Texas Instruments Incorporated, “Passivation of mercury cadmium telluride semiconductor surfaces by anodic oxidation,” U.S. Patent process disclosure, publication corresponding to patent 3,977,018.
3. “The interface characteristics of passivity anodic oxide films on Hg0.8Cd0.2Te by C–V measurements,” primary experimental article reporting 0.1 M KOH / 90% ethylene glycol / 10% water and 0.2–0.5 mA/cm² room-temperature anodization.
