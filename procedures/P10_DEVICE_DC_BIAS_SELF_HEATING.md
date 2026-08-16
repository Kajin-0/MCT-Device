# P10 — Photoconductor geometry, DC bias, sweepout, and self-heating qualification

**Status:** `CONTROLLED-QUALIFICATION-METROLOGY` — the RP-01 electric-field conditions and contact-string geometry are substantially anchored, while the exact contact pair used for each historical performance curve, bias/load circuit, thermal resistance and self-heating limit remain qualification variables.

**Purpose:** Define the electrical geometry and bias conditions of the completed RP-01 photoconductor so that responsivity, noise, sweepout, spectral response and D* are compared at the same semiconductor electric field without hidden errors from nominal voltage, contact spacing, series resistance or Joule heating.

---

## 1. Direct RP-01 geometry anchors

The experimental structure is reported as:

- HgCdTe thickness `t = 9.5 µm` `[P-RP01]`;
- string of nine metal contacts `[P-RP01]`;
- each contact approximately `300 µm × 300 µm` `[P-RP01]`;
- initial contact separation `50 µm` `[P-RP01]`;
- subsequent separation increments `50 µm` `[P-RP01]`.

The structure was designed to permit both TLM contact-resistance extraction and photoconductor performance measurements.

The available paper text does **not** uniquely identify which contact spacing was used for every plotted “typical device” responsivity/noise/spectral curve. That gap remains `OPEN`.

---

## 2. Electric field is the primary bias variable

RP-01 reports detector bias in electric field `E`, not merely voltage.

For a contact gap `L`:

`E = V_active / L`.

Therefore the voltage required for a desired field is:

`V_active = E L`.

`L` must be the **measured electrical active gap**, not a mask nominal value.

### Historical operating point

The noise and spectral-response measurements in RP-01 use:

`E = 10 V/cm` at `80 K`. `[P-RP01]`

The responsivity–field sweeps extend to approximately `50 V/cm`. `[P-RP01]`

---

## 3. Contact-gap metrology

Before electrical characterization, measure the actual fabricated gap between the relevant contact edges.

Record:

- contact-pair IDs;
- nominal gap;
- measured gap at at least three positions across the contact width;
- mean gap;
- min/max gap;
- contact-edge nonparallelism;
- actual conducting width;
- microscope calibration uncertainty.

Preferred dimensional method:

- calibrated optical microscope or SEM on process-control structures.

The field uncertainty shall include gap uncertainty:

`u_E/E = sqrt[(u_V/V)^2 + (u_L/L)^2]`

for independent first-order terms.

---

## 4. Active width and area

For a nominal pair of 300-µm-wide square contacts, the nominal photoconductive stripe width is approximately:

`W ≈ 300 µm`.

The planar illuminated area between contacts is approximately:

`A_det = W L`

only if:

- the optical aperture exposes the entire gap;
- contact shadowing is treated consistently;
- lateral carrier collection outside the nominal gap is negligible or modeled;
- the mesa geometry does not truncate the width.

Because D* normalization depends on detector area, use a **measured/defined optical active area**, not automatically `300 µm × L`.

The final active-area convention remains a major characterization release item.

---

## 5. Nominal one-carrier electrical consistency model

For screening, take the RP-01 supplier values:

- `n_H/reference ≈ 9.8×10^14 cm^-3`;
- `µ_H/reference ≈ 4.0×10^4 cm²/V·s`;
- `t = 9.5 µm`.

Under the one-carrier, Hall-factor-one consistency model:

- `ρ ≈ 0.15922 Ω·cm`;
- for `W=300 µm`, conducting cross-section `A_x = W t ≈ 2.85×10^-5 cm²`.

Ideal bulk resistance between contacts is:

`R_bulk = ρ L/(W t)`.

At fixed electric field:

`I_bulk = E W t / ρ`,

so ideal current is independent of contact gap.

At `E=10 V/cm`, the ideal screening current is approximately:

`I_bulk ≈ 1.79 mA`.

This is a **derived consistency value**, not a directly published RP-01 current.

---

## 6. Nominal gap/bias table at 10 V/cm

Assumptions:

- `ρ=0.15922 Ω·cm`;
- `W=300 µm`;
- `t=9.5 µm`;
- ideal uniform bulk conduction;
- no contact/series resistance;
- `E=10 V/cm`.

| Gap L (µm) | V_active (V) | R_bulk (Ω) | I_bulk (mA) | P_bulk (mW) |
|---:|---:|---:|---:|---:|
| 50 | 0.050 | 27.93 | 1.790 | 0.0895 |
| 100 | 0.100 | 55.87 | 1.790 | 0.1790 |
| 150 | 0.150 | 83.80 | 1.790 | 0.2685 |
| 200 | 0.200 | 111.73 | 1.790 | 0.3580 |
| 250 | 0.250 | 139.67 | 1.790 | 0.4475 |
| 300 | 0.300 | 167.60 | 1.790 | 0.5370 |
| 350 | 0.350 | 195.53 | 1.790 | 0.6265 |
| 400 | 0.400 | 223.47 | 1.790 | 0.7160 |

This table is useful for instrument-range and self-heating planning only. Actual current must be measured.

---

## 7. Total measured voltage is not automatically active-region voltage

If contact/lead/series resistance is appreciable:

`V_source = V_active + I R_series + V_contact_terms`.

Therefore electric field should preferably be calculated from a four-terminal measurement of the active semiconductor voltage where the geometry permits.

If only two-terminal bias is available, quantify:

- lead resistance;
- contact resistance from P09 TLM;
- wiring resistance;
- series/load resistor drops.

Correct the voltage before calculating `E` when the correction is material relative to the field uncertainty budget.

---

## 8. Bias-source requirements

The bias system shall provide:

- low-noise bipolar or reversible DC bias/current capability;
- measured output voltage/current;
- current compliance;
- four-wire sensing where practical;
- low thermal EMF switching;
- sufficient isolation from the noise measurement chain;
- protection against transient overbias during connection/range changes.

Record:

- source model;
- range;
- calibration status;
- output noise over relevant bandwidth;
- compliance;
- filter network;
- grounding topology.

The exact historical RP-01 bias-source model is not yet known.

---

## 9. Required dark I–V / R–E sweep

At stabilized `80 K` and in darkness:

1. begin at zero bias;
2. acquire symmetric positive and negative field points;
3. use fine spacing through the intended 0–50 V/cm range;
4. dwell long enough for electrical and thermal settling;
5. record source V, active V, current, temperature and timestamp;
6. return to zero periodically to test drift/hysteresis.

Minimum outputs:

- `I(E)`;
- differential conductance/resistance;
- `R(E)`;
- polarity asymmetry;
- hysteresis;
- temperature versus field;
- dissipated power `P=V_active I`.

The exact sweep grid is a local qualification setting and must be frozen after sensitivity testing.

---

## 10. Ohmic/linearity gate

At low field the device should behave approximately ohmically if contacts and bulk state are stable.

Define a low-field fit range during qualification and fit:

`I = G_0 V + I_0`.

Report:

- slope `G_0`;
- intercept;
- fit residual;
- positive/negative polarity difference.

Deviations may indicate:

- contact non-ohmicity;
- carrier heating;
- field-dependent mobility;
- self-heating;
- sweepout/photoconductive effects under illumination;
- leakage or parallel conduction.

Do not normalize responsivity by a nominal bias field if the dark electrical state is already nonlinear/uncontrolled.

---

## 11. Self-heating is a measured process variable

Joule power is:

`P_J = I V_active = I² R_bulk`.

Detector temperature rise is approximately:

`ΔT = P_J R_th`

only in a linear steady-state thermal model with thermal resistance `R_th`.

`R_th` depends on:

- HgCdTe/CdZnTe geometry;
- die attach;
- cold-finger material;
- contact/wire thermal paths;
- exchange gas/vacuum;
- package geometry.

Therefore there is no universal allowable power in mW.

---

## 12. Self-heating qualification methods

At least one direct or indirect temperature-sensitive method must be calibrated.

### Preferred direct method

Place a calibrated temperature sensor sufficiently close to the detector mount and characterize the thermal gradient/lag between sensor and device.

### Electrical thermometer method

Measure `R(T)` at negligible bias over a narrow range around 80 K.

Then, during DC bias:

- measure device resistance after thermal steady state;
- infer effective temperature from the calibrated low-bias `R(T)` relation.

This method is valid only if electric field itself does not materially alter resistance independently of temperature over the calibration region.

### Pulsed/DC comparison

Compare short-pulse electrical response with steady DC response at the same nominal field. A systematic DC drift toward the high-temperature state can identify Joule heating.

---

## 13. R(T) calibration near operating temperature

Using minimal excitation:

1. stabilize at a sequence of temperatures bracketing 80 K;
2. record detector resistance/current at near-zero-heating field;
3. fit a local monotonic interpolation `R(T)`;
4. quantify repeatability and thermal hysteresis;
5. repeat after relevant package/anneal changes if necessary.

The useful thermometer sensitivity is:

`α_R = (1/R)(dR/dT)`.

If `|α_R|` is too small near 80 K for reliable thermometry, use direct temperature sensing or another independent method.

---

## 14. Initial self-heating acceptance rule

Before a fixed numerical `ΔT_max` is established, use a physics-based qualification gate:

At the selected characterization field, measured responsivity/noise must be invariant within measurement uncertainty when:

- bias dwell time is varied;
- duty cycle is reduced;
- the detector is returned to the same mount temperature;
- a short-pulse measurement is compared with DC where feasible.

Any statistically significant temperature/power dependence must be modeled or the bias reduced.

The final production/characterization temperature-rise limit remains `QUAL`.

---

## 15. Responsivity versus electric field / sweepout

RP-01 measured single-wavelength responsivity versus field at:

- `T=80 K`;
- `λ=4 µm` for the principal field sweep;
- `FOV=60°`;
- chopping `1 kHz`.

The response departs from linear growth at higher field. Smith et al. identify this as **sweepout**, where photogenerated minority carriers drift to a contact and the effective lifetime/responsivity saturates if the n+/n barrier does not block recombination sufficiently.

Therefore responsivity-field nonlinearity is an electrical-contact/device-physics diagnostic, not automatically self-heating.

---

## 16. Separating sweepout from heating

For each field where responsivity deviates from the low-field linear trend, perform diagnostic comparisons:

1. monitor device temperature / R(T)-inferred temperature;
2. compare DC and reduced-duty-cycle operation;
3. reverse field polarity;
4. compare devices with different contact gaps at the same `E`;
5. compare P08 n+ density/depth/contact process conditions;
6. compare signal chopping frequency if relevant to lifetime dynamics.

Interpretation:

- power-dependent deviation that collapses under pulsed bias suggests heating;
- field-dependent deviation at constant temperature that correlates with blocking-contact properties is consistent with sweepout/contact recombination.

Both mechanisms may coexist.

---

## 17. Sweepout metric

Define a normalized departure from the low-field responsivity extrapolation:

`S(E) = R_meas(E) / R_lin(E)`.

where `R_lin(E)` is the responsivity predicted by a fit over a verified low-field linear region.

Possible process metrics:

- field where `S(E)=0.95`;
- field where `S(E)=0.90`;
- maximum responsivity;
- field at maximum responsivity.

Final acceptance thresholds remain `QUAL`.

Use this metric to correlate P08 variables (`n+`, `d_conv`, lateral extent) with device-level blocking performance.

---

## 18. Bias polarity test

Measure responsivity and dark I–V for both bias polarities.

Large asymmetry may indicate:

- non-identical contact conversion;
- contact-metal asymmetry;
- unequal RIE lateral/depth profile;
- local surface/passivation damage;
- illumination asymmetry;
- temperature gradient.

A nominally symmetric detector should not have unexplained strong polarity dependence.

---

## 19. Load circuit must be documented

Voltage responsivity depends on the electrical readout topology.

Record:

- detector bias mode: voltage, current or resistor-biased;
- source/load resistance;
- detector DC resistance;
- preamplifier input impedance;
- coupling capacitors/high-pass network;
- cable resistance/capacitance;
- lock-in/spectrum-analyzer input impedance;
- whether the reported signal is detector voltage, load voltage or amplified voltage.

Until the exact RP-01 load/bias network is recovered, this remains a major reproduction gap.

---

## 20. Geometry normalization for cross-device comparison

For photoconductors, compare devices at fixed:

- electric field `E`, not fixed V;
- optical irradiance/background/FOV;
- temperature;
- frequency;
- active-area convention;
- material thickness/composition;
- carrier state.

Also report:

- `L`;
- `W`;
- `t`;
- `L/W`;
- measured dark resistance;
- dissipated power.

This prevents an apparent process improvement that is actually a geometry/bias change.

---

## 21. Process-development data record

Every P10 characterization run shall store:

- device ID and wafer position;
- contact-pair IDs;
- measured gap/width/thickness;
- active-area convention;
- temperature and thermal environment;
- bias source/load network;
- source V/current and sensed active V;
- electric field;
- current;
- resistance;
- power;
- temperature proxy/direct T;
- polarity;
- illumination/chopper condition;
- responsivity if measured;
- sweepout metric;
- raw timestamps.

---

## 22. Failure modes

Log:

- contact-pair gap not known accurately;
- field calculated from nominal source voltage despite large series drop;
- asymmetric I–V;
- non-ohmic contact behavior;
- resistance drift with dwell time;
- measurable Joule heating;
- thermal runaway;
- responsivity saturation caused by sweepout;
- unexplained polarity asymmetry;
- excessive load-induced signal attenuation;
- detector resistance inconsistent with P05/P06 geometry/material state;
- active-area definition incompatible with D* normalization.

---

## 23. Release blockers

P10 remains qualification-level until closed:

1. exact contact pair/gap used for the canonical RP-01 performance curves;
2. final active-area convention;
3. exact device mesa width/outline beyond contact dimensions;
4. exact historical or selected bias circuit;
5. load resistance/input impedance;
6. self-heating temperature-rise limit;
7. package thermal resistance/time constant;
8. final low-field ohmic linearity tolerance;
9. sweepout acceptance metric;
10. maximum characterization field before heating/sweepout invalidates linear responsivity comparison;
11. allowed polarity asymmetry;
12. field/voltage/current uncertainty budget.

---

## 24. Primary source

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

Direct anchors used here include the nine 300×300-µm contacts, 50-µm incremental spacing, 9.5-µm layer thickness, responsivity field sweep to ~50 V/cm, and the canonical 10-V/cm spectral/noise condition at 80 K.
