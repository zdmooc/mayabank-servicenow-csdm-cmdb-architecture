# Service Instance

CSDM v5 emploie **Service Instance**, appelé *Application Service* dans les versions antérieures.

Une Service Instance représente une instance logique déployée d’un stack applicatif et peut être utilisée dans Incident, Problem et Change.

## MayaBank

- Payment Hub PROD
- Payment Hub PREPROD
- Payment Hub UAT

Chaque instance peut avoir ses propres dépendances OpenShift, Kafka, DB, réseau et observabilité.

Référence : https://www.servicenow.com/docs/r/servicenow-platform/configuration-management-database-cmdb/application-services.html
