from pba.benchmarks.suite_runner import run_suite
from pathlib import Path
import json

root = Path.cwd()
result = run_suite(root, root / "configs" / "suite_v1_0.json", compile_summary=True)
print(json.dumps(result, indent=2))