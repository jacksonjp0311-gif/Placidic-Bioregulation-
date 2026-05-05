# ledgers

## Purpose

Append-only local continuity records.

## S - Formal specification

Ledgers track runtime, evolution, and decision events.

## H - Hooks

Written by evidence/runtime_ledger.py and local scripts.

## A - Artifacts

- pba_evolution_ledger.jsonl
- pba_runtime_ledger.jsonl
- pba_decision_ledger.jsonl

## T - Theory

Continuity requires append-only trace records.

## I - Invariants

- Do not overwrite ledger history.
- Append new events.
- Preserve local-only status until push is approved.

## E - Example

Get-Content .\ledgers\pba_runtime_ledger.jsonl