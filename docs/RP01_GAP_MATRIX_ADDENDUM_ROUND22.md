# RP-01 gap matrix addendum — Round 22 empirical CdZnTe substrate / final-surface recovery

**Date:** 2026-08-16 America/New_York  
**Controlling new procedure:** `procedures/P29_CZT_SUBSTRATE_FINAL_SURFACE_EMPIRICAL_PROCESS_WINDOW.md`

Status vocabulary:

- `CLOSED-P` — direct RP-01 historical closure;
- `PRIMARY-TRANSFER` — direct primary process evidence from another HgCdTe branch;
- `PARTIAL-P` — primary evidence narrows but does not identify RP-01;
- `LOCAL-QUAL` — must be established locally;
- `OPEN` — not defensibly closed.

---

| Substrate / interface item | Round-22 status | Strongest evidence / current value | Remaining action |
|---|---|---|---|
| substrate family | `CLOSED-P` | electrically insulating CdZnTe | none |
| RP-01 exact Zn fraction | `OPEN` | ~4 mol% Zn is strongly represented in primary x≈0.30 LPE transfer literature | recover historical source or locally qualify measured lattice state |
| Cd0.96Zn0.04Te as transfer center | `PRIMARY-TRANSFER` | primary x≈0.30 LPE and detector-LPE literature | characterize actual supplied lot |
| historical substrate plane | `OPEN` | `{111}` strongly supported by primary LPE literature | recover RP-01 source or qualify locally |
| historical A/B polarity | `OPEN` | `(111)B` common transfer center; direct 2023 slider comparison shows A also viable | polarity DOE |
| polarity effect on wetting | `PRIMARY-TRANSFER` | contact angle A `50±2°`, B `30±2°`; A reduced residual melt in one slider process | repeat in local P03 |
| historical miscut magnitude | `OPEN` | primary dipping-LPE study showed favorable result near 1.2° off (111) | local miscut screen; no historical inference |
| historical miscut azimuth | `OPEN` | none recovered | measure/qualify locally |
| orientation/polarity verification | `LOCAL-QUAL` | XRD/Laue + validated polarity method | establish local MSA/reference |
| substrate dimensions/thickness | `OPEN-HISTORICAL` | transfer branch: 10×10×1 mm³ | choose local tool/boat-compatible geometry |
| substrate resistivity | `OPEN-HISTORICAL` | MBE transfer branch ~10^5 Ω·cm | derive local leakage/isolation requirement |
| XRD benchmark | `PRIMARY-TRANSFER` | Cd0.96Zn0.04Te best material ~25 arcsec in 1994 study | correlate local substrate XRD with epilayer/device |
| EPD benchmark | `PRIMARY-TRANSFER` | ~5×10^4 cm^-2 in same study | correlate locally; do not release as limit |
| inclusion/precipitate limit | `OPEN / LOCAL-QUAL` | primary literature establishes defect relevance | IR map + local yield correlation |
| Cu impurity relevance | `PRIMARY-TRANSFER` | substrate Cu can degrade lightly doped LPE electrical properties | obtain certificate/measurement; derive local limit |
| other trace impurity limits | `OPEN / LOCAL-QUAL` | Fe/Ni/Na/etc. controlled in related LPE apparatus/material chains | measure genealogy / correlate |
| mechanical polish traveler | `OPEN-HISTORICAL` | detector LPE branch states chemical + mechanical polish | establish local process or supplier certificate/equivalence |
| as-polished roughness | `OPEN-HISTORICAL` | no RP-01 number | local incoming surface metrology |
| final Br2/MeOH family | `PARTIAL-P / PRIMARY-TRANSFER` | detector LPE branch uses 2–3% Br2-MeOH for a few seconds | local mathematically defined recipe |
| Br2 percentage basis | `OPEN` | not defined in recovered LPE source | do not guess; explicit local basis |
| exact final-etch duration | `OPEN` | “a few seconds” only | local removed-depth/surface DOE |
| final bath temperature | `OPEN` | not recovered | log/qualify locally |
| final agitation | `OPEN` | not recovered | log/qualify locally |
| final rinse | `OPEN` | not recovered | local qualification/source recovery |
| final dry | `OPEN` | not recovered | local qualification/source recovery |
| removed depth | `OPEN / LOCAL-QUAL` | no historical depth | protected-step/witness measurement |
| surface chemistry state | `LOCAL-QUAL` | Br-MeOH can change termination/Te enrichment in CdZnTe surface studies | XPS/proxy vs growth result |
| clean-to-load time | `OPEN / LOCAL-QUAL` | transfer literature emphasizes immediate/rapid loading but no exact RP-01 value | timestamped delay DOE |
| clean-to-load atmosphere | `OPEN / LOCAL-QUAL` | not recovered | compare controlled practical ambient/inert branch |
| in-situ meltback role | `OPEN` | not closed for RP-01 | search LPE source / quantify if local P03 uses it |
| substrate genealogy effect | `PRIMARY-TRANSFER` | substrate impurity/ingot differences can change LPE electrical behavior | mandatory lot/ingot traceability |
| downstream release | `LOCAL-QUAL` | morphology + wetting + XRD/defects + x/d + Hall + detector | repeat over independent lots/runs |

---

## Round-22 selection rule

The current strongest local starting family is:

`high-quality Cd0.96Zn0.04Te {111}`

with all of the following explicitly measured/controlled:

- A/B polarity;
- miscut magnitude and azimuth;
- XRD/EPD/inclusion state;
- impurity genealogy;
- electrical isolation;
- mechanical/final-surface history;
- clean-to-load clock.

This is a **transfer center**, not a reconstructed RP-01 substrate specification.

---

## Highest-value remaining historical searches

1. RP-01/Fermionics supplier material record or source paper identifying CdZnTe composition/face;
2. Honeywell/SBRC Te-rich LPE experimental sections containing substrate orientation/miscut and final preparation;
3. original primary papers behind historical miscut claims rather than secondary reviews;
4. any source that explicitly links x≈0.30 slider-LPE morphology to CdZnTe final chemical polish/removal depth;
5. source documenting whether historical ex-situ substrate chemistry was followed by an in-situ meltback.

---

## Round-22 process consequence

P29 can now qualify substrate state as a complete interface process:

`substrate genealogy -> crystallography -> defects/impurities -> surface preparation -> clean-to-load -> melt wetting/wipe-off -> grown interface/material -> electrical/device quality`.

A vendor “epi-ready” label, 4%-Zn nominal composition, or `(111)B` marking alone is insufficient for reproducibility.
