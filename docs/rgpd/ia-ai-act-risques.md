# IA responsable et AI Act : analyse préliminaire

Responsable : Personne 3. Ce document ne conclut pas sur la qualification juridique. Il identifie les questions à trancher.

## Cas d'usage

Assistant interne de conseil produit et de disponibilité en magasin, testé dans deux magasins, utilisé par des conseillers, sans décision automatique concernant des personnes.

## Éléments de cadrage (statut de vérification)

Le règlement (UE) 2024/1689 (AI Act) est entré en vigueur le 1er août 2024 et s'applique par paliers. Des sources secondaires consultées le 6 novembre 2026 indiquent qu'il a été modifié par le règlement (UE) 2026/1744 (dit Digital Omnibus sur l'IA) qui déplace certaines dates, notamment celles des systèmes à haut risque, et que les obligations de transparence de l'article 50 s'appliquent depuis août 2026 avec une période de grâce pour le marquage de certains contenus. Nous n'avons pas pu relire le texte sur EUR-Lex : toute date doit être vérifiée sur la source officielle avant d'être utilisée.

## Questions de qualification

| Question | Appréciation préliminaire | Vérification à faire |
|---|---|---|
| Rôle de Verdalia | déployeur du système ; le prestataire est fournisseur du modèle | contrat et statut exact du fournisseur |
| Pratique interdite ? | non apparente | relire la liste de l'article 5 |
| Cas listés à l'annexe III (haut risque) | non apparent : l'assistant ne sert ni à l'emploi, ni au crédit, ni à l'accès à des services essentiels | relire l'annexe III avec un juriste, surtout si l'assistant évaluait des salariés ou des clients |
| Obligations de transparence (article 50) | l'assistant interagit directement avec des personnes (les conseillers) : informer qu'ils échangent avec une IA, sauf si c'est évident | lignes directrices de la Commission sur l'article 50 |
| Maîtrise de l'IA (article 4) | formation des conseillers et du personnel concerné | contenu et traçabilité de la formation |
| Modèle à usage général | relève du fournisseur | garanties contractuelles |

Conclusion préliminaire : niveau de risque probablement limité, sous réserve de ces vérifications et du maintien du périmètre (aide au conseil, humain décideur).

## Conditions qui changeraient la qualification

Usage de l'assistant pour noter ou classer des clients ou des salariés, décisions automatiques de remise ou d'accès, suivi de la performance des conseillers, extension à des données de catégories particulières. Chacune déclenche une nouvelle analyse (AI Act et AIPD).

## Registre des risques IA

| Risque | Probabilité (qualitative) | Impact | Mesures | Indicateur |
|---|---|---|---|---|
| Hallucination : fausse information de stock ou de compatibilité produit | moyenne | moyen | sources citées, stock lu à l'ERP, vérification humaine | taux de réponses erronées relevées dans l'échantillon |
| Biais : conseils orientés vers certaines gammes ou clientèles | faible à moyenne | moyen | revue périodique, absence de données démographiques dans les requêtes | écarts observés |
| Exposition de données personnelles ou confidentielles | faible si les mesures tiennent | élevé | requêtes sans identité, filtrage, contrat | incidents |
| Accès excessifs | moyenne | élevé | rôles, revue trimestrielle | comptes non justifiés |
| Injection de prompt | moyenne | moyen à élevé | séparation données et instructions, pas d'outil d'écriture, tests | tentatives détectées |
| Dépendance au fournisseur | moyenne | moyen | API de découplage, réversibilité, test de remplacement | résultat du test |

Les niveaux de probabilité et d'impact sont des appréciations du groupe, non chiffrées.
