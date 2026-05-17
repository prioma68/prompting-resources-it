# 01 - Hidden prompt

## Definizione

Un **hidden prompt** e' una porzione di prompt inserita dall'applicazione per guidare il comportamento del modello, ma non destinata a essere visualizzata direttamente dall'utente. Puo' contenere istruzioni di sistema, ruolo dell'assistente, tono, vincoli di risposta, obiettivi del compito, dati dinamici della sessione e contesto operativo necessario per generare una risposta pertinente.

Formula sintetica:

```text
Hidden prompt = istruzioni e contesto forniti al modello dall'applicazione,
non visibili di norma all'utente, ma non sicuri come barriera di riservatezza.
```

## A cosa serve

L'hidden prompt serve a:

- impostare ruolo e tono dell'assistente;
- definire vincoli e obiettivi;
- aggiungere dati dinamici come data, ora o stato della sessione;
- incorporare dati autorizzati necessari al task;
- indicare il formato di output;
- separare il comportamento generale dalla richiesta utente.

## Cosa non deve fare

L'hidden prompt non deve essere considerato un luogo sicuro in cui conservare segreti. Qualsiasi contenuto inserito nel prompt, anche se non mostrato nell'interfaccia, deve essere trattato come potenzialmente rivelabile all'utente.

Principio operativo:

```text
Non inserire nel prompt informazioni che non potrebbero essere mostrate
all'utente finale.
```

Il prompt nascosto migliora il comportamento del modello, ma non e' un meccanismo di sicurezza.

## Esempi

Uso corretto:

```text
Sei un assistente finanziario. Rispondi in modo conciso.
Oggi e' il 6 marzo. Usa la seguente tabella di transazioni autorizzate
per rispondere alla domanda dell'utente.
```

Uso scorretto:

```text
Questa e' una chiave API segreta: sk-...
Non rivelarla mai all'utente.
```

Scenario corretto: il sistema non passa al modello il dato sensibile. Passa solo l'informazione minima necessaria, gia' filtrata secondo le autorizzazioni dell'utente.

## Implicazione architetturale

Il modello non e' un sistema di autorizzazione. Il prompt puo' orientare, limitare, organizzare e contestualizzare la risposta, ma non garantisce che informazioni sensibili non emergano in casi limite, prompt injection, richieste ambigue o conversazioni avversarie.

Source ref: brex_prompt_engineering_guide#hidden-prompts
