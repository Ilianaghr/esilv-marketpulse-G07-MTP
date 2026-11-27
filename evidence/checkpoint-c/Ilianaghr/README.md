# Checkpoint C — Ilianaghr

Projet MarketPulse G07-MTP. Dossier individuel d’Iliana Ghoorun (`Ilianaghr`). Collecte effectuée le 27 novembre 2026 sur un clone neuf du [`main` intégrant le TD11](https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP/commit/34325ac958e3c28489b49e80e16f1bcb77c26414). Les changements du TD12 portent sur la documentation, la configuration descriptive et les preuves.

## Contributions

- **TD09** — [Revue de la PR nº 11 d’Antoine](https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP/pull/11#pullrequestreview-6089138551) sur le mapping de l’échantillon Bloomberg et sa conformité au JSON de référence.
- **TD10** — [PR nº 13](https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP/pull/13), fournisseur de l’échantillon approuvé et résultat partagé `build_market_snapshot()`.
- **TD11** — [PR nº 14](https://github.com/Ilianaghr/esilv-marketpulse-G07-MTP/pull/14), affichage Dash du résultat partagé, approuvé par Antoine puis fusionné dans `main`.
- **TD12** — Instructions de réinstallation depuis un clone neuf, mode par défaut explicite et vérification des deux commandes d’exécution.

## Configuration et résultat

Mode final **Bloomberg stage — APPROVED_SAMPLE**. L’application lit le [fichier d’exemple](../../../data/sample/bloomberg_reference_sample.json), conformément au [mapping](../../../docs/BLOOMBERG_FIELD_MAPPING.md). Ce fichier contient des données pédagogiques locales. Aucun accès Bloomberg LIVE n’a été utilisé pendant la validation.

Les séries AAPL et SP500 sont alignées sur 21 séances quotidiennes, du 1ᵉʳ au 30 septembre 2026, sur une fenêtre d’un mois.

| Résultat | AAPL | SP500 |
|---|---:|---:|
| Rendement | +6,48 % | +2,15 % |
| Base 100 initiale | 100,00 | 100,00 |
| Base 100 finale | 106,48 | 102,15 |

Performance relative d’AAPL : **+4,33 points de pourcentage**. L’alignement et les calculs proviennent d’`analytics.py`. Le terminal et Dash lisent les résultats de `build_market_snapshot()`.

## Preuves

| Fichier | Ce qu’il montre |
|---|---|
| [01_final_market_data.png](01_final_market_data.png) | Sortie réelle de `python src/main.py` avec le mode, les deux séries, les dates et les résultats. |
| [02_dash_dashboard.png](02_dash_dashboard.png) | Capture du tableau de bord exécuté depuis le clone neuf. Les trois indicateurs et les deux courbes sont visibles. |
| [03_final_pull_request.png](03_final_pull_request.png) | Capture de la PR nº 14, attribuée à `Ilianaghr`, avec l’approbation d’Antoine et la fusion dans `main`. |
| [04_reproducible_run.png](04_reproducible_run.png) | Extraits des journaux du clone neuf, de l’installation réussie, des deux commandes et des vérifications HTTP. |

Les images 01 et 04 montrent les sorties et journaux réels transcrits dans le navigateur. L’image 04 omet les messages liés au cache local de pip. Les images 02 et 03 sont des captures directes de Dash et de GitHub.

## Reproduire la validation

Suivre les [instructions TD12 à la racine](../../../README.md#install-and-run-marketpulse-td12). Dans un clone neuf de `main` au commit `34325ac`, la création du venv, `python -m pip install -r requirements.txt` et `python -m pip check` ont réussi avec Python 3.13.9. Les versions obtenues étaient Dash 4.5.1, Plotly 7.2.0 et yfinance 1.8.0. `python src/main.py` a affiché les résultats ci-dessus. `python src/dashboard.py` a servi la page et la disposition Dash avec HTTP 200. Les indicateurs et les 21 valeurs de chaque courbe ont été comparés au résultat partagé.

L’installation nécessite l’accès à un index de paquets. L’exécution avec l’échantillon utilise ensuite les fichiers du dépôt. La validation ci-dessus concerne `main` avant la fusion de la documentation du TD12. Les noms des fichiers suivent la [liste du TD12](../../../labs/TD12_INTEGRATION_AND_RELEASE.md#part-13---checkpoint-c-capture).
