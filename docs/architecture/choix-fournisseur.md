# Fournisseur externe et réversibilité

Responsable : Personne 2 (choix), avec Personne 3 (clauses RGPD). Exigence : EX-09.

## Périmètre

Deux catégories de fournisseurs sont possibles : celui du modèle d'IA et celui de la plateforme (hébergement du Warehouse, outils d'ingestion). Le choix d'un produit précis n'est pas fait ici ; nous définissons une grille de sélection.

## Grille de sélection (critères, sans note chiffrée)

| Critère | Question à poser |
|---|---|
| Localisation et transferts | où sont traitées et stockées les données ? un transfert hors Union européenne est-il prévu et encadré ? |
| Non-réutilisation | les données de Verdalia sont-elles exclues de l'entraînement et de l'amélioration du service ? |
| Sécurité | chiffrement, gestion des accès, journalisation, certifications fournies ? |
| Sous-traitance | liste des sous-traitants ultérieurs, information préalable en cas de changement ? |
| Incidents | délai de notification d'une violation de données ? |
| Audit | droit d'audit ou rapports tiers ? |
| Portabilité | formats ouverts, export complet des données et des configurations ? |
| Interopérabilité | interfaces standards permettant de remplacer le fournisseur ? |
| Viabilité | stabilité de l'offre, conditions tarifaires prévisibles ? |

## Clauses contractuelles à exiger

Contrat de sous-traitance au sens de l'article 28 du RGPD (instructions documentées, confidentialité, sécurité, assistance pour les droits des personnes, suppression ou restitution en fin de contrat, audit). Clause de non-réutilisation. Clause de réversibilité. Niveaux de service. Les clauses définitives doivent être revues par le DPO et le service juridique.

## Plan de réversibilité

1. Découplage : l'API de Verdalia est la seule interface vers le modèle ; un changement de fournisseur n'affecte pas les sources.
2. Données : seules des données minimales transitent ; les prompts et configurations sont conservés par Verdalia dans le dépôt.
3. Portabilité : export des données et paramètres dans des formats ouverts avant la fin du contrat.
4. Test : un test de remplacement par un second fournisseur (ou un modèle alternatif) est prévu à la fin de la phase 4 pour vérifier que l'API reste compatible.
5. Sortie : suppression certifiée des données chez l'ancien fournisseur, avec preuve écrite.

## Responsables

Choix : Sponsor (décision), Responsable plateforme data et DSI (analyse), DPO (garanties). Suivi du contrat : DSI.
