# Grounding, citazioni e retrieval

Grounding significa vincolare la risposta a fonti, documenti o dati disponibili. È essenziale quando servono accuratezza, tracciabilità e controllo delle allucinazioni.

## Principi

1. Dichiarare quali fonti usare.
2. Separare ciò che è supportato da ciò che è inferito.
3. Chiedere citazioni o riferimenti precisi.
4. Stabilire cosa fare quando l'informazione manca.
5. Fermarsi quando le prove sono sufficienti.

## Prompt base

```text
Usa solo le fonti fornite. Per ogni affermazione importante, indica la fonte. Se una informazione non è presente, scrivi "informazione non presente nelle fonti". Non trasformare assenza di prova in prova di assenza.
```

## Retrieval budget

Un retrieval budget è una regola per evitare ricerche infinite. Esempio:

```text
Fai una prima ricerca ampia. Se i primi risultati rispondono alla domanda con fonti affidabili, fermati. Cerca ancora solo se manca un fatto essenziale, una data, una definizione o una fonte primaria.
```

## Evidence pack

Per ricerche importanti, produrre un evidence pack:

- domanda;
- fonti consultate;
- fatti supportati;
- citazioni;
- incertezze;
- conclusione.

## Fonte OpenAI collegata

### Citation formatting

Fonte: https://developers.openai.com/api/docs/guides/citation-formatting

Questa fonte è collegata a grounding, citazioni e retrieval perché riguarda il modo in cui una risposta deve rendere verificabili le affermazioni fondate su fonti.

Uso pratico nella repository:

- collegare ogni affermazione importante a una fonte;
- distinguere fatti supportati, inferenze e punti non verificati;
- costruire evidence pack;
- evitare che l'assenza di una fonte venga trasformata automaticamente in una conclusione.
