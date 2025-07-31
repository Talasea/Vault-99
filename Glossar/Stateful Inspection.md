- **Kerndefinition:** **Stateful Inspection**, auch als zustandsgesteuerte Paketfilterung bekannt, ist eine fortschrittliche Firewall-Technologie, die den Verbindungsstatus von Netzwerkverkehr überwacht. Sie trifft Filterentscheidungen nicht nur auf Basis einzelner Pakete, sondern basierend auf dem Kontext der gesamten Kommunikationssitzung.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** Eine Stateful Firewall führt eine Zustandstabelle (State Table), in der sie Informationen über alle aktiven Verbindungen speichert (z. B. Quell-/Ziel-IP, Ports, Protokollstatus). Wenn ein ausgehendes Paket eine neue Verbindung aufbaut, wird ein Eintrag in dieser Tabelle erstellt. Eingehende Antwortpakete werden dann mit der Tabelle abgeglichen.
        
    - **Kontextbezogene Filterung:** Nur Pakete, die zu einer bekannten, aktiven Verbindung gehören, dürfen die Firewall passieren. Beispielsweise wird ein DNS-Antwortpaket aus dem Internet nur dann zugelassen, wenn es eine passende, kurz zuvor gestellte DNS-Anfrage aus dem internen Netzwerk gab.
        
    - **Zweck:** Das Ziel ist eine deutlich höhere Sicherheit als bei der einfachen (stateless) Paketfilterung, da die Firewall den logischen Zusammenhang der Kommunikation versteht.
        
- **Einordnung in den Gesamtkontext:** Stateful Inspection ist die technologische Weiterentwicklung der **stateless Paketfilterung**, die jedes Paket isoliert betrachtet. Sie ist die Grundlage für die meisten modernen Firewalls, einschließlich **Next-Generation Firewalls (NGFWs)**, die diese Funktionalität um weitere Sicherheitsdienste wie Intrusion Prevention (IPS) und Application Control erweitern.
    
- **Sicherheitsaspekte:** Durch das Verständnis des Verbindungskontexts schützt eine Stateful Firewall effektiv vor vielen Arten von Angriffen, bei denen Angreifer versuchen, gefälschte Pakete in das Netzwerk einzuschleusen. Die Zustandstabelle selbst kann jedoch ein Ziel für Denial-of-Service-Angriffe sein, bei denen ein Angreifer versucht, die Tabelle durch eine Flut von neuen Verbindungsanfragen zu überlasten.
    
- **Praxisbeispiel / Analogie:** Eine stateless Firewall ist wie ein Türsteher, der nur prüft, ob jemand eine Eintrittskarte hat. Eine Stateful Firewall ist ein aufmerksamerer Türsteher: Er merkt sich nicht nur, wer mit einer gültigen Karte hineingegangen ist, sondern erwartet auch, dass nur diese Personen wieder herauskommen. Er würde eine fremde Person, die plötzlich von innen aus der Tür kommt, als verdächtig einstufen und aufhalten.
    
- **Fazit / Bedeutung für IT-Profis:** Stateful Inspection ist eine fundamentale Technologie der modernen Netzwerksicherheit. Jeder Netzwerk- und Sicherheitsadministrator muss das Prinzip verstehen, da es die Basis für die Konfiguration und das Troubleshooting von Firewalls bildet. Es ist der Standard für den Schutz von Netzwerkgrenzen.