---
created: 2025-01-16T09:27
updated: 2025-01-16T10:05
---

Alle Geräte mit einem offenen SSH Port (22) anzeigen

```bash
nmap -Pn -p 22 --open 192.168.22.0/24
```

Alle Ports scannen

```bash
nmap -p 1-65535 192.168.22.100
nmap -p- 192.168.22.100 # shortcut für alle Ports
```