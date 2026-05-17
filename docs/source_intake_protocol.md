# Protocollo per aggiungere nuove fonti

La repository verra estesa con molti PDF e link ufficiali. Per evitare confusione, le fonti vanno aggiunte a blocchi piccoli e tracciabili.

## Regola pratica

Non caricare decine di fonti tutte insieme. Procedere per blocchi di 3-8 materiali, possibilmente dello stesso vendor o dello stesso tema.

## Formato richiesto per ogni blocco

```text
Blocco fonti n. X

Vendor:
OpenAI / Anthropic / Google / Perplexity / altro

Materiali:
- file.pdf - tema
- https://... - tema

Priorita:
alta / media / bassa

Obiettivo:
es. migliorare agenti, retrieval, tools, deep research, coding

Note:
eventuali indicazioni
```

## Cosa viene registrato nel registry

Ogni fonte deve avere almeno:

```yaml
id: vendor_short_title_year
vendor: openai | anthropic | google | perplexity | other
title: titolo leggibile
source_type: pdf | web_page | guide | whitepaper | docs | blog | repository
access: uploaded_pdf | uploaded_text | official_url
canonical_url: TBD
local_reference: nome_file_o_url
language: en | it | other
topics:
  - prompting
  - agents
  - retrieval
ingestion_status: pending | processed_draft | reviewed
license_status: link_only_plus_transformed_notes
freshness: static | versioned | needs_periodic_check
```

## Cosa non fare

- Non mischiare PDF personali e documentazione ufficiale senza segnalarlo.
- Non rinominare fonti in modo ambiguo come `documento1.pdf` se e possibile evitarlo.
- Non aggiungere chunk senza source_ref.
- Non trattare sintesi LLM come evidenza primaria.

## Cosa fare

- Usare nomi file leggibili.
- Indicare vendor e tema.
- Conservare sempre il riferimento alla fonte.
- Distinguere contenuto esplicito, sintesi e inferenza.
- Testare la ricerca dopo ogni blocco aggiunto.
