# 06 — Service Mapping

Discovery répond surtout à **« quels CI existent ? »** ; Service Mapping répond à **« quels CI et dépendances délivrent ce service ? »**.

```mermaid
flowchart TD
  SI[Payment Hub PROD] --> GW[API Gateway]
  GW --> API[Payment API]
  API --> KAF[Kafka]
  API --> DB[Oracle]
  KAF --> FRAUD[Fraud Engine]
  API --> OCP[OpenShift]
```

L’architecte définit le périmètre, les entry points, les dépendances utiles et la stratégie de maintenance.

Référence : https://www.servicenow.com/docs/r/it-operations-management/service-mapping/service-mapping-setup.html
