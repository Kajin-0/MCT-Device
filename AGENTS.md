# AGENTS.md — MCT-Device continuity record

## Mission

Develop an extremely detailed, source-traceable procedure for fabricating and characterizing HgCdTe photodetectors. The endpoint is a booklet/manual plus process travelers specifying measurements, metrics, times, equipment, machinery, tolerances, calibration requirements, acceptance criteria, failure modes, and provenance sufficiently well that a competent researcher can reproduce the selected reference process without undocumented tribal knowledge.

## Non-negotiable research rules

1. **Never fabricate missing numbers.** `[OPEN]` or `[QUAL]` is better than a plausible but unsupported setpoint.
2. **Do not splice process families casually.** Composition, substrate, melt chemistry, Hg chemical potential, thermal history, surface treatment, passivation, etch history and doping are coupled.
3. **Primary literature first.** Reviews/books are maps; process-critical numbers should be traced to original experimental sources or official metrology documentation where possible.
4. **Separate evidence classes:** directly published observation, derived physics, apparatus calibration, local qualification experiment.
5. **Preserve rejected branches and corrections.** Record why a seemingly useful recipe was not promoted.
6. **Every critical process step needs metrology.** A furnace/RIE/etch setpoint without measured material outcome is incomplete.
7. **Every module needs a gate.** State what must be true before the sample advances.
8. **Safety is part of reproducibility.** Hg, Cd, Br2/HBr/KOH chemistry, high-temperature graphite/quartz systems, H2/CH4 plasma, vacuum/pressure systems and cryogens require institution-approved EH&S procedures. Repo documents are scientific specifications, not operating authorization.
9. **Do not collapse distinct spectral quantities.** Transmission edge, optical band gap, inferred x and detector-response cutoff must remain separately defined.
10. **Do not collapse Hall quantities.** Report Hall density/mobility unless Hall-factor and multicarrier assumptions have been justified.

---

# RP-01 — first canonical reference process

Primary anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

RP-01 was selected because actual n-type HgCdTe photoconductors were fabricated and characterized and the downstream process is unusually well documented.

## RP-01 starting material — directly stated

- LPE-grown HgCdTe on electrically insulating CdZnTe.
- approximately x=0.30, n-type.
- supplier-specified carrier density: `9.8×10^14 cm^-3`.
- supplier-specified electron mobility: `4.0×10^4 cm²/V·s`.
- experimental device-layer thickness: `9.5 µm`.

**Important 2026-08-15 audit result:** Smith et al. give no measurement temperature for the Fermionics-specified `n` and `µ`. Do not relabel those historical values as “77 K” or “80 K.” Temperature remains `OPEN`.

## RP-01 contact-window RIE — directly stated

- Plasma Technology parallel-plate reactor.
- CH4/5H2 gas mixture.
- total gas flow `64 sccm`.
- pressure `100 mTorr`.
- RF power `50 W`.
- time `1 min`.
- RIE-converted density `2.0×10^15 cm^-3`.
- RIE-converted mobility `3.3×10^4 cm²/V·s`.

Smith et al. explicitly state that RIE-converted material was measured at **80 K and 300 K using a van der Pauw structure and variable magnetic field up to 2 T**. The currently available text does not yet assign the reported summary density/mobility pair unambiguously to one temperature.

## RP-01 lithography/passivation/metallization — directly stated

- photoresist thickness approximately `4–5 µm`.
- prebake `80 °C`, `30 min`.
- chlorobenzene soak `30 min`.
- anodic oxide `800 Å = 80 nm`.
- Cr `300 Å`.
- Au `2700 Å`.

Still open: resist identity, exposure dose, developer, develop time, exact anodization recipe, metal-deposition method/base pressure/rate, lift-off solvent/time, RIE-to-metal delay.

## RP-01 TLM structure — directly stated

- nine contacts.
- each `300 µm × 300 µm`.
- first separation `50 µm`.
- successive separation increment `50 µm`.
- 80-K specific contact resistivity `~9×10^-4 Ω·cm²`.

## RP-01 detector benchmark — directly stated

- detector operating temperature `80 K`.
- FOV `60°`.
- chopping frequency `1 kHz`.
- representative noise field `10 V/cm`.
- HP35665A analyzer + low-noise preamp.
- 1/f knee ~`3 kHz`.
- g-r noise ~`24.5 nV/√Hz`.
- detector spectral cutoff reported near `4.4 µm`.
- BLIP `D*≈2.0×10^11 cm·Hz^1/2/W` at `4 µm`.
- reported 300-K/60° background photon flux `1.0×10^15 cm^-2 s^-1`.
- QE `~70%`.

---

# Controlled process architecture

Current coherent RP-01 reconstruction:

1. qualify semi-insulating CdZnTe substrate;
2. synthesize/prepare composition-matched Te-rich LPE source;
3. grow x≈0.30 HgCdTe in a Hg-contained horizontal-slider system;
4. inspect/map as-grown thickness, composition and electrical state;
5. Hg-overpressure anneal to the required n-type state;
6. repeat FTIR + Hall gates;
7. wet-chemical mesa isolation;
8. native anodic-oxide passivation;
9. contact-window lithography;
10. localized CH4/H2 RIE only under contact regions;
11. Cr/Au deposition/lift-off;
12. TLM/contact QC;
13. detector packaging/interconnection;
14. electrical, spectral, noise, temporal and absolute-performance characterization.

This is a controlled **architecture**, not yet a released end-to-end traveler.

---

# P01 — wet mesa qualification

Same-UWA-lineage detector work establishes the architectural decision: wet mesa isolation is preferred over blanket H2/CH4 RIE mesa processing for this photoconductor branch.

Primary same-lineage source:

E. P. G. Smith et al., “H2-based dry plasma etching for mesa structuring of HgCdTe,” *J. Electron. Mater.* 29, 853–858 (2000), DOI `10.1007/s11664-000-0237-7`.

Quantitative transfer source near RP-01 composition:

V. Srivastav et al., *J. Electron. Mater.* 34, 1440–1445 (2005), DOI `10.1007/s11664-005-0203-5`, x=0.28:

- selected `2% Br2` in `3:1 EG:HBr`;
- 21 °C mean vertical rate `2.78 µm/min`;
- process variation ~`±26%`;
- anisotropy `A≈0.63 ±11%`;
- best reported RMS roughness ~`2 nm`;
- 5–50 °C investigated;
- rate approximately doubles per +10 °C;
- lower temperature improves dimensional control.

**Release blocker:** accessible primary text does not unambiguously define the concentration basis of “2% Br2.” Do not invent w/v, v/v or mass fraction.

File: `procedures/P01_WET_MESA_QUALIFICATION.md`.

---

# P02 — anodic-oxide qualification

RP-01 closes the target film thickness (`800 Å`) but not the recipe.

Strong historical transfer candidate from a TI primary process disclosure:

- `0.1 M KOH`;
- `90% ethylene glycol / 10% DI water`;
- constant current ~`0.3 mA/cm²`;
- formation endpoint ~`15 V`;
- ~`2 min`;
- resulting native oxide ~`800 Å`.

Independent HgCdTe experiments support the same electrolyte family and 0.2–0.5 mA/cm² constant-current regime.

**Do not call this the exact UWA recipe.** It remains a transfer candidate until lineage or local x≈0.30 qualification closes interface/electrical behavior and compatibility with contact-window RIE.

File: `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`.

---

# P03 — x≈0.30 Te-rich horizontal-slider LPE qualification

## Corrected core article

DOI `10.1016/0022-0248(82)90468-7` is:

J. L. Schmit, R. J. Hager, R. A. Wood, “Liquid phase epitaxy of Hg1−xCdxTe,” *Journal of Crystal Growth* 56, 485–489 (1982).

Earlier project attribution to “Tung et al.” was wrong. The paper explicitly includes x=0.2, 0.3 and 0.4 growth.

## Best composition-matched tie line

Bowers–Schmit, U.S. Patent 4,317,689, same Honeywell/Schmit Te-rich-slider lineage:

- liquid metal Cd fraction `xL=0.082`;
- liquid Te fraction `yL=0.810`;
- liquidus `TL=507 °C`;
- grown solid `xS=0.29`;
- `xS/xL=3.54`.

Derived elemental mole fractions:

- Hg `0.17442`;
- Cd `0.01558`;
- Te `0.81000`.

Derived mass fractions:

- Hg `0.249738`;
- Cd `0.012502`;
- Te `0.737760`.

For total selected charge mass `M`:

- `mHg=0.249738M`;
- `mCd=0.012502M`;
- `mTe=0.737760M`.

**Total charge mass remains OPEN/CAL.** Do not combine Radhakrishnan's 4.8-g charge with this Honeywell composition and call the combination published.

## Charge metrology sensitivity

File: `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`.

At a hypothetical 5.000-g charge, nominal Cd mass is only ~62.508 mg. A +0.1-mg Cd error gives `δxL≈+1.20×10^-4`, while +0.1 mg Hg gives only `δxL≈−6.0×10^-6`. Cd weighing precision dominates direct xL error.

Balance selection must therefore be based on propagated composition uncertainty near the **tens-of-milligrams Cd range**, not simply nominal balance readability.

## LPE apparatus architecture

Bowers–Schmit supports:

- covered graphite horizontal slider;
- separate HgTe or HgTe+Te vapor source;
- Hg-distribution grooves/moats;
- quartz tube;
- N2 purge before heating;
- flowing H2;
- heat above liquidus then grow below liquidus;
- operation near 500 °C for the selected branch.

For `TL=507 °C`, `Tgrowth≈500 °C` corresponds to derived `ΔT≈7 °C`; this is a qualification center point, not a released setpoint.

Radhakrishnan et al. 2003 contributes engineering/process ideas, not the x≈0.30 composition:

- high-density graphite;
- `15×15×1 mm` CdZnTe recess;
- 6N Hg/Cd/Te;
- evacuated-ampoule source synthesis `700 °C / 8 h` for their composition;
- ~4.8 g/run and 3 g HgTe in their apparatus;
- in-situ meltback;
- improved wipe-off geometry.

Do not transfer their 4.8-g/3-g masses blindly into the Honeywell composition branch.

File: `procedures/P03_LPE_X030_QUALIFICATION.md`.

---

# LPE wipe-off architecture

Correct high-value patent:

**US4592304A**, “Apparatus for liquid phase epitaxy of mercury cadmium telluride.”

Important correction: an earlier note pointing to US4706604 was wrong for this purpose.

The patent uses:

- dedicated wipe-off well adjacent to growth well;
- loose unpolished polycrystalline CdTe pieces;
- pieces in vertical slots roughly `1 mm` apart;
- slider motion draws the pieces across the grown layer;
- melt removed by mechanical wiping + surface-tension adhesion + capillary wicking;
- wipe well maintained under the same Hg-rich environment;
- CdTe wipe pieces discarded after cooldown.

Still open:

- translation speed;
- exact wiper dimensions/contact force;
- wipe temperature;
- scratch tolerance;
- residual-droplet acceptance limits.

Research record: `research/2026-08-15_wipeoff_and_hg_anneal.md`.

---

# CdZnTe substrate branch

RP-01 closes the substrate family as insulating CdZnTe.

Tranchart et al. 1985 support CdZnTe around y≈0.04 for x≈0.30 Te-rich LPE detector material. Separate lattice-matching primary work gives an optimum ZnTe fraction around 2.9 mol% for Hg0.7Cd0.3Te.

Therefore:

- do not declare one universal “exact 4% Zn” number;
- release substrate based on measured lattice mismatch, orientation, miscut and quality;
- {111} family is strongly supported for Te-rich LPE, but exact RP-01 face/miscut remains open.

---

# P04 — Hg-overpressure anneal qualification

File: `procedures/P04_HG_ANNEAL_QUALIFICATION.md`.

Primary Harman process anchor, US Patent 4,642,142:

- anneal regime broadly `200–300 °C`;
- Hg partial pressure broadly `0.1–250 Torr`, selected according to defect state;
- pseudo-isothermal Hg-saturated example `250 °C / 1 h`;
- then cool to room temperature;
- sample temperature and Hg chemical potential are both state variables;
- this specific process typically ended in the low `10^16 cm^-3` carrier-density range.

Thus `250 °C / 1 h` is a legitimate kinetic screening anchor but **not** an RP-01 electrical endpoint.

Nagahama branch, x≈0.17–0.30:

- as-grown p-type;
- Hg-overpressure anneal studied 250–400 °C;
- 250–300 °C produced well-behaved n-type material without apparent composition change;
- 400 °C produced interface-region composition change.

Chandra–Schaake–Kinch 2003:

- anneal kinetics depend on x, vacancy concentration and temperature;
- rate decreases with increasing x over the investigated range;
- for x above roughly 0.26, incomplete metal-vacancy ionization at 77 K complicates electrical inference of defect state.

**P04 control principle:** final state is defined by measured `(carrier sign, n_H/transport state, mobility, optical composition/edge, thickness, morphology)`, not temperature×time alone.

Initial qualification DOE in P04 brackets `250 °C / 1 h` with time/temperature/Hg-chemical-potential variation, but these are qualification experiments, not a released recipe.

---

# P05 — Hall / van der Pauw material metrology

File: `procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md`.

Status: controlled qualification metrology.

Key decisions:

- report `n_H/p_H` and `µ_H` unless Hall-factor/multicarrier correction is explicitly justified;
- use small peripheral ohmic contacts on a valid van der Pauw geometry;
- measure in darkness at recorded temperature;
- current-linearity/self-heating screening before selecting drive current;
- eight zero-field current-reversal/reciprocity measurements;
- solve full van der Pauw equation, not a symmetry approximation unless justified;
- symmetric variable-B sweep during process qualification;
- current reversal + magnetic-field reversal;
- retain all raw voltages/fields/currents/temperatures;
- antisymmetrize Hall voltage in B;
- test Hall linearity before one-carrier reduction;
- escalate to multicarrier/mobility-spectrum analysis when curvature/sign changes/unexplained MR appear.

NIST consistency gate adopted:

- `≤3%`: routine PASS;
- `>3–5%`: conditional/repeat/investigate;
- `>5%`: fail basic van der Pauw reduction.

NIST general field-uniformity guidance: ~3%; current and field reversals required for offset control.

Initial proposed qualification field grid for RP-01-like n material:

`B = 0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T`.

This is a project qualification grid, not an original RP-01 setting.

Derived RP-01 one-carrier benchmark for `n=9.8×10^14 cm^-3`, `µ=4×10^4 cm²/Vs`, `t=9.5 µm`:

- `ρ≈0.1592 Ω·cm`;
- `Rs≈167.6 Ω/square`;
- `|RH|≈6.37×10^3 cm³/C`;
- at `I=100 µA`, `B=0.10 T`, ideal `|VH|≈6.70 mV`.

Research record: `research/2026-08-15_hall_metrology_and_rp01_temperature.md`.

---

# P06 — FTIR composition/thickness mapping

File: `procedures/P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`.

Status: controlled qualification metrology.

Core rule: keep separate

- measured transmission edge;
- optically inferred band gap;
- inferred alloy x;
- detector-response cutoff.

Hougen 1989, DOI `10.1063/1.344038`, is the preferred primary model lineage because it explicitly models LPE HgCdTe transmission including thickness, composition profile, surface nonuniformity and back reflection.

Preferred method:

- spatial FTIR transmission map;
- retain raw spectrum;
- report a traceable normalized edge metric such as `λ_50T` separately;
- use low-absorption interference fringes for thickness information;
- full-spectrum physical fit preferred over one-point composition conversion;
- cross-calibrate FTIR thickness against independent profilometry/cross section during process qualification;
- before/after anneal measurements at identical coordinates and method version.

Initial project method candidates:

- spectral range roughly `500–5000 cm^-1` for x≈0.30 MWIR material;
- resolution `≤4 cm^-1` during qualification;
- minimum 9-point spatial map; 5×5 or denser preferred for LPE process development.

These are project qualification settings, not RP-01 published settings.

### Important RP-01 spectral consistency observation

Hansen relation at `x=0.30`, `80 K` gives:

- `Eg≈0.243684 eV`;
- band-gap-equivalent `hc/Eg≈5.09 µm`.

RP-01 detector-response cutoff is reported around `4.4 µm` at 80 K.

Do not declare this a contradiction. `x≈0.30` is approximate, detector cutoff is convention/device dependent, and finite absorption/optical structure/grading matter. It is evidence that the manual must not force `λ_det=hc/Eg`.

---

# Current controlled modules

1. `procedures/P01_WET_MESA_QUALIFICATION.md`
2. `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`
3. `procedures/P03_LPE_X030_QUALIFICATION.md`
4. `procedures/P04_HG_ANNEAL_QUALIFICATION.md`
5. `procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md`
6. `procedures/P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`

Supporting calculations:

- `calculations/HANSEN_BANDGAP_MODEL.md`
- `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`

Research records preserve initial reasoning, mesa lineage, passivation lineage, LPE reconciliation, wipe-off/anneal and Hall audit.

---

# Highest-priority open variables

## Upstream growth/material

- full Schmit–Hager–Wood 1982 experimental section;
- exact CdZnTe orientation/miscut and measured mismatch target;
- substrate polish/clean and in-situ interface preparation;
- selected boat/well dimensions and total charge mass;
- exact x≈0.30 source synthesis/homogenization process;
- N2 purge/H2 flow/purity criteria;
- Hg-source capacity/free-volume rule;
- equilibrium hold criterion;
- exact supercooling/cooling trajectory;
- growth-time/thickness calibration to 9.5 µm;
- wipe-off translation speed and acceptance limits;
- exact anneal Hg source/pressure/time/cooldown to hit target transport state;
- precise production FTIR x/thickness uniformity limits;
- final Hall acceptance windows and Hall-factor convention.

## Downstream fabrication

- exact detector active dimensions;
- Mask-1 resist/exposure/develop process;
- Br2 2% concentration basis and post-etch quench/rinse;
- exact UWA anodization lineage or local P02 qualification;
- Mask-2 resist identity/exposure/develop;
- RIE electrode geometry, DC self-bias, sample temperature, etch rate and conversion depth;
- Cr/Au deposition method, base pressure, rates, sample temperature and transfer delay;
- lift-off method;
- die attach and wire bond;
- package optical/thermal geometry.

## Final characterization

- calibrated electrical bias/load network;
- absolute responsivity radiometry;
- blackbody/aperture/FOV calibration;
- noise preamplifier model and full PSD/ENBW chain;
- bandwidth/lifetime procedure;
- final D* uncertainty budget.

---

# Most natural next work

1. Close **substrate preparation and orientation/miscut** from primary LPE sources.
2. Close **RIE conversion depth / reactor transfer variables** from same-UWA primary work.
3. Close **metal deposition and vacuum transfer** from the UWA/Faraone lineage.
4. Build a controlled **material morphology/crystal-quality metrology** module: Nomarski/optical defect map, XRD rocking curve, EPD/defect metric and acceptance schema.
5. Build a controlled **spectral-responsivity/radiometry** module once the downstream device geometry is sufficiently closed.
6. Keep `docs/RP01_GAP_MATRIX.md` and dated research records synchronized after each branch.
