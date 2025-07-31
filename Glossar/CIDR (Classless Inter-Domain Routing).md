### 1. Kerndefinition

**CIDR (Classless Inter-Domain Routing)** ist eine Methode zur Zuweisung von IP-Adressen und zum IP-Routing, die das ursprüngliche, klassenbasierte System (Klasse A, B, C) abgelöst hat. Sie ermöglicht eine wesentlich flexiblere und effizientere Verteilung des knappen IPv4-Adressraums, indem sie die starren Grenzen der Netzklassen aufhebt und die Größe von Netzwerkblöcken variabel gestaltet.

### 2. Detaillierte Erläuterung / Funktionsweise

**Schlüsselkomponenten:**

- **IP-Präfix:** Eine IP-Adresse wird durch einen Schrägstrich (/) und eine Zahl ergänzt, die als Präfixlänge bezeichnet wird (z. B. `192.168.0.0/16`).
    
- **Präfixlänge:** Diese Zahl gibt an, wie viele Bits am Anfang der Adresse den Netzwerkteil (Netz-ID) definieren. Die verbleibenden Bits definieren den Hostteil (Host-ID). Eine höhere Präfixlänge bedeutet ein kleineres Netz (weniger Hosts), eine niedrigere Präfixlänge ein größeres Netz (mehr Hosts).
    

**Prozess:** Im Gegensatz zum klassenbasierten System, bei dem die Netzmaske fest durch die erste Oktettzahl bestimmt war (z. B. Klasse C immer `/24`), erlaubt CIDR jede Präfixlänge von `/0` bis `/32`. Dies ermöglicht es Internet Service Providern (ISPs) und Netzwerkadministratoren, Adressblöcke genau nach Bedarf zuzuweisen. Beispielsweise kann ein `/27`-Netz (32-27=5 Host-Bits, 25−2=30 Hosts) statt eines ganzen `/24`-Netzes (254 Hosts) vergeben werden, was die Adressverschwendung massiv reduziert.

**Zweck und Anwendungsfälle:**

- **Effiziente Adressvergabe:** Verhindert die Verschwendung von IPv4-Adressen.
    
- **Route Aggregation (Supernetting):** CIDR ermöglicht es, mehrere kleinere Routen zu einer einzigen, größeren Route zusammenzufassen (z. B. können acht `/24`-Netze zu einer `/21`-Route aggregiert werden). Dies reduziert die Größe der globalen Routing-Tabellen im Internet-Backbone erheblich, was die Router entlastet und die Routing-Effizienz steigert.
    

### 3. Einordnung in den Gesamtkontext

CIDR ist ein fundamentaler Baustein des modernen Internets und eine Weiterentwicklung des IP-Protokolls (speziell IPv4). Es arbeitet Hand in Hand mit Routing-Protokollen wie **BGP (Border Gateway Protocol)**, das CIDR-Präfixe nutzt, um Routen im Internet auszutauschen. Ohne CIDR wäre der IPv4-Adressraum bereits viele Jahre früher erschöpft gewesen und die Routing-Tabellen der Kernrouter wären aufgrund ihrer Größe kollabiert. Es ist die Grundlage für Konzepte wie **VLSM (Variable Length Subnet Mask)**, das die flexible Unterteilung eines zugewiesenen Adressblocks in Subnetze unterschiedlicher Größe erlaubt.

### 4. Sicherheitsaspekte

Obwohl CIDR primär ein Adressierungs- und Routing-Mechanismus ist, hat es sicherheitsrelevante Implikationen:

- **Firewall- und ACL-Regeln:** Administratoren verwenden CIDR-Notationen, um Zugriffsregeln (Access Control Lists) präzise zu definieren. Statt einzelner IP-Adressen können ganze Netzbereiche (`10.0.0.0/8`) für Whitelisting oder Blacklisting verwendet werden. Eine falsche Konfiguration (z. B. ein zu weites Präfix wie `/16` statt `/24`) kann unbeabsichtigt zu großen Sicherheitslücken führen, indem Angreifern der Zugriff gewährt wird.
    
- **Netzwerksegmentierung:** CIDR ist die technische Grundlage für eine saubere Netzwerksegmentierung. Durch die Aufteilung eines Netzwerks in logische Zonen (z. B. DMZ, internes Netz, Datenbank-Netz) mit spezifischen CIDR-Blöcken kann der Datenverkehr gezielt kontrolliert und die Ausbreitung von Angriffen (laterale Bewegung) erschwert werden.
    

### 5. Praxisbeispiel / Analogie

**Analogie: Telefonnummern** Stellen Sie sich das alte System wie Telefonnummern vor, bei denen die Vorwahl fest die Größe der Stadt definierte. Eine große Stadt bekam eine kurze Vorwahl (viele Anschlüsse), eine kleine Stadt eine lange (wenige Anschlüsse) – unabhängig vom tatsächlichen Bedarf. **CIDR ist wie ein flexibles Vorwahlsystem:** Man kann einem Bezirk genau die Anzahl an Nummern zuteilen, die er benötigt, indem man die Länge des "gemeinsamen" Teils der Nummern (die Vorwahl) variabel gestaltet. Zudem kann man im Telefonbuch sagen: "Alle Nummern, die mit `02421-` beginnen, gehören zu Düren." Das ist Route Aggregation – eine einzige, einfache Regel statt tausender Einzelregeln.

**Praxisbeispiel:** Ein Cloud-Provider wie AWS weist einem Kunden ein Virtual Private Cloud (VPC) mit dem Adressbereich `10.0.0.0/16` zu. Der Kunde kann diesen großen Block nun mittels VLSM (was auf CIDR basiert) weiter unterteilen:

- Ein öffentliches Subnetz für Webserver: `10.0.1.0/24`
    
- Ein privates Subnetz für Datenbanken: `10.0.2.0/24`
    
- Ein weiteres privates Subnetz für interne Dienste: `10.0.3.0/28`
    

### 6. Fazit / Bedeutung für IT-Profis

Für jeden IT-Profi, der mit Netzwerken, Cloud-Infrastrukturen oder IT-Sicherheit zu tun hat, ist ein tiefes Verständnis von CIDR unverzichtbar. Es ist das Rückgrat der IP-Adressverwaltung und des Routings im Internet und in Unternehmensnetzwerken. Die Fähigkeit, CIDR-Notationen korrekt zu lesen, zu berechnen und anzuwenden, ist eine Kernkompetenz für die Konfiguration von Firewalls, Routern, Switches und Cloud-Umgebungen und entscheidend für den Aufbau sicherer, effizienter und skalierbarer Netzwerkinfrastrukturen.