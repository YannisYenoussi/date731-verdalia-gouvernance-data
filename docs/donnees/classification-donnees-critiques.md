# Classification des données critiques

Responsable : Personne 1. La politique de classification (niveaux et règles) est dans [gouvernance/politique-classification.md](../gouvernance/politique-classification.md).

| Donnée | Famille(s) | Niveau | Personnelle | Source | Data Owner proposé | Justification du niveau |
|---|---|---|---|---|---|---|
| Identité client (nom, prénom, date de naissance) | référence, sensible | Personnel | oui | CRM, e-commerce | Marketing et relation client | identifie directement une personne |
| Coordonnées (e-mail, téléphone, adresse) | référence, sensible | Personnel | oui | CRM, e-commerce | Marketing et relation client | permet de contacter la personne |
| Identifiant client unique (MDM) | référence | Personnel (pseudonyme) | oui, indirectement | MDM | Marketing et relation client | reste rattachable à une personne via le MDM |
| Consentements et oppositions | opérationnelle, sensible | Personnel | oui | CRM, e-commerce | Marketing et relation client | preuve juridique à conserver |
| Historique d'achats nominatif | opérationnelle, sensible | Personnel | oui | caisses, e-commerce | Ventes et Marketing | révèle des habitudes de consommation |
| Points de fidélité | opérationnelle | Personnel | oui | CRM | Marketing et relation client | valeur financière pour le client |
| Ticket de caisse sans identifiant client | opérationnelle | Confidentiel | non | caisses | Ventes et exploitation | donnée commerciale |
| Commande e-commerce | opérationnelle | Personnel | oui | e-commerce | E-commerce | contient adresse de livraison |
| Catalogue et prix de vente | référence | Interne (public une fois publié) | non | ERP | Produits et stocks | information déjà exposée aux clients |
| Prix d'achat et marge | stratégique, sensible | Confidentiel | non | ERP, Finance | Finance | information concurrentielle |
| Stock par magasin | opérationnelle | Interne | non | ERP | Produits et stocks | usage interne |
| KPI financiers certifiés (CA, marge, panier) | stratégique | Confidentiel | non | couche métier | Finance | pilotage de l'entreprise |
| Journaux de requêtes de l'assistant IA | opérationnelle | Personnel (conseiller) | oui | API IA | Responsable plateforme data | identifient des salariés |
| Fichiers Excel d'export | variable | niveau de la donnée la plus sensible qu'ils contiennent | variable | divers | propriétaire déclaré | règle du niveau le plus élevé |

Règle de précédence : un fichier ou une table prend le niveau de sa donnée la plus sensible. Les données de catégories particulières (article 9 du RGPD) ne sont pas collectées par conception ; tout champ libre est considéré à risque et contrôlé.
