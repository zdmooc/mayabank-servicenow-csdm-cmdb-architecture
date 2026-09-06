# Design d’un payload IRE

Un payload d’intégration doit porter au minimum : classe cible, valeurs utiles, identité de source et informations nécessaires aux relations quand elles sont gérées.

Exemple conceptuel :

```json
{
  "items": [
    {
      "className": "cmdb_ci_server",
      "values": {"name": "server01", "serial_number": "ABC123"},
      "sys_object_source_info": {
        "source_name": "MAYABANK_LAB",
        "source_native_key": "server-abc123"
      }
    }
  ]
}
```

Le schéma exact doit être validé contre l’API IRE de la release utilisée avant exécution.
