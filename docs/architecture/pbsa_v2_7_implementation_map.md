# PBSA v2.7 Implementation Map

## Purpose

Map PBSA v2.7 release-candidate audit-bundle architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Release candidate policy | configs/release/release_candidate_policy_v2_7.json |
| Release audit manifest | configs/release/release_audit_manifest_v2_7.json |
| Evidence index | src/pba/release/evidence_index.py |
| Claim-boundary table | src/pba/release/claim_boundary_table.py |
| Failure-surface index | src/pba/release/failure_surface_index.py |
| Command surface | src/pba/release/command_surface.py |
| Release readiness verifier | src/pba/release/release_readiness.py |
| Release bundle | src/pba/release/release_bundle.py |
| Release candidate report | src/pba/evidence/release_candidate_report.py |
| CLI command | python -m pba.cli release-candidate-report |
| Reports | reports/release/ |

## Current lock

Automatic kernel replacement remains disabled.
