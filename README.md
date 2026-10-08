# Heillheim Cosmology Lab

A public research and art repository mapping the **Celestial Atlas**: the self-styled cosmology published on TikTok by @hz.heillheim. We treat the material as a living belief system and map it with imaginative commitment, intellectual curiosity, and respect for the person who shared the work.

Our task is **cartography**, not diagnosis. Claims of extraordinary events or forces are documented as source statements, not adopted as established facts.

## The three-layer map

| Layer | What it is | Where |
| --- | --- | --- |
| **ATLAS RECORD** | Sourced statements from the creator's recordings and posts, with provenance and confidence | `sources/`, `data/claims.json` |
| **ATLAS READING** | Interpretation, synthesis and cross-references by contributors | `analysis/`, `cosmology/` |
| **ATLAS EXPANSION** | Contributor-authored original branches that develop Atlas elements | `atlas-expansions/` |

## Status

- **Recordings catalogued:** 56 (REC-001…REC-056) + 1 steward artifact (STW-001)
- **With working transcripts:** 31 (30 timecoded FoxNote ASR + 1 inline; confidence C)
- **Claims atomized:** see `data/claims.json` (CSV: `data/exports/claims.csv`)
- **Latest intake:** BATCH-2026-10-08 — 55 distinct recordings resolved from a 155-page FoxNote export ([index](analysis/batch-2026-10-08-index.md), [dedup report](analysis/dedup-report.md))
- **Open clarifications:** [ledger](analysis/clarification-ledger.md)

## Consent and rights

- `permission_requested: true` — the steward has publicly invited the creator to participate (see STW-001).
- `permission_confirmed: false` — approval and involvement are **not yet confirmed**.
- **2026-10-08 policy note:** full working transcripts were added to this repository at the project steward's explicit instruction. Until the creator states redistribution terms, all material remains `provisional_pending_creator_consent`; any creator request to modify or remove material supersedes this note.
- Media files (video/audio) are never committed. No private messages, no health speculation, no identifying details beyond the public handle.

## Start here

1. [Project voice charter](PROJECT-VOICE.md) — how we write
2. [Field guide](docs/FIELD-GUIDE.md) — what lives where, intake pipeline, confidence notation
3. [Batch index](analysis/batch-2026-10-08-index.md) → [study packet](ghost/study-packet-batch-2026-10-08.md)
4. [Cosmology overview](cosmology/OVERVIEW.md) → [mechanics](cosmology/mechanics.md) → [glossary](cosmology/glossary.md)
5. [Predictions](chronology/predictions.md) · [Timeline](chronology/timeline.md)
6. [Contributing](CONTRIBUTING.md) · [Data schemas](data/SCHEMA.md)

## Directory map

- `sources/` — register + per-recording cards + working transcripts (`sources/transcripts/`)
- `data/` — claims, entities, nodes/edges, timeline, predictions, glossary + `exports/` CSVs + `SCHEMA.md`
- `analysis/` — dossiers, batch index, dedup report, cross-reference map, clarification ledger
- `cosmology/`, `chronology/` — human-readable map layers
- `ghost/` — reusable study packets
- `templates/` — entry forms · `atlas-expansions/` — contributor branches
