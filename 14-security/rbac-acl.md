# RBAC / ACL

## Principe
Accorder les rôles par persona et responsabilité, pas directement à tous les utilisateurs.

## Personas MayaBank
- CMDB admin ;
- CMDB analyst ;
- application owner ;
- platform owner ;
- service owner ;
- integration service account ;
- auditor/read-only.

Les ACL sont testées sur lecture/écriture de tables/champs sensibles. L’architecte documente le modèle, l’admin implémente.
