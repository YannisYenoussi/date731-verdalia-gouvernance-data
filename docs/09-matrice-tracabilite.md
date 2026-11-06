# 09 — Matrice de traçabilité des exigences

Travail collectif. Fiches complètes : [tracabilite/exigences.md](tracabilite/exigences.md).

| ID | Exigence | Solution retenue | Mécanisme clé | Responsable | Critère de vérification | Chapitres | Auteur principal |
|---|---|---|---|---|---|---|---|
| EX-01 | Vue unique et fiable du client | MDM, identifiant unique | rapprochement, revue humaine, fusion réversible | Data Owner Client | doublons résiduels inférieurs à 1 % (hypothèse) | 02, 04 | Personne 1 |
| EX-02 | Définitions communes des KPI | glossaire, couche métier | calcul unique, validation DAF | Data Owner Finance | KPI publiés uniquement certifiés | 04 | Personne 2 |
| EX-03 | Responsable par jeu de données | Owners et Stewards | catalogue, comité | Sponsor et comité | 100 % des jeux avec Owner | 05 | Personne 3 |
| EX-04 | Gestion RGPD des données clients | registre, bases légales, AIPD | consentement filtré, droits via MDM | DPO | registre complet, droits dans le délai | 03, 06 | Personne 3 |
| EX-05 | Traçabilité des indicateurs | lineage de bout en bout | identifiants de lot, versions | Responsable plateforme data | démonstration complète d'un KPI | 04 | Personne 2 |
| EX-06 | Droits d'accès par profil | accès par rôle | moindre privilège, revue trimestrielle | DSI et RSSI | revue signée, 0 compte injustifié | 05 | Personne 3 |
| EX-07 | Qualité minimale | indicateurs et quarantaine | contrôles à l'ingestion, délais de correction | Data Stewards | indicateurs mensuels dans les seuils | 02 | Personne 1 |
| EX-08 | Encadrement des données de l'IA | API intermédiaire | filtrage, requêtes minimales, vérification humaine | DPO et plateforme data | aucune identité client envoyée au modèle | 04, 06 | Personne 3 |
| EX-09 | Fournisseur et réversibilité | grille et contrat | clauses, test de remplacement | Sponsor et DSI | contrat signé, test réalisé | 04 | Personne 2 |
| EX-10 | Trajectoire 6 et 12 mois | quatre phases, quatre jalons | critères de passage | Comité | J2 et J4 franchis | 08 | Personne 2 |

Contrôle de complétude : les dix identifiants sont présents ; chacun a une solution, un responsable, un critère et un chapitre. Si une exigence évoluait, cette matrice et `tracabilite/exigences.md` doivent être mises à jour ensemble.

Précédent : [08](08-trajectoire.md). Suite : [10 Conclusion](10-conclusion.md).
