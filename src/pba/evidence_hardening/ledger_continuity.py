from __future__ import annotations

import json
from pathlib import Path


REQUIRED_LEDGER_EVENTS = [
    "pbsa_v2_1_routed_validation_report_generated",
    "pbsa_v2_2_external_validation_report_generated",
    "pbsa_v2_3_stress_validation_report_generated",
    "pbsa_v2_4_calibration_report_generated",
]


def read_ledger_events(root: str | Path) -> list[dict]:
    root = Path(root)
    path = root / "ledgers" / "pba_decision_ledger.jsonl"
    events = []
    if not path.exists():
        return events

    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            events.append({"event": "unparseable_ledger_line", "raw": line})
    return events


def verify_ledger_continuity(root: str | Path) -> dict:
    events = read_ledger_events(root)
    names = [e.get("event") for e in events]
    missing = [name for name in REQUIRED_LEDGER_EVENTS if name not in names]

    return {
        "present": bool(events),
        "event_count": len(events),
        "required_events": REQUIRED_LEDGER_EVENTS,
        "missing_events": missing,
        "latest_events_verified": len(missing) == 0,
        "ledger_continuity_valid": bool(events) and len(missing) == 0,
    }
