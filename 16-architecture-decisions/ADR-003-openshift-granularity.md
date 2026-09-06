# ADR-003 — Granularité OpenShift

**Status:** Accepted as POC policy.

## Decision
Persister en priorité cluster, nodes, namespaces/projects, workloads et endpoints/services structurants utiles au service management. Les objets très éphémères sont exclus par défaut.

## Consequence
La CMDB reste exploitable et son lifecycle ne dépend pas de milliers d’objets à durée très courte.
