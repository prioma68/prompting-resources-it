# Agentic workflows e tool use

Un workflow agentico è un processo in cui il modello non produce solo testo, ma pianifica, usa strumenti, legge file, cerca informazioni, aggiorna risorse o coordina più passaggi.

## Quando serve

Serve quando il compito richiede:

- ricerca su più fonti;
- lettura e confronto di documenti;
- uso di strumenti;
- azioni sequenziali;
- validazione finale;
- aggiornamento di repository, file o issue.

## Prompt base

```text
Obiettivo: completa il compito end-to-end.

Vincoli:
- usa gli strumenti quando servono prove o dati aggiornati;
- non compiere azioni distruttive senza conferma;
- documenta le azioni completate;
- segnala blocchi e informazioni mancanti.

Output finale:
- azioni completate;
- risultati;
- file modificati o creati;
- prossimi passi.
```

## Sicurezza

Per azioni irreversibili o visibili ad altri, chiedere conferma:

- eliminazione di file;
- force push;
- cancellazione di branch;
- pubblicazione;
- invio email;
- modifica di dati condivisi.


## Fonte Anthropic / Claude collegata

### Tool use e sistemi agentici

Fonte: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-best-practices

Questa fonte è collegata ai workflow agentici perché tratta uso degli strumenti, azione proattiva, gestione del contesto, prompt chaining, subagenti e sicurezza nelle azioni.

Uso pratico nella repository:

- distinguere quando il modello deve solo rispondere e quando deve agire;
- rendere esplicito l'uso degli strumenti;
- evitare azioni distruttive senza conferma;
- progettare workflow multi-step con controllo finale;
- documentare azioni completate, limiti e blocchi.
