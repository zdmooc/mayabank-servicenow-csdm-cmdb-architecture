"""Normalize the OpenShift inventory into a neutral MayaBank model.
It deliberately does NOT guess ServiceNow class names.
"""
from __future__ import annotations
import json
from pathlib import Path

src = Path(__file__).with_name("output") / "openshift-inventory.json"
out = Path(__file__).with_name("output") / "openshift-normalized.json"
data = json.loads(src.read_text(encoding="utf-8"))

records = []
for kind, payload in data.items():
    for item in payload.get("items", []):
        meta = item.get("metadata", {})
        uid = meta.get("uid")
        if not uid:
            continue
        records.append({
            "kind": kind,
            "name": meta.get("name"),
            "namespace": meta.get("namespace"),
            "uid": uid,
            "source_name": "MAYABANK_OPENSHIFT_LAB",
            "source_native_key": f"openshift:{kind}:{uid}",
        })

out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(records, indent=2), encoding="utf-8")
print(out)
