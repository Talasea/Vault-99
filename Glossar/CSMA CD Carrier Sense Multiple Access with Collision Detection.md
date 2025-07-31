
### 1. Kerndefinition

**CSMA/CD (Carrier Sense Multiple Access with Collision Detection)** ist ein Zugriffsverfahren für geteilte (shared) Übertragungsmedien in Computernetzwerken, das vor allem aus dem klassischen **Ethernet** bekannt ist. Es regelt, welcher Teilnehmer in einem Netzwerksegment senden darf, um Datenkollisionen zu vermeiden oder, falls sie doch auftreten, diese zu erkennen und zu beheben. Das Verfahren stellt sicher, dass immer nur eine Station gleichzeitig erfolgreich Daten sendet.

### 2. Detaillierte Erläuterung / Funktionsweise

CSMA/CD funktioniert nach einem einfachen Prinzip, das sich in drei Phasen gliedert:

- **1. Carrier Sense (CS):** "Auf die Leitung horchen". Bevor eine Station Daten sendet, prüft sie, ob das Übertragungsmedium (z. B. das Koaxialkabel oder Twisted-Pair-Kabel) frei ist. Ist eine andere Übertragung im Gange ("Trägersignal vorhanden"), wartet die Station, bis das Medium wieder frei ist.
    
- **2. Multiple Access (MA):** "Mehrfachzugriff". Alle Stationen im Netzwerksegment haben gleichberechtigten Zugriff auf das Medium. Es gibt keine zentrale Instanz, die Sendezeiten zuteilt; der Zugriff erfolgt dezentral und kompetitiv.
    
- **3. Collision Detection (CD):** "Kollisionserkennung". Da zwei Stationen fast gleichzeitig das Medium als frei erkennen und mit dem Senden beginnen können, sind Kollisionen unvermeidlich. Eine Kollision tritt auf, wenn sich zwei oder mehr Signale auf dem Medium überlagern und die Daten unbrauchbar werden. Jede sendende Station überwacht das Medium auch während des eigenen Sendevorgangs. Stellt sie fest, dass das Signal auf dem Medium von ihrem eigenen gesendeten Signal abweicht, erkennt sie eine Kollision.
    

**Prozess bei Kollision:**

1. Die Stationen, die die Kollision erkennen, brechen ihre Übertragung sofort ab.
    
2. Sie senden ein kurzes **Jam-Signal**, um sicherzustellen, dass alle anderen Stationen im Segment die Kollision ebenfalls bemerken.
    
3. Jede beteiligte Station startet einen zufälligen Timer (basierend auf dem **Binary Exponential Backoff Algorithmus**).
    
4. Nach Ablauf des individuellen Timers versucht die Station erneut, den Prozess bei Schritt 1 (Carrier Sense) zu starten. Der zufällige Timer sorgt dafür, dass die Stationen nicht sofort wieder gleichzeitig zu senden beginnen.
    

### 3. Einordnung in den Gesamtkontext

CSMA/CD ist das definierende Zugriffsverfahren für **Half-Duplex-Ethernet** über geteilte Medien, wie es bei alten **Hub-basierten Netzwerken** oder Koaxialkabel-Topologien (Bus) der Fall war. In einem solchen Netzwerksegment bilden alle angeschlossenen Geräte eine einzige **Kollisionsdomäne**. Mit der Einführung von **Switches** anstelle von Hubs hat CSMA/CD an Bedeutung verloren. Ein Switch erstellt für jeden Port eine separate, dedizierte Kollisionsdomäne. Da an einem Port typischerweise nur ein Endgerät angeschlossen ist und die Kommunikation im **Full-Duplex-Modus** stattfindet (gleichzeitiges Senden und Empfangen ist möglich), treten keine Kollisionen mehr auf. CSMA/CD ist in modernen, geswitchten Ethernet-Netzwerken daher praktisch nicht mehr aktiv, bleibt aber ein fundamental wichtiges Konzept zum Verständnis der Ethernet-Evolution.

### 4. Sicherheitsaspekte

CSMA/CD selbst ist ein Protokoll zur Medienzugriffskontrolle und hat keine direkten Sicherheitsfunktionen. Die zugrunde liegende Architektur (geteilte Medien) ist jedoch aus Sicherheitssicht problematisch:

- **Sniffing/Abhören:** In einer klassischen CSMA/CD-Umgebung (mit Hubs) wird jeder gesendete Frame an alle Ports des Hubs weitergeleitet. Ein Angreifer kann seinen Netzwerkadapter in den **Promiscuous Mode** versetzen und den gesamten Datenverkehr innerhalb der Kollisionsdomäne mühelos mitschneiden, auch wenn dieser nicht für ihn bestimmt ist. Dies ermöglicht das Ausspähen von Passwörtern, Daten und anderen sensiblen Informationen. Die Segmentierung durch Switches löst dieses Problem, da Frames nur an den Zielport weitergeleitet werden.
    

### 5. Praxisbeispiel / Analogie

**Analogie: Eine höfliche Gesprächsrunde** Stellen Sie sich eine Gruppe von Personen vor, die an einem runden Tisch sitzt und diskutiert, aber alle sehr höflich sind.

- **Carrier Sense:** Bevor jemand spricht, hört er, ob bereits jemand anderes redet. Wenn ja, wartet er.
    
- **Multiple Access:** Jeder am Tisch hat das gleiche Recht zu sprechen.
    
- **Collision Detection:** Wenn zwei Personen exakt gleichzeitig zu sprechen beginnen, bemerken sie dies sofort ("Oh, Entschuldigung!").
    
- **Jam-Signal & Backoff:** Beide hören sofort auf zu reden. Um zu vermeiden, dass sie sofort wieder gleichzeitig anfangen, warten beide eine kurze, zufällig gewählte Zeitspanne (der eine vielleicht eine Sekunde, der andere zwei), bevor sie einen neuen Versuch starten.
    

### 6. Fazit / Bedeutung für IT-Profis

Obwohl in der Praxis durch Full-Duplex-Switching weitgehend abgelöst, ist das Verständnis von CSMA/CD für IT-Profis von fundamentaler Bedeutung. Es ist ein Schlüsselkonzept zum Verständnis der Funktionsweise und der historischen Entwicklung von Ethernet, der wichtigsten LAN-Technologie der Welt. Kenntnisse über CSMA/CD helfen zu verstehen, warum Hubs durch Switches ersetzt wurden, was eine Kollisionsdomäne ist und welche Leistungs- und Sicherheitsprobleme in alten Netzwerktopologien auftreten. Es ist ein klassisches Thema in der Netzwerk-Grundlagenausbildung und Zertifizierungen wie CompTIA Network+ oder CCNA.