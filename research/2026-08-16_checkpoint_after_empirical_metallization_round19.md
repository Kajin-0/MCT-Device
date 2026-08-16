# Checkpoint — after empirical Cr/Au metallization / lift-off Round 19

**Date:** 2026-08-16 America/New_York  
**Round:** 19  
**Primary new module:** P26

## Why this round was performed

The user explicitly redirected the project toward an empirical/practical fabrication manual rather than allowing theoretical derivation to substitute for recoverable process data.

After Round 18 strengthened anodic oxide/passivation, Cr/Au metallization and lift-off were the next major practical step with direct historical thickness/contact results but missing operating details.

Round 19 therefore searched primary HgCdTe papers, UWA records, current open-access interface work and author-available contact papers for actual:

- deposition method;
- deposition rates;
- surface preparation;
- air exposure;
- contact resistivity;
- post-metal heat treatment;
- TLM measurement conditions;
- lift-off/process evidence.

---

# Files created

- `procedures/P26_CR_AU_METALLIZATION_LIFTOFF_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P26_CR_AU_METALLIZATION_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND19.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND19.md`
- this checkpoint

`AGENTS.md` is updated after this checkpoint to make Round 19 the front door.

---

# Most important direct RP-01 facts retained

Canonical Cr/Au:

- Cr = `300 Å = 30 nm`;
- Au = `2700 Å = 270 nm`;
- total = `300 nm`.

Mask-2/lift-off support:

- resist ~`4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene `30 min`;
- pattern/develop/water rinse;
- same photoresist remains through RIE and is explicitly reported suitable for Cr/Au lift-off.

TLM:

- nine `300×300 µm` contacts;
- first gap `50 µm`, then +50 µm increments;
- `rho_c≈9×10^-4 Ω·cm² at 80 K`.

No direct RP-01 deposition method/rate/pressure/lift-off solvent was recovered.

---

# Direct RP-01 load-lock nuance

Smith et al. explicitly state that connecting the RIE chamber by load lock to the metal-deposition system creates a more beneficial vacuum-processing environment.

This is now classified:

`DIRECT-RP01-PROPOSED-ARCHITECTURE`.

It does **not** prove that the canonical measured devices were transferred RIE→metal entirely under vacuum.

Preserve this distinction.

---

# Strongest deposition-method conclusion

Thermal evaporation is now the strongest local transfer candidate because:

1. same-UWA 1998 HgCdTe detector work explicitly used angled thermal evaporation for contact metal deposition;
2. modern UWA HgCdTe photoconductors use Cr/Au `10/200 nm` by thermal evaporation and show linear/symmetric I–V;
3. multiple primary LPE HgCdTe Au-contact studies provide quantitative thermal-evaporation rate/contact data.

Still:

**thermal evaporation is NOT historical RP-01 closure.**

---

# Au deposition-rate empirical scale recovered

Primary LPE p-HgCdTe x≈0.29 Au study:

- thermal Au `3 Å/s`;
- thermal Au `10 Å/s`;
- as-deposited `rho_c=2.73×10^-3 Ω·cm²`;
- `80 °C / 2 h` air anneal -> `rho_c=7.11×10^-4 Ω·cm²`;
- optimized roughness ~`4.19±0.02 nm`.

Another 2026 p-HgCdTe Au study compared thermal and e-beam deposition at:

- `6 Å/s`;
- `12 Å/s`.

Thus real HgCdTe Au studies span a practical rate scale of about 3–12 Å/s.

**Use restriction:** this is experiment-sizing evidence only. It does not close RP-01 Au rate.

Cr rate remains `OPEN`.

Do not copy Au rate to Cr.

---

# Surface timing / interface chemistry recovered

2026 open-access x≈0.30 LPE HgCdTe metal-interface study:

- 9-µm Hg0.7Cd0.3Te LPE/CdZnTe;
- wet surface preparation before metal;
- one measured state used approximately `10 min` air exposure after deoxidation to represent just-before-metallization condition;
- HAXPES model estimates roughly 0.9-nm as-prepared Te oxide, ~0.3 nm after deoxidation/pre-metal, and an apparent larger buried oxide after metal;
- ToF-SIMS detects O plus cleanroom-related F/O/C/N-related interface contamination.

Do not use those oxide thicknesses as RP-01 limits.

The project consequence is:

`RIE-to-Cr time + atmosphere = mandatory process state`.

P26 traveler now records all P08→metal timestamps and cumulative air/inert exposure.

---

# Pre-metal-clean restriction strengthened

A 2005 n-HgCdTe contact process directly used:

- 500-eV Ar ion mill;
- 0.05% Br2/HBr for 2 s;
- DC-sputtered Ti/Pt/Au 300/300/4500 Å;
- low substrate deposition temperature;
- lift-off;
- low-temperature TLM.

This proves such surface-reset operations are deliberate contact-engineering steps, not harmless housekeeping.

For RP-01:

**baseline = P08 RIE state → controlled transfer → Cr.**

No undocumented ion mill/wet etch/plasma clean may be inserted after P08.

Any added pre-metal clean requires a new branch and revalidation of P08 converted state + TLM + device outputs.

---

# Post-metal thermal history

Published contact branches show that post-metal heat can materially change `rho_c`.

The 2023 p-Au branch improved after 80 °C / 2 h air anneal.

The Ti/Pt/Au branch showed cryogenic contact evolution after long low-temperature aging/annealing.

Therefore P26 baseline is:

**as-deposited, no intentional post-metal anneal**.

Any anneal is a distinct DOE branch; never import 80 °C / 2 h as RP-01.

---

# TLM background-light caution

The 2005 primary HgCdTe contact work reports low-temperature TLM distortion by background-generated carriers and uses a cold shield to obtain interpretable contact behavior.

This does not impose a cold-shield requirement on canonical RP-01 MWIR TLM.

It does require P26 to record and, during qualification, test:

- optical background;
- shield state;
- sample temperature;
- current/self-heating.

A cryogenic `rho_c` without the optical-background state is incomplete metrology.

---

# Lift-off state after Round 19

Historical RP-01 closes that the chlorobenzene-conditioned 4–5-µm photoresist successfully supported lift-off of the 30/270-nm Cr/Au stack.

Still unrecovered:

- lift-off solvent;
- temperature;
- soak time;
- agitation/ultrasound;
- rinse/dry.

P26 therefore provides a controlled local lift-off development traveler but does not invent acetone or any other solvent as historical UWA practice.

---

# Current recommended empirical replication chain

1. P08 qualification passes and Mask-2 profile survives RIE.
2. Record `t_RF_off` and all later timestamps.
3. Use shortest controlled transfer to selected deposition tool.
4. No undocumented pre-metal surface reset.
5. Record base/process pressure and full chamber history.
6. Deposit calibrated `30 nm Cr`.
7. Keep under vacuum if practical; record Cr→Au interval.
8. Deposit calibrated `270 nm Au`.
9. Record rate traces and sample thermal proxy.
10. No intentional post-metal anneal on baseline.
11. Perform locally qualified sacrificially proven lift-off.
12. Measure actual contact dimensions/gaps.
13. Perform dark 80-K I–V/TLM with background state recorded.
14. Compare with historical `rho_c≈9×10^-4 Ω·cm²`.
15. Thermal-cycle/age selected contacts.
16. Close with detector responsivity/noise/time-response on matched devices.

---

# Highest-value OPEN metallization details

- exact historical deposition method;
- metal-deposition tool/model;
- base/process pressure;
- Cr rate;
- Au rate;
- source purities/boats;
- sample temperature;
- canonical RIE-to-Cr delay;
- whether canonical Cr→Au had a vacuum break;
- exact lift-off solvent/time/temp/agitation;
- rinse/dry sequence.

Continue literature recovery before assigning any of these numerically.

---

# Recommended next empirical branch

After P26, the next largest practical fabrication gaps are likely:

1. **P14 exact photoresist / exposure / developer reconstruction**, because RP-01 gives thickness/bake/chlorobenzene but not the resist product, spin, UV dose or developer;
2. **P01 exact mesa etch chemistry implementation**, particularly resolving the percentage basis of the near-composition Br2 formulation and identifying an RP-01-compatible endpoint/rinse;
3. **P07 CdZnTe substrate orientation/final clean**, if source recovery can improve exact face/miscut/surface traveler.

Given the booklet goal, prioritize whichever branch yields the most recoverable primary process numbers rather than returning to abstract theory.
