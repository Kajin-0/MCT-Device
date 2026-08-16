# P30 — Te-rich horizontal-slider LPE apparatus / charge / contact / wipe-off empirical process window

**Status:** EMPIRICAL TRANSFER / QUALIFICATION WINDOW — not an RP-01 historical recipe and not a production release.

## 1. Purpose

Convert the P03 thermodynamic/material framework into an experimentally traceable horizontal-slider LPE execution sequence for x≈0.30 HgCdTe. P30 controls the variables that are otherwise hidden behind phrases such as “equilibrate,” “bring the melt into contact,” and “wipe off.”

P30 does **not** replace P03/P03A–P03E/P21/P22. It adds the practical hardware, charge genealogy, timing and wipe-off layer needed to make those modules physically executable.

## 2. Evidence classes

- `DIRECT-HONEYWELL-PATENT` — Bowers & Schmit, US4317689A / divisional US4366771A.
- `DIRECT-HONEYWELL-WIPEOFF` — Hager/Wood/Honeywell US4592304A and Hager/Honeywell US4706604A.
- `PRIMARY-HARMAN-1980` — T. C. Harman, J. Electron. Mater. 9 (1980), DOI 10.1007/BF02822728.
- `PRIMARY-RSG-2003` — J. K. Radhakrishnan, S. Sitharaman, S. C. Gupta, J. Cryst. Growth 252 (2003) 79–86, DOI 10.1016/S0022-0248(02)02530-7.
- `PRIMARY-SHINOHARA-1994` — M. Shinohara et al., J. Cryst. Growth 141 (1994) 352–356, DOI 10.1016/0022-0248(94)90237-2.
- `PRIMARY-BERNARDI-1988` — slider LPE with in-situ Te-solution preparation, J. Cryst. Growth 87 (1988) 365–371, DOI 10.1016/0022-0248(88)90189-3.
- `DERIVED` — arithmetic from directly published quantities.
- `QUAL` — local qualification variable.
- `OPEN` — not recovered or not transferable.

## 3. Canonical x≈0.30 thermodynamic center retained from P03

Honeywell tie-line anchor:

- `xL = 0.082`
- `yL = 0.810`
- `TL = 507 °C`
- resulting `xS ≈ 0.29`
- `xS/xL = 3.54`

For the source solution `(Hg1−xL CdxL)1−yL TeyL`, derived elemental mole fractions are:

- Hg `0.17442`
- Cd `0.01558`
- Te `0.81000`

and derived mass fractions are:

- Hg `0.249738`
- Cd `0.012502`
- Te `0.737760`.

**Restriction:** these fractions define composition, not total charge mass. The Honeywell patent does not disclose an exact charge mass for this tie line.

## 4. Minimum boat architecture — direct Honeywell lineage

The historical Honeywell apparatus family contains:

- graphite base/stator with substrate recess;
- movable graphite slider/carrier;
- one or more through-wells for Te-rich growth solution;
- plug/cap over the growth-solution well;
- shallow auxiliary Hg-source recess;
- graphite cover fitted closely to the slider;
- Hg-distribution grooves/moats around the growth region;
- horizontal quartz furnace tube;
- external heating zone;
- gas flow under H2 after purge;
- longitudinal slider actuation to align growth well and substrate.

The patent states that the recessed areas associated with the solution wells are generally comparable in size to the substrate recess. It does **not** publish a complete dimensioned mechanical drawing suitable for direct machining.

### 4.1 P30 hardware record

For every local boat revision record:

- graphite grade, supplier, density/purity grade;
- base/slider/cover IDs;
- substrate recess L/W/depth;
- growth-well top/bottom dimensions and depth;
- growth-well volume;
- auxiliary Hg-source recess dimensions/volume;
- plug dimensions/mass;
- slider-to-base clearance;
- cover-to-slider fit;
- moat/groove width/depth/path;
- substrate-to-well overlap area;
- cooling/wipe-off region geometry;
- actuator stroke and measured position repeatability.

No local boat may be called “Honeywell-identical” without a recovered dimensioned source drawing.

## 5. Furnace and atmosphere sequence

Honeywell direct sequence:

1. load substrate and Te-rich charge;
2. cap the growth well;
3. load HgTe or HgTe+Te auxiliary source;
4. install graphite cover;
5. place boat in quartz tube;
6. thoroughly purge with nitrogen before heating;
7. establish flowing H2;
8. heat to the equilibration/growth region;
9. contact the growth solution with the substrate only after the chosen thermal condition is reached.

### 5.1 Still OPEN/CAL

- N2 purge flow/time;
- H2 flow;
- purifier/getter specification;
- dew point/O2 acceptance;
- total pressure and tube pressure drop;
- exact boat axial position;
- furnace-zone dimensions;
- thermocouple type and location in historical Honeywell runs.

Local release therefore uses measured gas quality and temperature, not assumed flow values.

## 6. Source synthesis / homogenization — quantified transfer branch

Radhakrishnan et al. 2003 provide a practical, directly reported source-preparation branch:

- total synthesized growth compound: `10 g`;
- elemental feed: `6N` Cd, Te and Hg;
- representative liquid coordinates: `z≈0.049`, `y≈0.84` in `(Hg1−zCdz)1−yTey`;
- synthesis: evacuated quartz ampoule;
- synthesis temperature: `700 °C`;
- synthesis time: `8 h`;
- synthesized material subsequently ground and thoroughly mixed;
- charge used per growth run: `~4.8 g`;
- HgTe reservoir used per run: `3 g`.

These values belong to a different composition/device branch. They are **not** copied into the Honeywell x≈0.29 center.

### 6.1 Why this branch is valuable

It proves that an executable Te-rich slider process must define at least:

- elemental purity;
- batch mass;
- ampoule material and evacuation state;
- synthesis T/time;
- post-synthesis comminution/mixing;
- per-run aliquot mass;
- auxiliary HgTe inventory.

P30 therefore treats all of these as mandatory traveler fields.

## 7. Alternative in-situ solution preparation — separate branch

Bernardi et al. 1988 demonstrated in-situ preparation of Te-rich MCT growth solution by transporting Hg from vapor into a Cd-rich Te melt under controlled reactor conditions, avoiding separate ampoule preparation/homogenization for every run.

Classification: `PRIMARY-BERNARDI-1988 / ALTERNATE-SOLUTION-PREPARATION`.

Do not combine this approach with the ampoule-synthesis branch inside one recipe. It is a distinct process family requiring its own material-balance and equilibrium validation.

## 8. Equilibration

Harman 1980 reports:

- growth temperatures used: `450–550 °C`;
- growth times used: `0.25–10 min`;
- typical growth-solution equilibration: `~1 h at 550 °C`;
- highest-quality layers used source wafers, supercooled solutions and `(111)` substrates;
- reported layer thicknesses in that study: `3–15 µm`.

The Honeywell patent separately describes heating above the liquidus and then bringing the solution below the liquidus for growth.

### P30 rule

`1 h at 550 °C` is a direct Harman branch value, not a universal xL=.082/yL=.810 setpoint.

For the local x≈0.30 branch record:

- `t_above_TL_start/end`;
- peak charge temperature;
- hold duration above TL;
- measured temperature at the melt/boat region;
- evidence used to declare equilibration;
- subsequent cooling trajectory.

## 9. Thermal trajectory and supercooling

Honeywell directly permits three families:

1. step supercooling before contact;
2. contact near liquidus followed by slow cooling;
3. a combination.

For the xL=.082/yL=.810 tie line, `TL=507 °C`. A 500 °C contact would correspond to a derived nominal supercooling of about `7 K`, but this remains an experiment-sizing point only.

Shinohara et al. 1994 directly demonstrate that thermal trajectory strongly changes thickness and wipe-off behavior:

- equilibrium cooling from the melting point produced thin `2–4 µm` MCT layers with slightly terraced surfaces;
- supercooling/step cooling with `15 K` supercooling produced thick `30–40 µm` layers;
- compositions covered `x≈0.25–0.42`.

Therefore temperature history may not be collapsed to one scalar `Tgrowth`.

## 10. Growth contact

Honeywell patent operation:

- substrate sits in the base recess;
- the molten growth-well charge is translated over the substrate to initiate growth;
- growth ends when the well is translated away.

The same patent gives an **example** in which growth may continue for about `0.5 h`.

Harman's direct experimental branch used `0.25–10 min`.

These values are intentionally preserved as different branches.

### 10.1 Required local contact record

Record with timestamps:

- slider pre-contact position;
- temperature at first physical overlap;
- actual supercooling at contact;
- contact start;
- contact end;
- contact duration;
- commanded slider speed;
- measured travel time;
- any pause/stiction;
- full `T(t)` during contact;
- run number for this melt/source genealogy.

## 11. Charge mass, well fill and depletion

Total charge mass is a coupled apparatus coordinate, not a cosmetic scaling variable.

P30 records:

- synthesized batch ID;
- pre-run aliquot mass;
- growth-well volume;
- estimated/observed fill height;
- substrate overlap area;
- pre/post-run residual charge mass where feasible;
- material removed with wipe-off elements;
- source-reuse count;
- cumulative grown HgCdTe volume/mass estimate;
- change in layer x, thickness and morphology with source age.

P03D depletion rules remain controlling.

## 12. Hg-loss compensation

Honeywell mechanism:

- auxiliary HgTe or HgTe+Te is placed under the graphite cover;
- Hg vapor from that source surrounds the growth-solution region;
- near 500 °C the relevant Te-rich growth solution and HgTe source produce Hg vapor pressure on the order of `0.1 atm` in the patent description;
- the source compensates Hg that would otherwise be swept away in flowing H2.

The exact auxiliary-source composition need not remain fixed as Hg is lost because the patent argues Hg vapor pressure is relatively insensitive to source composition in the relevant Te-rich range.

### Qualification observables

- source initial/final mass;
- source geometry/area;
- source reuse count;
- growth-charge mass change;
- run-order drift in `xS`/cutoff;
- Hg-loss surface features;
- liquidus-temperature drift.

Shinohara 1994 independently found that increasing HgTe reservoir amount could stabilize source-liquid weight change due to Hg evaporation, reinforcing reservoir inventory as a process variable.

## 13. Wipe-off is a distinct unit operation

Te-rich solution has low surface tension and can remain as residual droplets/films after slide-out. P30 therefore treats wipe-off as a controlled process, not merely “move slider away.”

### 13.1 Honeywell CdTe-piece wipe-off — US4592304A

Direct features:

- dedicated wipe-off well adjacent to growth well;
- several CdTe pieces held in vertical slots about `1 mm` apart;
- pieces may be polycrystalline and unpolished;
- pieces rest against the base surface;
- on slide-out they remove residual solution by mechanical wiping, surface-tension adhesion and capillary wicking;
- pieces are discarded after cooldown.

Classification: `DIRECT-HONEYWELL-WIPEOFF`.

### 13.2 Honeywell scribed-apron wipe-off — US4706604A

Later Honeywell improvement:

- discardable CdTe apron placed in tandem with the growth substrate;
- apron can be polycrystalline CdTe or single crystal of any orientation;
- exposed apron carries diagonal diamond-scribed marks;
- growth solution overlaps at least part of apron during growth;
- on slide-out, residual solution is drawn onto/retained by apron rather than migrating back to the epilayer;
- cooling well subsequently covers the region;
- patent reports complete/“100%” wipe-off for this geometry.

This is a distinct hardware generation; do not silently combine it with the earlier CdTe-piece well.

## 14. Slider clearance and scratch risk

US4706604A explicitly states that the slider must float a finite distance above the grown epilayer; zero clearance would scratch the HgCdTe. That finite clearance also permits a residual liquid film, creating the back-migration problem.

Therefore local release must measure/control:

- slider-to-base clearance;
- substrate recess height relative to base;
- epilayer thickness at slide-out;
- wipe-off contact geometry;
- slider flatness;
- scratch density after growth.

No arbitrary micron clearance is assigned without local metrology.

## 15. Slide-out dynamics

Radhakrishnan et al. emphasize smooth and uniform slide-out as necessary to minimize voids, pinholes, melt traps and residual melt.

P30 records:

- slide-out direction;
- commanded speed;
- measured travel time;
- acceleration profile if actuator supports it;
- stick-slip or force anomaly;
- separation temperature;
- residual-droplet area fraction;
- scratch/terrace morphology.

A nominal motor speed without actual travel verification is insufficient.

## 16. Post-contact cooling

The selected thermal branch must define the trajectory after separation.

Record:

- separation temperature;
- cooling-well position/time where applicable;
- `T(t)` until below the temperature at which residual Te-rich solution can move/reflow;
- atmosphere during cooldown;
- time at any intentional hold;
- time to boat removal;
- visual state of wipe-off element after cooldown.

Do not infer the RP-01 cooldown from later anneal procedures.

## 17. Required process outputs

Every P30 run must map apparatus/process coordinates to:

### Surface
- whole-layer image;
- residual-melt area fraction;
- largest residual droplet;
- void/pinhole density;
- scratch density;
- terrace morphology;
- edge-loss width.

### Layer
- P06 thickness map;
- composition/optical-edge map;
- mean and spatial variation;
- HRXRD/defect metric where available.

### Electrical
- pre/post-anneal P05 transport on matched coupon;
- carrier sign;
- density/mobility;
- P13 lifetime/device proxy when material permits.

### Genealogy
- growth-solution batch;
- aliquot/run number;
- Hg-source batch/run count;
- boat revision;
- substrate lot/face;
- operator/tool/date.

## 18. First local x≈0.30 transfer strategy

Do not merge all published numbers into one synthetic “literature recipe.”

Use the following hierarchy:

1. **Composition center:** Honeywell xL=.082/yL=.810/TL=507 °C.
2. **Hardware topology:** covered Honeywell graphite horizontal-slider/Hg-source architecture.
3. **Practical source-prep branch for experiment sizing:** Radhakrishnan 700 °C/8 h ampoule synthesis and measured per-run charge concept, but rescaled only after local well-volume/material-balance work.
4. **Equilibration scale:** Harman 1 h at 550 °C as a transfer datum, not a setpoint.
5. **Contact-time scale:** Harman 0.25–10 min and Honeywell ~30-min example as separate bracket evidence.
6. **Wipe-off architecture:** qualify one defined Honeywell-derived branch at a time (CdTe-piece well or scribed apron), plus smooth-actuation control.
7. **Release:** based on x/thickness/morphology/electrical repeatability, not literature resemblance.

## 19. Explicit OPEN blockers after Round 23

Still unrecovered for exact RP-01/Fermionics x≈0.30 material:

- exact boat drawing/dimensions;
- graphite grade;
- exact total charge mass;
- exact source-synthesis method;
- exact Hg source mass/geometry;
- N2/H2 flows and gas-purity controls;
- historical thermocouple placement/calibration;
- actual equilibration T/time;
- actual supercooling and cooling rate;
- exact substrate-contact time;
- exact slider speed/clearance;
- exact wipe-off hardware generation;
- exact cooldown trajectory;
- whether/rehow the melt was reused.

## 20. Release rule

P30 remains `EMPIRICAL-QUALIFICATION` until one locally defined apparatus/recipe shows repeatable:

- target x and thickness;
- acceptable spatial uniformity;
- low residual-melt/scratch/void burden;
- stable source genealogy;
- acceptable post-anneal transport;
- detector-relevant downstream performance over multiple independent runs.

## 21. Primary sources

1. J. E. Bowers, J. L. Schmit, US4317689A, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution.”
2. R. J. Hager, R. A. Wood, US4592304A, “Apparatus for liquid phase epitaxy of mercury cadmium telluride.”
3. R. J. Hager, US4706604A, “Wipe-off apparatus of liquid phase epitaxy of mercury cadmium telluride.”
4. T. C. Harman, “Liquidus isotherms, solidus lines and LPE growth in the Te-rich corner of the Hg-Cd-Te system,” J. Electron. Mater. 9 (1980), DOI 10.1007/BF02822728.
5. J. K. Radhakrishnan, S. Sitharaman, S. C. Gupta, “Liquid phase epitaxial growth of HgCdTe using a modified horizontal slider,” J. Cryst. Growth 252 (2003) 79–86, DOI 10.1016/S0022-0248(02)02530-7.
6. M. Shinohara et al., “Hg-loss compensation and wiping-off of source liquid on slider liquid phase epitaxy of Hg1−xCdxTe,” J. Cryst. Growth 141 (1994) 352–356, DOI 10.1016/0022-0248(94)90237-2.
7. S. F. Bernardi et al., “Slider LPE growth of MCT using in situ Te-solution preparation,” J. Cryst. Growth 87 (1988) 365–371, DOI 10.1016/0022-0248(88)90189-3.
