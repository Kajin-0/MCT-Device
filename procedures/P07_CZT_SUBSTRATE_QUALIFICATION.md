# P07 — CdZnTe substrate qualification and pre-LPE surface gate

**Status:** `CONTROLLED-QUALIFICATION-METROLOGY` for incoming-substrate characterization; **surface-preparation chemistry remains `QUALIFICATION-CANDIDATE`** until the exact RP-01-compatible lineage is closed.

**Purpose:** Define the crystallographic, structural, optical, chemical, electrical, dimensional, and surface-state requirements that a CdZnTe substrate must satisfy before entering the RP-01 Te-rich LPE process.

This module deliberately does **not** reduce the substrate specification to “Cd0.96Zn0.04Te (111).” For HgCdTe LPE, nominal Zn fraction, polarity, miscut, dislocation density, Te-rich secondary phases, trace impurities, polishing damage, and final surface preparation all affect the resulting epilayer.

---

## 1. RP-01 requirement

The Smith et al. RP-01 process states that the HgCdTe starting layer was LPE-grown on an **electrically insulating CdZnTe substrate**. `[P-RP01]`

The source does not presently close:

- exact CdZnTe Zn fraction;
- (111)A versus (111)B face;
- miscut magnitude and azimuth;
- substrate thickness;
- incoming dislocation/precipitate limits;
- impurity limits;
- polishing method;
- final chemical preparation before LPE.

These are therefore explicit qualification variables rather than assumed historical facts.

---

## 2. Why CdZnTe is retained as the canonical substrate family

Primary LPE/substrate studies show that CdZnTe substantially improves the lattice/crystalline interface relative to CdTe for x≈0.30 HgCdTe.

### Tranchart et al. 1985

Cd1−yZnyTe with `y≈0.04` was developed as a close lattice-match substrate for Hg1−xCdxTe with `x≈0.30`, and improved-quality Te-rich LPE HgCdTe was obtained on this substrate family. `[P-TR]`

### Crystalline-quality study, 1994

A direct comparison of CdTe, Cd0.96Zn0.04Te and CdMnTe substrates used for LPE Cd0.7Hg0.3Te found the best substrate results in the Cd0.96Zn0.04Te material, including a representative:

- etch-pit density `EPD≈5×10^4 cm^-2`;
- X-ray rocking-curve linewidth `≈25 arcsec`.

HgCdTe layers grown on the Cd0.96Zn0.04Te substrates were of better crystalline quality than comparable layers on CdTe. `[P-CQ94]`

These values are useful quality benchmarks but are **not yet final RP-01 production limits**.

---

## 3. Zn fraction and lattice mismatch

Do not release the substrate by nominal Zn fraction alone.

Different primary sources place the composition needed for x≈0.30 lattice matching in the few-mol-% Zn range; `y≈0.04` is experimentally established in successful LPE work, while other lattice-parameter analyses give values closer to `y≈0.03` depending on the adopted lattice constants, temperature and composition calibration.

### P07 release principle

The primary control variable is the **measured lattice mismatch** between the actual substrate and the intended HgCdTe composition at the relevant reference temperature, not the supplier's nominal `y` alone.

Record:

- nominal `y` from supplier;
- measured substrate lattice parameter;
- measurement temperature;
- uncertainty;
- calculation/model used to compare against target Hg1−xCdxTe;
- resulting mismatch `f=(a_epi-a_sub)/a_sub`.

Until a detector-performance/process-capability study establishes a final numerical mismatch tolerance, substrate lots are classified by measured mismatch and compared against epilayer defect density rather than accepted solely from composition label.

---

## 4. Crystallographic plane, polarity and miscut are separate variables

For zincblende CdZnTe, “(111)” is incomplete because the two polar surfaces are physically distinct.

P07 shall record:

- nominal plane;
- measured surface normal;
- polarity: `(111)A` or `(111)B`;
- off-cut magnitude in degrees;
- off-cut azimuth/direction.

### Evidence for deliberate off-cut

Li, Zhang, Zhu and Chu reported that HgCdTe LPE films grown on substrates approximately `1.2–2° off (111)A` exhibited better crystalline quality and fewer Te precipitates than films on other tilted substrates. Their study also emphasizes substrate melt-etch/interface preparation. `[P-LI98]`

A separate vicinal-plane LPE study found best crystalline quality and fewer Te precipitates near `1.2° off (111)` in its dipping-LPE geometry. `[P-VIC96]`

These studies show that deliberate miscut can materially improve LPE growth, but the optimum is **process dependent**.

### Evidence that B-face material is also highly relevant

Successful Te-rich horizontal-slider LPE processes routinely use `(111)B` CdZnTe, and the Everson substrate-screening method was specifically developed for the technologically important B faces of `(111)` and `(211)` CdTe/CdZnTe. `[P-EVERSON]`

A modern direct comparison of horizontal-slider LPE on `(111)A` and `(111)B` CdZnTe showed that both polarities can produce high-quality HgCdTe; the reported HgCdTe rocking-curve FWHM values were approximately `33.1 arcsec` for A-face growth and `39.6 arcsec` for B-face growth in that particular process, while melt wetting/contact angles differed substantially. `[P-POLARITY]`

### RP-01 rule

**Do not release an exact face/miscut until it has been qualified in the selected horizontal-slider process.**

The current candidate substrate DOE should evaluate polarity and miscut as explicit controlled variables rather than importing a single optimum from a dipping-LPE paper.

---

## 5. Polarity determination

Supplier marking alone is insufficient for process development.

At least one qualified polarity-verification method must be available per substrate lot. Candidate methods include:

- polarity-selective chemical etch with a validated reference specimen;
- X-ray photoelectron diffraction / diffraction-based polarity method;
- other crystallographic polarity method with traceable calibration.

Record:

- method;
- reference specimen or standard;
- face designation;
- confidence/uncertainty;
- physical mark applied to preserve face identity through cleaning and loading.

P07 shall not permit A/B identity to be inferred from an operator's memory of wafer orientation.

---

## 6. Miscut measurement

Measure miscut rather than accepting a supplier nominal value.

Preferred approach:

- high-resolution X-ray diffraction or a qualified Laue/XRD orientation measurement;
- determine both magnitude and azimuth relative to the intended crystallographic direction.

During qualification, report to at least `0.1°` resolution if the metrology supports it because the literature optimum region spans only approximately one degree.

A final production tolerance tighter than the demonstrated instrument uncertainty shall not be specified.

---

## 7. Crystalline-quality gate

At minimum, characterize each incoming substrate lot using:

1. high-resolution X-ray rocking curve;
2. etch-pit/dislocation assessment on representative/sacrificial material;
3. infrared inspection for inclusions/secondary phases;
4. optical inspection for twins, subgrains, cracks and polishing damage.

### Benchmark, not final limit

The 1994 Cd0.96Zn0.04Te study reports `EPD≈5×10^4 cm^-2` and XRD linewidth `≈25 arcsec` for its best material used for x≈0.30 LPE. `[P-CQ94]`

P07 uses these as **historical benchmark values**. Final RP-01 acceptance limits must be established by correlating substrate metrics with:

- epilayer rocking curve;
- epilayer EPD/threading dislocation density;
- P05 transport;
- P06 composition/thickness uniformity;
- final detector noise/yield.

---

## 8. Etch-pit density / dislocation screening

Everson et al., *Journal of Electronic Materials* 24, 505–510 (1995), DOI `10.1007/BF02657954`, developed an etch system specifically for B-face `(111)` and `(211)` CdTe/CdZnTe used in HgCdTe epitaxy. `[P-EVERSON]`

The reported pits are approximately `10:1` wider than deep, permitting defect delineation without excessive substrate removal.

### P07 use

EPD characterization is a **sacrificial or controlled characterization step**, not automatically the final surface-preparation etch.

Record:

- etchant recipe/version;
- temperature;
- time;
- face/polarity;
- microscope magnification;
- counted area;
- number of fields;
- EPD mean, standard deviation and spatial distribution;
- classification of precipitate-related pits versus dislocation pits where possible.

Do not report a single EPD number without area/count statistics.

---

## 9. Te-rich secondary phases / precipitates

CdZnTe Te inclusions/precipitates are not benign substrate defects.

Primary substrate/LPE studies show that Te precipitates and substrate imperfections can propagate into or alter the electrical state of lightly doped HgCdTe layers. `[P-TOWER] [P-WEISS]`

### Inspection methods

Preferred non-destructive incoming inspection:

- infrared transmission microscopy over the intended growth area;
- spatial map of inclusions/precipitates;
- record size and areal density.

Etch-pit observation may be used on sacrificial material to distinguish precipitate-related defects. Literature demonstrates optical detection of precipitate pits associated with secondary phases larger than approximately `5 µm`. `[P-PRECIP]`

### Required record

- total inspected area;
- detection threshold/minimum resolvable size;
- precipitate/inclusion count by size bin;
- largest observed feature;
- areal density;
- clustering metric or spatial map;
- active-area exclusion if applicable.

Final numerical reject limits remain `QUAL` until correlated with LPE and detector performance.

---

## 10. Trace impurities — copper is a critical control variable

Tower et al. showed that impurity contamination in CdZnTe substrates can degrade lightly doped LPE HgCdTe electrical/device properties. Copper contamination was specifically associated with degraded LPE material and anomalous carrier-type behavior. `[P-TOWER]`

Weiss et al. later showed that substrate impurity/precipitate effects can materially alter carrier concentration after annealing, including a strong polarity dependence for Cu contamination in `(111)` substrates. In their contaminated-substrate case, layers on `(111)A` showed very high Cu concentrations whereas `(111)B` layers showed normal carrier concentrations. `[P-WEISS]`

This is especially important for RP-01 because its target electron density is only ~`10^15 cm^-3`.

### P07 impurity rule

For process qualification, each substrate lot should have a trace-impurity certificate or representative analytical measurement with explicit attention to:

- Cu;
- Fe;
- Ni;
- Na;
- other electrically active metallic contaminants identified by the supplier/process history.

Candidate analytical methods:

- GDMS;
- ICP-MS after validated digestion/sampling;
- graphite-furnace atomic absorption for selected elements;
- supplier certificate backed by a qualified analytical process.

**No arbitrary ppb/ppm acceptance value is released yet** because the primary sources located so far establish the effect qualitatively/experimentally but do not provide a universally transferable threshold for RP-01.

---

## 11. Electrical-isolation gate

RP-01 requires an electrically insulating substrate so the photoconductor current path remains in the HgCdTe layer.

Measure substrate resistivity or an equivalent leakage metric on representative incoming material.

Record:

- measurement temperature;
- geometry;
- electric field/current range;
- dark/light condition;
- measured resistivity or leakage;
- instrument floor.

A final numerical minimum substrate resistivity remains `OPEN/QUAL` until detector-geometry leakage sensitivity is calculated.

---

## 12. Dimensional/metrology gate

For every substrate record:

- length/width or diameter;
- thickness at multiple positions;
- total thickness variation (TTV);
- bow/warp where sample size warrants it;
- edge chips;
- crack inspection;
- polished-side designation.

Candidate historical process dimensions include `10×10×1 mm` and `15×15×1 mm` CdZnTe substrates in separate LPE systems. These are **apparatus examples, not RP-01 dimensional requirements**.

The released dimensions must be derived from the selected graphite boat/substrate recess.

---

## 13. Incoming surface roughness and damage

Before the final pre-LPE chemical preparation, inspect the polished growth face using:

- Nomarski/DIC microscopy;
- AFM or qualified optical profilometry on representative locations;
- high-magnification inspection for polishing scratches, pits and embedded particles.

Record:

- RMS roughness over stated scan size;
- peak-to-valley height;
- scratch density/maximum scratch size;
- pit density;
- scan coordinates.

Do not use a single roughness value without scan area/bandwidth because RMS roughness is scale dependent.

Final roughness limits remain `QUAL`.

---

## 14. Mechanical/chemical polishing history

The substrate traveler must retain the complete polishing history when available:

- saw/dicing method;
- lapping abrasives and grit sequence;
- mechanical polish slurry;
- chemical-mechanical polish chemistry;
- total material removed;
- final polish direction/fixture;
- post-polish storage time/ambient.

Published HgCdTe/CdZnTe LPE processes commonly use chemically and mechanically polished CdZnTe before a short bromine/methanol treatment, but exact recipes vary by growth family. `[P-PREP]`

---

## 15. Final bromine/methanol surface preparation — candidate only

A successful HgCdTe LPE process from the Military University of Technology reports `(111)B` CdZnTe substrates, `10×10×1 mm`, chemically/mechanically polished and then etched in approximately `(2–3)% Br2/methanol` for **a few seconds** immediately before loading into the graphite boat. `[P-PREP]`

Other HgCdTe surface-polishing studies use substantially weaker Br2/methanol concentrations for controlled removal of sub-micrometre surface layers.

Therefore concentration and time are not universal.

### P07 rule

The final RP-01 substrate surface etch remains `QUALIFICATION-CANDIDATE`.

Do **not** convert “2–3% for a few seconds” into a released recipe until the following are closed:

- concentration basis;
- reagent purity;
- methanol water content;
- bath temperature;
- solution age;
- immersion/agitation method;
- etch rate on the selected CdZnTe composition/polarity;
- target removal depth;
- rinse sequence;
- maximum air exposure before LPE contact;
- resulting roughness/oxide state.

---

## 16. Surface-cleanliness verification after chemical preparation

Chemical etching is not proof of a clean surface.

CdZnTe surface studies show that bromine/methanol treatment can reveal or interact with polishing damage, silica/abrasive residues and Te-rich secondary phases.

At qualification stage, verify representative etched surfaces by at least:

- Nomarski/DIC;
- AFM/roughness;
- optical/SEM inspection for residues/precipitates where available;
- surface spectroscopy on development coupons if required to close oxide/contamination state.

The final LPE process should minimize the elapsed time between accepted final preparation and protected/inert loading.

---

## 17. Candidate polarity/miscut DOE

Because the primary literature does not establish a universal optimum for the selected RP-01 horizontal-slider geometry, run a controlled substrate-orientation qualification before production release.

### Factor A — polarity

- `(111)A`
- `(111)B`

### Factor B — off-cut magnitude

Candidate levels:

- nominal/on-axis;
- ~`1.0°`;
- ~`1.5°`;
- ~`2.0°`.

These levels span the primary LPE literature region where reduced terracing/fewer precipitates were reported. They are qualification levels, not all claimed optima.

Where material cost prohibits a full factorial design, prioritize the polarity used by the chosen same-lineage boat process and bracket its miscut around the literature 1.2–2° region.

### Responses

After identical P03 growth conditions, compare:

- P06 thickness uniformity;
- P06 x/edge uniformity;
- surface terrace amplitude/period;
- residual melt/wipe-off quality;
- XRD rocking-curve FWHM;
- EPD/threading defect metric;
- Te precipitate density;
- P05 carrier state/mobility after matched P04 anneal;
- final device yield/noise on later lots.

Select the production orientation from these responses, not aesthetics alone.

---

## 18. Incoming substrate traveler fields

Every accepted substrate shall have, at minimum:

### Identity

- supplier;
- lot/boule number;
- wafer/coupon number;
- date received;
- storage history.

### Composition/crystallography

- nominal Zn fraction;
- measured lattice parameter/mismatch;
- orientation;
- polarity;
- miscut magnitude;
- miscut azimuth.

### Dimensions

- lateral dimensions;
- thickness;
- TTV;
- bow/warp where relevant.

### Structural quality

- XRD FWHM;
- EPD/dislocation metric;
- IR inclusion/precipitate map;
- twin/subgrain observations.

### Chemistry/electrical

- trace impurity record, especially Cu;
- substrate resistivity/leakage metric.

### Surface

- polishing history;
- pre-clean roughness;
- final chemical-preparation batch/time;
- post-clean inspection;
- elapsed time to LPE loading.

### Disposition

- PASS / CONDITIONAL / FAIL;
- deviations;
- approved use area/edge exclusion.

---

## 19. Initial acceptance philosophy

Until detector-correlated process capability is established, P07 shall use **benchmark-based qualification**, not invented hard tolerances.

Immediate rejection conditions include:

- wrong or unknown face/polarity;
- cracked/chipped growth area;
- visible gross twinning/subgrain boundary through active area;
- dense/large secondary-phase region intersecting intended detector area;
- unresolved surface contamination after final preparation;
- substrate electrical leakage incompatible with isolating the HgCdTe layer;
- impurity history indicating uncontrolled Cu contamination;
- crystallographic mismatch/orientation outside the range intentionally entered into the qualification DOE.

Historical values such as `EPD≈5×10^4 cm^-2` and `XRD FWHM≈25 arcsec` are benchmarks for high-quality Cd0.96Zn0.04Te, not yet mandatory limits.

---

## 20. Release blockers

P07 becomes a released production substrate specification only after closing:

1. exact substrate composition/lattice-mismatch target for the selected x≈0.30 material;
2. selected polarity `(111)A/B`;
3. selected off-cut magnitude and azimuth;
4. allowable orientation/miscut tolerances;
5. dimensional specification matched to the released boat;
6. EPD/dislocation acceptance limit;
7. XRD FWHM acceptance limit;
8. Te inclusion/precipitate size-density limit;
9. trace-impurity/Cu acceptance threshold or qualified supplier process;
10. minimum electrical resistivity/leakage requirement;
11. polishing specification;
12. exact final surface-etch formulation and target removal depth;
13. rinse/dry method;
14. maximum allowable clean-to-LPE delay;
15. post-clean surface roughness/contamination acceptance criteria.

---

## 21. Primary sources

1. J. C. Tranchart, B. Latorre, C. Foucher, Y. Le Gouge, “LPE growth of Hg1−xCdxTe on Cd1−yZnyTe substrates,” *Journal of Crystal Growth* 72, 468–473 (1985). `[P-TR]`
2. “Study of the crystalline quality of CdTe, CdZnTe and CdMnTe substrates used for liquid phase epitaxy of Cd0.7Hg0.3Te,” *Journal of Crystal Growth* 139, 6–14 (1994), DOI `10.1016/0022-0248(94)90022-1`. `[P-CQ94]`
3. B. Li, X. Zhang, J. Zhu, J. Chu, “Crystallinity improvement of Hg1−xCdxTe films grown by a liquid-phase epitaxial technique,” *Journal of Crystal Growth* 184–185, 1242–1246 (1998), DOI `10.1016/S0022-0248(98)80260-1`. `[P-LI98]`
4. “Growth of Hg1−xCdxTe liquid phase epitaxial films on vicinal planes,” *Journal of Crystal Growth* 169, 480–484 (1996), DOI `10.1016/S0022-0248(96)00418-6`. `[P-VIC96]`
5. W. J. Everson, C. K. Ard, J. L. Sepich, B. E. Dean, G. T. Neugebauer, H. F. Schaake, “Etch Pit Characterization of CdTe and CdZnTe Substrates for Use in Mercury Cadmium Telluride Epitaxy,” *Journal of Electronic Materials* 24, 505–510 (1995), DOI `10.1007/BF02657954`. `[P-EVERSON]`
6. J. P. Tower, S. P. Tobin, M. Kestigian, P. W. Norton, A. B. Bollong, H. F. Schaake, C. K. Ard, “CdZnTe Substrate Impurities and Their Effects on Liquid Phase Epitaxy HgCdTe,” *Journal of Electronic Materials* 24 (1995). `[P-TOWER]`
7. E. Weiss, O. Klin, E. Benory, E. Kedar, Y. Juravel, “Substrate quality impact on the carrier concentration of undoped annealed HgCdTe LPE layers,” *Journal of Electronic Materials* 30, 756–761 (2001), DOI `10.1007/BF02665868`. `[P-WEISS]`
8. J. K. Radhakrishnan, S. Sitharaman, S. C. Gupta, “Surface morphology of Hg0.8Cd0.2Te epilayers grown by LPE using horizontal slider,” *Applied Surface Science* 207, 33–39 (2003), DOI `10.1016/S0169-4332(02)01227-8`.
9. Huo Qin et al., “Effect of polarity of CdZnTe substrate on slider liquid phase epitaxy of HgCdTe,” primary experimental study (2023), reporting direct `(111)A`/`(111)B` slider-LPE comparison and HRXRD/morphology/wetting data. `[P-POLARITY]`
10. Status/process paper from the Military University of Technology describing `(111)B` CdZnTe, `10×10×1 mm`, chemical/mechanical polish and `(2–3)% Br2/methanol` for a few seconds before LPE loading. `[P-PREP]` — transfer evidence only; x≈0.20–0.22 branch.

### Supporting substrate-defect source

- Primary CdZnTe precipitate/etch-pit studies using Everson etching and IR microscopy demonstrate discrimination and counting of secondary phases; use for metrology design, not as a direct RP-01 acceptance threshold. `[P-PRECIP]`
