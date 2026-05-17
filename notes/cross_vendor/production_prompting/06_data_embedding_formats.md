# 06 - Formati per incorporare dati nel prompt

## Definizione

L'**embedding dei dati nel prompt** indica il modo in cui dati applicativi, documenti, tabelle, risultati di ricerca o record strutturati vengono inseriti nel contesto fornito al modello.

La scelta del formato e' importante. Lo stesso contenuto puo' essere piu' o meno comprensibile, affidabile, compatto o citabile a seconda di come viene rappresentato.

Principio generale:

```text
Il formato del contesto deve rendere chiaro al modello che cosa e' istruzione,
che cosa e' dato, che cosa e' fonte e che cosa e' output atteso.
```

## Liste semplici

Le liste semplici sono adatte a pochi attributi o oggetti brevi.

```text
- Name: Steve
- Occupation: Engineer
- Location: Seattle
```

Vantaggi: leggibili, semplici, adatte a pochi dati.

Limiti: poco compatte per molti record, poco adatte a dati relazionali, meno stabili per consumo programmatico.

## Tabelle Markdown

Le tabelle Markdown sono utili quando ci sono molti record con gli stessi campi.

```markdown
| Merchant | Date | Amount | Action |
| --- | --- | --- | --- |
| Target | Feb 2 | $84.91 | Needs receipt |
| Shake Shack | Feb 2 | $17.53 | Needs memo |
```

Vantaggi: compatte, leggibili, adatte a record omogenei, buone per confronti, utili in prompt tecnici e documentali.

Limiti: meno adatte a dati annidati, difficili con troppe colonne, possibili errori se richiedono molti join.

## JSON

JSON e' adatto a dati strutturati, annidati o destinati a elaborazione software.

```json
{
  "transactions": [
    {
      "merchant": "Target",
      "date": "2023-02-02",
      "amount": 84.91,
      "action": ["receipt", "memo"]
    }
  ]
}
```

Vantaggi: mantiene vicini chiavi e valori, gestisce bene strutture annidate, e' leggibile da software, facilita validazione ed e' utile per output programmatici.

Limiti: puo' consumare piu' token, puo' diventare verboso e richiede attenzione alla validita' sintattica.

## Testo libero delimitato

Il testo libero delimitato e' utile per documenti, email, articoli, trascrizioni o contenuti da analizzare.

```xml
<document>
Qui va il testo del documento da analizzare.
</document>
```

Vantaggi: separa il documento dalle istruzioni, aiuta il modello a capire cosa analizzare, utile per fonti lunghe.

Limiti: se il documento contiene istruzioni malevole, serve protezione da prompt injection; i delimitatori non sono una barriera di sicurezza; servono metadati e ID per citazioni affidabili.

## XML

XML e' utile per strutturare prompt complessi con sezioni diverse.

```xml
<context>
  <source id="doc_001" type="policy">
    ...
  </source>
  <source id="doc_002" type="email">
    ...
  </source>
</context>

<task>
Rispondi usando solo le fonti nel contesto. Cita gli id delle fonti usate.
</task>
```

Vantaggi: separa chiaramente istruzioni, contesto, fonti e task; consente metadati; utile per documenti multipli; migliora la leggibilita' del prompt.

## Dati annidati

Quando i dati hanno relazioni interne, JSON e' spesso la scelta migliore.

```json
{
  "user": {
    "name": "George",
    "address": {
      "city": {
        "name": "Seattle",
        "median_income": 90000
      }
    }
  }
}
```

Il modello puo' seguire relazioni semplici, ma l'affidabilita' diminuisce quando ci sono troppi livelli o troppi collegamenti impliciti.

## Dati relazionali

Quando JSON annidato diventa troppo verboso, si possono usare tabelle relazionali in Markdown con ID.

```markdown
Users
| user_id | name | address_id |
| --- | --- | --- |
| u1 | George | a1 |

Addresses
| address_id | city_id |
| --- | --- |
| a1 | c1 |

Cities
| city_id | city | median_income |
| --- | --- | --- |
| c1 | Seattle | 90000 |
```

Regola: le relazioni devono essere esplicite tramite ID.

## Citazioni e ID

Ogni elemento che potrebbe essere citato dovrebbe avere un ID stabile.

```json
{
  "id": "txn_001",
  "merchant": "Target",
  "amount": 84.91
}
```

Questo consente al modello di restituire riferimenti verificabili:

```json
{
  "answer": "Hai speso $84.91 da Target.",
  "sources_used": ["txn_001"]
}
```

## Applicazione alla repository

Nel progetto Prompting, i file `documents.jsonl`, `chunks.jsonl` e `concepts.jsonl` devono permettere recupero, confronto, citazione, tracciabilita', generazione di evidence pack e controllo delle fonti.

Ogni chunk dovrebbe avere un identificatore stabile, metadati di fonte e informazioni sufficienti per essere usato in una risposta grounded.

Source ref: brex_prompt_engineering_guide#embedding-data
