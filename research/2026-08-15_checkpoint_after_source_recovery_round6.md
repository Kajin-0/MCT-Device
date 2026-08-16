# Recovery checkpoint — source-recovery round 6

**Date:** 2026-08-15 America/New_York

**Purpose:** Fast handoff after the RIE/LBIC/reactor-equivalence research round. Read after `AGENTS.md` and round-5 checkpoint.

## 1. What changed in round 6

The RIE branch has moved from a nominal-controller recipe to a physically controlled transfer framework.

New files:

- `procedures/P08C_UWA_LBIC_CONVERSION_METHOD_LINEAGE.md`
- `procedures/P08D_RIE_REACTOR_EQUIVALENCE_DEPTH_QUALIFICATION.md`
- `procedures/P08E_RIE_MULTICARRIER_TRANSPORT_QUALIFICATION.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND6.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND6.md`

## 2. Direct RP-01 RIE anchors remain unchanged

- Plasma Technology parallel-plate reactor;
- printed gas notation `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- RF power `50 W`;
- process duration `60 s`;
- converted density reported `~2.0×10^15 cm^-3` averaged over converted thickness;
- mobility reported `~3.3×10^4 cm²/Vs`;
- previous same-lab n-type work cited as showing approximately `8 µm` conversion under similar conditions.

Exact individual MFC values, reactor model, RF frequency, electrode geometry, self-bias and sample temperature remain unrecovered.

## 3. Important source separation — p-type versus n-type RIE

### Siliquini 1997 vacancy-doped p-type branch

Direct UWA-lineage primary result:

- Hg0.69Cd0.31Te, vacancy-doped p-type;
- `410 mTorr`;
- CH4/H2;
- `0.4 W/cm²`;
- physical etch ~`0.2 µm`;
- electrical n-type conversion ~`1.5 µm`.

Use as direct proof that physical etch depth and electrical conversion depth are different.

Do not transfer the 1.5-µm depth to RP-01.

### Siliquini 1998 arsenic-doped branch

UWA institutional record gives:

- Hg0.71Cd0.29Te, arsenic-doped p-type;
- prior Hg anneal eliminating Hg vacancies;
- `340 mTorr`;
- CH4/H2;
- `0.4 W/cm²`;
- LBIC 80–300 K;
- SEMICAD DEVICE donor-density fitting.

Secondary/reposted sources sometimes give `390 mTorr`. Controlled project value is 340 mTorr pending publisher-full-text audit; 390 mTorr is logged as a source discrepancy.

### RP-01 n-type branch

Distinct process:

- starting n-type x≈0.30;
- `100 mTorr / 64 sccm total / 50 W / 60 s`;
- ~8-µm conversion is a prior same-lab n-type result under similar conditions, not yet a directly process-matched release value.

## 4. LBIC depth model is not geometry-independent

Musca et al., JEM 28, 603–610 (1999), DOI `10.1007/s11664-999-0042-x`, is now a formal method source.

It establishes that LBIC junction-depth extraction depends on:

- junction doping density;
- excitation wavelength;
- front/back illumination;
- test-structure geometry.

P08 therefore requires raw maps, acquisition conditions and model version/inputs whenever a depth is reported.

## 5. Reactor-area inference explicitly rejected

Same-UWA 1999 mesa paper reports:

- CH4/5H2;
- 400 mTorr;
- 0.4 W/cm².

RP-01 reports:

- CH4/5H2;
- 100 mTorr;
- 50 W.

Pure algebra would give `A=50/0.4=125 cm²`, equivalent circular diameter ~12.6 cm, if both power statements referred to the identical powered electrode and definition.

**This inference is rejected/unreleased.** The project has not established identical reactor geometry or power-density definition.

Do not use 125 cm² as historical electrode area.

## 6. P08D reactor-equivalence rule

A local reactor is not equivalent merely because controller settings match `64 sccm / 100 mTorr / 50 W / 60 s`.

It must close or measure:

- exact gas split;
- RF frequency;
- powered/ground electrode geometry;
- electrode spacing;
- sample placement/loading;
- forward/reflected power;
- DC self-bias or other ion-energy proxy;
- sample temperature;
- chamber history;
- oxide-clear time;
- physical recession;
- electrical conversion depth/lateral spread;
- transport state;
- final TLM/contact outcome.

Local equivalence output vector:

`Y_RIE = {t_clear, d_etch, R_sheet/Ns, transport decomposition, d_conv, L_conv, rho_c, detector-noise delta}`.

## 7. Multicarrier transport is now mandatory to test

Nguyen et al. 2002, DOI `10.1007/s11664-002-0214-4`, directly shows same-UWA RIE-converted HgCdTe can contain:

- damaged moderate-mobility surface electrons;
- deeper high-mobility converted electrons;
- residual holes if conversion is incomplete.

Differential Hall/QMSA indicates a diffusion-like dopant profile and distinct temperature behavior for surface and deeper channels.

Composition-matched companion Antoszewski et al. 2000, DOI `10.1007/s11664-000-0234-x`, reports at 77 K in a different p-type branch:

- surface electron sheet `Ns≈9×10^12–1×10^13 cm^-2`;
- deeper converted electrons around `1.5–3×10^15 cm^-3`;
- deeper mobility `~4–6×10^4 cm²/Vs`;
- surface mobility much lower, roughly `1.5×10^3–1.5×10^4 cm²/Vs`.

These are not RP-01 targets. They prove that one uniform Hall layer is not a safe default.

## 8. P08B density/depth coupling remains important

RP-01's `2.0×10^15 cm^-3` is averaged over converted thickness.

Conditional sheet scale:

- over 8 µm: `Ns≈1.6×10^12 cm^-2`;
- over 9.5 µm: `Ns≈1.9×10^12 cm^-2`.

Report sheet/multicarrier quantities first; only convert to volumetric density with independently supported `d_conv`.

## 9. In-situ processing archival bridge

Smith et al. 2000, “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors,” SIMC-XI, pp. 318–321, is confirmed as the closest same-team archival bridge for reactor-to-metal transfer.

Public UWA record remains metadata only. No reactor model/electrode area/RF frequency/base pressure/deposition sequence recovered.

Do not continue repetitive title-only web searches unless a new archive/provider becomes available.

## 10. Highest-value next work after round 6

1. acquire full Musca et al. 1998 JEM n-type LBIC paper and exact condition tied to ~8 µm;
2. acquire full Smith et al. 1999 JVST-A and Smith et al. 2000 SIMC-XI experimental text;
3. recover Plasma Technology reactor model/RF frequency/electrode geometry if an archival equipment record becomes accessible;
4. otherwise execute/retain P08D local reactor equivalence methodology;
5. continue non-RIE blockers rather than endlessly re-querying metadata-only records.

## 11. Recovery order

1. `AGENTS.md`
2. this checkpoint after prior checkpoints
3. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND6.md`
4. `docs/SOURCE_LEDGER_ADDENDUM_ROUND6.md`
5. P08 through P08E
6. corresponding prior RIE research notes

The RIE branch is now controlled enough that future work should not regress to “match 50 W and 100 mTorr.”