#!/usr/bin/env python3
"""Internal source, ID and export consistency; not external claim verification."""
import csv
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []
def data(p):
    return json.loads((root / p).read_text(encoding="utf-8"))
def table(p):
    with (root / p).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))
def check(value, message):
    if not value:
        errors.append(message)
def ids(items, key="id"):
    a = [x[key] for x in items]
    check(len(a) == len(set(a)), "duplicate IDs in " + key)
    return set(a)

reg = data("sources/register.json")["items"]
claims = data("data/claims.json")["claims"]
graph = data("data/nodes.json")
pred = data("data/predictions.json")["predictions"]
timeline = data("data/timeline.json")["events"]
glossary = data("data/glossary.json")["terms"]
entities = data("data/entities.json")["entities"]
source_ids = ids(reg)
claim_ids = ids(claims)
node_ids = ids(graph["nodes"])
for c in claims:
    check(c["source_id"] in source_ids, c["id"] + " has missing source")
    check(bool(c.get("source_voice_role")), c["id"] + " missing voice role")
    if c.get("normalized_by"):
        check(c["normalized_by"] in claim_ids, c["id"] + " bad normalized_by")
for node in graph["nodes"]:
    for src in node.get("source_ids", []):
        check(src in source_ids, node["id"] + " unknown source " + src)
for edge in graph["edges"]:
    check(edge["from"] in node_ids and edge["to"] in node_ids,
          "dangling graph endpoints " + edge["from"] + "/" + edge["to"])
    evidence = edge.get("evidence")
    check(isinstance(evidence, list) and bool(evidence), "edge lacks evidence array")
    if isinstance(evidence, list):
        for claim in evidence:
            check(claim in claim_ids, "dangling graph evidence " + claim)
for rec in reg:
    check(bool(rec.get("source_evidence_basis")), rec["id"] + " missing evidence grade")
    if rec["id"].startswith("REC-"):
        card = root / "sources" / ("recording-" + rec["id"][-3:] + ".md")
        check(card.exists(), "source card missing " + rec["id"])
        if card.exists() and rec["analysis_status"] == "summary_only":
            text = card.read_text(encoding="utf-8")
            check("FoxNote ASR blocks (original speed presumed" not in text,
                  "summary-only card implies ASR " + rec["id"])
for rid in ("REC-003", "REC-004", "REC-010", "REC-014", "REC-031"):
    check(next(r for r in reg if r["id"] == rid)["transcript_truncated"],
          rid + " cutoff unmarked")
for path, things, key in (
    ("data/exports/sources.csv", reg, "id"),
    ("data/exports/claims.csv", claims, "id"),
    ("data/exports/predictions.csv", pred, "id"),
    ("data/exports/timeline.csv", timeline, "id"),
    ("data/exports/glossary.csv", glossary, "term"),
    ("data/exports/entities.csv", entities, "id"),
):
    check({r[key] for r in table(path)} == ids(things, key),
          path + " out of sync")
source_csv = {x["id"]: x for x in table("data/exports/sources.csv")}
for rec in reg:
    check(source_csv[rec["id"]]["source_evidence_basis"] == rec["source_evidence_basis"],
          rec["id"] + " CSV evidence grade mismatch")
    if "transcript_truncated" in rec:
        check(source_csv[rec["id"]]["transcript_truncated"] ==
              str(rec["transcript_truncated"]),
              rec["id"] + " CSV cutoff mismatch")
edge_rows = table("data/exports/nodes_edges.csv")
check(sum(r["record_type"] == "node" for r in edge_rows) == len(graph["nodes"]),
      "graph CSV nodes mismatch")
check(sum(r["record_type"] == "edge" for r in edge_rows) == len(graph["edges"]),
      "graph CSV edges mismatch")
def markdown_ids(path, prefix):
    return set(re.findall(r"^\|\s*(" + prefix + r"-\d+)\s*\|",
                          (root / path).read_text(encoding="utf-8"), re.M))
check(markdown_ids("chronology/predictions.md", "PRED") == ids(pred),
      "prediction ledger mismatch")
check(markdown_ids("chronology/timeline.md", "EVT") == ids(timeline),
      "timeline ledger mismatch")
c = next(x for x in claims if x["id"] == "CLAIM-012-03")
check("75%" in c["summary"] and "exterminated" in c["summary"],
      "wildlife statement regression")
a = (root / "sources/recording-002.md").read_text(encoding="utf-8")
b = (root / "sources/recording-005.md").read_text(encoding="utf-8")
def desc(s):
    return s.split("## Source description", 1)[1].split("## Verified wording", 1)[0]
check(desc(a) != desc(b), "REC-002/005 descriptions crossed")
if errors:
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    sys.exit(1)
print("PASS:", len(reg), "sources;", len(claims), "claims;",
      len(graph["nodes"]), "nodes;", len(graph["edges"]), "edges;",
      len(pred), "predictions;", len(timeline), "timeline events;",
      len(glossary), "glossary terms")
