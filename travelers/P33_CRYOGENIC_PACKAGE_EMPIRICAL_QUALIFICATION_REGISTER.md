# P33 — Cryogenic package empirical qualification register

**Status:** BLANK CONTROLLED QUALIFICATION REGISTER  
**Date:** 2026-08-16 America/New_York

Use with:

- P15 die attach/interconnect/cryogenic package qualification;
- P33 empirical package process window;
- P10 bias/self-heating;
- P11 radiometry;
- P12 noise;
- P13 temporal response.

Do not fill an `OPEN` field from memory or from another package family.

---

## A. Build identity

- P33 run/build ID:
- date:
- operator:
- package construction revision:
- die ID:
- wafer/growth ID:
- wafer coordinate:
- P31 anneal/state ID:
- P32/P28/P25/P27/P26/P24 process IDs:
- pre-package qualification disposition:

## B. Incoming die geometry/state

- die length:
- die width:
- CdZnTe thickness:
- HgCdTe active thickness:
- mesa/contact geometry ID:
- singulation method/program:
- edge-chip map:
- crack/damage inspection:
- pre-package optical image IDs:
- room-T resistance/continuity:
- baseline 80-K P10 result ID:
- baseline P12 result ID:
- baseline P11 result ID:
- baseline P13 result ID:

## C. Carrier / cold-finger

- carrier material/grade:
- coating/plating:
- carrier dimensions:
- detector-seat flatness:
- surface finish/roughness:
- carrier CTE source:
- carrier thermal-conductivity source:
- cold-finger material:
- carrier-to-cold-finger interface:
- grounding/electrical role:
- detector-seat area:
- temperature sensor ID:
- sensor location relative to die:

## D. Die-attach material genealogy

- candidate branch: silicone / epoxy / mechanical / other
- manufacturer:
- product:
- lot:
- expiration:
- received/storage history:
- mix ratio and basis:
- actual component masses/volumes:
- mixing method/time:
- degas method/time:
- dispense mass/volume:
- die/carrier surface preparation:
- placement force/fixture:
- cure temperature trace ID:
- cure time:
- cure atmosphere:
- cure ramp/cooldown:
- cure-to-test elapsed time:

## E. Measured bondline state

- bondline thickness positions/method:
- mean bondline thickness:
- min/max:
- die tilt:
- coverage fraction:
- void fraction:
- void-map file:
- squeeze-out extent:
- contamination/residue:
- pre-cool mechanical disposition:

## F. Interconnect

- wire/ribbon material:
- diameter/thickness:
- bonder model:
- tool/capillary/wedge ID:
- bond mode:
- stage temperature:
- force:
- ultrasonic amplitude/power:
- ultrasonic time:
- loop geometry:
- pad-preparation method:
- first/second-bond map:
- continuity result:
- contact/lead resistance:
- bond visual disposition:
- destructive witness pull/shear record ID:

## G. Package optics

- header/Dewar ID:
- cold-shield material/finish:
- aperture shape:
- aperture dimensions:
- detector-to-aperture distance:
- calculated full/half angle:
- window material:
- window thickness:
- coatings:
- detector-to-window distance:
- filter ID:
- `T_window(lambda)` data ID:
- `T_filter(lambda)` data ID:
- vignetting/alignment measurement:

## H. Vacuum / atmosphere

- pump/purge sequence:
- pressure sensor/method:
- pressure before cooldown:
- leak/outgassing evidence:
- getter/desiccant:
- bake temperature/time:
- detector thermal-budget authorization/qualification ID:
- pumpdown-to-test elapsed time:

## I. Initial cooldown

- warm-start temperature:
- cold-target temperature:
- actual cold-finger `T(t)` trace ID:
- cooldown time:
- dwell/equilibration criterion:
- observed cracking/delamination:
- bond/interconnect observation:
- detector resistance after equilibration:
- contact/lead resistance:

## J. Steady-state package thermal test

- bias/current condition:
- dissipated power estimate:
- cold-finger/reference temperature:
- die-temperature proxy:
- proxy calibration ID:
- inferred die temperature:
- `DeltaT_die`:
- `R_theta,eff`:
- uncertainty/limitations:

## K. Thermal transient test

- excitation: optical / electrical
- source/instrument:
- pulse duration:
- pulse amplitude/power/energy:
- detector bias/current:
- sample rate/bandwidth:
- acquisition duration:
- baseline temperature:
- resistance-vs-time data file:
- repeated amplitudes:
- fast recovery metric:
- intermediate thermal pole/time scale:
- slow thermal pole/time scale:
- fit model:
- fit residuals:
- amplitude dependence:
- `H_pkg,thermal` record ID:
- interpretation/disposition:

## L. Initial packaged detector comparison

- P10 result ID:
- P11 result ID:
- P12 result ID:
- P13 result ID:
- `DeltaR/R` pre/post:
- contact/lead resistance change:
- noise change:
- 1/f-knee change:
- responsivity change:
- apparent bandwidth/transient change:
- optical-throughput/FOV change:
- microphonics/pickup observation:

## M. Thermal-cycle genealogy

For each cycle block record:

| Block | Cycle range | Warm T | Cold T | Ramp/cool trace | Endpoint dwell | Vacuum/ambient | Abnormal event |
|---|---|---:|---:|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## N. Post-cycle state

- total cycle count:
- die crack/chip comparison:
- attachment/delamination comparison:
- void-map comparison:
- wire/bond comparison:
- contact resistance:
- P10 result ID:
- P12 result ID:
- thermal-transient result ID:
- optical alignment/FOV:
- other P11/P13 result IDs:

## O. Failure classification

Check/describe as applicable:

- [ ] die crack/chip propagation
- [ ] attachment delamination
- [ ] bondline voiding/creep
- [ ] excessive thermal resistance
- [ ] package thermal pole contaminates detector measurement
- [ ] interconnect lift/fracture
- [ ] contact/lead resistance increase
- [ ] excess noise / 1/f increase
- [ ] microphonics / EMI pickup
- [ ] optical clipping/misalignment
- [ ] vacuum/outgassing/bake damage
- [ ] no detected failure

Failure notes:

## P. Evidence / disposition

- construction evidence class:
- historical claim made? yes/no; justification:
- local qualification level:
- mechanical PASS/FAIL:
- electrical/noise PASS/FAIL:
- thermal PASS/FAIL:
- optical/device PASS/FAIL:
- overall disposition:
- deviations/nonconformances:
- P18 failure-analysis record if applicable:
- next action:

---

**Permanent reminder:** one repeatedly cycled package is one package genealogy, not multiple independent package replicates.
