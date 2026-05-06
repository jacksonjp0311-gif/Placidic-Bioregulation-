from __future__ import annotations


def compare_decision(original: dict, replayed: dict, decision_field: str = "decision") -> dict:
    original_decision = original.get(decision_field)
    replayed_decision = replayed.get(decision_field)

    status = "match" if original_decision == replayed_decision else "semantic_drift"

    return {
        "original_decision": original_decision,
        "replayed_decision": replayed_decision,
        "status": status,
        "matches": status == "match",
    }


def compare_decision_map(original_reports: dict, replayed_reports: dict, decision_fields: dict) -> dict:
    results = {}
    for key, field in decision_fields.items():
        if key not in original_reports or key not in replayed_reports:
            results[key] = {
                "original_decision": None,
                "replayed_decision": None,
                "status": "missing_report",
                "matches": False,
            }
            continue
        results[key] = compare_decision(original_reports[key], replayed_reports[key], field)
    return results


def semantic_drift_items(decision_replay: dict) -> list[dict]:
    drift = []
    for key, result in decision_replay.items():
        if result.get("status") != "match":
            drift.append({
                "report": key,
                "status": result.get("status"),
                "original_decision": result.get("original_decision"),
                "replayed_decision": result.get("replayed_decision"),
            })
    return drift
