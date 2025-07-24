
In der Netzwerktechnik unterscheidet man zwischen aktiven und passiven Netzwerk-Komponenten. Während aktive Netzwerk-Komponenten eine eigene Logik haben, zählen die passiven Netzwerk-Komponenten zur fest installierten Netzwerk-Infrastruktur.  
In der Regel dienen Netzwerk-Komponenten zur Kopplung der Netzwerk-Stationen. Man spricht deshalb auch von Kopplungselementen.

### Passive Netzwerk-Komponenten

- Patchkabel und Installationskabel
- Anschlussdose
- Steckverbinder
- Patchfeld / Patchpanel
- Netzwerk-Schrank / Patch-Schrank

Hinweis: Zu den passiven Netzwerk-Komponenten zählen die Bestandteile der Verkabelung. Diese ist im OSI-Schichtenmodell nicht definiert.

### Aktive Netzwerk-Komponenten

In kleinen privaten Netzwerken, haben Netzwerk-Komponenten noch klare Bezeichnung, wie Switch oder Router. In großen Unternehmensnetzwerken ist die Benennung der Kopplungselemente nicht immer eindeutig.

- [Netzwerkkarte](https://www.elektronik-kompendium.de/sites/net/0811011.htm)
- [Repeater](https://www.elektronik-kompendium.de/sites/net/0901091.htm)
- [Hub](https://www.elektronik-kompendium.de/sites/net/1405161.htm)
- [Bridge](https://www.elektronik-kompendium.de/sites/net/0901101.htm)
- [Medienkonverter](https://www.elektronik-kompendium.de/sites/net/0811071.htm)
- [Switch](https://www.elektronik-kompendium.de/sites/net/0811021.htm)
- [Managed Switch / Enterprise Switch](https://www.elektronik-kompendium.de/sites/net/2509021.htm)
- [Router](https://www.elektronik-kompendium.de/sites/net/1404181.htm)
- [Layer-3-Switch](https://www.elektronik-kompendium.de/sites/net/1405171.htm)
- [Gateway](https://www.elektronik-kompendium.de/sites/net/0901111.htm)
- [Server](https://www.elektronik-kompendium.de/sites/net/0505081.htm)
- [Proxy](https://www.elektronik-kompendium.de/sites/net/1101221.htm)
- [Printserver](https://www.elektronik-kompendium.de/sites/net/1409081.htm)
- [NAS (Storage)](https://www.elektronik-kompendium.de/sites/net/1409141.htm)
- [Firewall](https://www.elektronik-kompendium.de/sites/net/0803051.htm)
- [Load Balancer](https://www.elektronik-kompendium.de/sites/net/0904131.htm)

### Switch

Ein Switch ist ein Kopplungselement, das mehrere Stationen in einem Netzwerk miteinander verbindet. In einem Ethernet-Netzwerk, das auf der Stern-Topologie basiert dient ein Switch als Verteiler für die Datenübertragung.

- [Switch](https://www.elektronik-kompendium.de/sites/net/0811021.htm)
- [Managed Switch / Enterprise Switch](https://www.elektronik-kompendium.de/sites/net/2509021.htm)
- [Layer-3-Switch](https://www.elektronik-kompendium.de/sites/net/1405171.htm)

### Router

Router verbinden Netzwerke mit unterschiedlichen Protokollen und Architekturen. Router finden sich häufig an den Außengrenzen eines Netzwerkes. Hier wird die Verbindung zu anderen Netzen und dem Internet geschaffen.

- [Router](https://www.elektronik-kompendium.de/sites/net/1404181.htm)[](https://www.elektronik-kompendium.de/sites/net/0810101.htm)

### Gateway

Ein Gateway ist eine Hardware oder Software oder eine Kombination daraus, die eine Schnittstelle zwischen zwei inkompatiblen Netzwerken darstellt. Das Gateway kümmert sich darum, dass die Form und Adressierung der Daten in das jeweilige andere Format und die Protokolle eines anderen Netzes konvertiert werden.

- [Gateway](https://www.elektronik-kompendium.de/sites/net/0901111.htm)

### Firewall

Sicherheit ist immer ein Gesamtkonzept, in dem festgelegt ist, was wovor geschützt sein muss, was die Angriffsflächen sind und wie man diese schließt oder minimiert. In einem lokalen Netzwerk ist die Angriffsfläche die Schnittstelle zum Internet.

- [Firewall](https://www.elektronik-kompendium.de/sites/net/0803051.htm)

### Server

Was ein "richtiger Server" ist, darüber lässt sich trefflich streiten. In den meisten Fällen wird es ein Computer mit einem leistungsstarken Prozessor, viel Arbeitsspeicher, mehreren Festplatten und großzügiger Netzwerk-Anbindung sein. Auf Servern werden zentrale Aufgaben bearbeitet, verwaltet und gespeichert.

- [Server](https://www.elektronik-kompendium.de/sites/net/0505081.htm)

### Zuordung im OSI-Schichtenmodell (aktive Komponenten mit Verteilfunktion)

|Schicht|Repeater|Hub|Bridge|Switch|Router|Gateway|Firewall|
|---|---|---|---|---|---|---|---|
|7||||||x|(x)|
|6||||||x|(x)|
|5||||||x|(x)|
|4|||||(x)|x|x|
|3||||(x)|x|x|x|
|2|||x|x||x||
|1|x|x||||x||

- [OSI-Schichtenmodell in der Netzwerktechnik](https://www.elektronik-kompendium.de/sites/net/0706101.htm)

### Software Defined Networking (SDN)

Zu Software Defined Networking, Software Defined Network oder softwaredefiniertes Netzwerk, kurz SDN, gehören Netzwerk-Komponenten, deren Funktionen sich individuell programmieren lassen. Gleichzeit ist eine übergeordnete Steuerung aller Netzwerk-Komponenten möglich.

- [SDN - Software Defined Networking](https://www.elektronik-kompendium.de/sites/net/2507021.htm)
- [Virtualisierung im Netzwerk](https://www.elektronik-kompendium.de/sites/net/2507011.htm)