# Evidence pack

Query: Perché il prompt non basta come barriera di sicurezza in un sistema LLM?

## Coverage

### Vendors

- arthur_ai: 4
- brex: 5
- openai: 2
- perplexity: 1

### Topics

- fine_tuning: 1
- grounding: 2
- guardrails: 1
- hidden_prompts: 1
- production_prompting: 1
- prompt_security: 3
- prompting: 2
- runtime_safety: 1

## Retrieved chunks

### 1. arthur_ai - Runtime guardrails and LLM safety

- score: 3.631
- chunk_id: arthur_shield_agent_development_toolkit__runtime_guardrails_001
- doc_id: arthur_shield_agent_development_toolkit
- topic: runtime_safety
- techniques: llm_guardrails, runtime_safety, rule_placement
- use_cases: production_llm_apps, safety_pipeline, governance
- source_ref: arthur_shield_agent_development_toolkit#runtime-guardrails

Evidence summary:

Arthur Shield viene integrato come fonte secondaria strategica: non insegna a scrivere prompt migliori, ma mostra che la sicurezza di un sistema LLM richiede guardrails runtime esterni al prompt, policy configurabili, validazione e monitoraggio. Il prompt non basta come barriera di sicurezza in un sistema LLM: input, contesto, output e strumenti devono essere controllati dalla pipeline applicativa.

### 2. arthur_ai - Prompt injection detection

- score: 2.812
- chunk_id: arthur_shield_agent_development_toolkit__prompt_injection_001
- doc_id: arthur_shield_agent_development_toolkit
- topic: prompt_security
- techniques: prompt_injection_detection, jailbreak_detection, instruction_manipulation, validate_prompt
- use_cases: input_security, untrusted_content_filtering, agent_safety
- source_ref: arthur_shield_agent_development_toolkit#prompt-injection

Evidence summary:

Prompt injection detection intercetta tentativi di manipolare il comportamento di un LLM o di un'applicazione LLM. Arthur distingue jailbreaking, che cerca di violare istruzioni o policy, e instruction manipulation, che cerca di far ignorare, rivelare o sovrascrivere system prompt e prompt template. Il controllo va collocato soprattutto in validate prompt.

### 3. brex - Prompt as system component

- score: 2.747
- chunk_id: brex_prompt_engineering_guide__prompt_as_system_component_001
- doc_id: brex_prompt_engineering_guide
- topic: production_prompting
- techniques: prompt_as_source_code, non_determinism, system_design
- use_cases: architecture, prompt_governance
- source_ref: github:brexhq/prompt-engineering/README.md#why-do-we-need-prompt-engineering

Evidence summary:

Brex descrive il prompt come una specie di codice sorgente interpretato dal modello. La metafora va normalizzata: un LLM non esegue codice in modo deterministico, ma il prompt resta un componente di sistema che orienta comportamento, contesto, vincoli e output.

### 4. brex - Prompt injection and untrusted content

- score: 2.340
- chunk_id: brex_prompt_engineering_guide__prompt_injection_untrusted_content_001
- doc_id: brex_prompt_engineering_guide
- topic: prompt_security
- techniques: prompt_injection, untrusted_content, instruction_separation
- use_cases: rag, web_retrieval, document_analysis
- source_ref: github:brexhq/prompt-engineering/README.md#prompt-hacking

Evidence summary:

La prompt injection avviene quando contenuti non fidati, come pagine web, email, PDF o risultati RAG, contengono istruzioni malevole che il modello potrebbe seguire. Il sistema deve separare istruzioni autorevoli e documenti da analizzare.

### 5. openai - Outcome-first prompting

- score: 2.247
- chunk_id: openai_gpt55_prompting_guide__outcome_first_001
- doc_id: openai_gpt55_prompting_guide
- topic: prompting
- techniques: outcome_first, success_criteria, stopping_conditions
- use_cases: research, agents, support, coding
- source_ref: uploaded_text:Guida-Open-AI.txt#outcome-first-prompts

Evidence summary:

OpenAI imposta il prompt efficace come descrizione del risultato atteso: obiettivo, criteri di successo, vincoli, evidenza disponibile e forma finale. Questo riduce prompt troppo procedurali e lascia al modello spazio per scegliere il percorso piu efficiente.

### 6. arthur_ai - Validate prompt

- score: 2.007
- chunk_id: arthur_shield_agent_development_toolkit__validate_prompt_001
- doc_id: arthur_shield_agent_development_toolkit
- topic: guardrails
- techniques: validate_prompt, prompt_injection_detection, sensitive_data_leakage, pii_leakage
- use_cases: pre_llm_filtering, prompt_firewall, input_safety
- source_ref: arthur_shield_agent_development_toolkit#validate-prompt

Evidence summary:

validate prompt e' un controllo pre-LLM: valuta il prompt o il contenuto in ingresso prima della chiamata al modello. E' il punto naturale per prompt injection detection, jailbreak detection, instruction manipulation, PII leakage in input, sensitive data leakage in input e custom guardrail rule su keyword o regex.

### 7. openai - Grounding and citations

- score: 1.981
- chunk_id: openai_gpt55_prompting_guide__grounding_citations_001
- doc_id: openai_gpt55_prompting_guide
- topic: grounding
- techniques: citations, source_backed_claims, missing_evidence_behavior
- use_cases: reports, research, knowledge_base
- source_ref: uploaded_text:Guida-Open-AI.txt#grounding-citations

Evidence summary:

Per le risposte fondate, la guida separa affermazioni concrete supportate da fonti da formulazioni creative. Quando il supporto manca, il sistema dovrebbe usare placeholder o indicare assunzioni invece di inventare dettagli.

### 8. arthur_ai - Hallucination: intrinsic and extrinsic

- score: 1.955
- chunk_id: arthur_shield_agent_development_toolkit__hallucination_types_001
- doc_id: arthur_shield_agent_development_toolkit
- topic: grounding
- techniques: hallucination_detection, intrinsic_hallucination, extrinsic_hallucination
- use_cases: rag, grounded_generation, source_verification
- source_ref: arthur_shield_agent_development_toolkit#hallucination-intrinsic-extrinsic

Evidence summary:

Arthur distingue hallucination intrinsic ed extrinsic. Una intrinsic hallucination contraddice direttamente il contesto fornito. Una extrinsic hallucination aggiunge informazioni non presenti nel contesto, anche se potrebbero essere vere in generale. In un sistema RAG, una claim puo' fallire per mancanza di supporto nelle fonti, non solo per falsita' assoluta.

### 9. perplexity - Prompting for work

- score: 1.928
- chunk_id: perplexity_at_work_guide__prompting_for_work_001
- doc_id: perplexity_at_work_guide
- topic: prompting
- techniques: goal_first_prompting, tab_context, multi_step_workflow
- use_cases: browser_research, comparison, workflow_execution
- source_ref: uploaded_pdf:pplx-at-work.pdf#page=6-7

Evidence summary:

La guida consiglia di non trattare Perplexity come un motore di ricerca a keyword: conviene partire dall obiettivo, usare contesto proprio e descrivere workflow sequenziali completi.

### 10. brex - Fine-tuning as last resort

- score: 1.884
- chunk_id: brex_prompt_engineering_guide__fine_tuning_last_resort_001
- doc_id: brex_prompt_engineering_guide
- topic: fine_tuning
- techniques: fine_tuning, synthetic_data_for_finetuning, training_data_privacy
- use_cases: model_customization, prompt_governance
- source_ref: github:brexhq/prompt-engineering/README.md#fine-tuning

Evidence summary:

Il principio Brex da conservare e che il fine-tuning e una ultima risorsa. Prima vanno provati prompt chiari, esempi, schema di output, retrieval, tool e validazione. Non usare dati cliente reali o sensibili: preferire dati sintetici, anonimizzati o autorizzati.

### 11. brex - Hidden prompt is not a security boundary

- score: 1.838
- chunk_id: brex_prompt_engineering_guide__hidden_prompt_security_boundary_001
- doc_id: brex_prompt_engineering_guide
- topic: prompt_security
- techniques: hidden_prompt_leakage, secret_minimization, privacy_boundary
- use_cases: security_review, prompt_design
- source_ref: github:brexhq/prompt-engineering/README.md#hidden-prompts

Evidence summary:

Il principio Brex da conservare e che qualsiasi contenuto passato al modello puo emergere in output. Non inserire nel prompt credenziali, chiavi API, dati riservati o informazioni che l utente non sarebbe autorizzato a vedere. La protezione deve avvenire prima del prompt.

### 12. brex - Hidden prompt definition

- score: 1.760
- chunk_id: brex_prompt_engineering_guide__hidden_prompt_definition_001
- doc_id: brex_prompt_engineering_guide
- topic: hidden_prompts
- techniques: system_prompt, hidden_context, session_context
- use_cases: chatbots, assistants, workflow_initialization
- source_ref: github:brexhq/prompt-engineering/README.md#hidden-prompts

Evidence summary:

Un hidden prompt e una parte di contesto inserita dall applicazione ma non mostrata intenzionalmente all utente: ruolo, tono, vincoli, obiettivi, dati dinamici e istruzioni operative. Serve a guidare il modello, non a proteggere segreti.

## Prompt for downstream LLM

Use only the chunks in this evidence pack. Do not attribute claims to a source unless the claim is supported by that source's chunk. Distinguish explicit evidence, reasonable inference, and limitations. For every concrete claim, include chunk_id or source_ref. If coverage is weak for a vendor or topic, say so.

Suggested answer structure:

1. Short answer
2. Source-by-source analysis
3. Explicit evidence
4. Reasonable inferences
5. Biases or limits
6. Convergences and divergences
7. Operational implications
