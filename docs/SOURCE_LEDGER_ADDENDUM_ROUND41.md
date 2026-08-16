# Source ledger addendum — Round 41 minimum laboratory capability specification

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Scope

Round 41 does not add a new literature branch and does not reopen documentary searches. It converts the already controlled evidence base into a **physics-based minimum laboratory capability envelope** for future implementation.

New controlled artifacts:

- `docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`
- `travelers/P16C_MINIMUM_LAB_CAPABILITY_IMPLEMENTATION_REGISTER.md`

The source class for this round is primarily `CONTROLLED-INTERNAL-INTEGRATION`: every numerical capability is inherited from a controlled Pxx source/equation or is explicitly labeled as an engineering envelope/design check.

---

## S41-01 — P16A/P16B integration basis

Controlled sources:

- `procedures/P16A_FIRST_BUILD_RELEASE_READINESS_AUDIT.md`
- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`

Use:

- preserve P16A as authoritative readiness state;
- use P16B as the selected candidate process architecture;
- map irreducible local identity/calibration groups into concrete laboratory functions.

Permanent result:

`candidate branch -> capability requirement -> local implementation`, not `candidate branch -> assumed tool`.

---

## S41-02 — LPE capability basis

Controlled sources:

- P03/P03B/P03C/P03D/P03E;
- P30/P30A;
- Round-35/40 source ledgers.

Inherited anchors:

- `xL=.082`, `yL=.810`, `TL=507 °C`, historical `xS≈.29`;
- above-liquidus equilibration followed by below-liquidus growth;
- ~2–10 °C supercooling as a represented transfer neighborhood, not one frozen recipe;
- N2 purge followed by H2 process atmosphere;
- actual well volume/charge/thermal field remain local.

Round-41 engineering envelope:

- thermal commissioning around approximately `495–520 °C` to span the direct liquidus neighborhood, selected supercooling region and above-liquidus operation.

Classification:

`FIRST-BUILD-ENGINEERING-ENVELOPE`, not RP-01 historical setpoint.

---

## S41-03 — charge-composition numerical convention

Authoritative controlled calculation:

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`.

Frozen atomic weights:

- Hg `200.59 g/mol`;
- Cd `112.414 g/mol`;
- Te `127.60 g/mol`.

Therefore canonical mass fractions are:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

Round-41 audit found later P30A/P16B/Round-40 integration text using approximately `0.249740 / 0.012502 / 0.737758`, corresponding to a slightly different Hg atomic-weight convention.

Disposition:

- frozen calculation convention remains authoritative;
- future calculations use the canonical values above unless a deliberate versioned constant update is approved;
- difference is only ~2 ppm in dominant mass fractions and does not alter scientific conclusions.

---

## S41-04 — Hg anneal capability basis

Controlled sources:

- P04/P04A/P04B/P23/P31.

Inherited first-screen center:

- approximately `250 °C / 1 h / Hg-saturated-isothermal-like`.

Near-composition transfer region:

- approximately `250–300 °C` useful low-temperature mapping region.

Round-41 capability consequence:

- sample and Hg-source/reservoir temperatures must be separately measurable/logged even for an initial isothermal branch;
- full cooldown trace is mandatory;
- exact Hg inventory and geometry remain local.

---

## S41-05 — FTIR capability basis

Controlled source:

- P06/P06A and traveler.

Inherited current P06 engineering method:

- approximately `500–5000 cm^-1` (`20–2 µm`) coverage;
- `<=4 cm^-1` resolution for qualification unless sensitivity work validates coarser settings;
- minimum 9-point map;
- preferred 5x5 or denser map where geometry permits;
- independent physical thickness reference over the expected ~5–15-µm range.

Round-41 use:

These become minimum **instrument capability** requirements, not historical RP-01 FTIR settings.

---

## S41-06 — Hall/VdP capability basis

Controlled source:

- P05 and P16B.

Inherited P05 initial grid:

`B=0, +/-0.01, +/-0.025, +/-0.05, +/-0.10, +/-0.20, +/-0.50 T`.

Same-UWA converted-layer context retained in P16B includes fields up to approximately `2 T`.

Round-41 result:

- `>= +/-0.50 T` is the current HARD-MINIMUM required to execute the P05 initial grid;
- approximately `+/-2 T` is preferred extended capability for multicarrier/lineage work, not a first-build hard minimum;
- ~80 K and 300 K measurement states remain required.

---

## S41-07 — lithography / wet chemistry / anodization basis

Controlled sources:

- P14/P14A/P27/P32;
- P28/P28A;
- P25/P25A.

Direct Mask-2 anchors:

- `4–5 µm` resist;
- `80 °C / 30 min` prebake;
- chlorobenzene `30 min`;
- RIE survival and lift-off of ~300-nm Cr/Au.

Wet-mesa candidate center:

- `2% Br2 / 3:1 EG:HBr / ~21 °C`, with concentration/ratio bases still local/open.

Anodization transfer center:

- ~`0.3 mA/cm²`;
- formation-voltage neighborhood near `15 V`;
- ~2-min first screen;
- ~80-nm oxide.

Round-41 capability rule:

anodization source sizing is area-dependent through `I=J A_exposed`; no fixed current is inserted before cell area is measured.

---

## S41-08 — RIE capability basis

Controlled sources:

- P08/P08A/P08D/P24/P34.

Direct RP-01 controller center:

- total `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`;
- printed `CH4/5H2`.

Same-lineage selected candidate:

- `CH4:H2=1:5`;
- derived nominal `10.6667 sccm CH4 / 53.3333 sccm H2`.

Round-41 capability consequence:

- tool must cover those controller coordinates;
- individual MFC ranges must place nominal flows in calibrated useful range;
- self-bias/sheath proxy, reflected power, sample thermal state, chamber genealogy and oxide-clear time are mandatory observables;
- no numerical base-pressure requirement is invented.

---

## S41-09 — Cr/Au deposition capability basis

Controlled sources:

- P09/P09A/P26/P26A.

Direct layer targets:

- Cr `30 nm`;
- Au `270 nm`.

Round-41 capability consequence:

- QCM/witness calibration is separate for Cr and Au unless equivalence is demonstrated;
- pressure is measured but no conventional base-pressure value is assigned;
- RIE-to-Cr exposure and sample thermal load are mandatory states.

Design relationship retained:

for fractional thickness allocation `b_t`, `u_t <= t*b_t`.

The example 5% budget -> 1.5-nm Cr / 13.5-nm Au is an engineering example, not a released tolerance.

---

## S41-10 — integrated detector-station basis

Controlled sources:

- P10/P10A;
- P11/P11A;
- P12/P12A/P12B/P12C;
- P13/P13A;
- P33 thermal/package coupling.

Inherited direct/reference conditions:

- ~80 K;
- `10 V/cm` canonical P10–P12 field;
- responsivity/noise comparison at `1 kHz` where applicable;
- ~`4 µm` D* point;
- ~`4.4 µm` response edge;
- ~3-kHz 1/f knee;
- high-frequency g-r reference ~`24.5 nV/sqrtHz`.

Round-41 engineering envelopes:

- radiometry first-build coverage approximately `2–6 µm` to span the MWIR response and beyond-edge region;
- noise chain must at least cover the historical `10^2–10^4 Hz` band and should extend below 100 Hz / above 10 kHz where practical;
- temporal qualification includes 1 kHz, 10 kHz, 100 kHz and 1 MHz and extends to >=5–10x observed `f3dB` when the external chain permits.

Design checks:

- if electronics PSD budget is fraction `beta` of detector plateau PSD, `e_elec <= 24.5*sqrt(beta) nV/sqrtHz`;
- if deliberately resolving a 25-ns pulse with first-order rise-time logic, `BW~0.35/tr≈14 MHz` is an instrument-sizing check only.

---

## S41-11 — singulation/package basis

Controlled sources:

- P35;
- P33/P15.

Round-41 use:

- low-force wire-saw remains first singulation screen;
- compliant silicone-family remains first die-attach screen;
- actual tool/material/settings remain local;
- package/Dewar infrastructure must permit 77–80 K operation, measured vacuum/optics/thermal state and repeated warm-cold cycling.

No new singulation or adhesive product is selected.

---

## S41-12 — no new external literature claim

Round 41 is intentionally an integration/requirements round. No new publication is promoted to the source ledger. All technical anchors remain traceable through the pre-existing controlled Pxx modules and their primary citations.
