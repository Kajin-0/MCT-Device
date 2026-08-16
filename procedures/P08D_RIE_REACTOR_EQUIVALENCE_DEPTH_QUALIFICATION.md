# P08D — RIE reactor-equivalence and conversion-depth qualification

**Status:** CONTROLLED LOCAL TRANSFER METHOD. Supplements P08/P08A/P08B/P08C. P34 is now the empirical apparatus/execution layer.

## 1. Purpose

Define how a non-historical RIE reactor may be qualified to reproduce the RP-01 localized CH4/H2 blocking-contact process without pretending that matching only pressure, total flow, RF power and time guarantees plasma equivalence.

Historical RP-01 direct setpoints remain:

- parallel-plate Plasma Technology reactor;
- printed gas notation `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- RF power `50 W`;
- RF-on time `60 s`.

The exact powered-electrode area, electrode spacing, RF frequency, DC self-bias, sample temperature and individual MFC values have not been recovered from the primary RP-01 paper.

Therefore a transferred reactor is accepted by **measured plasma/device outcomes**, not by nominal controller settings alone.

For current empirical source evidence and the operator-level reactor traveler, use:

- `procedures/P34_RIE_REACTOR_EQUIVALENCE_EMPIRICAL_PROCESS_WINDOW.md`;
- `travelers/P34_RIE_REACTOR_EQUIVALENCE_EMPIRICAL_QUALIFICATION_REGISTER.md`.

## 2. Important rejected inference

The 1999 same-UWA mesa paper reports CH4/5H2 RIE at `400 mTorr` and `0.4 W/cm²`.

RP-01 reports `100 mTorr` and `50 W`.

A tempting calculation is:

`A = P / (P/A) = 50 W / (0.4 W/cm²) = 125 cm²`.

For a circular powered electrode this would correspond to an equivalent diameter of about `12.6 cm`.

**Do not use this as historical reactor geometry.** The project has not established that:

- both papers used the same reactor;
- the powered electrode area was unchanged;
- the quoted 0.4 W/cm² was defined using total powered-electrode area rather than exposed sample area or another convention;
- matching network/electrode loading/sample placement were identical.

Tag the 125-cm² result as a rejected/conditional derivation only.

## 3. Variables required to claim reactor equivalence

Record for the actual qualification reactor:

### RF/electrode system

- manufacturer/model;
- RF frequency;
- powered-electrode diameter/area;
- grounded-electrode/chamber area;
- electrode spacing;
- sample radial position;
- sample holder/backing material;
- total loaded sample area;
- forward power;
- reflected power;
- measured DC self-bias or another calibrated sheath/ion-energy proxy.

### Gas system

- CH4 purity;
- H2 purity;
- individual MFC setpoints;
- actual gas ratio;
- total flow;
- MFC range/calibration/correction factor;
- gas stabilization time before RF;
- chamber pressure gauge type and calibration.

P08A currently supports `CH4:H2 = 1:5` only at secondary/same-lineage evidence level. If adopted locally with the direct 64-sccm total, the derived candidate split is 10.6667 sccm CH4 / 53.3333 sccm H2; these are not direct historical MFC values.

### Thermal state

- chuck/electrode temperature;
- sample mounting/contact method;
- sample starting temperature;
- sample temperature or validated temperature proxy versus time;
- plasma-on thermal transient;
- cooldown before vent.

No reactor-equivalence claim is valid if sample thermal state is unknown.

### Vacuum/chamber state

- base pressure;
- prior process/chamber history;
- cleaning/seasoning sequence;
- pump/throttle configuration;
- process pressure stability;
- elapsed time since chamber clean.

## 4. Qualification outputs

The transferred RIE condition must be characterized by all of the following:

1. oxide-clear time `t_clear` for the actual ~80-nm anodic oxide;
2. physical HgCdTe recession `d_etch` after the full process;
3. surface morphology/roughness change;
4. sheet resistance/sheet carrier state after RIE;
5. Hall mobility or multicarrier transport state;
6. electrical conversion depth `d_conv` from LBIC or validated destructive correlation;
7. lateral conversion distance `L_conv`;
8. final Cr/Au TLM specific contact resistivity after P09/P09A;
9. detector I-V/noise/responsivity comparison against matched untreated/control structures.

No single output is sufficient.

## 5. Depth metrology

P08C identifies the UWA LBIC lineage:

- 1997 vacancy-doped p-type x≈0.31: 410 mTorr, CH4/H2, 0.4 W/cm²; ~0.2-µm physical etch but ~1.5-µm electrical conversion;
- 1998 arsenic-doped p-type x≈0.29: UWA institutional record gives 340 mTorr, CH4/H2, 0.4 W/cm²;
- 1999 Musca et al. junction-depth paper develops LBIC depth extraction with sensitivity to doping, wavelength, illumination direction and geometry;
- RP-01 cites a distinct n-type Musca et al. 1998 JEM result of ~8-µm conversion under similar conditions, but the exact process condition tied to that value remains unrecovered.

Therefore local `d_conv` must be measured. It may not be inferred from physical etch depth or copied from the p-type branches.

## 6. Sheet-density-first transport rule

RP-01 states the reported `2.0×10^15 cm^-3` converted density is averaged over the converted thickness.

Accordingly the more direct transport quantities for a converted sheet are:

- sheet resistance;
- sheet conductance;
- sheet carrier density where a one-layer reduction is justified;
- mobility/multicarrier state.

Only report a volumetric converted density after an independently justified `d_conv` is available.

For reference only:

- if `n_avg = 2.0×10^15 cm^-3` and `d_conv = 8 µm`, then `N_s ≈ 1.6×10^12 cm^-2`;
- if the full 9.5-µm layer were converted at the same averaged density, `N_s ≈ 1.9×10^12 cm^-2`.

These are conditional consistency values, not released targets.

## 7. Initial local transfer sequence

### Stage 1 — metrology/calibration

Before HgCdTe processing:

- calibrate MFCs;
- calibrate pressure measurement;
- record electrode geometry and RF frequency;
- establish a repeatable self-bias/ion-energy proxy measurement;
- establish sample-temperature calibration;
- define chamber clean/season state.

### Stage 2 — oxide clearing

Use matched anodic-oxide coupons and a short-time series to determine:

- oxide removal rate;
- `t_clear`;
- onset of HgCdTe physical recession;
- repeatability versus chamber history.

Define the semiconductor-exposure interval explicitly:

`t_sem = t_RF - t_clear`.

Do not treat all 60 s as HgCdTe exposure unless `t_clear` has independently been shown negligible.

### Stage 3 — nominal historical-center run

Use the direct RP-01 nominal controller values as the first historical center where the local reactor can safely support them:

- 100 mTorr;
- 64 sccm total;
- 50 W forward-power target;
- 60 s total RF time;
- locally chosen CH4/H2 split documented with provenance.

Record the resulting self-bias and temperature; these measured values become more useful transfer coordinates than 50 W alone.

### Stage 4 — output characterization

Measure `d_etch`, sheet transport, LBIC footprint/depth, lateral spread and TLM.

### Stage 5 — bounded transfer DOE

If the historical-center run misses the desired electrical/contact outcomes, vary one or two physically meaningful plasma coordinates at a time, prioritizing:

- self-bias/ion-energy proxy;
- pressure;
- sample temperature;
- semiconductor exposure time after oxide clear;
- CH4:H2 ratio within a bounded qualified range.

Do not vary every controller parameter simultaneously.

## 8. Equivalence metric

A local process should be labeled `RP01-RIE-TRANSFER-QUALIFIED` only when repeated runs reproduce a stable multivariate outcome vector:

`Y_RIE = {t_clear, self_bias(t), T_sample(t), d_etch, R_sheet/N_s, mu_H or transport model, d_conv, L_conv, rho_c, blocking_response, detector-noise delta}`.

Final numerical windows must be established from local repeatability and detector-performance correlation.

Matching `50 W / 100 mTorr / 64 sccm / 60 s` alone is not equivalence.

## 9. New empirical evidence incorporated by P34

### 9.1 Self-bias is not optional metadata

Semu et al. 1991 directly reported CH4/H2 HgCdTe RIE at total flow 85 sccm, 20 mTorr, 35 °C and 150 W with RF-induced dc bias in the approximate range `-360` to `-440 V`; an explicit 15-sccm CH4 / 70-sccm H2 example had about `-390 V` bias. The authors associated rough sidewalls/etched surfaces with the high dc-bias condition.

**Consequence:** forward power alone is not a portable ion-energy coordinate.

### 9.2 Crystallographic orientation follows the sample into RIE

Elkind and Orloff 1992 directly found strong face-dependent CH4/H2 RIE rate and morphology in HgCdTe. P29 plane/polarity genealogy must therefore remain attached to every P34 run.

### 9.3 Same-manufacturer hardware evidence is transfer-only

A primary same-era Plasma Technology RIE80 publication documents a 13.56-MHz lower powered electrode, base pressure below 0.5 mTorr and platform-temperature control. These are useful fields to recover/measure but **do not identify the RP-01 reactor model or settings**.

## 10. Mandatory raw records

Store:

- complete RIE run log;
- chamber history;
- gas/MFC calibration records;
- pressure trace;
- forward/reflected power trace;
- self-bias trace;
- temperature trace;
- oxide-clear metrology;
- physical etch metrology;
- Hall/sheet-transport raw data;
- LBIC raw maps and model version;
- TLM raw I-V and regression;
- matched detector/control electrical/noise data.

## 11. Current release blockers

Historical closure still sought for:

- exact individual RP-01 CH4/H2 flows;
- Plasma Technology reactor model;
- RF frequency;
- powered-electrode area and spacing;
- historical self-bias;
- historical sample temperature;
- base pressure / pumping / throttle configuration;
- historical chamber clean/seasoning state;
- RP-01 oxide-clear time and semiconductor exposure interval;
- exact condition tied to the ~8-µm n-type conversion result.

John Kenion White's 2005 UWA thesis has been positively identified as a likely high-value source, but the current repository PDF route returned HTTP 403 and full experimental text remains unrecovered.

Until historical details are recovered, P08D + P34 are the controlled route to local reproducibility.