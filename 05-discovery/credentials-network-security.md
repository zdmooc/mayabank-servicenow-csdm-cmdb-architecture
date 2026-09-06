# Credentials, réseau et sécurité Discovery

## Principes

- least privilege ;
- comptes dédiés non humains ;
- rotation des secrets ;
- éviter secrets en scripts ;
- segmentation des ranges ;
- audit des utilisations ;
- tests depuis le MID vers les cibles ;
- revue régulière des droits.

## Architecture review

Pour chaque protocole : source MID, destination, port, méthode d’authentification, secret owner, rotation, journalisation, justification.

Ne jamais ouvrir un firewall « any/any » pour simplifier Discovery.
