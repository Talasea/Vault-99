---
created: 2024-11-14T11:53
updated: 2024-11-18T12:16
---
# Softwareaktualisierung

Alle Paketreferenzen aktuallisieren (es werden noch keine Pakete heruntergeladen)

```bash
sudo apt update
```

Alle Pakete herunterladen und installieren

```bash
sudo apt upgrade
```

# Netzwerk
## DNS Server konfigurieren

`/etc/resolv.conf`

Der Inhalt sieht üblicherweise wie folgt aus:
```bash
search mshome.net
nameserver 172.29.96.1
nameserver 192.168.1.220 # Zweiten Nameserver ergänzt (IP Adresse von WS)
```

❗Der erste DNS Server muss auskommentiert sein, damit das richtige Interface verwendet wird