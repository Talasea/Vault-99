Open Shortest Path First (OSPF) ist ein Routingprotokoll für IP-Netze, das zur Klasse der Link-State-Routingprotokolle gehört.3 Es dient als Interior Gateway Protocol (IGP) in größeren Netzwerken und zeichnet sich durch schnelle Konvergenz und gute Skalierbarkeit aus.3 OSPF verwendet den Shortest-Path-First-Algorithmus (SPF-Algorithmus) zur Berechnung der Routingtabellen und des besten Weges zu einem Ziel.3 Das Protokoll ist in der Version 2 für IPv4 und der Version 3 für IPv6 verfügbar.



Open Shortest Path First (OSPF) ist ein Routingprotokoll für IP-Netze, das zur Klasse der Link-State-Routingprotokolle gehört. Es kommt als Interior Gateway Protocol (IGP) in größeren Netzwerken zum Einsatz und zeichnet sich durch eine schnelle Konvergenz und eine gute Skalierbarkeit aus. Das Protokoll ist in der Version 2 für IPv4 und der Version 3 für IPv6 verfügbar.


Die Abkürzung OSPF steht für Open Shortest Path First. Es handelt sich um ein Protokoll für dynamisches [Routing](https://www.ip-insider.de/was-ist-der-unterschied-zwischen-routing-und-switching-a-1077049/) in [IP](https://www.ip-insider.de/was-ist-ip-a-812352/)-Netzen. OSPF wird der Klasse der Link-State-Routingprotokolle zugeordnet. Die Berechnung der Routingtabellen und des besten Weges zu einem Ziel basiert auf dem Shortest-Path-First-Algorithmus (SPF-Algorithmus). OSPF ist eines der am häufigsten verwendeten Interior [Gateway](https://www.ip-insider.de/was-ist-ein-gateway-a-581268/) Protokolle (IGP) und kommt in größeren Netzwerken zum Einsatz.

Im Gegensatz zu [RIP](https://www.ip-insider.de/was-ist-rip-routing-information-protocol-a-90bf1d6dc342483264271a1e56008682/) (Routing Information Protocol) skaliert es auch in großen Netzen, garantiert die Schleifenfreiheit, konvergiert bei Routenänderungen sehr schnell und ermöglicht Loadbalancing über gleichwertige Verbindungen. Open Shortest Path First verwendet nicht die Anzahl der Hops zu einem bestimmten Ziel als Entscheidungskriterium für die beste [Route](https://www.ip-insider.de/was-ist-ein-router-a-751339/), sondern die Pfadkosten basierend auf Metriken wie die Datenrate einzelner Links. Das Protokoll ist in der Version 2 für IPv4 und in der Version 3 für [IPv6](https://www.ip-insider.de/was-ist-ipv6-a-642703/) verfügbar. OSPF Version 2 ist in RFC 2328 spezifiziert, OSPF Version 3 im RFC 5340.

### Grundsätzliches zu Routingprotokollen

Datenpakete werden in einem IP-Netz auf Basis der [IP-Adressen](https://www.ip-insider.de/was-ist-eine-ip-adresse-a-781830/) zugestellt. Die Weiterleitung der IP-Pakete eines sendenden Endgeräts übernehmen innerhalb des Netzwerks die Router. Diese verwenden Routingtabellen, mit deren Hilfe sie den ausgehenden Link zu einem bestimmten Ziel bestimmen. Die Routingtabellen lassen sich mit fest vorgegebenen statischen Routen aufbauen oder dynamisch über Routingprotokolle zusammenstellen.

Statisches Routing eignet sich nur für kleinere Netzwerke und ist mit manuellen Aufwand zur Konfiguration der statischen Routen verbunden. Ändern sich Wege zu einem Ziel oder fallen Verbindungen aus, erkennen das die Router nicht automatisch und die Routingtabellen müssen angepasst werden.

Dynamisches Routing erkennt Veränderungen im Netzwerk selbständig, indem sich die Router untereinander austauschen. Die Routingtabellen passen sich dynamisch der jeweiligen Situation an. Optimale Wege zu einem Ziel lassen sich auf Basis verschiedener Eigenschaften und Metriken wie die Anzahl der Hops, die [Bandbreite](https://www.ip-insider.de/was-ist-bandbreite-a-aa9b63cf1d5fe248691ca7432f00d18d/), die Auslastung eines Links oder konfigurierte Kosten bestimmen. Ausfälle einzelner Verbindungen werden erkannt und binnen kurzer Zeit alternative Wege berechnet.

### Dynamische Routingprotokolle werden in Link-State-Protokolle und

Distance-Vector-Protokolle unterschieden. Distance-Vector-Protokolle wie RIP (Routing Information Protocol) bestimmen die Erreichbarkeit eines Ziels mithilfe eines Vektors. Der Vektor hält die Information über die Richtung (das Routerinterface zum nächsten Hop) und die Entfernung (Anzahl der Hops) zu einem bestimmten Ziel bereit. Diese Vektoren teilt er anderen Routern mit. Die Router lernen so den optimalen Nachbarn für ein bestimmtes Ziel kennen, sind aber nicht über die Topologie des kompletten Netzwerks informiert. Das Problem der Bestimmung des kürzesten Weges zu einem Ziel verteilt sich auf mehrere Router.

Link-State-Protokolle wie OSPF ermöglichen den Routern einen ganzheitlichen Blick auf die Topologie eines Netzwerks. Die Router tauschen untereinander Link-State-Informationen aus und bauen daraus eine Topologie-Datenbank des Netzwerks auf. Ausgehend von dieser Datenbank kann jeder Router den jeweils besten Weg zu einem Ziel selbst bestimmen. Die Ermittlung des besten Weges basiert auf einem Algorithmus wie dem Shortest-Path-Algorithmus von Dijkstra. Aus den Informationen der besten Wege stellt der Router seine [Routingtabelle](https://www.ip-insider.de/was-ist-eine-routing-table-a-665204/) zusammen.

Ein weiteres Unterscheidungsmerkmal der Routingprotokolle ist ihre Verwendung für das Intradomain-Routing oder das Interdomain-Routing. Interior Gateway-Protokolle (IGP) wie OSPF oder RIP werden für das Routing innerhalb einer Domain genutzt. Für das Routing zwischen verschiedenen Domains kommen Exterior Gateway-Protokolle (EGP) wie [BGP](https://www.ip-insider.de/was-ist-das-border-gateway-protocol-bgp-a-804823/) (Border Gateway Protocol) zum Einsatz.

### Die prinzipielle Funktionsweise von OSPF

Ein zentrales Funktionselement von OSPF ist die Topologie-Datenbank. Sie wird über den Austausch von Routinginformationen mit anderen Routern aufgebaut. Jeder Router übermittelt hierfür seine lokale Sicht des Netzwerks mit seinen über die einzelnen Routerinterfaces erreichbaren Nachbarn an alle anderen Router des Netzwerks. Mithilfe des Shortest Path Algorithmus erstellt jeder Router aus seiner Sicht einen Baum mit dem optimalen Weg zu einem bestimmten Ziel. Aus diesen Informationen kann dann die Routingtabelle erstellt werden. Die Routingtabelle enthält die Informationen, über welchen nächsten Router ein bestimmtes Netz mit welchen "Kosten" erreichbar ist.


Der Austausch der Router bezüglich ihrer jeweiligen lokalen Sicht des Netzwerks findet über so genannte Link State Advertisements (LSAs) statt. Es werden abhängig von den Routertypen und Netzbereichen verschiedene Typen von Link State Advertisements unterschieden, auf die hier nicht im Detail eingegangen werden kann.

Sehr wichtig für den Routingprozess von OSPF ist das Hello-Protokoll. Über regelmäßige Keepalive-Nachrichten erfahren die Nachbarrouter, ob ein Router noch funktioniert und seine Informationen nach wie vor Gültigkeit besitzen. Kommen keine Hello-Pakete eines bestimmten Routers mehr an, können dessen Informationen gestrichen und eine Neuberechnung des Shortest Path gestartet werden. Darüber hinaus kommt das Hello-Protokoll zur Entdeckung neuer Router und zur Wahl eines so genannten Designated Routers (DR) zum Einsatz.

OSPF unterscheidet verschiedene Routertypen wie den Designated Router, den Area Border Router (ABR) oder den Autonomous System Boundary Router (ASBR). Ihnen kommen jeweils spezifische Aufgaben zu. Beispielsweise ist der Designated Router dafür verantwortlich, die Aktualisierungsinformationen innerhalb eines bestimmten Netzbereichs (einer Area) zu verteilen. Dadurch lässt sich die Menge an den zu übertragenen Link State Advertisements reduzieren. Neben dem DR wird auch ein Backup-Designated Router (BDR) gewählt. Area Border Router übernehmen Routing-Schnittstellenfunktionen zwischen einer bestimmten Area und der Backbone Area, die Autonomous System Boundary Router (ASBR) zwischen Autonomen Systemen (AS).

Grundsätzlich sind OSPF-Router bestimmten Areas zugeordnet. Mithilfe des Area-Konzepts lässt sich eine Hierarchie abbilden. Der Routing Traffic wird durch das Area-Konzept reduziert, da die innere Topologie einer Area den anderen Areas verborgen bleibt. Die Backbone Area verbindet die einzelnen Areas miteinander. Zusätzlich existieren noch weitere besondere Area-Typen wie Stub Areas, Transit Areas, Totally Stubby Areas, Not So Stubby Areas oder Totally Not So Stubby Areas.

### Abgrenzung von OSPF zum Distance-Vector-Protokoll RIP

Im Gegensatz zu OSPF ist RIP ein Distance-Vector-Protokoll. Es handelt sich um ein sehr einfaches Routingprotokoll, das in kleineren Netzwerken zum Einsatz kommt. RIP speichert in seiner Routingtabelle die Zieladresse, das zugehörige abgehende Routerinterface und die Anzahl der Hops bis zum Ziel.

Diese Infos versendet der Router in festen regelmäßigen Abständen an alle weiteren benachbarten Router des Netzwerks. Je größer das Netz und je mehr Router vorhanden sind, desto größer ist der durch RIP verursachte Datenverkehr. Fällt eine Verbindung oder eine Route aus, kann es relativ lange dauern, bis sich die Information im Netzwerk verteilt hat.

Darüber hinaus kann RIP keine Routing-Schleifenfreiheit sicherstellen, da jeder Router nur die Vektoren zum Ziel und nicht die Topologie des Netzwerks kennt. OSPF-Router hingegen kennen die Netztopologie und können beste Wege zu einem Ziel nicht nur auf Basis von Hops, sondern auch unter Berücksichtigung weiterer Netzwerkinformationen wie Kosten und Bandbreiten bestimmen.

### Vor- und Nachteile von OSPF

OSPF bietet gegenüber statischem Routing oder einfachen Routingprotokollen wie RIP zahlreiche Vorteile, aber auch einige Nachteile. Die Vorteile sind beispielsweise:

- Unterstützung hierarchischer Netzstrukturen und Unterteilung der Netze in Areas

- geeignet für große Netzwerke

- schnelle Konvergenz bei Veränderungen im Netz

- Sicherstellung der Schleifenfreiheit

- Wahl des besten Weges auf Basis verschiedener Informationen wie Kosten, Auslastung oder Bandbreiten

- dynamische Lastverteilung und Loadbalancing möglich

- Berücksichtigung des Type of Service (TOS) im Routing

- geringer Bandbreitebedarf für den Austausch der Routinginformationen

- Unterstützung der gegenseitigen Authentifizierung der OSPF-Router

Als Nachteile lassen sich aufführen:

- komplexes Protokoll

- tieferes Know-how zur Implementierung notwendig

- leistungsfähigere Router notwendig (Router benötigen eine gewisse Grundperformance und Intelligenz zur Unterstützung von OSPF)



