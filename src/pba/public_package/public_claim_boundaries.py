from __future__ import annotations


ALLOWED_PUBLIC_CLAIMS = [
    "PBSA is a computational regime-routing and validation framework.",
    "PBSA includes route selection and routed validation.",
    "PBSA includes external-domain toy validation.",
    "PBSA includes stress/adversarial toy validation.",
    "PBSA includes threshold calibration with caution.",
    "PBSA includes evidence package hardening.",
    "PBSA includes reproducibility replay.",
    "PBSA includes release-candidate audit packaging.",
    "PBSA preserves no automatic kernel replacement.",
    "PBSA preserves no kernel mutation.",
]

FORBIDDEN_PUBLIC_CLAIMS = [
    "PBSA is medical guidance.",
    "PBSA is biological validation.",
    "PBSA proves a physiological mechanism.",
    "PBSA proves universal bioregulation.",
    "PBSA is clinical safety evidence.",
    "PBSA should be used for treatment decisions.",
    "PBSA automatically replaces the active kernel.",
    "PBSA proves PBA is universally superior.",
]


def build_public_claim_boundary_table() -> dict:
    return {
        "allowed_public_claims": ALLOWED_PUBLIC_CLAIMS,
        "forbidden_public_claims": FORBIDDEN_PUBLIC_CLAIMS,
        "public_caution": "Public package readiness is computational audit readiness only.",
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
    }


def public_claim_boundaries_valid(table: dict) -> bool:
    allowed = " ".join(table.get("allowed_public_claims", [])).lower()
    forbidden = " ".join(table.get("forbidden_public_claims", [])).lower()

    if "medical guidance" in allowed:
        return False
    if "biological validation" in allowed:
        return False
    if "automatically replaces" in allowed:
        return False

    required_forbidden = [
        "medical guidance",
        "biological validation",
        "physiological mechanism",
        "clinical safety",
        "treatment decisions",
    ]

    return all(item in forbidden for item in required_forbidden)
