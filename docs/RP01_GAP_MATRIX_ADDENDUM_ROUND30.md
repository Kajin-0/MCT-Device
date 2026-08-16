# RP-01 gap matrix addendum — Round 30

## Scope

Round 30 audits the detector-bias/load/self-heating chain that bridges P10 to P11/P12.

Result: P10 is already the canonical operator method. P10A now provides historical lineage and detector-terminal transfer qualification. No duplicate P35/P36/P37 top-level procedure was created.

---

## Gap matrix

| Gap | State after Round 30 | Evidence / reason | Required closure |
|---|---|---|---|
| Meaning of RP-01 applied field | **CLOSED-DIRECT** | Smith 2001 identifies applied electric field as voltage bias between contacts | Preserve `E=V_contact/L_active` |
| Figure-3 field range | **SUBSTANTIALLY CLOSED-DIRECT** | Plot spans roughly 0–50 V/cm | Original numerical data desirable, not required for method |
| Figure-5/6/7 canonical field | **CLOSED-DIRECT** | 10 V/cm, 80 K; Figure 5 and spectral figures tied to same device | Preserve state |
| Same physical detector across Figs 3/5/6/7 | **CLOSED-DIRECT** | Canonical text | Keep same-device lineage |
| Performance contact pair/gap | **OPEN-HISTORICAL** | Nine gaps known, selected pair not identified | Recover lab record/thesis/raw data; never guess |
| Bias-source make/model | **OPEN-HISTORICAL** | Not reported | Recover UWA traveler/notebook/thesis |
| Bias topology | **OPEN-HISTORICAL** | Direct voltage-bias concept known; internal circuit not reported | Recover schematic; local reproduction qualifies terminal state |
| Series/load resistor value | **OPEN-HISTORICAL** | No primary value recovered | Recover source or define/calibrate local network |
| Bias/load resistor temperature | **OPEN-HISTORICAL** | Not reported | Recover or measure locally for noise model |
| Detector terminal voltage sensing | **OPEN-HISTORICAL** | Paper reports contact bias but not sensing method | Recover circuit; local direct/high-Z sensing preferred |
| Detector current at 10 V/cm | **OPEN-HISTORICAL** | P10 `~1.79 mA` is derived screening only | Recover raw data or measure local detector |
| Detector resistance at 10 V/cm | **OPEN-HISTORICAL** | Contact gap/current unresolved | Recover raw data or measure local detector |
| Preamplifier identity | **PARTIAL-LINEAGE** | Later UWA work cites Siliquini 1995 thesis for bias-capable low-noise voltage preamp | Acquire thesis; identity with 2001 still must be proven |
| Preamplifier input impedance | **OPEN-HISTORICAL** | No circuit recovered | Thesis/lab record or local measured `Z_pre(f)` |
| Preamplifier gain/bandwidth | **OPEN-HISTORICAL** | No circuit/settings recovered | Thesis/lab record or P12B local calibration |
| AC coupling / bias tee | **OPEN-HISTORICAL** | Not reported | Recover circuit or locally measure transfer |
| Bias-source noise | **OPEN-HISTORICAL / LOCAL-QUAL** | Not reported | P10A source-on/source-off detector-equivalent tests |
| Signal transfer at 1 kHz | **OPEN-HISTORICAL / LOCAL-QUAL** | Optronics/preamp chain incomplete | Measure `H_sig(1 kHz)` locally |
| Noise transfer detector→preamp | **OPEN-HISTORICAL / LOCAL-QUAL** | P12C/P12B require calibrated loading | Measure `H_noise(f)` / full network transfer |
| Responsivity/noise exact topology identity | **OPEN-HISTORICAL** | Same detector/state known; same circuit not stated | Recover records or prove common local state explicitly |
| Self-heating numerical limit | **OPEN-QUALIFICATION** | No historical ΔT or P limit | Local duty/pulse/DC invariance and P33 thermal kernel |
| Historical use of pulsed bias | **OPEN / DO NOT INFER** | Other UWA photoconductor work uses pulsed bias for power management in different architecture | No RP-01 claim absent direct source |
| Package thermal resistance/time constants | **LOCAL-QUAL / HISTORICAL OPEN** | P33 demonstrates package dependence | Measure local `R_theta` and `H_pkg,thermal` |
| Sweepout versus heating separation | **CONTROLLED-LOCAL-METHOD** | P10/P10A define discriminating tests | Execute on local detector |
| Siliquini 1995 thesis electronics | **IDENTIFIED-NOT-RECOVERED** | Later UWA APL explicitly cites it for the bias-capable preamp | Acquire/scan thesis |

---

# Important state corrections

## 1. Source voltage is not the historical field definition

Do not write

`E = V_source/L`

unless source-to-detector drop has been shown negligible.

Historical RP-01 language points to

`E = V_contact-contact/L_active`.

The local traveler therefore records both `V_source` and `V_contact`.

---

## 2. Same device does not close contact pair

Figures 3, 5, 6 and 7 use the same physical detector, but a nine-contact string offers several possible active gaps.

No contact separation may be chosen by making the published D* algebra come out conveniently.

`contact_pair = OPEN-HISTORICAL`.

---

## 3. Ideal screening current is not historical current

P10 derives approximately `1.79 mA` at 10 V/cm from supplier n/µ, nominal width and thickness under a one-carrier ideal model.

This remains:

`DERIVED-CONSISTENCY`.

It is not evidence for the Figure-5 detector current.

---

## 4. Later UWA voltage-preamp evidence is transfer only

Hatch et al. 2011 directly shows:

`photoconductor -> low-noise voltage preamplifier that permits device bias`,

with stated bias voltage converted to electric field.

That supports the laboratory lineage but does not close the 2001 circuit.

---

## 5. Equal peak field does not imply equal thermal state

Same-UWA vertical-photoconductor work treats power dissipation as a critical device constraint and uses pulsed biasing in a different architecture.

Therefore local P10 transfer records:

`{peak field, current, P_peak, P_avg, duty, pulse width, repetition rate, thermal settling}`.

A pulsed and DC run are not interchangeable simply because `E_peak` is the same.

---

# Highest-value recovery targets after Round 30

1. J. F. Siliquini 1995 UWA PhD thesis full text.
2. Any UWA electronics drawing/traveler for the bias-capable low-noise photoconductor preamplifier.
3. Original Figure-3/5/6/7 device notebook identifying contact pair and current/resistance.
4. Optronics measurement-system wiring or bias interface record.
5. HP35665A acquisition record linked to the same bias network.

---

# Local qualification now available

Even if the historical schematic remains unrecovered, a new laboratory can reproduce the physical measurement more rigorously by closing:

`Y_bias = {contact_pair,L,W,V_source,V_contact,I,E,P_det,R_static,R_diff,H_sig(f),H_noise(f),Z_pre(f),source_noise,T,H_pkg,thermal,duty,polarity,sweepout_metric}`.

The P11/P12 state can then be declared:

- `STATE-ELECTRICALLY-IDENTICAL`,
- `CORRECTED-TO-COMMON-ELECTRICAL-STATE`, or
- `INCOMPATIBLE — DO NOT CALCULATE JOINT D*`.

---

# Round-30 conclusion

The principal bias uncertainty has shifted from **what 10 V/cm means** to **how UWA generated, sensed and read out that detector-terminal state**.

That is a real reduction in the historical gap: field definition is now directly anchored, while circuit implementation remains explicitly open and locally qualifiable.
