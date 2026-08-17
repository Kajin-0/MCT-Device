# Source-ledger addendum — Round 63 targeted LPE recovery

**Date:** 2026-08-17 America/New_York  
**Use with:** `docs/RP01_TARGETED_LPE_CLOSURE_ROUND63.md`

## Evidence rule

Both recovered papers are peer-reviewed primary experiments but originate outside the Smith/UWA/Fermionics RP-01 line. Every numerical value below is therefore `PT` unless explicitly marked `DER`. Apparatus similarity does not promote these values to `RP` or `SL`.

## R63-S01 — Suh et al. 1992 — `PT`

S. H. Suh, S. W. Moon, J. S. Kim, S. W. Lim, N. J. Kwak, H. K. Kim, J. M. Kim, “Slider liquid phase epitaxial growth of Hg0.8Cd0.2Te, Hg0.7Cd0.3Te and Hg0.3Cd0.7Te with precise control of alloy compositions,” *Journal of Crystal Growth* 121 (1992) 417–422.

### Recovered apparatus/process coordinates

- high-purity graphite slider boat;
- separate solution and HgTe wells under a tightly bolted graphite cover;
- conical graphite button over the solution well;
- central-hole vapor throttle for x≈0.2 and x≈0.3 branches;
- Hg influx modeled as proportional to `D(P_HgTe-P_solution)d_hole^2/t_button`;
- external Hg loss depends separately on slider/body gap;
- target is near-zero net solution-weight change over the cycle.

### x≈0.30-specific branch

For nominal Hg0.7Cd0.3Te:

- growth-solution elemental mole fractions approximately `Hg0.158 Cd0.012 Te0.830`;
- equivalent `DER` Round-61 notation: `xL≈0.0706, yL=0.830`;
- growth-temperature range approximately `500–489 °C`;
- graphite-button central-hole diameter near `2 mm` produced near-zero net solution-mass change in that boat;
- source solution mass about `2.5 g` per run;
- source compounded in vacuum-sealed quartz at `700 °C / 12 h`, then water quenched;
- homogenization approximately `20 °C` above liquidus;
- substrate contact approximately `1 °C` below liquidus;
- slow cooling/ramp about `0.3 °C/min` during the relevant stage;
- growth about `30 min`;
- rapid separation/cooldown after growth.

### Material outcomes

- average run-to-run x approximately `0.304`;
- run-to-run standard deviation approximately `0.003`;
- within-layer composition variation approximately `±0.002`;
- interface width approximately `2–3 µm`;
- mirror-like surfaces, generally with terrace-like morphology for x≈0.2/0.3 material.

### Transfer restriction

The 2-mm button hole is not a universal x≈0.30 geometry. It is the solution of a gas-transport balance in Suh's specific well/cover/slider geometry. Transfer the measured state and zero-mass-change objective, not the dimension alone.

Disposition: P03B/P03C/P03D/P03E/P30 strengthened.

---

## R63-S02 — Shinohara et al. 1994 — `PT`

M. Shinohara, Nugraha, Y. Noda, Y. Furukawa, “Hg-loss compensation and wiping-off of source liquid on slider liquid phase epitaxy of Hg1-xCdxTe,” *Journal of Crystal Growth* 141 (1994) 352–356.

### Recovered apparatus/process coordinates

- conventional graphite slider LPE boat with HgTe reservoir;
- transparent quartz process tube, `100 mm ID`;
- gold-image furnace;
- H2 atmosphere at `1 atm`;
- H2 flow `0.5 L/min`;
- source temperature `746 K` (~473 °C);
- source melting point `727 K` (~454 °C);
- heating/homogenization to growth start about `130 min`;
- growth period `30 min`;
- HgTe reservoir inventory `2 g` and `3 g` compared, with 3 g giving more stable compensation behavior;
- source and reservoir weighed to characterize Hg transfer/loss.

### Growth/wipe branches

Substrates:

- `(111)` CdTe or Cd0.97Zn0.03Te;
- `10 × 10 × 1 mm`;
- both sides chemically etched in `3% Br2/methanol`.

Four thermal modes were studied. Key outcomes:

- `DeltaT=15 K` supercooling/step-cooling branches: approximately `30–41 µm` layers;
- equilibrium cooling (`DeltaT=0`) at `0.06–0.15 K/min`: approximately `2–4 µm` layers and best wipe behavior.

### x≈0.31 complete-wipe branch — CZT4

- Cd0.97Zn0.03Te substrate;
- equilibrium cooling;
- `0.15 K/min`;
- complete wipe across `10 × 10 mm`;
- slider-bottom/substrate-surface clearance approximately `20 µm`;
- authors identify clearance variation below roughly `5 µm` as important for large-area specular wiping;
- layer thickness approximately `4 µm`;
- interdiffusion boundary approximately `2 µm`;
- composition approximately `x=0.31`;
- surface specular/slightly terraced.

A second equilibrium-cooling branch used approximately `20–25 µm` clearance.

### Hg mass-balance result

Despite continued Hg-vapor supply, the source liquid lost approximately `0.014 g` over the growth period in the discussed branch. The paper associates Hg loss with Cd-rich composition shift, while also identifying substrate dissolution and phase-diagram interpolation uncertainty as contributors.

### Transfer restriction

The 20-µm clearance is a particularly valuable PT apparatus coordinate but is not the RP-01 historical clearance and is not a universal optimum. The complete-wipe result also produced only ~4-µm material, so it cannot replace the RP-01 ~9.5-µm thickness target.

Disposition: P03B/P03D/P30 wipe/Hg-loss state materially strengthened.

---

## Round-63 net effect

Before these full texts, the evidence corpus had:

- qualitative/indirect numerical wipe-clearance evidence;
- Hg-source inventory and vapor-path concepts;
- x≈0.30 Honeywell tie-line thermodynamics;
- Radhakrishnan geometry-coupled charge/Hg-source mass;
- Astles/Chiang/Chen Hg-loss-control branches.

Round 63 adds:

1. a relevant numerical x≈0.31 wipe-clearance branch (`20 µm`, with 20–25 µm observed and <5 µm variation warning);
2. an x≈0.30-specific vapor-throttle geometry (`~2 mm` central hole in Suh's apparatus);
3. an independent x≈0.30 Te-rich liquid composition and 500–489 °C growth branch;
4. x≈0.30 composition repeatability/uniformity benchmarks;
5. direct source/reservoir mass-vs-time evidence and a measured ~0.014-g growth-window loss;
6. independent 700 °C source-synthesis evidence at 12 h.

Historical RP-01 machine dimensions remain OPEN.