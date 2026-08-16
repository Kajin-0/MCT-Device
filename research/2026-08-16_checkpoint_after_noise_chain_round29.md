# Research checkpoint — after noise-chain / analyzer-state Round 29

**Date:** 2026-08-16

## Why this checkpoint exists

Round 29 audited P12/P12A/P12B before adding documentation. The audit found that the existing noise metrology architecture is already technically sufficient; the remaining high-value work was historical state recovery and explicit coupling between the published responsivity/noise/`D*` figures.

No new top-level P35/P36 noise procedure was created.

Instead Round 29 created:

- `procedures/P12C_RP01_NOISE_STATE_IDENTITY_ANALYZER_LINEAGE_ADDENDUM.md`;
- `travelers/P12C_NOISE_CHAIN_STATE_IDENTITY_TRANSFER_REGISTER.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND29.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND29.md`;
- this checkpoint;
- integration updates to P12 / continuity files as applicable.

---

# 1. Audit conclusion

P12 already controls:

- PSD versus ASD versus finite-band RMS distinction;
- ENBW/window normalization;
- multiple detector/electronics/background states;
- preamplifier input-voltage/current-noise effects;
- complex gain calibration;
- analyzer span/line/window/averaging records;
- Johnson-noise validation;
- PSD-level electronics subtraction;
- stationarity;
- `1/f` model/knee extraction;
- g-r diagnostics;
- same-frequency responsivity/noise rule for `D*`;
- active-area discipline;
- background-scaling BLIP verification;
- uncertainty.

P12B already provides the traceable replacement route when historical electronics settings are unavailable.

Therefore a duplicate noise SOP would reduce clarity rather than increase reproducibility.

---

# 2. Strongest new direct RP-01 result

Re-audit of the complete Smith et al. 2001 article closes two previously underused facts.

## 2.1 Figure-5 noise state includes 60° FOV

The published noise spectrum is directly associated with:

- `80 K`;
- `10 V/cm`;
- stated `60° FOV`;
- low-noise preamplifier;
- HP35665A spectrum analyzer.

Thus Figure 5 is not an unspecified-dark-background spectrum.

The exact physical aperture/radiance remains open, so retain `stated 60° FOV` rather than silently converting it into a specific blackbody geometry.

## 2.2 Figures 3/5/6/7 are the same detector

The field-response, noise, spectral-response and spectral-`D*` performance data are tied to the same physical detector/device.

This materially strengthens state closure:

`Fig3 -> Fig5 -> Fig6 -> Fig7 = same detector`.

It does **not** identify the contact pair/gap from the nine-contact structure.

---

# 3. Critical D* ambiguity remains

The paper gives:

- spectral signal chopping `f_sig = 1 kHz`;
- `1/f` knee `~3 kHz`;
- high-frequency g-r plateau `~24.5 nV/sqrt(Hz)`.

Therefore:

`1 kHz < 3 kHz`.

Do not equate the 24.5-nV/sqrtHz plateau with the total detector ASD at 1 kHz.

The exact noise value/frequency/bandwidth convention used in the historical Figure-7 `D*` calculation remains open.

For new measurements use:

`D*(lambda,1kHz) = R_v(lambda,1kHz) sqrt(A) / e_det(1kHz)`

under the same physical detector/background/loading state.

Report `e_GR` and historical knee separately.

---

# 4. Historical knee convention

For RP-01 comparison, the knee is the intersection of:

- the low-frequency `1/f` trend;
- the high-frequency g-r level.

Do not redefine the historical `~3 kHz` knee as a -3-dB or Lorentzian corner.

Modern fitted breakpoints may be reported as additional metrics with different names.

---

# 5. Preamplifier lineage state

P12A remains valid.

Later UWA photoconductor work directly describes a low-noise voltage preamplifier designed to permit detector bias and cites:

`J. F. Siliquini, UWA PhD thesis, 1995`.

This is the strongest archival lead for the UWA detector preamplifier architecture.

The thesis/circuit has not been recovered.

Do not claim exact 1995 = 2001 circuit identity.

---

# 6. HP35665A state

Official Keysight documentation recovered/confirmed:

- Operators Guide `35665-90026`, Sep. 1991;
- Concepts Guide `35665-90028`, Sep. 1991.

Official instrument capability includes PSD, linear spectrum, cross spectrum, frequency response and time-domain functions with multiple resolution-line choices.

This proves instrument capability, not the UWA Figure-5 settings.

Still open:

- span;
- lines;
- record length;
- window;
- averaging type/count;
- overlap;
- scaling/display mode;
- input range/coupling/impedance state.

---

# 7. Background fluctuations are a real noise coordinate

Jozwikowski et al. 2003 same-UWA HgCdTe work explicitly includes background-illumination fluctuations in the modeled noise sources and compares the model against measured MWIR photoconductor noise spectra.

Therefore P12 transfer now treats background stability as a recorded measurement coordinate, not merely a radiometry concern.

Record:

- source/background temperature;
- FOV/aperture;
- window/filter;
- background drift;
- chopper state;
- pump/mechanical state where it can modulate optical coupling.

Do not automatically assign background-driven low-frequency fluctuations to intrinsic detector `1/f` physics.

---

# 8. Same-device identity does not close geometry

RP-01 gives nine 300×300-µm contacts with 50-µm-increment gaps, but the exact pair used for the performance figures remains open.

Permanent rule:

`same device != known active gap`.

Do not choose a convenient 50, 100, 150 ... 400 µm gap to back-calculate historical `D*`.

A figure-digitization or device-layout inference may be explored only as an explicitly conditional analysis and never promoted to direct historical fact.

---

# 9. Current controlled noise chain

Historical comparison state:

`device -> chosen contact pair -> bias/load network -> custom/qualified low-noise preamp -> HP35665A or calibrated equivalent -> PSD reduction`.

Traceable output vector:

`Y_NOISE={device_ID,contact_pair,T,E,I,P,FOV/background,Z_d(f),G(f),analyzer_state,e_det(f),alpha,f_k,hist,e_GR,e_n(1kHz),A,D*_closure}`.

P12C traveler requires an explicit P11/P12 state-identity matrix before `D*` may be calculated.

---

# 10. Highest-priority unresolved items

1. Siliquini 1995 UWA PhD thesis / preamplifier schematic.
2. Figure-5 HP35665A state/settings or raw data.
3. Exact performance-device contact pair and active gap.
4. Exact noise frequency/value/bandwidth convention used for Figure-7 `D*`.
5. Exact Figure-5 background radiance/aperture behind `60° FOV`.
6. Any original UWA noise-analysis calculation sheet/source code.

---

# 11. Recommended next round

Proceed to **Round 30: audit P10 bias/load/self-heating historical execution and the same-device electrical operating state**.

Reason:

Round 29 shows that the remaining uncertainty in noise is not mainly spectral estimation; it is the electrical loading between the detector and preamplifier. P10 already controls active-field/self-heating physics but historical RP-01 bias implementation remains incompletely reconstructed.

Priority recovery:

- exact detector bias-source topology;
- load/series resistance;
- where detector voltage was sensed;
- whether AC signal was capacitively coupled;
- preamplifier input impedance;
- detector differential resistance/current at 10 V/cm;
- exact contact pair/gap;
- relation between responsivity, noise and bias circuit;
- any same-UWA/Siliquini bias-preamp schematic evidence.

Audit P10 before creating new documentation. If P10 is already complete, create only a bias/readout lineage addendum/traveler rather than a duplicate top-level procedure.

A second possible Round-30 branch, if the bias chain cannot be advanced, is P13 transient/frequency-response apparatus recovery with explicit separation of intrinsic detector poles from P33 package thermal poles.
