# 04 - Semantic search e RAG

## Definizione

La **semantic search** e' una tecnica di recupero dell'informazione basata sulla similarita' concettuale tra una query e un insieme di documenti o chunk.

Nei sistemi RAG, retrieval-augmented generation, la semantic search viene usata per recuperare documenti o frammenti rilevanti, che vengono poi inseriti nel prompt come contesto per il modello.

## Semantic search come context assembly

La semantic search non e' la risposta finale. E' una fase del context assembly.

Il suo compito e' selezionare materiale utile da fornire al modello. La qualita' della risposta finale dipende da qualita' dei documenti indicizzati, granularita' dei chunk, pertinenza del recupero, qualita' degli embedding, metadati, ordinamento dei risultati, istruzioni date al modello e capacita' di citare i riferimenti.

## Processo base

1. L'utente fa una domanda.
2. Il sistema calcola o costruisce una query di recupero.
3. Il sistema confronta la query con documenti o chunk indicizzati.
4. Il sistema recupera i documenti o chunk piu' rilevanti.
5. I contenuti recuperati vengono filtrati per pertinenza, autorizzazione e ridondanza.
6. I contenuti vengono inseriti nel prompt con source id o chunk id.
7. Il modello risponde usando quel contesto.
8. La risposta viene validata quando sono richiesti grounding e sicurezza runtime.

## Limiti delle query brevi

Le query molto brevi o ambigue possono produrre recupero debole. Strategie utili sono query expansion, ricerca ibrida keyword + semantica, uso di metadati, query multiple e chiarimento utente quando necessario.

## HyDE

HyDE, Hypothetical Document Embeddings, e' una tecnica avanzata in cui il sistema genera un testo ipotetico che potrebbe rispondere alla domanda e usa quel testo per cercare documenti semanticamente vicini.

HyDE puo' migliorare il recupero quando la query iniziale e' povera di contesto, ma introduce un passaggio generativo che va controllato: il documento ipotetico non e' evidenza. Serve a cercare evidenza, non a sostituirla.

## Intrinsic ed extrinsic hallucination nei sistemi RAG

Arthur Shield aggiunge una distinzione utile per la valutazione delle risposte grounded.

Una **intrinsic hallucination** avviene quando la risposta contraddice il contesto fornito. Una **extrinsic hallucination** avviene quando la risposta contiene informazioni non presenti nel contesto, anche se potrebbero essere vere nel mondo reale.

Nei sistemi RAG, una risposta non deve essere valutata solo rispetto alla verita' generale, ma rispetto al supporto fornito dalle fonti recuperate. Una claim vera ma non presente nel contesto puo' essere fuori policy se il compito richiede risposta solo sulle fonti.

## Claim-by-claim evaluation

Per validare risposte lunghe, e' utile dividerle in claim. Ogni claim puo' essere confrontato con il contesto recuperato. Questo permette di distinguere una risposta interamente infondata da una risposta quasi corretta con un solo claim non supportato.

Nel progetto Prompting, questa logica e' coerente con `compare_sources.py`: l'evidence pack recupera chunk tracciabili, il LLM sintetizza, e un passaggio di verifica puo' controllare se ogni affermazione concreta e' supportata da un chunk o source_ref.

## Concetti collegati

semantic_search, embedding, rag, chunk_retrieval, query_expansion, hyde, hybrid_search, retrieval_quality, context_assembly, hallucination_detection, intrinsic_hallucination, extrinsic_hallucination, claim_by_claim_evaluation.

Source refs: brex_prompt_engineering_guide#semantic-search; arthur_shield_agent_development_toolkit#hallucination; openai_gpt55_prompting_guide#retrieval-budget
