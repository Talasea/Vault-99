
# Das Bussystem

Das _**Bussystem**_ bezeichnet die Verbindung zwischen einzelnen Komponenten, die zur **Kommunikation** untereinander dient. Dabei wird zwischen dem **lokalen** und **peripheren** bzw. zwischen dem **seriellen** und **parallelen Bussystem** unterschieden. Die Kommunikation wird mithilfe der **Initiator**- und **Follower**-Rollenverteilung gesteuert.

---

## Lokales vs. peripheres Bussystem

Das _**Bussystem**_ dient zur **Kommunikation** zwischen den einzelnen **Computerkomponenten**.

Dabei handelt es sich um **Verbindungen** - genauer **elektronische Leitungen** -, über die Daten zwischen den einzelnen Komponenten **gesendet und empfangen** werden.

Dabei wird in das **lokale** und das **periphere Bussystem** bzw. in den **internen** und **externen Bus** unterschieden:

- **Lokales Bussystem**: Starre Leitungen auf dem Motherboard (**interner Bus**)
- **Peripheres Bussystem**: Flexible Leitungen zwischen den Computerkomponenten (**externer Bus**)

## Lokales Bussystem

Alle Computerkomponenten, die **direkt** mit dem **Prozessor** verbunden sind, werden am **Motherboard** angeschlossen. Diese werden mithilfe eines **lokalen Bussystems** elektrisch verbunden:

![Lokales Bussystem](https://api.simpleclub.com/v2/language_areas/de/assets/gK40tLq5UqRKignLvSgQ/files/7bc0c746-b15b-444a-9b4b-6ec1efa68486.svg)## Peripheres Bussystem

An das **lokale Bussystem** ist über eine **Erweiterungsschnittstelle** das _**periphere Bussystem**_ angeschlossen.

Dieses verbindet das **Motherboard** mit der **Peripherie**, also zum Beispiel Laufwerke, Ein- und Ausgabegeräte und Anschlüsse.

App öffnen zum Interagieren

NeustartPeriphäres Bussystem

App öffnen zum Interagieren

## Steuerung der Kommunikation

Da eigentlich **alle** an ein Bussystem angeschlossenen Komponenten **Daten senden und empfangen** können, muss verhindert werden, dass mehrere Komponenten **gleichzeitig** Daten senden und empfangen.

Außerdem muss auch dafür gesorgt werden, dass **nur die Komponenten empfangsbereit** sind, für die die aktuellen Daten **relevant** sind.

Diese **Verwaltung** erfolgt entweder direkt über den **Prozessor**, aber manchmal auch über einen eigenen **Bus-Controller**.

Hierbei werden den Komponenten festgelegte Zeiten zugeteilt, zu denen sie kommunizieren dürfen.

## Initiator und Follower

Bei dieser **Kommunikation** wird in zwei verschiedene Arten von **Knoten** (also **Kommunikationspartnern**) unterschieden:

- **Initiator**
- **Follower**

Der _**Initiator**_ kann selbstständig eine Kommunikation auf dem Bus **initiieren**.

Er darf also unaufgefordert Daten an andere Knoten senden.

Die _**Follower**_-Knoten hingegen sind passiv, das heißt, sie dürfen nur auf Anfragen **antworten**.

Schau dir das am besten am folgenden Beispiel an:

![Initiator vs Follower](https://api.simpleclub.com/v2/language_areas/de/assets/949pLhYyfiiFiWCTiD6F/files/3193bc67-44ec-4cb9-80e2-9a4488a3dba2.svg)

Nehmen wir mal an, der **Prozessor** möchte mit dem **Arbeitsspeicher** kommunizieren.

Der Prozessor ist dann in dieser Kommunikation der **Initiator**, das heißt, er kann Daten an den Arbeitsspeicher - hier also der **Follower** - senden.

Der Arbeitsspeicher kann hingegen aufgrund seiner Rolle nur dann Daten senden, wenn ihn der Prozessor dazu auffordert.

Diese Rollenverteilung ist gerade bei sehr komplexen Verbindungen, wie sie zum Beispiel im Computer vorliegen, sehr wichtig, damit die Kommunikation über das Bussystem problemlos und ohne Datenverlust funktionieren kann.

## Serielles vs. paralleles Bussystem

Bei einem Bussystem spielt neben der **Art** des Systems auch die _**Breite**_ eine wichtige Rolle. Diese beschreibt dabei die **Anzahl an Leitungen** eines Busses.

→→ Je **mehr Leitungen** ein Bus also hat, desto **breiter** ist er.

In einem Computer gibt es zwei verschiedene Bussysteme, die sich in diesem Merkmal unterscheiden:

- _**Serielles Bussystem**_: Daten werden Bit für Bit **hintereinander** über **ein** Datenkanal gesendet.
- _**Paralleles Bussystem**_: Über **mehrere** Datenkanäle können **gleichzeitig** Daten versendet werden.

## Serielles Bussystem

Das **serielle Bussystem** besteht aus nur **einer** Leitung. Deswegen können die Daten auch nur _nacheinander_ (also _seriell_) übertragen werden.

Du kannst dir einen seriellen Bus wie eine **Einbahnstraße** vorstellen:

![Serielles Bussystem](https://api.simpleclub.com/v2/language_areas/de/assets/S3FD6ZgMgsJfQKPZkv6t/files/a2695690-e1f1-469e-9161-68e3d2763cb1.svg)

Auf einer **Einbahnstraße** fahren alle Autos **hintereinander** und wenn einer anhält, müssen auch alle anderen stoppen.

Dadurch ist der **serielle Bus** zwar langsam, aber auch **günstig**, da nur **eine Leitung** verwendet wird.

Er wird außerdem eher für **lange Strecken** verwendet.

→→ Zum Beispiel als Verbindung zwischen dem **Motherboard** und den **Ein- und Ausgabegeräten**.

## Paralleles Bussystem

Das _**parallele Bussystem**_ besteht aus mehreren **parallelen Leitungen**.

→→ Dadurch können **mehrere** Daten **gleichzeitig** verschickt werden.

Du kannst dir den **parallelen Bus** also wie eine **mehrspurige Autobahn** vorstellen:

![Paralleles Bussystem](https://api.simpleclub.com/v2/language_areas/de/assets/anFHJ7tfb6NxDrgNu7LQ/files/71fce33b-2f7a-4668-bb5b-4614ce8e83b0.svg)

Das **parallele Bussystem** wird im Gegensatz zum **seriellen Bussystem** eher für **kurze Distanzen** verwendet.

→→ Zum Beispiel für die Verbindung zwischen **Prozessor** und **Speicher**.

## Der bekannteste serielle Bus

Der wohl bekannteste **serielle Bus** ist der _**USB**_, also _**Universal Serial Bus**_.

Die meisten Geräte werden über ihn an den Computer angeschlossen.

Auch hier werden die Daten **seriell** übertragen. Das bedeutet, dass die Daten **Bit für Bit** von einem Gerät auf das andere übertragen werden.

Dabei kann außerdem in beide Richtungen gesendet und empfangen werden, weswegen man hier auch von einer **I/O-Schnittstelle** spricht.

Bei einer **externen Festplatte** zum Beispiel können also über den USB-Anschluss Daten von dem Computer auf die Festplatte bzw. von der Festplatte auf den Computer geladen werden:

![USB](https://api.simpleclub.com/v2/language_areas/de/assets/s4utYgpfs20DXIsMdWZ9/files/782770e4-b712-4144-925c-337cb48e5910.svg)

Da jedoch die Anforderungen seit der Entwicklung des ersten USBs stark gestiegen sind, gibt es mittlerweile viele weitere USB-Typen, wie den **USB 2.0**, **USB 3.0** oder **USB 3.1**, welche eine **schnellere Übertragungsrate** als der ursprüngliche USB haben.


#####

Daten buss

Ein Datenbus ist ein Verbindungssystem zur Übertragung von Informationen zwischen digitalen Schaltwerken, wie zum Beispiel zwischen Prozessor, Arbeitsspeicher und Peripheriegeräten. Es ermöglicht die Kommunikation zwischen verschiedenen Komponenten eines Computersystems oder eines Automobils.

## Grundlagen

Ein Datenbus besteht aus einer oder mehreren Leitungen, über die Daten zwischen den angeschlossenen Komponenten übertragen werden. Die Anzahl der Leitungen bestimmt die Breite des Busses und damit die Anzahl der Bits, die pro Takt übertragen werden können.

Es gibt verschiedene Arten von Datenbussen:

- **Paralleler Datenbus**: Mehrere Leitungen nebeneinander, über die synchronisierte Informationen übertragen werden.
- **Serieller Datenbus**: Eine Leitung, über die nacheinander Informationen übertragen werden.

## Funktionen

Ein Datenbus ermöglicht:

- Die Übertragung von Daten zwischen verschiedenen Komponenten eines Systems.
- Die Adressierung von Zielkomponenten, um sicherzustellen, dass Daten an den richtigen Empfänger gesendet werden.
- Die Steuerung von Zugriffen auf den Bus, um Konflikte zwischen mehreren Komponenten zu vermeiden.

## Beispiele

- Im Automobilbau werden Datenbusse wie CAN (Controller Area Network) oder LIN (Local Interconnect Network) verwendet, um verschiedene Systeme wie z.B. die Klimaanlage, die Sitze und die Navigation zu verbinden.
- Im Computerbau werden Datenbusse wie ISA (Industry Standard Architecture), PCI (Peripheral Component Interconnect) oder USB (Universal Serial Bus) verwendet, um Peripheriegeräte wie z.B. Tastaturen, Maus und Grafikkarten zu verbinden.

## Merkmale

Ein Datenbus hat folgende Merkmale:

- **Breite**: Die Anzahl der Leitungen, über die Daten übertragen werden.
- **Takt**: Die Frequenz, mit der Daten übertragen werden.
- **Adressierung**: Die Methode, mit der Zielkomponenten identifiziert werden.
- **Steuerung**: Die Art, wie Zugriffe auf den Bus gesteuert werden.









# Das Bussystem des 8051

Ein Bus ist eine Sammelleitung für Daten zur Datenübertragung. Die einfachste Form eines Busses sind parallele Kabel. Ein 8-Bit Bus überträgt 8 Bit auf einmal und besitzt somit 8 parallele Leitungen. Der 8051 Mikrocontroller hat 3 unterschiedliche Bussysteme, welche nach ihren Aufgaben unterschieden werden. Es gibt den Datenbus, den Adressbus und den Steuerbus.

![8051 Bussystem](https://www.holzers-familie.de/schule/book/img/bus.png)  
Abb 1: Das Bussystem des 8051

## Der Steuerbus

Der Steuerbus ist 8 Bit breit und transportiert Steuersignale. Diese Signale bestimmen, ob in den Speicher geschrieben oder von ihm gelesen wird. Er legt ebenso fest, welche Operation die ALU ausführt bzw. welches Ergebnis die ALU ausgibt.

## Der Datenbus

Er transportiert die Daten und hat wie der Steuerbus eine Breite von 8 Bit. Auf diesem Bus gelangen Befehle aus dem ROM zum Steuerwerk, ebenso wie Konstanten aus dem ROM zur Alu. Der Datenbus transportiert Daten vom internen Speicher (RAM) an die Alu und Ergebnisse von der Alu in den Speicher.

## Der Adressbus

Der Adressbus hat eine Breite von 16 Bit und gibt die Adresse des nächsten Befehls im ROM an. Wird aus dem RAM gelesen oder in ihn geschrieben, so muss vorher die Adresse der betreffenden Speicherzelle über den Adressbus übermittelt werden. Die ausgelesenen Daten legt der jeweilige Speicher auf den Datenbus. Da der Adressbus 16 Bit breit ist hat das ROM eine maximale Größe von 64kb (=216 Byte).

## Anbindung an den Bus

Bindet man Speicherzellen parallel an den Datenbus an, wie es in Abbildung 2 dargestellt ist, treten mehrere Probleme auf. Zum einen lesen alle Speicherzellen gleichzeitig Daten vom Bus, so dass alle Speicherzellen stetig den gleichen Wert haben. Zum anderen schreiben alle Speicherzellen gleichzeitig auf den Bus. Werden unterschiedliche Werte auf den Bus geschrieben, also 0 und 1, so kommt es zu einem Kurzschluss.

![falsche Busanbindung 1](https://www.holzers-familie.de/schule/book/img/busconnect1.png)  
Abb 2: falsche Busanbindung 1

Die in Abbildung 3 dargestellte Modifikation bringt die Verbesserungen, dass jede Speicherzellen ein eigenes Schreib- und Lesesignal besitzen. Hierdurch können Speicherzellen gezielt zum Schreiben (write) angesteuert werden, indem man das Write-Signal auf 1 setzt. Ist das Write-Signal 0, so nimmt das statische Flip-Flop keine Werte in seinen Speicher auf.  
Das Und-Gatter am Ausgang liefert den gespeicherten Wert nur an den Bus, falls das Read-Signal auf 1 gesetzt ist.  
Allerdings kommt es auch hier noch zu Kurzschlüssen auf dem Bus, da ein Und-Gatter immer entweder 0 (-5V) oder 1 (+5V) ausgibt. Somit kommt es zum Kurzschluss, wenn ein Speicherbit auf 1 steht und das zugehörige Read-Signal ebenfalls auf 1 steht. Da alle anderen Speicherzellen das Read-Signal 0 bekommen, schließt die 1 sich mit den 0-Signalen der anderern Flip-Flops kurz.

![falsche Busanbindung 2](https://www.holzers-familie.de/schule/book/img/busconnect2.png)  
Abb 3: falsche Busanbindung 2

Um das Kurzschlussproblem zu lösen, benötigt man ein zusätzliches Bauteil, welches Tri-State heißt und in Abbildung 4 dargestellt ist. Dieses Bauteil liefert das Signal am `in`-Eingang an den `out`-Ausgang weiter, falls das Signal `on` auf 1 steht. Ist das `on`-Signal auf 0 so ist der Ausgang `out` hochohmig. Das heißt es fließt kein Strom weder -5V noch +5V, sondern es verhält sich so, als ob das Bauteil nicht am Bus angeschlossen wäre. Somit kommt es zu keinen Kurzschlüssen, wenn man mehrere Ausgänge parallel anschließt.

![Tristate](https://www.holzers-familie.de/schule/book/img/tristate.png)  
Abb 4: Tri-State

Baut man in den Entwurf aus Abbildung 3 je ein Tri-State zwischen dem Und-Gatter und dem Bus ein, so kommt es zu keinen Kurzschlüssen mehr. An den Eingängen der Speicher ist keine Modifikation nötig, da hier nur gelesen und nicht geschrieben wird. Diese Tri-State-Bauteile werden auch Bustreiber genannt. Hierbei handelt es sich um Hardware-Treiber-Bausteine, welche nicht mit Software-Treibern von Betriebssystemen verwechselt werden sollten.

![Busanbindung](https://www.holzers-familie.de/schule/book/img/busconnect3.png)  
Abb 5: Busanbindung
