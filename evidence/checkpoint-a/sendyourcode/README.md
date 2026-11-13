# Checkpoint A — sendyourcode

Projet : ESILV MarketPulse G07-MTP. Membre : Antoine Mai, compte GitHub `sendyourcode`.

## État documenté

Ce dossier documente une collecte rétrospective des preuves après intégration des TD05 et TD06, le 13 novembre 2026. Il décrit l'état réel du dépôt ; il ne présente pas ces captures comme prises à la fin du TD04.

- Base commune inspectée : `9be856c`.
- Le programme affiche les dates `2026-09-01` / `2026-09-30` pour AAPL et SP500, avec 21 observations par série.
- Les fonctions de dates du TD04 proviennent du commit `8f1e338` d'Iliana. Elles ne sont pas attribuées à Antoine dans ce dossier.
- Contribution publiée sous `sendyourcode` : `6d64010`, `feat: display market metadata`, branche `feature/display-market-metadata`.
- Cette branche est effectivement intégrée dans `main`, via la PR nº 3 et le merge `692dcc5`, après revue. Ce travail a été produit dans le cadre du TD05 ; il fournit une trace réelle de branche et d'intégration.
- Les commandes du journal sont rejouées sur la copie actuelle. Le dossier documente leur résultat technique ; la compréhension individuelle reste à vérifier.

## Captures réalisées

Les trois captures ont été réalisées localement par Antoine le 13 novembre 2026 avec `Capturer_Checkpoint_A_sendyourcode.command`, puis inspectées visuellement. Le lanceur est conservé à la racine du dépôt ; il exécute les commandes réellement et ouvre les sélections de capture macOS. Il ne modifie ni les branches, ni les commits, ni la configuration Git et ne publie rien.

Les trois fichiers présents sont :

| Fichier | Contenu montré |
|---|---|
| `01_terminal_python.png` | Exécution de `python3 src/main.py` depuis la racine. |
| `02_git_status_log.png` | État actuel, historique et identité du commit `6d64010`. |
| `03_branch_merge.png` | Branche personnelle listée comme fusionnée dans main et graphe de l'intégration. |

Les trois PNG sont inclus, lisibles et cohérents avec le dépôt. La première capture montre le programme et les deux séries ; la deuxième montre le statut et le commit `6d64010` attribué à `sendyourcode` ; la troisième montre la branche de métadonnées déjà intégrée à `main`. Le fichier PNG non suivi visible dans le statut est la première capture en cours de collecte, pas une modification du code. Le journal texte complète ces captures. Aucune capture d'un autre membre n'est réutilisée.

## Points à expliquer pour la validation

- `git add` sélectionne un état pour le prochain commit ; enregistrer un fichier seul ne crée pas de commit.
- `git diff` montre les différences non indexées ; `git diff --staged` montre ce qui sera commité.
- Une branche permet de développer avant l'intégration à main.
- `git branch --merged main` liste les branches dont le commit est déjà contenu dans main.
- La fusion de la branche de métadonnées est un merge commit réel ; la fusion fast-forward des dates dans le main local d'Iliana est une autre opération.
- Un conflit signifie que Git ne peut pas choisir automatiquement le contenu final ; aucune création de conflit artificiel n'est requise au CORE.

Le contrat détaillé `docs/04_CHECKPOINTS_AND_EVIDENCE.md` est absent du dépôt. Les noms de fichiers suivent l'énoncé TD04 disponible. La portée des preuves reste celle de l'état actuel et de la branche de métadonnées ; elles ne reconstituent pas une manipulation personnelle de la fonctionnalité de dates au TD04.
