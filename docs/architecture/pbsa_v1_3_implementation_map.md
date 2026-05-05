# PBSA v1.3 Implementation Map

## Purpose

Map PBSA v1.3 architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Holdout domains | configs/domains/holdout_*.json |
| Holdout suite | configs/suite_holdout_v1_3.json |
| Holdout summary | src/pba/evidence/holdout_summary.py |
| Candidate specification | src/pba/evolution/candidate_spec.py |
| Candidate readiness | src/pba/evolution/candidate_readiness.py |
| CLI holdout summary | python -m pba.cli summarize-holdout |
| CLI candidate readiness | python -m pba.cli candidate-readiness |
| Holdout reports | reports/holdout/ |
| Candidate reports | reports/candidates/ |

## Current decision

preserve_champion

## Kernel mutation

Disabled. PBSA v1.3 prepares evidence and candidate specs only.
