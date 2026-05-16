# Prompt patterns

Raccolta di pattern riutilizzabili.

## 1. Analisi di fonte

```text
Analizza la fonte seguente.

Obiettivo: capire se è utile per una repository sul prompting.

Produci:
- sintesi;
- argomenti trattati;
- tipo di fonte;
- livello di affidabilità;
- sezioni della repository in cui inserirla;
- limiti o rischi.
```

## 2. Evidence pack

```text
Rispondi usando solo le fonti fornite.

Output:
1. risposta breve;
2. tabella delle prove;
3. punti incerti;
4. cosa andrebbe verificato.
```

## 3. Prompt da migliorare

```text
Valuta questo prompt.

Criteri:
- chiarezza dell'obiettivo;
- contesto;
- istruzioni;
- vincoli;
- formato dell'output;
- criteri di verifica;
- rischi di ambiguità.

Poi riscrivilo in una versione migliore.
```

## 4. Repository intake

```text
Valuta questa fonte per la repository Prompting Resources IT.

Campi:
- titolo;
- autore/vendor;
- URL;
- tipo;
- argomenti;
- perché è utile;
- limiti;
- sezione consigliata;
- priorità: alta/media/bassa.
```

## 5. Prompt per ricerca operativa

```text
Obiettivo: raccogliere e sintetizzare informazioni su {{tema}}.

Procedi così:
1. identifica le fonti più rilevanti;
2. separa fatti supportati, inferenze e punti incerti;
3. crea una sintesi operativa;
4. restituisci una tabella con fonte, informazione utile, livello di affidabilità e applicazione pratica.

Output:
- sintesi breve;
- tabella delle fonti;
- implicazioni operative;
- punti da verificare.
```

## 6. Prompt per workflow multi-step

Questo pattern serve quando vuoi trasformare una ricerca in un deliverable operativo, per esempio un report, una scheda, una presentazione, un briefing o una tabella decisionale.

```text
Obiettivo: trasformare una ricerca in un deliverable operativo.

Prima analizza il tema.
Poi organizza le informazioni per argomento.
Infine produci un output utilizzabile da {{pubblico}}.

Formato:
- executive summary;
- tabella dei punti principali;
- raccomandazioni;
- prossime azioni.
```