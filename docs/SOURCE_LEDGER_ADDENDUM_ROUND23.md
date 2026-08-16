# Source ledger addendum — Round 23: Te-rich horizontal-slider LPE execution

## Scope

Primary-source recovery for P30: boat topology, source synthesis, charge inventory, equilibration, thermal trajectory, Hg-loss compensation, contact duration, slide-out and wipe-off.

## S23-01 — Bowers & Schmit, Honeywell, US4317689A

**Class:** `DIRECT-HONEYWELL-PATENT`

Recovered directly:

- atmospheric-pressure Te-rich slider LPE;
- covered graphite slider/base/cover architecture;
- substrate recess and covered growth-solution well;
- auxiliary HgTe or HgTe+Te source beneath cover;
- Hg-distribution grooves/moats;
- N2 purge before heating, then flowing H2;
- solution heated above liquidus and brought below liquidus for growth;
- allowed thermal modes: step supercooling, slow cooling after contact, or combination;
- example growth may continue ~0.5 h;
- tie line `xL=.082`, `yL=.810`, `TL=507 °C` -> `xS=.29`, `xS/xL=3.54`;
- Hg vapor pressure described as ~0.1 atm near 500 °C in relevant Te-rich regime.

Not recovered:

- exact total charge mass;
- dimensioned machining drawing;
- historical gas flows;
- exact equilibration duration for xL=.082/yL=.810;
- exact supercooling/contact/cooling trajectory used for the xS=.29 run.

## S23-02 — Hager & Wood, Honeywell, US4592304A

**Class:** `DIRECT-HONEYWELL-WIPEOFF`

Recovered directly:

- dedicated wipe-off well adjacent to growth well;
- several CdTe pieces held in vertical slots about 1 mm apart;
- pieces are polycrystalline/unpolished in described implementation;
- pieces rest against base and pass across grown epilayer;
- wipe-off mechanisms stated: mechanical wiping, surface-tension adhesion, capillary wicking;
- wipe-off region remains under Hg-source pressure;
- pieces discarded after cooldown.

Do not infer this exact hardware generation was used to produce RP-01 material.

## S23-03 — Hager, Honeywell, US4706604A

**Class:** `DIRECT-HONEYWELL-WIPEOFF`

Recovered directly:

- later scribed-CdTe-apron wipe-off architecture;
- CdTe apron sits in tandem with growth substrate;
- apron can be polycrystalline or single crystal of any orientation;
- diagonal scribe marks formed with diamond scribe;
- growth solution overlaps at least part of apron;
- finite slider clearance is necessary to avoid scratching but leaves a residual liquid film;
- apron/scribes prevent reverse migration of final drop after slide-out;
- patent reports complete/100% wipe-off for described arrangement.

Critical consequence: slider clearance and wipe-off geometry are coupled morphology variables.

## S23-04 — Harman 1980

T. C. Harman, “Liquidus isotherms, solidus lines and LPE growth in the Te-rich corner of the Hg-Cd-Te system,” *Journal of Electronic Materials* 9 (1980), DOI `10.1007/BF02822728`.

**Class:** `PRIMARY-HARMAN-1980`

Recovered directly:

- Te-rich HgCdTe LPE under flowing H2 using horizontal slider;
- growth temperatures `450–550 °C`;
- growth times `0.25–10 min`;
- typical solution equilibration `~1 h at 550 °C`;
- highest-quality layers used source wafers, supercooled solutions and `(111)` substrates;
- resulting layers `3–15 µm` in that study.

Restriction: these are branch ranges, not an x≈0.30 RP-01 recipe.

## S23-05 — Radhakrishnan, Sitharaman & Gupta 2003

J. Cryst. Growth 252 (2003) 79–86, DOI `10.1016/S0022-0248(02)02530-7`.

**Class:** `PRIMARY-RSG-2003`

Recovered directly:

### Hardware
- high-purity/high-density graphite slider boat;
- base + movable sliding plate;
- recess for `15×15×1 mm` CdZnTe substrate;
- block with solution bins and HgTe cavity;
- tightly fitting graphite cover;
- horizontal quartz tube with stainless flanges;
- ports for gas flow, push-pull rod and thermocouple;
- provision for in-situ meltback and improved wipe-off.

### Source synthesis
- `10 g` growth compound synthesized;
- representative composition parameter `z≈0.049`, `y≈0.84`;
- `6N` Cd/Te/Hg;
- evacuated quartz ampoule;
- `700 °C / 8 h`;
- synthesized material ground and thoroughly mixed;
- `~4.8 g` per growth run;
- `3 g HgTe` for Hg-loss compensation per run.

### Morphology conclusion
- smooth/uniform slide-out and careful loading reduce voids/pinholes/melt traps.

Restriction: different composition/device branch. Numerical masses/times are experiment-sizing transfer data only.

## S23-06 — Shinohara et al. 1994

J. Cryst. Growth 141 (1994) 352–356, DOI `10.1016/0022-0248(94)90237-2`.

**Class:** `PRIMARY-SHINOHARA-1994`

Recovered directly:

- slider LPE with HgTe reservoir;
- increased HgTe reservoir inventory can stabilize source-liquid weight against Hg evaporation;
- equilibrium cooling from melting point gave `2–4 µm` layers with slight terracing;
- supercooling/step cooling with `15 K` supercooling gave `30–40 µm` layers;
- composition range `x≈0.25–0.42`.

Use: proves thermal trajectory and Hg reservoir inventory are major process coordinates.

## S23-07 — Bernardi et al. 1988

J. Cryst. Growth 87 (1988) 365–371, DOI `10.1016/0022-0248(88)90189-3`.

**Class:** `PRIMARY-BERNARDI-1988 / ALTERNATE-SOLUTION-PREPARATION`

Recovered directly:

- in-situ Te-rich MCT solution preparation by Hg vapor transport into Cd-rich Te melt;
- method can avoid separate in-ampoule preparation/homogenization for every run;
- thermal control is emphasized for reproducibility;
- procedure allows maintaining solution around liquidus without compositional change.

Restriction: separate source-preparation family; do not merge with ampoule synthesis.

## Negative / unresolved searches

Still not recovered from accessible primary text:

- exact Honeywell graphite boat machining dimensions;
- exact total growth charge mass for xL=.082/yL=.810;
- exact source-wafer composition/size for Harman highest-quality x≈.3 branch;
- historical Honeywell/Harman H2 and N2 flows;
- exact slider speed and clearance;
- exact x≈.29 contact time/supercooling trajectory;
- exact RP-01 supplier growth sequence;
- melt reuse/depletion traveler for the original source material.

These remain `OPEN`; absence from this recovery round is not proof of nonexistence.
