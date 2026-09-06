# 01 — Carte des compétences et parcours Architecte Solution ServiceNow

> Cadrage initial du parcours MayaBank — CSDM / CMDB / IRE / ITOM / Discovery / Service Mapping / intégrations / OpenShift / Azure.

## 1. Objectif professionnel

La cible n'est pas de devenir développeur ServiceNow généraliste.

La cible est de devenir capable d'intervenir comme **Architecte Solution — ServiceNow CSDM / CMDB / ITOM — OpenShift / Azure**, capable de :

- comprendre le modèle de données ServiceNow ;
- concevoir une modélisation CSDM cohérente ;
- challenger une CMDB existante ;
- définir les CI, classes, attributs et relations utiles ;
- définir les sources autoritatives ;
- concevoir Identification et Reconciliation avec IRE ;
- concevoir la population de la CMDB ;
- comprendre Discovery, MID Server et Service Mapping ;
- intégrer Azure, AWS, OpenShift/Kubernetes et des sources externes ;
- relier la CMDB à ITOM, ITSM et Enterprise Architecture ;
- produire les dossiers d'architecture, ADR, RACI et schémas nécessaires ;
- expliquer les choix simplement en entretien ou devant des équipes projet.

La cible fonctionnelle de bout en bout est :

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

La chaîne d'alimentation et d'exploitation est :

```text
Sources externes
│
├── Azure
├── AWS
├── OpenShift / Kubernetes
├── VMware
├── Linux / Windows
├── Databases
├── Network
├── Monitoring
└── APIs
      │
      ▼
Discovery / Service Graph / IntegrationHub ETL / REST
      │
      ▼
IRE
      │
      ▼
CMDB
      │
      ▼
CSDM
      │
      ▼
Service Mapping
      │
      ▼
ITOM / ITSM / Enterprise Architecture
```

---

## 2. Carte des compétences

Échelle cible :

```text
0 - Inconnu
1 - Je reconnais
2 - Je comprends
3 - Je sais expliquer
4 - Je sais configurer
5 - Je sais concevoir
6 - Je sais challenger
7 - Je sais architecturer en entreprise avec expérience projet répétée
```

| Domaine | Priorité | Niveau cible /7 | Raison |
|---|---:|---:|---|
| CSDM 5 | Indispensable | 6 | Modèle architectural ServiceNow |
| CMDB / CI / classes / relations | Indispensable | 6 | Socle de tous les cas d'usage |
| IRE | Indispensable | 6 | Identification, doublons, sources autoritatives |
| Gouvernance CMDB | Indispensable | 6 | Responsabilités, ownership et qualité |
| CMDB Health / Data Manager | Indispensable | 5 | Fiabilité et cycle de vie |
| Service Instance | Indispensable | 6 | Représentation opérationnelle d'une application déployée |
| Architecture d'intégration | Indispensable | 6 | API, ETL, Service Graph, Discovery |
| OpenShift/Kubernetes ↔ CMDB | Indispensable | 6 | Différenciateur principal du profil |
| Azure/AWS ↔ ServiceNow | Indispensable | 5 | Architecture hybride / cloud |
| Discovery + MID Server | Indispensable | 5 | Population automatique de la CMDB |
| Service Mapping | Indispensable | 5 | Dépendances applicatives et impact |
| REST / IRE API | Indispensable | 5 | Intégration et POC |
| ITSM ↔ CMDB | Important | 4 | Incident, Problem, Change, impact |
| ITOM Visibility | Important | 4–5 | Discovery + Service Mapping |
| Service Graph / IntegrationHub ETL | Important | 5 | Ingestion industrielle |
| Enterprise Architecture / APM | Important | 4–5 | Portefeuille, capabilities, lifecycle |
| Sécurité / ACL / OAuth / MID | Important | 4 | Architecture sécurité |
| HA/DR ServiceNow | Important | 3–4 | Architecture de la plateforme SaaS |
| Event Management | Secondaire au départ | 3 | À traiter après CMDB/CSDM |
| ITOM Optimization | Secondaire au départ | 2–3 | À traiter plus tard |
| Flow Designer | Secondaire au départ | 2–3 | Compréhension utile, pas spécialité initiale |
| Glide API / scripting avancé | Faible priorité | 2 | Pas le métier cible |
| UI Builder | Faible priorité | 1 | Pas prioritaire pour l'architecture visée |
| Développement ServiceNow avancé | Faible priorité | 1–2 | Hors cible initiale |

### Priorité structurante

```text
CSDM
  ↓
CMDB
  ↓
IRE
  ↓
Governance / Health
  ↓
Discovery / Service Graph / ETL
  ↓
Service Mapping
  ↓
ITOM / ITSM
```

Ne pas commencer par ITOM ou par la configuration avancée avant de maîtriser **CSDM + CMDB + IRE**.

---

## 3. Compétences déjà réutilisables

Le socle existant est directement exploitable :

- architecture SI ;
- architecture applicative et technique ;
- OpenShift / Kubernetes ;
- Azure / AWS ;
- API REST ;
- Kafka / Event Driven Architecture ;
- bases de données ;
- réseau et infrastructure ;
- sécurité technique ;
- HA / DR ;
- environnements banque, paiements et assurance ;
- TOGAF / ArchiMate en cours d'apprentissage.

L'objectif n'est donc pas de réapprendre ces technologies mais d'apprendre leur **projection correcte dans ServiceNow**.

Exemple :

```text
CONNU

OpenShift
 ├── Cluster
 ├── Namespace
 ├── Deployment
 ├── Service
 ├── Route
 ├── Pod
 └── Node

À APPRENDRE DANS SERVICENOW

OpenShift
   ↓
Quels objets doivent réellement être des CI ?
   ↓
Dans quelles classes ?
   ↓
Avec quelles relations ?
   ↓
À quelle granularité ?
   ↓
Quelle source les crée ?
   ↓
IRE
   ↓
CMDB
   ↓
Service Instance
   ↓
Business Application
```

Le point d'architecture essentiel est de ne pas transformer la CMDB en inventaire exhaustif d'objets éphémères sans valeur opérationnelle. La granularité Kubernetes/OpenShift devra être justifiée par les usages : incident, changement, impact, service mapping, ownership, conformité, coût, sécurité ou exploitation.

---

## 4. Gap principal à combler

Le manque principal n'est pas l'architecture technique générale.

Il se concentre sur :

```text
                    GAP PRINCIPAL
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
        CSDM            CMDB            IRE
          │              │              │
          └──────────────┼──────────────┘
                         ▼
              SERVICE MANAGEMENT
                         │
                  Service Instance
                         │
                  Service Mapping
                         │
          Discovery / Service Graph
                         │
              OpenShift / Azure
```

Les concepts à maîtriser en priorité sont :

1. Business Capability
2. Business Application
3. Service Instance
4. Business Service
5. Technology Management Service
6. CI / classe / héritage / relation
7. Identification
8. Reconciliation
9. Source autoritative / source of truth
10. Lifecycle et qualité CMDB

---

## 5. Terminologie CSDM 5 à utiliser

Le dépôt adopte la terminologie actuelle de **CSDM 5**, tout en gardant les anciens termes lorsqu'ils restent nécessaires pour comprendre les environnements existants.

| CSDM 5 / terminologie actuelle | Ancienne terminologie / usage historique |
|---|---|
| **Service Instance** | **Application Service** avant CSDM v5 |
| **Technology Management Service** | Terme à utiliser pour le service technologique géré |

La documentation ServiceNow actuelle décrit **Service Instance** comme une représentation logique d'une pile applicative déployée. Elle précise qu'il s'agit du concept appelé *Application Service* avant CSDM v5.

En mission, il faut donc savoir comprendre et employer les deux vocabulaires sans les confondre.

### Exemple MayaBank

```text
Business Application
Payment Hub
      │
      ├── Service Instance : Payment Hub PROD
      ├── Service Instance : Payment Hub PREPROD
      └── Service Instance : Payment Hub UAT
```

Le **Business Application** représente l'application du portefeuille architectural.

Le **Service Instance** représente une instance opérationnelle/déployée de cette application, potentiellement distincte par environnement ou région.

---

## 6. Parcours optimal

### Phase A — Data Foundation

```text
ServiceNow Platform
       ↓
CMDB
       ↓
CI / Classes / Tables
       ↓
Relationships
       ↓
CSDM 5
       ↓
IRE
```

Objectif : comprendre les objets et les règles avant toute automatisation.

### Phase B — Gouvernance et qualité

```text
Sources
  ↓
Identification
  ↓
Reconciliation
  ↓
CMDB Health
  ↓
Lifecycle
  ↓
CMDB Data Manager
  ↓
Governance / RACI
```

À ce stade, être capable de répondre clairement à :

- qui crée le CI ?
- qui peut le modifier ?
- quelle source fait autorité ?
- comment détecter un doublon ?
- comment arbitrer deux sources concurrentes ?
- qui maintient la relation ?
- quand le CI doit-il être retiré ?
- comment mesurer la qualité ?

### Phase C — Population de la CMDB

Étudier et comparer :

```text
Manual
REST API
Import Sets
Transform Maps
IntegrationHub ETL
Service Graph Connectors
Discovery
Cloud Discovery
```

Objectif : choisir le mécanisme adapté à chaque source, sans contourner IRE.

### Phase D — Services et exploitation

```text
Service Instance
       ↓
Service Mapping
       ↓
ITOM
       ↓
Incident / Problem / Change
```

Objectif : passer d'un inventaire de CI à une compréhension des services et de leurs dépendances.

### Phase E — Cloud / OpenShift

```text
ServiceNow
   │
   ├── Azure
   ├── AWS
   ├── OpenShift / Kubernetes
   ├── Kafka
   ├── API Gateway
   └── Databases
```

Cette phase doit devenir le différenciateur du profil.

### Phase F — Enterprise Architecture

```text
Business Capability
       ↓
Business Application
       ↓
Technologies
       ↓
Lifecycle
       ↓
Risk / Cost / Technical Debt
       ↓
Roadmap
```

Puis construire les correspondances et différences avec :

- TOGAF ;
- ArchiMate ;
- MEGA HOPEX ;
- LeanIX ;
- Sparx Enterprise Architect ;
- ServiceNow Enterprise Architecture / APM.

---

## 7. POC à construire

Le parcours doit produire quelques POC complets plutôt qu'une accumulation de démonstrations isolées.

| POC | Sujet | Résultat attendu |
|---|---|---|
| POC-01 | MayaBank CSDM | Business Capability → Business Application → Service Instance |
| POC-02 | MayaBank CMDB | CI, classes, héritage, relations, lifecycle |
| POC-03 | IRE | Plusieurs sources → un CI correctement identifié et réconcilié |
| POC-04 | OpenShift → ServiceNow | CRC/OpenShift Local → Python → IRE → CMDB |
| POC-05 | Discovery | MID Server → infrastructure → CMDB |
| POC-06 | Service Mapping | Payment Service → API → Kafka → DB → OpenShift |
| POC-07 | Azure | Azure → connecteur/ETL/API → IRE → CMDB |

### POC différenciateur : OpenShift → ServiceNow

```text
OpenShift Local / CRC
       ↓
Kubernetes / OpenShift API
       ↓
Python Collector
       ↓
Transformation / Mapping
       ↓
IRE REST API
       ↓
CMDB
       ↓
Relations
       ↓
Service Instance
       ↓
MayaBank Payment Hub
```

Ce POC devra permettre de comprendre réellement :

```text
Source
  ↓
Collecte
  ↓
Mapping
  ↓
Identification
  ↓
Reconciliation
  ↓
CI
  ↓
Relation
  ↓
Service Instance
```

L'objectif n'est pas de réimplémenter ServiceNow Discovery mais de comprendre chaque étape de la chaîne de données.

---

## 8. Certification — ordre recommandé

Les certifications doivent servir le positionnement professionnel et non devenir une collection de badges.

### 1. CSA — Certified System Administrator

À faire en premier.

Pourquoi :

- compréhension de la plateforme ;
- navigation ;
- modèle de données ;
- sécurité ;
- import / intégration ;
- bases CMDB/CSDM ;
- administration nécessaire pour être autonome dans un lab.

Un architecte n'a pas besoin de devenir administrateur expert, mais il doit comprendre la plateforme qu'il architecture.

### 2. CIS-DF — Certified Implementation Specialist, Data Foundations (CMDB and CSDM)

Certification particulièrement cohérente avec la cible.

Priorité forte car elle porte directement sur :

```text
CMDB
+
CSDM
```

Pour ce profil, elle est plus directement alignée que de commencer par une spécialisation ITSM complète.

### 3. CIS-DISCO — Certified Implementation Specialist, Discovery

À traiter après la maîtrise de CMDB/CSDM/IRE.

Elle renforce :

- MID Server ;
- Discovery ;
- infrastructure ;
- population CMDB ;
- architecture réseau/sécurité associée.

### 4. CIS-SM — Certified Implementation Specialist, Service Mapping

À traiter ensuite pour approfondir :

- Service Instances ;
- dépendances ;
- entry points ;
- top-down discovery ;
- impact analysis.

### 5. Ensuite selon les missions

- CIS-ITSM si le rôle devient fortement orienté processus ITSM ;
- Enterprise Architecture / APM si le rôle se rapproche davantage du portefeuille applicatif ;
- autres certifications ITOM selon besoin réel.

### CTA — Certified Technical Architect

Objectif long terme uniquement.

Ne pas le traiter comme une certification immédiate. Il doit venir après une vraie maîtrise de la plateforme et, surtout, après de l'expérience projet ServiceNow réelle et répétée.

### Ordre cible

```text
CSA
 ↓
CIS-DF
 ↓
CIS-DISCO
 ↓
CIS-SM
 ↓
Expérience projet réelle
 ↓
CTA éventuellement
```

---

## 9. Estimation réaliste de progression

Pour un architecte déjà expérimenté en architecture/cloud/OpenShift/API :

| Travail sérieux | Résultat réaliste |
|---:|---|
| 2 semaines | Comprendre CMDB/CSDM/IRE et utiliser le bon vocabulaire |
| 4–6 semaines | Répondre sérieusement aux questions d'entretien fondamentales |
| 8–10 semaines | POC complet + MayaBank + architecture + préparation entretien |
| 3–6 mois | Niveau technique plus solide et répétable sur plusieurs POC |
| Expérience réelle | Autonomie complète sur une transformation ServiceNow d'entreprise |

Avec environ **2 à 3 heures de travail quotidien**, une cible raisonnable est **8 semaines** pour devenir crédible sur des missions d'architecture solution où ServiceNow/CSDM/CMDB constitue une composante importante du rôle.

Cela ne doit pas être présenté comme équivalent à plusieurs années d'expérience ServiceNow.

Positionnement honnête :

> Architecte Solution expérimenté Cloud/OpenShift/API ayant construit une spécialisation ServiceNow CSDM/CMDB/ITOM démontrable par des POC et un référentiel d'architecture.

---

## 10. Niveau cible

```text
CSDM                     ██████░  6/7
CMDB                     ██████░  6/7
IRE                      ██████░  6/7
Governance               ██████░  6/7

Service Mapping          █████░░  5/7
Discovery                █████░░  5/7
IntegrationHub / ETL     █████░░  5/7
REST / Integration       █████░░  5/7

OpenShift                ██████░  6/7
Azure                    █████░░  5/7

ITSM                     ████░░░  4/7
ITOM Health              ████░░░  4/7
ServiceNow Admin         ███░░░░  3/7

ServiceNow Development   ██░░░░░  2/7
```

La priorité est **niveau 5–6 sur CSDM / CMDB / IRE / architecture**, pas niveau 7 d'administrateur ou de développeur ServiceNow.

---

## 11. Architecture MayaBank cible

À la fin du parcours, l'architecture suivante doit pouvoir être reconstruite et expliquée au tableau blanc sans assistance :

```text
                         MAYABANK

BUSINESS
Payments
   │
   ▼
BUSINESS CAPABILITY
Execute Instant Payment
   │
   ▼
BUSINESS APPLICATION
Payment Hub
   │
   ├──────────────────────────┐
   ▼                          ▼
SERVICE INSTANCE          SERVICE INSTANCE
Payment Hub PROD          Payment Hub PREPROD
   │
   ▼
TECHNOLOGY MANAGEMENT SERVICES
   │
   ├── OpenShift
   ├── Kafka
   ├── Database
   └── API Gateway
   │
   ▼
CMDB
   │
   ├── Cluster
   ├── Nodes
   ├── VMs
   ├── Databases
   ├── Network
   └── Cloud Resources
   ▲
   │
IRE
   ▲
   │
   ├── Discovery
   ├── Azure
   ├── OpenShift
   ├── Service Graph
   ├── IntegrationHub ETL
   └── REST APIs
```

Pour chaque objet, l'architecte doit savoir expliquer :

- pourquoi il existe ;
- s'il s'agit réellement d'un CI ;
- sa classe ;
- son propriétaire ;
- sa source de création ;
- sa source autoritative ;
- ses règles d'identification ;
- ses règles de reconciliation ;
- ses relations autorisées ;
- son lifecycle ;
- les consommateurs de cette information ;
- les conséquences d'une donnée incorrecte.

---

## 12. IRE — principe non négociable

IRE doit devenir un réflexe d'architecture.

```text
Azure --------┐
Discovery ----┼──► IRE ───► CI unique dans la CMDB
SCCM ---------┘
```

### Identification

Question : plusieurs sources parlent-elles du même CI ?

Exemple :

```text
Azure      → server01
Discovery  → server01
SCCM       → server01
```

La cible n'est pas de créer trois CI mais de permettre à IRE d'identifier correctement l'objet selon les règles et identifiants disponibles.

### Reconciliation

Question : quelle source est autorisée à écrire quel attribut ?

Exemple conceptuel :

```text
Discovery → IP / données techniques observées
Azure     → Cloud Resource ID / métadonnées cloud
SCCM      → certaines données OS / endpoint
```

Les responsabilités réelles devront être définies selon les sources et règles de l'entreprise.

Principe : **ne pas contourner IRE pour alimenter arbitrairement les CI de la CMDB**.

---

## 13. Gouvernance cible

Le futur modèle de gouvernance devra au minimum inclure :

```text
Architecture
Operations
Application Owners
CMDB Team
Cloud Team
OpenShift Team
Security
ServiceNow Team
```

Pour chaque type d'objet, produire un RACI répondant à :

- qui crée ?
- qui modifie ?
- qui valide ?
- quelle source est autoritative ?
- qui maintient les relations ?
- qui gère le lifecycle ?
- qui contrôle la qualité ?
- qui corrige les doublons ?
- qui arbitre les conflits de sources ?

---

## 14. Méthode de travail du dépôt

Chaque LAB doit suivre strictement :

```text
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
```

Chaque LAB doit produire des preuves concrètes :

- Markdown ;
- schémas ;
- captures si utiles ;
- scripts ;
- payloads API ;
- résultats de test ;
- ADR ;
- checklist de validation ;
- questions/réponses d'entretien.

---

## 15. Prochaine étape

**LAB 01 — ServiceNow + CMDB + CSDM Foundations**

Le LAB 01 ne doit commencer qu'après validation de ce cadrage.

Il devra couvrir au minimum :

```text
ServiceNow Platform
      ↓
Tables
      ↓
cmdb_ci
      ↓
Classes / héritage
      ↓
CI
      ↓
Relations / cmdb_rel_ci
      ↓
Premiers objets CSDM MayaBank
```

Aucune configuration avancée de Discovery, Service Mapping ou ITOM ne doit être engagée tant que ces fondations ne sont pas validées.

---

## Références officielles

Documentation à privilégier pendant tout le parcours :

- ServiceNow Product Documentation — CSDM data domains: https://www.servicenow.com/docs/r/servicenow-platform/common-service-data-model-csdm/csdm-conceptual-model.html
- ServiceNow Product Documentation — Identification and Reconciliation Engine (IRE): https://www.servicenow.com/docs/r/servicenow-platform/configuration-management-database-cmdb/ire.html
- ServiceNow Product Documentation — Components and process of Identification and Reconciliation: https://www.servicenow.com/docs/r/servicenow-platform/configuration-management-database-cmdb/c_CompsandProcessIDandReconcil.html
- ServiceNow Product Documentation — Service Instance / Application Service: https://www.servicenow.com/docs/r/servicenow-platform/configuration-management-database-cmdb/create-it-services.html
- ServiceNow University — Certified System Administrator (CSA) Exam Blueprint: https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011554
- ServiceNow University — CIS Data Foundations (CMDB and CSDM): https://learning.servicenow.com/lxp/en/pages/now-learning-get-certified?achievement_id=0e97835c47ea2e10c00af235126d431b&id=amap_detail
- ServiceNow University — CIS Discovery (CIS-DISCO): https://learning.servicenow.com/lxp?id=kb_article_view&sysparm_article=KB0011545
- ServiceNow University — CIS Service Mapping (CIS-SM): https://learning.servicenow.com/lxp/en/it-operations-management/certified-implementation-specialist-service?course_id=16b4ab0647f8b21019dfe23c326d4302&id=learning_content_prev

> Vérifier systématiquement la release ServiceNow et la documentation officielle courante avant de figer une décision d'architecture, car le modèle CSDM, les interfaces et les parcours de certification évoluent.
