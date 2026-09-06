# Erreurs, retry et observabilité

Pour chaque appel : correlation ID, source object ID, HTTP status, durée, nombre de retry et résultat IRE.

## Catégories

- 4xx fonctionnel/auth : corriger, ne pas boucler aveuglément ;
- 429 : respecter throttling/backoff ;
- 5xx/transitoire : retry borné ;
- timeout : vérifier idempotence avant rejeu ;
- mapping/IRE rejection : dead-letter ou file d’erreur avec remédiation.

Le POC doit produire un résumé : reçus, créés, mis à jour, rejetés, retriés.
