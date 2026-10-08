# Second-pass source-fidelity repair log — 2026-10-08

**Status:** Source-to-repository audit and programmatic corrections against the steward-supplied `Hz.pdf` (155-page FoxNote export). **Not** an independent verification of the physical, historical, biological or political claims made in the recordings.

## Completed corrections

1. **Cross-wired record (REC-002):** Replaced its incorrect REC-005 Part 3 source description with its actual naval/Sargasso/Celestial Atlas/consciousness themes. REC-005 retains the oracle/architect discussion.
2. **Inverted quotation (REC-012):** Corrected CLAIM-012-03: the creator *claims 75% of animal life was lost since 1975*, and separately stresses preserving what remains. This is a source-reported figure, not an independently verified measurement.
3. **Incomplete ASR:** Marked REC-003 and REC-004 incomplete, joining previously flagged REC-010, REC-014 and REC-031; synchronized transcript headers, source cards, source register, CSV, README and batch index. A truncated FoxNote excerpt is not proof that the original recording ends there.
4. **Clipped descriptions:** Replaced the source-description fields that were hard-truncated at approximately 1,200 characters with full, bounded descriptions in REC-002, 004, 005, 008, 009, 010, 017, 018, 025, 028, 034, 036, 039, 044 and 056.
5. **Ambiguous source merge:** REC-007 contains (A) a drowned-grubs preparation summary and (B) a later interaction transcript. They are only **candidate segments**, not established as one or two videos. The batch's 55-record count remains *provisional*.
6. **Speaker and evidence provenance:** All claims now carry a `source_voice_role`. Creator introductions are distinguished from published explainer narration, FoxNote-only paraphrases, and performance. All 25 summary-only cards explicitly state the absence of transcript evidence; the full-voice verification remains pending original videos.
7. **Restored atomic propositions:** Claims increased **99 → 127**. Important recovered lines cover regional bloodline authority; oracle/architect polarity; tri-sensor detection; MCE's five pillars and disciplines; two-way Grid/AI forecasting; Gaia as a distinct information source; timeline 14 to 15 information transfer; dream restoration sequence; two stages of metacognition; and the nuanced legal questions in REC-013. These additions document the source's account, not external establishment.
8. **Misattributed geology / MCE:** REC-011's published explainer uses **last glacial maximum** for Ymir, while REC-030/038 FoxNote-only summaries describe **Snowball Earth**. The Atlas stores both as distinct claims/events with Q-020 unresolved. Genesis 1/post-Chicxulub material is attributed to **REC-011**, not imported into REC-038 without source support.
9. **Predictions parity:** Restored PRED-001/002 in JSON/CSV so all nine IDs match the written ledger; they are explicitly associated with the broader PRED-003 and must not be double-counted as independent forecasts.
10. **Graph consistency:** Repaired the nonexistent `REC-002-claims` node and malformed `CLAIM-002-12/13`-style evidence IDs. Every edge now contains an array of individually resolvable claim IDs. Added source-backed nodes/edges for recovered mechanics.
11. **Export/indices parity:** Regenerated claims, predictions, source-register, graph, glossary and timeline CSVs; expanded schema notes, cross-reference map, glossary, and mechanisms ledger.
12. **Provenance and open questions:** Added Q-019–Q-023 on MCE authorship, Ymir chronology, grub-video boundaries, multi-speaker attribution and legal questions. The original post IDs/dates/audio hashes are explicitly unknown rather than invented.

## Validation

Run from the repository root:

```sh
python3 scripts/validate_atlas.py
```

The script checks unique IDs, claim and graph references, source-register evidence grades, CSV↔JSON mirrors, prediction/timeline Markdown↔JSON parity, known ASR cutoffs, and source-card label consistency.

## Still requires original video access / creator input

- **REC-007 A/B identity:** original media IDs, TikTok URLs and runtimes. No reliable automated split can be made from this PDF alone.
- **25 summary-only sources:** recover post audio and publish accurate timecoded transcripts. All source quotations remain provisional until original-speed listening.
- **Unknown metadata:** actual post dates, URLs, hashes, and licensing/redistribution preferences; do not infer from FoxNote archive date.
- **Source voice and authorship:** establish which explainer passages, MCE terminology and Moon narrative details originated with the creator versus published auxiliary narration (Q-014, Q-019, Q-022).
- **External verification:** no empirical tests of claims, forecast adjudications, public-record corroboration or regulated-technology assessment was performed here.

## Editorial boundary

`ATLAS RECORD` = what a recording/summary says. `ATLAS READING` = contributor interpretation with references. `ATLAS EXPANSION` = original added material. No unsourced additions should be promoted to an originator quotation; no source claim is automatically treated as independently verified.
