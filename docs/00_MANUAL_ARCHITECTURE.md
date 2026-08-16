# Manual architecture

## Working title

**Reproducible Fabrication and Characterization of HgCdTe Infrared Photodetectors: A Source-Traceable Process Manual**

## Design philosophy

The final manual is intended to behave like a controlled semiconductor process specification rather than a narrative review. Each chapter must distinguish:

- target device physics;
- material state entering the process;
- apparatus state;
- operator action;
- measured output state;
- acceptance criterion;
- source provenance;
- uncertainty;
- failure disposition.

A researcher should never have to infer whether a quoted temperature is furnace setpoint, sample temperature, melt temperature, reservoir temperature, or measured local temperature. Similar distinctions are required for pressure, gas flow, dimensions, optical power, detector temperature, electrical bandwidth, and noise normalization.

---

# Part I — Device definition and physical design

## 1. Reference detector specification

Define the exact detector architecture before fabrication begins:

- PC or PV architecture;
- spectral band and cutoff convention;
- operating temperature;
- active dimensions;
- absorber thickness;
- target alloy composition x;
- conductivity type;
- carrier concentration and mobility range;
- minority-carrier lifetime target;
- contact architecture;
- passivation architecture;
- resistance range;
- allowable bias field/current/power;
- target responsivity, noise PSD, NEP, D*, and temporal response.

Each target is assigned an acceptance class:

- **hard gate** — sample cannot proceed if out of range;
- **characterization gate** — process may proceed but deviation must be recorded;
- **informational** — measured for process learning but not currently yield-limiting.

## 2. Material-property model

Required equations and validity ranges:

- HgCdTe band gap Eg(x,T);
- composition-to-cutoff relations;
- intrinsic carrier concentration;
- carrier mobility models;
- resistivity;
- absorption coefficient and absorption depth;
- radiative/Auger/SRH lifetime models where relevant;
- photoconductive gain;
- responsivity;
- Johnson, generation-recombination, photon-background, and 1/f noise models;
- NEP and D* definitions;
- uncertainty propagation.

No equation enters the controlled calculation set without units, assumptions, validity interval, and original citation.

---

# Part II — Facility, equipment, and calibration

## 3. Facility/EH&S prerequisites

The process manual must identify, but not replace, institution-approved SOPs for:

- Hg and Cd-containing material handling;
- wet corrosive chemistry;
- methane/hydrogen gas systems;
- high-temperature sealed ampoules and furnaces;
- vacuum equipment;
- cryogens;
- high voltage/current and RF equipment;
- waste segregation and contamination control.

A process traveler must include a field confirming that the applicable local SOP and training are current before hazardous operations.

## 4. Equipment register

For every instrument:

- manufacturer/model or functional minimum specification;
- measurement range;
- resolution;
- absolute accuracy;
- repeatability;
- calibration interval;
- calibration standard;
- uncertainty contribution;
- maintenance state;
- software/firmware version if it affects results.

Equipment families include:

- analytical balance;
- furnace and zone controllers;
- thermocouples/RTDs;
- vacuum gauges;
- mass-flow controllers;
- pressure regulators/gauges;
- quartz ampoules and graphite/quartz boats;
- microscope/profilometer/AFM;
- FTIR/monochromator;
- XRD;
- Hall/Van der Pauw station;
- photolithography equipment;
- RIE/ICP-RIE;
- evaporation/sputtering;
- wire bonder/die attach;
- cryostat and temperature controller;
- calibrated blackbody/source;
- chopper/lock-in;
- spectrum analyzer/FFT acquisition system;
- low-noise preamplifier.

---

# Part III — Material growth

## 5. Incoming elemental/source-material qualification

Record:

- supplier;
- lot;
- stated purity;
- certificate of analysis;
- mass uncertainty;
- storage history;
- contamination controls;
- rejection criteria.

## 6. CdZnTe substrate qualification

Record:

- Cd/Zn composition;
- crystal orientation and miscut;
- dimensions;
- thickness;
- resistivity/insulating behavior;
- polish specification;
- surface roughness;
- inclusion/precipitate density if available;
- etch-pit density/dislocation metric if required;
- IR transmission/microscopy;
- lot map.

## 7. Substrate preparation

Must eventually specify:

- dicing;
- lapping/polishing;
- solvent sequence;
- oxide/chemical treatment;
- rinse-water specification;
- dry method;
- maximum allowed time to growth loading;
- pre-growth inspection and rejection criteria.

## 8. LPE charge synthesis

Required fields:

- elemental masses and uncertainty;
- molar/atomic fractions;
- ampoule internal volume;
- evacuation criterion;
- backfill if used;
- synthesis temperature profile;
- ramp rates;
- homogenization time/method;
- cooldown;
- recovered mass;
- allowable Hg mass loss;
- post-synthesis homogenization/sectioning.

## 9. LPE growth

Required fields:

- growth method/boat geometry;
- furnace temperature profile and mapped gradients;
- thermocouple positions;
- solution mass/composition;
- Hg-loss compensation method;
- substrate orientation;
- meltback/wash step if used;
- equilibration temperature/time;
- supercooling;
- substrate contact time;
- cooling rate during growth;
- rotation/tilt/slider velocity if relevant;
- solution wipe-off/decant procedure;
- cooldown atmosphere/profile;
- run-abort limits.

Outputs:

- epilayer thickness map;
- composition/cutoff map;
- morphology/defect map;
- Hall concentration/mobility;
- resistivity;
- uniformity metrics.

## 10. Post-growth anneal / stoichiometry control

Define:

- Hg chemical-potential boundary condition;
- reservoir arrangement;
- temperature;
- dwell;
- ramp/cooldown;
- sample position;
- pre/post Hall data;
- pre/post optical cutoff;
- acceptance window.

---

# Part IV — Device fabrication

## 11. Device/mask geometry

Archive machine-readable and human-readable dimensions for:

- detector mesa;
- contact openings;
- contact pads;
- active optical region;
- TLM structures;
- Van der Pauw structures;
- alignment marks;
- dicing lanes;
- process-control monitors.

## 12. Mesa lithography and isolation

Record:

- resist product/lot;
- dehydration treatment;
- dispense volume;
- spin speed/acceleration/time;
- measured resist thickness;
- prebake temperature/time;
- exposure wavelength/intensity/dose;
- focus/contact mode;
- developer/concentration/time/temperature/agitation;
- CD inspection;
- etchant composition;
- bath temperature;
- etch rate;
- time/depth;
- endpoint;
- undercut;
- rinse/dry;
- resist strip;
- post-etch surface inspection.

## 13. Passivation

Treat each passivation family as a separate qualified module. Potential families include native anodic oxide, ZnS-over-oxide, CdTe, sulfide treatments, SiNx, etc. Never merge values from one family into another.

Metrics:

- thickness/uniformity;
- fixed charge/interface-state evidence where measured;
- leakage/shunt resistance;
- 1/f noise impact;
- adhesion and thermal-cycle stability.

## 14. Contact-window opening / blocking-contact formation

For RP-01 this is a CH4/H2 RIE module combining oxide removal and n+ conversion. Required controls include:

- gas composition and purity;
- MFC calibration;
- chamber base pressure;
- process pressure;
- RF power definition and calibration;
- electrode spacing;
- sample temperature;
- process duration;
- endpoint for passivation removal;
- induced carrier density/mobility;
- converted depth;
- plasma damage characterization.

## 15. Metallization and lift-off

Record:

- surface delay after contact opening;
- deposition tool;
- base pressure;
- metal purity;
- layer sequence/thickness;
- rate;
- substrate temperature;
- vacuum break status;
- lift-off chemistry/time/agitation;
- final optical inspection;
- TLM contact resistance.

## 16. Dicing, die attach, wire bonding, packaging

Record:

- dicing protection;
- blade/specification and feed;
- die cleaning;
- die-attach material/thickness/cure;
- package metallurgy;
- bond wire material/diameter;
- bond parameters;
- pull/shear acceptance;
- package leak/thermal-cycle requirements if used.

---

# Part V — Characterization

## 17. Structural/optical material qualification

- optical microscopy/Nomarski;
- thickness by profilometry/cross-section/FTIR fringes;
- FTIR cutoff/composition mapping;
- XRD where available;
- surface roughness;
- defect-density metrics.

## 18. Hall and resistivity

Specify:

- geometry;
- contact formation;
- magnetic field and calibration;
- current magnitude;
- temperature;
- field reversal;
- polarity checks;
- calculation method;
- uncertainty.

## 19. DC electrical characterization

- I–V;
- differential resistance;
- polarity symmetry;
- bias-field normalization;
- self-heating test;
- contact contribution;
- temperature dependence.

## 20. Spectral responsivity

- source and traceability;
- monochromator/FTIR configuration;
- slit/bandwidth;
- chopper frequency;
- reference detector;
- detector temperature;
- FOV/aperture;
- bias field;
- optical power;
- cutoff definitions;
- calibration uncertainty.

## 21. Noise

- circuit topology;
- bias source;
- load resistor;
- preamplifier model/gain/noise;
- analyzer settings;
- frequency span;
- RBW/ENBW;
- averaging;
- window;
- shielding/grounding;
- detector temperature;
- optical background;
- bias field;
- measured electronics floor;
- Johnson prediction;
- 1/f fit/knee;
- g-r plateau/model;
- uncertainty.

## 22. Temporal response

- modulated source;
- modulation transfer calibration;
- amplitude and phase versus frequency;
- -3 dB definition;
- rise/fall-time measurement;
- lifetime extraction;
- electronics de-embedding.

## 23. Absolute performance

Calculate and report:

- responsivity;
- quantum efficiency if independently supportable;
- NEP;
- D*;
- background-limited condition;
- uncertainty budget;
- comparison against theoretical limit under identical optical/electrical bandwidth definitions.

---

# Part VI — Process control and reproducibility

## 24. Process-control charts

Per run/device record at minimum:

- source/substrate lots;
- growth run ID;
- melt chemistry;
- furnace calibration ID;
- thickness;
- x/cutoff;
- n, p, mobility, resistivity;
- passivation thickness;
- contact resistivity;
- device resistance;
- responsivity;
- 1/f knee;
- white/g-r noise;
- cutoff;
- D*;
- yield.

## 25. Failure-analysis atlas

Each failure entry should contain:

- symptom;
- quantitative signature;
- likely causes ranked by plausibility;
- discriminating measurements;
- corrective action;
- evidence/source.

## 26. Master traveler

Final executable format for every operation:

`STEP ID -> prerequisite -> equipment -> calibration status -> material ID -> action -> setpoint -> tolerance -> duration/rate -> measurement -> acceptance criterion -> operator record -> disposition -> next step`

The traveler is the endpoint of the research, not the starting point.
