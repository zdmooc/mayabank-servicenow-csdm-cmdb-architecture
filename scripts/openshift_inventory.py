"""Collect a deliberately limited OpenShift inventory via the local oc CLI.
Pods are excluded by design (ADR-005).
"""
from __future__ import annotations
import json
import os
import subprocess
from pathlib import Path

KINDS = ["nodes", "namespaces", "deployments", "statefulsets", "services", "routes"]
namespace = os.getenv("OCP_NAMESPACE")

def oc_json(kind: str) -> dict:
    cmd = ["oc", "get", kind, "-o", "json"]
    if namespace and kind not in {"nodes", "namespaces"}:
        cmd.extend(["-n", namespace])
    cp = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads(cp.stdout)

inventory = {kind: oc_json(kind) for kind in KINDS}
out = Path(__file__).with_name("output")
out.mkdir(exist_ok=True)
path = out / "openshift-inventory.json"
path.write_text(json.dumps(inventory, indent=2), encoding="utf-8")
print(path)
