# Data model basics

## Concepts

- **Table** : structure persistante.
- **Record** : ligne logique d’une table.
- **Field** : attribut.
- **sys_id** : identifiant interne unique.
- **Inheritance** : une table enfant hérite des champs d’une table parent.
- **Reference field** : lien vers un record d’une autre table.

Dans la CMDB, la classe de base est `cmdb_ci`. Les classes spécialisées ajoutent sémantique et attributs. Les relations entre CI sont stockées via le modèle de relations CMDB, notamment `cmdb_rel_ci`.

## Décision architecte

Choisir la classe la plus précise disponible et supportée ; ne pas créer une nouvelle classe simplement pour reproduire la structure d’un outil source.
