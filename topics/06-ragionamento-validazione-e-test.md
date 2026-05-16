# Ragionamento, validazione e test

Per compiti complessi non basta chiedere una risposta: bisogna chiedere anche una verifica del risultato.

## Ragionamento

Alcune tecniche storiche chiedono al modello di pensare passo passo. Nei workflow moderni, spesso è preferibile chiedere una sintesi controllata del metodo o una verifica finale, invece di pretendere tutto il ragionamento interno.

## Prompt utile

```text
Risolvi il problema. Prima di concludere, verifica la risposta rispetto a questi criteri:
- risponde alla domanda principale;
- non usa informazioni esterne non autorizzate;
- distingue fatti, inferenze e punti incerti;
- rispetta il formato richiesto.
```

## Validazione

Per output tecnici o operativi, aggiungi:

```text
Alla fine, includi una sezione "Controllo qualità" con eventuali limiti, assunzioni e punti da verificare.
```

## Test su prompt

Quando costruisci un prompt riutilizzabile, testa almeno:

- caso normale;
- caso ambiguo;
- caso con informazione mancante;
- caso limite;
- input rumoroso;
- output troppo lungo;
- richiesta fuori ambito.
