
# Netztrennung und Network Access Control

Die Netztrennung ist oftmals ein unterschätztes Instrument in der IT-Sicherheit – kann aber bei guter und konsequenter Umsetzung das Sicherheitsniveau deutlich steigern.

Netzwerke sind die Grundvoraussetzung, um verschiedene Teilnehmer miteinander zu verbinden.  
Diese Infrastrukturen sind nicht selten über einen langen Zeitraum gewachsen. Schutzmaßnahmen wie [Firewall](https://www.prosec-networks.com/blog/firewall/), Antivirus oder regelmäßige Updates sind oftmals implementiert, werden aber heutigen Sicherheitsanforderungen nicht mehr gerecht.

## Was ist das Ziel einer Netztrennung?

Durch eine granulare Segmentierung des Netzwerkes und Abschottung der Segmente einer Firewall, soll das Sicherheitslevel angehoben, Angriffsflächen verringert, Ausbreitung von schadhaften Vorgängen verhindert und/oder deutlich verlangsamt werden (vgl. im Risikomanagment: „Risikoreduktion“). Eine Erkennung von Angriffen sollte durch eine Zonierung möglich sein sowie Zugriffe über Firewall-Systeme auf das notwendige beschränkt werden.

## Vorraussetzungen für das Umsetzen und Einführen

einer Netztrennung in neue und bestehende Netzwerkarchitekturen

Vorgehensweise: Bestandsaufnahme aller betroffenen Standorte, Bereiche und Geschäftsprozesse dokumentieren. So wird die gesamte Netzwerkinfrastruktur mit allen Netzteilnehmer sauber erfasst.

### Abgrenzung / Out-of-Scope

Das Konzept beschreibt einen möglichen technischen Ansatz, um das Netzwerk in verschiedene Segmente zu unterteilen. Tiefgreifende Konfigurationen werden nicht beschrieben. Desweiteren muss ein Berechtigungskonzept (aufbauorganisatorische Art des Unternehmens) vorliegen, anhand dessen Sicherheitszonen abgeleitet werden können.

### Besondere Randbedingungen und Restriktionen

Durch die Kombination von verschiedenen Technologien ist die Komplexität hoch.

Die verwendete Hard- und Software ist aufeinander abzustimmen.

### Umsetzungsrisiken

Bei nicht vorliegenden Abhängigkeiten oder fehlerhafter Dokumentation, auf dessen Basis beispielsweise Firewallregeln erstellt werden, kann es zur nicht Verfügbarkeit von Diensten für Benutzer kommen. Es besteht die Gefahr sich im Micro-Management zu verlieren.

Bei allen verwendeten System mit zentraler Bedeutung ist zu vermeiden, dass ein SPOF (Single Point of Failure) entsteht. Es wird empfohlen, die Verfügbarkeit dieser Systeme zusätzlich durch einen Servicevertrag mit dem Hersteller oder Dienstleister sicherzustellen.

Willst du als Penetration Tester durchstarten?

Qualifiziere dich mit unserem praxisorientierten Intensivkurs für deinen Traumjob!

[Zum Junior Penetration Tester Zertifikatslehrgang](https://www.prosec-networks.com/junior-penetration-tester/)

## Konzept - Voraussetzungen

### Netztrennung auf Layer 1 bis 7

Die Umsetzung einer Netztrennung findet auf allen Netzwerk-Layern statt. Daher ist es notwendig die jeweiligen Schichten der Netzwerkinfrastruktur zu betrachten.

|       |                    |             |                                    |                             |
| ----- | ------------------ | ----------- | ---------------------------------- | --------------------------- |
| **#** | **ISO/OSI**        | **TCP/IP**  | **Protokoll**                      | **System**                  |
| 7     | Anwendungen        | Anwendung   | SNMP, SMTP, http, DNS, DHCP, LDAP, | Firewall, NAC               |
| 6     | Darstellung        |             |                                    |                             |
| 5     | Sitzung            |             |                                    |                             |
| 4     | Transport          | Transport   | TCP, UDP                           |                             |
| 3     | Vermittlung-/Paket | Internet    | IP, ICMP                           | Router, L3-Switch, Firewall |
| 2     | Sicherung          | Netzzugriff | ARP                                | Switch, NAC                 |
| 1     | Bitübertragung     |             | Netzwerkkabel, Patchfeld           |                             |

Die Netzwerksegmentierung ist auf den “Nord-Süd-Datenverkehr” ausgerichtet – also den eingehenden und ausgehenden Datenverkehr für das Netzwerk.

Die Mikrosegmentierung führt eine weitere Schutzschicht für den „Ost-West-Datenverkehr“ ein – also den internen Datenverkehr wie Client zu Server, Server zu Server oder Anwendung zu Server. Hier werden die Segmente verkleinert – ein größeres Netzwerk wird in kleinere Netzsegmente unterteilt.

In einem prakmatischen Vergleich mit einer Burg, wäre die Netzwerksegmentierung der Verbund aus Mauern, Türmen und tiefen Wassergräben. Die Mikrosegmentierung stellt die Bogenschützen auf den Zinnen oder die Wachposten an den Türen und Toren zu wichtigen Bereichen dar. Diese Lösung verhindert ein ungewolltes eindringen.

### Berechtigungskonzept

Ein Berechtigungskonzept ist nicht zwingend erforderlich, jedoch kann hierüber festgestellt werden, welche Zugriffe benötigt werden, um daraus Sicherheitszonen für die Netztrennung ableiten zu können. Für die Erstellung eines Berechtigungskonzepts kann das Firmenorganigramm als Grundlage dienen.

![Berechtigung und Rolle in einer Netwerktrennung](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_2.webp)

### Sicherheitszonen

Eine Sicherheitszone ist ein Netzbereich, der von anderen Netzbereichen getrennt ist. Der Traffic in eine Zone hinein sowie aus einer Zone hinaus wird durch Sicherheitsmechanismen kontrolliert. Hierfür werden Firewalls auch in Kombination mit IPS/IDS Systemen eingesetzt. In Abhängigkeit des Schutzbedarfs, kann die Kommunikation innerhalb einer Zone eingeschränkt werden. Dies kann durch Privat-VLANs umgesetzt werden. Zonen können neben dem Berechtigungskonzept auch aus einem IP/VLAN-Konzept abgeleitet werden.

#### Beispiele für Zonen

##### Trusted-Zonen:

In Trusted Zonen werden ausschließlich bekannte Systeme mit einer bestimmten Konfiguration und einem bestimmten Zustand verwaltet. Durch Eigenschaften wie die Version der Betriebssystems, dem Patchlevel oder ob eine aktuelle End-Point-Protection vorhanden ist werden diese Systeme als vertrauenswürdig eingestuft.

##### DMZ-Zonen:

Über eine DMZ-Zone wird der Datenaustausch mit dem Internet geregelt. Die DMZ-Zone hat weder eine direkte Verbindung in das Internet noch in das Campusnetz. E-Mail-Gateway, Reverse-Proxy, WAF oder andere Sicherheitsgateways werden typischerweise in einer DMZ untergebracht.

##### Management-Zonen:

Management-Zonen beinhalten ausschließlich Systeme oder Dienste, die zur Bereitstellung und Verwaltung von IT-Infrastruktur verwendet werden. Da diese System i.d.R. als hoch sensitiv eingestuft sind, ist der Zugriff in diese Zone äußerst streng zu limitieren. Ein Zugriff aus dem Access-Bereich ist zu vermeiden.

#### Zonenmatrix

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
||   |**Ziel**|   |   |   |   |
|WAN|DMZ|Client|Server|MGMT|
|**Quelle**|WAN||X||||
|DMZ|X|X||X||
|Client||||X||
|Server|||X|X||
|MGMT|||||X|

### Verkabelung: Layer 1

Die Grundlage für den Betrieb von leistungsfähigen Netzwerken zur Übertragung von Daten und Sprache, ist die strukturierte Verkabelung. Hier sind die Anforderungen für mehrerer Jahrzehnte ebenso zu berücksichtigen wie Reserven und flexible Erweiterbarkeit, unabhängig von der genutzten Anwendung.

Strukturierte Gebäudeverkabelung

- standardisierte Komponenten
- hierarchische Netzwerk-Topologie (Stern, Baum, …)
- Empfehlungen für Verlegung und Installation einhalten
- standardisierte Mess-, Prüf- und Dokumentationsverfahren
- Unterstützung aller aktuellen und zukünftigen Kommunikationssysteme
- Kapazitätsreserve
- flexible Erweiterbarkeit
- Ausfallsicherheit durch redundante Verkabelung mit unterschiedlicher Wegeführung
- Einhaltung existierender Standards
- ausreichend bis zum Endpunkt dimensioniert

Bereits bei der Verkabelung können Netzbereiche, die nicht miteinander verbunden sein sollen, voneinander getrennt werden. Beispiel für Netzbereiche mit physikalischer Trennung:

- DMZ
- Netz für Storage-Systeme
- separates Netz für Vorstand, BR
- Hochsicherheitsbereiche bei KRITIS (z.B. Produktionsnetze oder ähnliches)

**Hinweis**: Auch bei der Auswahl der GBIC-Module (Gigabit Interface Converter) für die Anbindung der Switche und Firewalls untereinander, sind die Kabel-Typen und Längen zu berücksichtigen.

[![Lichtwellenleiter](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_3.webp)](https://de.wikipedia.org/wiki/Lichtwellenleiter%E2%80%83)

https://de.wikipedia.org/wiki/Lichtwellenleiter 

### Hierarchische Switch-Infrastrukturen (Layer 1 & 2)

Die Switche sind in unterschiedliche Klassen unterteilt und müssen für Ihre jeweilige Funktion ausgelegt sein. Für das Management der Switche ist ein separater IP-Adressbereich und ein eigenes VLAN auszuwählen. Es gibt unterschiedliche Architekturmodelle – abhängig von der Größe des Netzwerkes:

#### Dreistufige Architektur

![Dreistufige Architektur - Hierarchische Switch-Infrastrukturen](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_2-1.webp)

#### Zweistufige Architektur

![Zweistufige Architektur - Hierarchische Switch-Infrastrukturen](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_3-1.webp)

#### Beispiel für ein zweistufiges Modell

Switche, die Aufgrund ihrer Funktion nicht direkt angebunden sind, müssen über einen dedizierten Management Port verbunden werden. Das Management-Interface hat in diesem Fall eine andere IP-Adresse als der Switch intern. Der Switch kann über das Management-Interface nur administriert werden.

##### Core-Switche

- mehrfach redundante Anbindung untereinander
- Anbindung der Core-Firewall
- im Idealfall getrennte Wegstrecke der (Gebäude-) verkabelung
- redundante Netzteile

![Core-Switche](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_4.webp)

##### Workgroup-Switche

- Bereitstellung des Campus-Netzes für Netzteilnehmer
- redundante Anbindung an die Core-Switches
- ausreichende Anzahl an Access-Ports
- mittelfristige Erweiterungsmöglichkeiten berücksichtigen
- jeden Teilnehmer über einen eigenen Port anbinden
- PoE für Telefonie oder Kameras berücksichtigen
- ausreichend Ersatzgeräte bevorraten

![Workgroup-Switche Bereitstellung des Campus-Netzes für Netzteilnehmer, Netztrennung](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_5.webp)

##### Server-Switche

- werden über den Core-Switch angebunden
- Bereitstellung des Netzwerkes für die Serverinfrastruktur
- mehrfach redundante Anbindung an die Core-Switche
- redundante Netzteile

![Server-Switche - werden über den Core-Switch angebunden, Netztrennung](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_6.webp)

##### Data-Switche / SAN

- über MGMT-Port an Serverswitche angebunden
- keine direkte Verbindung ins Campus-Netz
- mehrfach redundante Anbindung
- redundante Netzteile

![Data-Switche über MGMT-Port an Serverswitche angebunden, Netztrennung](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_7.webp)

##### Virtueller Switch

Virtuelle Switche verbinden die virtuellen Netzwerkkarten von virtuellen Maschinen mit den physischen Netzwerkkarten der Hosts. Der Host kann mit einem dedizierten Speichernetz und über andere Ports mit einem Serverswitch aus dem Campusnetz verbunden sein.

##### DMZ

- über MGMT-Port an Serverswitche angebunden
- keine direkte Verbindung ins Campus-Netz
- redundante Anbindung
- redundante Netzteile

![DMZ über MGMT-Port an Serverswitche angebunden, Netztrennung](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_8.webp)

### Logische Segmente (Layer 2 & 3)

#### VLAN (Layer 2)

Über VLANs wird das Netzwerk logisch auf Layer 2 getrennt. Ein Switch wird mit VLANs in mehrere virtuelle Switche aufgeteilt – auch Switch übergreifend. Dabei wird ein 32-Bit Header vorangestellt, der auch die VLAN-ID (12 Bit) transportiert. Nur an Teilnehmer, eines bestimmten VLANs werden Pakete auf den Switchports übertragen. Technisch gesehen bilden VLANs separate Broadcast-Domains.

Es gibt verschiedenen Arten von VLANs:

##### Portbasierte VLANs (untagged)

Mit portbasierten VLANs werden physische Switche in mehrere logische Switche unterteilt. Alle Switch-Ports die einem VLAN zugeordnet sind, können untereinander kommunizieren.

|   |   |   |   |
|---|---|---|---|
||VLAN1|VLAN 2|VLAN 3|
|VLAN 1|O|–|–|
|VLAN 2|–|O|–|
|VLAN 3|–|–|O|

##### Tagged VLANs

Bei tagged VLANs können mehrere VLANs über einen einzelnen Switch-Port genutzt werden. Die einzelnen Ethernet Frames bekommen dabei Tags angehängt, in dem jeweils die VLAN-ID vermerkt ist zu dessen VLAN das Frame gehört.

##### Privat-VLANs

Private-VLANs beschränken die Kommunikation innerhalb eines VLANs. Ein PVLAN enthält Switch-Ports, die so eingeschränkt sind, dass sie nur mit einem bestimmten Uplink-Port oder einer Link Aggregation Group (LAG) kommunizieren können. Der Uplink-Port oder die LAG ist in der Regel mit einem Switch, einem Router oder einer Firewall verbunden.

Im Gegensatz zu einer Trennung durch VLANs wird die Kommunikation in einem PVLAN zwischen bestimmten Ports im gleichen VLAN verhindert.

Porttypen von PVLAN:

- Isolated Ports
- Promiscuous Ports
- Community Ports (mit Community n)

Isolated Ports können nur mit dem Promiscuous Port kommunizieren. Promiscuous Ports können zu allen Ports kommunizieren. Community Ports (n) können zum Promiscuous und den eigenen Community Ports kommunizieren.

|   |   |   |   |   |
|---|---|---|---|---|
||Isolated|Promiscuous|Community (1)|Community (2)|
|Isolated|–|O|–|–|
|Promiscuous|O|O|O|O|
|Community (1)|–|O|O|–|
|Community (2)|–|O|–|O|

#### IP-Konzept (Layer 3)

Über das IP-Protokoll wird das Netzwerk auf Layer-3 in Segmente aufgeteilt. Hier werden Systeme nach Funktion, Standort oder anderen Kriterien zusammengefasst oder aufgeteilt. Beispielsweise kann im zweiten Oktett nach Standort und im dritten Oktett nach Funktion unterschieden werden: 172.Standort.Funktion.x.

Es ist darauf zu achten, dass die Host-Range ausreichend bemessen wird, um auch ein mittelfristiges Wachstum zu ermöglichen. Auch eine sinnvolle Ergänzung um zusätzliche Segmente muss berücksichtigt werden. Die IP-Adressvergabe kann statisch, dynamisch oder dynamisch mit Reservierung erfolgen. Bei der Reservierung erhält ein Netzteilnehmer immer dieselbe IP-Adresse.

#### Beispiel für ein IP und VLAN Konzept

Für unterschiedliche Anwendungsfälle sind IP-Bereiche definiert. Pro Anwendungsfall ist ein VLAN definiert. Netze, die ein hohes Schadenspotential bieten, werden durch PVLANs zusätzlich gesichert, indem die Teilnehmer untereinander isoliert werden.

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|**Name**|**Host-Range**|**Mask**|**Gateway**|**Dynamisch**<br><br>**/ statisch**|**VLAN-ID**|
||**172.16.x.x**||||Default (1)|
||_172.16.0.1 – 172.16.3.254_|||||
|Server (AD)|172.16.4.1 – 172.16.4.254|255.255.255.0 /24|172.16.4.1|statisch|1004|
|Server (Mail)|_172.16.5.1 – 172.16.5.254_|255.255.255.0 /24|172.16.5.1|statisch|105|
|Server (DB)|_172.16.6.1 – 172.16.6.254_|255.255.255.0 /24|172.16.6.1|statisch|106|
||_172.16.7.1 – 172.16.7.254_|||||
|Data|172.16.8.1 – 172.16.8.254|255.255.255.0 /24|172.16.8.1|statisch|108|
||_172.16.9.1 – 172.16.9.254_|||||
||_172.16.10.1 – 172.16.10.254_|||||
||_172.16.11.1 – 172.16.11.254_|||||
|Client|172.16.12.1 – 172.16.14.254|255.255.252.0 /22|172.16.12.1|dynamisch|1012 + 2012* (PVLAN)|
|Client|172.16.15.1 – 172.16.15.254|255.255.252.0 /22|172.16.12.1|statisch|1012 + 2012* (mit PVLAN)|
||_172.16.16.1 – 172.16.19.254_|||||
|Drucker Laser|172.16.20.1 – 172.16.20.254|255.255.255.0 /24|172.16.20.1|statisch|1020|
|Drucker Label|172.16.21.1 – 172.16.21.254|255.255.255.0 /24|172.16.21.1|statisch|1021|
||_172.16.22.1 – 172.16.22.254_|||||
||_172.16.23.1 – 172.16.23.254_|||||
|Peripherie|172.16.24.1 – 172.16.27.254|255.255.252.0 /22|172.16.24.1|statisch|1024|
||_172.16.28.1 – 172.16.31.254_|||||
|Telefonie|172.16.32.1 – 172.16.35.254|255.255.252.0 /22|172.16.32.1|dynamisch|1032|
||_172.16.32.1 – 172.16.35.254_|||||
||_172.16.36.1 – 172.16.39.254_|||||
|Prod.Systeme 1|172.16.40.1 – 172.16.43.254|255.255.252.0 /22|172.16.40.1|statisch|1040|
|Prod.Systeme 2|172.16.44.1 – 172.16.47.254|255.255.252.0 /22|172.16.44.1|statisch|1044|
|Prod.Systeme 3|172.16.48.1 – 172.16.51.254|255.255.252.0 /22|172.16.48.1|statisch|1048|
|Prod.Systeme 4|172.16.52.1 – 172.16.55.254|255.255.252.0 /22|172.16.52.1|statisch|1052|
|IoT|172.16.56.1 – 172.16.59.254|255.255.252.0 /22|172.16.56.1|statisch|1059|
||_172.16.60.1 – 172.16.63.254_|||||
|Fremdsysteme|172.16.64.1 – 172.16.64.254|255.255.255.0 /24|172.16.64.1|statisch|1064 + 2064* (mit PVLAN)|
|EOL-Systeme|172.16.65.1 – 172.16.65.254|255.255.255.0 /24||statisch|1065 + 2064*<br><br>(mit PVLN)|
|Transition|172.16.68.1 – 172.16.68.254|255.255.255.0 /24|172.16.68.1|dynamisch|1068|
|||||||
||**192.168.x.x**|||||
|DMZ|192.168.200.1 – 192.168.200.254|255.255.255.0 /24|192.68.200.1|statisch|200|
|Transfernetz 1|192.168.220.1 – 192.168.220.2|255.255.255.252 /30|–|statisch|220|
|Transfernetz 2|192.168.221.1 – 192.168.221.6|255.255.255.248 /29|–|statisch|221|
|MGMT|192.168.230.1 – 192.168.230.254|255.255.255.0 /24|192.68.230.1|statisch|230|

*Privat-VLAN

#### Besondere Netze:

##### Transfer-Netz

Ein Transfernetz verbindet i.d.R. zwei, in manchen Fällen auch mehrere Netzteilnehmer miteinander – z.B. ISP-Router und Perimeter-Firewall. Der Datenverkehr ist in einem Transfernetz so gesehen nur auf der Durchreise und wird nicht weiter behandelt.

Ein Transfernetz ist üblicherweise ein /30-Netz. In ein /30-Netz passen genau die beiden Hosts, die miteinander verbunden werden sollen.

##### Transition-Netz

Im Transition-Netz werden Netzteilnehmer untergebracht, die legitimiert sind, jedoch bestimmte Voraussetzungen nicht oder nicht mehr erfüllen. Diese Teilnehmer werden vom Regelbetrieb ganz oder teilweise, temporär oder dauerhaft ausgeschlossen.

**Beispiel:**

EPP-Version ist zu alt > Transition-Netz

EPP-Version wurde aktualisiert > Client-Netz

#### VRF - Virtual Routing and Forwarding

Über virtuelle Router kann eine zusätzliche Trennung auf Layer 3 eingerichtet werden. Hier werden auf einem physischen Routing-Device mehrere virtuelle Router betrieben. Auf einem Gerät werden voneinander getrennte Routinginstanzen betrieben. Eine Kommunikation zwischen den einzelnen Instanzen ist ohne explizites Routing nicht möglich.

#### Einfache Darstellung einer Netztrennung

![Einfache Darstellung einer Netztrennung​](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_9-1.webp)

Angriffsszenarien unter realistischen Bedingungen durchspielen?

Das kannst du ganz legal in unserem ganzheitlichen Hacking-Labor!

[Zum Junior Penetration Tester Kurs](https://www.prosec-networks.com/junior-penetration-tester/)

### Firewall (Layer 3 bis 7)

Über Firewalls wird eine Netzwerkzone vor einer anderen geschützt. Dabei wird nur benötigter und geprüfter Traffic über ein Regelwerk zugelassen. Durch UTM-Profile (Unified Threat Management) für Application-Control, IPS oder andere Mechanismen kann im Regelwerk die Sicherheit zusätzlich erhöht werden.

Empfehlung: 2-stufiges Firewall-Konzept

Bei einem 2-stufigen Firewall-Konzept trennt die Perimeter-Firewall das öffentliche vom internen Netz. Die Core-Firewall trennt die internen Netze voneinander und stellt die Verbindung zur Perimeter-Firewall her.

Im Idealfall sind beide Firewalls von verschiedenen Herstellern. Hierdurch wird vermieden, dass eine bekannte Schwachstelle ausreicht, um beide Firewalls zu überwinden. Zudem hat eine [Denial of Service](https://www.prosec-networks.com/blog/denial-of-service-attack/) Attacke aus dem öffentlichen Netz keine direkte Auswirkung auf die internen Systeme.

Verschiedene Hersteller setzen auf eine ASIC-basierte Architektur, die den Inhalt von Datenpaketen in Echtzeit analysiert und somit den Durchsatz beschleunigt.

#### Perimeter-Firewall

- High availability
- Anbindung ans WAN (ISP-Router)
- ausreichend Durchsatz bei IPsec-VPN
- Side-2-Side VPN
- Client-VPN: IP-Sec
- Unified Threat Management (AV, IPS, DLP, WEB-Filter, Mail, APP, DNS)
- Gateway und Router für alle externen Netze & DMZ

#### Core-Firewall

- High availability
- hoher Durchsatz auch bei Paket Inspektion
- Unified Threat Management (AV, IPS, DLP, WEB-Filter, Mail, APP, DNS)
- Proxy:
    - Transparent
    - Explicit
    - TLS- Inspection
- Anbindung per LWL und Kupfer
- Gateway und Router für alle internen Netze

#### Regelwerk

Im Regelwerk wird genau definiert, welcher Absender zu welcher Zieladresse mit welchem Protokoll Verbindungen aufbauen und Daten übertragen darf. Nicht erlaubter Traffic wird geblockt. Wünschenswert: Um die Nachvollziehbarkeit sicherzustellen, jegliche Kommunikation protokollieren.

![Regelwerk Absender Zieladresse Protokoll](https://www.prosec-networks.com/wp-content/uploads/elementor/thumbs/PSN_KB_netztrennung_13-qp96ep9zda7fjn1lvb4jms189nmxwx8wjp0mtsfei6.webp "PSN_KB_netztrennung_13")

#### Beispiel 2-stufiges Firewall-Konzept

![Beispiel 2-stufiges Firewall-Konzept als Netztrennung](https://www.prosec-networks.com/wp-content/uploads/PSN_KB_netztrennung_10-1.webp)

### IPS/IDS

Über [Intrusion Detection Systems](https://www.prosec-networks.com/blog/intrusion-detection-system/) (IDS) und Intrusion Prevention Systems (IPS) kann die Sicherheit zusätzlich erhöht werden. Über solche Systeme wird das Netzwerk kontinuierlich überwacht, Sicherheitsvorfälle erkannt oder verhindert. Die dazugehörigen Informationen werden protokolliert.

IPS (Intrusion Detection System) und IDS (Intrusion Prevention Systemen) sind häufig in UTM-Firewalls bereits integriert. Die Leistungsfähigkeit variiert je nach Hersteller und Firewall-Modell. In Abhängigkeit vom Datendurchsatz der Architektur, vor allem des Schutzbedarfs, ist eine dedizierte Lösung zu empfehlen.

### Application Layer Gateway Architecture (Layer 5-7)

#### Reverse Proxy

Ein Reverse Proxy leitet Anfragen aus dem Internet an einen internen Webserver weiter. Hierdurch wird der Webserver nur über eine definierte Zwischenstufe angesprochen. Eine direkte Kommunikation aus dem Internet Richtung Webserver ist so nicht möglich. Damit steigert der Reverse Proxy die Sicherheit von Webservern.

Über einen eigenen Cache kann der Reverse Proxy den Webserver entlasten. Zugriffe auf mehrere Webserver verteilt werden – Load Balancing.

#### Web Application Firewalls (WAF)

Ein weiterer Schutzmechanismus auf Anwendungsebene ist eine WAF. Ein- und ausgehender Traffic wird überwacht, analysiert, gefiltert oder blockiert. So werden Anwendungen beispielsweise vor Angriffen wie SQL Injection, Cross-Site Scripting (XSS) oder Cookie Poisoning geschützt.

WAF-Funktionalitäten sind häufig in UTM-Firewalls bereits integriert. In Abhängigkeit vom Datendurchsatz der Architektur und vor allem des Schutzbedarfs, ist eine dedizierte Lösung zu empfehlen.

### Network Access Control (NAC) (Layer 2 bis 7)

Ein NAC realisiert eine port-basierte Zugriffskontrolle im LAN und setzt über ein Regelwerk individuelle Sicherheitspolicies im gesamten Netzwerk durch. Als Ergänzung zu den gängigen Sicherheitssystemen wie Firewalls, Virenschutz oder Intrusion Detection Systeme ist das NAC ein wichtiger Baustein bei der Segmentierung von Netzwerken. Eine Voraussetzung für die Einführung eines NAC-Systems sind managed Switches.

Durch den Einsatz einer NAC können VLANs nicht nur statisch, sondern auch dynamisch eingesetzt werden. Die Flexibilität wird dadurch deutlich erhöht und der Konfigurationsaufwand verringert.

Aufgabe:

- Netzwerkzugangskontrolle
- dynamisches VLAN-Management
- Schutz vor unautorisierten Zugriffen
- Lokalisierung und Identifizierung aller Geräte im Netzwerk
- Aussperrung oder Isolierung von Fremdgeräten
- Angriffe auf Layer 2 (ARP-Poisoning, MAC-Flooding, IP-Spoofing etc.) erkennen, lokalisieren und abwehren
- Regelwerk

Bei der Planung ist zu definieren, welche Ports vom NAC aktiv gemanaged werden sollen. Ports von Core-, Data-, Server- oder DMZ-Switchen werden bevorzugt statisch konfiguriert, ebenso Uplink-Ports oder LAGs (Link Aggregation)

Im NAC-System werden Gruppen definiert – z.B. analog des IP-&VLAN-Konzepts. Anhand der Zugehörigkeit zu einer bestimmten Gruppe wird über ein Regelwerk bei einem definierten Ereignis (z.B: link up) der entsprechende Port auf dem Switch in das gewünschte VLAN verschoben. Bei _link down_ kann ebenfalls eine Aktion ausgelöst werden.

Unbekannte Teilnehmer können abgelehnt werden. Als Aktion kann hier der Port für einen bestimmten Zeitraum deaktiviert werden. Alternativ können unbekannte Teilnehmer auch einem isolierten Netzbereich mit einem Privat-VLAN zugewiesen werden.

Verschiedene NAC-Systeme sind in der Lage, während der Authentifizierung zu prüfen, ob Endgeräte einen bestimmten Sicherheitsstandard erfüllen. Kriterien können beispielsweise der Patch-Level des OS oder die Aktualität der EPP sein.

Geräte, die diese Anforderungen nicht erfüllen, können so lange isoliert werden, bis alle erforderlichen Voraussetzungen geschaffen sind. Erst dann erfolgt der Zugang zum regulären Netzbereich.

Network Access Control sollte nach Möglichkeit auch auf vSwitches realisiert werden.

### Netzteilnehmer

#### MAC-Adressen Authentifizierung

Die Netzteilnehmer werden eindeutig über die MAC-Adresse identifiziert. Idealerweise sind die MAC-Adressen bei neuen Netzteilnehmern vorab bekannt und werden im NAC-System eingepflegt und zugeordnet. Anhand der MAC-Adresse wird das entsprechende VLAN auf dem Access-Port geschaltet. Da MAC-Adressen manipuliert werden können, bietet dieser Ansatz nur einen einfachen Schutz.

#### IEEE 802.1X

Um das Sicherheitslevel weiter anzuheben, kann die zertifikatsbasierte Netzwerkzugangskontrolle IEEE 802.1x angewendet werden. Hier wird auf dem Client ein Zertifikat hinterlegt, welches er zur Anmeldung verwendet.

Der Aufwand für eine erfolgreiche IEEE 802.1X Implementierung ist nicht zu unterschätzen. Auch ist zu berücksichtigen, dass die Zertifikate vor dem Ablaufdatum zu ersetzen sind.

#### Fingerprint

Beim Fingerprint werden verschiedene Eigenschaften von einen Endgerät erfasst. Der so generierte Fingerprint wird zur eindeutigen Identifizierung (auch in Kombination mit der MAC-Adresse) des Endgerätes herangezogen.

Selbst für Endgeräte, die keine IEEE-802.1x-Unterstützung mitbringen, wie zum Beispiel Drucker, Webcams oder VoIP-Telefone, kann so eine sichere Identifizierung bewerkstelligt werden.

#### Interne Netzteilnehmer

Jeder interne Netzteilnehmer wird über einen eigenen Switchport in das Netzwerk eingebunden.

#### Externe Netzteilnehmer

Externe Netzteilnehmer sind über eine sichere Methode anzubinden. Die gebräuchlichste VPN-Technologie hierfür ist IPSec (Internet Protocol Security).

Eine gute Alternative zu IPSec ist die freie Software WireGuard. Die erste Version von WireGuard wurde unter Linux veröffentlicht. Mittlerweile ist WireGuard für verschiedene Betriebssysteme sowie als App für Android und iOS verfügbar.

Voraussetzungen:

- kein Split-Tunnel
- nur gemanagte Endgeräte zulassen
- Authentifizierung, z.B. gegen AD