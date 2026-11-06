# ADR-002 — L'assistant IA accède aux données uniquement par une API intermédiaire

Statut : proposé. Date : 6 novembre 2026. Rédaction principale : Personne 3, relecture Personne 2.

Contexte : un assistant IA interne sera testé dans deux magasins. Les données clients et les données financières ne doivent pas être exposées à un modèle externe sans contrôle.

Problème : comment fournir au modèle un contexte utile sans accès direct ni illimité au Warehouse ou au CRM ?

Options : (1) accès direct du modèle aux bases ; (2) export de données vers le prestataire ; (3) API intermédiaire contrôlée.

Décision : option 3. L'API authentifie, autorise, minimise, filtre, journalise. Le modèle reçoit des fiches produits validées et un stock récent lu à l'ERP. L'historique client limité n'est pas transmis au modèle sauf exception formelle.

Conséquences positives : surface d'exposition réduite, fournisseur remplaçable, preuves de contrôle.
Limites : latence et développement d'une couche supplémentaire ; réponses moins personnalisées.
Compromis : moins de personnalisation contre plus de confidentialité.
Réexamen : si le pilote montre qu'un usage de l'historique client est indispensable, une analyse complémentaire (AIPD, base légale, information des clients) est menée avant toute extension.
