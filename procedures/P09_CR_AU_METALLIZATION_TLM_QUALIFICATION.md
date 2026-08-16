# P09 — Cr/Au contact metallization, lift-off, and TLM qualification

**Status:** `CONTROLLED-QUALIFICATION-PROCESS` — the RP-01 metal stack and 80-K contact-resistivity outcome are directly anchored, while deposition method details, vacuum limits, rates, substrate temperature, lift-off chemistry and RIE-to-metal transfer window remain qualification variables.

**Purpose:** Deposit and pattern the RP-01 Cr/Au contact stack onto the P08 RIE-modified n+ HgCdTe contact regions and demonstrate reproducible ohmic behavior with specific contact resistivity compatible with the historical RP-01 result.

---

## 1. Direct RP-01 anchors

Smith et al. 2001 directly report a multilayer contact of:

- chromium: `300 Å = 30 nm` `[P-RP01]`;
- gold: `2700 Å = 270 nm` `[P-RP01]`.

The reported lift-off resist preparation was:

- resist thickness approximately `4–5 µm` `[P-RP01]`;
- prebake `80 °C` for `30 min` `[P-RP01]`;
- chlorobenzene soak `30 min` `[P-RP01]`;
- pattern/develop/water rinse before the RIE/passivant opening `[P-RP01]`.

The resulting Cr/Au contacts on CH4/H2-RIE-modified n-type MWIR HgCdTe gave:

`ρ_c ≈ 9×10^-4 Ω·cm² at 80 K` `[P-RP01]`.

This measured electrical outcome is the principal P09 benchmark.

---

## 2. Metallization-method status

The accessible RP-01 paper does **not** state whether the historical 30/270-nm stack was deposited by:

- thermal evaporation;
- electron-beam evaporation;
- sputtering;
- another PVD method.

Therefore the exact historical method remains `OPEN`.

A later UWA HgCdTe photoconductor process demonstrates Cr/Au thermal evaporation and verifies ohmic behavior over 77–300 K, establishing thermal evaporation as a strong transfer candidate. Its layer thicknesses and device architecture differ from RP-01, so its numerical process is not transferred directly.

### P09 candidate

Use **thermal evaporation** as the initial local qualification branch unless same-lineage historical evidence identifies another method.

A different deposition method requires its own contact-resistance and damage qualification because energetic-particle bombardment, substrate heating, film stress and interface chemistry differ.

---

## 3. Functional role of the bilayer

For the RP-01 contact architecture:

- the thin Cr layer acts primarily as the HgCdTe-contact/adhesion/interfacial metal;
- the much thicker Au layer provides low-resistance conduction and a bondable/probeable noble-metal surface;
- the P08 n+ region beneath the metal reduces the deleterious electrical role of the direct metal/n-HgCdTe interface.

Do not interpret the metal stack independently from the RIE-modified semiconductor state. The controlled contact is the composite:

`Au / Cr / RIE-n+ HgCdTe / n-HgCdTe`.

---

## 4. Pre-metal process gate

A wafer/coupon may enter P09 only if:

1. P08 process record is complete;
2. contact windows are fully open through the anodic oxide;
3. no gross polymer/resist residue is visible in the contact windows;
4. P08 physical recess and electrical-conversion state are within the qualification window;
5. lift-off resist remains mechanically intact after RIE;
6. no plasma-induced resist collapse blocks the contact opening;
7. RIE completion timestamp is recorded.

The contact window must not receive an undocumented wet clean after P08. Any pre-metal clean becomes a controlled process variable and requires requalification.

---

## 5. RIE-to-metal transfer

RP-01 explicitly identifies the ability to connect the RIE chamber by load-lock to a metal-deposition system as a beneficial in-vacuum process architecture.

This does not prove that every historical experimental device was metallized without atmospheric exposure, but it establishes a preferred process direction.

### P09 transfer hierarchy

Preferred:

`RIE -> vacuum transfer/load lock -> metal deposition`

Second-best qualification branch:

`RIE -> controlled inert transfer/storage -> metal deposition`

Atmospheric transfer is acceptable only as a controlled experimental branch whose delay and environment are recorded and whose TLM result passes.

### Required timestamps

Record:

- RIE RF-off;
- chamber vent;
- sample unload;
- beginning/end of atmospheric or inert exposure;
- metal-tool load;
- pumpdown start;
- deposition start.

Define:

`t_air` = cumulative uncontrolled/air exposure between RIE and Cr deposition.

`t_total` = total RIE-off to Cr-start delay.

Final maximum values remain `QUAL` and must be correlated with `ρ_c` and contact stability.

---

## 6. Vacuum-system requirements

Every P09 run must record:

- tool identifier;
- deposition method;
- chamber base pressure immediately before deposition;
- pressure during Cr deposition;
- pressure during Au deposition;
- pump type;
- chamber-clean history;
- source/crucible condition;
- residual-gas data if available.

### Base-pressure release status

No exact historical RP-01 base pressure has yet been recovered.

Therefore **do not invent a fixed vacuum number** such as `1×10^-6 Torr` and label it RP-01.

During qualification, use the best stable high-vacuum condition of the selected tool and deliberately correlate contact performance with measured base pressure if the tool's normal range is broad enough to matter.

A final base-pressure upper limit shall be set from demonstrated contact-resistivity/reproducibility data.

---

## 7. Film-thickness control

Targets:

- `t_Cr = 30 nm`;
- `t_Au = 270 nm`.

Use an in-situ quartz crystal microbalance (QCM) or equivalent thickness monitor.

### QCM qualification

Before releasing the process:

1. verify tooling factor for Cr;
2. verify tooling factor for Au;
3. deposit witness films at nominal thickness;
4. measure witness thickness independently by profilometry, ellipsometry or calibrated cross-sectional measurement;
5. derive correction factors;
6. repeat across multiple runs.

Report both:

- instrument-indicated thickness;
- independently calibrated actual thickness estimate.

Final thickness tolerances remain `QUAL` until film/contact capability is characterized.

---

## 8. Deposition-rate control

RP-01 does not report Cr or Au deposition rates.

Record continuously or at sufficient temporal resolution:

- instantaneous rate;
- mean rate;
- peak excursion;
- time to stabilize before opening the shutter;
- total layer deposition time.

Do not transfer deposition rates from a later UWA HgCdTe device or another semiconductor without qualification.

### Qualification strategy

Initially select a conservative, stable rate supported by the local evaporator and then test whether varying rate changes:

- film continuity;
- adhesion;
- surface morphology;
- lift-off quality;
- contact I–V linearity;
- `ρ_c`;
- thermal-cycle stability.

The process outcome, not an arbitrary “standard evaporation rate,” determines release.

---

## 9. Substrate temperature during deposition

HgCdTe electrical/surface state is temperature sensitive.

Record:

- holder/chuck initial temperature;
- maximum measured/estimated sample temperature during Cr;
- maximum during Au;
- cooling time between layers if any;
- backside mounting/thermal-contact method.

If direct sample thermometry is unavailable, perform a dummy thermal calibration under representative source power/deposition duration.

No intentional substrate heating is introduced into RP-01 without a separate qualification.

---

## 10. Cr deposition sequence

The Cr layer is deposited first and therefore defines the semiconductor/metal interface.

Controlled sequence:

1. confirm pre-metal gate;
2. load sample without disturbing resist profile;
3. pump to qualified base pressure;
4. stabilize deposition source/rate behind shutter;
5. record start pressure and sample/holder temperature;
6. open shutter;
7. deposit to calibrated `30 nm` target;
8. close shutter;
9. record indicated thickness, actual rate history and end pressure;
10. proceed to Au without unnecessary vacuum break.

No undocumented in-situ ion clean/plasma clean is permitted. Such cleaning could alter the deliberately engineered P08 n+ region and must be a separately qualified process.

---

## 11. Au deposition sequence

Without breaking vacuum where possible:

1. stabilize Au source/rate behind shutter;
2. verify no unacceptable sample temperature rise;
3. deposit calibrated `270 nm` target;
4. close shutter;
5. record QCM thickness/rate history and pressure;
6. cool sample sufficiently before venting to avoid resist reflow or thermally induced damage;
7. vent/unload under the qualified procedure.

The final Au thickness is much smaller than the 4–5 µm resist thickness, which supports lift-off geometrically if the resist profile/undercut is preserved.

---

## 12. Lift-off process status

RP-01 demonstrates that the chlorobenzene-treated 4–5 µm resist profile is compatible with lift-off of the 30/270-nm Cr/Au stack after RIE.

However, the paper does not disclose:

- resist product;
- lift-off solvent;
- bath temperature;
- soak time;
- agitation/ultrasonication;
- rinse/dry sequence.

These remain release blockers.

### Qualification rule

The initial local lift-off process must be developed on dummy/test structures before detector wafers and must avoid aggressive ultrasonication unless mechanical-damage testing shows it is safe for the CdZnTe/HgCdTe structure.

Record:

- solvent identity/lot;
- temperature;
- soak start/end;
- agitation method;
- any ultrasound power/time;
- rinse sequence;
- dry method.

---

## 13. Post-lift-off visual/metrology gate

Inspect every qualification device/TLM structure by optical microscopy and, where needed, profilometry/SEM.

Record:

- complete metal removal outside intended regions;
- metal fencing/stringers;
- discontinuities/voids;
- edge tearing;
- resist residue;
- pinholes;
- pad scratches;
- Cr/Au delamination;
- contact-window registration;
- actual contact dimensions.

For process-development coupons, measure final metal thickness on a witness and step coverage/edge profile on representative structures.

---

## 14. Ohmic I–V qualification

Before TLM extraction, verify contact linearity.

At minimum:

- measure in darkness;
- test both polarities;
- sweep a sufficiently small voltage/current range to avoid self-heating or carrier sweepout;
- repeat at 80 K;
- optionally repeat at 300 K for process diagnosis.

Pass condition:

- symmetric, linear I–V within measurement uncertainty over the declared low-field range;
- no hysteresis or time-dependent instability beyond repeatability.

A contact that yields a low apparent resistance only at one bias polarity is not accepted as ohmic.

---

## 15. RP-01 TLM geometry

The published TLM structure contains:

- nine contacts;
- each approximately `300 µm × 300 µm`;
- first contact spacing `50 µm`;
- successive spacing increments `50 µm`.

Use this geometry as the initial canonical TLM monitor unless mask reconstruction establishes additional dimensional details.

Record actual fabricated contact dimensions and gaps by calibrated optical metrology rather than assuming mask nominal dimensions.

---

## 16. TLM extraction

For each adjacent/relevant contact pair:

1. measure low-field two-terminal resistance at 80 K;
2. use current reversal;
3. verify linearity and thermal stability;
4. record actual gap length;
5. plot measured total resistance against contact spacing;
6. perform weighted linear regression;
7. inspect residuals for nonlinearity/contact variability;
8. extract sheet/contact terms using the documented TLM geometry model;
9. calculate transfer length and specific contact resistivity where the geometry assumptions are valid.

Store:

- raw I–V data;
- pair resistance;
- gap dimensions;
- regression slope/intercept;
- covariance/uncertainty;
- extracted sheet resistance;
- contact resistance;
- transfer length;
- `ρ_c`.

Do not report `ρ_c` without the regression plot/residual or enough information to reproduce the extraction.

---

## 17. Historical electrical benchmark

RP-01 reports:

`ρ_c = 9×10^-4 Ω·cm² at 80 K`

for the Cr/Au contact technology on RIE-modified n-type MWIR HgCdTe with an average contact-region n-type level near `2×10^15 cm^-3`.

This is the initial P09 benchmark, not yet the final statistical upper specification.

A transferred process should aim to reproduce or improve this value while retaining:

- ohmic symmetry;
- low contact-to-contact spread;
- detector performance;
- thermal-cycle stability.

---

## 18. Contact-to-contact uniformity

For the nine-contact structure report:

- mean pair/contact metric;
- standard deviation;
- coefficient of variation;
- min/max;
- outlier criterion;
- spatial trend.

A low mean `ρ_c` with one or more unstable/high-resistance contacts is not a robust production process.

Final statistical acceptance limits require repeated wafers/lots.

---

## 19. Thermal-cycle stability

HgCdTe detectors operate cryogenically, so contact integrity must be checked after thermal cycling.

Qualification cycle:

- room temperature -> ~80 K -> room temperature;
- repeat enough cycles to expose gross adhesion/interfacial problems before process release.

At selected cycles repeat:

- visual inspection;
- representative contact I–V;
- TLM or pair resistance.

Final required cycle count and drift tolerance remain `QUAL`.

---

## 20. Process-variable DOE

The minimum P09 transfer program should separate four questions.

### A. Vacuum-transfer delay

At otherwise fixed deposition conditions, compare controlled `t_air/t_total` branches including the shortest achievable transfer.

Response: I–V, `ρ_c`, spread, aging.

### B. Cr rate / interface formation

Vary Cr deposition rate within the stable local-tool range.

Response: adhesion, `ρ_c`, film continuity.

### C. Au rate / heating

Vary Au rate while monitoring holder/sample temperature.

Response: lift-off quality, stress, heating, pad integrity.

### D. Vacuum quality

If the tool allows controlled variation or natural run-to-run base-pressure variation, correlate `ρ_c` and contact aging with measured residual pressure rather than setting a vacuum limit by convention.

---

## 21. Failure modes

Log:

- incomplete lift-off;
- metal fencing;
- Cr/Au delamination;
- pad cracking;
- non-ohmic/rectifying I–V;
- excessive `ρ_c`;
- strong contact-to-contact spread;
- regression nonlinearity;
- contact aging after hours/days;
- thermal-cycle drift;
- surface contamination from RIE-to-metal delay;
- excessive deposition heating;
- poor QCM/witness agreement;
- vacuum excursions;
- source spitting/particulate contamination;
- unintended plasma/ion cleaning damage.

---

## 22. Safety hold point

P09 uses vacuum deposition equipment, high-current/high-temperature evaporation sources, Cr and Au materials, solvents for lift-off, cryogenic characterization and HgCdTe containing Hg/Cd. Execution requires equipment-specific vacuum/high-voltage/thermal interlocks, source-material handling, solvent/EH&S controls, toxic-metal contamination control and cryogenic procedures.

---

## 23. Release blockers

P09 remains `CONTROLLED-QUALIFICATION-PROCESS` until the following are closed:

1. exact historical or selected deposition method;
2. chamber/base-pressure limit;
3. Cr deposition rate and allowed variation;
4. Au deposition rate and allowed variation;
5. sample-temperature limit;
6. QCM tooling-factor/thickness calibration;
7. exact RIE-to-metal transfer architecture and maximum delay;
8. any pre-metal clean, if used;
9. exact lift-off solvent/time/temperature/agitation;
10. post-lift-off rinse/dry;
11. final Cr/Au thickness tolerances;
12. TLM extraction uncertainty;
13. statistical `ρ_c` acceptance window;
14. contact-to-contact uniformity criterion;
15. thermal-cycle count/drift limit;
16. aging/stability requirement.

---

## 24. Primary/lineage sources

1. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors,” Proceedings SIMC-XI (2000), pp. 318–321.
3. C. Musca, E. P. G. Smith, J. Dell, L. Faraone, “Performance and stability of HgCdTe photoconductive devices: A study of contact and passivation technology,” 1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings (published 1999), pp. 283–286.
4. Later UWA HgCdTe photoconductor work using thermally evaporated Cr/Au contacts is retained as transfer-method evidence only; its material architecture and metal thickness differ from RP-01 and its numerical deposition recipe is not transferred.
