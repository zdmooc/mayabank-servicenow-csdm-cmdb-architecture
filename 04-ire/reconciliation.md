# Reconciliation

La réconciliation détermine quelles sources peuvent écrire quels CI/attributs et avec quelle priorité.

## Exemple

| Attribut | Source autoritative proposée |
|---|---|
| Cloud resource ID | Azure |
| OS observé / IP runtime | Discovery |
| Ownership applicatif | référentiel applicatif / EA |
| Lifecycle technique | source d’infrastructure maîtrisée |

Cette matrice est un design à valider avec les équipes ; elle ne doit jamais être implicite.
