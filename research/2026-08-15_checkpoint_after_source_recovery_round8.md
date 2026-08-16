# Recovery checkpoint — source-recovery round 8

**Date:** 2026-08-15 America/New_York

**Purpose:** Fast handoff after the upstream source-synthesis / melt-inventory / substrate-face round. Read after `AGENTS.md` and round-7 checkpoint.

## 1. New controlled upstream files

Round 8 introduced or consolidated:

- `procedures/P03C_TE_RICH_SOURCE_SYNTHESIS_HOMOGENIZATION_QUALIFICATION.md`
- `procedures/P03D_LPE_MELT_INVENTORY_DEPLETION_QUALIFICATION.md`
- `procedures/P07B_CZT_FACE_MISCUT_LPE_SELECTION_QUALIFICATION.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND8.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND8.md`

## 2. Historical Honeywell source-synthesis boundary is now explicit

The composition-matched Bowers–Schmit x≈0.30 Te-rich branch remains:

- `xL=.082`;
- `yL=.810`;
- `TL=507 °C`;
- historical `xS≈.29`;
- derived mass fractions Hg=.249738, Cd=.012502, Te=.737760.

Full patent re-audit confirms the growth charge is treated as an **already prepared Te-rich input**.

The public Honeywell sources do not state whether this charge was synthesized by:

- direct elemental reaction;
- pre-reacted binaries/ternary;
- a cast source ingot;
- in-situ Hg-vapor equilibration;
- or another route.

Therefore source synthesis remains historically `OPEN`.

P03C closes it locally by measuring:

`{mass closure, actual composition, homogenization state, liquidus/growth behavior, output x/thickness, mobility/lifetime, source conditioning/reuse}`.

## 3. Do not import the earlier Honeywell pseudobinary source process

An earlier Honeywell near-pseudobinary process cast approximately 13–15 g HgCdTe source material and used much higher-temperature source melting around ~800 °C.

That process is a different liquid-chemistry branch and must not be spliced into the later Te-rich xL=.082/yL=.810 source.

## 4. Radhakrishnan source synthesis is a candidate method only

Radhakrishnan/Sitharaman/Gupta 2003, DOI `10.1016/S0022-0248(02)02530-7`, directly reports for its different x≈.20 Te-rich branch:

- 10 g synthesized source compound;
- 6N elemental Cd/Te/Hg;
- evacuated quartz ampoule;
- 700 °C / 8 h synthesis;
- synthesized charge ground and thoroughly mixed;
- ~4.8 g used per growth run;
- 3 g HgTe compensation;
- 15×15×1-mm CdZnTe recess.

Use this only as a candidate **source-preparation methodology**.

Never combine its 4.8-g/3-g numbers with the Honeywell x≈.30 composition and call the result published.

## 5. Alternative in-situ source preparation remains a separate branch

A 1988 JCG study, DOI `10.1016/0022-0248(88)90189-3`, demonstrates in-situ Te-rich source preparation by transporting Hg vapor into a Cd-rich Te melt.

This proves separate ampoule source synthesis is not mandatory in principle.

It is a different process family, not the historical Honeywell method.

## 6. Historical Honeywell melt mass/well volume are genuinely absent

US4317689A describes:

- tapered through-wells;
- a plug over the growth solution;
- substrate-sized recessed contact regions;
- Hg-source well/moats;
- growth near 500 °C.

It does **not** disclose:

- well diameter;
- well depth;
- well volume;
- melt depth;
- charge mass;
- source-use count.

Targeted full-text searches for gram/volume/dimension values found none.

Do not manufacture a Honeywell charge mass from drawings.

## 7. P03D — finite melt inventory/depletion is now controlled

Sanz-Maudes/Sangrador/Rodriguez et al. 1990, DOI `10.1016/0022-0248(90)90076-W`, explicitly models finite Te-rich liquid dimensions and Hg loss.

Key physical result:

- for times beyond a characteristic time related to liquid thickness, growth rate decreases;
- Hg loss makes the grown layer Cd-richer;
- outcome depends on liquid dimensions and Hg-loss flux.

Thus “small melt volume” is not equivalent to “depletion irrelevant.”

P03D requires local dimensioned well geometry, charge mass -> liquid inventory/depth conversion, and source-run-order drift tracking.

Core response:

`d_layer = f(t_growth, ΔT, thermal trajectory, liquid inventory/depth, source-use index, Hg-loss state)`.

Release a source depletion/use limit from actual output drift, not arbitrary run count.

## 8. Independent x=.30 Hg-loss-control evidence

Suh et al. 1992, DOI `10.1016/0022-0248(92)90152-9`, grew slider-LPE material with x=.2, .3 and .7 and specifically used a graphite button between the growth-solution and HgTe wells to keep solution composition constant / control Hg loss.

Use this as **independent composition-matched proof that Hg-loss geometry materially affects reproducibility**.

Do not transplant its graphite-button architecture into Honeywell without creating a separate boat/process branch.

## 9. P07B — composition-matched miscut evidence improved

Kwak/Lim/Choi/Kim/Suh 1991 studied Te-rich slider LPE of Hg0.7Cd0.3Te on `(111)Cd` CdTe.

Direct abstract-level findings:

- substrates deliberately misoriented by different magnitudes/directions;
- at 1° miscut, terrace fronts are perpendicular to misorientation direction;
- terrace width decreases and height increases with increasing miscut;
- above ~2°, terraces begin transforming toward wave-like morphology;
- initial growth attributed to step bunching;
- dislocations increasingly matter when terrace width reaches roughly 10–30 µm.

This narrows P07B's local composition-matched screening neighborhood to low-degree miscut, particularly around 0–2°.

Important restrictions:

- substrate was CdTe, not CdZnTe;
- independent process, not Honeywell;
- `(111)Cd` is a candidate/DOE anchor, not historical RP-01 polarity closure.

## 10. x=.30 morphology also evolves with growth time

Independent 1990 x=.30 slider work reports early wave-like morphology gradually changing to terrace-like morphology with growth time and increasing terrace width.

Therefore P07B face/miscut conclusions must be interpreted jointly with P03B growth-time/supercooling state.

Do not optimize orientation from one fixed growth-time micrograph.

## 11. Upstream control chain now established

The upstream local qualification chain is now:

`P07/P07A/P07B substrate -> P03C source synthesis -> P03D melt inventory/Hg-loss/depletion -> P03B time/supercooling -> wipe-off -> P06 optical/thickness map -> P04/P04A Hg anneal -> P05 transport -> P13 lifetime/device proxy`.

A process is not accepted because it hits x alone.

## 12. Highest-value upstream blockers after round 8

Historical variables still open:

1. exact Honeywell x≈.30 source synthesis;
2. Honeywell growth-well dimensions/charge mass;
3. exact RP-01/Honeywell CdZnTe polarity/miscut;
4. exact x≈.30 substrate final surface treatment;
5. exact Honeywell equilibration duration/thermal trajectory for the x=.29 tie line;
6. local source-use/depletion limit;
7. exact post-growth Hg anneal required for RP-01's low-density n transport state.

However, items 1–4 now have controlled local qualification paths; they are no longer unbounded blanks.

## 13. Recommended next work

Do not continue ordinary web searches for Honeywell source mass or well dimensions unless a new drawing archive or internal process document appears.

The strongest next paths are:

- recover/qualify the **equilibration criterion and thermal-uniformity requirement** for the x=.29 tie line;
- tighten **P07A final surface preparation** using x≈.30 primary/near-primary LPE sources;
- quantify the **Hg anneal state map** further;
- or move to statistical process capability/release criteria tying the now-defined Pxx modules together.

## 14. Recovery order

1. `AGENTS.md`
2. this checkpoint after round 7
3. `docs/SOURCE_LEDGER_ADDENDUM_ROUND8.md`
4. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND8.md`
5. P03C/P03D/P07B
6. P03/P03A/P03B/P07/P07A for broader context.
