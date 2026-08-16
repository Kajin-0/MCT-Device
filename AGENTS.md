# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 39  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** executable by a competent researcher without undocumented tribal knowledge.

Canonical first process:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**.

---

# Continuity preservation

This file is the current front-door summary. The complete pre-Round-39 rule set remains permanently available in Git history:

- Round-38 head: `2f46f251b4b6f6655197779a1694078fc333f860`
- `AGENTS.md` blob at that state: `18f193b5442bf4b916611f33c4bdb3da463d6145`

If a subtle older rule is needed, inspect that historical AGENTS revision plus the relevant checkpoint rather than reconstructing it from memory.

**Do not delete or rewrite historical checkpoints/source ledgers merely because this front-door file is condensed.** They are the detailed audit trail.

---

# Current checkpoint — READ THIS FIRST

Latest:

`research/2026-08-16_checkpoint_after_lithography_documentary_limit_round39.md`

Then, as needed:

- `research/2026-08-16_checkpoint_after_cr_au_deposition_round38.md`
- `research/2026-08-16_checkpoint_after_rie_gas_anodization_round37.md`
- `research/2026-08-16_checkpoint_after_wet_mesa_chemistry_round36.md`
- `research/2026-08-16_checkpoint_after_lpe_absolute_charge_round35.md`
- `research/2026-08-16_checkpoint_after_first_build_readiness_round34.md`
- `research/2026-08-16_checkpoint_after_singulation_round33.md`
- `research/2026-08-16_checkpoint_after_ftir_composition_thickness_round32.md`
- `research/2026-08-16_checkpoint_after_temporal_deembedding_round31.md`
- `research/2026-08-16_checkpoint_after_bias_network_round30.md`
- `research/2026-08-16_checkpoint_after_noise_chain_round29.md`
- `research/2026-08-16_checkpoint_after_radiometry_round28.md`
- older checkpoints for detailed fabrication genealogy.

Latest source/gap addenda:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND39.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND39.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND38.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND38.md`
- older addenda as needed.

---

# Maturity labels — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — one complete build can be executed without undocumented irreversible choices, including explicitly local transfer branches where historical identity is unavailable.
2. `HISTORICAL-RP01-REPRODUCED` — historical identity/source closure is sufficient to claim the Smith et al. process itself was reproduced.
3. `REPRODUCIBLE-RELEASE` — repeated stability/MSA/capability/yield/change-control/performance evidence exists.

Current status:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`

P16A and its 36-row readiness register are authoritative. The weakest mandatory coordinate controls first-build disposition.

---

# Non-negotiable provenance / scientific rules

## Evidence discipline

- Never invent a missing number.
- Use explicit states such as `OPEN`, `OPEN-HISTORICAL`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, `IDENTIFIED-NOT-RECOVERED`, `DERIVED`, or a named evidence class.
- Separate direct RP-01, same-lineage, transfer-family, model, derived, apparatus-calibration and local-qualification evidence.
- Repetition does not promote evidence class.
- “Not recovered” does not mean “does not exist.”
- Preserve negative searches, rejected inferences, source conflicts and failed branches.
- Empirical/practical primary literature comes before theoretical placeholders.
- Theory may sanity-check or bridge a genuine gap; it does not manufacture process settings.
- Do not splice incompatible process generations into a fictitious published recipe.
- A controlled closure method is not the same thing as a physically closed readiness row.

## Geometry / measurement discipline

- Use measured fabricated geometry for field, active area and D* normalization.
- Keep Hall quantities, optical edges, physical etch depth, electrical conversion depth, sheet density, `rho_c`, minority blocking, package response and detector response distinct.
- Measured system bandwidth is not detector bandwidth before de-embedding.
- A fitted decay is not automatically carrier lifetime.
- Specifications derive from downstream performance, not merely observed process spread.
- Repeated observations from one melt/source/bath/substrate/chamber/tool/package genealogy are not iid replicates.

## Process-state discipline

Treat these as first-class variables, not operator trivia:

- incoming surface state;
- clean-to-next-step delay and ambient;
- LPE source/use genealogy;
- anneal cooldown and Hg boundary state;
- wet-etch bath age/agitation/temperature;
- P28->P25 handoff;
- P25->lithography handoff;
- post-RIE exposure;
- RIE chamber clean/season/loading state;
- RIE->Cr transfer history;
- Cr->Au vacuum history;
- lift-off/strip history;
- singulation consumable/tool state;
- package assembly and thermal-cycle genealogy.

## Failure-analysis discipline

Use:

`signature -> competing mechanisms -> discriminating tests -> root cause -> CAPA -> verification`.

Do not diagnose all post-process noise/responsivity changes as one familiar mechanism.

## EH&S

Repository procedures do not replace institution-specific controls for Hg/Cd/Br2/HBr/H2/CH4, high temperature, pressure/vacuum, solvents, high voltage, cryogens or toxic-metal contamination.

---

# Canonical RP-01 direct anchors — do not drift

## Material

- LPE n-HgCdTe on electrically insulating CdZnTe.
- nominal `x≈0.30`.
- supplier `n≈9.8×10^14 cm^-3`.
- supplier `mu≈4.0×10^4 cm²/V·s`.
- active layer thickness `9.5 µm`.
- historical methods used to establish x and thickness remain open.

## Passivation / lithography / RIE / metal

- native anodic oxide `~800 Å = 80 nm`.
- Mask-1: photolithographic wet-mesa delineation; commercial resist/process not disclosed.
- Mask-2: `4–5 µm` resist; prebake `80 °C / 30 min`; chlorobenzene `30 min`; then patterned/developed/water rinse.
- same Mask-2 resist survives RIE and supports Cr/Au lift-off.
- RIE: Plasma Technology parallel-plate; printed `CH4/5H2`; total `64 sccm`; `100 mTorr`; `50 W`; `60 s`.
- converted average n-type density ~`2.0×10^15 cm^-3`; mobility ~`3.3×10^4 cm²/V·s`.
- Cr `30 nm`; Au `270 nm`.
- nine contacts approximately `300×300 µm`; gaps 50–400 µm in 50-µm increments.
- `rho_c≈9×10^-4 Ω·cm²` at 80 K.

## Detector / radiometry / noise

- operating temperature ~80 K for key reported data.
- stated 60° FOV.
- spectral response chopped at 1 kHz.
- field is contact-to-contact voltage bias divided by active gap.
- Figure-3 sweep roughly 0–50 V/cm; Figures 5–7 use 10 V/cm.
- Figures 3/5/6/7 are the same physical detector; exact contact pair/gap is open.
- detector cutoff reported ~4.4 µm; exact cutoff convention is open.
- BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm.
- quoted QE ~70%.
- low-noise preamp + HP35665A.
- 1/f knee ~3 kHz.
- high-frequency g-r level ~24.5 nV/sqrtHz.
- **24.5 nV/sqrtHz is not the historical 1-kHz noise value.**
- no direct RP-01 lifetime/f3dB curve has been recovered.

---

# Controlled module architecture

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP
- P06 FTIR composition/thickness + P06A apparatus/model/cutoff lineage + register
- P07 CdZnTe + P07A/P07B/P07C
- P08 RIE blocking contact + P08A–P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating + P10A bias/load transfer + register
- P11 absolute radiometry/responsivity + P11A transfer + register
- P12 noise/PSD/NEP/D* + P12A/P12B/P12C + register
- P13 temporal/frequency response + P13A UWA TPCD/de-embedding + register
- P14 lithography/CD + P14A chlorobenzene lineage
- P15 cryogenic package framework
- P16 master traveler + P16A first-build/release-readiness audit + 36-row register
- P17 statistical release/capability + P17A package/singulation change control
- P18 failure analysis/CAPA + P18A package/edge extension
- P19 requirements traceability
- P20 analytical sensitivity / requirements allocation
- P21 LPE empirical Jacobian
- P22 information-optimal DOE
- P23 Hg-anneal state boundary / local Jacobian
- P24 blocking-contact empirical window + register
- P25 anodic-oxide empirical window + P25A cell/electrolyte instantiation + registers
- P26 Cr/Au empirical window + P26A deposition-apparatus instantiation + registers
- P27 Mask-2 empirical lithography/lift-off window + register
- P28 wet-mesa empirical window + P28A chemistry-definition/handoff closure + registers
- P29 CdZnTe/final-surface empirical window + register
- P30 Te-rich LPE execution + P30A absolute-charge/apparatus calibration + registers
- P31 Hg-overpressure anneal apparatus/reservoir/trajectory + register
- P32 Mask-1/wet-mesa lithography empirical window + register
- P33 cryogenic die-attach/interconnect/package empirical window + register
- P34 CH4/H2 RIE reactor-equivalence empirical window + register
- P35 HgCdTe/CdZnTe singulation/die-edge empirical window + register

Rounds 28–32 mainly strengthened existing methods. Round 33 created P35. Rounds 34–38 added integration/calibration/instantiation layers. Round 39 deliberately added **no new physical-process module** because P27 and P32 were already method-complete.

---

# High-value permanent process rules

## Wet mesa / lithography

- Wet-etch percentage without an explicit basis is not executable.
- Never guess Srivastav `2% Br2` basis.
- Same-SSPL `v/v` bromine usage supports `CANDIDATE-VV-SAME-LAB` only; other primary HgCdTe sources explicitly use `w/w` conventions.
- `3:1 EG:HBr` basis and HBr stock assay remain historically open.
- Matching ~2.78 µm/min does not prove chemistry identity.
- Wet-mesa endpoint is measured through-layer isolation/profile, not time alone.
- P28->P25 is a timed surface-state trajectory.
- Mask-1 and Mask-2 have different functions; never copy Mask-2's 4–5 µm/chlorobenzene recipe into Mask-1 by convenience.
- Mask-2 chlorobenzene establishes a positive diazo/DNQ-novolak lift-off lineage but not a product identity.
- Preserve RP-01 wording/order; do not silently reorder chlorobenzene to match a familiar fab recipe.
- Resist product/profile changes reopen wet-etch bias or lift-off equivalence.
- No default ultrasonics for strip/lift-off.

### Round-39 lithography documentary limit

- P27 is already the controlled Mask-2 local closure method; do not create another addendum unless new evidence adds a genuinely missing coordinate.
- P32 is already the controlled Mask-1 local closure method; do not create another addendum merely because historical identity remains open.
- John White 2005 UWA thesis PDF is officially identified but currently returns 403 through the available retrieval path: `IDENTIFIED-NOT-RECOVERED`.
- Srivastav 2005 full primary text does not identify the photoresist product, actual resist thickness, spin, bake, exposure, developer or strip.
- `CN101740502B` remains the strongest product-identified Br2/HBr HgCdTe Mask-1 transfer: AZ4620, 3 µm in that embodiment.
- Current commercial AZ P4620 documentation places normal film thickness substantially higher (~5–30 µm). **Same product name across decades does not establish formulation/process equivalence.** A current lot is a new local branch.
- R12, R16 and R21 therefore remain physical branch-selection problems, not missing-procedure problems.

## LPE

- LPE composition is not absolute charge mass.
- Honeywell xL=.082 / yL=.810 / TL=507 °C / xS≈.29 closes a tie-line/composition center, not grams.
- `V_well`, plug displacement, usable hot volume, `M_charge`, melt depth, overlap area and auxiliary Hg-source mass are distinct.
- Do not area-scale Radhakrishnan's ~4.8-g charge / 3-g HgTe reservoir into Honeywell/Fermionics.
- P30A method existence does not close R04–R07; actual hardware/charge/gas/trajectory must be instantiated.

## Hg anneal

- `250 °C in Hg` is not a complete recipe.
- Preserve `T_s(t)`, `T_Hg(t)`, source identity/geometry, boundary state and cooldown.
- Isothermal and two-temperature branches are distinct.
- Hg saturation is a boundary condition, not a universal gram amount.
- Do not transfer multi-day bulk kinetics onto a 9.5-µm epilayer without final-state measurement.

## Anodic oxide

- Equal oxide thickness does not imply equal interface state.
- TI US3977018 provides a strong photoconductor transfer center: 0.1 mole KOH per liter of stated 90% EG / 10% DI-water solvent, HgCdTe anode, carbon-rod cathode, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å/deep blue.
- The source does not explicitly resolve the 90:10 basis; keep it open.
- Do not splice the earlier carbon-cathode photoconductor process with the later Pt horizontal-cell apparatus into one published recipe.
- Current density uses measured electrochemically exposed area: `I=J A_exposed`.
- P25A method existence does not close R15.

## RIE

- RIE watts are not ion energy.
- Keep physical etch depth, electrical conversion depth and lateral conversion distinct.
- Separate oxide-clear time from semiconductor-exposure time.
- Matching `64 sccm / 100 mTorr / 50 W / 60 s` is not reactor equivalence.
- Direct UWA sources still print `CH4/5H2` without separate MFC values.
- Same-lineage 1:5 decoding + direct 64-sccm total yields candidate 10.6667/53.3333-sccm CH4/H2 only; never call them direct RP-01 MFC values.
- Do not repeat generic gas-ratio searches absent a genuinely new source family.

## Cr/Au

- No undocumented wet clean, ion mill or plasma clean between qualified P08 and Cr.
- RP-01 load-lock wording is `DIRECT-RP01-PROPOSED-ARCHITECTURE`, not proof the measured devices had zero air break.
- Same-UWA 1998 angled thermal evaporation makes thermal evaporation a strong method-family candidate, not exact RP-01 identity.
- Do not copy the same-UWA deposition angle into RP-01 lift-off geometry.
- Historical RP-01 tool, base pressure, Cr/Au rates, source hardware, QCM, wafer temperature and lift-off chemistry remain open.
- Cr and Au tooling-factor/thickness calibration are separate unless measured equivalence supports otherwise.
- Do not copy an Au rate to Cr.
- Holder temperature is not automatically wafer temperature.
- P26A method existence does not close R20; an actual apparatus register must reach `P26-APPARATUS-READY`.

## Metrology / detector state

- P06: keep physical thickness, FTIR thickness, optical edge, Hansen-equivalent bandgap/composition and detector cutoff distinct.
- Hansen x=.300 at 80 K vs a 4.4-µm hc/lambda equivalent is a consistency comparison only; never back-fill a new measured x.
- P10 field uses measured detector-contact voltage and measured active gap.
- P11 FOV angle is not radiometric geometry; controller temperature is not automatically radiance temperature.
- P12 analyzer output is not detector-terminal ASD until the full electrical transfer/ENBW normalization is calibrated.
- P13 low average optical power does not prove low injection; source/electrical/package transfer must be de-embedded.
- Package thermal poles are not detector lifetime by default.

## Singulation / package

- P35 owns finished-device singulation; P33 owns package construction.
- Visible edge damage, functional damage and released edge exclusion are distinct.
- No visible chip does not prove no subsurface damage.
- Deep bulk-CdZnTe bromine damage-removal etches are not automatically compatible with a finished ~9.5-µm HgCdTe device stack.
- Laser/non-contact singulation is not chemically inert by assumption.
- Mechanical yield is not detector functional yield.
- Die attach/bondline/interconnect/package thermal state are detector variables.
- P33 cryogenic edge-survival results feed back to P35 release.

---

# Current first-build readiness highlights

Full authoritative table: `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`.

Key open rows after Round 39:

- R01 source-element inventory — `OPEN-CHOICE`
- R02 CdZnTe composition/face/miscut — `OPEN-CHOICE`
- R03 final CdZnTe surface — `OPEN-CHOICE`
- R04 LPE apparatus — `APPARATUS-NOT-SELECTED`
- R05 LPE absolute charge — `OPEN-CHOICE`
- R06 LPE atmosphere — `OPEN-CHOICE`
- R07 LPE trajectory — `OPEN-CHOICE`
- R08 FTIR — `METROLOGY-NOT-IMPLEMENTED`
- R09 Hall — `METROLOGY-NOT-IMPLEMENTED`
- R10 anneal enclosure — `APPARATUS-NOT-SELECTED`
- R11 anneal trajectory — `OPEN-CHOICE`
- R12 Mask-1 — `OPEN-CHOICE`
- R13 wet-mesa chemistry basis — `UNDEFINED-BASIS`
- R14 wet-mesa endpoint/handoff — `OPEN-CHOICE`
- R15 anodization — `OPEN-CHOICE`
- R16 Mask-2 — `OPEN-CHOICE`
- R17 RIE gas realization — `UNDEFINED-BASIS`
- R18 RIE reactor — `APPARATUS-NOT-SELECTED`
- R19 oxide clear/semiconductor exposure — `OPEN-CHOICE`
- R20 metallization apparatus — `APPARATUS-NOT-SELECTED`
- R21 lift-off — `OPEN-CHOICE`
- R22–R27 detector/metrology implementations — `METROLOGY-NOT-IMPLEMENTED`
- R28–R33 singulation/package choices — `OPEN-CHOICE`
- R34 cryogenic package survival — `RELEASE-DATA-OPEN`
- R35 genealogy — conceptually `LOCAL-BRANCH-FROZEN`
- R36 SPC/yield — `RELEASE-DATA-OPEN`.

Round 39 does not promote R12/R16/R21. P27/P32 existing is a closure method, not physical branch selection.

---

# Active high-value unrecovered sources

- Vanya Srivastav IISc thesis `G25544.pdf` — official file identified; current route returns 403.
- John Kenion White 2005 UWA thesis PDF — official download identified; current route returns 403.
- J. F. Siliquini UWA thesis full experimental appendices.
- Ryan Westerhout 2013 UWA thesis full experimental text.
- Redfern/Musca/Smith/Dell/Faraone 1999 TPCD proceedings full text.
- Musca/Smith/Dell/Faraone 1999 contact/passivation full experimental text.
- Smith et al. 2000 in-situ vacuum-processing proceedings full experimental text.
- Honeywell/Fermionics dimensioned LPE travelers / absolute charge records.
- exact UWA Mask-1/Mask-2 cleanroom traveler.
- exact RP-01 anodization traveler.
- exact RP-01 gas-delivery/MFC record.
- exact RP-01 Cr/Au deposition/lift-off traveler.
- exact RP-01 package/singulation traveler.
- exact RP-01 Optronics calibration and HP35665A acquisition record.
- original device notebook identifying performance contact pair/current/resistance.
- supplier/UWA certificate identifying the historical x/thickness measurement method.

Do not repeatedly rediscover these titles and treat that as progress. Reopen them when a genuinely new archival access route appears.

---

# Strategic transition after Round 39

The project has reached **documentary saturation for several execution blockers**.

For many rows, the repository now answers:

> “How should a competent laboratory define and qualify this missing coordinate?”

but the row remains open because the laboratory has not supplied the actual tool/product/reagent geometry.

Examples:

- P30A knows how to close LPE apparatus/charge, but no actual boat/tool exists in the repo.
- P28A knows how to define wet chemistry, but no actual local chemistry basis/stock assay is selected.
- P25A knows how to instantiate anodization, but no actual cell/reagents are selected.
- P26A knows how to instantiate metallization, but no actual evaporator/source/vacuum chain is selected.
- P27/P32 know how to qualify lithography, but no actual commercial resist/aligner/developer branch is selected.
- P34 knows how to qualify RIE equivalence, but no actual reactor/manifold is selected.

**Do not respond to this state by generating endless new addenda.** The next research phase is systems integration and branch selection.

---

# Next logical work — Round 40

Proceed with **first-qualification-build branch integration / documentary-saturation audit**.

Goal:

Construct one coherent, source-traceable **literature-defined candidate first-build branch matrix** over the 36 P16A coordinates.

Round 40 should:

1. classify each unresolved row as:
   - `DIRECT-RP01-EXECUTABLE`;
   - `PUBLISHED-TRANSFER-CENTER-AVAILABLE`;
   - `LOCAL-TOOL-IDENTITY-REQUIRED`;
   - `LOCAL-MATERIAL/CONSUMABLE-IDENTITY-REQUIRED`;
   - `LOCAL-CALIBRATION/QUALIFICATION-REQUIRED`;
   - `HISTORICAL-IDENTITY-ONLY`;
2. choose one defensible published transfer center for each row where such a center genuinely exists;
3. include exact numerical values only when the cited source actually gives them;
4. label every non-RP01 selection as a candidate/local transfer branch;
5. identify the **irreducible laboratory-specific blanks** that literature cannot supply;
6. create a master first-qualification-build candidate branch register rather than another physical-process SOP;
7. check cross-module compatibility, especially P28->P25, P25->P27, P27->P08, P08->P26, P26->P35/P33, and shared P10–P13 state;
8. calculate arithmetic consequences only after branch selection and label them `DERIVED`;
9. do not change P16A readiness states unless the P16A definition is genuinely met;
10. update source/gap/checkpoint/AGENTS.

The objective is to move from:

**“we know how a future lab would close every row”**

toward:

**“this is the strongest coherent first qualification build supported by the published record, and these are the smallest irreducible laboratory-specific blanks.”**
