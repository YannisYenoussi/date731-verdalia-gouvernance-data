# 01 — Contexte et besoins

Responsable de la rédaction : Personne 1 (analyse et données). Relecture collective.

## 1.1 Verdalia en chiffres

Verdalia est une entreprise fictive de jardinage et d'équipement extérieur. Les valeurs ci-dessous sont des faits fournis par l'énoncé. Les ratios par jour et par magasin sont des calculs du groupe à partir de ces faits.

| Indicateur | Valeur (énoncé) | Ordre de grandeur calculé |
|---|---|---|
| Magasins | 14 | |
| Salariés | 520 | |
| Chiffre d'affaires | 190 M€ | |
| Clients fidélisés | environ 600 000 | |
| Profils CRM | 650 000 | écart de 50 000 avec les clients fidélisés, à expliquer |
| Références catalogue | 18 000 | |
| Mouvements de stock | 2 millions par an | environ 5 500 par jour |
| Tickets de caisse | 6 millions par an | environ 16 400 par jour, environ 1 200 par magasin et par jour |
| Commandes e-commerce | 400 000 par an | environ 1 100 par jour |

Lecture : ces volumes sont ceux d'une entreprise moyenne. Ils ne justifient pas une plateforme de très grande échelle. L'écart entre 650 000 profils CRM et 600 000 clients fidélisés n'est pas une preuve de doublons (il peut s'agir de profils sans carte, de prospects ou de comptes inactifs), mais c'est la première chose à mesurer lors de l'inventaire.

## 1.2 Les cinq sources actuelles

| Source | Contenu principal | Données personnelles | Point de vigilance |
|---|---|---|---|
| ERP | catalogue, stocks, achats | non pour le catalogue ; oui pour des contacts fournisseurs éventuels | référence de vérité pour le stock |
| Caisses magasins | tickets de vente | oui si la carte de fidélité est scannée | identification client partielle |
| Site e-commerce | commandes, comptes clients, navigation | oui, y compris données de navigation | cookies et traceurs |
| CRM fidélité | profils, points, consentements marketing | oui, cœur des données clients | doublons, consentements à fiabiliser |
| Excel | exports et suivis non maîtrisés | souvent oui | circulation par e-mail, aucune traçabilité |

## 1.3 Problèmes constatés et causes probables

| Problème (énoncé) | Cause probable (hypothèse du groupe) | Effet métier |
|---|---|---|
| Clients en plusieurs exemplaires | pas d'identifiant commun entre caisse, e-commerce et CRM | vision client fausse, sollicitations en double |
| Orthographes et identifiants incohérents | saisie libre, pas de normalisation | rapprochements impossibles |
| Chiffres d'affaires différents | périmètres et règles de calcul propres à chaque service | décisions contradictoires |
| Pas de définition unique des KPI | absence de glossaire validé | débats sur les chiffres plutôt que sur les actions |
| Exports clients par e-mail | pas de libre-service sécurisé | risque de fuite et de non-conformité |
| Responsabilités floues | pas de Data Owner | corrections sans propriétaire |
| Durées de conservation inconnues | pas de registre des traitements | risque RGPD |
| Transformations difficiles à tracer | calculs dans des fichiers Excel | impossibilité d'auditer un chiffre |
| Pas de stratégie commune | projets isolés | duplication des efforts |

## 1.4 Ambitions de la direction

1. Tableaux de bord communs.
2. Vision client unique.
3. Indicateurs financiers cohérents.
4. Meilleure utilisation des données de fidélité.
5. Assistant IA interne testé dans deux magasins.
6. Gestion responsable et conforme des informations clients.

## 1.5 Besoins fonctionnels et contraintes

Les dix exigences officielles (EX-01 à EX-10) sont reformulées dans le chapitre 09 et dans `docs/tracabilite/exigences.md`. Elles se regroupent en quatre familles de besoins :

- Fiabiliser : vue client unique (EX-01), qualité minimale (EX-07), traçabilité des indicateurs (EX-05).
- Partager : définitions communes des KPI (EX-02), responsables de jeux de données (EX-03).
- Protéger : RGPD (EX-04), droits d'accès (EX-06), encadrement de l'IA (EX-08), fournisseur et réversibilité (EX-09).
- Planifier : trajectoire à 6 et 12 mois (EX-10).

Contraintes retenues : projet de conception (aucun développement), pas de budget fourni, équipe data interne de taille réduite (hypothèse), obligation de conformité RGPD.

## 1.6 Périmètre

Dans le périmètre : les cinq sources, le socle data, la gouvernance, la conformité, le pilote d'assistant IA dans deux magasins.
Hors périmètre : choix d'un produit précis (nous raisonnons par capacités), développement, données RH, données fournisseurs détaillées.

## 1.7 Problématique

Comment donner à 14 magasins une base de données commune, fiable et conforme, qui supporte aussi un assistant IA interne, sans accumuler de technologies que Verdalia ne saurait pas gouverner ?

Précédent : [00 Synthèse](00-synthese-executive.md). Suite : [02 Cartographie des données](02-cartographie-donnees.md).
