# P16 — RP-01 master end-to-end process traveler

**Status:** CONTROLLED QUALIFICATION TRAVELER — NOT `REPRODUCIBLE-RELEASE`.

## 1. Purpose

Integrate the controlled RP-01 process architecture, including P01–P35 and their applicable addenda/registers, into one auditable sequence from incoming CdZnTe substrate through a packaged, characterized HgCdTe photoconductor.

P16 does not replace the detailed procedure modules. It defines:

- process order;
- lot/sample genealogy;
- required witness structures;
- hold points;
- measurements that must exist before advancement;
- elapsed-time controls between sensitive steps;
- deviation/nonconformance handling;
- data package required to call one complete fabrication run traceable.

A run cannot be called “reproduced” merely because a functioning detector is obtained. It must satisfy the defined process-state and metrology gates.

Use `P16A_FIRST_BUILD_RELEASE_READINESS_AUDIT.md` and its readiness register before authorizing an end-to-end qualification build.

---

## 2. Process-state codes

Use only the following traveler states:

- `NOT STARTED`
- `IN PROCESS`
- `HOLD — DATA REQUIRED`
- `HOLD — ENGINEERING REVIEW`
- `PASS`
- `PASS-CONDITIONAL` — only with documented rationale and disposition
- `FAIL`
- `SCRAPPED`
- `REWORK AUTHORIZED` — only under an approved rework instruction

Never convert `OPEN`, `CAL`, or `QUAL` variables in the procedure documents into arbitrary traveler setpoints.

### 2.1 Project-maturity labels are separate from step status

Do not use a process-step `PASS` as evidence for a project-level maturity claim.

- `TRACEABLE-FIRST-BUILD-READY` — pre-execution state defined by P16A; every mandatory branch and metrology implementation is frozen enough to execute one qualification build without undocumented choices.
- `HISTORICAL-RP01-REPRODUCED` — historical-identity claim requiring source closure for the process identities actually represented as historical.
- `REPRODUCIBLE-RELEASE` — end-to-end release state requiring P17 measurement-system, stability/capability, detector-performance/yield and change-control evidence.

These are different axes.

---

## 3. Genealogy hierarchy

Every record must preserve this hierarchy:

`SOURCE LOT → LPE CHARGE → GROWTH RUN → EPILAYER/WAFER → COUPON/DIE → DEVICE → CONTACT PAIR → MEASUREMENT DATASET`

### 3.1 Required identifiers

Assign unique IDs for:

- `MAT-HG-####` mercury source lot;
- `MAT-CD-####` cadmium source lot;
- `MAT-TE-####` tellurium source lot;
- `SUB-CZT-####` CdZnTe substrate;
- `CHG-####` prepared growth charge;
- `LPE-YYYYMMDD-##` growth run;
- `WFR-####` resulting epitaxial wafer/sample;
- `COUP-####` material/process witness coupon;
- `DIE-####` singulated detector die;
- `DEV-####` individual device/string;
- `C1...C9` contact labels for the project nine-contact geometry;
- `DATA-####` measurement dataset.

The exact naming syntax may be adapted to the laboratory information system, but genealogy must remain one-to-one and reversible.

---

## 4. Required top-level traveler header

Record before work begins:

- traveler revision;
- RP-01 process revision;
- P16A readiness-register revision and disposition;
- date opened;
- responsible researcher/operator;
- approved equipment set;
- facility/location;
- intended reference-device variant;
- target composition;
- target layer thickness;
- target post-anneal transport state;
- target operating temperature;
- planned device/contact geometry;
- applicable procedure/addendum/register revisions through P35;
- applicable source-ledger revision;
- known historical substitutions/local-transfer branches;
- known deviations approved before start.

**Precondition:** `TRACEABLE-FIRST-BUILD-READY = YES` in P16A for the route being attempted. If NO, P16 may still be used for isolated module qualification, but not to represent a no-tribal-knowledge end-to-end build.

---

# PHASE A — incoming materials and substrate

## STEP A0 — facility / calibration / safety readiness

**Procedure references:** all modules as applicable.

Before material handling verify/document:

- required facility authorization/EH&S controls active;
- balances calibrated;
- thermometry calibrated;
- gas-flow/MFC calibration current;
- pressure/vacuum gauges calibrated where used;
- lithography dose/spin/hotplate calibration current;
- Hall magnetic-field calibration current;
- FTIR wavelength/intensity checks current;
- RIE tool qualification current;
- metal-thickness/QCM calibration current;
- singulation tool/calibration/inspection state where applicable;
- cryogenic thermometer calibration current;
- electrical/noise instrument calibration/current verification.

**Gate A0:** all critical calibrations/authorizations valid.

Status: ______  Date/time: ______  Operator: ______

---

## STEP A1 — elemental source receipt/lot record

Record for Hg/Cd/Te:

- supplier;
- lot;
- purity;
- CoA/impurity data;
- container state;
- storage history;
- opening date;
- mass inventory.

**Gate A1:** source materials meet current P03/P30 qualification requirements.

---

## STEP A2 — CdZnTe substrate qualification

**Procedures:** P07/P29 and applicable P07A/P07B/P07C.

Record:

- substrate ID;
- dimensions/thickness;
- Zn/lattice parameter/mismatch metric;
- face/polarity;
- miscut magnitude/azimuth;
- HRXRD metric;
- EPD/dislocation metric;
- IR inclusion/precipitate map;
- trace-impurity data where available;
- resistivity/leakage;
- surface roughness/polish state;
- microscopy images.

**Gate A2:** selected P07/P29 branch PASS or documented PASS-CONDITIONAL.

No LPE loading if substrate identity/polarity or surface condition is unresolved.

---

# PHASE B — charge preparation and LPE growth

## STEP B0 — growth-well / boat configuration record

**Procedures:** P03/P30.

Record:

- graphite boat ID/revision;
- growth-well dimensions;
- calculated/verified melt volume/depth;
- substrate recess geometry;
- Hg-source geometry;
- cover configuration;
- wipe-off configuration;
- thermocouple/sensor positions;
- previous run/cleaning history.

**Gate B0:** apparatus configuration matches the selected executable P30 branch.

---

## STEP B1 — charge calculation

Current composition-matched candidate tie line:

- `xL=0.082`;
- `yL=0.810`;
- derived mass fractions:
  - Hg `0.249738`;
  - Cd `0.012502`;
  - Te `0.737760`.

Total mass `M` must come from the locally qualified boat/melt-depth process; it remains apparatus-specific.

Record:

- target M;
- calculated target masses;
- balance ID;
- actual masses;
- actual normalized mole fractions;
- deviation from target xL/yL;
- propagated weighing uncertainty using the current charge-sensitivity calculation.

**Gate B1:** charge composition inside the currently authorized qualification/released window for the selected apparatus branch.

Do not round Cd mass prematurely; Cd weighing dominates direct xL error in this tie-line formulation.

---

## STEP B2 — charge synthesis / homogenization

**Procedures:** P03/P03C/P30.

Record complete:

- container/ampoule ID;
- loading sequence;
- evacuation/backfill conditions;
- temperature-time history;
- agitation/rocking history;
- cooldown;
- final visual state;
- recovered/available mass.

Current exact x≈0.30 historical synthesis schedule remains subject to qualification; do not silently insert a different-composition synthesis as historical RP-01 fact.

**Gate B2:** selected charge-preparation endpoint achieved.

---

## STEP B3 — substrate final pre-LPE surface preparation

**Procedures:** P07C/P29/P30.

Record:

- final surface chemistry;
- concentrations/bases/stock assays;
- removed depth where applicable;
- time;
- temperature;
- rinse/dry;
- microscopic surface state;
- completion timestamp;
- LPE-load timestamp.

Define:

`Δt_clean→load = t_load − t_clean_end`.

**Gate B3:** selected surface branch completed, clean-to-load interval inside its current qualification rule, and surface free of visible contamination/damage.

Historical RP-01 final CdZnTe surface chemistry may remain open; the local branch itself may not.

---

## STEP B4 — LPE atmosphere / thermal equilibration

**Procedures:** P03/P03E/P30.

Record continuously where possible:

- N2 purge flow/time;
- residual O2/H2O if monitored;
- H2 flow;
- pressure;
- Hg source ID/mass/temperature;
- furnace-zone temperatures;
- growth-zone temperature;
- solution temperature;
- axial gradient;
- equilibration start/end;
- evidence/criterion used to declare equilibrium.

For the Bowers–Schmit xS≈0.29 candidate branch:

- `TL≈507 °C` is a published tie-line anchor;
- growth near 500 °C / derived ~7 °C supercooling is a qualification center point, not automatic release.

**Gate B4:** thermal/atmosphere state satisfies the selected P30 branch.

---

## STEP B5 — growth initiation / run

Record:

- substrate-contact timestamp;
- actual contact/growth temperature;
- full temperature trajectory;
- slider position/state;
- growth duration/contact interval;
- cooling trajectory during growth;
- abnormal events.

**Gate B5:** no process excursion outside the authorized qualification envelope.

---

## STEP B6 — growth termination / wipe-off

Record:

- separation/wipe timestamp;
- temperature;
- slider direction/speed where calibrated;
- wipe-off configuration/clearance;
- residual-melt observation;
- scratch/damage observation;
- post-separation cooldown trajectory.

**Gate B6:** wafer safely separated under the selected P30 branch; proceed to as-grown inspection.

---

# PHASE C — as-grown material state

## STEP C1 — as-grown visual/morphology inspection

Record:

- whole-surface image;
- residual melt droplets;
- pinholes/voids;
- terraces/scratches;
- cracks/delamination;
- usable-area map.

**Gate C1:** morphology inside current P03/P30 qualification criteria.

---

## STEP C2 — as-grown FTIR / composition / thickness map

**Procedures:** P06/P06A.

Record:

- map coordinates and physical registration;
- raw spectra;
- edge metric with explicit definition;
- full-spectrum model/version;
- inferred optical composition metric;
- FTIR optical thickness;
- independent physical thickness reference where required;
- within-wafer statistics.

**Gate C2:** composition/thickness suitable to enter anneal development.

Do not replace the optical map with a single center-point cutoff or equate detector cutoff with optical composition.

---

## STEP C3 — as-grown Hall / transport state

**Procedure:** P05.

Use dedicated material coupon or approved geometry.

Record:

- sample thickness;
- contact configuration;
- temperature;
- current;
- B grid;
- raw reversal data;
- VdP consistency;
- Hall sign;
- `n_H/p_H`;
- `µ_H`;
- magnetoresistance/linearity evidence;
- multicarrier escalation if required.

**Gate C3:** baseline electrical state established; not necessarily final n-type state.

---

# PHASE D — Hg-overpressure anneal

## STEP D1 — anneal setup

**Procedures:** P04/P31.

Record:

- sample ID;
- Hg source/material;
- ampoule/reactor geometry;
- sample/source positions;
- pressure/chemical-potential control method;
- sample and reservoir thermometry;
- initial surface state.

**Gate D1:** selected P31 apparatus/reservoir branch is completely instantiated.

---

## STEP D2 — anneal run

Record complete:

- ramp rate/history;
- sample temperature `T_s(t)`;
- Hg-source/reservoir temperature `T_Hg(t)`;
- Hg pressure/chemical-potential proxy;
- soak time;
- cooldown path;
- vacuum/atmosphere.

Historical screening anchors are not the endpoint by themselves.

**Gate D2:** selected P31/P23 qualification trajectory completed without uncontrolled excursion.

---

## STEP D3 — post-anneal FTIR gate

Repeat P06/P06A at the same coordinates where possible.

Compare:

- thickness;
- edge/composition metric;
- spectrum shape;
- model residual;
- Hall/electronic-state context before interpreting an edge shift as composition change.

**Gate D3:** no unintended optical/material shift beyond the current qualification criterion.

---

## STEP D4 — post-anneal Hall gate

Repeat P05.

Reference RP-01 material-state targets:

- n-type;
- historical supplier density `~9.8×10^14 cm^-3`;
- historical supplier mobility `~4.0×10^4 cm²/V·s`;
- historical supplier measurement temperature remains unknown.

Local acceptance must specify measurement temperature, transport model/state classification and current numerical criterion explicitly.

**Gate D4:** selected final transport state reached.

If not, disposition = additional anneal development, reject, or documented rework; never repeatedly anneal without genealogy.

---

# PHASE E — frontside device fabrication

## STEP E1 — Mask-1 lithography

**Procedures:** P14/P32.

Record:

- resist/product/lot;
- coating/spin data;
- thickness map;
- bake;
- mask ID/revision;
- exposure;
- developer;
- developed CD;
- alignment;
- branch revision.

**Gate E1:** selected P32 branch is fully executable and developed pattern is inside its current CD/profile window.

---

## STEP E2 — wet mesa isolation

**Procedures:** P01/P01A/P28.

Record:

- etchant preparation and concentration basis;
- HBr stock assay and EG:HBr basis where applicable;
- reagent lots;
- bath temperature/age;
- time;
- agitation;
- rinse/quench/dry;
- depth;
- undercut;
- top/base CD;
- roughness/sidewall morphology;
- electrical isolation.

**Gate E2:** complete electrical isolation with acceptable geometry/passivation-ready surface.

No production/qualification run may use an undefined `2% Br2` concentration convention or an undefined `3:1 EG:HBr` preparation basis.

---

## STEP E3 — anodic oxide passivation

**Procedures:** P02/P25.

Record:

- electrolyte composition/basis;
- cell geometry/exposed area;
- bath temperature;
- current density;
- voltage-versus-time trace;
- charge/area where applicable;
- endpoint;
- time;
- rinse/dry;
- measured oxide thickness;
- witness/interface metrics.

Historical RP-01 target film thickness = `80 nm`.

**Gate E3:** selected P25 branch and oxide/interface outcomes inside the authorized qualification window.

---

## STEP E4 — Mask-2 lift-off/contact-window lithography

**Procedures:** P14/P14A/P27.

Direct historical anchors:

- resist ~4–5 µm;
- prebake 80 °C / 30 min;
- chlorobenzene soak 30 min.

Record the complete selected local branch including:

- resist/product/lot;
- coating/spin data;
- thickness before/after chlorobenzene;
- chlorobenzene bath state and sequence;
- exposure/tool/dose;
- developer;
- developed opening CD;
- lift-off-profile/overhang proxy;
- resist remaining height;
- alignment to Mask 1.

**Gate E4:** profile suitable for P08/P34 RIE + P09/P26 metal lift-off.

---

## STEP E5 — RIE contact-window / n+ formation

**Procedures:** P08/P24/P34.

Direct historical controller anchors:

- total flow 64 sccm;
- printed gas notation `CH4/5H2`;
- 100 mTorr;
- 50 W;
- 60 s.

Record:

- actual local CH4/H2 gas realization/composition and individual delivered flows where applicable;
- MFC IDs/calibration;
- base pressure;
- chamber clean/season history;
- electrode/reactor/sample-holder configuration;
- RF frequency/power;
- self-bias or qualified sheath/ion-energy proxy;
- sample temperature;
- process pressure;
- total RF time;
- oxide-clear time `t_clear`;
- semiconductor exposure `t_sem`;
- physical recession;
- n+ Hall/LBIC witness state;
- conversion depth/lateral extent where required.

**Gate E5:** physical + electrical conversion/contact-window state matches the selected P34 qualification branch.

The historical exact CH4/H2 delivery realization remains unresolved and must not be guessed or relabeled as direct history.

---

## STEP E6 — RIE-to-metal transfer clock

Record:

- RIE plasma off time;
- chamber vent time if any;
- ambient exposure;
- any qualified intervening operation;
- metal-system load time;
- pumpdown start;
- Cr deposition start.

Compute:

`Δt_RIE→Cr`.

**Gate E6:** surface transfer inside selected P26/P34 rule. No undocumented ion mill, wet etch, plasma clean or UV treatment may be inserted.

---

## STEP E7 — Cr/Au deposition

**Procedures:** P09/P09A/P26.

Historical thickness targets:

- Cr 30 nm;
- Au 270 nm.

Record:

- deposition method;
- tool ID;
- base pressure;
- deposition pressure;
- Cr rate/time/thickness;
- Au rate/time/thickness;
- QCM/witness calibration;
- substrate temperature;
- source/tool genealogy;
- abnormal events.

**Gate E7:** metal thickness/process inside selected P26 qualification window.

---

## STEP E8 — lift-off

**Procedures:** P14A/P26/P27.

Record:

- solvent/product/lot;
- temperature;
- time;
- agitation;
- rinse/dry;
- final optical inspection.

**Gate E8:** no bridges, fencing, flakes, delamination or contact damage.

---

## STEP E9 — final dimensional metrology

**Procedure:** P14.

For each device/contact pair record:

- final metal pad dimensions;
- actual gap;
- active width;
- mesa dimensions;
- alignment/clearances;
- device/contact-pair label.

These measured values, not CAD values, feed P10–P13.

---

## STEP E10 — TLM/contact QC

**Procedures:** P09/P24/P26.

For the nine-contact reference structure record:

- individual contact-pair resistance;
- gap;
- fit/regression;
- sheet/contact components;
- extracted `ρc`;
- temperature/background state;
- I–V linearity/symmetry;
- minority-carrier blocking/sweepout functional evidence from P08F where applicable.

Historical benchmark: `ρc ~9×10^-4 Ω·cm² at 80 K`.

**Gate E10:** contact technology accepted for detector characterization. Remember `rho_c != S_c`.

---

# PHASE F — bare-device detector baseline

## STEP F1 — P10 DC field / self-heating baseline

**Procedures:** P10/P10A.

Record:

- exact contact pair;
- actual gap;
- detector T;
- source voltage;
- measured detector contact-to-contact voltage;
- field;
- current;
- power;
- I–V symmetry;
- static/differential resistance;
- thermal drift;
- sweepout behavior;
- bias/load network revision.

**Gate F1:** safe operating field envelope established from actual detector voltage/geometry.

---

## STEP F2 — pre-package optical/noise/dynamic baseline

Where the fixture permits, obtain selected:

- P11 responsivity;
- P12 noise;
- P13 temporal/frequency response.

This creates the pre/post P35/P33 comparison. If a performance baseline cannot be measured before singulation/packaging, identify matched witnesses and explicitly record the reduced diagnostic power.

---

# PHASE G — singulation / package / interconnect

## STEP G1 — die separation and package-ready die preparation

**Procedure:** P35.

Record at minimum:

- selected singulation branch/revision;
- cut street/orientation and P29 crystallographic state;
- tool/blade/wire/laser state as applicable;
- support/protection materials;
- coolant/slurry/atmosphere;
- motion/pass/tool-age variables;
- die release/clean/handling;
- final die dimensions/kerf/position error;
- front/back chipping/crack state;
- subsurface-damage evidence from the qualified route;
- `d_visible`, `d_functional`, and current `d_release` status;
- residue/passivation/metal inspection;
- pre/post electrical/noise/responsivity evidence where available.

**Gate G1:** `SINGULATION-ROOM-TEMP-QUALIFIED` or an explicitly authorized qualification disposition under P35. Mechanical intactness alone is insufficient.

---

## STEP G2 — die attach

**Procedures:** P15/P33.

Record:

- carrier/cold finger;
- attach material/lot;
- dispense/bondline thickness/coverage/voiding;
- cure trajectory/atmosphere;
- placement/tilt;
- thermal history.

**Gate G2:** attachment mechanically acceptable, inside detector thermal budget, and eligible for cold qualification.

---

## STEP G3 — wire bond/interconnect

**Procedures:** P15/P33.

Record full bonder construction/settings and bond map, including wire/ribbon, tool, force, ultrasonic state, time, stage temperature and coupon qualification evidence.

**Gate G3:** visual/electrical qualification passed; corresponding coupon pull-test/process evidence exists where required.

---

## STEP G4 — aperture/window/shield / vacuum assembly

**Procedures:** P11/P15/P33.

Record actual geometry/transmission and pump/purge/bake history.

Do not use a nominal FOV label in place of measured aperture, separation, window/filter and view-factor state.

**Gate G4:** optical path and thermal/vacuum state fully defined.

---

## STEP G5 — cryogenic package + singulation closure

**Procedures:** P33/P35 with P10–P13 feedback.

Cool under measured thermal trajectory.

Repeat:

- P10 electrical baseline;
- selected P12 noise;
- selected P11 responsivity;
- P13 dynamic/thermal check where parasitics or package poles matter;
- die-edge/crack inspection after selected thermal cycles.

Determine package thermal response where required and feed it into P13 de-embedding.

**Gate G5:** no unacceptable packaging-induced degradation and no singulation-edge crack propagation/degradation. Close P35 final disposition as `RP01-SINGULATION-QUALIFIED` only when its cryogenic feedback requirement is satisfied.

---

# PHASE H — final detector characterization

## STEP H1 — absolute spectral responsivity

**Procedures:** P11/P11A.

Record complete traceable optical chain, wavelength calibration, detector geometry, package/window/FOV/background and same operating field/T/frequency state used for comparison.

---

## STEP H2 — noise / NEP / D*

**Procedures:** P12/P12B/P12C.

Record:

- PSD/ASD normalization;
- electronics floor;
- preamplifier/analyzer transfer;
- frequency;
- window/ENBW;
- detector T/E/background;
- active area from measured geometry;
- responsivity from the same or explicitly corrected state.

Use:

`D*(λ,f) = Rλ(f) sqrt(A) / e_n(f)`.

Do not substitute the historical 24.5-nV/√Hz g-r plateau into a 1-kHz D* calculation unless it is actually the detector-terminal noise at the signal frequency under the defined convention.

---

## STEP H3 — temporal response / bandwidth

**Procedures:** P13/P13A.

Record de-embedded amplitude/phase and time-domain response where available.

Explicitly include source, optics, bias/readout, cable/instrument and P33 package thermal response.

Determine whether the canonical 1-kHz responsivity/noise measurement lies on the actual detector low-frequency plateau. Do not infer historical RP-01 lifetime from the fact that 1 kHz was used.

---

## STEP H4 — final report / maturity decision

Compile:

- full traveler;
- P16A readiness authorization;
- raw data locations;
- all deviations;
- source/material genealogy;
- local-transfer versus historical branch labels;
- calibration records;
- measurement uncertainty summaries;
- P35 singulation/edge/subsurface-damage disposition;
- P33 package/thermal-cycle disposition;
- final performance table;
- failure/nonconformance history.

Run-level state options:

- `QUALIFICATION RUN — COMPLETE`
- `QUALIFICATION RUN — FAILED`
- one or more module states `LOCAL-QUALIFIED`

Project-level claims require separate evidence:

- `HISTORICAL-RP01-REPRODUCED` — permitted only under P16A historical-identity criteria;
- `PILOT-RELEASE` — only under P17;
- `REPRODUCIBLE-RELEASE` — **not permitted until every material/process-critical execution branch is frozen and the selected end-to-end route satisfies P17 measurement-system, stability/capability, numerical acceptance, yield and change-control requirements.**

A locally substituted but rigorously qualified process may eventually achieve `REPRODUCIBLE-RELEASE` without qualifying as literal `HISTORICAL-RP01-REPRODUCED`.

---

# 5. Witness/coupon plan

A complete qualification run should reserve/process matched material for:

- Hall/VdP before anneal;
- Hall/VdP after anneal;
- FTIR/thickness map and independent thickness reference;
- passivation oxide thickness/interface witness;
- Mask-1/wet-mesa depth/CD/isolation witnesses;
- RIE oxide-clear/recession witness;
- RIE n+ Hall/LBIC witness;
- metal thickness witness;
- TLM structure;
- lift-off/profile witness;
- P35 singulation street/tool/subsurface-damage witnesses;
- die-attach shear samples/coupons;
- wire-bond pull coupons;
- package thermal/noise qualification devices.

Do not consume the only detector die to learn a destructive-process parameter that could have been measured on a witness.

---

# 6. Elapsed-time variables to track

Surface and defect-sensitive processes require clocks. At minimum record:

- substrate final clean → LPE load;
- growth termination → first as-grown metrology;
- anneal end → electrical/optical metrology;
- mesa etch/rinse → passivation;
- anodization → Mask-2 coating;
- Mask-2 development → RIE;
- RIE → Cr deposition;
- Au deposition → lift-off;
- lift-off → first electrical test;
- last bare-device baseline → singulation;
- singulation completion → cleaning;
- singulation clean → die attach;
- die attach cure → wire bond;
- package pumpdown/bake → first cold test.

A future statistically qualified process may set maximum/minimum intervals for these clocks.

---

# 7. Deviation handling

Every deviation must record:

- affected sample IDs;
- intended setpoint/branch;
- actual value/event;
- timestamp;
- suspected physical consequence;
- immediate disposition;
- required extra metrology;
- authorization for continue/rework/scrap.

Examples that require HOLD include:

- undefined reagent concentration/preparation basis;
- unknown/unauthorized gas realization;
- temperature excursion;
- uncalibrated balance/MFC/thermocouple;
- loss of contact-pair identity;
- missing active-area measurement before D* reporting;
- uncontrolled RIE-to-metal delay;
- unqualified singulation protection/clean chemistry;
- visible new crack/chip beyond P35 allowance;
- package bake above qualified thermal budget.

---

# 8. Rework policy

Rework is allowed only when the specific rework physics and history are documented.

Potentially non-benign rework includes:

- repeat Hg anneal;
- repeat wet etch;
- stripping/regrowing passivation;
- repeat plasma exposure;
- metal strip/redeposit;
- post-singulation chemical material removal;
- repeated package bake;
- repeated wire bonding on the same pad.

Each may alter material/contact/interface/edge state. Never relabel a reworked sample as if it followed the nominal sequence.

---

# 9. Minimum final data package

A completed qualification run must contain:

1. P16 traveler with signatures/statuses;
2. P16A readiness register and branch selections;
3. raw source-material records;
4. exact charge calculations/actual masses;
5. full furnace/growth temperature traces;
6. gas/pressure/Hg-source records;
7. as-grown P05/P06 data;
8. anneal traces + post-anneal P05/P06;
9. lithography records/mask revisions/CD maps;
10. wet-etch preparation basis and final geometry/isolation;
11. anodization trace/thickness/interface evidence;
12. RIE actual gas realization + calibrated process state + witness data;
13. metal deposition traces/witness thickness;
14. TLM/raw I–V/regression + blocking-contact functional evidence;
15. actual device geometry/contact-pair mapping;
16. P35 singulation traveler, edge/subsurface-damage evidence and clean/handling record;
17. P33 package traveler, package thermal response and thermal cycles;
18. absolute responsivity calibration files;
19. noise spectra/PSD processing and analyzer transfer;
20. P13 frequency/time response and de-embedding;
21. uncertainty and deviation reports;
22. final performance summary;
23. failure/nonconformance/CAPA history.

If any mandatory item is unavailable, the run may still be scientifically useful but is not a complete reproducibility record.

---

# 10. Current master blockers to first-build and release maturity

Use P16A for the authoritative row-by-row state. The compact grouping is:

### A. Current `EXECUTION-BLOCKER` / `LOCAL-IMPLEMENTATION-GATE` set

Highest-impact items include:

- selected CdZnTe final surface and clean-to-load branch;
- selected P30 LPE apparatus/absolute charge/atmosphere/contact/wipe/cooldown branch;
- selected P31 Hg-anneal apparatus/reservoir/trajectory branch;
- fully executable Mask-1 + wet-mesa chemistry/rinse/strip branch;
- selected anodic-oxide cell/bath branch;
- fully executable Mask-2/chlorobenzene/developer/lift-off branch;
- selected P34 RIE gas/reactor/sheath/thermal/oxide-clear branch;
- selected P26 Cr/Au deposition/RIE-to-metal branch;
- implemented P05/P06/P10–P13 measurement systems;
- selected P35 singulation/protection/clean/edge-inspection branch;
- selected P33 package/interconnect/optical/vacuum branch.

Until these are frozen, `TRACEABLE-FIRST-BUILD-READY = NO`.

### B. `HISTORICAL-IDENTITY-ONLY` gaps

These remain important to literal reconstruction but do not prevent a clearly labeled local-transfer qualification build once local branches are frozen:

- exact historical material-metrology method behind x≈0.30 and 9.5 µm;
- exact UWA/Honeywell/Fermionics apparatus identities where local transfer is used;
- exact Optronics model/calibration chain;
- exact Figure-5 HP35665A settings and historical preamplifier circuit;
- exact historical performance contact pair/gap;
- exact 4.4-µm cutoff convention;
- exact RP-01 singulation/die outline;
- exact RP-01 package/interconnect construction;
- direct historical RP-01 lifetime/f3dB.

### C. `RELEASE-BLOCKER` set

After first-build execution is possible, P17 still requires:

- measurement-system adequacy for release metrics;
- repeated stable runs/lots;
- detector-derived numerical limits;
- variance separation and yield;
- capability/risk analysis appropriate to the data;
- change control/requalification;
- repeated end-to-end performance closure.

Therefore P16 is the **master qualification traveler**, P16A is the **first-build readiness gate**, P17 is the **release layer**, and P19 is the **requirement traceability layer**.
