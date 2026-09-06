# Health / Event Management — niveau architecte

Le principe à maîtriser : des événements provenant d’outils de monitoring sont rapprochés de CI/services afin de réduire le bruit et comprendre l’impact.

```text
Monitoring → Event → CI → Service Instance → Business impact
```

Le détail de configuration est secondaire avant d’avoir une CMDB fiable. Sans identité correcte des CI, la corrélation et l’impact deviennent fragiles.
