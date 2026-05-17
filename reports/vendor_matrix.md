# Vendor matrix v0.1

| Tema | OpenAI | Claude / Anthropic | Google / Gemini | Perplexity |
|---|---|---|---|---|
| Prompting generale | Outcome-first, criteri di successo, vincoli, stopping rules | Chiarezza, esempi, XML, ruolo e formato | Tassonomia completa: zero-shot, one-shot, few-shot, system/context/role | Prompt di lavoro orientati a obiettivo, contesto e workflow multi-step |
| Retrieval e grounding | Retrieval budget, citazioni, comportamento quando manca evidenza | Citazioni rilevanti nei documenti lunghi e struttura multi-documento | ReAct con search/tool e schema per strutturare input/output | Research e Spaces per fonti, note, contesto e report citati |
| Agenti e tool use | Workflow tool-heavy, preamble, validation loops | Tool use esplicito, subagent, stato, sicurezza e reversibilita | ReAct come reason-act loop con strumenti esterni | Comet Agent, agentic actions, Tasks e Shortcuts |
| Reasoning | Focus su risultato e validazione, meno su tassonomia classica | Thinking/effort e riflessione dopo tool | Step-back, CoT, self-consistency, Tree of Thoughts | Ricerca e sintesi operative, meno formalizzazione delle tecniche |
| Coding agent | Prompt per coding agent, test, build e verifica | Investigare prima di rispondere, gestione file, sicurezza azioni | Code prompting: scrivere, spiegare, tradurre, debuggare codice | Casi d'uso piu business/workflow che coding puro |
| Output strutturato | Formati finali e validazione | XML, structured outputs e tool schema | JSON repair, schema e input/output strutturati | Deliverable: dashboard, presentazioni, email, proposte |
| Workflow business | Utile come metodo di prompt e controllo | Utile per agenti e knowledge work controllato | Utile per classificare tecniche e progettare esperimenti | Fonte piu forte per casi d'uso: sales, meeting prep, lead gen, automazione |

## Sintesi

- OpenAI fornisce le regole operative per progettare prompt robusti: risultato, evidenza, retrieval budget e validazione.
- Claude fornisce la grammatica per prompt complessi e agentici: XML, long context, tool use, stato e sicurezza.
- Google fornisce la tassonomia tecnica delle tecniche di prompt engineering e dei pattern di ragionamento.
- Perplexity fornisce esempi concreti di workflow applicativi, ricerca, automazioni e deliverable.

## Implicazione per la repository

La repository dovrebbe usare Google come mappa tecnica, OpenAI come metodo di controllo della ricerca, Claude come struttura per contesto e agenti, Perplexity come catalogo di workflow applicabili.
