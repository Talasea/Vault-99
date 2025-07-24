### Aufbau einer Festplatte

![Prinzipaufbau einer Festplatte / Harddisk](https://www.elektronik-kompendium.de/sites/com/bilder/06102911.gif)  
In einem geschlossenen Metallgehäuse befinden sich alle Komponenten, die für das Funktionieren der Festplatte wichtig sind. Um das Eindringen von Staub und Schmutz in das Gehäuse zu verhindern, sind die einzelnen Teile einer Festplatte in ein nahezu luftdichtes Gehäuse verschlossen. Als einziger Kontakt zum Computersystem dient eine Anschlussleiste für eine Schnittstelle (IDE, SATA, SCSI, etc.), über die die Daten übertragen werden.  
Der eigentliche Datenspeicher einer Festplatte ist eine oder mehrere Metallscheiben, die mit einem magnetisierbaren Material beschichtet sind. Um die Speichermenge zu erhöhen liegen mehrere Scheiben übereinander. Die Scheiben sind um eine Drehachse mittels Halteklammern befestigt und dadurch voneinander getrennt. Zwischen den Metallscheiben greifen die Schreib-Lese-Kopf-Arme hinein. Auf diesen Armen befindet sich eine federnde Aufhängung. Auf dieser ist der Kopf befestigt, der zum Lesen und Schreiben der Daten dient.  
![Größenvergleich](https://www.elektronik-kompendium.de/sites/com/bilder/06102913.gif)  
Der Abstand zwischen Kopf und Scheibe ist geringer, als ein Haar, Staub- oder Rauchpartikel. Die Berührung von Kopf und Scheibe führt zum Head-Crash, der wiederum zum Datenverlust führt. Dabei wird der Datenträger zerstört, was die Festplatte unbrauchbar macht. Normalerweise können sich Kopf und Platte nicht berühren. Denn bei hohen Rotationsgeschwindigkeiten, bei der sich eine Festplatte dreht, bildet sich ein Luftpolster zwischen Kopf und Platte.  
Die Schreib-Lese-Arme werden von einem Motor gesteuert, der zur Kopfpositionierung dient. Zur Steuerung des Motors befindet sich direkt daneben die Armelektronik. Unterhalb dieser ganzen Konstruktion befindet sich die Platine, auf der sich die Laufwerkselektronik befindet.  
Während des Festplattenbetriebs rotieren die Scheiben ständig. Während des Schreib- oder Lese-Vorgangs werden die Arme und damit die Köpfe hin und her bewegt. Damit die Schreib-Lese-Köpfe beim Transport keinen Schaden nehmen, werden die Arme beim Stromverlust in eine Parkposition gebracht und arretiert. Der dafür nötige Strom wird von einem Generator erzeugt, der die Schwungmasse der Plattenrotation ausnutzt. So ist es möglich, dass die Parkposition auch bei einem plötzlichen Stromausfall eingenommen werden kann.

### Geschwindigkeit einer Festplatte

Je schneller eine Festplatte ist, desto flüssiger laden die Daten und laufen die Programme. Besonders beim Start von Betriebssystem und Anwendungen spürt der Anwender eine schnelle Festplatte. Und nur mit einem schnellen Massenspeicher speichert ein Computer große Datenmengen mühelos. Folgende vier Kriterien machen eine Festplatte schnell:

##### Umdrehungsgeschwindigkeit

Die Umdrehungsgeschwindigkeit wird in Umdrehungen in der Minute (UPM, U/Min) angegeben. Je geringer die Drehzahl, desto länger dauert der Zugriff auf zufällig ausgewählte Sektoren.  
Üblich sind die Umdrehungsgeschwindigkeiten 10.000, 7.200 und 5.400 U/Min. Sehr schnelle Festplatten laufen mit 10.000 U/Min. Dafür bedarf es einer zusätzlichen Kühlung. Deshalb findet man sie selten in normalen PCs. Normale Festplatten laufen mit 7200 U/Min. Das ist die Standardumdrehungsgeschwindigkeit. Geräuscharme und Strom sparende Festplatten laufen mit 5.400 U/Min.

##### Anzahl der Datenscheiben

Je mehr Datenscheiben eine Festplatte hat, desto höher ist ihre Kapazität. Doch auch die Lese- und Schreibgeschwindigkeit steigt, wenn der Datenstrom über mehrere Lese- und Schreibköpfe summiert wird.

##### Datendichte auf den Datenscheiben

Je höher die Datendichte, desto mehr Bit ziehen pro Sekunde am Schreib-Lese-Kopf vorbei und können gelesen oder geschrieben werden.

##### Zugriffszeit / Access Time / Datenzugriffszeit

![Zugriffszeit Festplatte](https://www.elektronik-kompendium.de/sites/com/bilder/06102916.gif)  
Die Zugriffszeit gibt an, wie lange es dauert, bis die Festplatte die gewünschten Daten auf ihren Datenschreiben gefunden hat und die ersten Bit liefert. Die Zugriffszeit ist die Summe aus Such- und Latenzzeit und wird hauptsächlich von der Umdrehungsgeschwindigkeit der Festplatte bestimmt. Je schneller sich die Platte dreht, desto geringer ist diese Zeit.  
Doch die Zugriffszeit hängt noch von zwei weiteren Faktoren ab: Als erstes braucht der Lese-/Schreibkopf eine bestimmte Zeit, um sich über eine bestimmte Spur zu platzieren (mittlere Suchzeit). Danach dauert es etwas, bis die Daten unter dem Lesekopf vorbeikommen (Latenzzeit). Im Schnitt benötigt die Platte eine halbe Umdrehung. Von der Anfrage, zur Positionierung des Lese-/Schreibkopfes auf der gewünschten Spur und Erscheinen des richtigen Sektors, bis zur Auslieferung der Daten können zwischen 4 und 20 Millisekunden vergehen.  
Ein weiterer Faktor beeinflusst die Zugriffszeit. Zum Beispiel, wenn wegen Fragmentierung viele Sektoren an verschiedenen Stellen der Festplatte gelesen und geschrieben werden müssen. Dann müssen die Datenscheiben öfter gedreht werden, bis der Lesekopf an allen Sektoren vorbeigekommen ist. Besser ist es, wenn die zu lesenden Daten in einem Stück hintereinander abgelegt sind. In dem Fall hilft eine Defragmentierung.

### Schreib-Lese-Verfahren: Longitudial Magnetic Recording (LMR)

![Longitudial Recording](https://www.elektronik-kompendium.de/sites/com/bilder/06102914.gif)  
Ein Schreibkopf wird über die magnetisierbare Scheibe bewegt. Im Kopf befinden sich eine Spule, die von einem Strom durchflossen wird. Das entstehende Magnetfeld magnetisiert die Stelle unter dem Kopf. So entstehen viele kleine magnetisierbare Bereich, die kreisförmig auf der Scheibe angeordnet sind.  
Beim Lesen induzieren die kleinen magnetischen Bereiche ein Magnetfeld in der Spule des Kopfes. Es wird eine Spannung induziert. Diese wird verstärkt und als Datenstrom ausgelesen.  
Im Laufe der Zeit, von der ersten Festplatte bis heute, wurden die Schreib- und Lesevorgänge immer schneller und die Speicherstruktur immer kleiner. Diese Speicherstruktur muss man sich wie winzige Stabmagneten vorstellen, die in einer langen Kette hintereinander liegen. Man nennt dieses Schreib-Lese-Verfahren Longitudial Magnetic Recording. Mit diesem Verfahren werden 120 GBit pro Quadratzoll Speicherdichte erreicht. Dieser Wert gilt als Grenze, bis zu der sich der superparamagnetische Effekt in den Griff bekommen lässt. Beim superparamagnetischen Effekt reichen bereits geringfügige äußere Einflüsse, z. B. Temperaturschwankungen, um die magnetische Ausrichtung der Speicherbereiche umzukehren. Die Daten wären dann verloren.

### Schreib-Lese-Verfahren: Perpendicular Magnetic Recording (PMR)

![Perpendicular Recording](https://www.elektronik-kompendium.de/sites/com/bilder/06102915.gif)  
Perpendicular Magnetic Recording geht auf die Forschung des dänischen Wissenschaftlers Valdemar Poulsen zurück. Im späten 19. Jahrhundert zeichnete er Töne erstmals mit Perpendicular Magnetic Recording magnetisch auf.  
Der Name dieser Aufzeichnungstechnik kommt von der vertikalen Anordnung der Speicherbereiche auf der Oberfläche der magnetischen Scheibe. Der wesentliche Unterschied, im Vergleich zum Longitudial Magnetic Recording, ist der geringe Platzverbrauch jedes einzelnen Speicherbereichs. Man spricht davon, dass 1 Terabit pro Quadratzoll möglich ist.  
Für Perpendicular Recording muss ein neuer Schreibkopf und ein neues Speichermedium her. Die Feldlinien müssen über den Schreibkopf senkrecht in das Medium eindringen, um eine senkrechte Magnetisierung eines Speicherbereichs zu ermöglichen. Deshalb hat der Schreibkopf zwei unterschiedliche Schenkel. Im Medium wird der obere Schreibkopf durch eine zweite untere magnetische Schicht gespiegelt. Dieser Magnet ist nicht wirklich da. Die untere Schicht verhält sich jedoch so, also ob es ihn geben würde. Die Feldlinien treten aus dem breiten Schenkel heraus und in den dünnen Schenkel hinein. Die senkrecht verlaufenden Feldlinien erzeugen einen senkrecht ausgerichteten Speicherbereich.  
Zum Lesen der Speicherbereiche wird ein normaler Lesekopf verwendet.

Perpendicular Magnetic Recording ist an seine technischen Grenzen gestoßen. Um die Speicherkapazität zu steigern, werden zusätzliche magnetische Platten eingebaut, damit man bei derselben Gehäusegröße bleiben kann.

### Organisation der Daten auf einer Festplatte (Spuren und Sektoren)

![Speicherorganisation](https://www.elektronik-kompendium.de/sites/com/bilder/06102912.gif)  
Damit die Daten, die auf den magnetischen Platten abgelegt sind, wieder gefunden werden, ist es notwendig eine Einteilung der Magnetscheiben vorzunehmen. Als erster Schritt wird eine herstellerseitige Low-Level-Formatierung vorgenommen. Dazu werden auf den Scheiben Spuren angelegt. Es handeln sich dabei um konzentrische Kreise, die auf allen Magnetscheiben gleich sind. Die Spuren werden vom äußeren Rand der Platte nach innen, beginnend bei 0, durchnummeriert. Der Abstand der Spuren, die Spurdichte, bestimmt die Speichermenge. Diese Dichte wird in Spuren pro Zoll (Tracks per Inch, TPI) angegeben.  
Die Anordnung mehrerer Spuren (durch übereinander gelagerte Magnetscheiben) nennt man Zylinder.  
Die Spuren werden wiederum in kleinere Abschnitte eingeteilt. Dieser Abschnitt nennt sich Sektor und entspricht einem Kreisausschnitt.

### Sektorengröße

Der Speicherplatz auf Festplatten ist in Spuren und Sektoren eingeteilt. Alle Festplatten hatten mit 512 Byte lange Zeit die gleiche Sektorengröße. Auch spezielle Festplatten, die intern mit einer Sektorgröße von 4 kByte arbeiteten, gaben nach außen hin 512 Byte große Sektoren an. Intern bilden diese Festplatten acht logische 512-Byte-Sektoren auf einem physikalischen 4-kByte-Sektor ab. Durch die Umrechnung wurde die Festplatten allerdings langsamer.  
Für solche Festplatten wurde die Bezeichnung Advanced Format Drives (AFD) verwendet und zusätzlich ein "512e" angehängt. Das "e" steht dabei für emulated. Das bedeutet, bei 512e werden die 512 Byte großen Sektoren auf einer 4-kByte-Sektoren-Festplatte nur emuliert.

**Seit Mitte 2014 sind Festplatten mit 4 kByte Sektorengröße im Handel, die 4 kByte auch nach außen hin bekannt geben. Man bezeichnet das als "4 kByte native" oder kurz "4Kn".**

Die Umstellung von "512e" auf "4Kn" hat natürlich Konsequenzen. Und zwar abhängig vom Betriebssystem und Dateisystem. Man kann nicht mehr in den Laden gehen und einfach eine beliebige Festplatte mit der gewünschten Speicherkapazität kaufen. Man muss vorher klären, ob Betriebssystem, Dateisystem und sonstige Hardware auch mit 4Kn-Festplatten klarkommen. Während einer Übergangsphase ist also mit Schwierigkeiten und Missverständnissen zu rechnen. Es ist aber davon auszugehen, dass in mittlerer Zukunft nur noch 4Kn-Festplatten angeboten werden.

Folgende Betriebssysteme sind mit nativen 4-kByte-Sektoren kompatibel:

- Windows 7 (Achtung: nicht bootbar und nur eingeschränkt nutzbar)
- ab Windows 8.1 mit Microsoft-Treiber storahci.sys (nicht mit Intel Rapid-Storage-Treiber iastor.sys)
- ab Windows Server 2012 R2
- jedes aktuelle Linux
- Mac OS X (Achtung: nicht bootbar)

### 4-kByte-Sektoren: Advanced Format Drives (AFD) / Advanced Format Technology

Advanced Format Drives (AFD) sind Festplatten mit einer physikalischen Sektorengröße von 4 kByte. Meist sind diese Laufwerke mit "4Kn" gekennzeichnet, was für "4 kByte native" steht. Doch nicht jede Hardware und Software ist darauf vorbereitet. Deshalb melden AFDs oft noch eine Sektorengröße von 512 Byte ("512e").

Der Vorteil größerer Sektoren oder Speicherblöcken ist das Einsparen von Overhead, den jeder logische Speicherblock umschließt. Dazu gehört ein Synchronisationsblock (Sync Section), eine Data Allocation Map (DAM), eine Prüfsumme (ECC) und ein kleiner Leerbereich zwischen den Speicherblöcken. Fasst man acht 512-Byte-Blöcke zu einem 4-kByte-Block zusammen, dann fallen sieben mal die Steuer- und Korrekturblöcke weg. Die Prüfsumme wird zwar größer, aber insgesamt reduziert sich der Overhead bei 4K-Sektoren um 75 Prozent. Das gilt auch für 512e-Festplatten. Bei 4Kn-Festplatten fällt in Zukunft nur noch die Umrechnung der externen Sektorgröße weg.  
Dateisysteme, wie NTFS oder HFS+, verwalten den Speicher auf Festplatten schon lange mit 4 kByte großen Einheiten. Auch der Arbeitsspeicher wird in den gängigen Betriebssystemen mit 4 kByte großen Blöcken (Pages) adressiert.  
Desweiteren erleichtert es die Fertigung von Festplatten mit hoher Speicherkapazität. Parallel entsteht so mehr Platz für die Nutzdaten auf der Magnetscheibe. In der Regel profitiert man auch von einer Geschwindigkeitssteigerung.

Wie erkennt man 4K-Sektor-Festplatten? Unter Windows gibt es die "smartmontools", mit denen man unter anderem die Sektorgröße auslesen kann.

### MTBF - Mean Time Between Failures

Grob übersetzt bedeutet MTBF soviel wie Hardware-Ausfallwahrscheinlichkeit. Der MTBF wird in Stunden angegeben. Die typischen Werte für Enterprise-Festplatten liegen bei 1.000.000 Stunden und bei normalen Festplatten bei 600.000 Stunden.  
Das ist allerdings kein garantierter Wert. Der MTBF basiert auf Stichproben, die hochgerechnet werden. Also mehr so eine Art Durchschnitt. Man muss dabei auch berücksichtigen, dass die Betriebsbedingungen auf den MTBF Einfluss haben. Ohne diese Berücksichtigung ist der Wert eigentlich nutzlos.

### Partitionsgrenze 2 TByte

Dank höhere Datendichte auf den Magnetscheiben ist die Speicherkapazität auf über 3 TByte angestiegen. Leider gibt es eine Grenze, aufgrund der Festplatten mit mehr als 2 TByte nicht als Bootlaufwerk zu gebrauchen sind.

Schuld ist die Partitionstabelle, die sich seit den 80er Jahren im Master Boot Record (MBR) befindet. Damit kommen alle x86-Betriebssystem zurecht. Zum Beispiel Windows und Linux. Doch diese Partitionstabelle fasst nur 32 Bit breite Felder für die Sektornummern. Rein rechnerisch ist bei 232 mit 512-kByte-Sektoren Schluss. Das wäre 2 TByte.

Die beste Lösung wäre der Einsatz von EFI bzw. UEFI anstatt dem veralteten PC-BIOS und der GUID Partition Table (GPT) statt dem Master Boot Record (MBR). Doch die PC-Hersteller lassen noch auf sich warten. Mit ein Grund ist, dass es kein 32-Bit-Windows gibt, das UEFI beherrscht. Bisher unterstützt nur Windows Vista und Windows 7 in der 64-Bit-Version den Boot-Vorgang von GPT-Festplatten und auch nur dann, wenn statt dem herkömmlichen BIOS das Unified Extensible Firmware Interface (UEFI) zum Einsatz kommt.  
Anstatt dem seit Jahren bekannten Problem mit einer zukunftsweisenden Lösung Herr zu werden, wird lieber an Notlösungen gebastelt. So formatieren die Festplattenhersteller ihre 3-TByte-Festplatten mit 4-kByte-Sektoren anstatt mit 512-Byte-Sektoren. Auf diese Weise reicht der Speicher des MBR für die Partitionstabelle wieder aus.  
Vom Einsatz als Boot-Laufwerk solcher Festplatten wird jedoch abgeraten. So lange kann man Festplatten über 2 TByte nur als Zweitspeicher verwenden.

### NCQ - Native Command Queuing

Unter Command Queuing versteht man die Fähigkeit einer Festplatte, mehrere Kommandos entgegenzunehmen und in einer Warteschlange (Queue) zu verwalten. Anstatt sie nacheinander abzuarbeiten, sortiert die Festplatte die Kommandos so, dass die Schreib-Lese-Köpfe möglichst kurze Wege zurücklegen. So wird die Latenzzeit minimiert, die vergeht, bis der gewünschte Sektor unter den Köpfen vorbeikommt.  
NCQ kann die Daten selbständig in den Hauptspeicher schreiben bzw. daraus lesen. Erst nach Beendigung eines oder mehrerer Kommandos wird das Betriebssystem informiert. Die Daten sind dann bereits im Puffer oder sogar weggeschrieben.  
NCQ wurde in Serial-ATA-Festplatten eingeführt, da kannte man dieses Verfahren in SCSI-Festplatten schon länger. Dort wird das Feature als "Tagged Command Queuing" bezeichnet. NCQ in SATA-Festplatten ist eine neue Implementierung von Command Queuing.  
Command Queuing erhöht den Datendurchsatz in Multi-Tasking-Umgebungen. Denn hier wollen viele Prozesse gleichzeitig auf die Platte zugreifen. Wenn Command Queuing tatsächlich die Kommando-Reihenfolge optimieren kann, dann wird der Datendurchsatz tatsächlich gesteigert.

### Partitionierung

Das Partitionieren ist das Aufteilen eines physikalischen Laufwerks oder einer erweiterten Partition in mehrere kleinere logische Partitionen, um sie als eigenständige Laufwerke ansprechen zu können.

- [Mehr Informationen zu Partitionierung](https://www.elektronik-kompendium.de/sites/com/0705011.htm)

### Fragmentierung / Defragmentierung

Unter Fragmentierung versteht man den Effekt, dass zusammenhängende Dateien nicht am Stück auf der Festplatte gespeichert werden. Sie werden verstreut auf der ganzen Festplatte verteilt. Das äußert sich in einer geringeren Datentransferrate, weil die Festplatten-Logik die Daten erst an verschiedenen Stellen lesen und zusammensetzen muss.  
Defragmentieren ist ein Vorgang, bei dem die Einzelteile von Dateien nachträglich so auf die Festplatte geschrieben werden, dass sie zusammenhängend gespeichert sind. In der Regel erhöht man dadurch die Lesegeschwindigkeit. Besonders beim Starten von Betriebssystem und Anwendungen.

- [Mehr Informationen zu Fragmentierung / Defragmentierung](https://www.elektronik-kompendium.de/sites/com/1312131.htm)

### Energiespar-Festplatten

Festplatten mit Energiesparfunktionen können manuell oder automatisch schlafen gelegt werden. Insbesondere dann, wenn sie für eine gewisse Zeit keine Schreib- und Lesetätigkeiten ausführen, also untätig sind, macht es Sinn auf diese Weise Energie zu sparen. In der Praxis fallen die Pausen nicht sehr häufig und lange aus, weil Multitasking-Betriebssysteme, wie Windows immer einen Dienst im Hintergrund laufen haben, der auf die Festplatte zugreift.  
Um Energie zu sparen arbeiten Energiespar-Festplatten mit einer variablen Drehzahl. Finden über eine längere Zeit keine Zugriffe statt, wird die Drehzahl automatisch von 7.200 auf 5.400 U/min reduziert. Außerdem werden die Schreib-/Leseköpfe während des Leerlaufs entladen.

### SSHD - Solid-State Hybrid Drives (Hybrid-Festplatten)

Hybrid-Festplatten sind herkömmliche Festplatten mit einem zusätzlichen Flash-Speicher. Der Flash-Speicher in Hybrid-Festplatten bietet verschiedene Vorteile. Zum einen kann das Betriebssystem schneller booten. Die Zeit, bis der Computer gestartet und betriebsbereit ist, kann so deutlich reduziert werden. Dadurch, dass die Magnetscheiben der Festplatte nicht ständig rotieren müssen, wird auch noch Strom gespart. Das ist besonders interessant bei Notebooks.

- [SSHD - Solid-State Hybrid Drives (Hybrid-Festplatten)](https://www.elektronik-kompendium.de/sites/com/1207051.htm)

### SSD - Solid State Drive

Bei den zukünftigen Festplatten wollen die Hersteller nur noch Flash-Speicher verwenden. Somit werden alle beweglichen Teile einer Festplatte verschwinden. Doch bis es soweit ist wird es noch einige Jahre dauern. Zumindest so lange, bis Flash-Speicher schneller und günstiger ist und eine größere Speicherkapazität erreicht als herkömmliche Festplatten.  
In Notebooks, in denen die Speicherkapazität der Festplatte keine so große Rolle spielt, werden bereits SSDs mit Flash-Speicher eingesetzt.