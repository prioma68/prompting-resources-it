# Arthur Shield / Arthur AI - Agent Development Toolkit

## Ruolo nella repository

Arthur Shield e' integrato come fonte secondaria strategica per runtime guardrails e LLM safety. Non e' una fonte primaria di prompt engineering. La sua funzione editoriale e' spiegare come controllare input, response, privacy, grounding e policy a runtime attraverso regole esterne al prompt.

## Punti integrati

- rule placement: `validate_prompt` e `validate_response`;
- hallucination detection: intrinsic vs extrinsic;
- claim-by-claim evaluation;
- prompt injection detection: jailbreaking e instruction manipulation;
- sensitive data leakage su prompt e response;
- PII leakage con direct identifier e quasi-identifier;
- custom rules con regex e keyword;
- governance con default rules e task rules.

## Punti esclusi

Non sono stati importati benchmark numerici, costi, latenze, claim commerciali, esempi API completi o dettagli di setup. La fonte viene normalizzata in concetti vendor-neutral.

## Decisione editoriale

Status: integrare parzialmente. Priorita': alta. Ruolo: fonte secondaria strategica per sicurezza runtime.

Source: https://www.arthur.ai/agent-development-toolkit
