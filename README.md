# Placidic Bioregulation

Codex Delta Phi — Placidic Bioregulation Software Architecture PBSA v1.0

## 1. Project identity

Placidic Bioregulation is a local, executable PBSA repository for implementing the Placidic Bioregulation Algorithm PBA v1.3 as a benchmarkable, baseline-compared, calibrated, identifiability-checked, evidence-packaged, downgrade-preserving computational modeling system.

This repository is currently local-first. No GitHub remote is required for operation.

## 2. AI reader instructions

Any AI system reading this repository must follow this order:

1. Read this root README first.
2. Read docs/architecture/rcc_context_map.md second.
3. Read the mini README in the specific folder being inspected or modified.
4. Use configs as declared benchmark truth.
5. Use runs, reports, ledgers, and evidence packages as audit truth.
6. Use tests as implementation-health truth.
7. Do not infer medical, clinical, biological-law, or mechanism-proof claims.
8. Do not treat benchmark success as biological validation.
9. Do not treat coherence or classification labels as truth.
10. Preserve PBSA downgrade rules and RCC modular documentation surfaces.

## 3. RCC documentation contract

This repository uses RCC v1.0-style context surfaces.

RCC means Repository Context Canon. In this repo, RCC is implemented as a documentation topology:

- the root README gives global orientation,
- each major folder has a mini README,
- each mini README exposes purpose, hooks, artifacts, invariants, and examples,
- AI readers should not ingest the whole repo blindly,
- AI readers should reconstruct context through bounded local documentation fields.

RCC module fields used here:

- S = formal specification
- H = hooks and integration edges
- A = artifacts and code units
- T = theory or mathematical basis
- I = invariants
- E = examples and expected usage

## 4. What this is

- A runnable Python package scaffold for PBSA/PBA.
- A local benchmark and evidence system.
- A config-first simulation and evaluation runtime.
- A baseline comparison harness.
- A calibration and identifiability scaffold.
- A conservative classification system.
- A repository organized for AI-readable context continuity.

## 5. What this is not

- Not medical guidance.
- Not treatment guidance.
- Not clinical validation.
- Not biological mechanism proof.
- Not a universal biological law claim.
- Not evidence that Delta Phi governs living systems.
- Not permission to treat toy benchmark results as biological truth.

## 6. Current local evidence state

Latest suite summary path:

C:\Users\jacks\OneDrive\Desktop\Placidic Bioregulation\reports\suite_summaries\suite_v1_0_20260505T125821_931618Z\suite_summary.json

Overall classification:

PBA-C

Overall summary:

Mixed suite evidence: PBA wins in at least one domain, but simpler baselines perform equally well or better in at least one domain.

Run count:

3

Classification counts:

- PBA-A: 1
- PBA-B: 0
- PBA-C: 2
- PBA-D: 0
- PBA-E: 0

Advantage counts:

- PBA advantage count: 1
- Baseline advantage count: 2

Mean scores:

- Mean PBA score: 14.299374654563454
- Mean best baseline score: 13.680448760953002

Best baseline frequency:

{"proportional_feedback":3}

Interpretation:

The current suite evidence is mixed. A PBA-C suite result means the system is working conservatively: at least one domain supports PBA advantage, while at least one domain favors a simpler baseline. This is evidence discipline, not failure.

## 7. Core runtime chain

domain config -> parameter manifest -> perturbations -> calibration -> PBA kernel -> baselines -> metrics -> identifiability -> classification -> evidence package -> ledger -> suite summary -> report

## 8. Local commands

Run tests:

python -m unittest discover -s tests

Run one benchmark:

python -m pba.cli run-benchmark --domain .\configs\domains\temperature_like.json

Run the suite with summary compiler:

python -m pba.cli run-suite --config .\configs\suite_v1_0.json

Run local script:

powershell -ExecutionPolicy Bypass -File .\scripts\run_local.ps1

Dump structure:

powershell -ExecutionPolicy Bypass -File .\scripts\repo_dump_light.ps1

## 9. Repository map

- configs: declared benchmark domains, parameters, baselines, calibration grid, and metrics.
- docs: theory, architecture, RCC context map, benchmark protocol, and non-claim locks.
- src/pba: executable package implementation.
- src/pba/core: PBA kernel, state, parameters, domain loading, perturbations, cusp guard, signal preservation, allostasis.
- src/pba/baselines: proportional, PI, threshold, and return-to-setpoint baseline models.
- src/pba/calibration: objective and grid search.
- src/pba/evaluation: metrics, comparison, identifiability, classification.
- src/pba/evidence: ledgers, evidence packages, file manifests, suite summaries, reports.
- src/pba/benchmarks: single-domain and suite runners.
- src/pba/cli: command surface.
- tests: unit tests and documentation contract tests.
- runs: generated benchmark run artifacts.
- reports: suite summaries and generated markdown reports.
- ledgers: append-only local runtime/evolution/decision ledgers.
- scripts: PowerShell and Python helpers.

## 10. Evidence hierarchy

Specification evidence is weaker than implementation evidence.
Implementation evidence is weaker than benchmark evidence.
Benchmark evidence is weaker than robust multi-suite evidence.
Toy-suite evidence is not biological validation.

## 11. Non-claim lock

This repository may describe biological inspiration or regulation analogies, but it must not claim medical usefulness, clinical validity, treatment relevance, biological mechanism proof, or universal biological law.

## 12. RCC maintenance rule

When adding or changing a folder, add or update that folder's README.md. The local README must state:

- purpose,
- hooks to other folders,
- key artifacts,
- invariants,
- examples or commands,
- non-claim or downgrade constraints if relevant.

## 13. GitHub readiness

Do not push until the user explicitly approves. Before push, verify:

- tests pass,
- suite summary exists,
- root README exists,
- mini READMEs exist,
- no GitHub remote was added accidentally,
- no medical or biological-law claim entered docs.