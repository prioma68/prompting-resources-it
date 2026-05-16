# Anthropic / Claude

## Focus

Questa sezione raccoglie fonti Claude su chiarezza, esempi, tag XML, long context, thinking, prompt chaining, tool use e sistemi agentici.

## Idee chiave

- Definire criteri di successo prima di ottimizzare il prompt.
- Usare esempi rilevanti e diversificati.
- Separare istruzioni, contesto, input ed esempi con tag espliciti.
- Per input lunghi, posizionare bene documenti e query.
- Usare tool e azioni in modo esplicito quando il modello deve agire.

## Fonti principali

### Prompt engineering overview

- Tipo: official-doc
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Argomenti: criteri di successo, test empirici, prompt da migliorare.
- Nota: utile come punto di partenza metodologico.

### Prompting best practices

- Tipo: official-doc
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-best-practices
- Argomenti: chiarezza, esempi, XML, ruolo, contesto lungo, output e tool use.
- Nota: fonte centrale per prompt complessi.

### Reduce hallucinations

- Tipo: official-doc
- URL: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Argomenti: riduzione allucinazioni, incertezza, grounding.
- Nota: utile per collegare prompt e affidabilità.

## Pattern da estrarre

```xml
<instructions>
  Spiega il compito e i vincoli.
</instructions>

<context>
  Inserisci informazioni di contesto.
</context>

<input>
  Inserisci l'input da elaborare.
</input>

<output_format>
  Specifica il formato richiesto.
</output_format>
```
