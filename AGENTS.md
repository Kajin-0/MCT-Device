# AGENTS.md — MCT-Device continuity record

## Mission

Develop an extremely detailed, source-traceable procedure for fabricating and characterizing HgCdTe photodetectors. The endpoint is a booklet/manual plus process travelers that specify measurements, metrics, times, equipment, machinery, tolerances, calibration requirements, acceptance criteria, failure modes, and provenance sufficiently well that a competent researcher can reproduce the process without relying on undocumented tribal knowledge.

## Non-negotiable research rules

1. **Do not fabricate missing numbers.** A blank or `[Q]` qualification requirement is preferable to a plausible but untraceable setpoint.
2. **Do not splice process families casually.** HgCdTe composition, substrate orientation, melt chemistry, Hg chemical potential, passivation, etch history, doping, and thermal history are coupled.
3. **Primary literature first.** Books/reviews are excellent maps, but process-critical numbers should be traced to original experimental sources wherever possible.
4. **Separate four things:** published observation, derived physics, apparatus calibration, and proposed qualification experiment.
5. **Preserve negative results.** If a paper/process is rejected as incompatible with the reference process, record why.
6. **Every critical process step needs metrology.** A setpoint without a measurement confirming the resulting material/device state is insufficient.
7. **Every process module needs a gate.** State what must be true before the sample advances.
8. **Safety is part of reproducibility.** Hg, Cd-containing material, corrosive wet chemistry, vacuum systems, high temperatures, methane/hydrogen plasmas, cryogens, and electrical systems require institution-approved EH&S procedures and apparatus-specific risk assessment. Do not substitute this repository for local chemical hygiene, hazardous-gas, pressure/vacuum, or high-temperature operating procedures.

## Current state — 2026-08-15

Repository initialized. RP-01 has been selected as the first downstream reference process:

> E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, and L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001). DOI: 10.1088/0268-1242/16/6/306.

Why RP-01 was selected:

- actual n-type HgCdTe photoconductors were fabricated and measured;
- starting epilayer composition, carrier density, and mobility are stated;
- RIE reactor type, gas mixture, total flow, pressure, RF power, and process time are stated;
- photoresist thickness/prebake/chlorobenzene soak are stated;
- anodic oxide thickness and Cr/Au metallization thicknesses are stated;
- RIE-induced n+ carrier density and mobility were measured;
- contact resistivity was measured by TLM;
- detector responsivity, noise, cutoff, and D* were reported under stated test conditions.

Important: RP-01 does **not** publish enough information to reproduce every upstream and downstream operation without additional sources. Missing data are not to be guessed.

## RP-01 published anchors currently extracted

Starting material:

- LPE-grown HgCdTe on insulating CdZnTe `[P]`.
- x ≈ 0.30, n-type `[P]`.
- starting carrier density: 9.8×10^14 cm^-3 `[P]`.
- starting electron mobility: 4.0×10^4 cm^2 V^-1 s^-1 `[P]`.
- experimental device layer thickness: 9.5 µm `[P]`.

RIE/contact module:

- parallel-plate Plasma Technology reactor `[P]`.
- CH4/5H2 gas mixture `[P]`.
- total flow: 64 sccm `[P]`.
- chamber pressure: 100 mTorr `[P]`.
- RF power: 50 W `[P]`.
- process time: 1 min `[P]`.
- resulting RIE-converted carrier density: 2.0×10^15 cm^-3 `[P]`.
- resulting mobility: 3.3×10^4 cm^2 V^-1 s^-1 `[P]`.
- prior related work cited by Smith et al. indicated approximately 8 µm conversion depth under similar conditions; do not treat this depth as a directly measured RP-01 value `[T/P-other-source]`.

Lithography/lift-off test:

- photoresist thickness: approximately 4–5 µm `[P]`.
- prebake: 80 °C, 30 min `[P]`.
- chlorobenzene soak: 30 min `[P]`.
- pattern/develop/water rinse stated, but resist identity, exposure dose, developer identity/concentration, and develop time are not specified in RP-01 `[GAP]`.

Passivation/metallization:

- anodic oxide: 800 Å `[P]`.
- Cr: 300 Å `[P]`.
- Au: 2700 Å `[P]`.
- deposition base pressure/rate/substrate temperature are not specified `[GAP]`.

Contact test structure:

- nine contacts `[P]`.
- each contact 300 µm × 300 µm `[P]`.
- first spacing 50 µm; successive spacings increase in 50 µm increments `[P]`.
- TLM specific contact resistivity at 80 K: 9×10^-4 Ω cm^2 `[P]`.

Detector characterization:

- spectral response system: Optronics Laboratories Spectral Response Measurement System `[P]`.
- operating temperature: 80 K `[P]`.
- field of view: 60° `[P]`.
- chopping frequency: 1 kHz `[P]`.
- representative noise measurement field: 10 V cm^-1 `[P]`.
- noise analyzer: HP35665A spectrum analyzer with low-noise preamplifier `[P]`.
- 1/f knee: ~3 kHz `[P]`.
- g-r noise voltage: ~24.5 nV Hz^-1/2 `[P]`.
- measured spectral cutoff: 4.4 µm `[P]`.
- BLIP D*: 2.0×10^11 cm Hz^1/2 W^-1 at 4 µm `[P]`.
- reported background photon flux: 1.0×10^15 cm^-2 s^-1 for 300 K background, 60° FOV `[P]`.
- reported quantum efficiency: 70% `[P]`.

## Known gaps requiring closure

### Starting material / LPE

- exact RP-01 LPE growth recipe used by Fermionics;
- CdZnTe composition, orientation, resistivity, dimensions, and surface preparation;
- growth-solution composition and mass;
- furnace/boat geometry;
- equilibration temperature/time;
- growth temperature, supercooling, cooling rate, contact time;
- Hg-loss compensation;
- post-growth anneal and stoichiometry control;
- wafer uniformity metrics.

### Mesa isolation

- exact mask geometry for the measured photoconductors;
- photoresist and exposure/development conditions for Mask 1;
- exact wet chemical mesa etchant concentration, temperature, agitation, etch rate, endpoint, depth, and rinse sequence.

**Mesa branch decision now closed:** same-UWA-lineage papers from 1999 and 2000 establish that the intended RP-01-style n-type x≈0.31 photoconductors should retain the wet bromine/HBr mesa branch. Blanket CH4/H2 dry mesa etching modifies active-region electrical properties and degraded detector performance in the published comparison. Use RIE narrowly at RP-01 contact windows, where the n+ conversion is intentional.

### Passivation

- anodization electrolyte;
- current/voltage mode;
- current density;
- anodization time;
- oxide growth calibration;
- post-anodization rinse/dry;
- whether ZnS was present on the actual experimental devices discussed in RP-01 (paper explicitly states 800 Å anodic oxide for experimental devices; do not add ZnS without evidence).

**Passivation candidate now identified:** historical HgCdTe photoconductor processes report 800 Å native anodic oxide using a constant-current KOH/ethylene-glycol/water process. This is a strong qualification candidate because it independently reproduces the RP-01 film thickness, but it is not yet proven to be the exact UWA recipe. See `research/2026-08-15_passivation_lineage.md`.

### Metal deposition/lift-off

- deposition method;
- base pressure;
- deposition rates;
- delay between RIE and metallization;
- sample temperature;
- lift-off solvent/time/agitation;
- wire-bond metallurgy and package attachment.

### Device characterization

- exact active detector length/width used for the representative RP-01 device;
- bias circuit and load resistor;
- optical calibration traceability;
- noise preamplifier model/gain/input noise;
- FFT/RBW/ENBW/averaging settings;
- spectral bandwidth definition used for reported D*.

## Same-lineage process sources now accepted into the research tree

### Smith et al. 1999 — mesa RIE versus wet etch

E. P. G. Smith et al., *J. Vac. Sci. Technol. A* 17, 2503–2509 (1999), DOI `10.1116/1.581988`.

Use: establishes electrical modification from CH4/H2 RIE and supports wet chemical mesa isolation when preserving active-region electrical state is the priority.

### Smith et al. 2000 — detector-level mesa comparison

E. P. G. Smith et al., *J. Electron. Mater.* 29(6), 853–858 (2000), DOI `10.1007/s11664-000-0237-7`.

Use: direct n-type x≈0.31 photoconductor comparison of wet bromine/HBr versus H2/CH4 dry mesa processing; strongly supports RP-01 wet-mesa branch.

### Musca et al. 1998 — RIE-induced n-type region characterization

C. A. Musca et al., *J. Electron. Mater.* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.

Use: LBIC confirmation and spatial characterization of RIE-induced n-type/n+ regions; this is the correct lineage to audit for conversion-depth claims.

### Agnihotri, Musca, Faraone 1998 — passivation review

O. P. Agnihotri, C. A. Musca, and L. Faraone, *Semicond. Sci. Technol.* 13, 839–847 (1998), DOI `10.1088/0268-1242/13/8/002`.

Use: map same-laboratory passivation physics and primary anodic-oxide references; executable setpoints still need primary-source closure.

## Upstream LPE lead under investigation

Radhakrishnan, Sitharaman, and Gupta, *J. Crystal Growth* 252, 79–86 (2003), DOI 10.1016/S0022-0248(02)02530-7, reports a modified horizontal-slider Te-rich LPE process with Hg-loss compensation and in-situ meltback. Published anchors include 6N elemental sources, synthesis at 700 °C for 8 h, ~4.8 g charge per growth run, 3 g HgTe for Hg-loss compensation, and a 15×15×1 mm CdZnTe substrate recess. This is a strong apparatus/process source but **must not yet be declared the RP-01 upstream recipe** until material composition and electrical-state compatibility are closed.

Tung et al., *J. Crystal Growth* 56, 485–489 (1982), DOI `10.1016/0022-0248(82)90468-7`, is the high-priority composition-matched lead because its Te-rich horizontal-slider work explicitly includes x≈0.30 material.

## Most natural next work

1. Recover the **exact Br2/HBr wet mesa recipe** from the UWA 1999/2000 experimental sections or directly linked theses/process papers.
2. Recover the **exact UWA anodic-oxide process** used for the 800 Å RP-01 film; if unavailable, formalize and qualify the historical 800 Å constant-current candidate rather than silently adopting it.
3. Audit Musca et al. 1998 for exact RIE conversion-depth conditions and separate them from RP-01 contact-window conditions.
4. Fully extract the x≈0.30 Tung LPE process and compare material/electrical outputs with RP-01.
5. Build the first `procedures/` module only when one step has complete setpoints, apparatus transfer requirements, metrology, and go/no-go criteria.
6. Continue dated research logs for all accepted and rejected branches.
