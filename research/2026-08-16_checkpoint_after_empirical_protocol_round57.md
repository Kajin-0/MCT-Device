# Checkpoint after targeted empirical-protocol metrology closure — Round 57

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Input review disposition

The Round-56 adversarial re-review judged the prior blockers genuinely repaired and upgraded the manual substantially, but identified three remaining major downstream reproducibility gaps: field convention, absolute optical-power coupling and missing executable LBIC/blocking qualification.

Round 57 addresses those directly and then closes the smaller DOE/TLM/singulation/statistics/timing findings.

## Major closures

### Field

The manual now reports both `E_Smith=V_terminal/L_gap` and contact-corrected `E_bulk,est`. Historical comparison remains tied to the terminal convention; the corrected field remains an estimate based on TLM/contact geometry because D1 has no Kelvin voltage-sense pair.

### Absolute responsivity

Protocol 18 is now one explicit underfilled radiant-power comparator method. It requires measured beam size/profile, centering and >=99% overlap with the 100×300-µm active gap before the result is accepted as the canonical `V/W` response.

### Blocking function

Protocol 14A/P37 introduces W1, a dedicated LBIC process-control witness. The reference test uses 1.047-µm CW excitation around 400 mW/cm² at 80 K and quantitative bipolar-boundary criteria. TLM plus W1 LBIC, not TLM alone, is required before detector-performance testing.

## Secondary repairs

- LPE validation is a blocked 2² factorial screen with independent source-synthesis center blocks; no longer called a response surface.
- FTIR gradient coordinate and optional composition-smear parameter are mathematically defined; exact model/code/coefficient hashes are required with real data.
- Wet-etch witness is geometry/resist/orientation matched and co-immersed near D1.
- T1 uses finite-width 2-D TLM reduction.
- Singulation gets explicit SYN wire/tension/speed/feed/slurry mechanics and treats the primary source’s 125-mm wording cautiously.
- Packaging names the historical Dow Corning 3110 RTV reference adhesive; modern substitutions are separate recipes.
- Noise tests record independence/stationarity before nominal DOF; fixed 995–1005-Hz estimator; record bootstrap for final band uncertainty.
- Transient repetition period grows with record length and fitted slow pole; explicit baseline-recovery gate prevents pulse pileup.

## Artifact state

Round-57 files:

- `RP01_HgCdTe_Empirical_Protocol_Manual_Round57.docx`
- `RP01_HgCdTe_Empirical_Protocol_Manual_Round57.pdf`

QA:

- 41 pages;
- DOCX accessibility: `0 high / 0 medium / 0 low`;
- all 41 DOCX-render pages visually inspected;
- final PDF inspector/preflight: 41 letter-size pages, openable, unencrypted, text-native, zero form fields;
- final PDF pixel comparison against the visually inspected LibreOffice PDF: `0 changed pages`;
- final PDF independently rendered at 200 dpi.

SHA-256:

- DOCX `162f51b424acc2a5754bf11fb615f5077091a03f57b5b468e93be5c0181f3d1e`;
- PDF `92f5ec2a6a05af22f77add2ed10c5dded36162c79b27b7d1dc51392dce1aaca8`.

## Current maturity

`RP01-EMPIRICAL-PROTOCOL-ROUND57-REVIEW-CANDIDATE = YES`.

Still false:

- `TRACEABLE-FIRST-BUILD-READY` for an unspecified/uninstantiated lab;
- `HISTORICAL-RP01-REPRODUCED`;
- `REPRODUCIBLE-RELEASE`.

## Next work

The strongest remaining uncertainty is no longer basic downstream metrology architecture. It is the empirical validity of `SYN` settings and cross-lineage process combinations, especially upstream LPE/anneal, modern resist implementation, RIE transfer, metal interface state and package construction. Preserve the hard-number research-protocol format and attack those values individually.