# RP-01 gap matrix addendum — Round 20 Mask-2 lithography / lift-off

**Date:** 2026-08-16 America/New_York  
**Controlling new procedure:** `procedures/P27_MASK2_PHOTORESIST_EXPOSURE_DEVELOPER_LIFTOFF_EMPIRICAL_WINDOW.md`

Status vocabulary:

- `CLOSED-P`: direct RP-01 publication closure;
- `CLOSED-FAMILY`: historical process family/mechanism is strongly established;
- `TRANSFER-P`: primary transfer example only;
- `PARTIAL-P`: evidence narrows but does not close identity;
- `LOCAL-QUAL`: local qualification required;
- `OPEN`: not defensibly closed.

---

| Mask-2 item | Round-20 status | Strongest evidence/value | Remaining action |
|---|---|---|---|
| resist thickness | `CLOSED-P` | ~4–5 µm | local coating capability |
| prebake | `CLOSED-P` | 80 °C / 30 min | local calibrated bake method |
| chlorobenzene duration | `CLOSED-P` | 30 min | bath temperature/purity/order still open |
| sequence after CB | `CLOSED-P/PARTIAL` | paper says then patterned/developed/water-rinsed | resolve exact exposure ordering |
| resist survives RIE | `CLOSED-P` | directly demonstrated | local post-RIE profile capability |
| Cr/Au lift-off compatibility | `CLOSED-P` | 30/270 nm lifted off successfully | local defect/lift-off capability |
| resist chemistry family | `CLOSED-FAMILY` | positive AZ-type diazo/DNQ-novolak chlorobenzene lift-off lineage | exact product open |
| exact resist product | `OPEN` | no UWA product name recovered | thesis/process-record recovery + local screening |
| AZ4110 as historical identity | `NOT-CLOSED` | strong CB evidence; 1.1-µm quantified example | use control only, do not claim identity |
| AZ4330 thickness match | `TRANSFER-P` | ~4.3 µm @ 3500 rpm/30 s in primary example | chlorobenzene compatibility/local screen |
| AZ4400 thickness match | `TRANSFER-P` | direct 4–5-µm primary examples | exact spin/CB/exposure local screen |
| AZ4620 thickness match | `TRANSFER-P` | direct 5-µm example @ 4000 rpm | late process; local screen only |
| spin speed/time | `OPEN-HISTORICAL` | candidate examples 3000–4000 rpm in other AZ processes | set from measured 4–5 µm locally |
| exposure wavelength | `OPEN-HISTORICAL` | 365 nm appears in AZ4330 transfer example | qualify actual aligner/resist |
| exposure dose | `OPEN-HISTORICAL` | transfer examples ~78.9, 90, 150 mJ/cm² | determine clearing/profile window locally |
| exposure mode | `OPEN` | no direct contact/proximity mode | local tool qualification/source recovery |
| chlorobenzene before/after exposure | `OPEN-HISTORICAL` | Hatzakis supports both; RP-01 wording may imply pre-exposure | A/B branch until direct source recovered |
| chlorobenzene temperature | `OPEN` | transfer examples 28–30 °C etc. | define/record locally |
| chlorobenzene purity/use state | `OPEN` | historical process-control literature says impurities/use state matter | define fresh-bath baseline and track |
| post-soak bake | `OPEN-HISTORICAL` | quantified control branch uses 90 °C/10 min; RP-01 does not mention | baseline no added bake unless qualified |
| developer family | `PARTIAL-P` | aqueous alkaline strongly consistent; water rinse direct | exact product/concentration open |
| Microposit 303A | `TRANSFER-P` | direct AZ1350J chlorobenzene example | not RP-01 identification |
| AZ400K/KOH developer | `TRANSFER-P` | direct AZ4000-family process use | product-match locally |
| develop time | `OPEN-HISTORICAL` | transfer examples 10–60 s and longer depending process | local clearing/profile DOE |
| water rinse | `CLOSED-P` | direct RP-01 | exact duration/dry open |
| final dry method | `OPEN` | not reported | local qualification/source recovery |
| undercut/overhang | `OPEN-HISTORICAL` | no RP-01 number | measure local profile and lift-off outcome |
| CB thickness loss as process metric | `CLOSED-FAMILY` | IBM manufacturing control lineage | implement locally |
| post-RIE resist thickness/profile | `LOCAL-QUAL` | direct need, no historical number | measure pre/post P08 |
| lift-off solvent | `OPEN-HISTORICAL` | acetone documented in same generic CB lineage | screen sacrificially; do not claim UWA |
| lift-off time | `OPEN` | 10+5 min successful control branch; 8 h poor control example | local solvent/profile-dependent qualification |
| ultrasonics | `OPEN-HISTORICAL / RISK` | used in generic CB lift-off examples | do not baseline on HgCdTe without damage qualification |
| final lift-off defect rate | `LOCAL-QUAL` | no historical distribution | repeated runs/P17 |
| final TLM impact | `LOCAL-QUAL` | historical rho_c target from P26 | correlate P27 branch with P26 |
| low-frequency noise impact | `LOCAL-QUAL` | no isolated historical lithography comparison | matched detector P12 closure |

---

## Candidate family ranking after Round 20

### Strong chlorobenzene-control reference

`AZ4110` / `AZ1350J` lineage.

Strength: detailed historical chlorobenzene process behavior.

Weakness: quantified films in recovered examples are thinner than RP-01.

### Strong thickness candidates

`AZ4330 / AZ4400 / AZ4620-class`.

Strength: primary examples directly occupy approximately 4–5-µm film thickness.

Weakness: exact RP-01 product-specific chlorobenzene/exposure/developer branch not recovered.

**Do not collapse these strengths into a claim that UWA used one particular product.**

---

## Highest-value remaining searches

1. full RP-01-era UWA thesis/process appendices;
2. full Fathimulla 1985 experimental article;
3. full Collins/Halsted and Halverson IBM process tables if accessible;
4. UWA laboratory records naming resist/developer/lift-off solvent;
5. same-UWA 1999 contact/passivation proceedings full text;
6. exact 2000 in-situ vacuum paper experimental process details.

---

## Round-20 process consequence

A local Mask-2 transfer can now be run without arbitrary guesses:

`candidate positive thick resist -> measured 4–5 µm -> direct 80 °C/30 min bake -> direct 30-min chlorobenzene with controlled bath/order -> product-specific exposure/developer DOE -> measured undercut/profile -> P08 survival -> P26 Cr/Au -> sacrificially qualified lift-off -> 80-K TLM -> detector/noise closure`.

The product identity, exposure/developer and lift-off solvent remain historical gaps, but the experimental search space is now constrained by direct process-family evidence.
