# RP-01 gap matrix addendum — Round 39 lithography documentary-limit audit

**Date:** 2026-08-16 America/New_York

## Purpose

Update the first-build gap state after re-auditing both lithography masks against primary/same-UWA sources and the already controlled P27/P32 qualification layers.

---

| Coordinate | Historical RP-01 state | Strongest transfer / current evidence | Round-39 execution state | Closure route |
|---|---|---|---|---|
| Mask-2 resist identity | `OPEN-HISTORICAL` | positive diazo/DNQ-novolak chlorobenzene mechanism; candidate AZ families only | `OPEN-CHOICE` | select actual positive resist/product/lot capable of 4–5 µm and qualify through P27 |
| Mask-2 thickness | `DIRECT-RP01 ~4–5 µm` | fixed historical target | target closed; coating recipe open | select product-specific spin recipe and verify mapped thickness |
| Mask-2 prebake | `DIRECT-RP01 80 °C / 30 min` | direct | center closed; tool realization open | calibrate actual bake tool/sample temperature |
| Mask-2 chlorobenzene | `DIRECT-RP01 30 min` | historical chlorobenzene lift-off lineage | duration closed; bath state/order details open | P27 branch with controlled bath, temperature, order, product lot, profile outputs |
| Mask-2 exposure | `OPEN-HISTORICAL` | product/process-specific primary examples | `OPEN-CHOICE` | actual aligner/wavelength/irradiance/dose matrix through P27 |
| Mask-2 developer | `OPEN-HISTORICAL` | aqueous alkaline family strongly plausible, product not identified | `OPEN-CHOICE` | product-matched developer, concentration, temperature/time, rinse/dry through P27 |
| Mask-2 RIE survival | functional requirement direct | P27 contains pre/post-P08 profile gate | local data required | qualify resist thickness/profile/CD before/after P08 |
| Mask-2 lift-off solvent/process | `OPEN-HISTORICAL` | acetone/NMP/remover examples from other branches | `OPEN-CHOICE` / R21 | select least-damaging local remover branch and qualify full P08/P26 stack |
| Mask-1 resist identity | `OPEN-HISTORICAL` | AZ4620 product-identified Br2/HBr HgCdTe transfer; Hunt 180CP Br2/MeOH transfer | `OPEN-CHOICE` / R12 | select actual current product/lot + complete coating/exposure/developer/strip branch through P32 |
| Mask-1 thickness | `OPEN-HISTORICAL` | primary AZ4620 3-µm transfer; other deep-HgCdTe masks vary | `OPEN-CHOICE` | determine from actual P28 survival/profile/isolation, not active-layer thickness rule |
| Mask-1 bake/exposure/developer | `OPEN-HISTORICAL` | no UWA recipe recovered | `OPEN-CHOICE` | current product documentation + calibrated local dose/development matrix + P28 coupling |
| Mask-1 resist survival in Br2/HBr/EG | `OPEN-HISTORICAL` | Srivastav proves PR thickness/T strongly affect profile but does not name product | local qualification required | P32/P28 coupled survival, edge-retreat, pinhole/lift, mesa profile and isolation |
| Mask-1 strip | `OPEN-HISTORICAL` | acetone used in some HgCdTe transfer branches | `OPEN-CHOICE` | explicit strip/rinse/dry and P25 handoff qualification |
| White 2005 UWA thesis | official PDF identified | PDF path currently returns 403 | `IDENTIFIED-NOT-RECOVERED` | recover thesis through another legitimate archival route before revisiting historical product identity |

---

## Mask-2 disposition

P27 is already sufficient as the controlled local closure method. The round did not find evidence justifying a new P27A.

P16A R16 therefore remains:

`OPEN-CHOICE`.

The row closes only when an actual product/lot, coating condition, bake realization, chlorobenzene branch, exposure/developer branch and post-develop profile are physically frozen and shown to survive P08/P26.

R21 likewise remains `OPEN-CHOICE` until the actual lift-off remover/time/temperature/agitation/rinse branch is frozen and demonstrated not to damage the HgCdTe/oxide/contact stack.

---

## Mask-1 disposition

P32 is already sufficient as the controlled local closure method. The round did not find evidence justifying a new P32A.

P16A R12 remains:

`OPEN-CHOICE`.

The strongest current screening hierarchy remains:

1. product-identified AZ4620 Br2/HBr HgCdTe transfer branch;
2. one current thick positive novolak/DNQ control selected for actual etch compatibility;
3. Hunt 180CP as historical transfer evidence only when authentic process/material documentation is available.

### Product-name continuity warning

Do not treat the `AZ4620` name as formulation equivalence across time. The primary patent embodiment reports a 3-µm AZ4620 mask while current commercial documentation gives a substantially thicker normal film range. Current material must receive a new local branch ID and measured thickness/exposure/development/etch-survival qualification.

---

## Documentary saturation statement

For generic web-accessible UWA lithography searching, both R12 and R16 are now near a documentary limit. Future historical searches should be triggered by a genuinely new source family, especially:

- White 2005 thesis full PDF;
- Siliquini thesis full experimental appendices;
- UWA cleanroom travelers/notebooks;
- original 1999/2000 conference proceedings full fabrication text;
- mask-shop or process logs.

Absent such a source, repeated keyword searching is lower value than selecting and integrating an explicitly nonhistorical first-build candidate branch.
