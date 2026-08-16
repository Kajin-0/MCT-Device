# P28 — HgCdTe wet-mesa empirical process window

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Turn the existing P01/P01A wet-mesa branch into a practical, literature-grounded qualification method for the RP-01 x≈0.30 n-HgCdTe photoconductor while preserving the central formulation ambiguity instead of hiding it.

RP-01 directly establishes only that the device mesa is delineated by wet chemical etching before anodic oxidation. A same-UWA x=0.31 photoconductor comparison establishes bromine/HBr wet mesa processing as a successful device branch. The most quantitative near-composition mesa study is Srivastav et al. on x=0.28 HgCdTe using nominal `2% Br2` in `3:1 EG:HBr`.

The practical chain controlled by P28 is:

`incoming HgCdTe + Mask-1 -> explicitly defined etchant genealogy -> measured bath T/age/agitation -> vertical + lateral etch state -> electrical isolation -> surface chemistry/air exposure -> P25 passivation handoff`.

P28 supplements P01/P01A. It does not claim to reconstruct an unpublished RP-01 wet-etch traveler.

---

# 2. Evidence classes

## `DIRECT-RP01`

Directly stated in the canonical Smith et al. 2001 detector paper.

## `SAME-UWA-WET-MESA`

Same UWA/Faraone HgCdTe photoconductor lineage demonstrating a bromine/HBr wet-mesa branch and device-level performance.

## `PRIMARY-X028-MESA`

Srivastav et al. 2005 systematic x=0.28 Br2/HBr/EG mesa study.

## `PRIMARY-CONVENTION-TRANSFER`

Primary HgCdTe etch papers/patents that explicitly define a bromine concentration convention, rinse or process sequence, but are not the Srivastav/RP-01 formulation.

## `PRIMARY-SURFACE-TRANSFER`

Primary HgCdTe surface-analysis work establishing surface-chemistry/air-exposure consequences of Br-based etching.

## `LOCAL-QUAL`

A locally defined and measured condition used because the historical parameter is not recoverable.

No transfer value may be relabeled as `DIRECT-RP01` or `PRIMARY-X028-MESA` merely because it appears compatible.

---

# 3. Historical RP-01 and same-UWA function

## 3.1 `DIRECT-RP01`

The canonical process uses wet chemical mesa delineation before native anodic-oxide passivation.

The recovered RP-01 paper does not provide:

- etchant identity/formulation;
- bromine concentration;
- HBr concentration;
- temperature;
- etch duration;
- agitation;
- rinse/quench;
- endpoint/overetch;
- Mask-1 resist process.

## 3.2 `SAME-UWA-WET-MESA`

Smith et al. 2000 directly compared n-type x=0.31 HgCdTe photoconductors mesa-etched by:

- H2/CH4 RIE; versus
- wet chemical etching using bromine in hydrobromic acid.

At 80 K, 3-µm signal wavelength and stated 60° field of view, the wet-chemical devices reached background-limited performance with reported `D_lambda*≈2.5×10^11 cm Hz^1/2 W^-1`, whereas the dry-plasma branch was approximately `1.0×10^10` in the reported experiment.

The same lineage also reported that bromine-based chemical mesa etching caused no significant LBIC-detectable electrical modification compared with strong RIE-induced modification.

### P28 consequence

Wet chemical mesa processing is not merely a chemically plausible transfer process; it is directly supported by same-UWA detector-performance evidence close to the RP-01 material composition.

The exact UWA wet chemistry still remains open.

---

# 4. Strongest quantitative transfer center — Srivastav x=0.28

Srivastav et al. systematically varied:

- nominal Br2 concentration from `1%` to `3%`;
- fraction of EG in HBr from `0` to `1`;
- temperature from `5 °C` to `50 °C` for the selected chemistry.

The selected formulation was reported as:

`2% Br2 in 3:1 EG:HBr`

and in a figure caption as:

`2% Br2 + 75% EG + 25% HBr`.

At/near 21 °C, important measured values include:

- mean vertical etch rate `R_V≈2.78 µm/min` in preliminary process-uniformity work;
- approximately `±26%` run/process variation in mean etch rate;
- mean anisotropy `A≈0.63` with approximately `±11%` variation;
- best RMS roughness near `~2 nm` for the high-EG/selected formulation, with investigated roughness approximately `2–7 nm`;
- apparent activation energy `~7.5 kcal/mol`;
- etch rate approximately doubling for each `+10 °C` increase over the studied regime;
- lower-temperature etching giving better feature control and less photoresist attack;
- a 10 °C SEM example showing improved geometric control relative to the 21 °C example.

Anisotropy is defined by the paper as:

`A = 1 - R_L/R_V`,

where `R_L` and `R_V` are lateral and vertical etch rates.

### Critical restriction

These are x=0.28 transfer values. They are not exact x≈0.30 RP-01 process limits.

---

# 5. The `2% Br2` formulation basis remains OPEN — and must remain so

The full accessible Srivastav article repeatedly states `1–3% Br2` and the selected `2% Br2`, but does not provide:

- bromine mass;
- bromine volume;
- final solution mass/volume;
- molarity;
- `w/w`, `w/v`, `v/v`, mole fraction or another explicit basis.

This cannot be repaired by assuming a historical convention.

## 5.1 Primary evidence that HgCdTe bromine conventions were not uniform

Leech, Gwynn and Kibel (1989) explicitly describe a comparison HgCdTe etchant as:

`0.1% (w/w) Br:HBr`.

A later HgCdTe mesa patent, CN101740502B, explicitly defines its Br2:HBr process by **volume ratio** (`0.1–1% : 1`).

A separate HgCdTe surface-preparation patent, US4436580A, explicitly defines a bromine/methanol example as `2% bromine / 98% solution (V/V)`.

Therefore at least weight/weight and volume/volume conventions both exist in primary HgCdTe process literature.

### Permanent P28 rule

**Never translate Srivastav `2% Br2` into grams, milliliters, molarity or mass fraction unless the exact basis is recovered.**

---

# 6. The `3:1 EG:HBr` preparation basis is also not fully closed

The accessible primary paper reports the ratio and describes the selected mixture as 75% EG / 25% HBr, but it does not provide an explicit preparation equation stating whether the liquid ratio is made by volume, mass or another laboratory convention.

Therefore preserve the source notation:

`EG:HBr = 3:1`

until the exact preparation convention is source-verified or locally defined under a new recipe ID.

Do not silently convert this to `75 mL EG + 25 mL HBr` and call it the published recipe.

---

# 7. HBr stock concentration remains OPEN

The Srivastav paper does not state the assay/concentration of the HBr stock used.

Because acid concentration changes:

- solution acidity;
- oxide/reaction-product dissolution;
- water content;
- viscosity and mass transport;
- the effective Br2/EG/HBr chemistry,

HBr assay is a first-class formulation variable.

For every local P28 recipe record:

- supplier;
- product/lot;
- certified HBr assay (`wt%`, molarity or equivalent as supplied);
- density where needed for an explicitly defined mass/volume preparation;
- stabilizer/impurity specification if supplied;
- bottle open date/storage state.

Do not assume `48% HBr` or another commercial stock concentration as historical fact.

---

# 8. Local formulation strategy if the historical basis remains inaccessible

A local process may be qualified without falsely identifying the Srivastav preparation, but the recipe must receive an explicit local identity.

Examples of allowed local branches:

- `P28-LOCAL-WW-*`: bromine fraction explicitly defined by mass of final solution;
- `P28-LOCAL-VV-*`: bromine fraction explicitly defined by liquid volume of final solution;
- other branch only with an explicit mathematical definition.

For each branch, separately define the EG:HBr mixing basis and the HBr stock assay.

### Important

The labels above define **local experiments**, not interpretations of what Srivastav meant.

Do not directly compare nominal `2%` branches as chemically equivalent. Their actual bromine molarity/free-bromine activity can differ, especially because HBr stock concentration and solvent density are additional variables.

---

# 9. Bath preparation genealogy

Because Br2 volatility was identified directly by Srivastav et al. as an important source of run-to-run drift, every etchant batch must have a genealogy.

Record:

- recipe ID and explicit concentration definitions;
- Br2 supplier/lot/purity;
- EG supplier/lot/purity/water specification;
- HBr supplier/lot/assay;
- individual reagent masses/volumes actually delivered;
- final solution mass/volume as defined by the recipe;
- vessel material/ID;
- covered/sealed/open state;
- mixing order;
- mixing duration/method;
- preparation start/end timestamp;
- bath temperature after mixing;
- elapsed time from preparation to first coupon;
- cumulative open-vessel exposure;
- number/order of samples etched;
- total exposed HgCdTe area;
- bath volume remaining;
- reuse history.

### Optional process-drift metrology

Where facility capability permits, add a calibrated analytical proxy for free bromine concentration and/or record sealed vessel + bath mass before and after use.

A mass change is only an evaporation diagnostic; it shall not be converted directly into bromine loss without a validated composition model or analytical measurement.

---

# 10. Mixing order remains OPEN

No recovered matched primary source closes the Srivastav reagent-addition sequence.

Mixing concentrated HBr, Br2 and EG can produce thermal and chemical transients, so mixing order is not an operator preference.

P28 therefore requires:

- institution-approved chemistry/EH&S procedure;
- explicit local mixing order in the recipe;
- temperature measured during/after preparation;
- no undocumented changes in order between qualification runs.

Different mixing orders are different local process branches until equivalence is demonstrated.

---

# 11. Bath temperature control

Temperature is one of the strongest empirically demonstrated process variables.

Srivastav studied `5–50 °C` and observed approximately a factor-of-two rate increase per `+10 °C` for the selected formulation, together with degraded edge/photoresist behavior at higher temperature.

### P28 first-transfer temperature hierarchy

- `21 °C` is the principal published quantitative reference point;
- `10 °C` is a published lower-temperature morphology example;
- neither is automatically the production optimum.

For every run record:

- bath temperature before immersion;
- bath temperature during etch where practicable;
- bath temperature immediately after removal;
- sensor ID/calibration;
- sample equilibration procedure;
- ambient cleanroom temperature.

Use bath/sample temperature, not room thermostat setpoint.

---

# 12. Agitation / mass transport

The Srivastav mechanism discussion explicitly identifies agitation, viscosity and reactant transport as kinetic variables and states that agitation of the viscous solution assists removal/transport of reaction products.

The accessible experimental text does **not** state the actual agitation method/rate used for the reported 2.78-µm/min result.

Therefore agitation remains `OPEN-HISTORICAL`.

Local recipes must state one reproducible mode, e.g.:

- static immersion;
- controlled holder motion;
- magnetic stirring with defined geometry/rate;
- another explicitly calibrated mode.

Do not label any one mode as the Srivastav condition unless primary evidence is recovered.

Because agitation changes the mass-transfer boundary layer, an agitation change invalidates direct use of a previously measured etch-rate calibration.

---

# 13. Pre-etch surface state

The x=0.28 primary source prepared material by:

1. wire-saw dicing;
2. sapphire mounting;
3. mechanical lap/polish with decreasing alumina grit;
4. chemomechanical polishing;
5. free etch in nominal `0.1% Br2 in methanol / 1 min`;
6. Nomarski + 6328-Å ellipsometry.

The authors used those checks to establish a surface without observable oxide/damage/contamination before patterned etching.

### RP-01 restriction

This aggressive bulk-material preparation sequence is not the RP-01 LPE device-surface recipe and shall not be transplanted automatically onto the 9.5-µm active epilayer.

P28 instead records the actual incoming P03/P04/P07/P14 surface history and requires a defined Mask-1 process state.

The source `0.1% Br2/methanol` concentration basis is itself not explicitly closed by that article.

---

# 14. Mask/test geometry for local etch calibration

The Srivastav primary study used:

- approximately `600 µm` long linear structures with `50 µm` trench width;
- two-dimensional mesa structures separated by `30 µm` trenches.

These are useful diagnostic geometry classes because they allow measurement of:

- vertical depth;
- lateral undercut;
- anisotropy;
- corner/profile effects.

P28 local calibration should include at least:

1. a step-depth witness;
2. a line/trench pattern for lateral etch;
3. representative RP-01 mesa geometry from the controlled mask set.

Do not calibrate a mesa process from blanket-film removal alone.

---

# 15. Initial etch-rate calibration — required before through-layer device etch

For each new combination of:

- formulation branch;
- reagent lots/assay where material;
- bath age class;
- temperature;
- agitation;
- material lot/composition;

establish local `R_V` and `R_L` on matched coupons.

Recommended empirical structure:

1. use multiple independently timed calibration features/coupons;
2. measure actual depth after etch;
3. regress depth against actual immersion time only over the locally observed linear regime;
4. report slope, intercept, residuals and uncertainty;
5. measure lateral undercut on the same chemistry/time regime;
6. compute `A=1-R_L/R_V` only with consistent definitions.

Do not force the regression through zero if the data show an induction/rinse/handling offset.

A single timed coupon is not a rate calibration.

---

# 16. Why `9.5/2.78 = 3.42 min` is not a mesa recipe

For dimensional context only:

`9.5 µm / 2.78 µm min^-1 ≈ 3.42 min`.

Using the reported ±26% rate spread gives a rough source-study timing span of approximately:

- fast edge ~`2.71 min`;
- slow edge ~`4.62 min`

to remove 9.5 µm before any required overetch or transfer shift.

This alone demonstrates that a fixed 3.42-min process cannot be justified from the literature.

### Permanent rule

**Time is a process input; isolation depth is the process output.**

Release requires measured through-layer isolation, not merely elapsed time.

---

# 17. Through-layer endpoint and overetch

RP-01 has approximately `9.5 µm` electrically active HgCdTe on an insulating CdZnTe substrate.

For mesa isolation, the conducting HgCdTe path between detector elements must be removed.

P28 distinguishes:

- `d_HgCdTe,in` — measured incoming active-layer thickness at/near the device;
- `d_etch` — measured vertical material removal;
- `d_over = d_etch - d_HgCdTe,in` when the substrate interface is crossed;
- `R_iso` or equivalent — measured electrical isolation metric.

No overetch fraction is currently released.

A local process must identify the smallest robust overetch/depth condition that provides complete electrical isolation while keeping:

- lateral undercut;
- sidewall morphology;
- CdZnTe attack;
- passivation compatibility

within the qualified window.

If an optical, electrical, interferometric or other in-situ endpoint is developed, it must be calibrated against physical depth and isolation before release.

---

# 18. Rinse / quench remains OPEN for the matched process

No recovered primary source closes the exact Srivastav or RP-01 Br2/EG/HBr post-etch rinse/quench sequence.

Other primary HgCdTe branches demonstrate that rinse practice is chemistry-specific:

- CN101740502B uses deionized-water cleaning after its Br2/HBr process;
- US4436580A uses methanol or DMF quenching for its bromine-methanol/DMF chemistries, followed by acetone/methanol and immediate N2 drying.

These processes are not interchangeable.

### P28 rule

Do not import DI water, methanol, acetone or another rinse into the Srivastav/RP-01 branch and call it historical.

The local rinse/quench sequence must:

1. be explicitly named by recipe ID;
2. stop continuing etch reproducibly;
3. remove residual Br/HBr/EG species;
4. avoid unacceptable surface roughening/residue;
5. produce a reproducible P25 anodization handoff.

Rinse-development experiments should be performed on sacrificial/matched coupons before device release.

---

# 19. Post-etch surface chemistry and air exposure

The Srivastav paper reports negligible apparent composition change by its ellipsometric `Psi` metric for the Br2/EG/HBr family, while Br2/HBr without EG showed a shift consistent with a probably Te-rich surface. The authors explicitly call that conclusion qualitative and identify XPS/AES as stronger surface methods.

Independent primary HgCdTe surface work shows that Br-based etchants can leave elemental Te and that subsequent air exposure changes oxidation and surface-recombination behavior.

Therefore the end of P28 is not simply “mesa depth passed.”

Record:

- etch-end timestamp;
- quench/rinse-end timestamp;
- dry timestamp/method;
- atmosphere and elapsed time until P25 anodization;
- Nomarski/optical morphology;
- representative AFM/profilometry roughness;
- optional XPS/AES/ellipsometry on qualification witnesses;
- P25 `V(t)`/induction signature as a downstream surface-state diagnostic.

Define:

`t_etch_to_P25 = t_P25_immersion - t_P28_etch_end`.

This interval becomes a controlled surface-history variable until local data demonstrate insensitivity.

---

# 20. Physical metrology after etch

At minimum measure:

## Vertical

- etch depth at multiple locations;
- depth uniformity;
- trench-floor morphology;
- residual HgCdTe if visible/measurable.

Srivastav used a Veeco Dektak 3 profiler for vertical measurements.

## Lateral

- top mesa CD;
- base/trench CD where resolvable;
- undercut per side;
- edge/corner asymmetry;
- `R_L` and anisotropy.

The source used high-magnification phase-contrast microscopy for undercut and SEM for profile examples.

## Surface/profile

- RMS roughness;
- sidewall smoothness;
- notch/trenching;
- convex trench-floor profile;
- resist erosion/attack;
- substrate-interface condition.

Do not reduce mesa quality to one mean etch rate.

---

# 21. Electrical isolation and material-preservation gate

For RP-01-compatible test structures measure, as appropriate:

- resistance/leakage between nominally isolated mesas at the intended operating temperature;
- room-temperature screening resistance where useful;
- Hall/VdP state on matched etched material;
- LBIC/spatial response if electrical modification is suspected;
- detector dark I–V after downstream passivation/contact processing.

Same-UWA data support wet chemical etching as substantially less electrically damaging than the compared RIE branch, but local isolation and electrical preservation must still be measured.

A mesa that looks geometrically complete but remains electrically connected fails P28.

---

# 22. Bath-loading / run-order experiment

Because the etchant contains volatile Br2 and is used to dissolve HgCdTe reaction products, initial qualification must test run order rather than assuming one batch is stationary.

For one fixed local formulation, temperature and agitation:

- prepare a fresh batch;
- process sequential matched coupons with known exposed area;
- record bath age and cumulative etched area before each coupon;
- measure `R_V`, `R_L`, roughness and surface outcome for each position in the sequence.

Responses should be modeled against:

- elapsed bath age;
- cumulative open-vessel time;
- cumulative exposed/etched area;
- run order.

Do not pool repeated coupons from one bath as independent etchant-batch replicates.

---

# 23. Temperature/process-transfer DOE

After the exact local formulation and bath-handling procedure are frozen, a practical first x≈0.30 transfer study should compare the source-anchored temperature neighborhood while preserving direct measurements.

Useful source-anchored levels include:

- `10 °C` — lower-temperature published morphology example;
- an intermediate local point if needed;
- `21 °C` — published quantitative reference condition.

This is a qualification design, not a claim that 10 °C or 21 °C is optimal.

For every condition measure:

- `R_V`;
- `R_L`;
- `A`;
- roughness;
- resist integrity;
- depth uniformity;
- sidewall/trench-floor morphology;
- electrical isolation;
- P25 surface/passivation handoff.

Avoid extending immediately to 50 °C on valuable RP-01-like material because the source directly reports greater resist/profile degradation at high temperature. High-temperature points are mechanism/bounding experiments, not necessary first-device centers.

---

# 24. Candidate process selection objective

Select the local P28 process by a multi-output requirement, not fastest etch rate.

A suitable center must jointly provide:

- robust through-layer isolation;
- low lateral CD loss;
- predictable anisotropy/profile;
- low roughness;
- intact Mask-1 resist until endpoint;
- no unacceptable electrical degradation;
- stable post-etch surface/passivation behavior;
- acceptable bath-age/run-order sensitivity.

The literature `~2.5–2.78 µm/min` result is a transfer benchmark, not the objective function.

---

# 25. Failure modes to preserve

Record and retain:

- unexplained etch-rate shift;
- rapid bath-age drift;
- excessive lateral undercut;
- edge trenching/notching;
- convex/non-flat trench floor;
- ragged sidewalls;
- photoresist attack/lift;
- nonuniform depth;
- incomplete isolation;
- excessive CdZnTe overetch/attack;
- increased surface roughness;
- Te-rich/oxidized surface evidence;
- post-etch surface instability with air time;
- anomalous P25 anodization `V(t)` after mesa etch;
- altered Hall/LBIC behavior;
- detector responsivity/noise regression.

Do not discard failed runs from process statistics without a documented assignable cause.

---

# 26. Safety hold point

Br2 and HBr are highly toxic/corrosive and volatile; HgCdTe contains Hg and Cd. EG is also hazardous. Exact solution preparation, exhaust, compatible vessels, PPE, exposure/spill controls and Hg/Cd/halogen waste routing must be authorized under institution-specific EH&S and equipment procedures.

P28 defines scientific process control and provenance. It is not a substitute for institutional chemical-hygiene authorization.

---

# 27. Current numerical status

## `DIRECT-RP01`

- wet chemical mesa occurs before anodic oxide;
- active HgCdTe thickness ~`9.5 µm`.

## `SAME-UWA-WET-MESA`

- bromine/HBr wet process used on x=0.31 n-HgCdTe photoconductors;
- wet branch achieved BLIP-level reported device performance in the direct comparison.

## `PRIMARY-X028-MESA`

- nominal Br2: `2%` **basis OPEN**;
- EG:HBr: `3:1` **preparation basis not explicitly closed**;
- reference T: `21 °C`;
- mean `R_V≈2.78 µm/min`;
- rate variation ~`±26%`;
- `A≈0.63`, variation ~`±11%`;
- best roughness ~`2 nm`;
- `Ea≈7.5 kcal/mol`;
- rate ~doubles per +10 °C over tested regime;
- low-T example at 10 °C gives improved feature control.

## Still `OPEN`

- exact Srivastav 2% basis;
- exact 3:1 preparation convention;
- HBr stock assay;
- mixing order;
- reported-run agitation method/rate;
- exact rinse/quench/dry;
- exact RP-01 UWA wet formulation;
- x≈0.30 local rate/anisotropy;
- through-layer overetch window;
- electrical-isolation acceptance limit;
- clean-to-P25 maximum time.

---

# 28. Primary sources

1. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16 (2001) 455–462, DOI `10.1088/0268-1242/16/6/306`.
2. E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *Journal of Electronic Materials* 29 (2000) 853–858, DOI `10.1007/s11664-000-0237-7`.
3. E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “Reactive ion etching for mesa structuring in HgCdTe,” *Journal of Vacuum Science & Technology A* 17 (1999) 2503, DOI `10.1116/1.581988`.
4. V. Srivastav, R. Pal, B. L. Sharma, A. Naik, D. S. Rawal, V. Gopal, H. P. Vyas, “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34 (2005) 1440–1445, DOI `10.1007/s11664-005-0203-5`.
5. P. W. Leech, P. J. Gwynn, M. H. Kibel, “A selective etchant for Hg1−xCdxTe, CdTe and HgTe on GaAs,” *Applied Surface Science* 37 (1989) 291–298, DOI `10.1016/0169-4332(89)90491-1`.
6. CN101740502B, “Photosensitive element array forming method of mercury cadmium telluride micro-mesa infrared detection chip.”
7. US6657194B2 / US20030160172A1, “Multispectral monolithic infrared focal plane array detectors.”
8. US20030102432A1, “Monolithic infrared focal plane array detectors.”
9. US4436580A, “Method of preparing a mercury cadmium telluride substrate for passivation and processing.”
10. R. Sporken, R. Kiran, T. Casselman, F. Aqariden, S. Velicu, Y. Chang, S. Sivananthan, “The effect of wet etching on surface properties of HgCdTe,” *Journal of Electronic Materials* 38 (2009) 1781–1789, DOI `10.1007/s11664-009-0844-x`.
11. K. Shimanoe, M. Sakashita, HgCdTe Br2/methanol surface study, *Japanese Journal of Applied Physics* 30 (1991) 2723–2729, DOI `10.1143/JJAP.30.2723`.
12. Vanya Srivastav, *Modelling, Fabrication and Characterization of HgCdTe Infrared Detectors for High Operating Temperatures*, IISc thesis repository record, file `G25544.pdf`; full thesis process text not recovered through the current accessible route.
