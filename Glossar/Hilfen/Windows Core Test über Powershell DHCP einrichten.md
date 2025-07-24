SCconfig um in den isntaltions helfer zu kommen

### **DHCP, Active Directory (AD) & DNS auf Windows Server 2022 Core installieren – Schritt-für-Schritt-Anleitung**

Hier wird erklärt, wie du einen Windows Server 2022 Core als **Domain Controller (AD)**, **DNS-Server** und **DHCP-Server** einrichtest – komplett über PowerShell. Für Quereinsteiger sind mögliche Fehler und Lösungen hervorgehoben.

---

### **Voraussetzungen**

1. **Windows Server 2022 Core** installiert und mit Netzwerk verbunden.
    
2. **Statische IP-Adresse** für den Server (über PowerShell konfiguriert).
    
3. **Administratorrechte** (als lokaler Admin anmelden).

powershell -Command "Start-Process powershell -Verb runAs" als Admin über die cmd starten 

---

### **Schritt 1: Statische IP-Adresse festlegen**

Ohne statische IP funktionieren AD, DNS und DHCP nicht stabil.

powershell

Copy

# Netzwerkadapter-Name herausfinden (z. B. "Ethernet")
Get-NetAdapter

# Statische IP konfigurieren (Beispielwerte anpassen!)
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress "192.168.1.10" -PrefixLength 24 -DefaultGateway "192.168.1.1"
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "192.168.1.10"  # DNS auf sich selbst verweisen

**⚠️ Fehler & Lösungen:**

- **Fehler:** _"Default gateway is not reachable"_  
    Prüfe, ob der Gateway korrekt ist und der Server im gleichen Netzwerk liegt.
    
- **Tipp:** Nutze `Test-NetConnection 192.168.1.1`, um die Verbindung zum Gateway zu testen.
    

---

### **Schritt 2: Active Directory (AD) und DNS installieren**

AD und DNS sind eng verbunden. Der Server wird zum **Domain Controller** (DC).

#### **A. AD-Domain-Services und DNS installieren**

powershell

Copy

# AD-Rolle und DNS installieren
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
Install-WindowsFeature DNS -IncludeManagementTools

#### **B. Domain Controller einrichten**

powershell
I
Copy

# Neuen AD-Wald (Forest) erstellen (Beispielwerte anpassen!)
Install-ADDSForest `
  -DomainName "meine-domain.local" `
  -DomainNetbiosName "MEINEDOMAIN" `
  -InstallDns:$true `
  -SafeModeAdministratorPassword (ConvertTo-SecureString -String "SicheresPasswort123!" -AsPlainText -Force) `
  -Force:$true

**⚠️ Wichtig:**

- Nach der Ausführung **startet der Server automatisch neu**.
    
- **SafeModeAdministratorPassword** muss komplex sein (Groß-/Kleinbuchstaben, Zahlen, Sonderzeichen).
    
- **DomainName** darf keine Leerzeichen enthalten (z. B. `meine-domain.local`).
    

**🔴 Mögliche Fehler:**

- **Fehler:** _"Verbindung zum DNS-Server fehlgeschlagen"_  
    Stelle sicher, dass die DNS-Einstellung des Servers auf die eigene IP zeigt (Schritt 1).
    
- **Fehler:** _"Domain Name ist bereits vergeben"_  
    Wähle einen eindeutigen Domain-Namen oder demontiere einen bestehenden DC.
    

---

### **Schritt 3: DHCP-Server installieren und konfigurieren**

#### **A. DHCP-Rolle installieren**

powershell

Copy

Install-WindowsFeature DHCP -IncludeManagementTools

#### **B. DHCP-Server autorisieren**                                   
- **Get-ADDomainController**: Zeigt alle Domänencontroller in der aktuellen Domäne an.

powershell

Copy

# DHCP-Server in AD autorisieren
Add-DhcpServerInDC -DnsName "mein-server.meine-domain.local" -IPAddress 192.168.5.200

#### **C. DHCP-Scope erstellen**

powershell

Copy

# IP-Bereich (Scope) definieren
Add-DhcpServerv4Scope `
  -Name "Mein Netzwerk" `
  -StartRange 192.168.5.100 `
  -EndRange 192.168.5.199 `
  -SubnetMask 255.255.255.0 `
  -State Active

# DHCP-Optionen setzen (DNS, Router)
Set-DhcpServerv4OptionValue `
  -DnsServer 192.168.1.10 `
  -Router 192.168.1.1 brauchen wir in unserem fall nicht 

**⚠️ Fehler & Lösungen:**

- **Fehler:** _"DHCP-Server ist nicht autorisiert"_  
    Führe `Add-DhcpServerInDC` **als Enterprise-Admin** aus.
    
- **Fehler:** _Clients erhalten keine IP-Adressen_  
    Prüfe, ob der Scope **aktiviert** ist und der Server im richtigen Netzwerksegment liegt.
    

---

### **Schritt 4: Überprüfung der Dienste**

#### **A. AD und DNS testen**

powershell

Copy

# Domain-Controller-Status prüfen
Get-ADDomainController

# DNS-Auflösung testen
Resolve-DnsName -Name "mein-server.meine-domain.local"

#### **B. DHCP testen**

powershell

Copy

# Aktive DHCP-Leases anzeigen
Get-DhcpServerv4Lease -ScopeId 192.168.1.0

---

### **Häufige Probleme & Lösungen**


| **Problem**                          | **Lösung**                                                                          |
| ------------------------------------ | ----------------------------------------------------------------------------------- |
| **AD-Installation schlägt fehl**     | Prüfe die DNS-Einstellungen und ob der Server eine statische IP hat.                |
| **DNS-Abfragen funktionieren nicht** | Stelle sicher, dass die **Forwarder** im DNS-Server konfiguriert sind.              |
| **DHCP-Scope nicht aktiv**           | Aktiviere den Scope mit `Set-DhcpServerv4Scope -ScopeId 192.168.1.0 -State Active`. |
| **Firewall blockiert Dienste**       | Öffne die Ports für AD (TCP 389, 636), DNS (TCP/UDP 53) und DHCP (UDP 67/68).       |

---

### **Visuelle Übersicht der PowerShell-Befehle**

powershell

Copy

# Statische IP
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress "192.168.1.10" -PrefixLength 24

# AD und DNS installieren
Install-WindowsFeature AD-Domain-Services, DNS -IncludeManagementTools
Install-ADDSForest -DomainName "meine-domain.local" ...

# DHCP installieren
Install-WindowsFeature DHCP
Add-DhcpServerInDC -DnsName "mein-server.meine-domain.local"
Add-DhcpServerv4Scope -StartRange 192.168.1.100 -EndRange 192.168.1.200

---

### **Tipps für Quereinsteiger**

1. **Logs prüfen:** Nutze `Get-EventLog -LogName System`, um Fehler im Systemprotokoll zu finden.
    
2. **Firewall:** Deaktiviere die Firewall temporär zum Testen: `Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False`.
    
3. **Backup:** Erstelle vor kritischen Schritten einen Snapshot des Servers (falls virtualisiert).
    

Mit diesen Schritten hast du einen voll funktionsfähigen **Domain Controller mit DNS und DHCP**! 🎯  
Bei Fragen oder Fehlern: Überprüfe immer zuerst die **IP-Einstellungen**, **Firewall** und **Dienstestatus** (`Get-Service`).



server herunterfahren

Stop-Computer
Stop-Computer -Force  (zum erzwingen des Herunterfahrens)

