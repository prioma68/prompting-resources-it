# Pubblicazione su GitHub

## Opzione A: da interfaccia web

1. Vai su GitHub.
2. Crea una nuova repository chiamata `prompting-resources-it`.
3. Non inizializzarla con README se vuoi usare questi file.
4. Carica i file oppure usa Git da terminale.

## Opzione B: da terminale

```bash
cd prompting-resources-it
git init
git add .
git commit -m "Initial repository structure"
git branch -M main
git remote add origin https://github.com/TUO-UTENTE/prompting-resources-it.git
git push -u origin main
```

## Opzione C: GitHub CLI

```bash
cd prompting-resources-it
git init
git add .
git commit -m "Initial repository structure"
gh repo create prompting-resources-it --public --source=. --remote=origin --push
```

## Nota

Se la repository esiste già, non usare `git init` su una cartella sbagliata. Prima clona la repo:

```bash
git clone https://github.com/TUO-UTENTE/prompting-resources-it.git
```

Poi copia dentro i file e fai commit.
