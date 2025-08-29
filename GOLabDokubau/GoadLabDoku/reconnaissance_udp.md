# Reconnaissance Phase Report (UDP-Erweiterung)

## Übersicht der aktiven Hosts und deren UDP-Dienste (Top 1000 Ports)

| IP-Adresse    | UDP-Ports (Services)                                                                                                      | Anmerkungen                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| 192.168.20.10 | 53 (domain), 88 (kerberos-sec), 123 (ntp), 137 (netbios-ns), 138 (netbios-dgm), 389 (ldap), 464 (kpasswd5), 500 (isakmp), 3389 (ms-wbt-server), 4500 (nat-t-ike), 5353 (zeroconf), 5355 (llmnr), diverse high UDP-Ports (open|filtered) | Active Directory Domänencontroller, DNS, Kerberos, LDAP, RDP, NTP   |
| 192.168.20.11 | 53 (domain), 88 (kerberos-sec), 123 (ntp), 137 (netbios-ns), 138 (netbios-dgm), 389 (ldap), 464 (kpasswd5), 500 (isakmp), 3389 (ms-wbt-server), 4500 (nat-t-ike), 5353 (zeroconf), 5355 (llmnr), diverse high UDP-Ports (open|filtered) | Zweiter Domänencontroller, LDAP, Kerberos, RDP           |
| 192.168.20.12 | 53 (domain), 88 (kerberos-sec), 123 (ntp), 137 (netbios-ns), 138 (netbios-dgm), 389 (ldap), 464 (kpasswd5), 500 (isakmp), 3389 (ms-wbt-server), 4500 (nat-t-ike), 5050 (mmcc), 5353 (zeroconf), 5355 (llmnr), diverse high UDP-Ports (open|filtered) | Domänencontroller, zusätzliche UDP-Angebote (MMCC)     |
| 192.168.20.13–21 | keine UDP-Antwort (open|filtered auf allen 1000 Ports)                                                             | Netzwerksegmente oder Firewall filtern UDP vollständig |
| 192.168.20.22 | 123 (ntp), 137 (netbios-ns), 138 (netbios-dgm), 500 (isakmp), 3389 (ms-wbt-server), 4500 (nat-t-ike), 5353 (zeroconf), 5355 (llmnr), diverse high UDP-Ports (open|filtered) | SQL- und RDP-Host, UDP-Filter gemischt                   |
| 192.168.20.23 | 123 (ntp), 137 (netbios-ns), 138 (netbios-dgm), 500 (isakmp), 3389 (ms-wbt-server), 4500 (nat-t-ike), 5050 (mmcc), 5353 (zeroconf), 5355 (llmnr), diverse high UDP-Ports (open|filtered) | Datenbank- und RDP-Host mit MMCC                         |

## Erkenntnisse

Die zusätzlichen UDP-Scans bestätigen:

- **Domain-, Kerberos- und LDAP-Dienste** laufen unverändert zuverlässig über UDP bei den Domänencontrollern.
- **NetBIOS- (137, 138) und ISAKMP/IPSec-Ports (500, 4500)** sind offen bzw. gefiltert, was VPN/IPSec-Verkehr unterstützen kann.
- **NTP (123/udp)** ist auf allen drei DCs aktiv und synchronisiert Systemzeit, wichtig für Kerberos.
- **Ein Host (192.168.20.12, 192.168.20.23)** bietet UDP-Port 5050 (MMCC), möglicherweise zusätzlicher Dienst.
- **Mehrere Hosts (13–21)** antworten auf UDP-Scans nicht, was auf strenge Firewall-Regeln oder Netzwerksegmentierung hindeutet.

## Empfehlungen zur weiteren Vorgehensweise

- **UDP-basierte Enumeration**: Testen von LDAP und Kerberos über UDP (`rpcclient`, `krb5-user`).
- **IPSec/VPN Analyse**: Prüfen der IPsec/IKE-Konfiguration (Port 500/4500) auf Schwachstellen.
- **NTP-Sicherheit**: Sicherstellen, dass NTP-Server korrekt konfiguriert sind, um Zeitmanipulation zu verhindern.
- **Unbekannte UDP-Dienste (5050/MMCC)**: Identifizieren und untersuchen dieser Dienste, ggf. Versionserkennung.
- **Firewall-Bypass-Techniken**: Hosts ohne UDP-Antworten könnten intern erreichbar sein – Pivoting oder interne Scans erwägen.

*Erstellt am 22.08.2025*