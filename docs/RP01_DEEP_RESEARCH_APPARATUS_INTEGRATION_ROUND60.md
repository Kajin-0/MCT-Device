# RP-01 deep-research apparatus integration — Round 60

**Date:** 2026-08-17 America/New_York  
**Publication state:** `RP01-EXHAUSTIVE-EMPIRICAL-PROTOCOL-ROUND60-DEEP-RESEARCH-CANDIDATE = YES`

## Purpose

Round 60 integrates an unusually deep primary/official-source research pass into the exhaustive HgCdTe research-fabrication protocol. The goal is not a manufacturing traveler or process release. The goal is to make each experimental coordinate physically meaningful by preserving material state, apparatus geometry, calibration state, hard-number recipe, operator sequence and measured result.

## Evidence handling

Existing publication classes remain `RP`, `SL`, `PT`, `DER`, `SYN`.

Round 60 adds optional SYN confidence modifiers:

- `SYN-H`: strongly constrained engineering implementation;
- `SYN-M`: plausible working coordinate with partial primary/official support;
- `SYN-L`: first prototype coordinate introduced where exact historical apparatus geometry remains unpublished.

A SYN modifier never turns a synthesized choice into historical fact or validated capability.

## Major primary-source recovery — source synthesis and LPE

### Radhakrishnan et al. 2003

The original modified-horizontal-slider HgCdTe paper provides the following apparatus/process facts:

- high-purity/high-density graphite construction;
- `15 × 15 × 1 mm` CdZnTe substrate;
- movable sliding plate and solution-bin block;
- separate HgTe cavity under a close graphite cover;
- horizontal quartz tube with stainless-steel end flanges;
- gas-flow, push-pull-rod and thermocouple access;
- 6N Hg, Cd and Te;
- evacuated-quartz-ampoule source synthesis at `700 °C / 8 h`;
- `10 g` source batch;
- approximately `4.8 g` source charge per growth;
- `3 g` HgTe reservoir per run;
- apparatus functions addressing Hg-loss compensation, in-situ meltback, substrate removal and wipe-off.

Primary identifier: DOI `10.1016/S0022-0248(02)02530-7`.

### Honeywell patents

Bowers & Schmit / Honeywell US4317689A adds:

- graphite substrate recess;
- through-growth wells tapered toward the substrate and capped above;
- separate shallow HgTe-source recess;
- upper/lower Hg-vapor grooves/moats beneath a close-fitting graphite cover;
- N2 purge followed by H2 process atmosphere;
- Hg-loss compensation via the auxiliary source.

Hager & Wood / Honeywell US4592304A adds a dedicated wipe-off architecture using CdTe pieces held in vertical guides at approximately `1 mm` spacing.

The patents establish architecture, not a complete dimensioned machining drawing.

## Round-60 source-ampoule implementation

Historical HgCdTe source paper gives quartz + evacuated + `700 °C / 8 h`, but not ID/OD/wall/free volume/seal geometry.

Round 60 therefore uses a semiconductor-crystal-growth transfer geometry as a development start:

- fused-silica ampoule `25 mm OD / 22 mm ID` (`SYN-M`);
- approximately `150 mm` usable internal length (`SYN-M`);
- gross cylindrical volume about `57.0 mL` (`DER`);
- target loaded free volume `50±5 mL` (`SYN-M`);
- vertical/fixed initial orientation (`SYN-L`).

The ampoule is explicitly treated as a pressure-bearing hazardous containment system at 700 °C. A facility-specific pressure/thermal engineering qualification, seal qualification and secondary containment are required before loaded use. PNNL-37304 is used for quartz seal/inspection practice only; its different slight-vacuum irradiation-specimen procedure is not a HgCdTe source-synthesis vacuum.

Hg-bearing material is kept cold during pump-down with an Hg-compatible trapping/containment scheme so evacuation does not become an uncontrolled Hg-distillation path.

## Round-60 LPE prototype geometry

Because exact historical dimensions remain unpublished, Round 60 supplies one clearly labeled first prototype consistent with the recovered 15-mm substrate, 4.8-g run charge and covered-slider architecture:

- substrate recess: `15.10 × 15.10 mm`, depth `t_s+0.02 mm` — `SYN-L`;
- slider thickness: `4.00 mm` — `SYN-L`;
- growth-well upper envelope: about `15.5 × 15.5 mm` — `SYN-L`;
- lower opening: `14.5–14.8 mm` — `SYN-L`;
- well depth: `4.0 mm` — `SYN-L`;
- geometric well volume: about `0.961 mL` — `DER` from prototype geometry;
- HgTe-source cavity: about `20 × 15 × 2 mm` — `SYN-L`;
- first Hg-vapor moat cross-section: about `1 × 1 mm` — `SYN-L`;
- active-region mating-surface flatness target `<20 µm` — `SYN-M`;
- slider translation reference `2.0 mm/s` — retained SYN development center.

A dimensioned drawing and CMM/optical metrology report are required before the apparatus is described as defined. No prototype dimension is to be relabeled Honeywell-identical.

## Furnace and atmosphere

Round 60 retains tube-volume-normalized atmosphere control because absolute flow is not portable across tube diameters:

- N2 purge: at least five measured tube-volume exchanges;
- process H2 flow recorded as both actual flow and tube-volumes/minute;
- O2/dew-point process endpoints retained;
- calibrated thermometry position and dummy-boat temperature map required;
- temperature map, thermal correction and actual T(t) archived with each research campaign.

This makes the physical gas/thermal state reconstructible without inventing an historical sccm value.

## Wet processing

### Mesa etch

Round 60 retains the primary x≈0.28 family and the existing 100-mL transferred implementation while adding:

- HBr stock assay recorded explicitly;
- mixing order `EG -> HBr -> equilibrate -> Br2 last`;
- `5±1 min` post-mix equilibration;
- controlled bath temperature and age;
- reproducible gentle agitation;
- co-patterned same-bath witness;
- device time calculated from the witness rate rather than a blind literature exposure.

The exact historical meaning of “2% Br2” is still not documentary proof of the 2.00-mL/100-mL implementation; the latter remains an explicit transfer choice.

### Anodization

Primary `0.1 M KOH / 90% EG / 10% water / ~0.3 mA cm^-2 / ~2 min / ~80 nm` anchors are preserved. Apparatus definition now emphasizes actual cell geometry, electrode spacing/area, wetted device area, microampere current-source calibration, V(t) logging and independent oxide-thickness verification.

## Lithography

Current AZ P4620 documentation is used as modern implementation guidance, not historical RP-01 identity. The important portable coordinate is measured film thickness and measured exposure dose at the specimen plane, not a nominal spin speed or exposure time alone.

Where the deep-research report suggested process values weaker than existing direct/primary-transfer anchors, Round 60 retains the stronger existing value rather than replacing it merely for uniformity.

## RIE apparatus definition

Direct RP-01 remains:

- Plasma Technology parallel plate;
- printed `CH4/5H2`;
- `64 sccm` total;
- `100 mTorr`;
- `50 W`;
- `60 s`.

Round 60 additionally requires:

- powered-electrode diameter/area and material;
- electrode spacing and powered/grounded assignment;
- exact RF frequency;
- MFC model, full scale, gas calibration and setpoint;
- chamber/base-pressure/seasoning state;
- specimen x/y/carrier/backside seating;
- forward/reflected power;
- dc self-bias;
- sample/platen thermal state;
- oxide-clear time and semiconductor exposure separately.

The historical electrode diameter and self-bias were not recovered. A nominal 50 W remains insufficient for reactor equivalence. `P/A_e` is useful context only.

## Metallization

Round 60 retains the direct `30/270 nm` Cr/Au stack and the qualified thermal-evaporation first branch, while adding apparatus geometry:

- QCM location in `x,y,z,theta` relative to source and sample;
- material-specific controller/QCM parameters;
- separate Cr and Au tooling-factor closure against substrate-plane witnesses;
- source/boat/crucible identity and geometry;
- source-to-substrate distance/orientation;
- sample rotation and thermal history.

For a multiplicative tooling-factor convention:

`TF_new = TF_old * t_witness/t_QCM`.

The installed controller's convention must be checked before applying this expression.

## Packaging and cryogenic assembly

Primary Honeywell evidence supports compliant silicone attachment as a design family because rigid/glass attachment cracked during deep cooling while silicone-attached devices survived. It does not establish a universal modern adhesive or unique force optimum.

Round 60 adds research coordinates for:

- die-seat geometry/flatness;
- bondline and tilt;
- geometry-derived dispense volume;
- modern candidate material prescreening using NASA outgassing data;
- five 300-K to 77–80-K development thermal cycles;
- initial cool/warm rate `<=2 K/min` (`SYN-L`);
- cold dwell `>=30 min` after stability;
- matched-state resistance/noise checks.

For a `2 × 2 mm` die and `50 µm` ideal bondline:

`V_ideal = 0.200 µL`; with a 20% allowance, `V_dispense ≈ 0.24 µL`.

## Absolute responsivity and measurement implementation

NIST detector-metrology sources strengthen the Round-57 underfilled radiant-power substitution method:

- InSb working-standard-class reference preferred over roughly the 3–5.2 µm region when the certificate is applicable;
- detector-plane beam profile and centering are part of the uncertainty model;
- radiant-power and irradiance calibrations are distinct modes;
- reference-before / DUT / reference sequence is retained;
- NIST-style component uncertainty budget is now explicit.

The representative Round-60 planning budget RSS is about `1.65%` relative standard uncertainty (`k=1`) and approximately `3.3%` at `k=2`. These are planning values, not a substitute for the actual reference certificate and measured campaign uncertainty.

## Appendix D — physical apparatus definition

Round 60 adds a multi-page apparatus-definition appendix covering the physical coordinates required to reconstruct:

- source ampoule and synthesis furnace;
- LPE tube/furnace/boat/drive/gases;
- wet etch/anodization;
- spinner/aligner;
- RIE;
- evaporator/QCM;
- package/wire bond;
- cryostat;
- optical bench/monochromator;
- lock-in/noise/transient chain;
- analysis software/calibration files.

The appendix is deliberately not a traveler. It does not collect signatures. It defines what makes an apparatus implementation scientifically reconstructible.

## Residual OPEN coordinates

Even after this pass, the following historical quantities remain genuinely unrecovered:

- Radhakrishnan source-synthesis ampoule ID/OD/wall/free volume;
- exact synthesis pre-seal pressure, ramp/cool and orientation;
- historical Honeywell/Radhakrishnan slider thickness and solution-well dimensions;
- substrate-pocket clearance, Hg-source-recess dimensions and moat cross section;
- exact LPE tube diameter, thermocouple type/position and slider velocity;
- exact meltback recipe;
- Smith RIE electrode diameter and dc self-bias;
- Smith specimen temperature during RIE;
- historical RP-01 Cr/Au source boats, source distance and QCM location;
- original detector-package drawing, silicone cure state and wire-bond recipe;
- exact historical optical-bench/monochromator implementation for all reported measurements.

These remain OPEN or SYN development coordinates rather than fabricated historical facts.

## Disposition

Round 60 materially closes apparatus/operator detail from public evidence but remains a literature-derived research protocol. It does not demonstrate historical reproduction or end-to-end empirical process validation.