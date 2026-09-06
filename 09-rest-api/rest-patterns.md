# REST patterns

## Lecture
Utiliser filtres précis, champs nécessaires, pagination et limites.

## Écriture
Pour CI, ne pas utiliser une écriture directe générique si elle contourne les mécanismes d’identification/réconciliation attendus.

## Idempotence
Un même événement rejoué ne doit pas créer un nouveau CI. La combinaison source + native key + IRE aide à maîtriser ce comportement.

## Résilience
Retry avec backoff sur erreurs transitoires, pas sur erreurs fonctionnelles permanentes.
