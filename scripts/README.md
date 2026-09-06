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
- `sample_ire_payload.json` : payload pédagogique.

Toujours commencer par l’endpoint IRE `/query` pour simuler avant commit lorsque pertinent.
