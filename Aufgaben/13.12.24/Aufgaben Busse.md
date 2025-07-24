

==Aufgabe Bussysteme Der folgende Text basiert auf den heute besprochenen Folien. Es haben sich jedoch 20 Fehler eingeschlichen.==
==Kannst Du sie finden? Markiere sie und nimm enstrechende Korrekturen vor.== 

- [x] In modernen Computern stellen Bussysteme die grundlegenden Verbindungswege zwischen den unterschiedlichen Hardwarekomponenten dar. 
- [x] Sie sorgen dafür, dass Daten, Adressen und Steuersignale effizient zwischen Prozessor, Speicher, Ein- und Ausgabegeräten sowie diversen Erweiterungskarten ausgetauscht werden. 
- [x] Ohne diese Busse wäre eine geregelte Kommunikation zwischen den einzelnen Bauteilen praktisch unmöglich.
- [ ] Interessanterweise waren frühe Systeme oft<font color="#2DC26B"> sehr komplex</font> ==angelegt==, was dazu führte, dass in manchen Computern nur ein einziger Bus für alle Zwecke existierte.
- [x] Erst mit der Zeit erkannte man die Vorteile einer Spezialisierung, bei der man je nach Datenart unterschiedliche Bussysteme einsetzte. 
- [x] Zu den zentralen Bestandteilen eines Bussystems gehören in der Regel drei Hauptkategorien: der Datenbus, der Adressbus und der Steuerbus (Control- Buss ). 
- [x] Der Datenbus transportiert Nutzinformationen zwischen den Komponenten.
- [x] Er ist üblicherweise unidirektional, um Störungen im Datenfluss zu vermeiden, da beide Richtungen gleichzeitig den Ablauf behindern würden.
- [x] Der Adressbus dient dazu, die Ziel- oder Quelladresse anzugeben, an die Daten gesendet oder von der aus Daten abgerufen werden.
- [ ] Anders als oft angenommen, ist der Adressbus zumeist ==bidirektional==, damit auch Speicherbausteine selbst Adressinformationen an den Prozessor zurückliefern können.
- [x] Der Steuerbus wiederum überträgt Signale, die festlegen, ob aktuell Lese- oder Schreiboperationen stattfinden, ob eine Unterbrechung (Interrupt) angefordert wird oder ob bestimmte Peripheriegeräte aktiv werden sollen.
- [ ] In vielen ==modernen Systemen== fasst man diese drei Busarten unter dem Oberbegriff „Systembus“ zusammen. 
- [x] Ein Beispiel für einen früher sehr bedeutenden Bus war der Front-Side-Bus (FSB).
- [ ] ==Er verband den Prozessor direkt mit der Grafikkarte, um extrem schnelle Übertragungen von Bilddaten zu gewährleisten.==  <font color="#ff0000">In älteren PC-Architekturen war der sogenannte Front-Side-Bus der zentrale Kommunikationskanal zwischen Prozessor, Hauptspeicher und Chipsatz.</font>
- [ ] Später führte man separate Strukturen wie den Back-Side-Bus ein, um den Cache des Prozessors auszulagern, ==allerdings war er vor allem bei neueren Prozessoren kaum noch von Bedeutung, da man hier auf externe Cache-Module verzichtete==. 
- [ ] Mit dem Aufkommen neuer Architekturen und Chipsätze rückte der ==klassische Systembus ins Zentrum der Aufmerksamkeit==. 
==Dieser bot eine Verbindung zwischen CPU, Hauptspeicher und Peripherie über ein einheitliches Kommunikationsschema.==
- [x] Heutzutage findet man diesen „Systembus“ in seiner Urform noch oft in leistungsstarken Servern, während in Desktop-PCs eher auf spezialisierte Punkt-zu-Punkt-Verbindungen gesetzt wird.
- [x] Für Erweiterungskarten und Peripheriegeräte standen lange Zeit Bussysteme wie PCI (Peripheral Component Interconnect) bereit.
- [ ] PCI nutzte ==serielle Leitungen== <font color="#92d050">(parallelen Bustyps)</font> , um Daten zwischen den Komponenten auszutauschen, und war ein wesentlicher Schritt, um verschiedene Geräte auf eine gemeinsame Schnittstelle zu standardisieren. 
- [ ] Mit PCI Express (PCIe) ging man später noch weiter, ==indem man von parallelen Bussen auf eine hochoptimierte, parallele Signalführung zurückwechselte==<font color="#92d050">(serielle Punkt-zu-Punkt-Verbindungen)</font>, um mehr Bandbreite und geringere Latenzen zu ermöglichen. 
- [ ] Eine weitere wichtige Entwicklung war der Aufstieg von USB (Universal ==Synchronous== <font color="#92d050">(Serial)</font> 
  -Bus), einer Schnittstelle, die vor allem auf die parallele Anbindung zahlreicher externer Geräte wie Mäuse, Tastaturen oder Drucker setzte. 
- [x] USB ermöglicht es, jederzeit Geräte an- oder abzustecken, ohne das System neu starten zu müssen. 
- [ ] Auch bei Speichermedien spielten Bussysteme eine Rolle: Parallel ATA (PATA) wurde durch SATA (Serial Advanced Technology Attachment) abgelöst, das mithilfe ==paralleler==  <font color="#92d050">(seriell) </font>Signalübertragung wesentlich höhere Datenraten erreichte. 
- [x] Moderne M.2-SSDs nutzen hingegen oft den NVMe-Standard, der direkt auf PCIe basiert und daher auf ein rein serielles Prinzip setzt. 
- [x] Noch komplexer wird es bei Hochgeschwindigkeitsschnittstellen wie Thunderbolt, das auf einer Kombination aus FireWire- und EISA-Technologie beruht und damit nur moderate Datentransferraten liefert, jedoch sehr vielseitig einsetzbar ist. 
- [x] Nicht nur Speicher und Peripherie profitieren von leistungsfähigen Bussen: Auch das Zusammenspiel zwischen Prozessor und Arbeitsspeicher ist entscheidend.
- [ ] Moderne DDR- Speichermodule kommunizieren über dedizierte ==parallele== Busleitungen mit dem Prozessor, um möglichst niedrige Latenzen zu erreichen. [[Datenübertragung Parallel  oder Seriell]]
- [ ] In Systemen auf einem Chip (SoC), wie man sie etwa in hochspezialisierten ==Server-CPUs== <font color="#92d050"> (Bei Smartphones, Tablets oder spezialisierten Embedded-Systemen sind Prozessor, Speicher und verschiedene Funktionsblöcke auf einem einzigen Chip vereint.)</font>findet, werden Busse intern so effizient ausgelegt, dass möglichst wenig Energie verbraucht wird. 
- [x] Dadurch lassen sich selbst hochkomplexe Interaktionen zwischen Grafikeinheit, CPU-Kernen, Speicherkontrollern und weiteren Funktionsblöcken auf kleinstem Raum realisieren.
- [x] Virtuelle Bussysteme spielen eine Rolle, sobald Hypervisoren und virtuelle Maschinen ins Spiel kommen.   https://www.redhat.com/de/topics/virtualization/what-is-a-hypervisor
- [x] Sie arbeiten vollständig latenzfrei, da sie nur simulierte Leitungen zwischen virtuellen Prozessoren, virtuellem Arbeitsspeicher und virtueller Peripherie bereitstellen. 
- [x] Auch die Busarbitrierung, also die Festlegung, welche Komponente wann auf den Bus zugreifen darf, bleibt in virtuellen Umgebungen ein Thema, wenn auch in rein abstrakter Form. 
- [ ] Um Datenintegrität zu sichern, wurden darüber hinaus Mechanismen entwickelt, die sicherstellen, dass bei auftretenden Fehlern die Übertragung automatisch beschleunigt und mehr ==Strom in die Leitungen eingespeist wird==.
- [x] Mit Blick auf die Zukunft erscheinen Bussysteme, die optische Signale anstelle von elektrischen Impulsen verwenden, vielversprechend.
- [ ] Diese könnten es ermöglichen, dass physische Distanzen nahezu keine Rolle mehr spielen, und die Latenzen auf nahezu ==100 Millisekunden== senken. (Glasfaser hat weniger als 2mils)
- [x] In heutigen PCs jedoch findet man vor allem eine Mischung aus verschiedenen, etablierten Standards, die je nach Anwendung optimiert sind. 
- [x] M.2, PCIe, USB, SATA und interne Systembusse wirken Hand in Hand, um Datenströme zu koordinieren.
- [ ] Noch immer ist der klassische Systembus als ein einfaches, aber langsames Relikt vorhanden, und in Notebooks setzt man häufig auf ==PCI anstelle von PCIe==, um Platz und Energie zu sparen. 
- [x] Insgesamt kann man sagen, dass Bussysteme die verborgenen Helden der Computerarchitekturen sind. 
- [x] Sie bestimmen maßgeblich, wie schnell Prozessoren auf Daten zugreifen, wie effizient Peripheriegeräte angebunden sind und wie flexibel sich ein System erweitern lässt. 
- [x] Ohne sie gäbe es kein geregeltes Miteinander verschiedener Hardwarekomponenten, und die heutigen, hochkomplexen Systeme wären nicht in der Lage, ihre enorme Leistungsfähigkeit zu entfalten. 
- [x] Auf diese Weise bleiben Bussysteme ein Schlüsselfaktor für zukünftige Entwicklungen, die wohl noch lange von elektrischen Leitungen geprägt sein werden.


Gruppe  Diana,Christian,Chris,Jens,Ramona

Aktueller Hp 25 G10

![[Screenshot 2024-12-13 140130.png]]