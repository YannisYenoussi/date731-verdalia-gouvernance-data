# ADR-001 — Architecture cible des données de Verdalia

Statut : proposé par le groupe, à valider lors de la soutenance et par la direction.
Date : 6 novembre 2026.
Auteurs : équipe DATE731 (3 étudiants). Rédaction principale : Personne 2.

## Contexte

Verdalia exploite cinq sources (ERP, caisses de 14 magasins, e-commerce, CRM fidélité, Excel) sans identifiant client commun ni définition unique des KPI. Volumes annuels : 6 millions de tickets, 2 millions de mouvements de stock, 400 000 commandes. Une conformité RGPD et un assistant IA pilote dans deux magasins sont attendus.

## Problème

Quelle architecture de données permet d'obtenir des chiffres cohérents et une vue client unique, tout en restant gouvernable par une organisation de taille moyenne et en encadrant l'accès de l'IA aux données ?

## Options

1. Data Warehouse centralisé avec MDM client.
2. Data Lake.
3. Lakehouse.
4. Data Mesh.
5. Approche hybride (Warehouse, MDM et zone brute extensible).

Description et justification : [comparaison-architectures](../architecture/comparaison-architectures.md).

## Critères de décision

Dix critères : coût relatif, complexité technique, complexité organisationnelle, qualité et fiabilité, capacité d'évolution, sécurité et conformité, adaptation à 14 magasins, délai, ressources humaines, maintenance. Pondération du groupe (somme 100) : qualité 15, sécurité 15, coût 10, complexité technique 10, complexité organisationnelle 10, évolution 10, adaptation 10, maintenance 10, délai 5, ressources 5. Notes ordinales de 1 à 5, appréciations qualitatives. Test de sensibilité avec trois autres jeux de poids.

Résultats (note sur 5) :

| Option | A. Poids du groupe | B. Égaux | C. Évolutivité | D. Délai et coût |
|---|---|---|---|---|
| Warehouse + MDM | 4,20 | 4,10 | 3,90 | 4,20 |
| Hybride | 3,80 | 3,60 | 3,75 | 3,55 |
| Lakehouse | 3,30 | 3,10 | 3,65 | 2,95 |
| Data Lake | 2,45 | 2,50 | 2,75 | 2,50 |
| Data Mesh | 2,30 | 2,10 | 2,90 | 1,95 |

## Décision retenue

Architecture centralisée et modulaire : ingestion ELT, zone de préparation avec quarantaine, MDM client, Data Warehouse en étoile, couche métier de KPI certifiés, consommation par tableaux de bord, marketing sous conditions RGPD et assistant IA via API sécurisée. Une zone brute à durée limitée est conservée pour l'audit. Le Warehouse est pseudonymisé (ADR-003) et l'IA n'y accède jamais directement (ADR-002).

## Conséquences positives

- Une seule source de chiffres et un seul calcul du CA.
- Vue client unique et corrections traçables.
- Contrôle d'accès et conservation plus simples à gouverner.
- Mise en œuvre progressive adaptée à une petite équipe.

## Limites

- Moins souple pour des données non structurées volumineuses.
- Point de centralisation : une erreur de règle se propage à tous les rapports, d'où le contrôle de version et la recette.
- Dépendance à la qualité des sources et à l'engagement des métiers (Data Owners).
- Notes qualitatives : le classement reste sensible à la pondération (écart réduit dans le scénario C).

## Compromis

Nous acceptons une moindre capacité d'évolution immédiate contre la simplicité, la fiabilité et la conformité. Nous acceptons que l'assistant IA reçoive moins de contexte (pas d'identité client) contre une exposition réduite des données.

## Conditions de réexamen

Réexaminer la décision si : le nombre de magasins dépasse environ 28 ou la charge de chargement ne tient plus dans la fenêtre prévue ; des cas d'usage non structurés significatifs apparaissent (images, journaux de navigation détaillés) ; le pilote IA montre un besoin de données que l'API ne peut pas fournir ; une organisation avec équipes data autonomes par domaine se met en place ; le bilan à 12 mois révèle des coûts ou délais très supérieurs aux estimations.
