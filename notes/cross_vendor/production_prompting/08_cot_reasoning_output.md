# 08 - Chain of Thought, ragionamento e delimitazione dell'output

## Definizione

La **Chain of Thought** e' una tecnica di prompting che spinge il modello a produrre passaggi intermedi di ragionamento prima della risposta finale.

La fonte Brex presenta la tecnica come utile quando il modello sbaglia compiti che richiedono calcolo, interpretazione di codice o ragionamento intermedio.

## Valore operativo

Il principio da conservare e':

```text
Quando la risposta finale richiede passaggi intermedi, puo' essere utile
chiedere al modello di scomporre il problema.
```

Casi utili:

- calcoli;
- medie;
- confronto di dati;
- interpretazione di codice;
- trasformazioni multi-step;
- uso di strumenti;
- classificazioni ambigue;
- analisi con criteri multipli.

## Aggiornamento per la repository

Questa sezione va integrata con prudenza. Nei sistemi moderni non sempre e' opportuno mostrare all'utente tutto il ragionamento del modello. E' spesso preferibile chiedere:

- una spiegazione sintetica;
- i passaggi verificabili;
- il calcolo essenziale;
- le evidenze usate;
- la risposta finale separata.

Non e' necessario esporre ogni passaggio interno.

## Delimitare ragionamento e risposta

Quando serve una parte visibile di spiegazione e una risposta finale usabile da software, si puo' delimitare l'output.

Esempio:

```json
{
  "explanation": "Ho escluso Target, sommato le altre spese e diviso per il numero di elementi considerati.",
  "final_answer": 136.77
}
```

Oppure:

```json
{
  "calculation_steps": [
    "Excluded Target expenses.",
    "Summed remaining expenses.",
    "Divided by count of remaining expenses."
  ],
  "answer": "$136.77"
}
```

## Costi

Chain of Thought o spiegazioni passo-passo consumano piu' token, aumentano latenza e costo. Vanno usate quando migliorano affidabilita' o verificabilita', non come default per ogni risposta.

Regola pratica:

```text
Chiedere ragionamento esplicito quando serve verificabilita'.
Chiedere risposta diretta quando il compito e' semplice.
```

Source ref: brex_prompt_engineering_guide#chain-of-thought
