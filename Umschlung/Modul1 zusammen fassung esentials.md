[Modul Eins – Kompaktwissen IT-Infrastruktur & Security (erweitert)](data: text/markdown;charset=utf-8'''# Modul Eins – Kompaktwissen IT-Infrastruktur & Security (erweitert)

## Kapitelübersicht

1. Netzwerksicherheit & Authentifizierung
    
2. PowerShell-Grundlagen
    
3. ISO/OSI-Schichten & TCP/IP
    
4. IP-Adressierung & Subnetting
    
5. Übertragungs- & Kabeltechnik
    
6. Netzwerktechnik & Topologien
    
7. Sendearten, Ethernet & WLAN
    
8. Windows Server & Active Directory
    
9. Dateidienste & Freigaben
    
10. DHCP & DNS
    
11. Routing & Remote Access
    
12. Netzwerk-Troubleshooting & Monitoring
    
13. Software- und Systemhärtung
    
14. Informationssicherheit vs. IT-Sicherheit
    
15. Schutzziele der Informationssicherheit
    
16. Defense-in-Depth (DiD)
    
17. Maßnahmen der Informationssicherheit
    
18. Bedrohungslandschaft & Angreifer
    
19. Sicherheitsbewusstsein
    
20. Computer-Architektur Grundlagen
    
21. Netzwerkanalyse mit Wireshark
    
22. Datenspeicher & Einheiten
    
23. Datenschutz-Grundverordnung
    
24. Lage der IT-Sicherheit
    
25. Funkfeldmessung
    
26. Glasfaser-Werkzeuge
    
27. Patchpanel
    
28. Media Access Control
    
29. Hash-Algorithmen
    

## 1. Netzwerksicherheit & Authentifizierung

- Kennwort-, Zwei-Faktor-, Token-, Biometrische und Transaktionale Authentifizierung
    
- Authentifizierungsprotokolle: Kerberos (Ticket-basiert) und TLS/SSL (Handshake, Zertifikate, symmetrische Sitzungsschlüssel)
    
- Trennung von Authentifizierung (Identitätsnachweis) und Autorisierung (Rechteprüfung)
    

## 2. PowerShell-Grundlagen

- Objektorientierte Shell + Skriptsprache, Cmdlet-Schema Verb-Substantiv
    
- Pipeline übergibt .NET-Objekte, nicht Text – automatisierbare Auswertung
    
- Remoting via WinRM; Desired State Configuration (DSC); Modul-System, Fehlerbehandlung
    

## 3. ISO/OSI-Schichten & TCP/IP

- 7-Schichten-Modell vs. 4-Schichten-TCP/IP
    
- Typische Protokolle je Ebene (Ethernet, IP, TCP/UDP, HTTP …)
    
- Encapsulation, MTU, Fragmentierung, Ports
    

## 4. IP-Adressierung & Subnetting

- IPv4 (32-Bit), private Netze, Loopback, APIPA
    
- CIDR-Notation, Variable Length Subnet Mask (VLSM), Magic-Number-Methode
    
- Subnetz- und Host-Berechnung, Broadcast-Adresse, Supernetting
    

## 5. Übertragungs- & Kabeltechnik

- Twisted Pair (UTP, STP, S/FTP) Cat 5–8, Glasfaser (LWL SM/MM), Koax
    
- PoE-Standards 802.3af/at/bt (Leistungsklassen)
    
- RJ45-Pinout (EIA/TIA 568 A/B), GBIC/SFP-Module, Medienkonverter
    
- Dämpfung ≤ 100 m Kupfer; Repeater/Switch/LWL für längere Strecken
    

## 6. Netzwerktechnik & Topologien

- Geräte: Hub, Switch (L2/L3), Router, WAP, Modem, Firewall, IDS/IPS
    
- Topologien: Bus, Ring, Stern, Mesh; Backbone-Segmente als performanter Kern
    

## 7. Sendearten, Ethernet & WLAN

- Ethernet (IEEE 802.3) – CSMA/CD; WLAN (802.11) – CSMA/CA
    
- WLAN-Sicherheit: SSID-Konzept, WPA2/3-PSK, 802.1X, MAC-Filter, Gäste-VLAN
    
- VLAN-Trunking (802.1Q), Spanning Tree, Link-Aggregation
    

## 8. Windows Server & Active Directory

- Rollenbasierte Installation (AD DS, DNS, DHCP, File, Hyper-V)
    
- AD-Struktur: Domäne, OU, Objekte; Sites; FSMO-Rollen; Replikation
    

## 9. Dateidienste & Freigaben

- NTFS- vs. Freigaberechte; DFS Namespaces, Quotas, Auditing
    

## 10. DHCP & DNS

- DHCP-Prozess DORA, Scopes, Optionen, Failover, Reservations
    
- DNS-Hierarchie, Zonen, RR-Typen (A, AAAA, CNAME, MX, SRV), DNSSEC
    

## 11. Routing & Remote Access

- Statisches vs. dynamisches Routing (RIP, OSPF, BGP)
    
- NAT/PAT, VPN-Techniken (IPsec, IKEv2, WireGuard), DMZ-Konzepte
    

## 12. Netzwerk-Troubleshooting & Monitoring

- CLI-Tools: ping, tracert, netstat, nslookup, arp, iperf
    
- Vier-Stufen-Plan: Alarm → Untersuchung → Isolierung → Lösung
    
- SNMP, NetFlow/IPFIX, Syslog, SIEM-Integration
    

## 13. Software- und Systemhärtung

- Patch-Management, Application Whitelisting, Sandbox-Tests
    
- Secure Baseline, Hardening Benchmarks (CIS, DISA STIGs), Supply-Chain-Risiken
    

## 14. Informationssicherheit vs. IT-Sicherheit

- IT-Sicherheit schützt digitale Systeme – Teilgebiet der umfassenden Informationssicherheit inklusive Prozesse & Organisation
    

## 15. Schutzziele der Informationssicherheit

|Kernziel|Bedeutung|Erweiterte Ziele|
|---|---|---|
|Vertraulichkeit|Schutz vor unbefugtem Zugriff|Pseudonymität, Verdecktheit|
|Integrität|Unveränderlichkeit & Korrektheit|Revisionsfähigkeit, Kontingenz|
|Verfügbarkeit|Ständige Nutzbarkeit von Systemen|Widerstandsfähigkeit|
|Authentizität|Echtheits- / Ursprungsnachweis|Nicht-Vermehrbarkeit|
|Nichtabstreitbarkeit|Handlungen nicht leugbar|Verbindlichkeit|

## 16. Defense-in-Depth (DiD)

- Mehrschichtige Verteidigung: physisch, technisch, administrativ
    
- Ebenen: Zugangskontrolle, Endpunktschutz, Perimeter, Monitoring, Awareness
    

## 17. Maßnahmen der Informationssicherheit

- Technisch: Firewalls, Verschlüsselung, Backup, Endpoint-Protection
    
- Organisatorisch: Richtlinien, Schulungen, ISMS-Prozesse
    

## 18. Bedrohungslandschaft & Angreifer

- Identitätsdiebstahl, Ransomware, APT, Supply-Chain-Angriffe
    
- Hacker-Typen: White-, Grey-, Black-Hat; Script-Kiddies; Insider
    

## 19. Sicherheitsbewusstsein

- Kontinuierliche Awareness-Programme, Phishing-Simulationen, Social-Engineering-Tests
    

## 20. Computer-Architektur Grundlagen

- Von-Neumann-Modell: ALU, CU, Register, Memory, I/O
    
- Systembus (Address-, Daten-, Steuerleitungen), Takt, Pipelining
    

## 21. Netzwerkanalyse mit Wireshark

- Live-Capture & PCAP-Auswertung, Display/Capture-Filter, Experteninfo
    
- Einsatz: Performance-Analyse, Incident-Response, Cloud-Monitoring
    

## 22. Datenspeicher & Einheiten

- Speichermedien: magnetisch (HDD, Tape), optisch (CD/DVD/BD), Halbleiter (SSD, NVMe, Flash)
    
- Speicherhierarchie: Register → Cache (L1/L2/L3) → RAM → SSD/HDD → Archiv (Tape/Cloud)
    
- Einheiten: Bit (b) → Byte (B) → KiB (1024 B) → MiB → GiB → TiB
    
- Übertragungsgrößen & Geschwindigkeit: Latenz (ms/µs), Durchsatz (MB/s, Gb/s)
    
- RAID-Konzepte (0, 1, 5, 6, 10), Speicher-Deduplizierung, Snapshots
    

## 23. Datenschutz-Grundverordnung

- Gilt für alle Verarbeitung personenbezogener Daten in der EU
    
- Grundprinzipien: Rechtmäßigkeit, Transparenz, Zweckbindung, Datenminimierung
    
- Betroffenenrechte: Auskunft, Berichtigung, Löschung, Widerspruch
    
- Bußgelder bis 20 Mio. € oder 4% des weltweiten Jahresumsatzes
    

## 24. Lage der IT-Sicherheit

- Aktuelle Bedrohungslandschaft: Ransomware-Wellen, Supply-Chain-Attacken, KI-gestützter Social Engineering
    
- Wachsende Relevanz von Cloud- und IoT-Sicherheit
    
- Regulatorische Entwicklungen: NIS2-Richtlinie, Cybersecurity Act
    

## 25. Funkfeldmessung

- Einsatzgebiete: WLAN-Site-Survey, Interferenz-Analyse, Planung von Funkzellen
    
- Messgeräte: Spektrumanalysatoren, WiFi-Scanner, Antennen
    
- Kennzahlen: RSSI, SNR, Interferenzpegel
    

## 26. Glasfaser-Werkzeuge

- Schneide- und Abisolierwerkzeuge (Stripping & Cleaving)
    
- Spleißgeräte (Fusion & mechanisch)
    
- Mess- und Prüfgeräte: OTDR, Lichtquellen, Leistungsmesser
    

## 27. Patchpanel

- Zentraler Verteiler für Kupfer- und LWL-Leitungen
    
- Rack-montiert, modulare Einsätze (RJ45, LC/SC)
    
- Kennzeichnung & Dokumentation für Fehlersuche
    

## 28. Media Access Control

- MAC-Adresse: 48-Bit-Hardwareadresse, weltweit einmalig
    
- Adresstypen: Unicast, Multicast, Broadcast
    
- ARP-Protokoll für IPv4 → MAC-Auflösung
    

## 29. Hash-Algorithmen

- Zweck: Integritätsnachweis, Passwort-Hashing, digitale Signaturen
    
- Typen: MD5 (veraltet), SHA-1 (eingeschränkt), SHA-2/3, BLAKE2
    
- Eigenschaften: Kollisionsresistenz, Vorbildresistenz