# P08 — CH4/H2 RIE blocking-contact qualification for RP-01

**Status:** `CONTROLLED-QUALIFICATION-PROCESS` — the RP-01 nominal plasma recipe and required electrical outcomes are well anchored, but exact gas-ratio interpretation, reactor transfer variables, oxide-clear endpoint, conversion depth and lateral-spread limits remain qualification items.

**Purpose:** Reproduce the localized reactive-ion-etching-induced `n+` region used beneath the Cr/Au contacts of the RP-01 n-type HgCdTe photoconductor without exposing the active photoconductor body to blanket plasma-induced electrical modification.

---

## 1. Architectural role

RP-01 deliberately uses the CH4/H2 plasma as an **electrical contact-engineering process**, not merely as a physical etch.

The selected downstream architecture is:

`wet mesa isolation -> anodic oxide -> contact-window lithography -> localized CH4/H2 RIE -> Cr/Au`

The plasma serves two coupled functions:

1. clear the approximately `800 Å` native anodic oxide from the contact window;
2. modify the exposed HgCdTe into a more highly n-type `n+` region that blocks minority-carrier injection and improves contact behavior.

These two functions must be characterized separately. The time required to remove ~80 nm of oxide is not necessarily the time required to establish the target electrical conversion profile.

---

## 2. Direct RP-01 nominal setpoints

Smith et al. 2001 state the following for the experimental process:

- reactor class: parallel-plate Plasma Technology RIE system `[P-RP01]`;
- gas notation: `CH4/5H2` `[P-RP01]`;
- total gas flow: `64 sccm` `[P-RP01]`;
- chamber pressure: `100 mTorr` `[P-RP01]`;
- applied RF power: `50 W` `[P-RP01]`;
- process time: `1 min` `[P-RP01]`.

These are the strongest direct blocking-contact process anchors in the project.

### Critical gas-ratio release blocker

The accessible same-lineage literature consistently prints the chemistry as `CH4/5H2`, `CH4/H2`, or H2/CH4, but the current source audit has **not** located an explicit statement converting `CH4/5H2` into individual CH4 and H2 MFC setpoints.

Therefore:

- total flow `64 sccm` is `CLOSED-P`;
- individual `Q_CH4` and `Q_H2` remain `OPEN`;
- do **not** assume `1:5`, `5:1`, `5% H2`, or any other interpretation without a source or local gas-manifold record.

This ambiguity is a production-release blocker.

---

## 3. Direct RP-01 electrical outcome

After RIE, Smith et al. report approximately:

- converted region carrier density: `2.0×10^15 cm^-3` `[P-RP01]`;
- converted-region mobility: `3.3×10^4 cm²/V·s` `[P-RP01]`.

The paper states that the RIE-converted material was characterized at `80 K` and `300 K` using a van der Pauw structure with variable magnetic field up to `2 T`. `[P-RP01]`

The currently accessible text does not unambiguously assign the summary `n` and `µ` pair to one of those two temperatures. Preserve that ambiguity until the numerical plot/table is recovered.

### P08 process gate

A nominal `50 W / 100 mTorr / 64 sccm / 60 s` run is **not accepted** merely because the controller reached its setpoints.

The plasma-transfer process must reproduce the required electrical state using P05-compatible transport characterization on a matched process-control structure.

---

## 4. Test-structure geometry from RP-01

Smith et al. used an oxidized plain-wafer test structure patterned with square exposed regions approximately:

- `300 µm × 300 µm` `[P-RP01]`.

The surrounding material retained approximately `800 Å` anodic oxide. `[P-RP01]`

This geometry is useful for:

- visual oxide-clear verification;
- LBIC mapping of lateral electrical modification;
- subsequent contact/TLM development.

The exact production detector contact-window geometry remains separate from this qualification pattern.

---

## 5. Physical etch depth and electrical conversion depth are different quantities

This distinction is mandatory throughout the manual.

### Physical etch depth

`d_etch` = material physically removed from the surface by the plasma.

Measure with:

- stylus profilometry across a protected/unprotected step;
- AFM for shallow etch development where appropriate;
- cross-sectional microscopy for validation.

### Electrical conversion depth

`d_conv` = depth over which the semiconductor electrical state has been modified sufficiently to form the relevant `n+`/junction region.

Measure/infer with:

- LBIC using a validated geometry/model;
- differential Hall/SIMS/cross-sectional electrical methods where destructive validation is justified;
- transport/model correlation.

### Why the distinction matters

Same-lineage p-type work reports RIE-induced n-type conversion extending approximately `1.5 µm` into Hg0.69Cd0.31Te after only about `0.2 µm` of physical material removal under `410 mTorr`, CH4/H2, `0.4 W/cm²`. `[P-SILIQUINI]`

RP-01 cites prior n-type work under **similar RP-01 conditions** indicating an `n+` region extending approximately `8 µm` below the surface. `[P-RP01 citing MUSCA98]`

Therefore `d_conv` may greatly exceed `d_etch`, and neither value may be inferred from the other without a qualified model.

---

## 6. Status of the ~8 µm depth claim

RP-01 explicitly states that previous work on n-type HgCdTe under similar RIE conditions indicated `n+` doping extending approximately `8 µm` below the semiconductor surface.

The cited source is:

C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.

The source confirms that LBIC was used to determine both depth and lateral extent of RIE-induced `n+` doping in mid-wave n-type HgCdTe.

### Provenance rule

Until the complete experimental section is recovered and its exact pressure/power/time/gas mixture is matched to RP-01:

- `~8 µm` is tagged `P-OTHER-SOURCE/SIMILAR-CONDITIONS`;
- it is **not** a directly measured depth for the specific RP-01 detector wafer;
- it is **not** a production acceptance value yet.

---

## 7. LBIC qualification method

RP-01 gives unusually useful LBIC apparatus detail for the blocking-contact test.

Published anchors include:

- scanner: Waterloo Scientific scanning-laser system `[P-RP01]`;
- laser: diode-pumped Nd:YLF `[P-RP01]`;
- wavelength: `1.047 µm` `[P-RP01]`;
- approximate optical intensity: `400 mW/cm²` `[P-RP01]`;
- sample temperature: `80 K` `[P-RP01]`.

The optical map was used to identify electrically modified RIE squares on the oxidized n-type wafer.

### P08 LBIC outputs

For every RIE qualification condition, report:

- raw 2-D LBIC map;
- exposed-window physical dimensions;
- apparent electrical footprint;
- lateral extension beyond the lithographic window on each side;
- line scans through at least two orthogonal axes;
- signal amplitude/statistics inside and outside the RIE region;
- measurement temperature;
- laser wavelength/intensity/spot size;
- bias/load configuration;
- map pixel pitch and scan speed;
- model/version if depth is extracted.

Do not reduce the LBIC result to a single depth number while discarding the spatial map.

---

## 8. Lateral conversion is a lithographic design variable

RIE-induced electrical modification may extend laterally beyond the physical mask/window boundary.

Define:

`L_conv = lateral electrical extension beyond the nominal exposed-window edge`.

Measure `L_conv` independently along orthogonal directions because:

- plasma/sheath geometry may not be perfectly symmetric;
- lithographic edge profile may differ by direction;
- crystallographic or transport anisotropy may affect the LBIC footprint.

The production mask bias/contact overlap must be based on measured `L_conv`, not on the optical mask dimension alone.

Final lateral-extension tolerance remains `QUAL`.

---

## 9. Oxide-clear endpoint must be separated from conversion endpoint

RP-01 reports that removal of the anodic oxide from the RIE-exposed regions was confirmed optically.

For a transferred reactor, perform a split-time oxide-clear experiment before running the full 60-s electrical conversion process.

### Initial oxide-clear split

Use matched ~80-nm anodic-oxide coupons and expose for a time series bracketing the expected clear point.

At each time measure:

- remaining oxide thickness by profilometry/ellipsometry or another calibrated method;
- optical appearance;
- HgCdTe physical recess after oxide clear;
- surface morphology.

Determine:

- `t_clear` = first time the oxide is reproducibly fully removed;
- oxide etch rate over the qualified region;
- HgCdTe etch rate after clear.

Then distinguish:

- oxide clearing phase `0 -> t_clear`;
- HgCdTe plasma exposure `t_clear -> 60 s`.

This is critical because a reactor with a different oxide etch rate changes the effective semiconductor exposure even if total process time remains 60 s.

---

## 10. Reactor variables that must be closed for transfer

Absolute RF power is not sufficient to define an RIE plasma.

The following must be recorded and qualified:

### Chamber geometry

- reactor manufacturer/model;
- RF frequency;
- powered-electrode diameter/area;
- grounded-electrode/chamber geometry;
- electrode spacing;
- sample location relative to electrode center;
- sample carrier/backing material;
- thermal contact method;
- exposed sample area / total chamber loading.

### Gas system

- individual gas identities and purities;
- exact individual MFC flow setpoints;
- MFC calibration date/range/gas correction;
- total flow;
- gas-line/purge sequence;
- chamber seasoning/cleaning state.

### Vacuum/process

- base pressure before gas admission;
- process pressure measured at the chamber;
- pressure gauge type/calibration/location;
- throttle-valve/control mode;
- pump configuration.

### RF/sheath

- forward power;
- reflected power;
- RF frequency;
- electrode area, permitting power-density calculation;
- measured DC self-bias or equivalent ion-energy proxy;
- match-network state if available.

### Thermal

- sample starting temperature;
- sample temperature versus time;
- electrode/chuck temperature;
- backside cooling/thermal-contact condition.

### Time

- gas stabilization time before RF;
- RF-on duration;
- plasma ignition transient handling;
- post-RF gas/pump sequence.

Until these are closed, a different reactor cannot be claimed equivalent to the historical Plasma Technology process merely by setting `50 W` and `100 mTorr`.

---

## 11. Why sample temperature and pressure require explicit control

Later UWA high-density-plasma work demonstrates that plasma-induced HgCdTe conversion depth and transport state are strongly sensitive to process pressure and sample temperature, with RF/ICP power also significant.

The reactor architecture differs from RP-01, so those later numerical setpoints are **not** transferable. The mechanistic conclusion is transferable: temperature and plasma/sheath state must be measured, not ignored.

### P08 rule

No production RIE qualification is valid if sample temperature is unknown.

If direct wafer-temperature measurement during plasma is impractical, establish a validated thermal model/calibration using:

- embedded chuck sensor;
- dummy-wafer thermometry/temperature labels where compatible;
- transient calibration runs;
- repeatable sample mounting.

---

## 12. Physical etch-rate qualification

Using masked/protected HgCdTe coupons representative of RP-01:

1. measure pre-process surface height/roughness;
2. process at nominal RIE conditions;
3. remove mask/protection without additional HgCdTe etch;
4. measure step height at multiple locations;
5. calculate mean HgCdTe physical etch rate;
6. map within-sample uniformity;
7. repeat on at least three coupons/runs.

Report:

- mean rate;
- standard deviation;
- min/max;
- center-to-edge variation;
- surface roughness change.

Do not infer physical removal from electrical conversion depth.

---

## 13. Electrical transport qualification

Use P05 or an equivalent validated variable-field Hall structure on material exposed to the nominal blocking-contact plasma.

Record pre- and post-RIE:

- conductivity type;
- sheet resistance;
- Hall density `n_H`;
- Hall mobility `µ_H`;
- field linearity / multicarrier flags;
- sample thickness / converted-layer model;
- temperature.

### Historical target

RP-01 reports approximately:

- `n+ ≈ 2.0×10^15 cm^-3`;
- `µ ≈ 3.3×10^4 cm²/V·s`.

These are process-performance anchors; the final production window must be determined from contact resistance, injection blocking and detector performance.

---

## 14. TLM/contact-performance gate

The plasma process ultimately exists to improve the electrical contact region.

After RIE and Cr/Au metallization, qualify using the RP-01 nine-contact TLM structure or an equivalent structure.

Historical target:

`ρ_c ≈ 9×10^-4 Ω·cm² at 80 K`.

Record:

- TLM contact dimensions/spacings;
- RIE condition;
- time from RIE to metal deposition;
- metal thickness/deposition lot;
- measurement temperature;
- I–V linearity;
- extracted sheet resistance;
- transfer length;
- specific contact resistivity;
- fit residual.

The blocking-contact RIE is not accepted if the target transport modification is achieved but contact resistance is poor or unstable.

---

## 15. RIE-to-metallization delay is a process variable

HgCdTe surfaces can oxidize/adsorb contamination rapidly after plasma exposure.

Until a same-lineage source closes the exact transfer sequence, record:

- RF-off timestamp;
- chamber vent timestamp;
- sample removal timestamp;
- atmospheric environment;
- any wet/dry clean;
- metal-deposition load timestamp;
- pump-down/base-pressure timeline.

The interval from semiconductor plasma exposure to metal deposition must be correlated with TLM contact resistance before a maximum delay is released.

---

## 16. Initial reactor-transfer DOE

The first transfer experiment should not vary every plasma variable simultaneously.

### Stage A — reproduce oxide clearing

At fixed nominal pressure/power/gas system:

- time split around oxide clear;
- measure remaining oxide and HgCdTe recess.

### Stage B — reproduce electrical conversion at nominal 60 s

Using representative n-HgCdTe:

- run nominal total time `60 s`;
- measure P05 transport;
- obtain LBIC spatial map;
- measure physical etch depth.

### Stage C — time sensitivity

After stable nominal operation, use a small time series around 60 s to establish sensitivity of:

- `n_H`;
- `µ_H`;
- `d_etch`;
- LBIC footprint/depth proxy;
- TLM contact resistance.

### Stage D — pressure / thermal sensitivity

Only after the nominal condition is reproducible, perturb pressure and/or controlled sample temperature in a bounded DOE.

Do not use later ICP-RIE numerical conditions as the DOE center; they are a different reactor class.

---

## 17. Chamber-history / reproducibility controls

Hydrocarbon/hydrogen plasmas can be sensitive to wall condition and chamber memory.

Every run shall log:

- prior chamber process;
- chamber clean/season procedure;
- elapsed time since clean;
- base pressure;
- residual-gas condition if monitored;
- dummy seasoning run, if required;
- wafer/sample exposed area.

A production recipe must demonstrate that electrical conversion is reproducible across realistic chamber histories or define an explicit preconditioning sequence.

---

## 18. Failure modes

Log explicitly:

- incomplete oxide removal;
- excessive HgCdTe physical etch;
- carbonaceous/polymer residue;
- roughened or damaged surface;
- nonuniform converted carrier density;
- `n+` density too low/high;
- mobility degradation;
- conversion too shallow/deep;
- lateral conversion excessive for mask geometry;
- plasma damage extending into active region;
- non-ohmic Cr/Au contact;
- high or unstable specific contact resistance;
- excessive contact-to-contact variation;
- temperature drift/runaway;
- large reflected RF power;
- MFC/pressure-control instability;
- chamber-history dependence;
- post-RIE aging before metallization.

---

## 19. Safety hold point

This process uses hydrogen/methane gases, RF plasma, vacuum equipment, HgCdTe containing Hg/Cd, and potentially pyrophoric/flammable gas infrastructure. Execution requires facility-approved hazardous-gas cabinets, mass-flow and pressure interlocks, purge logic, leak detection, ventilation/exhaust, RF/vacuum interlocks, toxic-metal handling, and emergency procedures. P08 specifies scientific process control; it is not a substitute for equipment/facility safety authorization.

---

## 20. Release blockers

P08 remains `CONTROLLED-QUALIFICATION-PROCESS` until the following are closed:

1. exact interpretation of `CH4/5H2` and individual MFC setpoints;
2. gas purities;
3. exact Plasma Technology reactor geometry or experimentally validated transfer equivalent;
4. RF frequency and electrode area;
5. DC self-bias / ion-energy proxy;
6. sample/chuck temperature and thermal-contact method;
7. base pressure and chamber-conditioning sequence;
8. oxide-clear time/rate for the released P02 oxide;
9. HgCdTe physical etch rate;
10. quantitative `d_conv` and lateral-conversion calibration under the nominal transferred condition;
11. numerical allowable lateral spread;
12. electrical `n_H/µ_H` process window;
13. RIE-to-metal maximum delay;
14. Cr/Au deposition process;
15. TLM contact-resistivity process capability;
16. repeatability across chamber cleans, operators and material lots.

---

## 21. Primary sources

1. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.
3. C. A. Musca, D. A. Redfern, E. P. G. Smith, J. M. Dell, L. Faraone, J. Bajaj, “Junction Depth Measurement in HgCdTe Using Laser Beam Induced Current (LBIC),” *Journal of Electronic Materials* 28, 603–610 (1999), DOI `10.1007/s11664-999-0042-x`.
4. J. F. Siliquini, J. M. Dell, C. A. Musca, L. Faraone, “Scanning Laser Microscopy of Reactive Ion Etching Induced n-Type Conversion in Vacancy-Doped p-Type HgCdTe,” primary experimental paper reporting ~1.5-µm conversion after ~0.2-µm physical etch under 410 mTorr CH4/H2, 0.4 W/cm².
5. E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “Reactive ion etching for mesa structuring in HgCdTe,” *Journal of Vacuum Science & Technology A* 17, 2503–2509 (1999), DOI `10.1116/1.581988`.
6. B. A. Park et al., “Effect of High-Density Plasma Process Parameters on Carrier Transport Properties in p-to-n Type Converted Hg0.7Cd0.3Te Layer,” *Journal of Electronic Materials* 36, 913–918 (2007), DOI `10.1007/s11664-007-0132-6` — used only to identify plasma-transfer sensitivities; reactor/setpoints are not transferred to RP-01.
