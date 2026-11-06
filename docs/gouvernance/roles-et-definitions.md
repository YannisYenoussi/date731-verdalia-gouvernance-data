# Rôles et responsabilités

Responsable : Personne 3. Exigence : EX-03.

## Data Owners proposés et jeux de données

| Domaine | Data Owner proposé | Data Steward proposé | Jeux de données placés sous sa responsabilité |
|---|---|---|---|
| Client et fidélité | Direction marketing et relation client | Responsable CRM | profils CRM, MDM client, consentements, points |
| Ventes et magasins | Direction commerciale et exploitation | Adjoint de magasin référent | tickets, lignes de ticket, dim_magasin |
| Produits et stocks | Direction achats et approvisionnement | Responsable catalogue | catalogue, prix, stocks, mouvements |
| Finance | Direction financière | Contrôleur de gestion | KPI financiers, règles de CA et de marge |
| E-commerce | Responsable e-commerce | Chef de produit web | commandes web, comptes, navigation |

Règle EX-03 : aucun jeu de données n'est publié dans le Warehouse sans Data Owner et Data Steward déclarés dans le catalogue. Un jeu orphelin est mis en quarantaine d'accès.

## Rituels

Comité de gouvernance mensuel (ordre du jour : KPI, incidents, demandes d'accès sensibles, qualité, jalons). Revue trimestrielle des accès et des durées de conservation. Point hebdomadaire des Data Stewards pendant le déploiement.

## Charge indicative (hypothèse du groupe)

Data Owner : environ une demi-journée par mois. Data Steward : de 10 à 20 % du temps durant le déploiement, à confirmer en phase 1. Ces valeurs sont des estimations, non issues de l'énoncé.
