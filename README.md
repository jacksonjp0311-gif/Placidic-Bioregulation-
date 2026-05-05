# Placidic Bioregulation

Codex Delta Phi - Placidic Bioregulation Software Architecture PBSA v1.2

Local-first executable research repository for the Placidic Bioregulation Algorithm PBA v1.4.

Status: GitHub-published research repository
GitHub remote: https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-
GitHub push: performed
Package version: 0.3.0
Current software architecture: PBSA v1.2 - Multi-Label Regime Detection and RCC Synchronization
Current theory layer: PBA v1.4 - Evidence Feedback and Regime-Aware Placidity
Current decision: preserve_champion
Current suite classification: PBA-C
Current tests: 21 passing
Next target: PBSA v1.3 - Holdout Domain Expansion and Candidate Evaluation Readiness

---

## Version ledger

| Layer | Current version | Repository status |
|---|---:|---|
| Software architecture | PBSA v1.2 | implemented and pushed |
| Algorithm theory | PBA v1.4 | documented in docs/theory |
| Python package | 0.3.0 | active |
| Test suite | 21 passing | active |
| Evolution decision | preserve_champion | active |
| Overall suite classification | PBA-C | active |
| RCC documentation contract | passing | active |
| Next planned layer | PBSA v1.3 | holdout domain expansion and candidate evaluation readiness |

## Current architecture status

PBSA v1.1 is a diagnostic-first evidence-feedback layer. It adds regime detection, baseline advantage mapping, evolution policy, evolution reports, and champion/challenger scaffolding. It does not automatically replace the current PBA kernel.

The current champion kernel remains preserved until a future candidate passes tests, suite comparison, baseline comparison, evolution reporting, decision ledger checks, non-claim lock verification, and holdout or repeat-suite evidence where available.

# PART I - Human README

## Executive summary

Placidic Bioregulation is a runnable Python research scaffold that implements PBSA v1.1: a diagnostic evidence-feedback software architecture for testing a bounded regulation algorithm against simpler baselines under declared toy benchmark conditions, preserving RCC context surfaces, and generating evolution reports without automatically replacing the champion kernel.

The repository is designed to be honest before it is impressive. It runs tests, executes benchmark domains, compares PBA against baseline controllers, emits metrics, checks identifiability, classifies each run, aggregates suite-level evidence, and preserves non-claim boundaries.

## Current finding

Latest overall suite classification:

PBA-C

Latest conclusion:

The current suite result is honest mixed evidence. PBA wins in at least one declared toy domain, but a simpler proportional baseline performs better in at least one declared domain. This supports local implementation usefulness under specific perturbation geometry, not broad biological or medical claims.

Suite summary:

Mixed suite evidence: PBA wins in at least one domain, but simpler baselines perform equally well or better in at least one domain.

## Current benchmark results

Latest suite summary files:

- JSON: C:\Users\jacks\OneDrive\Desktop\Placidic Bioregulation\reports\suite_summaries\suite_v1_0_20260505T130602_845599Z\suite_summary.json
- Markdown: C:\Users\jacks\OneDrive\Desktop\Placidic Bioregulation\reports\suite_summaries\suite_v1_0_20260505T130602_845599Z\suite_summary.md
- Folder: C:\Users\jacks\OneDrive\Desktop\Placidic Bioregulation\reports\suite_summaries\suite_v1_0_20260505T130602_845599Z

Benchmark artifact locations:

- Individual benchmark runs: runs
- Suite summaries: reports/suite_summaries
- Runtime ledgers: ledgers
- Evidence package per run: runs/run_*/evidence_package.json
- Per-run classification: runs/run_*/classification.json
- Per-run metric comparison: runs/run_*/metric_comparison.json
- Per-run benchmark summary: runs/run_*/benchmark_summary.md

Current suite counts:

- Run count: 3
- PBA-A: 1
- PBA-B: 0
- PBA-C: 2
- PBA-D: 0
- PBA-E: 0

Advantage counts:

- PBA advantage count: 1
- Baseline advantage count: 2
- Tie count: 0

Mean scores:

- Mean PBA score: 14.299374654563454
- Mean best baseline score: 13.680448760953002

Best baseline frequency:

{"proportional_feedback":3}

Domain-level result table:

| Domain | Classification | Result | PBA score | Best baseline | Best baseline score | Identifiability |
|---|---:|---|---:|---|---:|---|
| temperature_like | PBA-C | baseline_advantage | 14.102427430425653 | proportional_feedback | 12.098345439576836 | stable |
| pulse_recovery | PBA-C | baseline_advantage | 12.891225613932782 | proportional_feedback | 9.86217943228449 | stable |
| oscillatory_signal | PBA-A | pba_advantage | 15.904470919331928 | proportional_feedback | 19.08082141099768 | stable |

## How to interpret the current result

A PBA-C suite result is not a crash and not a failure of the framework. It means the evidence system is working conservatively.

In the current evidence state, PBA shows advantage in one declared domain, while a simpler proportional feedback baseline performs better in two declared domains. That means the current PBA kernel is not universally superior across the toy suite. The correct conclusion is bounded:

- PBSA implementation is working.
- Evidence generation is working.
- The downgrade system is working.
- PBA has local advantage in a specific perturbation geometry.
- Simpler baselines remain stronger in other declared geometries.
- Further kernel tuning or domain-specific calibration is required before stronger claims.

## What this project is

- A local executable PBSA/PBA research repository.
- A benchmarkable Python package.
- A baseline-comparison system.
- A calibration and identifiability scaffold.
- A suite-level evidence aggregator.
- A repository organized for human and AI readability using RCC-style mini READMEs.

## What this project is not

- Not medical guidance.
- Not treatment guidance.
- Not clinical validation.
- Not biological mechanism proof.
- Not a universal biological law claim.
- Not proof that Delta Phi governs living systems.
- Not permission to treat toy benchmark results as biological evidence.
- Do not treat benchmark success as biological validation.

## Quick start

From the repository root:

    cd "C:\Users\jacks\OneDrive\Desktop\Placidic Bioregulation"

Run tests:

    python -m unittest discover -s tests

Run one benchmark:

    python -m pba.cli run-benchmark --domain .\configs\domains\temperature_like.json

Run the full suite:

    python -m pba.cli run-suite --config .\configs\suite_v1_0.json

Run the local automation script:

    powershell -ExecutionPolicy Bypass -File .\scripts\run_local.ps1

Dump the repo structure:

    powershell -ExecutionPolicy Bypass -File .\scripts\repo_dump_light.ps1

## Repository map for humans

- configs: declared suite, domains, parameters, baseline settings, calibration grid, and metrics.
- docs: theory, architecture, RCC context map, and benchmark protocol.
- src/pba: Python implementation.
- tests: unit tests and RCC README coverage checks.
- runs: generated benchmark run artifacts.
- reports: generated suite summaries.
- ledgers: local runtime and decision continuity records.
- scripts: local helper scripts.

## Release and GitHub status

This repository has been published to GitHub.

Remote:

    https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-

Current published status:

- PBSA v1.1 diagnostic evidence-feedback layer added.
- PBA v1.4 theory/governance docs archived.
- 18 tests passing.
- Latest evolution report generated.
- Current decision: preserve_champion.
- Overall suite classification: PBA-C.
- Kernel replacement: disabled by default.
- Next target: PBSA v1.2 multi-label regime detection.

Before future pushes, verify:

- tests pass,
- suite summary exists,
- evolution report exists if diagnostics changed,
- root README is current,
- mini READMEs exist,
- docs/theory and docs/architecture reflect current versioning,
- no medical or biological-law claim entered the docs.

---

# PART II - AI / Agent README

## AI version tracking contract

Current canonical versions:

- PBSA_VERSION: PBSA-v1.2
- PBA_VERSION: PBA-v1.4
- package version: 0.3.0
- current decision: preserve_champion
- current suite classification: PBA-C
- current tests: 21 passing
- current docs archive: docs/theory and docs/architecture
- next target: PBSA v1.3 holdout domain expansion and candidate evaluation readiness

AI agents must update this README when version constants, suite evidence, docs/theory, docs/architecture, or evolution reports change.

## AI operating contract

Any AI agent reading or modifying this repository must follow this order:

1. Read this root README first.
2. Read docs/architecture/rcc_context_map.md second.
3. Read the mini README in the target folder.
4. Inspect only the relevant source, config, test, run, or report files.
5. Use configs as benchmark declaration truth.
6. Use tests as implementation health truth.
7. Use runs and reports as evidence truth.
8. Use ledgers as continuity truth.
9. Preserve PBSA downgrade rules.
10. Preserve RCC mini README surfaces.

## RCC documentation contract

This repository uses RCC-style context surfaces.

RCC means Repository Context Canon. In this repository, RCC is implemented as a documentation topology where every major folder has a mini README that exposes local purpose, hooks, artifacts, invariants, and examples.

RCC module fields:

- S = formal specification
- H = hooks and integration edges
- A = artifacts and code units
- T = theory or mathematical basis
- I = invariants
- E = examples and expected usage

AI agents must not blindly ingest the whole repository. They should reconstruct repository context through bounded README surfaces first.

## PBSA evidence contract

PBSA requires the following before any benchmark interpretation:

- declared domain config,
- declared parameter manifest,
- declared baseline config,
- declared calibration grid,
- declared metric manifest,
- PBA runtime output,
- baseline runtime output,
- calibration record,
- fit/evaluation distinction,
- PBA metrics,
- baseline metrics,
- identifiability report,
- per-run classification,
- evidence package,
- suite summary,
- non-claim boundary.

## Canonical runtime chain

domain config -> parameter manifest -> perturbations -> calibration -> PBA kernel -> baselines -> metrics -> identifiability -> classification -> evidence package -> ledger -> suite summary -> report

## AI file routing guide

Use this routing map before editing:

- Modify configs only when changing declared benchmark conditions.
- Modify src/pba/core only when changing PBA runtime primitives.
- Modify src/pba/baselines only when changing comparators.
- Modify src/pba/calibration only when changing parameter search.
- Modify src/pba/evaluation only when changing metrics, identifiability, or classification.
- Modify src/pba/evidence only when changing evidence package, reports, manifests, or suite summaries.
- Modify src/pba/benchmarks only when changing orchestration.
- Modify src/pba/cli only when changing command-line behavior.
- Modify tests whenever behavior changes.
- Modify folder README whenever folder purpose, hooks, artifacts, or invariants change.

## AI non-claim lock

Never claim or imply:

- medical guidance,
- treatment relevance,
- clinical validation,
- biological mechanism proof,
- universal biological law,
- physical force,
- proof that Delta Phi governs living systems,
- proof from coherence alone,
- proof from toy benchmarks alone.

## AI interpretation of current evidence

Current overall classification:

PBA-C

Current evidence conclusion:

The current suite result is honest mixed evidence. PBA wins in at least one declared toy domain, but a simpler proportional baseline performs better in at least one declared domain. This supports local implementation usefulness under specific perturbation geometry, not broad biological or medical claims.

AI agents must preserve this interpretation unless a newer suite_summary.json exists and is explicitly cited in the README update.

## AI modification rules

Before modifying code:

1. Identify the target folder.
2. Read that folder's README.
3. Locate tests covering the behavior.
4. Patch the smallest necessary surface.
5. Run tests.
6. Run suite if benchmark behavior changed.
7. Update suite summary if suite changed.
8. Update README evidence section only from generated JSON.
9. Commit locally only unless push is explicitly requested.

## Required local verification

After any meaningful patch, run:

    python -m unittest discover -s tests

If benchmark behavior changed, also run:

    python -m pba.cli run-suite --config .\configs\suite_v1_0.json

## README maintenance rule

When adding a new major folder, create a mini README with:

- Purpose
- S - Formal specification
- H - Hooks
- A - Artifacts
- T - Theory
- I - Invariants
- E - Example

Update tests/test_rcc_readmes.py so the documentation contract remains executable.

## Final AI warning

This repository is built to downgrade itself. Do not optimize documentation to sound stronger than the evidence. The correct behavior is to preserve mixed results, baseline wins, failure surfaces, and non-claim boundaries.

## PBSA v1.1 Diagnostic Evidence Feedback Upgrade

This repository now includes the PBSA v1.1 diagnostic-first evolution layer.

Added surfaces:
- regime detection
- baseline advantage mapping
- evolution policy
- evolution reports
- champion/challenger scaffolding
- RCC-aware continuity updates

Important lock:
- PBSA v1.1 does not automatically replace the current PBA kernel.
- The current kernel remains champion until a candidate passes tests, suite comparison, baseline comparison, evolution reporting, and non-claim lock checks.

Commands:
    python -m pba.cli diagnose-evolution
    python -m pba.cli compare-kernels

## Docs and theory archive

Canonical documentation has been added under docs/theory and docs/architecture.

Important files:

- docs/theory/pba_v1_4_evidence_feedback_regime_aware_placidity.md
- docs/theory/pbsa_v1_1_diagnostic_evidence_feedback_rcc_architecture.md
- docs/architecture/pbsa_v1_1_implementation_map.md
- docs/benchmark_protocol/evolution_acceptance_policy.md

Current PBSA v1.1 status:

- tests: 18 passing
- decision: preserve_champion
- overall classification: PBA-C
- kernel replacement: disabled by default
- next target: multi-label regime detection


## PBSA v1.2 Multi-Label Regime Detection Upgrade

This repository now includes the PBSA v1.2 diagnostic refinement layer.

Added surfaces:
- primary_regime
- secondary_regimes
- risk_overlays
- regime_scores
- evidence_notes
- PBSA-v1.2 evolution report rendering
- docs/theory PBSA v1.2 archive
- docs/architecture PBSA v1.2 implementation map
- RCC mini README synchronization

Important lock:
- PBSA v1.2 improves diagnosis only.
- The current PBA kernel remains champion.
- Kernel mutation remains disabled by default.
- Better regime labels are not biological proof or medical validation.

Expected current interpretation:
- temperature_like -> direct_recovery + cusp_risk + baseline_advantage
- pulse_recovery -> pulse_recovery + cusp_risk + baseline_advantage
- oscillatory_signal -> oscillatory + cusp_risk + pba_advantage

Next target:
- PBSA v1.3 holdout domain expansion and candidate evaluation readiness

## PBSA v1.2.1 RCC Version Drift Cleanup

This maintenance pass cleaned stale PBSA v1.1 labels from PBSA v1.2 configuration and evolution surfaces.

Updated:
- configs/evolution_policy.json
- configs/suite_holdout_v1_0.json
- src/pba/evolution/README.md
- src/pba/evolution/kernel_candidate.py
- latest evolution report after regeneration

No kernel mutation occurred. Current decision remains preserve_champion.
