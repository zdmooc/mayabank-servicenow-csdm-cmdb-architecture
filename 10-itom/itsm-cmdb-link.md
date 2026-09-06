# ITSM ↔ CMDB

La valeur de la CMDB devient visible dans Incident, Problem et Change lorsque les tickets ciblent des CI/services corrects et que les relations permettent l’analyse d’impact.

## Incident
Identifier le CI ou la Service Instance affectée, son owner et ses dépendances.

## Problem
Analyser les récurrences par CI/technologie/service.

## Change
Évaluer les services dépendants et le risque avant modification.

## MayaBank
Un incident sur `Payment Hub PROD` doit permettre de remonter aux dépendances critiques OpenShift/Kafka/DB sans obliger l’utilisateur à connaître chaque Pod.
