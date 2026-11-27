# Checkpoint B — Ilianaghr

Projet : ESILV MarketPulse G07-MTP. Étudiante : Iliana Ghoorun (`Ilianaghr`).
Collecte des preuves : 27 novembre 2026. Base vérifiée : `eb84846`.

## Contribution individuelle et collaboration

- **TD05** : [PR nº 5](https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP/pull/5), branche `docs/clarify-sample-execution`, commit `aa09537`. Amélioration des instructions Python, des résultats attendus et du diagnostic de répertoire. Revue par Antoine (`sendyourcode`), puis fusion dans `main`.
- **TD06** : [revue de la PR nº 4 d’Arnaud](https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP/pull/4#pullrequestreview-5895167194), publiée sous `Ilianaghr`. Vérification du libellé CSV, de la configuration, de la conservation des résultats et d’une intégration locale ; approbation sans correction nécessaire. La PR a ensuite été fusionnée.
- **TD07, travail commun** : [PR nº 9 d’Arnaud](https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP/pull/9), alignement des dates et calculs réutilisables.
- **TD08, travail commun** : [PR nº 10 d’Antoine](https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP/pull/10), fournisseur Yahoo, relu par Arnaud puis fusionné. Ce dossier valide l’exécution de ce code partagé ; il ne m’en attribue pas l’écriture.

## Preuves

| Fichier | Contenu |
|---|---|
| `01_pull_request.png` | Capture de ma PR nº 5, avec auteur, branche, description, revue et fusion. |
| `02_code_review.png` | Capture de ma revue technique et de mon approbation sur la PR nº 4 d’Arnaud. |
| `03_yahoo_market_data.png` | Capture du compte rendu de récupération Yahoo réelle : symboles, dates, effectifs et dernières lignes canoniques. |
| `04_instrument_benchmark.png` | Capture du compte rendu des résultats MarketPulse : AAPL, SP500, période, intervalle, rendements, performance relative et base 100. |

Les deux premières images sont des captures directes de GitHub. Les deux dernières
sont des captures d’une restitution dans le navigateur des sorties Python réellement
obtenues le 27 novembre à 14 h 43 (heure de Paris), et non des captures de Terminal.
Elles utilisent les mêmes réponses réelles de `fetch_yahoo_prices()` pour les deux
vues. Le programme `python -B src/main.py` a également été exécuté avec succès
séparément. Aucun résultat CSV ni donnée simulée n’a remplacé Yahoo.
Les quatre images ont été vérifiées visuellement et ne montrent aucun secret.

## Résultat constaté

Paramètres : `period="1mo"`, `interval="1d"`, `auto_adjust=False`.
`AAPL` utilise le symbole Yahoo `AAPL` ; `SP500` utilise `^GSPC` puis conserve
son ticker canonique `SP500` dans les lignes normalisées.

| Série | Dates communes | Observations | Premier cours | Dernier cours | Rendement | Base 100 finale |
|---|---|---:|---:|---:|---:|---:|
| AAPL | 2026-10-26 → 2026-11-25 | 23 | 343.91 USD | 355.58 USD | +3.39 % | 103.39 |
| SP500 | 2026-10-26 → 2026-11-25 | 23 | 7676.77 | 7182.78 | −6.43 % | 93.57 |

Performance relative : **+9.83 points de pourcentage**, calculée avant arrondi.
Ces valeurs décrivent la réponse obtenue lors de la collecte ; une nouvelle requête
peut retourner une fenêtre ou des valeurs différentes.

## Points à expliquer

L’alignement retient les dates communes triées avant comparaison. Le rendement
vaut `(dernier cours / premier cours - 1) × 100`. La base 100 vaut
`cours / premier cours × 100`. La performance relative est la différence entre
les deux rendements, en points de pourcentage. `analytics.py` reste indépendant
du fournisseur ; `yfinance` gère l’acquisition et n’est pas une API officielle Yahoo.

Les noms des cinq fichiers suivent la partie Checkpoint B du TD08 présent dans
`labs/TD08_YAHOO_FINANCE.md`. Le contrat détaillé
`docs/04_CHECKPOINTS_AND_EVIDENCE.md` est absent de ce dépôt. La compréhension
personnelle et l’acceptation finale des preuves restent à valider avec l’enseignant.
