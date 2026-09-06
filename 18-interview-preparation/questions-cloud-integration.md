# Questions Cloud / intégration

## Pourquoi ne pas importer chaque Pod ?
Identité/lifecycle trop courts, bruit et coût de gouvernance souvent sans valeur pour Incident/Change. On conserve les objets stables utiles au service, sauf besoin produit spécifique.

## Azure source of truth ?
Azure peut être autoritatif pour attributs natifs cloud ; pas nécessairement pour owner applicatif ou criticité métier.

## ETL ou API ?
Standard/connecteur supporté en priorité ; custom lorsque le besoin n’est pas couvert ou pour un POC, en acceptant la responsabilité sécurité/mapping/maintenance.
