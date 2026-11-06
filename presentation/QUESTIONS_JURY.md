# Questions possibles du jury

Vingt-six questions avec réponses argumentées. Orateur conseillé entre parenthèses (P1, P2, P3). Reformulez avec vos mots et restez honnêtes sur les hypothèses.

## Architecture

1. Pourquoi ne pas choisir un Data Lake ? (P2)
Un lake est utile pour des volumes massifs ou des données non structurées. Verdalia a surtout des données transactionnelles structurées et modestes en volume. Sans catalogue ni règles de qualité, un lake devient un dépôt illisible, ce qui reproduirait le problème actuel de chiffres contradictoires. Dans notre grille, il obtient entre 2,45 et 2,75 sur 5, selon la pondération.

2. Pourquoi utiliser un MDM ? (P1 ou P2)
Parce que dédupliquer uniquement dans le Warehouse corrige les rapports mais pas les sources : les doublons reviennent. Le MDM crée un identifiant unique, un point de décision traçable, des fusions réversibles, et facilite les droits des personnes (une demande, un identifiant).

3. Pourquoi centraliser les données ? (P2)
Pour avoir un calcul unique et un contrôle d'accès unique. La centralisation a un coût : un point de défaillance et un risque de propagation d'une erreur de règle. Nous le réduisons par le versionnement des règles, la recette et les alertes. À 14 magasins, la décentralisation d'un Data Mesh multiplierait les définitions concurrentes.

4. Quelle différence entre ETL et ELT ? (P2)
ETL transforme les données avant de les charger ; ELT charge d'abord la donnée brute puis transforme dans l'entrepôt. Nous préférons l'ELT par défaut (copie brute pour l'audit, rechargement facile) et gardons l'ETL pour masquer des données personnelles avant tout chargement.

5. Comment fonctionne un Data Warehouse ? (P2)
C'est une base structurée en étoile : des faits (lignes de vente, mouvements de stock) reliés à des dimensions (client, produit, magasin, date). Les données sont chargées par lots, historisées si nécessaire, et servent à analyser, pas à exécuter les opérations quotidiennes.

6. Pourquoi votre note de 4,20 est-elle fiable ? (P2)
Elle ne l'est qu'avec prudence : ce sont des appréciations qualitatives. C'est pourquoi nous avons testé quatre pondérations. Le Warehouse reste premier mais l'écart tombe à 0,15 point avec l'hybride si l'évolutivité domine. Nous le déclarons comme limite.

7. Comment faire évoluer le système avec 28 magasins ? (P2)
Le modèle en étoile ajoute des magasins comme des lignes de dimension. La charge double environ, ce qui reste modeste. Points à revoir : la fenêtre de chargement, la file de revue du MDM, le nombre de Data Stewards. L'ADR-001 prévoit un réexamen vers le Lakehouse si des données non structurées apparaissent.

8. Différence entre données analytiques et opérationnelles ? (P2)
Analytiques : copies consolidées de la veille dans le Warehouse, pour analyser. Opérationnelles : état courant d'un système source (le stock maintenant). Pour l'IA, le stock est lu à l'ERP en temps réel, car une donnée de la veille serait trompeuse.

## Données et qualité

9. Comment résoudre les doublons clients ? (P1)
Normalisation, règles certaines (même carte ou e-mail vérifié), score de similarité, revue humaine dans la zone intermédiaire. Nous restons prudents : un faux rapprochement est pire qu'un doublon. Les seuils sont à calibrer sur des données réelles.

10. Comment garantir la cohérence du chiffre d'affaires ? (P2)
Une définition validée par la direction financière, un seul calcul dans la couche métier, un contrôle quotidien entre les caisses et le Warehouse (seuil hypothétique de 0,1 %), et un lineage permettant de retracer tout chiffre.

11. D'où viennent vos seuils de qualité ? (P1)
Ce sont des hypothèses du groupe, pas des normes. Ils seront calibrés après une mesure initiale en phase 1. Nous les avons marqués comme tels dans le dossier.

12. Que se passe-t-il si un lot de ventes est incorrect ? (P1)
Il est détecté à l'ingestion, mis en quarantaine, jamais chargé dans le Warehouse. Le Data Steward qualifie sous 1 jour ouvré, la correction est faite à la source ou dans la règle, puis le lot est rechargé. Tout est tracé.

## RGPD

13. Comment respecter le droit à l'effacement ? (P3)
Identification de la personne via l'identifiant unique, effacement ou anonymisation dans le CRM, l'e-commerce et le MDM, rupture du lien nominatif dans le Warehouse, information des sous-traitants. Les pièces comptables à conserver par obligation légale sont maintenues, dissociées de l'identité quand c'est possible. Les sauvegardes expirent par rotation.

14. Un consentement est-il nécessaire pour tous les traitements ? (P3)
Non. Le contrat suffit pour gérer une commande ou le programme de fidélité, l'obligation légale pour la comptabilité. Le consentement concerne notamment la prospection électronique envers les prospects ; pour les clients, un régime particulier existe, à confirmer avec le DPO.

15. Les durées de conservation sont-elles toutes légales ? (P3)
Non. Nous distinguons : obligation légale (10 ans pour les documents comptables, article L123-22 du code de commerce), recommandation CNIL (3 ans pour clients et prospects, non contraignante), proposition interne (zone brute 90 jours, par exemple). Chacune doit être validée par le DPO.

16. Faut-il une AIPD ? (P3)
Notre analyse préliminaire la recommande pour le MDM et la vision client (croisement de cinq sources, plus de 600 000 personnes) et la rend nécessaire pour l'IA si l'historique client est utilisé. La décision revient au DPO.

17. Qui est responsable en cas de fuite de données ? (P3)
Juridiquement Verdalia, responsable de traitement, représentée par la direction. Opérationnellement, la DSI conduit la réponse, le DPO qualifie et prépare la notification à la CNIL dans les 72 heures quand elle est requise, et le sponsor décide.

## Accès et gouvernance

18. Comment empêcher un accès injustifié ? (P3)
Moindre privilège, rôles et périmètre magasin, approbation du Data Owner, authentification forte, masquage des colonnes sensibles, journalisation, revue trimestrielle, retrait automatique au départ, interdiction des exports par e-mail.

19. Quelle est la différence entre Data Owner, Data Steward et DPO ? (P3)
Le Data Owner décide des règles d'un domaine. Le Data Steward applique et corrige. Le DPO conseille et contrôle, sans décider des traitements. Le responsable de traitement est Verdalia.

## IA

20. Que se passe-t-il si l'IA se trompe ? (P3)
C'est un risque prévu : réponses fondées sur des sources citées, stock lu à l'ERP, vérification humaine avant toute action, retour d'erreurs des conseillers, périmètre limité à deux magasins, aucune décision automatique concernant une personne.

21. Comment changer de fournisseur IA ? (P2)
L'API de Verdalia est le seul lien avec le modèle ; les sources ne changent pas. Prompts et configurations sont conservés par Verdalia. Le contrat prévoit portabilité et suppression certifiée. Un test de remplacement est prévu en phase 4.

22. Pourquoi ne pas entraîner notre propre modèle ? (P2 ou P3)
Coût, compétences et volume de données disproportionnés. Fournir des extraits validés au moment de la question apporte l'actualité sans réentraîner. On le réexaminera si le pilote révèle un besoin non couvert.

23. L'AI Act classe-t-il votre assistant à haut risque ? (P3)
Notre analyse préliminaire n'identifie pas de cas de l'annexe III, puisque l'assistant aide au conseil produit sans décider sur des personnes, mais nous ne concluons pas. Il faut vérifier les textes et le calendrier sur EUR-Lex avec un juriste. Un usage de notation de clients ou de suivi des conseillers changerait l'analyse.

## Coûts, calendrier, limites

24. Quel est le budget ? (P2)
L'énoncé n'en donne pas et nous n'en inventons pas. Nous donnons une charge indicative d'environ 615 jours-personne, avec des hypothèses d'équipe explicites. Un chiffrage en euros demanderait des devis et le coût journalier interne.

25. Quels risques menacent le calendrier ? (P2)
La qualité des sources inférieure aux hypothèses, la faible disponibilité des métiers et le retard dans la désignation des rôles. Les réponses : mesure initiale en phase 1, sponsor actif, conditions de passage écrites. Un retard décale le pilote plutôt que de réduire les contrôles.

26. Quelle est la principale limite de votre proposition ? (tous)
Elle repose sur des hypothèses non encore mesurées (qualité réelle des sources, charges) et sur l'engagement des métiers. De plus, nous n'avons pu relire les textes juridiques que par extraits : tout point juridique doit être confirmé par le DPO.
