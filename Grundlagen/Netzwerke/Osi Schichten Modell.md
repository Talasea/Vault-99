

**OSI-Modell**: Das OSI-Modell (Open Systems Interconnection) ist ein Referenzmodell für Netzwerkprotokolle, das beschreibt, wie technische Systeme miteinander kommunizieren. Es besteht aus 7 Schichten, die konzeptionell von unten nach oben aufeinander “gestapelt” sind.

- **Schichten des OSI-Modells**:
    - **Bitübertragung**: Die unterste Schicht, die sich mit der Übertragung von Bits beschäftigt.
    - **Sicherung**: Die Schicht, die die Fehlererkennung und -korrektur übernimmt.
    - **Vermittlung**: Die Schicht, die die Weiterleitung von Paketen regelt.
    - **Transport**: Die Schicht, die die zuverlässige Übertragung von Daten gewährleistet.
    - **Sitzung**: Die Schicht, die die Kommunikation zwischen Anwendungen regelt.
    - **Darstellung**: Die Schicht, die die Daten in ein lesbares Format umwandelt.
    - **Anwendung**: Die oberste Schicht, die die Kommunikation zwischen Benutzer und Anwendung regelt.

Das OSI-Modell dient als Standard für die Gestaltung von Netzwerken und die Herstellung von Hardware-Ausrüstung. Es ermöglicht die Kommunikation zwischen verschiedenen Systemen und garantiert die Interkonnektivität zwischen ihnen.

- **Funktionsweise des OSI-Modells**:

- Wenn zwei Systeme miteinander kommunizieren, durchlaufen die Daten alle sieben Schichten des OSI-Modells, sowohl beim Sender als auch beim Empfänger.
- Jede Schicht fügt ihren eigenen Header und Trailer an die Daten an, um die Kommunikation zu ermöglichen.
- Die Daten werden von der Anwendungsschicht bis hin zur Physikalischen Schicht übertragen und dann wieder zurück zur Anwendungsschicht.

![[Pasted image 20241220084032.png]]


### Das OSI-Schichtenmodell in der Praxis

Das OSI-Schichtenmodell wird sehr häufig als Referenz herangezogen, wenn es darum geht, Abläufe einer Kommunikation oder Nachrichtenübermittlung darzustellen. Doch eigentlich ist das DoD-Schichtenmodell (TCP/IP) viel näher an der Realität.  
Das Problem des OSI-Schichtenmodells ist die Standardisierungsorganisation ISO, die einfach zu schwerfällig war, um in kürzester Zeit einen Rahmen für die Aufgaben von Protokollen und Übertragungssystemen in der Netzwerktechnik auf die Beine zu stellen. TCP/IP dagegen war frei verfügbar, funktionierte und verbreitete sich mit weiteren Protokollen rasend schnell. Der ISO blieb nichts anderes übrig, als TCP/IP im OSI-Schichtenmodell zu berücksichtigen.  
Neben TCP/IP haben sich noch weitere Netzwerkprotokolle entwickelt. Die wurden jedoch irgendwann von TCP/IP abgelöst. Fast alle Netzwerke arbeiten heute auf der Basis von TCP/IP.

In der folgenden Tabelle werden die verschiedensten Protokolle, Übertragungs- und Vermittlungstechniken den Schichten des OSI-Modells zugeordnet.  
Viele Protokolle und Übertragungsverfahren nutzen mehr als nur eine Schicht. Deshalb kann eine vollständige und korrekte Darstellung der Tabelle nicht gewährleistet werden.

|   |   |   |
|---|---|---|
|Schicht 7|Anwendung|Telnet, FTP, HTTP, SMTP, NNTP|
|Schicht 6|Darstellung|Telnet, FTP, HTTP, SMTP, NNTP, NetBIOS|
|Schicht 5|Kommunikation|Telnet, FTP, HTTP, SMTP, NNTP, NetBIOS, TFTP|
|Schicht 4|Transport|TCP, UDP, SPX, NetBEUI|
|Schicht 3|Vermittlung|IP, IPX, ICMP, T.70, T.90, X.25, NetBEUI|
|Schicht 2|Sicherung|LLC/MAC, X.75, V.120, ARP, HDLC, PPP|
|Schicht 1|Übertragung|Ethernet, Token Ring, FDDI, V.110, X.25, Frame Relay, V.90, V.34, V.24|

Auch wenn nur die Schichten von 1 bis 7 offiziell definiert sind, gelten steht im allgmeinen Sprachgebraucht die Schicht 0 für die Verkabelung und die Hardware. Die Schicht 8 stellt den Anwender mit seinen Anforderungen oder die Politik dar. Die Schicht 9 ist die Religion oder ein Dogma.




Das OSI-Modell (Open Systems Interconnection-Modell) ist ein konzeptionelles Rahmenwerk, das die Funktionen eines Netzwerkkommunikationssystems in sieben Schichten unterteilt. Es wurde von der Internationalen Organisation für Normung (ISO) entwickelt und dient als Referenzmodell, um zu verstehen, wie verschiedene Netzwerkprotokolle und -technologien zusammenarbeiten.

Hier ist eine detaillierte Erläuterung der einzelnen Schichten:

**1. Physikalische Schicht (Physical Layer):**

- Diese Schicht ist die unterste Schicht des OSI-Modells und befasst sich mit der physischen Übertragung von Daten über ein Übertragungsmedium.
- Sie definiert die elektrischen, mechanischen und physikalischen Spezifikationen für die Datenübertragung.
- Sie ist verantwortlich für die Umwandlung von Datenbits in elektrische Signale, Lichtimpulse oder Funkwellen und umgekehrt.
- Zu den Technologien, die auf dieser Schicht arbeiten, gehören Ethernet-Kabel, Glasfaserkabel und Funkfrequenzen.
- Hier werden die Daten als Bits übertragen.

**2. Sicherungsschicht (Data Link Layer):**

- Diese Schicht ist für die zuverlässige Übertragung von Daten zwischen benachbarten Netzwerkgeräten verantwortlich.
- Sie unterteilt die Daten in Frames und fügt Header- und Trailer-Informationen hinzu, um Fehler zu erkennen und zu korrigieren.
- Sie befasst sich auch mit der MAC-Adressierung (Media Access Control), die zur eindeutigen Identifizierung von Netzwerkgeräten verwendet wird.
- Die Sicherungsschicht ist in zwei Unterschichten unterteilt:
    - MAC (Media Access Control): Steuert den Zugriff auf das Übertragungsmedium.
    - LLC (Logical Link Control): Bietet eine Schnittstelle zur Netzwerkschicht.
- Hier findet die Übertragung von Frames statt.

**3. Netzwerkschicht (Network Layer):**

- Diese Schicht ist für die logische Adressierung und das Routing von Datenpaketen über das Netzwerk verantwortlich.
- Sie verwendet IP-Adressen (Internet Protocol), um Geräte im Netzwerk zu identifizieren und Datenpakete von einem Netzwerk zum anderen zu leiten.
- Sie befasst sich auch mit dem Routing, das den besten Pfad für die Datenpakete durch das Netzwerk bestimmt.
- Hier werden die Daten in Pakete verpackt, und erhalten eine IP-Adresse.

**4. Transportschicht (Transport Layer):**

- Diese Schicht ist für die zuverlässige und geordnete Übertragung von Daten zwischen Anwendungen auf verschiedenen Geräten verantwortlich.
- Sie bietet Mechanismen zur Fehlerkorrektur, Flusskontrolle und Segmentierung von Daten.
- Die beiden wichtigsten Protokolle auf dieser Schicht sind:
    - TCP (Transmission Control Protocol): Bietet eine verbindungsorientierte, zuverlässige Übertragung.
    - UDP (User Datagram Protocol): Bietet eine verbindungslos, unzuverlässige Übertragung.
- Hier wird die Ende zu Ende Verbindung aufgebaut.

**5. Sitzungsschicht (Session Layer):**

- Diese Schicht ist für die Einrichtung, Verwaltung und Beendigung von Sitzungen zwischen Anwendungen verantwortlich.
- Sie verwaltet die Dialogsteuerung, die Synchronisation und das Checkpointing.
- Sie ist für die Verwaltung von Verbindungen zwischen Anwendungen verantwortlich.
- Hier findet die Sitzungssteuerung statt.

**6. Darstellungsschicht (Presentation Layer):**

- Diese Schicht ist für die Datenformatierung und -konvertierung verantwortlich.
- Sie befasst sich mit der Datenverschlüsselung, -komprimierung und -übersetzung.
- Sie stellt sicher, dass die Daten von der Anwendung des Senders in einem Format empfangen werden, das von der Anwendung des Empfängers verstanden wird.
- Hier findet die Daten übersetzung statt.

**7. Anwendungsschicht (Application Layer):**

- Diese Schicht ist die oberste Schicht des OSI-Modells und bietet Netzwerkdienste für Anwendungen.
- Sie ermöglicht Anwendungen den Zugriff auf das Netzwerk und bietet Funktionen wie E-Mail, Webbrowser und Dateiübertragung.
- Zu den Protokollen, die auf dieser Schicht arbeiten, gehören HTTP (Hypertext Transfer Protocol), SMTP (Simple Mail Transfer Protocol) und FTP (File Transfer Protocol).
- Hier findet die Benutzer interaktion statt.

Das OSI-Modell bietet einen wertvollen Rahmen für das Verständnis der Komplexität der Netzwerkkommunikation und ist ein wichtiges Werkzeug für Netzwerkadministratoren, Entwickler und Sicherheitsexperten.



-----

https://studyflix.de/informatik/osi-modell-5524


-----
# OSI-Schichten-Modell

Im OSI-Schichten-Modell wird beschrieben, welche Voraussetzungen gegeben sein müssen, damit verschiedene Netzwerkkomponenten miteinander kommunizieren können. OSI steht für „Open System Interconnection“ und heißt übersetzt „Offenes System für Kommunikationsverbindungen“.

![das Osi Schichtmodell](https://www.netzwerke.com/wp-content/uploads/osi-schicht-modell-300x225.jpg)Die Kommunikation geschieht folgendermaßen: Sender und Empfänger senden bzw. erhalten Informationen in einer Anwendung, wie z. B. in ihrem E-Mail-Programm. Diese Information läuft dann von der Anwendung zur Netzwerkkarte, verlässt den Rechner über ein Übertragungsmedium ([Kabel](https://www.netzwerke.com/Netzwerk-Kabel.htm "Kabel") oder Funk), läuft darüber vielleicht noch über andere Netzwerkkomponenten, wie beispielsweise einen Hub und erreicht dann über die Netzwerkkarte des Zielrechners die Anwendung des Empfängers. Alle Schritte, die vom Sender bis zum Empfänger gemacht werden müssen, werden während der Übertragung in einem Protokoll festgehalten, damit jede einzelne Station auf diesem Weg weiß, wohin das Paket möchte, woher es kommt und welche Eigenschaften es hat. Damit dieser Weg funktioniert, muss dieser eindeutig festgelegt werden und alle Geräte und jede Software, die in diesem Prozess involviert sind, müssen den Ablauf kennen und dieselbe Sprache sprechen. Diese Normen legt das OSI-Schichten-Modell fest. 1983 wurde dieses Modell von der Internationalen Organisation für Normung (ISO) standardisiert.  

Das OSI-Schichten-Modell sorgt durch diesen Standard dafür, dass in einem [Netzwerk](https://www.netzwerke.com/ "Netzwerk") Komponenten und Software verschiedener Hersteller miteinander arbeiten können.

Da das Thema der Datenkommunikation sehr komplex ist, wurde das OSI-Schichten-Modell in sieben Schichten unterteilt. Die Schichten 1 bis 4 gehören zum Transportsystem. Die Schichten 5-7 sind anwendungsorientierte Schichten. Jede Schicht behandelt eine Anforderung, die für eine funktionierende Kommunikation erfüllt werden muss. Ein vom Sender kommendes, zu übertragendes Datenpaket durchläuft die Schichten 7 bis 1. Jede Schicht fügt dem Datenpaket Protokoll-Information zu, die dann im Protokoll des Datenpaketes stehen. Die Schicht 1 wandelt das Datenpaket inklusive aller Protokoll-Informationen dann schließlich in technisch übertragbare Daten um und schickt es über das Übertragungsmedium (Kabel oder Funk) weg. Auf der Empfängerseite durchläuft das Datenpaket dann die Schichten in umgekehrter Reihenfolge, nämlich von Schicht 1 bis Schicht 7. Hier werden die Protokoll-Informationen wiederum Schicht für Schicht entfernt, nachdem sie von den einzelnen Schichten interpretiert worden sind.  

## Schichten – Details

**Schicht 1  
Bitübertragungsschicht (engl.: Physical Layer)**  
Die Bitübertragungsschicht ist für die Übertragung der Bitströme über das Übertragungsmedium (Kabel, Funk) zuständig. Hier werden folgende Parameter festgelegt:

1.    Übertragungsmedium (Kupfer, Glasfaser, Funk)  
2.    Die Funktion der einzelnen Leitungen (Datenleitung,  
Steuerleitung)  
3.    die Übertragungsrichtung (simplex: in eine Richtung /  
halb-[duplex](https://www.netzwerke.com/Netzwerk-Glossar/Duplex.html "duplex"): abwechselnd in beide Richtungen / duplex:  
gleichzeitig in beide Richtungen  
4.    Übertragungsgeschwindigkeit

Beispielgeräte, die dieser Schicht zugeordnet werden sind Netzwerkkarte und Hub.

**Schicht 2  
Sicherungsschicht (engl.: [Link Layer](https://www.netzwerke.com/Netzwerk-Glossar/Link-Layer.html "Link Layer"))**  
Die Aufgabe der Sicherungsschicht ist der zuverlässige Austausch von Datenpaketen zwischen den Systemen. Sie wird in zwei Unterschichten unterteilt: in die MAC-Schicht (Medium Access Control), die an die Bitübertragungsschicht (Schicht 1) grenzt und in die LLC-Schicht (Logical Link Control), die an die Netzwerkschicht (Schicht 3) grenzt. –  
Die **Mac-Schicht** regelt die Nutzung der Übertragungsmedien und schreibt die physikalische Sende- und Empfangsadresse in das Protokoll der Datenpakete. Die **LLC-Schicht** teilt den Bitdatenstrom in Datenrahmen (frames) und führt eine Fehlererkennung und -korrektur durch. – Beispielgeräte, die dieser Schicht zugeordnet werden sind [Bridge](https://www.netzwerke.com/Netzwerk-Glossar/Bridge.html "Bridge") und [Switch](https://www.netzwerke.com/Netzwerk-Switch.htm "Switch").

**Schicht 3  
Netzwerkschicht (engl.: Network Layer)**  
Die Netzwerkschicht steuert den Austausch von Datenpaketen, da diese nicht direkt an das Ziel vermittelt werden können und deshalb mit Zwischenzielen versehen werden müssen. Die Datenpakete werden dann von Knoten zu Knoten übertragen bis sie ihr Ziel erreicht haben. Um das umzusetzen zu können, identifiziert die Netzwerkschicht die einzelnen Netzknoten, baut Verbindungskanäle auf und wieder ab und kümmert sich um die Wegsteuerung (Routing) und die Datenflusssteuerung. – Beispielgerät, das dieser Schicht zugeordnet wird ist ein [Router](https://www.netzwerke.com/Netzwerk-Router.htm "Router").

**Schicht 4  
Transportschicht (engl.: Transport Layer)**  
Die Transportschicht ist die oberste Schicht des Transportsystems (Schicht 1 bis 4) und ist die Schnittstelle zum Anwendungssystem (Schicht 5 bis 7). Die Transportschicht wandelt die Datenpakete laut Protokoll-Informationen um und sorgt für die richtige Zusammensetzung der Pakete beim Empfänger. – [Protokolle](https://www.netzwerke.com/TCP-IP.htm "Protokolle"), die in dieser Schicht genutzt werden: TCP, UDP, SCTP

**Schicht 5  
Sitzungsschicht (engl.: Session Layer)**  
Die Sitzungsschicht ist die unterste Schicht des Anwendungssystems (Schicht 5-7) und baut logische Verbindungen zwischen Sender und Empfänger auf, kontrolliert diese und beendet sie wieder. – Folgende Dienste können in den Schichten 5-7 genutzt werden: FTP, [Telnet](https://www.netzwerke.com/Netzwerk-Glossar/Telnet.html "Telnet"), SMTP

**Schicht 6  
Präsentationsschicht (engl.: Presentation Layer)**  
Die Präsentationsschicht fungiert als Dolmetscher, indem sie die Datenpakete in das jeweilige Format des Sender- oder Empfängerknotens übersetzt. Datenkompression- und verschlüsselung gehören auch zu ihren Aufgaben. – Formate und Codierungen dieser Schicht: ASCII, JPEG, HTML, Unicode

**Schicht 7  
Anwendungsschicht (engl.: Application Layer)**  
Die Anwendungsschicht ist die Schnittstelle zur eigentlichen Benutzeranwendung. Hier werden die Netzwerkdaten in vom Benutzer verwendbare Daten umgewandelt. – Beispielanwendungen: [Internet](https://www.netzwerke.com/Internet.htm "Internet") Explorer, Outlook Express



https://www.coursera.org/de-DE/articles/osi-model





# ISO/OSI-Schichtenmodell

Das ISO (International Standard Organization) / OSI (Open System Interconnection) – Schichtenmodell ist ein **Referenzmodell für Kommunikationsprotokolle** und Rechnernetze als Schichtenarchitektur. Das bedeutet, dass die Kommunikation zwischen zwei Systemen in **verschiedene Schichten unterteilt** ist, mit dem Zweck, die Kommunikation über unterschiedlichste technische Systeme zu ermöglichen. Jede Schicht hat eine **bestimmte Aufgabe** und ist abgeschottet. Es bestehen lediglich **Schnittstellen zu den benachbarten Schichten** um Daten zu übertragen.

## OSI-Schichtenmodell

|   |   |   |
|---|---|---|
|Schicht|Schichtbezeichnung|TCP/IP-Schicht|
|Schicht 7|Anwendungsschicht (Application)|Anwendung|
|Schicht 6|Darstellungsschicht<br><br>(Presentation)|
|Schicht 5|Sitzungsschicht<br><br>(Session)|
|Schicht 4|Transportschicht<br><br>(Transport)|Transport|
|Schicht 3|Vermittlungsschicht<br><br>(Network)|Internet|
|Schicht 2|Sicherungsschicht<br><br>(Data Link)|Netzzugang|
|Schicht 1|Bitübertragungsschicht<br><br>(Physical)|

## Schicht 1

Die **Bitübertragungsschicht** stellt die elektrischen, mechanischen, prozeduralen und funktionalen Hilfsmittel zur Verfügung, um **physische Verbindungen zu verwalten**. Dadurch ist es möglich, einzelne **Bits** durch verschiedene Verfahren über diese Verbindung zu übertragen.

**Protokollbeispiele**: Ethernet, Token Ring, IEEE 802.11

**Netzwerkgeräte**: Hub, Repeater, Netzwerkkabel

## Schicht 2

Die **Sicherungsschicht** ist für die **zuverlässige und fehlerfreie Übertragung** der Daten zuständig. Dazu werden die Daten in Frames aufgeteilt und erhalten jeweils Prüfsummen, mit denen der Empfänger fehlerhafte Pakete erkennen und verwerfen bzw. korrigieren kann. Außerdem wird durch diese Schicht der **Zugriff auf das Übertragungsmedium geregelt** und sie ist für die **MAC-Adresse**, also die physikalische Adressierung des Computers zuständig.

**Protokollbeispiele**: HDLC, PPP, ARP

**Netzwerkgeräte**: Bridge, Switch, Netzwerkkarte

## Schicht 3

Die **Vermittlungsschicht** ist für den **Verbindungsaufbau**, das **Routing** der Frames zwischen verschiedenen Rechnern und die Adressierung der Hostsysteme zuständig. Weitere Aufgaben sind unter anderem das **Erstellen und Aktualisieren einer Routingtabelle** und das **Fragmentieren von Datenblöcken**.

**Protokollbeispiele**: IP, ICMP

**Netzwerkgeräte**: Router

## Schicht 4

Die **Transportschicht** ist dafür zuständig, **ankommende Datenblöcke einer Anwendung zuzuweisen**, da sie die Verbindung zwischen der transportorientierten und anwendungsorientierten Schicht darstellt.

**Protokollbeispiele**: UDP, TCP

## Schicht 5

Die **Sitzungsschicht** **verwaltet die Sitzungen** zwischen verschiedenen Hostsystemen. Dazu gehört auch das Aufbauen und Beenden der Sitzungen und das Bereitstellen von Diensten für einen organisierten und synchronisierten Datenaustausch.

**Protokollbeispiele**: SSH, SMB, RPC, NFS, NetBios

## Schicht 6

Die **Darstellungsschicht** ist nur dafür zuständig, die Daten in ein **geeignetes Format umzuwandeln**, welches von den Anwendungen akzeptiert wird und umgekehrt.

**Protokollbeispiele**: TLS, SSL

## Schicht 7

Die **Anwendungsschicht** ist die Schnittstelle der Anwendungen zur Darstellungsschicht und **stellt diverse Dienste** für diese **zur Verfügung**. Hier findet die **Datenausgabe und -eingabe** statt. Es ist also die Schicht, mit der der Benutzer in Berührung kommt.

**Protokollbeispiele**: DNS, FTP, HTTP, HTTPS, NTP, SSH, Telnet, SMB, WebDav