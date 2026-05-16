# Brex Prompt Engineering Guide

## Tipo

- Categoria: github-repo / practical-guide
- URL: https://github.com/brexhq/prompt-engineering
- Fonte: Brex
- Stato: fonte complementare, non vendor ufficiale

## Perché è utile

La guida Brex è utile perché tratta il prompt engineering come pratica di progettazione per sistemi reali basati su LLM. Non è una documentazione ufficiale di un vendor, ma una fonte pratica con buoni spunti su prompt nascosti, sicurezza, dati dinamici, citazioni, JSON e consumo programmatico dell'output.

## Concetti da estrarre

### Prompt come codice sorgente

L'analogia del prompt come "source code" aiuta a spiegare che il prompt guida il comportamento del modello, ma con una differenza: il modello è non deterministico.

### Hidden prompts

Regola importante: non inserire nel prompt nascosto informazioni che non renderesti visibili all'utente.

### Embedding data

La guida distingue diversi modi per inserire dati nel prompt:

- liste semplici;
- tabelle Markdown;
- JSON;
- testo libero;
- dati annidati.

### Citazioni

Suggerisce di assegnare ID agli elementi da citare, utile per output verificabili.

### Programmatic consumption

Quando l'output deve essere usato da software, preferire formati strutturati come JSON o YAML.

## Limiti

- Alcune parti possono essere datate rispetto ai modelli più recenti.
- Le sezioni su Chain of Thought vanno reinterpretate con le pratiche moderne: meglio chiedere verifiche, metodo sintetico o output controllato, non necessariamente tutto il ragionamento.
- Non è una fonte ufficiale OpenAI, Anthropic, Google o Perplexity.

## Come usarla nella repository

Collocarla tra le fonti pratiche e citarla quando si parla di:

- progettazione di prompt per sistemi;
- sicurezza dei prompt nascosti;
- inserimento dati dinamici;
- citazioni;
- output strutturato;
- pattern applicativi.
