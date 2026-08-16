# Source ledger addendum — Round 37

**Date:** 2026-08-16 America/New_York  
**Scope:** RP-01 CH4/H2 gas-realization re-audit and anodic-oxide cell/electrolyte execution closure.

---

## 1. Round objective and disposition

Round 37 began by re-auditing P08/P08A/P24/P34 for the RP-01 notation `CH4/5H2`.

Result:

- no new primary source recovered separate historical `Q_CH4` and `Q_H2` MFC values;
- the primary UWA 1999 branch still prints `CH4/5H2`;
- P08A's same-lineage review decoding `CH4:H2=1:5` remains the strongest explicit ratio evidence;
- another RIE gas-ratio addendum would therefore be redundant.

The round pivoted to P16A R15, anodic-oxide cell/bath execution.

Round-37 output:

- new P25A apparatus/electrolyte instantiation addendum;
- new P25A qualification register;
- R15 now has a controlled closure route but remains `OPEN-CHOICE` until actual hardware/chemistry is instantiated.

---

# 2. RIE gas-ratio source re-audit

## S37-RIE-01 — Smith et al. 1999, same-UWA primary

E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “Reactive ion etching for mesa structuring in HgCdTe,” *Journal of Vacuum Science & Technology A* 17(5), 2503–2509 (1999), DOI `10.1116/1.581988`.

### Recovered primary condition

Indexed primary/authoritative records continue to report the relevant branch as approximately:

- `400 mTorr`;
- `CH4/5H2`;
- `0.4 W/cm²`.

### What this source does not close

No separate historical CH4 and H2 MFC values were recovered in the accessible primary record.

**Disposition:** `SAME-UWA-RIE / PRIMARY / GAS-SPLIT-NOT-CLOSED`.

---

## S37-RIE-02 — Smith et al. 2001 RP-01

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

Direct:

- Plasma Technology parallel-plate RIE;
- printed `CH4/5H2`;
- total flow `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`.

Still not direct:

- individual CH4 MFC;
- individual H2 MFC;
- premix-cylinder identity if any;
- gas-line/manifold architecture.

**Disposition:** `DIRECT-RP01 / TOTAL-FLOW-CLOSED / INDIVIDUAL-FLOW-OPEN`.

---

## S37-RIE-03 — Srivastav/Pal/Vyas 2005 review

V. Srivastav, R. Pal, H. P. Vyas, “Overview of etching technologies used for HgCdTe,” *Opto-Electronics Review* 13(3), 197–211 (2005).

P08A already records the explicit same-lineage table entry:

`CH4:H2 = 1:5`.

With direct RP-01 total flow 64 sccm, derived candidate individual flows are:

- `Q_CH4 = 64/6 = 10.6667 sccm`;
- `Q_H2 = 53.3333 sccm`.

These remain:

`DERIVED from DIRECT total + SAME-LINEAGE SECONDARY ratio`.

Do not state that Smith et al. directly published these MFC values.

---

## Round-37 RIE search conclusion

No source upgrade occurred. The gas-split issue is at the current documentary limit.

Future work should not repeat generic searches for `CH4/5H2` unless one of the following new source families becomes accessible:

- UWA laboratory notebook/reactor traveler;
- full primary experimental supplement with MFC table;
- thesis appendix explicitly recording gas settings;
- Plasma Technology/UWA equipment log tied to the run.

`NOT-RECOVERED != NONEXISTENT`.

---

# 3. Anodic-oxide primary source recovery

## S37-AO-01 — Catagnus & Baker, TI US3977018

P. C. Catagnus and C. T. Baker, Texas Instruments, U.S. Patent 3,977,018, “Passivation of mercury cadmium telluride semiconductor surfaces by anodic oxidation,” filed 1975, issued 1976.

### Direct photoconductor-process evidence

The patent is directly about photoconductive HgCdTe infrared detectors.

Recovered apparatus/process details:

- HgCdTe specimen is the anode;
- carbon rod cathode;
- electrolyte tank may be plastic-lined stainless steel;
- constant-current source/controller;
- recorder for current/formation time;
- several KOH/borax electrolyte families investigated.

Preferred high-uniformity electrolyte:

- `0.1 M KOH`;
- `90% ethylene glycol / 10% deionized water`;
- explicitly described as `0.1 mole KOH dissolved in 1 liter` of that mixed solvent.

Preferred process center:

- current density approximately `0.3 mA/cm²`;
- formation voltage approximately `15 V`;
- time approximately `2 min`;
- oxide approximately `800 Å`;
- uniform deep-blue film.

The patent states the formation-voltage/thickness relation for this electrolyte was reproducible run to run.

### Still not defined by recovered text

The `90% EG / 10% DI water` solvent ratio is not explicitly labeled `v/v`, `w/w`, or another basis.

Therefore:

- KOH molar inventory = source-defined;
- 90:10 ratio basis = `OPEN-HISTORICAL`.

### Derived quantity

Using KOH molar mass 56.1056 g/mol:

`0.1 mol KOH -> 5.61056 g pure KOH`.

Correct actual reagent mass for certified assay before any local preparation. This arithmetic is `DERIVED`, not a historical weighed-mass record.

### Transfer restriction

The patent's lapping, 1% Br2/methanol polishing, later buffered-HF contact-window processing and indium metallization belong to its own detector architecture. They are not inserted into RP-01.

**Disposition:** `PRIMARY-TI-PC-3977018 / STRONGEST EXECUTABLE PHOTOCONDUCTOR ANODIZATION TRANSFER`.

---

## S37-AO-02 — TI US5036376A

U.S. Patent 5,036,376, “Passivation oxide conversion.”

### Direct cell-construction evidence

The patent gives an unusually explicit HgCdTe anodization cell:

- two-electrode Teflon cell;
- HgCdTe slice horizontal;
- cleaned HgCdTe surface as anode;
- etched tungsten or titanium anode-contact probe;
- circular platinum cathode;
- Teflon or polypropylene tank;
- example electrolyte `0.1 M KOH in 10% water / 90% ethylene glycol`;
- electrolyte unstirred;
- approximately room temperature;
- constant-current supply;
- voltage and anodization time recorded.

Example material/process:

- Hg0.8Cd0.2Te;
- 20 mm × 5 mm slice;
- approximately `350 µA/cm²`;
- approximately 15 min;
- approximately `600 Å` oxide;
- reported approximate oxide composition ~50% HgTeO3 / 20% CdTeO3 / 30% TeO2.

### Transfer restriction

This is a later oxide-conversion process and uses a Pt cathode, not the earlier TI photoconductor carbon rod.

Do not combine its cell hardware with US3977018 time/thickness and claim a single published branch.

**Disposition:** `PRIMARY-TI-LATER-CELL-5036376 / APPARATUS-TRANSFER`.

---

## S37-AO-03 — x≈0.30 Janousek/Carscallen lineage

Already controlled by P02B.

Important retained conclusions:

- composition-matched n-type x≈0.30 HgCdTe;
- initial dissolution/precipitation stage;
- induction behavior depends on current density, mass transport, pH and starting surface;
- agitation can alter or prevent stable oxide growth at low current density.

Round 37 does not relabel detailed values recovered through Talasek's later synthesis as direct primary values.

**Disposition:** `PRIMARY-X030-MECHANISM / PROCESS-SENSITIVITY SUPPORT`.

---

## S37-AO-04 — other direct HgCdTe experimental support

Direct experimental HgCdTe anodization literature independently uses the same broad KOH/EG/water constant-current family near:

- room temperature;
- `0.1 M KOH`;
- `90% EG / 10% H2O` notation;
- approximately `0.2–0.5 mA/cm²` current-density range in representative work;
- oxide thickness on the order of tens of nanometers.

This supports the transfer-family plausibility but is not used to overwrite the photoconductor TI branch or RP-01 identity.

**Disposition:** `PRIMARY-HGCDTE-TRANSFER`.

---

# 4. Same-UWA passivation search

## S37-UWA-01

C. Musca, E. P. G. Smith, J. Dell, L. Faraone, “Performance and stability of HgCdTe photoconductive devices: A study of contact and passivation technology,” 1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings, IEEE, published 1999, pp. 283–286.

UWA institutional metadata confirms the paper and team overlap.

No experimental anodization recipe was exposed in the accessible institutional record.

## S37-UWA-02

C. A. Musca, J. F. Siliquini, B. Nener, L. Faraone, “Passivation and Surface Effects in Long Wavelength Infrared HgCdTe Photoconductors,” SPIE Vol. 2552, 158–169 (1995).

UWA institutional metadata confirms the paper.

No executable native-oxide traveler was recovered from the accessible metadata.

**Disposition for both:** `SAME-UWA-BIBLIOGRAPHIC-CLOSED / RECIPE-NOT-RECOVERED`.

---

# 5. Round-37 evidence-boundary conclusions

1. Direct RP-01 RIE still does not disclose individual gas flows.
2. P08A `1:5` remains the strongest candidate gas ratio and should not be repeatedly re-derived.
3. TI US3977018 materially strengthens P25 because it defines the KOH amount as 0.1 mole per liter of the stated 90/10 solvent.
4. The 90:10 solvent **basis** remains open; do not silently convert it to 900 mL + 100 mL and call that historical TI/UWA fact.
5. Carbon-rod and Pt-cathode anodization cells are different apparatus lineages.
6. Electrochemical current density is defined from actual `A_exposed`, not nominal die footprint.
7. P25A provides the method to close R15 but does not itself make R15 `LOCAL-BRANCH-FROZEN`.
8. Same-UWA passivation recipe remains historically open.
