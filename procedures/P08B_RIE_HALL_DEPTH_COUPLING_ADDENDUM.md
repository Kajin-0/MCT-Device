# P08B — RIE Hall-density / conversion-depth coupling addendum

**Status:** CONTROLLED METROLOGY CORRECTION. This addendum supplements P08 and P05 and takes precedence over any wording that treats the RP-01 `2.0×10^15 cm^-3` RIE carrier density as independent of conversion depth.

## 1. Primary-source observation

Smith et al. 2001 state that Hall/resistivity measurements on RIE-converted n-type HgCdTe gave:

- carrier density `2.0×10^15 cm^-3`, **averaged over the RIE-converted thickness**;
- mobility `3.3×10^4 cm²/V·s`.

Measurements were performed at 80 K and 300 K using a van der Pauw structure with magnetic field up to 2 T.

The same paper separately cites earlier UWA n-type work indicating an RIE-induced n+ region extending approximately 8 µm below the surface under similar conditions.

## 2. Consequence

The published volumetric density is coupled to the thickness used to convert sheet transport into a volume concentration.

For a laterally uniform converted layer,

`N_s = n_vol * d_conv`

where:

- `N_s` = sheet carrier density, cm^-2;
- `n_vol` = reported volume density, cm^-3;
- `d_conv` = electrically converted layer depth, cm.

Therefore a different assumed or measured `d_conv` changes the inferred `n_vol` even if the directly measured Hall sheet signal is unchanged.

## 3. Derived historical sheet-density scale

If the cited `d_conv≈8 µm` is the thickness used in the RP-01 reduction, then

`N_s ≈ (2.0×10^15 cm^-3)(8×10^-4 cm) = 1.6×10^12 cm^-2`.

Tag this value:

`[D / CONDITIONAL ON d_conv=8 µm]`.

It is **not** claimed as a directly published RP-01 sheet-density value until the exact reduction in Musca/Smith data is recovered.

For comparison, if the full 9.5-µm device layer were assumed converted, the same volume density would imply `1.9×10^12 cm^-2`. This illustrates the scale of the thickness dependence.

## 4. Revised P08 transport gate

During reactor transfer, report the following quantities separately:

1. sheet resistance `R_s` of the RIE-modified structure;
2. Hall sheet coefficient / sheet carrier density `N_s` where a single-carrier sheet reduction is valid;
3. Hall mobility `µ_H`, with multicarrier flags;
4. independently measured/inferred electrical conversion depth `d_conv`;
5. derived volumetric converted-region density `n_conv = N_s/d_conv` only after item 4 is closed.

Do not tune the plasma solely to reproduce `2.0×10^15 cm^-3` while allowing an unmeasured change in conversion depth.

## 5. Why this matters physically

The blocking contact depends on both:

- the carrier concentration / electrostatic barrier of the n+ region;
- the depth and lateral geometry of that region.

Two plasmas can yield the same inferred volume density yet different sheet charge and junction depth, or the same sheet density but different volume density because of a different conversion depth. These structures need not give the same blocking potential, sweepout behavior, or contact performance.

Thus the controlled state vector should be treated as at least

`{N_s, µ_H, d_conv, L_conv, d_etch, ρ_c}`

rather than only `{n_vol, µ}`.

## 6. Interaction with P05

For a thin electrically modified layer on a conducting underlying epilayer, a one-layer van der Pauw reduction may be invalid. During qualification:

- retain full variable-field Hall and magnetoresistance data;
- compare pre-RIE and post-RIE transport;
- use mobility-spectrum / multilayer analysis if the response is non-linear or clearly contains parallel conduction;
- report sheet conductance directly before assigning a converted-layer volume density.

## 7. Historical provenance state

Directly published in RP-01:

- `n_avg≈2.0×10^15 cm^-3`, averaged over converted thickness;
- `µ≈3.3×10^4 cm²/V·s`;
- prior similar-condition depth approximately 8 µm is cited to Musca et al. 1998.

Still unresolved:

- exact plasma conditions attached to the 8-µm depth in Musca et al. 1998;
- whether RP-01 used exactly 8 µm in the Hall volume-density reduction;
- exact raw sheet Hall values.

Until these are recovered, use the sheet-density calculation only as a conditional consistency value.
