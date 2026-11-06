# Politique de classification des données

Responsable : Personne 3. Complément : [classification des données critiques](../donnees/classification-donnees-critiques.md).

## Niveaux

| Niveau | Définition | Exemples | Règles d'accès | Stockage et protection | Partage |
|---|---|---|---|---|---|
| Public | information destinée à être connue de tous | catalogue publié, horaires des magasins | libre | pas d'exigence particulière | libre, via canaux officiels |
| Interne | usage interne, faible impact en cas de fuite | stock par magasin, procédures | tout salarié concerné | espace interne authentifié | interne uniquement |
| Confidentiel | impact commercial ou financier en cas de fuite | prix d'achat, marge, KPI financiers, contrats | profils nommés, accord du Data Owner | accès restreint, journalisé | interdit hors Verdalia sans accord ; pas d'e-mail de fichiers bruts |
| Personnel ou sensible | données se rapportant à une personne identifiée ou identifiable ; catégories particulières (article 9 du RGPD) si elles existent | identité, coordonnées, historique d'achats nominatif, consentements | moindre privilège, finalité déclarée, validation du Data Owner Client, DPO informé | chiffrement, zone restreinte, journalisation des accès, pseudonymisation dès que possible | interdit par e-mail et messagerie ; export tracé, limité et à durée limitée ; sous-traitant uniquement avec contrat article 28 |

Catégories particulières : Verdalia n'a pas vocation à collecter des données de santé, d'opinion, d'origine ou autres catégories de l'article 9. Elles sont considérées comme non collectées par conception ; les champs libres sont contrôlés pour éviter leur présence involontaire. Si un besoin apparaissait, il faudrait un traitement spécifique avec analyse juridique préalable.

## Règles générales

1. Le niveau est défini par le Data Owner à la création du jeu de données et enregistré dans le catalogue.
2. Un ensemble prend le niveau de sa donnée la plus sensible.
3. Une donnée déclassée (par exemple après anonymisation réelle) nécessite une validation du DPO.
4. Les environnements de test n'utilisent pas de données personnelles réelles, sauf dérogation tracée.
5. Les exports de niveau Personnel sont interdits par e-mail ; l'alternative est le libre-service BI ou un dépôt sécurisé avec expiration.
6. Étiquetage : chaque table et chaque tableau de bord porte son niveau.
