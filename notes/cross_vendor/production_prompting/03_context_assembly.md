# 03 - Context assembly

## Definizione

Il **context assembly** e' il processo con cui un'applicazione seleziona, organizza e inserisce nel prompt le informazioni necessarie perche' il modello possa rispondere correttamente.

Nei sistemi LLM in produzione, la qualita' della risposta non dipende solo dalla formulazione dell'istruzione, ma anche da quali dati vengono forniti al modello, in quale forma, con quali vincoli, con quali permessi e con quali riferimenti.

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
4. Applicare controlli di minimizzazione e privacy prima del prompt.
5. Inserire il contesto in formato strutturato.
6. Indicare al modello come usare quel contesto.
7. Richiedere citazioni o riferimenti se la risposta e' grounded.
8. Fermare il recupero quando l'evidenza e' sufficiente.
9. Validare la risposta prima di mostrarla all'utente quando il rischio e' alto.

## Give a Bot a Fish

**Give a Bot a Fish** significa fornire direttamente al modello, nel contesto, tutte le informazioni necessarie per completare il compito. Questa strategia e' piu' affidabile quando il sistema conosce gia' i dati necessari e puo' recuperarli in modo autorizzato.

Esempio concettuale:

```text
L'utente chiede un riepilogo della propria inbox.
Il sistema recupera la lista delle transazioni autorizzate.
Il sistema inserisce la lista nel prompt.
Il modello sintetizza i dati e risponde.
```

## Minimo contesto sufficiente

Troppo poco contesto produce risposte vaghe, incomplete o inventate. Troppo contesto produce rumore, aumenta costi e latenza, rende piu' difficile citare le fonti rilevanti e puo' aumentare il rischio di leakage.

Il principio operativo e': inserire il minimo contesto sufficiente per rispondere bene, con riferimenti tracciabili.

## Privacy-aware context assembly

Arthur Shield rafforza un punto critico: il context assembly deve essere accompagnato da controlli runtime su prompt e response.

La sensitive data leakage puo' avvenire nel prompt, quando dati aziendali o segreti vengono inviati al modello, oppure nella response, quando il modello restituisce dati privati recuperati dal sistema ma non autorizzati per l'utente finale.

La PII leakage richiede attenzione sia agli identificatori diretti sia ai quasi-identificatori. Un dato apparentemente non sensibile puo' diventare identificativo se combinato con altri dati presenti nel contesto.

## Collegamento a validate_prompt e validate_response

`validate_prompt` puo' essere usato prima della chiamata al modello per controllare dati sensibili, PII, prompt injection o custom rules.

`validate_response` puo' essere usato dopo la generazione per controllare che la risposta non contenga dati sensibili, PII, contenuti non ammessi o informazioni non autorizzate.

Questi controlli non sostituiscono il context assembly; lo completano. Il sistema deve comunque evitare di recuperare o passare al modello dati non autorizzati.

## Concetti collegati

context_assembly, dynamic_context, hidden_prompt, retrieval_budget, context_filtering, grounded_generation, source_selection, privacy_boundary, sensitive_data_leakage, pii_leakage, validate_prompt, validate_response, runtime_safety.

Source refs: brex_prompt_engineering_guide#give-a-bot-a-fish; arthur_shield_agent_development_toolkit#sensitive-data-leakage; arthur_shield_agent_development_toolkit#pii-leakage; arthur_shield_agent_development_toolkit#rules-overview
