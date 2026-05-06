# src/pba/public_package

## Purpose

PBSA v3.0 public research package implementation.

## S - Formal specification

This layer packages PBSA as a public computational research artifact with publication abstract, evidence summary, limitations, command surface, claim boundaries, readiness checks, release tag metadata, and public package reports.

## H - Hooks

Consumes PBSA v2.0-v2.7 configs, reports, release candidate audit bundle, evidence package, replay audit, README/RCC surfaces, docs, and mini READMEs.

## A - Artifacts

- public_abstract.py
- evidence_summary.py
- public_limitations.py
- public_command_surface.py
- public_claim_boundaries.py
- public_package_readiness.py
- public_package_bundle.py

## T - Theory

Release-candidate readiness is not enough. A public PBSA package must expose evidence, commands, limitations, claim boundaries, downgrade locks, and audit surfaces.

## I - Invariants

- Public release is not biological validation.
- Public audit readiness is not medical safety.
- Public package status is not mechanism proof.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.

## E - Example

python -m pba.cli public-package-report
