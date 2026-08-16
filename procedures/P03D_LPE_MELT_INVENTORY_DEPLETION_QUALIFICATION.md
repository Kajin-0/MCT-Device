# P03D — Te-rich LPE melt inventory, finite-liquid and depletion qualification

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. Supplements P03/P03A/P03B/P03C.

## 1. Purpose

Define how total Te-rich melt inventory, effective liquid depth, growth-well geometry and source depletion shall be selected and controlled for the locally qualified x≈0.30 horizontal-slider process when the historical Honeywell charge mass/well volume are not disclosed.

The correct process variable is not simply “grams of source.” The physically relevant state includes:

- source composition;
- total liquid inventory;
- liquid depth/shape over the substrate;
- exposed area;
- growth duration;
- Hg-loss flux;
- solute depletion after repeated growths.

## 2. Historical source boundary

Bowers–Schmit US4317689A directly describes:

- a tapered through-well containing the Te-rich growth solution;
- a plug over the charge;
- recessed regions sized approximately to the substrate;
- covered Hg-source/moat geometry;
- growth near 500 °C;
- an example growth duration of roughly one half hour.

The patent does **not** give:

- growth-well diameter;
- well depth;
- well volume;
- melt depth;
- growth-charge mass;
- number of layers grown per charge.

Searches for explicit gram/volume/dimension values in the patent returned no such values.

Therefore the historical total melt inventory remains `OPEN`.

## 3. Why finite melt size matters

A primary numerical study:

“Numerical simulation of the growth of HgCdTe layers by liquid phase epitaxy from Te-rich solutions: The effect of liquid dimensions and mercury loss,” *Journal of Crystal Growth* 106, 303–317 (1990), DOI `10.1016/0022-0248(90)90076-W`, explicitly models:

- finite liquid dimensions;
- moving solid/liquid interface;
- Hg loss;
- step cooling;
- ramp cooling;
- supercooling.

The study shows that for growth times longer than a characteristic time related to liquid thickness:

- growth rate decreases because the finite liquid reservoir becomes compositionally depleted;
- Hg loss drives the grown layer toward higher Cd composition;
- the magnitude of the effect depends on liquid dimensions and Hg-loss flux.

This is the physical reason P03 cannot release a total charge mass independently of well geometry and growth time.

## 4. Related experimental process evidence

Radhakrishnan et al. 2003, DOI `10.1016/S0022-0248(02)02530-7`, use a different x≈0.20 Te-rich horizontal-slider branch and directly disclose:

- 10 g synthesized source compound;
- ~4.8 g charge per growth run;
- 3 g HgTe for Hg-loss compensation;
- 15×15×1 mm CdZnTe substrate recess.

Those values are **not** transferred to the Honeywell x≈0.30 tie line.

Their value here is to demonstrate that total melt mass is an intentional apparatus/process variable that can be independently specified and logged.

## 5. Geometry that must be measured

For the selected local slider/boat record:

- growth-well top diameter/width;
- growth-well bottom diameter/width if tapered;
- well depth;
- plug insertion depth and displaced volume;
- recessed liquid-contact area over substrate;
- substrate dimensions;
- nominal liquid height at growth orientation;
- dead volume not participating in substrate mass transfer;
- liquid free-surface area exposed to Hg-containing vapor;
- Hg-source/moat geometry;
- slider/base clearance where it can affect leakage.

Generate a dimensioned drawing and controlled revision.

## 6. Convert charge mass to liquid inventory

For every source charge record:

- weighed total mass;
- actual component masses/composition;
- estimated liquid density at growth temperature from the selected thermodynamic model/data;
- calculated total liquid volume;
- calculated effective liquid depth/height in the actual well geometry.

Because high-temperature liquid density may be uncertain, propagate density uncertainty into liquid-depth/volume uncertainty.

The process traveler should eventually control both mass and geometry-derived liquid depth rather than one alone.

## 7. Initial melt-inventory DOE

At fixed:

- xL=.082/yL=.810 target composition;
- source-preparation method/lot;
- substrate face/surface state;
- Hg source condition;
- growth temperature/supercooling trajectory;
- contact time;
- wipe-off method;

compare at least three liquid inventories spanning a practical range around the apparatus nominal.

For each inventory measure:

- layer mean thickness;
- thickness uniformity;
- mean x/edge;
- x uniformity;
- surface morphology;
- residual melt behavior;
- post-anneal P05 transport.

Do not choose the largest inventory automatically; excessive melt volume can affect thermal equilibration, wipe-off and source utilization.

## 8. Characteristic depletion behavior

For each inventory, repeat growths from the same source charge where the apparatus permits reuse.

Define run index `j = 1,2,...`.

Track:

- `d_j` = layer thickness;
- `x_j` = mean solid composition;
- within-layer x gradient/uniformity;
- morphology;
- growth time/temperature trace;
- source mass before/after use where practical;
- auxiliary Hg source state.

Fit trends such as:

`d_j = f(j)`

and

`x_j = g(j)`

without imposing a model form until the data support one.

## 9. Source depletion limit

A source-use count or depletion criterion shall be released only after defining the largest acceptable change in:

- mean x;
- x uniformity;
- thickness/growth rate;
- morphology;
- detector-relevant electrical properties.

Possible release forms include:

- maximum number of substrate growths;
- maximum cumulative growth time;
- maximum estimated solute extraction fraction;
- maximum measured change in a source-condition proxy.

The criterion should be based on output drift, not on arbitrary run count.

## 10. Hg-loss coupling

Finite-liquid depletion and Hg loss are coupled but distinct.

A layer can become Cd-richer because of:

- selective Hg loss from the melt;
- solute depletion/finite-reservoir evolution;
- temperature/liquidus drift;
- source-preparation composition error.

Record enough variables to distinguish these mechanisms.

At minimum retain:

- complete thermal trace;
- Hg-source identity/condition;
- run index/source reuse history;
- melt inventory;
- x/edge result;
- thickness result.

## 11. Hg-loss compensation acceptance

The historical Bowers–Schmit covered boat aims to maintain approximately the same Hg vapor pressure over the Te-rich growth solution as generated by HgTe/HgTe+Te, approximately 0.1 atm near 500 °C.

The local Hg-source mass is not fixed historically.

Qualification should demonstrate that, over the released source-use range:

- mean x does not show a systematic Hg-loss signature beyond allowed variation;
- liquidus/growth behavior remains stable;
- post-growth surface/morphology remain stable.

Where practical, record auxiliary source mass before/after runs as supporting evidence.

## 12. Growth-time interaction

P03B establishes thickness as a response to contact time and supercooling.

P03D adds melt inventory as another state variable:

`d_layer = f(t_growth, ΔT, thermal trajectory, liquid depth/inventory, run index, Hg-loss state)`.

The production schedule may use a simpler local model only after demonstrating that neglected terms are small over the released process window.

## 13. Composition interaction

For the composition-matched Honeywell tie line, a nominal solid x≈0.29 is expected near the cited thermal condition.

If x systematically shifts with melt inventory at otherwise matched settings, investigate:

- finite-reservoir composition evolution;
- incorrect effective liquid depth;
- incomplete source homogenization;
- Hg loss;
- temperature gradients.

Do not “correct” the charge composition first without identifying the mechanism.

## 14. Melt-volume versus substrate-area scaling

If substrate size changes, the same gram mass generally does not imply the same growth state.

Define a geometry ratio such as:

`V_liquid / A_substrate`

or an equivalent effective liquid depth.

During scale-up, preserve the physically relevant mass-transfer geometry rather than simply scaling all masses linearly.

The exact dimensionless scaling parameter should be chosen from the local P03D/P03B data and transport model.

## 15. Wipe-off coupling

Changing melt inventory can alter:

- meniscus geometry;
- drainage volume;
- residual solution carried during slide-out;
- wipe-off load on P03/Honeywell CdTe wiping structures.

Therefore include residual-melt/usable-area metrics in the inventory DOE.

## 16. Acceptance vector

Define a melt-inventory capability vector:

`Y_melt = {mean d, σ_d/spatial map, mean x, σ_x/spatial map, morphology, run-order drift, Hg-loss proxy, post-anneal mobility}`.

A selected inventory is acceptable only if all components remain within locally released windows over the intended source-use history.

## 17. Historical closure status

Historical Honeywell x≈0.30:

- charge composition: strongly anchored;
- charge mass/well dimensions/melt volume: **OPEN**.

P03D is therefore the controlled local path to release those apparatus-dependent variables without manufacturing historical precision.