# Faits, hypothèses, choix et points à valider

Ce document sépare les cinq types d'information du dossier.

## 1. Faits fournis par l'énoncé

14 magasins ; 520 salariés ; 190 M€ de chiffre d'affaires ; environ 600 000 clients fidélisés ; 650 000 profils CRM ; 18 000 références ; 2 millions de mouvements de stock par an ; 6 millions de tickets par an ; 400 000 commandes e-commerce par an ; cinq sources (ERP, caisses, e-commerce, CRM, Excel) ; problèmes listés (doublons, KPI différents, exports par e-mail, responsabilités, durées inconnues, traçabilité, stratégie) ; ambitions de la direction ; dix exigences EX-01 à EX-10 ; assistant IA testé dans deux magasins ; milestones à 6 et 12 mois.

## 2. Hypothèses du groupe

| N° | Hypothèse | Où | À valider avec |
|---|---|---|---|
| H1 | seuils de qualité (par exemple doublons inférieurs à 1 %, écart caisses inférieur à 0,1 %, 98 % de chargements avant 7 h) | qualité des données | DSI, DAF |
| H2 | fréquences d'ingestion (caisses en fin de journée, e-commerce horaire…) | cartographie | DSI |
| H3 | équipe data de 3 personnes et charges en jours-personne | trajectoire | DSI, direction |
| H4 | seuils haut et bas du rapprochement client à calibrer | MDM | données réelles |
| H5 | durées internes (zone brute 90 jours, quarantaine 30 jours, journaux 6 mois) | RGPD | DPO |
| H6 | notes et poids de la comparaison d'architectures | ADR-001 | relecture critique |
| H7 | désignation des Data Owners par fonction | gouvernance | direction |
| H8 | date de démarrage fictive du Gantt (janvier 2027) | trajectoire | calendrier réel |
| H9 | définitions provisoires des KPI | KPI | DAF |
| H10 | délais de traitement des anomalies (1, 5 jours ouvrés) | qualité | Data Owners |

## 3. Choix d'architecture proposés

Warehouse centralisé avec MDM (ADR-001) ; API intermédiaire pour l'IA (ADR-002) ; Warehouse pseudonymisé (ADR-003) ; ELT par défaut ; modèle en étoile ; zone brute à durée limitée ; stock lu à l'ERP en temps réel pour l'IA.

## 4. Informations issues de sources externes

Voir [BIBLIOGRAPHIE](BIBLIOGRAPHIE.md) : CNIL (durées de 3 ans, AIPD), article L123-22 du code de commerce (10 ans), AI Act et sa modification (sources secondaires).

## 5. Éléments encore à faire valider

| N° | Point | Responsable de la validation |
|---|---|---|
| V1 | les neuf parties officielles du dossier : nous avons mappé les chapitres 01 à 09 sur la liste du brief ; à confronter au cahier des charges | groupe, enseignant |
| V2 | base légale de la prospection auprès des clients (exception L.34-5) | DPO |
| V3 | définition du « dernier contact » pour la durée de 3 ans | DPO |
| V4 | version en vigueur du délai fiscal de conservation | DPO, comptable |
| V5 | qualification AI Act et calendrier modifié | juriste |
| V6 | durée de conservation des journaux et des preuves de consentement | DPO, RSSI |
| V7 | transferts hors UE selon le prestataire retenu | DPO |
| V8 | explication de l'écart 650 000 profils CRM et 600 000 clients fidélisés | Data Steward Client |
| V9 | consultation éventuelle des représentants du personnel pour l'assistant IA | direction, RH |

## Questions pour l'enseignant

1. Peut-on confirmer la liste des neuf parties officielles du dossier ?
2. Un budget indicatif en jours-personne suffit-il, ou attendez-vous des fourchettes en euros ?
3. Quel niveau de détail est attendu sur le choix d'un produit précis ?
