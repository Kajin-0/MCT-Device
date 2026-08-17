# Round 61 — consequential-coordinate closure and evidence-discipline revision

**Date:** 2026-08-17 America/New_York

## Trigger

A second independent deep-research audit reviewed the remaining experimentally consequential coordinates in the EEFP. Its most useful contribution was corrective rather than additive: it showed that several low-confidence Round-60 prototype dimensions had been promoted too far merely to make the apparatus numerically complete.

Round 61 therefore strengthens the manual by distinguishing:

1. topology/apparatus facts actually recovered from primary sources;
2. physical relationships that can be derived;
3. local empirical coordinates that can be established by deliberately instrumented qualification;
4. genuinely unresolved historical/apparatus quantities that should remain `OPEN`.

## Formal evidence-state extension

Round 61 adds `OPEN` as a first-class state alongside `RP`, `SL`, `PT`, `DER` and `SYN`.

An OPEN coordinate is acceptable when:

- the parameter is experimentally consequential;
- no defensible numerical value is supported;
- its physical consequence is stated;
- the route to documentary or empirical closure is specified.

The unacceptable state is an important coordinate that remains unnamed or buried in laboratory custom.

A modern experiment may establish a local `SYN` value; it cannot establish an historical `RP`/`SL` identity without documentary evidence.

## Source-synthesis ampoule correction

Round 60 introduced a `25 mm OD / 22 mm ID / ~150 mm` development ampoule with `50±5 mL` free volume.

Round 61 retracts these values from the canonical recipe.

Primary transfer evidence closes only:

- 10-g source synthesis;
- 6N Hg/Cd/Te;
- evacuated quartz ampoule;
- 700 °C / 8 h synthesis.

Remain `OPEN`:

- tube ID/OD/wall;
- loaded free volume and charge/free-volume ratio;
- neck/seal geometry;
- furnace support/orientation;
- maximum hot internal pressure.

Pure-Hg vapor-pressure extrapolation is explicitly rejected for the ternary charge. The closure sequence is engineering pressure/thermal-stress assessment -> professionally fabricated dimensioned quartz revision -> blank thermal qualification -> source-containing qualification.

## LPE geometry correction

Primary facts retained:

- high-purity/high-density graphite horizontal-slider topology;
- base, slider, cover, solution wells/bin, substrate recess, Hg-source cavity, Hg-retaining moats/grooves and plugs;
- 15 × 15 × 1 mm CdZnTe substrate in the Radhakrishnan transfer branch;
- horizontal quartz tube, actuator and thermocouple access;
- ~4.8-g growth charge and 3-g HgTe compensation in that transfer geometry;
- Honeywell CdTe wipe pieces at about 1-mm spacing.

Round 61 removes Round-60 numerical prototype recess/well/slider/Hg-cavity/moat dimensions from the canonical recipe.

The charge quantities are now explicitly geometry-coupled:

`h_melt(T) = m_melt / [rho_melt(T) A_well]`.

Do not scale 4.8 g by substrate area and call the result a melt-depth correction. `A_well` is the missing coordinate.

### Local mechanical closure

Create a revision-controlled CAD drawing and dimensional inspection record before detector-grade growth.

For substrate flushness define:

`Delta z = d_recess - t_substrate`.

A first dummy-mechanics screen may use `Delta z = -50, 0, +50 µm` as SYN experimental levels, measuring slider force, snagging, scratching and wipe behavior.

### Graphite

Present-day PT/SYN procurement specification:

- purified isotropic semiconductor-grade graphite;
- characteristic particle size ~1–5 µm;
- no metallic impregnation;
- lot-specific ash/GDMS or equivalent contamination certificate.

Exact historical grade, final roughness, machining method and cleaning remain OPEN.

Do not introduce an arbitrary acid-cleaning recipe for porous graphite without HgCdTe-LPE evidence or supplier compatibility.

### Thermal mapping

Use an instrumented dummy boat with 3–5 sensors at the growth-well wall, substrate recess, Hg-source recess, adjacent furnace gas and normal control-TC position. Run the actual thermal program three independent times.

Record:

`Delta T_i(t) = T_i(t) - T_control(t)`.

Initial SYN target: active growth-region deviation approximately <=1 °C with run-to-run mapping uncertainty clearly below the ±3 °C LPE perturbation used in the validation screen.

### Hg-source geometry

Record source mass, shape, exposed/projected area, location, enclosed vapor geometry and post-run mass change.

Useful coordinate:

`Psi_Hg = A_Hg-source / V_enclosed`.

This makes the transferred 3-g source mass physically interpretable only after geometry is fixed.

## Wet-etch mass-transfer closure

The nominal Br2/EG/HBr chemistry and geometry-matched witness logic remain. The new state vector is:

`{C_Br2, T, t_age, V_bath, A_exposed, D_vessel, H_liquid, agitation mode, U_agitation, t_quench}`.

Report the bath-inventory coordinate:

`Gamma_bath = V_etchant / A_exposed,HgCdTe`.

No universal vessel diameter, inventory ratio or agitation velocity is claimed historical.

Suggested local screen uses same-material witnesses and varies bath age, hydrodynamics, bath inventory and quench latency while measuring rate, lateral etch, roughness and final profile.

## Anodization electrical-state closure

Direct TI reference center remains:

- 0.1 M KOH;
- 90% EG / 10% water;
- 0.3 mA/cm²;
- ~15 V;
- 120 s;
- ~80 nm oxide.

Derived:

`Q/A = J t = 0.036 C/cm²`.

Round 61 requires the process record to include `J(t)`, `V(t)`, integrated `Q/A`, and independently measured `d_ox`.

Terminal voltage is not a universal oxide-thickness coordinate because

`V_supply = V_interface + I R_solution + V_film`.

Electrode spacing, cathode/anode area ratio, electrolyte conductivity/temperature and bath age therefore remain explicit cell coordinates.

## RIE state closure

Historical controller settings remain direct RP evidence. Reactor equivalence is defined by physical state, not watts alone.

Dynamic vector:

`P_RIE(t) = [F_CH4, F_H2, p, P_fwd, P_refl, V_dc, T_platen, T_sample]`.

Static geometry:

`G_RIE = [D_powered, A_powered, d_electrode, chamber geometry/volume, carrier geometry, sample position]`.

Before a larger DOE on a new reactor, perform three nominal instrumented witness runs. Log relevant state variables at >=1 Hz.

Initial SYN equipment-state screens:

- `P_refl/P_fwd < 0.05`;
- `CV(V_dc) < 5%`;
- `T_sample,max < 40 °C`;
- mean pressure within ~±2% calibrated target.

Record base pressure, pumpdown, previous chemistry, cleaning/seasoning and time since clean.

The ultimate acceptance remains electrical conversion/LBIC/Hall/TLM, not the apparatus screen itself.

## Cr/Au closure

Official primary-transfer equipment guidance now carried explicitly:

- Cr and Au evaporation rates ~1–5 Å/s;
- appropriate W-based Cr source hardware;
- alumina-compatible Au source hardware;
- Au base pressure ~<=1e-6 Torr as equipment guidance;
- QCM Z-ratios `Z_Cr=0.305`, `Z_Au=0.381`;
- independent witness step-height calibration.

Round 61 removes a universal source-to-sample distance and rotation rate from the canonical recipe. Those are apparatus-specific coordinates.

SYN shutter endpoint: open only after rate is within ±5% of target for >=30 s and chamber pressure is stable.

Reference implementation keeps Cr->Au under vacuum with no intentional break.

## Cryogenic measurement-state closure

Round 61 separates package-safe cooldown history from detector measurement equilibrium.

Potential local branches:

- deliberately slow ~1–2 K/min;
- <=5 K/min;
- natural cryostat profile if mechanically safe.

If available, use approximately six packaged devices over >=3 thermal cycles/device to test persistent package/device changes and time-to-equilibrium separately.

Initial SYN measurement-start gate:

- temperature SD <=0.05 K over 10 min;
- `|Delta R|/R < 0.2%` over the same interval.

Retain cooldown trajectory, controller/stage/detector temperature or proxy, soak duration, bias history and illumination/dark history.

## Research closure architecture

Round 61 introduces Appendix E as a finite consequential-coordinate map. It is a scientific research map, not manufacturing-control paperwork.

The two closure tracks remain separate:

### Documentary

Search original drawings, theses, patents, proceedings, supplier records and laboratory archives. Priority targets include Honeywell LPE machine drawings, Radhakrishnan original boat records, Fermionics/UWA process/tool records, SSPL etch records, TI anodization-cell records, and original evaporator/cryostat documentation.

### Empirical/local

Use instrumented witnesses and minimal experiments to establish locally executable SYN states without pretending to recover history.

Priority order:

`LPE CAD/dimensional closure -> dummy thermal map -> Hg-source/melt geometry -> RIE physical-state closure -> anodization V(Q/A) -> wet-etch hydrodynamics -> Cr/Au source/QCM closure -> cryogenic equilibrium closure`.

## Artifact QA

Round-61 PDF:

- 74 pages;
- text-native;
- letter size;
- no encryption;
- zero form/XFA fields;
- all fonts embedded;
- all pages rendered at 200 dpi and visually inspected;
- no overfull LaTeX box or undefined-control errors; one benign underfull LPE prose warning.

SHA-256:

- PDF `a1dd7888a92c2b129dae453f3e0684e6aab289b4c6bd9338b92660868bfb455f`;
- TeX `8103673ccc8952a8868974f12fb0c1c506e3de71c6bde6fd8f763322b79d9ec1`.

## Disposition

`RP01-EEFP-ROUND61-CONSEQUENTIAL-COORDINATE-CANDIDATE = YES`.

Round 61 is a stronger reference than Round 60 because it removes false numerical completeness while adding more physically meaningful state definition.