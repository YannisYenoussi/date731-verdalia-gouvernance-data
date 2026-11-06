# Analyse de la nécessité d'une AIPD

Responsable : Personne 3. L'analyse d'impact relative à la protection des données (article 35 du RGPD) est requise lorsqu'un traitement est susceptible d'engendrer un risque élevé pour les droits et libertés. La CNIL publie une liste de types de traitements pour lesquels elle est requise (quatorze types selon les sources consultées, délibération de 2018) ; nous n'avons consulté que des extraits.

Conclusion préliminaire : à confirmer par le DPO.

## Grille de critères

| Critère de risque | MDM et vision client unique | Segmentation marketing | Assistant IA sans donnée client | Assistant IA avec historique client |
|---|---|---|---|---|
| Croisement ou combinaison de jeux de données | oui (cinq sources) | oui | non | oui |
| Données à grande échelle | oui (plus de 600 000 personnes) | oui | non | oui |
| Évaluation, notation, profilage | non par défaut | possible | non | possible |
| Technologie nouvelle ou innovante | non | non | oui (IA générative) | oui |
| Personnes vulnérables ou catégories particulières | non prévu | non prévu | non | non prévu |
| Décision automatisée à effet significatif | non | non | non | non |
| Conclusion préliminaire | AIPD recommandée avant production | AIPD recommandée si profilage fin | analyse allégée et journal de décision | AIPD requise |

Raisonnement : lorsque plusieurs critères se cumulent, la pratique recommande de réaliser une AIPD. Ce n'est pas une règle mécanique ; le DPO apprécie.

## Contenu minimal à produire

Description des traitements et des finalités, nécessité et proportionnalité, risques pour les personnes (accès illégitime, modification non désirée, disparition de données), mesures prévues, avis du DPO, consultation éventuelle de la CNIL si un risque élevé subsiste.

## Calendrier

Lancement en phase 3 (mois 7), avant l'ouverture du pilote IA ; l'AIPD du MDM est préparée dès la phase 2 pour ne pas bloquer le jalon de mise en production.
