# LLM guardrails e safety tools runtime

## Ruolo della fonte Arthur Shield

Arthur Shield viene integrato come fonte secondaria strategica per la sicurezza runtime delle applicazioni LLM. Non e' una fonte primaria di prompt engineering e non serve a insegnare a scrivere prompt migliori. Serve invece a chiarire che un sistema LLM affidabile richiede controlli esterni al prompt: regole applicative, validazione degli input, validazione degli output, policy configurabili e monitoraggio.

La tesi operativa e' coerente con il principio gia' introdotto da Brex: il prompt non e' una barriera di sicurezza. Il prompt orienta il comportamento del modello, ma non deve essere l'unico punto in cui si proteggono dati, strumenti, azioni o policy.

## Perche' i guardrail runtime servono

Nei sistemi LLM in produzione, una richiesta dell'utente attraversa una pipeline. Prima del modello possono essere presenti classificazione del task, recupero documenti, filtri privacy e controlli di autorizzazione. Dopo il modello possono essere presenti validazione dello schema, controllo delle fonti, policy di sicurezza, mascheramento dati e fallback.

I guardrail runtime sono controlli eseguiti durante questa pipeline. Possono bloccare, segnalare, mascherare, richiedere conferma, fare fallback o inviare a revisione umana. Non rendono il sistema perfetto, ma spostano la sicurezza da una sola istruzione nel prompt a un insieme di controlli verificabili.

## Rule placement: validate_prompt e validate_response

Una distinzione centrale e' il posizionamento delle regole.

`validate_prompt` indica i controlli applicati prima della chiamata al modello. Serve a intercettare input sospetti o non ammessi: prompt injection, PII, dati sensibili, tossicita', richieste vietate o pattern organizzativi bloccati. In questo punto della pipeline il sistema puo' evitare che contenuti pericolosi o non autorizzati raggiungano il modello.

`validate_response` indica i controlli applicati dopo la generazione e prima di mostrare la risposta all'utente. Serve a intercettare output non fondati, dati sensibili, PII, contenuti tossici, violazioni di policy o risposte che non rispettano i vincoli del task.

La validazione del prompt puo' essere descritta come un firewall applicativo, ma non va trattata come garanzia assoluta. Ogni detector puo' avere falsi positivi e falsi negativi. Per questo il controllo runtime deve essere accompagnato da minimizzazione del contesto, autorizzazioni lato sistema, isolamento dei contenuti non fidati, validazione degli strumenti e logging.

## Matrice delle regole

Le regole non si applicano tutte nello stesso punto:

- prompt injection detection: di norma sul prompt, prima della chiamata al modello;
- hallucination detection: sulla response, con il contesto rilevante disponibile;
- sensitive data leakage: sia sul prompt sia sulla response;
- PII leakage: sia sul prompt sia sulla response;
- custom rules: sia sul prompt sia sulla response, secondo il caso d'uso;
- toxicity o content safety: sia sul prompt sia sulla response, se il prodotto lo richiede.

Questa matrice e' importante per la progettazione: una regola collocata nel punto sbagliato puo' essere inutile. Ad esempio, il controllo hallucination richiede response e contesto; il controllo prompt injection lavora invece sull'input dell'utente o sul contenuto non fidato prima che influenzi il modello.

## Hallucination detection: intrinsic vs extrinsic

Nei sistemi grounded o RAG, una risposta puo' fallire in due modi diversi.

Una **intrinsic hallucination** avviene quando la risposta contraddice direttamente il contesto fornito. Una **extrinsic hallucination** avviene quando la risposta contiene informazioni non presenti nel contesto, anche se potrebbero essere vere in senso generale.

Per questo, la valutazione non deve chiedere soltanto: "questa affermazione e' vera?". Deve chiedere anche: "questa affermazione e' supportata dalle fonti fornite?". In una pipeline RAG, una claim non supportata puo' essere problematica anche se non e' falsa nel mondo reale.

## Claim-by-claim evaluation

Una risposta lunga puo' contenere parti corrette e un singolo claim non supportato. Per questo e' utile valutare la risposta a livello di claim.

La claim-by-claim evaluation scompone la risposta in affermazioni verificabili e valuta ogni claim rispetto al contesto disponibile. I frammenti non assertivi, come formule di cortesia o risposte che dichiarano esplicitamente mancanza di informazione, possono essere esclusi dalla valutazione fattuale. Questo approccio permette di localizzare il problema: risposta interamente non fondata, claim isolato non supportato, oppure risposta coerente con il contesto.

Nel progetto Prompting, questo pattern si collega direttamente a evidence pack, `chunks.jsonl`, citazioni e verifica del grounding. Ogni claim concreto dovrebbe poter essere collegato a chunk o source_ref.

## Prompt injection detection

La prompt injection e' il tentativo di manipolare il comportamento di un LLM o di un'applicazione LLM attraverso istruzioni strategiche inserite nel prompt o in contenuti che il modello deve leggere.

Due famiglie utili sono:

- **jailbreaking**, cioe' il tentativo di far violare al modello istruzioni, policy o vincoli;
- **instruction manipulation**, cioe' il tentativo di far ignorare, rivelare o sovrascrivere il system prompt o il prompt template dell'applicazione.

Tra le tecniche comuni rientrano role play, obfuscation, payload splitting e adversarial suffix. La detection runtime puo' aiutare a bloccare input sospetti prima della chiamata al modello, ma non sostituisce isolamento dei contenuti non fidati, permessi sui tool e validazione delle azioni.

## Sensitive data leakage

La sensitive data leakage puo' avvenire in due direzioni.

Nel prompt, l'utente o l'applicazione potrebbero inviare al modello dati aziendali, segreti, informazioni confidenziali o contenuti non necessari. Nella response, il modello potrebbe restituire dati privati recuperati dal sistema ma non autorizzati per l'utente finale.

Per dati sensibili specifici di dominio, una regola puo' essere definita con esempi positivi e negativi. Gli esempi positivi mostrano cosa bloccare; gli esempi negativi aiutano a ridurre falsi positivi. Un hint descrittivo puo' chiarire il tipo di dato sensibile senza importare una regola rigida e fragile.

La formulazione corretta per la repository e' prudente: quando si usano LLM esterni, i dati inviati al modello devono essere trattati secondo le policy del provider e del contratto applicabile; in ogni caso va minimizzata l'esposizione e va evitato l'invio di dati non necessari.

## PII leakage

La PII leakage riguarda l'esposizione di informazioni personali identificabili. I controlli PII possono essere applicati sia al prompt sia alla response.

E' utile distinguere tra:

- **direct identifier**, cioe' un dato che identifica una persona da solo, come documento, numero di telefono, email personale o identificativo fiscale;
- **quasi-identifier**, cioe' un dato che puo' identificare una persona se combinato con altri dati, come nome, data di nascita, luogo, ruolo o combinazioni demografiche.

Nei sistemi con RAG, memory layer o dati utente, il controllo PII deve avvenire prima dell'inserimento nel prompt e prima della risposta finale. Una regola PII puo' includere allow list o esclusioni di entita' per evitare falsi positivi quando certi valori sono ammessi dal caso d'uso.

## Custom rules: regex e keyword

Le custom rules permettono di bloccare input o output che corrispondono a pattern definiti dall'organizzazione.

Le **regex rules** sono adatte a pattern variabili: ID interni, formati di account, token, codici, numeri di pratica o segreti tecnici. Le **keyword rules** o key phrase rules sono adatte a parole o frasi statiche: termini vietati, nomi di competitor, segreti aziendali, topic bloccati o categorie non consentite.

Queste regole non devono diventare un sostituto della progettazione del sistema. Sono efficaci per pattern noti, ma non catturano tutti i rischi semantici o contestuali.

## Default rules e task rules

Una governance utile distingue tra:

- **default rules**, applicate globalmente a tutte le applicazioni o task;
- **task rules**, applicate solo a uno specifico use case.

Le default rules definiscono una base minima comune, ad esempio prompt injection, PII e alcune regole custom organizzative. Le task rules permettono controlli specializzati per domini ad alto rischio, come finance, healthcare, legal, customer support, HR o applicazioni agentiche con tool.

Anche quando una regola restituisce solo un risultato binario, pass o fail, l'applicazione deve decidere l'azione: bloccare, avvisare, mascherare, chiedere conferma, fare fallback, ridurre il contesto, riprovare con una query piu' stretta o inviare a revisione umana.

## Limiti dei guardrail

I guardrail runtime sono necessari, ma non sufficienti. Non sostituiscono:

- autorizzazioni lato sistema;
- minimizzazione del contesto;
- separazione tra istruzioni e contenuti non fidati;
- validazione degli argomenti dei tool;
- policy per azioni rischiose;
- audit log;
- test su set di validazione;
- revisione umana quando l'impatto e' alto.

Regola finale: non proteggere con il prompt cio' che deve essere protetto dal sistema. Non delegare a un detector cio' che deve essere protetto da permessi, data minimization, isolamento e validazione applicativa.

Source refs: arthur_shield_agent_development_toolkit#rules-overview; arthur_shield_agent_development_toolkit#hallucination; arthur_shield_agent_development_toolkit#prompt-injection; arthur_shield_agent_development_toolkit#sensitive-data-leakage; arthur_shield_agent_development_toolkit#pii-leakage; arthur_shield_agent_development_toolkit#custom-rules; arthur_shield_agent_development_toolkit#rule-configuration
