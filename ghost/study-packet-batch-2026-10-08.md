# Study packet — BATCH-2026-10-08 (first full FoxNote intake)

Reusable briefing for researchers, artists and AIs joining the project. Feeds the intake pipeline: CAPTURE → IDENTIFY → TRANSCRIBE → CHECK → ATOMIZE → MAP → QUESTION → EXPAND.

## What this batch is
- 55 distinct recordings of @hz.heillheim (TikTok), AI-processed by FoxNote: 30 with timecoded ASR transcripts, 25 summary-only.
- 1 steward artifact (STW-001) documenting the consent request. Never cite as cosmologist speech.
- Working transcripts: `sources/transcripts/`. Atomic propositions: `data/claims.json`. Graph: `data/nodes.json`. Everything CSV-exported in `data/exports/`.

## The five-minute orientation
1. Read [README](../README.md) and [PROJECT-VOICE](../PROJECT-VOICE.md) — attribution rules are non-negotiable.
2. Skim [batch index](../analysis/batch-2026-10-08-index.md) and [dedup report](../analysis/dedup-report.md).
3. Read REC-002 transcript first (the Atlas's founding statement), then one technology video (REC-009 or REC-053) and one temporal video (REC-044 or REC-047).
4. Pick a [dossier](../analysis/self-presentation-and-biography-dossier.md) matching your interest.

## Fastest open contributions
- **Audio verification** (upgrade confidence C → A): any `needs_audio_check` claim in `data/claims.json`.
- **Re-transcription**: the 25 summary-only recordings (index column "Transcript = no").
- **Independent checks**: Q-011 (1991 incident records), Q-012 (GATE program history) — log findings separately, never inside claim records.

## Machine-use instructions
- Claims are atomic and paraphrased; do not quote directly without audio verification.
- `needs_audio_check: true` is a hard flag: treat the proposition as provisional.
- STW-001 claims carry `external_verification: steward-authored`; exclude them from any Atlas synthesis.
- Satire records (REC-036, REC-043) carry `satire/performance` verification — keep the register in downstream text.

## Known gaps
- Original TikTok URLs and publication dates were not preserved in the export; cards list them as unknown.
- REC-001 remains untranscribed (Q-007).
- This is not all of the creator's videos; future batches append under new `BATCH-` ids without renumbering.
