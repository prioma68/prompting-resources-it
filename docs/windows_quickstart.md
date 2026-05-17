# Windows quickstart

Questa guida serve per usare la repository da Windows CMD.

## 1. Aprire il CMD nella cartella corretta

1. Apri Esplora file.
2. Entra nella cartella `ai-docs-repository`.
3. Devi vedere file e cartelle come:

```text
README.md
data
scripts
sources
reports
tests
```

4. Clicca la barra del percorso in alto.
5. Scrivi:

```bat
cmd
```

6. Premi Invio.

Si apre una finestra CMD gia posizionata nella repository.

## 2. Verificare Python

```bat
python --version
```

Se compare una versione come `Python 3.12.2`, va bene.

## 3. Prima ricerca

```bat
python scripts\search.py "ReAct agenti tool use"
```

Risultato atteso: chunk su Google/ReAct, Anthropic/tool use, OpenAI/tool-heavy tasks e Perplexity/agentic actions.

## 4. Test principali

```bat
python scripts\search.py "retrieval budget citazioni grounding"
python scripts\search.py "XML documenti lunghi contesto"
python scripts\search.py "temperature top K top P output length"
python scripts\search.py "Spaces knowledge base brand consistency"
```

## 5. Filtri vendor

```bat
python scripts\search.py "tool use agents" --vendor anthropic
python scripts\search.py "Comet Research Labs Spaces" --vendor perplexity
```

## 6. Output JSON

```bat
python scripts\search.py "retrieval budget" --json
```

Questo output e utile per notebook, script o futura integrazione con LLM.

## 7. Evidence pack

```bat
python scripts\compare_sources.py "prompting bias limiti confronto fonti" --top-k 12
```

Questo non genera una risposta finale. Prepara un pacchetto di evidenze da passare a un LLM o da leggere manualmente.
