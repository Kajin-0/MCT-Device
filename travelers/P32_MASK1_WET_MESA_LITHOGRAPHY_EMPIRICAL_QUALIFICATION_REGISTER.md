# P32 — Mask-1 wet-mesa lithography empirical qualification register

**Status:** BLANK CONTROLLED DEVELOPMENT / QUALIFICATION RECORD  
**Use with:** P14, P28, P32, P25

## A. Run identity

- P32 run ID:
- Date/time:
- Operator:
- HgCdTe wafer/coupon ID:
- P03/P04 source/anneal genealogy:
- Wafer coordinate:
- Composition / optical-edge state:
- Incoming local HgCdTe thickness:
- Incoming surface history:
- Time since prior surface process:

## B. Mask / geometry

- Mask ID/revision:
- Tone:
- Nominal mesa dimensions:
- Nominal trench/open dimensions:
- Alignment-mark ID:
- `CD_mask` measurement/reference:

## C. Resist identity

- Manufacturer:
- Product:
- Chemistry/family:
- Positive/negative:
- Product grade/viscosity:
- Lot:
- Expiry:
- Storage history:
- Candidate evidence class:
  - [ ] PRODUCT-IDENTIFIED HBR TRANSFER
  - [ ] THICK NOVOLAK CONTROL
  - [ ] HISTORICAL 180CP CONTROL
  - [ ] OTHER LOCAL-QUAL

## D. Pre-coat surface

- Dehydration treatment:
- Adhesion promoter:
- Cleaning step immediately before coat:
- Surface image/reference:
- Ambient T/RH:

## E. Coat

- Spin coater/chuck ID:
- Dispense method:
- Dispense amount:
- Spin speed:
- Acceleration:
- Spin time:
- Edge-bead action:
- Thickness map positions:
- `h_PR,0` mean:
- `h_PR,0` min/max:
- Uniformity:

## F. Bake / pretreatment

- Bake method:
- Temperature:
- Duration:
- Actual calibrated temperature:
- Post-bake delay to exposure:
- Additional treatment/ash:

## G. Exposure

- Aligner/tool:
- Wavelength/band:
- Contact/proximity/vacuum mode:
- Irradiance calibration ID:
- Dose:
- Focus/gap setting:
- Alignment x/y/rotation:

## H. Development

- Developer product/concentration:
- Developer lot:
- Temperature:
- Time:
- Agitation:
- Rinse chemistry/time:
- Dry method:
- Post-develop bake/ash:

## I. Developed-resist metrology

- `CD_PR` mesa width/length:
- Open/trench CD:
- Resist thickness after develop:
- Sidewall/profile metric:
- Scum/residue:
- Pinhole count/density:
- Adhesion defects:
- Edge roughness:
- Images/file IDs:

## J. P28 etchant genealogy

- P28 recipe ID:
- Explicit Br2 concentration definition:
- EG:HBr definition:
- HBr stock assay:
- Bath batch ID:
- Bath age:
- Vessel:
- Bath temperature before/during/after:
- Agitation mode/rate:
- Sample orientation:
- Exposure start/stop timestamps:
- Actual etch duration:
- Rinse/quench:
- Dry method:

## K. Resist survival after P28

- Remaining resist thickness `h_PR,f`:
- `Delta h_PR`:
- Calculated `S_PR = d_HgCdTe/Delta h_PR` where valid:
- Resist edge retreat `Delta CD_PR`:
- Swelling/softening:
- Cracking/crazing:
- Blister/lift fraction:
- Pinhole breakthrough:
- Discoloration:
- Images/file IDs:

## L. Mesa-transfer metrology before strip

- Etch depth:
- Incoming thickness crossed?:
- Lateral undercut:
- `R_V`:
- `R_L`:
- `A = 1-R_L/R_V`:
- Edge trenching:
- Mesa-top CD:
- Mesa-base CD:
- Sidewall angle/profile:
- Roughness/edge metric:
- Isolation test possible before strip?:

## M. Resist strip

- Strip branch ID:
- Chemistry/product:
- Lot:
- Temperature:
- Duration:
- Agitation:
- Ultrasonics used? If yes, qualified procedure ID:
- Rinse sequence:
- Dry method:
- Etch-end timestamp:
- Strip start/end:
- `t_etch_to_strip`:

## N. Post-strip / P25 handoff

- Residue inspection:
- DIC/optical result:
- Final mesa-top CD:
- Final mesa-base CD:
- Final etch depth:
- Electrical isolation metric:
- Sidewall condition:
- Storage/ambient after strip:
- P25 start timestamp:
- `t_strip_to_P25`:
- P25 bath/process ID:
- P25 anodization `V(t)` file:
- P25 charge/area:
- Any changed induction/voltage signature?:

## O. Dimensional transfer

- `Delta_CD_lith = CD_PR-CD_mask`:
- `Delta_CD_wet = CD_top-CD_PR`:
- `Delta_CD_total = CD_top-CD_mask`:
- Symmetric edge retreat demonstrated?:
- Proposed per-edge mask bias (development only):
- Evidence/uncertainty:

## P. Downstream closure

- P10 fabricated active geometry:
- P11 responsivity result:
- P12 noise/D* result:
- Leakage/surface result:
- Yield/visual defects:

## Q. Disposition

- [ ] INVALID RUN
- [ ] FAIL — COAT/LITHOGRAPHY
- [ ] FAIL — RESIST CHEMICAL SURVIVAL
- [ ] FAIL — MESA GEOMETRY
- [ ] FAIL — ELECTRICAL ISOLATION
- [ ] FAIL — STRIP/PASSIVATION HANDOFF
- [ ] EMPIRICAL-PRELIMINARY
- [ ] EMPIRICAL-VERIFIED
- [ ] LOCAL-QUALIFIED

Failure/observation notes:

Corrective action / next branch:

Reviewer:

Review date:
