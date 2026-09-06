# Modèle CSDM MayaBank

```mermaid
flowchart TD
  PAY[Payments] --> CAP[Execute Payment]
  CAP --> BA[Payment Hub]
  BA --> PROD[Payment Hub PROD]
  BA --> PRE[Payment Hub PREPROD]
  PROD --> OCP[OpenShift Platform Service]
  PROD --> KAF[Kafka Messaging Service]
  PROD --> DB[Database Service]
  OCP --> CL[OpenShift Cluster PROD]
  KAF --> KC[Kafka Cluster PROD]
  DB --> ORA[Oracle PROD]
```

## Ownership proposé

- Capability : métier / enterprise architecture.
- Business Application : application owner + EA.
- Service Instance : application/service owner + opérations.
- Technology Management Service : platform/service owner.
- Infrastructure CI : équipes techniques, alimentés par sources autoritatives.
