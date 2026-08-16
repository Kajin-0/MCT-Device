# P26A — Cr/Au deposition apparatus / vacuum / thermal-state instantiation addendum

**Status:** CONTROLLED EMPIRICAL CLOSURE METHOD / PRE-FIRST-BUILD  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Close the specific P16A R20 execution gap without converting a same-UWA metallization method into an undocumented RP-01 historical traveler.

P09/P09A/P26 already control the Cr/Au stack, transfer-delay DOE, deposition-pressure/rate studies, lift-off, TLM, cryogenic stability and detector-level correlation. P26A adds the missing **apparatus-instantiation layer** needed before a competent laboratory can execute a first qualification build without inventing deposition hardware choices at the tool.

Controlled chain:

`historical stack + same-lineage method evidence -> actual tool/revision -> source hardware -> vacuum metrology -> QCM/thickness calibration -> source/sample geometry -> thermal calibration -> RIE-to-Cr handoff -> Cr/Au sequence -> P26 run qualification -> LOCAL-BRANCH-FROZEN`.

P26A does not replace P09/P09A/P26 and does not claim recovery of the historical UWA deposition tool.

---

## 2. Evidence classes

### `DIRECT-RP01`
Smith et al. 2001 canonical photoconductor paper.

### `DIRECT-RP01-PROPOSED-ARCHITECTURE`
A capability or architecture explicitly described by RP-01 but not demonstrated as the actual configuration used for every reported experimental device.

### `SAME-UWA-1998-ANGLED-THERMAL`
Musca et al. 1998 / Piotrowski et al. 1998 UWA HgCdTe photovoltaic fabrication lineage explicitly using angled thermal evaporation for contact-metal deposition.

### `SAME-UWA-CRAU-THERMAL`
Later UWA HgCdTe device work explicitly using thermally evaporated Cr/Au, useful for method-family continuity but not historical identity.

### `PRIMARY-HGCDTE-RATE-TRANSFER`
Primary HgCdTe contact experiments supplying real deposition-rate/interface/thermal sensitivities in other architectures.

### `LOCAL-DEFINED`
Actual local deposition apparatus and process branch fully specified but not yet empirically qualified.

### `LOCAL-QUAL`
Local branch that has passed applicable P26 thickness, lift-off, TLM, stability and detector-function gates.

### `OPEN-HISTORICAL`
Historical RP-01 parameter not recovered.

No evidence class may be promoted merely because a value is common semiconductor practice.

---

## 3. Historical RP-01 boundary

### 3.1 Directly closed

RP-01 directly gives:

- `Cr = 300 Å = 30 nm`;
- `Au = 2700 Å = 270 nm`;
- Mask-2 resist about `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene soak `30 min`;
- pattern/develop/water rinse before RIE;
- the same resist survives RIE and supports metal lift-off;
- nine `300 µm × 300 µm` contacts with 50–400-µm gaps;
- `rho_c ≈ 9×10^-4 Ω·cm²` at 80 K after the complete contact process.

### 3.2 Still open

The recovered RP-01 text does **not** identify:

- deposition method;
- tool manufacturer/model;
- Cr source type or boat/crucible;
- Au source type or boat/crucible;
- source-to-sample distance;
- incidence angle or wafer rotation;
- base pressure;
- pressure during either layer;
- pump/gauge architecture;
- Cr rate;
- Au rate;
- QCM/model/tooling factor;
- sample/holder temperature;
- whether Cr and Au were deposited without vacuum break;
- actual RIE-to-metal air exposure for the reported devices;
- lift-off solvent/time/temperature/agitation.

Therefore all are `OPEN-HISTORICAL` for RP-01.

---

## 4. What the UWA lineage actually establishes

### 4.1 Same-UWA 1998 method evidence

Two closely related 1998 UWA HgCdTe photovoltaic papers explicitly state that detector structures were formed using conventional dry etching, angled ion milling and **angled thermal evaporation for contact-metal deposition**.

This is strong evidence that thermal evaporation was an established UWA HgCdTe contact process in the immediate pre-RP-01 era.

It does **not** establish:

- that RP-01 used thermal evaporation;
- that RP-01 used the same evaporator;
- that RP-01 used angled incidence;
- that its Cr and Au rates/pressure matched those photovoltaic structures.

Correct use:

`thermal evaporation = strongest SAME-UWA method-family candidate`.

Incorrect use:

`RP-01 Cr/Au was thermally evaporated at an angle`.

### 4.2 Later UWA method continuity

Later UWA HgCdTe device work reports thermally evaporated Cr/Au stacks in other detector structures. This reinforces method-family continuity but does not improve historical RP-01 apparatus identity.

### 4.3 Angled deposition is not a neutral detail

In the 1998 photovoltaic structures, angled deposition is part of a specific contact geometry. RP-01 instead relies on a chlorobenzene-shaped lift-off mask and self-aligned contact windows.

Therefore deposition incidence angle/rotation is a controlled geometry variable. Do not import an angled-photovoltaic contact geometry into RP-01 merely because both use HgCdTe.

---

## 5. RP-01 load-lock statement — capability, not demonstrated run history

RP-01 states that a vacuum-processing capability can arise by allowing the RIE process chamber to be connected via load lock to the metal-deposition system and identifies this as beneficial for yield/uniformity.

The recovered experimental section does not state that the reported devices were actually processed through such a connected load-lock line without an air break.

Evidence state:

`RIE->metal load-lock = DIRECT-RP01-PROPOSED-ARCHITECTURE`.

Do not convert it to:

`reported RP-01 devices had zero air exposure`.

P26/P26A must therefore record the actual local exposure clock.

---

## 6. Historical search boundary after Round 38

The following same-lineage sources were re-audited:

- Musca/Smith/Dell/Faraone 1999 contact/passivation proceedings paper;
- Smith/Winchester/Musca/Dell/Faraone 2000 in-situ vacuum-processing proceedings paper;
- related 1998 UWA HgCdTe device papers;
- RP-01 itself.

The first two are bibliographically confirmed and highly relevant, but their full experimental travelers were not recovered through the current accessible source path.

No primary UWA source recovered in Round 38 gives an exact RP-01:

- Cr rate;
- Au rate;
- base pressure;
- evaporator model;
- source hardware;
- source/sample distance;
- substrate temperature;
- QCM configuration;
- actual load-lock use on the measured RP-01 devices;
- lift-off solvent/time.

Disposition: `IDENTIFIED-NOT-RECOVERED`, not evidence that such details never existed.

Future generic searches should not reopen this question unless a new source family appears: thesis appendix, laboratory traveler, equipment log, archived proceedings full text, notebook, or author-held process record.

---

# 7. Local branch selection

Before any RP-01-compatible metallization run, choose exactly one deposition-method branch.

## `P26A-TE-*` — thermal evaporation

Strongest current same-UWA method-family candidate.

Requires explicit:

- resistance/source-heating architecture;
- Cr source/boat/crucible;
- Au source/boat/crucible;
- shutter geometry;
- source-to-sample geometry;
- QCM geometry;
- sample thermal calibration.

## `P26A-EBEAM-*` — electron-beam evaporation

Separate branch because electron/secondary-radiation loading, source geometry, outgassing and film nucleation can differ.

## `P26A-SPUTTER-*` — sputtering

Separate branch because energetic bombardment, plasma exposure, pressure and interface damage differ substantially from evaporation.

No branch is called “equivalent” until P26 outputs demonstrate equivalence.

For first transfer, thermal evaporation is the preferred literature-lineage candidate **when an appropriate qualified local tool exists**. This is a selection rule, not a historical statement.

---

# 8. Apparatus state vector

Freeze one apparatus revision as:

`X_dep = {tool/revision, chamber, pump, gauges, source stations, source hardware, source materials, source-sample geometry, holder, thermal contact, rotation/tilt, QCM head, tooling factors, shutters, pressure state, Cr rate trace, Au rate trace, T_sample proxy, RIE-transfer architecture, Cr-Au vacuum history}`.

A change in any state variable that can affect film/interface formation is change-controlled under P17.

---

# 9. Tool / vacuum instantiation requirements

Record before first use:

- manufacturer/model/serial or unique local tool ID;
- chamber revision/liner state;
- pump type/model;
- roughing/high-vacuum sequence;
- base-pressure gauge type/model/range/location;
- deposition-pressure gauge type/location;
- calibration date/state;
- chamber clean/season procedure;
- routinely attainable clean base-pressure distribution;
- accepted base-pressure criterion for the qualification branch;
- pressure acquisition/logging cadence;
- RGA availability and reference state where available.

### No invented pressure specification

P26A does not assign `1e-6 Torr`, `1e-7 Torr`, or another conventional value as an RP-01 requirement.

A local pressure criterion becomes frozen only after:

1. the actual tool is characterized;
2. the value is routinely attainable;
3. P26 TLM/stability data show the selected region is acceptable.

Before those data exist, record the actual pressure rather than replacing it with a presumed standard.

---

# 10. Source hardware and material genealogy

For Cr and Au separately record:

- source material supplier/product/lot;
- certified purity;
- source form;
- source mass/charge where useful;
- boat/crucible/hearth material;
- source-station ID;
- source conditioning/preheat history;
- prior use/recharge history;
- source-to-sample distance;
- source angular relation to sample;
- shutter position and effective opening;
- evidence of spitting/particulate generation.

Changing source hardware or source geometry is not merely maintenance if it changes rate stability, radiative load or deposition directionality.

---

# 11. QCM / thickness-metrology instantiation

The direct historical thickness targets remain:

- Cr `30 nm`;
- Au `270 nm`.

For each material independently record:

- QCM controller/head/crystal ID;
- crystal position relative to source and sample;
- density/acoustic-impedance/material settings;
- tooling factor;
- calibration date;
- rate measurement bandwidth/update rate;
- indicated thickness;
- independent witness thickness method;
- QCM-to-witness ratio and uncertainty.

### Required calibration

Do not use one generic tooling factor for Cr and Au unless independent calibration demonstrates that it is valid for both.

At minimum, calibrate witness thickness at the intended sample/source geometry. If the wafer is tilted or rotated, the witness layout must capture the resulting flux geometry or the tooling factor is not transferable.

Qualification state:

`THICKNESS-METROLOGY-QUALIFIED` only after repeated QCM/witness agreement is demonstrated.

---

# 12. Deposition-rate state

Historical Cr and Au rates remain `OPEN-HISTORICAL`.

P26 already contains primary HgCdTe Au rate-transfer examples on the order of several Å/s. They prove practical scale, not RP-01 identity or a production window.

P26A rule:

- never copy an Au rate to Cr;
- never convert a stable local source rate into a historical number;
- freeze local rates only after P26 low/center/high screening or equivalent evidence.

For each layer retain:

`r(t), r_mean, r_min, r_max, t_shutter, thickness_QCM, thickness_witness`.

The interface-forming Cr layer receives independent qualification because it directly contacts the P08-engineered n+ HgCdTe.

---

# 13. Sample thermal-load calibration

A 300-nm total metal deposition can impose nontrivial radiative/conductive heating on both HgCdTe and the chlorobenzene-conditioned resist.

Before first detector use, qualify the selected apparatus with a dummy assembly reproducing as closely as practical:

- substrate dimensions/material thermal mass;
- carrier/holder contact;
- resist presence or a thermal surrogate;
- source-to-sample geometry;
- Cr and Au deposition duration/power history.

Record:

- holder initial temperature;
- holder temperature trace;
- sample-temperature measurement/proxy method;
- peak temperature during Cr;
- peak temperature during Au;
- cool-down after Au;
- measurement uncertainty/lag.

If direct sample thermometry is impossible, document the calibration method and do not label holder temperature as exact wafer temperature.

Qualification state:

`THERMAL-LOAD-CALIBRATED`.

No intentional substrate heating or post-metal anneal is part of baseline RP-01 transfer without a separate branch.

---

# 14. RIE-to-Cr handoff instantiation

Define the actual facility branch, not an idealized flow diagram.

Possible branches:

- `VACUUM-TRANSFER` — physically connected transfer without atmospheric exposure;
- `INERT-TRANSFER` — controlled inert handling/storage;
- `AIR-TRANSFER` — documented laboratory-air exposure;
- other explicitly defined branch.

Required timestamps:

- `t_RF_off`;
- `t_RIE_vent`;
- `t_sample_out`;
- `t_metal_load`;
- `t_pump_start`;
- `t_base_accept`;
- `t_Cr_start`.

Derived separately:

- `Delta t_RIE-Cr`;
- cumulative `Delta t_air`;
- cumulative controlled-inert exposure.

P26 determines the acceptable maximum delay from TLM/stability data.

### Pre-metal intervention rule

Baseline remains:

`P08 -> controlled transfer -> Cr`.

No undocumented wet clean, ion mill, plasma clean, UV/ozone or other intervention is permitted because it may modify the engineered P08 contact region.

---

# 15. Cr-to-Au sequence instantiation

Preferred local qualification baseline, where hardware permits:

`Cr 30 nm -> remain under vacuum -> Au 270 nm`.

This preference minimizes an uncontrolled Cr-interface variable but is **not** a recovered RP-01 historical fact.

Record:

- Cr end time;
- Au start time;
- pressure between layers;
- source-switch procedure;
- sample thermal recovery;
- any vacuum break/treatment.

A required vacuum break is a separate process branch.

---

# 16. Geometry / directionality gate

Before first detector run record:

- source-to-wafer distance;
- wafer normal relative to source line-of-sight;
- fixed tilt angle if any;
- rotation/planetary motion;
- witness positions;
- Mask-2 top/bottom CD and undercut/overhang;
- expected shadowing/sidewall exposure.

P26A does not copy the same-UWA 1998 **angled** evaporation geometry into RP-01.

The local incidence geometry is released only after P27/P26 lift-off/CD results show no unacceptable fencing, bridging or metal discontinuity.

---

# 17. Apparatus qualification progression

Use these states exactly:

1. `METHOD-FAMILY-SELECTED`
2. `TOOL-REVISION-DEFINED`
3. `VACUUM-CHAIN-DEFINED`
4. `SOURCE-HARDWARE-DEFINED`
5. `GEOMETRY-DEFINED`
6. `THICKNESS-METROLOGY-QUALIFIED`
7. `THERMAL-LOAD-CALIBRATED`
8. `RIE-CR-HANDOFF-DEFINED`
9. `CR-AU-SEQUENCE-DEFINED`
10. `P26-APPARATUS-READY`
11. `P26-LOCAL-QUALIFIED`

`P26-APPARATUS-READY` means an operator can execute a controlled qualification deposition without inventing apparatus choices. It does **not** mean contact performance has passed.

`P26-LOCAL-QUALIFIED` additionally requires applicable P26 TLM, physical, stability and detector-function gates.

---

# 18. P16A R20 closure rule

P16A R20 may move from `APPARATUS-NOT-SELECTED` to `LOCAL-BRANCH-FROZEN` only when the actual laboratory has completed the P26A register through at least `P26-APPARATUS-READY` and the selected first-build values are under change control.

Required frozen items include:

- deposition method/tool revision;
- source hardware/material genealogy;
- source/sample geometry;
- vacuum metrology and base-accept rule;
- separate Cr/Au QCM calibration;
- initial selected Cr/Au rate branches;
- thermal-load calibration/hold criterion;
- RIE-to-Cr handoff branch and clocks;
- Cr-to-Au vacuum-history rule;
- linked P26 lift-off recipe ID.

Creating P26A alone does **not** change R20 readiness state.

---

# 19. Change-control triggers

Reopen relevant P26/P17 qualification for changes to:

- deposition method;
- chamber/tool revision;
- source station/boat/crucible/hearth;
- source-to-sample geometry;
- wafer tilt/rotation;
- pump/gauge or pressure-reference configuration;
- base-pressure acceptance rule;
- QCM location/tooling factor/controller;
- Cr or Au source material class/purity;
- Cr or Au rate branch;
- holder/backside thermal contact;
- RIE-to-metal transfer mode;
- pre-metal intervention;
- Cr-to-Au vacuum break;
- Mask-2 profile affecting deposition/lift-off.

---

# 20. Sources / provenance record

Primary/direct anchors and same-lineage sources to retain:

1. E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306` — direct RP-01 stack, lift-off compatibility, TLM outcome and proposed load-lock capability.
2. C. Musca et al., *Journal of Electronic Materials* 27, 740–746 (1998), DOI `10.1007/s11664-998-0046-y` — same-UWA angled thermal contact-metal evaporation.
3. J. Piotrowski et al., *Semiconductor Science and Technology* 13, 1209–1214 (1998), DOI `10.1088/0268-1242/13/10/025` — closely related same-UWA angled thermal contact-metal evaporation.
4. E. P. G. Smith et al., “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors,” SIMC-XI (2000), pp. 318–321 — bibliographically identified high-priority bridge; detailed traveler not recovered in Round 38.
5. C. Musca et al., “Performance and stability of HgCdTe photoconductive devices: A study of contact and passivation technology,” 1998 conference proceedings, published 1999, pp. 283–286 — bibliographically identified same-team bridge; detailed traveler not recovered.
6. P26-controlled primary HgCdTe contact studies for transfer rate/interface/thermal sensitivity; retain their existing evidence classes.

---

# 21. Round-38 boundary statement

Round 38 materially improves **how R20 can be closed**, not the historical identity of the RP-01 evaporator.

Current defensible statement:

- thermal evaporation is the strongest recovered UWA HgCdTe method-family candidate;
- exact RP-01 deposition method remains open;
- exact RP-01 rates, vacuum, source geometry, thermal state and actual vacuum-transfer history remain open;
- a dimensioned/calibrated local P26A branch can support `TRACEABLE-FIRST-BUILD-READY` without supporting `HISTORICAL-RP01-REPRODUCED`.
