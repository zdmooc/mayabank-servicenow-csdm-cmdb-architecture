# Discovery Cloud et Kubernetes — principes

Cloud et Kubernetes apportent de fortes volumétries et des ressources éphémères. L’objectif n’est pas de tout persister.

## Décisions

- quelles ressources ont une identité stable ?
- quelles classes ServiceNow sont supportées par le connecteur/version ?
- quel connecteur ou pattern est disponible ?
- quelle source conserve les détails de runtime ?
- quelle rétention pour les objets courts ?
- quelle valeur pour Incident/Change/Impact ?

Pour OpenShift, favoriser les objets structurels/stables nécessaires aux services plutôt qu’une copie exhaustive de l’API Kubernetes.
