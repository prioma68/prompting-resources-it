# 05 - Command grammars e interfacce con strumenti

## Definizione

Una **command grammar** e' un insieme controllato di comandi che il modello puo' usare per interagire con un sistema applicativo.

Il modello non esegue liberamente azioni arbitrarie. Produce invece una sequenza di comandi, con argomenti, che il sistema puo' interpretare, validare ed eventualmente eseguire.

La fonte Brex presenta questa strategia come parte del passaggio da **Give a Bot a Fish** a **Teach a Bot to Fish**: non si forniscono solo dati al modello, ma gli si insegna come richiedere dati o azioni attraverso comandi disponibili.

## Teach a Bot to Fish

**Teach a Bot to Fish** significa fornire al modello strumenti, comandi o procedure che gli permettono di recuperare informazioni o compiere azioni controllate.

E' utile quando:

- il modello deve recuperare dati non noti in anticipo;
- il compito richiede piu' passaggi;
- la domanda richiede interrogazioni specifiche;
- il modello deve compiere azioni per conto dell'utente;
- il recupero semantico non basta;
- servono calcoli, grafici, aggiornamenti o modifiche di stato.

## Cosa deve definire una command grammar

Una command grammar dovrebbe definire:

- nome del comando;
- descrizione;
- argomenti;
- tipo degli argomenti;
- vincoli;
- esempi;
- formato dell'output;
- condizioni di errore;
- eventuale richiesta di conferma.

Esempio:

```markdown
| Command | Arguments | Description |
| --- | --- | --- |
| list_expenses | budget_id | Returns a list of expenses for a given budget |
| converse | message | Shows a message to the user |
| plot_expenses | expenses[] | Plots a list of expenses |
| get_budget_by_name | budget_name | Retrieves a budget by name |
| list_budgets | none | Returns the budgets the user can access |
| add_memo | inbox_item_id, memo | Adds a memo to the provided inbox item |
```

## Livello di astrazione

Il punto piu' importante e' scegliere il giusto livello di astrazione.

Comandi troppo specifici sono poco flessibili:

```text
plot_last_90_days_expenses()
```

Comandi troppo granulari sono fragili:

```text
draw_pixel(x, y, color)
```

Comandi migliori offrono primitive componibili:

```text
list_expenses(budget_id)
filter_expenses(expenses, date_range)
plot_expenses(expenses)
add_memo(expense_id, text)
```

Il modello deve avere abbastanza liberta' per comporre soluzioni utili, ma non tanta da inventare strumenti o agire fuori dai limiti.

## Rischio di allucinazione dei comandi

Con grammatiche complesse, il modello puo' inventare:

- comandi non disponibili;
- argomenti inesistenti;
- campi plausibili ma falsi;
- sequenze di azioni non valide;
- valori non autorizzati.

Per questo il sistema deve validare ogni comando prima dell'esecuzione.

## Esempi e few-shot

Le command grammars diventano piu' affidabili quando includono esempi. I modelli sono few-shot learners: possono imparare un nuovo schema operativo da pochi esempi. Tuttavia gli esempi consumano token, quindi bisogna bilanciare affidabilita' e budget di contesto.

Regola pratica:

```text
Usare esempi per i comandi piu' importanti, per i casi ambigui e per le azioni rischiose.
```

## Output in JSON

Le sequenze di comandi possono essere prodotte in JSON, cosi' il sistema puo' leggerle e validarle.

Esempio:

```json
{
  "commands": [
    {
      "name": "get_budget_by_name",
      "arguments": {
        "budget_name": "Marketing"
      }
    },
    {
      "name": "list_expenses",
      "arguments": {
        "budget_id": "budget_123"
      }
    }
  ]
}
```

Il JSON e' preferibile quando l'output deve essere interpretato da software.

## ReAct

ReAct, Reason + Act, e' un pattern in cui il modello alterna ragionamento, azione e osservazione.

Schema:

```text
Thought: il modello decide cosa serve.
Action: il modello chiede di usare uno strumento.
Observation: il sistema restituisce il risultato.
Thought: il modello aggiorna il piano.
Action: nuovo strumento o risposta finale.
```

Questo pattern permette al modello di agire come assistente di ricerca o agente operativo. Tuttavia richiede controlli forti, perche' ogni azione deve essere validata dal sistema.

## Sicurezza

Ogni tool interface deve rispettare questi principi:

- esporre solo strumenti necessari;
- validare ogni argomento;
- applicare i permessi dell'utente;
- bloccare comandi inventati;
- chiedere conferma per azioni rischiose;
- registrare le azioni;
- distinguere proposta ed esecuzione.

Source ref: brex_prompt_engineering_guide#command-grammars
