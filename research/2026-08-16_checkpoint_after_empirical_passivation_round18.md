# Checkpoint after empirical passivation Round 18

**Date:** 2026-08-16 America/New_York  
**Repo:** `Kajin-0/MCT-Device`

## What Round 18 changed

Round 18 continued the user-requested shift from theory-first development to **empirical/manual-first reconstruction**.

The P02 native anodic-oxide branch now has a dedicated practical process module:

- `procedures/P25_ANODIC_OXIDE_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P25_ANODIC_OXIDE_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND18.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND18.md`

P25 supplements P02/P02A/P02B/P02C rather than replacing their historical/provenance rules.

---

## Strongest direct RP-01 fact

RP-01 directly establishes:

- native anodic oxide;
- nominal thickness approximately `800 Å = 80 nm`;
- oxide formed after mesa definition and before Mask-2/RIE contact opening.

RP-01 still does not disclose its exact anodization bath/current/cell/endpoint/rinse.

---

## Strongest executable transfer center

Texas Instruments U.S. Patent 3,977,018 gives an actual HgCdTe photoconductor anodization process that independently lands at approximately the RP-01 800-Å film:

- HgCdTe = anode;
- carbon-rod cathode;
- `0.1 M KOH`;
- `90% ethylene glycol / 10% DI water`;
- galvanostatic constant current;
- approximately `0.3 mA/cm²`;
- terminal/formation region around `15 V`;
- approximately `2 min`;
- approximately `800 Å` film;
- uniform deep-blue appearance.

This is the default **transfer center**, not the historical UWA recipe.

Never rewrite it as `DIRECT-RP01`.

---

## Independent empirical support

A direct experimental Hg0.8Cd0.2Te C–V/native-oxide study used:

- 0.1 M KOH / 90% EG / 10% water;
- room-temperature anodization;
- approximately 0.2–0.5 mA/cm² constant-current density;
- example oxide ~70 nm.

Thus the TI transfer center sits inside a real experimentally used HgCdTe anodization family.

Composition/structure work including n-type x≈0.30 shows that film chemistry changes materially with pH, current density and EG/water environment. Equal film thickness is therefore not sufficient evidence of interface equivalence.

---

## Voltage-time trace is now mandatory

P25 no longer treats `0.3 mA/cm² for ~2 min` as a sufficient recipe description.

For every run store and reduce:

- exposed area;
- current/current density;
- raw `V(t)`;
- induction interval `t_ind`;
- growth-region `dV/dt` descriptor;
- terminal voltage;
- total charge;
- charge per area;
- final oxide thickness;
- physical uniformity;
- interface/device outputs.

The x≈0.30 anodic-oxidation lineage shows a dissolution/precipitation induction stage that depends on mass transport, current density and starting surface. A final 80-nm film reached after an anomalous V(t) trace is not automatically process-equivalent.

---

## Agitation / cell geometry are not incidental

P25 requires explicit record of:

- anode contact;
- cathode material;
- cathode dimensions;
- electrode separation;
- sample orientation;
- immersion depth;
- exposed top/sidewall/backside area;
- agitation state/rate;
- bubbles.

First transfer condition is a static/unstirred bath unless a selected primary implementation requires otherwise.

The TI carbon cathode and later Pt-cathode lineages remain distinct. Do not merge their details.

---

## Electrical passivation is a separate output

Other-x native-oxide work supplies approximate interface-state/fixed-charge scales, but P25 does not turn those into RP-01 specifications.

Same-UWA x≈0.23 gate-controlled photoconductor work is especially important functionally:

- surface accumulation can suppress recombination;
- excessive accumulation can create surface shunting;
- that device showed an optimum surface potential near 50 mV versus a floating value near 72 mV and ~70% responsivity improvement near the optimum.

These numbers are transfer-only.

Permanent practical conclusion:

**passivation must be optimized on detector responsivity/noise/electrical behavior, not by maximizing accumulation or matching oxide thickness alone.**

---

## Sidewall / downstream chain

P02C remains mandatory because RP-01 anodizes after mesa etch.

P25 release requires:

`oxide formation -> sidewall coverage -> P08 oxide clear/n+ conversion -> P09 TLM -> P10 dark electrical -> P11 responsivity -> P12 noise/D* -> P13 dynamics`.

An 80-nm planar witness is not sufficient.

---

## New practical traveler

The P25 register records:

- incoming surface provenance;
- bath preparation and age;
- cell geometry;
- electrochemically exposed area;
- actual current/J;
- full V(t);
- induction/growth metrics;
- charge/area;
- rinse/dry;
- film thickness/uniformity/color;
- C–V/field-effect/interface results when used;
- sidewall result;
- P08 oxide clear;
- P09 contact result;
- detector noise/responsivity/time response;
- storage/bake/cryogenic history.

This is intentionally operator/manual oriented.

---

## Source-recovery results / negative searches

New or reinforced source records:

- TI anodic-oxide patent — executable transfer process;
- direct HgCdTe C–V/native-oxide experiment;
- x≈0.30 oxide chemistry/mechanism lineage;
- native-oxide interface electrical study;
- same-UWA gate-controlled photoconductor passivation;
- John K. White 2005 UWA thesis institutional record;
- Ryan Westerhout 2013 UWA thesis institutional record;
- Smith et al. 2000 same-UWA “Dry plasma technology for in-situ vacuum processing…” conference record.

The White/Westerhout direct institutional thesis PDF endpoints were identified but inaccessible through the current retrieval route. The dry-plasma full paper also remains unrecovered.

This is negative-search evidence only; do not infer the documents lack the missing details.

---

## Current P25 release blockers

1. exact historical UWA anodization traveler;
2. local 90:10 ratio preparation convention and reagent grades;
3. selected local cathode geometry/separation;
4. exposed-area definition/fixture;
5. RP-01-compatible minimal-damage pre-anodization clean;
6. exact local rinse/dry sequence;
7. x≈0.30 LPE V(t)/Q/A/thickness repeatability;
8. electrical-interface/noise acceptance metric;
9. sidewall closure;
10. P08 oxide-clear compatibility;
11. storage/thermal stability;
12. P17 repeated-run capability.

No production tolerance is released.

---

## Important continuity rule added by Rounds 17–18

For fabrication-manual gaps, search for actual experimental numbers before building a theoretical surrogate.

Preferred evidence order:

1. exact RP-01 paper/supplement/thesis;
2. same-UWA experimental lineage;
3. composition-/architecture-matched primary experiments;
4. primary patents/process disclosures;
5. carefully labeled transfer-family experiments;
6. theory only where empirical closure ends.

---

## Strongest next action

Proceed with **Round 19 empirical Cr/Au metallization / lift-off / vacuum-transfer recovery**.

Search broadly for the exact UWA/RP-01-era metallization method and practical numbers:

- thermal vs e-beam evaporation;
- base pressure;
- Cr/Au deposition rates;
- source material/purity;
- substrate temperature;
- tooling/boat/crucible;
- chamber history;
- RIE-to-metal delay and storage;
- in-situ vs air transfer;
- lift-off solvent/time/agitation;
- post-metal anneal, if any;
- contact adhesion/stability/cryogenic cycling;
- TLM conditions and geometry.

RP-01 directly closes only Cr 30 nm / Au 270 nm and resulting ~9e-4 ohm cm² at 80 K. The next round should attempt to turn that into an actual practical deposition traveler before adding more contact theory.
