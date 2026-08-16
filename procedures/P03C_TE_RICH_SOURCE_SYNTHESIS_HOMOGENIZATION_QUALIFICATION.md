# P03C — Te-rich x≈0.30 LPE source synthesis and homogenization qualification

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. Supplements P03/P03A/P03B.

## 1. Purpose

Define how the composition-matched Te-rich Hg-Cd-Te growth solution for RP-01 upstream qualification shall be prepared and accepted when the exact Honeywell historical source-synthesis traveler is not publicly disclosed.

The controlled composition anchor remains the Bowers–Schmit tie line:

- liquid metal Cd fraction `xL = 0.082`;
- liquid Te fraction `yL = 0.810`;
- liquidus `TL = 507 °C`;
- resulting solid `xS ≈ 0.29` in the historical source;
- tabulated `xS/xL = 3.54`.

Derived elemental mole fractions:

- Hg `0.17442`;
- Cd `0.01558`;
- Te `0.81000`.

Derived mass fractions:

- Hg `0.249738`;
- Cd `0.012502`;
- Te `0.737760`.

The total charge mass remains apparatus dependent.

## 2. Historical source boundary

Bowers–Schmit US4317689A and the later Hager–Wood apparatus patent describe:

- placement of a Te-rich `(Hg1−xCdx)1−yTey` charge into the graphite slider well;
- HgTe/HgTe+Te auxiliary source;
- N2 purge;
- H2 process atmosphere;
- heating near 500 °C;
- taking the charge above liquidus before growth below liquidus.

They treat the Te-rich growth solution as an **already prepared input**.

The patents do not currently disclose whether the xL=.082/yL=.810 charge was prepared by:

- direct elemental reaction;
- pre-reacted binary/ternary components;
- cast ternary source ingot;
- in-situ vapor equilibration;
- or another source-preparation method.

Do not invent that missing historical step.

## 3. Process-family restrictions

### Earlier Honeywell near-pseudobinary source route

US3902924 describes an earlier Honeywell LPE process in which a 13–15-g HgCdTe ingot was cast as source material and melted near ~800 °C.

That process uses a near-pseudobinary/stoichiometric liquid, not the later strongly Te-rich xL=.082/yL=.810 branch.

**Do not transplant the 13–15-g cast-ingot source procedure into P03.**

### Radhakrishnan 2003 source synthesis

Radhakrishnan et al. used 6N elemental Hg/Cd/Te and evacuated-ampoule synthesis around 700 °C for 8 h in a different Te-rich x≈0.20 process family.

This is a useful **candidate source-preparation method**, not the historical x≈0.30 Honeywell source traveler.

### In-situ Te-solution preparation

A separate 1988 slider-LPE study (J. Crystal Growth 87, 365–371, DOI `10.1016/0022-0248(88)90189-3`) demonstrated in-situ Te-rich source preparation by transporting Hg from vapor into a Cd-rich Te melt.

This establishes another technically valid source-preparation concept but is not assumed to match Honeywell RP-01 upstream material.

## 4. Qualification philosophy

Because source preparation is not historically closed, the source is released by its **measured thermodynamic/growth behavior**, not by the preparation narrative alone.

A source-preparation route is acceptable only if it repeatedly produces a charge that:

1. has the intended elemental composition within the released mass/assay uncertainty;
2. melts/equilibrates reproducibly near the expected liquidus neighborhood;
3. does not show unresolved solid inclusions/segregated phases at the growth condition;
4. yields the correct solid x/composition distribution under the P03/P03B growth condition;
5. yields acceptable surface morphology/thickness uniformity;
6. does not introduce transport/lifetime degradation attributable to source contamination.

## 5. Candidate preparation Route A — sealed elemental reaction

**Status:** CANDIDATE-P / LOCAL-QUAL, based on related Te-rich LPE literature rather than direct Honeywell disclosure.

Concept:

- weigh high-purity Hg, Cd and Te to the selected total mass using the P03 composition fractions;
- load into a compatible sealed reaction vessel under an approved Hg/high-temperature protocol;
- react/homogenize at a temperature sufficiently above the intended LPE liquidus to form a uniform liquid source;
- cool/store or transfer the synthesized charge under a controlled contamination history;
- remelt/equilibrate in the slider for growth.

**Exact synthesis temperature/time is not released by this document.**

The related 700 °C / 8 h Radhakrishnan process is a screening reference only and must not be labeled the historical x=.30 Honeywell recipe.

## 6. Candidate preparation Route B — in-situ elemental/binary equilibration

**Status:** LOCAL-QUAL.

A source may be prepared directly in the growth vessel/boat from weighed components if the apparatus can demonstrate:

- complete melting/reaction;
- no unacceptable Hg loss;
- stable composition;
- adequate mixing/homogenization;
- repeatable liquidus/growth output.

This route should not be called historically equivalent unless a direct same-lineage source is recovered.

## 7. Candidate preparation Route C — in-situ Hg-vapor transport into Cd/Te-rich melt

**Status:** DIFFERENT-PROCESS-FAMILY / RESEARCH-OPTION.

The 1988 primary study proves the concept can avoid separate ampoule synthesis. It should be treated as a separate process-development branch, not silently merged into the Bowers–Schmit apparatus.

Only evaluate if Route A/B are impractical or if contamination/reproducibility data justify the additional complexity.

## 8. Weighing and mass closure

For every charge record:

- nominal total charge mass `M`;
- actual weighed Hg, Cd, Te masses;
- balance ID/calibration;
- source lot/purity/certificate;
- container/tare correction;
- mass before/after synthesis where measurable;
- normalized actual mole fractions;
- deviation from target xL/yL.

P03 charge-sensitivity work shows Cd weighing error dominates direct xL error because Cd is only ~1.25 wt% in the composition-matched source.

Do not release a balance tolerance based only on display resolution; qualify repeatability/linearity at the actual Cd mass range.

## 9. Homogenization variables

For whichever preparation route is selected, control and record:

- peak reaction temperature;
- time above full-melt threshold;
- time above the target liquidus;
- mixing/agitation/rocking/stirring method if used;
- thermal gradients along the charge;
- ramp rates;
- vessel/boat geometry;
- Hg chemical-potential control;
- cooling/solidification history if the charge is stored before growth;
- number of remelts/reuses.

A source is not assumed homogeneous merely because it was molten.

## 10. Homogeneity qualification

Use at least two independent forms of evidence during process development.

Candidate evidence:

- reproducible liquidus/thermal signature;
- sampled chemical assay on sacrificial synthesized charges;
- composition of multiple epitaxial layers grown from different positions/run order;
- absence of solid residue at the intended equilibrium temperature;
- run-to-run P06 x/edge map repeatability;
- no systematic composition drift with charge use/depletion beyond the modeled growth behavior.

## 11. Source-conditioning study

Before freezing a production source protocol, test whether the first growth from a fresh charge differs systematically from subsequent growths.

Record for sequential runs:

- source-use number;
- pre-growth hold history;
- Hg-source state/mass where possible;
- layer mean x;
- x uniformity;
- thickness/growth rate;
- morphology;
- Hall state after the same anneal protocol.

A first-run conditioning effect must either be eliminated or deliberately built into the traveler.

## 12. Contamination gate

Source synthesis and storage must not create detectable performance-limiting contamination.

Record/qualify:

- reaction vessel material and cleaning history;
- graphite/quartz compatibility;
- storage container;
- handling atmosphere;
- elemental impurity certificates;
- source reuse count;
- trace impurity analysis where available;
- corresponding P05 mobility and P13 lifetime trends.

A source route that reaches the correct x but lowers mobility/lifetime or introduces unstable doping fails.

## 13. Thermodynamic consistency gate

The historical tie line expects liquidus `TL≈507 °C` for xL=.082/yL=.810.

The exact measured liquidus in a local apparatus may differ modestly because of:

- composition uncertainty;
- thermometer calibration;
- Hg loss/chemical potential;
- source contamination;
- thermal gradients.

Do not force the controller to display exactly 507 °C as proof of correct composition.

Instead compare the measured thermal/growth behavior with the uncertainty budget and resulting P06 solid composition.

## 14. Coupling to P03B

Source synthesis and growth-rate calibration cannot be optimized independently.

For every P03B growth-time/supercooling point, record the source-preparation lot and conditioning history.

If two nominally identical P03B conditions give different thickness/x because the source-preparation lot differs, the source protocol is not yet controlled.

## 15. Source-reuse/depletion rule

Do not assume one charge can be reused indefinitely.

Track:

- cumulative growth time;
- number of substrate contacts;
- estimated material removal;
- mean x drift;
- liquidus/growth-rate drift;
- morphology drift.

Define a maximum qualified source-use count or depletion criterion from data.

## 16. Initial local comparison experiment

If multiple preparation routes are available, compare them at the same:

- target elemental composition;
- total charge mass/melt geometry;
- auxiliary Hg environment;
- growth temperature/supercooling;
- substrate class;
- growth duration.

For each route collect at least:

- charge mass closure;
- thermal/equilibration trace;
- P06 layer thickness/x map;
- morphology;
- P05 transport after a matched anneal;
- repeated-run variability.

Select the route that gives the best reproducibility and material quality, not the route that most resembles generic historical practice.

## 17. Release state

Until a direct x≈0.30 Honeywell source-synthesis document is recovered, the historical preparation method remains `OPEN`.

A local route may nevertheless become `SOURCE-PREP-QUALIFIED` once its composition, homogenization, contamination, source-conditioning and layer-output capability are statistically demonstrated.

The final process traveler must explicitly label the chosen source-preparation method as **locally qualified**, not historically reconstructed, unless direct evidence is later obtained.