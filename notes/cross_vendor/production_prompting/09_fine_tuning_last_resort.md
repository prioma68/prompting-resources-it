# 09 - Fine-tuning come ultima risorsa

## Definizione

Il **fine-tuning** consiste nell'addestrare ulteriormente un modello gia' esistente su un insieme di coppie input-output, in modo da adattarlo a un compito, stile o formato specifico.

La fonte Brex presenta il fine-tuning come fallback quando prompting, esempi, struttura del contesto e output programmatici non bastano.

## Principio operativo

```text
Prima di ricorrere al fine-tuning, provare a risolvere il problema con prompt chiari,
esempi, schemi di output, recupero di contesto, strumenti e validazione.
```

## Perche' e' una scelta da valutare con cautela

Il fine-tuning puo' rendere alcuni comportamenti piu' stabili, ma introduce costi e complessita':

- richiede dataset di qualita';
- rallenta il ciclo di iterazione;
- puo' incorporare errori presenti negli esempi;
- non elimina la necessita' di contesto dinamico;
- non sostituisce autorizzazioni, retrieval e validazione;
- puo' creare rischi se si usano dati sensibili.

## Dati sintetici

Un principio importante da conservare e':

```text
Non usare dati reali sensibili o dati cliente non necessari per il fine-tuning.
Preferire dati sintetici, anonimizzati o autorizzati.
```

Il motivo e' che un modello puo' memorizzare o riprodurre parti dei dati di addestramento. Per questo la preparazione dei dati e' una fase di sicurezza, non solo di performance.

## Fine-tuning e hidden prompt

Il fine-tuning non elimina il bisogno di prompt o contesto. Anche un modello fine-tuned puo' aver bisogno di:

- dati aggiornati;
- dati utente;
- policy correnti;
- documenti recuperati;
- istruzioni di output;
- vincoli applicativi.

## Regola pratica

```text
Usare il fine-tuning per stabilizzare pattern ripetuti e ben definiti.
Non usarlo per sostituire retrieval, permessi, sicurezza o contesto dinamico.
```

## Parti datate della fonte Brex

Le affermazioni specifiche su disponibilita' del fine-tuning per modelli specifici, prezzi relativi e costi numerici non vanno importate come conoscenza operativa, perche' dipendono dal momento storico e possono cambiare.

Source ref: brex_prompt_engineering_guide#fine-tuning
