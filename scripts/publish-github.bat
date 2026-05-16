@echo off
set REPO_NAME=prompting-resources-it
set GITHUB_USER=TUO-UTENTE

git init
git add .
git commit -m "Initial repository structure"
git branch -M main
git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git
git push -u origin main
