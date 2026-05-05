# PBSA v2.3 Implementation Map

## Purpose

Map PBSA v2.3 stress/adversarial validation architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Stress domain configs | configs/stress_domains/*.json |
| Stress validation suite | configs/stress_validation_suite_v2_3.json |
| Stress validation policy | configs/validation/stress_validation_policy_v2_3.json |
| Stress domain loader | src/pba/stress/stress_domain_loader.py |
| Malformed input guard | src/pba/stress/malformed_input_guard.py |
| Contradiction detector | src/pba/stress/contradiction_detector.py |
| Stress validation runner | src/pba/stress/stress_validation_runner.py |
| Stress route drift | src/pba/stress/stress_route_drift.py |
| Stress failure surface | src/pba/stress/stress_failure_surface.py |
| Stress validation report | src/pba/evidence/stress_validation_report.py |
| CLI command | python -m pba.cli stress-validation-report |
| Reports | reports/stress_validation/ |

## Current lock

Automatic kernel replacement remains disabled.
