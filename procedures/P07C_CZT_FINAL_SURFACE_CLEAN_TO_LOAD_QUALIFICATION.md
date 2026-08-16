# P07C — CdZnTe final surface preparation / removal-depth / clean-to-load qualification

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. Supplements P07/P07A/P07B.

## 1. Purpose

Define the final CdZnTe surface state immediately before x≈0.30 Te-rich LPE by measurable interface variables rather than by copying a bromine/methanol concentration and time from a different growth branch.

The release objective is a reproducible substrate surface that:

- removes mechanically damaged material;
- has controlled roughness/topography;
- has a known/consistent chemical termination state;
- is not significantly reoxidized/contaminated before LPE contact;
- yields reproducible HgCdTe nucleation, morphology, composition and transport.

## 2. Historical RP-01 state

RP-01 states only that LPE HgCdTe was supplied on electrically insulating CdZnTe.

The original supplier's final:

- polish sequence;
- chemical etchant;
- bromine concentration basis;
- etch duration;
- material-removal depth;
- rinse/dry sequence;
- clean-to-load delay

are not published.

These remain historically `OPEN`.

## 3. LPE-specific transfer candidate

A detector-oriented Te-rich LPE branch on `(111)B` CdZnTe reports:

- chemical + mechanical polishing;
- final `2–3% Br2/methanol` treatment;
- immersion for only a few seconds;
- loading into the graphite boat immediately afterward.

The branch produces x≈0.20–0.22 material, not RP-01 x≈0.30.

Use it as evidence that a **brief bromine/methanol final surface treatment with short clean-to-load interval** is a legitimate LPE interface-preparation strategy.

Do not transfer its concentration/time as the historical RP-01 recipe.

## 4. Independent CdZnTe surface evidence

Primary CdZnTe surface studies show that Br–methanol:

- removes mechanically damaged surface material;
- generally improves surface crystalline/morphological quality;
- produces a Te-enriched surface;
- can alter IR transmission;
- can produce different pitting/waviness behavior as concentration/time change.

Examples:

### Bensouici et al. 2010

“Study of effects of polishing and etching processes on Cd1−xZnxTe surface quality,” *Journal of Crystal Growth* 312, 2098–2102 (2010), DOI `10.1016/j.jcrysgro.2010.03.045`.

For its radiation-detector CdZnTe material, 2% Br–MeOH for 30 s was reported as an optimal condition among the tested set. Etching produced Te enrichment.

### Zheng et al. 2011

“Influence of surface preparation on CdZnTe nuclear radiation detectors,” *Applied Surface Science* 257, 8742–8746 (2011), DOI `10.1016/j.apsusc.2011.05.098`.

The study found Br–methanol produced favorable surface crystallinity/roughness compared with other alcohol solvents, while concentration changes altered pitting/waviness behavior and produced a Te-rich surface.

These are **surface-physics/metrology sources**, not LPE recipe sources.

## 5. Why concentration/time alone are poor release variables

The same nominal Br2 concentration can produce different final surfaces because of:

- bromine stock purity/age;
- concentration preparation basis;
- solution evaporation;
- temperature;
- agitation;
- sample orientation;
- polishing damage depth;
- face/polarity;
- surface area/solution volume ratio;
- rinse latency;
- solution reuse.

Therefore the traveler shall control both process inputs and measured output surface state.

## 6. Pre-etch mechanical state

Before final chemical preparation record:

- substrate ID/lot;
- plane/polarity/miscut from P07B;
- slicing method/history;
- lapping abrasives/particle sizes;
- polishing slurry/abrasive;
- polish duration/load;
- surface roughness;
- DIC/optical image;
- residual scratch/pit map.

A chemically etched surface cannot be interpreted without knowing the starting mechanical damage state.

## 7. Removal-depth qualification

For each candidate final etch condition determine the material removed.

Preferred methods:

- protected-step profilometry;
- calibrated thickness before/after treatment;
- sacrificial witness geometry;
- cross-sectional verification during process development.

Report:

- mean removed depth;
- spatial variation;
- run-to-run repeatability.

The final process should remove enough material to eliminate the mechanically damaged layer without excessive substrate consumption or morphology degradation.

Do not assume “few seconds” corresponds to the same removed depth across lots/solutions/faces.

## 8. Candidate chemical-treatment DOE

During local qualification, compare a bounded matrix around the LPE-specific brief Br2/methanol branch.

Variables may include:

- Br2 concentration;
- exposure time;
- solution temperature;
- agitation/no agitation;
- solution age/reuse state.

Use only a range approved by local hazardous-chemical procedures.

The purpose is to map output surface state, not to maximize etch rate.

## 9. Required surface outputs

For each condition measure as available:

### Morphology

- AFM RMS roughness;
- peak-to-valley/large-feature roughness;
- DIC/Nomarski images;
- SEM on sacrificial coupons where useful;
- pit density/size;
- wave/terrace-like chemical-etch artifacts.

### Structural quality

- HRXRD rocking curve before/after treatment where sensitivity permits;
- evidence of residual polishing damage.

### Chemistry

Preferred during qualification:

- XPS/EDS or equivalent surface-composition evidence;
- Te/(Cd+Zn) trend;
- oxide/elemental Te state;
- contamination residue.

The released production process may use a simpler correlated proxy once the surface-state relation is established.

## 10. Face/polarity dependence

P07B demonstrates that growth-face selection is process critical.

The final chemical treatment must be qualified on the **selected actual face/polarity/miscut**.

Do not assume:

- Cd-terminated and Te-terminated surfaces etch identically;
- the same removal rate;
- the same final roughness;
- the same Te enrichment.

Changing substrate face requires P07C requalification unless equivalence is demonstrated.

## 11. Rinse/dry sequence

The released local traveler shall explicitly define:

- first rinse solvent;
- number/duration of rinse steps;
- DI-water use or avoidance based on validated interface result;
- final solvent rinse if used;
- drying method;
- handling tools/materials;
- permitted exposure to ambient.

The exact RP-01 historical sequence is not known.

Do not add a water rinse simply because a downstream surface-treatment paper used one; the correct sequence is determined by the local LPE interface result.

## 12. Clean-to-load clock

Define:

`t_CTL = t_growth-boat-load / furnace-load - t_end-final-surface-prep`

using an explicitly chosen endpoint/start convention.

Record at minimum:

- end-of-final-rinse timestamp;
- dry-complete timestamp;
- graphite-boat load timestamp;
- furnace/tube insertion or purge-start timestamp.

Atmospheric exposure can rebuild oxide/adsorbates after Br–methanol treatment, so the time history is a process variable.

## 13. Clean-to-load DOE

At fixed final surface chemistry, deliberately compare at least several exposure delays spanning the practical handling window.

Then perform otherwise matched LPE and measure:

- initial interface morphology;
- meltback behavior if used;
- epilayer surface morphology;
- thickness/x uniformity;
- interface defect density where measurable;
- P05 mobility after matched anneal;
- P13 lifetime/device proxy.

Release a maximum clean-to-load delay from detector-relevant output stability rather than from convention.

## 14. Ambient/environment control

Record the substrate environment between surface treatment and boat/furnace loading:

- ambient air;
- dry N2;
- clean bench classification;
- covered solvent-compatible container;
- other inert environment.

If an inert storage/transfer environment materially improves interface repeatability, include it in the production traveler.

## 15. Interaction with substrate meltback

If P03 uses an in-situ meltback/interface-cleaning step, P07C and meltback must be qualified jointly.

A deeper meltback may erase differences between final chemical treatments; a weak meltback may leave them dominant.

Measure actual removed depth from meltback and avoid double-removing excessive substrate material.

## 16. Interface acceptance vector

Define:

`Y_surface = {removed depth, roughness, pit/wave density, chemical-state proxy, t_CTL, epilayer morphology, interface-defect metric, mobility, lifetime}`.

A candidate P07C process passes only when both the substrate surface and the resulting epitaxial interface/material quality are repeatable.

## 17. Historical closure status

Exact RP-01/Fermionics final CdZnTe surface treatment remains `OPEN`.

P07C provides the controlled local path to release:

- chemical treatment;
- removal depth;
- rinse/dry;
- clean-to-load interval;
- surface-state acceptance

without manufacturing historical precision.