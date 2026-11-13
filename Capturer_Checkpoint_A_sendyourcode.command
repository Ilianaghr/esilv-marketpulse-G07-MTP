#!/bin/bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
EVIDENCE="evidence/checkpoint-a/sendyourcode"
export GIT_PAGER=cat
mkdir -p "$EVIDENCE"

git rev-parse --is-inside-work-tree >/dev/null
if ! git merge-base --is-ancestor 6d64010 main; then
  printf 'Le main local ne contient pas encore le commit 6d64010. Synchronise-le avant la collecte.\n'
  exit 1
fi
if ! git show-ref --verify --quiet refs/heads/feature/display-market-metadata; then
  printf 'La branche locale feature/display-market-metadata est absente. Reprendre la collecte dans la copie préparée.\n'
  exit 1
fi
if ! command -v python3 >/dev/null; then
  printf 'python3 est introuvable dans ce terminal.\n'
  exit 1
fi

capture() {
  local target="$EVIDENCE/$1"
  if [ -s "$target" ]; then
    printf '\n%s existe déjà : fichier conservé.\n' "$target"
    return
  fi
  printf '\nAgrandis le terminal pour rendre toute la sortie lisible.\n'
  printf 'Appuie sur Entrée, puis sélectionne la zone du terminal pour %s.\n' "$1"
  read -r
  /usr/sbin/screencapture -i "$target"
  if [ ! -s "$target" ]; then
    printf 'Capture annulée. Relance le lanceur pour terminer les captures manquantes.\n'
    exit 1
  fi
}

clear
printf 'Checkpoint A — sendyourcode — état actuel après TD06\n\n$ python3 src/main.py\n'
python3 src/main.py
capture 01_terminal_python.png

clear
printf 'Checkpoint A — sendyourcode — état et historique actuels\n\n$ git status\n'
git status
printf '\n$ git log --oneline -5\n'
git log --oneline -5
printf '\n$ git show -s --format="%%h %%an %%s" 6d64010\n'
git show -s --format='%h %an %s' 6d64010
capture 02_git_status_log.png

clear
printf 'Checkpoint A — sendyourcode — branche de métadonnées intégrée\n'
printf 'Contribution TD05 ; les dates TD04 sont attribuées à Iliana.\n\n$ git branch\n'
git branch
printf '\n$ git branch --merged main\n'
git branch --merged main
printf '\n$ git log --oneline --graph --decorate --simplify-by-decoration main feature/display-market-metadata -8\n'
git log --oneline --graph --decorate --simplify-by-decoration main feature/display-market-metadata -8
capture 03_branch_merge.png

printf '\nLes trois captures sont enregistrées dans %s.\n' "$EVIDENCE"
printf 'Vérifie leur contenu et leur lisibilité avant publication. Aucun commit ni push effectué.\n'
printf 'Appuie sur Entrée pour fermer.\n'
read -r
