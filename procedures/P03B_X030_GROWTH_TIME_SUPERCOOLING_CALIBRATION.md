# P03B — x≈0.30 LPE growth-time / supercooling / thickness calibration

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. Historical composition and apparatus family are well anchored; the exact RP-01 9.5-µm growth time is not published and must be calibrated on the selected boat/thermal program.

## 1. Purpose

Determine a reproducible relation between:

- growth-solution composition;
- liquidus temperature;
- initial supercooling;
- thermal trajectory;
- substrate/solution contact time;
- melt geometry/history;

and the resulting:

- HgCdTe thickness;
- solid composition `x`;
- across-wafer uniformity;
- surface morphology;
- electrical state after the defined post-growth treatment.

The immediate target interface to RP-01 is a layer near:

- nominal `x≈0.30`;
- thickness `9.5 µm`;
- suitable morphology/uniformity for downstream device fabrication.

## 2. Historical anchors

### Composition-matched Honeywell tie line

Bowers–Schmit same-lineage source:

- liquid `xL=0.082`;
- liquid `yL=0.810`;
- liquidus `TL=507 °C`;
- resulting solid `xS=0.29`;
- tabulated `xS/xL=3.54`.

The same patent family supports operation near 500 °C, heating above liquidus before growth below liquidus, and step cooling, slow continuous cooling, or a combination.

A patent example gives a growth interval of about 0.5 h, but that time is not explicitly tied to the xS=.29 row or to 9.5-µm thickness.

### Same-family general evidence

Te-rich horizontal-slider literature shows that layer thickness is controlled by **both degree of supercooling and growth time**.

Harman-family studies report layers from a few micrometers to tens of micrometers with growth times ranging from fractions of a minute to many minutes, depending strongly on apparatus and thermal trajectory.

This large inter-source spread is the reason a literature time cannot substitute for local calibration.

## 3. Core rule

Do not fit thickness as a function of time alone unless supercooling, thermal ramp, melt geometry, charge history and composition are held fixed.

The minimum local response model is

`d = f(t_contact, ΔT0, dT/dt, melt_depth, charge_history)`

with composition response

`x = g(t_contact, ΔT0, dT/dt, melt_depth, Hg_loss/history)`.

A useful process point must satisfy both `d≈9.5 µm` and the optical/compositional target simultaneously.

## 4. Prerequisites

Before P03B begins, freeze or document:

- selected graphite boat/well geometry;
- substrate size/recess geometry;
- Hg-loss-control architecture/source;
- charge composition and weighing method;
- charge synthesis/homogenization method;
- atmosphere sequence;
- substrate orientation/polarity/miscut;
- final substrate surface-prep recipe ID;
- temperature-sensor calibration and axial thermal map;
- slide-in/slide-out actuation method;
- wipe-off configuration.

If any of these changes materially, the thickness-time calibration must be revalidated.

## 5. Define actual liquidus reference experimentally

The Bowers–Schmit `TL=507 °C` value is the primary composition anchor, but the actual local system includes weighing error, Hg loss and temperature-calibration error.

Therefore before the full DOE:

1. prepare the composition-matched charge;
2. establish the local thermal equilibrium procedure;
3. use the best available phase/liquidus observation or growth/no-growth bracketing method to verify the effective local onset region;
4. record the relationship between controller/sensor temperature and the expected published liquidus.

Do not silently redefine the published phase point. Report any local offset as apparatus/process calibration.

## 6. Initial supercooling center

The composition-matched source gives `TL≈507 °C` and describes growth near 500 °C.

Thus

`ΔT0≈7 °C`

is a defensible **qualification center**, not a production setpoint.

The local DOE should bracket this center using bounded lower and higher supercooling levels selected so that:

- all conditions remain in the same physical growth regime;
- morphology does not catastrophically degrade;
- thickness spans the 9.5-µm target within practical contact times.

Exact bracket values should be selected from preliminary local runs/thermal-control capability and recorded as local DOE settings.

## 7. Stage A — contact-time sweep at fixed thermal condition

At the initial center supercooling/thermal trajectory:

- hold charge composition fixed;
- use fresh or history-matched charge state;
- use matched substrate preparation;
- run at least three contact times selected to bracket the expected 9.5-µm thickness;
- replicate the center time across independent runs.

For every run record:

- full temperature trace;
- exact substrate/solution contact timestamp;
- exact separation timestamp;
- actual contact duration;
- actuator trace/notes;
- Hg-source condition;
- pre/post charge/Hg-source mass where feasible;
- atmosphere state;
- wipe-off outcome.

## 8. Stage B — supercooling sweep

After a stable time center is identified, vary `ΔT0` while holding:

- charge composition;
- contact time;
- thermal-ramp shape after contact;
- substrate state;
- boat/well;
- atmosphere

as fixed as practicable.

At least three supercooling levels are required for process-development characterization.

Measure thickness, composition and morphology at each level.

## 9. Stage C — thermal-ramp comparison

Only after the step/supercooling response is understood, compare thermal trajectories supported by the same-lineage process family:

- step-supercool + nominally isothermal contact;
- slow continuous cooling after contact;
- combined step + controlled cooling.

Each trajectory gets a separate recipe ID.

Do not average results across thermal modes into one generic growth-rate model.

## 10. Mandatory post-growth measurements

### Thickness

Use P06 spatial thickness mapping plus independent calibration.

Report at minimum:

- wafer mean thickness;
- standard deviation;
- min/max;
- peak-to-valley;
- edge exclusion;
- map coordinates.

### Composition/optical edge

Use identical spatial coordinates where possible.

Report:

- raw spectra;
- chosen optical-edge descriptor;
- model-inferred `x` with method version;
- across-wafer variation;
- evidence of depth grading if the spectral model resolves it.

### Surface morphology

Record:

- full-wafer optical image;
- DIC/Nomarski map;
- residual melt area/count;
- pinholes/voids;
- scratches;
- terrace/macrostep structure;
- usable-area fraction.

### Electrical state

Measure representative Hall material before and after the defined P04 anneal sequence so growth-condition effects are not conflated with post-growth defect equilibration.

## 11. Model fitting

Within one frozen apparatus/thermal mode, fit a local empirical response such as

`d = β0 + β1 t + β2 ΔT + β3 tΔT + β4 t² + β5 ΔT² + ...`

only if data support those terms.

The intent is not to claim a universal LPE law; it is to interpolate within the qualified local region.

Also model composition response:

`x = γ0 + γ1 t + γ2 ΔT + γ3 run_order + ...`

where `run_order` or charge reuse can detect depletion/Hg-loss drift.

Use residual plots and replicated center points to separate lack of fit from run-to-run process noise.

## 12. Charge-history effect

A reused growth charge may not be equivalent to a fresh charge because of:

- solute depletion;
- Hg loss;
- contamination pickup;
- residual solidification/remelting history.

Therefore every run must be classified as:

- fresh charge;
- reused charge with run count;
- replenished/modified charge.

Do not combine these classes in one thickness-time calibration unless statistical testing demonstrates equivalence.

## 13. Growth termination and wipe-off as covariates

If slider separation/wipe-off is not repeatable, apparent thickness/morphology variation may be dominated by residual melt rather than epitaxial growth kinetics.

Record:

- separation temperature;
- slider speed/actuation state;
- residual melt footprint;
- wiper/contact state;
- scratches.

Reject locations covered by residual solidified growth solution from the epitaxial thickness fit, but record the lost area as a yield outcome.

## 14. Target centering

The local process target is not exactly one measured 9.500-µm point.

After the response surface is fit, choose a center condition that:

- targets 9.5 µm mean thickness;
- is locally insensitive to small time/temperature errors where possible;
- gives acceptable composition and uniformity;
- avoids a steep morphology/yield penalty;
- leaves process margin on both sides.

A robust center is preferable to a mathematically exact but highly sensitive point.

## 15. Apparatus tolerance derivation

Once local derivatives are measured, convert acceptable material variation into equipment/process tolerances.

For example, if local sensitivity is

`S_t = ∂d/∂t`

and allowed thickness contribution from timing is `u_d,t`, require approximately

`u_t <= u_d,t / |S_t|`.

Similarly, with

`S_T = ∂d/∂T`

and composition sensitivity

`S_xT = ∂x/∂T`,

temperature-control requirements should be set from the tighter of the thickness and composition budgets.

This is preferable to declaring an arbitrary ±0.1 °C or ±1 s tolerance before measuring sensitivity.

## 16. Candidate process release criteria

A P03B condition can advance toward local release only when:

- mean thickness is centered near the RP-01 target;
- thickness uniformity is measured and stable;
- composition/edge map meets the selected RP-01 optical target;
- run-to-run repeatability is established;
- morphology/usable-area yield is acceptable;
- charge-run-order drift is absent or explicitly compensated;
- the resulting material can be driven by P04 into the required n-type transport state;
- downstream P01/P02/P08/P09 processing yields detector performance comparable to RP-01.

Numerical acceptance windows remain `QUAL` until enough local runs exist for capability analysis.

## 17. Negative-result preservation

For every failed P03B run, record why it failed:

- too thin/thick;
- composition wrong;
- strong grading;
- poor morphology;
- residual melt;
- electrical state unacceptable;
- substrate/interface defect;
- Hg-loss drift;
- thermal-control excursion.

Do not discard failed runs from model development without preserving the data and exclusion reason.

## 18. Historical conclusion

The literature now closes the **composition family and thermal logic**, but not the exact 9.5-µm contact time for RP-01.

Accordingly, the scientifically correct route is local calibration of `time × supercooling × thermal trajectory` rather than copying a growth time from another slider geometry or composition branch.
