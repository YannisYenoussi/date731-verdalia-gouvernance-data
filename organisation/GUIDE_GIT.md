# Guide Git pour le groupe

Dépôt cible : `date731-verdalia-gouvernance-data` (privé). Branche principale : `main`. Branches de travail : `feat/analyse-donnees`, `feat/architecture-trajectoire`, `feat/gouvernance-rgpd-ia`.

## 1. Installation

Installer Git (https://git-scm.com), puis configurer son identité :

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "adresse@exemple.fr"
```

Optionnel : GitHub CLI (`gh`) puis `gh auth login`.

## 2. Cloner le dépôt

```bash
git clone https://github.com/<organisation-ou-compte>/date731-verdalia-gouvernance-data.git
cd date731-verdalia-gouvernance-data
```

Le dépôt est privé : le propriétaire doit ajouter les deux autres membres comme collaborateurs (Settings, Collaborators).

## 3. Créer ou changer de branche

```bash
git fetch origin
git switch feat/analyse-donnees          # ou la branche de votre rôle
git branch --show-current                # vérifier
```

Pour une nouvelle sous-branche : `git switch -c feat/analyse-donnees-mdm`.

## 4. Récupérer les changements (pull)

```bash
git pull --ff-only origin <votre-branche>
```

L'option `--ff-only` évite une fusion implicite imprévue.

## 5. Ajouter et valider (add, commit)

```bash
git status
git add docs/donnees/mdm-client.md
git commit -m "docs(data): détailler les règles de rapprochement MDM"
```

Ajouter les fichiers un par un ou par dossier ; éviter `git add .` sans avoir lu `git status`.

## 6. Pousser (push)

```bash
git push -u origin <votre-branche>     # premier push
git push                               # ensuite
```

Ne jamais utiliser `git push --force` sur `main` ni sur la branche d'un autre membre.

## 7. Pull Request

1. Sur GitHub, ouvrir une Pull Request de votre branche vers `main`.
2. Remplir le modèle (résumé, fichiers, vérifications).
3. Demander une relecture à un autre membre.

## 8. Revue

Le relecteur vérifie : cohérence avec les autres chapitres, hypothèses signalées, sources citées, liens valides, absence de données personnelles réelles, orthographe. Il commente, demande des corrections, puis approuve. L'auteur ne fusionne pas sa propre PR sans approbation.

## 9. Synchroniser sa branche avec `main`

```bash
git fetch origin
git switch <votre-branche>
git merge origin/main
```

Alternative avec historique linéaire (réservée à une branche que vous seul utilisez) : `git rebase origin/main`, suivie d'un `git push --force-with-lease` uniquement sur votre propre branche.

## 10. Résoudre un conflit

```bash
git merge origin/main
# Git signale "CONFLICT" ; ouvrir le fichier, chercher <<<<<<<, =======, >>>>>>>
# garder la bonne version (ou combiner), supprimer les marqueurs
git add <fichier>
git commit
```

En cas de doute, parler à l'auteur de l'autre modification avant de trancher. Pour annuler une fusion en cours : `git merge --abort`.

## 11. Convention de commit

Format : `type(portée): description à l'infinitif, en minuscules`.

| Type | Usage |
|---|---|
| docs | documentation (usage principal) |
| feat | nouveau contenu important |
| fix | correction d'une erreur |
| chore | maintenance, scripts, configuration |
| style | mise en forme sans changement de sens |

Portées usuelles : data, architecture, rgpd, gouvernance, ia, presentation, organisation.

Exemples :

```
docs(data): documenter la cartographie des sources
docs(architecture): ajouter le schéma cible
docs(rgpd): définir les règles de conservation
fix(gouvernance): corriger le A de la ligne conservation
```

## 12. Régénérer les livrables

```bash
bash scripts/build_diagrams.sh     # exports SVG et PNG
python3 scripts/build_docx.py      # dossier Word
python3 scripts/build_pptx.py      # présentation
python3 scripts/check_raci.py      # un seul A par ligne
python3 scripts/check_links.py     # liens internes
```

Le Markdown reste la source de référence : modifier le Markdown puis régénérer, ne pas éditer le Word seul sans reporter les changements.
