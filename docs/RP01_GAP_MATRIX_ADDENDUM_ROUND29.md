# RP-01 gap matrix addendum — Round 29 noise-chain / analyzer-state closure

**Date:** 2026-08-16

This addendum supersedes earlier uncertainty where the canonical article itself now closes a state variable. It does not convert unresolved electronics or geometry into guessed historical values.

| Item | Round-29 state | Evidence / consequence | Required closure route |
|---|---|---|---|
| Figure-5 detector temperature | **CLOSED-DIRECT: 80 K** | RP-01 Figure-5 state | preserve in historical comparison |
| Figure-5 applied field | **CLOSED-DIRECT: 10 V/cm** | RP-01 Figure-5 state | use measured active-region field locally |
| Figure-5 FOV | **CLOSED-DIRECT: stated 60°** | Figure-5 caption explicitly includes 60° FOV | preserve label; P11A still needed to translate to physical aperture/view factor |
| Figure-5 exact background radiance/source temperature | **OPEN-HISTORICAL** | 60° does not define radiance | recover optical traveler/source or characterize local background explicitly |
| Figures 3/5/6/7 physical device identity | **CLOSED-DIRECT: same device** | canonical performance discussion links them | preserve same-device coupling in reconstruction |
| Figure 3/5/6/7 exact contact pair | **OPEN-HISTORICAL** | nine-contact structure known, used pair not recovered | paper/thesis/lab traveler/figure-layout recovery |
| Figure 3/5/6/7 active gap `L` | **OPEN-HISTORICAL** | cannot infer from 50–400-µm TLM spacing list | direct source or digitized/device-layout evidence with explicit provenance |
| Active width / `D*` area convention | **PARTIAL** | contact width and `A=lw` equation known; exact performance-device `l,w` still incomplete | recover contact pair/mesa geometry; otherwise use measured local geometry |
| Figure-5 preamplifier identity | **OPEN-HISTORICAL** | only “low-noise pre-amplifier” direct | acquire Siliquini 1995 thesis / UWA archival traveler |
| UWA preamp functional architecture | **PARTIAL-SAME-LINEAGE** | later UWA source explicitly describes bias-capable low-noise voltage preamp and cites Siliquini thesis | do not claim exact circuit identity until archival recovery |
| Bias/load/coupling network | **OPEN-HISTORICAL** | determines loading and detector-terminal transfer | archival circuit; locally measure transfer under P12B |
| Analyzer model | **CLOSED-DIRECT: HP35665A** | canonical Figure-5 chain | official Keysight manuals define instrument behavior |
| HP35665A operator manual | **CLOSED-OFFICIAL** | 35665-90026, Sep. 1991 | retain as instrument reference |
| HP35665A concepts manual | **CLOSED-OFFICIAL** | 35665-90028, Sep. 1991 | retain as PSD/window/analysis reference |
| Historical analyzer span | **OPEN-HISTORICAL** | figure visual range does not prove front-panel span | archival instrument state/data file/notes |
| Historical line count / record length | **OPEN-HISTORICAL** | 35665A supports multiple line counts | do not choose one from capability list |
| Historical window / ENBW | **OPEN-HISTORICAL** | critical to RMS/PSD conversion | archival state or raw data; local Johnson-noise validation |
| Historical averaging type/count | **OPEN-HISTORICAL** | paper says averaged spectrum only | archival setting/data file |
| Historical analyzer display/scaling | **OPEN-HISTORICAL** | analyzer can display spectrum and PSD | archival state; local chain calibrates terminal-referred ASD independently |
| Historical knee definition | **CLOSED-DIRECT/PARTIAL-NUMERIC** | intersection of low-frequency 1/f trend with high-frequency g-r level; ~3 kHz | preserve this comparison metric separately from modern fits |
| High-frequency g-r level | **CLOSED-DIRECT: ~24.5 nV/sqrtHz** | reported RP-01 benchmark | treat as plateau diagnostic, not automatically 1-kHz noise |
| Noise at 1-kHz signal frequency | **OPEN-HISTORICAL** | 1 kHz lies below ~3-kHz knee | recover reduction convention/raw data; new work directly measures `e_det(1kHz)` |
| Noise quantity used for Figure-7 `D*` | **OPEN-HISTORICAL** | paper equation does not identify whether plateau or total 1-kHz value was inserted | archival calculation/raw data/figure reconstruction |
| P11/P12 physical-state identity | **IMPROVED** | same device now direct; T/E/FOV align at canonical conditions | still require contact pair, area, loading and frequency convention |
| Background-fluctuation noise | **CLOSED-AS-REAL-MECHANISM / SAME-UWA** | Jozwikowski 2003 includes background-illumination fluctuations in measured/modelled MWIR HgCdTe PC noise | monitor/control background stability in P12 transfer |
| Exact historical BLIP proof | **PARTIAL** | reported BLIP and background flux; exact frequency/noise reduction remains open | local background-scaling experiment + archival reduction if historical exactness sought |

---

## Highest-value unresolved items after Round 29

### Historical exactness

1. Siliquini 1995 UWA thesis and custom preamplifier schematic.
2. Exact Figure-5 HP35665A settings/state file or laboratory notes.
3. Exact contact pair/gap used by the same Figure-3/5/6/7 detector.
4. Exact noise value/frequency convention used to calculate Figure-7 `D*`.
5. Exact Figure-5 background source/radiance behind the stated 60° FOV.

### Local traceable transfer

1. Bias/load-network transfer function.
2. Preamplifier complex gain and source-impedance-dependent noise.
3. Analyzer PSD normalization and window/ENBW verification using Johnson references.
4. Direct total detector ASD at 1 kHz under matched P11 state.
5. Background-stability monitor and background-flux sweep for BLIP verification.
6. Same physical device/contact pair for responsivity and noise whenever possible.

---

## Round-29 release statement

The project can now reconstruct the **physical state identity** of the published noise/responsivity/detectivity sequence more tightly than before, but it still cannot reconstruct the historical electrical acquisition controller-for-controller.

The correct status is:

`DIRECT SAME-DEVICE / T-E-FOV STATE CLOSURE + TRACEABLE LOCAL ANALYZER TRANSFER; HISTORICAL PREAMP/FFT/CONTACT-PAIR/D* REDUCTION OPEN`.
