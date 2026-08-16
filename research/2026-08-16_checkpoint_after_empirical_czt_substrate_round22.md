# Checkpoint — after empirical CdZnTe substrate / final-surface Round 22

**Date:** 2026-08-16 America/New_York  
**Round:** 22  
**Primary new module:** P29

## Why this round was performed

After P28 closed the wet-mesa branch as far as the accessible empirical literature allows, the next major upstream fabrication uncertainty was the CdZnTe substrate itself.

RP-01 directly says only that n-HgCdTe was LPE grown on an electrically insulating CdZnTe substrate. A reproducible LPE booklet cannot leave the substrate as a one-line material name because crystallographic plane, polarity, miscut, Zn/lattice state, dislocations, inclusions, impurities, mechanical damage and final surface preparation all enter the epitaxial interface.

Round 22 therefore re-read the existing P07/P07A/P07B/P07C modules and searched primary LPE/substrate literature for actual substrate/process information.

---

# Files created

- `procedures/P29_CZT_SUBSTRATE_FINAL_SURFACE_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P29_CZT_SUBSTRATE_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND22.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND22.md`
- this checkpoint

`AGENTS.md` is refreshed after this checkpoint.

---

# Direct RP-01 state — unchanged

Direct:

- CdZnTe substrate;
- electrically insulating;
- n-HgCdTe grown by LPE;
- nominal HgCdTe x≈0.30;
- HgCdTe thickness 9.5 µm.

Still historically open:

- exact Zn fraction;
- plane;
- A/B polarity;
- miscut magnitude/azimuth;
- dimensions/thickness;
- supplier/ingot;
- resistivity;
- crystalline-quality/inclusion limits;
- impurity limits;
- polish/final chemical preparation;
- clean-to-load timing.

Do not silently replace these with later industry-standard values.

---

# Strongest composition transfer center

Primary x≈0.30 LPE literature repeatedly supports Cd0.96Zn0.04Te.

A 1994 primary comparison of CdTe, Cd0.96Zn0.04Te and CdMnTe for LPE Cd0.7Hg0.3Te reported the best substrate quality in the Cd0.96Zn0.04Te branch, including representative:

- EPD ~`5×10^4 cm^-2`;
- XRD rocking-curve width ~`25 arcsec`;
- improved grown HgCdTe crystal quality relative to CdTe in that experiment.

These become **historical transfer benchmarks**, not production limits.

Therefore:

`Cd0.96Zn0.04Te` = strongest current local composition transfer center.

It is not direct RP-01 composition closure.

---

# Strong detector-LPE final-surface branch

Kubiak et al. directly report a detector-oriented Te-rich LPE process using:

- `(111)B` CdZnTe;
- `4% Zn`;
- `10×10×1 mm^3` substrates;
- chemical and mechanical polishing;
- `(2–3)% bromine-methanol` etch for `a few seconds`;
- loading into the graphite boat afterward.

This is a practical surface-preparation branch, but it is x≈0.20–0.22 material and the recovered text does not define the bromine percentage basis, exact seconds, rinse/dry or clean-to-load interval.

P29 therefore retains:

`brief Br2/MeOH + rapid boat loading`

as a transfer concept, not an executable historical RP-01 recipe.

Any local Br2/MeOH formulation must define its concentration basis mathematically.

---

# Polarity result changes the local strategy

A 2023 primary direct slider-LPE experiment compared `(111)A` and `(111)B` CdZnTe.

Recovered results:

- composition/thickness on A comparable to B;
- contact angle A: `50±2°`;
- contact angle B: `30±2°`;
- A-grown HgCdTe FWHM: `33.1 arcsec`;
- A face greatly reduced residual melt droplets in that process without reducing reported crystal quality.

This is important because P03 includes wipe-off/residual-melt control.

### Permanent consequence

Do not freeze `(111)B` merely because it is historically common.

Treat:

`polarity -> wetting -> residual melt -> wipe-off -> morphology`

as an empirical chain.

A/B polarity is now a real P29 qualification variable.

---

# Miscut remains process dependent

A primary 1996 dipping-LPE study found its best crystal quality/fewest Te precipitates near `1.2° off (111)`.

This proves low-degree miscut matters.

It does **not** justify assigning 1.2° to RP-01 or even to the local slider process.

Older secondary reviews/textbooks report differing preferred offcuts. Those were deliberately not promoted because the original primary experimental details were not recovered in Round 22.

Historical RP-01 miscut magnitude and azimuth remain `OPEN`.

---

# Substrate impurity genealogy is mandatory

Primary work by Tower et al. establishes that impurities in CdZnTe/CdTe substrates can influence lightly doped LPE HgCdTe.

Copper is a particularly important warning variable: Cu-contaminated substrate material was associated with degraded electrical/device properties and anomalous carrier behavior.

This is directly relevant to an RP-01 layer near `10^15 cm^-3` electron density.

P29 therefore records, as available:

- Cu;
- Fe;
- Ni;
- Na;
- other active trace elements;
- analytical method and detection limit;
- substrate lot/ingot position.

No universal ppb/ppm limit is released.

A substrate lot change is treated as a material-process genealogy change.

---

# “Epi-ready” is not a traveler

Primary detector LPE work uses epi-ready polished Cd0.96Zn0.04Te `(111)B`, confirming that this commercial state can support HgCdTe growth.

But “epi-ready” does not expose:

- mechanical damage removal;
- polish chemistry;
- final termination;
- roughness;
- age since clean;
- storage atmosphere.

P29 therefore requires independent incoming metrology/certificate linkage even for supplier epi-ready substrates.

---

# Detailed MBE clean retained only as contrast

A primary HgCdTe MBE branch on Cd0.96Zn0.04Te `(211)B` explicitly used:

- trichloroethylene -> acetone -> methanol degrease;
- 60 °C / 15 min;
- 0.5% Br2/methanol / 60 s;
- methanol rinse;
- substrate resistivity ~`10^5 Ω·cm`.

This is valuable evidence for the level of process detail that matters, but it is not an LPE recipe.

Do not transplant this MBE surface preparation to P03.

---

# P29 empirical chain

The new controlled substrate chain is:

1. substrate lot/ingot genealogy;
2. nominal + measured Zn/lattice state;
3. plane;
4. A/B polarity;
5. miscut magnitude + azimuth;
6. HRXRD/EPD/inclusion map;
7. impurity certificate/measurement;
8. electrical isolation;
9. mechanical polish genealogy;
10. mathematically defined final chemical treatment;
11. removed depth + morphology + surface chemistry;
12. clean-to-load timing/ambient;
13. P03 wetting/melt residue/wipe-off;
14. epilayer XRD/defects/morphology;
15. P06 x/thickness uniformity;
16. P05 transport;
17. P13/device proxy.

Release is downstream-output based.

---

# Practical first-transfer strategy

If substrate availability allows:

### Stage 1

Use a high-quality Cd0.96Zn0.04Te `{111}` family and fully characterize it.

### Stage 2

Compare `(111)A` and `(111)B` under matched P03 conditions.

Primary response should explicitly include residual melt/wetting/wipe-off behavior, not only XRD.

### Stage 3

After polarity is stable, compare bounded small miscuts based on measured supplier inventory.

Do not use 1.2° as a default setpoint.

### Stage 4

At fixed face/lot, qualify final Br2/MeOH chemistry by measured removed depth, surface state and resulting LPE interface.

### Stage 5

Map clean-to-load delay/ambient.

### Stage 6

Repeat over independent substrate lots/ingot positions.

---

# Highest-value OPEN substrate details

- exact RP-01 Zn fraction;
- exact face/polarity;
- exact miscut magnitude and azimuth;
- substrate supplier/lot;
- substrate resistivity;
- exact dimensions/thickness;
- impurity limits;
- inclusion/EPD/XRD limits;
- historical mechanical polish;
- historical final surface chemistry;
- Br2 percentage basis;
- exact final etch time;
- rinse/dry;
- removed depth;
- clean-to-load maximum;
- in-situ meltback/interface-removal history.

---

# Recommended next empirical branch

The largest remaining upstream practical gaps are now concentrated in **P03 LPE apparatus / source synthesis / charge inventory / graphite-boat geometry / growth-contact-wipeoff execution**.

A useful Round 23 would search primary Honeywell/SBRC/Harman/Radhakrishnan patents, papers and theses for actual:

- graphite boat/well dimensions;
- substrate dimensions/orientation in boat;
- total melt/charge mass;
- source synthesis method;
- homogenization duration;
- Hg-loss handling;
- equilibrium/saturation procedure;
- substrate introduction/contact sequence;
- supercooling trajectory;
- growth duration;
- wipe-off/decant mechanics;
- cooling and source reuse.

This should become a P30 empirical LPE apparatus/charge/growth traveler if sufficient primary numbers can be recovered.

Continue empirical source recovery before adding theoretical placeholders.
