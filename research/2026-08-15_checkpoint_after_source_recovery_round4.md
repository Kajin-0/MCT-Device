# Recovery checkpoint — source-recovery / qualification round 4

**Date:** 2026-08-15 America/New_York  
**Current checkpoint:** yes, after round 3.

Round 4 marks a deliberate transition for several blockers: archival searching has established the process family and physics but has repeatedly failed to recover unique historical RP-01 setpoints. Rather than fill those gaps with conventional fab values, controlled local qualification modules were created.

## 1. P14A — chlorobenzene lift-off lineage

Direct RP-01 Mask-2 fingerprint remains:

- resist `~4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene treatment `30 min`;
- then pattern/develop/water rinse;
- same resist retained during CH4/H2 RIE and Cr/Au lift-off;
- metal stack `30 nm Cr / 270 nm Au`.

Historical chlorobenzene lift-off literature establishes that the process is a single-layer positive diazo/novolak profile-modification method. The chlorobenzene-modified near-surface resist develops more slowly, creating undercut/overhang for metal discontinuity.

Important control variables from that literature:

- resist formulation;
- film thickness;
- residual casting solvent / soft-bake history;
- chlorobenzene soak time/T/purity/water content;
- order relative to exposure;
- exposure dose;
- developer identity/concentration/T/time;
- agitation.

### Critical historical limit

No recovered UWA/RP-01 source names AZ1350J, AZ4000/AZ4110, Shipley 1400-series, S18xx or another exact commercial resist. Those products appear only in unrelated historical chlorobenzene processes.

Do **not** assign one of them as RP-01.

Derived resist:metal thickness ratio:

- 4 µm /0.30 µm = 13.3;
- 5 µm /0.30 µm = 16.7.

This is only a geometric consistency check. P14A requires developed-profile/undercut metrology before and after P08 RIE and after metal deposition/lift-off.

Created:

- `procedures/P14A_CHLOROBENZENE_LIFTOFF_LINEAGE_ADDENDUM.md`.

## 2. Adjacent UWA photovoltaic/passivation branch — process principle only

Same-UWA primary paper:

M. H. Rais et al., “HgCdTe photovoltaic detectors fabricated using a new junction formation technology,” *Microelectronics Journal* 31(7), 545–551 (2000), DOI `10.1016/S0026-2692(00)00028-8`.

Direct experiment uses:

- p-HgCdTe LPE on CdZnTe;
- CH4/H2 RIE through windows in thermally deposited ZnS;
- ZnS remains both RIE mask and passivant;
- process intentionally avoids exposing the RIE-converted junction to atmosphere.

Dell et al. 2001, Proc. SPIE 4454, 106–115, DOI `10.1117/12.448166`, further shows strong passivant dependence of x≈.3 RIE-junction stability under 80 °C bake.

These are **different photovoltaic architectures**. Do not insert ZnS into RP-01. Their transferable lesson is that passivation and post-RIE surface exposure/thermal history are electrically consequential.

## 3. P09A — Cr/Au deposition transfer DOE

Repeated same-UWA source searching did not recover:

- historical deposition tool;
- base pressure;
- Cr/Au rates;
- substrate temperature;
- RIE-to-metal delay;
- lift-off solvent/time.

Modern UWA-associated HgCdTe photoconductor work demonstrates Cr/Au thermal evaporation, so thermal evaporation is a reasonable local candidate method but not historical proof.

P09A therefore fixes the direct RP-01 stack:

- Cr 30 nm;
- Au 270 nm;

and qualifies:

- QCM/tooling calibration;
- actual deposition pressure;
- Cr rate;
- Au rate;
- RIE-to-metal and air-exposure delay;
- Cr-to-Au vacuum break;
- substrate thermal load;
- lift-off compatibility;
- 80-K TLM;
- cryogenic aging;
- detector 1/f-noise correlation.

No arbitrary universal base pressure/rate was inserted.

Created:

- `procedures/P09A_CR_AU_DEPOSITION_TRANSFER_DOE.md`.

## 4. P03B — x≈0.30 LPE growth-time/supercooling calibration

Same-lineage Honeywell state remains:

- xL=.082;
- yL=.810;
- TL=507 °C;
- xS=.29;
- growth near 500 °C gives derived ΔT≈7 °C qualification center;
- patent example ~0.5-h growth, but not tied to xS=.29 +9.5 µm.

Wood–Hager same Honeywell atmospheric slider work reports composition uniformity/reproducibility around `σx≈0.002`, but public indexing still does not expose a usable 9.5-µm thickness/time table.

Harman-family Te-rich slider work independently establishes that **both supercooling and growth time** control thickness; published time ranges differ strongly by apparatus.

Therefore P03B maps:

`d,x,morphology = f(t_contact, ΔT0, thermal trajectory, melt geometry/history)`

rather than copying a time.

Key controls:

- bracket time at fixed thermal mode;
- bracket supercooling;
- treat step/continuous/combined cooling as separate recipe branches;
- map P06 thickness/x simultaneously;
- track charge history and Hg-loss/run-order drift;
- derive timing/T tolerances from measured sensitivities (`∂d/∂t`, `∂d/∂T`, `∂x/∂T`) after data exist.

Created:

- `procedures/P03B_X030_GROWTH_TIME_SUPERCOOLING_CALIBRATION.md`.

## 5. P04A — x≈0.30 Hg-anneal state mapping

Nagahama composition-matched branch confirms:

- x≈.17–.30;
- CdTe(111)A;
- open-tube H2 slider growth;
- as-grown p-type;
- Hg-overpressure anneal 250–400 °C;
- 250–300 °C gives n-type material without apparent composition change;
- 400 °C produces interface composition change.

The public record still does not reveal exact dwell/source/cooldown.

Harman provides a separate ~250 °C /1-h Hg-saturated screening example but generally ends in low-10^16 cm^-3 material rather than RP-01's ~10^15 scale.

P04A therefore defines the final endpoint as:

`{carrier sign, n_H/multicarrier state, µ_H, optical x/edge, thickness, morphology}`

and maps:

- dwell time;
- anneal temperature;
- Hg chemical potential/source condition;
- cooldown path;
- pre-anneal material state.

The ~250 °C /1 h point is a **screening center only**, not a production recipe.

Created:

- `procedures/P04A_X030_HG_ANNEAL_STATE_MAPPING_DOE.md`.

## 6. Repository synchronization for round 4

Created:

- `procedures/P14A_CHLOROBENZENE_LIFTOFF_LINEAGE_ADDENDUM.md`;
- `procedures/P09A_CR_AU_DEPOSITION_TRANSFER_DOE.md`;
- `procedures/P03B_X030_GROWTH_TIME_SUPERCOOLING_CALIBRATION.md`;
- `procedures/P04A_X030_HG_ANNEAL_STATE_MAPPING_DOE.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND4.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND4.md`;
- this checkpoint.

## 7. Current process philosophy after round 4

For a missing historical setpoint, there are now three acceptable states:

1. **directly recovered** from compatible primary literature;
2. **bounded candidate** from adjacent/secondary lineage with explicit provenance;
3. **locally qualified** by a controlled DOE whose endpoint is measured material/device behavior.

There is no acceptable fourth state of “ordinary semiconductor practice, therefore probably what they used.”

## 8. Highest-impact blockers still unresolved

### Chemistry/frontside

1. Br2 percentage basis in P01 or new local formulation definition;
2. exact UWA anodization traveler/rinse/dry;
3. exact RP-01 resist product/developer/exposure;
4. historical Cr/Au deposition data — local P09A now provides recovery path.

### RIE

5. primary CH4:H2 ratio / individual MFCs;
6. exact Musca-1998 plasma condition for ~8-µm conversion;
7. historical reactor geometry/self-bias/sample temperature.

### Upstream

8. exact x≈0.30 source synthesis/homogenization;
9. final CdZnTe face/miscut/surface preparation;
10. historical 9.5-µm growth schedule — local P03B recovery path now exists;
11. historical Hg anneal dwell/pHg/cooldown — local P04A recovery path now exists.

### Measurement/history

12. exact historical contact pair/gap used for Figures 3/5/6/7;
13. low-noise preamplifier / analyzer ENBW settings;
14. package/interconnect construction.

## 9. Recommended next work

Next high-value directions are:

- historical measurement-chain reconstruction (preamp/RBW/ENBW) because it affects independent D* reproduction;
- exact active-gap inference from Figures 3/5/6/7 if numerical figure data can be recovered;
- local P01/P02 DOE formalization for chemistry once the archival ceiling is accepted;
- exact x≈.30 source synthesis/homogenization and substrate surface branch;
- update front-door `AGENTS.md` to point to this round-4 checkpoint.

## 10. Recovery order

Read:

1. `AGENTS.md`;
2. through-P16 checkpoint;
3. round-1 checkpoint;
4. round-2 checkpoint;
5. round-3 checkpoint;
6. **this round-4 checkpoint**;
7. round-3 and round-4 gap/source addenda;
8. relevant procedures/addenda/DOEs.
