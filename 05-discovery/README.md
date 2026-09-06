# 05 — Discovery

Objectif architecte : comprendre comment ServiceNow découvre l’infrastructure, quelles dépendances réseau/sécurité existent et comment les résultats sont identifiés dans la CMDB.

```mermaid
flowchart LR
  SN[ServiceNow SaaS] <--> MID[MID Server]
  MID --> NET[Network]
  MID --> LNX[Linux/Windows]
  MID --> DB[Databases]
  MID --> VM[VMware/Cloud]
```

## À challenger

- placement et résilience des MID Servers ;
- flux firewall et DNS ;
- comptes/credentials et moindre privilège ;
- IP ranges / schedules ;
- capabilities ;
- patterns ;
- volumétrie et fenêtres de scan ;
- comportement IRE ;
- erreurs de découverte et ownership.

Référence : https://www.servicenow.com/docs/r/servicenow-platform/mid-server/explore-mid-server.html
