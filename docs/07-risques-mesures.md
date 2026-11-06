# 07 — Risques et mesures

Responsable : Personne 3, avec contributions de Personne 2 pour les risques de calendrier. Les niveaux (faible, moyen, élevé) sont des appréciations qualitatives du groupe, non chiffrées.

| ID | Risque | Probabilité | Impact | Mesure de réduction | Responsable | Phase |
|---|---|---|---|---|---|---|
| R01 | Faux rapprochements clients (deux personnes fusionnées) | moyenne | élevé | seuils prudents, revue humaine, fusion réversible, journal | Data Steward Client | 2 |
| R02 | Doublons résiduels qui faussent la vision client | moyenne | moyen | mesure mensuelle, amélioration des règles, file de revue | Data Steward Client | 2 à 4 |
| R03 | Désaccord sur la définition du CA ou de la marge | élevée | élevé | glossaire, validation écrite de la DAF, version unique | Data Owner Finance | 1 et 2 |
| R04 | Faible implication des métiers (Data Owners absents) | moyenne | élevé | sponsor actif, rôles nommés en phase 1, comité mensuel | Sponsor | 1 |
| R05 | Qualité des sources inférieure aux hypothèses | élevée | moyen | mesure initiale, quarantaine, plan de correction à la source | Data Stewards | 1 et 2 |
| R06 | Retard de l'inventaire ou de l'accès aux sources | moyenne | moyen | accès demandés dès le mois 1, priorisation des sources | Responsable plateforme data | 1 |
| R07 | Fuite via exports et fichiers Excel persistants | moyenne | élevé | interdiction e-mail, libre-service BI, registre Excel, sensibilisation | DSI, DPO | 1 à 3 |
| R08 | Accès excessifs ou comptes non retirés | moyenne | élevé | moindre privilège, revue trimestrielle, processus départs | DSI, Data Owners | 3 |
| R09 | Non-conformité RGPD (durées, consentements, information) | moyenne | élevé | registre, AIPD, validation du DPO, preuves | DPO | 1 à 3 |
| R10 | Défaillance ou changement de fournisseur IA | moyenne | moyen | API de découplage, contrat de réversibilité, test de remplacement | DSI | 3 et 4 |
| R11 | Réponses erronées de l'IA suivies par les conseillers | moyenne | moyen | sources citées, vérification humaine, retour d'erreurs, périmètre limité | Data Owner Produits | 4 |
| R12 | Injection de prompt ou fuite par le modèle | moyenne | élevé | tests, filtrage, pas d'outils d'écriture, journalisation | RSSI | 3 et 4 |
| R13 | Dépassement du calendrier (charge sous-estimée) | élevée | moyen | jalons de passage, périmètre minimal viable, revue à chaque fin de phase | Sponsor, comité | toutes |
| R14 | Charge de travail excessive de l'équipe data réduite | moyenne | moyen | priorisation, appui externe ponctuel si besoin, périmètre progressif | Responsable plateforme data | 2 et 3 |
| R15 | Résistance au changement dans les magasins | moyenne | moyen | formation, référents magasin, communication, bénéfices visibles | Direction commerciale | 2 à 4 |
| R16 | Évolution réglementaire (AI Act, doctrine CNIL) | moyenne | moyen | veille, revue du DPO à chaque jalon | DPO | toutes |
| R17 | Perte de confiance si un incident survient pendant le pilote | faible | élevé | procédure d'incident, communication, arrêt du pilote possible | Sponsor, RSSI | 4 |

Risques majeurs à défendre à l'oral : R01 (faux rapprochements), R03 (KPI), R04 (implication des métiers), R13 (calendrier).

Précédent : [06](06-rgpd-ia-responsable.md). Suite : [08 Trajectoire](08-trajectoire.md).
