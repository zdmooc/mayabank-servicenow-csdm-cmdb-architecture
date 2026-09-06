# HOPEX / LeanIX / Sparx ↔ ServiceNow

Ces outils peuvent couvrir architecture d’entreprise, cartographie ou portefeuille avec des périmètres qui recouvrent ServiceNow EA/APM/CSDM.

## Règle de conception
Avant toute synchronisation définir :
- objet maître ;
- attributs maîtres ;
- sens du flux ;
- identifiant de rapprochement ;
- fréquence ;
- gestion des suppressions ;
- conflits ;
- audit.

Exemple : HOPEX peut rester maître de certains éléments d’architecture tandis que ServiceNow est maître des Service Instances et CI opérationnels. Le choix dépend de l’organisation réelle.
