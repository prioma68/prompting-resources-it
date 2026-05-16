# Anatomia di un prompt

Un prompt robusto può essere costruito come una piccola scheda di incarico.

## Struttura base

```text
Obiettivo:
Contesto:
Ruolo:
Input:
Istruzioni:
Vincoli:
Formato dell'output:
Criteri di verifica:
```

## Esempio minimo

```text
Obiettivo: sintetizzare il documento allegato per un responsabile amministrativo.

Contesto: il lettore deve capire rapidamente novità, rischi e azioni operative.

Istruzioni: usa solo il documento fornito. Non inventare dati non presenti.

Output: produci una sintesi esecutiva, una tabella delle novità e una lista di punti da verificare.

Criteri di verifica: segnala sempre quando un'informazione non è presente.
```

## Quando accorciare

I modelli più recenti spesso funzionano meglio con prompt orientati all'esito: obiettivo, criteri di successo, vincoli e formato. Evitare processi troppo rigidi quando il percorso non è importante.

## Quando dettagliare

Serve più dettaglio quando:

- l'output deve avere uno schema stabile;
- ci sono fonti o dati da rispettare;
- il compito è ripetitivo o produttivo;
- bisogna ridurre allucinazioni;
- l'output verrà usato da software o da un workflow.

## Fonte OpenAI collegata

### Using GPT-5.5

Fonte: https://developers.openai.com/api/docs/guides/latest-model

Questa fonte è collegata all'anatomia del prompt perché rafforza un principio moderno: partire dall'esito desiderato, dai criteri di successo, dai vincoli e dalle condizioni di stop, invece di prescrivere sempre una sequenza rigida di passaggi.

Uso pratico nella repository:

- costruire prompt outcome-first;
- definire criteri di successo;
- separare obiettivo, vincoli, fonti disponibili e formato finale;
- ridurre prompt troppo lunghi o meccanici quando non servono.
