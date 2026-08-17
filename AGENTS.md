# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 61  
**Date:** 2026-08-17 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Produce an **Exhaustive Empirical Fabrication Protocol (EEFP)** for HgCdTe photoconductor fabrication and characterization: a hybrid of a scientific methods monograph, an SOP-level executable protocol, and an internal R&D process-development reference.

The governing question is:

> What exactly does the researcher do, with what material, apparatus geometry, quantity, timing, physical state, measurement, calculation, endpoint, failure response, and retained raw data?

The document is not a manufacturing-control package. Do not add operator signoff forms, lot-release fields, capability-index requirements, or production-control charts merely to make the document look industrial.

Canonical downstream anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_CONSEQUENTIAL_COORDINATE_CLOSURE_ROUND61.md`
2. `research/2026-08-17_checkpoint_after_consequential_coordinate_round61.md`
3. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND61.md`
4. `docs/SOURCE_LEDGER_ADDENDUM_ROUND61.md`
5. Round-57 metrology closure remains controlling where Round 61 did not intentionally revise it:
   - `docs/RP01_EMPIRICAL_PROTOCOL_METROLOGY_CLOSURE_ROUND57.md`
   - `procedures/P37_LBIC_BLOCKING_CONTACT_FUNCTIONAL_QUALIFICATION.md`
   - `analysis/ftir/ROUND57_FTIR_MODEL_SPECIFICATION.md`
6. Detailed P01–P37 procedures/calculations remain the technical evidence corpus.

## Current publication state

- `RP01-EEFP-ROUND61-CONSEQUENTIAL-COORDINATE-CANDIDATE = YES`.
- Round 61 integrates a second independent deep-research audit into the Round-60 LaTeX document.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `END-TO-END-EMPIRICALLY-VALIDATED = NO`.

## Evidence state

Round 61 formally uses six states:

- `RP` — direct Smith/RP-01 evidence.
- `SL` — same-laboratory/process-lineage primary evidence.
- `PT` — primary transfer evidence from an analogous process or official technical source.
- `DER` — transparent derivation from better-established quantities.
- `SYN` — explicit locally executable empirical implementation synthesized from evidence/physics.
- `OPEN` — experimentally consequential coordinate for which no defensible numerical value is presently supported.

`OPEN` is a valid, successful documentation state. The failure state is an important coordinate that is left unnamed or implicitly assumed.

Optional `SYN-H/M/L` confidence modifiers may still be used, but Round 61 intentionally demotes several Round-60 `SYN-L` apparatus dimensions back to `OPEN` because the second deep-research audit showed that assigning a prototype dimension there created more false certainty than scientific value.

Modern experiments can establish a local `SYN` implementation. They cannot retroactively establish what UWA, Fermionics, Honeywell, or another historical laboratory actually used; only documentary evidence can promote an historical unknown to `RP` or `SL`.

## Round-61 governing model: state transitions

Each operation is treated as a transition between experimentally observable state vectors rather than as a scalar setpoint list:

`state_(j-1) -> operation_j -> measured outputs -> state_j`.

The state may include:

- material/composition/carrier/contamination state;
- geometry and surface state;
- thermal field and time derivative;
- age/queue/dwell history;
- pressure, chemistry and flow;
- electrical/plasma state;
- measurement-system/calibration state.

This is particularly important for LPE, wet etching, anodization, RIE, metallization and cryogenic detector characterization.

## Major Round-61 corrections and additions

### 1. Source-synthesis ampoule: weak prototype geometry retracted

Round 60 proposed a `25 mm OD / 22 mm ID / ~150 mm` ampoule with `50±5 mL` loaded free volume as a development coordinate. Round 61 removes those values from the canonical recipe.

Direct/transfer evidence closes only:

- `10 g` source synthesis;
- 6N Hg/Cd/Te source materials;
- evacuated quartz ampoule;
- `700 °C / 8 h` source synthesis.

The following remain `OPEN` pending vessel engineering or archival recovery:

- tube ID/OD/wall;
- loaded free volume and charge/free-volume ratio;
- seal/neck geometry;
- support/orientation;
- maximum internal pressure at synthesis temperature.

Do not estimate the 700 °C vessel pressure by extrapolating a pure-Hg vapor-pressure formula. The ternary charge chemical potential is not pure mercury.

Closure order: engineering pressure/thermal-stress assessment -> dimensioned professionally fabricated quartz revision -> blank thermal qualification -> source-containing qualification.

### 2. LPE geometry: topology preserved, unsupported dimensions demoted

Recovered primary apparatus evidence remains strong:

- high-purity/high-density graphite horizontal-slider architecture;
- base, movable slider, cover, through-wells/solution bin, substrate recess, Hg-source cavity, Hg-retaining moats/grooves and plugs;
- 15 × 15 × 1 mm CdZnTe substrate in the Radhakrishnan transfer source;
- horizontal quartz reactor with gas, actuator and thermocouple access;
- ~4.8 g growth charge and 3 g HgTe compensation in that same transfer geometry;
- Honeywell CdTe wipe pieces approximately 1 mm apart, sliding-fit, contacting the base surface.

Round 61 retracts the Round-60 numerical prototype recess/well/slider/Hg-cavity/moat dimensions. Exact dimension stack remains `OPEN`.

The ~4.8 g and 3 g quantities are now explicitly treated as **geometry-coupled PT values, not universal recipe constants**. The relevant melt-depth relation is

`h_melt(T) = m_melt / [rho_melt(T) A_well]`.

Until `A_well` and a defensible melt-density model/measurement are known, `h_melt` remains OPEN.

First local closure should use CAD/CMM/profilometry and dummy mechanics before detector-grade growth. For recess flushness define `Delta z = d_recess - t_substrate` and screen `-50, 0, +50 µm` on dummy coupons as SYN experiment levels, measuring slider force, snagging, scratches and wipe behavior.

### 3. Present-day graphite procurement

A defensible PT/SYN procurement family is now explicit:

- purified isotropic semiconductor-grade graphite;
- characteristic particle size approximately 1–5 µm;
- no metallic impregnation;
- lot-specific ash/GDMS or equivalent CoA retained.

Exact historical grade, final surface roughness, machining method and post-machining clean remain OPEN. Do not insert an acid cleaning method without HgCdTe-LPE evidence or supplier compatibility because porous graphite can retain residues.

### 4. LPE thermal map and Hg-source geometry

Before interpreting controller temperature as the growth-interface temperature, instrument a dummy boat with at least 3 and preferably 5 calibrated sensors at the well wall, substrate recess, Hg-source recess, adjacent furnace gas and normal control-TC location. Run the actual thermal program three times.

Provisional SYN mapping target: local growth-region deviation within about ±1 °C with run-to-run mapping uncertainty comfortably below the ±3 °C temperature perturbation already used in the LPE screen.

For the Hg source, record mass, shape, exposed/projected area, location, enclosed vapor geometry and post-run mass loss. A useful geometry coordinate is `Psi_Hg = A_Hg-source / V_enclosed`.

### 5. Wet mesa: mass-transfer state added

The remaining major uncertainty is hydrodynamics rather than the nominal chemistry. Preserve per run:

`{C_Br2, T, t_age, V_bath, A_exposed, D_vessel, H_liquid, agitation mode, U_agitation, t_quench}`

and report

`Gamma_bath = V_etchant / A_exposed,HgCdTe`.

No historical vessel diameter, universal bath-volume/area ratio, or agitation velocity is promoted. Suggested witness qualification factors include bath age, static/reproducible agitation, bath inventory and quench latency.

### 6. Anodization: electrical trajectory becomes part of the recipe

Direct TI center remains `0.1 M KOH`, `90% EG / 10% water`, `0.3 mA/cm²`, about `15 V`, `120 s`, about `80 nm`.

Derived charge coordinate:

`Q/A = J t = 0.036 C/cm²`.

Record `J(t)`, `V(t)`, `Q/A` and measured oxide thickness. Do not use `80 nm / 15 V` as a universal formation factor because terminal voltage contains electrolyte/cell ohmic drop. Electrode spacing, cathode/anode area ratio, bath conductivity/temperature and bath age remain explicit coordinates.

An initial local cell-geometry closure may use three electrode separations × two cathode/anode area ratios × two repetitions, logging V/I at >=1 Hz and independently measuring oxide thickness.

### 7. RIE: physical reactor state is mandatory

Every transfer run records the dynamic vector:

`[F_CH4(t), F_H2(t), p(t), P_fwd(t), P_refl(t), V_dc(t), T_platen(t), T_sample(t)]`

and static reactor geometry:

`[D_powered, A_powered, d_electrode, chamber volume/geometry, carrier geometry, sample position]`.

Before a larger DOE on a new reactor, perform three nominal instrumented witness runs. Prefer a fiber-optic specimen-temperature method on a mechanically representative dummy for initial thermal qualification where RF pickup compromises conventional thermocouples.

Initial SYN equipment-state screens:

- `P_refl/P_fwd < 0.05`;
- `CV(V_dc) < 5%`;
- `T_sample,max < 40 °C`;
- mean pressure within about ±2% of calibrated target.

These are apparatus-state screens, not historical specifications. Ultimate acceptance remains the electrical/conversion/LBIC/TLM result.

Record base pressure, pumpdown, preceding chamber chemistry, clean/seasoning procedure and elapsed time since clean.

### 8. Cr/Au: official evaporation/QCM details promoted

Direct stack remains 30/270 nm Cr/Au.

Official PT starting guidance now includes:

- Cr and Au thermal-evaporation rates in the ~1–5 Å/s range;
- W-based Cr source hardware and alumina-compatible Au source hardware as appropriate to the actual evaporator;
- Au base pressure around `<=1e-6 Torr` as PT equipment guidance;
- QCM Z-ratio starting values `Z_Cr = 0.305`, `Z_Au = 0.381`;
- independent witness profilometry/interferometry to calibrate QCM/tooling response.

Round 61 removes a universal source-to-sample distance/rotation as a canonical value. Actual source, QCM, shutter, substrate position/orientation and rotation are apparatus coordinates to measure and retain.

Open the substrate shutter only after deposition rate is within ±5% of target for at least 30 s and chamber pressure is stable (SYN endpoint). Preserve no vacuum break between Cr and Au in the reference implementation.

### 9. Cryogenic measurement state: equilibrium replaces elapsed time

The fixed cooldown-rate value is retained only as a candidate branch, not a universal physics rule. A local package study should compare deliberately slow ~1–2 K/min, <=5 K/min, and the natural cryostat cooldown profile when package-safe.

If enough devices are available, use ~6 packaged devices and >=3 300↔80 K cycles/device to separate permanent package effects from time-to-equilibrium.

Before low-noise measurements, a provisional SYN stationarity gate is:

- detector/stage temperature SD `<=0.05 K` over 10 min;
- `|Delta R|/R < 0.2%` over the same interval.

Record controller, stage and detector/proxy temperature, cooldown history, soak duration, bias dwell, resistance/current and illumination/dark history.

## Round-61 artifact state

Review artifacts:

- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round61.pdf`
- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round61.tex`

Final state:

- 74 physical PDF pages;
- letter size;
- text-native, openable and unencrypted;
- no PDF forms/XFA;
- all fonts embedded;
- all pages rendered at 200 dpi and visually inspected through contact sheets and key-page review;
- no overfull LaTeX boxes or undefined-control errors in the release compile; one visually benign underfull paragraph warning remains in the LPE thermal-map prose.

SHA-256:

- PDF `a1dd7888a92c2b129dae453f3e0684e6aab289b4c6bd9338b92660868bfb455f`;
- TeX `8103673ccc8952a8868974f12fb0c1c506e3de71c6bde6fd8f763322b79d9ec1`.

## Immediate next work

Round 61 is the preferred review candidate. Future work should pursue two parallel closure tracks:

1. **Documentary:** Honeywell machine drawings; Radhakrishnan original boat/Fig. 1 records; Fermionics/UWA starting-wafer/fabrication/RIE records; SSPL wet-etch notes; TI anodization cell drawings; original evaporator and cryostat/readout records.
2. **Empirical/local:** CAD/CMM LPE closure; dummy thermal maps; Hg-source/melt geometry; wet-etch mass-transfer witnesses; anodization V(Q/A) cell study; instrumented RIE state; Cr/Au QCM/source closure; cryogenic equilibrium qualification.

Do not respond to remaining uncertainty by inventing historical dimensions. Keep every consequential coordinate `RP`, `SL`, `PT`, `DER`, `SYN`, or `OPEN`.