

Folgende Grundbegriffe kommen im Zusammenhang mit Kommunikationssysteme und Netzwerke immer wieder vor. Die Reihenfolge der Grundbegriffe hat didaktische Gründe, weshalb hier auf eine alphabetische Sortierung verzichtet wurde.


### LAN und WAN

Netzwerke unterscheidet man häufig in ihrer räumlichen und geografischen Ausdehnung. LAN ist die Abkürzung für Local Area Network. Damit wird oft ein lokal begrenztes Netzwerk bezeichnet, das je nach Organisationsgröße mehrere Tausend Teilnehmer umfassen kann. WAN ist die Abkürzung für Wide Area Network. Damit wird oft ein Weitverkehrsnetzwerk bezeichnet, dass dazu dient kleinere Netzwerke zu einem großen Netzwerk zusammenzuschalten.  
Das LAN ist über einen Router mit einem größeren Netzwerk, dem WAN, verbunden. Darüber ist in der Regel eine Verbindung ins Internet möglich.

- [LAN - Local Area Network](https://www.elektronik-kompendium.de/sites/net/0904021.htm)
- [WAN - Wide Area Network](https://www.elektronik-kompendium.de/sites/net/0908091.htm)

### Node

Ein Node ist ein allgemeiner Begriff für eine physikalisch vorhandene Komponente in einem Netzwerk. Es handelt sich um ein Gerät, dass an einem oder mehreren Netzwerken angeschlossen ist. Dazu verfügt es über eine oder mehrere Schnittstellen.  
Ein Node kann ganz allgemein ein Host, ein Client oder ein Server sein.

### Link

Ein physikalisches Netzwerk bezeichnet man manchmal auch als Link, was Verbindung bedeutet. Zu diesem Netzwerk gehören alle Nodes, die an dem selben Link angeschlossen sind bzw. die direkt miteinander verbunden sind.

### Site

Ein Netzwerk und die daran angeschlossenen Nodes bilden eine Site, wenn sie einer gemeinsamen und zusammenhängenden Verwaltung unterstellt sind.  
Dieser Begriff ist eher unüblich. Oft ist eine Site das lokale Netzwerk und wird als LAN bezeichnet.

### Host

Ein Host ist ein Node ohne Router-Eigenschaft, die damit eine Endstelle in einem Netzwerk darstellt. Typischerweise wird ein Client oder Server als Host bezeichnet.

### Knoten

Allgemein formuliert ist ein Knoten ein Verzweigungspunkt in einem Kommunikationsnetzwerk, an dem mehrere Verbindungen zusammenlaufen. Knoten sind im Telefonnetz die Vermittlungsstellen oder auch Telefonanlagen. In einem IP-Netzwerk sind Router und in einem Ethernet-Netzwerk sind Switche die Knoten.  
Zugangspunkte zu einem Netzwerk, z. B. WLAN-Access-Points, werden häufig auch als Knoten bezeichnet.

### Client

Ein Client ist ein Endgerät oder auch nur eine Software-Komponente, die von einer zentralen Stelle Dienste oder Daten anfordert oder über einen zentralen Zugang am Netzwerk teilnimmt. Der Client ist als Teil der Client-Server-Architektur in größere Zahl in allen Netzwerken zu finden.  
Typische Hardware-Clients sind PCs, Smartphones, Tablets und Notebooks. Auf diesen laufen dann mehrere Software-Clients für unterschiedliche Dienste. WWW, E-Mail, Messaging, usw.

- [Client-Server-Architektur](https://www.elektronik-kompendium.de/sites/net/2101151.htm)

### Server

Ein Server ist ein Computer, der Rechenleistung, Speicher, Daten und Dienste in einem Netzwerk bereitstellt und Zugriffsrechte verwaltet. Auf dem Server laufen mehrere Dienste und Anwendungen, die von anderen Netzwerk-Teilnehmern mit einem Software-Client über das Netzwerk angefordert werden.

- [Server](https://www.elektronik-kompendium.de/sites/net/0505081.htm)

### Router

Ein Router ist ein Node, der Pakete weiterleitet, die nicht an ihn selbst gerichtet sind. In einem dezentralen Netzwerk ist der Übertragungsweg der Datenpakete nicht fest vorgegeben. Genau genommen weiß niemand in einem dezentralen Netzwerk über alle Verbindungen Bescheid.  
Die einzelnen Router treffen bei jedem eingehenden Datenpaket erneut die Entscheidung, welchen Weg das Datenpaket geht.

- [Router](https://www.elektronik-kompendium.de/sites/net/1404181.htm)

### Routing

Die Art und Weise, wie Datenpakete in einem dezentralen Netzwerk oder IP-Netzwerk verarbeitet werden, bezeichnet man als Routing. Man könnte Routing auch als Wegfindung bezeichnen. Dabei wird der Weg zum Ziel anhand mehrerer Kriterien (metric) ermittelt. Je mehr Kriterien berücksichtigt werden müssen, desto genauer und gezielter ist der Weg zum Ziel. Aber desto (zeit-)aufwendiger ist die Bestimmung oder Berechnung des Wegs.  
In der Regel ist das maßgebliche Kriterium die Zieladresse und damit der kürzeste bzw. schnellste Weg zum Ziel. In gewisser Weise suchen sich die Datenpakete ihren Weg zum Empfänger selber. Beim Routing geht darum den optimalen Weg vom Sender zum Empfänger zu finden.  
Das maßgebliche Hilfsmittel beim Routing ist die Routing-Tabelle, in der mögliche Routen festgelegt sind.

- [Routing](https://www.elektronik-kompendium.de/sites/net/0810101.htm)
- [IP-Routing](https://www.elektronik-kompendium.de/sites/net/0903151.htm)

### Subnetz

Ein Subnetz ist ein oder mehrere LAN-Segmente, die durch Router begrenzt werden und das gleiche IP-Adresspräfix verwenden. Statt Subnetz sind auch die Begriffe Netzwerksegment oder Link gebräuchlich.

### Gateway

Ein Gateway ist eine Hardware oder Software oder eine Kombination daraus, die eine Schnittstelle zwischen zwei inkompatiblen Netzwerken darstellt. Das Gateway kümmert sich darum, dass die Form und Adressierung der Daten in das jeweilige andere Format oder Protokoll des anderen Netzes konvertiert werden.

- [Gateway](https://www.elektronik-kompendium.de/sites/net/0901111.htm)

### Bridge

Eine Bridge bzw. Netzwerkbrücke verbindet zwei Teilnetze, die auf der Schicht 1 und 2 des OSI-Schichtenmodells arbeiten. Für die Hosts im Netzwerk ist die Bridge transparent, sie können sie nicht sehen.

In den Anfangszeiten von lokalen Netzwerken mit Ethernet stand der Begriff Bridge für ein Gerät zur Kopplung zweier Ethernet-Segmente. Die Bridge war eine wichtige Komponente, um große lokale Netzwerke zu betreiben. Die Segmentierung begrenzt die Größen der Kollisions-Domänen und das Risiko einer Schleifenbildung.

Einen Switch kann man auch als Multiport-Bridge betrachten.

- [Bridge](https://www.elektronik-kompendium.de/sites/net/0901101.htm)

### Switching

Switching bedeutet, dass Verbindungen in einem Netzwerk aufgrund von Adressen geschaltet werden. In einem geswitchten Netzwerk bestimmt typischerweise die Empfängeradresse einen konstanten Pfad mit einer definierten Bandbreite, welchen Weg Datenpakete nehmen. Wenn ein Datenpaket abgeschickt wird, steht der Weg durch das Netzwerk praktisch schon fest.

- [Switching](https://www.elektronik-kompendium.de/sites/net/0907141.htm)

### Protokoll

In der Netzwerktechnik ist ein Protokoll der Ablauf einer Kommunikation zwischen zwei Systemen. In der Netzwerktechnik sind die Protokolle meist einer bestimmten Schicht des OSI-Schichtenmodells zugeordnet.

- [Protokolle in der Netzwerktechnik](https://www.elektronik-kompendium.de/sites/net/2507261.htm)
- [ISO/OSI-7-Schichtenmodell](https://www.elektronik-kompendium.de/sites/kom/0301201.htm)

### Domäne

Ein Domäne bezeichnet in der Netzwerktechnik ein logisches Subnetz, einen Namensbereich oder ein Objekt, das an der Spitze eines Verwaltungsbereichs steht.  
Im Zusammenhang mit Verzeichnisdienste und großen lokalen Netzwerken spricht man öfter von einer Domäne.

- [Verzeichnisdienste (X.500)](https://www.elektronik-kompendium.de/sites/net/0905011.htm)

### Ressourcen

In der Netzwerktechnik spricht man häufig von Ressourcen. In der Hauptsache meint man damit Speicher, auf dem man Daten ablegen kann. Dazu zählen aber auch Drucker, Server und andere Netzwerkgeräte, die einen Dienst bereitstellen, der zentral in einem Netzwerk zur Verfügung steht.

### Datenpaket / Paket

In der Netzwerktechnik werden einzelne Übertragungseinheiten als Paket oder Datenpaket bezeichnet. Datenpakte werden neben den Daten mit eine Sender- und Empfänger-Adresse ausgestattet. Fehlerkorrektur und Verschlüsselung sind zusätzliche Merkmale.

### Frame

Ein Frame ist ein logischer Rahmen, in dem sich ein Bit-Strom befinden. Frames werden von einer Netzwerkkarte oder einem Netzwerk-Interface über ein Übertragungsmedium gesendet und empfangen. Das Frame ist jeweils mit Daten und einem Protokoll-Header und einem Ethernet-Header versehen. Darin sind Start- und Endsequenzen, Kontrollzeichen, Adressen und Prüfsummen enthalten. Frames werden auch Pakete bzw. Datenpakete genannt. In Zusammenhang mit Ethernet bezeichnet man ein Datenpaket als Frame.

- [Ethernet-Frame](https://www.elektronik-kompendium.de/sites/net/1406191.htm)

### Datagramm

Ein Datagramm ist eine in sich geschlossene Einheit. Ein IP-Paket, das an den Netzwerk-Adapter (NIC, Network Interface Card) übergeben wird, wird als Datagramm bezeichnet.

### Datenstrom / Datastream / Stream

Datastream oder Stream ist ein Datenstrom aus logisch zusammenhängenden Datenpaketen, die über ein Netzwerk übertragen werden. Die logische Verbindung der Datenpakete ist üblicherweise die Empfänger-Adresse. Auf IP-Ebene wäre das die IP-Adresse. Auf TCP- oder UDP-Ebene wäre das die Portnummer.  
Die Datenpakete können aber auch auf der Anwendungsebene eine logische Verbindung zueinander haben.

### Port

In der Netzwerktechnik kann ein Port eine Steckverbindung an einem Switch, Router, etc. oder eine logische Assoziation sein. Zum Beispiel der Zugang zum Netzwerk für einen WLAN-Client an einem WLAN-Access-Point.  
Der Port bei den Protokollen TCP und UDP ist eine Art Adresse, die die Zuordnung zwischen einem Protokoll und einer Anwendung oder zwischen einem Datenstrom und einer Anwendung definiert.  
Ein Port, egal ob logisch oder physisch, wird häufig durch eine Nummer oder Adresse gekennzeichnet.

- [TCP- und UDP-Ports](https://www.elektronik-kompendium.de/sites/net/1812041.htm)

### Unidirektionale Kommunikation

Unidirektional bedeutet "in eine Richtung". Bei der unidirektionalen Kommunikation oder Übertragung zwischen zwei Teilnehmern steht nur ein Kanal zur Verfügung, der nur in eine Richtung genutzt werden kann. Einen Rückkanal gibt es nicht.

### Bidirektionale Kommunikation

Bidirektional bedeutet "in beide Richtungen". Bei der bidirektionalen Kommunikation oder Übertragung können Signale, Daten oder Informationen in beide Richtungen fließen. Es gibt zwischen Sender und Empfänger zwei Kanäle. Einen Hin- und einen Rückkanal. Bei der Unterscheidung der Kanäle spricht man auch von Upstream und Downstream bzw. Uplink und Downlink.  
Bei der bidirektionalen Übertragung unterscheidet man zwischen Halbduplex, bei der nur jeweils ein Kommunikationspartner senden und empfangen darf, und Vollduplex, bei der beide Kommunikationspartner gleichzeitig senden und empfangen dürfen.

### Unicast, Multicast, Broadcast und Anycast

- **Unicast:** Unicast-Adressen adressieren genau einen Host. Die Übertragung erfolgt von einem Host zu einem anderen Host.
- **Multicast:** Hinter einer Multicast-Adresse verbergen sich eine ganze Gruppen von Hosts. Die Übertragung erfolgt von einem Host an mehrere Hosts.
- **Broadcast:** Broadcast-Adressen adressieren alle Hosts. Die Übertragung erfolgt von einem Host an alle anderen Hosts.
- **Anycast:** Anycast-Adressen werden von mehreren Hosts in einem Netzwerk verwendet. Die Übertragung erfolgt von einem Host an einen Host aus einer Gruppe bzw. einem Verbund.

- [Unicast, Multicast, Broadcast und Anycast](https://www.elektronik-kompendium.de/sites/net/2505121.htm)

### Tunneling

Tunneling bezeichnet ein Verfahren, wenn ein Protokoll-Frame mit allen seinen Eigenschaften als Nutzdaten innerhalb eines anderen Protokolls eingebettet ist.

- [Tunneling](https://www.elektronik-kompendium.de/sites/net/1410141.htm)

### Masquerading

Masquerading bezeichnet das Verbergen ganzer Netze hinter einer einzigen IP-Adressen.

Masquerading findet ich häufig bei SOHO-Umgebungen, die vom Internet-Provider nur eine IP-Adresse bekommen und hinter dieser sich verschiedene Endgeräte verbergen, die alle eine Verbindung in das Internet benötigen. Das bedeutet, mehrere interne Adressen werden über ein NAT-Verfahren auf eine externe Adresse gebündelt. Von der externen Seite sind die internen Rechner nicht direkt adressierbar, da von außen nur eine IP-Adresse sichtbar ist.

### Bonding

Beim Bonding werden mehrere physikalisch vorhandene Leitungen zu einer logischen Leitung zusammengeschaltet. In der Regel um eine höhere Geschwindigkeit zu erreichen.

### Topologie

Die Struktur des Netzwerks wird als Topologie bezeichnet. Bus, Ring und Stern sind typische Netzwerk-Topologien. Die Verbindungen innerhalb der Topologie erfolgt über Funk, Kupfer- oder Glasfaserkabel.

- [Netzwerk-Topologie](https://www.elektronik-kompendium.de/sites/net/0503281.htm)

### Backbone

Backbone ist eine Bezeichnung für die Hauptübertragungsstrecke in einem Netzwerk. Der Backbone verbindet in der Regel mehrere Netzknoten. Die Netzknoten sind die Zugangspunkte zum Backbone. Man spricht in dem Zusammenhang auch vom Kernnetz oder Core Network.  
Bei größeren Vernetzungen mit mehreren Netzwerkstrukturen bildet ein Backbone die Infrastruktur im Hintergrund. Zum Beispiel um lokale Netze und Hochleistungssysteme miteinander zu verbinden. Ein Backbone wird dabei redundant ausgelegt.

### Leitungen und Kabel

Die Begriffe Leitungen und Kabel werden häufig gleichwertig verwendet. Doch das ist nicht ganz richtig. Leitungen und Kabel kann man folgender Maßen unterscheiden. Kabel sind Leitungen, die im Boden oder auf hoher See (Meeresboden) verlegt werden. Was man sehen kann sind Leitungen, Kabel sieht man nicht wenn sie genutzt werden.

Umgangssprachlich sagen die meisten Menschen zur Leitung ein Kabel, was falsch (unfachlich) ist. Es ist die häufigste Fehlbenennung in der Elektrotechnik und Informationstechnik, noch vor der Glühbirne.

Kabel ist kürzer und damit das schneller gesprochene Wort. Daher ist der Begriff "Kabel" in vielen Bereichen üblich, auch wenn es falsch ist. So befinden sich auf der Kabeltrommel kein Kabel, sondern eine Leitung. Aber den Begriff Leitungstrommel wird man im Fachhandel sicher nicht finden. Netzwerkleitung sagt auch niemand, obwohl das korrekt wäre.