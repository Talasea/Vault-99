# 5-4-3-Regel

## 1. Kerndefinition

Die **5-4-3-Regel** ist eine historische Designrichtlinie für klassische, auf Repeatern basierende Ethernet-Netzwerke (insbesondere 10BASE-T und 10BASE5/2). Sie diente dazu, die maximale Ausdehnung eines Netzwerks zu begrenzen, um die zuverlässige Funktionsweise des Kollisionserkennungsverfahrens CSMA/CD zu gewährleisten. Die Regel besagt, dass zwischen zwei beliebigen Endgeräten im Netzwerk maximal **fünf Segmente**, verbunden durch **vier Repeater**, liegen dürfen, wobei nur auf **drei** dieser Segmente aktive Endgeräte (wie Computer) angeschlossen sein dürfen.

## 2. Detaillierte Erläuterung / Funktionsweise

Die 5-4-3-Regel ist eine direkte Konsequenz der physikalischen Einschränkungen von frühen, geteilten Ethernet-Topologien (Shared Ethernet). In einem solchen Netzwerk teilen sich alle Geräte eine gemeinsame Übertragungsleitung, was als eine einzige **Kollisionsdomäne** bezeichnet wird.

### 2.1 Schlüsselkomponenten

Die Zahlen der Regel definieren die maximal erlaubten Komponenten zwischen den zwei am weitesten voneinander entfernten Punkten im Netzwerk:

- **5 Segmente:** Ein Netzwerksegment ist ein physischer Abschnitt eines Netzwerkkabels (z. B. ein Koaxialkabel oder ein Twisted-Pair-Kabel), der Geräte miteinander verbindet. Die Regel erlaubt eine Kette von insgesamt bis zu fünf solchen Segmenten.
    
- **4 Repeater (oder Hubs):** Ein Repeater ist ein Gerät der OSI-Schicht 1, das ein eingehendes elektrisches Signal regeneriert und verstärkt, um es über längere Distanzen weiterzuleiten. Hubs sind im Grunde Repeater mit mehreren Ports. Jeder Repeater führt eine kleine Signalverzögerung (Latenz) ein, die für die Regel entscheidend ist.
    
- **3 besetzte Segmente:** Von den fünf erlaubten Segmenten dürfen nur drei direkt Endgeräte (wie PCs, Server oder Drucker) angeschlossen haben. Die verbleibenden zwei Segmente dürfen ausschließlich als Verbindungsstrecken (Inter-Repeater-Links) zwischen den Repeatern dienen.
    

### 2.2 Prozess und Zweck

Der Zweck der Regel war es, die **Round-Trip Time (RTT)**, also die Zeit, die ein Signal für den Weg vom einen Ende des Netzwerks zum anderen und wieder zurück benötigt, innerhalb eines kritischen Zeitfensters zu halten. Dies war für das **CSMA/CD-Verfahren (Carrier Sense Multiple Access with Collision Detection)** unerlässlich:

1. Ein Gerät lauscht, ob das Medium frei ist (Carrier Sense).
    
2. Wenn es frei ist, beginnt es zu senden (Multiple Access).
    
3. Sollten zwei Geräte gleichzeitig senden, entsteht eine **Kollision**.
    
4. Diese Kollision erzeugt ein spezielles Spannungssignal, das sich im gesamten Netzwerk ausbreiten muss.
    
5. Alle sendenden Geräte müssen diese Kollision erkennen (Collision Detection), bevor sie ihre Übertragung beendet haben. Nur dann können sie den Sendevorgang abbrechen und es nach einer zufälligen Zeit erneut versuchen.
    

Jeder Meter Kabel und jeder Repeater fügt der Signallaufzeit eine Verzögerung hinzu. Wenn das Netzwerk zu groß ist (zu viele Segmente und Repeater), wird die Gesamtverzögerung so hoch, dass ein Gerät seine Datenübertragung bereits abgeschlossen haben könnte, bevor das Kollisionssignal von der am weitesten entfernten Stelle bei ihm ankommt. In diesem Fall würde die Kollision nicht korrekt behandelt, was zu fehlerhaften Datenübertragungen führt. Die 5-4-3-Regel definierte eine "sichere" Obergrenze für die Netzwerkgröße, um dies zu verhindern.

## 3. Einordnung in den Gesamtkontext

Die 5-4-3-Regel ist ein Konzept der **OSI-Schicht 1 (Bitübertragungsschicht)** und ist untrennbar mit veralteten Netzwerktechnologien verbunden:

- **Hubs vs. Switches:** Die Regel ist nur für Netzwerke relevant, die **Hubs oder Repeater** verwenden. Diese leiten eingehende Datenpakete an alle anderen Ports weiter und vergrößern somit die Kollisionsdomäne. Moderne Netzwerke verwenden **Switches**, die auf **Schicht 2 (Sicherungsschicht)** arbeiten. Ein Switch erstellt für jeden Port eine separate Kollisionsdomäne. Da eine Kollision auf einem Port die anderen nicht betrifft, wird das Problem, das die 5-4-3-Regel löst, grundlegend eliminiert.
    
- **CSMA/CD und Duplex-Modi:** Die Regel ist eine direkte Folge von CSMA/CD, das im Halbduplex-Modus (Geräte können nicht gleichzeitig senden und empfangen) erforderlich ist. Heutige geswitchte Netzwerke arbeiten fast ausschließlich im Vollduplex-Modus, bei dem Kollisionen per Definition nicht mehr auftreten.
    

## 4. Sicherheitsaspekte

Obwohl die 5-4-3-Regel selbst keine Sicherheitsrichtlinie ist, ist die Technologie, auf die sie sich bezieht, aus heutiger Sicht fundamental unsicher:

- **Eavesdropping (Abhören):** In einem Netzwerk, das auf Hubs basiert, wird jedes Datenpaket an jeden Port innerhalb der Kollisionsdomäne gesendet. Ein Angreifer kann seinen Computer in den "Promiscuous Mode" versetzen und mit einem Paket-Sniffer (wie Wireshark) mühelos den gesamten Netzwerkverkehr des Segments mitlesen, auch wenn dieser nicht für ihn bestimmt ist.
    
- **Mangelnde Segmentierung:** Die große, übergreifende Kollisionsdomäne macht das Netzwerk anfälliger für Denial-of-Service-Angriffe durch "Collision Flooding".
    

Der Umstieg auf Switches, der die 5-4-3-Regel obsolet machte, war daher nicht nur ein Performance-Gewinn, sondern auch ein massiver Fortschritt für die Netzwerksicherheit, da der Datenverkehr gezielt nur an den Empfänger-Port weitergeleitet wird.

## 5. Praxisbeispiel / Analogie

Stellen Sie sich eine **Diskussionsrunde in einer sehr langen Halle** vor.

- Die **Teilnehmer** sind die Endgeräte.
    
- Die Regel lautet: **"Nur eine Person spricht zur Zeit."**
    
- Wenn zwei Personen gleichzeitig zu sprechen beginnen (eine **Kollision**), müssen sie das sofort bemerken und aufhören.
    
- In der Mitte der Halle stehen **Helfer (Repeater)**, die das Gesagte laut wiederholen, damit es auch am anderen Ende ankommt. Jeder Helfer braucht aber einen kurzen Moment zum Zuhören und Wiederholen (**Latenz**).
    

Die **5-4-3-Regel** wäre hier eine Bauvorschrift für die Halle: "Die Halle darf maximal **500 Meter lang sein (5 Segmente)**, es dürfen höchstens **4 Helfer (4 Repeater)** eingesetzt werden und nur in **3 der 5 Abschnitte (3 besetzte Segmente)** dürfen Teilnehmer sitzen." Hält man sich nicht daran, ist die Halle zu groß. Ein Teilnehmer am einen Ende würde sein ganzes Statement beenden, bevor er überhaupt mitbekommt, dass am anderen Ende jemand gleichzeitig angefangen hat zu reden. Die Diskussion wäre chaotisch und unverständlich.

## 6. Fazit / Bedeutung für IT-Profis

Die 5-4-3-Regel ist heute für den Entwurf moderner Netzwerke **obsolet**. Ihr Wert ist primär **historisch und didaktisch**. Für IT-Profis ist das Verständnis dieser Regel dennoch wichtig, denn es schafft ein tiefes Fundament für die Kernkonzepte der Netzwerktechnik:

- Es erklärt das **"Warum"** hinter dem Übergang von Hubs zu Switches.
    
- Es verdeutlicht anschaulich die physikalischen Grenzen von Übertragungsmedien und die Bedeutung von **Latenz** und **Signallaufzeiten**.
    
- Es ist essenziell für das Verständnis des Begriffs der **Kollisionsdomäne**, einem fundamentalen Konzept, das auch in Prüfungen für IT-Zertifizierungen (z. B. CompTIA Network+) nach wie vor eine Rolle spielt.
    

Wer die 5-4-3-Regel versteht, begreift, welche grundlegenden Probleme Switches gelöst haben und warum moderne Ethernet-Netzwerke so robust und performant sind.