# Codex Delta Phi - Placidic Bioregulation Software Architecture (PBSA v1.1)

## Status

Canonical v1.1 diagnostic evidence-feedback and RCC context architecture layer.

## Purpose

PBSA v1.1 evolves the Placidic Bioregulation Software Architecture from a runnable reference architecture into a diagnostic evidence-feedback and AI-readable continuity architecture.

It adds:

- regime detection,
- baseline-win mapping,
- evolution reports,
- champion/challenger scaffolding,
- holdout or repeat-suite policy,
- decision ledgers,
- RCC README continuity,
- and human/AI repository context surfaces.

PBSA v1.1 prepares kernel evolution, but it does not silently mutate or replace the current PBA kernel.

## Core invariant

PBSA becomes safely self-improving only when suite evidence can diagnose regimes, preserve baseline wins, generate evolution reports, and prepare candidate kernels without silently replacing the champion kernel.

## Live repo alignment

The live repository after the PBSA v1.1 upgrade has:

- PBSA version: PBSA-v1.1
- package version: 0.2.0
- tests: 18 passing
- decision: preserve_champion
- overall classification: PBA-C
- evolution report generation active
- diagnose-evolution CLI command active
- compare-kernels CLI scaffold active

## Architecture chain

The PBSA v1.1 chain is:

tests -> suite run -> suite summary -> regime diagnosis -> baseline-win map -> evolution report -> candidate proposal -> champion/challenger readiness -> RCC / README refresh.

## Existing PBSA v1.0 spine preserved

PBSA v1.1 preserves the v1.0 runtime spine:

- configs
- domain files
- PBA kernel
- baselines
- calibration
- metrics
- identifiability
- classification
- suite summary
- runtime ledgers
- evidence packages
- tests
- reports

## New PBSA v1.1 modules

The v1.1 layer adds:

- src/pba/evaluation/regime_detector.py
- src/pba/evaluation/baseline_advantage.py
- src/pba/evolution/__init__.py
- src/pba/evolution/evolution_policy.py
- src/pba/evolution/kernel_candidate.py
- src/pba/evolution/champion_challenger.py
- src/pba/evidence/evolution_report.py
- configs/evolution_policy.json
- configs/suite_holdout_v1_0.json
- reports/evolution/
- tests/test_regime_detector.py
- tests/test_baseline_advantage.py
- tests/test_champion_challenger.py
- tests/test_evolution_report.py

## RCC merger

RCC is the Repository Context Canon. It treats README files as operational context fields.

PBSA v1.1 requires:

- root README human-facing section,
- root README AI/agent-facing section,
- folder-local mini READMEs,
- RCC context map,
- README coverage tests,
- evidence sections tied to generated artifacts.

AI agents should read the root README, RCC context map, and relevant folder README before modifying source, configs, tests, reports, or benchmark interpretation.

## Diagnostic-first lock

PBSA v1.1 is diagnostic-first.

The current kernel remains champion until a future candidate passes:

- tests,
- suite comparison,
- baseline comparison,
- evolution reporting,
- decision ledger entry,
- non-claim lock verification,
- and holdout or repeat-suite evidence where available.

## Non-claim lock

Software improvement is not biological proof. Benchmark improvement is not medical validation. AI-readable coherence is not empirical truth.