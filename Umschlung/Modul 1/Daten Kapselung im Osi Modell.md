
im OSI-Modell (Open Systems Interconnection) wird die Kapselung von Daten als Prozess beschrieben, bei dem Kontrollinformationen an die Daten angehängt werden, während sie durch die Schichten des OSI-Modells nach unten fließen. Dieser Prozess sichert die Integrität und die erfolgreiche Interpretation der Daten.

Die Kapselung findet in folgenden Schritten statt:

1. **Anwendungsschicht**: Anwendungsdaten werden mit einem Protokollkopf versehen, der für die jeweilige Anwendung spezifische Informationen enthält, wie z.B. HTTP-Header für Webdaten.
2. **Präsentationsschicht**: Eventuell werden Daten konvertiert oder verschlüsselt, um das richtige Format für die Übertragung zu gewährleisten.
3. **Sitzungsschicht**: Es werden zusätzliche Header-Informationen hinzugefügt, um die Steuerung und Koordination der Kommunikation zwischen den Anwendungen zu ermöglichen.
4. **Transportsschicht**: Die Daten werden in Segmente aufgeteilt und mit Quell- und Zielportnummern versehen, um die Übertragung und Rekonstruktion zu ermöglichen.
5. **Netzwerkschicht**: Die Daten werden mit IP-Adresse und anderen Netzwerkinformationen versehen, um die Routenwahl und -zuweisung zu ermöglichen.
6. **Datensicherungsschicht**: Die Daten werden mit Fehlersicherheitsinformationen versehen, um die Übertragung und Rekonstruktion zu sichern.
7. **Physische Schicht**: Die Daten werden in ein physikalisches Signal umgewandelt und übertragen.

Jeder Schritt der Kapselung und Entkapselung ist entscheidend, um die Integrität und die erfolgreiche Interpretation der Daten zu sichern.

## Beispiel: E-Mail-Übertragung

Im Beispiel einer E-Mail-Übertragung wird die Kapselung wie folgt durchgeführt:

- Anwendungsschicht: Die E-Mail-Nachricht wird mit einem SMTP-Header versehen.
- Präsentationsschicht: Die Nachricht wird in ASCII-Format konvertiert.
- Sitzungsschicht: Ein Session-Header wird hinzugefügt, um die Verbindung zwischen dem E-Mail-Client und dem E-Mail-Server zu koordinieren.
- Transportsschicht: Die Nachricht wird in Segmente aufgeteilt und mit Quell- und Zielportnummern versehen.
- Netzwerkschicht: Die Nachricht wird mit IP-Adresse und anderen Netzwerkinformationen versehen.
- Datensicherungsschicht: Fehlersicherheitsinformationen werden hinzugefügt, um die Übertragung und Rekonstruktion zu sichern.
- Physische Schicht: Die Nachricht wird in ein physikalisches Signal umgewandelt und übertragen.

Die Entkapselung findet analog in umgekehrter Reihenfolge statt, um die ursprünglichen Anwendungsdaten zu rekonstruieren.