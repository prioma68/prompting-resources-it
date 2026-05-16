# Zero-shot, one-shot e few-shot

Queste tecniche riguardano la quantità di esempi forniti al modello.

## Zero-shot

Il modello riceve solo l'istruzione, senza esempi.

```text
Classifica questa recensione come POSITIVA, NEUTRA o NEGATIVA.
```

Utile per compiti semplici o quando il modello conosce bene il formato richiesto.

## One-shot

Il modello riceve un esempio.

```text
Esempio:
Input: "Il servizio è stato rapido e preciso."
Output: POSITIVA

Ora classifica:
Input: "{{RECENSIONE}}"
Output:
```

Utile quando vuoi indicare il tono o il formato con un solo caso.

## Few-shot

Il modello riceve più esempi.

```text
Esempi:
Input: ...
Output: ...

Input: ...
Output: ...

Input: "{{NUOVO_INPUT}}"
Output:
```

Utile per classificazioni, estrazioni, trasformazioni di formato, stile e casi limite.

## Qualità degli esempi

Gli esempi devono essere:

- pertinenti;
- coerenti;
- diversi;
- privi di errori;
- vicini al caso d'uso reale.

Un esempio sbagliato può insegnare al modello il comportamento sbagliato.


## Fonte Anthropic / Claude collegata

### Esempi e multishot prompting

Fonte: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-best-practices

Questa fonte è collegata a zero-shot, one-shot e few-shot perché raccomanda esempi rilevanti, diversi e strutturati per orientare il formato, il tono e il comportamento del modello.

Uso pratico nella repository:

- usare esempi quando il formato dell'output è importante;
- includere casi limite;
- evitare esempi ambigui o contraddittori;
- preferire pochi esempi di qualità rispetto a molti esempi rumorosi.
