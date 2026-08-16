# P26 — Cr/Au metallization and lift-off empirical process window

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert the existing P09/P09A/P14A contact-metallization branch into a literature-grounded, operator-executable qualification sequence for the RP-01 Cr/Au contact stack.

The historical RP-01 process directly closes the metal identities, layer thicknesses, Mask-2 resist sequence, TLM geometry and a cryogenic contact-resistivity outcome, but does **not** disclose the deposition tool/method, base pressure, deposition rates, sample temperature or final lift-off solvent/time/agitation.

P26 therefore uses the following empirical hierarchy:

`direct RP-01 stack + direct RP-01 TLM outcome -> same-UWA deposition-method evidence -> composition-matched HgCdTe contact experiments -> local deposition/lift-off qualification -> detector-level closure`.

P26 supplements P09, P09A and P14A. It does not overwrite their provenance rules.

---

# 2. Evidence classes

## `DIRECT-RP01`

Directly reported by Smith et al. 2001 for the canonical two-mask photoconductor.

## `DIRECT-RP01-PROPOSED-ARCHITECTURE`

A processing architecture explicitly identified by Smith et al. as advantageous, but not proved to have been used on every reported experimental device.

## `SAME-UWA-METHOD`

A UWA HgCdTe fabrication paper from the same laboratory lineage establishing a practical deposition method, but not the exact RP-01 recipe.

## `PRIMARY-X029-AU-TRANSFER`

Direct LPE HgCdTe experiment near x≈0.29 using thermally evaporated Au, useful for rate/thermal-history screening but based on p-type material and no Cr adhesion layer.

## `PRIMARY-X030-INTERFACE-TRANSFER`

Direct x≈0.30 HgCdTe metal-interface experiment with quantitative surface/interface oxidation or timing evidence, but different doping/contact architecture.

## `PRIMARY-HGCDTE-CONTACT-TRANSFER`

Other direct HgCdTe metal-contact experiments useful for process-variable/failure evidence.

No value may change class through repetition in this repository.

---

# 3. Canonical RP-01 metallization — `DIRECT-RP01`

The published contact stack is:

- Cr: `300 Å = 30 nm`;
- Au: `2700 Å = 270 nm`;
- total nominal metal thickness: `300 nm`.

Mask-2 photoresist directly reported for the same RIE + metal lift-off sequence:

- resist thickness approximately `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene soak `30 min`;
- then pattern/develop/water rinse;
- resist remains in place through CH4/H2 RIE and subsequent metal deposition/lift-off.

Thus nominal resist:metal thickness ratio is approximately:

- `4/0.30 = 13.3`;
- `5/0.30 = 16.7`.

This favorable thickness ratio does not by itself guarantee successful lift-off; sidewall profile and deposition directionality remain controlling variables.

Historical contact structure:

- nine contacts;
- each `300 µm × 300 µm`;
- initial separation `50 µm`;
- separation increased in `50-µm` increments;
- reported specific contact resistance approximately `9×10^-4 Ω·cm² at 80 K`.

This `rho_c` value is the direct empirical P26 contact benchmark.

---

# 4. Historical deposition-method status

The recovered RP-01 article does **not** identify whether Cr/Au was deposited by:

- thermal evaporation;
- electron-beam evaporation;
- sputtering;
- another PVD method.

Therefore no deposition method is `DIRECT-RP01`.

However, same-UWA HgCdTe work from 1998 directly reports **angled thermal evaporation for contact-metal deposition** in fabricated HgCdTe detector structures. Modern UWA HgCdTe photoconductor work also directly reports thermal evaporation of Cr/Au stacks (`10/200 nm`) and linear/symmetric detector I–V behavior over cryogenic-to-room-temperature testing.

### P26 local first-transfer selection

Thermal evaporation is therefore the strongest current **same-laboratory transfer method** for the RP-01 Cr/Au stack.

This is a method selection for local qualification, not a claim that Smith et al. historically used thermal evaporation.

If a local facility instead uses e-beam evaporation or sputtering, treat it as a separate branch because interface bombardment, radiative heating, deposition directionality, stress and residual-gas interactions differ.

---

# 5. RIE-to-metal interface timing

RP-01 explicitly identifies the ability to connect the RIE chamber to the metal-deposition system through a load lock as an advantageous vacuum-processing architecture.

**Evidence class:** `DIRECT-RP01-PROPOSED-ARCHITECTURE`.

The paper does not prove that the reported devices were all metallized without an air break.

## 5.1 Required timestamps

For every P26 run record:

- `t_RF_off` — P08 plasma off;
- `t_RIE_vent`;
- `t_sample_out`;
- `t_metal_load`;
- `t_pump_start`;
- `t_base_accept`;
- `t_Cr_start`;
- `t_Cr_end`;
- `t_Au_start`;
- `t_Au_end`;
- `t_vent_after_metal`;
- `t_liftoff_start`.

Derived clocks:

`Delta t_RIE-Cr = t_Cr_start - t_RF_off`

`Delta t_air = cumulative time with the contact window exposed to laboratory/inert atmosphere before Cr deposition`

`Delta t_Cr-Au = t_Au_start - t_Cr_end`.

Do not substitute total process time for actual air exposure.

## 5.2 Why the clock is mandatory — direct x≈0.30 interface evidence

A 2026 primary study on LPE Hg0.7Cd0.3Te metal contacts deliberately characterized the surface after deoxidation followed by approximately `10 min` of air exposure to represent the condition just before metallization.

In that p-type transfer branch, HAXPES estimated a Te-oxide layer of roughly:

- `~0.9 nm` on the as-prepared surface;
- `~0.3 nm` after deoxidation / before metallization under the study preparation;
- an apparent larger buried oxide after metallization, with the homogeneous-model estimate around `1.6 nm`.

The authors emphasize uncertainty in the post-metal oxide quantification and the origin of the oxidation.

### P26 use restriction

These thicknesses are **not** RP-01 interface specifications. The transferable conclusion is that the state of an x≈0.30 HgCdTe surface can evolve measurably on a practical clean-to-metal timescale and can retain oxide/contaminants at the buried interface.

Therefore RIE-to-Cr delay and atmosphere are process variables, not logistics.

---

# 6. Pre-metal surface rule

The RP-01 contact window exits P08 as deliberately plasma-modified n+ HgCdTe. The same resist is still present for metal lift-off.

Therefore the default P26 baseline is:

`P08 RIE -> controlled transfer -> Cr deposition`

with **no undocumented intermediate wet etch, ion mill or plasma clean**.

A primary HgCdTe Ti/Pt/Au contact study demonstrates how strongly alternative contact technologies can deliberately modify the surface before metal:

- n-type x≈0.20 HgCdTe;
- low-energy `500 eV` Ar ion mill to create an n+ surface;
- fresh `0.05% Br2 + HBr` etch for `2 s`;
- Ti/Pt/Au `300/300/4500 Å` deposited by DC sputtering and patterned by lift-off.

That process achieved specific contact resistance of order `10^-4 Ω·cm²` in its own architecture.

### P26 restriction

Do **not** transplant the `500 eV` ion mill or `0.05% Br2/HBr / 2 s` treatment into RP-01. Either could alter/remove the deliberately engineered P08 converted layer and represents a separate process branch.

If local data show an interface-cleaning step is necessary, create a new recipe ID and remeasure:

- electrical conversion depth/state;
- TLM;
- responsivity/noise;
- stability.

---

# 7. Vacuum and chamber record

No historical RP-01 base pressure has been recovered.

Therefore P26 does not assign an invented universal vacuum requirement.

Every deposition run shall record:

- tool manufacturer/model and chamber ID;
- deposition method;
- pump type;
- chamber-clean/seasoning state;
- prior material/source run;
- base pressure immediately before Cr deposition;
- pressure trace during Cr;
- pressure between layers;
- pressure trace during Au;
- RGA spectrum where available;
- source/boat/crucible identities and conditioning;
- source-to-sample distance/orientation;
- substrate holder/carrier configuration.

A local vacuum limit is released only after correlation with contact output and repeatability.

---

# 8. Source material and thickness metrology

For Cr and Au record:

- source form;
- supplier/lot;
- stated purity;
- source mass before/after where useful;
- evaporation boat/crucible material;
- conditioning/pre-evaporation history.

Targets remain fixed for the first transfer program:

- Cr `30 nm`;
- Au `270 nm`.

Use QCM or equivalent in-situ monitoring and independently calibrate actual thickness on witness structures.

Record separately:

- QCM indicated thickness;
- tooling factor;
- density/acoustic-impedance settings;
- witness measured thickness;
- measurement uncertainty;
- within-run and run-to-run thickness variation.

Do not infer Cr thickness by subtracting Au thickness from a combined step unless the metrology uncertainty supports that operation.

---

# 9. Empirical Au deposition-rate anchors

A 2023 primary study on LPE p-HgCdTe near `x≈0.29` thermally deposited Au at two explicitly reported rates:

- `3 Å/s = 0.3 nm/s`;
- `10 Å/s = 1.0 nm/s`.

The optimized Au/p-HgCdTe TLM structure in that study showed:

- as-deposited `rho_c = 2.73×10^-3 Ω·cm²`;
- after `80 °C / 2 h` air anneal, `rho_c = 7.11×10^-4 Ω·cm²`;
- optimized Au-film RMS roughness about `4.19 ± 0.02 nm`.

A separate 2026 p-HgCdTe comparison tested thermal and e-beam Au deposition at `6 Å/s` and `12 Å/s`; the resulting TLM contact resistivities remained much larger than the RP-01 n+/n-contact benchmark, reinforcing that deposition method/rate and semiconductor/contact state cannot be separated.

### P26 use

The values `3`, `6`, `10`, and `12 Å/s` demonstrate **real HgCdTe Au deposition-rate scales present in the literature**.

They do not close the historical RP-01 Au rate and do not define a production range.

For a local thermal-evaporation transfer, the initial Au-rate screen should be chosen inside the stable calibrated operating range of the actual tool, with these published values used only as practical screening references when compatible with the tool and resist thermal budget.

---

# 10. Cr deposition rate remains open

No direct RP-01 or sufficiently matched same-UWA numerical Cr deposition rate has been recovered in the current literature pass.

Do **not** copy the Au rate to Cr.

Cr is the first metal to contact the engineered n+ surface and has different vapor-pressure/source/film-nucleation behavior.

Local Cr-rate qualification shall therefore use at least three stable tool settings (`low / center / high`) while holding:

- final Cr thickness `30 nm`;
- surface preparation;
- RIE-to-metal delay;
- base-pressure class;
- holder geometry;
- Au process;
- lift-off process

fixed.

Responses:

- film continuity/roughness;
- adhesion;
- TLM `rho_c`;
- contact spread;
- I–V symmetry;
- thermal-cycle drift;
- detector noise where appropriate.

Numerical Cr rates remain `LOCAL-QUAL` until measured.

---

# 11. Sample thermal budget during deposition

HgCdTe and the chlorobenzene-shaped photoresist both make substrate heating relevant.

Record:

- initial holder/sample temperature;
- maximum temperature during Cr;
- maximum temperature during Au;
- cumulative time above selected temperature landmarks established during local calibration;
- source-to-wafer distance;
- shutter-open times;
- cooling interval before vent.

If direct wafer thermometry is impractical, qualify the holder/tool using a dummy wafer with representative optical/thermal loading.

## 11.1 Primary HgCdTe contact evidence for temperature sensitivity

The 2005 Ti/Pt/Au contact study explicitly states that metal deposition was kept at low substrate temperature to limit Hg out-diffusion from contact regions. Long-duration subsequent heating changed cryogenic contact properties.

The 2023 Au study found substantial improvement in contact resistivity after an `80 °C / 2 h` air anneal on its p-type Au-contact branch.

These results point in opposite engineering directions depending on interface architecture: modest thermal treatment can modify contact resistance, while Hg loss/interdiffusion is a concern.

### P26 baseline

The first RP-01 transfer shall therefore use **as-deposited, no intentional post-metal anneal** unless direct RP-01 evidence is recovered.

Any post-metal anneal is a separate qualification branch requiring remeasurement of:

- P05/P08 transport where meaningful;
- TLM;
- optical/morphological state;
- responsivity/noise;
- contact aging.

Do not apply the 80 °C / 2 h p-Au result as an RP-01 recipe.

---

# 12. Cr-to-Au deposition sequence

Preferred local baseline:

1. stabilize Cr source behind shutter;
2. deposit calibrated `30 nm Cr`;
3. remain under vacuum;
4. stabilize Au source;
5. deposit calibrated `270 nm Au`;
6. cool sufficiently to protect resist/profile before venting.

Record any delay or vacuum excursion between the two metals.

If the tool requires a vacuum break between Cr and Au, label it as a separate process branch.

No recovered source supports deliberately oxidizing Cr between layers for RP-01.

---

# 13. Deposition directionality and lift-off geometry

Same-UWA HgCdTe work establishes that angled thermal evaporation has been used intentionally for HgCdTe contact formation in other device structures. This demonstrates that arrival-angle geometry can be a designed process variable.

For RP-01 lift-off, the objective is different: reproduce the final metal footprint while preserving discontinuity between metal on the substrate and metal on the resist top/sidewall.

Record:

- source-to-wafer geometry;
- wafer tilt/rotation;
- planetary rotation if used;
- deposition incidence angle where known;
- developed resist top/bottom opening;
- undercut/overhang;
- final Cr/Au CD.

Changing deposition geometry requires repeating the P14A profile/lift-off gate even if rates/thicknesses are unchanged.

---

# 14. Lift-off status

RP-01 proves that the chlorobenzene-conditioned `4–5 µm` photoresist survived P08 and was suitable for lift-off of the `30/270 nm` Cr/Au overlayer.

The recovered historical paper still does **not** disclose:

- lift-off solvent;
- solvent temperature;
- soak time;
- agitation;
- ultrasonication;
- rinse/dry sequence.

Therefore those values remain `OPEN`; P26 does not fill them with generic semiconductor practice.

## 14.1 Local lift-off development rule

Develop the lift-off process first on sacrificial structures reproducing:

- actual P14 resist thickness/profile;
- P08 plasma exposure;
- actual 30/270-nm metal deposition geometry;
- representative mesa geometry.

Record:

- solvent product/lot;
- bath temperature;
- time to first visible release;
- total soak time;
- number of bath exchanges;
- agitation method;
- ultrasound frequency/power/time if tested;
- rinse sequence;
- dry method;
- elapsed metal-deposition-to-lift-off time.

Ultrasonication is not part of the baseline until shown not to cause HgCdTe mesa/contact/passivation damage.

---

# 15. Post-lift-off physical gate

Inspect every qualification TLM/device structure using calibrated optical microscopy and additional SEM/profilometry where necessary.

Record:

- complete unwanted-metal removal;
- metal fences/stringers;
- lifted/peeling edges;
- resist residue;
- particulate redeposition;
- pad scratches;
- pinholes/voids;
- Au/Cr delamination;
- contact opening registration;
- actual contact length/width;
- actual gaps;
- edge roughness;
- evidence of mesa/passivation damage.

Do not mechanically scrape a detector to make a failed lift-off appear passing.

---

# 16. TLM measurement gate

Use the P09/P05 cryogenic methodology with actual fabricated geometry.

Minimum P26 contact qualification:

1. dark low-field I–V of relevant contact pairs at 80 K;
2. both polarities;
3. current-linearity/self-heating check;
4. resistance versus actual measured gap;
5. TLM regression with residual inspection;
6. extracted sheet resistance/contact resistance/transfer length/`rho_c` where assumptions are valid;
7. repeat contact-pair measurements after warm-up/cooldown or controlled aging.

Historical benchmark:

`rho_c ≈ 9×10^-4 Ω·cm² at 80 K`.

A candidate process is not accepted merely because one pair shows a low two-terminal resistance.

---

# 17. TLM measurement-condition warning

The 2005 primary HgCdTe contact study found that background-generated carriers could distort low-temperature TLM interpretation on LWIR material and explicitly used a cold shield to improve contact-resistance determination.

RP-01 is MWIR and a different contact architecture, but P26 shall record:

- optical background/shield state;
- detector/sample temperature;
- bias/current;
- thermal loading.

If TLM changes materially with optical background, the effect must be separated before releasing `rho_c`.

---

# 18. Empirical transfer matrix

P26 development should proceed sequentially rather than varying everything at once.

## Stage 0 — metrology/tool qualification

Close:

- QCM calibration for Cr and Au;
- base-pressure repeatability;
- deposition-rate stability;
- sample thermal calibration;
- source-to-sample geometry;
- P14 resist profile after P08.

## Stage 1 — shortest-delay historical-stack baseline

Use:

- P08 released-candidate contact opening/conversion;
- shortest controlled RIE-to-Cr delay;
- best routinely reproducible clean vacuum;
- 30 nm Cr / 270 nm Au;
- no intentional post-metal anneal;
- conservative stable deposition rates;
- qualified local lift-off.

Measure full TLM/physical output.

## Stage 2 — RIE-to-metal delay

Hold deposition/lift-off fixed and compare multiple controlled delays.

Primary response:

- `rho_c`;
- I–V symmetry;
- contact spread;
- aging.

If available, add XPS/HAXPES/ToF-SIMS witness work to correlate surface oxide/contamination with contact behavior.

## Stage 3 — Cr rate

Use low/center/high stable Cr rates at fixed 30 nm.

## Stage 4 — Au rate / thermal load

Use bounded Au rates at fixed 270 nm. Published `3–12 Å/s` Au studies provide empirical screening scale only.

## Stage 5 — vacuum quality

Use naturally occurring or deliberately controlled safe differences in base/process pressure to estimate contact sensitivity. Do not intentionally introduce contamination that violates tool rules.

## Stage 6 — optional post-metal thermal branch

Only after the as-deposited process is stable, test a bounded thermal treatment if there is an engineering reason. Do not automatically start at 80 °C / 2 h.

## Stage 7 — detector correlation

Freeze the selected metal process and fabricate matched detectors for:

- P10 I–V/self-heating;
- P11 responsivity;
- P12 noise/NEP/D*;
- P13 temporal response;
- thermal-cycle/aging stability.

---

# 19. Practical run record

Every P26 run shall record, at minimum:

### Incoming structure

- wafer/coupon/device ID;
- x/optical metric;
- thickness;
- P08 recipe ID;
- P08 converted-state result;
- P14 recipe/profile result;
- actual contact-window geometry.

### Transfer

- all P08-to-metal timestamps;
- air/inert/vacuum exposure state;
- storage temperature/ambient if delayed.

### Vacuum deposition

- tool/method;
- base/process pressure traces;
- source material/purity/lot;
- source hardware;
- source-sample geometry;
- rate trace for Cr;
- rate trace for Au;
- QCM thicknesses/settings;
- witness thicknesses;
- holder/sample temperature trace/proxy;
- Cr-to-Au interval/vacuum condition.

### Lift-off

- solvent/lot;
- temperature;
- duration;
- agitation/ultrasound;
- rinse/dry;
- final defect inspection.

### Electrical/device closure

- raw I–V;
- actual TLM dimensions;
- regression/residuals;
- `rho_c`;
- thermal-cycle/aging result;
- detector noise/responsivity result when fabricated.

---

# 20. Failure modes

Preserve and classify:

- high or drifting `rho_c`;
- non-ohmic/rectifying I–V;
- contact-to-contact spread;
- air-delay dependence;
- surface oxidation/contamination evidence;
- Cr discontinuity;
- Cr/Au delamination;
- source spitting/particulates;
- Au hillocks/roughness;
- excessive substrate/resist heating;
- resist reflow;
- metal sidewall fencing;
- incomplete lift-off;
- solvent residue;
- ultrasound/mechanical mesa damage;
- vacuum excursions;
- QCM/witness mismatch;
- thermal-cycle cracking;
- contact aging;
- detector 1/f-noise increase despite acceptable TLM;
- responsivity loss caused by contact/process change.

Failed branches remain part of the process history.

---

# 21. Current numerical status

## Direct historical values that may be used as replication targets

- Cr `30 nm`;
- Au `270 nm`;
- photoresist `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene `30 min`;
- TLM contact size `300×300 µm`;
- gaps `50–400 µm` in 50-µm increments;
- `rho_c ≈ 9×10^-4 Ω·cm² at 80 K`.

## Literature transfer values useful for experiment sizing only

- thermal Au rates `3` and `10 Å/s` on LPE p-HgCdTe x≈0.29;
- thermal/e-beam Au rates `6` and `12 Å/s` in another p-HgCdTe study;
- p-Au thermal-anneal example `80 °C / 2 h`, which improved `rho_c` in that branch;
- x≈0.30 interface study used about `10 min` air exposure after deoxidation as a representative pre-metal state;
- n-HgCdTe Ti-contact branch used 500-eV ion milling + 0.05% Br2/HBr / 2 s + DC-sputtered Ti/Pt/Au, demonstrating a **different** deliberate surface-conditioning architecture.

None of these transfer values is an RP-01 production specification.

---

# 22. Release blockers

P26 remains `PRE-RELEASE` until the following are closed locally or historically:

1. historical RP-01 deposition method;
2. historical/base-pressure requirement or local qualified maximum;
3. Cr source/purity and deposition rate;
4. Au source/purity and deposition rate;
5. sample-temperature limit during deposition;
6. RIE-to-Cr maximum air/total delay;
7. Cr-to-Au vacuum-break rule;
8. exact lift-off solvent/time/temperature/agitation;
9. rinse/dry sequence;
10. QCM-to-witness thickness calibration;
11. final Cr/Au thickness tolerances;
12. TLM measurement uncertainty/background-light control;
13. `rho_c` statistical acceptance window;
14. contact-uniformity criterion;
15. thermal-cycle/aging requirement;
16. detector-noise/responsivity correlation.

---

# 23. Primary-source set used by P26

1. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16 (2001) 455–462, DOI `10.1088/0268-1242/16/6/306`.
2. E. P. G. Smith et al., “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors,” Proc. SIMC-XI (2000), pp. 318–321, IEEE document `939185`.
3. J. Piotrowski et al./C. Musca et al., same-UWA 1998 HgCdTe heterostructure detector papers reporting angled thermal evaporation for contact-metal deposition, DOI `10.1088/0268-1242/13/10/025` and `10.1007/s11664-998-0046-y`.
4. S. Ma et al., “Damage-free lift-off of epitaxial HgCdTe thin films for future curved infrared imaging array applications,” *Infrared Physics & Technology* 151 (2025) 106073, DOI `10.1016/j.infrared.2025.106073`.
5. W. Pan et al., “Van der Waals Epitaxy of HgCdTe Thin Films for Flexible Infrared Optoelectronics,” *Advanced Materials Interfaces* (2023), DOI `10.1002/admi.202201932`.
6. V. S. Meena et al., “Structural, compositional, morphological and electrical characteristics of thermally evaporated Au Ohmic Contact on p-type HgCdTe substrate for possible infrared detectors,” *Optical Materials* 141 (2023) 113943, DOI `10.1016/j.optmat.2023.113943`.
7. A. Colas Reuillon et al., “Electrical and Physicochemical Study of the Metal/p-HgCdTe Interface for MCT-Based Infrared Detectors,” *Journal of Electronic Materials* 55 (2026) 6638–6646, DOI `10.1007/s11664-026-12909-8`.
8. V. Srivastav et al., “Electrical properties of titanium-HgCdTe contacts,” *Journal of Electronic Materials* 34 (2005) 225–231, DOI `10.1007/s11664-005-0208-0`.
9. S. K. Gaur et al., “Experimental study of the nanoscale gold Ohmic Contact's for prospective infrared detectors on a p-type HgCdTe,” *Optics Communications* 604 (2026) 132846, DOI `10.1016/j.optcom.2025.132846`.

