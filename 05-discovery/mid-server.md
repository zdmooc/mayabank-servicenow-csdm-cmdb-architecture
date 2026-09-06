# MID Server

Le MID Server sert d’intermédiaire entre l’instance ServiceNow et les ressources du réseau privé. Il exécute des actions localement puis échange avec l’instance.

## Design

- au moins un domaine réseau atteignable ;
- compte de service dédié ;
- sortie HTTPS vers ServiceNow selon exigences officielles ;
- pas d’exposition entrante inutile ;
- capacité/affinité selon Discovery, Service Mapping, intégrations ;
- supervision du service MID ;
- stratégie HA quand le cas d’usage l’exige.

## MayaBank

Prévoir des MID distincts ou groupés par zone de sécurité si PROD, PREPROD et zones sensibles ont des règles réseau différentes.
