# LAB-08 — OpenShift → ServiceNow

**Statut : À EXÉCUTER**

## Pré-requis
CRC/OpenShift Local + `oc` connecté.

## Étapes
```bash
oc project mayabank
python scripts/openshift_inventory.py
```
Puis analyser l’inventaire, choisir objets persistants, mapper classes de la PDI, générer payloads IRE et commencer par dry-run.

## Tests
rejeu, changement de label/version, scale deployment, suppression workload, absence de Pod dans le modèle par défaut.
