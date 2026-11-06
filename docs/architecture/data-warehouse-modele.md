# Modèle du Data Warehouse

Responsable : Personne 2. Conception logique, sans implémentation.

## Principe

Modèle en étoile : des tables de faits (événements mesurables) entourées de dimensions (axes d'analyse).

## Dimensions

| Dimension | Contenu | Historisation | Remarque |
|---|---|---|---|
| dim_client | identifiant client unique, tranche d'âge, code postal tronqué, ancienneté, statut fidélité | oui, pour les changements de statut | pas de nom ni de coordonnées : voir ADR-003 |
| dim_produit | référence, famille, marque, statut | oui, pour les changements de famille | 18 000 références |
| dim_magasin | code, région, surface, date d'ouverture, type (magasin ou e-commerce) | oui | 14 magasins aujourd'hui |
| dim_date | jour, semaine, mois, saison, jour férié | non | la saisonnalité du jardinage compte |

Historisation justifiée : on conserve l'historique quand une analyse passée doit refléter la situation de l'époque (un produit change de famille ; un client change de statut). Sinon, la valeur courante suffit, pour limiter la complexité et le volume de données personnelles.

## Faits

| Fait | Grain | Mesures | Dimensions liées |
|---|---|---|---|
| fait_ventes_ligne | une ligne de ticket ou de commande | quantité, montant HT, remise, TVA, coût d'achat | client (si identifié), produit, magasin, date |
| fait_mouvement_stock | un mouvement de stock | quantité signée, type de mouvement | produit, magasin, date |
| fait_consentement (optionnel) | un changement de statut | type de consentement, valeur | client, date |

## Tables analytiques et agrégats

Agrégats préparés pour la performance : ventes par magasin et par jour, par famille et par semaine ; rotation des stocks. Les KPI certifiés sont calculés à partir de ces tables, jamais à la main.

## Accès

Rôles décrits dans [gouvernance/politique-acces](../gouvernance/politique-acces.md). Les colonnes de coût d'achat et de marge sont réservées aux profils autorisés.
