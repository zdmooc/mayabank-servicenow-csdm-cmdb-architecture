# MID, credentials et secrets

- secrets jamais dans Git ;
- comptes non interactifs dédiés ;
- rotation ;
- permissions minimales par technologie ;
- logs d’usage ;
- séparation PROD/non-PROD lorsque nécessaire ;
- accès réseau strict ;
- durcissement hôte MID ;
- surveillance disponibilité/queue.

Le MID Server ne doit pas devenir un « bastion universel » doté de privilèges excessifs.
