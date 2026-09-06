# Authentification et sécurité API

## Production
Préférer mécanismes d’authentification supportés avec secrets courts/rotatifs, OAuth lorsque pertinent, scopes/roles minimaux, TLS et journalisation.

## PDI
Basic Auth peut être utilisé pour un lab contrôlé, avec un utilisateur dédié et sans publier le secret.

## Git
Jamais de password/token dans le dépôt. Utiliser variables d’environnement :

```text
SN_INSTANCE
SN_USERNAME
SN_PASSWORD
```

ou un mécanisme OAuth lorsque le lab est étendu.
