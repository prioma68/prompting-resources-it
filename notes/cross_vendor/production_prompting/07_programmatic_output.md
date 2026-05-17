# 07 - Output programmatico

## Definizione

L'**output programmatico** e' una risposta del modello progettata per essere letta non solo da una persona, ma anche da un software.

Invece di produrre solo testo naturale, il modello restituisce dati in un formato strutturato come JSON, YAML, XML, enum o uno schema con campi obbligatori.

## Perche' serve

Nei sistemi in produzione, l'output del modello puo' servire a:

- compilare campi;
- alimentare una UI;
- attivare workflow;
- creare pulsanti o azioni;
- aggiornare record;
- restituire citazioni;
- classificare richieste;
- validare decisioni;
- preparare chiamate a strumenti;
- generare evidence pack.

Per questi casi, il testo naturale non basta. Serve una struttura stabile e validabile.

## Separare messaggio umano e dati macchina

Un buon output programmatico separa cio' che l'utente deve leggere da cio' che il sistema deve usare.

```json
{
  "message": "Ho trovato due opzioni coerenti con la policy aziendale.",
  "hotel_id": "hotel_432",
  "flight_id": "flight_831"
}
```

Il sistema puo' mostrare `message` all'utente e usare `hotel_id` e `flight_id` per generare pulsanti, precompilare form o attivare passaggi successivi.

## Non esporre ID nel messaggio umano

Se gli ID servono al sistema, non devono necessariamente comparire nel testo per l'utente.

```json
{
  "message": "Ti consiglio questa combinazione di volo e hotel perche' rispetta budget e orari.",
  "flight_id": "flight_831",
  "hotel_id": "hotel_432"
}
```

Regola:

```text
Il messaggio umano deve essere chiaro; gli ID servono alla macchina.
```

## Citazioni programmatiche

Oltre ai link testuali, il modello puo' restituire una lista di fonti usate.

```json
{
  "answer": "Hai speso $188.16 da Target.",
  "sources_used": ["txn_001", "txn_014", "txn_027"]
}
```

Questo approccio e' utile quando non serve sapere esattamente quale frase dipende da quale fonte, ma e' necessario sapere quali elementi sono stati usati per produrre la risposta.

## Schema consigliato per risposte grounded

```json
{
  "answer": "Sintesi leggibile per l'utente.",
  "sources_used": ["chunk_001", "chunk_004"],
  "claims": [
    {
      "claim": "Affermazione specifica.",
      "source_ids": ["chunk_001"]
    }
  ],
  "missing_information": [],
  "confidence": "medium"
}
```

## Validazione

L'output strutturato deve essere validato lato applicazione.

Controlli minimi:

- JSON valido;
- campi obbligatori presenti;
- valori ammessi;
- ID esistenti;
- permessi rispettati;
- nessun comando non autorizzato;
- nessuna azione rischiosa senza conferma.

## Esempi

Classificazione:

```json
{
  "label": "requires_response",
  "confidence": "high",
  "reason": "The email asks for a specific confirmation by tomorrow."
}
```

Recupero con citazioni:

```json
{
  "answer": "La fonte aggiunge valore soprattutto per command grammars e output programmatici.",
  "sources_used": ["brex_command_grammar", "brex_programmatic_consumption"],
  "decision": "integrate_partially"
}
```

Azione proposta:

```json
{
  "user_message": "Posso aggiungere il memo alla ricevuta Shake Shack.",
  "proposed_action": {
    "type": "add_memo",
    "target_id": "inbox_item_123",
    "memo": "Team lunch"
  },
  "requires_confirmation": true
}
```

Regola pratica:

```text
Quando l'output deve essere usato da software, chiedere struttura, schema ed esempi.
Quando l'output e' solo conversazionale, non appesantire inutilmente la risposta.
```

Source ref: brex_prompt_engineering_guide#programmatic-consumption
