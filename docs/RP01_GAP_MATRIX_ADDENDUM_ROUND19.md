# RP-01 gap matrix addendum — Round 19 empirical Cr/Au metallization/lift-off

**Date:** 2026-08-16 America/New_York  
**Controlling new procedure:** `procedures/P26_CR_AU_METALLIZATION_LIFTOFF_EMPIRICAL_PROCESS_WINDOW.md`

Status vocabulary:

- `CLOSED-P`: direct historical publication closure;
- `CLOSED-METHOD`: method demonstrated in same-UWA HgCdTe lineage, not direct RP-01 identity;
- `PARTIAL-P`: primary/lineage evidence narrows the gap;
- `TRANSFER-P`: primary experimental transfer value only;
- `LOCAL-QUAL`: to be established by local qualification;
- `OPEN`: no defensible numerical/process closure yet.

---

| Metallization/lift-off item | Round-19 status | Strongest evidence / value | Remaining action |
|---|---|---|---|
| metal identities | `CLOSED-P` | Cr / Au | none |
| Cr thickness | `CLOSED-P` | 300 Å = 30 nm | local thickness metrology/capability |
| Au thickness | `CLOSED-P` | 2700 Å = 270 nm | local thickness metrology/capability |
| total nominal metal thickness | `CLOSED-P/DERIVED` | 300 nm | none beyond layer metrology |
| Mask-2 resist thickness | `CLOSED-P` | ~4–5 µm | exact product/spin still open |
| Mask-2 prebake | `CLOSED-P` | 80 °C / 30 min | local profile repeatability |
| chlorobenzene treatment | `CLOSED-P` | 30 min | exact solvent grade/temp/agitation still open |
| resist retained through RIE + lift-off | `CLOSED-P` | directly demonstrated | local profile/RIE survival |
| historical deposition method | `OPEN` | RP-01 does not state method | recover source or locally choose/qualify |
| thermal evaporation as local transfer method | `CLOSED-METHOD` | same-UWA HgCdTe 1998 + modern UWA Cr/Au thermal evaporation | qualify exact local tool |
| RIE→metal load-lock architecture | `PARTIAL-P` | RP-01 explicitly identifies load-lock-connected vacuum processing as advantageous | canonical experimental use not proved |
| canonical RIE-to-Cr delay | `OPEN` | no direct time | local delay DOE; continue source recovery |
| canonical air exposure | `OPEN` | no direct value | local timing/atmosphere qualification |
| clean-to-metal surface-state importance | `CLOSED-MECHANISM/TRANSFER-P` | x≈0.30 HAXPES/ToF-SIMS shows oxide/contamination evolution; ~10 min air state directly studied | define local maximum delay from contact output |
| pre-metal wet clean | `OPEN-HISTORICAL` | none disclosed between RP-01 RIE and metal | baseline no undocumented clean; branch if needed |
| pre-metal ion mill | `NOT-RP01 / TRANSFER-P` | other HgCdTe contacts use 500-eV Ar milling | do not import without separate requalification |
| base pressure | `OPEN` | no RP-01 number recovered | log actual pressure; derive local maximum from outcome |
| process pressure during Cr/Au | `OPEN` | no RP-01 number | log/correlate locally |
| Cr source purity/form | `OPEN` | no direct source | select and record locally |
| Au source purity/form | `OPEN` | no direct source | select and record locally |
| Cr deposition rate | `OPEN` | no matched numerical rate recovered | low/center/high local rate qualification |
| Au deposition rate | `TRANSFER-P` | p-HgCdTe primary studies report 3, 6, 10, 12 Å/s | use as screening scale only; qualify local rate |
| Cr→Au vacuum break | `OPEN` | no canonical execution statement | local baseline no break where tool permits |
| substrate temperature during deposition | `OPEN` | other HgCdTe work deliberately limits metal-deposition temperature to suppress Hg loss | instrument/calibrate local thermal history |
| post-metal anneal | `OPEN-HISTORICAL` | p-Au transfer: 80 °C/2 h air changes rho_c; Ti contact branch also thermally evolves | baseline no intentional anneal; separate DOE if justified |
| QCM calibration | `LOCAL-QUAL` | standard metrology requirement; no historical record | calibrate Cr/Au separately to witness |
| historical lift-off solvent | `OPEN` | not reported | targeted source recovery + sacrificial local development |
| lift-off temperature | `OPEN` | not reported | local qualification |
| lift-off time | `OPEN` | not reported | local qualification |
| lift-off agitation/ultrasound | `OPEN` | not reported | baseline non-aggressive; qualify any ultrasound |
| post-lift-off rinse/dry | `OPEN` | not reported | local qualification/source recovery |
| TLM contact dimensions | `CLOSED-P` | 300×300 µm | measure fabricated CD |
| TLM spacing | `CLOSED-P` | 50–400 µm in 50-µm increments | measure fabricated gaps |
| TLM temperature | `CLOSED-P` | 80 K historical rho_c result | local exact T/background record |
| historical rho_c | `CLOSED-P` | ~9×10^-4 Ω·cm² at 80 K | statistical local acceptance distribution |
| TLM optical-background condition | `OPEN-HISTORICAL / TRANSFER-P` | other HgCdTe study shows low-T TLM affected by background carriers | record shield/background and test sensitivity |
| contact aging/thermal-cycle limit | `OPEN` | transfer studies show thermal evolution | local cycle/storage qualification |
| contact-to-detector noise correlation | `LOCAL-QUAL` | RP-01 device noise/D* are available but not an isolated metal DOE | matched device correlation |

---

## Highest-value remaining historical searches

1. full 2000 Smith/Winchester/Musca/Dell/Faraone in-situ-vacuum conference paper;
2. Smith/Winchester/Musca/Siliquini-era UWA theses or laboratory process appendices;
3. full 1999 “Performance and stability of HgCdTe photoconductive devices” proceedings paper;
4. any UWA process documentation naming the evaporation tool/source/rate/vacuum/lift-off solvent used with the 30/270-nm Cr/Au stack.

---

## Round-19 process consequence

The metallization branch is now sufficiently bounded to run a scientifically defensible local replication without inventing a historical vacuum or rate:

`P08 state -> timed/controlled surface transfer -> calibrated 30-nm Cr / 270-nm Au deposition -> controlled lift-off -> dimensional inspection -> 80-K TLM -> aging -> detector correlation`.

The largest remaining practical unknowns are the exact historical deposition method/rates/vacuum and the final lift-off chemistry. These remain literature-recovery priorities.
