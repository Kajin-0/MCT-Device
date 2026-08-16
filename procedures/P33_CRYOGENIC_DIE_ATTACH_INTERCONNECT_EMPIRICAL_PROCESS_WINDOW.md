# P33 — HgCdTe cryogenic die-attach / interconnect / package empirical process window

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert P15 from a general packaging qualification framework into an empirical execution layer for an RP-01-like HgCdTe photoconductor operated near 80 K.

The package is not treated as mechanically external to the detector. It can change:

- die stress/cracking;
- contact/interconnect resistance and excess noise;
- thermal resistance and self-heating;
- thermal recovery time constants;
- measured P13 frequency/transient response;
- optical field of view and throughput;
- microphonics and electromagnetic pickup.

The controlled chain is:

`fabricated die -> singulation/clean state -> attachment stack -> interconnect -> cold-finger/shield/window geometry -> cooldown history -> package thermal transfer -> P10/P11/P12/P13 detector state`.

P33 supplements P15. It does **not** claim to reconstruct an unpublished RP-01 package.

---

# 2. Evidence classes

- `DIRECT-RP01-PACKAGING` — directly disclosed by Smith et al. 2001.
- `PRIMARY-HONEYWELL-HGCDTE-PACKAGING` — Honeywell primary HgCdTe cryogenic attachment/device patents.
- `PRIMARY-HGCDTE-PC-THERMAL` — primary HgCdTe photoconductor thermal-stack measurements.
- `PRIMARY-HGCDTE-HYBRID-TRANSFER` — HgCdTe hybrid/FPA package mechanics that establish transfer constraints but are not RP-01 constructions.
- `SAME-UWA-DEVICE-CONTEXT` — UWA HgCdTe photoconductor work demonstrating operation/performance but not necessarily packaging detail.
- `LOCAL-QUAL` — locally defined construction qualified by measured detector response.

No external package construction may be relabeled `DIRECT-RP01-PACKAGING` because it is technologically plausible.

---

# 3. RP-01 historical state

RP-01 establishes detector operation around 80 K and the electrical/optical measurement context, but the recovered paper does not close:

- die separation method;
- die outline;
- carrier/cold-finger material;
- die-attach material;
- bondline thickness;
- cure schedule;
- wire/ribbon metallurgy;
- interconnect diameter;
- thermocompression/wedge/ball-bond method;
- bond force/ultrasonic/time;
- Dewar/header geometry;
- cold-shield aperture;
- window material;
- vacuum/bake history;
- thermal-cycle qualification.

These remain `OPEN-HISTORICAL`.

Siliquini and Faraone (1996), DOI `10.1088/0268-1242/11/12/024`, demonstrate 3×3 n-type HgCdTe photoconductor arrays with n+ blocking contacts and BLIP performance at 80 K, but the accessible institutional record does not close an RP-01-compatible assembly traveler.

---

# 4. Strong Honeywell cryogenic attachment evidence — compliant silicone branch

Honeywell US4081819A (T. T. S. Wong, filed 1977) directly addresses cracking of epitaxial HgCdTe devices during cryogenic cooling.

The patent describes the general construction:

- delineated epitaxial HgCdTe devices on a first crystalline substrate;
- the first substrate bonded to a second substrate;
- the second substrate may be a flat pack later attached to a Dewar cold finger or may be the Dewar structure itself;
- detector operation typically at 77 K or lower.

The prior glass-adhesive construction cracked on cooldown. Honeywell replaced the glass adhesive with silicone rubber.

Direct named examples:

- Dow Corning 3110 RTV silicone rubber;
- Dow Corning 3112 RTV silicone rubber;
- Dow Corning 3116 RTV silicone rubber.

The source specifies a silicone-rubber bonding material with thermal conductivity at least approximately `5.0×10^-4` in the source's printed thermal-conductivity units. Preserve the source notation; do not silently convert the unusual printed units without reconstructing the dimensional convention from the original patent.

### Controlled cracking experiment

Honeywell compared three combinations:

1. glass adhesive, air-abrasion depth `60 µm`, thermocompression bonding pressure `40 g`;
2. silicone rubber, air-abrasion depth about `50 µm`, thermocompression bonding pressure `40 g`;
3. silicone rubber, air-abrasion depth `15 µm`, thermocompression bonding pressure `5 g`.

After cooling to `5 K`, only the glass-adhesive device cracked; both silicone-rubber devices survived.

### P33 interpretation

This is strong evidence that attachment compliance/thermal transport can dominate cryogenic fracture behavior in epitaxial HgCdTe.

It does **not** establish:

- that RP-01 used Dow Corning 3110/3112/3116;
- that 5 g or 40 g is an RP-01 wire-bond or thermocompression setpoint;
- an optimum bondline thickness;
- an 80-K detector thermal time constant.

The 5-g/40-g values are retained as experimental transfer data only.

---

# 5. Direct HgCdTe photoconductor thermal-stack evidence

US4012691A, U.S. Navy, describes a directly relevant HgCdTe photoconductor assembly:

`HgCdTe crystal -> epoxy -> Irtran 2 or sapphire substrate -> GE 7031 varnish -> copper heat sink`.

The copper heat sink is maintained at `77 K`. Electrical conductors are fused to detector electrodes.

The primary result is that the epoxy and varnish layers are thermally resistive and vary appreciably between assembled detectors.

Thermal recovery occurs on two construction-dependent scales:

- initial recovery on the order of **several milliseconds**;
- slower recovery on the order of **hundreds of milliseconds**.

The patent attributes these two recovery scales to the two thermally resistive bonding layers and explicitly proposes pulse-heating/resistance recovery as an assembly-line method for determining detector thermal characteristics.

The patent also states that an electrical pulse through the detector leads may substitute for laser heating.

This method corresponds to the primary paper:

F. J. Bartoli, L. Esterowitz, M. R. Kruer, R. E. Allen, “Thermal recovery processes in laser irradiated HgCdTe (PC) detectors,” *Applied Optics* 14, 2499–2507 (1975), DOI `10.1364/AO.14.002499`.

### Permanent consequence

**A packaged HgCdTe photoconductor can exhibit package-generated time constants that are not intrinsic carrier lifetime.**

Therefore P13 shall not assign a slow transient pole to bulk detector physics until P33 package thermal response has been evaluated.

---

# 6. Thin-HgCdTe thermal-mismatch warning

US5462882A documents stress, slip lines, microcracks and fractures in thin HgCdTe structures mounted to materials with mismatched thermal expansion, especially during high-temperature processing and subsequent cooldown to approximately 77 K.

The patent specifically discusses thin HgCdTe in the `5–10 µm` class mounted by epoxy to silicon and the severe effect of thermomechanical mismatch.

Although this is an FPA/interdiffusion-anneal architecture, the thickness is close enough to the RP-01 `9.5 µm` active-layer scale to reinforce the following rule:

**Do not qualify a package adhesive from room-temperature bond strength alone.**

Thermal budget and cooldown strain must be tested on the actual CdZnTe/HgCdTe stack.

---

# 7. CTE-matched buffer evidence

US5365088A, Santa Barbara Research Center, documents repeated thermal-cycle failure in direct HgCdTe/Si hybrids and uses sapphire as a thermal/mechanical buffer because its thermal expansion is more similar to HgCdTe than silicon while retaining electrical insulation and useful thermal conductivity.

The source notes direct-hybrid reliability problems over repeated room-temperature-to-approximately-78-K cycling and identifies stress in both the HgCdTe and indium interconnects.

This is an FPA hybrid branch, not an RP-01 single-element package, but it establishes that carrier/substrate CTE is a first-class package variable.

---

# 8. Attachment selection is a multi-objective problem

P33 shall not optimize a single property such as lap shear.

Define the construction response vector:

`Y_attach = {cryogenic cracking, delamination, bondline voiding, R_theta, thermal transient poles, die tilt, electrical shift, noise shift, optical shift, vacuum stability}`.

The attachment system must trade:

- compliance;
- thermal conductivity;
- bondline thickness;
- vacuum/outgassing behavior;
- cure thermal budget;
- CTE mismatch;
- handling strength;
- detector electrical/noise stability.

A very stiff high-strength adhesive can fail mechanically through cryogenic stress. A highly compliant adhesive can survive mechanically while introducing excessive thermal impedance. Both failure modes are unacceptable.

---

# 9. First local attachment qualification branches

Historical RP-01 identity is open. Local qualification should compare a small number of explicitly identified constructions rather than a large uncontrolled adhesive survey.

## Branch A — compliant silicone-family transfer

A currently available, traceably specified cryogenic/vacuum-compatible silicone may be screened **only after** its formulation, cure and outgassing compatibility are reviewed.

The historical Dow Corning 3110/3112/3116 names are evidence of process family, not an instruction to procure an obsolete formulation or assume modern equivalence.

## Branch B — low-temperature epoxy-family transfer

A low-outgassing epoxy may be screened because epoxy-mounted HgCdTe photoconductors are directly represented in the NRL thermal literature.

The NRL source does not disclose a universally transferable epoxy identity.

## Branch C — mechanical/compliant alternative

A clamp/compliant mount may be investigated where optical access and die integrity permit. It is a local branch, not historical reconstruction.

### No solder default

Do not introduce an indium/eutectic die attach solely because indium is common in other HgCdTe architectures. The RP-01 Cr/Au top-contact chain and CdZnTe substrate interface must remain intact unless a separate qualification establishes compatibility.

---

# 10. Incoming die state

Before attachment record:

- die ID, wafer coordinate and P30/P31 genealogy;
- final P32/P28/P25/P27/P26/P24 process state;
- die outline and CdZnTe thickness;
- HgCdTe active thickness;
- contact/mesa geometry;
- edge chips/cracks;
- optical micrograph;
- room-temperature continuity/resistance where safe;
- 80-K P10 reference resistance/I–V where available;
- P12 reference noise on selected qualification units;
- P11/P13 reference on selected units.

Packaging-induced changes cannot be diagnosed without a pre-package baseline.

---

# 11. Carrier / cold-finger record

For every qualification build record:

- carrier material and grade;
- coating/plating;
- dimensions;
- detector-seat flatness;
- measured surface roughness where relevant;
- carrier CTE data source;
- thermal conductivity data source and temperature range;
- electrical potential/grounding role;
- attachment area;
- cold-finger material;
- carrier-to-cold-finger interface construction;
- temperature-sensor position relative to die.

Changing carrier material or thickness is a package-process change even when the adhesive is unchanged.

---

# 12. Bondline preparation and measurement

For each build record:

- attachment product, manufacturer, lot and expiration;
- storage history;
- mix ratio by explicit mass/volume basis;
- mix/degas method;
- dispense mass or volume;
- substrate/die surface preparation;
- placement force/fixture;
- cure temperature/time/atmosphere;
- cure ramp/cooldown;
- elapsed time to test.

Measure, where feasible:

- bondline thickness at several locations;
- die tilt;
- coverage fraction;
- edge squeeze-out;
- void fraction/void map by a qualified non-destructive method or destructive cross-section on witnesses.

### Rule

**Product identity is not a bondline specification.**

The same adhesive can produce materially different thermal response when thickness, coverage or voiding changes.

---

# 13. Package thermal characterization — mandatory development gate

After attachment and electrical connection, characterize the assembled detector thermal response near the intended operating temperature.

Two allowed excitation families are directly supported by the NRL primary method:

1. short optical heating pulse;
2. short electrical heating pulse through the detector.

Record:

- baseline die/cold-finger temperature;
- pulse power or electrical energy estimate;
- pulse duration;
- detector resistance versus time;
- acquisition bandwidth/sample rate;
- full recovery window;
- repeated pulses at more than one amplitude to test linearity.

Do not fit a one-pole model automatically.

At minimum inspect for:

- fast detector/internal recovery;
- intermediate attachment/substrate thermal pole;
- slow carrier/varnish/cold-finger pole;
- amplitude dependence;
- evidence of package nonlinearity.

Report package thermal response as `H_pkg,thermal(f)` or an equivalent time-domain kernel when needed for P10/P13 de-embedding.

---

# 14. Effective thermal resistance

Under a controlled steady dissipated power `P`, estimate

`R_theta,eff = (T_die - T_reference)/P`

only when a qualified die-temperature proxy exists.

The cold-finger sensor alone does not establish die temperature under bias.

Possible die-temperature proxies include:

- calibrated dark resistance versus temperature in a regime where the relation is stable;
- a dedicated witness thermometer/test structure;
- another independently qualified local method.

Report method and uncertainty.

---

# 15. Interconnect selection

RP-01 top metal is Cr/Au. This does not establish historical wire metallurgy or bond method.

Primary HgCdTe literature contains multiple other contact/interconnect architectures, including indium solder and Mo/Au-Ge systems. These are **not** substitutes for the qualified RP-01 Cr/Au interface.

For every interconnect trial record:

- wire/ribbon material;
- diameter/thickness;
- bonder model;
- wedge/capillary/tool ID;
- bond mode;
- stage temperature;
- force;
- ultrasonic amplitude/power;
- ultrasonic duration;
- loop geometry;
- pad location;
- pad pre-clean, if any;
- measured continuity/resistance;
- visual failure mode.

No force/ultrasonic setpoint is released from the Honeywell 5-g/40-g thermocompression cracking experiment.

---

# 16. Contact/interconnect stress-noise rule

Other primary HgCdTe technologies demonstrate that contact/lead metallurgy and thermal expansion can alter cryogenic stress and excess noise.

P33 therefore requires a pre/post interconnect check on qualification structures:

- low-current I–V linearity;
- lead/contact resistance;
- P12 dark noise;
- microphonic response;
- change after thermal cycling.

Do not replace RP-01 Cr/Au with a supposedly lower-stress metallurgy without reopening P26/P24 contact qualification.

---

# 17. Optical package state

Record the installed optical geometry, not only a nominal FOV label:

- detector active-plane coordinates;
- aperture size/shape;
- detector-to-aperture distance;
- cold-shield material/finish;
- window material/thickness/coating;
- detector-to-window distance;
- filter identity;
- measured or traceable `T_window(lambda)` and `T_filter(lambda)`;
- vignetting/alignment.

A nominal `60° FOV` is not a geometrical specification. P11 must use the measured package geometry/throughput.

---

# 18. Vacuum and package thermal budget

Record:

- pump/purge sequence;
- pressure measurement method;
- pressure before cooldown;
- leak/outgassing evidence;
- getters where used;
- bake temperature/time;
- time from pumpdown to test.

A vacuum bake is a detector process operation. It may change passivation/interface/contact state and must remain inside a P15/P33-qualified thermal budget.

The thin-HgCdTe stress literature is an explicit warning that package heating can harden/alter adhesives and amplify cooldown stress.

---

# 19. Thermal-cycle qualification

Each package construction must retain cycle genealogy:

- cycle number;
- warm-end temperature;
- cold-end temperature;
- ramp/cooldown history;
- dwell at endpoints;
- atmosphere/vacuum state;
- any interruption or abnormal event.

After selected cycle intervals inspect/measure:

- die cracks/chip growth;
- delamination/void change;
- wire/bond damage;
- contact resistance;
- detector resistance/I–V;
- P12 noise;
- thermal transient response;
- optical alignment.

Do not call multiple measurements from one repeatedly cycled package independent package replicates.

---

# 20. Package acceptance hierarchy

A candidate construction passes development only if it closes all four levels:

## Level 1 — mechanical

- no crack propagation;
- no delamination/lift;
- no unacceptable die shift/tilt;
- stable interconnect.

## Level 2 — electrical/noise

- no unacceptable contact/lead resistance change;
- no new rectification;
- no package leakage/ground loop;
- no material microphonics or excess noise.

## Level 3 — thermal

- acceptable `R_theta,eff`;
- reproducible transient kernel;
- package poles identified sufficiently for P10/P13 interpretation.

## Level 4 — optical/device

- stable throughput/FOV;
- no unacceptable responsivity shift;
- P12/P13 detector performance remains consistent with the pre-package state after package transfer functions are accounted for.

No construction is released solely from die shear or wire pull.

---

# 21. P33 qualification register outputs

Every package qualification build shall produce:

- complete pre-package baseline;
- carrier/cold-finger geometry record;
- attachment genealogy;
- measured bondline state;
- interconnect genealogy;
- vacuum/optical geometry;
- initial 80-K electrical/noise state;
- thermal pulse/recovery data;
- thermal-cycle genealogy;
- post-cycle electrical/noise/thermal/optical state;
- failure classification;
- process disposition.

---

# 22. Current historical blockers

Still `OPEN` for RP-01:

- exact die outline/singulation;
- die attach identity;
- bondline thickness;
- carrier/cold-finger construction;
- cure schedule;
- wire/ribbon metallurgy;
- bond tool/setpoints;
- Dewar/header/window;
- aperture/FOV construction;
- vacuum level/bake;
- thermal-cycle history.

The same-Honeywell silicone-rubber branch and NRL HgCdTe photoconductor thermal stack are strong empirical transfer evidence, not historical closure.

---

# 23. Primary sources

1. T. T. S. Wong, Honeywell Inc., US4081819A, “Mercury cadmium telluride device,” filed 17 Jan 1977, published 28 Mar 1978. Cryogenic substrate-cracking study; silicone-rubber attachment; Dow Corning 3110/3112/3116 examples; controlled 5-g/40-g thermocompression conditions.
2. US4012691A, U.S. Navy, “Determination of thermal impedances of bonding layers in infrared photoconductors,” filed 8 Apr 1976, published 15 Mar 1977. HgCdTe crystal/epoxy/Irtran-2-or-sapphire/GE-7031/copper-heat-sink stack at 77 K; pulse-recovery method.
3. F. J. Bartoli, L. Esterowitz, M. R. Kruer, R. E. Allen, “Thermal recovery processes in laser irradiated HgCdTe (PC) detectors,” *Applied Optics* 14, 2499–2507 (1975), DOI `10.1364/AO.14.002499`.
4. US5462882A, “Masked radiant anneal diffusion method.” Thin 5–10-µm HgCdTe/epoxy/Si thermomechanical-mismatch warning.
5. US5365088A, Santa Barbara Research Center, “Thermal/mechanical buffer for HgCdTe/Si direct hybridization.” Sapphire CTE-buffer and repeated cryogenic-cycle reliability evidence.
6. J. F. Siliquini and L. Faraone, “Two-Dimensional Infrared Focal Plane Arrays Based on HgCdTe Photoconductive Detectors,” *Semiconductor Science and Technology* 11, 1906–1911 (1996), DOI `10.1088/0268-1242/11/12/024`.

---

# 24. Release status

P33 remains `PRE-RELEASE` until a locally selected construction demonstrates repeatable:

- cryogenic mechanical survival;
- controlled bondline state;
- stable interconnect;
- measured package thermal response;
- acceptable self-heating;
- no material noise penalty;
- optical throughput closure;
- reproducibility across independent package builds.

Do not infer production tolerances from literature spread alone.
