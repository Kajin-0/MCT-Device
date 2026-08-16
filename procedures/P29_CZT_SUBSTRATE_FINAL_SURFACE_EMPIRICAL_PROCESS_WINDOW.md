# P29 — CdZnTe substrate, crystallographic face, and final pre-LPE surface empirical process window

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert P07/P07A/P07B/P07C into an operator-level empirical substrate traveler for the RP-01 x≈0.30 Te-rich LPE branch.

RP-01 directly establishes only that the HgCdTe layer was LPE grown on an **electrically insulating CdZnTe substrate**. It does not disclose the exact Zn fraction, surface plane, A/B polarity, miscut, substrate thickness, bulk-defect limits, impurity limits, mechanical polish, final chemical preparation, rinse/dry sequence, or clean-to-LPE timing.

P29 therefore controls the chain:

`substrate lot/genealogy -> composition/lattice parameter -> plane/polarity/miscut -> bulk defects/impurities -> mechanical surface -> final chemical surface -> clean-to-load history -> LPE interface -> epilayer morphology/crystal/electrical quality`.

P29 supplements P07/P07A/P07B/P07C and P03. It does not replace their historical-provenance rules.

---

# 2. Evidence classes

- `DIRECT-RP01` — directly stated by Smith et al. 2001.
- `PRIMARY-LPE-X030` — primary HgCdTe LPE evidence near x≈0.30.
- `PRIMARY-LPE-TRANSFER` — primary HgCdTe LPE evidence at another x or device family.
- `PRIMARY-SUBSTRATE-QUALITY` — direct CdZnTe crystal/surface/impurity data relevant to epitaxy.
- `PRIMARY-POLARITY-TRANSFER` — direct A/B polarity comparison in slider LPE.
- `SAME-UWA-TRANSFER` — same-UWA CdZnTe/HgCdTe evidence from another epitaxy method/device branch.
- `LOCAL-QUAL` — local process choice requiring empirical closure.
- `OPEN` — historically or empirically unresolved.

No value changes evidence class merely because it is common in later HgCdTe practice.

---

# 3. Direct RP-01 substrate state

`DIRECT-RP01` closes:

- substrate family: CdZnTe;
- electrical role: insulating substrate;
- overlayer: n-HgCdTe by LPE;
- nominal overlayer x≈0.30;
- overlayer thickness 9.5 µm.

RP-01 does **not** directly close:

- CdZnTe Zn fraction;
- exact resistivity;
- orientation;
- A/B polarity;
- miscut magnitude;
- miscut azimuth;
- substrate dimensions/thickness;
- supplier;
- EPD/XRD/inclusion limits;
- trace impurities;
- polish/etch sequence;
- final surface chemistry;
- clean-to-LPE load time.

These remain separate process coordinates.

---

# 4. Strongest composition/orientation transfer center

Multiple primary HgCdTe LPE studies near the relevant material family use approximately:

`Cd0.96Zn0.04Te`.

A primary crystalline-quality comparison for LPE Cd0.7Hg0.3Te found the best substrate result in its Cd0.96Zn0.04Te material, with representative substrate metrics around:

- etch-pit density `~5×10^4 cm^-2`;
- X-ray rocking-curve linewidth `~25 arcsec`;

and better HgCdTe epilayer crystalline quality than comparable CdTe substrates.

Another detector-oriented Te-rich LPE branch directly used:

- `(111)B` CdZnTe;
- `4% Zn`;
- substrate dimensions `10×10×1 mm^3`;
- chemical and mechanical polishing;
- a brief `2–3% bromine-methanol` final treatment;
- loading into the graphite boat after only a few seconds of etching.

### P29 classification

`Cd0.96Zn0.04Te (111)B` is the strongest current **LPE transfer center** for local first screening.

It is **not** the recovered RP-01 substrate identity.

Do not write `y=0.04`, `(111)B`, `10×10×1 mm`, or any offcut as `DIRECT-RP01`.

---

# 5. Zn fraction is not released from supplier label alone

The substrate should be controlled by both nominal composition and measured lattice state.

For each lot record:

- supplier and lot/ingot ID;
- nominal Cd/Zn/Te composition;
- composition certificate method;
- measured Zn fraction if independently available;
- lattice parameter;
- measurement temperature;
- spatial sampling positions;
- uncertainty;
- intended HgCdTe x target.

Use XRD/lattice-parameter, XRF, EPMA or another qualified method as appropriate.

### Release principle

The relevant physical output is the substrate/epilayer lattice relationship and resulting defect state, not nominal `4% Zn` by itself.

No final y tolerance is released until repeated local LPE data relate substrate composition/lattice parameter to:

- epilayer XRD;
- defect density;
- P05 mobility/carrier state;
- P06 x/thickness uniformity;
- detector yield/noise.

---

# 6. Plane, polarity, miscut magnitude and azimuth are independent coordinates

A substrate record must contain separately:

1. plane family;
2. A/B polarity;
3. miscut magnitude;
4. miscut azimuth.

Do not describe a substrate merely as `(111)` when polarity is relevant.

## 6.1 Primary polarity result in slider LPE

A 2023 direct slider-LPE comparison of `(111)A` and conventional `(111)B` CdZnTe found:

- comparable HgCdTe composition and thickness on the two polarities;
- melt/film contact angle about `50±2°` for `(111)A`;
- about `30±2°` for `(111)B`;
- `(111)A` HgCdTe XRD FWHM `33.1 arcsec`;
- substantially reduced residual melt droplets on the A-face branch without reported loss of crystal quality.

### P29 consequence

Polarity affects wetting/residual-melt behavior and therefore interacts directly with P03 wipe-off/morphology.

Do not assume `(111)B` is universally optimal simply because it is conventional.

## 6.2 Primary vicinal-plane result

A 1996 primary dipping-LPE study on vicinal substrates found best crystal quality and fewer Te precipitates near `1.2° off (111)` in that experimental geometry.

This demonstrates that low-degree misorientation can be an active growth variable.

### Restriction

That study used dipping LPE and a different substrate implementation. `1.2°` is therefore an experiment-sizing reference, not an RP-01 or local slider-LPE specification.

Historical RP-01 miscut remains `OPEN`.

---

# 7. Orientation/polarity verification

Supplier face marking shall not be the sole qualification evidence during process development.

Record:

- supplier nominal orientation;
- measured surface normal;
- polarity verification method;
- miscut magnitude;
- miscut azimuth;
- measurement uncertainty;
- reference standard used;
- permanent wafer/coupon orientation mark.

Candidate qualified methods include HRXRD/Laue plus a validated polarity-sensitive method appropriate to CdZnTe.

A/B polarity shall never be reconstructed from operator memory after the final surface clean.

---

# 8. Incoming crystalline-quality gate

Each substrate lot shall be characterized for the quantities that can seed or correlate with epilayer defects.

Minimum development record:

- HRXRD rocking-curve FWHM and curve shape;
- multiple spatial positions where substrate size permits;
- IR transmission microscopy for inclusions/precipitates;
- crack/twin/subgrain inspection;
- EPD or equivalent defect characterization on representative/sacrificial material;
- optical/DIC surface inspection;
- thickness/flatness/warp where relevant to boat contact.

Historical transfer benchmarks such as `EPD~5×10^4 cm^-2` and `~25 arcsec` are reference scales only, not release limits.

---

# 9. Te inclusions / precipitates

Map incoming substrates by IR microscopy or an equivalent qualified technique.

Record:

- inspected area;
- optical resolution/detection threshold;
- feature count;
- size distribution;
- largest feature;
- areal density;
- clustering/spatial map;
- whether the intended growth region intersects a major inclusion.

Do not collapse precipitate/inclusion data into EPD without a validated relation.

---

# 10. Trace impurities and substrate genealogy

Primary LPE evidence shows that CdZnTe substrate impurities can propagate into or alter lightly doped HgCdTe electrical behavior; copper is a particularly important warning variable.

RP-01 targets an electron density of order `10^15 cm^-3`, so substrate impurity genealogy cannot be treated as irrelevant bulk-material metadata.

For every substrate lot record, as available:

- Cu;
- Fe;
- Ni;
- Na;
- other supplier-reported electrically active trace elements;
- analytical method;
- sampling scheme;
- detection limits;
- lot/ingot position.

Use GDMS/ICP-MS/another validated analytical method or a traceable supplier certificate.

No universal concentration limit is released from the current evidence.

### Rule

A change of CdZnTe ingot/source lot is a material-process change and shall be traceable through P03/P05/P06 and device output.

---

# 11. Electrical-isolation gate

RP-01 requires an electrically insulating substrate.

For each qualification lot record:

- supplier resistivity/conductivity designation;
- measured substrate resistivity or leakage proxy where practical;
- measurement temperature;
- electrode geometry/method;
- uncertainty.

A later MBE branch using Cd0.96Zn0.04Te reported substrate resistivity of order `10^5 Ω·cm`, demonstrating a practical semi-insulating scale in this material family; it is not an RP-01 minimum specification.

The local limit shall be set from parasitic-current/leakage impact in the actual photoconductor geometry.

---

# 12. Mechanical preparation genealogy

Before the final chemical treatment record all known mechanical history:

- ingot/slice ID;
- slicing method;
- orientation cut;
- lapping sequence;
- abrasive identities and nominal grit/particle size;
- polishing slurry/compound;
- pad;
- load/pressure;
- duration;
- material removed;
- side processed;
- final as-polished roughness;
- scratches/pits/edge chips.

“Epi-ready” is a supplier condition label, not a complete P29 process record.

If an epi-ready commercial substrate is used, retain the vendor certificate and independently measure enough surface/crystal state to establish local equivalence.

---

# 13. Final pre-LPE surface — strongest empirical transfer branch

A detector-oriented Te-rich LPE source directly reports:

- `(111)B`, 4%-Zn CdZnTe;
- chemical + mechanical polishing;
- `2–3% bromine-methanol` final etch;
- exposure for `a few seconds`;
- loading into a graphite boat afterward.

This is the strongest current practical LPE final-surface transfer family.

### Critical restrictions

The source does not, in the currently recovered text, define:

- Br2 percentage basis;
- exact time within “a few seconds”;
- bath temperature;
- agitation;
- exact methanol rinse/dry;
- removed depth;
- exact clean-to-load delay.

Therefore P29 does not convert the historical wording into a reagent-mass/volume recipe.

---

# 14. Other detailed substrate-clean processes are method-specific

A primary MBE study on Cd0.96Zn0.04Te `(211)B` provides a much more explicit surface process:

- sequential degrease in trichloroethylene, acetone and methanol;
- `60 °C`;
- `15 min`;
- `0.5% Br2/methanol`;
- `60 s`;
- methanol rinse.

This is useful proof that surface preparation is explicitly parameterized in HgCdTe epitaxy, but it is **MBE transfer evidence**, not an LPE RP-01 recipe.

Do not transplant this sequence into P03 without matched LPE qualification.

---

# 15. Final-surface qualification variables

For a local LPE transfer, define a recipe ID that states mathematically:

- Br2 concentration basis;
- Br2 amount;
- methanol amount/grade;
- solution volume;
- bath temperature;
- solution age;
- fresh/reused status;
- sample area/loading;
- immersion time;
- agitation;
- face/polarity;
- rinse sequence;
- dry method;
- clean-to-load interval.

If the historical `2–3%` basis remains unresolved, local formulations may be tested under explicit `LOCAL-WW`, `LOCAL-VV`, or other unambiguous recipe classes. They may not be called the historical recipe.

---

# 16. Removed-depth and surface-state metrology

For each final-surface candidate measure, where feasible:

- removed depth by protected-step profilometry or equivalent;
- AFM RMS roughness;
- longer-scale waviness/peak-to-valley;
- DIC/Nomarski morphology;
- pit/particle density;
- XPS or another surface-chemistry method on development coupons;
- Te enrichment/oxide/contamination trend;
- HRXRD before/after where informative.

The lowest AFM roughness is not automatically the best LPE interface.

The final acceptance object is downstream epilayer quality.

---

# 17. Clean-to-load clock

Define and record:

- `t_final_etch_end`;
- `t_final_rinse_end`;
- `t_dry_complete`;
- `t_boat_load`;
- `t_furnace_or_reactor_load`;
- purge/start timestamp if distinct.

Derived:

`Delta t_CTL = t_boat_load - t_final_etch_end`

and, where useful,

`Delta t_surface_to_growth = t_first_melt_contact - t_final_etch_end`.

Also record atmosphere during every interval:

- ambient air;
- clean bench;
- dry N2/inert container;
- other controlled state.

No maximum clean-to-load time is released without local interface data.

---

# 18. P29 local empirical transfer sequence

## Stage 0 — incoming substrate characterization

For each candidate lot:

1. verify composition/lattice state;
2. verify orientation/polarity/miscut;
3. map crystalline quality;
4. map inclusions/precipitates;
5. capture impurity certificate/data;
6. verify electrical isolation;
7. document mechanical/surface genealogy.

## Stage 1 — first transfer center

If available, begin with a high-quality `Cd0.96Zn0.04Te {111}` substrate family because it has strong x≈0.30 LPE precedent.

Do not label B polarity or any miscut as RP-01.

## Stage 2 — polarity screen

Where supply allows, compare `(111)A` and `(111)B` with otherwise matched:

- substrate quality class;
- final surface preparation;
- P03 melt/source;
- supercooling/contact time;
- wipe-off;
- anneal.

Measure residual-melt/droplet behavior explicitly because direct slider-LPE evidence shows polarity-dependent wetting.

## Stage 3 — miscut screen

Only after polarity and baseline surface process are stable, compare a bounded small-offcut matrix based on supplier availability and measured XRD orientation.

The 1.2° vicinal result from dipping LPE is an experiment-sizing reference only.

## Stage 4 — final chemical surface

At fixed substrate face/lot class, compare mathematically defined Br2/methanol recipes and measure removed depth/surface state.

## Stage 5 — clean-to-load delay

At a selected surface treatment, compare practical exposure delays/ambients.

## Stage 6 — repeated substrate lots

Repeat on independent substrate lots/ingot positions to separate surface-process repeatability from substrate genealogy.

---

# 19. Downstream LPE acceptance vector

For every P29 condition link to P03/P05/P06/P13 and record:

### Growth/wetting

- melt contact behavior;
- wetting/contact-angle proxy if available;
- residual melt/droplet density;
- wipe-off success/damage;
- nucleation anomalies.

### Morphology

- whole-layer optical/DIC map;
- roughness;
- pinhole/crater density;
- usable-area fraction.

### Crystal quality

- epilayer HRXRD FWHM/shape;
- twins;
- EPD/threading defect metric;
- precipitates/inclusions propagated into epilayer.

### Composition/thickness

- mean x/optical edge;
- x uniformity;
- mean thickness;
- thickness uniformity.

### Electrical

- carrier state;
- Hall/multicarrier response;
- mobility;
- sheet resistance;
- spatial uniformity.

### Device/lifetime proxy

- tau_eff/lifetime proxy where available;
- responsivity/noise on matched devices when material permits.

Define:

`Y_CZT = {wetting, residual melt, morphology, epilayer XRD/defects, x/d uniformity, transport, lifetime/device yield}`.

P29 is released from this downstream vector, not from substrate appearance alone.

---

# 20. Failure modes

Preserve and classify:

- wrong/uncertain face polarity;
- miscut out of stated local class;
- Zn/composition nonuniformity;
- high rocking-curve width;
- excessive EPD;
- inclusions/precipitates in growth area;
- impurity anomaly, especially Cu;
- electrical leakage through substrate;
- scratches/edge chips/polishing residue;
- bromine overetch/pitting/waviness;
- Te-rich/oxidized/contaminated final surface;
- excessive clean-to-load delay;
- poor wetting;
- residual melt droplets;
- wipe-off damage;
- epilayer twins/dislocations/precipitates;
- transport anomaly or carrier-state shift correlated to substrate lot.

Substrate-related failed growths remain part of the genealogy record.

---

# 21. Current practical status

## Strong empirical transfer anchors

- Cd0.96Zn0.04Te is repeatedly successful for HgCdTe LPE near x≈0.30.
- `{111}` is a strongly established LPE orientation family.
- `(111)B` / 4% Zn / chemical+mechanical polish / brief 2–3% Br2-MeOH is a detector-LPE transfer process.
- direct slider-LPE data prove `(111)A` can also produce high-quality material and changes wetting/residual melt.
- vicinal-LPE data prove low-degree miscut can influence crystal quality/Te precipitates.
- substrate impurity genealogy can alter lightly doped LPE electrical properties.

## Still `OPEN` for RP-01

- exact y(Zn);
- plane/polarity;
- miscut magnitude/azimuth;
- substrate thickness/dimensions;
- supplier/ingot;
- substrate resistivity;
- impurity limits;
- XRD/EPD/inclusion limits;
- mechanical polish;
- final chemistry;
- Br2 concentration basis;
- exact etch time;
- rinse/dry;
- removed depth;
- clean-to-load limit.

---

# 22. Release blockers

P29 remains `PRE-RELEASE` until a local substrate/process class establishes:

1. accepted substrate composition/lattice window;
2. verified plane/polarity;
3. miscut magnitude/azimuth window;
4. crystalline-quality/inclusion metrics;
5. impurity/genealogy control;
6. electrical-isolation criterion;
7. mechanical surface state;
8. mathematically defined final chemical recipe;
9. removed-depth/surface-state acceptance;
10. rinse/dry;
11. clean-to-load maximum and ambient rule;
12. repeatable P03 morphology/wetting;
13. epilayer XRD/defect/x/thickness/transport closure;
14. repeated independent substrate lots.

---

# 23. Primary-source set

1. E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16 (2001) 455–462, DOI `10.1088/0268-1242/16/6/306`.
2. Primary 1994 *Journal of Crystal Growth* study comparing CdTe, Cd0.96Zn0.04Te and CdMnTe substrates for LPE Cd0.7Hg0.3Te; Cd0.96Zn0.04Te reported EPD ~5×10^4 cm^-2 and rocking-curve width ~25 arcsec in the best substrate material.
3. L. Kubiak et al., “Status of HgCdTe photodiodes at the Military University of Technology,” *Opto-Electronics Review* 11(3) (2003) 211–226.
4. Q. Huo et al., “Effect of polarity of CdZnTe substrate on slider liquid phase epitaxy of HgCdTe,” *Journal of Infrared and Millimeter Waves* 42(1) (2023) 1–7, DOI `10.11972/j.issn.1001-9014.2023.01.001`.
5. “Growth of Hg1−xCdxTe liquid phase epitaxial films on vicinal planes,” *Journal of Crystal Growth* 169 (1996) 480–484, DOI `10.1016/S0022-0248(96)00418-6`.
6. Tower et al., “CdZnTe Substrate Impurities and Their Effects on Liquid Phase Epitaxy HgCdTe,” *Journal of Electronic Materials* (1995).
7. Primary MBE Cd0.96Zn0.04Te `(211)B` substrate-preparation study reporting sequential solvent degrease, 0.5% Br2/methanol/60-s etch and methanol rinse; retained only as method-specific transfer evidence.
8. J. Gawron and A. Rogalski, “HgCdTe buried multi-junction photodiodes fabricated by the liquid phase epitaxy,” *Infrared Physics & Technology* 43 (2002) 157–163, DOI `10.1016/S1350-4495(02)00135-4`, reporting Cd0.96Zn0.04Te `(111)B` epi-ready substrates for LPE.

