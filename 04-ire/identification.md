# Identification

L’identification détermine si un objet entrant correspond à un CI existant ou doit créer un nouveau CI.

## Exemple MayaBank

Azure, Discovery et SCCM observent `server01`. La cible n’est pas trois CI mais **un CI correctement identifié**, à condition que les règles et identifiants permettent d’établir l’identité.

## Architecte

Définir les identifiants stables par classe. Éviter de dépendre uniquement d’un nom mutable. Exploiter, quand pertinent, les identifiants natifs de source et règles IRE supportées.
