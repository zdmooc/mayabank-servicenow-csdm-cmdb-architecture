# Patterns d’intégration d’entreprise

## ServiceNow ↔ Azure/AWS/OpenShift
Connecteur standard/Service Graph/Discovery en priorité, ETL/API si besoin spécifique.

## ServiceNow ↔ Kafka
Éviter de connecter directement la CMDB à chaque événement métier. Utiliser un service d’intégration lorsque le besoin est event-driven, avec idempotence, contrat, DLQ/retry et sécurité.

## ServiceNow ↔ API Gateway
API Gateway peut centraliser sécurité, throttling et observabilité pour des intégrations externes, mais ne remplace pas IRE côté CI.

## ServiceNow ↔ Monitoring
Normaliser l’identité des ressources afin que les événements puissent être rapprochés des CI/services.

## ServiceNow ↔ IAM
Séparer authentification humaine, comptes de service, groupes et provisioning ; appliquer least privilege.

## ServiceNow ↔ CMDB externe / HOPEX / LeanIX
Définir précisément le système de référence par objet/attribut et le sens de synchronisation afin d’éviter deux sources maîtres concurrentes.
