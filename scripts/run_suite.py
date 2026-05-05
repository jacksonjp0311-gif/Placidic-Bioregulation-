from pba.benchmarks.suite_runner import run_suite
from pathlib import Path
import json

root = Path.cwd()
runs = run_suite(root, root / "configs" / "suite_v1_0.json")
print(json.dumps({"runs": runs}, indent=2))