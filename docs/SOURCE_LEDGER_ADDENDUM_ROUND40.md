# Source ledger addendum — Round 40 first-qualification-build branch integration

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Scope

Round 40 did not reopen generic literature searches already saturated in Rounds 35–39. Its purpose was to synthesize the **already controlled primary literature** into one evidence-ranked candidate first-qualification-build branch across all 36 P16A rows.

The principal new controlled artifact is:

`travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`.

P16B is an integration register, not a new physical-process SOP.

---

## S40-01 — P16A first-build readiness architecture

Controlled source:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `procedures/P16A_FIRST_BUILD_RELEASE_READINESS_AUDIT.md`

**Class:** `CONTROLLED-READINESS-ARCHITECTURE`.

Round-40 use:

- retained the 36 mandatory/qualification/release rows as the authoritative structure;
- did not change row state simply because a literature candidate was selected;
- separated candidate-family selection from physical local closure.

Permanent result:

`candidate branch != LOCAL-BRANCH-FROZEN`.

---

## S40-02 — CdZnTe / final-surface integration

Controlled source:

- `procedures/P29_CZT_SUBSTRATE_FINAL_SURFACE_EMPIRICAL_PROCESS_WINDOW.md`.

Primary evidence already retained there includes:

- x≈0.30 LPE work using `Cd0.96Zn0.04Te`;
- detector-oriented Te-rich LPE using `4% Zn`, `(111)B`, `10×10×1 mm³` substrates;
- chemical/mechanical polishing followed by `2–3% Br2/methanol` for a few seconds before loading;
- separate polarity/miscut transfer studies.

**Round-40 decision:**

- `Cd0.96Zn0.04Te (111)B` becomes the preferred first-screen substrate family;
- physical size remains dependent on the actual P30A boat;
- the `2–3% Br2/methanol / few seconds` final-surface family is retained but not made executable because concentration basis/time/rinse remain insufficiently specified.

No substrate identity is promoted to `DIRECT-RP01`.

---

## S40-03 — Honeywell / P30A LPE integration

Controlled source:

- `procedures/P30_LPE_APPARATUS_CHARGE_CONTACT_WIPEOFF_EMPIRICAL_PROCESS_WINDOW.md`;
- `procedures/P30A_LPE_ABSOLUTE_CHARGE_APPARATUS_CALIBRATION_ADDENDUM.md`.

Primary Honeywell evidence retained:

- covered graphite horizontal-slider topology;
- substrate recess / movable slider;
- tapered through-well(s), plug/cap;
- separate Hg-source recess and Hg-distribution grooves/moats;
- quartz-tube furnace;
- N2 purge followed by flowing H2;
- composition-matched tie line `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`.

P30A derived current mass fractions for that composition:

- `w_Hg=.249740`;
- `w_Cd=.012502`;
- `w_Te=.737758`.

Primary transfer evidence retained:

- Radhakrishnan et al. 2003: 6N elements, ~4.8-g growth charge and 3-g HgTe reservoir in a different Te-rich apparatus;
- Harman transfer ranges for supercooling/contact time.

**Round-40 decision:**

- Honeywell topology/tie line becomes the selected candidate LPE architecture;
- Radhakrishnan masses remain scale evidence only;
- total `M_charge` remains irreducibly dependent on actual local well geometry;
- no area scaling is permitted.

---

## S40-04 — Hg anneal integration

Controlled source:

- `procedures/P31_HG_ANNEAL_APPARATUS_RESERVOIR_TRAJECTORY_EMPIRICAL_PROCESS_WINDOW.md`;
- P04/P04A/P04B/P23.

Primary transfer center retained:

- Harman: approximately `250 °C / 1 h / Hg-saturated`;
- Nagahama near-composition evidence: `250–300 °C` supports useful n-type material without the composition change observed near 400 °C in that branch.

**Round-40 selected first screen:**

`250 °C / 1 h / Hg-saturated/isothermal-like`.

Restriction:

- final time/trajectory is not released until local P05/P06 data confirm the desired carrier/optical state;
- ampoule geometry, source inventory and `T_s(t)/T_Hg(t)` remain local.

---

## S40-05 — Mask-1 / wet mesa / anodization integration

Controlled sources:

- `procedures/P32_MASK1_WET_MESA_LITHOGRAPHY_EMPIRICAL_PROCESS_WINDOW.md`;
- `procedures/P28_WET_MESA_EMPIRICAL_PROCESS_WINDOW.md`;
- `procedures/P28A_WET_MESA_CHEMISTRY_DEFINITION_LINEAGE_ADDENDUM.md`;
- `procedures/P25_ANODIC_OXIDE_EMPIRICAL_PROCESS_WINDOW.md`;
- `procedures/P25A_ANODIC_OXIDE_CELL_ELECTROLYTE_INSTANTIATION_ADDENDUM.md`.

Primary branches retained:

### Mask-1
- historical product-identified HgCdTe Br2/HBr transfer: AZ4620, 3-µm film in that embodiment;
- current-product equivalence remains unproven.

### Wet mesa
Srivastav x=.28:
- `2% Br2`;
- `3:1 EG:HBr`;
- ~21 °C reference;
- mean vertical rate ~2.78 µm/min;
- anisotropy ~0.63;
- best RMS roughness ~2 nm.

Critical unresolved fields:
- Br2 basis;
- EG:HBr ratio basis;
- HBr stock assay.

Same-SSPL v/v usage remains `CANDIDATE-VV-SAME-LAB`, not historical closure.

### Anodic oxide
TI photoconductor branch:
- `0.1 mole KOH in 1 liter` of stated `90% EG / 10% DI-water` solvent;
- HgCdTe anode;
- carbon-rod cathode;
- `J≈0.3 mA/cm²`;
- ~15 V;
- ~2 min;
- ~800 Å/deep-blue oxide.

Derived pure-KOH mass:
- `5.61056 g/L` before assay correction.

**Round-40 decision:** these are selected candidate centers/families; none is promoted to a closed local branch while their actual consumables, basis conventions, cell geometry or handoff trajectory remain uninstantiated.

---

## S40-06 — Mask-2 / RIE / Cr-Au integration

Controlled sources:

- `procedures/P14A_CHLOROBENZENE_LIFTOFF_LINEAGE_ADDENDUM.md`;
- `procedures/P27_MASK2_PHOTORESIST_EXPOSURE_DEVELOPER_LIFTOFF_EMPIRICAL_WINDOW.md`;
- P08/P08A/P24/P34;
- P09/P09A/P26/P26A.

### Mask-2 direct RP-01 anchors

- resist `4–5 µm`;
- `80 °C / 30 min` prebake;
- chlorobenzene `30 min`;
- pattern/develop/water rinse;
- resist survives RIE and lifts the ~300-nm Cr/Au stack.

Product/developer/lift-off identity remains local/open.

### RIE

Direct RP-01:
- printed `CH4/5H2`;
- total 64 sccm;
- 100 mTorr;
- 50 W;
- 60 s.

Same-lineage explicit interpretation:
- `CH4:H2=1:5`.

Derived candidate nominal split:
- `Q_CH4=10.6667 sccm`;
- `Q_H2=53.3333 sccm`.

Historical individual MFC values remain unrecovered.

### Cr/Au

Direct:
- Cr 30 nm;
- Au 270 nm.

Same-UWA transfer:
- thermal evaporation is the strongest method-family candidate;
- angled geometry is not transferred as RP-01 identity.

**Round-40 decision:** select thermal evaporation as the candidate method family while keeping tool/vacuum/QCM/rates/thermal history and lift-off local.

---

## S40-07 — singulation / package integration

Controlled sources:

- `procedures/P35_HGCDTE_CZT_SINGULATION_DIE_EDGE_EMPIRICAL_PROCESS_WINDOW.md`;
- `procedures/P33_CRYOGENIC_DIE_ATTACH_INTERCONNECT_EMPIRICAL_PROCESS_WINDOW.md`.

### Singulation transfer

Yoo et al. 1998 finished-CdZnTe detector branch:
- ~1×1-cm sample;
- graphite support with low-melting wax;
- photoresist protection;
- 125-mm stainless-steel wire;
- 16-µm BN slurry;
- very slow cutting, ~1 h per complete cut.

Restriction:
- the same source's 5% Br/methanol / 5-min damage-removal etch is not transferred onto a completed RP-01 device.

### Package transfer

Honeywell cryogenic attachment evidence:
- glass adhesive cracked in a represented test;
- silicone-rubber attachment survived cooling to 5 K;
- historical named silicone materials include Dow Corning 3110/3112/3116.

NRL HgCdTe photoconductor thermal-stack evidence:
- attachment layers can create ms and hundreds-ms thermal recovery components.

**Round-40 decision:**
- low-force wire-saw family selected as the first singulation screen;
- compliant silicone-family attachment selected as the first package-attach screen;
- actual contemporary products/tool settings/bondline/interconnect/optics/vacuum remain local.

---

## S40-08 — detector-state / metrology integration

Controlled sources:

- P05/P06/P06A;
- P09/P10/P10A;
- P11/P11A;
- P12/P12A/P12B/P12C;
- P13/P13A;
- P33 package transfer.

Direct RP-01 reference state retained:

- ~80 K;
- Figures 5–7 at 10 V/cm;
- stated 60° FOV;
- spectral response chopped at 1 kHz;
- low-noise preamp + HP35665A for noise;
- 1/f knee ~3 kHz;
- high-frequency g-r level ~24.5 nV/sqrtHz;
- BLIP D* ~2×10^11 cm Hz^1/2/W at 4 µm;
- QE ~70%;
- no direct historical lifetime/f3dB curve.

Same-UWA temporal transfer retained:
- 1.047-µm laser;
- 25-ns pulse;
- 1-kHz repetition;
- ~77 K vacuum;
- HP54522A acquisition branch.

**Round-40 decision:** all P10–P13 claims must share or explicitly correct the actual detector/contact/package/field/T/background state. Historical instrument identity is not required if a modern local chain is calibrated and clearly labeled.

---

# Round-40 documentary-saturation result

No new primary source in Round 40 closed a previously open historical identity. Instead, the existing source base was integrated into one preferred candidate architecture.

The literature is now sufficient to choose the **process families and several first-screen centers**, but it cannot determine at least the following realized local quantities:

- actual boat geometry/charge;
- gas-delivery calibration;
- local thermal fields;
- resist contemporary product behavior;
- undefined wet-chemistry bases;
- RIE sheath/clear state;
- evaporator vacuum/QCM/thermal state;
- instrument transfer functions;
- singulation damage response;
- package bondline/optical/vacuum geometry.

These are appropriately classified as local physical identities/calibrations rather than literature gaps.

“Literature cannot determine a local calibration” is not the same as “the literature search failed.”