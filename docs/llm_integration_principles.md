# Principi per integrazione LLM

La futura v1 della repository sara collegata a un LLM. Questo non garantisce automaticamente risposte corrette. Un LLM puo sintetizzare male, saltare fonti, sovrainterpretare chunk o presentare inferenze come fatti.

Per questo la repository deve essere progettata come sistema di controllo del contesto.

## Regola di progetto

```text
La repository recupera e vincola.
Il LLM sintetizza.
Il sistema verifica.
L'utente puo ispezionare le fonti.
```

## Flusso previsto

```text
query utente
  -> retriever trova chunk rilevanti
  -> evidence pack organizza i chunk
  -> LLM sintetizza solo dal contesto fornito
  -> evaluator controlla grounding e copertura
  -> risposta finale mostra fonti e limiti
```

## Cosa possiamo controllare

Possiamo controllare:

- quali chunk sono stati recuperati
- da quali fonti arrivano
- quali metadati hanno
- quale contesto e stato passato al LLM
- se il LLM cita source_ref o chunk_id
- se una fonte importante e stata esclusa

Non possiamo garantire al 100%:

- che il LLM interpreti sempre correttamente il bias
- che non faccia inferenze troppo forti
- che pesi tutte le fonti nel modo migliore
- che la sintesi sia sempre completa

## Formato consigliato per risposte LLM

Ogni risposta generata dovrebbe distinguere:

- evidenza esplicita nei chunk
- inferenza ragionevole
- limite o assunzione
- fonte usata

Esempio di schema:

```text
Fonte: OpenAI
Chunk usati: openai_gpt55_prompting_guide__outcome_first_001
Evidenza esplicita: ...
Inferenza ragionevole: ...
Limite: ...
```

## Guardrail prompt

Prompt base per il LLM:

```text
Usa solo i chunk forniti nell'evidence pack. Non attribuire a una fonte idee che non sono presenti nei chunk. Distingui sempre tra evidenza esplicita, inferenza ragionevole e ipotesi non verificata. Per ogni affermazione concreta, indica chunk_id o source_ref. Se una fonte non copre il tema, dillo esplicitamente.
```

## Ruolo di compare_sources.py

`compare_sources.py` non deve generare una sintesi finale libera. Deve preparare un evidence pack strutturato:

- query
- risultati ordinati
- copertura per vendor
- chunk_id
- source_ref
- testo sintetico
- istruzioni per il LLM

La generazione finale appartiene a un passaggio successivo e verificabile.
