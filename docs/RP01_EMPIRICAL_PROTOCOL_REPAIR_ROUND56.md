# Round 56 — adversarial repair of the empirical protocol manual

**Date:** 2026-08-16 America/New_York

## Trigger

An external adversarial methods review of the 34-page Round-55 manual found that the arithmetic was generally strong but that several synthesized process combinations had been promoted too quickly into a single executable recipe.

Three findings were treated as publication blockers:

1. the Round-55 `500 × 500 µm` mesa could not contain the published nine-contact TLM string, whose minimum contact-plus-gap envelope is `4500 µm`;
2. anodization chemistry was specified but the actual isolated-mesa anode fixture, wetted area and microampere current requirement were not;
3. the transient protocol used a `20 ns` digitizer interval for a `25 ns` optical pulse, defeating the intended source de-embedding.

## Blocker repairs

### Geometry

Round 56 defines two structures:

- `D1`: `900 × 500 µm` detector mesa, two `300 × 300 µm` contacts, `100 µm` reference gap;
- `T1`: `5000 × 500 µm` TLM mesa containing the direct RP-01 nine-contact, `50–400 µm` gap progression.

The direct contact-string envelope is `4500 µm`; T1 adds `250 µm` nominal margin per end.

### Anodization fixture

The strong TI chemistry transfer remains:

`0.100 M KOH / 90% EG + 10% DI / 0.300 mA cm^-2 / 120 s / ~15 V / ~80 nm`.

Round 56 adds:

- PTFE fixture;
- PTFE-coated temporary spring microprobe;
- `100 × 100 µm` dry contact patch located wholly inside a future Mask-2 metal-contact window;
- wetted-area calculation from actual mesa L/W/t and dry patch;
- nominal D1 current ~`1.40 µA`;
- nominal T1 current ~`7.78 µA`;
- current-source target accuracy `<=1% or +/-20 nA`, whichever is larger;
- sequential anodization of isolated mesas unless separately controlled anode contacts exist.

### Transient acquisition

Round 56 uses:

- `500 MS/s` (`2 ns` interval);
- ~`12.5` sample intervals over a 25-ns optical pulse;
- initial `100 µs` record with `10 µs` pretrigger;
- `128` averages;
- final record `>=10 tau_slowest`;
- separate slow package-thermal acquisition when necessary.

## Upstream material section reclassified

Smith et al. purchased the Fermionics starting LPE material. Protocols 1–7 are therefore labeled:

**COMPOSITE LITERATURE-DERIVED UPSTREAM MATERIAL HYPOTHESIS**.

The Honeywell composition tie-line remains a legitimate composition anchor, but the absolute charge, source synthesis, slider implementation, growth time/temperature and Hg-rich anneal originate from distinct primary lineages.

Round 56 therefore treats `500 °C / 5 min` only as the center of a seven-run local response-surface validation matrix, not an established optimum.

## Other major repairs

- Wet mesa: fixed 4.00-min etch replaced by same-bath witness calibration and `t_etch=(t_epi+d_overetch)/r_witness`; `d_overetch=max(1.0 µm,0.10*t_epi)`.
- HBr: reference implementation explicitly uses `48 wt% HBr in water`; this is a SYN definition, not historical Srivastav identity.
- FTIR: explicit full-spectrum coherent-film/incoherent-substrate model, fitting objective, bounds, beam-footprint rule, covariance/confidence output and physical-thickness cross-check.
- Hall: use `n_H`/`mu_H`; weak-field first fit `|B|<=0.10 T`; high field is diagnostic.
- Hg anneal: Hg reservoir inventory proves non-starvation only; post-anneal Hall/FTIR determines state.
- RIE: individual flows rounded to practical nominal values (`10.7/53.3 sccm`) with MFC uncertainty; reactor equivalence still requires self-bias/thermal evidence.
- Cr/Au: explicit rate tolerances, QCM witness closure and sample-temperature control.
- Packaging: both historical silicone/40-g and silicone/5-g branches survived; compliance is supported, not a 5-g optimum.
- Self-heating: pulse-width/duty sweep and zero-deposited-energy extrapolation.
- D*: RP comparison area frozen to active region between contacts (`L_gap W_active`).
- Noise: analog anti-alias filter, 64 independent records, ~128 DOF and approximate 95% PSD confidence interval; 1-kHz/~3-kHz Smith ambiguity preserved rather than repaired by assumption.
- False precision: process values are rounded to instrument-realizable nominal setpoints and uncertainties/tolerances are stated separately.
- Value-level provenance: critical claims now state source location and transfer delta/use.
- Research gates: explicit evidence required before passing material from one process family to the next.

## Artifact QA

Round-56 review artifacts:

- `RP01_HgCdTe_Empirical_Protocol_Manual_Round56.docx`
- `RP01_HgCdTe_Empirical_Protocol_Manual_Round56.pdf`

QA state:

- 37 pages;
- no fillable PDF fields;
- DOCX accessibility `0 high / 0 medium / 0 low`;
- all DOCX-render pages visually checked after pagination corrections;
- PDF openable, unencrypted, text-native, letter size;
- all 37 PDF pages independently rendered at 200 dpi and visually checked.

SHA-256:

- DOCX `9b9388aa3963489787c72e5899140202eae74ed0f5549e1eacd33b95b946ab21`;
- PDF `697212dca8b4808b9d2cba1a16437f08b569bbf1be9e06c1b2a588379c4cf71c`.

## Disposition

`RP01-EMPIRICAL-PROTOCOL-ROUND56-REVIEW-CANDIDATE = YES`.

This is not a validated reproducible fabrication release. The next pass should attack the remaining SYN values and cross-lineage interactions, not undo the repaired blockers or return to blank forms.
