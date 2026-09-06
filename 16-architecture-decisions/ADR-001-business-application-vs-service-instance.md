# ADR-001 — Business Application vs Service Instance

**Status:** Accepted for MayaBank design.

## Context
Payment Hub possède plusieurs environnements.

## Decision
`Payment Hub` est la Business Application logique. `Payment Hub PROD`, `PREPROD`, `UAT` sont des Service Instances lorsque la modélisation opérationnelle le justifie.

## Consequences
- portefeuille non dupliqué par environnement ;
- incidents/changements peuvent cibler l’instance opérationnelle ;
- relations techniques séparées par environnement.
