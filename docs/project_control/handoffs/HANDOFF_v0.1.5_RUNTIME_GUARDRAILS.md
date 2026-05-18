# Handoff finale - Cabina di regia v0.1.5

## Decisione consegnata

Arthur Shield e' stato integrato come fonte secondaria strategica per runtime guardrails and LLM safety.

## Principio da approvare

La sicurezza LLM non si ottiene solo con prompt migliori. Si ottiene con una pipeline che controlla input, contesto, output, strumenti e policy.

## Cosa cambia nella repository

La repository ora distingue piu' chiaramente tra:

- prompt engineering: come guidare il modello;
- production prompting: come assemblare contesto e output in sistemi reali;
- runtime guardrails: come controllare cio' che entra ed esce dal modello.

## Punti Arthur integrati

- validate_prompt e validate_response;
- hallucination intrinsic/extrinsic;
- claim-by-claim evaluation;
- prompt injection detection;
- jailbreaking e instruction manipulation;
- sensitive data leakage;
- PII leakage;
- direct identifier e quasi-identifier;
- regex rule e keyword rule;
- default rules e task rules.

## Punti esclusi

Benchmark numerici, costi, latenze, claim commerciali, setup tecnico e payload API completi non sono stati importati.

## Prossimo blocco consigliato

Per una futura release, valutare una fonte primaria o quasi-primaria su AI safety / prompt injection / model behavior, per confrontare Arthur con documentazione vendor o standard di sicurezza piu' generali.
