# RP-01 targeted LPE closure — Round 63

**Date:** 2026-08-17 America/New_York  
**Status:** TARGETED FULL-TEXT LPE EVIDENCE INTEGRATION  
**Baseline typeset artifact:** `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round61.pdf`  
**Controlling predecessor:** Round-62 full-text evidence integration

## 1. Trigger

Round 62 explicitly identified two final high-value literature targets before abandoning broad literature search:

1. S. H. Suh et al., *Slider liquid phase epitaxial growth of Hg0.8Cd0.2Te, Hg0.7Cd0.3Te and Hg0.3Cd0.7Te with precise control of alloy compositions*, J. Crystal Growth 121 (1992) 417–422.
2. M. Shinohara et al., *Hg-loss compensation and wiping-off of source liquid on slider liquid phase epitaxy of Hg1-xCdxTe*, J. Crystal Growth 141 (1994) 352–356.

Both full texts are now recovered. They materially strengthen the exact LPE coordinates that remained weak after Round 62: near-x≈0.30 liquid composition, Hg-vapor transport geometry, gravimetric Hg-loss control, wipe clearance and thermal/wipe coupling.

The evidence-state rule is unchanged: both papers are `PT`, not `RP` or `SL`.

---

## 2. Suh et al. 1992 — independent x≈0.30 Te-rich growth branch

### 2.1 Near-target liquid composition

For growth of nominal Hg0.7Cd0.3Te, Suh reports a Te-rich growth solution with elemental mole fractions approximately

`Hg = 0.158, Cd = 0.012, Te = 0.830`.

In the Round-61 liquid notation `(Hg_(1-xL) Cd_xL)_(1-yL) Te_yL`, this corresponds to

- `yL = 0.830`;
- `xL = 0.012/(0.158+0.012) ≈ 0.0706`.

The reported growth-temperature range for this x≈0.30 branch is about `500–489 °C`.

### Consequence

The Honeywell composition center `xL=0.082, yL=0.810, TL=507 °C -> xS≈0.29` remains the controlling historical-compatible center, but it is no longer the only directly demonstrated near-x≈0.30 Te-rich solution in the evidence corpus. Suh adds a genuinely independent `PT` empirical neighborhood.

Do **not** average the two liquid compositions. Preserve them as separate process branches.

### 2.2 Source synthesis

Suh reports:

- high-purity elemental Cd, Te and Hg;
- source compounding in vacuum-sealed quartz tubes;
- `700 °C / 12 h` synthesis;
- water quench;
- about `2.5 g` solution used for a growth run.

### Consequence

Round 61/62 already had a different primary branch at `700 °C / 8 h` from Radhakrishnan. The new evidence independently strengthens `700 °C` as a real Te-rich HgCdTe source-synthesis temperature family, including a specifically x≈0.30 growth branch.

It **does not** justify replacing the current 8-h synthesized reference with 12 h without a local source-homogeneity study. The defensible evidence statement is now:

> Primary Te-rich slider-LPE source-synthesis branches exist at 700 °C with at least 8-h and 12-h dwells; synthesis dwell is a qualification variable, while exact RP-01/Fermionics source preparation remains OPEN.

Ampoule ID/OD/wall, free volume, seal geometry and hot pressure remain OPEN.

---

## 3. Suh Hg-loss controller — gas-phase conductance is a geometry coordinate

Suh uses two wells under a tightly bolted high-purity graphite cover:

- growth-solution well;
- HgTe well.

A conical graphite button over the solution well throttles Hg exchange. With a central hole, the paper models Hg influx qualitatively as

`J_in ∝ D (P_HgTe - P_solution) d_hole^2 / t_button`,

while Hg leakage toward the exterior is separately controlled by the slider/body gap.

The key physical result is that the solution weight change can be driven close to zero by tuning button geometry rather than merely increasing Hg-source mass.

For the nominal x≈0.30 (`Hg0.7Cd0.3Te`) branch, the reported near-zero solution-weight-change condition occurs at approximately a **2-mm button-hole diameter** in that specific apparatus.

The paper separately uses button thickness rather than a hole for the very different x≈0.7 branch; that thickness result must not be assigned to x≈0.30.

### Round-63 process coordinate

Add the dimensionless/apparatus-linked Hg-transfer state:

`G_Hg,button ∝ d_hole^2 / t_button`

with the warning that the proportionality constant depends on the complete vapor geometry and gas-phase transport state.

Mandatory observables become:

- `d_hole`;
- `t_button`;
- button/body clearance where relevant;
- slider/body clearance;
- HgTe-well/source geometry;
- solution-well geometry;
- pre/post solution mass;
- pre/post Hg-source mass;
- `T_growth(t)` and `T_Hg(t)` if separately controlled.

The local qualification objective is not “use a 2-mm hole.” It is

`Delta m_solution ≈ 0`

through the actual growth cycle while maintaining the target x/thickness/morphology.

The 2-mm value is a `PT` initial branch datum only.

---

## 4. Suh thermal/contact branch

Reported sequence:

- load solution, HgTe and substrate in the slider boat;
- heat under slowly flowing H2;
- homogenize approximately `20 °C` above the liquidus;
- cool initially rapidly and then at about `0.3 °C/min`;
- bring substrate into contact at about `1 °C` below liquidus;
- continue growth for about `30 min` while ramping temperature;
- separate and cool rapidly after growth.

### Consequence

This is strong `PT` evidence that an x≈0.30 slider process can operate with contact very near measured liquidus rather than requiring a large step supercooling. It strengthens P03B/P03E's requirement that growth be parameterized by actual `TL`, contact offset `DeltaT_contact`, and `dT/dt` rather than controller temperature alone.

It does **not** replace the current Round-61 497/500/503 °C factorial screen, which remains an explicit SYN validation design around the Honeywell center.

---

## 5. Suh composition capability — benchmark, not acceptance criterion

For the Hg0.7Cd0.3Te branch Suh reports:

- average run-to-run composition approximately `x = 0.304`;
- run-to-run standard deviation approximately `0.003` in x;
- within-layer spatial composition variation approximately `±0.002` in x;
- no discernible composition change through most of the layer thickness in the reported profile;
- interface width approximately `2–3 µm`;
- mirror-like surfaces with terrace-like morphology.

### Consequence

These are useful `PT` empirical capability benchmarks for a well-controlled x≈0.30 slider system. They are not RP-01 release specifications and should not be copied as local acceptance limits before the actual apparatus demonstrates its own repeatability.

---

## 6. Shinohara 1994 — explicit source/Hg-reservoir mass trajectory

Shinohara uses a conventional graphite slider boat with an HgTe reservoir in a transparent quartz tube of `100 mm` ID heated by a gold-image furnace.

Reported growth-system branch:

- H2 atmosphere: `1 atm`;
- H2 flow: `0.5 L/min`;
- source temperature: `746 K` (`~473 °C`);
- source melting point: `727 K` (`~454 °C`);
- growth start after approximately `130 min` heating/homogenization;
- growth period: `30 min`;
- HgTe reservoir: `2 g` or `3 g` tested, with the 3-g inventory giving more stable compensation behavior.

The source and HgTe reservoir were weighed before/after the heating cycle. The experiment therefore treats **mass trajectory** as a first-class process measurement rather than assuming the reservoir maintains equilibrium merely because it is present.

### Consequence

P03D/P30 must distinguish:

- loaded source mass;
- source mass at growth start;
- source mass after growth;
- reservoir mass before/after;
- time at temperature before contact.

A particularly important mechanism is that the source can initially **gain** Hg from the reservoir and later lose Hg. Therefore a single end-of-run mass measurement can hide the relevant growth-start composition state.

Where practical, use sacrificial/dummy time-point runs or otherwise establish a validated mass-vs-time model for the selected boat.

---

## 7. Shinohara — x≈0.31 wipe branch closes a numerical PT clearance

Shinohara studied four cooling/growth modes. The most consequential result for RP-01 reconstruction is the equilibrium-cooling wipe branch:

- `(111)` Cd0.97Zn0.03Te substrate;
- `10 × 10 × 1 mm`;
- 3% Br2/methanol pre-growth etch;
- equilibrium cooling, `DeltaT = 0 K`;
- cooling rate `0.06–0.15 K/min`;
- rapid substrate removal after growth.

For sample `CZT4`:

- cooling rate `0.15 K/min`;
- **complete wipe across the 10 × 10 mm surface**;
- slider-bottom to substrate-surface clearance approximately **20 µm**;
- authors state clearance variation below approximately **5 µm** was important for obtaining a large-area specular layer;
- grown layer thickness about `4 µm`;
- interdiffusion boundary about `2 µm`;
- layer composition about `x = 0.31`;
- surface described as specular/slightly terraced.

A second equilibrium-cooling sample used approximately `20–25 µm` clearance.

### Round-63 correction to Round 61

Round 61 states that quantitative slider/base clearance is unrecovered and that no arbitrary micron clearance should be assigned. That remains true for **historical RP-01 identity**, but it is no longer true that no relevant numerical transfer branch exists.

New state:

- historical RP-01/Fermionics clearance: `OPEN`;
- Shinohara x≈0.31 equilibrium-wipe branch: `20 µm PT`, with `20–25 µm` observed branch range and `<5 µm` within-surface clearance-variation warning;
- local first-build clearance: must be qualified against actual epilayer thickness, slider flatness, recess flushness, scratch risk and wipe completeness.

Do not use 20 µm as an asserted universal optimum.

---

## 8. Shinohara — wipe and thickness are thermally coupled

Shinohara shows a strong trade:

- equilibrium cooling from the melting point gives thin layers, about `2–4 µm`, and the best wiping;
- supercooling/step-cooling with `15 K` supercooling gives much thicker layers, about `30–41 µm`;
- the RP-01 target is approximately `9.5 µm`.

### Consequence

Wipe quality cannot be optimized independently of growth thickness. A local x≈0.30 program should therefore treat at least

`{DeltaT_contact, dT/dt, t_contact, clearance, wipe geometry}`

as a coupled response space with outputs

`{thickness, x, residual-melt fraction, scratch density, terrace morphology}`.

The Shinohara 4-µm result is **not** substituted for the 9.5-µm RP-01 target.

---

## 9. Shinohara — Hg loss during the actual growth window

In the reported branch, the source liquid lost approximately `0.014 g` during the growth period despite continued Hg-vapor supply. Relative to a roughly 2-g source scale this is approximately `0.7%` mass change.

The paper associates this Hg loss with a shift toward Cd-richer solid than the intended composition, while also noting substrate dissolution and phase-diagram interpolation uncertainty.

### Consequence

The Round-61/62 rule is strengthened:

> Composition misses cannot be attributed to temperature alone until source mass balance/Hg chemical-potential state is closed.

Mandatory LPE run outputs should include `Delta m_source`, `Delta m_Hg-reservoir`, and resulting FTIR x-map.

---

## 10. Direct supersessions of Round-61 statements

### Protocol 3 / source synthesis

Round-61 statement: the 700 °C / 8-h source-synthesis branch is the principal quantified PT implementation.

Round-63 addition: Suh gives an independent x≈0.30 slider-LPE branch synthesized at `700 °C / 12 h` in vacuum-sealed quartz and water-quenched. Therefore 700 °C is independently supported, while dwell remains a qualification coordinate.

### Protocol 4 / numerical clearance

Round-61 statement: quantitative slider/base clearance is OPEN.

Round-63 refinement: historical clearance remains OPEN, but Shinohara provides a relevant `20 µm` PT branch at x≈0.31 with a `20–25 µm` observed range and `<5 µm` clearance-variation warning.

### Protocol 4 / Hg-loss controller

Round-61 state emphasizes Hg source mass/area/vapor volume.

Round-63 addition: Suh directly demonstrates a graphite vapor-throttle geometry; for its x≈0.30 branch, approximately `2 mm` central-hole diameter drove solution mass change near zero. Geometry is a Hg chemical-potential control coordinate, not merely a mechanical detail.

### Protocol 4 / wipe thermal trajectory

Round-61 uses a synthesized 500 °C / 5-min center and a Honeywell-derived wipe architecture.

Round-63 addition: Shinohara demonstrates complete wiping under an equilibrium-cooling branch at `0.15 K/min` and ~20-µm clearance but at only ~4-µm thickness. This is a PT mechanical/thermal branch and should be used to design qualification, not replace the RP-01 thickness target.

---

## 11. Remaining LPE OPEN coordinates after Round 63

Still genuinely OPEN for historical RP-01/Fermionics material:

- full base/slider/cover/well/recess numerical machine drawing;
- actual historical slider/base and epilayer clearance;
- actual Hg-vapor throttle/button geometry, if any;
- exact growth-well area/depth and melt depth;
- exact Hg-source exposed area/location/vapor path;
- exact graphite grade/finish/clean;
- source-synthesis ampoule ID/OD/wall/free volume/seal and hot pressure;
- actual historical source-synthesis dwell/mixing route;
- exact historical contact temperature, supercooling, cooling rate and growth time;
- exact wipe hardware generation and slider actuation dynamics;
- source reuse/depletion history.

These are now a substantially narrower set. Broad literature search is no longer justified.

---

## 12. Publication consequence

Round 63 is the controlling targeted LPE evidence layer after Round 62.

A typeset Round-63 artifact should preserve the released Round-61 body as the visual baseline and attach a controlled supersession/addendum rather than silently rewriting historical pages without the original TeX source. The addendum must explicitly mark every changed evidence state and retain the rule that transferred values do not become RP-01 historical facts.