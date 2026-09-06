# Scripts

Starter kit pour les labs. **Aucun secret dans Git.**

## Installation
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r scripts/requirements.txt
```

Copier `.env.example` vers `.env` puis renseigner localement.

## Scripts
- `servicenow_client.py` : client REST minimal ;
- `ire_upsert_example.py` : dry-run puis upsert IRE ;
- `openshift_inventory.py` : inventaire OpenShift via `oc` ;
- `openshift_normalize.py` : normalisation neutre sans inventer de classes ServiceNow ;
- `validate_no_secrets.py` : contrôle simple avant commit ;
- `sample_ire_payload.json` : payload pédagogique.

## Séquence OpenShift
```bash
python scripts/openshift_inventory.py
python scripts/openshift_normalize.py
```

Le mapping vers des classes ServiceNow réelles se fait seulement après vérification sur la PDI/release.

Pour IRE, commencer par `/api/now/identifyreconcile/query` pour simuler avant commit lorsque pertinent.
