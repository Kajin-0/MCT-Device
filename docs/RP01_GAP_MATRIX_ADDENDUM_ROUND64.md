# RP-01 gap-matrix addendum - Round 64

**Date:** 2026-08-17 America/New_York  
**Basis:** fifteen newly recovered full papers after Round 63.

Round 64 changes a gap only where full text supplies a stronger consequential coordinate. Historical RP-01 unknowns remain `OPEN` unless direct evidence closes them.

## G64-01 - Honeywell slider thermal/time branch strengthened

Schmit/Hager/Wood directly describe the Honeywell atmospheric-pressure Te-rich horizontal slider with high-purity graphite, horizontal quartz tube, flowing H2, push-rod actuation, supercooled isothermal growth and usual growth times about 1-20 min for <=~30-um layers.

State: `HONEYWELL-LPE-PROCESS-FAMILY-PT-STRENGTHENED / RP01-MECHANICAL-STACK-OPEN`.

## G64-02 - source-use number and Hg-reservoir depletion become explicit LPE coordinates

Nemirovsky et al. report a semiclosed branch with ~4.5-g HgTe reservoir, ~3.5-g solution, reservoir renewal each run, solution reuse for several runs, and ~20% reservoir loss over a typical 2-3 h branch near 460 C.

Action: record Hg-source use, initial/final mass, solution-use number and source conditioning separately.

State: `LPE-SOURCE-GENEALOGY-PT-STRENGTHENED`.

## G64-03 - substrate state during equilibration is not automatically inert

Nemirovsky et al. observed substrate-side crystallites/deposition during the equilibration environment before intentional solution contact.

Action: record substrate position/exposure state during equilibration and inspect a no-contact witness or equivalent during local qualification.

State: `PRECONTACT-VAPOR-EXPOSURE-COORDINATE-EXPLICIT`.

## G64-04 - same-UWA Plasma Technology physical state substantially strengthened

Smith 1999 provides 16 C cathode, 30 sccm total, 400 mTorr, 0.4 W/cm2 and printed 180-V dc bias in a Plasma Technology parallel-plate branch.

Action: use as SL reactor-equivalence evidence. Do not assign these values to RP-01's 100-mTorr/50-W/64-sccm/60-s exposure.

State: `RIE-SL-PHYSICAL-STATE-STRENGTHENED / RP01-SELFBIAS-OPEN`.

## G64-05 - approximately 8-um same-lineage electrical-conversion branch largely closed

Musca 1998 supplies the process state for an x=.31 Fermionics n-type branch:

`H2 27 sccm / CH4 5 sccm / 430 mTorr / 0.4 W cm^-2 / cathode 18 C / ~200 V dc / 30 s`

with ~0.075 um physical recession but an LBIC/etchback electrical junction signature extending to about 8 um.

Action: retain as a distinct SL branch. Do not average with 0.5-2-um conversion branches.

State: `SL-8UM-CONVERSION-BRANCH-CLOSED / RP01-CONVERSION-DEPTH-OPEN`.

## G64-06 - photoresist thickness/profile is a plasma-conversion coordinate

Musca 1998 shows apparent lateral conversion can be driven by resist thinning/taper near a mask edge.

Action: record resist thickness, edge slope/profile, minimum protected thickness and post-RIE resist condition in conversion-depth and lateral-spread studies.

State: `RIE-MASK-PHYSICAL-STATE-EXPLICIT`.

## G64-07 - RIE converted material is a multicarrier/multilayer electrical state

Antoszewski 2000 and Nguyen 2002 resolve a low-mobility surface-electron population from a deeper high-mobility converted bulk-electron population.

Action: one-carrier Hall values after RIE may be reported only as effective scalars unless field dependence supports a single-carrier model. Physical depth/doping claims require differential Hall/QMSA or equivalent resolved analysis.

State: `RIE-MULTICARRIER-TRANSPORT-SL-CLOSED`.

## G64-08 - actual sample temperature remains distinct from cooled-stage setpoint

White 2001 reports a 15 C stage but only estimates actual HgCdTe temperature during plasma exposure.

Action: record/qualify sample temperature separately from chuck/cathode setpoint. Post-RIE bake history is mandatory because mobile hydrogen redistributes.

State: `RIE-THERMAL-STATE-DISCIPLINE-STRENGTHENED / RP01-SAMPLE-TEMP-OPEN`.

## G64-09 - Hg annealing can reverse an SL RIE conversion branch

Smith 1998 shows 200 C / 17 h sealed-Hg treatment restoring the initial p-type state after a 400-mTorr/90-W RIE branch.

Action: preserve as an SL recovery experiment; do not install it as an RP-01 repair recipe.

State: `RIE-HG-ANNEAL-REVERSIBILITY-SL-STRENGTHENED`.

## G64-10 - expanded RIE exposure requires detector-level functional qualification

Smith 2000 directly shows large degradation in photoconductor responsivity, effective lifetime, noise and D* after long mesa RIE despite similar DC resistance and cutoff wavelength.

Action: any change in exposed plasma area, duration or mesa strategy requires matched-device checks of `Rv(lambda)`, `tau_eff`, PSD/ASD, knee frequency and D*.

State: `RIE-DETECTOR-PERFORMANCE-GATE-SL-CLOSED`.

## G64-11 - literal gas notation conflict is preserved

Smith 2000 prints `H2/5CH4` for the 70-min mesa branch, whereas other UWA papers report CH4/5H2 or explicit H2/CH4 flows.

Action: never normalize a historical gas ratio by assumption. Archive literal source notation and explicit MFC flows where available.

State: `RIE-GAS-NOTATION-PROVENANCE-CONFLICT-EXPLICIT`.

## G64-12 - LBIC absolute depth requires calibrated/model-supported interpretation

Musca 1999 demonstrates sensitivity of LBIC depth response to junction doping, wavelength, illumination direction, geometry and diffusion length.

Action: absolute `d_conv` from LBIC requires witness/calibration/model/destructive cross-check; raw lobe spacing alone is not a universal depth metric.

State: `LBIC-ABSOLUTE-DEPTH-CALIBRATION-REQUIRED`.

## G64-13 - passivation acceptance becomes a coupled state vector

Pal 1999 shows surface accumulation can both raise effective lifetime and lower surface shunt resistance.

Action: evaluate, where measurable, `{Qss, Dit, Rsh_surface, tau_eff, Rv}` rather than accepting oxide thickness alone.

State: `PASSIVATION-COUPLED-ELECTRICAL-STATE-PT-STRENGTHENED`.

## G64-14 - anodic oxide has illumination/bias/time memory

Schoolar 1982 on x=.30 material shows visible-light and applied-field charge transfer in the anodic oxide/interface, with recovery extending from minutes at room temperature to weeks at 77 K.

Action: record light exposure, dark-rest time, prior electric field/gate bias and measurement temperature before C-V, surface/shunt or detector comparisons.

State: `ANODIC-OXIDE-PRECONDITIONING-HISTORY-EXPLICIT`.

## G64-15 - passivant-induced surface shunt is a candidate detector-noise source

Bhan 2004 required a surface-shunt/noise contribution to fit HgCdTe-PC array data.

Action: when resistance/noise indicates surface-shunt domination, include surface-network noise rather than forcing all excess noise into bulk g-r or generic 1/f terms.

State: `SURFACE-SHUNT-NOISE-PT-EXPLICIT`.

## G64-16 - metal/HgCdTe interface chemistry remains a process state

Davis 1984 directly observes Te redistribution, cation/anion changes and band-bending modification during Au deposition on p-Hg0.72Cd0.28Te.

Action: preserve source, vacuum, rate/trajectory, QCM geometry, sample thermal state and premetal surface history. No RP-01 Cr/Au setpoint is promoted.

State: `METAL-HGCDTE-INTERFACE-CHEMISTRY-PT-STRENGTHENED`.

## Major historical OPEN coordinates after Round 64

Still `OPEN`:

- exact RP-01/Fermionics LPE base/slider/cover/well/recess dimension stack;
- historical slider/base/epilayer clearance and wipe implementation;
- historical growth-well area/depth, melt depth and source-vapor geometry;
- exact historical source-synthesis ampoule/free-volume/hot-pressure state;
- RP-01 RIE reactor model, RF frequency, electrode areas/spacing, matching-network state, self-bias, actual sample temperature and chamber seasoning;
- exact RP-01 electrical conversion depth/lateral spread under the 100-mTorr/50-W/64-sccm/60-s blocking-contact exposure;
- historical anodization electrode geometry/solution voltage drop;
- historical Cr/Au evaporator/QCM/source-to-sample geometry;
- original RP-01 cryostat/package/readout thermal state.

Broad paper mining remains lower priority than archival recovery.