# 12 — OpenShift / Kubernetes ↔ ServiceNow

C’est le différenciateur principal du dépôt.

## Objectif

Construire un modèle qui relie :

```text
Business Application
→ Service Instance
→ OpenShift Service/Route/Workload
→ Namespace
→ Cluster
→ Node/VM/Cloud
```

sans transformer la CMDB en copie d’`oc get all`.
