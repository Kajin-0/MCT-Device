# Research checkpoint — through P12

**Timestamp:** 2026-08-15, America/New_York  
**Purpose:** Fast recovery checkpoint for a replacement agent. This file records the current scientific frontier and the exact state of the controlled procedure set. It supplements `AGENTS.md`, the procedure files, source ledger, and closure matrix.

## Canonical objective

Construct a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual around RP-01, the n-type MWIR photoconductor process anchored to Smith et al. 2001, DOI `10.1088/0268-1242/16/6/306`.

The manual must distinguish:

- directly published values;
- derived quantities;
- apparatus calibration requirements;
- local qualification experiments;
- unresolved variables.

Never invent a missing process setpoint or silently merge incompatible process families.

## Controlled modules currently present

1. `P01_WET_MESA_QUALIFICATION.md`
2. `P02_ANODIC_OXIDE_QUALIFICATION.md`
3. `P03_LPE_X030_QUALIFICATION.md`
4. `P04_HG_ANNEAL_QUALIFICATION.md`
5. `P05_HALL_VDP_MATERIAL_METROLOGY.md`
6. `P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`
7. `P07_CZT_SUBSTRATE_QUALIFICATION.md`
8. `P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`
9. `P09_CR_AU_METALLIZATION_TLM_QUALIFICATION.md`
10. `P10_DEVICE_DC_BIAS_SELF_HEATING.md`
11. `P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md`
12. `P12_NOISE_PSD_NEP_DETECTIVITY.md`

These are qualification/control modules. There is not yet an end-to-end `REPRODUCIBLE-RELEASE` traveler.

## RP-01 direct historical anchors

Starting material:

- LPE HgCdTe on electrically insulating CdZnTe;
- nominal `x≈0.30`, n-type;
- supplier carrier density `9.8×10^14 cm^-3`;
- supplier mobility `4.0×10^4 cm²/V·s`;
- layer thickness `9.5 µm`;
- supplier n/µ measurement temperature remains unknown.

Contact-window RIE:

- Plasma Technology parallel-plate reactor;
- printed gas notation `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- RF power `50 W`;
- duration `60 s`;
- converted density `~2.0×10^15 cm^-3`;
- converted mobility `~3.3×10^4 cm²/V·s`;
- exact individual CH4/H2 MFC flows unresolved.

Lithography/passivation/metallization:

- resist `~4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene soak `30 min`;
- anodic oxide `800 Å = 80 nm`;
- Cr `300 Å = 30 nm`;
- Au `2700 Å = 270 nm`.

TLM:

- nine 300×300 µm contacts;
- first gap 50 µm, successive increments 50 µm;
- historical specific contact resistivity `~9×10^-4 Ω·cm² at 80 K`.

Detector benchmark:

- `T=80 K`;
- FOV stated as 60°;
- chopping `1 kHz`;
- representative noise field `10 V/cm`;
- HP35665A plus low-noise preamp;
- 1/f knee `~3 kHz`;
- g-r floor `~24.5 nV/√Hz`;
- detector response cutoff `~4.4 µm`;
- BLIP `D*≈2.0×10^11 cm·Hz^1/2/W` at `4 µm`;
- QE `~70%`.

## Major scientific/process decisions already made

### Wet mesa, not blanket dry mesa

Same-UWA-lineage detector work shows blanket H2/CH4 dry mesa modifies the active electrical state and strongly degrades detector performance relative to wet bromine/HBr mesa processing. RIE is therefore confined to contact regions where n+ conversion is intentional.

### P01 wet mesa candidate

Best current near-composition source: x=0.28 HgCdTe, selected `2% Br2 in 3:1 EG:HBr`, 21 °C rate `~2.78 µm/min`, anisotropy `~0.63`, best RMS roughness `~2 nm`.

Critical blocker: concentration basis of `2% Br2` is not source-verified. Do not guess w/v, v/v, etc.

### P02 anodic oxide candidate

RP-01 only closes target thickness at 80 nm. Strong historical candidate:

- `0.1 M KOH`;
- `90% EG / 10% DI water`;
- constant current `~0.3 mA/cm²`;
- endpoint `~15 V`;
- `~2 min`;
- resulting oxide `~80 nm`.

Do not label this the exact UWA recipe without lineage or local x≈0.30 qualification.

### P03 x≈0.30 Te-rich LPE composition anchor

Correct core article is Schmit–Hager–Wood 1982, not the earlier mistaken attribution to Tung et al.

Best explicit Bowers–Schmit tie line:

- `xL=0.082`;
- `yL=0.810`;
- `TL=507 °C`;
- resulting `xS=0.29`;
- `xS/xL=3.54`.

Derived charge mass fractions:

- Hg `0.249738`;
- Cd `0.012502`;
- Te `0.737760`.

Total charge mass remains apparatus dependent. Do not combine Radhakrishnan's ~4.8 g charge with this composition and call it a published recipe.

### LPE architecture

Supported architecture:

- covered graphite horizontal slider;
- auxiliary HgTe or HgTe+Te source;
- N2 purge;
- H2 process atmosphere;
- heat above liquidus then grow below;
- growth near 500 °C is a valid qualification center for the selected tie line, corresponding to derived `ΔT≈7 °C` relative to `TL=507 °C`.

Wipe-off source US4592304A uses loose unpolished CdTe pieces in slots about 1 mm apart in a dedicated wipe well. Translation speed/contact force remain apparatus variables.

### P04 Hg anneal

Historical screening envelope:

- roughly 200–300 °C;
- Hg partial pressure roughly 0.1–250 Torr depending target defect state;
- Harman example `250 °C / 1 h`.

This is NOT the RP-01 endpoint because that source typically produced carrier density in the low `10^16 cm^-3` range.

Control anneal by measured final state: carrier sign, `n_H`, `µ_H`, optical composition/edge, thickness, morphology. Anneal time/temperature alone is insufficient.

### P05 Hall/VdP

Use current and field reversal, full van der Pauw solution, symmetric B sweep, raw-data retention, current-linearity/self-heating screening, and multicarrier escalation when Hall curvature or unexplained magnetoresistance occurs.

Report Hall density/mobility unless Hall-factor correction is justified.

RP-01 one-carrier consistency values for `n=9.8×10^14 cm^-3`, `µ=4×10^4 cm²/Vs`, `t=9.5 µm`:

- `ρ≈0.159 Ω·cm`;
- `Rs≈168 Ω/sq`;
- `|RH|≈6.37×10^3 cm³/C`.

### P06 FTIR

Never identify detector cutoff with `hc/Eg` by default.

Hansen at nominal `x=0.30, T=80 K` gives `Eg≈0.2437 eV` and `hc/Eg≈5.09 µm`, while RP-01 reports detector response cutoff near 4.4 µm. This is not considered a contradiction because x is approximate and transmission/material edge, band gap, and detector response cutoff are distinct quantities.

### P07 substrate

CdZnTe substrate must be qualified by measured lattice match, A/B polarity, miscut, HRXRD linewidth, EPD/dislocation state, IR inclusions/Te precipitates, impurities such as Cu, resistivity, dimensions and surface condition.

Historical high-quality benchmark: Cd0.96Zn0.04Te around `EPD≈5×10^4 cm^-2` and XRD linewidth `≈25 arcsec`; benchmark only, not released acceptance limit.

Exact A/B face and miscut remain process-dependent.

### P08 RIE blocking contact

Separate:

- oxide-clear time;
- physical HgCdTe etch/recession;
- electrical conversion depth;
- lateral conversion distance;
- resulting n+/mobility state;
- final TLM contact performance.

RP-01 cites prior similar-condition n-type work with conversion depth about 8 µm, but the exact source-condition match remains unresolved.

### P09 Cr/Au

Historical stack: 30 nm Cr / 270 nm Au.

Thermal evaporation is the leading transfer candidate from later UWA work but is not proven to be the exact RP-01 deposition method.

Base pressure, deposition rates, substrate temperature and RIE-to-metal delay remain qualification variables. Historical target is TLM `ρc≈9×10^-4 Ω·cm² at 80 K`.

### P10 device bias/self-heating

Use actual measured contact gap `L` and define field from the active-region voltage: `E=V_active/L`.

Do not compare devices at equal applied voltage when gap differs.

Derived screening result from nominal RP-01 transport and 300-µm width: at 10 V/cm ideal current is about 1.79 mA independent of gap in uniform geometry; power scales with gap. These are derived values, not measured RP-01 currents.

### P11 absolute radiometry

Preferred modern method is spectral comparison against a traceably calibrated IR transfer detector at the same optical plane.

Important consistency inference: integrating 300-K Planck photon radiance to 4.4 µm gives about `1.124×10^15 cm^-2 s^-1` for a 30° half-angle cone, almost exactly RP-01's quoted `1.0×10^15`. A 60° half-angle gives about `3.37×10^15`. Therefore the historical `60° FOV` is provisionally interpreted as approximately a 60° full cone / ±30°, but this remains an inference.

### P12 noise / NEP / D*

Maintain PSD/ASD units explicitly and subtract independent electronics contributions at PSD level, not ASD level.

Use responsivity and detector-referred noise at the same operating condition and signal frequency:

`D*(λ,f) = Rλ(f) sqrt(A) / e_n(f)`.

Historical ambiguity: RP-01 spectral response used 1-kHz chopping, while the reported 1/f knee was about 3 kHz and the white/g-r floor about 24.5 nV/√Hz. Therefore do not assume the 24.5-nV/√Hz plateau was the noise value used for the published 1-kHz D* curve. Future reproduction must evaluate noise ASD at the same signal frequency used for responsivity unless a different convention is explicitly stated.

## Current largest unresolved blockers

Upstream:

- full Schmit–Hager–Wood x≈0.30 experimental section;
- exact substrate face/miscut selected for the final slider process;
- final CdZnTe surface preparation/clean-to-load sequence;
- selected LPE well geometry and total charge mass;
- x≈0.30 source synthesis/homogenization;
- exact equilibration/supercooling/cooling profile;
- growth-time/thickness calibration;
- wipe-off translation mechanics;
- Hg anneal time/chemical-potential/cooldown required to reach RP-01 transport state.

Downstream:

- exact detector active dimensions used for each historical performance curve;
- Mask-1/Mask-2 resist identities, exposure and developer details;
- Br2 concentration basis and post-etch rinse;
- exact UWA anodic-oxide recipe or completion of local transfer qualification;
- exact CH4/H2 individual MFC flows for `CH4/5H2`;
- exact 8-µm RIE conversion-depth source conditions;
- Cr/Au base pressure/rates and transfer delay;
- lift-off details;
- packaging/die attach/wire-bond process;
- exact historical low-noise preamplifier and analyzer RBW/ENBW settings;
- exact active area/noise-frequency convention used in historical D* figure.

## Next intended module

**P13 — temporal response / frequency response / lifetime / bandwidth.**

Required distinctions:

- intrinsic detector transfer function versus external readout/electronics transfer function;
- amplitude and phase versus modulation frequency;
- `f_-3dB` and rise/fall time;
- carrier-lifetime inference only when a single-pole detector model is justified;
- transit/sweepout effects versus recombination lifetime;
- multi-pole fits when needed;
- de-embedding of source/chopper/modulator/preamp/lock-in bandwidth.

Do not fold temporal response into conventional D* without explicitly defining a generalized metric.

## Recovery order for a replacement agent

1. Read `AGENTS.md`.
2. Read this checkpoint.
3. Read `docs/RP01_GAP_MATRIX.md` and `docs/SOURCE_LEDGER.md`.
4. Read the relevant procedure file(s) for the branch being continued.
5. Read dated `research/` notes for provenance/rejected alternatives.
6. Continue by updating the procedure + source/gap state + continuity record after every material scientific advance.
