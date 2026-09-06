# Kafka / Event Driven Architecture

ServiceNow n’a pas besoin de recevoir tout événement métier. Un flux événementiel doit servir un cas d’usage précis : changement de ressource, événement opérationnel, workflow ou synchronisation.

## Pattern recommandé
```text
Producer → Kafka → Integration Service → validation/idempotence → ServiceNow API → IRE/target API
```

## Points d’architecture
schema/versioning, ordering, replay, dead-letter, retries, correlation ID, secrets, débit, throttling ServiceNow et ownership.

Pour la CMDB, le message doit transporter une identité de source stable et ne pas créer un nouveau CI à chaque replay.
