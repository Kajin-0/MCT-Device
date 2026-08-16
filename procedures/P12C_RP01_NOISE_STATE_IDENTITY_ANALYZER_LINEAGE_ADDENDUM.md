# P12C — RP-01 noise-state identity and analyzer-lineage addendum

**Status:** `DIRECT-STATE-CLOSURE / HISTORICAL-ELECTRONICS-PARTIAL` — supplements P12/P12A/P12B. This addendum records newly recovered direct relationships among the RP-01 performance figures and converts them into a stricter historical-transfer rule without inventing the still-missing preamplifier/analyzer settings.

## 1. Purpose

Close as much as possible of the actual experimental state behind the RP-01 noise spectrum and `D*` benchmark.

The key distinction is between:

1. facts directly tied to the published device and figures;
2. same-UWA instrumentation lineage;
3. official HP35665A capability;
4. local transfer requirements;
5. unresolved historical implementation details.

The objective is not to imitate a front panel. It is to reproduce the detector-terminal noise quantity under the same physical detector/background state and to preserve every historical uncertainty that still affects `D*` reconstruction.

---

## 2. Newly closed direct RP-01 figure identity

Re-audit of the complete Smith et al. 2001 article closes a point that earlier P12 wording left too loose.

The paper identifies the performance data in Figures 3, 5, 6 and 7 as belonging to the **same representative detector/device**.

Accordingly, the following observations are linked to one physical device rather than merely to nominally similar devices from the same process:

- Figure 3: 4-µm responsivity versus applied electric field;
- Figure 5: averaged noise-voltage spectrum versus frequency;
- Figure 6: spectral response/responsivity;
- Figure 7: spectral specific detectivity `D*`.

### Consequence

For historical reconstruction, the preferred state chain is now

`same device -> Fig.3 bias response -> Fig.5 noise -> Fig.6 spectral response -> Fig.7 D*`.

This materially reduces one uncertainty: differences among these figures cannot be attributed to different device identities unless the article explicitly says otherwise.

### What this does **not** close

The same-device statement does **not** identify which contact pair of the nine-contact structure was used.

The fabrication article gives the test/contact structure as nine `300 x 300 µm` contacts with separations beginning at `50 µm` and increasing by `50 µm`, but the exact performance-device active gap/contact pair used for Figures 3/5/6/7 remains `OPEN-HISTORICAL`.

Therefore:

`same device != known active length`.

No specific 50–400-µm gap may be assigned to the published `D*` normalization without further evidence.

---

## 3. Newly closed direct RP-01 noise state

The Figure-5 caption directly places the averaged noise-voltage spectrum at:

- detector temperature `T = 80 K`;
- applied field `E = 10 V/cm`;
- field of view `60°`;
- low-noise preamplifier;
- HP35665A spectrum analyzer.

The article text reports:

- low-frequency `1/f` behavior;
- a high-frequency generation-recombination noise level of approximately `24.5 nV/sqrt(Hz)`;
- a knee frequency near `3 kHz`.

The graphical/historical knee is the intersection of the low-frequency `1/f` trend and the high-frequency g-r level.

### Consequence

The optical state of Figure 5 is no longer allowed to be called `UNKNOWN-FOV` or implicitly treated as an optically blocked noise spectrum.

For a historical state record, Figure 5 is:

`NOISE-RP01 = {same_device, 80 K, 10 V/cm, stated 60° FOV, low-noise preamp, HP35665A}`.

### Remaining optical ambiguity

The label `60° FOV` still does not close:

- full-angle versus half-angle by documentary proof;
- aperture dimensions;
- aperture temperature;
- cold-shield geometry;
- window/filter transmission;
- vignetting;
- exact radiance/background temperature during the Figure-5 acquisition.

P11A's flux consistency result supports a 60° **full cone** for the quoted 300-K background-flux statement, but that remains a derived consistency inference rather than a recovered Figure-5 aperture traveler.

Therefore do not silently replace `stated 60° FOV` with `300-K blackbody at exactly 30° half-angle` in the historical noise record.

---

## 4. The 1-kHz / 3-kHz / 24.5-nV ambiguity remains fundamental

RP-01 directly uses `1 kHz` optical chopping for the spectral response/detectivity measurement state.

RP-01 also reports a Figure-5 `1/f` knee near `3 kHz` and a high-frequency g-r level near `24.5 nV/sqrt(Hz)`.

Thus:

`1 kHz < f_k ~ 3 kHz`.

The high-frequency plateau is therefore **not automatically the detector noise ASD at the 1-kHz signal frequency**.

P12C permanently prohibits the substitution

`e_n(1 kHz) := 24.5 nV/sqrt(Hz)`

unless one of the following is recovered:

1. the authors' explicit `D*` reduction convention;
2. the actual historical Figure-5 data plus a documented demonstration that the value used in Figure 7 was the plateau rather than the total 1-kHz ASD;
3. an archival calculation sheet/thesis/source establishing the convention.

For a new reproduction, the default is still:

`D*(lambda,1 kHz) = R_v(lambda,1 kHz) sqrt(A) / e_det(1 kHz)`

under a matched physical state.

The g-r plateau and knee are reported separately as diagnostic metrics.

---

## 5. Historical knee definition must be preserved

For direct RP-01 comparison, define the historical knee from the intersection of the two trends shown in Figure 5:

`S_1/f(f_k) = S_GR,plateau`.

Do not silently replace it with:

- a -3 dB corner;
- a fitted Lorentzian corner;
- a frequency where total ASD is `sqrt(2)` times a floor;
- a modern automated breakpoint algorithm.

A modern fit may be reported in addition, but the historical-comparison knee remains a separate explicitly named metric.

---

## 6. P11/P12 state-identity rule for `D*`

Because Figures 3/5/6/7 are tied to one physical device, the historical reconstruction should preserve that same-device coupling wherever possible.

A `D*` closure record must identify:

- device ID;
- contact pair / measured active gap;
- measured active width;
- temperature;
- active-region electric field;
- detector current and dissipated power;
- stated/measured FOV and background state;
- package/window/filter state;
- responsivity signal frequency;
- detector-referred noise ASD at the declared `D*` frequency;
- active-area convention.

The required equality is not just nominal wafer/process equality:

`state_R == state_N`

for the physical variables that affect responsivity/noise, where `R` denotes responsivity and `N` denotes noise.

At minimum lock:

`{device, contact pair, T, E, A, package, FOV/background, loading, frequency convention}`.

---

## 7. Same-UWA preamplifier lineage

P12A remains the controlled source for the strongest recovered preamplifier lineage.

Later UWA photoconductor work (Hatch et al., 2011, *Applied Physics Letters* 98, 043505, DOI `10.1063/1.3540655`) directly states that detector output was connected to a low-noise voltage preamplifier specifically designed to permit bias application and cites J. F. Siliquini's 1995 UWA PhD thesis for that preamplifier.

This supports the functional architecture:

`biased photoconductor -> custom bias-capable low-noise voltage preamp -> measurement/analyzer`.

It does **not** prove that the exact 1995/2011 circuit was unchanged for RP-01 in 2001.

The Siliquini thesis remains the highest-value archival electronics target.

---

## 8. Official HP35665A lineage

Official Keysight legacy documentation positively identifies:

- **35665A Dynamic Signal Analyzer Operators Guide**, publication `35665-90026`, Sep. 1991;
- **35665A Dynamic Signal Analyzer Concepts Guide**, publication `35665-90028`, Sep. 1991.

Official product documentation confirms the analyzer supports, among other functions:

- linear spectrum;
- power spectral density;
- cross spectrum;
- frequency response;
- time waveform/correlation measurements;
- one-channel analysis bandwidth up to `102.4 kHz`;
- two-channel bandwidth up to `51.2 kHz`;
- selectable `100`, `200`, `400`, and `800` lines of resolution.

These facts prove that the historical instrument class was capable of a correctly normalized PSD measurement.

They do **not** recover Figure-5 settings.

The following remain `OPEN-HISTORICAL`:

- input range;
- AC/DC coupling;
- span;
- line count;
- time-record length;
- window;
- averaging type/count;
- overlap;
- PSD versus spectrum display mode;
- analyzer input impedance setting;
- anti-alias configuration;
- any user correction or postprocessing.

---

## 9. Analyzer display is not detector-terminal ASD

Even if an analyzer display is labeled PSD or `V/sqrt(Hz)`, the historical detector-terminal quantity is not known until the preceding electrical chain is characterized.

Use the P12B chain model:

`S_meas(f) = |G(f)|^2 [S_det,loaded(f) + S_pre,in(f;Z_s) + S_bias,in(f)] + S_an,in(f)`.

Thus the controlled quantity is obtained only after establishing:

- `G(f)`;
- detector/source impedance;
- bias-network transfer;
- preamplifier voltage/current noise;
- analyzer scale/normalization;
- cable/loading effects.

A numerical match to `24.5 nV/sqrt(Hz)` after an undocumented gain correction is not a valid reproduction.

---

## 10. Background stability is part of noise metrology

Same-UWA HgCdTe noise work, Jozwikowski et al., *Journal of Applied Physics* 94, 6541–6548 (2003), DOI `10.1063/1.1619198`, explicitly includes **fluctuations of background illumination** among modeled noise sources and compares the model with measured MWIR HgCdTe photoconductor spectra.

Therefore a P12 noise run must record more than nominal FOV.

Where the detector views a warm background, record or monitor as practical:

- source/background temperature;
- aperture/shield state;
- source stability versus time;
- chopper state;
- window/filter state;
- laboratory thermal changes that can modulate incident background;
- pump/mechanical states that can modulate optical coupling.

If background fluctuations contribute within the analysis band, they are part of the measured system state and must not automatically be fitted as intrinsic detector `1/f` noise.

---

## 11. Historical reconstruction hierarchy

### Level H0 — direct paper state

Known:

- same device for Figures 3/5/6/7;
- Figure-5 `80 K`, `10 V/cm`, `60° FOV`;
- low-noise preamp;
- HP35665A;
- averaged noise-voltage spectrum;
- knee ~3 kHz;
- high-frequency g-r level ~24.5 nV/sqrt(Hz).

### Level H1 — archival electronics recovery

Recover:

- Siliquini 1995 thesis/circuit;
- any UWA lab traveler or thesis documenting the 2001 preamp/bias chain;
- Figure-5 analyzer settings;
- exact contact pair and active dimensions;
- exact `D*` noise-frequency/reduction convention.

### Level T — traceable local transfer

If H1 cannot be recovered, reproduce the physical quantity through P12B using:

- measured detector/source impedance;
- calibrated bias network;
- calibrated `G(f)`;
- Johnson-noise normalization checks;
- detector/electronics PSD separation;
- complete FFT/window/ENBW record;
- matched P11/P12 detector/background state.

This route may be more metrologically traceable than the historical paper while remaining honest about historical non-equivalence.

---

## 12. Required outputs from a P12C historical-transfer attempt

Produce:

`Y_NOISE = {device_ID, contact_pair, T, E, I, P, FOV/background, Z_d(f), G(f), analyzer_state, e_det(f), alpha, f_k,hist, e_GR, e_n(1kHz), A, D*_closure}`.

Report separately:

- `f_k,hist` — historical intersection-style knee;
- any modern fitted breakpoint/corner;
- `e_GR` — high-frequency plateau;
- `e_n(1kHz)` — total detector-referred ASD at the signal frequency;
- electronics floor;
- background-stability diagnostics.

Do not collapse these into one generic “noise number.”

---

## 13. Current unresolved historical items

1. exact active contact pair/gap for Figures 3/5/6/7;
2. exact preamplifier circuit/gain/input-noise/loading;
3. exact bias-source/load/coupling network;
4. exact HP35665A Figure-5 settings;
5. exact displayed quantity/scaling and any subsequent conversion;
6. averaging count/type;
7. exact source/background radiance during Figure 5 beyond stated `60° FOV`;
8. exact 1-kHz noise value used for Figure-7 `D*`, if that was the convention;
9. exact `D*` active-area/contact-gap value;
10. archival Siliquini 1995 thesis.

These remain `OPEN-HISTORICAL`, not absent.

---

## 14. Primary / official sources

1. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. S. D. Hatch, C. A. Musca, C. R. Becker, J. M. Dell, L. Faraone, “Photoresponse in photoconductor devices fabricated from HgTe-HgCdTe superlattices,” *Applied Physics Letters* 98, 043505 (2011), DOI `10.1063/1.3540655`.
3. K. Jozwikowski, R. Sewell, C. A. Musca, J. M. Dell, L. Faraone, “Noise modeling in HgCdTe heterostructure devices,” *Journal of Applied Physics* 94, 6541–6548 (2003), DOI `10.1063/1.1619198`.
4. Keysight Technologies, *35665A Dynamic Signal Analyzer Operators Guide*, publication `35665-90026`, Sep. 1991.
5. Keysight Technologies, *35665A Dynamic Signal Analyzer Concepts Guide*, publication `35665-90028`, Sep. 1991.
6. J. F. Siliquini, PhD thesis, University of Western Australia (1995), archival acquisition target cited by later UWA work for the custom low-noise bias-capable preamplifier; exact thesis title/call number remains `OPEN` in the current source record.
