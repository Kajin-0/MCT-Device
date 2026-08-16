# Recovery checkpoint — source-recovery round 7

**Date:** 2026-08-15 America/New_York

**Purpose:** Fast handoff after the sidewall-passivation and blocking-contact functional-lineage round. Read after `AGENTS.md` and round-6 checkpoint.

## 1. New files in round 7

- `procedures/P02C_MESA_SIDEWALL_PASSIVATION_QUALIFICATION.md`
- `procedures/P08F_BLOCKING_CONTACT_SWEEPOUT_FUNCTIONAL_QUALIFICATION.md`
- `procedures/P08G_BLOCKING_CONTACT_PREDECESSOR_TECHNOLOGIES.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND7.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND7.md`

## 2. Sidewall passivation is now an explicit process gate

Same-UWA 1994 work (Siliquini et al., DOI `10.1088/0268-1242/9/8/013`) reports roughly a factor-of-two responsivity penalty when LWIR photoconductor sidewalls were left unpassivated.

This is not an RP-01 numerical target, but it proves sidewall recombination can dominate detector performance in the same lab/device family.

RP-01 process order is:

`wet mesa -> anodic oxide -> contact lithography -> localized RIE -> metal`.

Therefore mesa sidewalls are exposed when the native oxide is grown, and P02 must demonstrate electrically adequate sidewall passivation rather than merely ~80-nm planar oxide thickness.

P02C requires representative mesa/perimeter structures and either direct coverage metrology or electrical P/A scaling using responsivity/noise/leakage/lifetime.

P01 wet-etch geometry and P02 sidewall passivation are coupled; sidewall profile changes require requalification.

## 3. Blocking contacts predate RP-01

Siliquini & Faraone 1996, DOI `10.1088/0268-1242/11/12/024`, demonstrated a 3×3 n-type epitaxial HgCdTe photoconductor array with n+ blocking contacts; all elements reached BLIP at 80 K.

Accessible abstract does not state how those n+ regions were fabricated. Do not infer they were RIE-induced.

RP-01 should therefore be understood as a **fabrication simplification of an existing blocking-contact design objective**, not the invention of blocking contacts.

## 4. Three predecessor contact mechanisms must stay separate

### Ion-cleaning / accumulation contact

Ashley & Elliott 1982, *Infrared Physics* 22, 367–376:

- n-type HgCdTe;
- contact deposition preceded by ion cleaning;
- accumulation increased small-detector responsivity ~5×;
- response time strongly field dependent;
- approximate contact recombination velocity ~200–500 cm/s for x=0.30 and x=0.21 samples.

This is not RP-01 RIE.

### Wider-bandgap heterojunction contact

Smith, Arch, Wood, Walter Scott 1984, *Applied Physics Letters* 45, 83–85:

- wider-bandgap HgCdTe alloy layer inserted between metal and active photoconductor;
- sweepout/responsivity saturation strongly suppressed;
- 80-K responsivity ~4.5×10^5 V/W at 30 V/cm and >1.5×10^6 V/W at 125 V/cm.

Arch, Wood & Smith 1985, *J. Appl. Phys.* 58, 2360–2370, DOI `10.1063/1.335959`, is the detailed follow-on.

This is an epitaxial/isotype heterojunction, not an RIE n+ layer.

### RP-01 RIE n+/n contact

Canonical RP-01 process remains `CH4/5H2`, total 64 sccm, 100 mTorr, 50 W, 60 s, localized under contact windows.

P08A–P08E govern its gas ratio, sheet/depth coupling, LBIC lineage, reactor transfer and multicarrier transport.

## 5. Blocking-contact theory adds a bandwidth tradeoff

D. L. Smith 1984, DOI `10.1063/1.334155`, treats contact recombination velocity as the blocking parameter.

Stronger blocking:

- increases responsivity;
- can move D* toward background-limited behavior;
- increases effective carrier retention/lifetime;
- causes responsivity and g-r noise rolloff at **lower** frequency.

Thus blocking-contact optimization is not “maximize responsivity.” It is a coupled responsivity/noise/bandwidth problem.

P08F therefore closes detector-level contact qualification through P10/P11/P12/P13.

## 6. TLM rho_c is not contact recombination velocity S_c

Historical RP-01 TLM target:

`rho_c≈9×10^-4 Ω·cm² at 80 K`.

This characterizes majority-carrier electrical contact behavior.

Minority-carrier contact recombination velocity `S_c` controls photocarrier loss/sweepout and is not derivable from rho_c alone.

RP-01 does not publish S_c.

If S_c is later inferred locally, it must come from a validated spatial drift-diffusion model fitted to sufficient responsivity-vs-field / temporal / geometry data, not from TLM alone.

## 7. 2-D model parameters remain model-only

Smith/Musca/Faraone 2000, DOI `10.1016/S1350-4495(99)00054-7`, fit a practical MWIR photoconductor using modeled n+ density `1×10^16 cm^-3` and n+ depth `3 µm`.

These values are **not** substituted for RP-01's reported RIE state.

Their role is to demonstrate that blocking-contact depth/doping/geometry alter the 2-D electric-field and minority-carrier distribution.

## 8. P08F detector-level functional gate

A transferred blocking-contact process must demonstrate all of:

- stable/ohmic majority-carrier contact;
- acceptable TLM rho_c;
- credible P08E transport/depth state;
- reduced responsivity rolloff/sweepout over useful electric field;
- no unacceptable contact-related/1/f noise penalty;
- acceptable NEP/D*;
- acceptable P13 temporal response/bandwidth;
- reproducibility and cryogenic stability.

Normalized sweepout metric:

`S_R(E)=R(E)/R(E_ref)`

with P10 self-heating controls.

## 9. Current frontside functional model

The complete chain is now:

`P01 mesa geometry -> P02/P02C top+sidewall interface -> P08 plasma state/depth/multicarrier contact -> P09 metal/TLM -> P10 field/heating -> P11 responsivity -> P12 noise/D* -> P13 bandwidth`.

This is more physically meaningful than treating mesa, passivation, RIE and metal as independent recipes.

## 10. Highest-value next work

Round 7 completes the useful public blocking-contact history. Do not keep searching old blocking-contact papers unless a full-text archive appears.

Next recommended branch:

1. return upstream to the exact x≈0.30 LPE charge synthesis/homogenization and substrate final surface state;
2. or pursue a genuinely new archival route for the Siliquini 1995 thesis / UWA process records;
3. continue local qualification design where historical source ceilings are already documented.

## 11. Recovery order

1. `AGENTS.md`
2. this checkpoint after round 6
3. `docs/SOURCE_LEDGER_ADDENDUM_ROUND7.md`
4. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND7.md`
5. P02C / P08F / P08G
6. P08 through P08E and P10–P13 for detector-level implementation.
