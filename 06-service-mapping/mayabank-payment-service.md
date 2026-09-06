# Service Mapping — MayaBank Payment Hub

## Entry point proposé
`https://payments.mayabank.example/api`

## Dépendances attendues

```text
Payment Hub PROD
→ API Gateway
→ Payment API / OpenShift Service
→ Kafka
→ Oracle/PostgreSQL
→ Fraud Engine
```

## Validation

- chaque nœud a un CI/class approprié ;
- aucune dépendance importante n’est purement documentaire ;
- owner du service identifié ;
- mapping se met à jour sans duplication ;
- impact d’un CI critique visible depuis la Service Instance.
