# P24 — blocking-contact empirical qualification register

**Use with:** `procedures/P24_BLOCKING_CONTACT_EMPIRICAL_PROCESS_WINDOW.md`  
**Status:** BLANK CONTROLLED DEVELOPMENT REGISTER  
**Date:** 2026-08-16 America/New_York

Do not use this register to imply that historical-reference values are production acceptance limits.

---

# A. Run identity / material provenance

| Field | Entry |
|---|---|
| P24 record ID | |
| date / operator | |
| wafer / coupon / device ID | |
| P03 growth run | |
| wafer coordinate / orientation | |
| substrate lot | |
| source lot | |
| pre-RIE storage history | |
| previous thermal treatments | |
| downstream device/control pairing ID | |

## Pre-RIE material state

| Quantity | Result | T / method | uncertainty / note |
|---|---:|---|---|
| nominal / measured x | | | |
| optical edge metric | | | |
| HgCdTe thickness, µm | | | |
| carrier sign | | | |
| Hall density / multicarrier state | | | |
| Hall mobility | | | |
| sheet resistance | | | |
| morphology | | | |
| oxide thickness | | | |

---

# B. Historical benchmark block — reference only

These values are prefilled as `HISTORICAL-REFERENCE`, not pass/fail limits.

| Historical RP-01 item | Published reference |
|---|---:|
| reactor family | Plasma Technology parallel-plate |
| gas notation | CH4/5H2 |
| total flow | 64 sccm |
| pressure | 100 mTorr |
| RF power | 50 W |
| plasma time | 60 s |
| anodic oxide | ~80 nm |
| converted average n | ~2.0×10^15 cm^-3 |
| converted mobility | ~3.3×10^4 cm²/V/s |
| previous similar-condition n+ depth | ~8 µm — not exact canonical-device depth |
| TLM rho_c at 80 K | ~9×10^-4 Ω·cm² |
| detector noise condition | 80 K / 10 V·cm^-1 |
| 1/f knee | ~3 kHz |
| high-frequency g-r ASD | ~24.5 nV/√Hz |
| detector cutoff | ~4.4 µm |
| D* | ~2.0×10^11 cm·Hz^1/2/W at 4 µm |
| QE | ~70% |

---

# C. Reactor / chamber state

| Field | Entry |
|---|---|
| reactor manufacturer/model | |
| reactor serial / chamber ID | |
| RF frequency | |
| powered electrode dimensions / area | |
| grounded electrode / chamber geometry | |
| electrode spacing | |
| sample radial/axial position | |
| sample holder/backing material | |
| loaded sample area | |
| base pressure | |
| pressure gauge type / calibration | |
| chamber-clean method/date | |
| seasoning condition | |
| immediately prior process | |
| elapsed time since clean | |

---

# D. Gas / plasma record

| Variable | Commanded | Measured / calibrated | uncertainty / note |
|---|---:|---:|---|
| CH4 flow, sccm | | | |
| H2 flow, sccm | | | |
| other gas flow | | | |
| total flow, sccm | | | |
| CH4:H2 ratio | | | |
| pressure, mTorr | | | |
| forward RF power, W | | | |
| reflected RF power, W | | | |
| DC self-bias / ion-energy proxy | | | |
| gas stabilization time | | | |
| plasma time, s | | | |

Gas purity / lot / correction factors:

| Gas | purity | cylinder lot | MFC ID/range | correction/calibration |
|---|---|---|---|---|
| CH4 | | | | |
| H2 | | | | |
| other | | | | |

---

# E. Thermal state

| Field | Entry |
|---|---|
| chuck/electrode temperature | |
| sample starting temperature | |
| sample-temperature measurement/proxy | |
| calibrated sample peak temperature | |
| sample temperature at RF end | |
| temperature trace file | |
| cooling/hold before vent | |
| thermal calibration revision | |

**Rule:** nominal RF power is not sufficient reactor-transfer information if sample thermal state is unmeasured.

---

# F. Oxide clear / physical etch

| Quantity | Result | method | uncertainty / note |
|---|---:|---|---|
| initial oxide thickness | | | |
| oxide-clear time | | | |
| semiconductor exposure after oxide clear | | | |
| total HgCdTe recession, µm | | | |
| post-RIE roughness | | | |
| morphology / residue | | | |

Do not substitute physical recession for electrical conversion depth.

---

# G. Converted-region electrical state

## Variable-field Hall / transport

| Quantity | 80 K | 300 K | note |
|---|---:|---:|---|
| carrier sign | | | |
| sheet resistance | | | |
| Hall sheet density | | | |
| volume Hall density if depth qualified | | | |
| Hall mobility | | | |
| fit B range | | | |
| max B | | | |
| Hall curvature present? | | | |
| magnetoresistance diagnostic | | | |
| multicarrier escalation? | | | |

Raw P05 dataset link:

`______________________________`

---

# H. LBIC conversion geometry

| Field | Entry |
|---|---|
| LBIC instrument | |
| laser wavelength | |
| irradiance | |
| optical spot size | |
| sample temperature | |
| patterned-window geometry | |
| scan direction / step | |
| vertical conversion depth d_conv | |
| uncertainty / model version | |
| lateral conversion distance L_conv | |
| junction grading parameter if resolved | |
| map/data link | |

Historical practical LBIC reference:

- RP-01 test square `300×300 µm`;
- `1.047 µm` CW Nd:YLF;
- approximately `400 mW/cm²`;
- `80 K`.

---

# I. Post-RIE handling / stability record

| Event | timestamp | sample temperature | atmosphere | cumulative elapsed time since RIE |
|---|---|---:|---|---:|
| RIE end | | | | 0 |
| first Hall/LBIC | | | | |
| clean/bake | | | | |
| metallization | | | | |
| first TLM | | | | |
| detector test | | | | |
| intermediate stability repeat | | | | |
| long-interval stability repeat | | | | |
| thermal cycle | | | | |

## Stability outputs

| Quantity | immediate | intermediate | later | post-thermal-cycle |
|---|---:|---:|---:|---:|
| sheet resistance | | | | |
| Hall state | | | | |
| mobility | | | | |
| d_conv / LBIC metric | | | | |
| rho_c | | | | |
| responsivity reference | | | | |
| noise reference | | | | |

Any unplanned high-temperature exposure after RIE?

`YES / NO`

If yes, disposition:

`____________________________________________`

---

# J. Metallization / TLM

| Field | Entry |
|---|---|
| pre-metal clean | |
| RIE-to-metal elapsed time | |
| Cr thickness | |
| Au thickness | |
| deposition method | |
| base pressure | |
| deposition rates | |
| sample temperature / thermal exposure | |
| TLM pad width/length | |
| gap set | |
| TLM measurement temperature | |
| I-V linearity result | |
| sheet resistance from TLM | |
| transfer length | |
| contact resistance | |
| rho_c | |
| regression residual/QC | |

Historical comparison:

`rho_c≈9×10^-4 Ω·cm² at 80 K`.

---

# K. Detector geometry / operating state

| Field | Entry |
|---|---|
| detector ID | |
| measured active width | |
| measured contact gap L | |
| measured active area | |
| detector temperature | |
| background/FOV | |
| wavelength | |
| signal/chop frequency | |
| optical irradiance/power | |
| field grid E | |
| field based on V_active? | |
| thermal/self-heating controls | |

---

# L. Functional blocking-contact results

For each field point, attach raw P10/P11/P12/P13 data and summarize:

| E (V/cm) | I | P | R_v | e_n(f) | NEP | D* | tau_eff / f3dB | detector T | note |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

Low-field reference responsivity:

`R0 = __________`

Normalized sweepout metric used:

`S_R(E)=R(E)/R0`

Control-device/process split:

`____________________________________________`

---

# M. Empirical process-split comparison

| Split ID | variable changed | old level | new level | all fixed variables | d_conv | transport state | rho_c | R(E) result | noise/D* result | stability result |
|---|---|---:|---:|---|---:|---|---:|---|---|---|
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |

Priority factors after historical-center replication:

1. sample temperature / thermal state;
2. process pressure;
3. semiconductor exposure after oxide clear / effective dose;
4. self-bias / ion-energy / RF state;
5. gas ratio.

This priority is a qualification sequence, not a universal ranking.

---

# N. Four-gate disposition

## Gate 1 — plasma/material reproducibility

- oxide clear reproducible: `PASS / FAIL / OPEN`
- physical recession/morphology acceptable: `PASS / FAIL / OPEN`
- sheet transport reproducible: `PASS / FAIL / OPEN`
- d_conv/L_conv reproducible: `PASS / FAIL / OPEN`

Disposition:

`____________________________________________`

## Gate 2 — majority-carrier contact

- ohmic I-V: `PASS / FAIL / OPEN`
- TLM stable: `PASS / FAIL / OPEN`
- rho_c appropriate to detector current/field: `PASS / FAIL / OPEN`

Disposition:

`____________________________________________`

## Gate 3 — minority-carrier blocking function

- responsivity sweepout improved/acceptable: `PASS / FAIL / OPEN`
- self-heating separated: `PASS / FAIL / OPEN`
- comparison geometry/material adequately controlled: `PASS / FAIL / OPEN`

Disposition:

`____________________________________________`

## Gate 4 — complete detector performance

- responsivity: `PASS / FAIL / OPEN`
- noise/NEP/D*: `PASS / FAIL / OPEN`
- bandwidth/time response: `PASS / FAIL / OPEN`
- stability: `PASS / FAIL / OPEN`
- repeated devices/runs: `PASS / FAIL / OPEN`

Disposition:

`____________________________________________`

---

# O. Provenance / maturity conclusion

| Item | status |
|---|---|
| historical-center reproduction | OPEN / PARTIAL / CLOSED |
| local reactor transfer | OPEN / QUALIFIED |
| conversion-depth model | OPEN / QUALIFIED |
| majority contact | OPEN / QUALIFIED |
| minority blocking function | OPEN / QUALIFIED |
| stability | OPEN / QUALIFIED |
| detector-level candidate | OPEN / QUALIFIED |
| P17 release spec | NOT AUTHORIZED / AUTHORIZED |

Evidence files / source citations:

`____________________________________________`

Reviewer/signoff:

`____________________________________________`
