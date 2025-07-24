
- **Kommunikationsprotokolle:** Dazu gehören das Address Resolution Protocol (ARP), das Hypertext Transfer Protocol (HTTP), das Internet Protocol (IP), das Simple Mail Transfer Protocol (SMTP), das Transport Control Protocol (TCP) und das User Datagram Protocol (UDP).
- **Routing-Protokolle:** Dazu gehören das Border Gateway Protocol (BGP) und das Open Shortest Path First (OSPF).
- **Netzwerkmanagementprotokolle:** Dazu gehören das Domain Name System (DNS), das Dynamic Host Configuration Protocol (DHCP), das File Transfer Protocol (FTP), das Internet Control Message Protocol (ICMP), das Simple Network Management Protocol (SNMP) und Telnet.



## 1. Address Resolution Protocol (ARP)

[ARP](https://www.computerweekly.com/de/definition/ARP-Address-Resolution-Protocol) übersetzt [IP-Adressen](https://www.computerweekly.com/de/definition/IP-Adresse-Internet-Protokoll-Adresse) in [MAC-Adressen](https://whatis.techtarget.com/de/definition/MAC-Adresse-Media-Access-Control-Address) (Media Access Control) und umgekehrt, so dass [LAN](https://www.computerweekly.com/de/definition/LAN-Local-Area-Network)-Endpunkte miteinander kommunizieren können. ARP ist notwendig, weil IP- und MAC-Adressen unterschiedlich lang sind:

- [IPv4](https://www.computerweekly.com/de/tipp/IP-Adressen-und-Subnetze-Wie-man-IPv4-Subnetzmasken-mit-der-Host-Formel-berechnet)-Adressen bestehen aus 32 Bit
- [IPv6](https://www.computerweekly.com/de/definition/IPv6-Adresse)-Adressen haben eine Länge von 128 Bit
- MAC-Adressen – die physische Hardwareadresse eines Gerätes – bestehen aus zwölf Hexadezimalzahlen, unterteilt in sechs Paare.

Die Übersetzungen sind für eine ordnungsgemäße Gerätekommunikation erforderlich. ARP ist nicht jedes Mal nötig, wenn Geräte versuchen zu kommunizieren, da der [Host](https://www.computerweekly.com/de/definition/Host) des [LANs](https://www.computerweekly.com/de/definition/LAN-Local-Area-Network) die übersetzten Adressen in seinem ARP-Cache speichert. Deshalb erfolgt dieser Vorgang hauptsächlich dann, wenn neue Geräte dem Netzwerk beitreten.

![ARP übersetzt MAC- und IP-Adressen zwischen Endpunkten](https://www.computerweekly.com/rms/German/So-funktioniert-Address-Resolution-Protocol-ARP-deutsch_mobile.jpg)

Abbildung 1: ARP übersetzt MAC- und IP-Adressen zwischen Endpunkten.

## 2. Border Gateway Protocol (BGP)

[BGP](https://www.computerweekly.com/de/definition/BGP-Border-Gateway-Protocol) sorgt dafür, dass das Internet funktioniert. Dieses Routing-Protokoll steuert, wie Pakete die Router in einem [autonomen System](https://www.computerweekly.com/de/definition/Autonomes-System-AS) (AS) – einem oder mehreren Netzwerken, die von einer einzigen Organisation oder einem Provider betrieben werden – passieren und mit verschiedenen Netzwerken verbunden werden. BGP kann Endpunkte in einem LAN miteinander vernetzen, und es kann Endpunkte in verschiedenen LANs über das Internet miteinander verbinden.

Externes BGP leitet den Netzwerk-Traffic von verschiedenen autonomen Systemen ins Internet und umgekehrt. Außerdem steuert internes BGP den Netzwerk-Traffic zwischen Endpunkten innerhalb eines einzelnen AS.

![In diesem Diagramm wird auf den blauen Routern BGP ausgeführt, sodass der Traffic durch das Netzwerk eines Providers zum Kunden oder umgekehrt gelangen kann.](https://www.computerweekly.com/rms/German/BGP-im-Netzwerkdesign-deutsch_mobile.png)

Abbildung 2: In diesem Diagramm wird auf den blauen Routern BGP ausgeführt, sodass der Traffic durch das Netzwerk eines Providers zum Kunden oder umgekehrt gelangen kann.

## 3. Domain Name System (DNS)

[DNS](https://www.computerweekly.com/de/definition/Domain-Name-System-DNS) ist eine Datenbank, die den [Domain](https://www.computerweekly.com/de/definition/Domaene-Domain)-Namen einer Website enthält, über den Anwender auf die Website zugreifen. Außerdem enthält sie die dazugehörigen IP-Adressen, die Geräte zum Auffinden der Website nutzen.

DNS übersetzt den Domain-Namen in IP-Adressen, die im DNS enthalten sind. Server können DNS-Daten zwischenspeichern, was notwendig ist, um auf die Websites zuzugreifen. DNS umfasst auch das DNS-Protokoll, das sich innerhalb der IP-Suite befindet und die Spezifikationen beschreibt, die DNS zur Übersetzung und Kommunikation verwendet.

DNS ist wichtig, weil es den Benutzern schnell Informationen über sowie Zugang zu Remote-Rechnern und -Ressourcen im Internet liefern kann.

## 4. Dynamic Host Configuration Protocol (DHCP)

[DHCP](https://www.computerweekly.com/de/definition/DHCP-Dynamic-Host-Configuration-Protocol) weist Netzwerkendpunkten IP-Adressen zu, damit sie mit anderen Netzwerkendpunkten über IP kommunizieren können. Wenn ein Gerät zum ersten Mal einem Netzwerk mit einem DHCP-Server beitritt, [weist DHCP ihm automatisch eine neue IP-Adresse zu](https://www.computerweekly.com/de/tipp/So-konfigurieren-Sie-einen-Windows-DHCP-Server) und wiederholt dies jedes Mal, wenn ein Gerät seinen Standort im Netzwerk ändert.

Wenn ein Gerät eine Verbindung zu einem Netzwerk herstellt, findet ein DHCP-Handshake statt. Bei diesem Handshake kommunizieren das Gerät und der DHCP-Server anhand der folgenden Schritte:

1. Das Gerät stellt eine Verbindung her.
2. Der Server empfängt die Verbindung und stellt verfügbare IP-Adressen zur Verfügung.
3. Das Gerät fordert eine IP-Adresse an.
4. Der Server bestätigt die Adresse, um den Vorgang abzuschließen.

![DHCP-Handshakes erfolgen, wenn ein Gerät sich erstmalig mit einem Netzwerk verbindet.](https://www.computerweekly.com/rms/German/DHCP-Handshake-deutsch_mobile.png)

Abbildung 3: DHCP-Handshakes erfolgen, wenn ein Gerät sich erstmalig mit einem Netzwerk verbindet.

## **5. File Transfer Protocol (FTP)**

[FTP](https://www.computerweekly.com/de/definition/FTP-File-Transfer-Protocol) ist ein Client-Server-Protokoll, mit dem ein Client eine Datei anfordert und der Server sie zur Verfügung stellt. FTP läuft über [TCP/IP](https://www.computerweekly.com/de/definition/TCP-IP-Transmission-Control-Protocol-Internet-Protocol), eine Protokollsuite zur Kommunikation, und erfordert einen Befehlskanal und einen Datenkanal für die Kommunikation beziehungsweise den Austausch von Dateien. Clients fordern Dateien über den Befehlskanal an und erhalten über den Datenkanal den entsprechenden Zugriff, etwa um die Datei herunterzuladen, zu bearbeiten oder zu kopieren.

FTP ist nicht mehr ganz so populär, da die meisten Systeme inzwischen [HTTP](https://www.computerweekly.com/de/definition/HTTP-Hypertext-Transfer-Protocol) für das [File Sharing](https://www.computerweekly.com/de/definition/File-Sharing) nutzen. Trotzdem bleibt FTP ein gängiges Netzwerkprotokoll, wenn es um einen vertraulicheren Austausch von Daten geht, zum Beispiel im Bankwesen.

## **6. Hypertext Transfer Protocol (HTTP)**

Wie FTP ist auch HTTP ein Filesharing-Protokoll, das über TCP/IP läuft, obwohl HTTP in erster Linie per Webbrowser funktioniert und den meisten Nutzern allgemein bekannt ist. Wenn ein Anwender auf eine Website-Domäne zugreifen will, ermöglicht HTTP den Zugriff. HTTP stellt eine Verbindung zum Domain-Server her und fordert den [HTML](https://www.computerweekly.com/de/definition/Hypertext-Markup-Language-HTML)-Code der Webseite an, das heißt, den Code, der das Design der Seite strukturiert und anzeigt.

Eine Variante von HTTP nennt sich [HTTPS](https://www.computerweekly.com/de/definition/HTTPS-Hypertext-Transfer-Protocol-Secure). Die Abkürzung steht für _HTTP over Secure Sockets Layer_ oder _HTTP Secure_. HTTPS kann die HTTP-Anfragen eines Nutzers und Webseiten verschlüsseln. Dies bietet den Anwendern mehr Sicherheit und kann übliche Bedrohungen der Cybersicherheit, etwa [Man-in-the-Middle-Angriffe](https://www.computerweekly.com/de/definition/Man-in-the-middle-Angriff-MITM-Angriff), verhindern.

![Das HTTP-Protokoll ermöglicht es den Benutzern, auf die verschiedenen Komponenten innerhalb der Domäne einer Website zuzugreifen.](https://www.computerweekly.com/rms/German/Wie-HTTP-funktioniert-deutsch_mobile.png)

Abbildung 4: Das HTTP-Protokoll ermöglicht es den Benutzern, auf die verschiedenen Komponenten innerhalb der Domäne einer Website zuzugreifen.

## 7. Internet Control Message Protocol (ICMP)

[ICMP](https://www.computerweekly.com/de/definition/Internet-Control-Message-Protocol-ICMP) ist ein Protokoll der Vermittlungsschicht (Network Layer), das für Fehlerbehandlung, Diagnose und Kontrollmeldungen zwischen Netzwerkgeräten verwendet wird. Es hilft bei der Identifizierung von Netzwerkverbindungsproblemen und bei der Verwaltung des Datenpaketflusses. Es werden keine Daten übertragen.

Sowohl [Ping als auch Traceroute](https://www.computerweekly.com/de/antwort/Mit-Ping-und-Traceroute-Breitbandverbindungen-auf-Paketverlust-testen) verwenden ICMP, um die Konnektivität zu testen und Paketrouten zu verfolgen. Übliche ICMP-Nachrichten sind

- Echo Request und Echo Response
- Ziel nicht erreichbar
- Zeitüberschreitung
- Redirect Nachricht

## **8. Internet Protocol (IP)**

[IP](https://www.computerweekly.com/de/definition/Internet-Protocol-IP) funktioniert ähnlich wie die Post. Wenn Benutzer Daten an ein Gerät senden oder von ihm empfangen, werden die Daten in Pakete aufgeteilt, die wie Briefe mit zwei IP-Adressen aussehen: eine für den Absender und eine für den Empfänger.

Nachdem der Absender das Paket verschickt hat, geht es zu einem [Gateway](https://www.computerweekly.com/de/definition/Gateway). Dieses leitet, wie ein Postamt, das Paket in die richtige Richtung weiter. Die Pakete werden so lange per Gateways weitergeleitet, bis sie schließlich ihr Ziel erreichen.

IP wird üblicherweise mit [TCP](https://www.computerweekly.com/de/definition/TCP-Transmission-Control-Protocol) zu TCP/IP kombiniert. Beide zusammen bilden die Internetprotokollsuite. Die Arbeitsteilung funktioniert folgendermaßen: IP sendet Pakete an ihr Ziel, und TCP ordnet die Pakete in der korrekten Reihenfolge an. Das ist erforderlich, da IP manchmal Pakete in der falschen Reihenfolge sendet, um sicherzustellen, dass die Pakete auf dem schnellsten Weg übertragen werden.

## 9**. Open Shortest Path First (OSPF)**

[OSPF](https://www.computerweekly.com/de/definition/OSPF-Open-Shortest-Path-First) arbeitet mit IP zusammen, um Pakete an ihr Ziel zu befördern. IP versucht, Pakete auf dem schnellstmöglichen Weg zu übermitteln, was OSPF realisieren soll. OSPF ermittelt den kürzesten – oder schnellsten – Weg für Pakete anhand des Shortest-Path-First-Algorithmus. Zudem aktualisiert das Protokoll [Routing-Tabellen](https://www.computerweekly.com/de/definition/Routing-Tabelle-Routing-Table) – ein Regelsatz, der bestimmt, welchen Weg Pakete nehmen – und warnt Router vor Änderungen in der Routing-Tabelle oder im Netzwerk, wenn eine Änderung eintritt.

OSPF ähnelt dem Routing Information Protocol ([RIP](https://www.computerweekly.com/de/definition/Routing-Information-Protocol-RIP)) und unterstützt es. RIP steuert den Traffic basierend auf der Anzahl der [Hops](https://www.computerweekly.com/de/definition/Hop), die er auf einer Route zurücklegen muss. In vielen Netzwerken hat OSPF bereits RIP ersetzt. OSPF wurde als schlankere und besser skalierbare Alternative zu RIP entwickelt. Beispielsweise verschickt RIP alle 30 Sekunden aktualisierte Routing-Tabellen. OSPF hingegen sendet sie nur bei Bedarf und nimmt Aktualisierungen nur an dem Teil der Tabelle vor, in dem die Änderung aufgetreten ist.

![RIP kann feststellen, dass der Traffic über Router C sein Ziel mit weniger Hops erreicht. RIP und OSPF funktionieren auf ähnliche Weise.](https://www.computerweekly.com/rms/German/Routing-Information-Protocol-RIP-deutsch_mobile.png)

Abbildung 5: RIP kann feststellen, dass der Traffic über Router C sein Ziel mit weniger Hops erreicht. RIP und OSPF funktionieren auf ähnliche Weise.

## **10. Simple Mail Transfer Protocol (SMTP)**

[SMTP](https://www.computerweekly.com/de/definition/Simple-Mail-Transfer-Protocol-SMTP) ist das bekannteste E-Mail-Protokoll. Es ist Teil der TCP/IP-Suite und steuert, wie E-Mail-Clients die E-Mail-Nachrichten der Benutzer versenden. E-Mail-Server verwenden SMTP, um E-Mail-Nachrichten vom Client über den E-Mail-Server an den empfangenden E-Mail-Server zu senden. Allerdings steuert SMTP nicht, wie E-Mail-Clients Nachrichten empfangen – sondern lediglich, wie Clients Nachrichten senden.

Infolgedessen benötigt SMTP andere Protokolle, um zu gewährleisten, dass E-Mails ordnungsgemäß gesendet und empfangen werden. SMTP kann mit [POP3](https://www.computerweekly.com/de/definition/Post-Office-Protocol-3-POP3) (Post Office Protocol 3) oder [IMAP](https://www.computerweekly.com/de/definition/Internet-Message-Access-Protocol-IMAP) (Internet Message Access Protocol) zusammenarbeiten, die steuern, [wie ein Mail-Server E-Mail-Nachrichten empfängt](https://www.computerweekly.com/de/feature/Mit-E-Mail-Security-Gateways-die-Sicherheit-optimieren).

## 11. Simple Network Management Protocol (SNMP)

[SNMP](https://www.computerweekly.com/de/definition/SNMP-Simple-Network-Mangement-Protocol) ist ein Netzwerkmanagementprotokoll, das Administratoren bei der Verwaltung und Überwachung von Netzwerkgeräten unterstützt. Es sammelt Geräteinformationen, um die Leistung und den Zustand des Netzwerks zu überwachen. Netzwerkadministratoren nutzen SNMP häufig, um Netzwerkprobleme zu erkennen und zu beheben.

SNMP verwendet ein Manager-Agent-Modell und die folgenden Komponenten: 

- **SNMP-Manager**, der mit den Agenten kommuniziert und Informationen abfragt oder aktualisiert.
- SNMP-Agent, der auf Geräten installiert wird und Informationen an den Manager sendet.
- **Management Information Base** ([MIB](https://www.computerweekly.com/de/definition/MIB-Management-Information-Base)), die als Datenbank fungiert und Geräteinformationen enthält.

## 12. Telnet

[Telnet](https://www.computerweekly.com/de/definition/Telnet) ist für Remote-Konnektivität ausgelegt und stellt Verbindungen zwischen einem Remote-Endpunkt und einem Host-Rechner her, um eine Remote-Sitzung zu ermöglichen. Telnet fordert den Benutzer am Remote-Endpunkt auf, sich anzumelden. Nach der erfolgreichen [Authentifizierung](https://www.computerweekly.com/de/definition/Authentifizierung) gewährt es dem Endpunkt Zugriff auf Netzwerkressourcen und Daten auf dem Host-Computer.

Telnet existiert seit den 1960er Jahren und stand vermutlich Pate für das moderne Internet. Allerdings mangelt es Telnet an ausgeklügelten Sicherheitsvorkehrungen, die für moderne Kommunikation und Technologie erforderlich sind. Aus diesem Grund kommt es nicht mehr allzu häufig zum Einsatz.

## **13. Transmission Control Protocol (TCP)**

TCP ist der erste Teil der TCP/IP-Protokollsuite und ordnet die Pakete in der richtigen Reihenfolge an, sodass IP sie zustellen kann. Insbesondere nummeriert TCP die einzelnen Pakete, weil IP Pakete über verschiedene Routen an ihr Ziel senden kann, ohne sich um die Reihenfolge zu kümmern. Daher greift TCP ein, bevor IP die Pakete zustellt.

TCP erkennt zudem Fehler beim Sendevorgang – etwa wenn Pakete basierend auf dem TCP-Nummerierungssystem fehlen – und weist IP an, diese Pakete erneut zu übertragen, bevor IP die Daten an ihr Ziel liefert. Durch diesen Prozess steuert und kontrolliert die TCP/IP-Suite die Kommunikation über das Internet.

![Die Hauptunterschiede zwischen TCP und UDP sind die Paketreihenfolge und die Anwendungsfälle.](https://www.computerweekly.com/rms/German/Die-Unterschiede-zwischen-TCP-und-UDP-deutsch_mobile.png)

Abbildung 6: Die Hauptunterschiede zwischen TCP und UDP sind die Paketreihenfolge und die Anwendungsfälle.

## **14. User Datagram Protocol (UDP)**

[UDP](https://www.computerweekly.com/de/definition/UDP-User-Datagram-Protocol) ist eine Alternative zu TCP und arbeitet auch mit IP zusammen, um zeitkritische Daten zu übertragen. UDP ermöglicht Datenübertragungen mit geringer [Latenz](https://www.computerweekly.com/de/definition/Latenz) zwischen Internetanwendungen. Somit eignet sich dieses Protokoll ideal für Voice over IP ([VoIP](https://www.computerweekly.com/de/definition/VoIP-Voice-over-IP-IP-Telefonie)) oder andere Audio- und Videoanforderungen.

Im Gegensatz zu TCP wartet UDP nicht darauf, dass alle Pakete ankommen, und kümmert sich auch nicht um deren korrekte Reihenfolge. Stattdessen überträgt UDP alle Pakete ohne Rücksicht darauf, ob sie auch wirklich ankommen.

UDP übermittelt ausschließlich Pakete, während TCP die Pakete überträgt, organisiert und sicherstellt, dass sie auch ankommen. Zwar arbeitet UDP schneller als TCP, ist aber auch weniger zuverlässig.