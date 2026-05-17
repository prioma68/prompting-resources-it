# Evidence pack

Query: prompting bias limiti confronto fonti

## Coverage

### Vendors

- google: 1
- openai: 1
- perplexity: 1

### Topics

- prompting: 3

## Retrieved chunks

### 1. google - System, contextual and role prompting

- score: 1.085
- chunk_id: google_prompt_engineering_whitepaper_2025__prompt_roles_001
- doc_id: google_prompt_engineering_whitepaper_2025
- topic: prompting
- techniques: system_prompting, contextual_prompting, role_prompting
- use_cases: style_control, task_context, persona
- source_ref: uploaded_pdf:22365_3_Prompt Engineering_v7 (1).pdf#page=18-24

Evidence summary:

Google distingue system prompting per lo scopo complessivo, contextual prompting per dettagli specifici del task e role prompting per voce, prospettiva o competenza simulata.

### 2. perplexity - Prompting for work

- score: 0.863
- chunk_id: perplexity_at_work_guide__prompting_for_work_001
- doc_id: perplexity_at_work_guide
- topic: prompting
- techniques: goal_first_prompting, tab_context, multi_step_workflow
- use_cases: browser_research, comparison, workflow_execution
- source_ref: uploaded_pdf:pplx-at-work.pdf#page=6-7

Evidence summary:

La guida consiglia di non trattare Perplexity come un motore di ricerca a keyword: conviene partire dall obiettivo, usare contesto proprio e descrivere workflow sequenziali completi.

### 3. openai - Outcome-first prompting

- score: 0.621
- chunk_id: openai_gpt55_prompting_guide__outcome_first_001
- doc_id: openai_gpt55_prompting_guide
- topic: prompting
- techniques: outcome_first, success_criteria, stopping_conditions
- use_cases: research, agents, support, coding
- source_ref: uploaded_text:Guida-Open-AI.txt#outcome-first-prompts

Evidence summary:

OpenAI imposta il prompt efficace come descrizione del risultato atteso: obiettivo, criteri di successo, vincoli, evidenza disponibile e forma finale. Questo riduce prompt troppo procedurali e lascia al modello spazio per scegliere il percorso piu efficiente.

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
