Der Layer 3 im ISO/OSI-Schichtenmodell ist für die Vermittlung der Daten über die einzelnen Verbindungsabschnitte und Netzwerkknoten hinweg zuständig. Er kümmert sich um die Adressierung der Kommunikationspartner und das Finden des schnellsten oder günstigsten Wegs zum Ziel.

Weitere Bezeichnungen für den Layer 3 sind Vermittlungsschicht, Netzwerkschicht oder Network Layer. Die Schicht 3 findet einen Weg vom Empfänger zum Sender und überträgt die Datenpakete über die einzelnen Netzwerkknoten hinweg.

Im [TCP](https://www.ip-insider.de/was-ist-tcp-a-814290/)/[IP](https://www.ip-insider.de/was-ist-ip-a-812352/)-Umfeld nennt sich die Wegfindung durch das IP-Netz [Routing](https://www.ip-insider.de/was-ist-der-unterschied-zwischen-routing-und-switching-a-1077049/). Das Routing kann sowohl statisch vordefiniert sein als auch dynamisch erfolgen. In den einzelnen Netzwerkknoten (Routern) zwischen der Quelle und dem Ziel werden die Informationen des Layer 3 wie beispielsweise die Ziel- und Absenderadressen ausgewertet und für das Routing verwendet. Hierfür stellt der Network Layer ein eindeutiges Adresskonzept zur Verfügung.

Da auf den einzelnen Teilnetzen unterschiedliche Übertragungsverfahren und -medien zum Einsatz kommen können, enthält die Schicht 3 die Funktionen zur Umsetzung und Weiterleitung der Daten über die unterschiedlichen Teilnetze hinweg. Ebenfalls in der Schicht 3 können Abrechnungsfunktionen angesiedelt sein. Typische Protokolle des Layer 3 sind das Internet Protokoll (IP) oder X.25.

### Die typischen Aufgaben der Schicht 3

Die beiden Hauptaufgaben, um die sich die Schicht drei kümmert, sind die logische Adressierung der Kommunikationspartner und die Wegfindung über die Teilabschnitte eines Netzwerks hinweg. Neben der logischen Adressierung und dem Routing erfüllt die Schicht 3 die folgenden weiteren Aufgaben:

- das Verpacken der Daten höhere Schichten in Layer-3-Pakete und das Hinzufügen der für die Vermittlung benötigten Informationen im Paket-Header

- die Fragmentierung der Daten in für die Übertragungsstrecke geeignet große Datenpakete

- das Wiederzusammensetzen der fragmentierten Datenpakete

- die Aushandlung und Bereitstellung von Dienstgüten auf dem Übertragungsweg

- die Fehlerbehandlung und Diagnose

- die Flusskontrolle zwischen den Kommunikationspartnern und dem Vermittlungssystem

- das Zwischenspeichern (Buffern) von Daten

Je nach Kommunikationsnetz kann das Routing der Daten zwischen zwei Kommunikationspartnern immer auf dem gleichen Weg oder von Paket zu Paket auf unterschiedlichen, jeweils optimalen Routen erfolgen. Nehmen einzelne Pakete zum gleichen Ziel unterschiedliche Wege, kann es unter Umständen vorkommen, dass sie dort in der falschen Reihenfolge ankommen. In diesem Fall übernimmt der [Layer 4](https://www.ip-insider.de/was-ist-layer-4-a-651857/) die Aufgabe, die Pakete einer Verbindung wieder in die korrekte Reihenfolge zu sortieren.

### Typische vom Layer 3 verursachte Netzwerkprobleme

Aufgrund von Fehlern in der Vermittlungsschicht können verschiedene Netzwerkprobleme verursacht werden. Sind beispielsweise Adressen doppelt vergeben, lassen sich Datenpakete nicht mehr eindeutig einem Kommunikationspartner zustellen. Fehlerhaftes Routing kann zu Schleifen (Loops) bei der Datenvermittlung führen, bei denen die Datenpakete immer wieder zwischen einzelnen Netzknoten hin und her gesendet werden, ohne dass sie ihr eigentliches Ziel erreichen. Ein weiteres typisches Fehlerbild des Layer 3 sind falsche Paketgrößen. Ist ein Paket größer als die maximal übertragbare Paketgröße eines bestimmten Teilabschnitts und eine Fragmentierung nicht möglich, ist das Datenpaket zu verwerfen.