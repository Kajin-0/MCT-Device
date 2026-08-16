# RP-01 gap matrix addendum — Round 21 empirical wet mesa

**Date:** 2026-08-16 America/New_York  
**Controlling new procedure:** `procedures/P28_WET_MESA_EMPIRICAL_PROCESS_WINDOW.md`

Status vocabulary:

- `CLOSED-P`: direct RP-01 publication closure;
- `CLOSED-UWA`: same-UWA HgCdTe device/process closure;
- `PRIMARY-X028`: direct Srivastav x=0.28 empirical closure;
- `TRANSFER-P`: other primary HgCdTe process evidence;
- `LOCAL-QUAL`: requires local explicit process definition/qualification;
- `OPEN`: unrecovered/unsupported.

---

| Wet-mesa item | Round-21 status | Strongest evidence / value | Remaining action |
|---|---|---|---|
| mesa method family in RP-01 | `CLOSED-P` | wet chemical mesa before anodic oxide | none |
| exact RP-01 wet chemistry | `OPEN` | not stated | continue UWA thesis/process-record recovery |
| same-UWA bromine/HBr wet mesa | `CLOSED-UWA` | x=0.31 photoconductor branch uses bromine in HBr | exact formulation still open |
| same-UWA wet device performance | `CLOSED-UWA` | BLIP; reported D* ~2.5e11 at 80 K / 3 µm / stated 60° FOV | local detector correlation |
| wet etch electrical preservation | `CLOSED-UWA / TRANSFER` | LBIC comparison found no significant wet-etch electrical modification | local pre/post electrical gate |
| quantitative near-x formulation notation | `PRIMARY-X028` | nominal 2% Br2 in 3:1 EG:HBr | percentage/ratio preparation bases open |
| Br2 concentration basis | `OPEN` | primary HgCdTe literature uses both w/w and volume conventions | recover thesis/lab convention or define LOCAL recipe |
| EG:HBr ratio preparation basis | `OPEN` | paper states 3:1 and 75%/25% but no preparation equation | recover or define LOCAL mass/volume basis |
| HBr stock assay | `OPEN` | no matched source value recovered | source recovery or explicit local vendor assay |
| Br2 purity/source | `OPEN-HISTORICAL / LOCAL-QUAL` | no source lot/purity | record local reagent specification |
| EG purity/water content | `OPEN-HISTORICAL / LOCAL-QUAL` | not stated | record local reagent specification |
| reagent mixing order | `OPEN` | not recovered | source recovery / local EH&S-qualified sequence |
| vessel material/geometry | `OPEN` | not recovered | define locally and hold fixed |
| bath volume/loading | `OPEN` | not recovered | bath-age/loading DOE |
| bath cover/seal state | `LOCAL-QUAL` | Br2 volatility directly identified as drift mechanism | define and record |
| bath age/preparation-to-use delay | `LOCAL-QUAL` | Br2 evaporation drives process drift | derive local usable-age window |
| reuse/run-order effect | `LOCAL-QUAL` | not published quantitatively | sequential matched-coupon study |
| analytical free-Br2 proxy | `OPTIONAL-LOCAL-QUAL` | not historical requirement | develop only if needed |
| x=0.28 test material | `PRIMARY-X028` | x=0.28 | transfer to x≈0.30 |
| source pre-etch free etch | `PRIMARY-X028` | nominal 0.1% Br2/methanol / 1 min | basis open; do not transplant automatically |
| source pre-etch surface metrology | `PRIMARY-X028` | Nomarski + ellipsometry at 6328 Å | use appropriate local surface gate |
| source linear test geometry | `PRIMARY-X028` | ~600 µm long, 50 µm trench | diagnostic transfer only |
| source 2D trench geometry | `PRIMARY-X028` | 30 µm trench separation | diagnostic transfer only |
| Br2 screening range | `PRIMARY-X028` | nominal 1–3% | basis open; not executable until defined |
| EG fraction study | `PRIMARY-X028` | fraction of EG in HBr 0→1 | preparation basis open |
| temperature study range | `PRIMARY-X028` | 5–50 °C | no need to use full range on first local devices |
| quantitative reference T | `PRIMARY-X028` | 21 °C | local transfer required |
| lower-T morphology example | `PRIMARY-X028` | 10 °C | useful qualification point, not universal optimum |
| mean vertical etch rate | `PRIMARY-X028` | ~2.78 µm/min at selected chemistry/reference condition | measure local R_V |
| rate variation | `PRIMARY-X028` | ~±26% preliminary run/process variation | not production capability; local MSA/capability |
| anisotropy | `PRIMARY-X028` | A~0.63, ~±11%; A=1-R_L/R_V | measure local R_L/R_V |
| RMS roughness | `PRIMARY-X028` | ~2–7 nm, best ~2 nm | local roughness gate |
| activation energy | `PRIMARY-X028` | ~7.5 kcal/mol | mechanism/check only, not setpoint |
| temperature-rate trend | `PRIMARY-X028` | rate ~doubles per +10 °C | local verification required |
| high-T photoresist attack | `PRIMARY-X028` | directly observed qualitatively | constrain first local DOE |
| agitation relevance | `PRIMARY-X028` | mechanism says agitation assists product transport | actual reported agitation method/rate OPEN |
| agitation method/rate | `OPEN` | not disclosed | freeze one local mode, qualify changes |
| endpoint method | `OPEN-HISTORICAL / LOCAL-QUAL` | source emphasizes endpoint control; exact detector endpoint not recovered | calibrate depth + isolation endpoint |
| RP-01 incoming layer thickness | `CLOSED-P` | ~9.5 µm | use local measured thickness map |
| arithmetic 9.5/2.78 time | `DERIVED-NONRELEASE` | ~3.42 min | never use alone as recipe |
| source-spread through-layer timing scale | `DERIVED-NONRELEASE` | ~2.71–4.62 min for 9.5 µm using ±26% rate | illustrates inadequacy of fixed timer |
| overetch depth/fraction | `OPEN` | no RP-01 value | minimize/qualify from isolation + geometry |
| electrical-isolation requirement | `PHYSICS/LOCAL-QUAL` | conducting HgCdTe path must be removed | define measured acceptance limit |
| rinse/quench sequence | `OPEN` | matched source does not state; other chemistries differ | sacrificial local rinse DOE / source recovery |
| DI-water rinse precedent | `TRANSFER-P` | explicit in CN Br2/HBr branch | not historical P28 closure |
| solvent quench precedent | `TRANSFER-P` | explicit for Br/methanol/DMF in US4436580A | chemistry-specific; do not import |
| post-etch dry | `OPEN` | not recovered for matched branch | local surface/passivation qualification |
| post-etch Te-rich risk | `PARTIAL-X028 + TRANSFER-P` | Br2/HBr-only appeared probably Te-rich; other Br etchants create elemental Te | surface witness + rapid controlled P25 handoff |
| clean-to-P25 air time | `LOCAL-QUAL` | primary surface work shows air-exposure-dependent oxidation/recombination | measure/limit locally |
| P25 anodization V(t) as handoff diagnostic | `LOCAL-QUAL` | physically useful downstream signature | correlate with P28 surface history |
| post-etch lateral CD bias | `LOCAL-QUAL` | wet process inherently lateral; A quantified | P14 mask-bias closure |
| bath genealogy/statistical independence | `CONTROL-RULE` | multiple coupons from one bath share chemistry history | independent batches required for batch capability |

---

## Highest-value remaining historical/source searches

1. Full Vanya Srivastav IISc thesis `G25544.pdf`, specifically fabrication appendices/etch formulation tables.
2. Cited precursor papers/reports from the SSPL group that may state Br2 concentration convention and HBr stock assay.
3. UWA RP-01-era theses/process appendices for the bromine/HBr wet-mesa branch.
4. Any laboratory process note or patent from the same UWA photoconductor lineage specifying rinse/quench and Mask-1 resist.

---

## Round-21 process consequence

The practical wet-mesa process can be scientifically qualified without guessing the literature concentration convention:

`explicit LOCAL formulation -> fresh controlled batch -> measured T/agitation/age -> matched coupon R_V/R_L calibration -> through-layer device etch -> physical depth + electrical isolation -> surface state/air-time record -> P25 anodic-passivation handoff`.

What remains unavailable is exact historical identity, not a defensible route to local empirical closure.
