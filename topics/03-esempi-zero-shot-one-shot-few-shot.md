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
