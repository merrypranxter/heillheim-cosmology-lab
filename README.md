# Heillheim Cosmology Lab

A public research and art repository mapping the **Celestial Atlas**: the Celestial Atlas described in videos published by @hz.heillheim. We treat the material as a living belief system and map it with imaginative commitment, intellectual curiosity, and respect for the person who shared the work.

Our task is **cartography**, not diagnosis. Claims of extraordinary events or forces are documented as source statements, not adopted as established facts.

## The three-layer map

| Layer | What it is | Where |
| --- | --- | --- |
| **ATLAS RECORD** | Sourced statements from the creator's recordings and posts, with provenance and confidence | `sources/`, `data/claims.json` |
| **ATLAS READING** | Interpretation, synthesis and cross-references by contributors | `analysis/`, `cosmology/` |
| **ATLAS EXPANSION** | Contributor-authored original branches that develop Atlas elements | `atlas-expansions/` |

## Status

- **Recordings catalogued:** 56 (REC-001…REC-056) + 1 steward artifact (STW-001)
- **With working transcripts:** 31 (30 timecoded FoxNote ASR + 1 inline; provisional confidence C); five ASR records have known text cutoffs (REC-003/004/010/014/031).
- **Claims atomized:** 127 including second-pass repairs; see `data/claims.json` (CSV: `data/exports/claims.csv`)
- **Latest intake:** BATCH-2026-10-08 — 55 provisionally distinct recordings catalogued from a 155-page FoxNote export ([index](analysis/batch-2026-10-08-index.md), [dedup report](analysis/dedup-report.md))
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
6. **[External Context Concordance](research/external-context/README.md)** — 12 subject dossiers connecting Atlas terms to Norse sources, geology, experimental science, historical programs, ethics, ecology and other real-world research; includes an evidence matrix and citation register.
7. [Contributing](CONTRIBUTING.md) · [Data schemas](data/SCHEMA.md)

## Directory map

- `sources/` — register + per-recording cards + working transcripts (`sources/transcripts/`)
- `data/` — claims, entities, nodes/edges, timeline, predictions, glossary + `exports/` CSVs + `SCHEMA.md`
- `analysis/` — dossiers, batch index, dedup report, cross-reference map, clarification ledger
- `cosmology/`, `chronology/` — human-readable map layers
- `research/external-context/` — **ATLAS READING**: verified external reference register, master concept crosswalk, research-method guide, 12 scholarly context dossiers and research gaps
- `ghost/` — reusable study packets
- `templates/` — entry forms · `atlas-expansions/` — contributor branches

## External knowledge concordance

The [External Context and Conceptual Concordance](research/external-context/README.md) links the creator's source records to historical texts, public documents and scientific research **without merging these into the original ATLAS RECORD**. It includes a [master concept index](research/external-context/master-concordance.md), [twelve research dossiers](research/external-context/dossiers/), [external citation register](research/external-context/source-register.md), [verification matrix](research/external-context/verification-matrix.md), and [research gaps](research/external-context/research-gaps.md).

**Research intake (2026-10-08):** Gemini concept extraction + steward-supplied Perplexity Deep Research. The latter did not directly inspect original repository IDs; our concordance corrects that and marks unchecked references as leads. Reviewed external sources are labelled VERIFIED-READ only within the narrow claim checked. This is a working scholarly apparatus, not independent confirmation of all source-reported mechanisms.

## Source fidelity notes (2026-10-08)

An independent pass corrected mistaken descriptions, transcript-completeness metadata, an inverted wildlife statistic, mislabeled narrator voice and graph/prediction exports. **The 55-record intake deduplication remains provisional**: REC-007 may combine two posts; original TikTok IDs and dates were not preserved. Summary-only records are explicitly weaker source evidence than timecoded ASR. For diagnostics and remaining questions, see [`analysis/source-fidelity-repair-log.md`](analysis/source-fidelity-repair-log.md) and the [clarification ledger](analysis/clarification-ledger.md).

## External contextual research intake (2026-10-08)

A Perplexity Deep Research concordance and attached Gemini concept extraction were reconciled with the actual source-record IDs rather than pasted as first-person creator statements. The added [research companion](research/external-context/README.md) distinguishes documented outside literature, useful analogies, provisional source attributions, and proposed connections that current evidence does not establish. All original source cards and claims remain intact. The initial edition is a reference map, **not** independent verification of every citation in the original 300+ search-result bibliography.
