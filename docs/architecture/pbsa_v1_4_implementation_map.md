# PBSA v1.4 Implementation Map

## Purpose

Map PBSA v1.4 architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Candidate configs | configs/candidates/*.json |
| Candidate variants | src/pba/evolution/candidate_variants.py |
| Champion/challenger runner | src/pba/evolution/champion_challenger_runner.py |
| Promotion governance | src/pba/evolution/promotion_governance.py |
| Champion/challenger report | src/pba/evidence/champion_challenger_report.py |
| CLI command | python -m pba.cli champion-challenger-report |
| Reports | reports/champion_challenger/ |

## Current lock

Automatic kernel replacement remains disabled.
