# ROADMAP - Prompting Repository

## v0.1 - Seed funzionante

Stato: completata e testata.

Obiettivo: dimostrare che fonti diverse possono essere trasformate in note, chunk e ricerca locale.

Completato:

- struttura repository
- catalogo fonti seed
- note Markdown per OpenAI, Anthropic, Google, Perplexity
- `documents.jsonl`, `chunks.jsonl`, `concepts.jsonl`
- `search.py` funzionante senza dipendenze esterne
- test manuali su Windows CMD

## v0.1.1 - Assestamento

Stato: questa versione.

Obiettivo: rendere il progetto piu chiaro, replicabile e pronto per molte nuove fonti.

Incluso:

- README aggiornato con uso Windows
- report test v0.1
- principi per integrazione LLM
- protocollo per nuove fonti
- chiarimento su cosa e funzionante e cosa e placeholder
- `compare_sources.py` riposizionato come generatore di evidence pack

## v0.2 - Ingestion assistita

Obiettivo: aggiungere nuove fonti a blocchi senza rompere lo schema.

Da fare:

- completare `ingest_pdf.py` per estrazione testo PDF
- completare `ingest_web.py` per pagine ufficiali
- aggiornare `chunk_documents.py` per produrre chunk standard
- introdurre campi di tracciabilita:
  - `evidence_type`
  - `confidence`
  - `created_by`
  - `review_status`
- aggiungere test per ogni blocco fonte

## v0.3 - Retrieval migliore

Obiettivo: migliorare ranking e copertura.

Da fare:

- BM25 o SQLite FTS
- ricerca semantica con embeddings
- query expansion
- deduplicazione chunk
- scoring bilanciato tra keyword, vendor, topic, tecniche e fonte

## v1.0 - LLM collegato

Obiettivo: RAG controllato e auditabile.

Da fare:

- retriever locale
- evidence pack strutturato
- prompt vincolato per LLM
- risposta con distinzione tra evidenza esplicita e inferenza
- controllo grounding
- controllo copertura fonti
- log delle fonti passate al modello

Principio chiave:

```text
La repository recupera e vincola.
Il LLM sintetizza.
Il sistema verifica.
L'utente puo ispezionare le fonti.
```
