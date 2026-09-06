# 02 — CMDB

La CMDB n’est pas un inventaire universel. C’est un modèle opérationnel de configuration permettant d’analyser les services, dépendances, changements, incidents et impacts.

## Questions obligatoires pour chaque CI

1. Pourquoi existe-t-il dans la CMDB ?
2. Quelle classe ?
3. Quelle clé d’identification ?
4. Quelle source fait autorité ?
5. Qui en est propriétaire ?
6. Quelles relations sont utiles ?
7. Quel lifecycle ?
8. Comment détecter stale/duplicate/orphan ?

## Anti-pattern

`Source possède 40 types d’objets → créer 40 classes CMDB` est faux. La CMDB doit répondre aux cas d’usage Service Management, pas reproduire chaque source.
