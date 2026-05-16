# Contesto, ruolo, output e vincoli

Quattro elementi rendono un prompt più controllabile: contesto, ruolo, output e vincoli.

## Contesto

Il contesto spiega al modello la situazione, il pubblico, le fonti e lo scopo della risposta.

Esempio:

```text
Contesto: sto preparando una guida per funzionari comunali non tecnici. Devono capire gli effetti pratici, non i dettagli teorici.
```

## Ruolo

Il ruolo orienta tono, competenza e prospettiva.

Esempio:

```text
Agisci come esperto di gestione documentale e formazione interna.
```

Il ruolo non deve sostituire le istruzioni operative. Dire "agisci come esperto" non basta: bisogna comunque dire che cosa fare.

## Output

Specificare l'output riduce ambiguità.

Esempi:

```text
Produci una tabella con colonne: tema, fonte, utilità, rischio, link.
```

```text
Rispondi in massimo 300 parole, con una conclusione iniziale e poi due paragrafi.
```

## Vincoli

I vincoli chiariscono cosa evitare e cosa rispettare.

Esempi:

```text
Usa solo le fonti fornite.
```

```text
Se una informazione non è presente, scrivi: "informazione non presente nella fonte".
```

```text
Non aggiungere sezioni nuove.
```

## Criterio pratico

Un prompt è debole quando lascia al modello troppe decisioni implicite su scopo, fonti e forma dell'output. È forte quando rende esplicite le decisioni che contano.
