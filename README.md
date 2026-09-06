# MayaBank — ServiceNow CSDM / CMDB / ITOM Architecture

Référentiel d'apprentissage et de démonstration pour construire progressivement un niveau **Architecte Solution — ServiceNow CSDM / CMDB / ITOM — OpenShift / Azure**.

Le dépôt s'appuie sur une banque fictive, **MayaBank**, pour relier architecture métier, architecture applicative, CSDM, CMDB, IRE, Discovery, Service Mapping, ITOM, ITSM et intégrations Cloud/OpenShift.

## Objectif

Être capable de concevoir et d'expliquer de bout en bout :

```text
Métier
  ↓
Business Capability
  ↓
Business Application
  ↓
Service Instance
  ↓
Technology Management Service
  ↓
Infrastructure
  ↓
OpenShift / Kubernetes / Azure / AWS / VM / DB / Network
  ↓
CMDB
```

et la chaîne de population/gouvernance :

```text
Sources externes
  ↓
Discovery / Service Graph / IntegrationHub ETL / REST
  ↓
IRE
  ↓
CMDB
  ↓
CSDM
  ↓
Service Mapping
  ↓
ITOM / ITSM / EA
```

## Roadmap

Le cadrage initial complet est disponible ici :

- [Carte des compétences, gaps, parcours, POC et certifications](00-roadmap/01-skill-map-and-learning-path.md)

## Principes de travail

Chaque étape du parcours doit suivre la même méthode :

1. Concept
2. Explication simple
3. Architecture
4. Exemple MayaBank
5. Manipulation ServiceNow
6. Vérification
7. Questions d'entretien
8. Documentation GitHub
9. Commit
10. Validation avant l'étape suivante

## Positionnement professionnel visé

**Architecte Solution — ServiceNow CSDM / CMDB / ITOM — OpenShift / Azure**

Le dépôt doit démontrer des compétences réelles et vérifiables par des architectures, POC, scripts, ADR, modèles de données, mappings et dossiers d'architecture, sans prétendre à une expérience projet ServiceNow non encore acquise.

## Références de terminologie

Le dépôt utilise la terminologie **CSDM 5** tout en conservant les anciens termes entre parenthèses lorsqu'ils restent courants en mission :

- **Service Instance** — anciennement *Application Service* avant CSDM v5.
- **Technology Management Service** — terminologie actuelle pour les services technologiques gérés.

Références principales : documentation ServiceNow officielle, ServiceNow University et documentation CSDM/CMDB/IRE de la release courante.
