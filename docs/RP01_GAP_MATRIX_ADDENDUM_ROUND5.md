# RP-01 gap-matrix addendum — measurement-chain round 5

**Date:** 2026-08-15 America/New_York  
**Precedence:** This addendum supersedes older P10/P12 historical-measurement-chain entries where noted.

## P12 noise/readout chain — updated state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| historical detector condition | CLOSED-P | 80 K, 10 V/cm, same typical device as Figures 3/6/7 |
| historical noise instrument | CLOSED-P | HP35665A after low-noise preamplifier |
| historical plotted quantity | CLOSED-P | averaged noise-voltage spectrum |
| historical preamp identity/circuit | OPEN / ARCHIVAL TARGET | same-UWA later paper identifies custom bias-capable low-noise voltage preamp and cites J. F. Siliquini UWA PhD thesis (1995) |
| Siliquini thesis acquisition route | ACTIONABLE | UWA holds most pre-2017 PhD theses in print/storage; OneSearch/storage/thesis scan request route available |
| historical preamp gain/bandwidth/noise | OPEN | extract from thesis if acquired |
| analyzer class capability | CLOSED-OFFICIAL | official Keysight 35665A supports linear spectrum, PSD, cross-spectrum, frequency response; up to 102.4 kHz single-channel / 51.2 kHz dual-channel, 100–800 lines |
| historical HP35665A span/window/RBW/ENBW/averaging | OPEN | paper does not state; do not reverse engineer without original data/settings |
| local preamp/readout transfer `G(f)` | CONTROLLED-QUAL | P12B inject calibrated source through detector-equivalent impedance and measure magnitude/phase |
| source-impedance-dependent electronics noise | CONTROLLED-QUAL | short + precision resistors bracketing detector resistance; Johnson-noise consistency check |
| local analyzer PSD normalization | CONTROLLED-QUAL | verify with known resistor/white-noise reference using exact analyzer settings |
| electronics floor | CONTROLLED-QUAL | acquire under same gain/impedance/bias/cabling; subtract only at PSD level |
| stationarity / intermittent noise | CONTROLLED-QUAL | retain time records and diagnose bursts/drift/microphonics before averaging |
| two-channel cross-spectrum | OPTIONAL LOCAL ENHANCEMENT | permitted if loading/cross-talk are qualified; not historical claim |
| 1-kHz detector noise for D* | OPEN historically / CLOSED-METHOD locally | measure directly at 1 kHz for new D*; do not assume 24.5-nV/√Hz plateau applies |

Procedures:

- `procedures/P12A_UWA_PREAMPLIFIER_LINEAGE_ADDENDUM.md`
- `procedures/P12B_NOISE_READOUT_ANALYZER_TRANSFER_QUALIFICATION.md`

## P10/P11/P12 active geometry — updated state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| contact string geometry | CLOSED-P | nine contacts, each 300×300 µm, adjacent gaps 50–400 µm in 50-µm increments |
| Figures 3/5/6/7 common device | CLOSED-P | paper explicitly states same device |
| exact selected historical gap/contact pair | **OPEN — inference audit completed** | scalar R/noise/D* data are underdetermined because exact 1-kHz noise convention and device resistance/lifetime are missing |
| candidate rectangular area range | CLOSED-D / CONDITIONAL | if full 300-µm width is active: 0.015–0.120 mm² for 50–400 µm gaps |
| D*-based gap inversion | REJECTED AS NONUNIQUE | 24.5 nV/√Hz is high-frequency g-r plateau, not closed as 1-kHz D* noise; no unique gap can be selected |
| local reproduction geometry | CONTROLLED | directly measure fabricated gap, active width, aperture/illuminated area and use those values in E, responsivity, D* |

Research note:

- `research/2026-08-15_rp01_active_gap_inference_audit.md`

## Round-5 practical conclusion

Historical electronics exactness is blocked primarily by one archival source, the Siliquini 1995 UWA thesis. The physical detector-noise measurement does not need to wait for that acquisition: P12B permits a more traceable local measurement through full transfer/noise/PSD calibration.

The historical active gap also remains legitimately open. Future work should not force a gap from D* unless new raw/figure/layout evidence closes the missing variables.
