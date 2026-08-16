# Source ledger addendum — Round 38: Cr/Au deposition apparatus / vacuum / rate provenance

**Date:** 2026-08-16 America/New_York  
**Scope:** P16A R20 / P09 / P09A / P26 / P26A

## 1. Round objective

Determine whether the historical RP-01 Cr/Au deposition process can be upgraded beyond:

- Cr `30 nm`;
- Au `270 nm`;
- compatible chlorobenzene-shaped lift-off mask;
- 80-K `rho_c≈9×10^-4 Ω·cm²`;

and, where historical closure is not possible, define the minimum actual-laboratory apparatus state required for a traceable first qualification build.

---

## 2. Direct RP-01 source

### E. P. G. Smith et al. 2001

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Evidence:** `DIRECT-RP01`.

Recovered/confirmed:

- Cr `300 Å`;
- Au `2700 Å`;
- 4–5-µm resist;
- 80 °C / 30-min prebake;
- chlorobenzene 30 min;
- pattern/develop/water rinse;
- resist suitable for post-RIE lift-off of the Cr/Au stack;
- TLM structure and approximately `9×10^-4 Ω·cm²` specific contact resistivity at 80 K;
- text describes the beneficial vacuum-processing capability obtained by allowing the RIE chamber to be connected by load lock to a metal-deposition system.

Not recovered from the paper:

- deposition method;
- metal-deposition tool;
- source hardware;
- base/process pressure;
- Cr/Au rates;
- source/sample distance;
- sample temperature;
- QCM details;
- whether the experimental devices actually used the proposed load-lock architecture;
- lift-off solvent/time/agitation.

**Important interpretation:** load-lock is a `DIRECT-RP01-PROPOSED-ARCHITECTURE` statement, not documentary proof that the measured devices had zero air break.

---

## 3. Same-UWA method-family evidence

### C. Musca et al. 1998

C. Musca, J. Antoszewski, J. Dell, L. Faraone, J. Piotrowski, Z. Nowak, “Multi-Heterojunction Large Area HgCdTe Long Wavelength Infrared Photovoltaic Detector for Operation at Near Room Temperatures,” *Journal of Electronic Materials* 27, 740–746 (1998), DOI `10.1007/s11664-998-0046-y`.

**Evidence:** `SAME-UWA-1998-ANGLED-THERMAL`.

Direct abstract/repository wording states detector structures used:

- conventional dry etching;
- angled ion milling;
- **angled thermal evaporation for contact metal deposition**.

Use:

- establishes that thermal evaporation was a real UWA HgCdTe contact-deposition method in the immediate pre-RP-01 laboratory lineage.

Restriction:

- photovoltaic IVPE/As-doped architecture;
- not the RP-01 n-type LPE photoconductor;
- no basis to assign its angle/tool/rate/vacuum to RP-01.

### J. Piotrowski et al. 1998

J. Piotrowski, Z. Nowak, J. Antoszewski, J. Dell, L. Faraone, C. Musca, “A novel multi-Heterojunction HgCdTe long-wavelength infrared photovoltaic detector for operation under reduced cooling conditions,” *Semiconductor Science and Technology* 13, 1209–1214 (1998), DOI `10.1088/0268-1242/13/10/025`.

**Evidence:** `SAME-UWA-1998-ANGLED-THERMAL`.

Independently repeats angled thermal evaporation for contact-metal deposition in the closely related UWA device branch.

This corroborates method-family use but still does not identify RP-01 deposition hardware.

---

## 4. Same-team historical bridge sources — identified, detailed traveler not recovered

### Musca / Smith / Dell / Faraone 1999

“Performance and stability of HgCdTe photoconductive devices: A study of contact and passivation technology,” in *1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings*, published 1999, pp. 283–286.

UWA institutional metadata confirms:

- same laboratory;
- direct overlap with RP-01 authors;
- explicit contact/passivation subject.

**State:** `CLOSED-BIBLIOGRAPHIC / EXPERIMENTAL-TRAVELER-NOT-RECOVERED`.

No accessible full experimental text was recovered in Round 38 that closes deposition method/rate/vacuum/lift-off.

### Smith / Winchester / Musca / Dell / Faraone 2000

“Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors,” Proceedings of SIMC-XI (2000), pp. 318–321, IEEE document 939185.

UWA institutional metadata confirms the paper and authorship.

**State:** `CLOSED-BIBLIOGRAPHIC / EXPERIMENTAL-TRAVELER-NOT-RECOVERED`.

This remains the highest-value historical bridge for the RIE-to-metal vacuum-processing architecture, but Round 38 did not recover full text containing exact:

- evaporator model/method;
- pressure;
- rate;
- source hardware;
- transfer sequence.

Do not infer those details from the title.

---

## 5. Existing P26 primary transfer evidence retained

P26 already controls primary HgCdTe contact studies providing numerical Au deposition-rate/interface/thermal sensitivity in other architectures, including several-Å/s thermal/e-beam Au rate examples.

Round 38 did not promote those rates into an RP-01 range.

Rule retained:

`real HgCdTe rate scale != RP-01 historical rate != local production window`.

Cr numerical rate remains especially open and must be locally qualified independently from Au.

---

## 6. Round-38 negative search result

Targeted searches included combinations of:

- UWA + HgCdTe + Cr/Au + thermal evaporation;
- UWA theses + chromium/gold/evaporation;
- 2000 in-situ vacuum-processing title + metal/deposition/load-lock;
- 1999 contact/passivation title + Cr/Au;
- same-author 1998–2005 device papers.

No credible primary UWA source recovered exact RP-01 values for:

- deposition method/tool;
- Cr rate;
- Au rate;
- base pressure;
- pressure during deposition;
- source/boat/crucible;
- source-to-sample distance;
- deposition angle/rotation;
- QCM model/tooling factor;
- wafer temperature;
- actual load-lock use on the measured RP-01 devices;
- lift-off solvent/time.

This negative result should prevent repeated generic searching from being mistaken for progress.

Reopen only with a genuinely new source family: archived IEEE full text, UWA thesis appendix, laboratory traveler, equipment log, notebook, author archive, or another primary record not yet searched.

---

## 7. Resulting evidence hierarchy for first local branch

1. Keep `30 nm Cr / 270 nm Au` as `DIRECT-RP01`.
2. Keep the 80-K TLM result as direct downstream benchmark.
3. Rank **thermal evaporation** as the strongest same-UWA method-family candidate.
4. Do not import the 1998 angled geometry by default.
5. Treat e-beam and sputter as distinct local branches.
6. Define actual local vacuum/tool/source/QCM/thermal/handoff state through P26A.
7. Release process only from P26 physical/TLM/stability/device outcomes.

---

## 8. Controlled files created from this ledger

- `procedures/P26A_CR_AU_DEPOSITION_APPARATUS_INSTANTIATION_ADDENDUM.md`
- `travelers/P26A_CR_AU_DEPOSITION_APPARATUS_QUALIFICATION_REGISTER.md`
- Round-38 P16A integration
- Round-38 gap matrix
- Round-38 checkpoint
