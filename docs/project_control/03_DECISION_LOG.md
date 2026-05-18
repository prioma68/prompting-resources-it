# Decision Log

Registro delle decisioni editoriali e operative giÃ  prese.

## DEC-0001 - Repository leggera, non deposito PDF

La repository deve restare una biblioteca ragionata, non un archivio indiscriminato di PDF.

## DEC-0002 - compare_sources.py come evidence pack, non generatore libero

compare_sources.py deve aiutare a costruire evidence pack e confronti controllati, non generare testo libero non tracciabile.

## DEC-0003 - Brex da integrare parzialmente

La Brex Prompt Engineering Guide non deve essere importata integralmente. Vanno selezionate solo le parti compatibili con production prompting.

## DEC-0004 - Brex integrata come fonte secondaria/practitioner

Brex Ã¨ integrata come fonte pratica complementare, non come fonte primaria. Le fonti primarie restano OpenAI, Anthropic/Claude, Google/Gemini e Perplexity.

## DEC-0005 - Arthur Shield come fonte secondaria strategica

Decisione: integrare Arthur Shield / Arthur AI come fonte secondaria strategica per runtime guardrails e LLM safety.

Motivazione: Arthur aggiunge valore sui controlli a runtime, inclusi validate_prompt, validate_response, hallucination detection, prompt injection detection, sensitive data leakage e PII leakage.

Implicazione: Arthur non diventa fonte primaria di prompt engineering; serve a rafforzare la distinzione tra prompt engineering, production prompting e runtime guardrails.
