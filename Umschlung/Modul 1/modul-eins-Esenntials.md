# Modul Eins – Kompaktwissen IT-Infrastruktur

## 1. Netzwerksicherheit & Authentifizierung
* Kennwort-, Zwei-Faktor-, Token-, Biometrische und Transaktionale Authentifizierung
* CAPTCHA und Single-Sign-On als ergänzende Schutzmaßnahmen
* Authentifizierungs­protokolle: Kerberos (Ticket-basiert mit KDC) und TLS/SSL (Handshake, Zertifikate, symmetrischer Sitzungsschlüssel)
* Trennung von Authentifizierung (Identitätsnachweis) und Autorisierung (Rechteprüfung)

## 2. PowerShell Grundlagen
* Shell + Skriptsprache, arbeitet objektorientiert
* Cmdlets im Verb-Substantiv-Schema, Hilfe via `Get-Help`, Auflistung via `Get-Command`
* Pipeline übergibt Objekte, nicht Text
* Skripting: Parameter, Fehlerbehandlung, Module, Scheduling mit `Task Scheduler`, Remoting (WinRM)

## 3. ISO/OSI-Schichten & TCP/IP
* 7 Schichten: Physisch, Sicherung, Vermittlung, Transport, Sitzung, Darstellung, Anwendung
* TCP/IP-Referenzmodell fasst Schichten zusammen (Netzzugang, Internet, Transport, Anwendung)
* Typische Protokolle pro Schicht (Ethernet, IP, TCP/UDP, HTTP …)

## 4. IP-Adressierung & Subnetting
* IPv4 32-Bit, Klassen A/B/C, reservierte Bereiche (privat, Loopback, APIPA)
* Subnetzmaske trennt Netz- und Hostteil; CIDR-Notation /x
* Subnetting-Vorgehen (Magic Number, Berechnung von Netz-ID, Broadcast, Host-Range)

## 5. Übertragungs- & Kabeltechnik
* Twisted Pair (UTP, STP, Cat 5-8), Glasfaser (SM, MM), RJ-45-Pinning, PoE
* Dämpfung ≤ 100 m; längere Strecken via Switch/Repeater oder LWL

## 6. Netzwerktechnik & Topologien
* Netzwerkinfrastruktur = Hardware + Software + Dienste
* Netzwerkkarten mit eindeutiger MAC-Adresse (48-Bit)
* Netzgrößen: PAN, LAN, MAN, WAN, GAN

## 7. Sendearten & WLAN
* Ethernet (IEEE 802.3) – CSMA/CD; WLAN (802.11) – CSMA/CA
* Sicherheit: SSID, WPA2/3-PSK oder 802.1X, VPN, Firewall, IDS
* DNS & WINS für Namensauflösung

## 8. Windows Server & Active Directory
* Editionen, rollenbasierte Installation (AD DS, DNS, DHCP, File, Hyper-V)
* AD-Struktur: Domäne, OU, Objekte; FSMO-Rollen; Multimaster-Replikation
* Benutzer, Gruppen (RBAC, A-G-DL-P), Gruppenrichtlinien (GPO) – Verknüpfung, Vererbung, Filter

## 9. Dateidienste & Freigaben
* NTFS-Berechtigungen vs. Freigaberechte; Prinzip Least Privilege
* DFS, Quotas, Freigabeüberwachung und Auditing

## 10. DHCP & DNS
* DHCP-Prozess DORA, Scopes, Optionen, Failover
* DNS-Hierarchie (Root, TLD, SLD), Resource Records (A, AAAA, CNAME, MX, SRV)

## 11. Routing & Remote Access
* Statisches vs. dynamisches Routing (RIP, OSPF, EIGRP, BGP)
* NAT/PAT, VPN-Techniken (IPsec, IKEv2, OpenVPN, WireGuard), DMZ-Konzepte

## 12. Netzwerk-Troubleshooting & Monitoring
* CLI-Tools: `ipconfig`, `ping`, `tracert`, `netstat`, `nslookup`, `arp`, PowerShell-Cmdlets
* Vier-Stufen-Plan: Alarm → Untersuchung → Isolierung → Lösung
* Proaktives Monitoring, Log-Analyse, Incident-Management

## 13. Software- und System­härtung
* Vertrauenswürdige Quellen, Hash-Prüfung, Least Privilege bei Installation
* Patch-Management, Sandbox/VM-Tests, Rollback‐Strategien, Supply-Chain-Risiken

---
© 2025 Alex | Lernmodul für IT-Grundlagen