# Brex - Prompt Engineering Guide

## Posizionamento nella repository

Questa fonte viene integrata come **fonte secondaria/practitioner**. Non sostituisce le fonti primarie dei vendor di modello, ma aggiunge pattern operativi osservati nella costruzione di sistemi LLM di produzione: hidden prompts, prompt hacking, context assembly, semantic search/RAG, command grammars, formati per dati nel prompt, output consumabile da codice, ragionamento esplicito e fine-tuning come ultima risorsa.

Fonte: https://github.com/brexhq/prompt-engineering/blob/main/README.md
Licenza: MIT, vedi https://github.com/brexhq/prompt-engineering/blob/main/LICENSE

## Valore per il progetto Prompting

La guida e' utile per tradurre best practice generali in scelte implementative. Il suo focus non e' la teoria completa del prompting, ma il design di sistemi che costruiscono prompt dinamici, usano dati recuperati, producono output verificabile e gestiscono limiti di sicurezza.

Il valore aggiunto rispetto alle fonti primarie e' la prospettiva di prodotto: il prompt non e' solo istruzione, ma componente di sistema che deve essere assemblato, filtrato, validato e reso tracciabile.

## Sezioni da usare

Da conservare come conoscenza operativa:

- hidden prompts come contesto di inizializzazione non sicuro per segreti;
- prompt hacking, jailbreak, prompt injection, prompt leakage e data exfiltration;
- Give a Bot a Fish / Teach a Bot to Fish come distinzione tra context assembly e tool use;
- semantic search/RAG come fase di preparazione del contesto;
- HyDE come tecnica avanzata, da controllare;
- command grammars e scelta del livello di astrazione dei comandi;
- formati dati: liste, tabelle Markdown, JSON, XML, testo delimitato, dati relazionali;
- citation IDs e source traceability;
- output programmatico e schema validation;
- CoT/reasoning output come opzione di verificabilita', non default;
- fine-tuning come ultima risorsa, preferendo dati sintetici.

## Sezioni da non usare come riferimento operativo attuale

Non importare come conoscenza operativa corrente:

- confronto storico GPT-4 vs GPT-3.5;
- token limit specifici di modelli datati;
- disponibilita' o prezzi del fine-tuning;
- screenshot e full prompt non disponibili nel testo locale;
- sezione storica sui language model, salvo contesto generale.

## Relazioni con le fonti primarie

- Con OpenAI: rafforza retrieval budget, grounding e validazione con esempi di context assembly e output programmatico.
- Con Anthropic: si collega a isolamento di istruzioni/dati, XML/tag, untrusted content e gestione prudente dei tool.
- Con Google: estende CoT, ReAct, JSON e documentazione dei prompt verso casi applicativi di produzione.
- Con Perplexity: rende piu' tecnico il passaggio da workflow e ricerca a sistemi di automazione controllati.

## Note collegate

Vedi `notes/cross_vendor/production_prompting/00_overview.md` e successive.
