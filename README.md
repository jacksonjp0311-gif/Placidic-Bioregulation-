# Placidic Bioregulation

Codex Delta Phi - Placidic Bioregulation Software Architecture PBSA v2.0

Local-first executable research repository for the Placidic Bioregulation Algorithm PBA v1.4.

Status: GitHub-published research repository  
GitHub remote: https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-  
Package version: 1.0.0  
Current software architecture: PBSA v2.0 - Holdout Domain Expansion and Candidate Readiness  
Current theory layer: PBA v1.4 - Evidence Feedback and Regime-Aware Placidity  
Current decision: preserve_champion  
Original suite classification: PBA-C  
Holdout suite classification: PBA-D  
Current tests: 44 passing  
Candidate execution: comparison harness only  
Kernel mutation: disabled  
Next target: PBSA v2.1 - Routed-Suite Validation  

---

## Version ledger

| Layer | Current version | Repository status |
|---|---:|---|
| Software architecture | PBSA v2.0 | implemented and pushed |
| Algorithm theory | PBA v1.4 | documented in docs/theory |
| Python package | 1.0.0 | active |
| Test suite | 44 passing | active |
| Original suite classification | PBA-C | active |
| Holdout suite classification | PBA-D | active |
| Evolution decision | preserve_champion | active |
| Candidate execution | disabled | active |
| Kernel mutation | disabled | active |
| RCC documentation contract | passing | active |
| Next planned layer | PBSA v2.1 | routed-suite validation |

## Current architecture status

PBSA v2.0 is a holdout-expansion and candidate-readiness layer. It builds on PBSA v1.2 multi-label regime detection by adding holdout domains, a holdout suite, holdout summaries, regime coverage reporting, candidate specifications, and candidate-readiness reporting.

PBSA v2.0 does not replace the PBA kernel. Candidate specs are plans, not executable controllers. The current champion kernel remains preserved until a future candidate passes original-suite comparison, holdout-suite comparison, baseline comparison, evolution reporting, decision-ledger checks, non-claim lock verification, and RCC documentation checks.

---

# PART I - Human README

## Executive summary

Placidic Bioregulation is a runnable Python research scaffold that implements PBSA v2.0: a conservative evidence-producing architecture for testing a bounded regulation algorithm against simpler baselines under declared toy benchmark conditions.

The repository is designed to be honest before it is impressive. It runs tests, executes benchmark domains, compares PBA against baseline controllers, emits metrics, checks identifiability, classifies runs, aggregates suite-level evidence, runs holdout evaluation, generates candidate-readiness reports, and preserves non-claim boundaries.

## Current finding

The current evidence state is mixed and conservative.

Original suite:

- Overall classification: PBA-C
- PBA wins in one declared toy domain.
- A simpler proportional baseline performs better in two declared domains.

Holdout suite:

- Overall classification: PBA-D
- The holdout run broadened the evidence surface and showed weak generalization.
- This supports candidate readiness, not candidate promotion.

Current conclusion:

The system is working because it downgraded itself. PBSA did not hide baseline wins, did not promote the kernel, and did not inflate holdout evidence. The correct current decision remains preserve_champion.

## Current benchmark results

Original suite summary:

- Latest known original suite folder: reports/suite_summaries/suite_v1_0_20260505T130602_845599Z
- Run count: 3
- PBA-A: 1
- PBA-B: 0
- PBA-C: 2
- PBA-D: 0
- PBA-E: 0
- PBA advantage count: 1
- Baseline advantage count: 2
- Best baseline frequency: proportional_feedback in 3/3 domains

Original suite domain-level result table:

| Domain | Classification | Result | PBA score | Best baseline | Best baseline score | Identifiability |
|---|---:|---|---:|---|---:|---|
| temperature_like | PBA-C | baseline_advantage | 14.102427430425653 | proportional_feedback | 12.098345439576836 | stable |
| pulse_recovery | PBA-C | baseline_advantage | 12.891225613932782 | proportional_feedback | 9.86217943228449 | stable |
| oscillatory_signal | PBA-A | pba_advantage | 15.904470919331928 | proportional_feedback | 19.08082141099768 | stable |

Holdout suite:

- Suite config: configs/suite_holdout_v1_3.json
- Latest holdout summary: reports/holdout/latest_holdout_summary.json
- Latest candidate-readiness report: reports/candidates/latest_candidate_readiness_report.json
- Holdout run count: 4
- Holdout overall classification: PBA-D
- Candidate spec count: 4
- Candidate execution allowed: false
- Kernel mutation allowed: false

Candidate specs generated:

- direct_route_candidate_v0
- pulse_route_candidate_v0
- oscillatory_preservation_candidate_v0
- noisy_recovery_guard_candidate_v0

## How to interpret the current result

A PBA-C original-suite result and PBA-D holdout result are not crashes. They mean the evidence system is doing its job.

The correct interpretation is:

- PBSA implementation is working.
- Tests are passing.
- Evidence generation is working.
- Original-suite downgrade is preserved.
- Holdout evaluation found weak generalization.
- Candidate specs are justified as next-step plans.
- Candidate execution is not yet justified.
- Stronger claims are not justified.
- The next valid step is champion/challenger execution under PBSA v2.0.

## What this project is

- A local executable PBSA/PBA research repository.
- A benchmarkable Python package.
- A baseline-comparison system.
- A calibration and identifiability scaffold.
- A suite-level evidence aggregator.
- A holdout evaluation layer.
- A candidate-readiness layer.
- A repository organized for human and AI readability using RCC-style mini READMEs.

## What this project is not

- Not medical guidance.
- Not treatment guidance.
- Not clinical validation.
- Not biological mechanism proof.
- Not a universal biological law claim.
- Not proof that Delta Phi governs living systems.
- Not permission to treat toy benchmark results as biological evidence.
- Not permission to promote candidate specs into active controllers.
- Do not treat benchmark success as biological validation.

## Quick start

From the repository root:

    cd "C:\Users\jacks\OneDrive\Desktop\Placidic Bioregulation"

Run tests:

    python -m unittest discover -s tests

Run one benchmark:

    python -m pba.cli run-benchmark --domain .\configs\domains\temperature_like.json

Run the original suite:

    python -m pba.cli run-suite --config .\configs\suite_v1_0.json

Run the holdout suite:

    python -m pba.cli run-suite --config .\configs\suite_holdout_v1_3.json

Generate holdout summary:

    python -m pba.cli summarize-holdout

Generate candidate-readiness report:

    python -m pba.cli candidate-readiness

Generate evolution report:

    python -m pba.cli diagnose-evolution

Run the local automation script:

    powershell -ExecutionPolicy Bypass -File .\scripts\run_local.ps1

Dump the repo structure:

    powershell -ExecutionPolicy Bypass -File .\scripts\repo_dump_light.ps1

## Repository map for humans

- configs: declared suite, domains, holdout domains, parameters, baseline settings, calibration grid, and metrics.
- docs: theory, architecture, RCC context map, and benchmark protocol.
- src/pba: Python implementation.
- tests: unit tests and RCC README coverage checks.
- runs: generated benchmark run artifacts.
- reports: generated suite summaries, holdout summaries, candidate-readiness reports, and evolution reports.
- ledgers: local runtime and decision continuity records.
- scripts: local helper scripts.

## Release and GitHub status

This repository has been published to GitHub.

Remote:

    https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-

Current published status:

- PBSA v2.0 holdout and candidate-readiness layer added.
- PBA v1.4 theory/governance docs archived.
- Package version: 1.0.0.
- 27 tests passing.
- Original suite classification: PBA-C.
- Holdout suite classification: PBA-D.
- Latest holdout summary generated.
- Latest candidate-readiness report generated.
- Candidate spec count: 4.
- Current decision: preserve_champion.
- Candidate execution: comparison harness only.
- Kernel replacement: disabled by default.
- Next target: PBSA v2.0 champion/challenger execution and promotion governance.

Before future pushes, verify:

- tests pass,
- original suite summary exists,
- holdout summary exists if holdout behavior changed,
- candidate-readiness report exists if candidate semantics changed,
- evolution report exists if diagnostic semantics changed,
- root README is current,
- mini READMEs exist,
- docs/theory and docs/architecture reflect current versioning,
- no medical or biological-law claim entered the docs.

---

# PART II - AI / Agent README

## AI version tracking contract

Current canonical versions:

- PBSA_VERSION: PBSA-v1.3
- PBA_VERSION: PBA-v1.4
- package version: 0.4.0
- current decision: preserve_champion
- original suite classification: PBA-C
- holdout suite classification: PBA-D
- current tests: 27 passing
- candidate execution allowed: comparison harness only
- kernel mutation allowed: false
- current docs archive: docs/theory and docs/architecture
- next target: PBSA v2.1 routed-suite validation

AI agents must update this README when version constants, suite evidence, holdout evidence, candidate-readiness reports, docs/theory, docs/architecture, or evolution reports change.

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
- holdout summary when holdout behavior is discussed,
- candidate-readiness report when candidate behavior is discussed,
- non-claim boundary.

## Canonical runtime chain

domain config -> parameter manifest -> perturbations -> calibration -> PBA kernel -> baselines -> metrics -> identifiability -> classification -> evidence package -> ledger -> suite summary -> report

## PBSA v2.0 holdout/candidate chain

holdout domain config -> holdout suite -> holdout runs -> holdout summary -> regime coverage matrix -> candidate specs -> candidate-readiness report -> preserve_champion

## AI file routing guide

Use this routing map before editing:

- Modify configs only when changing declared benchmark conditions.
- Modify src/pba/core only when changing PBA runtime primitives.
- Modify src/pba/baselines only when changing comparators.
- Modify src/pba/calibration only when changing parameter search.
- Modify src/pba/evaluation only when changing metrics, identifiability, classification, or regime diagnostics.
- Modify src/pba/evidence only when changing evidence package, reports, manifests, suite summaries, or holdout summaries.
- Modify src/pba/evolution only when changing candidate specs, candidate readiness, champion/challenger logic, or promotion governance.
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
- proof from toy benchmarks alone,
- proof from holdout performance alone,
- proof from candidate readiness alone.

## AI interpretation of current evidence

Current original-suite classification:

PBA-C

Current holdout-suite classification:

PBA-D

Current evidence conclusion:

The current repository is functioning as a conservative research scaffold. PBA shows local advantage in one original-suite domain, loses to a simple proportional baseline in two original-suite domains, and does not yet generalize strongly under the v1.3 holdout suite. This supports candidate-readiness planning, not candidate execution or kernel promotion.

AI agents must preserve this interpretation unless newer generated JSON artifacts exist and are explicitly used to update this README.

## AI modification rules

Before modifying code:

1. Identify the target folder.
2. Read that folder's README.
3. Locate tests covering the behavior.
4. Patch the smallest necessary surface.
5. Run tests.
6. Run original suite if original benchmark behavior changed.
7. Run holdout suite if holdout behavior changed.
8. Generate holdout summary if holdout suite changed.
9. Generate candidate-readiness report if candidate semantics changed.
10. Update README evidence section only from generated JSON.
11. Commit locally only unless push is explicitly requested.

## Required local verification

After any meaningful patch, run:

    python -m unittest discover -s tests

If original benchmark behavior changed, also run:

    python -m pba.cli run-suite --config .\configs\suite_v1_0.json

If holdout behavior changed, also run:

    python -m pba.cli run-suite --config .\configs\suite_holdout_v1_3.json
    python -m pba.cli summarize-holdout
    python -m pba.cli candidate-readiness

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

This repository is built to downgrade itself. Do not optimize documentation to sound stronger than the evidence. The correct behavior is to preserve mixed results, baseline wins, failure surfaces, holdout weakness, candidate restrictions, and non-claim boundaries.

---

# Version history notes

## PBSA v1.1 Diagnostic Evidence Feedback Upgrade

Added regime detection, baseline advantage mapping, evolution policy, evolution reports, champion/challenger scaffolding, and RCC-aware continuity updates.

Important lock: PBSA v1.1 did not automatically replace the current PBA kernel.

## PBSA v1.2 Multi-Label Regime Detection Upgrade

Added primary_regime, secondary_regimes, risk_overlays, regime_scores, evidence_notes, PBSA-v1.2 report rendering, docs archive, implementation map, and RCC synchronization.

Important lock: PBSA v1.2 improved diagnosis only.

## PBSA v1.2.1 RCC Version Drift Cleanup

Cleaned stale PBSA v1.1 labels from PBSA v1.2 configuration and evolution surfaces.

Important lock: no kernel mutation occurred.

## PBSA v2.0 Holdout and Candidate Readiness Upgrade

Added four holdout domain configs, suite_holdout_v1_3.json, holdout summary generation, regime coverage matrix, candidate specification schema, candidate-readiness report, CLI commands for holdout/readiness, docs archive, implementation map, and RCC mini README synchronization.

Important lock: PBSA v2.0 broadens evidence only. Candidate specs are not executable controllers. Candidate execution is allowed only inside comparison harnesses.

Next target: PBSA v2.0 champion/challenger execution and promotion governance.

## PBSA v2.0 Champion/Challenger Governance Upgrade

This repository now includes the PBSA v2.0 champion/challenger execution layer.

Added surfaces:
- candidate route configs
- executable comparison-harness challenger variants
- champion/challenger runner
- promotion governance taxonomy
- champion/challenger report generator
- CLI command for champion/challenger reporting
- docs/theory PBSA v2.0 archive
- docs/architecture PBSA v2.0 implementation map
- RCC mini README synchronization

Important lock:
- Candidate execution is not promotion.
- Candidate execution is allowed only inside comparison harnesses.
- Automatic kernel replacement remains disabled.
- The current PBA kernel is not automatically replaced.
- Candidate improvement is not biological proof or medical validation.

Command:
    python -m pba.cli champion-challenger-report

Next target:
- PBSA v2.0 regime-routed PBSA or manual review


## PBSA v2.0 Regime-Routed PBSA Upgrade

This repository now includes the PBSA v2.0 regime-routing layer.

Added surfaces:
- routing policy config
- route registry
- route selector
- route eligibility gates
- routed runner
- route evidence packages
- routed suite report
- CLI command for routed suite reports
- docs/theory PBSA v2.0 archive
- docs/architecture PBSA v2.0 implementation map
- RCC mini README synchronization

Important lock:
- Routing is not biological validation.
- Routing is not global kernel replacement.
- Baseline routes remain valid when evidence supports them.
- Champion routes remain valid when evidence supports them.
- Candidate routes remain governed and review-bound.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.

Command:
    python -m pba.cli routed-suite-report

Next target:
- PBSA v2.1 routed-suite validation
