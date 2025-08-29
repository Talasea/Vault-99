### Naabu Scan-Ergebnisse 📋

Die Scans von Naabu auf die fünf Ziel-IPs haben eine Reihe von offenen Ports im TCP-Protokoll gefunden. Die Ergebnisse sind nach IP-Adresse gruppiert:

- **192.168.20.10**: 53, 80, 88, 135, 139, 389, 445, 464, 593, 636, 3269, 3389.
    
- **192.168.20.11**: 53, 88, 135, 139, 389, 445, 636, 3269, 3389.
    
- **192.168.20.12**: 53, 88, 135, 139, 389, 445, 464, 593, 636, 3268, 3269, 3389.
    
- **192.168.20.22**: 80, 135, 139, 445, 3389.
    
- **192.168.20.23**: 80, 135, 139, 445, 1433, 3389.
    

---

### Analyse und Einordnung 🕵️‍♂️

Die identifizierten offenen Ports weisen stark auf die Existenz einer Active Directory (AD) Umgebung hin. Die folgende Liste erklärt die Bedeutung der gefundenen Ports und deren Relevanz:

- **Ports 53 (DNS)**: DNS ist für die Namensauflösung und die Dienstsuche in einem AD-Netzwerk unerlässlich.
    
- **Port 88 (Kerberos)**: Kerberos ist das primäre Authentifizierungsprotokoll von AD. Dieser Port wird für die sichere Authentifizierung von Benutzern und Diensten verwendet.
    
- **Port 135 (RPC)**: Dies ist der RPC-Endpunkt-Mapper, ein kritischer Port, der von vielen Microsoft-Diensten für die Kommunikation verwendet wird.
    
- **Port 139 (NetBIOS Session Service)**: Dieser Port wird für SMB-Dienste über NetBIOS verwendet, die für die Freigabe von Dateien und Druckern in Windows-Netzwerken genutzt werden.
    
- **Port 389 (LDAP)**: Lightweight Directory Access Protocol (LDAP) ist der Standardprotokoll für Anfragen an Verzeichnisdienste wie AD. Er wird zum Abfragen und Modifizieren von Daten in einem Verzeichnisserver verwendet.
    
- **Port 445 (SMB)**: Server Message Block wird für die Freigabe von Dateien und Druckern verwendet, aber auch für die Authentifizierung zwischen Servern und Domain Controllern. SMB über Port 445 ermöglicht den Zugriff, ohne NetBIOS zu benötigen.
    
- **Ports 3268 und 3269 (Global Catalog)**: Diese Ports sind spezifisch für den globalen Katalog von AD. Port 3268 wird für unverschlüsselte Verbindungen und Port 3269 für verschlüsselte Verbindungen (LDAP over SSL) verwendet.
    
- **Port 3389 (RDP)**: Remote Desktop Protocol ermöglicht den Fernzugriff auf die Systeme.
    
- **Port 5985 & 5986 (WinRM)**: Windows Remote Management (WinRM) wird für die Remote-Verwaltung verwendet. Port 5985 für unverschlüsselte und Port 5986 für SSL/TLS-verschlüsselte Kommunikation.
    

---

### Schlussfolgerung 🎯

Die Ergebnisse des Naabu-Scans zeigen, dass eine Vielzahl von Ports, die für Active Directory-Dienste kritisch sind, auf den Ziel-IP-Adressen offen sind. Dies bestätigt die Vermutung, dass es sich um eine Windows-basierte Domain-Controller-Umgebung handelt. Die erfassten Informationen sind eine solide Grundlage für weitere Schritte im Penetrationstest, wie die Enumeration von Diensten, die Ausnutzung von bekannten Schwachstellen oder die Durchführung von Brute-Force-Angriffen auf die gefundenen Dienste.

