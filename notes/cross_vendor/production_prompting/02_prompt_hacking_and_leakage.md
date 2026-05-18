# 02 - Prompt hacking, prompt injection e leakage

## Definizione

Il **prompt hacking** indica l'insieme delle tecniche, intenzionali o accidentali, con cui un utente o un contenuto esterno tenta di far deviare un modello linguistico dalle istruzioni previste dall'applicazione.

La guida Brex aveva introdotto il principio architetturale: l'hidden prompt non e' una barriera di sicurezza e qualsiasi contenuto inserito nel prompt deve essere considerato potenzialmente rivelabile. Arthur Shield rafforza questo principio da una prospettiva runtime: i rischi di prompt injection, leakage e manipolazione delle istruzioni vanno intercettati anche con controlli esterni al prompt.

## Jailbreak

Un **jailbreak** e' un tentativo di far ignorare al modello una regola di comportamento. Puo' riguardare tono, ruolo, divieti, policy, vincoli di formato o limiti operativi.

Arthur Shield lo tratta come una famiglia di prompt injection che cerca di sovrascrivere o aggirare le istruzioni sottostanti del modello. Esempi di meccanismi sono role play, obfuscation, payload splitting e adversarial suffix.

## Prompt injection

Una **prompt injection** avviene quando istruzioni malevole o non affidabili vengono inserite nel prompt o dentro contenuti che il modello deve leggere: pagine web, email, documenti, ticket, PDF, chat, risultati di ricerca o record recuperati da un sistema RAG.

Il rischio centrale e' che il modello confonda contenuti da analizzare con istruzioni da seguire. Per ridurre il rischio, il sistema deve separare chiaramente istruzioni autorevoli, richiesta utente, contesto recuperato e contenuti non fidati.

## Instruction manipulation

Arthur Shield distingue anche la **instruction manipulation**: tentativi di far ignorare, rivelare o sovrascrivere il system prompt o il prompt template dell'applicazione. Questa categoria e' rilevante perche' collega prompt injection e prompt leakage: l'attaccante non vuole solo una risposta vietata, ma anche conoscere o manipolare le istruzioni che governano il sistema.

## Prompt leakage e data exfiltration

Il **prompt leakage** e' la fuoriuscita di istruzioni interne, messaggi di sistema, regole nascoste, contesto dinamico o dati inseriti nel prompt.

La **data exfiltration** e' il caso piu' grave: il modello rivela dati che l'utente non dovrebbe ricevere. Puo' accadere perche' quei dati sono stati inseriti nel prompt, recuperati da una fonte non filtrata, ottenuti tramite strumenti o inclusi in un contesto troppo ampio.

## Runtime detection

La prompt injection detection e' piu' adatta a `validate_prompt`, cioe' a un controllo prima della chiamata al modello. Può bloccare o segnalare input sospetti prima che influenzino il modello. Tuttavia non sostituisce:

- autorizzazioni lato sistema;
- isolamento dei contenuti non fidati;
- minimizzazione del contesto;
- validazione degli strumenti;
- conferma per azioni rischiose;
- logging e audit.

## Principio operativo

Non proteggere con il prompt cio' che deve essere protetto dal sistema. Il prompt puo' ridurre il rischio e guidare il comportamento ordinario, ma non deve essere usato come unico meccanismo di sicurezza.

## Regola pratica

Ogni volta che una fonte propone di inserire dati nel prompt, chiedersi:

1. L'utente e' autorizzato a vedere questi dati?
2. Questi dati sono necessari per il compito?
3. Possono essere minimizzati?
4. Sono separati dalle istruzioni?
5. Sono controllati contro prompt injection o leakage?
6. L'output sara' validato prima di essere usato?

Se una risposta e' negativa, il problema non va risolto aggiungendo un'altra istruzione al prompt. Va risolto a livello di sistema.

## Concetti collegati

prompt_hacking, prompt_injection_detection, jailbreak_detection, instruction_manipulation, prompt_leakage, data_exfiltration, validate_prompt, runtime_safety, untrusted_content, context_filtering, tool_validation, output_validation.

Source refs: brex_prompt_engineering_guide#prompt-hacking; arthur_shield_agent_development_toolkit#prompt-injection; arthur_shield_agent_development_toolkit#rules-overview
