# Google - Prompt Engineering whitepaper

## Abstract

Questa fonte e' la base tassonomica del progetto. Copre configurazioni LLM, tecniche classiche e avanzate di prompting, prompting per codice, output strutturati e documentazione degli esperimenti. E' particolarmente utile per costruire una classificazione tecnica delle tecniche di prompt engineering.

## Temi principali

- Configurazioni LLM: output length, temperature, top-K, top-P.
- Zero-shot, one-shot, few-shot.
- System, contextual e role prompting.
- Step-back prompting.
- Chain of Thought, self-consistency e Tree of Thoughts.
- ReAct come ciclo reason-act con strumenti esterni.
- Automatic Prompt Engineering.
- Code prompting: scrittura, spiegazione, traduzione, debugging e review del codice.
- JSON repair, schema e output strutturati.
- Documentazione sistematica degli esperimenti di prompt.

## Concetti chiave

- Le tecniche di prompting devono essere collegate a task e configurazioni del modello.
- Gli esempi few-shot aiutano il modello a seguire pattern di output.
- ReAct collega ragionamento e azione con strumenti esterni, quindi e' un ponte verso sistemi agentici.
- Gli schema e i formati strutturati riducono ambiguita' e facilitano integrazioni applicative.

## Domande interrogabili

- Quali sono le tecniche principali di prompt engineering?
- Quando usare zero-shot, one-shot o few-shot?
- Come funzionano CoT, self-consistency e Tree of Thoughts?
- Come si collega ReAct agli agenti?
- Come documentare esperimenti di prompt?

## Relazioni con altre fonti

- Con OpenAI: Google fornisce la tassonomia, OpenAI le regole operative di retrieval e validazione.
- Con Claude: Google introduce tecniche, Claude mostra come strutturarle in prompt lunghi e agentici.
- Con Perplexity: ReAct e ricerca avanzata aiutano a interpretare workflow come Comet, Research e Tasks.
