# Source ledger addendum — P13 / P14

This addendum prevents newly recovered sources from existing only in chat while the main `docs/SOURCE_LEDGER.md` awaits its next full consolidation.

## S031 — Redfern et al. 1999 — same-UWA transient lifetime lineage

**Class:** Primary-B / peer-reviewed conference paper  
**Citation:** D. A. Redfern, C. A. Musca, E. P. G. Smith, J. M. Dell, L. Faraone, “On the Transient Photoconductive Decay Technique for Lifetime Extraction in HgCdTe,” in *1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings*, IEEE, published 1999, pp. 275–278. ISBN 0-7803-4513-4.

**Role:** Especially strong P13 lineage because Redfern/Musca/Smith/Dell/Faraone overlap directly with the RP-01 team. Use for transient-photoconductive-decay methodology and lifetime-extraction caveats once the full paper is audited.

**Current audit state:** bibliographic record verified through the University of Western Australia research repository; full numerical experimental extraction pending.

---

## S032 — Hatzakis, Canavello, Shaw 1980 — chlorobenzene single-layer lift-off

**Class:** Primary-A  
**Citation:** M. Hatzakis, B. J. Canavello, J. M. Shaw, “Single-Step Optical Lift-Off Process,” *IBM Journal of Research and Development* 24 (1980) 452–460. DOI `10.1147/rd.244.0452`.

**Role:** Foundational general-process source for a positive AZ-type single resist layer whose surface/profile is modified by chlorobenzene or another aromatic-solvent soak so that development produces an overhang suitable for metal lift-off.

**Use restriction:** This explains why RP-01's 30-min chlorobenzene soak is process-relevant; it does **not** identify the actual RP-01 resist product or establish RP-01 exposure/development setpoints.

---

## S033 — Collins and Halsted 1982 — control of chlorobenzene lift-off

**Class:** Primary-A  
**Citation:** G. G. Collins, C. W. Halsted, “Process Control of the Chlorobenzene Single-Step Liftoff Process with a Diazo-Type Resist,” *IBM Journal of Research and Development* 26 (1982) 596–604.

**Role:** General process-control evidence that lift-off resist geometry depends on coupled variables including exposure, chlorobenzene soak, development and post-application bake. The paper uses linewidth, overhang, resist height and resist-thickness loss as control observables.

**Use restriction:** General mechanism/process-control source only. Do not copy a particular IBM resist/dose/developer into RP-01.

---

## S034 — Smith et al. 2001 — RP-01 geometry/lithography re-audit

**Class:** Primary-A; same as core source S001  
**DOI:** `10.1088/0268-1242/16/6/306`

**New P14-specific extraction:**

- simplified device flow uses two masks;
- Mask 1: wet chemical mesa delineation;
- passivation: anodic oxide;
- Mask 2: contact-window pattern used for RIE passivation opening + n+ generation;
- Cr/Au deposited and lifted off using the same Mask-2 resist, providing self-alignment;
- successful lift-off test used ~4–5 µm resist, 80 °C / 30 min prebake, chlorobenzene 30 min, then pattern/develop/water rinse prior to RIE;
- experimental device/test structure uses nine contacts, each 300×300 µm;
- first nominal separation 50 µm and successive separations increase by 50 µm, giving eight nominal gaps from 50 through 400 µm;
- same structure is stated to permit both TLM/contact-resistance and photoconductor performance evaluation.

**Still unresolved after re-audit:**

- resist manufacturer/product;
- coating/spin recipe;
- exposure wavelength/dose;
- mask aligner mode;
- developer chemistry/concentration/time;
- exact Mask-1 lithography recipe;
- exact mesa outline around the contact string;
- which contact pair/gap generated each published ‘typical device’ performance trace;
- final fabricated CD/undercut/alignment distributions.

---

## Derived geometry note `[D]`

If the nine 300-µm contacts are arranged sequentially in one linear string with the eight stated gaps 50,100,...,400 µm, the nominal end-to-end contact-plus-gap extent is:

`9(300 µm) + 50(1+2+...+8) µm = 2700 + 1800 = 4500 µm = 4.5 mm`.

This is a geometry derivation from the textual dimensions. Confirm the actual mask topology/outer mesa before using 4.5 mm as a sample or mesa dimension.
