# Contributing

## Adding a source

Use `intake/new_sources_template.yaml` as the intake format. For each new source, provide:

- vendor
- title
- canonical URL, if available
- local file name, if PDF
- topic tags
- priority
- notes about why the source matters

Then update:

1. `sources/registry.yaml`
2. `sources/{vendor}/notes/{source_id}.md`
3. `data/processed/documents.jsonl`
4. `data/processed/chunks.jsonl`
5. `tests/test_queries.md` when relevant

## Chunk rules

Chunks should be transformed summaries, not long copied passages. Each chunk should have stable metadata, tags and a source reference.
