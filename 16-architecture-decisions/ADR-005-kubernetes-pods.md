# ADR-005 — Pods Kubernetes

**Status:** Accepted for MayaBank POC.

## Decision
Les Pods ne sont pas persistés comme CI par le collector pédagogique par défaut. Ils peuvent rester observés dans Kubernetes/monitoring.

## Exception
Un besoin produit ServiceNow spécifique ou un connecteur standard peut conduire à une autre stratégie ; elle devra être évaluée en volumétrie, lifecycle et cas d’usage.
