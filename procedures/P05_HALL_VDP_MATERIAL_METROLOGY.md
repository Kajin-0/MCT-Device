# P05 — HgCdTe Hall / van der Pauw material-state metrology

**Status:** `CONTROLLED-QUALIFICATION-METROLOGY` — the measurement sequence is sufficiently defined for process-development use; final RP-01 material acceptance tolerances and Hall-factor corrections remain qualification items.

**Purpose:** Measure sheet resistance, resistivity, Hall coefficient, Hall carrier sign, Hall sheet density, bulk Hall density, and Hall mobility of HgCdTe process-control coupons reproducibly enough to control LPE growth and Hg-overpressure annealing.

This procedure is a required gate for P03 and P04.

---

## 1. Why a HgCdTe-specific Hall SOP is required

A generic single-field Hall measurement can be misleading in narrow-gap HgCdTe because:

- electrons, light holes, and heavy holes can contribute simultaneously;
- surface inversion/accumulation layers can contribute a parallel channel;
- carrier populations can change strongly with temperature;
- high electron mobility makes magnetotransport strongly field dependent;
- Hall factor need not equal unity;
- processing can create electrically modified near-surface layers;
- the sample may change measurably with surface age after processing.

UWA work on LPE p-HgCdTe explicitly showed that single-field Hall measurements can represent averaged transport from multiple carrier populations and used variable-field, variable-temperature measurements with quantitative mobility-spectrum analysis to separate them. `[P-HG-MULTI]`

Therefore the controlled output of the basic procedure is called **Hall density** `n_H` or `p_H` and **Hall mobility** `µ_H`. These quantities are not silently renamed “true carrier density” or “drift mobility” unless a single-carrier model and Hall-factor assumption have been justified.

---

## 2. RP-01 reference state

The downstream RP-01 paper reports starting material approximately:

- n-type;
- nominal x≈0.30;
- thickness `t≈9.5 µm`;
- electron concentration `n≈9.8×10^14 cm^-3`;
- electron mobility `µ≈4.0×10^4 cm² V^-1 s^-1`.

The source does not presently close the exact temperature and Hall-reduction convention associated with those two electrical numbers. Therefore the repo must preserve the distinction between:

- **RP-01 reported reference values**, and
- **P05 measurements made under explicitly stated temperature/field conditions**.

No lot should be declared matched to RP-01 without recording measurement temperature.

---

## 3. Derived RP-01 consistency values

Assuming for screening only a one-carrier model with Hall factor `r_H=1`:

`ρ = 1/(q n µ)`

For `n=9.8×10^14 cm^-3` and `µ=4.0×10^4 cm²/V·s`:

- bulk resistivity `ρ ≈ 0.15922 Ω·cm`;
- for `t=9.5 µm`, sheet resistance `R_s ≈ 167.60 Ω/square`;
- Hall coefficient magnitude `|R_H|≈6.3689×10^3 cm³/C`.

The ideal Hall voltage magnitude is

`|V_H| = |R_H| I B / t`.

For the nominal RP-01 state:

- `I=10 µA`, `B=0.10 T` → `|V_H|≈0.670 mV`;
- `I=100 µA`, `B=0.10 T` → `|V_H|≈6.70 mV`.

These are instrument-design benchmarks, not required operating current.

---

## 4. Sample geometry requirements

The basic material-control geometry is a van der Pauw specimen.

Required assumptions:

1. conducting region is thin relative to lateral dimensions;
2. sample is simply connected — no internal hole or isolated nonconducting island;
3. electrical properties are sufficiently homogeneous for a sheet reduction;
4. material is sufficiently isotropic for the scalar van der Pauw result to be meaningful;
5. four ohmic contacts lie at the sample perimeter and are small compared with the sample dimensions.

A Greek-cross geometry may be used where lithographically fabricated material-control structures are available; a square coupon with small corner contacts is acceptable for development measurements.

### Required dimensional record

For every coupon record:

- lateral dimensions;
- thickness of the HgCdTe conducting layer, not total CdZnTe+HgCdTe wafer thickness;
- contact dimensions;
- contact-to-edge geometry;
- sample orientation relative to crystal axes;
- layer/substrate structure.

The insulating CdZnTe substrate is an advantage for P05 because it minimizes substrate parallel conduction, but that assumption must be verified for the actual substrate lot.

---

## 5. Thickness metrology

Bulk density and bulk resistivity depend directly on `t`, so thickness uncertainty propagates one-for-one into those bulk quantities.

P05 must use the **local HgCdTe conducting-layer thickness** applicable to the Hall coupon.

Record:

- measurement method;
- calibration reference;
- number and coordinates of thickness measurements;
- mean thickness;
- standard deviation;
- uncertainty assigned to the mean used in reduction.

If thickness is not known adequately, report only:

- sheet resistance `R_s`;
- Hall sheet density `n_s` or `p_s`;
- sheet conductance.

Do not manufacture a bulk `cm^-3` value from a nominal growth thickness.

---

## 6. Contact requirements

Before magnetic-field measurements, each of the four contacts must be shown to be ohmic over the intended current range at the measurement temperature.

Required contact checks:

1. two-terminal I–V sweep through each practical contact pair;
2. linearity about zero current;
3. positive differential resistance with no rectifying knee in the intended range;
4. contact stability after temperature stabilization;
5. no single contact with anomalously high resistance relative to the others;
6. no visible cracking or delamination around contacts.

The contact material/process is not fixed by P05 because it must remain compatible with the upstream material state. Indium contacts are widely used in HgCdTe Hall work, but the exact RP-01-compatible Hall-contact SOP remains a separate closure item.

Record contact fabrication time because processed HgCdTe can develop time-dependent surface conduction.

---

## 7. Environmental requirements

Measure in darkness or under a defined opaque enclosure to suppress photoconductive and photovoltaic perturbations.

Required environmental records:

- sample temperature;
- temperature stability during each measurement block;
- cryostat/cold-stage identifier;
- ambient/light condition;
- vacuum or exchange-gas condition if relevant;
- elapsed time since sample processing/contact fabrication.

Thermal gradients across the specimen/wiring must be minimized because thermomagnetic and thermoelectric offsets can masquerade as Hall voltage.

---

## 8. Measurement temperatures

### 8.1 Mandatory material-control temperature

For detector-development material, `80 K` is the initial controlled comparison temperature because RP-01 device performance is reported at 80 K and many HgCdTe transport studies operate near 77–80 K.

This does **not** prove that the RP-01 starting-material n and µ values were measured at 80 K; that source detail remains open.

### 8.2 Recommended characterization temperatures

During LPE/anneal qualification, obtain at minimum:

- approximately 80 K;
- 300 K.

For anomalous, compensated, or mixed-conduction material, perform a temperature series over the available cryostat range with enough points to identify carrier freeze-out or sign changes.

A temperature-dependent series is diagnostic; it is not required on every production-control coupon after the process has been statistically qualified.

---

## 9. Current selection and self-heating test

NIST Hall/van-der-Pauw guidance recommends limiting sample dissipation below 5 mW and preferably near or below 1 mW for general semiconductor measurements. For cryogenic HgCdTe, P05 adds an empirical current-linearity/self-heating check rather than relying on a universal fixed current.

### 9.1 Initial current series

At zero magnetic field and stabilized temperature, measure the van der Pauw voltages at a symmetric series of current magnitudes spanning at least a factor of ten, for example:

- 10 µA;
- 30 µA;
- 100 µA.

These values are appropriate starting points for the nominal RP-01 sheet resistance and are **qualification currents**, not universal fixed values.

### 9.2 Selection rule

Choose the largest current for which:

- measured resistance is independent of current within the measurement repeatability;
- current reversal gives symmetric magnitude;
- temperature sensor shows no resolvable sample-temperature rise attributable to current;
- contacts remain ohmic;
- calculated electrical dissipation is comfortably below the general NIST limit.

If 10 µA already causes nonlinearity or heating, reduce current.

Record actual current with calibrated metrology rather than source setpoint alone.

---

## 10. Zero-field van der Pauw resistance sequence

Label contacts sequentially around the perimeter `1,2,3,4`.

At `B=0`, acquire the eight reciprocal/current-reversal measurements following the NIST van der Pauw sequence:

- `R_21,34`
- `R_12,43`
- `R_32,41`
- `R_23,14`
- `R_43,12`
- `R_34,21`
- `R_14,23`
- `R_41,32`

where `R_ab,cd = V_cd / I_ab` with the sign convention documented in the acquisition code.

Use enough settling time after each switch for the voltage to reach a stable plateau. Store the raw current, voltage, timestamp, and temperature for every state.

---

## 11. Zero-field consistency gates

### 11.1 Current-reversal checks

Corresponding reversal pairs should agree:

- `R_21,34` vs `R_12,43`;
- `R_32,41` vs `R_23,14`;
- `R_43,12` vs `R_34,21`;
- `R_14,23` vs `R_41,32`.

### 11.2 Reciprocity checks

Check the redundant reciprocal combinations defined by the van der Pauw sequence.

NIST guidance states failures above 5% should be investigated and agreement within about 3% is preferred.

**P05 rule:**

- `≤3%`: pass for routine qualification;
- `>3% to 5%`: conditional — investigate contacts/uniformity and repeat;
- `>5%`: fail the basic van der Pauw reduction until corrected.

This is one of the first numerical metrology acceptance gates in the MCT-Device process manual.

---

## 12. Sheet-resistance calculation

Form characteristic resistances `R_A` and `R_B` from the redundant measurements.

Solve the van der Pauw equation numerically:

`exp(-π R_A/R_s) + exp(-π R_B/R_s) = 1`.

Do not replace this with the symmetric approximation unless `R_A≈R_B` to a documented tolerance.

Calculate:

- sheet resistance `R_s`;
- bulk resistivity `ρ=R_s t` when thickness is qualified;
- zero-field conductivity `σ=1/ρ`.

Store both the raw characteristic resistances and solved `R_s` so the reduction is auditable.

---

## 13. Magnetic-field calibration and orientation

The magnetic field must be normal to the conducting plane.

Record:

- magnet identifier;
- gaussmeter/field-probe identifier;
- calibration date;
- measured field at the actual sample position;
- polarity convention;
- field angle/orientation;
- spatial field uniformity over the sample.

NIST general guidance calls for field uniformity within approximately 3% and alignment within a few degrees.

The acquisition must use measured `B`, not nominal magnet-current calibration alone.

---

## 14. Required field sweep for HgCdTe

A single `+B/-B` pair is adequate only after the material has been demonstrated to behave as a single-carrier conductor over the chosen range.

During P03/P04 qualification, P05 requires a symmetric field sweep.

### Initial field grid for RP-01-like n-type material

Recommended starting set:

`B = 0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T`.

This is a proposed qualification grid chosen to:

- resolve low-field Hall slope;
- expose curvature/mixed conduction;
- remain practical with a laboratory electromagnet;
- exploit the large Hall signal expected from ~10^15 cm^-3 material.

It is not claimed to be the original RP-01 measurement grid.

For complex or ambiguous material, extend the sweep if a suitable magnet is available. Published HgCdTe magnetotransport studies have used fields from hundredths of a tesla through multi-tesla sweeps specifically to separate carrier populations.

---

## 15. Hall-voltage acquisition at each field

For each nonzero `B`:

1. stabilize magnetic field;
2. record actual `B` and sample temperature;
3. drive current through one diagonal pair;
4. measure transverse voltage on the other pair;
5. reverse current and repeat;
6. repeat using the orthogonal diagonal pair;
7. repeat the full sequence at `-B`.

The minimum data block therefore contains both:

- current reversal;
- field reversal;
- two orthogonal diagonal configurations.

This redundancy separates the odd-in-B Hall component from zero-field geometric/thermoelectric offsets.

Do not discard raw voltages after computing Hall voltage.

---

## 16. Antisymmetrization

For a fixed current orientation, the Hall component is odd in magnetic field.

A basic field-antisymmetrized transverse voltage is

`V_H(B) = [V_trans(+B) - V_trans(-B)]/2`.

Where both current polarities are available, combine current and field reversal so that only the component odd in both current and field is retained.

The acquisition software must document its exact sign convention and unit tests using synthetic data.

Longitudinal magnetoresistance should be formed from the even-in-B component rather than mixed with Hall voltage.

---

## 17. Single-carrier Hall reduction

Only after the field sweep passes the single-carrier checks in Section 18 may the following reduction be used as the primary reported result.

Fit the antisymmetrized Hall voltage versus measured field:

`S_H = dV_H/dB`.

For sample thickness `t` and drive current `I`:

`R_H = t S_H / I`.

For n-type material under the simple one-carrier, `r_H=1` convention:

`n_H = -1/(q R_H)`

with magnitude

`|n_H| = 1/(q |R_H|)`.

For p-type:

`p_H = +1/(q R_H)` under the corresponding sign convention.

Hall mobility is

`µ_H = |R_H|/ρ`

or equivalently

`µ_H = 1/(q |n_H| ρ)`.

Report units explicitly:

- `R_H`: cm³/C;
- `n_H,p_H`: cm^-3;
- `µ_H`: cm²/V·s;
- `ρ`: Ω·cm.

---

## 18. Single-carrier validity checks

A simple one-carrier reduction is accepted only when all of the following are satisfied over the declared fit range:

1. antisymmetrized `V_H(B)` is linear within measurement uncertainty;
2. slopes from the two orthogonal Hall configurations agree within a released reproducibility tolerance;
3. carrier sign does not change within the fit range;
4. longitudinal magnetoresistance does not show behavior indicating an obvious unresolved parallel channel without explanation;
5. results are stable against modest changes in the chosen low-field fit interval;
6. contact/van-der-Pauw consistency gates pass.

If these fail, report **single-field/single-carrier values only as apparent Hall quantities**, not physical carrier densities.

---

## 19. Multicarrier escalation rule

Escalate to variable-field multicarrier analysis when any of the following occur:

- Hall curvature exceeds the voltage/field uncertainty;
- Hall sign changes with field or temperature;
- strong magnetoresistance accompanies Hall nonlinearity;
- processed and unprocessed geometries disagree unexpectedly;
- an n-type surface inversion layer is suspected on p-type bulk material;
- electrical values evolve significantly with time after processing;
- a low-density RP-01-like result cannot be reproduced by a stable linear Hall slope.

For such material, measure the conductivity/resistivity tensor over a sufficiently broad symmetric field sweep and use a documented multicarrier or mobility-spectrum model. Do not fit more carrier populations than the data support.

UWA's iQMSA work is the preferred same-lineage methodological reference for this escalation branch.

---

## 20. Hall factor

The simple relation `n_H=1/(q|R_H|)` implicitly treats the Hall factor `r_H` as unity.

For a single carrier population more generally:

`R_H = r_H/(q n)`

so

`n = r_H n_H`.

HgCdTe Hall factors can depend on band nonparabolicity, degeneracy, scattering mechanism, temperature, and compensation.

**P05 reporting rule:**

- raw/basic report: `n_H`, `µ_H`;
- corrected physical carrier density: only report `n` after stating the Hall-factor model/source and uncertainty;
- never use an undocumented `r_H` correction.

This distinction is important when comparing a new wafer against historical literature whose phrase “carrier concentration” may have used a conventional Hall reduction.

---

## 21. Measurement uncertainty budget

At minimum propagate or report contributions from:

### Hall density

- current calibration;
- magnetic-field calibration;
- Hall-voltage repeatability/noise;
- Hall fit slope;
- thickness uncertainty for bulk density;
- contact/geometry asymmetry residual after reversal;
- temperature stability;
- model/Hall-factor uncertainty separately from instrumental uncertainty.

### Mobility

All Hall-density/Hall-coefficient terms plus:

- sheet-resistance uncertainty;
- thickness uncertainty cancels if mobility is computed directly from sheet quantities, which is preferred where practical.

### Recommended reporting

Report:

- measured value;
- standard uncertainty where established;
- number of repeated readings/runs;
- fit range;
- goodness-of-fit or residual metric;
- whether uncertainty is instrumental-only or includes model uncertainty.

---

## 22. Repeatability protocol

For a process-qualification coupon:

1. complete the full zero-field + field-sweep measurement;
2. return to zero field;
3. repeat the zero-field van der Pauw sequence;
4. repeat at least one low-field `±B` Hall pair;
5. compare beginning/end values.

If drift exceeds the measurement uncertainty, do not average it away. Investigate:

- temperature drift;
- contact instability;
- sample heating;
- magnet hysteresis;
- surface-state evolution;
- light leakage;
- instrument offset.

---

## 23. Material-state record generated by P05

Every completed P05 run must produce a structured record containing:

- sample ID;
- wafer/growth/anneal provenance;
- date/time;
- operator;
- sample geometry and thickness;
- contact geometry/process/age;
- temperature;
- current series and selected current;
- magnetic-field grid and measured fields;
- raw zero-field voltages;
- raw Hall voltages;
- all reciprocal/reversal consistency errors;
- `R_A`, `R_B`, `R_s`;
- `ρ`;
- Hall slope(s);
- Hall sign;
- `R_H`;
- `n_H` or `p_H`;
- `µ_H`;
- field-linearity residual;
- magnetoresistance data;
- single-carrier PASS/FAIL;
- Hall-factor convention;
- uncertainty statement;
- final process-gate disposition.

---

## 24. P03/P04 process gate

For LPE/anneal development, a sample cannot be declared electrically matched to RP-01 based solely on nominal anneal conditions.

P05 must demonstrate:

- n-type sign;
- reproducible Hall density near the RP-01 target;
- reproducible Hall mobility near the RP-01 target;
- acceptable field linearity/single-carrier behavior or a justified multicarrier analysis;
- no unexplained temporal drift.

Exact production acceptance bands around `9.8×10^14 cm^-3` and `4.0×10^4 cm²/V·s` remain `QUAL` until the relationship between these material variables and detector performance/process capability is quantified.

---

## 25. Equipment class

Minimum system capability:

- cryogenic sample stage/cryostat covering approximately 80 K and 300 K;
- calibrated temperature sensor positioned to represent sample temperature;
- reversible electromagnet capable of the selected field sweep;
- calibrated magnetic-field probe/gaussmeter;
- low-noise programmable bipolar current source;
- nanovoltmeter/DMM with input impedance high relative to sample/contact network;
- automated or carefully controlled switching matrix;
- dark sample enclosure;
- four-wire/contact fixture compatible with cryogenic cycling;
- computer acquisition that stores every raw state rather than only reduced results.

For advanced mixed-conduction work, a higher-field superconducting-magnet Hall system is preferred.

---

## 26. Initial RP-01 benchmark check

For a 9.5-µm coupon that truly behaves as an ideal one-carrier material with the RP-01 nominal electrical state, P05 should obtain approximately:

- `R_s ≈ 168 Ω/square`;
- `ρ ≈ 0.159 Ω·cm`;
- `|R_H|≈6.37×10^3 cm³/C`;
- negative Hall sign under the defined n-type polarity convention;
- `n_H≈9.8×10^14 cm^-3` if `r_H=1`;
- `µ_H≈4.0×10^4 cm²/V·s`.

Large disagreement among these internally linked values is a diagnostic for thickness error, multicarrier conduction, Hall-factor assumptions, nonuniform material, contact problems, or a real mismatch to RP-01.

---

## 27. Release blockers

Before P05 becomes a final production-metrology SOP, close:

1. exact temperature associated with the RP-01 quoted starting `n` and `µ`;
2. final Hall-contact fabrication process and aging allowance;
3. thickness SOP and uncertainty requirement;
4. released field grid for routine production versus advanced qualification;
5. numerical field-linearity residual threshold;
6. orthogonal-Hall slope agreement threshold;
7. Hall-factor convention/model for the RP-01 comparison, if any correction is desired;
8. magnetic-field calibration uncertainty requirement;
9. temperature stability requirement;
10. final acceptable `n_H` and `µ_H` process windows;
11. reproducibility/repeatability capability criteria.

---

## 28. Sources

### General measurement method / official metrology guidance

- NIST Physical Measurement Laboratory, “The Hall Effect” and “Resistivity and Hall Measurements,” Hall-effect measurement guidance. The NIST procedure gives the van der Pauw equation, current/field reversal sequence, redundant consistency tests, general power guidance, field-uniformity guidance, and practical error sources. NIST notes this web material is an online archive, so the underlying van der Pauw method and cited ASTM/primary literature remain the method foundations.
- L. J. van der Pauw, “A Method of Measuring Specific Resistivity and Hall Effect of Discs of Arbitrary Shapes,” *Philips Research Reports* 13, 1–9 (1958).

### HgCdTe-specific magnetotransport

- G. K. O. Tsen, C. A. Musca, J. M. Dell, J. Antoszewski, L. Faraone, “Magneto-Transport Characterization of p-Type HgCdTe,” *Journal of Electronic Materials* 36, 826–831 (2007), DOI `10.1007/s11664-007-0103-y`.
- “Method for the characterization of electron, light- and heavy-hole concentrations and mobilities in narrow-gap p-type HgCdTe,” *Materials Science and Engineering B* 44, 278–282 (1997), DOI `10.1016/S0921-5107(96)01760-6`.
- D. Satish Chandra, H. F. Schaake, M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *Journal of Electronic Materials* 32, 810–815 (2003), DOI `10.1007/s11664-003-0075-5`; important caution that 77-K electrical inference of metal-vacancy state becomes problematic for x above roughly 0.26 because of incomplete ionization.
