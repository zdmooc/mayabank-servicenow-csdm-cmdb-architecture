# Préparation LAB OpenShift

**Statut : À EXÉCUTER**

Pré-requis : CRC/OpenShift Local opérationnel et projet `mayabank`.

Étapes :
1. collecter cluster/nodes/namespaces/workloads/services/routes ;
2. filtrer selon politique de granularité ;
3. produire JSON normalisé ;
4. mapper classes ServiceNow réelles ;
5. envoyer via IRE ;
6. rejouer et vérifier absence de doublon ;
7. modifier une ressource et vérifier update ;
8. supprimer une ressource et observer lifecycle.

Preuves : exports JSON + sys_id + captures + logs collector.
