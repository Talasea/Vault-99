---
created: 2025-02-06T11:59
updated: 2025-02-06T12:00
---
Pfad: `/etc/suricata/suricata.yaml`
```yml
HOME_NET: "<IP_KALI_AGENT>"
EXTERNAL_NET: "any"

default-rule-path: /etc/suricata/rules
rule-files:
- "*.rules"

# Linux high speed capture support
af-packet:
  - interface: eth0
```