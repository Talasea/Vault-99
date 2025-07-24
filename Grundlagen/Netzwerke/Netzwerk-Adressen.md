
Netzwerk-Adressen stehen meist in Zusammenhang mit einem bestimmten Übertragungsverfahren, Protokoll oder einer Zweckbindung. Das heißt, Netzwerk-Adressen erfüllen eine bestimmte Aufgabe.  
Je nach Zweck weisen sie einen hierarchischen Aufbau auf. Über die OSI-Schichten hinweg ist zwischen den Adressen und Namen eine Adressauflösung oder Namensauflösung notwendig.

#### Aufgaben von Netzwerk-Adressen

- Informationen über Quelle bzw. Sender (Absender)
- Informationen über Ziel bzw. Empfänger
- Informationen über Weg und Richtung zum Empfänger

#### Ziele und Adressen im Netzwerk

- Unicast-Adressen: einzelnes Ziel
- Multicast-Adressen: Gruppe von Empfängern
- Broadcast-Adressen: alle Teilnehmer eines Netzwerks

### Übersicht: Netzwerk-Adressen

- [MAC-Adresse](https://www.elektronik-kompendium.de/sites/net/1406201.htm)
- [IPv4-Adresse](https://www.elektronik-kompendium.de/sites/net/2011211.htm)
- [IPv6-Adresse](https://www.elektronik-kompendium.de/sites/net/1902111.htm)
- [Portnummern (TCP und UDP)](https://www.elektronik-kompendium.de/sites/net/1812041.htm)
- [Hostname](https://www.elektronik-kompendium.de/sites/net/0901141.htm)
- [Computername](https://www.elektronik-kompendium.de/sites/net/0901141.htm)
- [Domain-Namen](https://www.elektronik-kompendium.de/sites/net/0901141.htm)
- [URL - Uniform Resource Locator](https://www.elektronik-kompendium.de/sites/net/0908061.htm)
- [E-Mail-Adresse](https://www.elektronik-kompendium.de/sites/net/0902261.htm)
- [DID - Decentralized Identifiers](https://www.elektronik-kompendium.de/sites/net/2809011.htm)

### MAC-Adresse

Der Standard IEEE 802.1 definiert den Media Access Control (MAC). Hier wird unter anderem die physikalische Adresse für Netzwerk-Schnittstellen festgelegt. Und das unabhängig von der Übertragungstechnik. Die sogenannte MAC-Adressen gelten zum Beispiel für Ethernet (IEEE 802.3), Bluetooth (IEEE 802.15) und WLAN (IEEE 802.11).

- [MAC-Adresse](https://www.elektronik-kompendium.de/sites/net/1406201.htm)

### IPv4-Adresse

Die wichtigste Aufgabe von IP (Internet Protocol) ist, dass jeder Host in einem dezentralen TCP/IP-Netzwerk gefunden werden kann. Dazu wird jedem Hardware-Interface (Netzwerkkarte oder -adapter) eine logische IPv4-Adresse zugeteilt.

- [IPv4-Adresse](https://www.elektronik-kompendium.de/sites/net/2011211.htm)

### IPv6-Adresse

Eine IPv6-Adresse ist eine Netzwerk-Adresse, die einen Host eindeutig innerhalb eines IPv6-Netzwerks logisch adressiert. Im Gegensatz zu anderen Adressen hat ein IPv6-Host pro Interface mehrere IPv6-Adressen, die unterschiedliche Gültigkeitsbereiche haben. Zum Beispiel link-lokal und global.

- [IPv6-Adresse](https://www.elektronik-kompendium.de/sites/net/1902111.htm)

### Port-Nummern (TCP und UDP)

TCP- und UDP-Ports sind eine Software-Abstraktion, um parallele Kommunikationsverbindungen einer oder mehrerer Anwendungen voneinander unterscheiden zu können. Ähnlich wie IP-Adressen zur Adressierung von Rechnern in Netzwerken dienen, adressieren Ports spezifische Anwendungen und ihre Verbindungen, die auf einem Rechner laufen.

- [TCP- und UDP-Ports](https://www.elektronik-kompendium.de/sites/net/1812041.htm)

### Domain-Namen

Ein Domain-Name, kurz Domain, dient dazu, um Computer, die mit kaum merkbaren IP-Adressen adressiert sind, richtige Namen zu geben und gleichzeitig in eine hierarchische Struktur zu unterteilen.

- [Domain-Namen](https://www.elektronik-kompendium.de/sites/net/0901141.htm)

### URL

Der URL (nicht die) ist eine "einheitliche Angabeform für Ressourcen" in Netzwerken.

- [URL - Uniform Resource Locator](https://www.elektronik-kompendium.de/sites/net/0908061.htm)

### E-Mail-Adresse

Eine E-Mail-Adresse kennzeichnet das ungewöhnliche Zeichen "@" (Klammeraffe). Es wird als Trennzeichen zwischen Nutzername und dem Domain-Namen (Server-Adresse) verwendet. Darin unterscheidet sich die E-Mail-Adresse von anderen Internet- oder Netzwerk-Adressen.

- [E-Mail-Adresse](https://www.elektronik-kompendium.de/sites/net/0902261.htm)

### Protokolle und Dienste zur Adressauflösung und Namensauflösung

Zur Adressierung von Computern werden nicht Namen, sondern Nummern verwendet. Es ist nicht möglich, einen Computer direkt mit seinem Namen anzusprechen. Doch numerische Adressen sind für Menschen schwer zu merken und zu verstehen. Doch die digitale Welt besteht aus 1en und 0en (binäre Adresse). Aus diesem Grund wurden Methode entwickelt, um eine Umwandlung bzw. Auflösung von Namen in numerische Adressen und umgekehrt zu realisieren. Dafür gibt es Protokolle und Dienste zur Adressauflösung und Namensauflösung.

- [ARP - Address Resolution Protoco (IPv4)](https://www.elektronik-kompendium.de/sites/net/0901061.htm)
- [NDP - Neighbour Discovery Protocol (IPv6)](https://www.elektronik-kompendium.de/sites/net/1902261.htm)
- [DNS - Domain Name System](https://www.elektronik-kompendium.de/sites/net/0901141.htm)
- [WINS - Windows Internet Name Service](https://www.elektronik-kompendium.de/sites/net/0901151.htm)
- [PNRP - Peer Name Resolution Protocol](https://www.elektronik-kompendium.de/sites/net/1408251.htm)

### Übersicht: Tools zur Adressauflösung und Namensauflösung

- [arp (Windows)](https://www.elektronik-kompendium.de/sites/net/0901071.htm)
- [nslookup](https://www.elektronik-kompendium.de/sites/net/0901281.htm)
- [host](https://www.elektronik-kompendium.de/sites/net/0901121.htm)