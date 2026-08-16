# Research log — 2026-08-15

## Session objective

Establish a defensible starting architecture for a step-by-step HgCdTe detector fabrication manual and select the first canonical reference device/process without mixing incompatible process families.

## Initial problem statement

The intended final product is much more detailed than a literature review. It must eventually specify all measurements, metrics, times, process steps, equipment, tolerances, calibration requirements, and acceptance criteria needed for a competent researcher to reproduce an HgCdTe detector.

The main scientific risk identified immediately is **false precision created by stitching together individually valid numbers from incompatible HgCdTe processes**. This risk is severe because alloy composition, substrate orientation, Hg chemical potential, melt chemistry, thermal history, doping, surface state, passivation, and contact processing are coupled.

## Decision 1 — use provenance classes

Adopted provenance tags:

- `[P]` direct published experimental value;
- `[B]` authoritative book/reference;
- `[D]` derived value;
- `[C]` apparatus-specific calibration;
- `[Q]` qualification required before release;
- `[T]` tentative research lead.

Reason: a process manual needs to show not only *what number is used*, but *why that number is allowed to be used*.

## Decision 2 — choose a device demonstrated in the literature as the first anchor

Selected Smith et al. (2001), DOI `10.1088/0268-1242/16/6/306`, as RP-01.

Reasoning:

- starts from LPE-grown n-HgCdTe on insulating CdZnTe;
- nominal composition x≈0.30;
- reports starting carrier density and mobility;
- gives a two-mask process architecture;
- gives a complete set of major RIE operating variables;
- gives resist/lift-off preparation details;
- gives anodic-oxide and Cr/Au thicknesses;
- validates the converted contact region electrically;
- measures contact resistivity;
- measures responsivity, noise, cutoff, and D*.

This is substantially stronger than defining our own detector and filling the process with unrelated “typical” values.

## Extracted RP-01 state

Starting material reported by Smith et al.:

- LPE HgCdTe / insulating CdZnTe;
- x≈0.30 n-type;
- n = 9.8×10^14 cm^-3;
- electron mobility = 4.0×10^4 cm^2 V^-1 s^-1;
- device layer thickness = 9.5 µm.

A simple conductivity consistency calculation gives approximately 0.159 ohm cm resistivity from q n µ. This is `[D]`, not a replacement for measured resistivity.

The experimentally demonstrated downstream module includes mesa isolation, anodic-oxide passivation, patterned plasma opening/n+ conversion, Cr/Au metallization and lift-off, followed by electrical/optical characterization.

## Critical finding — published process is still incomplete

Even this unusually detailed paper cannot be converted directly into a literal fab traveler because it leaves out process-critical information, including:

- exact LPE history from the material supplier;
- CdZnTe orientation/composition;
- mesa wet-etch chemistry;
- anodic-oxide growth conditions;
- resist identity/exposure/development;
- metal-deposition environment and rates;
- exact measured detector geometry;
- packaging/interconnect;
- full bias/readout circuit;
- complete noise bandwidth/averaging/calibration settings.

Therefore, the correct representation is **reference process skeleton + closed modules + explicit gaps**, not “complete recipe.”

## Decision 3 — do not use the x≈0.20 LPE process as RP-01 upstream by default

A separate Te-rich LPE literature branch reports detailed growth of x≈0.20 material. Those values may be useful for an LWIR process later, but using them upstream of the x≈0.30 MWIR Smith device would silently change the detector.

Rejected path:

> x≈0.20 LPE growth recipe → Smith x≈0.30 fabrication module

Reason for rejection:

> changes the material band gap, intrinsic concentration, absorption edge, transport behavior, and likely optimum anneal/contact behavior; not a legitimate “completion” of RP-01.

## Upstream candidates identified

### Radhakrishnan, Sitharaman, Gupta 2003

DOI `10.1016/S0022-0248(02)02530-7`.

Strong because it describes a modified horizontal-slider Te-rich LPE apparatus with explicit Hg-loss compensation and in-situ meltback and gives useful charge-synthesis and apparatus information.

Status: candidate apparatus/process source, not yet RP-01-compatible upstream module.

### Harman 1980

DOI `10.1007/BF02822728`.

Strong because it experimentally maps Te-rich liquidus/solidus behavior and reports horizontal-slider LPE over a broad composition range. Useful for constraining valid growth windows rather than supplying a single copied setpoint.

### Tung et al. 1982

DOI `10.1016/0022-0248(82)90468-7`.

High-priority lead because controlled Te-rich horizontal-slider growth explicitly includes x=0.30, overlapping the RP-01 nominal composition.

## Material-property source identified

Hansen, Schmit, Casselman (1982), DOI `10.1063/1.330018`, provides the standard empirical Eg(x,T) relation used as a material-property consistency model.

Important caveat established:

`lambda = hc/Eg` is not automatically identical to a detector's measured cutoff because the experimental cutoff depends on spectral-response convention and edge physics. RP-01 reports a measured 4.4 µm cutoff at 80 K; that measurement takes precedence over an approximate x-based estimate.

## Process architecture created

The manual is divided into:

1. device definition/physics;
2. facility/equipment/calibration;
3. material/source/substrate qualification;
4. LPE charge and growth;
5. post-growth anneal/metrology;
6. mask/device geometry;
7. mesa fabrication;
8. passivation;
9. contact opening/blocking-contact formation;
10. metallization;
11. dicing/package/interconnect;
12. material/electrical/spectral/noise/temporal characterization;
13. process control;
14. failure analysis;
15. final manufacturing traveler.

## Next research questions, in order

1. What exact wet mesa etch was used in the UWA/Faraone photoconductor process lineage?
2. What anodic-oxide growth process generated the 800 Å passivation used on RP-01?
3. What is the original source and exact measurement behind the plasma-induced conversion-depth result cited by Smith et al.?
4. Can the x≈0.30 Tung/LPE process be closed sufficiently to reproduce material compatible with RP-01?
5. What anneal/stoichiometry treatment is required after growth to reach the target n-type electrical state?
6. What exact detector geometry was used for the reported RP-01 noise and D* measurements?
7. What measurement settings are required to reproduce the reported D* with an unambiguous ENBW?

## Continuity instruction

Do not skip directly to a polished final booklet. Continue closing one module at a time, maintaining explicit source compatibility and gap status. Update `AGENTS.md` when a major branch is accepted/rejected or when a process module reaches qualification-ready status.
