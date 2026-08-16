# P12 — Noise PSD/ASD, NEP, and specific detectivity

**Status:** `CONTROLLED-QUALIFICATION-METROLOGY` — the RP-01 noise benchmarks and detectivity definition are directly anchored, while the historical preamplifier, analyzer configuration, ENBW/window/averaging, exact device active area, and noise value used in the published 1-kHz spectral D* curve remain open.

**Purpose:** Measure detector-referred voltage-noise spectral density under the same temperature, electric field, optical background and electrical loading as P11 responsivity, separate detector noise from readout noise, quantify 1/f and generation-recombination regimes, and calculate wavelength-dependent NEP and `D*` with a complete bandwidth/area/uncertainty convention.

---

## 1. Direct RP-01 noise anchors

Smith et al. 2001 report noise measurements for a typical device at:

- detector temperature `80 K` `[P-RP01]`;
- applied electric field `10 V/cm` `[P-RP01]`;
- field of view `60°` `[P-RP01]`;
- low-noise preamplifier `[P-RP01]`;
- HP35665A spectrum analyzer `[P-RP01]`.

Reported noise features:

- `1/f` knee frequency approximately `3 kHz` `[P-RP01]`;
- generation-recombination noise voltage approximately `24.5 nV Hz^-1/2` `[P-RP01]`.

The spectral responsivity/detectivity measurements were performed at:

- `10 V/cm`;
- `80 K`;
- `60° FOV`;
- chopping frequency `1 kHz`.

RP-01 reports `D*≈2.0×10^11 cm Hz^1/2 W^-1` at `4 µm`.

---

## 2. Direct RP-01 detectivity definition

RP-01 defines

`D*_lambda = (R_lambda / V_n) sqrt(l w Δf)`

where:

- `R_lambda` = measured voltage responsivity in V/W;
- `V_n` = detector noise voltage in the electrical measurement bandwidth;
- `l` = detector length;
- `w` = detector width;
- `Δf` = electrical bandwidth.

With active detector area

`A = l w`,

and detector-referred voltage-noise ASD

`e_n = V_n / sqrt(Δf)`

for a locally white stationary process over the measurement band, this becomes

`D*_lambda = R_lambda sqrt(A) / e_n`.

This ASD form is the preferred P12 implementation because it makes the bandwidth normalization explicit.

---

## 3. PSD, ASD, RMS noise, and ENBW must not be conflated

Definitions:

### Voltage-noise power spectral density

`S_v(f)`

units `V²/Hz`.

### Voltage-noise amplitude spectral density

`e_n(f) = sqrt(S_v(f))`

units `V/sqrt(Hz)`.

### Integrated RMS noise over a band

`V_rms = sqrt(integral S_v(f) df)`.

For a narrow measurement filter with equivalent noise bandwidth `B_ENBW` and approximately constant `S_v` over the filter:

`V_rms ≈ e_n sqrt(B_ENBW)`.

A spectrum-analyzer line amplitude, FFT-bin RMS value, or lock-in output is **not automatically V/sqrt(Hz)**. The analyzer/window/filter ENBW must be known before converting to spectral density.

---

## 4. Historical ambiguity that must be preserved

RP-01 reports:

- `1/f` knee ~3 kHz;
- g-r ASD ~24.5 nV/sqrt(Hz);
- spectral responsivity/detectivity measured with 1-kHz optical chopping.

Because 1 kHz lies **below** the reported 3-kHz 1/f knee, P12 cannot assume without additional source evidence that:

- the white/g-r floor `24.5 nV/sqrt(Hz)` was the noise used for the published spectral D* curve; or
- the total noise ASD evaluated exactly at 1 kHz was used.

The RP-01 equation requires a noise voltage/bandwidth convention, but the accessible paper text does not close this implementation detail.

### P12 rule

For new measurements:

**evaluate detector-referred noise ASD at the same signal frequency used for responsivity** unless a different detectivity convention is explicitly stated.

For the canonical RP-01 comparison:

`f_sig = 1 kHz`.

Report additionally the white/g-r floor and 1/f knee as separate diagnostic metrics.

---

## 5. Measurement states

Noise characterization shall include multiple states so detector and electronics contributions can be separated.

### N0 — analyzer/preamplifier input termination

- preamplifier input terminated with a qualified low-noise impedance representative of the source condition where appropriate;
- establishes electronics floor and instrument artifacts.

### N1 — detector connected, zero/near-zero bias

- detector at target temperature/background;
- measures Johnson/readout/background contributions without the normal bias-dependent detector excess noise.

### N2 — detector at canonical bias, optically blocked/cold-background condition

- `E=10 V/cm`, 80 K;
- characterizes electrically generated excess noise with minimized external photon background.

### N3 — detector at canonical bias and canonical 300-K/60° background

- reproduces the RP-01 background-loaded state.

### N4 — optional bias sweep

- several fields spanning low-field through the responsivity/sweepout region;
- maps bias dependence of 1/f and g-r noise.

Every dataset must state which noise state it represents.

---

## 6. Detector operating condition

P12 uses P10 to establish:

- contact-pair ID;
- measured active gap `l`;
- width `w`;
- active area convention;
- active-region voltage;
- electric field;
- current;
- dissipated power;
- self-heating status.

For RP-01 comparison:

- `T=80 K`;
- `E=10 V/cm`;
- nominal `60° FOV`, provisionally interpreted by the P11 flux check as a 60° full cone until physical geometry is recovered.

Noise and responsivity data used in one D* calculation must refer to the same detector state.

---

## 7. Low-noise preamplifier requirements

The historical preamplifier model is not identified in the accessible RP-01 text.

The selected P12 preamplifier shall have a complete input-referred noise model:

- voltage noise ASD `e_a(f)`;
- current noise ASD `i_a(f)`;
- input impedance `Z_in(f)`;
- gain `G(f)` magnitude and phase;
- input bias/offset behavior;
- overload limits;
- AC-coupling/high-pass behavior;
- output noise;
- source-impedance dependence.

For detector impedance `Z_d(f)`, approximate amplifier input-current-noise contribution is

`e_i(f) = |Z_source(f)| i_a(f)`.

Total independent electronics ASD contributions add in quadrature at the PSD level, not by arithmetic addition of ASD values.

---

## 8. Preamplifier gain calibration

Before detector measurements, determine complex gain `G(f)` over the complete noise band using a traceable electrical injection.

Store:

- injected signal amplitude;
- source impedance;
- measured output;
- gain magnitude/phase;
- frequency grid;
- calibration uncertainty.

Detector-terminal-equivalent output noise is

`e_in(f) = e_out(f)/|G(f)|`

only after correcting for any analyzer scaling and known filter transfer functions.

Do not use nominal front-panel gain alone for quantitative D*.

---

## 9. Spectrum analyzer configuration

The HP35665A is the historical RP-01 analyzer, but the exact historical settings are open.

A controlled implementation must record:

- analyzer model/serial;
- input range;
- coupling mode;
- sample rate;
- frequency span;
- number of FFT lines / record length;
- window function;
- averaging type;
- number of averages;
- overlap;
- anti-alias filter state;
- units/scaling mode;
- analyzer input impedance;
- calibration/self-test status.

If another FFT/spectrum analyzer is used, equivalence is established by calibrated PSD/ASD response, not by matching brand.

---

## 10. Frequency span

The RP-01 figure spans approximately `10^2–10^4 Hz`, sufficient to display both the low-frequency 1/f region and the high-frequency g-r plateau around the reported 3-kHz knee.

P12 qualification should extend wider where hardware permits, for example:

- below 100 Hz to characterize 1/f exponent;
- above 10 kHz to verify the true white/g-r region and identify readout roll-off/resonances.

The exact released span must remain within the calibrated flat-gain region of the complete detector/preamplifier/analyzer chain.

---

## 11. Window ENBW and normalization

For FFT-based PSD estimation, the chosen window changes the equivalent noise bandwidth per spectral line.

The acquisition software shall store or calculate:

- frequency-bin spacing `Δf_bin`;
- window ENBW factor;
- effective noise bandwidth per displayed line;
- whether the analyzer output is already normalized as PSD/ASD.

Validation test:

1. inject a calibrated broadband noise source or use a resistor with calculable Johnson noise;
2. acquire using the selected analyzer configuration;
3. verify recovered ASD is independent of FFT span/line count within uncertainty after correct normalization.

A configuration that changes the reported `nV/sqrt(Hz)` merely because FFT resolution changed fails qualification.

---

## 12. Johnson-noise validation

For a passive resistor `R` at temperature `T`, open-circuit thermal voltage ASD is

`e_J = sqrt(4 k_B T R)`

when `R` is approximately real and frequency independent over the band.

Use precision resistors spanning the detector's expected source resistance to validate:

- preamplifier input-noise model;
- analyzer PSD normalization;
- gain calibration;
- source-impedance dependence.

For the detector itself, do not subtract `sqrt(4kTR)` blindly if the biased device/load network is non-equilibrium or the measured terminal transfer differs from open-circuit voltage-noise conditions.

---

## 13. Electronics-floor subtraction

Let measured input-referred PSD with detector connected be

`S_meas(f) = S_det(f) + S_elec(f)`

only if the contributions are statistically independent and the detector does not change amplifier noise through impedance/loading effects.

Then

`S_det(f) = S_meas(f) - S_elec(f)`.

In ASD form:

`e_det(f) = sqrt(e_meas(f)^2 - e_elec(f)^2)`.

Never subtract ASD values linearly.

### Reliability gate

If electronics noise is a large fraction of measured noise, the subtraction becomes ill-conditioned.

P12 should aim for electronics ASD comfortably below detector ASD at the frequency used for D*, or report the increased uncertainty explicitly.

A final detector/electronics margin requirement remains `QUAL`.

---

## 14. Averaging and stationarity

For each state:

- acquire multiple independent/overlapped records;
- average PSDs, not ASDs, unless the analyzer explicitly implements an equivalent unbiased estimator;
- monitor detector current, temperature and background during acquisition;
- reject records containing obvious transients only under a documented objective rule.

Store individual-record statistics so stationarity can be checked.

Noise spectra that drift systematically with time must not be collapsed into a single average without explanation.

---

## 15. 1/f model and knee extraction

Use a model in PSD form, for example

`S_v(f) = K/f^alpha + S_GR(f) + S_white,other(f)`

or an empirically adequate reduced model over the fitted band.

Do not assume `alpha=1` without fitting/testing.

Define the `1/f knee` by a documented convention.

For RP-01 comparison, the historical graphical convention is the intersection of:

- fitted/drawn low-frequency 1/f trend;
- high-frequency g-r noise level.

P12 shall reproduce this definition numerically:

`S_1/f(f_k) = S_GR_plateau`

using PSD quantities.

Report:

- fitted `alpha`;
- knee `f_k`;
- uncertainty/fit range;
- plateau ASD.

Historical benchmark:

`f_k≈3 kHz`.

---

## 16. Generation-recombination spectral shape

A single lifetime generation-recombination process commonly has Lorentzian PSD shape:

`S_GR(f) = S_0 / [1 + (2 pi f tau)^2]`

for an appropriate measured electrical variable and model.

At frequencies well below its GR corner, ASD can appear approximately flat.

Do not assume the RP-01 `24.5 nV/sqrt(Hz)` plateau implies the GR lifetime corner lies inside the displayed 100 Hz–10 kHz band; the paper labels a g-r noise level but does not close a fitted `tau_GR` from that figure.

If a GR roll-off is observed in a wider-band P12 spectrum, fit `tau_GR` and compare with independently measured optical/electrical response time.

---

## 17. Canonical noise ASD at the signal frequency

For P11 responsivity at `f_sig=1 kHz`, define

`e_n,sig = e_det(f=1 kHz)`

under the same:

- T;
- E;
- FOV/background;
- electrical load;
- detector geometry.

If the spectral estimate averages over a small band around 1 kHz, record the exact band and weighting.

This is the default P12 noise term for `D*(lambda,1 kHz)`.

Also report separately:

- g-r plateau `e_GR`;
- 1/f knee `f_k`;
- electronics floor.

---

## 18. NEP

For spectral voltage responsivity `R_v(lambda,f)` and detector-referred ASD `e_n(f)`:

`NEP(lambda,f) = e_n(f) / R_v(lambda,f)`

units

`W/sqrt(Hz)`.

This is the input optical power producing SNR=1 in a 1-Hz-equivalent bandwidth under the stated linear measurement conditions.

The same optical-power convention used in P11 must be used here.

---

## 19. Specific detectivity

For active optical area `A` in `cm²`:

`D*(lambda,f) = sqrt(A) / NEP(lambda,f)`

or

`D*(lambda,f) = R_v(lambda,f) sqrt(A) / e_n(f)`.

Units:

`cm sqrt(Hz) / W`.

If starting from measured RMS noise voltage `V_n` in finite equivalent noise bandwidth `B_ENBW`:

`D* = R_v sqrt(A B_ENBW) / V_n`.

This is equivalent to the RP-01 equation when `A=l w` and `Δf` is the true electrical noise bandwidth.

---

## 20. Active area is a major release variable

RP-01 uses `A=l w` in its D* equation.

The historical structure has 300-µm-wide contacts and multiple gap lengths, but the accessible text does not state which exact gap/device length was used for every Figure 5–7 performance dataset.

Therefore a numerical RP-01 D* reproduction is incomplete until the relevant `l` is recovered or the exact measured device geometry is independently defined.

P12 shall use the P10 measured active optical/electrical area and explicitly state the convention.

Do not normalize noise/responsivity using a different area from the incident-power definition in P11.

---

## 21. Measured versus theoretical BLIP

Define separately:

### Measured specific detectivity

`D*_meas = R_v sqrt(A) / e_total`

using measured total detector-referred ASD at the stated signal frequency/background.

### Background-limited theoretical/idealized detectivity

Computed from a documented photon/background generation-recombination model using:

- blackbody photon spectrum;
- optical transmission;
- QE;
- detector response band;
- photoconductor generation/recombination statistics.

Do not label a measured value “BLIP” solely because it is close to a simple theoretical formula.

Operational BLIP evidence requires the measured detector noise to be dominated by background-induced generation/recombination noise and to respond appropriately when background flux is varied.

---

## 22. Experimental BLIP verification

At fixed 80 K, 10 V/cm and signal frequency:

1. vary controlled background photon flux using blackbody temperature and/or calibrated aperture;
2. measure total detector ASD at each background level;
3. measure responsivity or verify it remains constant;
4. subtract/track electronics floor;
5. examine noise PSD versus incident background photon rate.

BLIP behavior should show the detector noise moving with background in the manner predicted by the selected generation-recombination model and dominating other detector/readout terms over the claimed operating region.

A single spectrum at one background level is weaker evidence than a background-scaling experiment.

---

## 23. RP-01 BLIP consistency anchors

Historical reported point:

- `lambda=4 µm`;
- `T=80 K`;
- `E=10 V/cm` for the associated spectral measurements;
- `300 K` background;
- `60° FOV`;
- background photon flux `~1.0×10^15 cm^-2 s^-1`;
- QE `~70%`;
- `D*≈2.0×10^11 cm sqrt(Hz)/W`.

P11's Planck consistency calculation shows that the quoted photon flux is highly consistent with a 60° **full-angle** cone and an effective upper response boundary around 4.35–4.4 µm.

This supports the radiometric geometry inference but does not by itself prove the detector was strictly background-noise-limited at 1 kHz.

---

## 24. Noise-component reporting

For every detector report, separate where resolvable:

- readout/electronics floor;
- Johnson/thermal component;
- 1/f component;
- g-r component;
- background-induced component;
- any narrow spectral lines/microphonics/pickup.

Do not force every white plateau to be “g-r noise” without background/bias/temperature evidence.

Narrow environmental lines should be identified and excluded from broadband model fitting only under a documented rule, while remaining visible in raw data.

---

## 25. Bias dependence

Repeat the noise spectrum over a selected field series.

Record:

- `e_n(1 kHz,E)`;
- `f_k(E)`;
- `e_GR(E)`;
- detector current/power;
- temperature/self-heating;
- responsivity at matching E.

Then calculate

`D*(lambda,E) = R_v(lambda,E) sqrt(A) / e_n(f_sig,E)`.

The optimum bias is the field maximizing detector performance under a stated constraint, not necessarily the field maximizing responsivity alone.

---

## 26. Temperature dependence

During process qualification, repeat selected noise measurements around the intended operating temperature.

This helps distinguish:

- thermally activated GR processes;
- Johnson contribution;
- surface 1/f behavior;
- background-limited operation;
- self-heating sensitivity.

Record the actual detector/mount temperature rather than only cryostat controller setpoint.

---

## 27. Grounding, shielding, and microphonics

Document the complete noise measurement topology:

- detector bias source location;
- batteries/isolated supplies where used;
- star/single-point grounds;
- cryostat ground;
- preamplifier chassis/shield connection;
- cable type/length;
- shield termination;
- isolation transformers if used;
- mechanical pump/chopper vibration state.

Diagnostic states should include:

- chopper off/on;
- pumps on/off where safe/possible;
- input short/termination;
- bias off/on.

A 50/60-Hz harmonic comb or mechanical line is not detector 1/f/g-r physics.

---

## 28. P12 uncertainty budget

At minimum include:

### Noise ASD

- preamplifier gain calibration;
- analyzer amplitude calibration;
- PSD estimator statistical uncertainty;
- ENBW/window normalization;
- electronics-floor subtraction;
- source-impedance dependence;
- detector temperature/background drift;
- selected frequency-band averaging.

### Responsivity

Import P11 uncertainty in `R_v(lambda)`.

### Area

- active width;
- active length/gap;
- optical aperture/illumination convention.

### D*

For independent first-order terms:

`(u_D/D)^2 ≈ (u_R/R)^2 + (u_e/e)^2 + (1/4)(u_A/A)^2`

with correlations handled separately.

Report expanded uncertainty with stated coverage factor when sufficient statistics/calibration exist.

---

## 29. Canonical acquisition sequence

### Electronics validation

1. warm up/calibrate analyzer and preamp;
2. acquire terminated-input electronics floor;
3. validate PSD normalization with precision resistor/noise source;
4. verify gain flatness over selected span.

### Detector preparation

5. mount/identify detector and contact pair;
6. establish 80 K;
7. establish released FOV/background;
8. establish 10 V/cm using P10;
9. verify no unacceptable self-heating.

### Noise acquisition

10. acquire N1 zero-bias/near-zero-bias spectrum;
11. acquire N2 biased blocked/cold-background spectrum;
12. acquire N3 biased canonical-background spectrum;
13. repeat at least one spectrum to establish repeatability;
14. optionally perform bias/background sweeps.

### Reduction

15. input-refer via calibrated gain;
16. convert correctly to PSD/ASD using analyzer/window ENBW;
17. subtract electronics PSD where justified;
18. fit 1/f exponent/knee and g-r plateau;
19. extract `e_n(1 kHz)`;
20. combine with P11 `R_v(lambda,1 kHz)` and P10 area to calculate NEP and D*.

---

## 30. Data record

Store:

- detector/wafer/contact pair;
- measured L/W/t and active area;
- T/E/current/power;
- background/FOV/aperture state;
- preamplifier ID/settings/calibration;
- analyzer ID/settings/window/lines/span/averages;
- raw time records where feasible;
- raw/output PSD;
- input-referred PSD/ASD;
- electronics-floor PSD;
- corrected detector PSD;
- `alpha`, `f_k`, g-r plateau;
- `e_n(1 kHz)`;
- P11 responsivity dataset/version;
- NEP(lambda);
- D*(lambda);
- uncertainty components;
- BLIP verification state;
- PASS/REVIEW disposition.

---

## 31. Failure modes

Log:

- analyzer output misinterpreted as ASD;
- missing/incorrect ENBW correction;
- preamplifier gain not calibrated;
- amplifier current noise significant and unmodeled;
- electronics floor comparable to detector noise;
- linear subtraction of ASD instead of PSD subtraction;
- nonstationary drift hidden by averaging;
- environmental narrowband lines mistaken for detector physics;
- wrong active area;
- responsivity and noise measured at different E/T/f/background;
- 24.5-nV/sqrtHz g-r floor used automatically at 1 kHz despite the reported 3-kHz knee;
- D* calculated with `Δf` equal to FFT bin spacing instead of ENBW;
- BLIP claimed without background-scaling evidence;
- self-heating during noise acquisition.

---

## 32. Release blockers

P12 remains qualification-level until closed:

1. exact historical low-noise preamplifier model and gain;
2. historical HP35665A analyzer span/window/RBW/ENBW/averaging;
3. exact contact gap/active area of the Figure 5–7 detector;
4. exact noise value/frequency convention used for historical Figure 7 D*;
5. final selected low-noise preamplifier and input-noise model;
6. calibrated analyzer/FFT PSD implementation;
7. detector/electronics noise-margin criterion;
8. final 1/f fit/knee algorithm and uncertainty;
9. background-flux sweep / BLIP verification protocol;
10. exact active-area convention shared with P11;
11. laboratory D* uncertainty capability;
12. final process acceptance limits for `f_k`, g-r ASD and D*.

---

## 33. Primary / official references

1. E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. M. A. Kinch, S. R. Borrello, A. Simmons, “0.1 eV HgCdTe photoconductive detector performance,” *Infrared Physics* 17, 127–135 (1977) — primary HgCdTe photoconductor performance/noise work referenced by RP-01.
3. T. Ashley, C. T. Elliott, *Infrared Physics* 22, 367–376 (1982) — primary HgCdTe photoconductor noise/performance work cited by RP-01.
4. Keysight/HP 35665A Dynamic Signal Analyzer operating/service documentation for the actual analyzer's spectrum/PSD/window/averaging implementation; exact manual revision shall match the instrument used in a historical reconstruction.
5. P11 NIST spectral-responsivity sources for the responsivity/optical-power side of the NEP/D* chain.
