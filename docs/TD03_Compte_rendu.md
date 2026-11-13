# TD03 — Git Local Workflow

Compte rendu des manipulations réalisées le 13 novembre 2026.

## Projet et identité

- Dépôt source : https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP
- Copie de travail : `outputs/MarketPulse-TD03`.
- Branche utilisée : `ArnaudBensimhon`, issue de la branche distante existante du même nom.
- Git : `2.55.0.windows.5`.
- Auteur configuré : Arnaud Bensimhon — `arnaud.bensb@gmail.com`.

Toutes les commandes ci-dessous s'exécutent depuis la racine du projet, le dossier contenant `src`, `data` et `.git`.

## 1. Retrouver le véritable travail du TD02

Au départ, `git status` indiquait un dossier de travail propre et `git diff` ne produisait aucune sortie : aucun changement non enregistré n'était disponible.

Le code du TD02 était déjà enregistré sur la branche personnelle dans le commit :

```text
ec7a8dc7836cf4bb25daf5209a0b07b96ad35421
Complete TD02 Python CSV JSON processing
Auteur : Arnaud Bensimhon <arnaud.bensb@gmail.com>
```

La commande `git show ec7a8dc -- src/main.py` a permis de lire ses changements réels :

- ajout de `get_first_close()` et `get_last_close()`, qui convertissent le champ CSV `close` en `float` ;
- ajout de `display_market_summary()` pour réutiliser le même affichage pour l'instrument et le benchmark ;
- remplacement des affichages dupliqués dans `main()` par des appels à cette fonction ;
- présentation des premiers et derniers cours, des observations et de la configuration.

Le TD02 étant déjà commité, le cycle du TD03 a été réalisé avec une amélioration utile de la documentation.

## 2. Changement choisi pour le TD03

Un seul fichier a été modifié : `README.md`.

Le diff ajoute 52 lignes et n'en supprime aucune. Ces lignes expliquent :

- le lancement depuis la racine du dépôt et les deux fichiers de données nécessaires ;
- les résultats attendus du jeu de données pédagogique ;
- le rôle des fonctions de résumé ;
- le contrôle de l'identité, la sélection d'un fichier, la vérification de l'index et la lecture de l'historique.

Ce changement aide à reproduire l'exécution du projet et à vérifier un commit. Le diff correspond à cet objectif et ne contient pas de sortie de débogage Python.

## 3. Cycle Git effectué

### Avant la sélection

```bash
git --version
git config user.name
git config user.email
git status
git diff
git show ec7a8dc -- src/main.py
python src/main.py
```

Après modification du README :

```bash
git status
git status --short
git diff --check
git diff -- README.md
```

Le statut court était ` M README.md` : le fichier était modifié dans le dossier de travail, sans être sélectionné pour le commit.

### Sélection et inspection de l'index

```bash
git add README.md
git status
git diff --staged --check
git diff --staged
git diff
```

Seul `README.md` a été ajouté à l'index. Le diff indexé contenait les 52 lignes prévues. Le dernier `git diff` était vide : aucune différence ne restait entre le dossier de travail et l'index.

### Commit et vérification finale

```bash
git commit -m "docs: clarify sample execution and local Git verification"
git status
git log --oneline -5
git show HEAD
git log --author="Arnaud Bensimhon" --oneline
python src/main.py
```

Commit créé :

```text
f83b5f2072ed8ed0cdeb090824f601c8ac1b0f46
docs: clarify sample execution and local Git verification
Auteur : Arnaud Bensimhon <arnaud.bensb@gmail.com>
Fichier : README.md — 52 lignes ajoutées
```

Le préfixe `docs:` convient parce que le changement porte sur la documentation. Le reste du message décrit précisément les deux sujets ajoutés.

À la fin, `git status` indique `nothing to commit, working tree clean`. La branche locale a un commit d'avance sur `origin/ArnaudBensimhon`.

## 4. Vérification de MarketPulse

L'exécution de `python src/main.py` a réussi avant le commit et lors du contrôle final.

| Série | Observations | Premier cours | Dernier cours |
|---|---:|---:|---:|
| AAPL | 21 | 250.00 USD | 266.20 USD |
| SP500 | 21 | 6600.00 | 6742.00 |

La configuration affichée est `1 month` et `Daily`. Il s'agit des données pédagogiques fournies avec le dépôt.

## 5. Explications à savoir donner

| Notion ou commande | Explication |
|---|---|
| Working tree | Fichiers du projet tels qu'ils existent actuellement sur le disque. |
| Staging area / index | État exact sélectionné pour le prochain commit avec `git add`. |
| Commit | État enregistré dans l'historique local avec auteur, date, message et identifiant. |
| Identifiant | Empreinte du commit ; `f83b5f2` est la forme courte du commit TD03. |
| `git status` | Indique les fichiers modifiés, indexés ou non suivis et l'état de la branche. |
| `git diff` | Compare les fichiers suivis du dossier de travail avec l'index. |
| `git diff --staged` | Compare l'index au dernier commit. |
| `git add README.md` | Sélectionne l'état actuel du README pour le prochain commit. |
| `git commit` | Enregistre l'état sélectionné dans l'historique local. |
| `git log` | Liste les commits ; `--oneline` fournit une vue compacte. |
| `git show HEAD` | Affiche les métadonnées et le diff du dernier commit de la branche courante. |
| Fichier non suivi | Fichier absent de l'index ; signalé par `??`, son contenu n'apparaît pas dans un `git diff` ordinaire. |

Enregistrer un fichier dans l'éditeur ne crée pas de commit. Un commit local ne publie pas le travail sur GitHub.

## 6. Bilan

Les opérations techniques du CORE ont été effectuées : identité consultée, travail TD02 inspecté, diff lu, fichier sélectionné, index vérifié, commit local créé, historique consulté, commit inspecté et application exécutée avec succès.

À la fin du cycle TD03 décrit ici, aucun push, aucune Pull Request et aucune capture du Checkpoint A n'avaient été réalisés. La publication et la fusion demandées ensuite constituent une étape distincte. Les exercices optionnels et avancés ne sont pas nécessaires au CORE.

La compréhension personnelle reste à valider en relisant les explications et en sachant décrire le diff. Le [journal des commandes](TD03_Journal_commandes.txt) contient les sorties réelles des commandes.
