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


## Fonte OpenAI collegata

### Reasoning best practices

Fonte: https://developers.openai.com/api/docs/guides/reasoning-best-practices

Questa fonte è collegata a ragionamento, validazione e test perché aiuta a progettare prompt per compiti complessi, verifiche, uso controllato del ragionamento e controllo qualità finale.

Uso pratico nella repository:

- decidere quando serve più ragionamento;
- evitare prompt inutilmente lunghi o troppo prescrittivi;
- aggiungere criteri di verifica;
- collegare reasoning, tool use e validazione dell'output.


## Fonte Google / Gemini collegata

### Chain of Thought, self-consistency e ReAct

Fonte: https://www.kaggle.com/whitepaper-prompt-engineering

Questa fonte è collegata a ragionamento, validazione e test perché descrive tecniche come Chain of Thought, self-consistency, Tree of Thoughts e ReAct, utili per compiti complessi che richiedono ragionamento o uso di strumenti.

Uso pratico nella repository:

- distinguere compiti semplici da compiti che richiedono ragionamento multi-step;
- collegare ragionamento e verifica;
- introdurre ReAct come pattern ragiona-agisci;
- evidenziare costi, limiti e necessità di validazione.
