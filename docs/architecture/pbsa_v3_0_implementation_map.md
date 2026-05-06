# PBSA v3.0 Implementation Map

## Purpose

Map PBSA v3.0 public research package architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Public package policy | configs/public_package/public_package_policy_v3_0.json |
| Public release manifest | configs/public_package/public_release_manifest_v3_0.json |
| Publication abstract | src/pba/public_package/public_abstract.py |
| Evidence summary | src/pba/public_package/evidence_summary.py |
| Public limitations | src/pba/public_package/public_limitations.py |
| Public command surface | src/pba/public_package/public_command_surface.py |
| Public claim boundaries | src/pba/public_package/public_claim_boundaries.py |
| Public package readiness | src/pba/public_package/public_package_readiness.py |
| Public package bundle | src/pba/public_package/public_package_bundle.py |
| Public package report | src/pba/evidence/public_package_report.py |
| CLI command | python -m pba.cli public-package-report |
| Reports | reports/public_package/ |

## Current lock

Automatic kernel replacement remains disabled.
