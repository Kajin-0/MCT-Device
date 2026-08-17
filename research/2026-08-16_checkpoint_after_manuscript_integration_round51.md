# Research checkpoint — after integrated manuscript Round 51

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. User-facing correction

The user clarified that the desired deliverable is the final HgCdTe fabrication/characterization procedure paper/booklet, not continued repository/security infrastructure work.

Round 51 therefore terminates the infrastructure-first direction and re-centers the project on the integrated technical manual.

## 2. Principal result

Added the first coherent user-facing manuscript:

`manuscript/RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md`

The draft integrates substrate preparation, LPE, Hall/FTIR, Hg anneal, both lithography masks, wet mesa, anodic oxide, RIE, Cr/Au, TLM, electrical bias/self-heating, singulation, package, absolute responsivity, noise/NEP/D*, and temporal/frequency response.

## 3. Critical architecture correction

Prior readiness files correctly state that an unspecified laboratory cannot be `TRACEABLE-FIRST-BUILD-READY` without actual apparatus, materials, calibrations and local branch qualification.

However, that physical truth must not be misused as a document-development rule.

Permanent distinction:

`LOCAL-EXECUTION-INSTANTIATION-REQUIRED != MANUSCRIPT-CONTENT-OPEN`.

A technical manual can and should state:

- the fixed source value;
- the strongest reference qualification center;
- what the executing laboratory must measure locally;
- how that local quantity is accepted/rejected.

It must not invent a universal furnace offset, gas calibration, QCM tooling factor, exposure dose, bondline thickness or view factor.

## 4. New manuscript state

`RP01-INTEGRATED-MANUSCRIPT-DRAFT-READY = YES`.

This is a document state only.

No physical maturity promotion:

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated lab;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

## 5. Integrated reference route frozen for manuscript Draft 0.1

1. insulating CdZnTe, first transfer center Cd0.96Zn0.04Te (111)B;
2. explicit local Br2/methanol final-surface recipe around the strongest Te-rich LPE transfer family;
3. covered Honeywell-derived graphite horizontal-slider LPE;
4. xL=.082, yL=.810, TL=507 °C, xS≈.29;
5. exact authoritative mass fractions Hg=.2497382358, Cd=.01250164993, Te=.7377601143;
6. N2 purge -> H2 growth atmosphere family;
7. first contact screen near 500 °C (~7 K nominal supercooling), with time determined by local thickness/morphology calibration rather than imported historical guess;
8. P05/P06 as-grown map;
9. Hg-rich/isothermal-like anneal first center ~250 °C / 1 h, released by post-anneal P05/P06;
10. thick positive novolak/DNQ Mask-1 family, AZ4620 strongest current product-identified Br2/HBr screening candidate;
11. wet mesa reference center nominal 2% Br2 in 3:1 EG:HBr near 21 °C, but exact local formulation must be mathematically defined and calibrated;
12. anodization reference center 0.1 M KOH in stated 90% EG/10% DI, HgCdTe anode/carbon cathode, J≈0.30 mA/cm², ~15 V, ~2 min, ~80 nm target, with solvent-ratio basis local and endpoint based on V(t)/Q/A/thickness;
13. Mask-2 direct fingerprint 4–5 µm, 80 °C/30 min, chlorobenzene 30 min, then exposure/develop/water rinse; local resist/dose/developer/order/profile qualification;
14. RIE direct controller center 64 sccm total, 100 mTorr, 50 W, 60 s, CH4/5H2; candidate 1:5 split 10.6667/53.3333 sccm must remain explicitly non-direct;
15. RIE equivalence based on t_clear/t_sem, self-bias/ion-energy proxy, sample temperature and electrical conversion, not watts alone;
16. Cr/Au 30/270 nm direct; thermal evaporation first same-UWA transfer method; rates/vacuum/QCM local;
17. TLM reference rho_c~9e-4 ohm cm² at 80 K;
18. P10–P13 same detector/contact pair/gap/T/E/background/package state or explicitly corrected;
19. low-force CdZnTe-compatible wire-saw family as first singulation screen, not historical identity;
20. compliant silicone-family first package attach screen, with package thermal response measured.

## 6. Important manuscript cautions retained

- detector cutoff ~4.4 µm is not Hansen band-gap-equivalent wavelength (~5.09 µm for x=.30 at 80 K);
- 24.5 nV/sqrtHz is high-frequency/g-r noise, not automatically 1-kHz noise;
- 50 W RIE does not establish reactor equivalence;
- physical RIE etch depth != electrical conversion depth;
- rho_c does not prove minority-carrier blocking;
- package thermal poles can masquerade as detector lifetime;
- an unqualified timing calculation for a ~9.5-µm wet etch must not replace local depth/isolation calibration;
- missing historical preparation basis remains missing and must not be guessed.

## 7. Next logical work — Round 52

Perform an adversarial manuscript integration review rather than another infrastructure round.

Priorities:

1. line-by-line contradiction audit between Draft 0.1 and P01–P35;
2. check all numerical values/evidence labels against source ledger/calculations;
3. normalize units, symbols and terminology;
4. identify any procedure step that still leaves an operator with an undocumented irreversible choice;
5. create a consolidated uncertainty/example-calculation appendix;
6. create a complete bibliography from controlled source records;
7. revise to Draft 0.2;
8. only then begin final layout/figures/typesetting.
