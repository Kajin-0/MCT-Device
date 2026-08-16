# AGENTS.md — MCT-Device front-door continuity record

**Current continuity round:** 42  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual/booklet executable by a competent researcher without undocumented tribal knowledge.

Canonical first process:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is no end-to-end reproducible release yet.

---

# READ FIRST

Latest checkpoint:

`research/2026-08-16_checkpoint_after_subsystem_acceptance_round42.md`

Then:

- `research/2026-08-16_checkpoint_after_minimum_lab_capability_round41.md`
- `research/2026-08-16_checkpoint_after_first_qualification_build_integration_round40.md`
- Round39/38/37/36/35/34 checkpoints as needed.

Latest source/gap:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND42.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND42.md`

Current integration/control registers:

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`
- `travelers/P16C_MINIMUM_LAB_CAPABILITY_IMPLEMENTATION_REGISTER.md`
- `travelers/P16D_SUBSYSTEM_ACCEPTANCE_REGISTER.md`
- `travelers/P16D1_SUPPORTING_METROLOGY_MICROFAB_ACCEPTANCE_REGISTER.md`

Current capability/acceptance architecture:

- `docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`
- `procedures/P36_LAB_SUBSYSTEM_COMMISSIONING_ACCEPTANCE.md`
- `procedures/P36A_SUPPORTING_METROLOGY_LITHOGRAPHY_WET_CHEMISTRY_ACCEPTANCE.md`

---

# Maturity / implementation states — never conflate

1. `TRACEABLE-FIRST-BUILD-READY` — complete build can execute without undocumented irreversible choices.
2. `HISTORICAL-RP01-REPRODUCED` — historical identity sufficiently closed to claim reproduction of Smith et al.
3. `REPRODUCIBLE-RELEASE` — repeated stability/MSA/capability/yield/change-control/performance evidence exists.
4. `P16C-INFRASTRUCTURE-READY` — actual laboratory infrastructure is identified/calibrated/commissioned to the P16C requirement.
5. `P16D-SURROGATE-COMMISSIONING-COMPLETE` — all possible non-HgCdTe IQ/OQ/surrogate-PQ acceptance work is complete for the selected infrastructure.

Current:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`
- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != local branch frozen != historical identity != reproducible release`.

---

# Permanent evidence discipline

- Never invent a missing number.
- Separate direct RP-01, same-lineage, transfer-family, derived, apparatus-calibration, local-qualification and acceptance evidence.
- Repetition does not promote evidence class.
- “Not recovered” does not mean absent.
- Preserve negative searches, rejected inferences, conflicts and failed branches.
- Empirical/practical primary literature precedes theoretical placeholders.
- Theory may check consistency; it does not manufacture process settings.
- Do not splice incompatible process generations into a fictional recipe.
- A controlled closure/acceptance method is not a physically closed readiness row.
- Engineering capability ranges are not historical process setpoints.
- Surrogate commissioning is not HgCdTe process equivalence.
- Configuration changes can invalidate calibration even before calendar expiration.

---

# Round-41 capability classes retained

- `HARD-MINIMUM`
- `FIRST-BUILD-ENGINEERING-ENVELOPE`
- `DESIGN-CHECK`
- `SURROGATE-COMMISSIONABLE`
- `HGCDTE-REQUIRED`
- `LOCAL-BLANK`
- `EH&S/FACILITY-GATE`

---

# Round-42 acceptance states

- `AT-NOT-STARTED`
- `AT-IQ-PASS`
- `AT-OQ-PASS`
- `AT-SURROGATE-PQ-PASS`
- `AT-HGCDTE-RESIDUAL-PENDING`
- `AT-HGCDTE-PASS`
- `AT-CONDITIONAL`
- `AT-FAIL`
- `AT-EH&S-BLOCKED`
- `AT-NOT-APPLICABLE`

New gap class:

`ACCEPTANCE-EVIDENCE-OPEN` — method defined; actual tool evidence absent.

Commissioning hierarchy:

`IQ -> OQ -> surrogate PQ -> HgCdTe residual qualification`.

---

# Canonical RP-01 anchors — do not drift

## Material

- LPE n-HgCdTe on insulating CdZnTe;
- nominal `x≈0.30`;
- supplier `n≈9.8×10^14 cm^-3`;
- supplier `mu≈4.0×10^4 cm²/V·s`;
- active layer ~9.5 µm.

## Passivation / lithography / RIE / metal

- anodic oxide ~800 Å = 80 nm;
- Mask-1 wet mesa; historical product/process open;
- Mask-2 4–5 µm;
- 80 °C / 30 min bake;
- chlorobenzene 30 min;
- same Mask-2 survives RIE and supports lift-off;
- RIE: Plasma Technology parallel plate, printed CH4/5H2, total 64 sccm, 100 mTorr, 50 W, 60 s;
- converted average n ~2.0×10^15 cm^-3, mobility ~3.3×10^4 cm²/Vs;
- Cr 30 nm / Au 270 nm;
- contacts ~300×300 µm;
- gaps 50–400 µm by 50 µm;
- `rho_c≈9×10^-4 Ω cm²` at 80 K.

## Detector state

- key data around 80 K;
- stated 60° FOV;
- spectral response chopped at 1 kHz;
- field = measured contact voltage / measured active gap;
- Figures 5–7 use 10 V/cm;
- cutoff ~4.4 µm;
- BLIP `D*≈2×10^11 cm Hz^1/2/W` at 4 µm;
- QE ~70%;
- historical 1/f knee ~3 kHz;
- high-frequency g-r ~24.5 nV/sqrtHz;
- 24.5 nV/sqrtHz is not the historical 1-kHz noise;
- RP-01 lifetime/f3dB remains open.

---

# Preferred candidate architecture retained

1. `Cd0.96Zn0.04Te (111)B` preferred substrate family; actual lot/size/plane/miscut local.
2. P29 Br2/methanol final-surface family; no invented concentration basis.
3. Honeywell covered graphite horizontal-slider LPE topology.
4. composition center `xL=.082`, `yL=.810`, `TL=507 °C`, `xS≈.29`.
5. N2 purge -> H2 atmosphere family.
6. Hg anneal first screen ~250 °C / 1 h / Hg-saturated-isothermal-like, released by P05/P06.
7. Mask-1 historical product screen AZ4620 transfer family; modern equivalence unproven.
8. wet mesa Srivastav center: `2% Br2 / 3:1 EG:HBr`, ~21 °C, ~2.78 µm/min, `A≈.63`, best roughness ~2 nm; bases open.
9. anodization TI center: 0.1 mol KOH per stated 1 L of 90% EG/10% DI-water solvent, carbon cathode, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å; solvent basis open.
10. Mask-2: 4–5 µm / 80 °C 30 min / chlorobenzene 30 min.
11. RIE candidate 1:5 CH4:H2; derived 10.6667/53.3333 sccm at total 64 sccm.
12. Cr/Au 30/270 nm; thermal evaporation strongest same-UWA method-family candidate.
13. low-force wire-saw first singulation screen.
14. compliant silicone-family first package-attach screen.
15. P10–P13 share one matched detector/contact/package/T/field/background state.

Candidate centers/families are not released build values.

---

# Authoritative LPE mass convention

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md` freezes:

- Hg 200.59 g/mol;
- Cd 112.414 g/mol;
- Te 127.60 g/mol.

For `xL=.082`, `yL=.810`:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

Later P30A/P16B rounded `0.249740/0.012502/0.737758` values are a controlled ppm-scale numerical erratum. Future calculations use the frozen values. Active P30A/P16B text should be normalized together when those large files are next revised.

`M_charge` remains apparatus-dependent.

---

# Round-42 acceptance architecture — key rules

## Universal measurement-discrimination rule

For a process decision interval `DeltaX_decision`:

- minimum logical requirement: `U_X < DeltaX_decision/2`;
- preferred engineering target where practical: `U_X <= DeltaX_decision/4`.

These are derived measurement-design criteria, not historical tolerances.

## LPE

Acceptance requires:

- dimensioned boat/capacity;
- hot motion;
- source/substrate thermal map around Round-41 ~495–520 °C engineering envelope;
- N2/H2 flow calibration;
- synchronized logging;
- actual HgCdTe liquidus/growth response as residual.

If a future branch needs to distinguish a ~2 °C supercooling difference, `U_DeltaT<1 °C` is minimum discriminability and ~<=0.5 °C is a preferred target.

## Hg anneal

- dimensioned enclosure;
- independent `T_s(t)` / `T_Hg(t)`;
- ~250–300 °C map;
- ~250 °C / 1 h dummy dwell;
- enclosure integrity;
- actual Hg/HgCdTe carrier-state response residual.

## FTIR

- ~500–5000 cm^-1;
- <=4 cm^-1 qualification resolution unless justified;
- baseline/repeatability;
- >=9-point map registration;
- independent ~5–15-µm thickness-reference capability;
- HgCdTe model validation residual.

## Hall

Calibrate actual B at sample through:

`0, ±.01, ±.025, ±.05, ±.10, ±.20, ±.50 T`.

±0.50 T hard minimum; ~±2 T preferred extension. Current/voltage reversal and Hall-reference surrogate required.

## Source weighing / dimensional metrology

- balance acceptance at actual element mass scales, especially Cd;
- propagate uncertainty into `xL/yL`;
- lateral geometry and vertical film/oxide/metal metrology must be independently calibrated.

## Lithography / wet mesa / anodization

- measured resist thickness, bake thermal state and exposure dose;
- 4–5-µm Mask-2 / 80 °C 30 min / chlorobenzene 30 min capability;
- wet-mesa concentration/ratio bases must become locally explicit before execution;
- anodization `A_exposed` measured and `I=J A_exposed`;
- current/voltage/time traceable;
- HgCdTe surface/interface behavior residual.

## RIE

Acceptance at candidate/direct state includes:

- CH4 10.6667 sccm;
- H2 53.3333 sccm;
- total 64 sccm;
- 100 mTorr;
- 50 W;
- 60 s;
- reflected power;
- self-bias/sheath proxy;
- sample thermal state;
- chamber genealogy;
- actual P25 oxide clear/HgCdTe electrical conversion residual.

`50 W != reactor equivalence`.

## Cr/Au

- independent Cr QCM/witness calibration around 30 nm;
- independent Au QCM/witness calibration around 270 nm;
- pressure/source/QCM/sample geometry and thermal state logged;
- sequential Cr->Au history;
- no arbitrary base-pressure criterion;
- HgCdTe TLM/contact residual.

## Integrated detector station

Acceptance as one system includes:

- 77–80 K thermal/vacuum state;
- DC/load terminal transfer;
- ~2–6 µm first-build radiometry envelope with 4-µm calibration and through/beyond ~4.4-µm edge;
- 1-kHz modulation;
- electronics PSD floor;
- Johnson-noise validation;
- temporal transfer at 1 kHz/10 kHz/100 kHz/1 MHz plus extension;
- package thermal kernel;
- matched-state metadata.

Noise design relation:

`e_elec <= 24.5 sqrt(beta) nV/sqrtHz` for PSD allocation fraction `beta`.

Example only: `beta=.10 -> 7.75 nV/sqrtHz`.

Temporal instrument-sizing check if 25-ns pulse branch is used:

`BW~0.35/25 ns~14 MHz`.

Neither is historical RP-01 release criterion.

## Singulation/package

Surrogate commissioning can close mechanical, thermal, optical, vacuum and interconnect infrastructure. Actual completed HgCdTe stack remains required for functional edge damage, cracks, noise/responsivity and detector/package thermal interaction.

---

# Critical handoffs — now explicit acceptance evidence

Must be timestamped/reconstructable:

- final CZT surface -> LPE;
- mesa -> anodization;
- anodization -> Mask-2;
- RIE -> Cr;
- Cr -> Au;
- singulation -> package;
- package -> P10–P13.

No critical elapsed time should depend on operator memory.

---

# EH&S

Repository procedures do not replace facility/institution-specific controls for Hg/Cd compounds, Br2/HBr, H2/CH4, high temperature/sealed ampoules, solvents/chlorobenzene, RF/vacuum, high voltage or cryogens.

An `AT-EH&S-BLOCKED` or P16C `EH&S-BLOCKED` state prevents physical execution regardless of scientific readiness.

---

# Strategic state after Round 42

The project is now:

**branch-selected + capability-specified + acceptance-method-specified + not physically instantiated**.

Generic historical searching has diminishing return unless a genuinely new archive/source family appears.

The next high-value work is quantitative uncertainty allocation across the acceptance interfaces using P20/P21/P22, not tighter arbitrary instrument specs.

---

# Next logical work — Round 43

Build an integrated **first-build uncertainty / requirements-allocation package**.

At minimum propagate:

1. charge-mass + thermal + FTIR/Hall uncertainty -> material state;
2. CD/geometry + voltage/current + temperature uncertainty -> E/R/self-heating/contact state;
3. radiometry + active area + noise-chain uncertainty -> responsivity/NEP/D*;
4. source/electrical/package transfer uncertainty -> detector `f3dB/tau`;
5. convert these budgets into quantitative acceptance targets only where a downstream detector-performance requirement justifies them.

Preserve model-conditional versus empirically required Jacobians. Do not manufacture missing sensitivities.