# RCC Context Map

## Purpose

This file tells humans and AI agents how to understand the repository without full source ingestion.

## RCC rule

Read context in this order:

1. Root README.
2. This RCC context map.
3. Folder-local README.
4. Relevant source/config/test files.
5. Latest run, report, or ledger only when evidence is needed.

## Echo state template

Each mini README should expose:

- S: formal specification
- H: hooks and integration edges
- A: artifacts and code units
- T: theory or mathematical basis
- I: invariants
- E: examples and expected usage

## Repository context topology

Root README:
Global orientation and AI-reader instructions.

docs:
Theory, architecture, benchmark protocol, RCC map, and non-claim constraints.

configs:
Declared benchmark surface. Treat these files as the source of truth for domains, parameter defaults, baselines, calibration grid, and metric manifest.

src/pba:
Executable package. Treat this as implementation truth.

src/pba/core:
PBA runtime kernel and primitives.

src/pba/baselines:
Shared-condition comparator models.

src/pba/calibration:
Fit split and parameter search surface.

src/pba/evaluation:
Metric, identifiability, and classification surface.

src/pba/evidence:
Evidence packages, suite summaries, reports, file manifests, and ledgers.

src/pba/benchmarks:
Benchmark orchestration layer.

src/pba/cli:
Human and automation command surface.

tests:
Implementation health and documentation-contract checks.

runs:
Generated benchmark evidence. Do not hand-edit.

reports:
Generated summaries. Do not inflate interpretation.

ledgers:
Append-only continuity records.

scripts:
Local automation. No GitHub push unless explicitly requested.

## AI operating instruction

When modifying this repository, preserve both PBSA and RCC:

- PBSA governs evidence and downgrade discipline.
- RCC governs context surfaces and AI readability.
- Both are required for repository continuity.