#!/bin/bash
set -e
cd -- "$(dirname -- "$0")"
EVIDENCE="evidence/checkpoint-a/Ilianaghr"
mkdir -p "$EVIDENCE"
export GIT_PAGER=cat
capture() {
  printf '\nSélectionne uniquement la zone du terminal pour la capture %s.\n' "$1"
  printf 'Appuie sur Entrée pour ouvrir la sélection de capture.'
  read -r
  /usr/sbin/screencapture -i "$EVIDENCE/$1"
  if [ ! -s "$EVIDENCE/$1" ]; then
    printf '\nCapture annulée. Relance ce fichier pour recommencer.\n'
    exit 1
  fi
}
clear
printf 'Checkpoint A — Ilianaghr — Exécution Python\n\n$ python3 src/main.py\n'
python3 src/main.py
capture 01_terminal_python.png
clear
printf 'Checkpoint A — Ilianaghr — État et historique\n\n$ git status\n'
git status
printf '\n$ git log --oneline -5\n'
git log --oneline -5
capture 02_git_status_log.png
clear
printf 'Checkpoint A — Ilianaghr — Branches et fusion\n\n$ git branch\n'
git branch
printf '\n$ git branch --merged main\n'
git branch --merged main
printf '\n$ git log --oneline --graph --decorate --all -16\n'
git log --oneline --graph --decorate --all -16
capture 03_branch_merge.png
printf '\nLes trois captures sont enregistrées dans %s.\n' "$EVIDENCE"
printf 'Vérifie leur lisibilité et leur contenu avant de les ajouter au commit.\n'
printf 'Aucun push effectué. Appuie sur Entrée pour fermer.\n'
read -r
