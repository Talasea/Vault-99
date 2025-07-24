
Unter einer Netzwerk-Topologie versteht man die typische Anordnung und physikalische Verbindung von Geräten in einem Netzwerk. Geräte sind Hosts, wie Clients und Server, die das Netzwerk aktiv nutzen. Dazu zählen auch Netzwerk-Komponenten, wie Switche und Router, die eine Verteilfunktion haben und dafür sorgen, dass alle Netzwerk-Teilnehmer miteinander eine logische Verbindung eingehen können. Die Netzwerk-Topologie bestimmt dabei die einzusetzende Komponente, sowie die Zugriffsmethoden auf das Übertragungsmedium.

Die im folgenden beschriebenen Netzwerk-Topologien beziehen sich auf paketvermittelnde Netzwerke.

- Point-to-Point (PtP) / Punkt-zu-Punkt
- Point-to-Multipoint (PtMP) / Punkt-zu-Mehrpunkt
- Line / Chain / Linie
- Bus
- Ring
- Star / Stern
- Tree / Baum
- Mesh / Vermascht Topologie
- Fully Connected / Vollvermaschte Topologie
- Fabric / Gewebe

### Point-to-Point (PtP) / Punkt-zu-Punkt

![Point-to-Point (PtP) / Punkt-zu-Punkt](https://www.elektronik-kompendium.de/sites/net/bilder/05032811.png)

Bei einer Punkt-zu-Punkt-Topologie besteht nur zwischen zwei Hosts bzw. Geräten eine einfache und direkte physikalische Verbindung. Die beiden Geräten können diese Verbindungen für die gegenseitigen Kommunikation nutzen.  
In einer Adhoc-Umgebung finden die Hosts meist spontan zusammen und kooperieren aber nicht zwangsläufig dauerhaft miteinander.  
In einer Netzwerk-Umgebung besteht die physikalische Verbindung und die darauf aufsetzende logische Verbindung in der Regel dauerhaft.  
Die Punkt-zu-Punkt-Topologie darf mit P2P bzw. der Peer-to-Peer-Architektur nicht verwechselt werden.

### Point-to-Multipoint (PtMP) / Punkt-zu-Mehrpunkt

![Point-to-Multipoint (PtMP) / Punkt-zu-Mehrpunkt](https://www.elektronik-kompendium.de/sites/net/bilder/05032812.png)

Bei einer Punkt-zu-Mehrpunkt-Topologie werden mehrere Hosts durch ein zentrales System gespeist. Dabei müssen sich alle Hosts innerhalb der Topologie eine Leitung zum zentralen System teilen. Zwar kann jeder Teilnehmer sein eigenes Übertragungsmedium haben. Aber eben nur bis zu einem Verzweigungspunkt, von dem aus eine Leitung zum zentralen System führt.

### Line / Chain / Linien-Topologie (Linientechnik)

![Line / Chain / Linien-Topologie (Linientechnik)](https://www.elektronik-kompendium.de/sites/net/bilder/05032813.png)

Bei der Linien-Topologie werden mehrere Hosts miteinander verbunden. Dabei wird eine Leitung von Host zu Host verlegt. Die beiden Enden der Linie werden jeweils mit einem Host abgeschlossen.  
Man bezeichnet die Linien-Topologie auch als Daisy-Chain-Konfiguration (engl. Gänseblümchenkette), bei der mehrere Hardware-Komponenten in Reihe bzw. Serie miteinander verbunden sind. Diese Art der Vernetzung findet man häufig in der Automatisierungs- und Sicherheitstechnik.  
Die Besonderheit bei der Linien-Topologie ist, dass das entfernen eines Hosts in der Linie dazu führt, dass die Linie unterbrochen wird und dabei das Netzwerk ausfällt. Man muss dann die entstandene Lücke überbrücken oder an dieser Stelle neu verkabeln. In der Konsequenz bedeutet das, dass die darauf aufsetzende Verbindungslogik zwischen allen Teilnehmern unter Umständen neu ausgehandelt werden muss (abhängig vom Übertragungssystem).  
Oft wird die Linien-Topologie mit der Bus-Topologie vermischt. Bei der physikalischen Verkabelung findet oft keine Unterscheidung statt. Bei der darauf aufsetzenden Übertragungslogik und Zugriffsverfahren schon.

### Bus / Bus-Topologie

![Bus / Bus-Topologie](https://www.elektronik-kompendium.de/sites/net/bilder/05032814.png)

In der Bus-Topologie sind alle Hosts über eine gemeinsame Leitung miteinander verbunden. Alle Hosts haben Zugriff auf das Übertragungsmedium und die Signale, die darüber übertragen werden. Um Störungen auf der Leitung zu verhindern und die physikalischen Bedingungen zu verbessern, werden die beiden Kabelenden mit einem Abschlusswiderstand versehen.

Eine zentrale Netzwerkkomponente, die die Abläufe auf dem Bus regelt, gibt es nicht. Dafür ist ein Zugriffsverfahren für die Abläufe auf dem Bus verantwortlich, an dessen Regeln sich alle Hosts halten. Die Intelligenz sitzt in den Hosts und wird in der Regel durch ein Protokoll vorgegeben. Der Bus selber ist nur ein passives Übertragungsmedium.

Soll der Bus erweitert werden oder Hosts hinzugefügt oder entfernt werden, kann das Netzwerk für die Zeit der Arbeiten ausfallen.

### Ring / Ring-Topologie

![Ring / Ring-Topologie](https://www.elektronik-kompendium.de/sites/net/bilder/05032815.png)

Die Ring-Topologie ist eine geschlossene Kabelstrecke in der die Netzwerk-Teilnehmer mit einem durchgehenden Kabelring miteinander verbunden sind. Das bedeutet, dass an jedem Host ein Kabel ankommt und ein Kabel abgeht.  
In der Ring-Topologie muss sich typischerweise keine aktive Netzwerk-Komponente befinden. Die Steuerung und der Zugriff auf das Übertragungsmedium regelt ein Protokoll, an das sich alle Stationen halten.  
Allerdings macht ein Ring-Manager Sinn. Denn wenn an einer Stelle der Ring unterbrochen ist, dann kann er in einen Bus-Betrieb umschalten.  
Das bedeutet, dass die Ring-Topologie redundant ist, was in Produktionsumgebungen wichtig ist, die auf hohe Verfügbarkeit angewiesen sind.

### Star / Stern-Topologie

![Star / Stern-Topologie](https://www.elektronik-kompendium.de/sites/net/bilder/05032816.png)

In der Stern-Topologie befindet sich eine Netzwerk-Komponenten, die eine physikalische Verbindung zu allen Hosts unterhält. Jeder Host ist über eine eigene Leitung mit der zentralen Netzwerk-Komponente verbunden. Es handelt sich im Regelfall um einen Hub oder einen Switch. Der Hub oder Switch übernimmt die Verteilfunktion für die Datenpakete. Dazu werden die Datenpakete entgegen genommen und an das Ziel weitergeleitet.  
Die Datenbelastung des zentralen Verteiler kann sehr hoch sein, da alle Daten und Verbindungen darüber laufen. Hosts können jederzeit hinzugefügt oder entfernt werden. Das hat keinen Einfluss auf den Betrieb des Netzwerks.

Ein Netzwerk mit Stern-Bus-Struktur ist ein Kombination aus Stern- und Bus-Topologie. Über eine Sternstruktur sind die Stationen mit einem Hub verbunden. Mehrere Switche sind über eine Busleitung miteinander verbunden.

### Tree / Baum-Topologie

![Tree / Baum-Topologie](https://www.elektronik-kompendium.de/sites/net/bilder/05032817.png)

Die Baum-Topologie ist eine erweiterte Stern-Topologie. Größere lokale Netze haben diese Struktur. Vor allem dann, wenn mehrere Topologien miteinander kombiniert werden. Meist bildet ein übergeordnetes Netzwerk-Element, entweder ein Router oder eine anderen Topologie, die Wurzel (hier umgekehrt dargestellt). Von dort bildet sich ein Stamm mit vielen Verästelungen und Verzweigungen.

### Mesh / Maschen-Topologie

![Tree / Baum-Topologie](https://www.elektronik-kompendium.de/sites/net/bilder/05032818.png)

Bei der Maschen-Topologie bzw. vermaschten Topologie handelt es sich um ein dezentrales Netzwerk, das keinen verbindlichen Strukturen unterliegen muss und in dem alle Netzwerkknoten irgendwie miteinander verbunden sind.  
Durch ein Mesh-Netzwerk erhöht sich die Reichweite des Netzwerks insbesondere für die am Rand liegender Knoten. Beim Ausfall einer Verbindung existiert im Regelfall immer eine alternative Strecke, um den Datenverkehr unterbrechungsfrei fortzuführen. Dazu müssen aktive Netzwerk-Komponenten die Datenpakete innerhalb des Netzwerks vermitteln. Zum Beispiel durch Routing.

- In einem lokalen Netzwerk (LAN) kommt die Maschen-Topologie immer dann vor, wenn ein Wildwuchs aus verschiedenen Systemen und mehrerer Topologien entsteht.
- Das Internet entspricht der Maschen-Topologie, weil keine zentrale Instanz über die Architektur des Netzwerks entscheidet.

### Fully Connected

![Fully Connected](https://www.elektronik-kompendium.de/sites/net/bilder/05032819.png)

Fully Connected bezeichnet eine Topologie, in der alle Hosts miteinander verbunden sind. Gemeint ist damit, dass jeder Host zu jedem Host eine eigene physikalische Verbindung hat. Entsprechend umfangreich muss die Anzahl der verfügbaren Schnittstellen bei jedem Host sein. Gleichzeitig muss für jede Verbindung auch ein Übertragungsmedium zur Verfügung stehen.  
Aus Topologie-Sicht handelt es sich dabei um ein perfektes Netzwerk, das aber nur in geringem Umfang praktiziert wird. Fully Connected macht nur dann Sinn, wenn für eine logische Verbindung zwischen zwei Netzwerk-Teilnehmern die volle Bandbreite der physikalischen Verbindung benötigt wird.

### Fabric / Geflecht-Topologie (Gewebe)

![Fabric / Geflecht-Topologie (Gewebe)](https://www.elektronik-kompendium.de/sites/net/bilder/05032810.png)

Ein hierarchischer Aufbau und die Segmentierung waren lange Zeit das Kriterium beim Strukturieren eines Netzwerks. Wegen dem vorwiegenden Client-Server-Datenstrom war hier die Stern- oder Baum-Topologie mit ihrem zentralistischen Ansatz die bevorzugte Verkabelungs- und Vernetzungsarchitektur. Heute hat der Datenverkehr durch dynamische Inhalte zwischen den Servern und dem Zusammenspiel von Web-, Applikations- und Datenbank-Servern stark zugenommen. Das heißt, die logischen Verbindungen finden nicht mehr nur zwischen Clients und Servern statt, sondern auch zwischen einzelnen Servern. Dabei treten Datenströme auf, die sehr unterschiedliche Charakteristiken aufweisen. Und deshalb müssen zukünftige Netzwerk-Topologien und Netzarchitekturen flexibel sein und über mehr Intelligenz verfügen.

Das Konzept der Fabric soll alle wichtigen Anforderungen an das Netzwerk im Rechenzentrum erfüllen:

- hohe Geschwindigkeit
- Ausfallsicherheit
- Flexibilität
- einfaches Management

Eine Fabric weist eine Sternstruktur auf, die allerdings keinen zentralen Knoten hat, sondern die verteilenden Komponenten redundant zu einer strukturiert vermaschten Topologie miteinander verbindet. Die Fabric bildet die Grundlage zu hochverfügbaren verteilten Systemen.

Die Fabric ist eine Netzwerk-Topologie, deren Begriff und technische Ansätze aus der Fibre-Channel-Welt stammen und in Speichernetzen schon sehr lange zum Einsatz kommt. Sie dienen als Vorbild für Ethernet im Rechenzentrum. Hier ist die Fabric eine verteilt angelegte Architektur, die zum Beispiel mehrere physische Switche zu einem großen logischen Switch zusammenfasst.

Für eine Gebäudevernetzung bedeutet das, dass weitere Core-, Etagen- und Access-Switche zum Einsatz kommen müssen, die über zusätzliche Leitungen miteinander verbunden sind. Hier arbeitet man dann oft auch mit Techniken aus dem Bereich Software Defined Networking.

- [SDN - Software Defined Networking](https://www.elektronik-kompendium.de/sites/net/2507021.htm)

### Vorteile und Nachteile der Grundtopologien

|   |   |   |
|---|---|---|
|**Topologie**|**Vorteile**|**Nachteile**|
|Bus-Topologie|- einfach installierbar<br>- kurze Leitungen|- Netzausdehnung begrenzt<br>- bei Kabelbruch fällt Netz aus<br>- aufwändige Zugriffsmethoden|
|Ring-Topologie|- verteilte Steuerung<br>- große Netzausdehnung|- aufwendige Fehlersuche<br>- bei Störungen Netzausfall<br>- hoher Verkabelungsaufwand|
|Stern-Topologie|- einfache Vernetzung<br>- einfache Erweiterung<br>- hohe Ausfallsicherheit|- hoher Verkabelungsaufwand<br>- Netzausfall bei Ausfall oder Überlastung des Hubs|
|Maschen-Topologie|- dezentrale Steuerung<br>- unendliche Netzausdehnung<br>- hohe Ausfallsicherheit|- aufwendige Administration<br>- teure und hochwertige Vernetzung|

### Verkabelungsaufwand im Vergleich

Der hohe Verkabelungsaufwand der Bus- und Ring-Topologie ist nicht zu unterschätzen. Es mag zwar sein, dass die Kabelstrecke hier kürzer ist als zum Beispiel bei der Stern-Topologie. Bei der Bus- und Ring-Topologie muss man jedoch sehr häufig lange und ungewöhnlich verwinkelte Kabelstrecken wählen, weil man von Host zu Host verlegen muss. Muss man einen Host mal versetzen, dann geht das Kabelziehen wieder von vorne los.  
Bei der Stern-Topologie ist es wesentlich einfacher. Zwar ist der Verkabelungsaufwand im ersten Schritt etwas aufwändiger. Dafür kann man die Leitungen der Stern-Topologie flexibel nutzen. So kann man unterschiedliche Netzwerk-Techniken oder andere Anwendungen auf den Kabelstrecken betreiben.

### WLAN-Topologie

Eine WLAN-Topologie besteht im wesentlichen aus den drahtlosen Netzteilnehmern, die als WLAN-Clients bezeichnet werden und mindestens einer WLAN-Basisstation, die als Wireless Access Point (WAP) oder einfache nur Access Point (AP) bezeichnet wird.

- [WLAN-Topologie](https://www.elektronik-kompendium.de/sites/net/0907071.htm)

