# Rapport de validation

Date : 6 novembre 2026. Statuts : Validé (vérifié par une commande ou une lecture effectivement réalisée), À vérifier (fait mais incomplet ou à confirmer par un humain), Non réalisé, Bloqué.

Aucun test logiciel n'existe : le projet est un travail de conception. Ce rapport ne déclare comme validé que ce qui a été exécuté.

## Validé

| Vérification | Moyen | Résultat |
|---|---|---|
| Les 8 diagrammes Mermaid sont syntaxiquement valides | `bash scripts/build_diagrams.sh` (rendu avec mermaid-cli) | 16 exports SVG et PNG générés sans erreur ; une erreur initiale du Gantt (deux-points dans les libellés) a été corrigée |
| Lisibilité des diagrammes | lecture visuelle des rendus d'architecture et du Gantt | architecture refaite en disposition verticale pour être lisible |
| Matrice RACI : un seul A par ligne et au moins un R | `python3 scripts/check_raci.py` | 11 lignes, aucune erreur |
| Calcul de la grille de comparaison | `python3 scripts/score_architectures.py` | scores du chapitre 04 et de l'ADR-001 recopiés depuis la sortie du script ; poids de chaque scénario somment à 100 |
| Dix exigences traitées | relecture de `docs/tracabilite/exigences.md` et `docs/09-matrice-tracabilite.md` | EX-01 à EX-10 présentes, chacune avec solution, mécanisme, responsable, critère, chapitres |
| Absence de texte en gras dans les documents Markdown | recherche de la séquence de gras | aucune occurrence |
| Dossier Word | génération par `scripts/build_docx.py`, ouverture avec python-docx, conversion en PDF avec LibreOffice, lecture visuelle des 12 premières pages sur 56 | fichier modifiable ; 14 titres de niveau 1, 65 tableaux, 10 images ; page de garde, numérotation et tableaux lisibles sur les pages contrôlées |
| PowerPoint | génération par `scripts/build_pptx.py`, ouverture avec python-pptx, conversion en PDF avec LibreOffice, lecture visuelle | 14 diapositives (13 plus une annexe), notes d'orateur sur les 13 diapositives, schémas principaux en formes modifiables |
| Vingt questions du jury au minimum | comptage | 26 questions avec réponses |
| Répartition de la parole | comptage de mots du script | environ 550 mots par orateur (551, 553, 550) |

## À vérifier

| Point | Pourquoi | Action |
|---|---|---|
| Liens internes | `python3 scripts/check_links.py` est exécuté avant chaque commit ; relancer après toute modification | voir le résultat de la dernière exécution dans la sortie du script |
| Table des matières du Word | c'est un champ Word : elle s'affiche après « Mettre à jour les champs » à l'ouverture | accepter la mise à jour à l'ouverture, ou clic droit sur la table |
| Pages 13 à 56 du Word | seules les 12 premières pages ont été relues visuellement | parcourir le PDF complet, surtout les tableaux larges (RACI, registre, risques) |
| Dernière version de la diapositive 8 (Gantt) | libellés raccourcis après la dernière lecture visuelle | rouvrir le PowerPoint |
| Durée de 15 minutes | le script compte environ 550 mots par orateur ; aucune répétition chronométrée | répéter avec un chronomètre |
| Sources juridiques | consultées uniquement par extraits de résultats de recherche le 6 novembre 2026 ; aucun texte intégral relu | voir `docs/sources/BIBLIOGRAPHIE.md`, section 5 |
| Date de modification de l'AI Act (règlement 2026/1744) et évolution du délai fiscal | rapportées par des sources secondaires | vérifier sur EUR-Lex et Légifrance |
| Neuf parties officielles du dossier | cahier des charges non disponible ; chapitres 01 à 09 supposés correspondre | confronter au cahier des charges |
| Hypothèses chiffrées (seuils qualité, charges, notes, durées internes) | non issues de l'énoncé | voir `docs/sources/HYPOTHESES_QUESTIONS.md` |
| Compatibilité de mise en page dans Microsoft Word et PowerPoint | contrôle fait avec LibreOffice uniquement | ouvrir dans les applications Microsoft |

## Non réalisé

- Lecture des documents de cours et du cahier des charges officiel : fichiers absents du workspace (recherche effectuée, aucun résultat).
- Archive `DATE731_Verdalia_Projet_Git_Equipe3.zip` : absente, aucun travail existant à préserver ou à reprendre.
- Chiffrage en euros : volontairement non fait (aucun budget dans l'énoncé).
- Répétition chronométrée de la soutenance.
- Création des Issues GitHub (voir Bloqué).

## Bloqué

| Étape | Cause | Conséquence |
|---|---|---|
| Création du dépôt GitHub privé `date731-verdalia-gouvernance-data` | `gh auth status` indique que le jeton GH_TOKEN est invalide | aucun dépôt distant, aucun `origin`, aucun push |
| Issues par membre | dépend du dépôt distant | non créées ; les tâches sont dans `organisation/TACHES.md` |

Commandes à exécuter pour terminer la publication (après `gh auth login` ou jeton valide) :

```bash
cd date731-verdalia-gouvernance-data
gh repo create date731-verdalia-gouvernance-data --private --source=. --remote=origin
git push -u origin main
git push -u origin feat/analyse-donnees feat/architecture-trajectoire feat/gouvernance-rgpd-ia
git ls-remote --heads origin    # vérifier les quatre branches distantes
```

Si le dépôt existe déjà sur le compte, ne pas relancer `gh repo create` : ajouter seulement l'origine avec `git remote add origin <url>`.

## Git (état local)

L'état suivant est vérifié par les commandes `git branch -v`, `git log` et `git status` exécutées après le commit initial (sortie reproduite dans le message de fin de session) : branche `main`, trois branches de travail créées au même commit, arbre de travail propre, aucun fusion, aucun force push.
