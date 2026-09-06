# Granularité Kubernetes

## Généralement pertinents selon cas d’usage
- cluster ;
- nodes ;
- namespace/projet ;
- workloads stables ;
- services/routes/ingress structurants ;
- relations vers application/service.

## À challenger fortement
- pods éphémères ;
- ReplicaSet temporaires ;
- events ;
- ConfigMaps/Secrets comme CI ;
- objets générés à très courte durée.

### Test
Si l’objet disparaît toutes les heures, qui gère son lifecycle CMDB et quel incident/changement utile lui est attaché ?
