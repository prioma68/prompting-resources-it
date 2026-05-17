# 00 - Pattern di prompting per sistemi LLM in produzione

Queste note raccolgono pattern di prompt engineering orientati alla costruzione di sistemi LLM in produzione. L'obiettivo non e' spiegare solo come scrivere una buona istruzione, ma come progettare il prompt come parte di un sistema: gestione del contesto, dati dinamici, ricerca semantica, interfacce con strumenti, output strutturati, citazioni e sicurezza.

La guida Brex viene integrata come fonte secondaria/practitioner. Non sostituisce le fonti primarie dei vendor di modello, ma aggiunge una prospettiva di prodotto: come trasformare il prompting in architettura applicativa.

## Prompt come componente di sistema

Brex propone un'analogia utile: il prompt puo' essere visto come una forma di codice sorgente che il modello interpreta. L'analogia non va presa alla lettera, perche' un LLM non esegue istruzioni come un programma deterministico. Resta pero' utile per capire che il prompt orienta il comportamento del modello, stabilisce il contesto e delimita lo spazio delle risposte possibili.

Il prompt engineering serve perche' i modelli linguistici sono sistemi non deterministici. Non fanno semplicemente cio' che e' stato detto loro. Tendono a completare, inferire, associare, generalizzare e talvolta deviare se non sono guidati in modo adeguato. Per questo il prompt deve tener conto del modello usato, della complessita' del compito, dei dati disponibili, dei limiti del contesto, della necessita' di affidabilita' e dell'eventuale uso di strumenti.

## Dimensioni da progettare

Nei sistemi reali, il prompt engineering comprende almeno sette dimensioni:

1. definire il comportamento del modello;
2. incorporare contesto dinamico;
3. recuperare informazioni pertinenti;
4. separare istruzioni, dati e fonti;
5. fornire strumenti o comandi controllati;
6. produrre output leggibili da software;
7. ridurre rischi di leakage, injection e uso improprio degli strumenti.

## Due famiglie operative

Queste note distinguono due famiglie principali di approcci:

- **Give a Bot a Fish**: fornire direttamente al modello il contesto necessario;
- **Teach a Bot to Fish**: fornire al modello strumenti, comandi o procedure per recuperare informazioni e compiere azioni controllate.

La prima strategia e' generalmente piu' affidabile quando il sistema conosce gia' i dati necessari. La seconda e' piu' potente quando il compito richiede esplorazione, recupero, calcolo, azione o interazione con sistemi esterni.

## Regola di integrazione nella repository

La guida Brex va usata per pattern di produzione, non per informazioni correnti su modelli, prezzi, token limit o disponibilita' di funzionalita'. Le sezioni storiche o vendor-specific datate restano contesto, ma non diventano principi operativi.

Source ref: brex_prompt_engineering_guide#why-do-we-need-prompt-engineering
