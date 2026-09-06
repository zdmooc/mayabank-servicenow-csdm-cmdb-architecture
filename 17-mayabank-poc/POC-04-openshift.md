# POC-04 — OpenShift → ServiceNow

**Status:** À EXÉCUTER

Collecter `oc get` / API, normaliser, filtrer par granularité, transformer en payloads IRE.

## Acceptation
- cluster/namespace/workload/service identifiés ;
- pods exclus par politique par défaut ;
- rejeu idempotent ;
- logs sans secret ;
- source/native key stable ;
- relations vers Payment Hub PROD démontrées ou documentées.
