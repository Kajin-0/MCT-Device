# 2026-08-15 — RP-01 RIE blocking-contact lineage

## Objective

Close the CH4/H2 reactive-ion-etching module sufficiently to reproduce the electrical blocking-contact function used in RP-01 rather than merely copy nominal RF/pressure/time setpoints.

---

## 1. Direct RP-01 process condition

Smith et al. 2001 directly state:

- parallel-plate Plasma Technology RIE;
- gas notation `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- RF power `50 W`;
- process time `1 min`.

These remain the canonical nominal P08 condition.

## 2. Gas-ratio ambiguity deliberately left open

The current source audit searched the exact printed notation `CH4/5H2` across the UWA/Faraone HgCdTe lineage.

Result:

- the notation is repeatedly reproduced in publications;
- related papers also use `CH4/H2` or `H2/CH4`;
- no source located in the current search explicitly states the two individual mass-flow-controller setpoints corresponding to `CH4/5H2`.

Therefore the project **must not infer** that the expression means:

- one part CH4 to five parts H2;
- five parts CH4 to one part H2;
- 5% H2 in CH4;
- 5% CH4 in H2;
- or another premixed-cylinder notation.

Until an original lab method, thesis, gas-system record or explicit full-text statement is located:

- `Q_total=64 sccm` is closed;
- `Q_CH4` is open;
- `Q_H2` is open.

This is a genuine release blocker, not a typographic detail.

---

## 3. RP-01 blocking-contact electrical outcome

Smith et al. report that RIE-converted material was characterized at 80 K and 300 K with variable magnetic field up to 2 T.

Reported summary properties:

- n-type converted density `~2.0×10^15 cm^-3`;
- mobility `~3.3×10^4 cm²/V·s`.

The accessible primary text does not yet uniquely map this numerical pair to one measurement temperature. Do not relabel it without the corresponding figure/data extraction.

The material target is therefore an **electrical process-response anchor**, not merely a nominal recipe consequence.

---

## 4. RP-01 LBIC test structure and instrument

The process paper uses a plain n-type HgCdTe wafer passivated with approximately 800 Å anodic oxide and patterned to expose approximately 300×300 µm RIE squares.

After plasma exposure:

- oxide removal in the exposed region was checked optically;
- electrical modification was imaged with LBIC;
- sample was measured at 80 K;
- scanner was a Waterloo Scientific system;
- illumination used a diode-pumped Nd:YLF laser at 1.047 µm;
- stated intensity was approximately 400 mW/cm².

This makes LBIC a direct in-line process-monitoring technique for the RIE conversion footprint.

---

## 5. ~8 µm conversion-depth provenance

RP-01 states that earlier work on n-type HgCdTe under similar RIE conditions indicated `n+` doping extending approximately **8 µm below the semiconductor surface**.

The cited source is:

C. A. Musca et al., *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.

The UWA repository abstract verifies that this work:

- studied mid-wave n-type HgCdTe;
- used LBIC to confirm an RIE-induced n+ region;
- extracted information about depth and lateral extent;
- modeled effects of junction depth, temperature and grading.

However, the currently accessible abstract does not give the exact RIE pressure/power/time that generated the ~8 µm result.

Therefore project tag:

`~8 µm = P-OTHER-SOURCE/SIMILAR-CONDITIONS`

not `P-RP01-DIRECT`.

---

## 6. Physical removal is not electrical conversion depth

A closely related UWA p-type experiment provides a useful counterexample:

J. F. Siliquini et al. studied vacancy-doped p-type Hg0.69Cd0.31Te under:

- `410 mTorr`;
- CH4/H2;
- `0.4 W/cm²`;
- physical etch depth `~0.2 µm`.

The electrically converted n-type region extended approximately `1.5 µm` into the semiconductor.

Thus electrical conversion penetrated many times deeper than the physically removed material.

This establishes a mandatory P08 distinction:

- `d_etch` — physical surface recession;
- `d_conv` — electrically modified depth.

Neither may be substituted for the other.

---

## 7. Reactor conditions are strongly process dependent

Same-UWA lineage mesa work used different conditions, for example:

- approximately `400 mTorr`;
- `CH4/5H2`;
- `0.4 W/cm²`.

These are not the RP-01 blocking-contact settings.

Later UWA high-density-plasma work further shows that conversion properties are highly sensitive to pressure and sample temperature and also depend on RF/ICP power.

Therefore `50 W` is not a portable recipe descriptor unless electrode area, RF frequency, self-bias/ion-energy proxy, sample temperature and chamber geometry are known.

---

## 8. Reversible RIE-induced electrical modification

Smith et al. 1998, DOI `10.1063/1.367389`, demonstrate that RIE-induced p-to-n conversion in x=0.31 material can be reversed by a sealed-tube Hg anneal:

- RIE example: `400 mT`, CH4/H2, `90 W`;
- anneal: `200 °C`, `17 h`;
- LBIC showed no remaining n-type converted region;
- Hall returned to the original p-type properties.

This is not part of the RP-01 contact recipe, but it reinforces the mechanism: plasma exposure changes the HgCdTe electrical/native-defect/hydrogen state, not just its topography.

---

## 9. Process-control architecture adopted

P08 now requires:

1. separately calibrate oxide-clear time on the released ~80-nm anodic oxide;
2. measure HgCdTe physical etch rate after oxide clear;
3. reproduce the electrical n+ state with P05 transport;
4. measure the 2-D electrical footprint using LBIC;
5. independently calibrate conversion depth/lateral spread;
6. fabricate Cr/Au TLM structures;
7. require contact resistivity compatible with the RP-01 benchmark;
8. log RIE-to-metallization time;
9. establish chamber-history and sample-temperature controls.

This closes the conceptual process loop:

`plasma setpoints -> oxide clear -> d_etch -> n+/µ -> d_conv/L_conv -> Cr/Au -> rho_c`.

---

## 10. Most important remaining P08 source gaps

1. explicit definition of `CH4/5H2` and individual MFC flows;
2. complete Musca 1998 experimental section giving the exact ~8-µm conversion condition;
3. Plasma Technology reactor model/electrode diameter/spacing;
4. RF frequency;
5. DC self-bias;
6. sample/chuck temperature;
7. physical HgCdTe etch rate under RP-01 conditions;
8. oxide etch rate under RP-01 conditions;
9. lateral conversion beyond a 300-µm square window;
10. RIE-to-metal transfer procedure.

---

## 11. Sources

1. E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. C. A. Musca et al., *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.
3. C. A. Musca et al., *Journal of Electronic Materials* 28, 603–610 (1999), DOI `10.1007/s11664-999-0042-x`.
4. J. F. Siliquini et al., primary UWA scanning-laser-microscopy work on RIE-induced p-to-n conversion in Hg0.69Cd0.31Te, reporting ~1.5 µm conversion after ~0.2 µm physical etch under 410 mTorr, CH4/H2 and 0.4 W/cm².
5. E. P. G. Smith et al., *Journal of Vacuum Science & Technology A* 17, 2503–2509 (1999), DOI `10.1116/1.581988`.
6. E. P. G. Smith et al., *Journal of Applied Physics* 83, 5555–5557 (1998), DOI `10.1063/1.367389`.
7. B. A. Park et al., *Journal of Electronic Materials* 36, 913–918 (2007), DOI `10.1007/s11664-007-0132-6`.
