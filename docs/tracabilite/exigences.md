# Traçabilité des dix exigences

Les dix exigences sont celles de l'énoncé. Pour chacune : besoin reformulé, solution, mécanisme, justification, responsable, critère de vérification, chapitre. Responsable de la matrice : travail collectif.

## EX-01 — Vue unique et fiable du client

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | pour chaque client, une seule fiche cohérente quel que soit le canal (magasin, web, CRM) |
| Solution retenue | référentiel MDM avec identifiant client unique |
| Mécanisme | normalisation, règles déterministes, score de similarité, revue humaine, fusion réversible, synchronisation contrôlée vers les sources |
| Justification | une déduplication dans le Warehouse seul ne corrige pas les sources ; le MDM crée un point de décision traçable |
| Responsable | Data Owner Client et fidélité ; Data Steward Client pour la revue |
| Critère de vérification | doublons résiduels estimés inférieurs à 1 % à 6 mois (hypothèse) ; 0 fusion sans journal ; taux de fusions annulées suivi |
| Chapitres | [02](../02-cartographie-donnees.md), [04](../04-architecture-cible.md), [MDM](../donnees/mdm-client.md) |

## EX-02 — Définitions communes des KPI

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | un même indicateur doit donner le même chiffre dans tous les services |
| Solution retenue | glossaire commun et couche métier avec KPI certifiés |
| Mécanisme | fiche de définition versionnée, calcul unique, validation écrite de la direction financière, distinction provisoire et validé |
| Justification | les écarts actuels viennent de règles de calcul locales |
| Responsable | Data Owner Finance |
| Critère de vérification | CA, marge et panier moyen publiés uniquement s'ils sont certifiés ; écart caisses et Warehouse sous le seuil ; aucun KPI sans fiche |
| Chapitres | [04](../04-architecture-cible.md), [KPI](../architecture/kpi-et-lineage.md) |

## EX-03 — Responsable pour chaque jeu de données

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | chaque jeu de données a un propriétaire identifié |
| Solution retenue | Data Owners par domaine et Data Stewards, catalogue |
| Mécanisme | désignation écrite, champ obligatoire dans le catalogue, jeu orphelin non publié, comité mensuel |
| Justification | sans propriétaire, personne ne corrige ni ne décide des accès |
| Responsable | Sponsor (nomination), comité de gouvernance (suivi) |
| Critère de vérification | 100 % des jeux publiés avec Owner et Steward ; revue trimestrielle |
| Chapitres | [05](../05-gouvernance-raci.md), [rôles](../gouvernance/roles-et-definitions.md) |

## EX-04 — Gestion RGPD des données clients

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | traiter les données clients dans le respect du RGPD |
| Solution retenue | finalités et bases légales distinctes, registre, durées qualifiées, consentements gérés, droits des personnes outillés par le MDM, AIPD |
| Mécanisme | registre des traitements, filtre de consentement, procédure d'effacement par identifiant unique, politique de conservation, procédure de violation |
| Justification | les finalités diffèrent ; un consentement unique pour tout serait inexact et inutile |
| Responsable | DPO (contrôle) ; Data Owner Client (exécution) ; Sponsor (responsable de traitement) |
| Critère de vérification | registre complet ; 100 % des clients avec statut de consentement ; demandes de droits traitées dans le délai ; durées appliquées |
| Chapitres | [03](../03-cycle-vie-donnees.md), [06](../06-rgpd-ia-responsable.md), [registre](../rgpd/registre-traitements.md) |

## EX-05 — Traçabilité de chaque indicateur

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | pouvoir expliquer d'où vient chaque chiffre affiché |
| Solution retenue | lineage de bout en bout et métadonnées |
| Mécanisme | identifiants de lot, journal d'ingestion, scripts versionnés, version de règle affichée avec le KPI |
| Justification | sans traçabilité, un écart ne peut pas être expliqué ni corrigé |
| Responsable | Responsable de la plateforme data |
| Critère de vérification | démonstration complète pour le CA d'un magasin et d'un jour ; indicateur « certifié » et date visibles |
| Chapitres | [04](../04-architecture-cible.md), [KPI et lineage](../architecture/kpi-et-lineage.md) |

## EX-06 — Droits d'accès par profil

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | chacun voit uniquement ce dont il a besoin |
| Solution retenue | accès par rôle, périmètre magasin et domaine, classification |
| Mécanisme | moindre privilège, approbation du Data Owner, masquage des colonnes, revue trimestrielle, journalisation |
| Justification | limite les fuites et les usages hors finalité |
| Responsable | DSI et RSSI (mise en œuvre) ; Data Owners (autorisation) |
| Critère de vérification | matrice d'accès appliquée ; revue trimestrielle signée ; 0 compte non justifié |
| Chapitres | [05](../05-gouvernance-raci.md), [politique d'accès](../gouvernance/politique-acces.md) |

## EX-07 — Qualité minimale des données

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | un niveau minimal de fiabilité garanti avant usage |
| Solution retenue | indicateurs, contrôles à l'ingestion, quarantaine, circuit de correction |
| Mécanisme | six dimensions de qualité avec seuils (hypothèses), alertes, délais de correction, traçabilité des corrections |
| Justification | les données erronées contaminent les KPI et le MDM |
| Responsable | Data Stewards ; plateforme data pour l'outillage |
| Critère de vérification | indicateurs suivis chaque mois ; lots non conformes jamais chargés dans le Warehouse |
| Chapitres | [02](../02-cartographie-donnees.md), [qualité](../donnees/qualite-donnees.md) |

## EX-08 — Encadrement des données de l'assistant IA

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | l'assistant n'accède qu'aux données nécessaires et autorisées |
| Solution retenue | API intermédiaire, droits, minimisation, historique client non transmis au modèle, vérification humaine |
| Mécanisme | authentification, autorisation par rôle, filtre d'entrée et de sortie, requêtes sans identité client, journalisation, tests d'injection |
| Justification | limite l'exposition vers un prestataire externe et la dépendance |
| Responsable | DPO et Responsable plateforme data ; Data Owner pour la validation des données |
| Critère de vérification | aucune requête au modèle contenant d'identité client dans l'échantillon audité ; tests d'injection réussis ; journal disponible |
| Chapitres | [04](../04-architecture-cible.md), [06](../06-rgpd-ia-responsable.md), [API IA](../architecture/assistant-ia-api.md) |

## EX-09 — Fournisseur externe et réversibilité

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | pouvoir contrôler puis quitter le fournisseur sans perdre ses données |
| Solution retenue | grille de sélection, contrat avec clauses, découplage par l'API |
| Mécanisme | contrat article 28, non-réutilisation, portabilité en formats ouverts, test de remplacement, suppression certifiée |
| Justification | évite l'enfermement et protège les données |
| Responsable | Sponsor (décision), DSI (contrat), DPO (garanties) |
| Critère de vérification | contrat signé avec clauses ; test de remplacement réalisé en phase 4 |
| Chapitres | [04](../04-architecture-cible.md), [fournisseur](../architecture/choix-fournisseur.md) |

## EX-10 — Trajectoire avec jalons à 6 et 12 mois

| Rubrique | Contenu |
|---|---|
| Besoin reformulé | un plan réaliste avec des étapes de contrôle à 6 et 12 mois |
| Solution retenue | quatre phases, quatre jalons, conditions de passage |
| Mécanisme | revue de fin de phase, critères d'acceptation, risques suivis |
| Justification | une progression par étapes sécurise l'IA en s'appuyant sur un socle fiable |
| Responsable | Comité de gouvernance ; Sponsor pour les décisions |
| Critère de vérification | J2 (mois 6) et J4 (mois 12) franchis selon critères écrits |
| Chapitres | [08](../08-trajectoire.md), [07](../07-risques-mesures.md) |
