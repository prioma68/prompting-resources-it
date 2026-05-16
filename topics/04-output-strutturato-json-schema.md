# Output strutturato, JSON e schema

Quando l'output deve essere letto da una persona, basta spesso una buona struttura Markdown. Quando deve essere consumato da software, serve un formato più rigido.

## Quando usare JSON

Usa JSON quando devi:

- estrarre dati;
- alimentare un database;
- confrontare risultati;
- automatizzare un passaggio;
- validare campi obbligatori.

## Esempio

```text
Estrai i dati in JSON valido con questo schema:

{
  "titolo": "string",
  "autore": "string",
  "argomenti": ["string"],
  "livello_affidabilita": "ufficiale | pratica | accademica | da_verificare",
  "note": "string"
}
```

## Attenzione

Nei sistemi API moderni, quando disponibile, è preferibile usare funzionalità native di structured outputs o schema validation invece di descrivere tutto lo schema nel prompt. Nel prompt resta comunque utile spiegare scopo, significato dei campi e criteri di compilazione.

## Regola editoriale

Se l'output ha valore operativo, chiedi anche una sezione `assunzioni` o `punti_da_verificare`.

## Fonte OpenAI collegata

### Structured outputs

Fonte: https://developers.openai.com/api/docs/guides/structured-outputs

Questa fonte è collegata agli output strutturati perché chiarisce quando non basta chiedere al modello di "rispondere in JSON", ma serve progettare un formato stabile, validabile e adatto a essere consumato da software.

Uso pratico nella repository:

- distinguere output leggibili da persone e output consumabili da software;
- collegare JSON, schema e validazione;
- mostrare perché gli output strutturati riducono ambiguità;
- costruire prompt riutilizzabili per estrazione dati, classificazione e automazioni.
