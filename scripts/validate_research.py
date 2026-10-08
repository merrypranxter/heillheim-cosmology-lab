#!/usr/bin/env python3
"""Verify internal links, provenance IDs, and research concordance coverage.

Does not verify the truth of source claims or the contents of external websites.
Standard library only; run at repo root with: python3 scripts/validate_research.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "external-context"
errors = []
def check(ok, message):
    if not ok:
        errors.append(message)
def get(path, field):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))[field]

claims = {x["id"] for x in get("data/claims.json", "claims")}
sources = {x["id"] for x in get("sources/register.json", "items")}
predictions = {x["id"] for x in get("data/predictions.json", "predictions")}
ledger = (ROOT / "analysis/clarification-ledger.md").read_text(encoding="utf-8")
questions = set(re.findall(r"\bQ-\d{3}\b", ledger))
source_register = (RESEARCH / "source-register.md").read_text(encoding="utf-8")
external_ids = set(re.findall(r"\bEXT-\d{3}\b", source_register))

expected = {
    "temporal-mechanics", "jormungandr-network",
    "mythic-compression-engine", "norse-cosmology-geology",
    "relativity-engineering", "anomalous-biology-optics",
    "bioelectricity-restoration", "consciousness-metacognition",
    "government-programs-uap", "theology-textual-history",
    "ecology-gaia", "sargasso-geopolitics",
}
actual = {p.stem for p in (RESEARCH / "dossiers").glob("*.md")}
check(expected <= actual, "missing required dossiers: " + ", ".join(sorted(expected - actual)))

pages = sorted(RESEARCH.rglob("*.md"))
check(len(pages) >= 20, "research set should include 12 dossiers and 8 shared index files")
for page in pages:
    data = page.read_text(encoding="utf-8")
    check(len(data) > 350, "research page unusually short: " + str(page))
    for pattern, valid in (
        (r"\bCLAIM-\d{3}-\d{2}\b", claims),
        (r"\bREC-\d{3}\b", sources),
        (r"\bPRED-\d{3}\b", predictions),
        (r"\bQ-\d{3}\b", questions),
        (r"\bEXT-\d{3}\b", external_ids),
    ):
        for key in re.findall(pattern, data):
            check(key in valid, "missing reference " + key + " in " + str(page))
    for link in re.findall(r"\]\(([^)]+)\)", data):
        link = link.split("#", 1)[0]
        if not link or "://" in link or link.startswith("mailto:"):
            continue
        check((page.parent / link).exists(), "broken relative link: " + str(page) + " -> " + link)

homepage = (ROOT / "README.md").read_text(encoding="utf-8")
check("research/external-context/README.md" in homepage, "main README missing research link")
if errors:
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: {len(pages)} research pages, {len(actual)} dossiers, linked provenance IDs and relative paths")
