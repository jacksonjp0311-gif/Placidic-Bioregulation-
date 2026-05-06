from __future__ import annotations


ALLOWED_CLAIMS = [
    "PBSA is a computational regime-routing and validation framework.",
    "PBSA emits internal routed validation reports.",
    "PBSA emits external-domain validation reports.",
    "PBSA emits stress/adversarial validation reports.",
    "PBSA emits calibration reports.",
    "PBSA emits evidence package reports.",
    "PBSA emits replay audit reports.",
    "PBSA preserves no automatic kernel replacement.",
    "PBSA preserves no kernel mutation.",
    "PBSA exposes downgrade locks and failure surfaces.",
    "PBSA can be audited from config to report to ledger to README/RCC anchors.",
]

FORBIDDEN_CLAIMS = [
    "PBSA is biological validation.",
    "PBSA is medical guidance.",
    "PBSA proves a physiological mechanism.",
    "PBSA proves universal bioregulation.",
    "PBSA is clinical safety evidence.",
    "PBSA automatically replaces the active kernel.",
    "PBSA proves PBA is universally superior.",
    "PBSA removes need for manual review.",
]


def build_claim_boundary_table() -> dict:
    return {
        "allowed_claims": ALLOWED_CLAIMS,
        "forbidden_claims": FORBIDDEN_CLAIMS,
        "caution": "Release-candidate readiness is public audit readiness only, not biological or medical validation.",
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
    }


def claim_boundary_valid(table: dict) -> bool:
    forbidden_text = " ".join(table.get("forbidden_claims", [])).lower()
    allowed_text = " ".join(table.get("allowed_claims", [])).lower()
    if "medical guidance" in allowed_text:
        return False
    if "biological validation" in allowed_text:
        return False
    return "medical guidance" in forbidden_text and "biological validation" in forbidden_text
