# Research checkpoint — after subsystem commissioning / acceptance architecture Round 42

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 42 began from the Round-41 conclusion that the project now has a procurement-neutral laboratory capability envelope but still lacks a controlled answer to:

> How does a future laboratory prove that each installed subsystem is trustworthy enough to begin HgCdTe process qualification?

The round therefore built an acceptance layer rather than performing more historical process-family searches.

No vendor was selected. No physical tool result was invented. No P16A readiness row was promoted.

---

## 2. New controlled artifacts

Created:

- `procedures/P36_LAB_SUBSYSTEM_COMMISSIONING_ACCEPTANCE.md`
- `procedures/P36A_SUPPORTING_METROLOGY_LITHOGRAPHY_WET_CHEMISTRY_ACCEPTANCE.md`
- `travelers/P16D_SUBSYSTEM_ACCEPTANCE_REGISTER.md`
- `travelers/P16D1_SUPPORTING_METROLOGY_MICROFAB_ACCEPTANCE_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND42.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND42.md`
- this checkpoint.

AGENTS is refreshed at the end of the round.

---

## 3. New integration concept — P16D

P16A/P16B/P16C/P16D now separate four questions:

1. **P16A:** is the complete first build ready to execute without undocumented irreversible choices?
2. **P16B:** which evidence-ranked process branch should be pursued?
3. **P16C:** does a real laboratory possess the required physical capability?
4. **P16D:** has that laboratory demonstrated, with controlled acceptance evidence, that the relevant subsystem transfer functions/controls are trustworthy?

New project-level commissioning label:

`P16D-SURROGATE-COMMISSIONING-COMPLETE`.

Permanent relation:

`P16D-SURROGATE-COMMISSIONING-COMPLETE = YES`

would mean the non-HgCdTe acceptance work is complete for the selected infrastructure, but it would **not** imply:

- `TRACEABLE-FIRST-BUILD-READY = YES`;
- `HISTORICAL-RP01-REPRODUCED = YES`;
- `REPRODUCIBLE-RELEASE = YES`.

---

## 4. Four-layer commissioning architecture

Round 42 formalized:

`IQ -> OQ -> surrogate PQ -> HgCdTe residual qualification`.

Where:

- **IQ** = installation/configuration/identity;
- **OQ** = calibrated operating range/control/measurement;
- **surrogate PQ** = end-to-end performance using non-HgCdTe standards/dummies/witnesses;
- **HgCdTe residual** = response that is intrinsically material/device dependent.

This resolves a recurring ambiguity in the repository: “calibrated” previously could refer to anything from a current certificate to a complete process-state transfer.

---

## 5. New acceptance evidence class

Round 42 adds:

`ACCEPTANCE-EVIDENCE-OPEN`.

Meaning:

> The acceptance method is controlled, but no actual laboratory measurement exists yet.

This is now the correct state for essentially all future physical subsystem commissioning rows.

---

## 6. Measurement-discrimination rule

A central Round-42 result is that acceptance tolerances shall not be arbitrary equipment-shopping numbers.

For a physical decision interval `DeltaX_decision`, require measurement uncertainty small enough to discriminate the intended states.

P36 defines:

`U_X < DeltaX_decision/2`

as the minimum logical condition and

`U_X <= DeltaX_decision/4`

as a preferred engineering target where practical.

These are **measurement-design rules**, not historical process tolerances.

Example:

Te-rich LPE literature carries candidate supercooling as small as ~2 °C in represented branches. If the future local branch intends to resolve a 2-°C distinction directly, then:

- `U_DeltaT < 1 °C` is the minimum discriminability check;
- near `<=0.5 °C` is a preferred engineering target.

The repository therefore no longer needs to invent a generic “furnace accuracy ±0.1 °C” or similar value without a downstream reason.

---

## 7. LPE acceptance result

P36 now separates six acceptance groups:

1. boat geometry/capacity;
2. hot slider motion;
3. source/substrate thermal map;
4. N2/H2 gas delivery;
5. synchronized process logging;
6. HgCdTe residual liquidus/growth qualification.

Important consequence:

A future furnace can be fully surrogate-commissioned while `M_charge`, `TL_local`, `DeltaT_SC`, contact time, Hg-source inventory and final growth response remain intentionally open.

This is the correct boundary between infrastructure commissioning and process qualification.

---

## 8. Hg anneal acceptance result

P36 requires:

- dimensioned sample/reservoir geometry;
- independently calibrated/logged `T_s(t)` and `T_Hg(t)`;
- mapping through the ~250–300 °C region;
- a representative ~250 °C / 1 h dummy dwell;
- enclosure integrity commissioning;
- complete cooldown trace.

Actual Hg chemical-potential/carrier-state response remains residual and must be released through P05/P06/P23.

---

## 9. FTIR / Hall acceptance result

### FTIR

Acceptance now explicitly covers:

- ~500–5000 cm^-1;
- <=4 cm^-1 qualification resolution unless justified otherwise;
- baseline/photometric repeatability;
- map registration;
- independent thickness reference;
- actual HgCdTe model validation as residual.

### Hall

Acceptance now explicitly covers the complete P05 initial field grid:

`0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T`,

with field measured at the sample, plus current/voltage reversal, 80-K/300-K temperature state and a Hall-reference surrogate.

---

## 10. Supporting metrology / microfabrication result

P36A was added because a future lab can otherwise own every major furnace/vacuum tool and still be unable to execute the process quantitatively.

It now covers:

- balance performance at the actual Cd/Hg/Te mass scales;
- propagation of mass uncertainty into `xL/yL`;
- lateral geometry/CD metrology;
- µm/sub-µm thickness metrology;
- Mask-1/Mask-2 coating/bake/dose/profile acceptance;
- wet-mesa chemistry-definition gate;
- anodization cell/current/voltage/area acceptance;
- critical handoff timestamps.

This creates a second important Round-42 rule:

> A chemistry notation is not executable until its concentration/ratio basis and measurement chain are explicit.

---

## 11. RIE acceptance result

The direct/candidate controller state remains:

- CH4 10.6667 sccm candidate;
- H2 53.3333 sccm candidate;
- total 64 sccm;
- 100 mTorr;
- 50 W;
- 60 s.

P36 now requires independent evidence for:

- gas-specific MFC calibration;
- process-pressure calibration;
- reflected RF;
- self-bias/sheath proxy;
- sample thermal state;
- chamber clean/season genealogy;
- actual P25 oxide clear time;
- actual HgCdTe conversion/blocking/contact response.

Permanent rule retained:

`50 W != reactor equivalence`.

---

## 12. Cr/Au deposition acceptance result

P36 now requires:

- separate Cr and Au QCM/witness correlations;
- 30-nm Cr and 270-nm Au capability;
- source/QCM/sample geometry;
- pressure trace;
- sample thermal proxy;
- sequential Cr->Au history;
- actual RIE->Cr handoff;
- HgCdTe TLM/contact residual qualification.

No arbitrary base-pressure threshold is introduced.

---

## 13. Integrated detector-station acceptance result

The most important Round-42 metrology result is that P10–P13 are now commissioned as an **integrated measurement system**.

Acceptance groups:

1. cryogenic temperature/vacuum state;
2. DC bias/load network;
3. MWIR wavelength/radiometry/view-factor chain;
4. 1-kHz modulation/timebase;
5. electronics noise floor;
6. Johnson-noise absolute validation;
7. temporal/frequency transfer;
8. package thermal kernel;
9. matched-state metadata integrity;
10. actual HgCdTe P10–P13 residual response.

### Noise design check retained

For a PSD allocation fraction `beta`:

`e_elec <= 24.5 sqrt(beta) nV/sqrtHz`.

Example:

`beta=.10 -> e_elec<=7.75 nV/sqrtHz`.

This remains an engineering allocation, not an RP-01 historical requirement.

### Johnson validation

P36 now explicitly requires physical Johnson-noise validation with traceable resistors at known temperature:

`S_v = 4 k_B T R`

with the full network prediction used where loading is non-negligible.

This is the strongest available pre-HgCdTe absolute validation of the noise/PSD normalization chain.

### Temporal design check retained

If the same-UWA ~25-ns pulse method is implemented:

`BW~0.35/25 ns~14 MHz`.

Again, instrument sizing only.

---

## 14. Singulation / package acceptance result

### Singulation

Surrogates can commission:

- cut path;
- kerf/wander;
- gross edge damage;
- support/protection;
- clean/release handling.

Actual CdZnTe/HgCdTe/completed stack remains required for subsurface/functional damage.

### Package

Dummy packages can commission:

- bondline geometry;
- thermal resistance/kernel;
- interconnect mechanics/resistance;
- aperture/window/view-factor geometry;
- vacuum/bake/cooldown;
- thermal cycling.

Actual detector remains required for crack/noise/responsivity/thermal-interaction release.

---

## 15. Critical handoff result

Round 42 elevates synchronized handoff timing to explicit acceptance evidence.

Critical transitions:

- final CZT surface -> LPE;
- mesa -> anodization;
- anodization -> Mask-2;
- RIE -> Cr;
- Cr -> Au;
- singulation -> package;
- package -> P10–P13.

A future dummy genealogy run must prove elapsed time/ambient/sample/tool identity can be reconstructed without memory.

---

## 16. Requalification / change control

P36 explicitly requires requalification after configuration changes that can alter the physical transfer function, not merely after a calendar interval.

Examples include:

- boat/sensor/MFC/gauge replacement;
- anneal fixture or furnace-zone changes;
- FTIR optical/stage changes;
- Hall magnet/probe/readout changes;
- RIE electrode/RF/chuck/clean protocol changes;
- QCM/source/sample geometry changes;
- detector-station preamp/load/cable/reference detector/cryostat changes;
- singulation consumable/support changes;
- package attach/interconnect/window/shield changes.

This is a significant improvement over calibration-expiration-only thinking.

---

## 17. Numerical convention status

Round 41 identified the later P30A/P16B rounded mass-fraction drift.

Canonical calculation remains:

- Hg `0.2497382358`;
- Cd `0.01250164993`;
- Te `0.7377601143`;

from the frozen atomic weights in `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`.

Round 42 continues to treat the P30A/P16B later rounded values as a documented erratum. Historical checkpoint/ledger text is not rewritten solely for ppm-scale cleanup.

A future controlled normalization edit should update active P30A/P16B text together if those large files are otherwise revised.

---

## 18. Readiness after Round 42

No physical infrastructure exists in the repository and no acceptance tests were run.

Therefore:

`P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`

`P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`

`TRACEABLE-FIRST-BUILD-READY = NO`

`HISTORICAL-RP01-REPRODUCED = NO`

`REPRODUCIBLE-RELEASE = NO`.

Round 42 closes a **methodological** gap: a future laboratory now has explicit evidence requirements for deciding whether installed tools are sufficiently characterized to proceed.

---

## 19. Strongest next logical work — Round 43

The project now has:

- selected candidate process branch;
- minimum capability envelope;
- subsystem acceptance methodology.

The strongest next analytical step is **first-build uncertainty and requirements allocation at the actual acceptance interfaces**, especially:

1. propagate source-mass + thermal + FTIR/Hall uncertainties into expected material-state uncertainty;
2. propagate lithography/CD + bias/load + temperature uncertainties into `E`, `R`, self-heating and contact-state uncertainty;
3. propagate radiometry + detector geometry + noise-chain uncertainty into responsivity/NEP/D* uncertainty;
4. propagate temporal source/electrical/package de-embedding uncertainty into `f3dB/tau` inference;
5. convert those budgets into quantitative acceptance targets **only where the downstream detector-performance requirement makes them necessary**.

This should be a requirements-allocation exercise using P20/P21/P22, not arbitrary tightening of every instrument specification.