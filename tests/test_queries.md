# Test queries v0.1

Run these manually with `python scripts/search.py "QUERY"`.

1. `ReAct agenti tool use`
   - Expected: Google ReAct chunk; Claude tool use; Perplexity agentic actions.

2. `retrieval budget citazioni grounding`
   - Expected: OpenAI retrieval budget and grounding chunks.

3. `XML documenti lunghi contesto`
   - Expected: Claude XML and long context chunks.

4. `few shot esempi classificazione`
   - Expected: Google shot prompting; Claude examples.

5. `Spaces knowledge base brand consistency`
   - Expected: Perplexity Spaces chunk.

6. `coding agent validation test build`
   - Expected: OpenAI validation loop; Claude agentic state; Google code prompting if added later.

7. `workflow multi step browser Comet`
   - Expected: Perplexity prompting for work and agentic actions.

8. `temperature top K top P output length`
   - Expected: Google LLM configuration chunk.

9. `self consistency tree of thoughts chain of thought`
   - Expected: Google reasoning chunk.

10. `business development lead generation market research`
   - Expected: Perplexity advanced research; future chunks can expand lead generation.

## v0.1.3 Brex assestata

```bat
python scripts\search.py "hidden prompt non e segreto dati sensibili" --vendor brex --top-k 3
python scripts\search.py "prompt injection data exfiltration untrusted content" --vendor brex --top-k 5
python scripts\search.py "give a bot a fish context assembly retrieval budget" --vendor brex --top-k 5
python scripts\search.py "HyDE query breve semantic search RAG" --vendor brex --top-k 5
python scripts\search.py "command grammar livello astrazione validazione comandi" --vendor brex --top-k 5
python scripts\search.py "citation IDs sources_used output programmatico JSON" --vendor brex --top-k 5
```

