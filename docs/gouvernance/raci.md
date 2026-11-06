# Matrice RACI détaillée

Responsable : Personne 3. La matrice est dans [05 Gouvernance](../05-gouvernance-raci.md), section 5.3. Ce document justifie la répartition. Règle : un et un seul A par ligne, vérifié par `scripts/check_raci.py`.

| Activité | A (décide) | Justification du A | Points d'attention |
|---|---|---|---|
| Définition des KPI | Data Owner | le domaine porte la définition ; pour les KPI financiers le Data Owner est la direction financière | validation finale écrite de la DAF pour CA et marge |
| Création d'un jeu de données | Data Owner | il décide de la finalité et de l'usage | le DPO est consulté si des données personnelles sont concernées |
| Correction des erreurs | Data Steward | action courante de qualité ; le Data Owner traite les escalades | délais définis dans la qualité des données |
| Fusion de fiches clients | Data Steward | décision opérationnelle sur les cas incertains | fusions réversibles, journalisées ; cas sensibles remontés au Data Owner Client |
| Gestion des droits d'accès | Data Owner | seul le propriétaire de la donnée accorde l'accès | la plateforme et la DSI exécutent ; revue trimestrielle |
| Modification des règles de conservation | Comité de gouvernance | décision structurante, transversale ; le président du comité en répond | le DPO propose et alerte, ce n'est pas lui qui décide |
| Gestion des consentements | Data Owner Client | responsable métier de la relation client | le DPO contrôle, la plateforme applique techniquement |
| Gestion des incidents | DSI et RSSI | conduite de la réponse technique et de la sécurité | le DPO qualifie l'atteinte aux données personnelles et prépare la notification ; le Sponsor décide de la notification, par délégation du responsable de traitement |
| Validation des données IA | Data Owner | seul le propriétaire autorise l'usage d'une donnée par l'assistant | le DPO est consulté pour toute donnée personnelle |
| Choix du prestataire externe | Sponsor | engagement contractuel de l'entreprise | analyse technique par la plateforme et la DSI ; garanties RGPD par le DPO |
| Validation du déploiement | Sponsor | go ou no-go de chaque phase | le comité recommande sur la base des critères d'acceptation |

Remarque : le RGPD attribue au responsable de traitement (Verdalia) la responsabilité juridique finale. Le Sponsor la représente. La matrice répartit les tâches sans transférer cette responsabilité.
