# RP-01 gap-matrix addendum — Round 37

**Date:** 2026-08-16 America/New_York  
**Scope:** R17 RIE gas-realization documentary limit + R15 anodic-oxide apparatus/electrolyte instantiation.

---

## 1. Status key

- `DIRECT-CLOSED` — directly stated for RP-01.
- `TRANSFER-CLOSED` — explicitly disclosed by a primary transfer source, but not RP-01.
- `METHOD-CLOSED` — controlled repository route exists to instantiate/qualify the variable.
- `OPEN-HISTORICAL` — exact RP-01/UWA value not recovered.
- `OPEN-CHOICE` — local physical branch still must be selected/frozen.
- `UNDEFINED-BASIS` — an essential notation or implementation basis is not yet instantiated.
- `RELEASE-DATA-OPEN` — execution can be defined, but release requires measured outcome/capability data.

---

# 2. RIE gas realization — R17

| Coordinate | Direct RP-01 | Best current evidence | Round-37 state | First-build action |
|---|---|---|---|---|
| gas family | `CH4/5H2` printed | direct RP-01 | `DIRECT-CLOSED notation` | preserve exact source notation |
| total flow | `64 sccm` | direct RP-01 | `DIRECT-CLOSED` | verify local total |
| individual ratio | not explicit | same-lineage 2005 review: `CH4:H2=1:5` | `OPEN-HISTORICAL / CANDIDATE` | if chosen, label local transfer |
| candidate CH4 flow | not explicit | derived from 64 sccm + 1:5 | `10.6667 sccm CANDIDATE` | freeze only in local branch |
| candidate H2 flow | not explicit | derived from 64 sccm + 1:5 | `53.3333 sccm CANDIDATE` | freeze only in local branch |
| premix vs separate MFC | not stated | none recovered | `OPEN-HISTORICAL` | define actual local delivery |
| gas purity | not stated | transfer only | `OPEN-CHOICE` | specify grade/lot |
| MFC range/calibration | not stated | P34 method | `METHOD-CLOSED / APPARATUS-OPEN` | instantiate actual MFCs |

### Round-37 decision

No new P08 gas-ratio module is justified. P08A already captures the best documentary decoding. R17 remains blocking because the actual local gas-delivery branch has not been instantiated.

---

# 3. Anodic oxide — R15

| Coordinate | Direct RP-01 | Best transfer evidence | Round-37 state | Closure action |
|---|---|---|---|---|
| passivant | native anodic oxide | RP-01 | `DIRECT-CLOSED` | retain |
| oxide thickness | ~800 Å | RP-01 | `DIRECT-CLOSED target descriptor` | measure local film |
| electrolyte family | not stated | TI US3977018: 0.1 M KOH / 90% EG / 10% DI | `TRANSFER-CLOSED` | select/freeze local branch |
| KOH inventory basis | not stated | TI: 0.1 mole KOH in 1 liter mixed solvent | `TRANSFER-CLOSED` | use explicit local reagent assay/calculation |
| 90:10 EG:H2O basis | not stated | notation only | `OPEN-HISTORICAL / OPEN-CHOICE` | define local v/v, w/w, or other branch explicitly |
| cathode — TI-PC branch | not stated | carbon rod | `TRANSFER-CLOSED` | one candidate branch |
| cathode — later TI branch | not stated | circular Pt | `TRANSFER-CLOSED SEPARATE BRANCH` | do not merge silently |
| anode contact | not stated | later TI: etched W/Ti probe | `TRANSFER-CLOSED SEPARATE BRANCH` | choose local method |
| cell material | not stated | TI-PC plastic-lined SS; later TI Teflon/PP | `TRANSFER-CLOSED SEPARATE BRANCHES` | dimension/freeze actual cell |
| sample orientation | not stated | later TI horizontal | `TRANSFER-CLOSED SEPARATE BRANCH` | choose local orientation |
| exposed area | not stated | electrochemical requirement | `METHOD-CLOSED / OPEN-CHOICE` | measure actual `A_exposed` |
| current density | not stated | TI-PC ~0.3 mA/cm² | `TRANSFER-CLOSED CENTER` | local qualification center |
| formation voltage | not stated | TI-PC ~15 V | `TRANSFER-CLOSED CENTER` | record V(t); do not blind-stop until calibrated |
| time | not stated | TI-PC ~2 min | `TRANSFER-CLOSED CENTER` | not universal endpoint |
| film appearance | not stated | TI-PC uniform deep blue | `TRANSFER-CLOSED AUXILIARY` | visual proxy only |
| bath agitation | not stated | later TI explicitly unstirred; x≈.30 mechanism shows sensitivity | `OPEN-HISTORICAL / METHOD-CLOSED` | freeze actual state |
| bath temperature | not stated | later TI ~room temperature | `OPEN-HISTORICAL / OPEN-CHOICE` | measure/freeze actual bath T |
| V(t) fingerprint | not stated | TI + x≈.30 mechanism | `METHOD-CLOSED` | continuous local recording |
| induction interval | not stated | x≈.30 mechanism lineage | `METHOD-CLOSED` | extract locally |
| rinse/dry | not stated | architecture-specific transfer sequences | `OPEN-HISTORICAL / OPEN-CHOICE` | define local compatible branch |
| P28->P25 clock | not stated | Round36/37 surface-state reasoning | `METHOD-CLOSED / OPEN-CHOICE` | timestamp and qualify |
| P25->Mask2/P08 clock | not stated | surface/interface control | `METHOD-CLOSED / OPEN-CHOICE` | timestamp and qualify |
| interface/noise release | not stated as numeric spec | P25/P12 | `RELEASE-DATA-OPEN` | correlate oxide branch with device outputs |

---

## 4. Readiness consequence

### R15

Current state remains:

`R15 = OPEN-CHOICE`.

P25A now provides an exact closure checklist. To become `LOCAL-BRANCH-FROZEN`, sections covering electrolyte mathematics, reagent genealogy, cell geometry, `A_exposed`, current density, V(t)/Q/A and rinse/dry must be instantiated for an actual laboratory.

### R17

Current state remains:

`R17 = UNDEFINED-BASIS` at the project execution level.

The documentary ambiguity has a ranked candidate resolution (`1:5`), but the actual local branch and gas delivery have not been frozen. Historical individual MFC values remain open.

### Overall

`TRACEABLE-FIRST-BUILD-READY = NO`.

Round 37 reduces uncertainty and supplies closure methods; it does not substitute documents for physical branch selection.

---

## 5. Negative-search / non-inference record

Do not infer:

- `CH4/5H2` directly equals published RP-01 10.67/53.33-sccm MFC settings;
- `90% EG / 10% water` in TI is automatically v/v;
- a Pt cathode is interchangeable with the earlier TI carbon rod without qualification;
- a 2-min anodization is portable across cell geometry, starting surface or exposed area;
- a deep-blue film alone proves ~80-nm thickness or interface equivalence;
- same final oxide thickness means same interface charge/noise state;
- same-UWA passivation paper identity supplies an unrecovered UWA anodization traveler.
