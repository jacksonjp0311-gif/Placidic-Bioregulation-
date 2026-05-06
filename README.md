# Placidic Bioregulation

<img width="1672" height="941" alt="image" src="https://github.com/user-attachments/assets/386c7971-e31b-49c0-9bc3-d179e1e8675e" />

Codex Delta Phi - Placidic Bioregulation Software Architecture PBSA v3.0

Local-first executable research repository for the Placidic Bioregulation Algorithm PBA v1.4.

Status: GitHub-published research repository  
GitHub remote: https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-  
Package version: 3.0.0  
Current software architecture: PBSA v3.0 - Public Research Package  
Current theory layer: PBA v1.4 - Evidence Feedback and Regime-Aware Placidity  
Current global decision: route_by_regime  
Original suite classification: PBA-C  
Holdout suite classification: PBA-D  
Current tests: 153 passing  
Candidate execution: comparison harness only  
Route execution: enabled through governed routing reports  
Manual review required: true  
Automatic kernel replacement: disabled  
Kernel mutation: disabled  
Next target: create and push release tag  

---

## Version ledger

| Layer | Current version | Repository status |
|---|---:|---|
| Software architecture | PBSA v3.0 | implemented and pushed |
| Algorithm theory | PBA v1.4 | documented in docs/theory |
| Python package | 3.0.0 | active |
| Test suite | 153 passing | active |
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
| Next planned layer | release tag | v3.0.0-public-research-package |

## Current architecture status

PBSA v3.0 is the public research package layer. It freezes the replay-verified and release-candidate-ready PBSA stack into a public computational research artifact.

The current stack is:

- PBA v1.4: Evidence Feedback and Regime-Aware Placidity.
- PBSA v2.0: regime-routed PBSA.
- PBSA v2.1: routed-suite validation.
- PBSA v2.2: external-domain validation.
- PBSA v2.3: stress/adversarial validation.
- PBSA v2.4: calibration and threshold tuning.
- PBSA v2.5: evidence package hardening.
- PBSA v2.6: reproducibility replay.
- PBSA v2.7: release candidate audit bundle.
- PBSA v3.0: public research package.

Current generated evidence state:

- Routed-suite decision: route_by_regime
- Routed-validation decision: validate_routing
- External-validation decision: external_validate_with_caution
- Stress-validation decision: stress_validate_with_caution
- Calibration decision: calibrate_with_caution
- Evidence-package decision: evidence_package_valid
- Replay decision: replay_valid_with_timestamp_drift
- Release-candidate decision: release_candidate_ready
- Public-package decision: public_package_ready
- Public-package readiness: true
- Semantic drift count: 0
- Expected timestamp/hash drift count: 6
- Release tag metadata: v3.0.0-public-research-package

PBSA v3.0 does not replace the PBA kernel globally. It does not promote a candidate globally. It publishes a computational audit package with explicit limitations, claim-boundary locks, downgrade locks, failure-surface visibility, reproducibility commands, and RCC-aligned README surfaces.

Automatic kernel replacement remains disabled. Kernel mutation remains disabled.

## Executive summary

Placidic Bioregulation is a runnable Python research repository that now implements PBSA v3.0: a public computational research package for evidence-feedback control-policy evaluation.

The project moved through a full governed evidence loop:

theory -> executable software -> tests -> benchmark evidence -> downgrade -> multi-label diagnosis -> holdout expansion -> candidate readiness -> champion/challenger comparison -> regime routing -> routed validation -> external validation -> stress validation -> calibration -> evidence packaging -> reproducibility replay -> release-candidate audit -> public research package.

The important current result is not "PBA wins everywhere." The important result is that PBSA preserves mixed evidence, baseline wins, holdout weakness, failure surfaces, timestamp drift, manual review, claim boundaries, and non-claim locks while making the repository reproducible and auditable.

Current public-package decision: `public_package_ready`.  
Current public-package readiness: `true`.  
Prepared release tag: `v3.0.0-public-research-package`.

## Current finding

The current evidence state is public-package ready but still conservative.

Original suite:

- Overall classification: PBA-C.
- PBA wins in one declared toy domain.
- A simpler proportional baseline performs better in two declared domains.

Holdout suite:

- Overall classification: PBA-D.
- The holdout run broadened the evidence surface and showed weak generalization.
- This supports routing and validation, not global candidate promotion.

Routing and validation stack:

- Routed-suite decision: `route_by_regime`.
- Routed-validation decision: `validate_routing`.
- External-validation decision: `external_validate_with_caution`.
- Stress-validation decision: `stress_validate_with_caution`.
- Calibration decision: `calibrate_with_caution`.
- Evidence-package decision: `evidence_package_valid`.
- Replay decision: `replay_valid_with_timestamp_drift`.
- Release-candidate decision: `release_candidate_ready`.
- Public-package decision: `public_package_ready`.

Current conclusion:

PBSA is functioning as a conservative, evidence-governed, regime-routed research scaffold. It is now packaged for public computational audit. The public package is not biological validation, not medical guidance, not clinical safety evidence, and not proof of a physiological mechanism.

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

A PBA-C original-suite result, PBA-D holdout result, `route_by_regime` routing decision, replay-valid audit state, and public-package-ready state are not global proof claims. They mean the evidence system is doing its job.

The correct interpretation is:

- PBSA implementation is working.
- 153 tests are passing.
- RCC README tests are passing.
- Evidence generation is working.
- Original-suite downgrade is preserved.
- Holdout weakness is preserved.
- Candidate specs were generated but not globally promoted.
- Champion/challenger comparison concluded routing is safer than replacement.
- PBSA routes by regime evidence.
- External, stress, calibration, evidence-package, replay, release-candidate, and public-package surfaces are now present.
- Semantic drift is clear at `0`.
- Expected timestamp/hash drift remains visible at `6`.
- Public-package readiness is `true`.
- Stronger biological or medical claims are not justified.
- The next valid step is to create and push the release tag `v3.0.0-public-research-package`.

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
- A routed-validation layer.
- An external-domain validation layer.
- A stress/adversarial validation layer.
- A calibration and threshold-tuning layer.
- An evidence-package hardening layer.
- A reproducibility replay layer.
- A release-candidate audit bundle layer.
- A public research package layer.
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

Run RCC README contract tests:

    python -m unittest tests.test_rcc_readmes -v

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

Generate routed-validation report:

    python -m pba.cli routed-validation-report

Generate external-validation report:

    python -m pba.cli external-validation-report

Generate stress-validation report:

    python -m pba.cli stress-validation-report

Generate calibration report:

    python -m pba.cli calibration-report

Generate evidence-package report:

    python -m pba.cli evidence-package-report

Generate replay-audit report:

    python -m pba.cli replay-audit-report

Generate release-candidate report:

    python -m pba.cli release-candidate-report

Generate public-package report:

    python -m pba.cli public-package-report

Run the local automation script:

    powershell -ExecutionPolicy Bypass -File .\scripts\run_local.ps1

Dump the repo structure:

    powershell -ExecutionPolicy Bypass -File .\scripts\repo_dump_light.ps1

Prepared release tag:

    v3.0.0-public-research-package

## Repository map for humans

- configs: declared suite, domains, holdout domains, routing policies, validation policies, external validation configs, stress validation configs, calibration policies, evidence-package policies, replay policies, release policies, public-package policies, candidate configs, parameters, baseline settings, calibration grid, and metrics.
- docs: theory, architecture, RCC context map, benchmark protocol, and versioned PBSA implementation maps.
- src/pba: Python implementation.
- src/pba/routing: PBSA v2.0 route registry, selector, eligibility gates, and routed runner.
- src/pba/evidence: generated evidence reports, manifests, suite summaries, holdout summaries, route evidence, validation reports, replay reports, release reports, and public-package reports.
- src/pba/evidence_hardening: PBSA v2.5 hash manifest, report-chain, ledger-continuity, RCC-anchor, downgrade-lock, and failure-surface verifiers.
- src/pba/replay: PBSA v2.6 reproducibility replay, decision replay, hash drift, replay lock verification, and replay audit logic.
- src/pba/release: PBSA v2.7 release-candidate audit bundle generation.
- src/pba/public_package: PBSA v3.0 public research package generation.
- tests: unit tests and RCC README coverage checks.
- runs: generated benchmark run artifacts.
- reports: generated suite summaries, holdout summaries, candidate-readiness reports, champion/challenger reports, routing reports, validation reports, evidence packages, replay audit reports, release candidate reports, and public package reports.
- ledgers: local runtime and decision continuity records.
- scripts: local helper scripts.

## Release and GitHub status

This repository has been published to GitHub.

Remote:

    https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-

Current published status:

- PBSA v3.0 public research package added.
- PBA v1.4 theory/governance docs archived.
- Package version: 3.0.0.
- 153 tests passing.
- RCC README tests passing.
- Original suite classification: PBA-C.
- Holdout suite classification: PBA-D.
- Latest holdout summary generated.
- Latest candidate-readiness report generated.
- Latest champion/challenger report generated.
- Latest routed-suite report generated.
- Latest routed-validation report generated.
- Latest external-validation report generated.
- Latest stress-validation report generated.
- Latest calibration report generated.
- Latest evidence-package report generated.
- Latest replay-audit report generated.
- Latest release-candidate report generated.
- Latest public-package report generated.
- Current global decision: route_by_regime.
- Public package decision: public_package_ready.
- Public package readiness: true.
- Manual review required: true.
- Candidate execution: comparison harness only.
- Route execution: governed routing report only.
- Automatic kernel replacement: disabled.
- Kernel mutation: disabled.
- Next target: create and push release tag `v3.0.0-public-research-package`.

Before future pushes, verify:

- tests pass,
- RCC README tests pass,
- generated reports are current if behavior changed,
- root README is current,
- mini READMEs exist,
- docs/theory and docs/architecture reflect current versioning,
- no medical or biological-law claim entered the docs.

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

- PBSA_VERSION: PBSA-v3.0
- PBA_VERSION: PBA-v1.4
- package version: 3.0.0
- current global decision: route_by_regime
- original suite classification: PBA-C
- holdout suite classification: PBA-D
- current tests: 153 passing
- candidate execution allowed: comparison harness only
- route execution enabled: governed reports only
- manual review required: true
- automatic kernel replacement allowed: false
- kernel mutation allowed: false
- current docs archive: docs/theory and docs/architecture
- current routing policy: configs/routing/regime_route_policy_v2_0.json
- latest routed suite report: reports/routing/latest_routed_suite_report.json

- latest routed validation report: reports/validation/latest_routed_validation_report.json
- latest external validation report: reports/external_validation/latest_external_validation_report.json
- latest stress validation report: reports/stress_validation/latest_stress_validation_report.json
- latest calibration report: reports/calibration/latest_calibration_report.json
- latest evidence package report: reports/evidence_packages/latest_evidence_package_report.json
- latest replay audit report: reports/replay/latest_replay_audit_report.json
- latest release candidate report: reports/release/latest_release_candidate_report.json
- latest public package report: reports/public_package/latest_public_package_report.json
- prepared release tag: v3.0.0-public-research-package
- next target: create and push release tag

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

- routed-validation report when routed validation is discussed,
- external-validation report when external behavior is discussed,
- stress-validation report when adversarial/stress behavior is discussed,
- calibration report when threshold tuning is discussed,
- evidence-package report when audit traceability is discussed,
- replay-audit report when reproducibility replay is discussed,
- release-candidate report when public audit readiness is discussed,
- public-package report when public release/readiness is discussed,
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

- Modify src/pba/evidence_hardening only when changing evidence-package verification, hash manifests, report-chain checks, ledger-continuity checks, RCC-anchor checks, downgrade-lock checks, or failure-surface verifiers.
- Modify src/pba/replay only when changing reproducibility replay, decision replay, hash drift, replay locks, or replay audit behavior.
- Modify src/pba/release only when changing release-candidate audit bundles, evidence index, claim boundaries, command surface, failure-surface index, or release readiness.
- Modify src/pba/public_package only when changing public abstract, evidence summary, public limitations, public command surface, public claim boundaries, or public package readiness.
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

Current public-package decision:

public_package_ready

Current evidence conclusion:

The current repository is functioning as a conservative regime-routed public research package. PBA shows local advantage in one original-suite domain, loses to a simple proportional baseline in two original-suite domains, and does not yet generalize strongly under the v1.3 holdout suite. PBSA v1.4 showed that the safer architecture is `route_by_regime`, not global replacement. PBSA v2.0 operationalized routing. PBSA v2.1-v2.7 added routed validation, external validation, stress validation, calibration, evidence packaging, replay, and release-candidate audit packaging. PBSA v3.0 now exposes the system as a public computational research package with claim boundaries, limitations, command surfaces, evidence summaries, release metadata, and no automatic kernel replacement.

This supports public computational audit and release-tag archiving, not biological validation, medical guidance, clinical safety, or physiological mechanism proof.

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
    python -m unittest tests.test_rcc_readmes -v

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
    python -m pba.cli routed-validation-report

If external validation behavior changed, also run:

    python -m pba.cli external-validation-report

If stress/adversarial behavior changed, also run:

    python -m pba.cli stress-validation-report

If calibration behavior changed, also run:

    python -m pba.cli calibration-report

If evidence-package behavior changed, also run:

    python -m pba.cli evidence-package-report

If replay behavior changed, also run:

    python -m pba.cli replay-audit-report

If release-candidate behavior changed, also run:

    python -m pba.cli release-candidate-report

If public-package behavior changed, also run:

    python -m pba.cli public-package-report

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

## PBSA v2.1 Routed-Suite Validation Upgrade

This repository now includes the PBSA v2.1 routed-suite validation layer.

Added surfaces:
- validation policy config
- control policy definitions
- champion-only / baseline-only / candidate-only / reject-manual-review controls
- route advantage metrics
- route preservation score
- route failure surface
- routed validation report
- CLI command for routed validation reports
- docs/theory PBSA v2.1 archive
- docs/architecture PBSA v2.1 implementation map
- RCC mini README synchronization

Important lock:
- Routed validation is not biological validation.
- Routed advantage is not medical evidence.
- Validation is not automatic kernel replacement.
- Failure surfaces remain visible.
- Baseline wins remain visible.
- Holdout weakness remains visible.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.
- Do not treat benchmark success as biological validation.

Command:
    python -m pba.cli routed-validation-report

Next target:
- PBSA v2.2 external-domain validation


## PBSA v2.2 External-Domain Validation Upgrade

This repository now includes the PBSA v2.2 external-domain validation layer.

Added surfaces:
- external toy-domain family configs
- external validation suite
- external validation policy
- external routed runner
- internal-vs-external comparison metrics
- route drift detector
- external failure surface
- external validation report
- CLI command for external validation reports
- docs/theory PBSA v2.2 archive
- docs/architecture PBSA v2.2 implementation map
- RCC mini README synchronization

Important lock:
- External validation is not biological validation.
- External advantage is not medical evidence.
- Route drift must remain visible.
- External failure surfaces must remain visible.
- Baseline wins remain visible.
- Holdout weakness remains visible.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.
- Do not treat benchmark success as biological validation.

Command:
    python -m pba.cli external-validation-report

Next target:
- PBSA v2.3 stress/adversarial validation


## PBSA v2.3 Stress/Adversarial Validation Upgrade

This repository now includes the PBSA v2.3 stress/adversarial validation layer.

Added surfaces:
- stress/adversarial toy-domain configs
- stress validation suite
- stress validation policy
- malformed input guard
- contradictory regime detector
- safe-fail route decisions
- stress route drift metrics
- stress failure surface
- stress validation report
- CLI command for stress validation reports
- docs/theory PBSA v2.3 archive
- docs/architecture PBSA v2.3 implementation map
- RCC mini README synchronization

Important lock:
- Stress validation is not biological validation.
- Adversarial robustness is not medical safety.
- Malformed inputs must not crash the report path.
- Contradictory regimes must route to reject/manual review unless evidence permits an admissible route.
- Stress failures must remain visible.
- Safe-fail score must remain visible.
- Crash rate must remain visible.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.
- Do not treat benchmark success as biological validation.

Command:
    python -m pba.cli stress-validation-report

Next target:
- PBSA v2.4 calibration and threshold tuning


## PBSA v2.4 Calibration and Threshold Tuning Upgrade

This repository now includes the PBSA v2.4 calibration and threshold tuning layer.

Added surfaces:
- calibration policy config
- threshold grid config
- threshold candidate schema
- calibration metrics
- overfitting guard
- safe-fail preservation check
- calibration runner
- calibration report
- CLI command for calibration reports
- docs/theory PBSA v2.4 archive
- docs/architecture PBSA v2.4 implementation map
- RCC mini README synchronization

Important lock:
- Calibration is not biological validation.
- Threshold tuning is not medical safety.
- Threshold tuning must not hide failures.
- Threshold tuning must not weaken safe-fail behavior.
- Overfitting guard must remain visible.
- Crash-rate preservation must remain visible.
- Failure visibility must remain preserved.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.
- Do not treat benchmark success as biological validation.

Command:
    python -m pba.cli calibration-report

Next target:
- PBSA v2.5 evidence package hardening


## PBSA v2.5 Evidence Package Hardening Upgrade

This repository now includes the PBSA v2.5 evidence package hardening layer.

Added surfaces:
- evidence package policy config
- evidence artifact manifest config
- hash manifest generator
- report-chain verifier
- ledger-continuity verifier
- RCC anchor verifier
- downgrade-lock verifier
- failure-surface verifier
- evidence package compiler
- evidence package report
- CLI command for evidence package reports
- docs/theory PBSA v2.5 archive
- docs/architecture PBSA v2.5 implementation map
- RCC mini README synchronization

Important lock:
- Evidence packaging is not biological validation.
- Auditability is not medical safety.
- Reproducibility is not mechanism proof.
- Evidence packages must not hide failures.
- Downgrade locks must remain visible.
- Failure surfaces must remain visible.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.
- Do not treat benchmark success as biological validation.

Command:
    python -m pba.cli evidence-package-report

Next target:
- PBSA v2.6 reproducibility replay


## PBSA v2.6 Reproducibility Replay Upgrade

This repository now includes the PBSA v2.6 reproducibility replay layer.

Added surfaces:
- replay policy config
- replay artifact manifest config
- replay runner
- decision replay comparator
- hash drift detector
- replay lock verifier
- failure-surface replay verifier
- replay audit report
- CLI command for replay audit reports
- docs/theory PBSA v2.6 archive
- docs/architecture PBSA v2.6 implementation map
- RCC mini README synchronization

Important lock:
- Reproducibility replay is not biological validation.
- Hash stability is not truth.
- Replay success is not medical safety.
- Decision drift must remain visible.
- Hash drift must remain visible.
- Downgrade locks must replay.
- Failure surfaces must replay.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.
- Do not treat benchmark success as biological validation.

Command:
    python -m pba.cli replay-audit-report

Next target:
- PBSA v2.7 release candidate audit bundle


## PBSA v2.7 Release Candidate Audit Bundle Upgrade

This repository now includes the PBSA v2.7 release candidate audit bundle layer.

Added surfaces:
- release candidate policy config
- release audit manifest config
- evidence index
- claim-boundary table
- failure-surface index
- command surface
- release readiness verifier
- release candidate report
- public audit index
- CLI command for release candidate reports
- docs/theory PBSA v2.7 archive
- docs/architecture PBSA v2.7 implementation map
- RCC mini README synchronization

Important lock:
- Release-candidate readiness is not biological validation.
- Public audit readiness is not medical safety.
- Reproducibility is not mechanism proof.
- Claim boundaries must remain visible.
- Failure surfaces must remain visible.
- Downgrade locks must remain visible.
- Semantic drift must remain visible.
- Timestamp drift must remain distinguished from semantic drift.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.
- Do not treat benchmark success as biological validation.

Command:
    python -m pba.cli release-candidate-report

Next target:
- PBSA v3.0 public research package


## PBSA v3.0 Public Research Package

This repository now includes the PBSA v3.0 public research package layer.

PBSA is a computational regime-routing and validation framework for evidence-feedback control policy evaluation. It includes internal routed validation, external-domain validation, stress/adversarial validation, calibration, evidence package hardening, reproducibility replay, release-candidate audit packaging, and public research package reporting.

Public package surfaces:
- publication abstract
- evidence summary
- public limitations
- public claim-boundary table
- public command surface
- public package readiness verifier
- release checklist
- release tag metadata
- public package report
- docs/theory PBSA v3.0 archive
- docs/architecture PBSA v3.0 implementation map
- RCC mini README synchronization

Important lock:
- Public release is not biological validation.
- Public release is not medical validation.
- Public release is not clinical safety evidence.
- Public package readiness is not mechanism proof.
- Public audit readiness is not medical safety.
- Claim boundaries must remain visible.
- Failure surfaces must remain visible.
- Downgrade locks must remain visible.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.
- Do not treat benchmark success as biological validation.

Core public command:
    python -m pba.cli public-package-report

Prepared release tag:
    v3.0.0-public-research-package

## PBSA v3.0 public package chain

release-candidate report -> public package policy -> publication abstract -> evidence summary -> public limitations -> public claim boundaries -> public command surface -> release checklist -> public package report -> release tag metadata -> RCC refresh


## Public release tag status

Prepared release tag:

    v3.0.0-public-research-package

Current next action:

    create and push release tag v3.0.0-public-research-package

This tag marks PBSA v3.0 as a public computational research package. It does not mark biological validation, medical validation, clinical safety evidence, or physiological mechanism proof.
