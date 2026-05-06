# configs/public_package

## Purpose

Public research package declarations for PBSA v3.0.

## S - Formal specification

Public package configuration freezes PBSA into a public computational research artifact with publication abstract, evidence summary, limitations, claim boundaries, command surface, and release tag metadata.

## H - Hooks

Used by src/pba/public_package.

## A - Artifacts

- public_package_policy_v3_0.json
- public_release_manifest_v3_0.json

## T - Theory

Release-candidate readiness is not enough. A public PBSA package must expose evidence, commands, limitations, claim boundaries, downgrade locks, and audit surfaces to outside readers.

## I - Invariants

- Public release is not biological validation.
- Public release is not medical safety.
- Public package readiness is not mechanism proof.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.

## E - Example

python -m pba.cli public-package-report
