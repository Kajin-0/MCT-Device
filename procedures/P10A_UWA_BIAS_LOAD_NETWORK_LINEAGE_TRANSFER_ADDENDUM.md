# P10A — UWA photoconductor bias/load-network lineage and transfer qualification addendum

**Status:** `HISTORICAL LINEAGE PARTIALLY CLOSED / LOCAL NETWORK QUALIFICATION CONTROLLED`.

**Parent:** `procedures/P10_DEVICE_DC_BIAS_SELF_HEATING.md`

**Purpose:** Close the electrical state between the HgCdTe photoconductor contacts and the P11/P12 measurement electronics without inventing the missing historical circuit. This addendum records the strongest recovered UWA evidence and defines a transfer-safe way to reproduce detector-terminal electric field, loading, small-signal voltage response, noise transfer and self-heating.

---

## 1. Why this addendum exists

P10 already defines the correct physical quantities:

- measured contact gap;
- active detector voltage;
- electric field `E = V_active/L`;
- current and dissipated power;
- source/load/contact drops;
- self-heating qualification;
- sweepout versus heating discrimination.

The unresolved historical gap is not the semiconductor physics. It is the **electrical network actually used to impose bias and extract signal/noise** in the UWA RP-01 measurements.

A transfer circuit is therefore qualified by the state it establishes at the detector terminals and by its measured transfer function, not by guessing a schematic.

---

## 2. Direct RP-01 evidence

Smith et al. 2001 directly state for Figure 3 that single-wavelength responsivity was measured as a function of applied electric field, explicitly described as:

> `voltage bias between the contacts`

Evidence class: `P-RP01-DIRECT`.

Direct RP-01 performance state:

- same physical detector is used for Figures 3, 5, 6 and 7;
- Figure 3: responsivity versus applied field, approximately 0–50 V/cm, 4 µm, 80 K, 60° FOV, 1-kHz chopping;
- Figure 5: noise at 10 V/cm, 80 K, 60° FOV, low-noise preamplifier -> HP35665A;
- Figures 6/7: spectral responsivity and D* at 10 V/cm, 80 K, 60° FOV, 1-kHz optical chopping for the responsivity measurement;
- detector has nine nominally 300×300-µm contacts separated by 50–400 µm in 50-µm increments.

### 2.1 What this closes

The canonical bias coordinate is the voltage across the selected detector contacts divided by their active gap:

`E_contact = V_contact-contact / L_active`.

The historical paper therefore does **not** justify interpreting `10 V/cm` as `V_source/L` when an unknown source/load/contact network could create additional voltage drops.

### 2.2 What remains open

RP-01 does not identify:

- bias-source model;
- source resistance;
- series/load resistor;
- whether bias was stiff-voltage, resistor-biased or another topology;
- detector current at 10 V/cm;
- detector resistance at the performance point;
- how detector-terminal DC voltage was sensed;
- AC-coupling/bias-tee topology;
- preamplifier input impedance;
- exact contact pair/gap for Figures 3/5/6/7;
- preamplifier input node and whether signal is detector voltage, load voltage or a transformed quantity;
- whether the same physical bias network was used for responsivity and noise.

All remain `OPEN-HISTORICAL`.

---

## 3. Same-UWA electronics lineage — Hatch et al. 2011

S. D. Hatch et al., *Applied Physics Letters* 98, 043505 (2011), DOI `10.1063/1.3540655`, is later than RP-01 and uses different HgTe/HgCdTe superlattice photoconductors, so it is **transfer evidence**, not historical proof.

The paper directly states that:

- photoconductors were mounted in a continuous-flow cryostat with a ZnSe window;
- output was connected to a **low-noise voltage preamplifier specifically designed so that a bias voltage could be applied to the device**;
- measurements were made at a chopping frequency just below 1 kHz;
- applied fields were varied over approximately 5–80 V/cm;
- temperature-dependent measurements used a stated `250 mV` bias;
- for one device `250 mV -> 9.2 V/cm`;
- for another `250 mV -> 8.6 V/cm`;
- the preamplifier citation is J. F. Siliquini's 1995 UWA PhD thesis.

### 3.1 Evidence-safe inference

This supports a persistent UWA architecture in which a voltage-domain readout allowed a controlled DC device bias while measuring chopped photoconductive response.

It does **not** prove:

- the 2001 RP-01 preamplifier was identical;
- 2001 used the same supply, coupling, input impedance or gain;
- the stated source bias equaled detector-terminal voltage without correction;
- the 1995 thesis circuit survived unchanged to 2001 or 2011.

---

## 4. UWA power-dissipation lineage

J. F. Siliquini and L. Faraone, *Infrared Physics & Technology* 38, 205–221 (1997), DOI `10.1016/S1350-4495(97)00016-9`, describes a different vertical HgCdTe photoconductor architecture.

Direct result relevant to P10 transfer:

- detector/array power dissipation is treated as a design-limiting quantity;
- a **pulsed biasing scheme** is used in the projected low-power array operation;
- the paper discusses bias field, detector impedance and power dissipation jointly.

The 1996 UWA 3×3 photoconductor-array paper, DOI `10.1088/0268-1242/11/12/024`, likewise identifies reduced power dissipation as an explicit motivation for the heterostructure/device architecture.

### P10A consequence

Bias duty cycle is a detector operating coordinate whenever self-heating matters:

`u_bias = {V_contact(t), I(t), duty, pulse width, repetition rate, settling interval}`.

Do not claim DC and pulsed operation are equivalent merely because their peak electric field is equal.

These are transfer principles; they do not establish that RP-01 Figure 3/5/6/7 used pulsed bias.

---

## 5. Historical state vector

For any attempted RP-01 reconstruction define the electrical state as

`S_bias = {device_ID, contact_pair, L_active, W_active, T, V_source, V_contact, I, E, P_det, source_R, load_R, Z_pre(f), coupling, duty, background, package_state}`.

For the historical Figures 3/5/6/7, currently closed values include:

- same physical detector;
- 80 K;
- selected performance field 10 V/cm for Figures 5–7;
- Figure-3 field sweep to roughly 50 V/cm;
- 60° FOV;
- contact voltage is the physical meaning of applied field.

Unknown coordinates remain explicit rather than back-calculated from a preferred circuit.

---

## 6. Detector-terminal field qualification

### 6.1 Preferred measurement

Measure detector voltage directly across the selected contact pair with a sensing path whose input impedance is high enough not to perturb the operating point.

`E = V_contact / L_active`.

Record:

- source output voltage;
- detector-contact voltage;
- detector current;
- selected contact-pair gap;
- all measurable series/load drops.

### 6.2 If direct four-terminal contact sensing is impossible

Reconstruct detector voltage from a calibrated network:

`V_contact = V_source - I R_series - V_other_drops`.

The correction must include uncertainty and frequency dependence where used for AC signal/noise interpretation.

### 6.3 Prohibited shortcut

Do not report

`E = V_source/L`

unless it has been demonstrated that the difference between `V_source` and `V_contact` is negligible relative to the released field uncertainty.

---

## 7. Bias/load network characterization

Freeze one complete schematic for every released measurement configuration.

Record at minimum:

- voltage/current source model and serial;
- source output impedance or programmed source resistance;
- series/load/bias resistors and measured values;
- resistor temperature where noise contribution matters;
- DC blocking / AC coupling capacitor values;
- bypass capacitors/filters;
- cryostat wiring resistance/capacitance;
- preamplifier input impedance versus frequency;
- analyzer/lock-in input impedance;
- grounding and shield topology;
- detector differential resistance at the operating point.

The circuit is part of the measurement method, not an incidental accessory.

---

## 8. DC load-line reconstruction

For a simple Thevenin source `(V_TH, R_TH)` feeding detector differential/static resistance `R_d`, the detector voltage is

`V_d = V_TH R_d/(R_TH + R_d)`

for a linear resistive operating point.

A photoconductor under background and bias may be nonlinear, so the actual load line shall be solved from measured `I-V` data rather than forcing a constant `R_d` model when nonlinearity is material.

Store:

- source-side I-V;
- detector-terminal I-V;
- inferred/observed `R_d = dV_d/dI`;
- network load line.

This is required to separate detector physics from a changing bias point when illumination changes resistance.

---

## 9. Small-signal responsivity transfer

A measured photoconductive signal is not automatically the open-circuit detector voltage.

For small-signal detector resistance perturbation `delta R_d` around a biased operating point, the external voltage response depends on the load/source topology.

Therefore characterize the empirical complex transfer

`H_sig(f) = V_meas(f) / V_detector-equivalent(f)`

or an equivalent circuit-defined transfer.

At the RP-01 signal frequency, store

`H_sig(1 kHz)`

with magnitude, phase and uncertainty.

P11 responsivity must specify whether its reported voltage is:

- detector-terminal small-signal voltage;
- preamplifier-input voltage;
- load-resistor voltage;
- amplified output divided by calibrated gain.

---

## 10. Noise transfer and bias-resistor noise

Every dissipative network element can contribute noise and can load detector noise.

For a resistor `R` at temperature `T_R`, equilibrium Johnson voltage PSD is

`S_V = 4 k_B T_R R`

only for the appropriate open-circuit representation; actual contribution at the preamp input must be propagated through the network transfer.

For P12/P12C, record:

- `H_det->pre(f)`;
- bias/load resistor Johnson contribution;
- source voltage/current noise;
- preamplifier voltage/current noise;
- detector source impedance;
- analyzer contribution.

Do not subtract a room-temperature load-resistor noise estimate from detector ASD without first propagating it through the actual circuit.

---

## 11. Bias-source noise qualification

Measure the bias source under the exact measurement configuration.

Minimum states:

1. source disconnected / preamp terminated;
2. source connected to a detector-equivalent resistor;
3. source on at the required DC output;
4. source replaced by a low-noise reference source where feasible.

Look for:

- broadband source noise;
- 50/60-Hz and harmonic pickup;
- switching-regulator components;
- reference/servo spurs;
- drift;
- noise dependence on output setting.

A source that is quiet in DC voltage specification can still corrupt a 100-Hz–10-kHz HgCdTe noise spectrum.

---

## 12. AC coupling / bias-tee qualification

If the detector's DC bias is blocked before the preamplifier/analyzer, record the entire high-pass transfer.

For a simple RC high-pass:

`H_HP(f) = j2πfRC / (1 + j2πfRC)`.

But actual transfer shall be measured because detector resistance and preamp impedance participate in the pole.

Qualification requires:

- measured amplitude/phase versus frequency;
- no material attenuation or phase ambiguity at 1 kHz unless corrected;
- known response across the 1/f-knee and g-r analysis bands;
- recovery/settling after bias changes.

---

## 13. Self-heating state is package-dependent

P10 and P33 must be combined.

At steady state, a simple approximation is

`Delta T ≈ P_det R_theta`

but P33 shows that bonding layers can produce package thermal poles from milliseconds to hundreds of milliseconds in HgCdTe photoconductor assemblies.

Therefore record both:

- steady thermal resistance / temperature rise;
- time-domain thermal response `H_pkg,thermal`.

A bias dwell shorter than thermal settling can produce a different detector state from nominally identical DC field measured after equilibrium.

---

## 14. Required self-heating discrimination experiment

At selected fields including the canonical 10 V/cm and points approaching the Figure-3 sweepout region:

1. establish the same cold-finger/package starting temperature;
2. acquire short-pulse response before appreciable package heating where feasible;
3. acquire multiple duty cycles at the same peak `V_contact`;
4. acquire steady DC after thermal settling;
5. monitor `I(t)`, `V_contact(t)`, package temperature and detector `R(t)`;
6. return to near-zero bias and verify recovery;
7. compare responsivity/noise at equal field but different dissipated-energy histories.

Interpretation:

- response that changes with duty/thermal history at fixed field indicates a thermal contribution;
- response that remains field-dependent after thermal state is held constant is stronger evidence for sweepout/contact physics.

Do not infer intrinsic sweepout from a single slow DC sweep with unmeasured temperature.

---

## 15. Canonical local operating sequence

### A. Geometry/state

1. identify detector and contact pair;
2. measure `L_active` and `W_active`;
3. establish P33 package/window/FOV state;
4. stabilize detector near 80 K.

### B. Network calibration

5. record complete bias/readout schematic;
6. calibrate resistor values and source output;
7. measure `Z_pre(f)` / relevant input impedance;
8. measure `H_sig(f)` and noise transfer using detector-equivalent standards;
9. verify source-noise contribution.

### C. DC qualification

10. sweep both field polarities at low power;
11. measure `V_source`, `V_contact`, `I`, `T` and time;
12. calculate actual `E` and `P_det`;
13. verify low-field linearity and absence of contact anomalies.

### D. Thermal qualification

14. perform duty-cycle/pulse/DC comparison;
15. derive/measure thermal settling and recovery;
16. freeze a maximum characterization dwell/power regime only after downstream invariance is demonstrated.

### E. P11/P12 handoff

17. establish exactly 10 V/cm from `V_contact/L_active`;
18. record current/power/background;
19. acquire responsivity and noise without changing circuit topology where practical;
20. if topology changes between P11 and P12, independently characterize both transfer functions and prove detector-state equivalence before joint D* calculation.

---

## 16. P11/P12 topology identity rule

The same physical detector and same nominal field are insufficient for joint D* if the electrical networks differ.

Define

`STATE-ELECTRICALLY-IDENTICAL`

only when at minimum the following are matched or explicitly corrected:

- selected contact pair;
- `V_contact` / field;
- detector current and power;
- source/load network or demonstrated equivalent operating point;
- detector differential resistance;
- preamp loading;
- thermal state;
- background/FOV;
- signal-frequency convention.

Otherwise use

`CORRECTED-TO-COMMON-ELECTRICAL-STATE`

or

`INCOMPATIBLE — DO NOT CALCULATE JOINT D*`.

---

## 17. Local output vector

For every released bias/readout state report

`Y_bias = {contact_pair, L, W, V_source, V_contact, I, E, P_det, R_static, R_diff, H_sig(f), H_noise(f), Z_pre(f), source_noise, T_detector_proxy, H_pkg,thermal, duty, polarity, sweepout_metric}`.

This vector is the electrical bridge from P10 to P11/P12/P13.

---

## 18. Explicit non-inferences

Do **not** infer any of the following without new primary evidence:

- RP-01 used the exact 1995 Siliquini thesis preamplifier;
- RP-01 used a resistor-biased circuit;
- RP-01 used a stiff low-impedance voltage source;
- RP-01 used battery bias;
- RP-01 used pulsed bias;
- RP-01's `10 V/cm` was calculated from source voltage without contact/load correction;
- the Figure-3/5/6/7 contact gap was 50, 100, 150, 200, 250, 300, 350 or 400 µm;
- the ideal screening current `~1.79 mA` was the historical current;
- one P11 and one P12 circuit were identical merely because the paper used the same detector.

---

## 19. Remaining historical blockers

Highest-value unresolved items:

1. J. F. Siliquini 1995 PhD thesis full text and preamplifier schematic;
2. exact RP-01 bias-source/load schematic;
3. exact contact pair for Figures 3/5/6/7;
4. measured Figure-5 detector resistance/current at 10 V/cm;
5. preamplifier input impedance and coupling;
6. source/bias resistor identities and temperatures;
7. whether P11 and P12 shared one electrical topology;
8. any original UWA lab traveler or notebook for the detector-performance measurements.

---

## 20. Primary sources

1. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. S. D. Hatch, C. A. Musca, C. R. Becker, J. M. Dell, L. Faraone, “Photoresponse in photoconductor devices fabricated from HgTe-HgCdTe superlattices,” *Applied Physics Letters* 98, 043505 (2011), DOI `10.1063/1.3540655`.
3. J. F. Siliquini, L. Faraone, “The vertical photoconductor: A novel device structure suitable for HgCdTe two-dimensional infrared focal plane arrays,” *Infrared Physics & Technology* 38, 205–221 (1997), DOI `10.1016/S1350-4495(97)00016-9`.
4. J. F. Siliquini, L. Faraone, “Two-dimensional infrared focal plane arrays based on HgCdTe photoconductive detectors,” *Semiconductor Science and Technology* 11, 1906–1911 (1996), DOI `10.1088/0268-1242/11/12/024`.
5. J. F. Siliquini, C. A. Musca, B. Nener, L. Faraone, “Temperature dependence of Hg0.68Cd0.32Te infrared photoconductor performance,” *IEEE Transactions on Electron Devices* 42, 1441–1448 (1995), DOI `10.1109/16.398658` — high-priority full-text recovery source for same-lineage electrical performance methods.

---

## 21. Release conclusion

P10 itself remains the canonical DC-bias/self-heating SOP. P10A adds the missing historical/electrical-network provenance layer.

A local reproduction is released by demonstrating the **same detector-terminal field and thermal/electrical state**, plus calibrated small-signal/noise transfer, rather than by recreating an undocumented historical schematic from inference.
