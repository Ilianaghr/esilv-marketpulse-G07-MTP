# Checkpoint A — Ilianaghr

Projet : ESILV MarketPulse G07-MTP. Branche personnelle : `ilianaghoorun`.
Voir `docs/TD04_Compte_rendu.md` et le journal associé pour les manipulations exécutées.

Les captures suivantes ont été réalisées dans un vrai terminal le 13 novembre 2026 et vérifiées visuellement :

- `01_terminal_python.png` : `python3 src/main.py`.
- `02_git_status_log.png` : `git status` et `git log --oneline -5`.
- `03_branch_merge.png` : `git branch`, `git branch --merged main` et
  `git log --oneline --graph --decorate --all`.

La branche `feature/display-observation-dates` est conservée et fusionnée dans `main`.
Le commit de fonctionnalité est `8f1e338`. La fusion dans `main` était fast-forward.
La fusion dans la branche personnelle est `df373b7`.
Ne supprimer la branche de fonctionnalité qu’après capture et validation de l’enseignant.
Les trois captures sont présentes, lisibles et sans secret visible. Aucun push effectué.

## Capture guidée

Ouvrir `Capturer_Checkpoint_A.command` à la racine du dépôt dans Terminal.
Le script exécute réellement chaque commande, attend Entrée et ouvre la sélection
macOS de capture. Sélectionner la zone du terminal trois fois. Les PNG sont
sauvegardés directement ici avec les noms imposés. Aucune sortie n’est simulée.
Le contrôle automatique de Terminal étant interdit dans cet environnement,
les captures ont été réalisées par intervention locale. Le script ne publie rien.

## Explication à préparer pour la validation

- `git branch` : l’astérisque marque la branche courante.
- `git switch -c` crée une branche et s’y place.
- `git diff main..feature/display-observation-dates` comparait les deux états avant fusion.
- Le commit `8f1e338` était isolé sur la branche de fonctionnalité avant fusion.
- La fusion fast-forward avance `main` jusqu’au commit existant ; elle reste valide avec un graphe linéaire.
- `git branch --merged main` confirme que la fonctionnalité appartient à `main`.
- Un conflit impose une décision humaine sur le contenu final ; l’exercice fabriqué est facultatif.
- Après validation du professeur, `git branch -d feature/display-observation-dates`
  supprime le nom local de la branche en conservant son commit dans l’historique.
