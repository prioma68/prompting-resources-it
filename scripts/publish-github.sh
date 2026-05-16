#!/usr/bin/env bash
set -e

REPO_NAME="${1:-prompting-resources-it}"
GITHUB_USER="${2:-TUO-UTENTE}"

git init
git add .
git commit -m "Initial repository structure" || true
git branch -M main
git remote add origin "https://github.com/${GITHUB_USER}/${REPO_NAME}.git" || true
git push -u origin main
