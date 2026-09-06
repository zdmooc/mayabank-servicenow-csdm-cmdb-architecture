# HA / DR / upgrades / cloning — vue architecte

ServiceNow étant SaaS, l’architecte doit distinguer les mécanismes fournis par la plateforme des responsabilités client autour des données, intégrations et dépendances externes.

## À connaître

- stratégie DEV / TEST / PROD ;
- clones et exclusions/protection de données ;
- promotion contrôlée des changements ;
- tests de régression et ATF selon périmètre ;
- releases/upgrades et compatibilité plugins/intégrations ;
- disponibilité de l’instance vs disponibilité des MID/IdP/sources externes ;
- RPO/RTO contractuels à vérifier dans les engagements ServiceNow du client ;
- plan de continuité des intégrations lorsque ServiceNow ou une source est indisponible.

## Architecture review
Ne jamais inventer un RPO/RTO ServiceNow : utiliser les engagements contractuels et la documentation de la souscription réelle.
