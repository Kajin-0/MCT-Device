# P01A — Srivastav 2005 primary experimental-method addendum

**Status:** PRIMARY-SOURCE METHOD CLOSURE / CONCENTRATION-BASIS STILL OPEN. Supplements `P01_WET_MESA_QUALIFICATION.md`.

## 1. Purpose

Capture experimental details present in the full primary text of V. Srivastav et al., “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005), DOI `10.1007/s11664-005-0203-5`, that were not fully represented in the original P01 qualification module.

This paper is a near-composition transfer source (`x=0.28`), not the exact UWA/RP-01 mesa recipe.

## 2. Starting material and pre-etch preparation — directly published

The paper states that the Hg1−xCdxTe wafers used for its experiments had:

- `x=0.28`;
- material procured from SMALL Enterprises, Ukraine;
- samples diced with a wire saw and mounted on sapphire;
- mechanical lapping/polishing using alumina powder of decreasing grit size;
- subsequent chemomechanical polishing;
- final free etch in `0.1% Br2 in methanol` for `1 min` before mesa-pattern experiments.

The polished surface was inspected by:

- Nomarski microscopy;
- ellipsometry at `6328 Å` using a Gartner Scientific instrument.

The authors state that the surface was checked for oxide, damage and contamination before the patterned etch study.

### Provenance warning

The `0.1% Br2/methanol` free etch is part of the source paper's sample-preparation sequence. The accessible primary text does **not** define the percentage basis of this 0.1% value either. Do not translate it into a mass/volume recipe without an independently verified convention.

## 3. Lithographic test geometry — directly published

Two test masks were used:

1. linear structures approximately `600 µm` long with `50 µm` trench width;
2. two-dimensional mesa structures separated by `30 µm` trenches.

These dimensions are useful for process-development metrology but are not the RP-01 detector geometry.

## 4. Etchant experimental matrix — directly published

The experimental etchant family is Br2/HBr/ethylene glycol (EG).

Phase I:

- Br2 nominal concentration varied from `1%` through `3%` at several levels;
- for each Br2 level, EG fraction in HBr was varied from 0 to 1.

Phase II:

- process temperature varied from `5 °C` to `50 °C` at the optimum composition selected in Phase I.

Selected optimum:

- nominal `2% Br2`;
- solvent mixture `3:1 EG:HBr`, equivalently `75% EG / 25% HBr` by the mixture fraction used in the paper;
- near-room-temperature reference measurements at `21 °C`.

## 5. Concentration-basis audit — still unresolved

The accessible full primary text repeatedly states:

- `1–3% Br2`;
- selected `2% Br2`;
- `0.1% Br2 in methanol` for the pre-etch;

but does **not** provide:

- bromine mass used;
- bromine volume used;
- final solution mass/volume;
- a statement such as w/v, v/v, wt%, mol%, etc.;
- a reagent-preparation equation.

Therefore the concentration basis remains a genuine `OPEN` variable.

Do not infer the basis from modern laboratory convention.

## 6. Etch metrology — directly published

Vertical etch rate `R_V` was determined from step/depth measurement using a Veeco Dektak profilometer.

Lateral etch rate `R_L` was determined from mask undercut observed using high-magnification phase-contrast microscopy.

The paper defines anisotropy as:

`A = 1 - R_L/R_V`.

Surface effects were evaluated using:

- profilometry/roughness measurements;
- ellipsometry;
- SEM for profile morphology.

The paper explicitly treats vertical and lateral rates as separate process outputs. P01 should preserve this distinction.

## 7. Optimum-process quantitative anchors — directly published

For nominal 2% Br2 in 3:1 EG:HBr:

- mean vertical etch rate reported in preliminary uniformity work: `2.78 µm/min`;
- run/process variation about `±26%`;
- mean anisotropy approximately `0.63` with about `±11%` variation;
- RMS roughness across investigated conditions approximately `2–7 nm`, with the best values near `2 nm` for the high-EG formulation;
- activation energy for the optimum process approximately `7.5 kcal/mol`;
- rate approximately doubles for each `+10 °C` increase over the investigated regime;
- lower-temperature processing gave better edge/profile control and reduced photoresist attack.

The authors state that tighter control of concentration and endpoint could potentially reduce etch nonuniformity to about ±10%; treat this as an author assessment, not a demonstrated production capability.

## 8. Process drift mechanism — directly published

The paper identifies bromine-concentration drift as a major reproducibility concern because Br2 evaporates readily from the etchant.

Therefore any local P01 transfer must treat the following as controlled variables:

- solution preparation timestamp;
- covered/open vessel state;
- elapsed time from preparation to use;
- bath temperature;
- bath volume and exposed surface area;
- use/reuse history;
- agitation state;
- sample loading/order.

A nominal starting composition without bath-age control is insufficient.

## 9. Derived RP-01 through-layer timing scale — NOT a recipe

RP-01's HgCdTe layer is approximately `9.5 µm` thick.

Using the source mean rate only as a dimensional consistency calculation:

`t_ideal = 9.5 µm / (2.78 µm/min) ≈ 3.42 min`.

Using the source's ±26% observed rate spread:

- slow-rate edge: `R≈2.06 µm/min` → about `4.62 min` to remove 9.5 µm;
- fast-rate edge: `R≈3.50 µm/min` → about `2.71 min` to remove 9.5 µm.

These numbers demonstrate why **timed etching alone is not adequate** for RP-01 transfer. They are not released setpoints.

The production mesa requires through-layer isolation plus a qualified overetch/endpoint strategy while controlling lateral undercut and substrate attack.

## 10. P01 qualification implication

Until the 2% basis is recovered, local transfer should not begin by pretending that the chemistry is exact. The scientifically valid choices are:

1. recover the preparation convention from laboratory records, precursor references or authors' related process papers; or
2. explicitly define a local concentration convention, then qualify it as a new local P01 formulation against rate, anisotropy, roughness, electrical preservation and device performance.

Any local formulation must receive its own recipe ID and may not be described as the exact Srivastav composition unless the percentage basis is source-verified.
