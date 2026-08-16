# Checkpoint — after empirical Mask-2 lithography / lift-off Round 20

**Date:** 2026-08-16 America/New_York  
**Round:** 20  
**Primary new module:** P27

## Why this round was performed

After Round 19 closed a practical Cr/Au metallization transfer route, the major remaining contact-process gap was Mask-2 lithography itself.

RP-01 gives an unusually specific fingerprint:

`4–5 µm resist -> 80 °C / 30 min prebake -> chlorobenzene 30 min -> patterned -> developed -> water rinse -> CH4/H2 RIE -> Cr 30 nm / Au 270 nm -> lift-off`.

The objective was to recover the strongest historical positive-resist / chlorobenzene process family, actual quantitative coating/exposure/development examples, and realistic lift-off controls without falsely naming the UWA resist.

---

# Files created

- `procedures/P27_MASK2_PHOTORESIST_EXPOSURE_DEVELOPER_LIFTOFF_EMPIRICAL_WINDOW.md`
- `travelers/P27_MASK2_LITHOGRAPHY_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND20.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND20.md`
- this checkpoint

`AGENTS.md` is refreshed after this checkpoint to make Round 20 the front door.

---

# Direct RP-01 Mask-2 anchors

Directly published:

- resist thickness approximately `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene soak `30 min`;
- then patterned/developed/water-rinsed;
- resist survives the contact-window CH4/H2 RIE;
- resist supports lift-off of Cr `300 Å` / Au `2700 Å`.

Still not published:

- resist manufacturer/product;
- dilution/solids;
- spin speed/acceleration/time;
- exposure wavelength/dose/tool/mode;
- exact exposure order relative to chlorobenzene;
- chlorobenzene temperature/purity/agitation;
- post-soak drying/bake;
- developer identity/concentration/time;
- post-water-rinse dry;
- lift-off solvent/time/temp/agitation.

---

# Historical process family is now strongly constrained

The Hatzakis/IBM single-step optical lift-off lineage establishes that chlorobenzene treatment is a historical method for **positive AZ-type diazo/DNQ-novolak photoresist**.

Mechanism:

- chlorobenzene penetrates/modifies the near-surface resist;
- the modified surface develops more slowly than the underlying exposed resist;
- differential dissolution creates a re-entrant/overhanging profile suitable for lift-off.

Historical process-control work shows strong coupling among:

- residual solvent / soft bake;
- exposure;
- chlorobenzene soak time;
- chlorobenzene temperature/purity/use state;
- developer strength/time;
- post-soak thermal treatment where used.

Therefore P27 treats these as a coupled process, not independent cookbook values.

---

# Candidate-resist narrowing — important, but not identity

## AZ4110

Strong direct chlorobenzene evidence.

One quantified primary example:

- `4000 rpm / 30 s`;
- `90 °C / 2 min` bake;
- UV dose `90 mJ/cm²`;
- chlorobenzene `28–30 °C / 2 min`;
- aqueous developer diluted `1:1`;
- develop `60 s`;
- water rinse/blow dry;
- final film approximately `1.1 µm`.

Conclusion:

**excellent chlorobenzene mechanism/control reference; poor thickness match in this specific coating condition.**

Do not identify RP-01 as AZ4110 from the chlorobenzene clue alone.

## AZ4330

Primary example:

- m-cresol-novolak AZ4330;
- approximately `4.3 µm`;
- `3500 rpm / 30 s`;
- `85 °C / 10 min` bake;
- `150 mJ/cm²` exposure at `365 nm`.

The example uses later silylation/development rather than chlorobenzene.

Conclusion:

**strong thickness-family match, not an RP-01 recipe.**

## AZ4400

Primary patents explicitly use AZ4400 around `4–5 µm`.

Conclusion:

**strong thickness candidate; exact chlorobenzene branch still unrecovered.**

## AZ4620

Primary later example reports approximately `5 µm` at `4000 rpm`.

Conclusion:

**strong thick-resist candidate, but late and not historical-UWA evidence.**

### Candidate hierarchy

For local screening:

- AZ4110 / AZ1350J lineage = chlorobenzene process-control references;
- AZ4330 / AZ4400 / AZ4620-class = stronger single-layer 4–5-µm thickness candidates.

No product is identified as historical RP-01.

---

# Quantified historical chlorobenzene control branch

U.S. Patent 5,654,128 provides a useful complete AZ1350J process:

- spin `3000 rpm`;
- soft bake `90 °C / 20 min`;
- chlorobenzene `15 min`;
- post-soak bake `90 °C / 10 min`;
- overhang approximately `0.4 µm` in the example;
- Cr `200 Å` / Al `9900 Å`;
- acetone `10 min` + ultrasonic agitation;
- then fresh acetone another `5 min`.

A comparative earlier branch used:

- AZ1350J `4000 rpm`;
- `90 °C / 10 min` bake;
- exposure `5.8 s × 13.6 mW/cm² ≈ 78.9 mJ/cm²`;
- chlorobenzene `10 min`;
- Shipley Microposit 303A developer `10 s`;
- acetone/ultrasonic lift-off requiring about `8 h`.

This is important empirical evidence that apparently modest changes in profile conditioning can change lift-off behavior enormously.

Do not transplant these AZ1350J values into RP-01.

---

# Chlorobenzene sequence ambiguity must remain explicit

RP-01 wording is:

`prebake -> chlorobenzene -> then patterned -> developed -> water rinse`.

A literal reading may suggest chlorobenzene before exposure, while historical Hatzakis-type processes permit chlorobenzene before or after exposure.

Until a direct UWA source closes the sequence, P27 carries two local branches:

- Branch A: `80 °C/30 min -> CB 30 min -> expose -> develop`;
- Branch B: `80 °C/30 min -> expose -> CB 30 min -> develop`.

Compare:

- film-thickness loss;
- top/bottom CD;
- undercut/overhang;
- scum;
- P08 survival;
- P26 lift-off yield.

Do not silently reorder the direct historical wording to match a familiar fab recipe.

---

# Exposure range is now empirically bounded, not assigned

Primary related process examples supply actual dose scales:

- AZ1350J branch: approximately `78.9 mJ/cm²`;
- AZ4110 chlorobenzene branch: `90 mJ/cm²`;
- 4.3-µm AZ4330 branch: `150 mJ/cm² at 365 nm`.

These establish a realistic order of magnitude for historical positive-resist screening, but are strongly product/thickness/process dependent.

P27 therefore requires an actual dose matrix around the candidate film's clearing/profile transition rather than selecting one of these values as RP-01.

---

# Developer family is narrowed but not identified

Direct RP-01:

- developed;
- water rinse.

Historical positive AZ/diazo-novolak processes use aqueous alkaline developer families, including:

- Shipley Microposit 303A in the quantified AZ1350J chlorobenzene branch;
- diluted aqueous developer in the quantified AZ4110 branch;
- AZ400K/KOH-family developers in AZ4000-series processes.

Thus an aqueous alkaline developer family is strongly mechanism-consistent.

Exact UWA product, dilution and time remain `OPEN`.

---

# Chlorobenzene itself is now treated as a controlled bath

Every P27 run records:

- product/grade/lot;
- fresh versus reused;
- bath age;
- bath temperature;
- exact soak duration;
- static/agitated state;
- sample orientation;
- film thickness before/after soak;
- post-soak drying/bake.

Historical literature shows soak temperature, impurities/use state and residual casting solvent can change penetration/profile.

Therefore `30 min in chlorobenzene` alone is not a complete reproducible process record.

---

# Lift-off solvent remains historical OPEN

Acetone is directly documented in the generic chlorobenzene-lift-off lineage, including successful quantified processes.

But no UWA/RP-01 source recovered in Round 20 identifies acetone as the historical solvent.

P27 therefore:

- does not label acetone historical;
- develops lift-off on sacrificial P14/P08/P26 stacks;
- begins with mechanically non-aggressive conditions;
- permits controlled ultrasonics only after proving no HgCdTe/mesa/passivation/contact damage.

---

# P27 local empirical sequence

1. Select candidate positive thick resist by chemistry + ability to reach 4–5 µm.
2. Determine spin condition that actually produces measured 4–5 µm after `80 °C / 30 min`.
3. Use controlled fresh/static 30-min chlorobenzene center.
4. Compare pre-/post-exposure chlorobenzene order until historically closed.
5. Run dose/developer matrix.
6. Measure resist height, top/bottom CD, undercut and scum.
7. Run P08 historical-center RIE on sacrificial profile structures.
8. Re-measure height/profile/CD.
9. Deposit P26 `30 nm Cr / 270 nm Au`.
10. Qualify lift-off on sacrificial structures.
11. Inspect final metal CD/fencing/residue/damage.
12. Close with 80-K TLM.
13. Close with detector I–V/noise/responsivity/stability on selected branch.

---

# Main historical gaps after Round 20

- exact UWA resist product;
- spin program;
- exposure tool/wavelength/dose;
- chlorobenzene order relative to exposure;
- chlorobenzene temperature/purity/agitation;
- post-soak bake/dry;
- developer product/dilution/time;
- post-rinse dry;
- lift-off solvent/time/agitation.

Continue source recovery before assigning these as historical numbers.

---

# Recommended next empirical branch

The strongest next practical gap is **P01 wet mesa etch chemistry / percentage basis / endpoint / rinse recovery**.

Existing near-composition empirical anchor:

- x≈0.28 HgCdTe;
- nominal `2% Br2` in `3:1 ethylene glycol:HBr`;
- ~`2.78 µm/min` at `21 °C`;
- anisotropy ~`0.63`;
- roughness ~`2 nm`;
- ~±26% reported rate variation;
- etch rate approximately doubles per +10 °C in the reported range;
- activation energy ~`7.5 kcal/mol`.

The source still does not define the percentage basis of “2% Br2,” which prevents an exact solution recipe.

Round 21 should aggressively search the original paper, same-author papers/theses, cited formulation lineage and patents for:

- wt%, vol%, wt/vol or other basis;
- reagent grades/concentrations;
- mixing order;
- bath volume / sample area;
- agitation;
- orientation;
- precise temperature control;
- rinse/quench;
- endpoint/overetch;
- depth and sidewall metrology;
- surface chemistry after etch.

Do not convert `9.5 µm / 2.78 µm/min ≈ 3.42 min` into a process setpoint without local depth/rate verification.
