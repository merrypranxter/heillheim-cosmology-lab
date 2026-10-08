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
`edges[]`: `from`, `to`, `relationship`, `evidence` (claim IDs or REC IDs).

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
