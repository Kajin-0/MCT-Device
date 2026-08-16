# First qualification build — minimum laboratory capability / implementation specification

**Status:** CONTROLLED PRE-IMPLEMENTATION SPECIFICATION / ROUND 41  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16, P16A, P16B, P19, P20, and the controlled P01–P35 process/metrology modules.

## 1. Purpose

Define the minimum **physical capability envelope** a future laboratory must instantiate before the P16B candidate branch can be converted into a traceable first qualification build.

This document does **not** select vendors, models or commercial products. It defines what the laboratory must be able to control, measure, calibrate and record.

The governing chain is:

`P16B candidate branch -> required physical function -> capability envelope -> surrogate commissioning -> tool-specific calibration -> HgCdTe qualification -> P16A local closure`.

A capable tool is not automatically a qualified process. A qualified process is not automatically historical RP-01 identity. A successful isolated run is not statistical release.

---

# 2. Capability-state vocabulary

Use these labels exactly.

- `HARD-MINIMUM` — required by a direct controlled process condition or an unavoidable measurement equation.
- `FIRST-BUILD-ENGINEERING-ENVELOPE` — deliberately broader capability needed to characterize/qualify the selected branch; not a historical setpoint.
- `DESIGN-CHECK` — derived instrument-sizing or uncertainty relationship; not itself a released process tolerance.
- `SURROGATE-COMMISSIONABLE` — may be commissioned without HgCdTe using inert, electrical, optical, dimensional or thermal standards.
- `HGCDTE-REQUIRED` — the relevant response cannot be validated honestly without HgCdTe/CdZnTe or the completed detector stack.
- `LOCAL-BLANK` — must remain blank until the actual tool, geometry, consumable or calibration exists.
- `EH&S/FACILITY-GATE` — institutional safety/facility authorization is required independently of scientific capability.

Numerical values below shall retain their evidence class. Do not convert a `FIRST-BUILD-ENGINEERING-ENVELOPE` into an RP-01 historical claim.

---

# 3. Global requirements applying to every capability

Every critical tool or station shall have:

1. unique tool/revision ID;
2. manufacturer/model/serial or equivalent local identity;
3. dimensional/configuration drawing where geometry is physically relevant;
4. calibration method, date, result and uncertainty;
5. raw-data retention, not only controller screenshots;
6. timestamped process traces where time-dependent state matters;
7. consumable/gas/source lot genealogy;
8. maintenance/clean/season/change history;
9. defined acceptance/requalification trigger;
10. mapping to the P16A rows it supports.

For an instrument reading `X_display`, assume

`X_physical != X_display`

until the transfer is calibrated at the location/state used by the process.

---

# 4. C01 — source-material weighing / charge-accounting capability

## Physical function

Realize and audit the selected Te-rich liquid composition after `M_charge` has been chosen from the actual P30A boat.

## Controlled composition basis

The repository calculation freezes:

- `A_Hg = 200.59 g/mol`;
- `A_Cd = 112.414 g/mol`;
- `A_Te = 127.60 g/mol`.

For `xL=.082`, `yL=.810`:

- `w_Hg = 0.2497382358`;
- `w_Cd = 0.01250164993`;
- `w_Te = 0.7377601143`.

Therefore:

`m_Hg = 0.2497382358 M_charge`

`m_Cd = 0.01250164993 M_charge`

`m_Te = 0.7377601143 M_charge`.

`M_charge` remains a `LOCAL-BLANK` until P30A boat capacity/freeboard/hot-meniscus calibration exists.

## Minimum capability

The balance system must demonstrate repeatability, linearity and calibration **at the actual Cd mass**, because Cd is only ~1.25 wt% and dominates direct `xL` weighing sensitivity.

No universal balance readability is released before `M_charge` and an allowable `delta xL` are allocated.

Design relation:

`u(xL) = sqrt(sum_i (partial xL/partial m_i)^2 u(m_i)^2 + covariance terms)`.

For reference only, the existing calculation shows a +0.1 mg Cd error produces approximately `delta xL=1.20e-4` for an illustrative 5-g charge. The 5-g mass is not a selected process mass.

## Surrogate commissioning

- traceable mass standards over Hg/Cd/Te mass ranges;
- tare/container repeatability;
- operator repeatability;
- linearity around the smallest component mass.

## HgCdTe-required closure

Final acceptance of a weighing allocation requires P03/P06/P05 response sensitivity and released composition tolerance.

---

# 5. C02 — LPE furnace / graphite boat / gas / actuator capability

## Physical function

Execute the selected Honeywell-family covered horizontal-slider process while measuring the actual apparatus coordinates that literature cannot supply.

## HARD-MINIMUM process anchors

- candidate liquidus anchor `TL=507 °C`;
- charge must be demonstrated above its local liquidus before below-liquidus contact;
- candidate process atmosphere family `N2 purge -> flowing H2`;
- substrate family centered on Cd0.96Zn0.04Te (111)B;
- covered graphite horizontal-slider topology with growth well, substrate recess, separate Hg-source region and controlled wipe/separation.

## FIRST-BUILD-ENGINEERING-ENVELOPE

The growth thermal system shall be calibratable over at least the neighborhood required to resolve:

- local liquidus near 507 °C;
- above-liquidus equilibration;
- contact conditions spanning the literature-supported ~2–10 °C supercooling neighborhood.

A practical commissioning map should therefore include at least approximately `495–520 °C` around the process region, with additional headroom determined by the selected above-liquidus hold. This is an engineering coverage envelope, not a released trajectory.

If a separate sealed-source synthesis route based on the Radhakrishnan transfer family is selected, the **source-synthesis furnace is a separate conditional capability** and must support the chosen qualification temperature; `700 °C / 8 h` remains a transfer screening reference, not the Honeywell recipe.

## Hardware fields that must exist

- furnace/tube unique revision;
- dimensioned graphite boat/base/slider/cover;
- substrate recess and growth-well dimensions;
- plug/cap displacement;
- auxiliary Hg-source recess/moats;
- slider stroke and indexed positions;
- hot position repeatability;
- actuator travel time/velocity trace;
- calibrated source/substrate-region temperature sensors;
- N2 and H2 gas delivery with gas-specific calibration;
- pressure/backpressure state if not atmospheric open-flow;
- O2/H2O monitoring where used;
- exhaust/containment state.

## Calibration before HgCdTe

`SURROGATE-COMMISSIONABLE`:

- room-temperature dimensional metrology;
- well-volume/capacity calibration with a compatible inert surrogate;
- cold/hot slider travel and repeatability;
- empty/dummy-loaded axial/transverse thermal maps;
- controller-to-process-position offsets;
- ramp/lag characterization;
- N2/H2 MFC calibration with appropriate standards/verification;
- leak/flow-path verification.

Surrogates do not validate molten HgCdTe wetting, Hg transport, meniscus state or growth.

## HGCDTE-REQUIRED

- local liquidus behavior;
- hot usable melt volume/meniscus/freeboard;
- Hg loss/source transport;
- contact/wipe performance;
- growth rate/thickness/composition map;
- source depletion/reuse behavior;
- morphology and post-anneal electrical quality.

## LOCAL-BLANKS

`M_charge`, Hg-source inventory, exact flow rates, equilibration duration, `T_contact`, `t_contact`, cooling rate, separation/wipe trajectory and source-reuse limit.

---

# 6. C03 — Hg-overpressure anneal system

## Physical function

Control both defect-kinetic temperature and Hg chemical-potential boundary condition.

Required state vector:

`X_anneal={enclosure,source,geometry,T_s(t),T_Hg(t),Hg-boundary proxy,dwell,cooldown}`.

## HARD-MINIMUM / selected first screen

The system must support the P16B first-screen center:

`T_s approximately 250 °C / t approximately 1 h / Hg-saturated-isothermal-like`.

This is a qualification center, not a release recipe.

## FIRST-BUILD-ENGINEERING-ENVELOPE

- stable sample-zone operation spanning at least the low-temperature mapping region around `250–300 °C`;
- independent measurement of sample and Hg-source/reservoir temperature even if initially operated isothermally;
- complete cooldown trace;
- sealed-enclosure or equivalent Hg-boundary integrity verification.

If later two-temperature work is undertaken, sample and reservoir thermal zones must be independently controllable and cross-talk characterized.

## Surrogate commissioning

- empty and dummy-loaded axial temperature maps;
- sensor calibration over the selected range;
- zone cross-talk/lag;
- ampoule dimensional/free-volume record;
- seal/leak protocol on non-Hg test articles where scientifically valid;
- controlled cooldown repeatability.

## HGCDTE-REQUIRED

- N-LIKE/P-LIKE/transition response;
- `n_H`, `mu_H`, sheet resistance;
- composition/edge preservation by P06;
- morphology/defect response;
- device/lifetime compatibility.

## LOCAL-BLANKS

Hg inventory, free surface area, exact enclosure dimensions, `T_s/T_Hg` offsets, dwell map and cooldown relation.

---

# 7. C04 — FTIR composition / thickness mapping station

## Physical function

Measure the transmission edge, optical composition proxy/model state, active-layer thickness and spatial nonuniformity before/after anneal.

## HARD-MINIMUM / current P06 engineering method

- usable spectral coverage approximately `500–5000 cm^-1` (`20–2 µm`) for the x≈0.30 branch;
- qualification spectral resolution `<=4 cm^-1` unless sensitivity testing validates coarser settings;
- calibrated wavenumber scale;
- purge or vacuum optical path sufficient to control atmospheric artifacts;
- sample aperture/spot suitable for spatial mapping;
- raw or minimally processed spectral data retained.

## Mapping capability

- minimum 9-point coordinate map;
- preferred `5x5` or denser map when beam/sample geometry permits;
- physical x-y coordinates and orientation relative to LPE growth direction;
- repeated coordinate registration pre/post anneal.

## Independent thickness reference

The laboratory must also provide a traceable physical thickness method over the expected ~`5–15 µm` active-layer range, e.g. step profilometry or calibrated cross-section microscopy.

## Surrogate commissioning

- wavenumber standard/reference verification;
- stable transmission reference specimen;
- repeatability/remount study;
- spatial-stage coordinate calibration;
- thickness standards/step-height references where available;
- software/model version control.

## HGCDTE-REQUIRED

- optical-model adequacy;
- edge/composition sensitivity;
- fringe-based thickness performance;
- graded-layer model escalation;
- pre/post anneal equivalence limits.

## LOCAL-BLANKS

instrument model, source/beamsplitter/detector combination, spot size, coadds, fit model coefficients, production map density and numerical x/thickness limits.

---

# 8. C05 — Hall / van der Pauw magnetotransport station

## Physical function

Determine carrier sign, sheet resistance, Hall density/mobility where valid, and diagnose multicarrier behavior.

## HARD-MINIMUM / P05 initial grid

The station shall support measured field points including:

`B = 0, +/-0.01, +/-0.025, +/-0.05, +/-0.10, +/-0.20, +/-0.50 T`.

Therefore a local station unable to produce/measure at least approximately `+/-0.50 T` cannot execute the current P05 initial qualification grid.

## Preferred extended capability

Same-UWA converted-layer work represented in P16B used fields up to about `2 T`; capability approaching `+/-2 T` materially improves multicarrier diagnosis and lineage comparison but is not a HARD-MINIMUM for the initial P05 grid.

## Temperature capability

- controlled approximately `80 K` measurement;
- controlled `300 K` measurement;
- intermediate/extended temperature series available when carrier sign/curvature is ambiguous.

## Electrical capability

- reversible low-current source spanning below and above the initial `10–100 µA` screening region;
- differential/low-thermal-EMF voltage measurement capable of resolving sub-mV Hall signals with adequate SNR;
- automated or auditable current reversal and field reversal;
- measured sample-position magnetic field, not magnet-current setpoint only.

For the nominal RP-01 one-carrier screening state, P05 estimates ~`0.670 mV` Hall voltage at `10 µA, 0.10 T` and ~`6.70 mV` at `100 µA, 0.10 T`; these are instrument-sizing checks, not operating-current requirements.

## Surrogate commissioning

- resistor/van-der-Pauw electrical standards;
- field-probe calibration and spatial map;
- current-source verification;
- voltage offset/noise/reversal test;
- cryostat temperature calibration;
- known semiconductor Hall standard where available.

## HGCDTE-REQUIRED

- single-carrier validity region;
- surface/parallel-channel sensitivity;
- p/n transition behavior;
- contact compatibility and self-heating limits.

---

# 9. C06 — lithography / wet chemistry / anodization infrastructure

## Physical function

Produce Mask-1 wet-mesa geometry, preserve the mesa-to-passivation surface trajectory, form the native anodic oxide, and produce the direct RP-01 Mask-2 state that survives RIE and permits Cr/Au lift-off.

## Lithography HARD-MINIMUM states

Mask-2 must support:

- measured resist thickness `4–5 µm`;
- `80 °C / 30 min` prebake;
- chlorobenzene `30 min`;
- controlled exposure/develop/water rinse;
- RIE survival;
- lift-off of total metal thickness ~`0.30 µm`.

The coater must also support the selected Mask-1 candidate thickness/product family.

## Required lithography equipment capabilities

- reproducible spin speed/acceleration/time with logged recipe;
- calibrated resist-film thickness measurement;
- temperature-calibrated hotplate/oven around the 80 °C direct Mask-2 bake and candidate Mask-1 process region;
- UV exposure with measured irradiance/dose, not seconds alone;
- alignment/metrology compatible with 300-µm contacts and 50–400-µm gaps;
- developer/solvent baths with controlled time/temperature/history;
- profile/CD inspection adequate to quantify top/bottom opening, undercut/overhang and RIE-induced profile change.

## Wet-mesa requirements

The facility must support explicit mathematical preparation of the selected Br2/EG/HBr branch, including:

- Br2 concentration basis;
- EG:HBr ratio basis;
- HBr stock assay;
- bath temperature around the ~21 °C literature center;
- controlled immersion time;
- rinse/quench/dry timing;
- etch-depth/profile metrology.

No concentration is executable if the percentage basis is not defined.

## Anodization HARD-MINIMUM center capability

The electrical cell must support the TI photoconductor transfer center:

- HgCdTe as anode;
- selected carbon-cathode branch or another separately qualified branch;
- `J approximately 0.3 mA/cm^2`;
- continuous `V(t)` acquisition through a formation-voltage neighborhood near `15 V`;
- process duration around the ~2-min first-screen center;
- independent oxide-thickness measurement around `80 nm`.

Current-source sizing is area-dependent:

`I = J A_exposed`.

For illustration, `A_exposed=1 cm^2` gives `I approximately 0.3 mA`; the actual current is not fixed until `A_exposed` is measured.

A practical supply must have compliance above the expected ~15-V formation region; the exact compliance margin is a local engineering selection.

## Surrogate commissioning

- spin-speed/tachometer verification;
- hotplate/oven temperature map;
- exposure-dose calibration;
- dimensional standards/photoresist-on-inert-substrate process controls;
- wet-bath temperature/timing verification;
- anodization current/voltage logger calibration using dummy electrical loads;
- cell dimensional/area metrology.

## HGCDTE-REQUIRED

- etch rate/profile/roughness/isolation;
- P28->P25 surface-state sensitivity;
- oxide `V(t)` fingerprint;
- oxide thickness/interface function;
- downstream RIE/contact/noise compatibility.

---

# 10. C07 — CH4/H2 RIE capability

## Physical function

Reproduce the direct RP-01 controller state while measuring the local plasma/sheath/thermal quantities required for reactor equivalence.

## HARD-MINIMUM direct controller center

- total gas flow `64 sccm`;
- process pressure `100 mTorr`;
- forward RF power `50 W`;
- RF-on time `60 s`;
- gas family printed `CH4/5H2`.

Selected same-lineage candidate ratio:

`CH4:H2 = 1:5`.

Derived candidate nominal flows:

- `Q_CH4 = 10.6667 sccm`;
- `Q_H2 = 53.3333 sccm`.

These are candidate nominal values, not historical MFC readings.

## MFC capability rule

Each selected MFC range must place the nominal process flow inside a calibrated useful portion of the device range and provide gas-specific calibration/correction. Do not select full-scale range solely from controller availability.

A convenient range class might be of order `0–20 sccm` for CH4 and `0–100 sccm` for H2, but this is an equipment-sizing example only; actual range/accuracy is selected from the calibration uncertainty budget.

## Mandatory reactor observables

- base pressure measured and logged, but no conventional numerical base-pressure spec is invented;
- process-pressure trace;
- forward/reflected RF power;
- measured dc self-bias or another calibrated sheath/ion-energy proxy;
- sample/chuck temperature or calibrated proxy;
- actual CH4/H2 flows;
- chamber clean/season/run-order state;
- sample loading/position;
- oxide-clear time `t_clear`;
- semiconductor exposure `t_sem = t_RF - t_clear`.

## Surrogate commissioning

- MFC calibration;
- pressure-gauge verification/correction state;
- RF forward/reflected calibration checks;
- self-bias diagnostic validation;
- chuck/sample thermal calibration on dummy substrates;
- clean/season reproducibility;
- oxide-removal witness calibration on representative non-device stacks where valid.

## HGCDTE-REQUIRED

- physical recession `d_etch`;
- electrical conversion depth/lateral extent;
- morphology;
- sheet/Hall state;
- TLM contact result;
- minority blocking/sweepout response;
- detector-noise impact.

---

# 11. C08 — Cr/Au thermal-evaporation candidate capability

## Physical function

Deposit the direct RP-01 `30 nm Cr / 270 nm Au` stack onto the RIE-engineered contact region with traceable thickness, vacuum, geometry and thermal history.

## HARD-MINIMUM layer capability

- Cr target `30 nm`;
- Au target `270 nm`;
- same selected Mask-2 profile must support the total ~`300 nm` stack and lift-off.

Thermal evaporation is the strongest same-UWA method-family candidate; it is not historical RP-01 proof.

## Required apparatus observables

- tool/revision;
- pump/gauge chain;
- measured base and deposition pressure;
- Cr and Au source hardware/lot;
- source-to-sample/QCM geometry;
- shutter timing;
- QCM controller/head/crystal settings;
- **separate Cr and Au tooling factors unless equivalence is demonstrated**;
- deposition-rate traces;
- independent witness thickness;
- holder/sample thermal proxy;
- RIE-to-Cr exposure clock;
- Cr-to-Au vacuum history.

## Thickness-metrology design check

For an allocated fractional thickness uncertainty `b_t`, required absolute uncertainty is:

- Cr: `u_t <= 30 nm * b_t`;
- Au: `u_t <= 270 nm * b_t`.

Example only: a 5% engineering budget corresponds to 1.5 nm Cr and 13.5 nm Au. The 5% budget is not a released process tolerance.

## Vacuum rule

Round 41 does **not** assign `1e-6 Torr`, `1e-7 Torr`, or another conventional number. The local pressure criterion is set only after the actual tool is characterized and P26 interface/TLM/stability data demonstrate an acceptable region.

## Surrogate commissioning

- QCM-to-witness calibration for each material;
- tooling-factor repeatability;
- source geometry/rotation mapping;
- dummy-wafer thermal-load characterization;
- shutter timing/rate stability;
- lift-off profile trials on inert substrates carrying the selected resist stack.

## HGCDTE-REQUIRED

- TLM `rho_c`;
- cryogenic ohmicity/stability;
- RIE-to-metal delay sensitivity;
- detector noise/responsivity/sweepout impact.

---

# 12. C09 — integrated 77–80 K detector characterization station

The detector station is one **matched-state system**, not four unrelated benches.

Shared state:

`S_det={device,contact pair,L,W,t,package,T,E,I,P,background,FOV,window/load network}`.

P10/P11/P12/P13 quantities may be combined only when this state matches or a correction model with uncertainty is supplied.

## C09A — cryogenic / DC bias capability

HARD-MINIMUM reference operation:

- stable detector operation near `80 K`;
- electric-field setpoint `10 V/cm` for key RP-01 comparison;
- safe field sweep through the intended region up to the historical ~`50 V/cm` comparison neighborhood where self-heating/sweepout checks permit;
- measured active-region voltage and current;
- reversible polarity;
- low-noise source/load network;
- detector-temperature or calibrated thermal proxy.

For the nominal one-carrier screening geometry P10 predicts ~`1.79 mA` at 10 V/cm; this is instrument sizing only. Actual current must be measured.

## C09B — absolute spectral responsivity / radiometry

HARD-MINIMUM reference points:

- detector near 80 K;
- `E=10 V/cm`;
- spectral comparison including `4 µm` and through/beyond the ~`4.4 µm` response edge;
- `1 kHz` optical chopping for the canonical spectral state.

FIRST-BUILD-ENGINEERING-ENVELOPE:

- monochromator/source/reference path covering at least the useful MWIR response plus an out-of-band region; approximately `2–6 µm` is a practical first-build envelope for the x≈0.30 device, while broader coverage is acceptable;
- wavelength calibration;
- order sorting/stray-light checks;
- dry-purge/vacuum path where atmospheric structure is material;
- calibrated reference detector traceable to SI/NMI or equivalent;
- measured aperture/view-factor/window transmission.

The nominal `60° FOV` is not itself a calibration.

## C09C — detector-terminal noise / PSD

HARD-MINIMUM spectral region:

- include `1 kHz` signal frequency;
- resolve the historical ~`3 kHz` 1/f knee region;
- extend through at least the `10^2–10^4 Hz` historical plotting band.

FIRST-BUILD-ENGINEERING-ENVELOPE:

- extend below 100 Hz where practical for 1/f exponent;
- extend above 10 kHz to verify plateau/readout rolloff;
- calibrated preamplifier complex gain and source-impedance dependence;
- analyzer PSD/ASD normalization, window, ENBW and averaging known;
- electronics-floor state and Johnson-noise validation.

Historical high-frequency g-r reference:

`e_GR approximately 24.5 nV/sqrtHz`.

Readout-floor design relation:

if the allowed electronics contribution is fraction `beta` of detector **PSD**, require approximately

`e_elec <= 24.5*sqrt(beta) nV/sqrtHz`

near the relevant plateau state.

Example: `beta=0.10` gives ~`7.75 nV/sqrtHz`. Beta remains a local uncertainty allocation, not a historical requirement.

## C09D — temporal / frequency response

FIRST-BUILD-ENGINEERING-ENVELOPE from P13:

- frequency-domain capability beginning in roughly the `10–100 Hz` region where practical;
- include 1 kHz, 10 kHz, 100 kHz and 1 MHz;
- continue to at least `5–10x` the observed detector `f_3dB` if external hardware permits;
- calibrated source, optics, bias/load, preamp, cable and acquisition complex transfer;
- package thermal response characterized separately.

Same-UWA transfer branch includes a `25 ns`, `1.047 µm` optical pulse. If this pulse method is deliberately implemented, source/reference/digitizer bandwidth must resolve the actual pulse. A first-order rise-time sizing estimate `BW approximately 0.35/t_r` gives ~14 MHz for 25 ns; this is a `DESIGN-CHECK`, not an RP-01 detector bandwidth requirement.

## Surrogate commissioning for C09

- cryogenic thermometer and temperature-control verification;
- resistor networks representing detector impedance;
- calibrated electrical signal/noise injection;
- blackbody/aperture/reference-detector radiometry checks;
- chopper frequency/duty verification;
- optical source monitor/reference transfer;
- electrical network gain/phase characterization;
- digitizer/analyzer scaling and ENBW checks;
- package dummy thermal transient tests.

## HGCDTE-REQUIRED

- self-heating/sweepout discrimination;
- absolute responsivity;
- detector excess noise;
- BLIP response to background;
- intrinsic/interface/contact/package dynamic separation;
- final `NEP`, `D*`, `tau_eff`, `f_3dB` under matched state.

---

# 13. C10 — singulation / die-edge implementation

## Physical function

Separate the completed HgCdTe/CdZnTe detector without hidden functional or cryogenic edge damage.

## Selected first-screen family

Low-force wire-saw/abrasive separation is the first P16B screening family.

Primary transfer evidence includes a finished ~`1x1 cm` CdZnTe detector sample, low-melting wax support, photoresist protection, `16 µm` BN slurry and a very slow ~1-h complete cut in that branch.

These are transfer facts, not released RP-01 settings.

## Required capability

- cut ~1-cm-class CdZnTe/HgCdTe coupons/die with defined street geometry;
- record tool/wire/blade/abrasive identity;
- record speed/feed/downfeed/pass strategy and tool age;
- quantify wander/runout/kerf where applicable;
- controlled support/protection and removal sequence;
- optical edge inspection;
- subsurface-damage proxy or destructive qualification method on witnesses;
- pre/post electrical/noise/responsivity correlation versus edge distance.

## Surrogate commissioning

- glass/ceramic/inert brittle coupons for motion/kerf repeatability;
- CdZnTe sacrificial coupons before completed HgCdTe devices;
- mounting/protection residue tests;
- dimensional/edge-inspection calibration.

## HGCDTE-REQUIRED

- functional damage distance;
- passivation/contact survival;
- noise/responsivity change;
- cryogenic edge-crack propagation.

The `5% Br/methanol / 5 min` bulk-CdZnTe damage-removal process from Yoo is **not** an allowed default completed-device clean.

---

# 14. C11 — cryogenic package / Dewar / interconnect capability

## Physical function

Mount, interconnect and optically define the detector while controlling thermal, mechanical, electrical and radiometric state.

## HARD-MINIMUM functional capability

- repeatable detector operation near `77–80 K`;
- measured detector/cold-finger thermal state;
- compatible carrier/die-attach/interconnect geometry;
- optical aperture/window/shield with measurable dimensions/transmission;
- vacuum/purge state measured;
- repeatable warm/cold cycling;
- electrical access compatible with P10–P13 bandwidth/noise requirements.

## Selected first-screen attach family

Compliant silicone-family attachment is the first P16B screen because primary Honeywell evidence showed improved cryogenic survival relative to glass adhesive in the represented experiment.

Historical Dow Corning 3110/3112/3116 names are lineage evidence only; a current formulation must be selected and qualified independently.

## Required package observables

- carrier/cold-finger material and geometry;
- die-attach product/lot/mix/cure;
- bondline thickness/coverage/voids;
- die tilt;
- interconnect material/tool/settings;
- continuity/contact resistance;
- aperture/window/shield geometry;
- `T_window(lambda)` / filter transmission;
- pressure/pump/bake/cooldown state;
- package thermal transient/kernel;
- cycle genealogy.

## Surrogate commissioning

- dummy die placement/bondline studies;
- package leak/vacuum tests;
- cryogenic cycling of mechanically representative dummy assemblies;
- electrical feedthrough/noise/bandwidth tests;
- calibrated thermal pulse/recovery on dummy heaters/resistors;
- optical aperture/alignment metrology.

## HGCDTE-REQUIRED

- cooldown cracking/delamination;
- contact/interconnect excess noise;
- package-generated thermal poles;
- detector temperature under bias;
- final optical view factor;
- P10–P13 stability through thermal cycles.

---

# 15. C12 — dimensional / surface / auxiliary inspection capability

The branch cannot be qualified from process controllers alone.

Minimum supporting metrology must cover, directly or through qualified access to an external facility:

- calibrated optical microscopy for device/contact/street dimensions;
- film/resist/step thickness where required;
- surface/roughness/profile inspection sufficient for P28/P35 decisions;
- oxide/metal thickness witness metrology;
- edge/chip/crack documentation;
- sample coordinate registration;
- balance/mass standards;
- gas-flow/pressure standards or calibration services;
- thermometer/field/wavelength/electrical traceability.

No requirement exists that every metrology function be owned in-house. The requirement is that the data be traceable, available at the required process point, and linked to sample genealogy.

---

# 16. C13 — data / genealogy / configuration-control capability

Before any HgCdTe qualification run, the laboratory shall instantiate the P16 identifier chain:

`SOURCE LOT -> LPE CHARGE -> GROWTH RUN -> WAFER -> COUPON/DIE -> DEVICE -> CONTACT PAIR -> DATASET`.

Required digital record functions:

- raw file retention;
- immutable or versioned calibration records;
- process-recipe revision;
- instrument/tool revision;
- operator/timestamp;
- sensitive handoff clocks;
- nonconformance/deviation record;
- parent-child sample genealogy;
- code/model version for reductions;
- ability to regenerate reported metrics from raw data.

This capability is scientific infrastructure, not administrative overhead.

---

# 17. EH&S / facility boundary

This specification does not replace institution-specific authorization for:

- elemental Hg and Hg-containing wastes;
- Cd/CdZnTe/HgCdTe toxic-metal contamination control;
- Br2/HBr and other corrosive wet chemistry;
- H2 and CH4 flammable gas service;
- high-temperature sealed ampoules;
- vacuum systems;
- RF plasma;
- solvents including chlorobenzene;
- cryogens;
- high voltage/current where present.

`SCIENTIFICALLY-CAPABLE != FACILITY-AUTHORIZED`.

Both are required before physical execution.

---

# 18. What can be commissioned before HgCdTe exists

A future laboratory can close substantial infrastructure risk using non-HgCdTe work:

1. balances and mass accounting;
2. boat dimensions/capacity and hot motion;
3. furnace thermal maps;
4. gas/MFC/pressure calibration;
5. anneal thermal-zone mapping and leak procedures;
6. FTIR wavelength/repeatability/stage calibration;
7. Hall field/current/voltage/temperature chain;
8. lithography spin/bake/dose/CD metrology;
9. anodization electronics/cell geometry;
10. RIE gas/pressure/RF/self-bias/thermal repeatability;
11. QCM/witness/thickness/source geometry;
12. cryogenic electrical/radiometric/noise/temporal transfer functions;
13. singulation mechanics and edge inspection;
14. package vacuum/thermal/mechanical/electrical infrastructure;
15. genealogy/data system.

This commissioning does **not** close HgCdTe-specific material/process responses.

---

# 19. Minimum laboratory capability completion rule

The laboratory may be labeled

`P16C-INFRASTRUCTURE-READY`

only when every mandatory first-build capability has:

- actual tool/station identity;
- required range demonstrated;
- calibration/uncertainty record;
- required surrogate commissioning completed;
- local blanks that depend only on HgCdTe qualification clearly identified;
- facility/EH&S gate resolved or explicitly blocking;
- P16A row mapping completed.

This label does **not** imply:

- `TRACEABLE-FIRST-BUILD-READY = YES`;
- `HISTORICAL-RP01-REPRODUCED = YES`;
- `REPRODUCIBLE-RELEASE = YES`.

P16A remains authoritative.

---

# 20. Round-41 numerical-convention erratum

The controlled charge-sensitivity calculation freezes `A_Hg=200.59 g/mol` and therefore gives:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

Some later Round-35/40 integration text printed approximately `0.249740 / 0.012502 / 0.737758`, which corresponds to a different Hg atomic-weight convention (~200.592 g/mol).

**Round-41 control decision:** the frozen calculation file is authoritative. Use the values above for future charge calculations unless a deliberate calculation-version change is approved and propagated consistently. This numerical correction is ~2 ppm in the dominant mass fractions and does not alter prior scientific conclusions.

---

# 21. Immediate implementation order for a future laboratory

To minimize consumption of HgCdTe material, instantiate in this order:

1. C13 genealogy/data + calibration registry;
2. C01 balances/mass traceability;
3. C02 LPE mechanical/thermal/gas infrastructure without HgCdTe;
4. C03 anneal thermal/enclosure infrastructure without Hg;
5. C04 FTIR + C05 Hall metrology;
6. C06 lithography/wet/anodization infrastructure;
7. C07 RIE reactor metrology;
8. C08 Cr/Au thickness/vacuum/thermal metrology;
9. C09 integrated cryogenic detector station;
10. C10 singulation;
11. C11 package/Dewar;
12. only then begin HgCdTe-specific qualification in upstream-to-downstream order.

This order is a material-risk minimization strategy, not a claim about historical RP-01 laboratory sequence.
