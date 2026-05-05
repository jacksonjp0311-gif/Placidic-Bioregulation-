# Codex Delta Phi - Placidic Bioregulation Algorithm (PBA v1.4)

## Status

Canonical v1.4 theory/governance layer.

## Purpose

PBA v1.4 evolves the Placidic Bioregulation Algorithm from a reference implementation and benchmark evidence layer into an evidence-feedback system. It formalizes the lesson from the first PBSA benchmark suite: PBA is not universally superior to simpler baselines, but may show local advantage under specific disturbance regimes.

## Core invariant

Placidity is not constant smoothing. Placidity is the minimum stabilizing regulation appropriate to the detected disturbance regime.

## What the first PBSA suite taught

The first PBSA implementation produced mixed evidence:

- PBA-A domains: 1
- PBA-C domains: 2
- Overall suite classification: PBA-C
- PBA advantage: 1 domain
- Baseline advantage: 2 domains
- Best baseline across all three domains: proportional_feedback
- Mean PBA score: approximately 14.2994
- Mean best baseline score: approximately 13.6804

This means PBA helps in at least one declared toy regime but does not yet dominate the suite.

## Evidence-feedback principle

Every baseline win is diagnostic evidence for kernel evolution.

A baseline-superior result is not a failure. It is a correct downgrade and a learning signal.

## Regime-aware placidity

PBA v1.4 introduces the idea that the kernel should adapt behavior by disturbance regime:

- Direct recovery: simplify and behave closer to proportional feedback when evidence supports it.
- Pulse recovery: preserve baseline wins and test direct correction candidates later.
- Oscillatory disturbance: preserve PBA behavior when PBA shows local advantage.
- Noisy disturbance: avoid over-promotion without repeat-run or holdout evidence.
- Cusp risk: prioritize bounded audit behavior and do not promote kernel changes prematurely.
- Unknown regime: preserve downgrade and collect evidence.

## Baseline-borrowing discipline

When a simpler baseline consistently performs better under shared conditions, PBA must do one of three things:

1. Learn a bounded version of that baseline behavior.
2. Route that regime to the baseline as preferred controller.
3. Downgrade itself for that regime.

## Champion/challenger governance

The current PBA kernel remains champion until a candidate kernel is explicitly tested.

No candidate kernel may replace the champion without:

- passing tests,
- suite comparison,
- baseline comparison,
- evolution report,
- preserved non-claim locks,
- and holdout or repeat-suite evidence where available.

## Non-claim lock

This is not medical guidance, clinical validation, biological mechanism proof, physiological truth, or universal biological law.

## Implementation target

PBA v1.4 maps into PBSA v1.1 through:

- src/pba/evaluation/regime_detector.py
- src/pba/evaluation/baseline_advantage.py
- src/pba/evolution/
- src/pba/evidence/evolution_report.py
- configs/evolution_policy.json
- reports/evolution/
- champion/challenger tests
- downgrade-preserving reports