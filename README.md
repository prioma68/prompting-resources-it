# AI Docs Repository - Prompting

Repository v0.1.3 per organizzare e interrogare fonti ufficiali su prompting, agenti, deep research e workflow AI.

Questa repository nasce come progetto pilota. La v0.1 e stata validata su quattro fonti seed, poi estesa con Brex come fonte secondaria/practitioner:

- OpenAI - GPT-5.5 prompting guide
- Anthropic Claude - Migliori pratiche di prompting
- Google/Gemini - Prompt Engineering whitepaper
- Perplexity - Perplexity at Work
- Brex - Prompt Engineering Guide (fonte secondaria/practitioner)

La strategia e leggera e scalabile: non trattiamo la repo come una cartella di PDF. Conserviamo metadati, note trasformate, chunk sintetici, riferimenti alle fonti e script per ricerca e preparazione di evidence pack.

## Stato attuale

Funzionante in v0.1.3:

- catalogo fonti in `sources/registry.yaml`
- note Markdown per le fonti seed e per Brex come fonte secondaria/practitioner
- corpus interrogabile in `data/processed/chunks.jsonl`
- ricerca locale con `scripts/search.py`
- filtri `--vendor`, `--topic`, `--top-k`, `--json`
- report comparativi iniziali
- test manuali eseguiti su Windows CMD
- documentazione per estendere la repo con molti PDF/link
- `compare_sources.py` come preparatore di evidence pack, non come generatore finale

Preparato ma non ancora completo:

- ingestion automatica PDF
- ingestion automatica pagine web
- BM25 reale / SQLite FTS
- vector search con embeddings
- collegamento diretto a un LLM
- verifica automatica del grounding

## Struttura principale

```text
sources/registry.yaml             # catalogo delle fonti
sources/*/notes/                  # note Markdown trasformate, una per fonte
data/processed/documents.jsonl    # metadati documento
data/processed/chunks.jsonl       # unita interrogabili
data/processed/concepts.jsonl     # concetti normalizzati
scripts/search.py                 # ricerca full-text semplice
scripts/compare_sources.py        # evidence pack per confronti tra fonti
reports/vendor_matrix.md          # confronto tra vendor/fonti
notes/cross_vendor/production_prompting/ # note practitioner su production prompting
reports/v0.1_test_report.md       # test manuali v0.1
docs/windows_quickstart.md        # uso base da Windows CMD
docs/llm_integration_principles.md # principi per aggancio LLM controllato
intake/new_sources_template.yaml  # formato per nuovi PDF/link
```

## Uso rapido su Windows

Apri la cartella `ai-docs-repository` in Esplora file, clicca la barra del percorso, scrivi `cmd` e premi Invio.

Esempio:

```bat
python scripts\search.py "ReAct agenti tool use"
```

Altri esempi:

```bat
python scripts\search.py "retrieval budget citazioni grounding"
python scripts\search.py "XML documenti lunghi contesto"
python scripts\search.py "temperature top K top P output length"
python scripts\search.py "Spaces knowledge base brand consistency"
python scripts\search.py "tool use agents" --vendor anthropic
python scripts\search.py "Comet Research Labs Spaces" --vendor perplexity
```

## Ricerca vs sintesi

`scripts/search.py` non genera una risposta finale argomentata. Recupera i chunk piu rilevanti.

Il flusso corretto e:

```text
query utente
  -> search.py recupera chunk rilevanti
  -> compare_sources.py prepara un evidence pack
  -> un LLM sintetizza usando solo quel contesto
  -> un passaggio di verifica controlla grounding e copertura
```

Regola di progetto:

```text
La repository recupera e vincola.
Il LLM sintetizza.
Il sistema verifica.
L'utente puo ispezionare le fonti.
```

## Evidence pack

Per creare un pacchetto di evidenze da passare a un LLM:

```bat
python scripts\compare_sources.py "che punto di vista hanno le fonti del progetto sul prompting, quali aspetti enfatizzano, quali bias o limiti hanno, e come si confrontano tra loro." --top-k 12
```

Per salvarlo in Markdown:

```bat
python scripts\compare_sources.py "prompting bias limiti confronto fonti" --top-k 12 --output reports\evidence_pack_prompting.md
```

## Aggiunta di nuove fonti

Quando il corpus crescera, aggiungere le fonti a blocchi piccoli e tracciabili.

Formato consigliato:

```text
Blocco fonti n. X

Vendor:
OpenAI / Anthropic / Google / Perplexity / altro

Materiali:
- file.pdf - tema
- https://... - tema

Priorita:
alta / media / bassa

Obiettivo:
es. migliorare agenti, retrieval, tools, deep research, coding

Note:
eventuali indicazioni
```

Per dettagli: `docs/source_intake_protocol.md`.

## Roadmap sintetica

- v0.1: repository seed funzionante e testata
- v0.1.1: assestamento documentale, test report, principi LLM, intake protocol
- v0.1.2: integrazione Brex come fonte secondaria/practitioner
- v0.1.3: assestamento Brex da conv3, note production prompting espanse e concetti granulari
- v0.2: ingestion assistita di PDF/link a blocchi
- v0.3: BM25/vector search e ranking migliore
- v1.0: RAG controllato con LLM, evidence pack, citazioni e verifica
