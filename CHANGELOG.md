# CHANGELOG

## v0.1.5

- Integrata Arthur Shield / Arthur AI come fonte secondaria strategica per runtime guardrails e LLM safety.
- Creato 
otes/tools/llm_guardrails_and_safety_tools.md con validate_prompt, validate_response, hallucination detection, prompt injection detection, sensitive data leakage, PII leakage, custom rules e rule governance.
- Aggiornate note cross-vendor su prompt hacking/leakage, context assembly e semantic search/RAG per collegare Arthur al principio: il prompt non e' una barriera di sicurezza.
- Aggiunta fonte Arthur in sources/registry.yaml, metadata in sources/arthur/sources.yaml e nota trasformata in sources/arthur/notes/.
- Aggiunto documento Arthur in documents.jsonl, chunk sintetici e tracciabili in chunks.jsonl, e concetti guardrail/privacy/safety in concepts.jsonl.
- Aggiunti report 0.1.5_change_audit.md, 0.1.5_test_report.md ed evidence pack evidence_pack_v0.1.5_prompt_security.md.
- Aggiunto handoff release in docs/project_control/handoffs/HANDOFF_v0.1.5_RUNTIME_GUARDRAILS.md senza sostituire il protocollo generale di handoff.
- Esclusi intenzionalmente benchmark numerici, costi, latenze, claim commerciali, dettagli di setup ed esempi API completi.
## v0.1.4

- Aggiunti file di governo progetto in docs/project_control/.
- Aggiunta mappa delle conversazioni del progetto Prompting.
- Aggiunto stato corrente della repository dopo la release v0.1.3.
- Aggiunto decision log con decisioni editoriali e operative giÃ  prese.
- Aggiunto release log sintetico.
- Aggiunto protocollo standard di handoff tra conversazioni.
- Aggiunto protocollo di valutazione nuove fonti.
- Nessuna nuova fonte aggiunta.
- Nessuna modifica alla knowledge base processata.
- Nessuna modifica alla logica degli script.
## v0.1.3

- Assestata l'integrazione Brex rispetto a `conv3.txt` e al report di audit v0.1.2.
- Espansa la serie `notes/cross_vendor/production_prompting/00-09` con definizioni operative, esempi, regole difensive e schemi JSON/XML.
- Rafforzate le sezioni su hidden prompt, prompt hacking, prompt injection, prompt leakage, data exfiltration e sicurezza defense-in-depth.
- Espanso il context assembly con processo operativo, Give a Bot a Fish, minimo contesto sufficiente e collegamento a retrieval budget.
- Espansa la nota semantic search/RAG con HyDE come tecnica avanzata controllata.
- Espansa la nota command grammars con livello di astrazione, validazione dei comandi, output JSON e ReAct loop.
- Espansa la nota sui formati dati con liste, tabelle Markdown, JSON, XML, testo delimitato, dati annidati/relazionali e citation IDs.
- Espansa la nota su output programmatico con separazione messaggio umano/dati macchina, schema grounded e validazione.
- Aggiunti chunk Brex piu granulari e tracciabili in `chunks.jsonl`.
- Aggiornato `concepts.jsonl` con concetti granulari mancanti: prompt injection, data exfiltration, citation IDs, HyDE, give/teach a bot to fish, tool validation, output validation e altri.
- Aggiornati README, registry, metadata Brex, MANIFEST e test report v0.1.3.

## v0.1.2

- Integrata la guida Brex come fonte secondaria/practitioner, non primaria.
- Aggiunta voce Brex in `sources/registry.yaml` e metadata in `sources/brex/sources.yaml`.
- Aggiunto documento Brex in `data/processed/documents.jsonl`.
- Create note cross-vendor in `notes/cross_vendor/production_prompting/` da `00` a `09`.
- Aggiunti chunk sintetici e tracciabili per hidden prompt, prompt hacking, context assembly, semantic search/RAG, command grammars, data formats, output programmatico, CoT e fine-tuning.
- Aggiornato `concepts.jsonl` con concetti di production prompting.
- Aggiunto report di test `reports/v0.1.2_test_report.md`.

## v0.1.1

- Aggiornato README con stato reale del progetto.
- Aggiunta guida Windows CMD.
- Aggiunto report test v0.1.
- Aggiunti principi per integrazione LLM controllata.
- Aggiunto protocollo per nuove fonti.
- Aggiunta roadmap.
- Aggiornato `compare_sources.py` per preparare evidence pack.

## v0.1

- Creata repository seed.
- Aggiunte quattro fonti iniziali.
- Creati registry, note, chunks, concepts e reports.
- Implementato `search.py` semplice.


