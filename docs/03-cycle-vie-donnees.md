# 03 — Cycle de vie des données

Responsable : Personne 1. Les durées citées sont détaillées et qualifiées dans [rgpd/durees-conservation.md](rgpd/durees-conservation.md) ; elles distinguent obligation légale, recommandation et proposition interne.

![Cycle de vie](diagrammes/04-cycle-vie-donnee.png)

## 3.1 Les cinq étapes

Pour chaque famille (opérationnelles, de référence, sensibles, stratégiques), le tableau indique les règles applicables. Une donnée appartenant à plusieurs familles cumule les règles, la plus stricte l'emportant.

| Étape | Règles communes | Responsable | Preuve de conformité |
|---|---|---|---|
| 1. Collecte | finalité définie avant collecte, minimisation, information des personnes, consentement lorsqu'il est requis | Data Owner du domaine, DPO pour l'information | registre des traitements, mentions d'information, journal des consentements |
| 2. Stockage | zone selon le niveau de classification, chiffrement, droits par profil | Responsable plateforme data, DSI | matrice d'accès, journaux d'accès |
| 3. Traitement | contrôles qualité, rapprochement MDM, transformations documentées | Data Steward, plateforme data | journal d'ingestion, lineage, journal de fusion |
| 4. Analyse et utilisation | KPI certifiés, droits par rôle, marketing sous conditions RGPD, IA via API | Data Owner, utilisateurs métiers | catalogue des KPI, journaux de requêtes |
| 5. Archivage ou destruction | durée justifiée, anonymisation ou effacement, archivage intermédiaire si obligation | Data Owner, DPO | journal de purge, preuve d'anonymisation |

## 3.2 Application par famille

| Famille | Collecte | Stockage | Traitement | Utilisation | Fin de vie |
|---|---|---|---|---|---|
| Opérationnelles (tickets, commandes, mouvements) | à la source (caisse, site, ERP) | zone brute courte puis Warehouse | contrôles à l'ingestion | agrégats et KPI | pièces comptables conservées selon l'obligation légale ; données nominatives dissociées ou anonymisées quand la finalité disparaît |
| De référence (clients, produits, magasins) | création contrôlée, une seule fois | MDM, tables de dimensions | déduplication, normalisation | clé de jointure commune | fiches clients inactives supprimées ou anonymisées selon la durée validée par le DPO |
| Sensibles (identité, contacts, consentements, marge) | minimale, avec information | zone à accès restreint, chiffrée | accès tracés | usage limité par rôle et finalité | effacement sur demande, sauf obligation légale de conserver |
| Stratégiques (KPI certifiés, prévisions) | calculées, non collectées | couche métier | règles versionnées | tableaux de bord | historique conservé pour comparaison selon décision du comité |

## 3.3 Zones techniques et durées proposées

| Zone | Contenu | Durée proposée (proposition interne) | Justification |
|---|---|---|---|
| Brute | copie fidèle des lots reçus | 90 jours après chargement validé pour les données personnelles | audit et rechargement ; au-delà, les tables de faits suffisent |
| Quarantaine | lots rejetés | 30 jours maximum | correction rapide ou abandon |
| Warehouse | données consolidées | selon la famille (voir durées) | finalité et obligations |
| Journaux techniques | ingestion, accès | à fixer avec le RSSI et le DPO | proportionnalité |

## 3.4 Droit à l'effacement dans le cycle de vie

Procédure : demande reçue par le point de contact du DPO, identification de la personne, recherche de toutes les occurrences via l'identifiant client unique, effacement ou anonymisation dans le CRM, l'e-commerce et le MDM, rupture du lien nominatif dans le Warehouse (les ventes restent comme données anonymisées lorsque la conservation comptable l'exige), information des sous-traitants, réponse à la personne dans le délai légal. Les sauvegardes expirent par rotation, sans restauration des données effacées. Détails au chapitre 06.

Précédent : [02](02-cartographie-donnees.md). Suite : [04 Architecture cible](04-architecture-cible.md).
