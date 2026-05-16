# OpenAI

## Focus

Questa sezione raccoglie fonti OpenAI su prompt orientati all'esito, criteri di successo, vincoli, grounding, retrieval, citazioni, structured outputs, reasoning, tool use e validazione.

## Idee chiave

- Definire l'outcome prima del processo.
- Specificare criteri di successo e condizioni di stop.
- Usare structured outputs quando serve uno schema rigido.
- Usare citazioni e grounding quando l'accuratezza dipende da fonti.
- Separare reasoning effort, verbosity, tool design e prompt.

## Fonti principali

### Using GPT-5.5

- Tipo: official-doc
- URL: https://developers.openai.com/api/docs/guides/latest-model
- Argomenti: GPT-5.5, reasoning effort, outcome-first prompting, tool-heavy workflows, verbosity, structured outputs.
- Nota: fonte primaria per impostare prompt moderni orientati a obiettivi e criteri di riuscita.

### Prompt engineering

- Tipo: official-doc
- URL: https://developers.openai.com/api/docs/guides/prompt-engineering
- Argomenti: prompt engineering, istruzioni, esempi, struttura, ottimizzazione dei prompt.
- Nota: fonte base per la sezione generale OpenAI.

### Structured outputs

- Tipo: official-doc
- URL: https://developers.openai.com/api/docs/guides/structured-outputs
- Argomenti: JSON schema, output vincolato, validazione.
- Nota: utile per distinguere prompt testuali da output formalmente validati.

### Citation formatting

- Tipo: official-doc
- URL: https://developers.openai.com/api/docs/guides/citation-formatting
- Argomenti: citazioni, fonti, grounding.
- Nota: utile per evidence pack e risposte verificabili.

### Reasoning best practices

- Tipo: official-doc
- URL: https://developers.openai.com/api/docs/guides/reasoning-best-practices
- Argomenti: reasoning models, effort, tool use, validazione.
- Nota: utile per prompt su compiti complessi.

## Pattern da estrarre

```text
Obiettivo:
Criteri di successo:
Fonti disponibili:
Vincoli:
Output richiesto:
Stop rules:
```
