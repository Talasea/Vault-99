### Wie funktioniert Stateful Inspection?

1. **Verbindungsaufbau:** Wenn ein Gerät in einem Netzwerk eine Verbindung zu einem anderen Gerät herstellt (z. B. ein Computer, der eine Website besucht), werden Informationen über diese Verbindung in einer Tabelle gespeichert, die als "Zustandstabelle" bezeichnet wird. Diese Informationen umfassen:
    
    - IP-Adressen von Absender und Empfänger
    - Ports von Absender und Empfänger
    - Protokoll (z. B. TCP, UDP)
    - Zustand der Verbindung (z. B. "aufgebaut", "wartend", "geschlossen")
2. **Paketprüfung:** Jedes Datenpaket, das die Firewall passiert, wird nicht nur anhand seiner eigenen Informationen (IP-Adresse, Port usw.), sondern auch anhand des Eintrags in der Zustandstabelle überprüft.
    
3. **Entscheidung:** Die Firewall trifft eine Entscheidung darüber, ob das Paket passieren darf oder nicht, basierend auf:
    
    - Den vordefinierten Regeln
    - Dem Zustand der Verbindung (wie in der Zustandstabelle gespeichert)

### Vorteile von Stateful Inspection

- **Erhöhte Sicherheit:** Stateful Inspection Firewalls sind in der Lage, komplexere Angriffe zu erkennen und zu blockieren, die über einfache Paketfilter hinausgehen.
- **Besserer Schutz vor Spoofing:** Durch die Überprüfung des Zustands der Verbindung können Stateful Inspection Firewalls besser zwischen legitimen und gefälschten (Spoofing-) Paketen unterscheiden.
- **Effizientere Verarbeitung:** Da die Firewall den Zustand der Verbindung kennt, muss sie nicht jedes einzelne Paket von Grund auf neu analysieren, was die Verarbeitung beschleunigt.

### Beispiel

Stellen Sie sich vor, Sie besuchen eine Website.

1. Ihr Computer sendet ein Anfragepaket an den Webserver.
2. Die Firewall erstellt einen Eintrag in der Zustandstabelle, der die Details dieser Verbindung speichert.
3. Der Webserver sendet Antwortpakete zurück.
4. Die Firewall überprüft anhand der Zustandstabelle, ob diese Antwortpakete zu einer bereits aufgebauten Verbindung gehören, und lässt sie passieren.
5. Wenn ein Angreifer versuchen würde, gefälschte Pakete in diese Verbindung einzuschleusen, würde die Firewall dies erkennen, da diese Pakete nicht zum Zustand der Verbindung passen.

Zusammenfassend lässt sich sagen, dass Stateful Inspection eine ausgeklügelte Technik ist, die modernen Firewalls ermöglicht, den Netzwerkverkehr nicht nur statisch, sondern auch dynamisch zu analysieren. Dadurch wird die Sicherheit erheblich verbessert, da komplexere Angriffe erkannt und blockiert werden können