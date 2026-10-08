# Data schemas

Machine-readable layer of the Celestial Atlas archive. All JSON files are UTF-8, indent 2.
CSV mirrors live in `data/exports/` with one file per JSON collection.

## claims.json
| field | type | meaning |
| --- | --- | --- |
| `id` | string | `CLAIM-<REC>-<nn>` (e.g. `CLAIM-047-02`) |
| `class` | string | `ATLAS RECORD` \| `ATLAS READING` \| `ATLAS EXPANSION` |
| `source_id` | string | `REC-###` \| `STW-001` \| `EXT-###` |
| `timecode` | string \| null | ASR block range from `sources/transcripts/` unless marked otherwise |
| `summary` | string | Atomic, paraphrased proposition (no unsourced quotes) |
| `external_verification` | string | `not verified` \| `source-reported` \| `satire/performance` \| `steward-authored` |
| `needs_audio_check` | bool | true until confirmed against original-speed audio |
| `tags` | string[] | free taxonomy (see analysis/cross-reference-map.md) |

## entities.json
`id`, `label`, `type` (structure/place/mechanism/entity*/capability/institution*/technology/phenomenon/performance/external-anchor/steward), `definition`, `source_ids`, `status` (core/mapped/performance/steward/external-anchor).

## nodes.json
Legacy graph layer. `nodes[]`: `id`, `label`, `type`, `source_ids`, `status`.
`edges[]`: `from`, `to`, `relationship`, `evidence` (**array of resolvable `CLAIM-###-##` IDs**; never slash-delimited or invented shorthand). All endpoints must match node IDs.

## timeline.json
`events[]`: `id` (`EVT-###`), `date_label` (as stated by source), `event`, `source_ids`, `kind`
(biography/conflict/cosmology/prediction/prediction-anchor/statement/archive).

## predictions.json
`predictions[]`: `id` (`PRED-###`), `source_id`, `date_context`, `described_event`, `type`, `evidence_status`.
Verification policy: freeze the prediction record before any fulfillment judgment.

## glossary.json
`terms[]`: `term`, `working_usage`, `layer` (ATLAS RECORD \| ATLAS READING), `evidence`.

## Register (sources/register.json)
`items[]`: `id`, `media_type`, `title`, `foxnote_titles`, `batch`, `analysis_status`
(`transcribed` \| `summary_only` \| `untranscribed`), `transcription_confidence`
(A audio-verified / B source-visible / C provisional / U unreviewed), `transcript_truncated`,
`source_location` (FoxNote export page span), `rights_status`.
`creator_consent` block mirrors README policy and must stay accurate.

## ID namespaces
`REC-###` recordings · `STW-###` steward artifacts (never Atlas sources) · `EXT-###` external leads
· `CLAIM-###-##` claims · `EVT-###` timeline · `PRED-###` predictions · `Q-###` clarifications
· `MEC-###` mechanisms · `EXP-###` contributor expansions · `BATCH-YYYY-MM-DD` intake batches.

## Second-pass provenance fields (2026-10-08)

- `claims[].source_voice_role`: distinguishes creator introduction, published explainer narration, FoxNote summary-only paraphrase, satirical performance, steward direct speech, and unverified post voice. The role classifies **available material**, not the underlying creator's private intent.
- `claims[].normalized_by`: optional existing claim ID identifying a more detailed restatement, without deleting earlier references.
- Summary-only claims use `timecode` text beginning `FoxNote summary` and must not be rendered as verbatim quotations.
- `register.items[].source_evidence_basis`: `foxnote_asr_provisional` / `foxnote_summary_only` / `untranscribed`.
- `register.items[].original_posted_at`, `video_url`, `video_id`, `media_sha256`, `asr_checked_by`: `null` until independently recovered; do not infer publication dates from archive date.
