# PBSA v2.2 Implementation Map

## Purpose

Map PBSA v2.2 external-domain validation architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| External domain configs | configs/external_domains/*.json |
| External validation suite | configs/external_validation_suite_v2_2.json |
| External validation policy | configs/validation/external_validation_policy_v2_2.json |
| External domain loader | src/pba/external/external_domain_loader.py |
| External validation runner | src/pba/external/external_validation_runner.py |
| Route drift metrics | src/pba/external/route_drift.py |
| External failure surface | src/pba/external/external_failure_surface.py |
| External validation report | src/pba/evidence/external_validation_report.py |
| CLI command | python -m pba.cli external-validation-report |
| Reports | reports/external_validation/ |

## Current lock

Automatic kernel replacement remains disabled.
