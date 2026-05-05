# Placidic Bioregulation

Codex Delta Phi - Placidic Bioregulation Software Architecture PBSA v2.0

Local-first executable research repository for the Placidic Bioregulation Algorithm PBA v1.4.

Status: GitHub-published research repository  
GitHub remote: https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-  
Package version: 1.0.0  
Current software architecture: PBSA v2.0 - Regime-Routed PBSA  
Current theory layer: PBA v1.4 - Evidence Feedback and Regime-Aware Placidity  
Current global decision: route_by_regime  
Original suite classification: PBA-C  
Holdout suite classification: PBA-D  
Current tests: 44 passing  
Candidate execution: comparison harness only  
Route execution: enabled through governed routing reports  
Manual review required: true  
Automatic kernel replacement: disabled  
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
| Champion/challenger decision | route_by_regime | active |
| Routed-suite decision | route_by_regime | active |
| Candidate execution | comparison harness only | active |
| Route execution | governed routing report only | active |
| Manual review required | true | active |
| Automatic kernel replacement | disabled | active |
| Kernel mutation | disabled | active |
| RCC documentation contract | passing | active |
| Next planned layer | PBSA v2.1 | routed-suite validation |

## Current architecture status

PBSA v2.0 is a regime-routed architecture. It operationalizes the PBSA v1.4 decision `route_by_regime` by selecting admissible routes from detected regime evidence rather than forcing one universal kernel to win everywhere.

PBSA v2.0 builds on:

- PBSA v1.2 multi-label regime detection,
- PBSA v1.3 holdout and candidate-readiness evidence,
- PBSA v1.4 champion/challenger governance,
- the v1.4 decision `route_by_regime`,
- and the non-claim locks that forbid medical, biological-law, and mechanism-proof overclaiming.

The current architecture selects among governed route families:

- baseline routes,
- champion/PBA routes,
- candidate routes under review,
- reject/insufficient-evidence routes.

PBSA v2.0 does not replace the PBA kernel globally. It does not promote a candidate globally. It routes locally by regime evidence and preserves global evidence, downgrade discipline, RCC surfaces, and non-claim boundaries.

---

# PART I - Human README

## Executive summary

Placidic Bioregulation is a runnable Python research scaffold that now implements PBSA v2.0: a conservative regime-routed architecture for selecting admissible control routes under declared toy benchmark conditions.

The project moved through a full evidence loop:

theory -> executable software -> tests -> benchmark evidence -> downgrade -> multi-label diagnosis -> holdout expansion -> candidate readiness -> champion/challenger comparison -> regime routing.

The important current result is not ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œPBA wins everywhere.ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â The important result is that PBSA learned not to force a single universal controller. The current architecture routes by regime while preserving baseline wins, holdout weakness, candidate restrictions, and non-claim boundaries.

## Current finding

The current evidence state is mixed and conservative.

Original suite:

- Overall classification: PBA-C.
- PBA wins in one declared toy domain.
- A simpler proportional baseline performs better in two declared domains.

Holdout suite:

- Overall classification: PBA-D.
- The holdout run broadened the evidence surface and showed weak generalization.
- This supports routing and validation, not global candidate promotion.

Champion/challenger report:

- Decision: route_by_regime.
- Promotion status: no_automatic_promotion.
- Automatic kernel replacement: false.
- Kernel mutation: false.

Routed suite report:

- Decision: route_by_regime.
- Manual review required: true.
- Automatic kernel replacement: false.
- Kernel mutation: false.
- Next required step: PBSA v2.1 routed-suite validation.

Current conclusion:

The system is working because it did not over-promote itself. PBSA preserved baseline wins, preserved holdout weakness, avoided automatic kernel replacement, and converted `route_by_regime` into executable routing architecture.

## Current benchmark results

This section includes both benchmark evidence and PBSA v2.0 routing evidence.

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
- Holdout run count: 4
- Holdout overall classification: PBA-D

Candidate readiness:

- Latest candidate-readiness report: reports/candidates/latest_candidate_readiness_report.json
- Candidate spec count: 4
- Candidate execution allowed in v1.3: false
- Candidate execution allowed in v1.4+: comparison harness only

Candidate specs generated:

- direct_route_candidate_v0
- pulse_route_candidate_v0
- oscillatory_preservation_candidate_v0
- noisy_recovery_guard_candidate_v0

Champion/challenger governance:

- Latest champion/challenger report: reports/champion_challenger/latest_champion_challenger_report.json
- Decision: route_by_regime
- Promotion status: no_automatic_promotion
- Automatic kernel replacement: false
- Kernel mutation: false

Regime-routed PBSA:

- Route policy: configs/routing/regime_route_policy_v2_0.json
- Latest routed suite report: reports/routing/latest_routed_suite_report.json
- Route evidence directory: reports/routing/route_evidence
- Routed-suite decision: route_by_regime
- Manual review required: true
- Automatic kernel replacement: false
- Kernel mutation: false

## How to interpret the current result

A PBA-C original-suite result, PBA-D holdout result, and `route_by_regime` routing decision are not failures. They mean the evidence system is doing its job.

The correct interpretation is:

- PBSA implementation is working.
- Tests are passing.
- Evidence generation is working.
- Original-suite downgrade is preserved.
- Holdout weakness is preserved.
- Candidate specs were generated but not globally promoted.
- Champion/challenger comparison concluded routing is safer than replacement.
- PBSA v2.0 now routes by regime evidence.
- Stronger biological or medical claims are not justified.
- The next valid step is PBSA v2.1 routed-suite validation.

## What this project is

- A local executable PBSA/PBA research repository.
- A benchmarkable Python package.
- A baseline-comparison system.
- A calibration and identifiability scaffold.
- A suite-level evidence aggregator.
- A holdout evaluation layer.
- A candidate-readiness layer.
- A champion/challenger governance layer.
- A regime-routing layer.
- A route-evidence and routed-suite reporting layer.
- A repository organized for human and AI readability using RCC-style mini READMEs.

## What this project is not

- Not medical guidance.
- Not treatment guidance.
- Not clinical validation.
- Not biological mechanism proof.
- Not a universal biological law claim.
- Not proof that Delta Phi governs living systems.
- Not proof that routing is biologically valid.
- Not permission to treat toy benchmark results as biological evidence.
- Do not treat benchmark success as biological validation.
- Not permission to promote candidate specs into active controllers.
- Not permission to treat local route selection as global kernel replacement.

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

Generate champion/challenger report:

    python -m pba.cli champion-challenger-report

Generate routed-suite report:

    python -m pba.cli routed-suite-report

Generate evolution report:

    python -m pba.cli diagnose-evolution

Run the local automation script:

    powershell -ExecutionPolicy Bypass -File .\scripts\run_local.ps1

Dump the repo structure:

    powershell -ExecutionPolicy Bypass -File .\scripts\repo_dump_light.ps1

## Repository map for humans

- configs: declared suite, domains, holdout domains, routing policies, candidate configs, parameters, baseline settings, calibration grid, and metrics.
- docs: theory, architecture, RCC context map, and benchmark protocol.
- src/pba: Python implementation.
- src/pba/routing: PBSA v2.0 route registry, selector, eligibility gates, and routed runner.
- tests: unit tests and RCC README coverage checks.
- runs: generated benchmark run artifacts.
- reports: generated suite summaries, holdout summaries, candidate-readiness reports, champion/challenger reports, routing reports, and route evidence.
- ledgers: local runtime and decision continuity records.
- scripts: local helper scripts.

## Release and GitHub status

This repository has been published to GitHub.

Remote:

    https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-

Current published status:

- PBSA v2.0 regime-routed architecture added.
- PBA v1.4 theory/governance docs archived.
- Package version: 1.0.0.
- 44 tests passing.
- Original suite classification: PBA-C.
- Holdout suite classification: PBA-D.
- Latest holdout summary generated.
- Latest candidate-readiness report generated.
- Latest champion/challenger report generated.
- Latest routed-suite report generated.
- Current global decision: route_by_regime.
- Manual review required: true.
- Candidate execution: comparison harness only.
- Route execution: governed routing report only.
- Automatic kernel replacement: disabled.
- Kernel mutation: disabled.
- Next target: PBSA v2.1 routed-suite validation.

Before future pushes, verify:

- tests pass,
- original suite summary exists,
- holdout summary exists if holdout behavior changed,
- candidate-readiness report exists if candidate semantics changed,
- champion/challenger report exists if candidate comparison changed,
- routed-suite report exists if routing behavior changed,
- root README is current,
- mini READMEs exist,
- docs/theory and docs/architecture reflect current versioning,
- no medical or biological-law claim entered the docs.

---


## RCC Compatibility Anchors

This section preserves stable README anchors required by the executable RCC documentation contract.

- Current benchmark results: see the benchmark and routing evidence section above.
- Human README: see PART I - Human README.
- AI README: see PART II - AI / Agent README.
- Quick start: see the Quick start section.
- Repository map for humans: see the repository map section.
- Required local verification: see the AI verification section.
- PBSA v2.0 routing chain: domain -> primary regime -> secondary overlays -> route eligibility -> route selection -> route evidence -> route ledger -> routed suite report -> RCC refresh.

# PART II - AI / Agent README

## AI version tracking contract

Current canonical versions:

- PBSA_VERSION: PBSA-v2.0
- PBA_VERSION: PBA-v1.4
- package version: 1.0.0
- current global decision: route_by_regime
- original suite classification: PBA-C
- holdout suite classification: PBA-D
- current tests: 44 passing
- candidate execution allowed: comparison harness only
- route execution enabled: governed reports only
- manual review required: true
- automatic kernel replacement allowed: false
- kernel mutation allowed: false
- current docs archive: docs/theory and docs/architecture
- current routing policy: configs/routing/regime_route_policy_v2_0.json
- latest routed suite report: reports/routing/latest_routed_suite_report.json
- next target: PBSA v2.1 routed-suite validation

AI agents must update this README when version constants, suite evidence, holdout evidence, champion/challenger evidence, routed-suite evidence, route policy, route selector behavior, docs/theory, docs/architecture, or evolution reports change.

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

PBSA requires the following before any benchmark, candidate, or route interpretation:

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
- champion/challenger report when candidate comparison is discussed,
- route evidence when routing is discussed,
- routed-suite report when routing behavior is discussed,
- non-claim boundary.

## Canonical runtime chain

domain config -> parameter manifest -> perturbations -> calibration -> PBA kernel -> baselines -> metrics -> identifiability -> classification -> evidence package -> ledger -> suite summary -> report

## PBSA v2.0 routing chain

domain -> primary regime -> secondary overlays -> route eligibility -> route selection -> route evidence -> route ledger -> routed suite report -> RCC refresh

## AI file routing guide

Use this routing map before editing:

- Modify configs only when changing declared benchmark, candidate, or routing conditions.
- Modify configs/routing only when changing route policy.
- Modify src/pba/core only when changing PBA runtime primitives.
- Modify src/pba/baselines only when changing comparators.
- Modify src/pba/calibration only when changing parameter search.
- Modify src/pba/evaluation only when changing metrics, identifiability, classification, or regime diagnostics.
- Modify src/pba/evidence only when changing evidence package, reports, manifests, suite summaries, holdout summaries, route evidence, or routed-suite reports.
- Modify src/pba/evolution only when changing candidate specs, candidate readiness, champion/challenger logic, or promotion governance.
- Modify src/pba/routing only when changing route registry, route selector, route eligibility, or routed runner.
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
- proof from candidate readiness alone,
- proof from champion/challenger comparison alone,
- proof from route selection alone.

## AI interpretation of current evidence

Current original-suite classification:

PBA-C

Current holdout-suite classification:

PBA-D

Current champion/challenger decision:

route_by_regime

Current routed-suite decision:

route_by_regime

Current evidence conclusion:

The current repository is functioning as a conservative regime-routed research scaffold. PBA shows local advantage in one original-suite domain, loses to a simple proportional baseline in two original-suite domains, and does not yet generalize strongly under the v1.3 holdout suite. PBSA v1.4 showed that the safer architecture is `route_by_regime`, not global replacement. PBSA v2.0 operationalizes that result by selecting admissible baseline, champion, candidate, or reject routes under evidence gates. This supports routed-suite validation next, not biological or medical overclaim.

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
10. Generate champion/challenger report if candidate comparison changed.
11. Generate routed-suite report if routing behavior changed.
12. Update README evidence section only from generated JSON.
13. Commit locally only unless push is explicitly requested.

## Required local verification

After any meaningful patch, run:

    python -m unittest discover -s tests

If original benchmark behavior changed, also run:

    python -m pba.cli run-suite --config .\configs\suite_v1_0.json

If holdout behavior changed, also run:

    python -m pba.cli run-suite --config .\configs\suite_holdout_v1_3.json
    python -m pba.cli summarize-holdout
    python -m pba.cli candidate-readiness

If candidate comparison changed, also run:

    python -m pba.cli champion-challenger-report

If routing behavior changed, also run:

    python -m pba.cli routed-suite-report

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

This repository is built to downgrade itself. Do not optimize documentation to sound stronger than the evidence. The correct behavior is to preserve mixed results, baseline wins, failure surfaces, holdout weakness, candidate restrictions, route restrictions, manual review gates, and non-claim boundaries.

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

## PBSA v1.3 Holdout and Candidate Readiness Upgrade

Added four holdout domain configs, suite_holdout_v1_3.json, holdout summary generation, regime coverage matrix, candidate specification schema, candidate-readiness report, CLI commands for holdout/readiness, docs archive, implementation map, and RCC mini README synchronization.

Important lock: PBSA v1.3 broadened evidence only. Candidate specs were not executable controllers.

## PBSA v1.4 Champion/Challenger Governance Upgrade

Added candidate route configs, executable comparison-harness challenger variants, champion/challenger runner, promotion governance taxonomy, champion/challenger report generator, CLI command for champion/challenger reporting, docs archive, implementation map, and RCC mini README synchronization.

Important lock: candidate execution is not promotion. Automatic kernel replacement remains disabled.

Command:

    python -m pba.cli champion-challenger-report

## PBSA v2.0 Regime-Routed PBSA Upgrade

Added routing policy config, route registry, route selector, route eligibility gates, routed runner, route evidence packages, routed suite report, CLI command for routed suite reports, docs archive, implementation map, and RCC mini README synchronization.

Important lock: routing is not biological validation, routing is not global kernel replacement, baseline routes remain valid when evidence supports them, champion routes remain valid when evidence supports them, candidate routes remain governed and review-bound, automatic kernel replacement remains disabled, and kernel mutation remains disabled.

Command:

    python -m pba.cli routed-suite-report

Next target:

    PBSA v2.1 routed-suite validation