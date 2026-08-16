# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 40  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** executable by a competent researcher without undocumented tribal knowledge.

Canonical first process:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**.

---

# Continuity preservation

This is the current condensed front door. Detailed older rules remain recoverable from Git history and the round checkpoints/source ledgers.

Useful preserved AGENTS states:

- pre-Round-39 detailed head: `2f46f251b4b6f6655197779a1694078fc333f860`, AGENTS blob `18f193b5442bf4b916611f33c4bdb3da463d6145`;
- Round-39 condensed AGENTS blob: `24b87adcf096ba487a1a8873ec0bf3db7dfae6b6`.

Do not delete historical checkpoints/source ledgers merely because this file is condensed.

---

# Current checkpoint — READ FIRST

Latest:

`research/2026-08-16_checkpoint_after_first_qualification_build_integration_round40.md`

Then:

- `research/2026-08-16_checkpoint_after_lithography_documentary_limit_round39.md`
- `research/2026-08-16_checkpoint_after_cr_au_deposition_round38.md`
- `research/2026-08-16_checkpoint_after_rie_gas_anodization_round37.md`
- `research/2026-08-16_checkpoint_after_wet_mesa_chemistry_round36.md`
- `research/2026-08-16_checkpoint_after_lpe_absolute_charge_round35.md`
- `research/2026-08-16_checkpoint_after_first_build_readiness_round34.md`
- older checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND40.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND40.md`
- then Round39/38/etc.

New Round-40 integration register:

`travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`.

---

# Maturity labels — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — one complete build can be executed without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — historical identity is sufficiently closed to claim reproduction of the Smith et al. process itself.
3. `REPRODUCIBLE-RELEASE` — repeated stability/MSA/capability/yield/change-control/performance evidence exists.

Current:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`

P16A is authoritative for readiness. P16B is authoritative for the current **preferred candidate branch architecture**. A P16B selection does not automatically change a P16A row state.

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
- `candidate branch != LOCAL-BRANCH-FROZEN != historical identity`.
- Values that depend on the actual tool—well volume, furnace gradient, MFC calibration, sheath state, QCM tooling factor, sample temperature, view factor, bondline geometry—are local physical quantities, not literature gaps.

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

Physical/process/metrology modules remain P01–P35 as previously documented.

Integration layer now includes:

- P16 master traveler;
- P16A first-build/release-readiness audit + 36-row register;
- **P16B first-qualification-build candidate branch register**;
- P17 release/capability;
- P18 failure analysis;
- P19/P20 requirements/sensitivity;
- P21/P22/P23 empirical modeling/DOE/state-boundary support.

Do not create a new physical SOP when an existing module already contains the closure method.

---

# Round-40 preferred candidate architecture

P16B currently selects the following evidence-ranked first-screen architecture:

1. `Cd0.96Zn0.04Te (111)B` as the preferred substrate family, with actual lot/size/plane/miscut still local;
2. P29 LPE-compatible Br2/methanol final-surface family, but no invented concentration basis;
3. Honeywell covered graphite horizontal-slider LPE topology;
4. composition center `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`;
5. after local `M_charge` selection: `w_Hg=.249740`, `w_Cd=.012502`, `w_Te=.737758`;
6. N2 purge -> flowing H2 atmosphere family;
7. Hg anneal first screen `250 °C / 1 h / Hg-saturated`, released only from P05/P06 final state;
8. Mask-1 historical product screen = AZ4620 3-µm Br2/HBr transfer branch, with no assumption modern AZ P4620 is equivalent;
9. wet mesa centered on Srivastav `2% Br2 / 3:1 EG:HBr`, ~21 °C, ~2.78 µm/min, A~.63, best RMS ~2 nm, while percentage/ratio bases remain open;
10. anodization centered on TI: 0.1 mol KOH per stated 1 L of 90% EG / 10% DI-water solvent, carbon cathode, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å/deep blue; solvent-ratio basis remains open;
11. direct RP-01 Mask-2 functional state: 4–5 µm / 80 °C 30 min / chlorobenzene 30 min;
12. RIE same-lineage gas candidate 1:5; with total 64 sccm gives derived `10.6667 sccm CH4 / 53.3333 sccm H2`;
13. Cr/Au direct 30/270 nm; thermal evaporation = strongest same-UWA method-family candidate;
14. low-force wire-saw family = first singulation screen; do not transplant the 5% Br/methanol bulk-damage-removal clean;
15. compliant silicone-family attachment = first package-attach screen;
16. P10–P13 use one explicitly matched detector/contact/package/T/field/background state.

These are candidate centers/families, not a released build.

---

# High-value process rules retained

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
- Same-SSPL v/v usage supports a candidate convention only.
- Matching 2.78 µm/min does not prove chemistry identity.
- Mask-1 and Mask-2 are different functional processes.
- Same commercial resist name across decades does not prove formulation equivalence.
- P28->P25 is a timed surface-state trajectory.
- No default ultrasonics.

## Anodic oxide

- Equal oxide thickness does not imply equal interface state.
- Current density uses measured electrochemically exposed area.
- Carbon-cathode TI branch and later Pt-cell branch are distinct.
- P25A method existence does not close R15.

## RIE

- Watts are not ion energy.
- Physical etch depth != electrical conversion depth.
- Separate oxide clear from semiconductor exposure.
- 64 sccm/100 mTorr/50 W/60 s is not reactor equivalence.
- Derived 10.6667/53.3333-sccm split is a local candidate, not direct historical MFC evidence.

## Cr/Au

- No undocumented wet/plasma/ion clean between qualified RIE and Cr.
- RP-01 load-lock language is proposed architecture/capability, not proof of zero historical air break.
- Thermal evaporation is a method-family candidate only.
- Cr and Au thickness/QCM calibration remain separate unless measured equivalence supports otherwise.
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

# Readiness after Round 40

Formal P16A row states remain unchanged.

Dominant unresolved local groups:

1. substrate lot/crystallography;
2. executable final pre-LPE surface;
3. dimensioned LPE hardware;
4. total charge + Hg source;
5. LPE gas/thermal/contact realization;
6. FTIR/Hall implementation;
7. anneal enclosure/Ts/THg;
8. Mask-1 implementation;
9. explicit wet-etch chemistry basis + handoff;
10. anodization basis/cell/area;
11. Mask-2/lift-off implementation;
12. RIE gas manifold/reactor/sheath/oxide clear;
13. Cr/Au evaporator/vacuum/QCM/rates/thermal state;
14. CD/TLM/bias/radiometry/noise/temporal instruments;
15. singulation tool/protection/clean/street;
16. package attach/interconnect/optical/vacuum construction;
17. package survival;
18. later SPC/yield.

P16B groups these into twenty irreducible local identity/calibration categories in more detail.

---

# Active archival targets

Still useful if a genuinely new access path appears:

- Vanya Srivastav IISc thesis `G25544.pdf` — identified, current route 403;
- John Kenion White 2005 UWA thesis — identified, current route 403;
- J. F. Siliquini UWA thesis;
- Ryan Westerhout UWA thesis;
- Redfern/Musca/Smith/Dell/Faraone 1999 TPCD full text;
- Musca/Smith/Dell/Faraone 1999 contact/passivation full traveler;
- Smith et al. 2000 in-situ vacuum-processing full traveler;
- Fermionics/Honeywell dimensioned LPE records;
- exact UWA Mask-1/Mask-2/anodization/RIE-gas/Cr-Au/package travelers;
- Optronics/HP35665A historical calibration/acquisition records;
- device notebook identifying the exact performance contact pair;
- supplier/UWA record identifying historical x/thickness measurement methods.

Do not repeatedly rediscover these titles and treat that as progress.

---

# Strategic state after Round 40

The project is now largely **branch-selected but not laboratory-instantiated**.

Broad historical process-family searching has diminishing return. The strongest analytical work is to convert the P16B local blanks into physics-based minimum apparatus/consumable/calibration specifications that a future laboratory can populate directly.

Because the user cannot perform real-life experiments in this project, never invent local measurement results. Build requirement sheets, calibration plans, witness strategies and acceptance logic instead.

---

# Next logical work — Round 41

Proceed with a **minimum laboratory capability / implementation specification package** derived from P16B.

Create at minimum:

`docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`

and, if useful, a controlled fill-in register/traveler.

For each critical capability define:

1. required physical function;
2. minimum range/capability implied by the selected P16B branch;
3. procurement/selection fields that must be known;
4. calibration required before HgCdTe is consumed;
5. non-HgCdTe witness/surrogate commissioning that is scientifically valid;
6. values that cannot be set until the actual tool is present;
7. downstream module/gate dependencies;
8. separate institutional EH&S/facility dependency.

Prioritize:

- LPE furnace/boat/gas/actuator;
- Hg anneal furnace/ampoule/reservoir;
- FTIR and Hall;
- lithography;
- RIE;
- Cr/Au deposition;
- 77–80-K electrical/optical/noise/temporal test infrastructure;
- singulation;
- package/Dewar.

Do not shop for commercial tools or choose vendors unless explicitly asked. Define the physics-based capability envelope first.