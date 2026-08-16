# P03A — Honeywell x≈0.30 LPE lineage provenance addendum

**Status:** CONTROLLED PROVENANCE UPDATE to `P03_LPE_X030_QUALIFICATION.md`.

## 1. Composition-matched tie line remains the primary anchor

Bowers–Schmit U.S. Patent 4,317,689 tabulates:

- `xL=0.082`;
- `yL=0.810`;
- `Tl=507 °C`;
- resulting solid `xS=0.29`;
- `xS/xL=3.54`.

This remains the best explicit same-Honeywell-lineage composition anchor near the RP-01 nominal x≈0.30 material.

## 2. Additional direct process details now recovered from full patent text

The preferred embodiment explicitly describes:

- growth substrate loaded into graphite base recess;
- Te-rich source loaded into a slider well and capped with graphite plug;
- separate HgTe source wafer in a shallow source well;
- graphite cover installed;
- assembly placed in quartz tube;
- **thorough nitrogen purge before heating**;
- H2 flow during subsequent processing;
- heat to around `500 °C`;
- after equilibration, slider translation brings molten source over substrate;
- Hg source/moat/cover architecture maintains roughly `0.1 atm` Hg partial pressure around the source/wafer near 500 °C.

These are `P-SAME-LINEAGE` process-architecture anchors.

## 3. Thermal trajectory now more strongly closed

The patent explicitly states:

1. the source must first be heated **above its liquidus temperature**;
2. epitaxial growth occurs **below liquidus**;
3. growth may use:
   - step supercooling before contact;
   - contact near liquidus followed by slow cooling;
   - or a combination.

For the xS≈0.29 tie line:

`Tl = 507 °C`.

Therefore 500 °C corresponds to derived supercooling:

`ΔT = 7 °C`.

This remains a qualification center point because the patent does not identify the exact cooling history used for a specific xS=.29 / target-thickness layer.

## 4. Growth-time example recovered

The patent states that once the molten charge is positioned over the substrate, **growth may continue about one half hour** as an example.

Evidence status:

`~30 min` = `P-SAME-LINEAGE / GENERAL APPARATUS EXAMPLE`.

It is **not** a released RP-01 growth time because the source does not connect that example to:

- the xL=.082/yL=.810 row specifically;
- 9.5-µm final thickness;
- RP-01 transport properties.

Use it only as a bounded qualification starting point until P06 thickness-versus-time data close the local process.

## 5. Full tie-line table

The patent reports:

| xL | yL | Tl | xS | k=xS/xL |
|---:|---:|---:|---:|---:|
| .100 | .825 | 508 °C | .40 | 4.00 |
| .095 | .820 | 508 °C | .37 | 3.89 |
| .082 | .810 | 507 °C | .29 | 3.54 |
| .060 | .800 | 510 °C | .22 | 3.67 |
| .050 | .800 | 499 °C | .195 | 3.90 |

This demonstrates that the covered Te-rich slider architecture spans MWIR and LWIR compositions with liquidus temperatures near 500 °C.

Do not extrapolate a growth-time or electrical-state relation from this table; it contains equilibrium composition parameters only.

## 6. Same-lineage reproducibility benchmark

Wood and Hager's 1983 follow-on horizontal-slider LPE paper reports single/double HgCdTe layers on 2×3-cm CdTe substrates with layer-to-layer composition reproducibility around:

`σx ≈ 0.002`.

Use as a **same-lineage achievable benchmark**, not an RP-01 release tolerance until the exact measurement method/statistics are fully audited.

## 7. Remaining P03 release blockers

Still open/qualification-dependent:

- Honeywell boat growth-well dimensions / total charge mass;
- exact charge synthesis/homogenization;
- N2 purge flow and quantitative endpoint;
- H2 flow;
- exact equilibration duration;
- exact x≈.29 cooling rate/supercooling/contact time;
- thickness-time relation centered on 9.5 µm;
- final substrate face/miscut/surface preparation;
- as-grown transport state;
- anneal state needed to reach RP-01 n/µ.

Detailed source-recovery record:

`research/2026-08-15_lpe_honeywell_full_patent_reaudit.md`
