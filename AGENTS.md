# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 41  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual/booklet executable by a competent researcher without undocumented tribal knowledge.

Canonical first process:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end REPRODUCIBLE-RELEASE yet**.

---

# Continuity preservation

This is the current condensed front door. Detailed historical reasoning remains in Git history, timestamped research checkpoints, source ledgers and gap-matrix addenda.

Useful preserved states:

- pre-Round-39 detailed head: `2f46f251b4b6f6655197779a1694078fc333f860`, AGENTS blob `18f193b5442bf4b916611f33c4bdb3da463d6145`;
- Round-39 condensed AGENTS blob `24b87adcf096ba487a1a8873ec0bf3db7dfae6b6`;
- Round-40 AGENTS blob `75fc060dfc18adf6051e636a516b812ca0a1f061`;
- Round-40 head `0ddecb56341d4266bd5cef9dc789342c95ccb9f7`.

Do not delete historical checkpoints/source ledgers merely because this file is condensed.

---

# Current checkpoint — READ FIRST

Latest:

`research/2026-08-16_checkpoint_after_minimum_lab_capability_round41.md`

Then:

- `research/2026-08-16_checkpoint_after_first_qualification_build_integration_round40.md`
- `research/2026-08-16_checkpoint_after_lithography_documentary_limit_round39.md`
- `research/2026-08-16_checkpoint_after_cr_au_deposition_round38.md`
- `research/2026-08-16_checkpoint_after_rie_gas_anodization_round37.md`
- `research/2026-08-16_checkpoint_after_wet_mesa_chemistry_round36.md`
- `research/2026-08-16_checkpoint_after_lpe_absolute_charge_round35.md`
- `research/2026-08-16_checkpoint_after_first_build_readiness_round34.md`
- older checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND41.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND41.md`
- then Round40/39/etc.

Current integration registers:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`
- `travelers/P16C_MINIMUM_LAB_CAPABILITY_IMPLEMENTATION_REGISTER.md`

Round-41 capability specification:

`docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`.

---

# Maturity / implementation labels — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — one complete build can be executed without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — historical identity is sufficiently closed to claim reproduction of the Smith et al. process itself.
3. `REPRODUCIBLE-RELEASE` — repeated stability/MSA/capability/yield/change-control/performance evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual laboratory tools/stations are identified, calibrated and surrogate-commissioned enough to begin the remaining HgCdTe-specific qualification.

Current:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`

P16A is authoritative for build readiness. P16B is authoritative for the preferred candidate branch. P16C is authoritative for the future laboratory capability fill-in record.

`candidate branch != infrastructure ready != LOCAL-BRANCH-FROZEN != historical identity != reproducible release`.

---

# Permanent evidence discipline

- Never invent a missing number.
- Separate direct RP-01, same-lineage, transfer-family, derived, apparatus-calibration and local-qualification evidence.
- Repetition does not promote evidence class.
- “Not recovered” does not mean absent.
- Preserve negative searches, rejected inferences, conflicts and failed branches.
- Empirical/practical primary literature precedes theoretical placeholders.
- Theory may check consistency; it does not manufacture process settings.
- Do not splice incompatible process generations into a fictional published recipe.
- A controlled closure method is not a physically closed readiness row.
- Values that depend on the actual tool—well volume, furnace gradient, MFC calibration, sheath state, QCM tooling factor, sample temperature, view factor, bondline geometry—are local physical quantities, not literature gaps.
- Engineering capability ranges are not historical process setpoints.
- Surrogate commissioning is not HgCdTe process equivalence.

---

# Round-41 capability evidence classes

Use:

- `HARD-MINIMUM`
- `FIRST-BUILD-ENGINEERING-ENVELOPE`
- `DESIGN-CHECK`
- `SURROGATE-COMMISSIONABLE`
- `HGCDTE-REQUIRED`
- `LOCAL-BLANK`
- `EH&S/FACILITY-GATE`

Do not promote one class into another silently.

---

# Canonical RP-01 anchors — do not drift

## Material

- LPE n-HgCdTe on electrically insulating CdZnTe;
- nominal `x≈0.30`;
- supplier `n≈9.8×10^14 cm^-3`;
- supplier `mu≈4.0×10^4 cm²/V·s`;
- active layer `9.5 µm`;
- historical methods used for x/thickness remain open.

## Passivation / lithography / RIE / metal

- native anodic oxide ~`800 Å = 80 nm`;
- Mask-1 = wet-mesa delineation; product/process not disclosed;
- Mask-2 `4–5 µm`; `80 °C / 30 min`; chlorobenzene `30 min`; then pattern/develop/water rinse;
- same Mask-2 survives RIE and supports lift-off;
- Plasma Technology parallel-plate RIE; printed `CH4/5H2`; total `64 sccm`; `100 mTorr`; `50 W`; `60 s`;
- converted average n ~`2.0×10^15 cm^-3`; mobility ~`3.3×10^4 cm²/V·s`;
- Cr `30 nm`; Au `270 nm`;
- nine ~`300×300 µm` contacts; gaps 50–400 µm by 50;
- `rho_c≈9×10^-4 Ω·cm²` at 80 K.

## Detector state

- key data around 80 K;
- stated 60° FOV;
- spectral response chopped at 1 kHz;
- field = measured contact-to-contact voltage / measured active gap;
- Figures 5–7 use 10 V/cm;
- same physical detector for Figures 3/5/6/7, exact contact pair open;
- cutoff ~4.4 µm, convention open;
- BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm;
- QE ~70%;
- low-noise preamp + HP35665A;
- 1/f knee ~3 kHz;
- high-frequency g-r ~24.5 nV/sqrtHz;
- 24.5 nV/sqrtHz is **not** the historical 1-kHz noise;
- RP-01 lifetime/f3dB remains open.

---

# Controlled architecture

Physical/process/metrology modules remain P01–P35.

Integration/control layer includes:

- P16 master end-to-end traveler;
- P16A first-build/release-readiness audit + 36-row register;
- P16B first-qualification-build candidate branch register;
- P16C minimum laboratory capability implementation register;
- P17 statistical release/capability;
- P18 failure analysis;
- P19/P20 requirements/sensitivity;
- P21/P22/P23 empirical modeling/DOE/state-boundary support.

Do not create a new physical SOP when an existing module already contains the closure method.

---

# Preferred candidate architecture retained from Round 40

1. `Cd0.96Zn0.04Te (111)B` preferred substrate family; actual lot/size/plane/miscut local.
2. P29 Br2/methanol final-surface family; no invented concentration basis.
3. Honeywell covered graphite horizontal-slider LPE topology.
4. composition center `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`.
5. N2 purge -> flowing H2 atmosphere family.
6. Hg anneal first screen `250 °C / 1 h / Hg-saturated-isothermal-like`, released only from P05/P06 final state.
7. Mask-1 historical product screen AZ4620 3-µm Br2/HBr transfer branch; modern equivalence unproven.
8. wet mesa centered on Srivastav `2% Br2 / 3:1 EG:HBr`, ~21 °C, ~2.78 µm/min, A~.63, best RMS ~2 nm; bases remain open.
9. anodization centered on TI: 0.1 mol KOH per stated 1 L of 90% EG / 10% DI-water solvent, carbon cathode, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å/deep blue; solvent-ratio basis remains open.
10. direct RP-01 Mask-2 functional state: 4–5 µm / 80 °C 30 min / chlorobenzene 30 min.
11. RIE same-lineage gas candidate 1:5; total 64 sccm -> derived 10.6667 sccm CH4 / 53.3333 sccm H2.
12. Cr/Au direct 30/270 nm; thermal evaporation strongest same-UWA method-family candidate.
13. low-force wire-saw first singulation screen; no automatic 5% Br/methanol bulk-damage-removal transfer.
14. compliant silicone-family first package-attach screen.
15. P10–P13 share one explicitly matched detector/contact/package/T/field/background state.

These are candidate centers/families, not a released build.

---

# Round-41 numerical convention — authoritative correction

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md` freezes:

- Hg `200.59 g/mol`;
- Cd `112.414 g/mol`;
- Te `127.60 g/mol`.

For `xL=.082`, `yL=.810` the canonical mass fractions are:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

Some P30A/P16B/Round-40 integration text printed approximately `0.249740 / 0.012502 / 0.737758` from a slightly different Hg atomic-weight convention. Treat those later rounded values as a controlled numerical erratum.

Future charge calculations use the frozen calculation values until a deliberate versioned constants update is propagated throughout the repository.

`M_charge` remains apparatus-dependent.

---

# Round-41 minimum laboratory capability envelope

## LPE

- process-region thermal commissioning around ~495–520 °C as an engineering envelope around the 507 °C liquidus and represented supercooling region;
- actual boat dimensions/capacity/hot motion/thermal map required;
- N2/H2 gas trains with calibrated flows;
- `M_charge`, Hg-source inventory, liquidus/contact/wipe/cooldown remain local/HgCdTe-dependent.

## Hg anneal

- support first screen around 250 °C / 1 h;
- map at least roughly 250–300 °C low-temperature region;
- separately measure/log `T_s(t)` and `T_Hg(t)`;
- complete cooldown trace.

## FTIR

- ~500–5000 cm^-1 coverage;
- <=4 cm^-1 qualification resolution unless sensitivity validates coarser;
- minimum 9-point map, preferred 5x5+ where geometry permits;
- independent thickness reference over expected ~5–15 µm.

## Hall/VdP

- HARD-MINIMUM >= +/-0.50 T to execute P05 initial grid;
- ~+/-2 T preferred extended capability;
- ~80 K and 300 K measurement states;
- field/current reversal and measured B at sample.

## Lithography / wet chemistry / anodization

- Mask-2 4–5 µm, 80 °C/30 min, chlorobenzene 30 min;
- measured exposure dose/development/profile;
- explicit Br2/EG:HBr/HBr basis for wet mesa;
- anodization around J~0.3 mA/cm², V~15 V, ~2-min first screen, ~80 nm with continuous V(t);
- `I=J A_exposed` — no fixed current before area is measured.

## RIE

- direct controller center 64 sccm / 100 mTorr / 50 W / 60 s;
- candidate flows 10.6667/53.3333 sccm;
- mandatory self-bias/sheath, reflected power, sample thermal state, chamber genealogy and oxide-clear calibration;
- no arbitrary base-pressure spec.

## Cr/Au

- 30 nm Cr / 270 nm Au capability;
- separate Cr/Au QCM-witness calibration unless equivalence is demonstrated;
- actual pressure, rates, source geometry, sample thermal load and RIE->Cr exposure must be logged;
- no arbitrary base-pressure spec.

## Integrated detector station

- stable ~80 K operation;
- canonical 10 V/cm, controlled exploration toward historical ~50 V/cm where qualified;
- absolute point at 4 µm and coverage through/beyond ~4.4-µm edge;
- 1-kHz optical modulation;
- noise coverage including 100 Hz–10 kHz / ~3-kHz knee;
- temporal transfer including 1 kHz, 10 kHz, 100 kHz, 1 MHz and extension to >=5–10x observed f3dB where practical;
- one matched detector/contact/package/T/E/background/load state across P10–P13.

Noise design check:

if electronics PSD is allocated fraction `beta` of the 24.5-nV/sqrtHz detector plateau PSD,

`e_elec <= 24.5 sqrt(beta) nV/sqrtHz`.

25-ns pulse design check if that branch is implemented:

`BW~0.35/25 ns~14 MHz`.

Neither is a historical release criterion.

## Singulation/package

- low-force ~1-cm-class brittle-II–VI singulation capability with edge/subsurface/function qualification;
- 77–80 K package/Dewar operation;
- measured bondline/interconnect/optics/vacuum/thermal state;
- repeated thermal cycling.

---

# What can be commissioned without HgCdTe

Before consuming HgCdTe, a future lab can close:

- mass metrology;
- LPE dimensions/motion/thermal/gas calibration;
- anneal thermal/enclosure commissioning;
- FTIR/Hall instrument validation;
- spin/bake/dose/CD calibration;
- anodization electronics/cell geometry;
- RIE gas/pressure/RF/self-bias/thermal reproducibility;
- evaporator QCM/witness/thermal calibration;
- cryogenic electrical/radiometric/noise/temporal transfer functions;
- singulation mechanics;
- package vacuum/thermal/electrical infrastructure;
- data/genealogy system.

Surrogate success never substitutes for HgCdTe-specific response qualification.

---

# High-value permanent process rules

## LPE

- Composition is not charge mass.
- Never area-scale another lab's LPE charge.
- `M_charge` comes from actual measured boat capacity/meniscus/geometry.
- Auxiliary Hg/HgTe source inventory is separate.
- `T_controller != T_solution` until calibrated.
- Do not average incompatible supercooling/contact/wipe branches into one recipe.

## Hg anneal

- `250 °C in Hg` is incomplete without enclosure/source/Ts/THg/cooldown.
- Hg saturation is a boundary condition, not a universal gram amount.
- Isothermal and two-temperature branches are distinct.
- Final Hall/optical state releases the process, not time alone.

## Wet mesa / lithography

- Unspecified bromine percentage basis is not executable.
- `2% Br2`, `3:1 EG:HBr`, and HBr assay remain historically open.
- Matching 2.78 µm/min does not prove chemistry identity.
- Mask-1 and Mask-2 are different functional processes.
- Same commercial resist name across decades does not prove formulation equivalence.
- P28->P25 is a timed surface-state trajectory.
- No default ultrasonics.

## Anodic oxide

- Equal oxide thickness does not imply equal interface state.
- Current density uses measured electrochemically exposed area.
- Carbon-cathode TI branch and later Pt-cell branch are distinct.

## RIE

- Watts are not ion energy.
- Physical etch depth != electrical conversion depth.
- Separate oxide clear from semiconductor exposure.
- 64 sccm/100 mTorr/50 W/60 s is not reactor equivalence.
- Derived 10.6667/53.3333-sccm split is a candidate, not direct historical MFC evidence.

## Cr/Au

- No undocumented clean between qualified RIE and Cr.
- RP-01 load-lock language is proposed capability, not proof of zero historical air break.
- Thermal evaporation is a method-family candidate only.
- Cr and Au QCM calibration remain separate unless measured equivalence supports otherwise.
- Holder temperature is not automatically wafer temperature.

## Detector metrology

- Use measured fabricated geometry for field/area/D*.
- FOV angle is not radiometric geometry.
- Analyzer display is not detector-terminal ASD without transfer/ENBW calibration.
- System bandwidth is not detector bandwidth before de-embedding.
- Low average optical power does not prove low injection.
- Package thermal poles are not carrier lifetime by default.

## Singulation/package

- Visible edge damage != subsurface/functional damage.
- Deep bulk-CdZnTe post-saw etches are not automatically compatible with the completed detector.
- Non-contact laser separation is not chemically inert by assumption.
- Die attach/bondline/interconnect/package thermal state are detector variables.
- P33 cryogenic survival feeds back to P35 release.

---

# EH&S boundary

Repository procedures do not replace institution-specific controls for Hg/Cd/Br2/HBr/H2/CH4, toxic-metal waste, high temperature, sealed ampoules, vacuum/RF, solvents, cryogens or electrical hazards.

`SCIENTIFICALLY-CAPABLE != FACILITY-AUTHORIZED`.

---

# Readiness after Round 41

Formal P16A row states remain unchanged.

The project is now:

**branch-selected + laboratory-capability-specified + not physically instantiated**.

No actual tool/model/lot/calibration has been supplied. Therefore P16C is not complete and P16A remains NO.

---

# Active archival targets

Still useful only if a genuinely new access path appears:

- Vanya Srivastav IISc thesis `G25544.pdf`;
- John Kenion White 2005 UWA thesis;
- J. F. Siliquini UWA thesis;
- Ryan Westerhout UWA thesis;
- Redfern/Musca/Smith/Dell/Faraone 1999 TPCD full text;
- Musca/Smith/Dell/Faraone 1999 contact/passivation full traveler;
- Smith et al. 2000 in-situ vacuum-processing full traveler;
- Fermionics/Honeywell dimensioned LPE records;
- exact UWA Mask-1/Mask-2/anodization/RIE-gas/Cr-Au/package travelers;
- Optronics/HP35665A historical calibration/acquisition records;
- device notebook identifying exact performance contact pair.

Do not repeatedly rediscover these titles and treat that as progress.

---

# Next logical work — Round 42

Proceed with procurement-neutral **subsystem acceptance-test specifications**, beginning with the highest-risk upstream infrastructure:

1. LPE furnace/boat/gas/actuator acceptance test;
2. Hg anneal enclosure/thermal-zone acceptance test;
3. integrated 80-K detector-station uncertainty/transfer budget;
4. RIE MFC/pressure/RF/self-bias/oxide-clear acceptance test;
5. Cr/Au QCM/vacuum/thermal acceptance test.

For each define test artifact, raw data, calculation, pass/fail/conditional logic, HgCdTe-only residuals and recalibration/change-control triggers.

Do not select commercial vendors unless explicitly requested.
