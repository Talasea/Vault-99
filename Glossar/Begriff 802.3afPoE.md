# Begriff: 802.3af (PoE)

## 1. Kerndefinition

**IEEE 802.3af** ist ein technischer Standard, der das Verfahren für **Power over Ethernet (PoE)** definiert. Er ermöglicht die Versorgung von Netzwerkgeräten mit elektrischer Energie direkt über ein Standard-Twisted-Pair-Ethernet-Kabel, wodurch eine separate Stromversorgung für das Endgerät überflüssig wird. Dieser Standard ist die Grundlage für die vereinfachte Installation von Geräten wie IP-Telefonen, WLAN-Access-Points und Überwachungskameras.

## 2. Detaillierte Erläuterung / Funktionsweise

PoE nach dem 802.3af-Standard vereinfacht die Netzwerkinfrastruktur erheblich, indem Daten und Strom über ein einziges Kabel übertragen werden.

### 2.1 Schlüsselkomponenten

- **Power Sourcing Equipment (PSE):** Dies ist das Gerät, das den Strom in das Ethernet-Kabel einspeist. Typischerweise ist dies ein PoE-fähiger Netzwerk-Switch ("Endspan") oder ein zwischengeschalteter "PoE-Injector" ("Midspan").
    
- **Powered Device (PD):** Dies ist das Endgerät, das über das Ethernet-Kabel mit Strom versorgt wird, z. B. eine IP-Kamera oder ein VoIP-Telefon.
    
- **Leistungsklassen:** Der 802.3af-Standard liefert am PSE eine Leistung von bis zu **15,4 Watt**. Aufgrund von Leistungsverlusten im Kabel wird dem PD eine garantierte Leistung von mindestens **12,95 Watt** zur Verfügung gestellt.
    

### 2.2 Prozess und Zweck

Der Hauptzweck ist die **Vereinfachung der Installation und die Erhöhung der Flexibilität**. Der Prozess beginnt mit einer Aushandlung:

1. Das PSE sendet eine niedrige Spannung auf das Kabel, um zu prüfen, ob ein kompatibles PD angeschlossen ist. Dies geschieht durch eine Widerstandsmessung, um zu verhindern, dass Nicht-PoE-Geräte durch die Stromzufuhr beschädigt werden.
    
2. Wird ein gültiges PD erkannt, klassifiziert das PSE dessen Leistungsbedarf (falls vom PD unterstützt).
    
3. Das PSE speist die volle Spannung (ca. 48 Volt Gleichstrom) auf das Kabel und versorgt das PD mit Strom.
    

## 3. Einordnung in den Gesamtkontext

802.3af ist Teil der **IEEE 802.3-Familie** von Ethernet-Standards und eine Technologie der **OSI-Schicht 1 (Bitübertragungsschicht)**. Er ist der ursprüngliche PoE-Standard und wurde durch leistungsfähigere Nachfolger erweitert:

- **802.3at (PoE+):** Liefert bis zu 25,5 W am Endgerät.
    
- **802.3bt (PoE++):** Liefert in verschiedenen Typen bis zu 51 W oder sogar 71 W am Endgerät, um auch energiehungrigere Geräte wie PTZ-Kameras oder kleine Switches zu versorgen.
    

## 4. Sicherheitsaspekte

- **Physische Sicherheit:** Die zentrale Stromversorgung über einen PoE-Switch, der idealerweise an eine unterbrechungsfreie Stromversorgung (USV) angeschlossen ist, erhöht die Ausfallsicherheit der Endgeräte.
    
- **Betriebssicherheit:** Der Aushandlungsprozess verhindert Schäden an Geräten, die kein PoE unterstützen.
    
- **Fernwartung:** Ein Administrator kann ein nicht reagierendes Gerät (z. B. eine Kamera) einfach neu starten, indem er den betreffenden Port am Switch kurz stromlos schaltet (Remote Reboot). Ein potenzielles Risiko ist jedoch, dass bei einem Ausfall des zentralen PoE-Switches alle angeschlossenen Geräte gleichzeitig ausfallen.
    

## 5. Praxisbeispiel / Analogie

Stellen Sie sich vor, Sie möchten eine **Überwachungskamera** an einer schwer zugänglichen Stelle unter dem Dachfirst installieren, wo es keinen Stromanschluss gibt. Anstatt einen Elektriker zu beauftragen, eine neue Steckdose zu verlegen, verwenden Sie PoE. Sie ziehen ein einziges Ethernet-Kabel von Ihrem PoE-Switch im Keller zur Kamera. Dieses eine Kabel liefert der Kamera nun sowohl die Datenverbindung zum Netzwerk als auch die Energie für den Betrieb.

## 6. Fazit / Bedeutung für IT-Profis

Der 802.3af-Standard und seine Nachfolger haben die Planung und Installation von Netzwerkinfrastrukturen revolutioniert. Die Technologie senkt Kosten, reduziert den Verkabelungsaufwand und ermöglicht die flexible Platzierung von Geräten unabhängig von vorhandenen Stromquellen. Für Netzwerkadministratoren ist das Wissen um PoE essenziell für die Planung moderner WLAN-, VoIP- und IoT-Infrastrukturen.