# Honeywell x≈0.30 Te-rich LPE full-patent re-audit

**Date:** 2026-08-15 America/New_York

## Purpose

Recover additional operational detail from the same Honeywell/Schmit/Hager/Wood Te-rich horizontal-slider lineage while the full 1982 Schmit–Hager–Wood Journal of Crystal Growth article remains inaccessible beyond abstract-level text.

Primary apparatus/process source:

J. E. Bowers and J. L. Schmit, U.S. Patent 4,317,689, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution” (1982).

## Newly re-audited direct process details

### Atmosphere / load sequence

The preferred embodiment states:

1. place growth substrate in the base recess;
2. place the Te-rich Hg-Cd-Te charge in the slider well and cap it with a graphite plug;
3. place a HgTe source wafer in a separate shallow source well;
4. install the graphite cover;
5. place assembly in quartz furnace tube;
6. **thoroughly purge with nitrogen before heating**;
7. establish H2 flow;
8. heat the boat/system to approximately 500 °C;
9. after equilibration, translate the slider to bring the molten charge over the substrate.

The source explains that H2 flows through the furnace tube during equilibration/growth and that the covered HgTe-source geometry supplies roughly the same Hg vapor pressure as the Te-rich growth charge, around 0.1 atm near 500 °C, limiting Hg loss.

### Example growth duration

The patent states that after slider translation brings the melted charge over the substrate, **“as an example, growth may continue about one half hour.”**

Evidence grade:

- `~0.5 h growth example` = `P-SAME-LINEAGE / NON-COMPOSITION-SPECIFIC-EXAMPLE`.

Do **not** turn this into a 9.5-µm RP-01 growth time because the patent does not state that the half-hour example corresponds specifically to the xS=0.29 tie line or to a 9.5-µm layer.

### Thermal trajectory

The patent explicitly states:

- 500 °C is used throughout as the described growth temperature;
- actual growth must occur below the liquidus temperature `Tl` of the selected solution;
- the charge is initially heated above `Tl` and then taken below `Tl` for growth;
- permitted modes include:
  - step cooling: supercool by a selected amount before substrate contact;
  - start at liquidus and slowly cool after contact;
  - combination of the two.

This materially strengthens P03's process architecture but still does not identify the exact cooling rate/supercooling history used for a particular 9.5-µm x≈0.30 layer.

## Full tie-line table recovered

The patent tabulates five Te-rich source solutions:

| xL | yL | Tl | solid xS | xS/xL |
|---:|---:|---:|---:|---:|
| 0.100 | 0.825 | 508 °C | 0.40 | 4.00 |
| 0.095 | 0.820 | 508 °C | 0.37 | 3.89 |
| 0.082 | 0.810 | 507 °C | 0.29 | 3.54 |
| 0.060 | 0.800 | 510 °C | 0.22 | 3.67 |
| 0.050 | 0.800 | 499 °C | 0.195 | 3.90 |

The `xL=0.082, yL=0.810 -> xS=0.29` row remains the best composition-matched candidate for RP-01.

### Important interpretation

The table itself does not state layer thickness, contact time or resulting transport state for each row. Therefore it closes a **liquid/solid equilibrium/process-composition anchor**, not a full device-grade growth recipe.

## Hg containment architecture — confirmed details

The patent describes:

- covered graphite slider/base/cover assembly;
- one or more plugged growth wells;
- separate shallow HgTe or HgTe+Te source region;
- grooves/moats around growth wells and on lower slider face;
- communication channel from Hg source region to those moats;
- close-fitting graphite cover;
- quartz furnace tube;
- H2 external process stream.

The Hg source is selected so its equilibrium Hg vapor pressure is approximately equal to that of the Te-rich source, around 0.1 atm at 500 °C; the patent specifically notes that exact source composition is not highly critical over the relevant HgTe/Te range because Hg vapor pressure is relatively insensitive to x/y over the stated composition range.

## What remains unclosed

Even after this full-patent audit, a literal x≈0.30 / 9.5-µm recipe still lacks:

- total charge mass/melt depth for the Honeywell boat;
- source-charge synthesis/homogenization method;
- quantitative N2 purge flow/time;
- H2 flow;
- exact equilibration duration/criterion;
- exact xS=0.29 supercooling magnitude or cooling rate;
- exact contact/growth time tied to xS=0.29;
- thickness-versus-time relation;
- substrate face/miscut/surface preparation for that exact run;
- final as-grown carrier state;
- post-growth Hg anneal state needed to reach RP-01 transport values.

## Full Schmit–Hager–Wood paper search result

The 1982 Journal of Crystal Growth article remains indexed by the publisher with abstract only:

J. L. Schmit, R. J. Hager, R. A. Wood, “Liquid phase epitaxy of Hg1−xCdxTe,” JCG 56, 485–489, DOI `10.1016/0022-0248(82)90468-7`.

The abstract directly confirms atmospheric-pressure horizontal-slider Te-rich LPE of n- and p-type material on CdTe up to 2×3 cm and controlled x=0.2, 0.3, 0.4.

No openly indexed full experimental section was recovered in this search session.

## Same-lineage follow-on

R. A. Wood and R. J. Hager, “Horizontal slider LPE of (Hg,Cd)Te” (1983), reports single/double layers on 2×3-cm single-crystal CdTe with extremely uniform composition and layer-to-layer reproducibility standard deviation approximately `σx=0.002`.

Accessible indexing again does not provide the full operational recipe, but this is useful same-lineage evidence for the achievable composition reproducibility of the mature Honeywell slider process.

## Controlled conclusion

P03 may now state more strongly that the composition-matched Honeywell process family directly supports:

- xS≈0.29 from xL=.082/yL=.810;
- Tl≈507 °C;
- N2 purge before heating;
- H2 flowing process environment;
- covered HgTe-source Hg containment;
- initial heat above Tl;
- growth below Tl near 500 °C;
- step, continuous or combined cooling modes;
- example contact/growth interval of ~30 min in the apparatus.

But **30 min is not yet the 9.5-µm RP-01 growth time** and must remain a qualification starting point only.
