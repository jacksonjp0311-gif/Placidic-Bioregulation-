# src/pba/evaluation

## Purpose

Metrics, comparison, identifiability, and classification.

## S — Formal specification

Computes metric vectors, compares PBA to baselines, checks identifiability, and emits PBA-A/B/C/D/E classification.

## H — Hooks

Used by benchmark runner and suite summary compiler.

## A — Artifacts

- metrics.py
- identifiability.py
- classification.py

## T — Theory

Classification happens after evidence. Mixed evidence must downgrade.

## I — Invariants

- PBA-A requires PBA advantage and stable identifiability.
- PBA-C is valid when simpler baselines perform equally well or better.
- PBA-E is required for non-claim lock violation.

## E — Example

Latest suite classification is PBA-C because evidence is mixed.