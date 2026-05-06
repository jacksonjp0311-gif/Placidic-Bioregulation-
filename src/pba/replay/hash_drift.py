from __future__ import annotations

import hashlib
from pathlib import Path


TIMESTAMP_DRIFT_PATH_HINTS = [
    "reports/routing/latest",
    "reports/validation/latest",
    "reports/external_validation/latest",
    "reports/stress_validation/latest",
    "reports/calibration/latest",
    "reports/evidence_packages/latest",
    "reports/replay/latest",
    "ledgers/",
]


def sha256_file(path: str | Path) -> str:
    path = Path(path)
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def classify_hash_drift(path: str, original_hash: str | None, replay_hash: str | None) -> dict:
    if original_hash == replay_hash:
        status = "match"
    elif any(hint in path.replace("\\", "/") for hint in TIMESTAMP_DRIFT_PATH_HINTS):
        status = "expected_timestamp_drift"
    else:
        status = "semantic_hash_drift"

    return {
        "path": path,
        "original_sha256": original_hash,
        "replay_sha256": replay_hash,
        "status": status,
        "drift": status != "match",
    }


def compare_hash_manifests(original_rows: list[dict], replay_rows: list[dict]) -> dict:
    replay_by_path = {row.get("path"): row for row in replay_rows}
    rows = []

    for original in original_rows:
        path = original.get("path")
        replay = replay_by_path.get(path, {})
        rows.append(classify_hash_drift(
            path=path,
            original_hash=original.get("sha256"),
            replay_hash=replay.get("sha256"),
        ))

    semantic = [row for row in rows if row["status"] == "semantic_hash_drift"]
    expected = [row for row in rows if row["status"] == "expected_timestamp_drift"]

    return {
        "hash_drift": rows,
        "semantic_drift": semantic,
        "expected_timestamp_drift": expected,
        "hash_drift_valid": len(semantic) == 0,
    }
