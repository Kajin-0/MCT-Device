# P14 research record — lithography / geometry / historical active-area problem

**Date:** 2026-08-15 America/New_York

## Direct RP-01 re-audit

Smith et al. 2001 explicitly establish:

- two-mask simplified process;
- Mask 1 performs wet chemical mesa delineation;
- anodic oxide follows mesa formation;
- Mask 2 defines contact openings;
- CH4/H2 RIE through Mask 2 both clears passivation and creates the n+ contact region;
- the same Mask-2 resist remains for Cr/Au deposition and lift-off;
- this self-alignment removes the conventional third metal-alignment mask.

Direct Mask-2 resist anchors:

- ~4–5 µm resist thickness;
- 80 °C / 30 min prebake;
- 30-min chlorobenzene soak;
- then pattern/develop/water rinse;
- successful lift-off of 30-nm Cr + 270-nm Au after RIE.

The paper does not identify:

- resist product;
- spin program;
- exposure wavelength/dose;
- aligner mode;
- developer/time;
- quantitative overhang;
- final lift-off solvent/time/agitation.

These remain open.

## General chlorobenzene lift-off sources

Hatzakis, Canavello and Shaw 1980, “Single-Step Optical Lift-Off Process,” IBM J. Res. Dev. 24, 452–460, DOI `10.1147/rd.244.0452`, establishes the positive-resist/aromatic-solvent soak method for creating an overhanging lift-off profile.

Collins and Halsted 1982, IBM J. Res. Dev. 26, 596–604, shows that exposure, chlorobenzene soak, development and bake interact and that linewidth, overhang, resist height and thickness loss are useful process-control observables.

These sources explain mechanism/process control only; they do not identify RP-01 resist chemistry.

## Direct geometry

RP-01 experimental structure:

- thickness 9.5 µm;
- nine contacts;
- each 300×300 µm;
- first separation 50 µm;
- gaps increment by 50 µm.

Derived adjacent gaps:

`50, 100, 150, 200, 250, 300, 350, 400 µm`.

Derived sequential string extent:

`9×300 + (50+100+...+400) = 4500 µm = 4.5 mm`.

Derived contact area:

`300 µm × 300 µm = 0.09 mm² = 9×10^-4 cm²`.

Derived nominal active inter-contact areas if width is exactly 300 µm:

- L=50 µm → A=1.50×10^-4 cm²;
- 100 → 3.00×10^-4;
- 150 → 4.50×10^-4;
- 200 → 6.00×10^-4;
- 250 → 7.50×10^-4;
- 300 → 9.00×10^-4;
- 350 → 1.05×10^-3;
- 400 → 1.20×10^-3 cm².

Final P10/P11/P12 normalization must use measured fabricated width/gap, not these nominal values.

## Stronger historical device-identity closure

RP-01 text explicitly says spectral responsivity and specific detectivity in Figures 6 and 7 are for **the same device presented in Figures 3 and 5**.

Therefore a single “typical device” underlies:

- Figure 3: 4-µm responsivity vs electric field;
- Figure 5: noise ASD vs frequency at 10 V/cm;
- Figure 6: spectral responsivity at 10 V/cm;
- Figure 7: spectral D* at 10 V/cm.

This is valuable because the active-area reconstruction problem is now a one-device problem.

Still missing: which of the eight adjacent contact gaps was used for this typical device.

## 50-µm gap inference — current status

For W=300 µm and L=50 µm:

`A = 1.50×10^-4 cm²`, `sqrt(A)=0.012247 cm`.

If `e_n = 24.5 nV/√Hz` and `Rλ(4 µm) ≈ 4×10^5 V/W`, then

`D* = Rλ sqrt(A)/e_n ≈ 2.0×10^11 cm Hz^1/2/W`,

matching the reported BLIP value.

This is **not yet proof** that the typical device is the 50-µm gap because:

1. the exact Figure-3/Figure-6 4-µm responsivity at 10 V/cm has not been numerically digitized from the primary graph;
2. the 24.5 nV/√Hz value is the reported g-r noise plateau at higher frequency, while the spectral response was chopped at 1 kHz and the 1/f knee is ~3 kHz;
3. the paper does not explicitly state which noise convention/value was inserted into Figure 7;
4. active optical width may not be exactly the full 300-µm metal-pad width if mesa geometry differs.

Status: `[INFERENCE-OPEN]`. Do not promote into RP-01 historical geometry.

## New controlled module

`procedures/P14_LITHOGRAPHY_MASK_GEOMETRY_CD_QUALIFICATION.md`

Key process-control principle:

Track separately:

`CD_mask → CD_resist → CD_mesa → CD_RIE_open → CD_n+ → CD_metal → measured gap/active area`.

Wet etch, RIE and electrical conversion each alter different geometrical boundaries, so they cannot be collapsed into one nominal mask CD.

## Next branch

P15 should address die separation, die attach, interconnect/wire bond, cold-finger/package geometry, cryogenic thermal anchoring and optical aperture/shield integration.

Historical RP-01 packaging details are not currently closed; search same-UWA/Faraone photoconductor papers/theses and authoritative HgCdTe package literature before defining a transfer qualification.
