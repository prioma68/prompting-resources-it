# 04 - Semantic search e RAG

## Definizione

La **semantic search** e' una tecnica di recupero dell'informazione basata sulla similarita' concettuale tra una query e un insieme di documenti o chunk.

Invece di cercare soltanto parole identiche, la semantic search rappresenta testi e query tramite embedding: vettori numerici che catturano caratteristiche semantiche del contenuto.

Nei sistemi RAG, retrieval-augmented generation, la semantic search viene usata per recuperare documenti o frammenti rilevanti, che vengono poi inseriti nel prompt come contesto per il modello.

## Embedding

Un embedding puo' essere pensato come una rappresentazione numerica a dimensione fissa di un testo.

Il sistema puo' calcolare embedding per:

- documenti;
- chunk;
- domande dell'utente;
- titoli;
- riassunti;
- metadati;
- testi generati per espandere la query.

Una volta calcolato l'embedding della query, il sistema cerca i documenti con embedding piu' simili e recupera i primi risultati.

## Processo base

1. L'utente fa una domanda.
2. Il sistema calcola l'embedding della domanda.
3. Il sistema confronta la domanda con gli embedding dei documenti.
4. Il sistema recupera i documenti o chunk piu' vicini.
5. I contenuti recuperati vengono inseriti nel prompt.
6. Il modello risponde usando quel contesto.

## Semantic search come context assembly

La semantic search non e' la risposta finale. E' una fase del context assembly.

Il suo compito e' selezionare materiale utile da fornire al modello. La qualita' della risposta finale dipende da qualita' dei documenti indicizzati, granularita' dei chunk, pertinenza del recupero, qualita' degli embedding, presenza di metadati, ordinamento dei risultati, istruzioni date al modello su come usare le fonti e capacita' di citare i riferimenti.

## Limiti delle query brevi

Le query molto brevi o ambigue possono produrre embedding poco informativi.

Esempi:

```text
policy
budget
prompt
fonti
```

In questi casi il recupero semantico puo' non bastare. Strategie utili:

- espansione della query;
- ricerca ibrida keyword + semantica;
- uso di sinonimi;
- uso di metadati;
- query multiple;
- richiesta di chiarimento;
- generazione di una query piu' ricca.

## HyDE

HyDE, **Hypothetical Document Embeddings**, e' una tecnica avanzata citata dalla fonte Brex. Consiste nel chiedere al modello di generare un documento ipotetico che potrebbe rispondere alla domanda dell'utente, e poi usare l'embedding di quel documento generato per cercare documenti reali semanticamente vicini.

Schema:

1. L'utente fa una domanda breve o ambigua.
2. Il modello genera un testo ipotetico di risposta.
3. Il sistema calcola l'embedding del testo ipotetico.
4. Il sistema recupera documenti simili a quel testo.
5. Il modello risponde usando documenti reali recuperati.

HyDE puo' migliorare il recupero quando la query iniziale e' povera di contesto. Tuttavia introduce un passaggio generativo che deve essere controllato, perche' il documento ipotetico puo' contenere assunzioni non vere.

Regola pratica:

```text
Il retrieval serve a trovare evidenze, non a confermare ipotesi inventate.
```

## Applicazione alla repository Prompting

Nel progetto Prompting, semantic search e RAG si collegano direttamente a `documents.jsonl`, `chunks.jsonl`, `concepts.jsonl`, `scripts/search.py`, `compare_sources.py` ed evidence pack.

I chunk devono essere abbastanza piccoli da essere recuperabili con precisione, ma abbastanza ricchi da mantenere contesto. Ogni chunk dovrebbe avere metadati e identificatori stabili per consentire tracciabilita' e citazione.

Source ref: brex_prompt_engineering_guide#semantic-search
