# Modèle Azure → CMDB

## Identité
Favoriser les IDs natifs Azure stables (resource IDs) quand le connecteur/IRE les exploite.

## Granularité
Conserver les ressources ayant valeur pour service management : subscriptions/accounts, ressources structurantes, compute, DB, network, load balancers, clusters. Éviter de dupliquer tout Azure Resource Graph sans cas d’usage.

## Relations
Doivent représenter hébergement/dépendances réellement utiles à l’impact.
