# PBSA v2.1 Implementation Map

## Purpose

Map PBSA v2.1 routed-suite validation architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Validation policy | configs/validation/routed_validation_policy_v2_1.json |
| Control policies | src/pba/validation/control_policies.py |
| Route metrics | src/pba/validation/route_metrics.py |
| Failure surface | src/pba/validation/failure_surface.py |
| Routed validation runner | src/pba/validation/routed_validation_runner.py |
| Routed validation report | src/pba/evidence/routed_validation_report.py |
| CLI command | python -m pba.cli routed-validation-report |
| Reports | reports/validation/ |

## Current lock

Automatic kernel replacement remains disabled.
