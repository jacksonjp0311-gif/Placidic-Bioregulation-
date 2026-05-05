# PBSA v1.1 Implementation Map

## Purpose

This file maps the PBSA v1.1 architecture to the actual repository implementation.

## Current implementation status

Implemented:

- PBSA_VERSION = PBSA-v1.1
- package version = 0.2.0
- 18 passing tests
- regime detector
- baseline advantage mapper
- evolution package
- evolution policy config
- holdout placeholder config
- evolution report generator
- diagnose-evolution CLI
- compare-kernels CLI scaffold
- latest evolution report
- decision: preserve_champion
- overall classification: PBA-C

## Architecture-to-code map

| Architecture object | Repository implementation |
|---|---|
| SuiteSummaryCompiler | src/pba/evidence/suite_summary.py |
| RegimeDetector | src/pba/evaluation/regime_detector.py |
| BaselineAdvantageMapper | src/pba/evaluation/baseline_advantage.py |
| EvolutionPolicy | src/pba/evolution/evolution_policy.py and configs/evolution_policy.json |
| KernelCandidate | src/pba/evolution/kernel_candidate.py |
| ChampionChallengerScaffold | src/pba/evolution/champion_challenger.py |
| EvolutionReportGenerator | src/pba/evidence/evolution_report.py |
| RCCContextValidator | tests/test_rcc_readmes.py |
| Evolution reports | reports/evolution/ |
| Decision ledger | ledgers/pba_decision_ledger.jsonl |

## Current evidence state

The current suite remains mixed:

- Overall classification: PBA-C
- PBA-A domains: 1
- PBA-C domains: 2
- PBA advantage: 1
- Baseline advantage: 2
- Best baseline frequency: proportional_feedback in 3/3 domains

The correct decision is preserve_champion.

## Important diagnostic finding

The first v1.1 regime detector classified all domains as cusp_risk because cusp-warning detection currently dominates domain-shape detection.

This is useful, not bad. It defines the next improvement:

- move from single-label regime detection to multi-label regime detection.

Expected next diagnostic output:

- temperature_like: direct_recovery + cusp_risk
- pulse_recovery: pulse_recovery + cusp_risk
- oscillatory_signal: oscillatory + cusp_risk

## Next architecture target

PBSA v1.2 should implement multi-label regime detection and report primary and secondary regimes without changing the champion kernel.

## Non-claim boundary

This implementation map is software architecture documentation. It is not medical guidance, clinical validation, biological-law proof, or mechanism proof.