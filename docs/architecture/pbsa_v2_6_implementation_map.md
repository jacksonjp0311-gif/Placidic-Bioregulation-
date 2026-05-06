# PBSA v2.6 Implementation Map

## Purpose

Map PBSA v2.6 reproducibility replay architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Replay policy | configs/replay/replay_policy_v2_6.json |
| Replay artifact manifest | configs/replay/replay_artifact_manifest_v2_6.json |
| Replay runner | src/pba/replay/replay_runner.py |
| Decision replay | src/pba/replay/decision_replay.py |
| Hash drift | src/pba/replay/hash_drift.py |
| Replay lock verifier | src/pba/replay/replay_lock_verifier.py |
| Replay audit report | src/pba/evidence/replay_audit_report.py |
| CLI command | python -m pba.cli replay-audit-report |
| Reports | reports/replay/ |

## Current lock

Automatic kernel replacement remains disabled.
