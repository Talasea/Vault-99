- **Kerndefinition:** Diese Akronyme beschreiben die verschiedenen Arten der Abschirmung von Twisted-Pair-Netzwerkkabeln gemäß der Norm ISO/IEC 11801. Die Abschirmung dient dem Schutz der Datenübertragung vor externen elektromagnetischen Störungen (EMI) und reduziert die eigene Abstrahlung des Kabels. Die Buchstaben geben an, ob eine Gesamtabschirmung (vor dem `/`) und/oder eine Abschirmung der einzelnen Adernpaare (nach dem `/`) vorhanden ist.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **U (Unshielded):** Keine Abschirmung.
        
    - **F (Foiled):** Eine Abschirmung aus Aluminiumfolie.
        
    - **S (Screened):** Eine Abschirmung aus einem Drahtgeflecht.
        
    - **TP (Twisted Pair):** Verdrillte Adernpaare (der grundlegende Aufbau).
        
    
    **Gängige Typen:**
    
    - **U/UTP (Unshielded/Unshielded Twisted Pair):** Das Standard-Netzwerkkabel ohne jegliche Abschirmung. Am häufigsten verwendet und am flexibelsten.
        
    - **F/UTP (Foiled/Unshielded Twisted Pair):** Besitzt eine Gesamtabschirmung aus Folie um alle Adernpaare. Guter Basisschutz. (Oft als FTP bezeichnet).
        
    - **S/FTP (Screened/Foiled Twisted Pair):** Bietet den besten Schutz. Jedes Adernpaar ist einzeln mit Folie geschirmt (FTP), und zusätzlich gibt es eine Gesamtabschirmung aus Drahtgeflecht (S).
        
    - **STP (Shielded Twisted Pair):** Ein älterer, oft unspezifischer Begriff, der meist ein Kabel mit einer Art von Abschirmung meint, oft S/UTP oder F/UTP.
        
- **Einordnung in den Gesamtkontext:** Die Wahl des Kabeltyps ist ein fundamentaler Teil der Planung der physischen Netzwerkinfrastruktur (Layer 1). Während in normalen Büroumgebungen oft ungeschirmte U/UTP-Kabel ausreichen, sind in Umgebungen mit starken Störquellen (z. B. Industrieanlagen mit großen Motoren, Krankenhäuser mit medizinischen Geräten) geschirmte Kabel (wie S/FTP) zwingend erforderlich, um eine stabile Datenübertragung zu gewährleisten.
    
- **Sicherheitsaspekte:** Der primäre Zweck der Abschirmung ist die Sicherstellung der Signalintegrität, nicht die Datensicherheit. Eine gute Abschirmung erschwert jedoch das "Abhören" der vom Kabel ausgehenden elektromagnetischen Abstrahlung (TEMPEST-Angriffe), was in Hochsicherheitsumgebungen relevant sein kann. Eine entscheidende Voraussetzung für die Wirksamkeit der Schirmung ist die korrekte Erdung an beiden Enden des Kabels.
    
- **Praxisbeispiel / Analogie:** Stellen Sie sich vor, Sie führen ein leises Gespräch in einem Raum. Ein U/UTP-Kabel ist wie ein Gespräch in einer ruhigen Bibliothek – keine Störungen. Ein S/FTP-Kabel ist wie das gleiche Gespräch in einer lauten Fabrikhalle – die Gesprächspartner tragen schalldichte Kopfhörer mit Mikrofonen (Paarschirmung) und stehen zusätzlich in einer schallisolierten Kabine (Gesamtschirmung), um die Nachricht klar und deutlich zu übertragen.
    
- **Fazit / Bedeutung für IT-Profis:** Für Netzwerkplaner und Installateure ist die Kenntnis der verschiedenen Abschirmungstypen und ihrer Anwendungsbereiche entscheidend. Die Auswahl des falschen Kabels kann zu unerklärlichen Netzwerkproblemen und Leistungseinbußen führen. Die Investition in eine höherwertige, geschirmte Verkabelung kann in störanfälligen Umgebungen langfristig Kosten und Aufwand für die Fehlersuche sparen.