# Granularité des CI

La bonne granularité maximise la valeur opérationnelle tout en limitant bruit et coût de gouvernance.

## Test en 5 questions

Un objet mérite-t-il un CI si :
1. on ouvre des incidents/changements dessus ?
2. son état influence un service ?
3. il a une identité suffisamment stable ?
4. une source fiable maintient son lifecycle ?
5. la relation apporte une analyse d’impact ?

Pour Kubernetes, un Pod très éphémère échoue souvent aux questions 3–4. Un cluster, node, namespace, workload stable ou service peut être plus pertinent selon le cas d’usage.
