# Contribuer au projet

Projet académique DATE731 (EPSI, Master 1) réalisé par trois étudiants. Ce document résume les règles de collaboration ; la procédure détaillée est dans [organisation/GUIDE_GIT.md](organisation/GUIDE_GIT.md).

## Règles

1. Ne pas committer directement sur `main` après le commit initial : passer par une branche et une Pull Request.
2. Une branche par rôle : `feat/analyse-donnees`, `feat/architecture-trajectoire`, `feat/gouvernance-rgpd-ia`. Des sous-branches sont possibles.
3. Chaque Pull Request est relue par au moins un autre membre avant fusion.
4. Messages de commit au format `type(portée): description`.
5. Distinguer toujours faits de l'énoncé, hypothèses, choix et sources externes (voir `docs/sources/HYPOTHESES_QUESTIONS.md`).
6. Ne jamais inventer une source, une statistique ou une durée légale.
7. Aucune donnée personnelle réelle dans le dépôt.
8. Le Markdown est la source de référence ; le Word et le PowerPoint sont générés par les scripts de `scripts/`.
9. Pas de force push sur `main` ni sur la branche d'un autre membre.
10. Pas de fichier temporaire ni de fichier de configuration personnel dans les commits.

## Style de rédaction

Phrases courtes, français clair, définitions des termes techniques, pas de langage marketing, tableaux lisibles.
