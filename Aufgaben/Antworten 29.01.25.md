.

Aufgabe 29.01.25

  

  

Teil 1

  

1. Erkläre möglichst umfassend: Was verstehst du unter einem DHCP- Server?

  

Der DHCP-Server spielt eine zentrale Rolle in der Netzwerkinfrastruktur, indem er die Konfiguration von Clients automatisiert und somit die Administration von Netzwerken erheblich vereinfacht.

Ein DHCP Server kann ein Netzwerkgerät (Hardware) oder auch eine Software lösung sein ,

die für die automatische Konfiguration von Netzwerkkommunikationsparametern für Clients zuständig ist

  

- Automatische IP-Adresse Zuweisung: Der DHCP-Server stellt IP-Adressen für Clients bereit, die sich im Netzwerk befinden. Diese Zuweisung erfolgt dynamisch, was bedeutet, dass die Clients nicht manuell konfiguriert werden müssen.
    
- Weitere Konfigurationsparameter: Neben der IP-Adresse können auch andere wichtige Netzwerkkonfigurationen wie Subnetzmaske, Gateway und DNS-Serveradressen automatisch von dem DHCP-Server bereitgestellt werden.
    
- DORA-Prozess: Die Kommunikation zwischen Client und DHCP-Server erfolgt über den sog. DORA-Prozess (Discover, Offer, Request, Acknowledge). In diesem Vier-Schritte-Prozess sendet der Client eine Anfrage an den DHCP-Server, der dann eine IP-Adresse und andere Konfigurationsdaten anbietet und bestätigt.
    
- Ausschlussbereiche: Der DHCP-Server kann bestimmte IP-Adressbereiche ausschließen, um sicherzustellen, dass statisch zugewiesene IP-Adressen nicht von ihm überschrieben werden.
    
- Reservierungen: Es ist möglich, spezifische IP-Adressen für bestimmte Geräte zu reservieren, sodass diese immer dieselbe IP-Adresse erhalten.
    
- Sicherheitsaspekte: Ein DHCP-Server kann potenziell zum Ziel von Angriffen werden, die dazu führen können, dass Clients ungültige Konfigurationen erhalten oder dass der Netzwerkverkehr manipuliert wird.
    
- **DHCPv6**: Für IPv6-Netzwerke gibt es eine erweiterte Version des Protokolls, DHCPv6, die zusätzliche Funktionen wie integrierte Sicherheitsfunktionen und die Möglichkeit bieten, weitere Konfigurationsdetails per DHCPv6 zu übertragen.
    

  

2. Erkläre: Was ist ein DNS- Server (FunkƟon, Auĩau, …)

  

  

  

  

![](file:///C:/Users/User/AppData/Local/Temp/lu92041ihw00.tmp/lu92041ihw0j_tmp_cdd8c8a7.png)  

  

  



  

Ein DNS-Server (Domain Name System)ist ein Server, der eine Verbindung zwischen einer Domain (zum Beispiel www.heise.de) und der zugehörigen IP-Adresse herstellt. Diese Funktion ist vergleichbar mit einem klassischen Telefonbuch , das Domainnamen in IP-Adressen umwandelt und umgekehrt.

  

  

Der DNS-Prozess beginnt, wenn wir eine URL in einem Browser eingibt.

Die Anfrage wird an einen DNS-Resolver gesendet, der in der Regel der DNS-Server des Internet Service Providers (ISP) ist.

Der Resolver leitet die Anfrage an verschiedene DNS-Server weiter,

bis die IP-Adresse der angefragten Domain gefunden wird.

Diese IP-Adresse wird dann an den Browser zurückgesendet, sodass dieser die Anfrage an den richtigen Server richten kann

  

  

Es gibt verschiedene Arten von DNS-Servern:

- **Autoritative DNS-Server**: Speichern gesicherte Domain-Informationen über eine bestimmte Zone im Domain-Namen-Space in ihrer DNS-Datenbank. Für jede Zone gibt es mindestens einen solchen Server, der als Master-System fungiert, während weitere als Slave-Systeme fungieren, um Redundanz und Ausfallsicherheit zu gewährleisten.
    
- **Nicht-autoritative DNS-Server**: Nutzen DNS-Informationen nicht aus der eigenen Zonendatei, sondern aus zweiter oder dritter Hand, wenn sie die Anfrage nicht direkt beantworten können.
    

  

  

DNS-Server bieten verschiedene Funktionen, wie z.B. die Sicherheit von Netzwerken durch die Gewährleistung, dass nur autorisierte Benutzer auf bestimmte Ressourcen zugreifen können.

  

  

Ein DNS-Server hat zwei wichtige Zonen: die Forward-Zone und die Reverse-Zone.

Die Forward-Zone dient dazu, Domainnamen in IP-Adressen umzuwandeln. Sie enthält Informationen wie ‘A’-Records, die einem Domainnamen eine IPv4-Adresse zuweisen, und ‘AAAA’-Records, die einem Domainnamen eine IPv6-Adresse zuweisen.

Diese Zonendatei wird auf einem Server gespeichert und enthält auch SOA- und NS-Records, die die Zone definieren und die Verknüpfungen zu anderen Nameservern realisieren.

Die Reverse-Zone dient dem umgekehrten Vorgang, also der Auflösung von IP-Adressen in Domainnamen.

Sie verwendet ‘PTR’-Records, die einer IP-Adresse einen Domainnamen zuordnen.

Diese Zonendatei enthält ebenfalls SOA- und NS-Records, ähnlich wie die Forward-Zone.

  
  

Beide Zonen können auf demselben Server gehostet werden oder auf separaten Servern, je nach Bedarf und Architektur des eigenen Netzwerks.

  

![](file:///C:/Users/User/AppData/Local/Temp/lu92041ihw00.tmp/lu92041ihw0j_tmp_2083fe82.gif)  

Funktion eines DNS-Servers  
  
Ablauf einer DNS-Anfrage:  
1. Nutzer gibt eine URL ein (z. B. Www.heise.com).  
2. Der Client fragt den DNS-Resolver (oft der DNS-Server des Internetanbieters),  
ob er die IP-Adresse kennt.  
3. Falls die Adresse nicht im Cache ist, wird die Anfrage an andere DNS-Server weitergeleitet:  
Root-Nameserver → Kennt nur die Top-Level-Domain (.com, .de usw.)  
TLD-Nameserver (.com-Server) → Verweist auf den zuständigen Nameserver der Domain  
Autoritativer Nameserver (google.com-Server) → Gibt die tatsächliche IP-Adresse zurück  
4. Der DNS-Resolver speichert die IP-Adresse für zukünftige Anfragen und  
gibt sie an den Client weiter.  
5. Der Browser verbindet sich mit der IP-Adresse, und die Webseite wird geladen.

  

  

3. Was ist (Microsoft) Active Directory?

  

Active Directory (AD) ist ein Verzeichnisdienst von Microsoft,  
der in Windows Server-Umgebungen genutzt wird, um Benutzer,  
Computer, Gruppen, Geräte und Ressourcen innerhalb eines Netzwerks zentral zu  
verwalten und zu organisieren.  
  
Es dient als eine Art Datenbank und Steuerungssystem,  
mit dem Administratoren Berechtigungen vergeben,  
Gruppenrichtlinien durchsetzen und Zugriffe auf Netzwerkressourcen steuern können.  
  
  
Funktionen von Active Directory  
🔹 Benutzer- und Gruppenverwaltung  
Benutzerkonten verwalten (Anlegen, Ändern, Deaktivieren, Löschen)  
Gruppen erstellen und Berechtigungen zentral steuern  
🔹 Zentrale Authentifizierung und Autorisierung  
Single Sign-On (SSO) → Ein Benutzer muss sich nur einmal anmelden und  
erhält Zugriff auf mehrere Ressourcen  
Passwortverwaltung und MFA (Multi-Faktor-Authentifizierung) möglich  
🔹 Gruppenrichtlinien (Group Policy Objects, GPOs)  
Regeln für Computer und Benutzer durchsetzen (z. B. Passwortrichtlinien,  
Softwareeinschränkungen, Netzlaufwerke, Druckerzuweisungen)  
🔹 Netzwerkressourcen organisieren  
Zugriff auf Freigaben, Drucker, Ordner, Anwendungen und  
andere Ressourcen regeln Rechteverwaltung für Dateien und Ordner  
🔹 Domänenstruktur & Hierarchie  
Ermöglicht die Verwaltung mehrerer Standorte und Netzwerke mit einer zentralen Struktur  
  
  
Komponenten von Active Directory  
🔹 Active Directory Domain Services (AD DS)  
Herzstück von Active Directory  
Ermöglicht die Verwaltung und Authentifizierung von Benutzern und  
Geräten in einer Domäne  
🔹 Domain Controller (DC)  
Der Hauptserver in einer AD-Umgebung  
Speichert alle AD-Daten, authentifiziert Benutzer und verwaltet Gruppenrichtlinien  
🔹 LDAP (Lightweight Directory Access Protocol)  
Ein Protokoll, mit dem AD mit anderen Systemen (z. B. Linux) kommunizieren kann  
🔹 Kerberos & NTLM – Authentifizierungsmechanismen  
Kerberos: Sichere Authentifizierungsmethode für Windows-Netzwerke  
NTLM: Älteres, aber immer noch genutztes Protokoll für Anmeldevorgänge  
🔹 FSMO-Rollen (Flexible Single Master Operations)  
Bestimmte Server (Domain Controller) übernehmen kritische Rollen, z. B. Schema-Master,  
um Änderungen im AD durchzuführen  
  
  
Vorteile von Active Directory  
✅ Zentrale Benutzerverwaltung -> Keine lokale Benutzerverwaltung auf jedem  
einzelnen Rechner nötig  
✅ Single Sign-On (SSO) -> Benutzer müssen sich nur einmal anmelden  
✅ Erhöhte Sicherheit -> Durch Gruppenrichtlinien, MFA und Berechtigungsmanagement  
✅ Einfache Skalierbarkeit -> Neue Benutzer, Computer oder  
Ressourcen lassen sich einfach hinzufügen  
✅ Kompatibilität mit Cloud (Azure AD)  
  

  

  

  

4. Liste einige Befehle auf, um Netzwerk-Troubleshooting vornehmen zu können und erkläre sie.  
  
⚡️ ping 8.8.8.8  
Sendet ICMP-Pakete (Echo-Request) an eine Ziel-IP oder Domain.  
Prüft, ob das Gerät oder die Webseite erreichbar ist.  
Misst die Antwortzeit (Latenz).  
  
⚡️ traceroute 8.8.8.8 (Unix) bzw. tracert 8.8.8.8 (Windows)  
Zeigt alle Knotenpunkte (Hops) zwischen deinem Computer und dem Zielserver.  
Misst die Zeit für jeden Hop.  
Hilft herauszufinden, wo genau ein Verbindungsproblem besteht.  
  
⚡️ ifconfig (Unix) bzw. ifconfig (Windows)  
Zeigt die aktuelle IP-Adresse, Subnetzmaske, Gateway und DNS-Server.  
Hilft bei der Fehleranalyse, ob der PC eine korrekte IP-Adresse hat.  
  
⚡️ nslookup google.com  
Fragt den DNS-Server nach der IP-Adresse eines Domain-Namens.  
Hilft zu prüfen, ob das DNS korrekt arbeitet.  
  
⚡️ netstat -an  
Zeigt aktive Verbindungen, offene Ports und welche Programme sie nutzen.  
Nützlich, um versteckte Verbindungen oder Malware zu finden.  
  
⚡️ arp  
Zeigt die MAC-Adressen der verbundenen Geräte in deinem Netzwerk.  
Nützlich, um zu prüfen, ob sich unbekannte Geräte im Netzwerk befinden.  
  
⚡️ route print  
Zeigt die aktuelle Routing-Tabelle, die festlegt, wie Datenpakete  
durch das Netzwerk gehen.  
  
⚡️ telnet google.com 80  
Prüft, ob eine Verbindung zu einer bestimmten IP und einem bestimmten Port möglich ist.