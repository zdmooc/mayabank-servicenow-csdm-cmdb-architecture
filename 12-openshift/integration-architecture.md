# Architecture d’intégration OpenShift

POC pédagogique :

```text
OpenShift API
→ Python collector
→ normalisation
→ payload IRE
→ ServiceNow
→ CMDB
```

Production : évaluer d’abord les intégrations/Discovery/Service Graph supportées.

Le collector du dépôt sert à comprendre de bout en bout : source, mapping, identité, reconciliation, relation, lifecycle, erreur et observabilité.
