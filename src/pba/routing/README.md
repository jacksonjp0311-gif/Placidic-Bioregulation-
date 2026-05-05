# src/pba/routing

## Purpose

PBSA v2.0 regime-routing implementation.

## S - Formal specification

The routing layer maps domain regime evidence to admissible baseline, champion, candidate, or reject routes.

## H - Hooks

Consumes regime maps, original suite summaries, holdout summaries, and champion/challenger reports.

## A - Artifacts

- route_registry.py
- route_selector.py
- route_eligibility.py
- routed_runner.py

## T - Theory

Route by evidence, not universal kernel loyalty.

## I - Invariants

- Routing is not kernel replacement.
- Candidate routes remain governed.
- Baseline routes remain valid when evidence supports them.
- Non-claim locks remain visible.

## E - Example

python -m pba.cli routed-suite-report
