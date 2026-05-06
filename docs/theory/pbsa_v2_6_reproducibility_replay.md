# Codex Delta Phi - PBSA v2.6 Reproducibility Replay

## Status

Canonical PBSA v2.6 reproducibility replay layer.

## Purpose

PBSA v2.6 replays the evidence package from source configs and verifies that decisions, locks, report schemas, failure surfaces, ledger continuity, RCC anchors, and drift status reproduce.

## Core invariant

Evidence packaging is not enough. A mature PBSA system must replay its evidence package.

## Added surfaces

- replay policy config
- replay artifact manifest
- replay runner
- decision replay comparator
- hash drift detector
- replay lock verifier
- failure-surface replay verifier
- replay audit report

## Lock

Reproducibility replay is not biological validation. Hash stability is not truth. Replay success is not medical safety.
