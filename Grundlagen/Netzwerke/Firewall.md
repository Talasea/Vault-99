![Firewall als Sicherheitsstrategie](https://www.elektronik-kompendium.de/sites/net/bilder/08030512.gif)

Eine Firewall ist eine Schutzmaßnahme gegen fremde und unberechtigte Verbindungsversuche aus dem öffentlichen (Internet) ins lokale Netzwerk. Mit einer Firewall lässt sich der kommende und gehende Datenverkehr kontrollieren, protokollieren, sperren und freigeben. Dabei ist die Firewall genau zwischen dem öffentlichen und dem lokalen Netzwerk platziert. Meist ist die Firewall Teil eines Routers. Sie kann aber auch als externe Komponente einem Router vor- oder nachgeschaltet sein.

### Firewall als Sicherheitsstrategie

Eine Firewall ist keine Blackbox, die Sicherheit für das lokale Netzwerk vor dem öffentlichen Netzwerk vorgaukelt. Eine Firewall ist eine technische Einrichtung, die eine Sicherheitsstrategie umsetzt, um unerwünschte, unsichere und schädigende Verbindungen zu verhindern. Ohne ständige Überwachung und Pflege bleibt nach einiger Zeit keine Schutzwirkung übrig.

Vor dem Einsatz einer Firewall ist die Akzeptanz und aktive Mitarbeit aller Beteiligten innerhalb eines lokalen Netzwerks zu gewährleisten, damit die Firewall effektiv funktionieren kann.  
Am Anfang steht die Entscheidung zur Grundhaltung gegenüber Datenverbindungen. Die Firewall kann zunächst alle Verbindungen erlauben und nur bekannte und gefährliche Datenverbindungen unterbinden. Oder sie sperrt alles und alle erwünschten Datenverbindungen müssen explizit freigegeben werden.

### Firewall-Strategie: Alles sperren

**Alles ist gesperrt. Bekannte sichere und erwünschte Vorgänge werden freigegeben.**

Diese Variante ist sehr sicher. Allerdings erfordert sie eine aufwendige Konfiguration der Firewall.

### Firewall-Strategie: Alles freigeben

**Alles ist freigegeben. Bekannte unsichere und unerwünschte Vorgänge werden gesperrt.**

Diese Variante ist relativ komfortabel. Bei der Einführung ist mit keinerlei Problemen zu rechnen. Allerdings ist sie nur so sicher, wie Gefahren und Sicherheitslöcher bekannt sind und gesperrt werden.  

### Elemente einer Firewall

![Firewall aus den Grundelementen Paketfilter und Gateway/Proxy](https://www.elektronik-kompendium.de/sites/net/bilder/08030511.gif)

Grundsätzlich gibt es zwei verschiedene Ansätze für ein Firewall-Konzept:

- passiver Paketfilter mit Port- und Protokoll-Filter
- aktives Gateway (Proxy) mit Virenscanner und Content-Filter

Ein Paketfilter (TCP/IP) kontrolliert die Quell- und Ziel-IP sowie die dazugehörigen Portnummern (TCP). Neben der Filterfunktion ist die Protokollierung abgelehnter Pakete für spätere Analysen wichtig.  
Das Gateway ist ein Proxy, der die Datenpakete der Internet-Dienste (HTTP, FTP, ...) zwischenspeichert. Dadurch lässt sich eine inhaltsbezogene Filterung der Daten vornehmen. Für ein LAN mit viel E-Mail-Verkehr ist ein Virencheck für E-Mails besonders empfehlenswert.  
Einen optimalen Schutz erreicht man durch eine Kombination aus Paketfilter und Proxy. Vorzugsweise sollte der Paketfilter dem Proxy vorgeschaltet sein, um unnötigen Datenverkehr über den Proxy zu vermeiden. Inhaltsbezogene Filterungen benötigen deutlich mehr Rechenleistung. Der Proxy sollte deshalb mit viel Rechenleistung und Arbeitsspeicher ausgestattet sein.  
Eine Firewall kann ein einzelner Computer oder eine Kombination aus Proxy und einem Router sein. Praktikabel ist es, wenn der Paketfilter ein Router mit Firewall-Funktionen ist.

Hauptproblem beim Einrichten einer Firewall ist das Überprüfen der Filterregeln und Beschränkungen. Nur wenige Firewall-Produkte bieten diese Möglichkeit. Sich auf die einwandfreie Funktion der Firewall zu verlassen wäre fatal. Entweder man beauftragt eine externe Firma, die Firewall zu testen oder man beschafft sich einschlägige Software-Tools und testet die Firewall selber. Aber über einen anderen Internet-Zugang, nicht über das eigene lokale Netz!

- [Was ist ein offener Port? (TCP- und UDP-Ports)](https://www.elektronik-kompendium.de/sites/net/1812041.htm)

### Angriffsszenarien, die eine IPv6-Firewall abwehren muss

Eine Firewall für IPv4 filtert keinen IPv6-Verkehr. Und IPv6 ist nicht einfach nur ein IPv4 mit anderen Adressen. Die Erfahrungen aus der IPv4-Welt lassen sich nur bedingt auf IPv6 übertragen. Der Schutz eines LANs durch eine Firewall bedarf für IPv6 völlig neuer Regeln, die bei IPv4 bisher nicht notwendig waren.

- Umgehen der Filterregeln durch den kreativen Einsatz von Extension Header.
- IPv6-Datagramme mit vorgetäuschter Absender-Adresse aus dem internen Netz.
- Beliebige ICMPv6-Pakete
- Fluten der NDP-Table
- Überlasten der Firewall per TCP-Flooding

Es muss nicht immer zwangsläufig das Umgehen der Firewall sein. Einem Angreifer kann es schon genügen, wenn die Firewall überlastet wird und somit die Verbindung zum Internet gestört ist.

### Sicherheitsvorkehrungen?

Keine Sicherheitsvorkehrungen oder Sicherheitsmechanismen zu verwenden ist fahrlässig. Allerdings sollte man schon genau hinschauen, was einem so als Sicherheitsfunktion angeboten wird.

Ein **MAC-Filter**, wie er in WLAN-Access-Points angeboten wird, ist als Sicherheitsfunktion bedingt tauglich. Zum einen ist der Verwaltungsaufwand groß und zweitens für einen Hacker kein wirkliches Hindernis. Jeder Netzwerk-Adapter kann mit einer anderen MAC-Adresse versehen werden.

**NAT** wird besonders in Produkt-nahen Beschreibungen als Sicherheitsmerkmal beschrieben. Hinter NAT steckt ein Mechanismus, der als Nebenprodukt verhindert, dass Stationen hinter dem NAT-Router von außerhalb direkt ansprechbar sind (bei IPv4). Von außen initiierte Verbindungsversuche werden verworfen und bekommen keinen Zugang zum lokalen Netzwerk.  
NAT als Sicherheitsmerkmal zu bezeichnen ist irreführend, weil es nicht die Aufgabe von NAT ist, die Sicherheit zu erhöhen.

Ein weiterer gut gemeinter Ratschlag ist das **Blockieren von Ports**. Dadurch soll verhindert werden, dass über nicht blockierte Ports irgendwelche Dienste angesprochen werden können. Allerdings erreicht man dadurch nicht mehr Sicherheit. Protokolle sind nicht an bestimmte Ports gebunden. Sie können irgendwelche Ports verwenden.  
Ziel sollte es sein, alle nicht in Gebrauch befindlichen Dienste abzuschalten. Denn dann braucht man sich um offene Ports keine Sorgen machen. Ports sperrt nur derjenige, der seine Server- und Netzwerk-Dienste nicht im Griff hat.

Trotz aller Sicherheitsmaßnahmen ist die beste Firewall die Isolation. Computer mit sensiblen oder datenschutzrechtlichen Daten sollten autark und vom Netzwerk getrennt laufen.

### SPI - Stateful Packet Inspection

SPI ist ein Firewall-Leistungsmerkmal. Dieses Verfahren entscheidet anhand mehreren Kriterien, ob ein eingehendes Datenpaket weitergeleitet oder verworfen wird. Z. B. wird der Zielport als Kriterium verwendet. Ist in der Firewall für diesen Port kein Server angegeben, werden die Datenpakete für diesen Port verworfen. SPI überprüft auch, ob eingehende Datenpakete zu zuvor gesendeten Datenpaketen in Beziehung stehen. Also zu einer Sitzung gehören, die durch das sichere lokale Netzwerk ausgelöst wurden. Datenpakete, die sehr häufig eintreffen werden identifiziert. Liegt der Verdacht nahe, dass es sich um eine DoS-Attacke (Denial-of-Service) handelt werden diese Datenpakete automatisch verworfen.

- [SPI - Stateful Packet Inspection](https://www.elektronik-kompendium.de/sites/net/1409291.htm)

### Next Generation Firewall

Die Bezeichnung "Next Generation Firewall" wurde von Gartner Research (Marktforschungsinstitut im Bereich IT) definiert. Diese Firewall der nächsten Generation kann im Datenstrom Anwendungen und Benutzer erkennen. Dazu gehört ein integriertes Intrusion Prevention System (IPS), die Identifikation von Anwendungen und Protokollen unabhängig vom genutzten Port und die Berücksichtigung externer Datenquellen, wie zum Beispiel Verzeichnisdienste mit Benutzerdaten.  
Next Generation Firewalls gehen also über die üblichen Fähigkeiten einer Firewall, wie Paketfilter, Network Address Translation (NAT) und Stateful Inspection hinausgeht.

Insbesondere die Benutzer- und Anwendungserkennung ist für die zukünftige Sicherheit von Netzwerk extrem wichtig. Seit sich HTTP als Universalprotokoll entwickelt hat, müssen nicht mehr nur ein Browser und Webserver die Endpunkte einer HTTP-Verbindung sein. Grundsätzlich kann man mit HTTP alles transportieren. Aus Sicherheitsgründen darf man HTTP nach außen hin nicht mehr generell freigeben.  
Hier setzt die Anwendungserkennung an, die versucht zu erkennen, was das System gerade überträgt. Die Anwendungserkennung übernimmt die Fähigkeiten eines Proxys bzw. Content-Filters. Aber sie muss weit mehr als das leisten. Um Anwendungen zu erkennen, bedarf es einen Abgleich mit Erkennungsmustern, ähnlich wie bei einem Virenscanner. Dabei ist es notwendig, dass diese Muster regelmäßig aktualisiert werden.

Typischerweise versucht man Google, Facebook, Youtube, Chats und Peer-to-Peer-Anwendungen zu erkennen. Wobei die meisten Anwendungen eher privater Nutzung zuzuordnen sind. Hierbei besteht der Irrweg darin, die Benutzer zu kontrollieren, anstatt Sicherheitslücken zu schließen. Sicherlich sinnvoll, wenn man bedenkt, dass der Mensch das größte Sicherheitsrisiko darstellt. Viel wichtiger wäre jedoch, dass die Firewall Anwendungen erkennt, vor denen das Unternehmensnetz tatsächlich geschützt werden muss.

Eine Firewall sollte im Optimalfall auch der VPN-Endpunkt sein. Damit können die Firewall-Regeln auch für die VPN-Daten gelten.

### Zero Trust

Zero Trust ist ein Sicherheitskonzept, bei dem generell jedem Netzwerkverkehr, unabhängig von seiner Herkunft, misstraut wird. Teil des Konzepts ist, dass jeder Zugriff einer Zugangskontrolle und jede Verbindung einer Verschlüsselung unterliegt.

- [Zero Trust](https://www.elektronik-kompendium.de/sites/net/2512031.htm)