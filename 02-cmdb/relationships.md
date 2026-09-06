# Relations CMDB

Une relation doit exprimer une dépendance exploitable, pas seulement une proximité documentaire.

## Catégories conceptuelles

- **Runs on / Hosted on** : hébergement.
- **Depends on / Used by** : dépendance fonctionnelle ou technique.
- **Contains / Contained by** : composition quand le modèle le justifie.
- **Connects to** : connectivité, à utiliser avec parcimonie.

## Règle

Toujours être capable d’expliquer l’impact : « si le CI B tombe, pourquoi le CI A est-il affecté ? ». Si la réponse n’est pas claire, la relation est probablement inutile ou mal typée.
