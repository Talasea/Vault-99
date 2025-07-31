- **Kerndefinition:** **SHA (Secure Hash Algorithm)** ist eine Familie von kryptografischen Hash-Funktionen, die von der US-amerikanischen National Security Agency (NSA) entwickelt und vom National Institute of Standards and Technology (NIST) als US-Bundesstandard veröffentlicht wurden. Sie erzeugen aus einer Eingabe beliebiger Größe eine eindeutige, nicht umkehrbare Zeichenkette fester Länge (den Hash-Wert), die zur Sicherstellung der Datenintegrität dient.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **SHA-1:** Erzeugt einen 160-Bit-Hash. Gilt seit 2005 als theoretisch und seit 2017 als praktisch gebrochen, da Kollisionen (zwei unterschiedliche Eingaben, die denselben Hash erzeugen) gezielt erzeugt werden können. **Die Verwendung von SHA-1 ist nicht mehr sicher.**
        
    - **SHA-2:** Eine Familie von sechs Hash-Funktionen mit unterschiedlichen Ausgabelängen: SHA-224, **SHA-256**, SHA-384, **SHA-512**, SHA-512/224, SHA-512/256. SHA-256 ist heute der am weitesten verbreitete Standard für viele Sicherheitsanwendungen, einschließlich TLS-Zertifikaten und Kryptowährungen.
        
    - **SHA-3:** Eine neue Familie von Hash-Funktionen (basierend auf dem Keccak-Algorithmus), die durch einen öffentlichen Wettbewerb ausgewählt wurde. SHA-3 ist intern völlig anders aufgebaut als SHA-1/2 und dient als sichere Alternative, falls in SHA-2 Schwachstellen gefunden werden sollten.
        
- **Einordnung in den Gesamtkontext:** SHA-Algorithmen sind ein fundamentaler Baustein der modernen Kryptografie. Sie sind die Nachfolger von älteren und unsicheren Funktionen wie **MD5**. Sie werden in einer Vielzahl von Sicherheitsprotokollen und -anwendungen eingesetzt, z. B. in digitalen Signaturen, zur Speicherung von Passwort-Hashes und zur Sicherstellung der Integrität von Software-Downloads.
    
- **Sicherheitsaspekte:** Der gesamte Zweck der SHA-Familie ist die Gewährleistung von Sicherheit, insbesondere der **Datenintegrität**. Die entscheidenden Sicherheitseigenschaften sind:
    
    - **Kollisionsresistenz:** Es muss praktisch unmöglich sein, zwei verschiedene Eingaben zu finden, die denselben Hash erzeugen.
        
    - **Prä-Bild-Resistenz:** Aus einem Hash-Wert darf nicht auf die ursprüngliche Eingabe geschlossen werden können. Die Entwicklung von SHA-2 und SHA-3 war eine direkte Reaktion auf die bei SHA-1 entdeckten kryptografischen Schwächen.
        
- **Praxisbeispiel / Analogie:** Ein SHA-Hash ist wie ein digitaler, genetischer Fingerabdruck für eine Datei. Der SHA-256-Algorithmus erzeugt einen extrem zuverlässigen Fingerabdruck. Ändert sich auch nur ein winziges Detail in der Datei (der DNA), ist der resultierende Fingerabdruck komplett anders. SHA-1 hingegen ist wie ein veraltetes Fingerabdruckverfahren, bei dem es Fälschern gelungen ist, künstlich einen passenden Fingerabdruck für eine andere Person zu erzeugen.
    
- **Fazit / Bedeutung für IT-Profis:** Für jeden IT-Sicherheitsexperten, Entwickler und Administrator ist es von entscheidender Bedeutung, den Status der verschiedenen SHA-Versionen zu kennen. Die Migration von unsicheren Algorithmen (MD5, SHA-1) zu aktuellen Standards (SHA-256, SHA-3) ist eine grundlegende Anforderung zur Aufrechterhaltung der Sicherheit von IT-Systemen und zur Einhaltung von Compliance-Vorgaben.