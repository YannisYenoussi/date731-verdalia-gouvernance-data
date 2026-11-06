# Qualité des données

Responsable : Personne 1. Exigence : EX-07.

Tous les seuils ci-dessous sont des hypothèses du groupe, à calibrer après une mesure initiale sur les données réelles de Verdalia. Ils ne sont pas issus de normes.

## Indicateurs et seuils cibles

| Dimension | Indicateur | Seuil cible (hypothèse) | Fréquence de mesure |
|---|---|---|---|
| Unicité | part estimée de doublons clients résiduels dans le MDM | inférieure à 1 % à 6 mois | mensuelle, sur échantillon |
| Complétude | tickets avec magasin, date, montant et au moins une ligne | 100 % (sinon quarantaine) | à chaque chargement |
| Complétude | clients fidélisés avec au moins un moyen de contact valide | au moins 85 % à 12 mois | mensuelle |
| Cohérence | écart entre total des caisses et total du Warehouse, par magasin et par jour | inférieur à 0,1 % | quotidienne |
| Exactitude | taux d'erreur relevé lors d'un audit par échantillon (adresse, produit, prix) | inférieur à 2 % | trimestrielle |
| Actualité | chargement des ventes de la veille disponible avant 7 h | 98 % des jours | quotidienne |
| Conformité | clients avec statut de consentement explicite | 100 % | quotidienne |
| Conformité | jeux de données avec un propriétaire déclaré | 100 % | trimestrielle |

## Contrôles à l'ingestion

| Contrôle | Exemple | Action si échec |
|---|---|---|
| Format | date valide, montant numérique, code magasin existant | lot ou ligne en quarantaine |
| Doublon technique | ticket déjà reçu (même magasin, numéro, date) | rejet du doublon, trace dans le journal |
| Cohérence interne | total du ticket égal à la somme des lignes | quarantaine |
| Cohérence référentielle | produit absent du catalogue | ligne en quarantaine, alerte au Steward Produits |
| Volume | écart important avec le volume habituel du magasin | alerte, pas de rejet automatique |
| Champs libres | présence d'informations personnelles inattendues | masquage et alerte au DPO |

## Gestion des anomalies

| Étape | Responsable | Délai cible (hypothèse) |
|---|---|---|
| Détection et alerte automatique | plateforme data | immédiat |
| Qualification (erreur source, règle, volumétrie) | Data Steward du domaine | 1 jour ouvré |
| Correction dans la source ou dans la règle | Steward avec l'équipe concernée | 5 jours ouvrés, 1 jour pour une anomalie bloquant un KPI de direction |
| Rechargement et vérification | plateforme data | 1 jour ouvré après correction |
| Escalade si dépassement | Data Owner puis comité de gouvernance | à l'échéance du délai |

Traçabilité des corrections : chaque correction enregistre l'anomalie, l'auteur, la date, l'ancienne et la nouvelle valeur, et la décision associée. Aucune correction n'est faite dans le Warehouse seul : la source ou la règle est corrigée, puis la donnée est rechargée.

## Exemple de lineage complet

Voir [exemple de traçabilité du CA](../architecture/kpi-et-lineage.md) et le schéma [08](../diagrammes/08-lineage-kpi-ca.png).
