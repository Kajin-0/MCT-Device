# RP-01 gap matrix addendum — Round 33: singulation / dicing / die-edge damage

**Date:** 2026-08-16 America/New_York

Round 33 closes a structural documentation gap by adding P35, but it does not recover the historical UWA singulation traveler.

---

## 1. Gap status matrix

| Item | Current status | Strongest evidence | Required closure |
|---|---|---|---|
| exact RP-01 die separation method | `OPEN-HISTORICAL` | RP-01 silent in audited text | UWA notebook/thesis/process traveler or direct author documentation |
| final RP-01 die outline | `OPEN-HISTORICAL` | no direct dimension recovered | historical drawing/traveler or device photo with calibrated scale |
| cut street / active-edge clearance | `OPEN-HISTORICAL` | no RP-01 value | historical layout/traveler; otherwise local functional qualification |
| diamond blade identity | `OPEN-HISTORICAL` | Rockwell shows HgCdTe diamond-grit saw was a conventional branch, not RP-01 identity | direct UWA record |
| wire-saw identity | `OPEN-HISTORICAL` | Yoo 1998 gives finished-CZT branch | direct UWA record |
| scribe/cleave use | `OPEN-HISTORICAL` | no same-UWA executable source recovered | direct UWA record |
| laser/excimer use | `OPEN-HISTORICAL` | Rockwell transfer branch only | direct UWA record |
| protection coating | `OPEN-HISTORICAL` | photoresist/wax and polyimide transfer branches | direct UWA record or local compatibility qualification |
| temporary mount/fixture | `OPEN-HISTORICAL` | graphite/wax CZT transfer only | direct UWA record or local qualification |
| coolant/slurry chemistry | `OPEN-HISTORICAL` | BN slurry CZT transfer only | direct UWA record or local qualification |
| saw/wire speed/feed/depth | `OPEN-HISTORICAL` | no RP-01 setpoint | direct UWA record or local DOE |
| laser wavelength/fluence/pulses | `OPEN-HISTORICAL` | Rockwell branches only | direct UWA record or local DOE |
| post-cut cleaning | `OPEN-HISTORICAL` | finished-CZT solvent/Br branch not compatible by default | direct UWA record or local compatibility qualification |
| post-cut damage-removal etch | `OPEN-HISTORICAL` | bulk-CZT transfer shows deep damage/removal need | avoid as default; local finished-device material-removal study if considered |
| visible chip acceptance | `LOCAL-QUAL REQUIRED` | no RP-01 criterion | calibrated optical edge statistics + downstream functional data |
| subsurface-damage acceptance | `LOCAL-QUAL REQUIRED` | primary CZT evidence shows hidden damage | destructive/non-destructive witness method + local correlations |
| functional edge clearance | `LOCAL-QUAL REQUIRED` | direct HgCdTe transfer shows edge-distance dependence | pre/post P10/P12/P11 versus cut distance |
| cryogenic edge survival | `LOCAL-QUAL REQUIRED` | P33 package stress framework | cooldown/warmup genealogy + crack/electrical/noise closure |
| tool wear/dressing life | `LOCAL-QUAL REQUIRED` | generic process physics; no RP-01 record | repeated-run data versus tool state |
| clean-to-die-attach interval | `LOCAL-QUAL REQUIRED` | P16 recognizes clock; no limit | repeated local stability/contamination data |

---

## 2. Closed methodological gaps

### 2.1 Separate singulation execution module now exists

Before Round 33, P15 contained a generic die-separation placeholder and P16 STEP G1 referenced it without an executable empirical process window. P33 began from an already singulated die.

P35 now closes this documentation architecture gap.

### 2.2 Functional edge damage distinguished from visual damage

P35 now distinguishes:

- `d_visible` — distance to visible damage/kerf;
- `d_functional` — distance required to avoid measured device degradation;
- `d_release` — local released exclusion including uncertainty/margin.

### 2.3 Subsurface damage is an explicit release axis

Primary CdZnTe manufacturing evidence demonstrates that saw-induced damage can extend substantially below a visibly acceptable surface. P35 therefore requires a subsurface-damage qualification route during process development.

### 2.4 Finished-device chemistry is protected

Bulk-CdZnTe post-saw bromine etches are explicitly barred from automatic transfer to the completed RP-01 device stack.

### 2.5 Cryogenic closure is required

P35 room-temperature success does not close singulation. Final `RP01-SINGULATION-QUALIFIED` requires P33 feedback after cryogenic package cycling.

---

## 3. Candidate process branches and status

| Branch | Evidence | Status for RP-01 reconstruction |
|---|---|---|
| abrasive blade saw | direct HgCdTe historical transfer evidence; known damage mechanisms | candidate only; settings OPEN |
| low-force wire saw | direct finished-CdZnTe process evidence | strong candidate transfer branch; settings must be locally qualified |
| scribe/cleave | physically plausible for crystalline II–VI | candidate only; strong dependence on P29 crystallography; no direct RP-01 evidence |
| excimer/laser | direct HgCdTe detector-array transfer evidence | candidate only; chemical/stoichiometric damage must be qualified |

No branch is currently declared the RP-01 historical method.

---

## 4. Prohibited shortcuts added in Round 33

Do not:

- infer the historical UWA method from the fact that diamond-grit saws were conventional for HgCdTe;
- set edge exclusion to a Rockwell `9–19 µm` mechanical-saw value;
- set edge exclusion to a Rockwell `0–6 µm` excimer value;
- use the Yoo `125 mm / 16 µm BN / ~1 h` branch as an RP-01 recipe without local finished-stack qualification;
- use `5% Br/methanol / 5 min` to clean a completed RP-01 die by default;
- assume no visible chips means no damage;
- assume laser separation is chemically inert;
- ignore P29 crystallography in a scribe/cleave branch;
- release a die before P33 cryogenic edge survival is checked.

---

## 5. New P35 release vector

Input/process vector:

`X_SING={method,tool/revision,crystal orientation,street/protection/support,blade-wire-laser state,motion parameters,coolant/slurry,pass sequence,tool age/conditioning,clean/release,handling}`.

Outcome vector:

`Y_SING={kerf_width,position_error,die_dimensions,squareness,front/back chipping,crack length/depth,subsurface damage,edge roughness/taper,residue,passivation/metal damage,Delta_R/I-V,Delta_noise,Delta_responsivity,cryogenic survival}`.

The process is released only against the complete response vector.

---

## 6. Highest-value historical recovery targets

1. UWA/Fermionics wafer/die photographs or mask/layout drawings showing final die street and outline.
2. UWA 1990s/2000s detector fabrication thesis sections mentioning dicing/scribing.
3. Siliquini/White/Westerhout theses if full experimental sections become accessible.
4. Smith/Musca/Dell/Faraone laboratory travelers or archived device-process notebooks.
5. Any supplier/Fermionics documentation indicating whether material arrived as coupon/die or was separated at UWA.

“Not recovered” remains different from “not used.”

---

## 7. Strongest next process question after P35

After P35, the front-end fabrication sequence from final device metal to P33 package is structurally complete enough to justify a **P16 end-to-end release-readiness audit**.

That audit should identify which remaining `OPEN-HISTORICAL` variables actually prevent a first physically reproducible local build, versus which variables can be legitimately replaced by local qualified transfer processes without claiming historical identity.
