# PBSA v2.0 Implementation Map

## Purpose

Map PBSA v2.0 regime-routing architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Route policy | configs/routing/regime_route_policy_v2_0.json |
| Route registry | src/pba/routing/route_registry.py |
| Route selector | src/pba/routing/route_selector.py |
| Route eligibility | src/pba/routing/route_eligibility.py |
| Routed runner | src/pba/routing/routed_runner.py |
| Route evidence | src/pba/evidence/route_evidence.py |
| Routed suite report | src/pba/evidence/routed_suite_report.py |
| CLI command | python -m pba.cli routed-suite-report |
| Reports | reports/routing/ |

## Current decision

route_by_regime

## Kernel mutation

Disabled. Routing is not global kernel replacement.
