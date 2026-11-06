# Assistant IA interne : accès par API

Responsables : Personne 2 (architecture) et Personne 3 (conformité). Exigence : EX-08. Analyse des risques : [rgpd/ia-ai-act-risques](../rgpd/ia-ai-act-risques.md).

## Cas d'usage retenu pour le pilote

Un conseiller en magasin pose une question de conseil produit ou de disponibilité. L'assistant propose une réponse fondée sur les fiches produits validées et le stock récent. Le pilote est limité à deux magasins. L'assistant ne prend aucune décision concernant une personne.

## Pourquoi une API intermédiaire

L'API est le seul point d'accès aux données pour l'assistant. Elle applique les droits, minimise les données, filtre, journalise et permet de changer de fournisseur de modèle sans toucher aux sources.

## Chaîne de contrôle

| Étape | Contrôle | Responsable |
|---|---|---|
| Authentification | SSO de l'entreprise et authentification forte ; pas de compte partagé | DSI |
| Autorisation | rôle, magasin, contexte ; moindre privilège | Data Owner via la plateforme |
| Contrôle d'entrée | détection de tentatives d'injection, limite de taille, retrait d'identifiants personnels | plateforme data |
| Sources de données | fiches produits validées (couche métier) ; stock récent via l'ERP en lecture seule | Data Owner Produits |
| Historique client | affiché au conseiller séparément, limité (par exemple derniers achats pertinents), non transmis au modèle sauf exception justifiée par écrit, avec avis du DPO | Data Owner Client, DPO |
| Appel du modèle | requête minimale, sans identité client | plateforme data |
| Contrôle de sortie | références aux sources, filtrage de données interdites, mention que la réponse est générée par IA | plateforme data |
| Vérification humaine | le conseiller valide avant d'agir ou de répondre au client | magasin |
| Journalisation | requête, rôle, sources utilisées, horodatage ; pas de conservation inutile du contenu | RSSI |

## Protection contre l'injection de prompt

Les contenus récupérés (descriptions produits, commentaires) sont traités comme des données, jamais comme des instructions. Le modèle n'a pas d'outils d'écriture. Les sorties ne déclenchent aucune action automatique. Des tests de résistance sont prévus avant le pilote.

## Exigences contractuelles envers le prestataire de modèle

Voir [choix-fournisseur](choix-fournisseur.md) : non-réutilisation des données pour l'entraînement, confidentialité, localisation et transferts, sous-traitants, sécurité, notification d'incident, audit, réversibilité.

## Pourquoi ne pas entraîner notre propre modèle

Coût, compétences, qualité des données et volumes disponibles : ce n'est pas proportionné. La récupération de passages validés (approche de type RAG : le modèle reçoit des extraits fiables au moment de la question) apporte l'actualité sans réentraîner. L'option sera réexaminée si le pilote montre un besoin non couvert.

## Indicateurs d'évaluation du pilote

Taux de réponses jugées correctes par les conseillers sur un échantillon, taux de réponses sans source, nombre de tentatives d'injection détectées, incidents de confidentialité (objectif zéro), satisfaction des conseillers. Les seuils d'acceptation sont à fixer en phase 3 par le comité ; aucun résultat n'est annoncé ici.
