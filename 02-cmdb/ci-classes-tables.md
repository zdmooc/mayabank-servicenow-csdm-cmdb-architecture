# CI, classes et tables

Un **Configuration Item** est un composant qu’il est utile de gérer pour délivrer un service. Tous les assets ne sont pas des CI et tous les objets techniques observables ne méritent pas une persistance CMDB.

## Pourquoi plusieurs classes ?

Pour porter une sémantique, des attributs et des règles adaptées : serveur, base, réseau, service, etc. L’héritage évite de dupliquer les champs communs de `cmdb_ci`.

## MayaBank

`Payment Hub PROD` n’est pas le même concept qu’un worker OpenShift : le premier représente une instance logique de service applicatif ; le second est une ressource d’infrastructure. Les placer dans des classes appropriées permet des règles d’identification et lifecycle différentes.
