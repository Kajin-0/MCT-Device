# Recovery checkpoint — round 17 empirical blocking-contact closure

**Date:** 2026-08-16 America/New_York

**Purpose:** Fast handoff after deliberately shifting the project back toward the empirical/practical fabrication-booklet objective.

Read this first after `AGENTS.md`.

---

# 1. User direction that governs future rounds

The user explicitly noted that the target artifact is an **empirical and practical paper/booklet**, not primarily a theory monograph.

Therefore future work should:

1. search broadly across primary papers, theses, patents and institutional repositories for reported process numbers, apparatus details, times, temperatures, flows, concentrations, geometry and metrology settings;
2. extract experimentally measured outputs and failure/optimization observations;
3. use theoretical derivation only to connect genuine literature gaps or check consistency;
4. never invent a missing setpoint merely to make a traveler look complete;
5. clearly label whether a number is direct RP-01, same-lineage, transfer-family, model-only or local qualification.

This is now a continuity priority, not a one-turn style preference.

---

# 2. New round-17 files

- `procedures/P24_BLOCKING_CONTACT_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P24_BLOCKING_CONTACT_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND17.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND17.md`
- this checkpoint
- `AGENTS.md` updated after these files.

P24 supplements P08/P08D/P08F. It does not replace them.

---

# 3. Canonical RP-01 process is now captured as a practical baseline

Direct reported contact-window RIE:

- Plasma Technology parallel-plate reactor;
- `CH4/5H2`;
- total `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`;
- through approximately 80-nm anodic oxide windows.

Direct converted-region transport:

- `n_avg≈2.0×10^15 cm^-3` over converted thickness;
- `mu≈3.3×10^4 cm²/V/s`;
- Hall/resistivity measured at 80 K and 300 K;
- variable field to 2 T.

The paper cites prior same-lineage n-type work with approximately 8-µm n+ depth under similar RIE conditions.

**Do not merge the 2e15 cm^-3 average and 8-µm depth into one directly measured canonical sheet density.**

---

# 4. Historical LBIC method now has concrete apparatus numbers

RP-01 patterned RIE test structure:

- 300×300 µm.

LBIC:

- Waterloo Scientific scanning laser microscope;
- Nd:YLF;
- 1.047 µm;
- CW;
- approximately 400 mW/cm²;
- 80 K.

This gives a reproducible practical measurement target for junction-presence mapping.

The same UWA lineage demonstrates that LBIC can estimate:

- vertical conversion depth;
- lateral conversion extent;
- junction grading;
- effective converted-region doping with a validated device model.

---

# 5. Strong empirical warning: physical etch depth is not electrical depth

Siliquini et al. 1997, p-Hg0.69Cd0.31Te:

- 410 mTorr;
- CH4/H2;
- 0.4 W/cm²;
- physical etch ~0.2 µm;
- electrical conversion ~1.5 µm.

This experimentally closes the general rule

`d_etch != d_conv`.

Do not use profilometry to infer the electrical junction depth.

---

# 6. Another practical p-type x≈.29 RIE branch

Siliquini et al. 1998 institutional UWA record:

- As-doped p-Hg0.71Cd0.29Te;
- prior Hg anneal;
- CH4/H2;
- 340 mTorr;
- 0.4 W/cm²;
- LBIC fitted over 80–300 K using SEMICAD DEVICE to estimate effective converted n-type doping.

A public secondary/search snippet near 390 mTorr conflicts with the UWA institutional record. Preserve the conflict; do not average.

---

# 7. Thermal/history stability is now part of the blocking-contact process

A separate x=.31 p-type study reports:

- RIE 400 mTorr / CH4-H2 / 90 W;
- RIE n-conversion by LBIC;
- sealed-tube Hg anneal 200 °C / 17 h;
- converted n-region disappeared;
- material returned to p-like starting transport.

A different x=.21 RIE branch reports:

- 77-K conductivity fell below half after ~2×10^5 s at room temperature;
- storage at 323 K accelerated the relaxation by ~5×.

These are transfer warnings, not RP-01 limits.

New P24 rule:

Record after RIE:

- elapsed time to Hall/LBIC;
- elapsed time to metal;
- cumulative room-temperature storage;
- storage atmosphere;
- every bake/thermal exposure;
- stability after metallization/device fabrication.

A later unqualified anneal/bake is not allowed merely because the Cr/Au stack can tolerate it mechanically.

---

# 8. Later x=.30 plasma experiments provide DOE-factor priority

Park et al. 2007 used quantitative mobility-spectrum analysis in p-Hg0.7Cd0.3Te ICPRIE.

Within their investigated parameter space:

- converted transport/depth were most sensitive to pressure and sample/process temperature;
- RIE power and ICP power also had significant influence.

The reactor differs from RP-01, so no ICP numerical setpoint is transferred.

But the empirical transfer priority is now:

1. measure/control actual sample temperature;
2. pressure;
3. semiconductor exposure after oxide clear;
4. self-bias/ion-energy/RF state;
5. gas-ratio refinement.

---

# 9. Majority contact numbers are substantially closed

Direct RP-01 contact structure:

- resist ~4–5 µm;
- prebake 80 °C / 30 min;
- chlorobenzene 30 min;
- Cr 30 nm;
- Au 270 nm;
- nine 300×300-µm contacts;
- gaps 50–400 µm in 50-µm increments;
- `rho_c≈9×10^-4 Ω·cm²` at 80 K.

Still open:

- exact deposition method/rate/base pressure;
- RIE-to-metal delay;
- effective minority `S_c`.

`rho_c != S_c` remains non-negotiable.

---

# 10. Detector-level empirical closure

Canonical RP-01 functional chain includes:

- 80 K;
- stated 60° FOV;
- 1-kHz spectral response;
- responsivity-vs-field near 4 µm;
- noise at 10 V/cm using low-noise preamp + HP35665A;
- 1/f knee ~3 kHz;
- high-frequency g-r ~24.5 nV/√Hz;
- cutoff ~4.4 µm;
- D* ~2×10^11 cm Hz^1/2/W at 4 µm;
- QE ~70%.

The paper says the contact still showed high-field sweepout and was not optimized; authors identify n+ density and junction depth as optimization variables.

Thus the historical condition is a **successful baseline, not an optimum**.

---

# 11. New practical P24 release hierarchy

Gate 1 — plasma/material:

- oxide clear;
- physical recession;
- sheet transport;
- LBIC vertical/lateral conversion.

Gate 2 — majority contact:

- ohmic I-V;
- TLM;
- stability.

Gate 3 — minority blocking function:

- R(E) sweepout behavior;
- self-heating separated;
- matched controls/process splits.

Gate 4 — detector:

- responsivity;
- noise/NEP/D*;
- bandwidth/time response;
- stability;
- repeated devices/runs.

No process is released on TLM alone.

---

# 12. Highest unresolved practical numbers

Still search for:

1. exact Plasma Technology reactor model;
2. RF frequency;
3. electrode area/spacing;
4. historical self-bias;
5. sample temperature during RP-01 RIE;
6. exact individual CH4/H2 flows;
7. oxide-clear time;
8. exact physical recession in canonical 60-s run;
9. exact process tied to the ~8-µm n-type conversion depth;
10. n(z) profile and lateral conversion;
11. exact typical detector gap/contact pair in the canonical device figures;
12. RP-01 post-RIE storage/thermal stability;
13. direct n-type MWIR process-response matrix from pressure/T/time/power to depth/doping;
14. direct matched-device process-to-D*/bandwidth optimization data.

A targeted UWA thesis/dissertation search in this round did **not** surface the relevant Smith/Siliquini/Musca thesis files through the indexed institutional search results. Preserve this as a negative search; do not claim those theses are unavailable, only that the current indexed search did not recover them.

---

# 13. Next logical work

Given the user's empirical/practical emphasis, do **not** automatically continue to another abstract theoretical sensitivity derivation.

Best next sequence:

1. continue source recovery for missing blocking-contact apparatus/process numbers, especially theses/patents/full PDFs;
2. then apply the same empirical-first treatment to another weakly closed fabrication module—most likely anodic oxide/passivation or Cr/Au deposition—because those still contain transfer candidates rather than complete practical recipes;
3. only derive theory where literature recovery leaves a genuine decision-critical gap.

P24 is now the empirical front end for all further blocking-contact work.
