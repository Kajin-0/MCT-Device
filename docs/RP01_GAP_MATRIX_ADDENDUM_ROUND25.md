# RP-01 gap matrix addendum — Round 25 Mask-1 / wet-mesa lithography

**Date:** 2026-08-16 America/New_York

| Variable / requirement | Historical RP-01 status | Best recovered primary evidence | Current control state | Closure action |
|---|---|---|---|---|
| Mask-1 purpose | CLOSED | Smith 2001: wet chemical mesa delineation / electrical isolation | DIRECT-RP01 | Preserve |
| Mask-1 resist identity | OPEN | None in RP-01; transfer candidates 180CP, AZ4620 | EMPIRICAL-REQUIRED | Local resist screen; continue thesis/source recovery |
| Resist family | OPEN | Novolak family supported in primary HgCdTe processing | TRANSFER-FAMILY | Do not infer RP-01 identity |
| Resist thickness | OPEN | 1–6 µm general HBr patent; 3 µm AZ4620 embodiment; 5 µm separate HBr mesa patent | EMPIRICAL-REQUIRED | Measure survival/edge retreat in actual P28 chemistry |
| Deep-etch resist process | OPEN | Hunt 180CP, 4000 rpm/20 s, 60 °C/3 min, develop 30 s, rinse 15 s, ash 200 W/30 s, Br/MeOH through ~12 µm HgCdTe | TRANSFER-BRANCH | Use as historical control only |
| HBr-compatible product identity | OPEN | AZ4620, 3 µm, Br2:HBr 0.5%:1 v/v deep-mesa embodiment | STRONG TRANSFER-CANDIDATE | Screen in explicitly defined P28 chemistry |
| Spin process | OPEN | 180CP branch 4000 rpm/20 s; AZ4620 embodiment does not close resist spin recipe | EMPIRICAL-REQUIRED | Supplier-valid local coating DOE + thickness map |
| Bake | OPEN | 180CP branch 60 °C/3 min | TRANSFER ONLY | Local resist-specific qualification |
| Exposure wavelength/dose/mode | OPEN | Not recovered for relevant Mask-1 branches | EMPIRICAL-REQUIRED | Dose/develop matrix on actual stack |
| Developer | OPEN | 180CP branch gives 30 s but not identity | EMPIRICAL-REQUIRED | Record product/concentration/time |
| Post-develop ash | OPEN | 180CP transfer: 200 W/30 s | TRANSFER ONLY | Do not add unless locally justified and HgCdTe-safe |
| Resist/P28 chemical compatibility | OPEN | Srivastav: high T attacks resist; profile depends on resist thickness/geometry | EMPIRICAL-REQUIRED | Measure `h_PR,0`, `h_PR,f`, edge retreat, adhesion |
| Resist selectivity | OPEN | No matched P28 value | EMPIRICAL-REQUIRED | Measure on local coupons; do not infer from thickness |
| Mask-edge trenching | OPEN | Srivastav directly reports faster etch near resist edges | PRIMARY-X028 TRANSFER | Quantify on diagnostic line/trench structures |
| Mask bias | OPEN | No RP-01 value | EMPIRICAL-REQUIRED | Map `CD_mask -> CD_PR -> CD_top/base` |
| Through-layer endpoint | OPEN numeric | P28: measured depth + electrical isolation | CONTROLLED EMPIRICAL | Preserve P28 endpoint rule |
| Resist strip chemistry | OPEN | Acetone used in several transfer branches | TRANSFER ONLY | Qualify strip + residue + P25 handoff |
| Ultrasonics | OPEN | No matched RP-01 evidence | PROHIBITED-BY-DEFAULT | Only after mechanical-damage qualification |
| Etch-to-strip interval | OPEN | No source value | EMPIRICAL-REQUIRED | Timestamp |
| Strip-to-anodization interval | OPEN | No source value | EMPIRICAL-REQUIRED | Timestamp and correlate with P25 response |
| Mesa final outer geometry | OPEN | RP-01 contact geometry known, outer mesa not recovered | EMPIRICAL/HISTORICAL GAP | Recover original mask/thesis or define local mask set |
| Alignment-mark chemistry protection | OPEN RP-01 | TI transfer warns exposed Al attacked by Br/MeOH | PROCESS-DEPENDENT | Keep alignment material chemically compatible |

## Round-25 release status

P32 is `PRE-RELEASE`. No Mask-1 commercial resist, thickness, dose, developer, strip chemistry or mask bias is released as historical RP-01 fact.

## Strongest first local empirical path

1. Select a current, traceable AZ4620 branch as the first product-identified Br2/HBr screening candidate if facility/process compatibility permits.
2. Select one additional thick positive novolak/DNQ control branch.
3. Establish coating/development on witness material.
4. Couple each branch to the exact P28 etchant recipe, temperature and agitation.
5. Measure resist thickness loss, edge retreat, adhesion, P28 depth/undercut/trenching and isolation.
6. Qualify strip residue/surface state and P25 anodization handoff.
7. Release mask bias only from repeated `CD_mask -> CD_PR -> CD_mesa` measurements.

This is a qualification sequence, not a claim that AZ4620 was used by UWA.
