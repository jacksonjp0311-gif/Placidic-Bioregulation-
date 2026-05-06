# configs

## Purpose

Declared benchmark surface for PBSA.

## S - Formal specification

Configs define domains, parameters, baselines, calibration grid, suite membership, and metric manifest.

## H - Hooks

Used by:
- src/pba/core/domain.py
- src/pba/core/parameters.py
- src/pba/benchmarks/runner.py
- src/pba/benchmarks/suite_runner.py
- tests

## A - Artifacts

- suite_v1_0.json
- pba_params.json
- baseline_params.json
- calibration_grid.json
- metric_manifest.json
- domains/*.json

## T - Theory

Config-first execution prevents hidden calibration and post-hoc benchmark claims.

## I - Invariants

- Parameters must be declared before run.
- Baselines must share task conditions.
- Domains must preserve non-claim locks.
- Fit and evaluation seeds must remain visible.

## E - Example

Run suite from repo root:
python -m pba.cli run-suite --config .\configs\suite_v1_0.json

## PBSA v1.1 evolution configs

- evolution_policy.json declares diagnostic-first rules.
- suite_holdout_v1_0.json is a holdout/repeat-suite placeholder until new domains are added.
- Kernel mutation is disabled by default.

## PBSA v1.2 policy drift cleanup

- evolution_policy.json now declares PBSA-EvolutionPolicy-v1.2.
- suite_holdout_v1_0.json now references PBSA v1.2 diagnostic schema.
- Kernel mutation remains disabled by default.

## PBSA v1.3 holdout configs

Added:
- configs/domains/holdout_direct_recovery.json
- configs/domains/holdout_delayed_pulse.json
- configs/domains/holdout_noisy_recovery.json
- configs/domains/holdout_mixed_oscillation.json
- configs/suite_holdout_v1_3.json

These are computational toy holdout domains only. They are not biological systems.

## PBSA v1.4 candidate configs

Added configs/candidates/*.json for candidate routes.

Candidate execution is allowed only inside comparison harnesses. Automatic promotion and kernel replacement are forbidden.

## PBSA v2.0 routing config

Added:
- configs/routing/regime_route_policy_v2_0.json

This policy selects baseline, champion, candidate, or reject routes under evidence gates.

## PBSA v2.1 validation config

Added:
- configs/validation/routed_validation_policy_v2_1.json

This config compares routed PBSA against champion-only, baseline-only, candidate-only, and reject/manual-review controls.

## PBSA v2.2 external-domain config

Added:
- configs/external_domains/*.json
- configs/external_validation_suite_v2_2.json
- configs/validation/external_validation_policy_v2_2.json

These configs test whether internally validated routing survives external unseen toy-domain families.

## PBSA v2.3 stress-domain config

Added:
- configs/stress_domains/*.json
- configs/stress_validation_suite_v2_3.json
- configs/validation/stress_validation_policy_v2_3.json

These configs test whether externally validated routing fails safely under adversarial pressure.

## PBSA v2.4 calibration config

Added:
- configs/calibration/calibration_policy_v2_4.json
- configs/calibration/threshold_grid_v2_4.json

These configs tune route thresholds while preserving safe-fail behavior, crash-rate visibility, overfitting guards, and non-claim locks.

## PBSA v2.5 evidence package config

Added:
- configs/evidence/evidence_package_policy_v2_5.json
- configs/evidence/evidence_artifact_manifest_v2_5.json

These configs declare required evidence artifacts, report-chain verification, downgrade locks, and RCC anchor checks.

## PBSA v2.6 replay config

Added:
- configs/replay/replay_policy_v2_6.json
- configs/replay/replay_artifact_manifest_v2_6.json

These configs define evidence package replay, decision replay, hash drift detection, ledger replay, RCC replay, and downgrade-lock replay.

## PBSA v2.7 release candidate config

Added:
- configs/release/release_candidate_policy_v2_7.json
- configs/release/release_audit_manifest_v2_7.json

These configs declare public audit surfaces, clone/run commands, evidence indexes, claim boundaries, failure-surface indexes, and release readiness checks.
