# P35 — HgCdTe/CdZnTe singulation and die-edge empirical process window

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Control the transition from a completed RP-01-like HgCdTe/CdZnTe device wafer/coupon to an individually handled package-ready die without introducing hidden mechanical, chemical, electrical, optical or cryogenic damage.

P35 supplements:

- `P15_DIE_ATTACH_INTERCONNECT_CRYOGENIC_PACKAGE_QUALIFICATION.md`, especially its generic die-separation section;
- `P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`, Phase G STEP G1;
- `P33_CRYOGENIC_DIE_ATTACH_INTERCONNECT_EMPIRICAL_PROCESS_WINDOW.md`, whose input state is already-singulated die.

This is a genuine fabrication operation. It is not treated as a neutral handling step.

The controlled chain is:

`completed frontside device -> pre-singulation baseline -> protection/support -> cut/scribe/ablate -> die release -> residue removal/clean -> edge/subsurface inspection -> electrical/noise check -> P33 package build -> cryogenic survival check`.

---

# 2. Historical RP-01 state

Smith et al. 2001 do not disclose the recovered RP-01 singulation traveler.

The following remain `OPEN-HISTORICAL`:

- whether devices were diced before or after the reported final electrical/optical characterization;
- saw versus wire saw versus scribe/cleave versus laser;
- tool model;
- blade/wire material, grit, bond and dimensions;
- spindle/wire speed;
- feed/downfeed;
- number/depth of passes;
- coolant/slurry;
- mounting tape/wax/fixture;
- frontside protection;
- cut-street location;
- die outline;
- post-cut cleaning;
- post-cut chemical damage removal;
- edge exclusion from active detector;
- pre/post-singulation electrical/noise verification.

Therefore no specific singulation setpoint may be labeled `DIRECT-RP01` until documentary evidence is recovered.

---

# 3. Evidence classes

Use these labels explicitly:

- `DIRECT-RP01-SINGULATION` — direct Smith/UWA RP-01 traveler evidence; currently none recovered.
- `PRIMARY-HGCDTE-DICING-TRANSFER` — primary HgCdTe detector-array or HgCdTe/CdTe dicing evidence from another architecture.
- `PRIMARY-CZT-SINGULATION-TRANSFER` — primary CdZnTe detector cutting/dicing evidence.
- `PRIMARY-II-VI-LASER-SURFACE-TRANSFER` — primary CdTe/HgCdTe/CdZnTe laser-ablation evidence relevant to chemical/surface risk.
- `GENERIC-HARD-BRITTLE-TRANSFER` — other semiconductor machining evidence; may inform experiment design but cannot release RP-01 setpoints.
- `LOCAL-QUAL` — locally demonstrated on the actual or faithful HgCdTe/CdZnTe device stack.

Transfer values are experimental evidence, not an executable RP-01 recipe by themselves.

---

# 4. Why a separate P35 is required

P15 correctly requires die-edge inspection but leaves the actual separation method open. P16 STEP G1 merely points to P15. P33 assumes a fabricated die has already arrived in a known singulation/clean state.

This creates an otherwise uncontrolled process gap.

Singulation can change:

- visible edge chipping;
- subsurface crack depth;
- microcrack propagation during cooldown;
- passivation integrity;
- exposed HgCdTe/CdZnTe edge chemistry;
- particle/residue load;
- contact-pad condition;
- detector resistance/leakage;
- 1/f/excess noise;
- responsivity;
- package mechanical survival.

A visually intact die is therefore not sufficient release evidence.

---

# 5. Primary HgCdTe dicing evidence — mechanical-saw versus excimer branch

Pierino I. Zappella / Rockwell International, US5214261, “Method and apparatus for dicing semiconductor substrates using an excimer laser beam,” filed 1991, issued 1993, is direct HgCdTe detector-array dicing evidence.

The patent states that the conventional method then used for substrates/circuitry such as **mercury cadmium telluride or sapphire wafers** employed a diamond-grit blade dicing saw of the type used for silicon. It identifies practical problems including:

- difficulty holding exact die tolerances;
- chipping/fracturing;
- localized frictional heating;
- degradation of electrical components;
- difficulty obtaining multiple straight/orthogonal buttable HgCdTe detector-array edges.

Its excimer branch uses deep-UV ablative photodecomposition and reports:

- preferred XeCl excimer source near `308 nm`;
- substrate/beam orientation several degrees out of normal, preferred approximately `5°`, to compensate taper;
- one illustrated cut approximately `25 µm` wide;
- optional partially cured polyimide protection in that sapphire/CdTe/HgCdTe architecture;
- detector-performance comparison before/after dicing as a function of distance from cut edge.

The patent interprets its data as mechanical-saw dicing requiring roughly `9–19 µm` clearance from detector pixel edge to avoid measured degradation in its tested array, while its excimer branch could approach about `0–6 µm` in that architecture.

### P35 interpretation

This source establishes three important principles:

1. **functional edge damage can extend beyond visible kerf/chipping**;
2. a pre/post detector metric versus edge distance is an appropriate qualification method;
3. non-contact dicing can reduce mechanical damage in some HgCdTe architectures.

It does **not** establish an RP-01 cut clearance, laser recipe or permitted protection chemistry because the patented stack is a sapphire/CdTe/HgCdTe focal-plane architecture, not an LPE HgCdTe/CdZnTe photoconductor.

The `9–19 µm` and `0–6 µm` values are retained as `PRIMARY-HGCDTE-DICING-TRANSFER`, never as P35 production limits.

---

# 6. Laser dicing is not automatically chemically benign

P. D. Brewer and J. J. Zinck / Rockwell, US5018164, “Excimer laser ablation method and apparatus for microcircuit fabrication,” provides direct II–VI evidence that excimer ablation can alter surface composition.

The source discusses CdTe/HgCdTe/CdZnTe and demonstrates for CdTe that ablation rate and resulting Cd/Te surface ratio depend on:

- wavelength;
- fluence;
- pulse duration;
- number of pulses.

Its CdTe example used KrF `248 nm`, `30 ns` pulses and showed fluence-dependent preferential removal / residual stoichiometry.

It also cites earlier HgCdTe excimer work in which severe local damage and mercury nodules occurred under unsuitable irradiation conditions.

### Permanent P35 laser rule

`non-contact != non-damaging`.

Any laser/excimer P35 branch must qualify:

- kerf/edge geometry;
- redeposition/debris;
- heat-affected or modified zone;
- near-edge Hg/Cd/Te chemical state where practical;
- passivation/metal damage;
- detector electrical/noise/responsivity state versus distance from edge.

Do not transfer the CdTe `248 nm / 30 ns / fluence` values as an HgCdTe/CdZnTe dicing recipe.

---

# 7. Primary CdZnTe finished-array wire-saw branch

S. S. Yoo, G. Jennings, P. A. Montano, “CdZnTe Array Detectors for Synchrotron Radiation Applications,” *Journal of Synchrotron Radiation* 5, 1332–1336 (1998), DOI `10.1107/S0909049598007237` gives unusually concrete singulation details on a metallized CdZnTe detector sample.

Direct process facts:

- starting detector sample approximately `1×1 cm`;
- after metallization, mounted on a graphite substrate using **low-melting-point wax**;
- photoresist applied over the whole surface to protect delicate CdZnTe;
- cut with a `125 mm` diameter stainless-steel wire saw;
- abrasive: `16 µm` boron nitride slurry;
- cutting performed extremely slowly to minimize edge chipping/wall damage;
- one complete cut took approximately `1 h`;
- afterwards the authors used `5% Br in methanol for 5 min` to etch wall damage, followed by trichloroethylene, acetone and methanol cleaning.

### P35 interpretation

The wire-saw/support/protection facts are valuable `PRIMARY-CZT-SINGULATION-TRANSFER` data.

However, the post-cut `5% Br/methanol / 5 min` process is **not an allowed default for a completed RP-01 die**. RP-01 has only about `9.5 µm` active HgCdTe plus anodic oxide, RIE-defined contact regions and Cr/Au metallization. A strong whole-die bromine etch could materially remove/alter the active semiconductor, passivation and contact geometry.

Likewise, wax, photoresist, boron-nitride slurry and the stated cleaning solvents require local compatibility qualification before contact with a completed RP-01 device.

---

# 8. Primary CdZnTe saw-damage depth warning

C. Szeles et al., “Fabrication of high performance CdZnTe quasi-hemispherical gamma-ray CAPture Plus detectors,” Proc. SPIE 6319, 631909 (2006), DOI `10.1117/12.683552`, describes production CdZnTe crystal mining and device fabrication.

The author-provided full text states that:

- low-damage high-precision wire-saw slicing/dicing still required removal of approximately a `100 µm` surface layer in their crystal fabrication flow to eliminate surface/subsurface saw damage;
- conventional blade slicing/dicing was described as producing deeper damage that could require **several hundred micrometres** of removal.

### P35 interpretation

These are bulk-CdZnTe crystal fabrication values, not finished-RP-01 post-device etch allowances.

They establish that:

**visible edge morphology does not bound subsurface damage depth.**

A completed RP-01 die cannot simply remove `100 µm` from its active edge after dicing without a separately designed exclusion geometry/process. Therefore P35 must control damage by the singulation operation itself and by sufficient sacrificial street/edge exclusion, not assume deep post-cut chemical removal is available.

---

# 9. Candidate process branches

P35 permits controlled screening of the following branches.

## Branch A — precision abrasive blade saw

Potential advantages:

- mature dicing hardware;
- controlled straight kerf and die geometry;
- high throughput after qualification.

Risks:

- edge chipping/fracture;
- subsurface damage;
- local mechanical/thermal stress;
- slurry/coolant contamination;
- metal/passivation damage;
- tool wear/dressing dependence.

No blade type, grit, bond, spindle speed, feed, cut depth or coolant is released from silicon practice.

## Branch B — wire saw / low-force abrasive cut

Supported by direct CdZnTe detector evidence.

Potential advantages:

- lower local force/damage than some blade processes;
- controlled material removal with suitable fixture.

Risks:

- slow process;
- abrasive slurry contamination;
- wire wander/bow;
- edge chipping;
- subsurface damage remains possible;
- protection/mount removal may attack completed device surfaces.

## Branch C — scribe and cleave

Potential advantages:

- low contamination;
- no coolant/slurry;
- simple apparatus for suitable crystal planes.

Risks:

- crack path depends on crystallography, polarity, miscut, defect population and substrate geometry;
- orthogonal rectangular die may not cleave equally well in both directions;
- uncontrolled crack branching/chipping;
- force transmission into brittle HgCdTe/CdZnTe stack.

P29 plane/polarity/miscut and defect genealogy must accompany this branch.

## Branch D — laser/excimer separation

Supported by direct HgCdTe detector-array transfer evidence.

Potential advantages:

- low mechanical cutting force;
- narrow kerf/close edge approach possible in some architectures;
- programmable geometry.

Risks:

- stoichiometry modification;
- redeposition/nodules;
- thermal/photochemical damage;
- taper;
- protection-film compatibility;
- possible oxide/metal damage.

Laser source parameters are separate qualification coordinates; no Rockwell setting is an RP-01 default.

---

# 10. Incoming device-stack state

Before any P35 trial, record:

- wafer/coupon/device ID and exact wafer coordinate;
- CdZnTe substrate thickness;
- substrate plane/polarity/miscut from P29;
- HgCdTe active thickness and P06/P06A state;
- mesa/passivation process revision;
- RIE/contact process revision;
- Cr/Au state;
- front/back surface state;
- device/contact geometry;
- nearest active/contact/passivated feature to each planned cut;
- existing chips/scratches/cracks;
- optical micrographs of all planned streets/edges;
- available pre-singulation P10 resistance/I–V;
- available P12 noise and P11 responsivity on qualification devices.

If a performance baseline cannot be measured before singulation because of fixture geometry, use matched witness devices and explicitly mark the reduced diagnostic power.

---

# 11. Street and edge-exclusion geometry

For every cut define:

- planned cut centerline;
- nominal kerf;
- allowed centerline-position error;
- minimum intended distance from kerf edge to:
  - mesa edge;
  - exposed HgCdTe sidewall;
  - contact window/n+ region;
  - Cr/Au pad;
  - wire-bond area;
  - optical active region;
- die final length/width target;
- whether edge is intended to become package locating datum.

Define separately:

`d_visible` = distance from active feature to visible kerf/chip boundary;

`d_functional` = minimum distance shown by pre/post device testing to avoid measurable degradation;

`d_release` = locally released design exclusion, including uncertainty and margin.

Do not set `d_release = d_visible` automatically.

---

# 12. Process-vector record

For each candidate run record the realized singulation state:

`X_SING = {method, tool/revision, cut orientation, protection, support/fixture, abrasive/laser state, motion state, coolant/slurry, pass sequence, tool age/conditioning, clean/release sequence, handling/pickup}`.

## 12.1 Abrasive saw/wire fields

Record where applicable:

- saw/wire machine model/serial;
- blade/wire manufacturer/product/lot;
- blade/wire material;
- abrasive species;
- nominal abrasive grit/size;
- bond type;
- blade/wire diameter/thickness;
- exposed blade/flange geometry;
- spindle/wire speed;
- feed rate;
- downfeed/cut depth;
- skim versus through-cut sequence;
- number of passes;
- entry/exit direction;
- dressing/conditioning state;
- accumulated cut length/time since new/dress;
- measured runout/wander where available.

Tool age and dressing are genealogy variables.

## 12.2 Laser fields

Record where applicable:

- laser type/wavelength;
- pulse duration;
- repetition rate;
- pulse energy/fluence at sample;
- spot/line dimensions;
- overlap/scanning velocity;
- number of passes;
- focus/defocus;
- beam incidence angle;
- atmosphere/pressure;
- debris extraction;
- protection coating.

## 12.3 Coolant/slurry fields

Record:

- chemistry/product/lot;
- abrasive concentration if slurry;
- resistivity/pH/conductivity where relevant;
- flow rate;
- temperature;
- filtration;
- recirculated versus fresh;
- bath/run history;
- exposure duration after cut completion.

---

# 13. Protection and temporary mounting

Any protection/support material is part of the process.

Record:

- product/lot;
- surface covered;
- coating thickness where applicable;
- bake/cure;
- mounting force;
- wax/tape/adhesive state;
- removal chemistry/time/temperature;
- residue inspection;
- elapsed time to cleaning/attach.

The Yoo 1998 photoresist + low-melting wax branch and Rockwell polyimide branch are transfer evidence only.

### Prohibitions

- no protective polymer is assumed compatible with anodic oxide/Cr/Au without local test;
- no ultrasonic removal/cleaning is a default P35 operation;
- no hot strip or plasma ash is inserted after final device fabrication without reopening surface/contact qualification.

---

# 14. Cutting sequence and sacrificial development

Initial process transfer should use, in order:

1. bare CdZnTe coupons of representative thickness;
2. HgCdTe/CdZnTe material witnesses where available;
3. metallized/passivated noncritical device-process coupons;
4. fully processed qualification devices;
5. production-intended devices only after branch release.

This prevents optimization directly on scarce detector die while still requiring eventual validation on the real completed stack.

At least one sacrificial cross-section/destructive specimen should be included during development to examine damage that is not visible from the top surface.

---

# 15. Immediate post-cut handling and cleaning

Record the exact sequence from tool stop to clean completion.

Control:

- time wet in coolant/slurry;
- transfer ambient;
- rinse chemistry;
- solvent identity/grade;
- rinse count/time;
- agitation;
- drying method;
- fixture/tape/wax removal;
- particle handling;
- tweezers/vacuum pickup/contact point;
- clean-to-attach storage/ambient.

The finished RP-01 device contains HgCdTe, native/anodic oxide, RIE-modified regions and Cr/Au. Cleaning must preserve all of them.

### No deep bromine damage-removal default

Br2/methanol damage-removal etches from bulk CdZnTe processing are not automatically compatible with a completed RP-01 device. Any chemical edge-treatment branch requires a separate material-removal budget and requalification of passivation/contact/device state.

---

# 16. Edge and subsurface metrology

Inspect every released die at minimum by calibrated optical microscopy.

Record separately for every edge/corner:

- frontside chip maximum lateral extent;
- backside chip maximum lateral extent;
- chip depth where measurable;
- longest visible crack;
- crack direction;
- corner breakout;
- kerf/edge roughness metric;
- edge taper/angle where relevant;
- die dimension and squareness;
- contamination/residue;
- passivation damage;
- metal-pad/contact damage.

Development methods may additionally include:

- cross-sectional optical/SEM examination on sacrificial samples;
- IR transmission imaging where cracks/inclusions are visible;
- confocal/profilometric edge mapping;
- another validated subsurface-damage method.

### Permanent rule

`no visible chip != no subsurface damage`.

---

# 17. Functional edge-damage test

Mechanical metrology alone does not release P35.

For qualification devices compare pre/post singulation, where feasible:

- resistance at fixed T and low field;
- I–V symmetry/nonlinearity;
- contact/lead continuity;
- P12 ASD at selected frequencies;
- 1/f/excess-noise signature;
- one P11 responsivity point or normalized optical response;
- leakage/isolation relevant to device geometry.

Across an edge-clearance experiment, plot each functional change versus measured distance from cut edge.

Example normalized metrics:

`r_R = R_post / R_pre`

`Delta_e(f) = e_post(f)/e_pre(f) - 1`

`r_resp = Rv_post / Rv_pre`

The Rockwell pre/post `R0` edge-distance experiment is the historical transfer precedent for this logic.

---

# 18. Cryogenic edge-survival closure

Microcracks that appear acceptable at room temperature can propagate under package stress/cooldown.

P35 therefore has two release levels:

### `SINGULATION-ROOM-TEMP-QUALIFIED`

Passed immediate geometry/edge/clean/electrical gates before die attach.

### `RP01-SINGULATION-QUALIFIED`

Requires later P33 closure showing:

- no edge-chip/crack growth after intended cooldown/warmup qualification;
- no package-induced fracture initiating at cut edge;
- no correlated electrical/noise/responsivity degradation;
- acceptable die position/attach behavior.

P33 feeds this result back to the P35 genealogy record.

---

# 19. Experimental process-window DOE

The purpose of P35 development is to locate a reproducible low-damage window, not to select the fastest cut.

For an abrasive branch, candidate controlled factors may include:

- abrasive size/class;
- blade/wire family;
- feed;
- spindle/wire speed;
- pass/depth strategy;
- coolant/slurry state;
- support/protection state;
- cut orientation relative to crystallography.

For a laser branch:

- wavelength/source family;
- fluence;
- repetition/overlap;
- scan speed;
- focus;
- pass count;
- incidence angle;
- protection/debris-control state.

Do not assign arbitrary coded-factor levels as physical production specifications. Initial ranges must come from tool/material compatibility testing and primary evidence.

---

# 20. Outcome vector

Use a combined response vector:

`Y_SING = {kerf_width, position_error, die_L/W, squareness, chip_front, chip_back, crack_length/depth, subsurface_damage, edge_roughness/taper, residue/particles, pad/passivation_damage, Delta_R/I-V, Delta_noise, Delta_responsivity, cryogenic_edge_survival}`.

Optimize against the complete vector.

A process with excellent dimensional accuracy but degraded noise fails.

A process with low visible chipping but hidden crack propagation during cooldown fails.

---

# 21. First local qualification sequence

1. Define device stack and planned streets.
2. Record P29 crystallography and P06 thickness state.
3. Acquire pre-cut micrographs and available electrical/noise baseline.
4. Qualify temporary protection/support on process coupons.
5. Execute candidate cut with complete `X_SING` record.
6. Record actual kerf/position/dimensions.
7. Clean/release using the candidate qualified sequence.
8. Inspect all four edges and corners.
9. Destructively inspect selected witnesses for subsurface damage.
10. Repeat electrical/noise/optical baseline on qualification devices.
11. Compare output versus edge clearance and process variables.
12. Advance only acceptable die to P33.
13. Perform package/cooldown qualification.
14. Feed cryogenic edge survival back to P35.
15. Freeze tool, protection, clean and handling revision only after repeated successful runs.

---

# 22. Failure modes and diagnostic signatures

## Excess frontside chipping

Investigate:

- unsupported exit/entry condition;
- feed/downfeed;
- blade/wire/grit state;
- fixture/tape support;
- cut direction/orientation;
- tool runout/wander.

## Excess backside chipping

Investigate support, breakthrough/pass strategy, cutting direction and substrate thickness.

## Long edge cracks with little chipping

Do not treat as cosmetic success. Investigate brittle crack propagation, crystallographic orientation, fixture stress and abrasive loading.

## Good visual edge but increased low-frequency noise

Investigate hidden mechanical damage, sidewall/passivation disturbance, contamination/residue, contact damage and package/readout state before blaming intrinsic detector physics.

## Good room-temperature result but fracture on cooldown

Investigate singulation microcrack seed + P33 attachment/CTE stress jointly. Do not assign the failure solely to die attach.

## Laser branch shows clean edge but electrical shift

Investigate near-edge stoichiometry, redeposition, surface damage, metal/passivation interaction and thermal/photochemical modification.

## Wire/saw branch leaves residue

Investigate slurry/coolant chemistry, temporary-mount removal, clean sequence and dwell time before introducing stronger cleans.

---

# 23. P18 escalation logic

Any post-singulation failure should enter P18 with at least competing hypotheses from:

- singulation mechanical damage;
- singulation chemical/residue damage;
- pre-existing wafer defect;
- contact/passivation defect;
- die-attach/package stress;
- measurement/readout artifact.

Use pre-cut baseline, edge map and matched witnesses to discriminate them.

Do not collapse “edge chip” and “package crack” into one cause without evidence.

---

# 24. Release blockers

P35 remains pre-release until the selected local branch closes:

1. actual RP-01-like device-stack geometry and street/exclusion;
2. selected singulation branch/tool;
3. protection/support compatibility;
4. complete tool-state/process vector;
5. coolant/slurry/laser-debris control;
6. post-cut clean and residue limit;
7. measured dimensional accuracy;
8. visible edge-chip/crack method and acceptance;
9. subsurface-damage qualification method;
10. functional pre/post electrical/noise acceptance;
11. edge-clearance criterion based on local functional data;
12. package/cooldown crack-survival closure;
13. repeated-run/tool-wear reproducibility;
14. final handling/pickup and clean-to-attach control.

No generic semiconductor dicing recipe may close these blockers.

---

# 25. Primary references

1. P. I. Zappella, Rockwell International, US5214261, “Method and apparatus for dicing semiconductor substrates using an excimer laser beam,” filed 1991, issued 1993. Direct HgCdTe detector-array dicing / edge-performance transfer evidence.
2. P. D. Brewer, J. J. Zinck, Rockwell International, US5018164, “Excimer laser ablation method and apparatus for microcircuit fabrication,” issued 1991. Primary CdTe/HgCdTe/CdZnTe laser-ablation and surface-stoichiometry transfer evidence.
3. S. S. Yoo, G. Jennings, P. A. Montano, “CdZnTe Array Detectors for Synchrotron Radiation Applications,” *J. Synchrotron Rad.* 5, 1332–1336 (1998), DOI `10.1107/S0909049598007237`.
4. C. Szeles, D. Bale, J. Grosholz Jr., G. L. Smith, M. Blostein, J. Eger, “Fabrication of high performance CdZnTe quasi-hemispherical gamma-ray CAPture Plus detectors,” Proc. SPIE 6319, 631909 (2006), DOI `10.1117/12.683552`.
5. E. P. G. Smith et al., *Semicond. Sci. Technol.* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306` — canonical RP-01; singulation method not recovered in the audited text.

---

# 26. Current conclusion

The historical RP-01 singulation method remains open, but the empirical control problem is now sufficiently defined to execute a local qualification without inventing a historical blade recipe.

The strongest practical conclusions are:

- finished II–VI devices require protection/support/clean compatibility testing, not only cutting optimization;
- low-force wire sawing is directly documented on finished CdZnTe detector structures;
- mechanical-saw damage can extend functionally beyond visible kerf in HgCdTe arrays;
- subsurface damage may be far deeper than visible chipping suggests;
- deep Br damage-removal methods from bulk CdZnTe cannot be transplanted onto a completed 9.5-µm HgCdTe photoconductor;
- laser separation trades mechanical damage for possible chemical/stoichiometric damage and requires its own qualification;
- final release requires cryogenic survival after P33, not room-temperature edge appearance alone.
