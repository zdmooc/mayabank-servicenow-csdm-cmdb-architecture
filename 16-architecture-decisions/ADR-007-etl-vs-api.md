# ADR-007 — IntegrationHub ETL / Service Graph vs API custom

**Status:** Accepted as decision principle.

## Decision
Préférer une intégration standard supportée lorsqu’elle couvre correctement la source. Utiliser un collector/API custom pour un besoin non couvert ou pour le POC pédagogique.

## Trade-off
Standard : support/upgrade simplifiés. Custom : contrôle accru mais responsabilité de mapping, sécurité, erreurs et maintenance.
