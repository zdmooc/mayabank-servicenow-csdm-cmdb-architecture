# Hiérarchie de classes

L’héritage CMDB fournit un socle commun et des spécialisations. L’architecte doit éviter :

- classe custom créée avant d’avoir recherché une classe OOTB ;
- CI insérés directement dans une classe trop générique ;
- attributs dupliqués alors qu’ils existent sur un parent ;
- modèle de classes aligné sur l’organisation interne plutôt que sur la sémantique technique.

## Revue d’architecture

Pour toute nouvelle classe : besoin métier, classe standard candidate, identifiants, source, volume, lifecycle, relations, reporting, impacts upgrades.
