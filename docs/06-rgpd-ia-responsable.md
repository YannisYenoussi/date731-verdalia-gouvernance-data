# 06 — RGPD et IA responsable

Responsable : Personne 3. Exigences : EX-04 et EX-08. Cette analyse est un travail d'étudiants : les points juridiques sont à faire valider par un DPO ou un juriste avant toute application réelle. Le statut de vérification de chaque source est indiqué dans [BIBLIOGRAPHIE](sources/BIBLIOGRAPHIE.md). Documents détaillés : [registre des traitements](rgpd/registre-traitements.md), [durées de conservation](rgpd/durees-conservation.md), [AIPD](rgpd/aipd-analyse.md), [IA et AI Act](rgpd/ia-ai-act-risques.md).

## 6.1 Finalités et bases légales

Le consentement marketing n'est pas nécessaire pour tous les traitements. La base légale dépend de chaque finalité (article 6 du RGPD).

| Finalité | Base légale proposée | Remarques |
|---|---|---|
| Gestion des ventes et commandes (magasin, e-commerce) | exécution du contrat (art. 6.1.b) | données strictement nécessaires |
| Facturation et comptabilité | obligation légale (art. 6.1.c) | durée liée aux textes comptables |
| Gestion du programme de fidélité (points, avantages) | exécution du contrat d'adhésion (art. 6.1.b) | règlement du programme à rédiger |
| Qualité des données et déduplication clients (MDM) | intérêt légitime (art. 6.1.f) et principe d'exactitude (art. 5.1.d) | mise en balance à documenter ; information des clients |
| Pilotage et statistiques de ventes | intérêt légitime ; données agrégées ou pseudonymisées | pas de décision individuelle |
| Prospection par e-mail ou SMS auprès de clients pour des produits analogues | règles de la prospection électronique (code des postes et des communications électroniques, article L.34-5) : exception au consentement sous conditions, droit d'opposition à la collecte et à chaque message | à confirmer par le DPO |
| Prospection électronique auprès de prospects (particuliers) | consentement (art. 6.1.a et art. 7) | preuve du consentement conservée |
| Prospection postale | intérêt légitime avec droit d'opposition | à confirmer par le DPO |
| Segmentation et personnalisation marketing | consentement ou intérêt légitime selon la nature ; prudence si profilage fin | AIPD recommandée, voir 6.7 |
| Assistant IA : conseil produit sans donnée client | intérêt légitime de Verdalia pour l'activité de conseil ; données de salariés limitées aux journaux | information des salariés, consultation des représentants du personnel si requis |
| Assistant IA : usage de l'historique client | à justifier au cas par cas ; non transmis au modèle par défaut | exception formelle avec avis du DPO |

## 6.2 Principes à appliquer

Minimisation : seules les données utiles à chaque finalité (Warehouse pseudonymisé, requêtes IA sans identité). Exactitude : MDM et contrôles qualité. Limitation de la conservation : durées ci-dessous. Intégrité et confidentialité : droits d'accès, chiffrement, journalisation. Protection dès la conception (art. 25).

## 6.3 Durées de conservation

Résumé ; détail et justifications dans [durees-conservation](rgpd/durees-conservation.md). Trois statuts sont distingués : obligation légale, recommandation d'une autorité, proposition interne du groupe. Aucune durée de conservation n'est présentée comme obligation si elle ne l'est pas.

| Donnée | Durée proposée | Statut | Validation demandée au DPO |
|---|---|---|---|
| Documents comptables et pièces justificatives | 10 ans | obligation légale (article L123-22 du code de commerce) | confirmer le périmètre exact des pièces concernées |
| Clients : données de gestion commerciale et de prospection | durée de la relation puis 3 ans maximum après le dernier contact | recommandation CNIL (référentiel gestion commerciale, non contraignant) | définir ce qui compte comme dernier contact ; archivage intermédiaire éventuel |
| Prospects | 3 ans après la collecte ou le dernier contact | recommandation CNIL | idem |
| Zone brute et quarantaine | 90 jours et 30 jours | proposition interne | valider la proportionnalité |
| Journaux techniques et journaux IA | à fixer (proposition : 6 mois) | proposition interne | comparer avec les recommandations CNIL sur la journalisation, à vérifier |

## 6.4 Consentement marketing

Le consentement est libre, spécifique, éclairé, univoque, par canal et finalité, avec retrait aussi simple que l'octroi. Il est stocké dans le CRM et diffusé via le MDM. Toute activation marketing applique un filtre de consentement ou d'exception avant envoi. Une opposition prévaut sur tout.

## 6.5 Droits des personnes

| Droit | Mécanisme | Délai cible |
|---|---|---|
| Accès | extraction des données via l'identifiant client unique dans les systèmes | délai légal d'un mois, prolongeable dans les cas prévus (à vérifier avec le DPO) |
| Rectification | correction dans la source puis synchronisation depuis le MDM | même délai |
| Opposition | mise à jour immédiate du statut de prospection, propagée à tous les canaux | immédiate pour la prospection |
| Effacement | procédure décrite au chapitre 03, avec exceptions pour obligations légales | même délai |

Le MDM facilite ces droits : une demande se traite sur un identifiant unique au lieu de chercher dans cinq systèmes.

## 6.6 Sécurité, violations et sous-traitance

Sécurité : chiffrement, accès par rôle, journalisation, tests d'intrusion avant le pilote, sauvegardes. Violation : procédure d'incident (RACI), évaluation par le DPO, notification à la CNIL dans les 72 heures lorsque requis et information des personnes en cas de risque élevé (articles 33 et 34 du RGPD). Registre des violations. Sous-traitants : contrat article 28, liste tenue à jour, vérification des garanties. Transferts hors Union européenne : à éviter par défaut ; sinon garanties au titre du chapitre V du RGPD, à faire valider.

## 6.7 AIPD

Analyse détaillée dans [aipd-analyse](rgpd/aipd-analyse.md). Conclusion préliminaire : une analyse d'impact est recommandée avant la mise en production du MDM et de la vision client unique, car plusieurs critères de risque se cumulent (croisement de sources, grand nombre de personnes, évolution technologique). Pour l'assistant IA, elle est requise si l'historique client est utilisé ; sans donnée client, une évaluation allégée est suffisante. Décision finale : DPO.

## 6.8 Assistant IA responsable

| Risque | Mesure |
|---|---|
| Hallucination (réponse inventée mais plausible) | réponses fondées sur des sources validées citées, vérification humaine, retour d'erreurs par les conseillers |
| Biais | pas d'usage de l'assistant pour évaluer ou classer des personnes ; revue d'un échantillon de réponses |
| Exposition de données | API intermédiaire, requêtes sans identité client, filtrage de sortie, journalisation |
| Accès excessifs | authentification, rôles, moindre privilège |
| Injection de prompt | séparation données et instructions, pas d'outils d'écriture, tests |
| Dépendance au fournisseur | API de découplage, contrat de réversibilité, test de remplacement |
| Usage détourné | charte d'usage pour les conseillers, formation, sanctions prévues par le règlement intérieur |

## 6.9 AI Act : analyse préliminaire

Cette analyse ne conclut pas. Voir [ia-ai-act-risques](rgpd/ia-ai-act-risques.md). En l'état du cas d'usage (aide au conseil produit, pas de décision sur des personnes), un classement en système à haut risque n'apparaît pas évident, mais la vérification des cas listés à l'annexe III, la qualification du rôle de Verdalia (déployeur) et les obligations de transparence et de formation restent à confirmer avec un juriste, d'autant que le calendrier d'application a été modifié selon des sources secondaires que nous n'avons pas pu recouper sur EUR-Lex.

Précédent : [05](05-gouvernance-raci.md). Suite : [07 Risques](07-risques-mesures.md).
