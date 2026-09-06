"""IRE example: simulate first, commit only with --commit.
Validate class names/identification rules on your PDI before real writes.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from servicenow_client import ServiceNowClient

parser = argparse.ArgumentParser()
parser.add_argument("--payload", default=str(Path(__file__).with_name("sample_ire_payload.json")))
parser.add_argument("--commit", action="store_true")
args = parser.parse_args()

payload = json.loads(Path(args.payload).read_text(encoding="utf-8"))
client = ServiceNowClient()
path = "/api/now/identifyreconcile" if args.commit else "/api/now/identifyreconcile/query"
result = client.post(path, payload)
print(json.dumps(result, indent=2, ensure_ascii=False))
