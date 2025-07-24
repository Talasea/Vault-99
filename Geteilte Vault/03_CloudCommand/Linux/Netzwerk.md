---
created: 2025-01-21T16:33
updated: 2025-01-21T16:34
---
Informationen über bestehende Interfaces ausgeben lassen (IP Adresse, Subnetzmaske, GW)

```bash
ip address
ip a # Kurzfassung
```

Neue IPv4 Adresse setzten

```bash
sudo ip address add 192.168.1.110/24 dev eth1
```

IPv4 Adresse löschen

```bash
sudo ip address delete 192.168.1.100/24 dev eth1
```

❗Hinweis: ein Löschen der primären IP Adresse (die erste) führt dazu, dass andere (sekundäre) IP Adressen auch gelöscht werden