# Prompting Resources IT

Repository ragionata di fonti, guide, documentazione ufficiale e pattern pratici sul prompt engineering.

L'obiettivo non è raccogliere link in modo indiscriminato, ma costruire una biblioteca ordinata: ogni fonte entra sotto un argomento, con una breve scheda che spiega perché è utile, a quale vendor o autore si riferisce, che tipo di fonte è e quando va aggiornata.

## Percorso consigliato

1. [Cos'è il prompting](topics/00-cos-e-il-prompting.md)
2. [Anatomia di un prompt](topics/01-anatomia-di-un-prompt.md)
3. [Contesto, ruolo, output e vincoli](topics/02-contesto-ruolo-output-vincoli.md)
4. [Zero-shot, one-shot e few-shot](topics/03-esempi-zero-shot-one-shot-few-shot.md)
5. [Output strutturato, JSON e schema](topics/04-output-strutturato-json-schema.md)
6. [Grounding, citazioni e retrieval](topics/05-grounding-citazioni-retrieval.md)
7. [Ragionamento, validazione e test](topics/06-ragionamento-validazione-e-test.md)
8. [Agentic workflows e tool use](topics/07-agentic-workflows-e-tool-use.md)

## Documentazione per vendor

### OpenAI

Fonti su prompt orientati all'esito, criteri di successo, vincoli, grounding, retrieval, citazioni, structured outputs, reasoning, tool use e validazione.

- [Scheda OpenAI](vendors/openai.md)

### Anthropic / Claude

Fonti su chiarezza delle istruzioni, esempi, tag XML, long context, thinking, prompt chaining, tool use e sistemi agentici.

- [Scheda Claude](vendors/anthropic-claude.md)

### Google / Gemini

Fonti su prompt design, prompt engineering, task, system instructions, few-shot examples, contextual information e parametri di generazione.

- [Scheda Google Gemini](vendors/google-gemini.md)

### Perplexity

Fonti su prompting applicato al lavoro: ricerca, sintesi, Spaces, workflow multi-step, automazione, report, dashboard e produttività.

- [Scheda Perplexity](vendors/perplexity.md)

## Guide pratiche e fonti complementari

Questa sezione raccoglie fonti non ufficiali ma utili: repository GitHub, guide operative, esempi aziendali, pattern ricorrenti e materiali didattici.

- [Brex Prompt Engineering Guide](practical-guides/brex-prompt-engineering.md)
- [Prompt patterns](practical-guides/prompt-patterns.md)

## Registro delle fonti

Il file [registry/sources.yaml](registry/sources.yaml) è il catalogo centrale. Ogni fonte dovrebbe indicare:

- identificativo stabile;
- titolo;
- autore o vendor;
- tipo di fonte;
- argomenti trattati;
- URL;
- stato della fonte;
- note editoriali.

## Criteri editoriali

Una fonte può essere inclusa se aiuta a chiarire un concetto, documentare una tecnica, confrontare vendor, migliorare prompt reali o costruire workflow affidabili.

Classificazione consigliata:

- `official-doc`: documentazione ufficiale del vendor;
- `whitepaper`: documento tecnico o paper divulgativo;
- `practical-guide`: guida pratica o tutorial;
- `github-repo`: repository con esempi o materiali;
- `academic-paper`: articolo scientifico;
- `article`: articolo divulgativo;
- `course`: corso o tutorial strutturato.

## Regola anti-confusione

Questa repository non deve copiare integralmente le fonti. Deve creare schede sintetiche, link, tassonomie, criteri di qualità e note operative. Il contenuto originale resta presso la fonte.
