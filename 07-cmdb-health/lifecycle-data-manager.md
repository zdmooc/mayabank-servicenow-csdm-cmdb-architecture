# Lifecycle et Data Manager

Le lifecycle doit être défini par classe et source : création, opération, maintenance, retrait, archive/suppression selon règles applicables.

## Questions architecte

- qui décide qu’un CI est retired ?
- la source le supprime-t-elle ou le marque-t-elle ?
- combien de temps conserver ?
- quelles relations empêcher avant suppression ?
- quelle différence entre logique et physique ?

La suppression automatique sans politique ni audit est interdite dans le lab.
