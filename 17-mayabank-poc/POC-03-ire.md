# POC-03 — IRE multi-source

**Status:** À EXÉCUTER

Simuler deux sources décrivant le même serveur/CI avec identifiant commun ou source native key.

## Tests
1. dry-run `/api/now/identifyreconcile/query` ;
2. insertion réelle contrôlée ;
3. rejeu identique → pas de doublon ;
4. deuxième source → update autorisé/refusé selon reconciliation ;
5. changement d’attribut prioritaire.

Référence : https://www.servicenow.com/docs/r/api-reference/rest-apis/c_IdentifyReconcileAPI.html
