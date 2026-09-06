# Patterns, ranges et schedules

Discovery doit être piloté par un périmètre maîtrisé.

## Ranges
Définir les espaces IP explicitement, avec exclusions et ownership.

## Schedules
Adapter fréquence et fenêtre au taux de changement des CI. Une CMDB temps réel n’existe pas si la source ne l’est pas.

## Patterns
Les patterns encapsulent la logique de découverte supportée. L’architecte privilégie standard/OOTB avant custom, car chaque custom augmente le coût d’upgrade et de support.

## KPI
Taux de succès Discovery, CI nouveaux, CI mis à jour, erreurs credentials, durée, stale CI après fenêtre définie.
