# RIE gas-split source recovery — CH4/5H2 notation

**Date:** 2026-08-15 America/New_York

## Question

What did the UWA/RP-01 notation `CH4/5H2` mean quantitatively, and can RP-01's published total flow of 64 sccm be decomposed into individual CH4 and H2 MFC flows without guessing?

## Direct primary RP-01 evidence

Smith et al. 2001 directly states:

- Plasma Technology parallel-plate reactor;
- gas notation `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- RF power `50 W`;
- time `60 s`.

The audited primary text does not explicitly state separate CH4 and H2 MFC values.

Therefore the individual flows are **not currently CLOSED-P**.

## Same-UWA primary-lineage evidence

Smith et al. 1999, “Reactive ion etching for mesa structuring in HgCdTe,” J. Vac. Sci. Technol. A 17, 2503–2509, DOI `10.1116/1.581988`, uses the same printed `CH4/5H2` notation in the UWA HgCdTe RIE lineage and reports an approximately 400-mTorr, ~0.4-W/cm² branch for x≈0.31 material.

This confirms notation continuity but, in currently accessible primary metadata/text, still does not explicitly decode individual MFC flows.

## Secondary review evidence — important provisional closure

V. Srivastav, R. Pal and H. P. Vyas, “Overview of etching technologies used for HgCdTe,” *Opto-Electronics Review* 13(3), 197–211 (2005), contains Table 2, “Process details for RIE of HgCdTe in RF parallel plate reactor.”

The table includes the x≈0.31 LPE p-/n-HgCdTe mesa-isolation/type-conversion branch and explicitly prints:

`CH4:H2 = 1:5`.

The surrounding review discussion cites the Smith/Musca/Redfern/Dell/Faraone 1999 UWA mesa-RIE work as the relevant HgCdTe mesa-isolation/type-conversion source.

### Important table/OCR caution

The accessible table text has degraded column alignment. Some adjacent pressure/flow entries are not sufficiently reliable to promote all table numbers independently. The **explicit ratio text `CH4:H2 = 1:5` is clear**, but the exact association of every OCR'd neighboring number with a reference column should be verified from a clean table image/full primary paper before use.

Therefore project status becomes:

- gas ratio `CH4:H2 = 1:5` → **CANDIDATE-SECONDARY / strong same-lineage support**;
- individual RP-01 MFC flows → **CLOSED-D only conditionally on the 1:5 interpretation**, not CLOSED-P.

## Derived RP-01 flow split if ratio = 1:5

Given RP-01 total flow

`Q_total = 64 sccm`

and candidate ratio

`Q_CH4 : Q_H2 = 1 : 5`,

then

`Q_CH4 = 64/(1+5) = 10.6667 sccm`

and

`Q_H2 = 5×64/(1+5) = 53.3333 sccm`.

These values are tagged:

`[D from RP-01 total flow + secondary-source-supported ratio]`.

They are **not to be described as directly published RP-01 MFC settings** until a primary UWA source explicitly decodes the notation or equivalent archival evidence is recovered.

## Why this matters physically

The 2005 review also emphasizes that methane fraction strongly affects polymer formation/surface behavior in CH4/H2 RIE. Therefore gas ratio is not a cosmetic bookkeeping variable; it is a reactor-transfer variable that can alter oxide clearing, etch behavior, surface chemistry, electrical conversion and eventual contact resistance.

## Searches that did NOT resolve primary MFC values

Targeted searches were performed for:

- exact Musca/Smith paper title + individual sccm values;
- `CH4/5H2` + 64 sccm;
- `CH4:H2 1:5` + Smith/Musca;
- possible alternative interpretations such as “5% H2.”

No primary UWA text recovered so far explicitly states `10.67 sccm CH4 + 53.33 sccm H2`, and no evidence was found supporting a “5% H2” interpretation.

## Current controlled recommendation

P08 should be revised to state:

1. direct historical condition remains `64 sccm total, CH4/5H2, 100 mTorr, 50 W, 60 s`;
2. strongest decoded ratio evidence is `CH4:H2=1:5` from a 2005 HgCdTe etch review summarizing the UWA-type RF parallel-plate branch;
3. applying that ratio gives candidate MFC center points `10.667 / 53.333 sccm`;
4. actual released MFC settings require primary-source confirmation **or** local process qualification against electrical conversion + TLM outcomes;
5. record calibrated actual flows independently for every run.

## Conversion-depth question remains separate

This gas-ratio work does not close the ~8-µm n+ conversion-depth provenance.

Relevant primary sources remain:

- Musca et al. 1998, DOI `10.1007/s11664-998-0032-4` — LBIC of RIE-induced n-type doping;
- Musca et al. 1999, “Junction Depth Measurement in HgCdTe Using LBIC,” JEM 28, 603–610.

The UWA repository confirms that the 1998 paper provides information on depth/lateral extent but accessible metadata does not give the exact ~8-µm sample conditions. Continue treating `~8 µm` as `P-OTHER-SOURCE/SIMILAR-CONDITIONS`, not a direct RP-01 measured value.
