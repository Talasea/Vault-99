- **Kerndefinition:** **DLP (Data Loss Prevention)**, auch als Data Leakage Prevention bekannt, bezeichnet eine Reihe von Strategien und technischen Werkzeugen, die sicherstellen sollen, dass sensible und vertrauliche Daten ein Unternehmen nicht unbefugt verlassen. DLP-Systeme identifizieren, überwachen und schützen Daten im Ruhezustand (Data at Rest), in Bewegung (Data in Motion) und in Verwendung (Data in Use).
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** Ein DLP-System wird mit Regeln und Richtlinien konfiguriert, die definieren, was sensible Daten sind (z. B. durch Schlüsselwörter, reguläre Ausdrücke für Kreditkartennummern oder durch Datenklassifizierung).
        
    - **Überwachungspunkte:**
        
        - **DLP for Network:** Überwacht den ausgehenden Netzwerkverkehr (z. B. E-Mails, Web-Uploads).
            
        - **DLP for Endpoint:** Läuft auf den Endgeräten (Laptops) und kontrolliert Aktionen wie das Kopieren von Daten auf USB-Sticks oder das Drucken.
            
        - **DLP for Storage:** Scannt Fileserver und Cloud-Speicher auf unsachgemäß abgelegte sensible Daten.
            
    - **Aktionen:** Wenn ein Regelverstoß erkannt wird, kann das System den Vorgang blockieren, eine Warnung an den Benutzer senden, den Vorfall protokollieren oder einen Administrator alarmieren.
        
- **Einordnung in den Gesamtkontext:** DLP ist eine spezialisierte Sicherheitstechnologie, die sich auf den Schutz vor Datenabfluss konzentriert. Sie ergänzt andere Sicherheitsmaßnahmen wie Firewalls (die den Zugriff kontrollieren) und Verschlüsselung (die die Daten unlesbar macht). DLP konzentriert sich auf den _Inhalt_ der Daten.
    
- **Sicherheitsaspekte:** DLP ist ein direktes Werkzeug zur Verhinderung von Datenpannen, sei es durch böswillige Insider, unachtsame Mitarbeiter oder kompromittierte Konten. Es hilft Unternehmen, Compliance-Anforderungen (wie die der DSGVO) zu erfüllen, indem es den unkontrollierten Abfluss von personenbezogenen Daten verhindert und nachweisbar macht.
    
- **Praxisbeispiel / Analogie:** Ein DLP-System ist wie ein extrem wachsamer und intelligenter Pförtner am Ausgang eines Forschungslabors. Er schaut nicht nur auf den Ausweis der Personen, die hinausgehen, sondern er hat auch einen Scanner, der den Inhalt jeder mitgeführten Tasche analysiert. Entdeckt er eine als "streng geheim" markierte Forschungsformel, schlägt er Alarm und verhindert, dass die Tasche das Gebäude verlässt.
    
- **Fazit / Bedeutung für IT-Profis:** Für Sicherheits- und Compliance-Beauftragte sind DLP-Lösungen ein wichtiges Instrument zum Schutz von geistigem Eigentum und sensiblen Kundendaten. Die Implementierung ist jedoch komplex, da eine präzise Definition von sensiblen Daten und die sorgfältige Abstimmung der Regeln erforderlich sind, um den normalen Geschäftsbetrieb nicht durch Fehlalarme (False Positives) zu stören.