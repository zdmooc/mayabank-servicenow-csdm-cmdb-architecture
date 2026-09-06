# IRE API

Le POC MayaBank utilisera un payload contrôlé vers l’API IRE appropriée à la release PDI.

## Flux

```mermaid
sequenceDiagram
  participant O as OpenShift Collector
  participant S as ServiceNow REST
  participant I as IRE
  participant C as CMDB
  O->>S: payload + source/native key
  S->>I: identify/reconcile
  I->>C: create or update
  C-->>O: result/sys_id/status
```

Avant exécution : vérifier endpoint, rôles, format exact du payload et comportement de la release.
