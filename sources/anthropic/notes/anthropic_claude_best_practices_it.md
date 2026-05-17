# Anthropic Claude - Migliori pratiche di prompting

## Abstract

Questa fonte e' il riferimento iniziale per strutturare prompt chiari, lunghi, multi-documento e agentici. E' forte su XML, esempi few-shot, long context, tool use, thinking/effort, subagent, sicurezza delle azioni e gestione dello stato in sessioni estese.

## Temi principali

- Chiarezza e specificita' del compito.
- Esempi rilevanti, diversi e strutturati.
- Tag XML per separare istruzioni, contesto, documenti, input e output.
- Prompting con contesto lungo: documenti sopra, query e istruzioni sotto.
- Uso degli strumenti: istruzioni esplicite su quando agire e quando solo suggerire.
- Thinking / effort: calibrare profondita' e costo.
- Sistemi agentici: stato, subagenti, sicurezza, reversibilita'.

## Concetti chiave

- I tag XML sono un formato naturale per corpus multi-documento.
- Le azioni irreversibili o visibili ad altri devono essere trattate diversamente da edit locali e reversibili.
- I subagenti sono utili quando i task sono paralleli o indipendenti, meno utili per operazioni semplici e sequenziali.
- Nei workflow lunghi serve persistenza dello stato: note, file JSON, progress log o git.

## Domande interrogabili

- Quando conviene usare XML nei prompt?
- Come strutturare documenti multipli in un prompt lungo?
- Come guidare l'uso degli strumenti?
- Come bilanciare autonomia e sicurezza di un agente?
- Quando usare subagent invece di un singolo agente?

## Relazioni con altre fonti

- Con OpenAI: combina outcome-first e retrieval budget con struttura XML e tool-use policy.
- Con Google: collega ReAct e tecniche di ragionamento a workflow agentici piu' controllati.
- Con Perplexity: fornisce struttura per trasformare casi d'uso operativi in agenti con stato e sicurezza.
