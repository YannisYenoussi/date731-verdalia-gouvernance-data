# Comparaison des architectures

Responsable : Personne 2.

## Définitions courtes

| Option | Principe | Données typiques |
|---|---|---|
| Data Warehouse centralisé + MDM | entrepôt structuré, modèle défini à l'avance, référentiel client maître | données structurées, requêtes SQL, reporting |
| Data Lake | stockage de fichiers bruts de tous formats, structure appliquée à la lecture | gros volumes, données non structurées |
| Lakehouse | stockage de type lake avec couche transactionnelle et SQL proche d'un entrepôt | structuré et non structuré, analytique avancée |
| Data Mesh | organisation décentralisée : chaque domaine publie ses données comme un produit, avec gouvernance fédérée | grandes organisations à nombreuses équipes data |
| Hybride | entrepôt et MDM pour les données certifiées, plus une zone brute extensible | structuré avec ouverture contrôlée |

## Appréciation qualitative par critère

Les notes de 1 à 5 sont ordinales (5 = le plus favorable). Elles traduisent un jugement argumenté du groupe, non une mesure.

| Critère (poids A) | Warehouse + MDM | Data Lake | Lakehouse | Data Mesh | Hybride | Justification principale |
|---|---|---|---|---|---|---|
| Coût relatif (10) | 4 | 3 | 3 | 2 | 3 | le Warehouse est plus économique pour des volumes modestes ; le Mesh multiplie les équipes et outils |
| Complexité technique (10) | 4 | 2 | 2 | 2 | 3 | le lake et le lakehouse demandent des compétences de moteur de requêtes et de formats ouverts |
| Complexité organisationnelle (10) | 3 | 3 | 3 | 1 | 3 | le Mesh exige des équipes data par domaine ; les autres demandent une gouvernance centrale |
| Qualité et fiabilité (15) | 5 | 2 | 4 | 3 | 5 | le schéma imposé du Warehouse et le MDM fiabilisent ; le lake sans règles dérive en dépôt non exploitable |
| Capacité d'évolution (10) | 3 | 4 | 5 | 5 | 4 | le Warehouse est moins souple pour les données non structurées |
| Sécurité et conformité (15) | 5 | 2 | 4 | 3 | 5 | le contrôle fin des accès et de la conservation est plus simple sur des tables structurées |
| Adaptation à 14 magasins (10) | 5 | 2 | 3 | 1 | 4 | 14 magasins n'ont pas la taille ni les équipes qui justifient un Mesh |
| Délai de mise en œuvre (5) | 4 | 3 | 2 | 1 | 3 | le périmètre du Warehouse est le plus rapide à cadrer |
| Ressources humaines (5) | 4 | 2 | 2 | 1 | 3 | équipe data réduite supposée |
| Maintenance (10) | 4 | 2 | 3 | 2 | 3 | moins de briques à maintenir |

## Résultats

Voir le tableau à quatre scénarios au chapitre 04, section 4.5. Résumé : Warehouse + MDM premier dans les quatre scénarios ; écart minimal de 0,15 point avec l'hybride dans le scénario C (évolutivité privilégiée).

## Pourquoi pas les autres options

Data Lake : la valeur d'un lake apparaît avec des données non structurées et volumineuses ; Verdalia a surtout des données transactionnelles structurées. Sans catalogue ni qualité, un lake produit un dépôt illisible, ce qui aggraverait le problème actuel de chiffres contradictoires.

Lakehouse : option crédible à terme, mais plus de compétences et de composants pour un gain qui n'est pas nécessaire aujourd'hui.

Data Mesh : solution organisationnelle pour de grands groupes dont les équipes de domaine sont autonomes. Verdalia n'a pas encore les rôles de base (Data Owners, Stewards) ; décentraliser avant de centraliser multiplierait les définitions concurrentes de KPI.

Hybride : proche de notre proposition. Nous intégrons déjà une zone brute courte pour l'audit ; l'hybride complet serait justifié si des cas d'usage non structurés apparaissent.

## Limites de la méthode

Les poids reflètent les priorités du groupe ; d'autres lecteurs pourraient en choisir d'autres, d'où les quatre scénarios. Les notes ne tiennent pas compte de prix réels de produits, que nous n'avons pas chiffrés.
