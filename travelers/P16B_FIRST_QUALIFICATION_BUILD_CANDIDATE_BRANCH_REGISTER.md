# P16B — first qualification build candidate branch register

**Status:** CONTROLLED INTEGRATION REGISTER / DOCUMENTARY-SATURATION OUTPUT  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16, P16A, and the controlled process modules P01–P35.

## 1. Purpose

P16A answers: **what must be closed before a traceable first build can be authorized?**

P16B answers a different question:

> **What is the strongest single coherent first-qualification-build branch that the currently controlled literature supports, and which coordinates remain irreducibly laboratory-specific?**

This register therefore integrates the 36 P16A rows into one candidate process path. It does **not** promote an open P16A readiness row merely because a literature candidate has been selected here.

A P16B candidate may be:

- a direct RP-01 value;
- a same-lineage candidate;
- a transfer-family process center;
- a derived consequence of a published branch;
- or an explicit laboratory-only blank where literature cannot determine the realized process state.

The governing rule is:

`candidate branch definition != local branch frozen != historical RP-01 identity`.

---

# 2. Round-40 classification tags

A row may carry more than one tag.

- `DIRECT-RP01-EXECUTABLE` — direct RP-01 value can be carried into the candidate branch without guessing.
- `PUBLISHED-TRANSFER-CENTER-AVAILABLE` — a primary source provides a defensible first qualification center, but it is not RP-01 identity.
- `LOCAL-TOOL-IDENTITY-REQUIRED` — a real apparatus/model/revision is needed; literature cannot supply it.
- `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED` — actual supplier/product/lot/assay or contemporary formulation must be selected.
- `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED` — a physical response, transfer function, geometry, endpoint or performance map must be measured locally.
- `HISTORICAL-IDENTITY-ONLY` — remaining uncertainty blocks a literal RP-01 historical claim but does not by itself block a clearly labeled local transfer branch.
- `RELEASE-DATA-REQUIRED` — repeated-run/cycle/capability evidence is intrinsically post-build.

P16A state remains authoritative.

---

# 3. Integrated candidate branch — executive chain

The current strongest literature-supported qualification chain is:

1. high-quality insulating CdZnTe, with `Cd0.96Zn0.04Te (111)B` retained as the strongest x≈0.30 LPE transfer center;
2. explicit local final-surface preparation qualified through P29, because the strongest LPE `2–3% Br2/methanol / few seconds` source does not define concentration basis tightly enough for execution;
3. Honeywell-derived covered graphite horizontal-slider LPE topology, with target tie-line `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`;
4. absolute growth-charge mass determined from the actual selected boat volume/capacity, never from substrate-area scaling;
5. N2 purge followed by flowing H2 as the strongest Honeywell atmosphere-family branch, with actual purity/flow/pressure instrumentation local;
6. Hg-rich post-growth anneal beginning from the primary transfer center `250 °C / 1 h / Hg-saturated`, then released only from P05/P06 final-state data;
7. Mask-1 as a locally qualified thick positive resist branch; historical `AZ4620 / 3 µm / Br2:HBr` remains the strongest product-identified transfer candidate but is not assumed equivalent to current AZ P4620;
8. wet mesa centered on Srivastav x=.28 outputs and notation: `2% Br2`, `3:1 EG:HBr`, ~`21 °C`, `R_V≈2.78 µm/min`, `A≈.63`, best roughness ~2 nm, while concentration/ratio bases remain explicitly unresolved until locally defined;
9. anodic oxide centered on TI photoconductor evidence: `0.1 mol KOH per 1 L` of stated `90% EG / 10% DI-water` solvent, HgCdTe anode, carbon cathode, `J≈0.3 mA/cm²`, ~`15 V`, ~`2 min`, ~`800 Å / deep blue`; solvent-ratio basis remains to be made explicit locally;
10. Mask-2 functional state fixed by RP-01: positive single-layer lift-off resist, measured `4–5 µm`, `80 °C / 30 min`, chlorobenzene `30 min`, then pattern/develop/water rinse; exact commercial resist/developer remains local;
11. RIE candidate gas realization `CH4:H2=1:5` with direct total 64 sccm, giving **derived candidate** `10.6667 sccm CH4 / 53.3333 sccm H2`, at direct RP-01 `100 mTorr / 50 W / 60 s`; actual reactor/sheath/oxide-clear state is local;
12. Cr/Au direct stack `30 nm / 270 nm`, with thermal evaporation the strongest same-UWA method-family candidate; actual evaporator/vacuum/QCM/rates/thermal history local;
13. singulation initially screened with a low-force CdZnTe-compatible branch, with the Yoo wire-saw process retained as the strongest finished-CdZnTe quantitative transfer and no deep bromine post-dice etch automatically carried onto completed RP-01 devices;
14. compliant cryogenic attachment screened first because Honeywell primary evidence directly shows silicone-family attachment suppressing HgCdTe cooldown cracking; exact current adhesive/carrier/interconnect/vacuum geometry remains local;
15. all detector performance measurements share one explicitly named detector/contact-pair/package state, with RP-01 reference condition near `80 K` and `10 V/cm` for Figures 5–7; spectral responsivity uses the direct `1 kHz` chopped condition, while noise and temporal measurements are independently transfer-calibrated rather than conflated with the 1-kHz spectral measurement.

This chain is the current **candidate architecture**, not `TRACEABLE-FIRST-BUILD-READY`.

---

# 4. Thirty-six-row candidate branch matrix

## R01 — source-element identity / inventory

**P16A state:** `OPEN-CHOICE`  
**Round-40 tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`.

**Candidate branch:** high-purity elemental Hg/Cd/Te source preparation consistent with the Honeywell xL/yL composition calculation; `6N` starting elements are retained as a real Te-rich LPE transfer purity from Radhakrishnan et al. 2003.

**Literature-fixed:** use the selected tie-line composition, not an arbitrary HgTe/Te percentage shorthand.

**Irreducible local fields:** actual supplier, product/form, purity certificate, lot, oxide/handling history, balance IDs, and whether the local charge is prepared elementally or from a separately controlled synthesized source.

**Do not:** label 6N as an RP-01 disclosed purity.

---

## R02 — CdZnTe substrate composition / face / miscut

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate first-screen center:** `Cd0.96Zn0.04Te (111)B`, insulating, because P29 identifies this as the strongest current x≈0.30 Te-rich LPE substrate center. A detector-oriented source directly used `4% Zn`, `(111)B`, `10×10×1 mm³` material.

**Restriction:** substrate dimensions are not frozen here because they must be compatible with R04 boat/recess geometry.

**Local closure:** supplier/lot, measured Zn fraction/lattice parameter, plane, A/B polarity, miscut magnitude/azimuth, inclusion/defect state and electrical isolation.

---

## R03 — final CdZnTe pre-LPE surface

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Strongest LPE transfer family:** chemical + mechanical polishing followed by `2–3% Br2/methanol` for `a few seconds`, then prompt loading.

**Not executable as printed:** the source does not define Br2 percentage basis, exact time, bath T/agitation, rinse/dry or removed depth.

**Candidate decision:** preserve this as the preferred **family**, but do not manufacture a v/v or w/w recipe in P16B. R03 remains an explicit pre-build local recipe definition/qualification task.

**Cross-module rule:** the selected surface must be released by resulting P03/P05/P06 quality, not AFM roughness alone.

---

## R04 — LPE boat / well / source hardware

**P16A state:** `APPARATUS-NOT-SELECTED`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate architecture:** Honeywell covered graphite horizontal-slider topology with substrate recess, movable slider, tapered growth well(s), graphite plug/cap, separate Hg-source recess, Hg-distribution grooves/moats, close cover and quartz-tube furnace.

**Local-only quantities:** every dimension, well volume, plug displacement, clearances, overlap, source recess, hot motion, furnace position and thermometry geometry.

**Authorization condition:** P30A apparatus register must reach a dimensioned/calibrated local revision before R05 can be numerical.

---

## R05 — absolute LPE charge inventory

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate composition center:** Honeywell `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`.

For a locally selected total growth charge `M_charge`, P30A gives the current derived mass fractions:

- `w_Hg = 0.249740`;
- `w_Cd = 0.012502`;
- `w_Te = 0.737758`.

Therefore:

`m_Hg = 0.249740 M_charge`  
`m_Cd = 0.012502 M_charge`  
`m_Te = 0.737758 M_charge`.

**Critical blank:** `M_charge` itself is not literature-closed and must be selected from the actual R04 well/capacity/meniscus geometry.

**Separate coordinate:** auxiliary Hg/HgTe source inventory is not part of `M_charge`.

**Prohibited:** area-scaling the Radhakrishnan ~4.8-g run charge into the Honeywell boat.

---

## R06 — LPE atmosphere

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate atmosphere family:** Honeywell `N2 purge -> flowing H2`.

**Literature-fixed:** sequence/family only.

**Local blanks:** gas suppliers/lots/grades, purification, line materials, purge volume/time, process flows, pressure/backpressure, flow calibration, O2/H2O monitoring and acceptance thresholds.

---

## R07 — LPE thermal / contact / wipe / cooldown trajectory

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate thermodynamic center:** use the Honeywell composition line `TL=507 °C` as the equilibrium anchor; demonstrate solution above local liquidus before below-liquidus contact.

**Transfer envelope:** Harman primary branches support supercooling of roughly `2–10 °C` and contact/growth durations from seconds to tens of minutes, while Honeywell examples can extend to ~30 min.

**Round-40 decision:** do **not** invent one supercooling/contact time by averaging incompatible branches. Local P03/P30A thickness/composition calibration must select the numerical trajectory.

**Wipe:** choose one explicit hardware branch and retain its genealogy.

---

## R08 — as-grown optical material metrology

**P16A state:** `METROLOGY-NOT-IMPLEMENTED`  
**Tags:** `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate method:** P06/P06A transmission FTIR mapping with frozen optical constants/model and an independent physical-thickness reference.

**Reference model:** Hansen `Eg(x,T)` may provide optical composition consistency, but does not substitute for instrument qualification.

**Local blanks:** FTIR model/serial, source/detector/beamsplitter state, aperture footprint, stage map, wavelength calibration, thickness-reference method and uncertainty.

---

## R09 — as-grown Hall / Van der Pauw

**P16A state:** `METROLOGY-NOT-IMPLEMENTED`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Method center:** Van der Pauw Hall/resistivity is direct UWA/RP-01 lineage; direct converted-layer work includes 80 K and 300 K measurements with magnetic field up to 2 T.

**Candidate first-build use:** apply P05 signed Hall/tensor analysis to the as-grown and post-anneal coupons, preserving the p/n transition rule.

**Local blanks:** magnet, cryostat, contacts, current source, voltmeter/preamp, field calibration and geometry/contact validity.

---

## R10 — Hg anneal enclosure / reservoir

**P16A state:** `APPARATUS-NOT-SELECTED`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate architecture:** closed sealed quartz ampoule with elemental-Hg reservoir; begin with an isothermal/Hg-saturated branch because this most directly targets the lightly n-type RP-01 final state.

**Local blanks:** ampoule geometry/free volume, reservoir vessel, Hg inventory, sample/source spacing, furnace zoning, seal/evacuation protocol and calibrated `T_s/T_Hg` positions.

---

## R11 — Hg anneal trajectory

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Selected first-screen center:** Harman primary branch `250 °C / 1 h / Hg-saturated`.

**Near-composition support:** Nagahama x≈0.17–0.30 evidence places `250–300 °C` in a useful n-type region without the composition change observed near 400 °C.

**Release rule:** the 1-h center is a first screen only. P05/P06 must confirm stable N-LIKE state, mobility, optical preservation and morphology; time is then mapped locally.

**Cooldown:** complete `T_s(t)` and `T_Hg(t)` remain local and mandatory.

---

## R12 — Mask-1 resist / lithography

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Strongest product-identified transfer:** historical HgCdTe Br2/HBr branch using `AZ4620`, `3 µm` resist and a 5-µm opening.

**Round-40 candidate use:** retain AZ4620 only as the first historical product-family screen; do not assume a current AZ P4620 lot is compositionally/process equivalent.

**Build-freezing requirement:** actual contemporary resist product/lot, one-coat thickness, bake, aligner, calibrated dose, developer, strip and P28 survival must be selected through P32.

---

## R13 — wet-mesa etchant preparation basis

**P16A state:** `UNDEFINED-BASIS`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Selected literature center:** Srivastav x=.28 notation `2% Br2` in `3:1 EG:HBr`.

**Important:** neither the Br2 percentage basis nor the 3:1 ratio basis nor HBr stock assay is directly closed.

Same-SSPL evidence raises volume-based Br2 interpretation to `CANDIDATE-VV-SAME-LAB`, but primary HgCdTe literature also contains explicit w/w bromine conventions.

**Round-40 decision:** do not convert this to executable masses/volumes in P16B. The actual local branch must explicitly define denominator, ratio basis and HBr assay before authorization.

---

## R14 — wet-mesa endpoint / rinse / passivation handoff

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Literature response center:** near `21 °C`, mean vertical rate `~2.78 µm/min`, anisotropy `~0.63`, best RMS roughness ~`2 nm` in the Srivastav x=.28 branch.

**Endpoint:** measured through-layer depth plus electrical isolation; do not release from calculated time alone.

**Candidate handoff philosophy:** minimize uncontrolled post-etch air exposure and timestamp quench/rinse/dry or wet-transfer path into P25. Same-SSPL process evidence establishes that rinse/no-air trajectory matters, but no exact RP-01 handoff is claimed.

**Local blanks:** bath state/agitation, actual quench/rinse sequence, dry/wet-transfer decision, air time and `t_etch->P25`.

---

## R15 — anodic oxide cell / bath execution

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Selected transfer center:** TI photoconductor branch:

- `0.1 mole KOH in 1 liter` of stated `90% EG / 10% DI-water` solvent;
- HgCdTe anode;
- carbon-rod cathode;
- `J≈0.3 mA/cm²`;
- final voltage around `15 V`;
- time around `2 min`;
- uniform deep-blue oxide around `800 Å`.

For pure KOH, the ideal inventory is **derived**:

`m_KOH = 5.61056 g per L`, or `5.61056/a_KOH g` for reagent assay fraction `a_KOH`.

**Unresolved source convention:** 90:10 solvent basis is not explicitly identified as v/v or w/w.

**Local closure:** choose explicit basis, reagent lots/assay, actual cell geometry, electrochemically exposed area, current, `V(t)`, `Q/A`, endpoint and rinse/handoff.

---

## R16 — Mask-2 resist / exposure / developer / chlorobenzene

**P16A state:** `OPEN-CHOICE`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Direct functional branch:** measured positive single-layer lift-off resist thickness `4–5 µm`; prebake `80 °C / 30 min`; chlorobenzene `30 min`; then pattern/develop/water rinse; same resist must survive P08 and lift off the 300-nm total Cr/Au stack.

**Candidate product philosophy:** use a positive DNQ/diazo-novolak-type product that can actually reproduce the direct thickness and chlorobenzene-shaped profile; product identity is local.

**Do not:** identify AZ4330/AZ4400/AZ4620 merely from thickness resemblance, or AZ4110 merely from chlorobenzene mechanism.

---

## R17 — RIE gas realization

**P16A state:** `UNDEFINED-BASIS`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

Direct RP-01:

- printed `CH4/5H2`;
- total `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`.

Same-lineage explicit interpretation:

`CH4:H2 = 1:5`.

Therefore the **derived candidate** split is:

`Q_CH4 = 64/6 = 10.6667 sccm`  
`Q_H2 = 5×64/6 = 53.3333 sccm`.

These are not direct historical MFC values.

**Local blanks:** gas purity/source, separate/premixed implementation, MFC ranges/calibration, line/purge state and realized flow accuracy.

---

## R18 — RIE reactor / sheath / thermal state

**P16A state:** `APPARATUS-NOT-SELECTED`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Direct architecture:** Plasma Technology parallel-plate RIE.

**Not recovered:** exact reactor model/revision, RF frequency, powered/grounded area, gap, sample position/loading, holder, temperature, pump/throttle, pressure gauge, base pressure, self-bias and chamber clean/season state.

**Candidate decision:** no substitute reactor can be called equivalent from 50 W alone. Select one local parallel-plate reactor and execute P34 equivalence mapping.

---

## R19 — oxide clear + semiconductor exposure

**P16A state:** `OPEN-CHOICE`  
**Tags:** `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate rule:** `t_sem = t_RF - t_clear` only after local oxide-clear time is measured in the selected R18 reactor.

**Direct total RF time:** 60 s is a target historical center, not permission to assume the entire interval is semiconductor conversion.

**Release outputs:** oxide-open fraction, physical etch depth, conversion depth, Hall sheet state, minority blocking and P26 contact performance.

---

## R20 — Cr/Au deposition

**P16A state:** `APPARATUS-NOT-SELECTED`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Direct stack:** `Cr 30 nm / Au 270 nm`.

**Selected method-family candidate:** thermal evaporation, because same-UWA 1998 HgCdTe fabrication explicitly used angled thermal evaporation for contact metal.

**Do not carry:** the historical angle into RP-01.

**Local blanks:** evaporator, source hardware, base/process pressure, Cr/Au rates, source-sample geometry, QCM tooling factors, witness calibration, wafer thermal load, actual RIE-to-Cr air break, Cr-to-Au vacuum history.

**P26A rule:** Cr and Au thickness calibration are separate unless data justify a common tooling factor.

---

## R21 — lift-off

**P16A state:** `OPEN-CHOICE`  
**Tags:** `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`, `HISTORICAL-IDENTITY-ONLY`.

Historical chlorobenzene lift-off literature demonstrates acetone-based and ultrasonic branches, but RP-01 solvent/time/agitation remain open.

**Candidate decision:** no historical solvent is selected in P16B. The first local branch shall start from the least mechanically aggressive remover compatible with the selected R16 resist, then qualify full release without fences/residue/delamination.

**No default ultrasonics.**

---

## R22 — final CD / contact geometry

**P16A state:** `METROLOGY-NOT-IMPLEMENTED`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Direct geometry reference:** nine contacts approximately `300×300 µm`, gap series `50–400 µm` in 50-µm increments.

**Candidate measurement:** calibrated optical/SEM/profilometric dimensional metrology sufficient to name the actual contact pair/gap used in P10–P13.

**Local blanks:** instrument, calibration, uncertainty, coordinate registration and acceptance limits.

---

## R23 — TLM / contact QC

**P16A state:** `METROLOGY-NOT-IMPLEMENTED`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Direct reference structure:** 9 × `300×300 µm` contacts with 50–400-µm gaps; historical `rho_c≈9×10^-4 Ω·cm²` at 80 K.

**Candidate closure:** implement P09/P26 TLM with actual fabricated dimensions and a declared optical-background state.

**Local blanks:** cryostat/fixture, excitation/current, voltage measurement, contact-pair automation and uncertainty/reduction validation.

---

## R24 — bare-device bias / load / self-heating

**P16A state:** `METROLOGY-NOT-IMPLEMENTED`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Direct detector-state center:** use `E=10 V/cm` for the key RP-01 noise/D* state and include a bounded field sweep comparable to Figure 3 where safe.

**Definition:** field derives from measured contact-to-contact voltage divided by measured active gap.

**Local blanks:** bias source, current limiting/load resistor, coupling/preamp network, detector-terminal voltage measurement and thermal transfer.

---

## R25 — absolute spectral responsivity

**P16A state:** `METROLOGY-NOT-IMPLEMENTED`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Direct reference state:** ~80 K, stated 60° FOV, chopped spectral response at `1 kHz`, detector cutoff reported ~`4.4 µm`, BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm and QE ~70%.

**Candidate local method:** P11 absolute radiometry with measured package geometry/view factor and calibrated wavelength-dependent optical transfer.

**Do not:** use “60° FOV” as the geometrical calibration itself.

---

## R26 — detector-terminal noise / PSD

**P16A state:** `METROLOGY-NOT-IMPLEMENTED`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Direct historical state:** same physical detector as other key figures; Figure 5 states ~80 K, `10 V/cm`, stated 60° FOV; low-noise preamp + HP35665A; 1/f knee ~3 kHz; high-frequency g-r level ~`24.5 nV/sqrtHz`.

**Critical rule:** 24.5 nV/sqrtHz is not the historical 1-kHz noise.

**Candidate local method:** P12/P12B detector-terminal-referred PSD with measured network/preamp/analyzer transfer, FFT/window/ENBW and background state.

---

## R27 — temporal / frequency response

**P16A state:** `METROLOGY-NOT-IMPLEMENTED`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`, `HISTORICAL-IDENTITY-ONLY`.

RP-01 has no direct lifetime/f3dB curve.

**Selected same-UWA transfer method center:** `1.047 µm` laser, `25 ns`, `1 kHz`, ~77 K vacuum, variable-current bias, AC-coupled amplifier, HP54522A, 500 samples at 20 ns spacing, 128 averages typical.

**Restriction:** these are apparatus/method transfer values, not RP-01 detector setpoints and not proof of low injection.

**Local closure:** source/spot/injection calibration, electrical transfer, package thermal response and model/residual checks.

---

## R28 — singulation method / support / protection / street

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Selected first-screen family:** low-force wire-saw separation because direct finished-CdZnTe detector evidence provides a concrete process:

- ~`1×1 cm` metallized sample;
- low-melting wax on graphite support;
- photoresist frontside protection;
- `125 mm` stainless-steel wire;
- `16 µm` BN slurry;
- very slow cut, ~`1 h` per complete cut.

**Restriction:** protection, wax, slurry and exact tool conditions require compatibility qualification on the completed RP-01 stack.

**Do not transfer:** the same source's `5% Br/methanol / 5 min` damage-removal etch onto a completed 9.5-µm HgCdTe device.

---

## R29 — singulation clean / edge / subsurface inspection

**P16A state:** `OPEN-CHOICE`  
**Tags:** `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate rule:** clean/release chemistry must remove the selected R28 temporary mount/protection/slurry without attacking oxide, Cr/Au or HgCdTe.

**No literature-defined universal completed-device clean has been recovered.**

**Required responses:** visible chipping, edge roughness, subsurface-damage proxy, residue, pre/post resistance/noise/responsivity versus edge distance and later cryogenic survival.

---

## R30 — die attach / carrier / cold finger

**P16A state:** `OPEN-CHOICE`  
**Tags:** `PUBLISHED-TRANSFER-CENTER-AVAILABLE`, `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Selected first-screen family:** compliant silicone attachment because Honeywell primary experiments directly showed HgCdTe cooldown cracking with glass adhesive but survival with silicone-rubber attachment to 5 K.

Historical named materials include Dow Corning 3110/3112/3116, but modern identity/equivalence is not assumed.

**Local closure:** current vacuum/cryogenic-compatible adhesive, carrier/cold-finger material, bondline thickness/coverage/voids, cure, die tilt, thermal resistance and package thermal poles.

---

## R31 — wire / interconnect

**P16A state:** `OPEN-CHOICE`  
**Tags:** `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`, `HISTORICAL-IDENTITY-ONLY`.

RP-01 Cr/Au top metal is direct; wire metallurgy and bond method are not.

**Round-40 decision:** do not invent Au-wire wedge/ball settings from generic microelectronics practice. Select actual wire/ribbon, bonder/tool and settings through P33 coupon qualification on the P26 pad stack.

Required outputs: continuity/contact resistance, pull/shear where appropriate, pad damage, thermal-cycle stability and noise/microphonics.

---

## R32 — aperture / window / shield / FOV

**P16A state:** `OPEN-CHOICE`  
**Tags:** `DIRECT-RP01-EXECUTABLE`, `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`, `HISTORICAL-IDENTITY-ONLY`.

**Direct reference:** stated `60° FOV` for key RP-01 detector measurements.

**Candidate requirement:** build a measured optical geometry that can reproduce a declared 60°-class field if desired, but record aperture dimensions, separations, window material/thickness/coating, shield geometry, alignment and spectral transmission.

**Do not:** treat a nominal angle label as a view-factor calibration.

---

## R33 — vacuum / pump / bake / cooldown

**P16A state:** `OPEN-CHOICE`  
**Tags:** `LOCAL-TOOL-IDENTITY-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

**Candidate requirement:** operate packaged detector near 77–80 K under a measured vacuum/purge state with a P33-qualified thermal budget.

**No exact RP-01 pressure, pump sequence or bake has been recovered.**

Local fields: chamber/Dewar, gauges, pump/purge, leak/outgassing evidence, bake, cooldown trajectory and die-temperature proxy.

---

## R34 — cryogenic singulation / package survival

**P16A state:** `RELEASE-DATA-OPEN`  
**Tags:** `RELEASE-DATA-REQUIRED`, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`.

No literature number can close this for the selected local R28–R33 stack.

Required evidence: repeated thermal cycles with edge/crack inspection, delamination/voiding, contact/interconnect resistance, P10/P12 state, package thermal transfer and optical alignment.

---

## R35 — end-to-end genealogy / data capture

**P16A state:** `LOCAL-BRANCH-FROZEN` conceptually  
**Tags:** `DIRECT-RP01-EXECUTABLE` in concept, `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED` for actual IDs.

**Candidate branch:** P16/P17 identifier chain is mandatory from the first qualification coupon onward.

Before physical work, instantiate:

- substrate/source/boat/anneal/chemistry/resist/RIE/metal/singulation/package run IDs;
- raw-data paths;
- instrument calibration IDs;
- deviations;
- timestamps for sensitive handoffs;
- operator/reviewer signatures.

This is one of the few readiness elements whose scientific architecture is already sufficiently defined; only actual laboratory identifiers remain.

---

## R36 — statistical process capability / yield

**P16A state:** `RELEASE-DATA-OPEN`  
**Tags:** `RELEASE-DATA-REQUIRED`.

Not required to authorize the first qualification build.

Requires repeated frozen-route runs, MSA, stability, process limits, yield, genealogy-aware statistics and change control before `REPRODUCIBLE-RELEASE`.

---

# 5. Safe derived quantities carried into the candidate branch

These are arithmetic consequences of explicitly identified source branches; they do not create missing physical setpoints.

## 5.1 Honeywell composition mass fractions

For selected local `M_charge`:

- `m_Hg = 0.249740 M_charge`;
- `m_Cd = 0.012502 M_charge`;
- `m_Te = 0.737758 M_charge`.

`M_charge` remains local-apparatus-dependent.

## 5.2 RIE candidate split

For total 64 sccm and candidate 1:5 CH4:H2:

- `Q_CH4 = 10.6667 sccm`;
- `Q_H2 = 53.3333 sccm`.

These are candidate local nominal values, not direct historical MFC readings.

## 5.3 TI anodization KOH inventory

For 0.1000 mol pure KOH:

`m_KOH = 0.1000 mol × 56.1056 g/mol = 5.61056 g`.

For assay fraction `a_KOH`:

`m_reagent = 5.61056/a_KOH g` per stated 1-L solvent batch.

The 90:10 EG:H2O preparation basis remains to be explicitly chosen before execution.

## 5.4 Direct Mask-2 metal/resist ratio

RP-01 resist `4–5 µm`; total metal `0.30 µm`:

- minimum nominal thickness ratio `4/0.30 = 13.3`;
- maximum `5/0.30 = 16.7`.

This is a geometry consistency check, not a lift-off guarantee.

---

# 6. Cross-module compatibility audit

## 6.1 P29 -> P30

The candidate `(111)B / 4% Zn` substrate family is compatible with the selected Te-rich horizontal-slider literature lineage. Physical substrate dimensions cannot be frozen until the actual P30A boat/recess is selected.

## 6.2 P30 -> P31

The selected anneal begins below 300 °C and is intentionally downstream of measured as-grown P05/P06 state. No high-temperature defect-conditioning stage is inserted by default.

## 6.3 P32 -> P28 -> P25

Mask-1 qualification, mesa etch and anodization are one coupled surface-state path. P16B does not allow an unqualified dry/storage interval between P28 and P25. The selected Mask-1 product must survive the locally defined Br2/EG/HBr branch to electrical isolation, strip cleanly, and preserve the P25 anodization response.

## 6.4 P25 -> P27

The selected Mask-2 resist/developer must be compatible with the completed native anodic oxide. Developer attack on oxide/passivated HgCdTe is a qualification response, not assumed benign.

## 6.5 P27 -> P08

Mask-2 is not lift-off-only. It must retain opening CD and re-entrant profile through the full RIE exposure. RIE survival is a release gate for the lithography branch.

## 6.6 P08 -> P26

No undocumented clean is inserted between the RIE-modified contact region and Cr. `t_RIE->Cr` and atmosphere are recorded. RP-01 load-lock capability is not treated as proof of zero air exposure.

## 6.7 P26 -> P35

Singulation protection/release chemistry must preserve the final Cr/Au, oxide and converted contact regions. Strong bulk-CdZnTe damage-removal etches are prohibited from automatic transfer to the completed detector.

## 6.8 P35 -> P33

P33 receives an edge-inspected, electrically baselined singulated die. Final singulation release is not complete until P33 thermal cycling confirms no edge-crack propagation or detector degradation.

## 6.9 P10 -> P11 -> P12 -> P13 shared detector state

Every combined performance claim must record or correct:

- physical detector ID;
- contact pair and measured gap;
- detector/contact voltage and field;
- temperature;
- package/window/shield geometry;
- optical background/FOV;
- dissipated power/thermal state;
- frequency or time-domain condition.

`D*`, responsivity, noise and lifetime/bandwidth are not combined across unmatched detector states without an explicit correction model and uncertainty.

---

# 7. Irreducible laboratory-specific minimum set

After documentary saturation, the following cannot be honestly closed by more literature searching alone. A real laboratory identity/measurement is required:

1. actual CdZnTe supplier/lot and measured crystallographic/material state;
2. executable final pre-LPE surface recipe and clean-to-load realization;
3. dimensioned LPE boat/furnace/tube/actuator;
4. numerical total LPE charge and auxiliary Hg-source inventory;
5. actual gas-delivery/purity/flow/pressure instrumentation;
6. calibrated LPE solution/substrate thermal field and contact/wipe/cooldown trajectory;
7. FTIR and Hall apparatus/calibration chains;
8. dimensioned Hg-anneal enclosure/reservoir and measured `T_s/T_Hg` trajectory;
9. actual Mask-1 resist, coater, aligner, developer and strip;
10. explicit P28 Br2 and EG:HBr preparation bases plus HBr assay;
11. actual P28 rinse/air/P25 handoff;
12. explicit P25 90:10 solvent basis, cell geometry and electrochemical area;
13. actual Mask-2 resist/developer/exposure/lift-off branch;
14. actual CH4/H2 gas delivery and calibrated MFCs;
15. selected RIE reactor/sheath/temperature/chamber-state implementation and oxide-clear time;
16. selected metal-deposition tool/vacuum/source/QCM/rate/thermal implementation;
17. final CD/TLM/bias/radiometry/noise/temporal measurement apparatus;
18. singulation tool/protection/clean/street implementation;
19. current cryogenic attachment/interconnect/window/shield/vacuum construction;
20. repeated package survival and later process-capability evidence.

These are not failures of literature review. They are properties of the local physical system.

---

# 8. What P16B does and does not close

P16B materially reduces the remaining design space by selecting one evidence-ranked process architecture and by refusing unnecessary alternative branches.

It closes:

- the preferred substrate-family center;
- the LPE composition/topology family;
- the first-screen anneal center;
- the wet-mesa empirical response center;
- the anodization transfer center;
- the Mask-2 direct functional state;
- the RIE candidate gas split;
- the Cr/Au stack and deposition-method family;
- the initial singulation family;
- the initial compliant die-attach family;
- the shared detector-state conventions for P10–P13.

It does **not** close the P16A execution rows whose realized value depends on actual tools, lots, geometry or calibration.

Current project disposition therefore remains:

`TRACEABLE-FIRST-BUILD-READY = NO`  
`HISTORICAL-RP01-REPRODUCED = NO`  
`REPRODUCIBLE-RELEASE = NO`.

---

# 9. Round-40 candidate-build authorization status

The candidate architecture is now sufficiently integrated that future work should no longer ask “which literature family should we use?” for every row.

The next useful question is:

> **Which of the twenty irreducible local identities/calibrations can be converted into explicit procurement/tool specifications and simulated/calibration travelers without performing the physical experiment?**

Because the project is literature/manual/theoretical only, future rounds should prioritize specification packages that a future laboratory could fill in directly:

- apparatus requirement sheets;
- procurement specification templates;
- calibration plans;
- pre-run data sheets;
- branch-freezing decision rules;
- cross-module acceptance logic.

Do not fabricate local measurements that have not been made.