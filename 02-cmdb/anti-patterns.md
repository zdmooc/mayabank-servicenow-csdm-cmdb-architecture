# Anti-patterns CMDB

- saisie manuelle massive sans ownership ;
- imports directs contournant IRE ;
- plusieurs sources écrivant les mêmes attributs sans règles ;
- CI sans classe précise ;
- relations génériques partout ;
- objets éphémères sans valeur métier ;
- CI jamais retirés ;
- Business Application confondue avec instance PROD ;
- modèle créé pour le reporting mais inutilisable pour Incident/Change ;
- qualité mesurée sans processus de remédiation.

Une « CMDB poubelle » est généralement un problème de **gouvernance + identification + lifecycle**, pas seulement de nettoyage ponctuel.
