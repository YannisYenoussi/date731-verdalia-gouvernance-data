# Politique d'accès par profil

Responsable : Personne 3, avec la DSI. Exigence : EX-06. Les profils sont des propositions à valider.

## Principes

Moindre privilège, besoin d'en connaître, séparation des fonctions (celui qui demande n'est pas celui qui approuve), accès nominatifs, authentification forte pour les données de niveau Personnel ou Confidentiel, journalisation, revue trimestrielle.

## Profils et droits

| Profil | Périmètre | Données autorisées | Restrictions |
|---|---|---|---|
| Direction générale | entreprise | KPI certifiés, tableaux de bord agrégés | pas d'accès nominatif aux clients |
| Direction financière | entreprise | CA, marge, coûts, détail des ventes | pas d'identité client |
| Direction de magasin | son magasin | ventes, stocks, performance du magasin | pas de marge détaillée par produit si non nécessaire ; pas d'export client |
| Conseiller en magasin | son magasin | fiches produits, stock, historique client limité via l'assistant ou l'outil de vente | pas d'accès au Warehouse ni aux exports |
| Marketing | segments | segments pseudonymisés, audiences filtrées par consentement | pas d'accès à la liste complète sans validation du Data Owner Client |
| Data Steward | son domaine | données de son domaine, files de correction | pas de droits d'administration technique |
| Plateforme data | technique | administration des pipelines et du Warehouse | accès aux données personnelles uniquement pour exploitation, tracé |
| DPO | contrôle | registre, journaux, demandes de droits | lecture ciblée, pas de modification des données |
| Prestataire externe | contractuel | uniquement ce que prévoit le contrat | comptes temporaires, journalisés |

## Contrôles

Accès par groupes de rôles, restriction par magasin et par domaine (sécurité au niveau des lignes), masquage des colonnes sensibles, approbation du Data Owner pour tout accès Confidentiel ou Personnel, comptes d'urgence tracés, désactivation automatique au départ ou au changement de poste (processus RH-DSI), revue des accès chaque trimestre avec signature des Data Owners.

## Preuves

Journal des demandes et approbations, journal des accès, rapport de revue trimestrielle conservé pour audit.

## Cas des exports

Tout export contenant des données de niveau Personnel est généré par la plateforme, journalisé (qui, quoi, pourquoi), limité aux colonnes nécessaires, pseudonymisé si possible, avec date d'expiration. L'envoi par e-mail est interdit.
