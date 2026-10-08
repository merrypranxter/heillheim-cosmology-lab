# Evidence, attribution and citation protocol

The concordance extends the existing three-layer Atlas architecture. It adds descriptive **external evidence statuses**, not a replacement source canon.

## Provenance

- **ATLAS RECORD** — what REC, timecoded ASR or another identified recording actually states. Source texts remain provisional where FoxNote ASR or automated summaries are the only record.
- **ATLAS READING** — our or Gemini/Perplexity's interpretation, including proposed scientific analogies and connections.
- **ATLAS EXPANSION** — a newly authored branch or artistic interpretation. None of these dossiers should be reclassified as such by default.
- **DOCUMENTED EXTERNAL KNOWLEDGE** — a specific externally retrieved study, primary text or document, within its own scope.
- **RESEARCH LEAD** — a cited link or claim carried over from Perplexity/Gemini but not verified against the source in this pass.

## Evidence status

| Label | Meaning |
| --- | --- |
| established-in-field | This narrower outside statement is supported by the referenced source |
| supported-limited | Some parts supported, but evidence does not establish the Atlas's proposed extension |
| scientific-frontier | Recognized ongoing investigation or interpretation dispute |
| not-independently-verified | Evidence consulted does not establish the specific source-reported claim |
| contradicted-in-specified-form | A particular framing conflicts with source definitions or measurements; do not generalize to an entire topic |
| original-source-needed | A claim's owner, quote, date, editing state or recording identity needs primary media |

## Citation verification

Source-register rows have a **check level**: VERIFIED-READ means the page or primary-study abstract was opened in this pass and checked for the narrow assertion shown; LEAD means Perplexity listed the source but it has not yet been checked here. VERIFIED-READ does **not** certify unrelated assertions or that an entire linked PDF has been reviewed line by line.

Record **retrieval date**, publication year/date when known, precise claim scope, and persistent DOI/official URL. Never preserve expiring Perplexity S3 attachment URLs as permanent evidence. Don't use the long Perplexity numbered source list as a bibliography without reviewing its hundreds of duplications, broken links and tangential search results.

## Scientific versus source truth

An experimental paper can accurately show a cellular effect while a separate Atlas recording proposes a larger capacity. Preserve the two separate statements, then describe exactly what would bridge the gap. Negative or null findings should be specific: e.g., *the BrainEx study found no global electrocorticographic activity*, not *all research into bioelectricity is impossible*.

## Sensitive subjects

Treat allegations about actual people, companies or agencies as attributed source claims until grounded in documentation. For clinical or biological claims, compare published research; do not instruct people to attempt proposed interventions. For military or geography claims, stay at public history, not operational exploitation.

## ID handling

Use existing REC-/CLAIM-/MEC-/EVT-/Q- identifiers, exactly as stored. **UNMAPPED** means a concept appeared in secondary synthesis or source summaries but has no independently checked atomic claim yet; it is not a request to invent one. No new primary claims are minted by external research.
