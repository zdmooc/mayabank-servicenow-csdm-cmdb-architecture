# LAB-07 — REST + IRE API

**Statut : À EXÉCUTER**

## Étapes
```bash
cp .env.example .env
pip install -r scripts/requirements.txt
python scripts/ire_upsert_example.py
# uniquement après revue du dry-run
python scripts/ire_upsert_example.py --commit
```

## Validation
- TLS vérifié ;
- aucun secret dans Git ;
- dry-run compris ;
- commit contrôlé ;
- rejeu idempotent ;
- réponse IRE archivée sans information sensible.
