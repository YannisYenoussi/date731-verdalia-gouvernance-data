# ADR-003 — Pseudonymisation du Data Warehouse

Statut : proposé. Date : 6 novembre 2026. Rédaction principale : Personne 2, avis Personne 3.

Contexte : le Warehouse alimente de nombreux tableaux de bord ; la plupart des analyses n'ont pas besoin de l'identité des clients.

Problème : comment limiter l'exposition des données personnelles dans les usages analytiques ?

Options : (1) stocker l'identité complète dans le Warehouse ; (2) stocker un identifiant unique et des attributs d'analyse, l'identité restant dans le MDM ; (3) anonymiser toutes les données (impossible pour le marketing individualisé et les droits des personnes).

Décision : option 2. L'identité directe reste dans le MDM à accès restreint. Le Warehouse conserve l'identifiant client unique, une tranche d'âge, un code postal tronqué et des statuts.

Conséquences positives : moins de risque en cas de mauvais accès, application plus simple de l'effacement (rompre le lien dans le MDM).
Limites : les données restent personnelles au sens du RGPD (la ré-identification est possible) ; une activation marketing exige de repasser par le MDM avec filtre de consentement.
Compromis : un peu de complexité supplémentaire contre une meilleure protection.
Réexamen : si l'analyse AIPD ou le DPO exigent un niveau supérieur (agrégation obligatoire ou anonymisation) ou si le coût d'exploitation devient excessif.
