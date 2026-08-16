# P15 — die separation / die attach / interconnect / cryogenic package qualification

**Status:** CONTROLLED QUALIFICATION METHOD — RP-01 historical packaging details are not closed.

## 1. Purpose

Convert a fabricated/qualified HgCdTe photoconductor die into a mechanically stable, electrically low-noise, optically defined 80-K detector assembly without degrading the material/device state established by P01–P14.

P15 controls:

- die separation and edge damage;
- die cleaning/handling after separation;
- die-attach material and bondline;
- mechanical stress from cooldown;
- thermal resistance to the cold finger;
- electrical interconnect/wire bonding;
- package grounding/shielding;
- optical aperture/window/cold-shield geometry;
- vacuum compatibility;
- thermal cycling;
- post-package electrical/noise/responsivity stability.

No adhesive, wire material or bonding schedule is labeled “RP-01 historical” without source evidence.

---

## 2. Historical RP-01 status

Smith et al. 2001 reports detector measurements at 80 K and defined optical/electrical test conditions but the currently audited paper text does **not** disclose:

- die singulation method;
- final die outline/dimensions;
- die-attach material;
- die-attach cure schedule;
- cold-finger material;
- wire/ribbon metallurgy;
- wire diameter;
- ball versus wedge bonding;
- bond force/ultrasonic energy/time;
- package/header style;
- Dewar/window material;
- cold-shield/aperture dimensions;
- vacuum level;
- package bakeout;
- thermal-cycle qualification.

These remain `[OPEN/QUAL]`.

---

## 3. Relevant external evidence

### 3.1 HgCdTe detector architecture

Published experimental work using HgCdTe photoconductors commonly operates the element at liquid-nitrogen/cryogenic temperature on a cold-finger/Dewar-type assembly. This supports the broad thermal architecture but does not define RP-01 mechanical construction.

### 3.2 UWA vacuum-history warning

Later UWA HgCdTe work explicitly studied changes in device I–V behavior caused by vacuum baking. Although that work concerns LWIR photodiodes rather than RP-01 photoconductors, it is sufficient to establish an important process-control principle:

**package bakeout/vacuum thermal history is a device process variable and must not be selected solely from package convenience.**

### 3.3 Mechanical-test framework

Current MIL-STD-883 Part 2 is an active mechanical-test-method standard for microelectronic devices.

Useful method references after construction is selected:

- Method 2011 — destructive bond-strength/bond-pull testing;
- Method 2019 — die-shear strength;
- other applicable visual/thermal/mechanical methods may be selected when package architecture is frozen.

MIL-STD-883 is used here as a test-method framework, not as proof that RP-01 was military-qualified.

Do not assign numerical wire-pull or die-shear limits until wire material/diameter, bond geometry, die area and attachment system are defined.

---

## 4. Pre-package baseline gate

Before singulation/assembly, record a baseline for each device or matched witness structure sufficient to detect packaging-induced degradation.

Minimum pre-package records:

- device ID and wafer coordinates;
- P14 measured contact pair/gap/active geometry;
- optical micrographs of mesa/contacts;
- room-temperature continuity/resistance where safe and meaningful;
- 80-K P10 I–V / resistance / field response where practical;
- P09 contact/TLM evidence from same process lot;
- P12 noise benchmark where practical;
- P11/P13 responsivity or dynamic benchmark on selected qualification devices;
- passivation/metal visual state.

A package process cannot be qualified if there is no pre/post comparison capable of detecting damage.

---

## 5. Die separation / singulation

### 5.1 Historical method

`[OPEN]`.

### 5.2 Candidate methods

Possible methods include precision dicing, cleaving/scribing or another semiconductor singulation process, but the chosen method must be qualified for the actual CdZnTe/HgCdTe stack.

Do not release saw blade type, spindle speed, feed rate, coolant chemistry or scribe force from generic III–V/Si practice.

### 5.3 Required singulation-development measurements

For each candidate process record:

- die outline dimensions;
- edge exclusion from active mesa/contact structures;
- frontside protection method;
- chuck/tape/fixture;
- coolant/cleaning exposure if used;
- tool settings;
- edge-chipping statistics;
- crack length/depth where measurable;
- surface particulate/residue;
- contact/passivation damage;
- pre/post device resistance and leakage/noise indicators.

### 5.4 Die-edge acceptance

Numerical edge-chip/crack acceptance remains `[QUAL]` and must be based on:

- distance from active mesa/contact region;
- mechanical survival through cooldown;
- no measurable electrical/noise/responsivity degradation.

---

## 6. Post-singulation cleaning

The final cleaning sequence must be compatible with:

- anodic oxide;
- exposed Cr/Au;
- HgCdTe mesa sidewalls;
- CdZnTe substrate;
- any remaining surface coating.

Record:

- solvents/chemicals;
- purity;
- duration;
- agitation/ultrasonic exposure if any;
- rinse/dry method;
- elapsed time to die attach.

**Do not use aggressive ultrasonic cleaning by default.** Mechanical damage to wire-bond pads, brittle die edges or passivation must be excluded by qualification.

---

## 7. Cold-finger / carrier design requirements

The mount must provide:

1. sufficiently low thermal resistance to hold the detector at its recorded operating temperature;
2. low mechanical stress through cooldown/warmup;
3. stable electrical reference/grounding;
4. unobstructed optical access to the intended active region;
5. compatibility with vacuum/cryogenic environment;
6. no conductive/adhesive creep into the active area or wire-bond pads;
7. reproducible detector position relative to aperture/window/reference plane.

Record cold-finger/carrier:

- material;
- surface finish/plating;
- dimensions;
- flatness;
- electrical potential/ground connection;
- temperature-sensor location;
- detector-seat geometry.

---

## 8. Die-attach selection DOE

Because historical RP-01 die attach is unknown, select the attachment system by measured performance.

Candidate classes may include:

- conductive or nonconductive adhesive;
- solder/eutectic attachment where metallurgical/thermal compatibility is demonstrated;
- mechanical clamp or compliant attachment where appropriate.

No candidate is preferred a priori.

### 8.1 Variables to record

- attach material manufacturer/product/lot;
- shelf life/storage;
- mix ratio where applicable;
- dispense mass/volume;
- placement force;
- bondline thickness;
- cure temperature/time/atmosphere;
- fixture pressure;
- die/carrier surface preparation;
- cure-to-test elapsed time.

### 8.2 Critical HgCdTe-specific constraint

The selected cure/bake profile must not impose an uncontrolled thermal history that changes:

- HgCdTe defect state;
- contact behavior;
- passivation/interface charge;
- detector resistance/noise.

Therefore the maximum package-process temperature is not set by adhesive data sheet alone; it must pass electrical/optical pre/post qualification.

---

## 9. Die-attach thermal-mechanical qualification

For each candidate construction measure:

- bondline thickness/uniformity;
- voiding where inspection method allows;
- die tilt;
- room-temperature die position;
- die shear on sacrificial qualification samples or matched coupons;
- detector temperature under known dissipated P10 power;
- thermal settling time;
- strain/crack indicators after cycling;
- electrical/noise changes after cycling.

### 9.1 Thermal resistance metric

Where practical determine effective package thermal resistance from a calibrated heater/test structure or device temperature proxy:

`R_theta = ΔT_die / P`.

Do not infer die temperature solely from the cold-finger sensor when self-heating is relevant.

### 9.2 Cooldown stress

The carrier, die attach and CdZnTe die have different thermal contractions. Qualification must include repeated transitions between room temperature and the intended ~80-K operating state.

Monitor:

- die cracking/chipping;
- delamination;
- metal/passivation cracking;
- resistance/contact shift;
- noise shift;
- optical alignment shift.

A precise thermal-cycle count and ramp rate remain `[QUAL]` until the intended application/reliability level is defined.

---

## 10. Electrical interconnect / wire bond selection

### 10.1 Historical RP-01 metallurgy

`[OPEN]`.

The device top metal is Au over Cr, but this fact alone does **not** prove the historical use of Au wire, Al wire, ribbon, thermosonic ball bonding or ultrasonic wedge bonding.

### 10.2 Bond-process DOE

For candidate bond construction record:

- wire/ribbon material;
- diameter/thickness;
- bonder model;
- capillary/wedge tool ID;
- bond mode;
- stage temperature;
- force;
- ultrasonic power/amplitude;
- ultrasonic time;
- loop height/shape;
- first/second bond location;
- pad metallization state/cleaning;
- operator/program revision.

Use sacrificial/contact-process coupons during first transfer rather than optimizing directly on scarce detector die.

---

## 11. Wire-bond acceptance

Inspect 100% of production/qualification bonds optically for:

- bond placement;
- pad-edge clearance;
- heel damage;
- cratering/die damage;
- excessive deformation;
- wire sweep/contact with neighboring structures;
- shorts;
- lifted/non-wetted bonds;
- contamination.

Perform destructive bond-pull testing on dedicated qualification coupons/samples using an applicable method such as MIL-STD-883 Method 2011 after the wire construction is frozen.

Record:

- failure force;
- failure location/mode;
- wire diameter/material;
- loop geometry;
- test condition;
- sample statistics.

A high pull force with semiconductor/pad damage is not automatically a successful process; failure mode matters.

---

## 12. Electrical parasitics and low-noise package design

Because P12 noise is in the nV/√Hz regime, package/interconnect parasitics are part of detector performance.

Record/qualify:

- lead/contact resistance;
- ground resistance;
- insulation leakage;
- parasitic capacitance across detector/readout nodes;
- cable/feedthrough capacitance;
- package microphonics;
- pickup sensitivity;
- shield connection scheme;
- ground-loop behavior.

### 12.1 Dark package/noise test

With detector optically blocked and held at operating temperature, compare:

- pre-package noise;
- packaged noise with bias off;
- packaged noise at canonical field;
- package with mechanical vibration/tapping susceptibility test where appropriate.

New spectral lines or broad noise increases after packaging are a failure/investigation trigger.

---

## 13. Optical package / cold-shield geometry

P11 requires an explicitly measured optical throughput. Therefore P15 must define the installed geometry.

Record:

- detector active-plane coordinates;
- window material/thickness/coating;
- window clear aperture;
- detector-to-window distance;
- cold-shield material/finish;
- aperture diameter/shape;
- detector-to-aperture distance;
- nominal full/half FOV;
- vignetting;
- any filter;
- measured/calibrated spectral transmission.

### 13.1 FOV rule

Do not merely label the package “60° FOV.”

Compute the geometric view cone from measured dimensions and verify radiometrically where possible.

The P11 Planck consistency analysis suggests that RP-01's historical “60° FOV” is compatible with approximately a 60° **full** cone (30° half-angle), but this remains an inference and is not a package dimension.

---

## 14. Window/filter transmission

Before absolute responsivity reporting, characterize or traceably source:

`T_window(λ)` and `T_filter(λ)`.

Record:

- serial/lot;
- temperature if transmission is temperature dependent;
- angle of incidence;
- coatings;
- contamination/frost state.

Do not correct responsivity with a room-temperature catalog transmission curve when the actual installed optic materially differs.

---

## 15. Vacuum / atmosphere

Record:

- package/Dewar pressure or vacuum measurement method;
- pump/purge sequence;
- leak rate where applicable;
- getters/desiccants if used;
- residual gas control if available;
- bakeout temperature/time;
- time from pumpdown to measurement.

### Critical rule

Any package bakeout must remain inside a detector-qualified thermal budget. A vacuum-packaging procedure that improves outgassing but changes HgCdTe electrical/passivation state fails P15.

---

## 16. Temperature measurement

At least one calibrated temperature sensor must establish the cold-finger/carrier temperature near the detector.

During P10 self-heating qualification, determine whether detector temperature differs measurably from that sensor under bias.

Record:

- sensor type/serial;
- calibration;
- mounting method/location;
- readout current/power where relevant;
- thermal equilibrium criterion;
- temperature stability during P11–P13 measurement.

Do not write “77 K” or “80 K” solely because LN2 is present.

---

## 17. Package qualification sequence

A candidate package process should follow this controlled sequence:

1. obtain pre-package electrical/optical baseline;
2. singulate die;
3. inspect/measure edge damage and final die dimensions;
4. clean using qualified sequence;
5. attach die using recorded candidate process;
6. inspect attach/position/bondline;
7. perform room-temperature electrical continuity check;
8. wire bond/interconnect;
9. inspect bonds;
10. install aperture/shield/window/package components;
11. pump/purge/bake only within qualified thermal budget;
12. cool to operating temperature under monitored conditions;
13. repeat P10 electrical baseline;
14. repeat selected P12 noise baseline;
15. repeat selected P11 responsivity/throughput check;
16. repeat P13 bandwidth/lifetime check on qualification units when package parasitics could matter;
17. warm to room temperature;
18. inspect mechanically;
19. perform prescribed thermal-cycle qualification;
20. repeat critical measurements after cycling.

---

## 18. Pre/post package comparison metrics

At minimum compare:

- device resistance at defined T/E;
- I–V symmetry/nonlinearity;
- contact/lead resistance;
- noise ASD at canonical frequencies;
- 1/f knee;
- responsivity at one or more wavelengths;
- spectral cutoff/shape if package optics can influence it;
- temporal response where package/readout capacitance is significant;
- detector temperature under bias;
- optical throughput/FOV.

Packaging is accepted only when changes are within statistically and physically justified limits.

---

## 19. Mechanical qualification references

When the final construction is defined, use current applicable mechanical-test standards as method references, for example:

- MIL-STD-883 Part 2 Method 2011 for destructive bond strength;
- MIL-STD-883 Part 2 Method 2019 for die shear.

Record the exact standard revision/test condition used because standards evolve.

Do not use a generic “MIL-STD-883 compliant” label without identifying test method, revision, sample plan and applicable limits.

---

## 20. Required package traveler fields

- wafer/die/device ID;
- singulation tool/program;
- die dimensions/edge inspection;
- clean sequence;
- carrier/cold-finger ID/material;
- die-attach material lot;
- dispense/placement/cure data;
- bondline measurement;
- wire/ribbon material/diameter;
- bonder/tool/program;
- force/ultrasonic/time/stage T;
- bond map;
- aperture/shield/window dimensions;
- window/filter serials;
- vacuum/pump/bake history;
- temperature-sensor ID/location;
- thermal-cycle history;
- pre/post electrical/noise/responsivity results;
- deviations/nonconformances.

---

## 21. Failure modes

### Mechanical

- die crack/chip growth;
- die-attach delamination;
- voiding/high thermal resistance;
- cold-cycle stress fracture;
- die shift/tilt;
- wire heel fracture;
- bond lift;
- pad/semiconductor damage.

### Electrical/noise

- increased contact/lead resistance;
- package leakage;
- ground loop;
- microphonics;
- EMI pickup;
- added capacitance limiting P13 bandwidth;
- new 1/f/noise features.

### Optical

- aperture clipping;
- incorrect FOV;
- window/filter transmission error;
- condensation/frost;
- stray warm-surface view;
- detector misregistration.

### Thermal

- inadequate thermalization;
- detector warmer than cold-finger sensor;
- bias-dependent temperature rise;
- package bake altering detector state.

---

## 22. Current release blockers

1. Historical RP-01 die dimensions/outline.
2. Historical singulation process.
3. Historical die-attach material/cure.
4. Historical cold-finger material/geometry.
5. Historical wire metallurgy/diameter/bond method.
6. Historical package/header/Dewar construction.
7. Historical window/cold-shield/aperture dimensions.
8. Historical vacuum/bakeout process.
9. Numerical thermal-cycle reliability requirement for the intended application.
10. Qualified pre/post package degradation limits.

Until these are recovered or locally qualified, P15 is a package-transfer framework rather than a literal historical package recipe.
