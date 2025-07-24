---
created: 2024-11-14T10:53
updated: 2024-11-25T09:22
---
# Grundlagen

Hilfe für ein Kommando anzeigen lassen

```bash
# commando -h oder --help (beides versuchen falls eines nicht verfügbar ist)
apt -h
apt --help
```
# Netzwerk

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