
- **Kerndefinition:** **Store-and-Forward** ist eine von zwei primären Vermittlungsmethoden, die von Netzwerk-Switches verwendet werden. Bei diesem Verfahren empfängt der Switch den gesamten Datenframe vollständig, speichert ihn kurzzeitig in einem Puffer und überprüft ihn auf Fehler, bevor er an den Zielport weitergeleitet wird.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:**
        
        1. **Store (Speichern):** Der Switch empfängt alle Bits eines ankommenden Datenframes und speichert sie in seinem internen Speicher.
            
        2. **Error-Checking (Fehlerprüfung):** Der Switch berechnet die **Frame Check Sequence (FCS)**, eine Prüfsumme am Ende des Frames, und vergleicht sie mit dem Wert im Frame.
            
        3. **Forward (Weiterleiten):** Wenn die Prüfsumme korrekt ist, schlägt der Switch die Ziel-MAC-Adresse in seiner Tabelle nach und leitet den Frame an den entsprechenden Port weiter. Ist der Frame fehlerhaft, wird er verworfen.
            
    - **Zweck:** Der Hauptzweck ist die Gewährleistung einer hohen Datenintegrität. Fehlerhafte oder unvollständige Frames werden nicht im Netzwerk verbreitet, was die Gesamtleistung und Stabilität verbessert.
        
- **Einordnung in den Gesamtkontext:** Store-and-Forward ist die zuverlässigste, aber auch langsamste Switching-Methode. Sie steht im Gegensatz zum **Cut-Through-Switching**, bei dem der Switch den Frame bereits weiterleitet, sobald er die Ziel-MAC-Adresse gelesen hat, ohne auf den Rest des Frames zu warten oder eine Fehlerprüfung durchzuführen. Cut-Through hat eine geringere Latenz, leitet aber auch fehlerhafte Frames weiter.
    
- **Sicherheitsaspekte:** Obwohl primär ein Mechanismus zur Qualitätssicherung, trägt Store-and-Forward indirekt zur Netzwerksicherheit bei. Indem es die Weiterleitung von korrupten oder absichtlich manipulierten (z. B. zu kurzen "Runt"-Frames) Paketen verhindert, kann es die Auswirkungen bestimmter Denial-of-Service-Angriffe oder Netzwerkprobleme eindämmen.
    
- **Praxisbeispiel / Analogie:** Store-and-Forward-Switching ist wie eine Postsortieranlage, die jedes einzelne Paket vor der Weiterleitung einer Qualitätskontrolle unterzieht. Das Paket wird vom Band genommen (Store), auf Beschädigungen und korrekte Adressierung geprüft (Error-Checking) und nur wenn alles in Ordnung ist, wird es auf das richtige Förderband für die Zustellung gelegt (Forward).
    
- **Fazit / Bedeutung für IT-Profis:** In modernen Netzwerken ist Store-and-Forward aufgrund der hohen Geschwindigkeiten der Switch-Hardware die vorherrschende Methode. Die minimale zusätzliche Latenz ist im Vergleich zum Vorteil der Fehlerfilterung vernachlässigbar. Für Netzwerktechniker ist das Verständnis der verschiedenen Switching-Methoden wichtig, um die Funktionsweise von Switches zu verstehen und in speziellen Anwendungsfällen (z. B. High-Frequency Trading) die richtige Hardware auszuwählen.