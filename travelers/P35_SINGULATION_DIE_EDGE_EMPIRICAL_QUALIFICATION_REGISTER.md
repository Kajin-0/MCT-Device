# P35 — Singulation / die-edge empirical qualification register

**Status:** CONTROLLED TRAVELER / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

Use with `procedures/P35_HGCDTE_CZT_SINGULATION_DIE_EDGE_EMPIRICAL_PROCESS_WINDOW.md`.

Purpose: capture the actual realized singulation state of a completed HgCdTe/CdZnTe device stack and determine whether the die remains electrically, mechanically and cryogenically equivalent to its pre-singulation state.

---

## A. Genealogy and incoming device state

- Qualification run ID: ____________________
- Date/operator: ____________________
- Wafer/coupon ID: ____________________
- Device/die provisional ID: ____________________
- Wafer x-y coordinate: ____________________
- P29 substrate genealogy/revision: ____________________
- CdZnTe thickness: ____________________
- plane/polarity: ____________________
- miscut magnitude/azimuth: ____________________
- P06/P06A HgCdTe thickness/state: ____________________
- HgCdTe active thickness: ____________________
- mesa/passivation revision: ____________________
- P24/P34 RIE/contact revision: ____________________
- P26 Cr/Au revision: ____________________
- frontside state/coatings: ____________________
- backside state: ____________________
- known pre-existing chips/cracks/scratches: ____________________

Incoming micrograph/data location: ____________________

### Pre-singulation functional baseline

| Quantity | condition | value/data ID | status |
|---|---|---|---|
| continuity | | | |
| resistance | T=___, E=___ | | |
| I–V | T=___ | | |
| noise ASD | T=___, E=___, f=___ | | |
| 1/f state | | | |
| responsivity | T=___, E=___, lambda=___ | | |
| other | | | |

If direct pre-cut baseline unavailable, matched-witness IDs and limitation: ____________________

---

## B. Planned die / street geometry

Final intended die dimensions:

- L: __________
- W: __________
- substrate thickness: __________

For each edge record the planned cut centerline and nearest protected feature.

| edge | cut orientation / crystal direction | nominal kerf | centerline tolerance | nearest feature | intended feature-to-kerf-edge distance |
|---|---|---:|---:|---|---:|
| E1 | | | | | |
| E2 | | | | | |
| E3 | | | | | |
| E4 | | | | | |

Nearest mesa edge: __________  
Nearest exposed HgCdTe sidewall: __________  
Nearest n+/contact region: __________  
Nearest Cr/Au pad: __________  
Nearest wire-bond area: __________  
Nearest optical active region: __________

Historical RP-01 edge exclusion known? `YES / NO`. Evidence: ____________________

---

## C. Candidate branch

Select one:

- [ ] A — abrasive blade saw
- [ ] B — wire saw
- [ ] C — scribe/cleave
- [ ] D — laser/excimer
- [ ] other approved branch: ____________________

Evidence class supporting branch:

- [ ] DIRECT-RP01-SINGULATION
- [ ] PRIMARY-HGCDTE-DICING-TRANSFER
- [ ] PRIMARY-CZT-SINGULATION-TRANSFER
- [ ] PRIMARY-II-VI-LASER-SURFACE-TRANSFER
- [ ] GENERIC-HARD-BRITTLE-TRANSFER
- [ ] LOCAL-QUAL continuation

Source/reference: ____________________

---

## D. Temporary protection and support

### Frontside/backside protection

- product/manufacturer: ____________________
- product/lot: ____________________
- chemistry/class: ____________________
- surface covered: ____________________
- applied thickness: ____________________
- application method: ____________________
- bake/cure T/t: ____________________
- compatibility witness ID: ____________________
- witness PASS? `YES / NO`

### Temporary mounting/support

- tape/wax/adhesive/fixture: ____________________
- product/lot: ____________________
- carrier/submount material: ____________________
- mounting temperature: ____________________
- mounting force/pressure: ____________________
- die support geometry: ____________________
- expected release method: ____________________

No undocumented protection/support material may contact the finished device.

---

# E. Abrasive saw / wire process record

Complete if Branch A or B.

- machine manufacturer/model: ____________________
- tool serial: ____________________
- blade/wire manufacturer: ____________________
- blade/wire product/lot: ____________________
- blade/wire material: ____________________
- abrasive species: ____________________
- nominal abrasive size/grit: ____________________
- abrasive bond: ____________________
- blade/wire diameter or thickness: ____________________
- blade exposure/flange geometry: ____________________
- tool age at start: ____________________
- accumulated cut length/time: ____________________
- last dress/condition: ____________________
- runout/wander check: ____________________

### Motion/cut state

- spindle speed or wire speed: ____________________
- feed rate: ____________________
- downfeed/cut depth: ____________________
- skim pass? ____________________
- through-cut pass? ____________________
- number of passes: ____________________
- cut direction / entry-exit face: ____________________
- cut sequence E1→E4: ____________________
- fixture orientation: ____________________

### Coolant/slurry

- product/chemistry: ____________________
- lot: ____________________
- abrasive concentration if applicable: ____________________
- pH/conductivity/resistivity if relevant: ____________________
- temperature: ____________________
- flow: ____________________
- filtration: ____________________
- fresh/recirculated: ____________________
- run history/age: ____________________

---

# F. Scribe/cleave process record

Complete if Branch C.

- scriber/tool: ____________________
- tip material/radius: ____________________
- scribe face: ____________________
- scribe direction vs crystal axes: ____________________
- scribe length/depth/force proxy: ____________________
- support geometry: ____________________
- cleave initiation method: ____________________
- cleave force/moment proxy: ____________________
- crack-propagation observation: ____________________
- branch/deflection event: ____________________

P29 plane/polarity/miscut record attached? `YES / NO`

---

# G. Laser/excimer process record

Complete if Branch D.

- laser type/model: ____________________
- wavelength: ____________________
- pulse duration: ____________________
- repetition rate: ____________________
- measured pulse energy: ____________________
- fluence at sample: ____________________
- beam/line dimensions: ____________________
- focus/defocus: ____________________
- incidence angle: ____________________
- scan velocity: ____________________
- pulse overlap: ____________________
- number of passes: ____________________
- atmosphere/pressure: ____________________
- debris extraction: ____________________
- protection coating: ____________________
- laser-energy calibration ID: ____________________

Near-edge chemistry/stoichiometry witness planned? `YES / NO`  
Method: ____________________

---

# H. Per-cut execution record

| edge | start time | stop time | realized tool state / deviation | abnormal sound/force/wander/debris | disposition |
|---|---|---|---|---|---|
| E1 | | | | | |
| E2 | | | | | |
| E3 | | | | | |
| E4 | | | | | |

Total wet/slurry exposure: ____________________  
Total cutting time: ____________________  
Any interruption/restart: ____________________

Deviation/NCR ID: ____________________

---

# I. Release from temporary support / post-cut cleaning

- tool stop time: ____________________
- first rinse/release time: ____________________
- protection removal method: ____________________
- temporary-mount removal method: ____________________
- solvent/reagent sequence with lot/purity: ____________________
- each exposure time/T: ____________________
- agitation: ____________________
- ultrasonic exposure: `NONE` unless specifically qualified; if used deviation/qualification ID: ____________________
- rinse: ____________________
- dry: ____________________
- handling/pickup method and contact point: ____________________
- clean completion: ____________________
- storage ambient to P33: ____________________
- clean-to-attach elapsed time: ____________________

### Chemical edge treatment

Any bromine/etch treatment? `NO / YES — separate approved branch`

If YES:

- separate approval/requalification ID: ____________________
- chemistry/concentration basis: ____________________
- time/T: ____________________
- calculated/measured material removal: ____________________
- effect on oxide/RIE contact/Cr-Au requalified? ____________________

No bulk-CZT `5% Br/methanol / 5 min` process may be copied onto a finished RP-01 die without this separate qualification.

---

# J. Dimensional / visible edge metrology

Instrument/calibration: ____________________

Final die:

- L: ____________________
- W: ____________________
- squareness: ____________________
- thickness: ____________________

For each edge:

| edge | kerf / cut-position error | front chip max | back chip max | longest crack | edge roughness/taper | residue | passivation/metal damage |
|---|---:|---:|---:|---:|---|---|---|
| E1 | | | | | | | |
| E2 | | | | | | | |
| E3 | | | | | | | |
| E4 | | | | | | | |

Corner breakout observations: ____________________

Actual minimum `d_visible` to protected active feature: ____________________

Micrograph file IDs: ____________________

---

# K. Subsurface-damage development record

Method:

- [ ] sacrificial cross-section optical
- [ ] SEM/FIB cross-section
- [ ] IR transmission crack imaging
- [ ] confocal/profilometry
- [ ] other: ____________________

Witness/device ID: ____________________

Measured/observed subsurface damage depth or upper bound: ____________________

Crack density/character: ____________________

Does visible chip size bound measured subsurface damage? ____________________

`SUBSURFACE-DAMAGE-QUALIFIED`: `PASS / FAIL / PARTIAL`

---

# L. Functional pre/post singulation comparison

Use the same condition and calibrated measurement chain where possible.

| metric | pre | post | normalized change | uncertainty | disposition |
|---|---:|---:|---:|---:|---|
| R(T,E) | | | | | |
| I–V symmetry | | | | | |
| contact/lead continuity | | | | | |
| noise ASD at f1 | | | | | |
| noise ASD at f2 | | | | | |
| 1/f knee/shape | | | | | |
| responsivity | | | | | |
| other | | | | | |

Data IDs: ____________________

For edge-clearance study:

- measured distance from functional detector region to nearest cut: ____________________
- `r_R = R_post/R_pre`: ____________________
- `Delta_e(f)=e_post/e_pre−1`: ____________________
- `r_resp=Rv_post/Rv_pre`: ____________________

Functional edge degradation detected? `YES / NO / INDETERMINATE`

---

# M. Room-temperature P35 disposition

All required gates:

- [ ] protection/support compatibility PASS
- [ ] cut dimensional state PASS
- [ ] visible edge state PASS
- [ ] residue/clean state PASS
- [ ] subsurface-damage method adequate for current qualification stage
- [ ] functional electrical/noise state PASS or documented bound
- [ ] die safe for P33 handling/attachment

Disposition:

- [ ] `SINGULATION-ROOM-TEMP-QUALIFIED`
- [ ] `HOLD — SUBSURFACE DATA REQUIRED`
- [ ] `HOLD — FUNCTIONAL DATA REQUIRED`
- [ ] `FAIL — MECHANICAL`
- [ ] `FAIL — CONTAMINATION/CHEMICAL`
- [ ] `FAIL — ELECTRICAL/NOISE`
- [ ] `SCRAP`

Reviewer/date: ____________________

---

# N. P33 cryogenic closure feedback

Package build ID: ____________________

P33 attachment revision: ____________________

Thermal-cycle history: ____________________

Compare before/after intended cryogenic qualification:

- edge chip growth: ____________________
- crack growth/new crack: ____________________
- fracture initiating at cut edge: ____________________
- delamination coupled to edge: ____________________
- resistance/I–V change: ____________________
- noise change: ____________________
- responsivity change: ____________________

Was failure separable from attachment/CTE stress? ____________________

Final disposition:

- [ ] `RP01-SINGULATION-QUALIFIED`
- [ ] `FAIL — CRYOGENIC EDGE PROPAGATION`
- [ ] `FAIL — COUPLED P35/P33 MECHANISM`
- [ ] `INDETERMINATE — MORE DISCRIMINATION REQUIRED`

Reviewer/date: ____________________

---

# O. Repeated-run / tool genealogy

Do not release from one visually successful die.

| run | tool age/dress state | process revision | worst visible damage | subsurface metric | functional shift | cryo result |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| ... | | | | | | |

Tool-wear trend detected? ____________________

Released tool-life/dressing interval: `QUAL / value after data`: ____________________

---

# P. Current historical unknowns

Do not fill these from local qualification:

- exact RP-01 separation method;
- RP-01 die outline;
- RP-01 blade/wire/laser;
- historical cut street/edge exclusion;
- historical frontside protection;
- historical post-cut clean;
- historical edge-damage acceptance.

Local `RP01-SINGULATION-QUALIFIED` means the reconstructed device survives a traceable singulation process; it does not mean the historical UWA cutting traveler has been recovered.
