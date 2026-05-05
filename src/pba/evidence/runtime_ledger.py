from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def append_ledger(path: str | Path, event: dict) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        **event
    }
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")