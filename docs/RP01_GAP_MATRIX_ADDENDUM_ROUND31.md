# RP-01 gap matrix addendum — Round 31

## Scope

Round 31 audits temporal/frequency-response/lifetime provenance and apparatus, with emphasis on separating intrinsic HgCdTe carrier dynamics from optical-source, bias/readout and package thermal response.

Result: P13 is already the canonical temporal-response method and has been corrected/expanded. P13A now contains a substantially closed same-UWA apparatus lineage. No duplicate top-level temporal module was created.

---

## Gap matrix

| Gap | State after Round 31 | Evidence / reason | Required closure |
|---|---|---|---|
| RP-01 detector lifetime `tau` | **OPEN-HISTORICAL** | Smith 2001 audited text publishes no lifetime | Measure reconstructed device or recover undiscovered primary data |
| RP-01 detector `f_3dB` | **OPEN-HISTORICAL** | No RP-01 frequency-response curve recovered | Measure locally / recover source |
| RP-01 1-kHz dynamic attenuation | **OPEN-HISTORICAL / LOCAL-QUAL** | 1 kHz is measurement frequency, not proof of flat response | P13 de-embedded `H_det(1kHz)` |
| RP-01 transient apparatus | **NOT REPORTED / OPEN** | No direct transient method in canonical paper | Recover lab records or qualify local method |
| Same-UWA x≈0.30 TPCD method | **SUBSTANTIALLY CLOSED-PRIMARY-THESIS** | Rajaduray 1998 | Preserve as lineage, not RP-01 recipe |
| UWA TPCD wavelength | **CLOSED for 1998 branch** | `1.047 µm` direct thesis | Do not transfer automatically to RP-01 |
| UWA pulse repetition | **CLOSED for 1998 branch** | `1 kHz` direct thesis | Same restriction |
| UWA pulse duration | **CLOSED for 1998 branch** | `25 ns` direct thesis | Same restriction |
| UWA optical pulse energy/fluence | **OPEN-HISTORICAL** | Not recovered quantitatively | Recover thesis apparatus record / calibrate local source |
| UWA optical pulse rise/fall/jitter | **OPEN-HISTORICAL** | Not recovered | Measure local source / recover original record |
| UWA spot size/profile for analyzed transient | **PARTIAL/OPEN** | scanning-laser context known; exact transient excitation profile incomplete | Recover original setup/data |
| 1.047-µm absorption-depth weighting | **PARTIAL-DIRECT-MODEL** | thesis estimates ~90% absorption within ~2.7 µm | Treat as thesis-specific model; do not equate to 4-µm response |
| UWA detector temperature/environment | **CLOSED for 1998 branch** | ~77 K, vacuum, LN2 cryogenic operation | Same-lineage only |
| UWA bias source type | **PARTIAL-CLOSED** | Keithley variable-current source | Exact model/current still open |
| UWA exact bias | **CLOSED for one analyzed state** | `-1.05 V` thesis value | Sample-specific; do not convert to RP-01 field |
| Low-field sweepout control rationale | **CLOSED-DIRECT SAME-UWA** | thesis explicitly keeps bias small to avoid carrier sweepout to contacts | Mandatory P13 low-field branch |
| UWA AC coupling | **CLOSED-FUNCTIONAL** | AC-coupled amplifier directly stated | Circuit/pole/gain still open |
| UWA AC amplifier model/circuit | **OPEN-HISTORICAL** | Not recovered | Recover source or locally calibrate transfer |
| UWA transient digitizer | **CLOSED for 1998 branch** | HP54522A | Exact settings partly open |
| Stored sample count/time spacing | **CLOSED for 1998 branch** | 500 points, 20 ns spacing | Historical method anchor |
| Typical waveform averages | **CLOSED for 1998 branch** | 128 | Historical method anchor |
| HP54522A input range/coupling/trigger/termination | **OPEN-HISTORICAL** | Not in recovered thesis details | Recover notebook/software or calibrate local scope |
| Matlab transient analysis | **CLOSED-FUNCTIONAL** | direct thesis | Exact code/version not recovered |
| Single-exponential adequacy | **REJECTED AS DEFAULT** | thesis non-exponential diffusion/recombination model fit better in analyzed data | Local model comparison + residual test |
| Injection state of historical 1998 pulse branch | **POTENTIALLY HIGH-INJECTION** | thesis estimates local initial excess carrier density can approach majority density | Do not call low-injection lifetime without fluence series |
| “Low optical power” as low-injection proof | **REJECTED** | same thesis analysis | Use excitation-series/`Delta n/n0` gate |
| Interface-trap delayed transients | **PRIMARY-TRANSFER CLOSED** | Pal 2001 / Gopal 2004 | Treat as non-UWA transfer mechanism |
| 2004 trap paper UWA attribution | **CORRECTED — FALSE ATTRIBUTION REMOVED** | actual authors Gopal/Devi/Pal/Kumar | Preserve non-UWA classification |
| Package thermal several-ms pole | **CLOSED PRIMARY TRANSFER** | Bartoli 1975 HgCdTe PC | P33/P13 thermal discrimination |
| Package thermal hundreds-ms pole | **CLOSED PRIMARY TRANSFER** | Bartoli 1975 | Same |
| P13 package term in transfer equation | **CLOSED-METHOD** | P13 updated Round31 | Execute local `H_pkg,thermal` qualification |
| Redfern/Musca/Smith/Dell/Faraone TPCD paper | **IDENTIFIED-NOT-RECOVERED** | IEEE conference bibliographic identity known | Recover full paper experimental section |
| Link from 1998 UWA TPCD apparatus to RP-01 performance device | **OPEN** | no direct identity found | Recover lab notebook/publication source |
| Time-domain vs frequency-domain consistency | **CONTROLLED-LOCAL** | P13/P13A traveler | Execute on local device |
| Bulk-lifetime interpretation | **CONDITIONAL ONLY** | multiple confounds demonstrated empirically | Must clear source/electrical/package/injection/sweepout/trap gates |

---

# Important Round-31 corrections

## 1. 1 kHz is not a lifetime

RP-01's 1-kHz chopped responsivity condition does not imply:

- `f_3dB=1 kHz`;
- `tau=1/(2pi*1kHz)`;
- flat response through 1 kHz.

Those remain experimentally unresolved until P13 is executed.

---

## 2. Package response belongs in temporal de-embedding

P13 now treats the measured response with package thermal context:

`H_meas = H_source H_optics H_detector H_bias H_preamp H_cable H_instrument H_pkg,thermal`

where a simple multiplicative representation is used only when physically valid. Thermal response can instead be a coupled/additive channel.

A slow pole is not intrinsic lifetime merely because electrical readout is fast.

---

## 3. Short pulse does not guarantee low injection

Rajaduray's 25-ns pulse branch itself provides a counterexample: localized generated carriers can approach the equilibrium carrier scale even when average laser power is described as low.

P13 therefore requires excitation-level reduction and waveform/time-constant invariance before a low-injection lifetime claim.

---

## 4. 1.047 µm and 4 µm weight different device regions

The 1998 UWA TPCD method uses 1.047-µm excitation, strongly absorbed near the surface. RP-01 performance is centered in the MWIR near 4 µm.

Do not silently equate their effective temporal responses.

---

## 5. AC coupling is a first-class temporal coordinate

The same-UWA transient branch explicitly used an AC-coupled amplifier.

Unknown high-pass transfer can distort long transient tails and apparent decay constants. Local reproduction must measure the AC transfer using detector-equivalent impedance.

---

# Highest-value source-recovery targets

1. Redfern et al. 1999 full conference paper.
2. Rajaduray apparatus/software appendices or UWA records, especially laser energy/spot and AC amplifier circuit.
3. Keithley model/current/bias-network record.
4. HP54522A trigger/range/termination setup.
5. Any direct transient/frequency-response data for the actual RP-01 Figure-3/5/6/7 detector.

---

# Local qualification now available

The new P13A register classifies a result as one or more of:

- `SOURCE-LIMITED`
- `ELECTRICAL-LIMITED`
- `PACKAGE-THERMAL-CONTAMINATED`
- `HIGH-INJECTION`
- `TRAP/MULTICOMPONENT`
- `SWEEPOUT/TRANSPORT-CONTAMINATED`
- `EFFECTIVE-ONLY`
- `ONE-POLE-DEVICE-RESPONSE-QUALIFIED`
- `BULK-LIFETIME-JUSTIFIED`

`BULK-LIFETIME-JUSTIFIED` is a terminal evidence state, not the default name for a fitted exponential.

---

# Round-31 conclusion

The historical gap has narrowed from “unknown UWA lifetime method” to a quantitatively documented 1998 same-lab transient apparatus, while the actual RP-01 temporal response remains correctly open.

The principal remaining uncertainties are now source fluence/profile, exact readout circuit, injection state, and direct linkage to the RP-01 performance device—not the generic mechanics of how to perform a transient measurement.
