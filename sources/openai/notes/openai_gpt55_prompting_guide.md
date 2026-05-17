# OpenAI - GPT-5.5 prompting guide

## Abstract

Questa fonte e' il riferimento iniziale per progettare prompt orientati al risultato. La guida insiste su obiettivi outcome-first, criteri di successo, vincoli, budget di retrieval, grounding, citazioni, stopping rules e validazione. E' particolarmente utile per progettare assistenti con strumenti, workflow di ricerca e risposte verificabili.

## Temi principali

- Outcome-first prompting: definire cosa deve essere vero alla fine, non solo quali passaggi eseguire.
- Personality e collaboration style: separare tono dell'assistente e comportamento operativo.
- Preamble per task lunghi o tool-heavy.
- Retrieval budget: regole per decidere quando cercare ancora e quando fermarsi.
- Grounding e citazioni: distinguere affermazioni supportate da fonti da formulazioni creative.
- Validation loops: chiedere al modello di controllare il proprio output quando esistono test o comandi di verifica.
- Prompt per coding agent, visual artifacts e workflow con tool.

## Concetti chiave

- Il prompt deve descrivere risultato, vincoli, evidenza disponibile e formato finale.
- Le regole assolute vanno riservate agli invarianti reali; per il resto convengono decision rules.
- Il retrieval non va usato indefinitamente: serve un budget e una regola di arresto.
- La validazione e' parte del prompt, non un ripensamento successivo.

## Domande interrogabili

- Come si imposta un retrieval budget?
- Come si struttura un prompt outcome-first?
- Quali regole aiutano un agente a fermarsi?
- Come si chiedono citazioni e grounding?
- Quali istruzioni servono per coding agent e validazione?

## Relazioni con altre fonti

- Con Claude: si integra bene con XML, long context e gestione agentica dello stato.
- Con Google: completa le tecniche classiche come few-shot, CoT, ReAct con regole operative di retrieval e validazione.
- Con Perplexity: fornisce il livello metodologico per trasformare workflow di ricerca e automazione in prompt robusti.
