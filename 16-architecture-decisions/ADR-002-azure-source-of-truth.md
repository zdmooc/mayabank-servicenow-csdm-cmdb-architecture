# ADR-002 — Azure comme source de vérité technique

**Status:** Proposed, à valider au LAB-09.

## Decision
Pour les attributs intrinsèques des ressources Azure (resource ID, région, type), Azure/connecteur supporté est prioritaire. Les attributs d’ownership applicatif restent gouvernés par le référentiel approprié.

## Reason
Une seule source n’est pas autoritative pour tous les attributs d’un CI.
