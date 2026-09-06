# OAuth et sécurité API

Checklist :
- client dédié par intégration ;
- scopes/roles minimum ;
- secret/token hors code ;
- rotation ;
- TLS ;
- allowlists/règles réseau si supportées ;
- journalisation ;
- rate limits ;
- révocation ;
- séparation DEV/PROD.

Les labs peuvent simplifier l’authentification mais doivent toujours signaler l’écart par rapport à la cible production.
