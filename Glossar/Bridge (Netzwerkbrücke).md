# Bridge (Netzwerkbrücke)

### 1. Kerndefinition

Eine **Netzwerk-Bridge** ist ein Netzwerkgerät, das zwei oder mehr separate Netzwerksegmente auf der **Sicherungsschicht (Schicht 2)** des OSI-Modells miteinander verbindet. Ihre Hauptfunktion besteht darin, den Datenverkehr zwischen diesen Segmenten zu filtern und weiterzuleiten, basierend auf den MAC-Adressen der angeschlossenen Geräte. Dadurch agieren die verbundenen Segmente als ein einziges, größeres logisches Netzwerk (eine einzige Broadcast-Domäne), während unnötiger Datenverkehr lokal gehalten wird.

### 2. Detaillierte Erläuterung / Funktionsweise

**Kernfunktionalität:** Eine Bridge arbeitet, indem sie eine **MAC-Adresstabelle** (auch bekannt als Forwarding-Tabelle oder CAM-Tabelle) aufbaut und pflegt.

1. **Lernen (Learning):** Wenn ein Datenpaket (Frame) an einem Port der Bridge ankommt, inspiziert die Bridge die **Quell-MAC-Adresse** des Frames. Sie trägt diese MAC-Adresse zusammen mit dem Port, an dem sie empfangen wurde, in ihre Tabelle ein. So "lernt" die Bridge, welche Geräte an welchem ihrer Ports angeschlossen sind.
    
2. **Weiterleiten (Forwarding):** Anschließend prüft die Bridge die **Ziel-MAC-Adresse** des Frames.
    
    - Findet sie die Ziel-MAC-Adresse in ihrer Tabelle, leitet sie den Frame **nur** an den zugehörigen Port weiter. Der Verkehr wird nicht an andere Ports gesendet.
        
    - Findet sie die Ziel-MAC-Adresse **nicht** in ihrer Tabelle (weil das Gerät noch nicht gesendet hat oder der Eintrag veraltet ist), leitet sie den Frame an **alle anderen Ports** weiter (Flooding), in der Hoffnung, das Zielgerät zu erreichen.
        
3. **Filtern (Filtering):** Wenn die Ziel-MAC-Adresse im selben Netzwerksegment liegt wie die Quell-MAC-Adresse (d. h., beide sind am selben Port der Bridge angeschlossen), erkennt die Bridge dies und **verwirft** den Frame. Er muss nicht in andere Segmente weitergeleitet werden.
    

**Zweck und Anwendungsfälle:** Historisch wurden Bridges eingesetzt, um die Leistung von Netzwerken zu verbessern, die durch zu viele Kollisionen überlastet waren (z. B. große, mit Hubs aufgebaute Netzwerke).

- **Segmentierung des Netzwerks:** Durch die Aufteilung eines großen Netzwerks in kleinere Segmente reduziert eine Bridge den lokalen Verkehr. Ein Frame, der für ein Gerät im Segment A bestimmt ist, wird nicht in Segment B gesendet, wodurch die Bandbreite in Segment B für dessen eigene Kommunikation frei bleibt.
    
- **Verbindung unterschiedlicher Medientypen:** Eine Bridge kann auch Segmente mit unterschiedlichen physikalischen Medien verbinden, z. B. ein Ethernet-Segment mit einem Token-Ring-Segment (obwohl dies heute kaum noch relevant ist).
    

### 3. Einordnung in den Gesamtkontext

Die Funktionalität der klassischen Bridge wurde weitgehend vom modernen **Netzwerk-Switch** übernommen und weiterentwickelt.

- **Bridge vs. Hub:** Ein **Hub** ist ein einfaches Schicht-1-Gerät, das eingehende Signale an alle anderen Ports blind weiterleitet. Er schafft eine einzige große Kollisionsdomäne. Eine **Bridge** ist intelligenter, da sie auf Schicht 2 arbeitet, den Verkehr filtert und für jeden Port eine separate Kollisionsdomäne schafft.
    
- **Bridge vs. Switch:** Ein **Switch** kann als eine **Multi-Port-Bridge** betrachtet werden. Während eine klassische Bridge oft nur zwei oder vier Ports hatte, haben Switches Dutzende. Jeder Port eines Switches ist eine eigene Kollisionsdomäne. Moderne Switches bieten darüber hinaus viele fortgeschrittene Funktionen, die über die einer einfachen Bridge hinausgehen (z. B. VLANs, Quality of Service).
    
- **Bridge vs. Router:** Ein **Router** ist ein Schicht-3-Gerät. Er verbindet unterschiedliche IP-Netzwerke (Broadcast-Domänen) und trifft Weiterleitungsentscheidungen basierend auf IP-Adressen, nicht auf MAC-Adressen. Während eine Bridge Segmente zu einem einzigen logischen Netzwerk verbindet, hält ein Router Broadcast-Verkehr strikt innerhalb der jeweiligen Netzwerke.
    

In der modernen IT wird der Begriff "Bridge" oft im Software-Kontext verwendet, z. B. bei der Virtualisierung, wo eine "virtuelle Bridge" die Netzwerkkarte des Host-Systems mit den virtuellen Netzwerkkarten der Gast-VMs verbindet.

### 4. Sicherheitsaspekte

Obwohl Bridges primär der Leistungsverbesserung dienen, haben sie auch sicherheitsrelevante Implikationen.

- **MAC-Spoofing:** Ein Angreifer könnte die MAC-Adresse eines anderen Geräts fälschen, um die Bridge dazu zu bringen, Frames, die für das legitime Gerät bestimmt sind, an den Port des Angreifers zu senden.
    
- **CAM-Table-Overflow-Angriff:** Ein Angreifer kann die MAC-Adresstabelle der Bridge (oder eines Switches) gezielt mit einer Flut von Frames mit gefälschten Quell-MAC-Adressen überlaufen lassen. Wenn die Tabelle voll ist, schaltet das Gerät in einen "Fail-Open"-Modus und agiert wie ein Hub, der allen Verkehr an alle Ports weiterleitet. Dies ermöglicht es dem Angreifer, den gesamten Netzwerkverkehr mitzuschneiden. Moderne Switches haben Schutzmechanismen (Port Security) dagegen.
    
- **Broadcast-Stürme:** Da eine Bridge alle angeschlossenen Segmente zu einer einzigen Broadcast-Domäne vereint, kann ein Broadcast-Sturm (z. B. durch eine fehlerhafte Netzwerkschleife) das gesamte von der Bridge verbundene Netzwerk lahmlegen. Das **Spanning Tree Protocol (STP)** ist ein Mechanismus, der solche Schleifen in gebrückten Netzwerken erkennt und blockiert.
    

### 5. Praxisbeispiel / Analogie

**Praxisbeispiel (historisch):** In den frühen 90er Jahren hat eine Universitätsbibliothek ein einziges großes Ethernet-Netzwerk, das mit Hubs aufgebaut ist. Mit zunehmender Anzahl von Computern kommt es ständig zu Datenkollisionen, und das Netzwerk wird sehr langsam. **Lösung mit Bridge:** Ein Netzwerktechniker installiert eine Bridge und teilt das Netzwerk in zwei Segmente: eines für die öffentlich zugänglichen Recherche-PCs und eines für die Computer der Mitarbeiter. Die Bridge lernt, welche Computer zu welchem Segment gehören. Nun wird der Datenverkehr zwischen den Recherche-PCs nicht mehr in das Mitarbeitersegment gesendet und umgekehrt. Das Ergebnis: Weniger Kollisionen und eine spürbar bessere Performance in beiden Segmenten.

**Analogie:** Stellen Sie sich einen **intelligenten Postverteiler in einem Großraumbüro** vor, das aus zwei Abteilungen (A und B) besteht.

- Ein **Hub** wäre ein Postbote, der jeden Brief laut für alle im ganzen Büro vorliest, egal für wen er ist.
    
- Eine **Bridge** ist ein Postverteiler, der am Schreibtisch zwischen den beiden Abteilungen sitzt. Er schaut sich die Adresse auf jedem Brief (die Ziel-MAC-Adresse) an.
    
    - Ist der Brief für jemanden in Abteilung A, gibt er ihn nur dorthin.
        
    - Ist er für jemanden in Abteilung B, gibt er ihn nur dorthin.
        
    - Ist ein Brief von einem Mitarbeiter aus Abteilung A an einen anderen Mitarbeiter in Abteilung A adressiert, erkennt der Verteiler das und wirft den Brief weg, da er die Abteilung gar nicht verlassen muss. Dieser intelligente Verteiler reduziert den Lärm und die Ablenkung im gesamten Büro erheblich.
        

### 6. Fazit / Bedeutung für IT-Profis

Obwohl dedizierte Hardware-Bridges heute weitgehend durch Switches ersetzt wurden, ist das **Verständnis des Bridging-Prinzips** für jeden IT-Profi von fundamentaler Bedeutung. Es ist die Grundlage für die Funktionsweise von Switches, dem Herzstück moderner LANs. Konzepte wie MAC-Adresstabellen, das Filtern von Verkehr auf Schicht 2 und die Notwendigkeit von Schleifenschutzmechanismen wie STP sind direkt aus der Welt der Bridges hervorgegangen und für die Konfiguration und Fehlersuche in heutigen Netzwerken unerlässlich.