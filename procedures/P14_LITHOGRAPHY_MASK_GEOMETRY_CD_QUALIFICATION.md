# P14 — lithography / mask geometry / critical-dimension qualification

**Status:** CONTROLLED QUALIFICATION METHOD — historical RP-01 lithography is only partially closed.

## 1. Purpose

Define and qualify the photolithographic dimensional-control process for the RP-01 two-mask HgCdTe photoconductor flow.

P14 must ensure that the dimensions used later in:

- P01 mesa isolation;
- P08 contact-window RIE;
- P09 Cr/Au contact/TLM qualification;
- P10 electric-field normalization;
- P11 responsivity/active-area normalization;
- P12 D* normalization;
- P13 dynamic response;

are **measured fabricated dimensions**, not merely nominal mask dimensions.

The historical paper does not disclose enough lithographic detail for a literal tool recipe. P14 therefore separates directly published process anchors from local exposure/profile/CD qualification.

---

## 2. Direct RP-01 mask architecture `[P]`

Primary source: Smith et al. 2001, DOI `10.1088/0268-1242/16/6/306`.

### Mask 1

Purpose:

- delineate individual HgCdTe detector mesas by wet chemical etching.

Directly established:

- photolithographic masking is used;
- mesa delineation is wet chemical;
- this is the first mask.

Not published:

- resist product;
- resist thickness;
- spin program;
- dehydration/adhesion treatment;
- soft-bake details;
- exposure wavelength/dose;
- mask-aligner mode;
- developer;
- develop time;
- mesa outer dimensions;
- alignment-mark geometry;
- resist-strip process.

All remain `[OPEN/QUAL]`.

### Mask 2

Purpose:

- define contact windows through the anodic oxide;
- expose selected HgCdTe areas to CH4/H2 RIE and create the n+ blocking-contact region;
- remain in place during Cr/Au deposition;
- enable lift-off of the Cr/Au stack;
- self-align the metal contact to the RIE-opened/passivation-opened region.

Direct successful preparation reported by RP-01:

- photoresist thickness approximately `4–5 µm`;
- prebake `80 °C for 30 min`;
- chlorobenzene soak `30 min`;
- resist then patterned, developed and rinsed in water;
- RIE then performed;
- Cr `30 nm` + Au `270 nm` deposited;
- lift-off successful.

Still not published:

- resist identity;
- dispense volume;
- spin speed/acceleration/time;
- exposure wavelength/dose;
- aligner contact/proximity/vacuum mode;
- developer identity/concentration/time;
- exact post-develop drying method;
- exact lift-off solvent/time/agitation;
- quantitative overhang dimensions.

---

## 3. General chlorobenzene lift-off lineage `[P-GENERAL]`

### Hatzakis–Canavello–Shaw 1980

M. Hatzakis, B. J. Canavello, J. M. Shaw, “Single-Step Optical Lift-Off Process,” *IBM Journal of Research and Development* 24, 452–460 (1980), DOI `10.1147/rd.244.0452`.

General finding:

- soaking a suitable positive AZ-type resist in chlorobenzene/aromatic solvent modifies the developed profile so that an overhang suitable for lift-off can be formed.

### Collins–Halsted 1982

G. G. Collins, C. W. Halsted, “Process Control of the Chlorobenzene Single-Step Liftoff Process with a Diazo-Type Resist,” *IBM Journal of Research and Development* 26, 596–604 (1982).

General finding:

- exposure, chlorobenzene soak, development and bake conditions interact;
- linewidth, overhang, resist height and thickness loss are useful control observables.

### Use restriction

These sources explain the mechanism and identify relevant process-control variables. They **do not establish the RP-01 resist product or its exposure/developer recipe**.

Do not infer AZ4000, AZ4110, AZ5214, Shipley, or any other commercial resist from the presence of a chlorobenzene soak alone.

---

## 4. Direct RP-01 contact-string geometry `[P]`

The experimental structure is reported as:

- HgCdTe layer thickness: `9.5 µm`;
- nine contacts;
- each contact: `300 µm × 300 µm`;
- initial contact separation: `50 µm`;
- separation increment: `50 µm` thereafter.

Thus the eight nominal inter-contact gaps are `[D from published geometry]`:

`L = {50, 100, 150, 200, 250, 300, 350, 400} µm`.

### 4.1 Derived nominal linear-string extent `[D]`

If these nine contacts are arranged consecutively along one axis as described:

`L_string = 9(300 µm) + Σ_{k=1}^{8}(50k µm)`

`= 2700 µm + 1800 µm`

`= 4500 µm = 4.5 mm`.

This is a **derived layout extent**, not proof that the outer mesa/sample is 4.5 mm long. Confirm actual mask topology before using it as a physical die dimension.

### 4.2 Nominal metal-contact area `[D]`

For a 300×300 µm contact:

`A_contact = 0.09 mm² = 9.0×10^-4 cm²`.

### 4.3 Nominal inter-contact optical/electrical area `[D]`

If the active strip width is exactly the published 300-µm contact width and the full gap is optically/electrically active, then

`A_active,nom = 300 µm × L_gap`.

| Nominal gap L | Nominal area | Area in cm² | sqrt(A) in cm |
|---:|---:|---:|---:|
| 50 µm | 0.015 mm² | 1.50×10^-4 | 0.01225 |
| 100 µm | 0.030 mm² | 3.00×10^-4 | 0.01732 |
| 150 µm | 0.045 mm² | 4.50×10^-4 | 0.02121 |
| 200 µm | 0.060 mm² | 6.00×10^-4 | 0.02449 |
| 250 µm | 0.075 mm² | 7.50×10^-4 | 0.02739 |
| 300 µm | 0.090 mm² | 9.00×10^-4 | 0.03000 |
| 350 µm | 0.105 mm² | 1.05×10^-3 | 0.03240 |
| 400 µm | 0.120 mm² | 1.20×10^-3 | 0.03464 |

**Critical restriction:** do not use this table for final D* normalization until the actual fabricated active width and selected contact pair are recorded.

---

## 5. Resist-to-metal thickness margin `[D]`

RP-01 reports:

- resist `4–5 µm`;
- Cr/Au total metal thickness `30+270 = 300 nm = 0.30 µm`.

Therefore nominal resist:metal thickness ratio is:

- `4/0.30 ≈ 13.3` at 4 µm resist;
- `5/0.30 ≈ 16.7` at 5 µm resist.

This is favorable geometrically for lift-off but is **not** a substitute for measuring the developed overhang/profile. Continuous metal coverage over the resist sidewall can still cause fencing or failed lift-off.

---

## 6. Dimensional hierarchy — never collapse these quantities

For every relevant feature P14 distinguishes:

1. `CD_mask` — designed/verified mask dimension;
2. `CD_resist` — developed resist dimension before etch/RIE;
3. `CD_mesa_top` — post-wet-etch mesa top dimension;
4. `CD_mesa_base` — post-wet-etch mesa/base dimension where measurable;
5. `CD_RIE_open` — passivation opening after RIE;
6. `CD_nplus` — electrically converted n+ lateral extent, from P08/LBIC or equivalent;
7. `CD_metal` — final metal footprint after lift-off;
8. `L_gap,metal` — final metal-to-metal gap used by P10;
9. `W_active` — actual active strip width used for area normalization.

The process is not dimensionally controlled if only the photomask CAD value is known.

---

## 7. Required lithography equipment / calibration

Before qualification record:

- mask aligner model;
- illumination wavelength/band;
- calibrated irradiance/dose measurement method;
- chuck/contact/proximity mode;
- stage alignment accuracy/repeatability;
- microscope calibration;
- spin coater model and chuck;
- spin-speed calibration;
- hotplate/oven temperature calibration and spatial uniformity;
- resist-thickness metrology instrument;
- feature-CD metrology instrument;
- profilometer/SEM capability where lift-off profile characterization is required;
- cleanroom temperature/RH during coating/exposure/development;
- mask ID/revision and inspection status.

Manufacturer nominal aligner resolution does not replace measured process CD capability on the actual thick-resist HgCdTe stack.

---

## 8. Mask-1 qualification sequence

Because exact historical Mask-1 resist conditions are open, production release requires a local qualification.

### 8.1 Witness/process-development samples

Use sacrificial HgCdTe-compatible coupons or process-equivalent witness substrates to establish coating/exposure/development behavior before consuming qualified detector material.

### 8.2 Coating qualification

For each trial record:

- resist identity/lot;
- substrate surface state/time since clean;
- dispense method/volume;
- spin speed, acceleration and time;
- edge-bead handling;
- bake method/time/T;
- thickness at multiple locations.

Select a thickness that survives the complete P01 wet mesa etch without mask breach, swelling, catastrophic edge retreat or adhesion loss.

### 8.3 Exposure/development matrix

Perform a dose/development matrix around the resist supplier’s technically valid process region.

Measure:

- open-feature CD;
- closed-feature CD;
- residual resist/scum;
- sidewall/profile quality;
- adhesion;
- post-P01 dimensional transfer.

Do not release exposure based only on visual clearing.

### 8.4 Coupling to P01

The released Mask-1 condition is the condition that gives acceptable **post-etch mesa geometry**, not simply the best developed resist pattern.

Wet lateral etch/undercut must be included in the final mask bias.

---

## 9. Mask-2 qualification sequence

Mask 2 must satisfy **both** RIE masking and metal lift-off, so it is a coupled process.

### 9.1 Preserve direct historical anchors during initial transfer

Initial center condition:

- target resist thickness: `4–5 µm` `[P]`;
- prebake: `80 °C / 30 min` `[P]`;
- chlorobenzene soak: `30 min` `[P]`.

Do not change these direct anchors casually during first transfer. Variables not disclosed historically must be optimized locally.

### 9.2 Required pre-RIE resist measurements

For each trial measure:

- thickness before chlorobenzene soak;
- thickness after soak and dry;
- developed opening width/length;
- resist remaining height;
- overhang/undercut or equivalent sidewall-discontinuity metric;
- residual scum in the opening;
- feature-to-feature uniformity across the test coupon.

Where SEM cross-section is impractical for every run, qualify a non-destructive proxy such as measured resist-thickness loss and periodic profile witness verification.

### 9.3 Exposure/development DOE

Because chlorobenzene profile formation interacts with exposure/development, vary these as a coupled DOE, not independently by intuition.

Required response variables:

- opening CD error;
- overhang/profile metric;
- resist height;
- RIE survival;
- metal sidewall discontinuity;
- final lift-off cleanliness;
- final metal CD.

---

## 10. Alignment

The simplified RP-01 flow self-aligns **RIE-opened contact region to metal footprint** through the same Mask-2 resist. This removes the conventional third-mask alignment error between a wet-opened passivation window and the subsequent metal.

However, Mask 2 still must align to the Mask-1 mesa/device geometry.

For every device record:

- x/y alignment error relative to Mask-1 alignment marks;
- rotational error where significant;
- minimum contact-window-to-mesa-edge clearance;
- final metal-to-mesa clearance;
- whether any metal/RIE opening overlaps an etched sidewall unintentionally.

Numerical alignment tolerance remains `[QUAL]` until electrical/contact yield and dimensional statistics define a process capability.

---

## 11. Post-P01 mesa CD metrology

After wet mesa etch and resist removal:

measure at minimum:

- mesa top width/length;
- lateral undercut relative to developed resist;
- etch depth;
- sidewall angle/profile where practical;
- edge roughness;
- dimensional nonuniformity among devices;
- alignment-mark survival.

Compute:

`ΔCD_wet = CD_mesa - CD_resist`

with sign convention documented.

The mask bias for production must be based on this measured transfer function.

---

## 12. Post-P08 RIE opening metrology

After RIE, before metal where inspection is compatible with surface-transfer requirements, characterize witness structures for:

- oxide-open CD;
- lateral resist erosion;
- physical HgCdTe recession;
- resist remaining height/profile;
- electrical n+ lateral extent on dedicated LBIC structures.

Do not interrupt the production RIE-to-metal sequence merely to obtain microscopy if such exposure degrades contact performance. Use matched witness coupons where needed.

---

## 13. Post-P09 metal CD / lift-off metrology

After lift-off measure:

- metal pad width/length;
- metal-to-metal gap for every contact pair used electrically;
- metal edge roughness/fencing;
- residual metal flakes/stringers;
- pinholes/discontinuities;
- Cr/Au delamination;
- unintended bridges;
- metal alignment to mesa.

The final `L_gap,metal` is the dimension used in P10:

`E = V_active / L_gap,metal`.

Do not use the nominal mask gap when the fabricated gap has been measured.

---

## 14. Historical-device identity problem

RP-01 reports the full 50–400 µm gap string but does not clearly identify which contact pair produced every published “typical device” responsivity/noise/D* curve.

Therefore historical reconstruction must label the gap for those curves as `[OPEN]` unless recovered from:

- original figure/caption/source data;
- author thesis/lab documentation;
- mathematical consistency that is independently overdetermined by exact Rλ, noise ASD and D* **and** the historical noise-frequency convention.

Do not promote a single consistency calculation to historical fact.

### Current speculative inference — DO NOT RELEASE AS FACT

If `W=300 µm`, `L=50 µm`, then `A=1.50×10^-4 cm²` and `sqrt(A)=0.01225 cm`.

With `e_n=24.5 nV/√Hz`, a responsivity near `4×10^5 V/W` would give

`D* ≈ (4×10^5)(0.01225)/(24.5×10^-9) ≈ 2.0×10^11 cm Hz^1/2/W`.

This numerical agreement is intriguing but insufficient because:

- exact Rλ at 4 µm must be extracted;
- the 24.5-nV/√Hz g-r floor may not be the noise used for the 1-kHz spectral D* curve;
- the same plotted device/contact pair is not textually identified.

Keep this inference in research status only.

---

## 15. Mask-set data package

A released mask set must contain:

- CAD/source file revision;
- mask vendor/fabrication specification;
- tone/polarity;
- feature dimensions;
- alignment marks;
- orientation marks;
- coordinate origin;
- Mask-1-to-Mask-2 overlay targets;
- dimensional inspection report;
- revision history;
- explicit mapping from contact pair ID to nominal gap;
- device ID convention engraved/encoded where feasible.

No device performance data should be accepted without a traceable mapping to its mask/device geometry.

---

## 16. Proposed device/contact-pair naming

For a nine-contact linear string label contacts `C1...C9` in physical order.

Nominal adjacent gaps:

- C1–C2: 50 µm
- C2–C3: 100 µm
- C3–C4: 150 µm
- C4–C5: 200 µm
- C5–C6: 250 µm
- C6–C7: 300 µm
- C7–C8: 350 µm
- C8–C9: 400 µm

This labeling is a **project convention** unless the historical mask labels are recovered.

For every measurement record the actual pair, e.g. `C1-C2`, rather than “typical detector.”

---

## 17. Qualification statistics

During lithography transfer, do not release from one visually successful sample.

For each key CD calculate:

- mean;
- standard deviation;
- min/max;
- systematic mask bias;
- within-sample spatial trend;
- run-to-run trend.

After sufficient data exist, establish process capability limits from electrical/performance requirements.

Do not invent Cp/Cpk targets before specification limits are physically justified.

---

## 18. Failure modes

### Mask 1

- resist delamination in Br-based etchant;
- pinholes/mask breach;
- excessive wet undercut;
- mesa narrowing;
- sidewall roughness;
- alignment-mark loss;
- incomplete isolation.

### Mask 2

- inadequate overhang;
- excessive overhang/CD enlargement;
- chlorobenzene-induced nonuniformity;
- residual scum preventing uniform RIE opening;
- resist erosion/collapse during RIE;
- metal sidewall continuity/fencing;
- incomplete lift-off;
- contact-window-to-mesa misalignment;
- metal bridging;
- particulate redeposition.

### Geometry/data system

- using nominal gap rather than measured gap;
- losing contact-pair identity between TLM and detector measurements;
- computing D* from an assumed active area;
- equating RIE opening CD with n+ electrical conversion CD.

---

## 19. Current P14 release blockers

The following historical details remain unresolved:

1. Mask-1 resist and complete photolithography process.
2. Mask-1 exact mesa geometry.
3. Mask-2 resist manufacturer/product.
4. Mask-2 spin/coating program.
5. exposure tool/wavelength/dose.
6. developer chemistry/time.
7. quantitative chlorobenzene-created overhang in RP-01.
8. exact lift-off solvent/time/agitation.
9. Mask-1-to-Mask-2 overlay tolerance.
10. which gap/contact pair produced each historical performance curve.

Until these are closed or locally qualified, P14 is a **controlled transfer/qualification procedure**, not a literal historical fabrication recipe.
