# Source-ledger addendum — Round 55 empirical synthesis rules

**Date:** 2026-08-16 America/New_York

## New publication code: `SYN`

Round 55 introduces `SYN` as a publication-layer evidence code for a **specific empirical starting value selected by synthesis** when the exact historical RP-01 value is not published.

`SYN` does not alter the underlying source ledger. It does not promote transfer evidence to direct RP-01 evidence.

A `SYN` value should satisfy all of the following:

1. it is a concrete number or operational choice;
2. at least one compatible primary source, same-lineage source, or explicit physics calculation constrains its scale;
3. the manual states the reasoning or nearest primary anchor;
4. it is presented as a starting implementation, not a historical fact or released production tolerance;
5. it can be falsified/adjusted by experiment without changing the evidence history.

## Existing codes carried into the publication layer

- `RP` — direct RP-01;
- `SL` — same lineage;
- `PT` — primary transfer;
- `DER` — derived;
- `SYN` — synthesized empirical starting implementation.

## Important examples

- `4.8000 g` LPE charge is constrained by a primary modified-horizontal-slider HgCdTe process, while target elemental fractions come from the controlled Honeywell tie-line calculation. The combination is explicitly synthesized.
- `10.6667/53.3333 sccm` individual RIE flows are derived from the 64-sccm total only under the chosen 1:5 interpretation of printed `CH4/5H2`; they are not direct RP-01 MFC values.
- `0.50 nm/s` Au deposition lies inside directly published HgCdTe Au thermal-evaporation rate scales; the exact RP-01 rate remains unrecovered.
- 60° full-cone / 30° half-angle is a derived/synthesized radiometry implementation because it reproduces the reported background-flux scale but is not documentary proof of historical aperture convention.

## Numerical authorities unchanged

The authoritative LPE composition calculation remains `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`:

- Hg 200.59;
- Cd 112.414;
- Te 127.60 g/mol;
- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

Direct RP-01 RIE, Cr/Au, geometry, temperature, field, spectral, noise and D* anchors remain unchanged.
