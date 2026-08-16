# P17A — singulation / package change-control and release extension

**Status:** CONTROLLED RELEASE-LAYER ADDENDUM  
**Date:** 2026-08-16 America/New_York

Supplements `P17_STATISTICAL_PROCESS_CAPABILITY_RELEASE.md` after creation of P35 and the empirical P33 package layer.

## 1. Purpose

Ensure that finished-device singulation and cryogenic package construction are treated as released detector-process variables rather than neutral handling operations.

The release chain is:

`P35 singulation state -> P33 package state -> P10/P11/P12/P13 detector state -> P17 stability/yield/change control`.

---

## 2. Singulation release vector

For capability/release work retain at minimum:

`Y_SING={kerf,position error,die dimensions,front/back chip statistics,crack/subsurface-damage metric,residue/clean state,d_functional,d_release,Delta I-V,Delta noise,Delta responsivity,cryogenic survival}`.

Do not use visual chip yield alone as the singulation capability metric.

### Variance hierarchy

Separate where data permit:

- measurement repeatability of edge/chip/subsurface method;
- cut-to-cut variation within one tool setup;
- die-position/orientation variation;
- blade/wire/laser consumable age or pulse-history variation;
- tool dress/season/maintenance state;
- operator/fixture variation;
- lot/run variation;
- cryogenic package-interaction variation.

Multiple cuts from one blade/wire/tool state are not independent tool-history replicates.

---

## 3. Package release vector

Retain at minimum:

`Y_PKG={cracking/delamination,bondline thickness/voiding,die tilt,R_theta,H_pkg_thermal,contact/lead R,Delta I-V,Delta noise,Delta responsivity,Delta bandwidth,optical alignment/FOV,vacuum stability,thermal-cycle survival}`.

Die shear or wire pull is not sufficient by itself.

---

## 4. Change-control triggers — P35 singulation

Require documented impact review/requalification after material changes to:

- singulation method class: blade / wire / scribe-cleave / laser;
- machine model or major tool revision;
- blade/wire manufacturer/product/bond/grit/dimensions;
- laser wavelength/pulse duration/fluence/spot/scan strategy;
- spindle/wire speed/feed/downfeed/pass sequence;
- tool dressing/conditioning method;
- coolant/slurry chemistry, filtration or recirculation state;
- protective coating/tape/wax/support material;
- cut orientation/street/edge-exclusion geometry;
- die release/pickup handling;
- post-cut clean/removal chemistry;
- inspection method for edge/subsurface damage.

Minimum requalification path normally includes:

`P35 geometry/edge/subsurface -> selected P10 electrical -> selected P12 noise -> selected P11 responsivity when edge-sensitive -> P33 cryogenic survival`.

Reduce this scope only with documented physical rationale.

---

## 5. Change-control triggers — P33 package/interconnect

Require impact review after changes to:

- carrier/cold-finger material, geometry or surface finish;
- die-attach product/formulation/lot family;
- bondline target/coverage/placement method;
- cure/bake trajectory;
- wire/ribbon metallurgy or diameter;
- bonder mode/tool/force/ultrasonic/time/stage temperature;
- aperture/shield/window/filter geometry or material;
- vacuum/pump/purge/bake procedure;
- temperature sensor/location;
- thermal-cycle endpoint/ramp/dwell;
- grounding/shield/feedthrough topology.

Requalification must follow the affected physical path. Examples:

- die-attach change -> mechanical + `R_theta/H_pkg_thermal` + P10/P12/P13 and selected P11;
- wire/interconnect change -> contact/lead R + P12 + microphonics + selected P13;
- window/aperture change -> P11 radiometry/FOV/throughput;
- package-bake change -> electrical/noise/passivation state plus vacuum stability.

---

## 6. Capability prerequisites

Before capability indices or release yield are quoted for P35/P33:

1. freeze the process branch/revision;
2. qualify measurement systems for the release metrics;
3. establish process stability versus tool/consumable/run order;
4. define detector-derived engineering limits;
5. separate destructive witness metrics from production-unit metrics;
6. include cryogenic survival in the final disposition;
7. preserve failed and reworked die/package genealogy.

No universal `Cpk` threshold is introduced.

---

## 7. Yield accounting

Track at least:

- `Y_mech-singulation` — die physically separated and dimensionally acceptable;
- `Y_func-singulation` — no unacceptable pre/post device degradation attributable to singulation;
- `Y_pkg-mech` — package survives assembly/cycling;
- `Y_pkg-func` — packaged detector retains electrical/noise/optical/dynamic function;
- `Y_final` — detector meets final program performance requirements.

Do not report only mechanical die yield when functional edge damage or package-induced noise reduces detector yield.

---

## 8. First-build versus release

P16A may authorize a qualification build with P35/P33 branches labeled `LOCAL-BRANCH-FROZEN` before statistical release exists.

P17/P17A release requires repeated evidence.

Thus:

`LOCAL-BRANCH-FROZEN != LOCAL-QUALIFIED != PILOT-RELEASE != REPRODUCIBLE-RELEASE`.
