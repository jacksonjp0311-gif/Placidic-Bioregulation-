# Evolution Acceptance Policy

## Purpose

Define the minimum evidence required before a PBSA/PBA candidate kernel can replace the current champion kernel.

## Current policy

PBSA v1.1 is diagnostic-first.

Kernel mutation is disabled by default.

## Candidate acceptance requirements

A candidate kernel may replace the champion only if all are true:

1. Unit tests pass.
2. RCC README coverage tests pass.
3. Suite evidence is generated.
4. Baseline comparison is preserved.
5. Evolution report is generated.
6. Decision ledger entry is written.
7. Non-claim locks are preserved.
8. PBA-E count remains zero.
9. Candidate does not hide baseline-superior domains.
10. Candidate does not erase a prior PBA-A domain without explicit disclosure.
11. Holdout or repeat-suite evidence is non-worse where available.

## Rejection conditions

Reject candidate if:

- it weakens non-claim locks,
- removes baseline comparison,
- hides PBA-C results,
- removes RCC context,
- improves one domain while hiding losses,
- treats benchmark improvement as biological proof,
- or claims medical/clinical/mechanistic validity.

## Current v1.1 decision

Decision: preserve_champion.

Reason: diagnostic evidence generated; no candidate kernel supplied.

## Next target

PBSA v1.2 should improve regime detection quality before any kernel replacement is considered.