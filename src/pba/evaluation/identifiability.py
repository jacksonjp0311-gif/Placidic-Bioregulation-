from __future__ import annotations


def identifiability_report(trials: list[dict], selected_loss: float, epsilon: float = 0.02) -> dict:
    near = [t for t in trials if abs(float(t["loss"]) - selected_loss) < epsilon]
    count = len(near)

    if count <= 1:
        status = "stable"
        downgrade = False
        note = ""
    elif count <= 3:
        status = "degenerate"
        downgrade = True
        note = "Multiple near-equivalent parameter sets; parameter interpretation downgraded."
    else:
        status = "unidentified"
        downgrade = True
        note = "Many near-equivalent parameter sets; mechanism interpretation rejected."

    return {
        "identifiability_report_id": "PBSA-ID-local",
        "epsilon": epsilon,
        "near_equivalent_parameter_sets": count,
        "status": status,
        "interpretive_downgrade": downgrade,
        "downgrade_note": note
    }