# Plateforme, instances et responsabilités

ServiceNow est consommé comme plateforme SaaS. L’architecte distingue :

- disponibilité de la plateforme fournie par ServiceNow ;
- configuration et qualité des données sous responsabilité client ;
- DEV/TEST/PROD et politiques de promotion ;
- clones et protection des données sensibles ;
- upgrades et tests de non-régression ;
- intégrations sortantes/entrantes et dépendances MID.

## PDI

Une PDI est un environnement d’apprentissage. Ne jamais supposer qu’un plugin ITOM payant y est disponible. Chaque lab indique une alternative : simulation REST, données synthétiques, schéma ou mock.
