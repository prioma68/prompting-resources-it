# 03 - Context assembly

## Definizione

Il **context assembly** e' il processo con cui un'applicazione seleziona, organizza e inserisce nel prompt le informazioni necessarie perche' il modello possa rispondere correttamente.

Nei sistemi LLM in produzione, la qualita' della risposta non dipende solo dalla formulazione dell'istruzione, ma anche da quali dati vengono forniti al modello, in quale forma, con quali vincoli e con quali riferimenti.

## Perche' serve

Il modello e' statico rispetto al momento dell'addestramento: se deve usare dati correnti, dati utente, risultati di ricerca, policy aziendali o documenti interni, questi devono essere recuperati e inseriti nel contesto.

Il context assembly serve a risolvere quattro problemi:

1. il modello non conosce necessariamente dati aggiornati;
2. il modello non conosce i dati privati o applicativi dell'utente;
3. il modello puo' generare risposte plausibili ma non fondate;
4. il modello ha una finestra di contesto limitata.

Un buon context assembly deve fornire contesto pertinente, autorizzato, aggiornato, sufficiente, non ridondante, strutturato e tracciabile alla fonte.

## Processo operativo

1. Capire il compito dell'utente.
2. Identificare quali fonti servono.
3. Recuperare solo dati autorizzati e pertinenti.
4. Inserire il contesto in formato strutturato.
5. Indicare al modello come usare quel contesto.
6. Richiedere citazioni o riferimenti se la risposta e' grounded.
7. Fermare il recupero quando l'evidenza e' sufficiente.

## Give a Bot a Fish

La prima famiglia di approcci e': **Give a Bot a Fish**.

Significa fornire direttamente al modello, nel contesto, tutte le informazioni necessarie per completare il compito.

Esempio concettuale:

```text
L'utente chiede un riepilogo della propria inbox.
Il sistema recupera la lista delle transazioni aperte.
Il sistema inserisce la lista nel prompt.
Il modello sintetizza i dati e risponde.
```

Questa strategia e' utile quando il sistema conosce gia' le informazioni necessarie. E' piu' affidabile perche' riduce l'autonomia richiesta al modello: invece di chiedergli di cercare, dedurre o interrogare strumenti, gli si fornisce direttamente il materiale rilevante.

## Esempio: dashboard o inbox

Scenario: l'utente apre una dashboard e il sistema vuole generare un messaggio sintetico sulle attivita' aperte.

Il sistema puo' inserire nel prompt una tabella autorizzata:

```markdown
| Merchant | Date | Amount | Action |
| --- | --- | --- | --- |
| Target | Mar 5 | $84.91 | Needs receipt |
| Blink Fitness | Jan 17 | $20.90 | Needs receipt and memo |
```

Il modello puo' quindi produrre una sintesi. Il punto importante e' che la risposta dipende dai dati forniti nel contesto, non da conoscenza intrinseca del modello.

## Esempio: viaggio

Scenario: l'utente vuole prenotare un viaggio.

Il sistema puo':

- chiedere date e destinazione;
- cercare voli e hotel dietro le quinte;
- recuperare la travel policy aziendale;
- inserire risultati e vincoli nel prompt;
- chiedere al modello di suggerire opzioni coerenti.

Questo approccio combina dati aggiornati, preferenze dell'utente e regole aziendali.

## Contesto dinamico

Il contesto deve cambiare in risposta al compito dell'utente. Non esiste un prompt statico valido per tutte le situazioni.

Esempi di contesto dinamico:

- dati dell'utente autorizzati;
- data e ora correnti;
- posizione, se rilevante e autorizzata;
- documenti recuperati;
- risultati di ricerca;
- policy applicabili;
- stato di workflow;
- cronologia sintetizzata della conversazione;
- output di strumenti precedenti.

## Rischi

Troppo poco contesto produce risposte vaghe, incomplete o inventate.

Troppo contesto produce rumore, aumenta costi e latenza, rende piu' difficile individuare le fonti rilevanti e puo' aumentare il rischio di leakage.

Principio operativo:

```text
Inserire il minimo contesto sufficiente per rispondere bene.
```

## Relazione con sicurezza e retrieval budget

Il context assembly deve rispettare i permessi dell'utente. Non bisogna inserire nel prompt dati che l'utente non e' autorizzato a vedere.

Il collegamento con OpenAI e' il retrieval budget: recuperare abbastanza evidenza per rispondere, ma fermarsi quando il core della risposta e' supportabile. Il collegamento con Anthropic e' la separazione esplicita tra istruzioni, contesto e input. Il collegamento con Perplexity e' il lavoro multi-step in cui contesto, tool e workflow restano collegati.

Source ref: brex_prompt_engineering_guide#give-a-bot-a-fish
