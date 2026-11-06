# Durées de conservation : base, statut et validation

Responsable : Personne 3. Principe : article 5.1.e du RGPD (limitation de la conservation). Nous n'inventons aucune durée légale.

Légende des statuts : OL = obligation légale ; REC = recommandation d'une autorité (non contraignante) ; INT = proposition interne du groupe ; À VÉRIFIER = non confirmé.

Vérifications faites le 6 novembre 2026 : lecture d'extraits de résultats de recherche ; les textes complets n'ont pas été relus. Voir [BIBLIOGRAPHIE](../sources/BIBLIOGRAPHIE.md).

| Donnée | Durée proposée | Statut | Base ou justification | Validation DPO demandée |
|---|---|---|---|---|
| Documents comptables et pièces justificatives (factures, tickets servant de pièces) | 10 ans | OL | article L123-22 du code de commerce, confirmé par la documentation fiscale BOFiP | périmètre exact : quels tickets et quelles données nominatives sont des pièces |
| Délai fiscal de conservation des documents contrôlables (livre des procédures fiscales) | à confirmer | À VÉRIFIER | des sources secondaires évoquent une évolution récente du délai ; non recoupée sur Légifrance | vérifier la version en vigueur de l'article L.102 B |
| Données clients pour gestion commerciale et prospection | durée de la relation commerciale puis 3 ans | REC | référentiel CNIL de gestion des activités commerciales, non contraignant | définir l'événement de départ (dernier achat, dernière connexion) ; la simple ouverture d'un e-mail ne prolonge pas selon les sources consultées |
| Données de prospects | 3 ans après collecte ou dernier contact émanant du prospect | REC | même référentiel | idem |
| Compte fidélité inactif | anonymisation ou suppression après 3 ans d'inactivité | INT | alignée sur la recommandation ci-dessus | valider la définition d'inactivité et l'information préalable |
| Preuve du consentement et des oppositions | durée du traitement concerné puis durée de preuve | INT / À VÉRIFIER | besoin de démontrer la conformité | durée de preuve (prescription) |
| Données de navigation et traceurs | à fixer | À VÉRIFIER | lignes directrices de la CNIL sur les traceurs à consulter | durées maximales de cookies et de données |
| Zone brute (copie des lots) | 90 jours après chargement validé | INT | audit et rechargement ; au-delà, les tables de faits suffisent | proportionnalité |
| Quarantaine | 30 jours maximum | INT | correction rapide | proportionnalité |
| Journaux d'ingestion et d'accès | 6 mois (proposition) | INT / À VÉRIFIER | sécurité ; comparer avec les recommandations CNIL sur la journalisation | durée définitive |
| Journaux de l'assistant IA | 6 mois (proposition), contenu des questions non conservé au-delà du nécessaire | INT | sécurité et amélioration, minimisation | durée et contenu |
| Demandes d'exercice des droits | durée à fixer | À VÉRIFIER | preuve de traitement de la demande | durée de preuve |
| Fichiers Excel déclarés | durée déclarée par le propriétaire, au plus celle du jeu source | INT | éviter les copies orphelines | validation lors du recensement |

Règle de lecture : une durée de type REC ou INT peut être différente si Verdalia la justifie par écrit dans son registre. Une durée OL ne peut pas être raccourcie. La conservation de pièces comptables pendant 10 ans ne justifie pas de conserver les coordonnées d'un client pendant 10 ans : on dissocie les données nominatives dès que la finalité prend fin.
