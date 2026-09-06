"""Small safety check for obvious secret patterns before commits."""
from pathlib import Path
import re
import sys

patterns = [
    re.compile(r"(?i)(password|passwd|token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{8,}"),
    re.compile(r"(?i)authorization:\s*bearer\s+\S+"),
]
ignored = {".git", ".venv", "venv", "__pycache__"}
failed = False
for path in Path(".").rglob("*"):
    if not path.is_file() or any(part in ignored for part in path.parts):
        continue
    if path.name in {".env"}:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue
    for pattern in patterns:
        if pattern.search(text):
            print(f"Potential secret pattern: {path}")
            failed = True
            break
sys.exit(1 if failed else 0)
