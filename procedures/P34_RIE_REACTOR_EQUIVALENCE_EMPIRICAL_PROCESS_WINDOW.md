# P34 — CH4/H2 RIE reactor-equivalence empirical process window

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Turn P08/P08D from a controller-setpoint transfer rule into an empirically measurable reactor-equivalence procedure for the RP-01 CH4/H2 blocking-contact process.

The direct RP-01 center is:

- parallel-plate Plasma Technology reactor;
- printed gas notation `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- forward RF power `50 W`;
- RF-on time `60 s`.

These values do **not** uniquely specify ion energy, ion flux, plasma density, sample temperature, residence time, chamber wall state or physical/electrical modification of HgCdTe.

P34 therefore controls the chain:

`reactor hardware + chamber state + calibrated gas state + RF/sheath state + sample thermal state -> oxide clear -> HgCdTe physical recession -> electrical conversion -> P26/P09 contact outcome -> detector outcome`.

P34 supplements P08D; it does not claim to reconstruct an unpublished Plasma Technology traveler.

---

## 2. Evidence classes

### `DIRECT-RP01`
Smith et al. 2001 blocking-contact process.

### `SAME-UWA-RIE`
UWA HgCdTe RIE papers from the same laboratory lineage, including the 1997–2000 conversion/mesa studies.

### `PRIMARY-HGCDTE-RIE-TRANSFER`
Primary HgCdTe CH4/H2 RIE studies from other groups.

### `PRIMARY-PLASMA-TECH-FAMILY`
Primary publications using a Plasma Technology/Oxford Plasma Technology parallel-plate RIE system of the same broad equipment family. These constrain plausible hardware architecture only; they do not identify the RP-01 model.

### `LOCAL-QUAL`
Measured values on the actual transfer reactor.

No transfer-family hardware value may be relabeled `DIRECT-RP01`.

---

## 3. Direct and same-lineage anchors

### 3.1 RP-01
Directly published:

`64 sccm / 100 mTorr / 50 W / 60 s / CH4/5H2`.

Still open:

- exact reactor model;
- RF frequency;
- powered-electrode diameter/area;
- grounded-area ratio;
- electrode spacing;
- sample position;
- chuck temperature;
- sample thermal coupling;
- DC self-bias;
- base pressure;
- pump/throttle architecture;
- individual historical CH4/H2 MFC settings;
- chamber clean/seasoning state.

### 3.2 Same-UWA mesa/conversion branch
Smith et al. 1999 reports RIE at approximately:

- `400 mTorr`;
- `CH4/5H2`;
- `0.4 W cm^-2`;

with p-to-n conversion in p-type HgCdTe and n+ doping in n-type HgCdTe.

Siliquini et al. 1997 reports for x≈0.31 vacancy-doped p-HgCdTe:

- `410 mTorr`;
- `CH4/H2`;
- `0.4 W cm^-2`;
- physical etch depth ~`0.2 µm`;
- electrical conversion depth ~`1.5 µm`.

Siliquini et al. 1998 reports x≈0.29 arsenic-doped p-HgCdTe conversion at:

- `340 mTorr`;
- `CH4/H2`;
- `0.4 W cm^-2`.

Smith et al. 1998 reports another same-UWA branch at:

- `400 mTorr`;
- `CH4/H2`;
- `90 W`;

followed by Hg anneal recovery.

These branches prove that pressure, power-density/power convention, starting carrier state and anneal history matter. They are not to be averaged into RP-01.

---

## 4. Primary HgCdTe evidence that self-bias is a first-class coordinate

Semu et al., *Applied Physics Letters* 59, 1752–1754 (1991), DOI `10.1063/1.106418`, directly studied CH4/H2 metalorganic RIE of HgCdTe.

A reported parametric condition was:

- total flow `85 sccm`;
- pressure `20 mTorr`;
- substrate/process temperature `35 °C`;
- RF power `150 W`;
- dc bias approximately `-360 to -440 V`.

One explicit example used:

- CH4 `15 sccm`;
- H2 `70 sccm`;
- `20 mTorr`;
- `150 W`;
- dc bias `-390 V`;
- `35 °C`.

The authors directly associated rough sidewalls/etched surfaces with the high RF-power-induced dc bias.

They also showed etch rate dependence on CH4:H2 ratio and used laser interferometry for in-situ etch-rate/endpoint measurement.

### P34 consequence

**Forward RF power is not a portable ion-energy coordinate.**

Every local run must record a measured dc self-bias or another calibrated sheath/ion-energy proxy. If the local reactor cannot measure any meaningful ion-energy proxy, reactor equivalence remains `PARTIAL`.

---

## 5. Chemistry/orientation transfer evidence

Elkind and Orloff, *JVST A* 10, 1106–1112 (1992), DOI `10.1116/1.578210`, found that:

- H2-only RIE produced a Cd-rich residue and rough surface;
- adding methane around the studied ~25% level produced smoother surfaces and deeper vias;
- etch rate and morphology depended strongly on HgCdTe surface orientation;
- for short etches the reported rate ordering was `(111)B > (100) > (111)A`, while `(111)A` produced the smoothest surface among those compared.

### P34 consequence

The incoming crystal face/polarity from P29 is part of the RIE genealogy. A process qualified on one crystallographic face may not be declared equivalent on another without measured confirmation.

---

## 6. Same-equipment-family architecture evidence — not historical proof

A primary 2001 Plasma Technology RIE80 study on GaAs reports:

- Plasma Technology `RIE80`;
- lower electrode RF-driven at `13.56 MHz`;
- base pressure below `0.5 mTorr`;
- controlled platform temperature, with `40 °C` used in that experiment.

This is useful because it demonstrates concrete architecture available in the same manufacturer/equipment family and era.

### Strict restriction

Do **not** assign `RIE80`, `13.56 MHz`, `<0.5 mTorr` base pressure, or `40 °C` to RP-01 unless a direct UWA source is recovered.

Use these only to define which hardware fields must be recorded on a modern transfer reactor.

---

## 7. Reactor hardware register

For every reactor revision record:

### Chamber/electrode
- manufacturer/model/serial;
- chamber material and internal liner state;
- powered electrode identity;
- powered electrode diameter/area;
- grounded surface area where estimable;
- electrode spacing;
- sample radial/azimuthal position;
- sample carrier dimensions/material;
- exposed carrier area;
- total loaded sample area;
- RF frequency;
- matching-network model/revision.

### Vacuum
- pump type/model;
- throttle valve/control mode;
- base pressure immediately before process;
- pressure gauge type/location/range;
- gauge calibration/correction state for H2/CH4 mixture;
- process pressure trace;
- pumpdown time;
- leak/outgassing anomalies.

### Gas
- CH4/H2 supplier, grade and lot;
- MFC model/range;
- calibration date;
- gas-specific correction;
- commanded and measured/verified flow;
- stabilization time before RF;
- total flow and actual ratio.

### RF/plasma
- forward power trace;
- reflected power trace;
- matching settings where available;
- dc self-bias trace;
- plasma ignition transient;
- RF stabilization interval;
- optical-emission or other plasma diagnostic if available.

### Thermal
- electrode/chuck temperature;
- sample carrier/contact method;
- backside gas or thermal interface if used;
- sample starting temperature;
- measured sample temperature or calibrated proxy versus time;
- RF-off cooldown time and vent temperature.

---

## 8. Chamber genealogy / seasoning

CH4/H2 processes can alter chamber-wall/polymer state. Therefore record:

- previous process chemistry;
- elapsed plasma time since chamber clean;
- clean chemistry and duration;
- seasoning recipe and duration;
- dummy-wafer/coupon loading;
- visible wall/coating state where inspection is possible;
- run order within one chamber state.

A chamber clean creates a new genealogy branch until equivalence is demonstrated.

Do not pool pre-clean and post-clean runs as iid replicates.

---

## 9. Oxide-clear calibration

RP-01 uses the same RIE step to remove the ~80-nm anodic oxide in the contact opening and then expose HgCdTe to the conversion-producing plasma.

Define:

- `t_clear` — experimentally measured time to clear the actual P25/P02 oxide under the local reactor condition;
- `t_sem = t_RF - t_clear` — semiconductor-exposure time after oxide clear.

Because oxide thickness/interface state can vary, `t_sem` is more physically meaningful than treating all 60 s as HgCdTe exposure.

Required short-time calibration:

1. matched anodized witness coupons;
2. multiple RF times spanning incomplete clear to slight semiconductor exposure;
3. oxide-removal metrology;
4. onset of HgCdTe physical recession;
5. repeat across at least two independently established chamber states before release.

Do not assume `t_clear=0`.

---

## 10. Physical etch and electrical conversion are independent outputs

Always distinguish:

- `d_etch` — physical HgCdTe recession;
- `d_conv` — vertical electrical conversion depth;
- `L_conv` — lateral electrical conversion distance.

The 1997 UWA result (`d_etch≈0.2 µm`, `d_conv≈1.5 µm`) proves directly that these are not equivalent.

For the RP-01 n-type blocking-contact branch, the previously cited ~8-µm converted depth remains a separate same-lineage result whose exact reactor condition has not been fully recovered.

No volumetric converted density may be calculated from sheet transport unless `d_conv` is independently justified.

---

## 11. Initial local equivalence experiment

### Stage A — reactor metrology
Establish all hardware/gas/RF/thermal records before HgCdTe.

### Stage B — chamber-state reproducibility
Run a defined clean/season sequence and demonstrate repeatable pressure, reflected power, self-bias and temperature on inert/dummy loads.

### Stage C — oxide-clear map
Determine `t_clear` using matched P25 oxide coupons.

### Stage D — direct-controller center
Where safe and within tool limits, execute:

`64 sccm total / 100 mTorr / 50 W / 60 s`

with the adopted CH4:H2 split stated explicitly by evidence class.

Record the actual:

- self-bias;
- reflected power;
- pressure trace;
- sample temperature;
- `t_clear` and `t_sem`.

### Stage E — semiconductor outcomes
Measure:

- `d_etch`;
- roughness/morphology;
- sheet resistance/conductance;
- Hall/multicarrier state;
- `d_conv` and `L_conv` via LBIC or validated equivalent;
- P26/P09 TLM contact response;
- P08F minority-carrier blocking functional response;
- P10/P12 detector changes on matched devices.

---

## 12. Bounded equivalence coordinates

If the direct-controller center misses the desired output vector, vary measured physical coordinates rather than blindly varying watts.

Priority coordinates:

1. dc self-bias / ion-energy proxy;
2. semiconductor-exposure time `t_sem`;
3. process pressure;
4. sample temperature;
5. CH4:H2 ratio;
6. chamber state/seasoning;
7. total flow / residence-time proxy;
8. loading/exposed area.

Forward power may be changed as an actuator, but the fitted response should be referenced to the measured plasma/thermal coordinates whenever possible.

---

## 13. Reactor-equivalence output vector

Define:

`Y_RIE = {t_clear, self_bias(t), T_sample(t), d_etch, roughness, sheet_state, d_conv, L_conv, rho_c, blocking_response, detector_noise_delta}`.

A reactor/process revision may be labeled `RP01-RIE-TRANSFER-QUALIFIED` only after repeated independent chamber-state preparations give a stable `Y_RIE` and downstream blocking/contact performance.

No acceptance criterion based only on `50 W`, power density, or nominal controller matching is permitted.

---

## 14. Critical rejected inferences

1. `50 W / 0.4 W cm^-2 = 125 cm^2` does not prove the historical powered-electrode area.
2. A same-era RIE80 architecture does not prove RP-01 used RIE80.
3. `13.56 MHz` is plausible equipment-family evidence, not RP-01 historical fact.
4. `CH4/5H2` does not by itself prove the exact MFC convention or individual historical flows.
5. Physical etch depth does not imply electrical conversion depth.
6. Same self-bias does not prove same ion flux/plasma chemistry if pressure, gas ratio, loading or chamber state differ.
7. Same forward power does not prove same ion energy.

---

## 15. Remaining historical gaps

- exact Plasma Technology model;
- RF frequency;
- powered/grounded electrode areas;
- electrode spacing;
- sample holder/loading;
- base pressure;
- pumping/throttle configuration;
- chamber clean/seasoning state;
- self-bias;
- sample temperature;
- exact CH4/H2 individual MFC values;
- oxide-clear time in RP-01;
- exact condition tied to the ~8-µm n-type conversion result.

These remain `OPEN-HISTORICAL`, not absent.

---

## 16. Primary sources

- E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
- E. P. G. Smith et al., *Journal of Vacuum Science & Technology A* 17, 2503–2509 (1999), DOI `10.1116/1.581988`.
- J. F. Siliquini et al., *Applied Physics Letters* 70, 3443–3445 (1997), DOI `10.1063/1.119159`.
- J. F. Siliquini et al., *Applied Physics Letters* 72 (1998), DOI `10.1063/1.120642`.
- E. P. G. Smith et al., *Journal of Applied Physics* 83, 5555–5557 (1998), DOI `10.1063/1.367389`.
- A. Semu et al., *Applied Physics Letters* 59, 1752–1754 (1991), DOI `10.1063/1.106418`.
- J. L. Elkind and G. J. Orloff, *Journal of Vacuum Science & Technology A* 10, 1106–1112 (1992), DOI `10.1116/1.578210`.
- Same-era Plasma Technology RIE80 hardware transfer evidence: primary 2001 Microelectronic Engineering RIE80 study; use only as manufacturer/equipment-family architecture evidence, never RP-01 identification.
