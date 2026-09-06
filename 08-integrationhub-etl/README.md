# 08 — IntegrationHub ETL / Service Graph

Objectif : choisir le bon pattern d’ingestion sans contourner IRE.

```text
Source → collecte → staging/mapping → IRE → CMDB → qualité
```

## Comparaison à maîtriser

- Import Set + Transform Map ;
- IntegrationHub ETL ;
- Service Graph Connector ;
- REST/IRE API ;
- Discovery.

Le choix dépend du produit source, du connecteur disponible, du volume, de la fréquence, du mapping, des relations et du support éditeur.
