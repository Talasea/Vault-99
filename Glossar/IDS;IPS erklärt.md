**Intrusion Detection System (IDS)**

- **Funktion**:
    - Ein IDS ist ein passives Sicherheitssystem, das den Netzwerkverkehr oder Systemaktivitäten überwacht.
    - Es analysiert Datenströme auf Anzeichen für potenzielle Sicherheitsverletzungen oder verdächtige Aktivitäten.
    - Bei Erkennung einer Bedrohung gibt das IDS eine Warnung aus, beispielsweise in Form eines Alarms oder eines Logeintrags.
    - Es greift jedoch nicht aktiv in den Datenverkehr ein, um Angriffe zu blockieren.
- **Arten von IDS**:
    - **Network-based IDS (NIDS)**: Überwacht den Netzwerkverkehr.
    - **Host-based IDS (HIDS)**: Überwacht Aktivitäten auf einem einzelnen System.
    - **Signature-based IDS**: Erkennt bekannte Angriffsmuster (Signaturen).
    - **Anomaly-based IDS**: Erkennt ungewöhnliche Verhaltensweisen, die von der Norm abweichen.
    - **Hybrid-IDS**: Kombiniert mehrere Erkennungsmethoden.
- **Einsatzbereiche**:
    - Überwachung von Netzwerken und Systemen auf verdächtige Aktivitäten.
    - Erkennung von Angriffen und Sicherheitsverletzungen.
    - Forensische Analyse von Sicherheitsvorfällen.

**Intrusion Prevention System (IPS)**

- **Funktion**:
    - Ein IPS ist ein aktives Sicherheitssystem, das über die Überwachungsfunktionen eines IDS hinausgeht.
    - Es analysiert den Netzwerkverkehr oder Systemaktivitäten in Echtzeit und greift aktiv ein, um erkannte Bedrohungen zu blockieren.
    - Bei Erkennung eines Angriffs kann das IPS beispielsweise den betreffenden Datenverkehr blockieren, die Verbindung unterbrechen oder den Angreifer isolieren.
- **Arten von IPS**:
    - Ähnlich wie beim IDS gibt es netzwerk- und hostbasierte IPS-Lösungen sowie solche, die auf Signaturen oder Anomalien basieren.
- **Einsatzbereiche**:
    - Aktiver Schutz von Netzwerken und Systemen vor Angriffen.
    - Blockierung von Schadsoftware, Viren und anderen Bedrohungen.
    - Verhinderung von DDoS-Angriffen (Distributed Denial-of-Service).

**Unterschiede zwischen IDS und IPS**

- Der Hauptunterschied besteht darin, dass ein IDS ein passives Überwachungssystem ist, während ein IPS ein aktives Eingriffssystem ist.
- Ein IDS erkennt Bedrohungen und gibt Warnungen aus, während ein IPS Bedrohungen aktiv blockiert.

**Beispiel: Suricata**

- Suricata ist ein Open-Source-IDS/IPS-System, das sowohl als NIDS als auch als IPS eingesetzt werden kann.
- Es bietet Funktionen zur Signature-based Detection, Anomaly Detection und Protokollanalyse.
- Suricata ist bekannt für seine hohe Leistung und Flexibilität.
- Suricata benutzt sogenannte "Rules" um den Netzwerktraffic zu analisieren. Diese Rules definieren wie sich der Trafffic verhalten soll oder darf.
- Suricata ist in der lage eine Große vielfalt an Protokollen zu Analysieren.

**Wichtige Aspekte gemäß ISO 27001**

- Die Implementierung von IDS/IPS-Systemen ist ein wichtiger Bestandteil eines Informationssicherheitsmanagementsystems (ISMS) gemäß ISO 27001.
- Die Systeme sollten regelmäßig überwacht und aktualisiert werden, um eine effektive Bedrohungserkennung und -abwehr zu gewährleisten.
- Die Protokollierung von IDS/IPS-Ereignissen ist wichtig für die forensische Analyse von Sicherheitsvorfällen.



**Intrusion Detection System (IDS)**

Da ein IDS primär ein Überwachungssystem ist, beschränken sich seine unmittelbaren Gegenmaßnahmen auf das Erkennen und Melden von Angriffen. Hier sind die typischen Reaktionen:

- **Alarmierung**:
    - Das IDS generiert Alarme, die an das Sicherheitspersonal oder an ein Security Information and Event Management (SIEM)-System weitergeleitet werden.
    - Diese Alarme enthalten detaillierte Informationen über den Angriff, wie Quelle, Ziel, Art des Angriffs und Schweregrad.
- **Protokollierung**:
    - Das IDS protokolliert alle verdächtigen Aktivitäten, um eine spätere forensische Analyse zu ermöglichen.
    - Diese Protokolle sind entscheidend, um den Ablauf eines Angriffs zu rekonstruieren und Schwachstellen zu identifizieren.
- **Benachrichtigungen**:
    - Das IDS kann Benachrichtigungen in verschiedenen Formen versenden, z. B. E-Mails, SMS oder SNMP-Traps, um das Sicherheitspersonal umgehend zu informieren.

**Intrusion Prevention System (IPS)**

Ein IPS geht über die reine Erkennung hinaus und ergreift aktive Maßnahmen, um Angriffe zu blockieren. Hier sind die häufigsten Gegenmaßnahmen:

- **Blockierung von Datenverkehr**:
    - Das IPS kann verdächtigen Datenverkehr in Echtzeit blockieren, indem es Pakete verwirft oder Verbindungen schließt.
    - Dies verhindert, dass der Angriff sein Ziel erreicht und Schaden anrichtet.
- **Unterbrechung von Verbindungen**:
    - Das IPS kann aktive Verbindungen unterbrechen, die für einen Angriff genutzt werden.
    - Dies isoliert den Angreifer und verhindert weitere Angriffe.
- **Sperrung von IP-Adressen**:
    - Das IPS kann IP-Adressen von Angreifern automatisch sperren, um weitere Angriffe von diesen Quellen zu verhindern.
    - Dies kann temporär oder Permanent erfolgen, und auch in verbindung mit einer Firewall benutzt werden.
- **Änderung von Sicherheitsrichtlinien**:
    - In einigen Fällen kann das IPS automatisch Sicherheitsrichtlinien anpassen, um sich gegen neue Angriffsmuster zu schützen.
- **Quarantäne**:
    - Bei Hostbasierten IPS systemen, ist es möglich infizierte Dateien in die Quarantäne zu verschieben.

**Zusätzliche Überlegungen**

- Die Wirksamkeit von IDS/IPS-Gegenmaßnahmen hängt von der Aktualität der Signaturdatenbanken und der Konfiguration des Systems ab.
- Falsch positive Erkennungen können zu unnötigen Blockaden führen, daher ist eine sorgfältige Konfiguration und Feinabstimmung wichtig.
- IDS/IPS-Systeme sollten regelmäßig überwacht und gewartet werden, um eine optimale Leistung zu gewährleisten.




Funktionsweise IDS 

**1. Signaturbasierte Erkennung (Signature-based Detection)**

- **Funktionsweise:**
    - Diese Methode vergleicht den Netzwerkverkehr oder Systemaktivitäten mit einer Datenbank bekannter Angriffsmuster, den sogenannten Signaturen.
    - Eine Signatur ist ein spezifisches Muster, das mit einem bekannten Angriff in Verbindung gebracht wird, z. B. eine bestimmte Folge von Bytes im Netzwerkverkehr oder eine bestimmte Abfolge von Systemaufrufen.
    - Wenn das IDS eine Übereinstimmung zwischen dem überwachten Datenverkehr und einer Signatur findet, wird ein Alarm ausgelöst.
- **Vorteile:**
    - Hohe Genauigkeit bei der Erkennung bekannter Angriffe.
    - Geringe Anzahl von Fehlalarmen, wenn die Signaturen gut definiert sind.
- **Nachteile:**
    - Kann unbekannte Angriffe (Zero-Day-Exploits) nicht erkennen.
    - Die Signaturdatenbank muss regelmäßig aktualisiert werden, um neue Bedrohungen zu erkennen.

**2. Anomaliebasierte Erkennung (Anomaly-based Detection)**

- **Funktionsweise:**
    - Diese Methode erstellt ein Profil des "normalen" Verhaltens des Netzwerks oder Systems.
    - Das IDS überwacht dann den Datenverkehr und Systemaktivitäten und vergleicht sie mit dem Profil.
    - Wenn das IDS eine signifikante Abweichung vom normalen Verhalten feststellt, wird ein Alarm ausgelöst.
    - Das Profil für das Normale verhalten wird mithilfe von Maschinellem lernen, oder Statistischen verfahren erstellt.
- **Vorteile:**
    - Kann unbekannte Angriffe erkennen.
    - Erfordert keine ständige Aktualisierung von Signaturdatenbanken.
- **Nachteile:**
    - Hohe Anzahl von Fehlalarmen, da normales Verhalten variieren kann.
    - Erfordert eine sorgfältige Konfiguration und Feinabstimmung.

**3. Protokollbasierte Erkennung (Protocol-based Detection)**

- **Funktionsweise:**
    - Diese Methode analysiert den Netzwerkverkehr auf der Protokollebene.
    - Das IDS überprüft, ob der Datenverkehr den Protokollstandards entspricht.
    - Wenn das IDS Verstöße gegen die Protokollstandards feststellt, wird ein Alarm ausgelöst.
- **Vorteile:**
    - Kann Angriffe erkennen, die Protokollschwachstellen ausnutzen.
    - Hilfreich bei der Erkennung von Angriffen, die sich als legitimer Datenverkehr tarnen.
- **Nachteile:**
    - Erfordert detaillierte Kenntnisse der Protokollstandards.
    - Kann rechenintensiv sein.

**4. Verhaltensbasierte Erkennung (Behavior-based Detection)**

- **Funktionsweise:**
    - Diese Methode überwacht das Verhalten von Benutzern und Anwendungen.
    - Das IDS erstellt ein Profil des "normalen" Verhaltens und erkennt Abweichungen.
    - Zum Beispiel kann das IDS erkennen, wenn ein Benutzer plötzlich auf ungewöhnliche Dateien zugreift oder wenn eine Anwendung unerwartet auf Netzwerkressourcen zugreift.
- **Vorteile:**
    - Kann Insider-Bedrohungen und komplexe Angriffe erkennen.
    - Bietet einen ganzheitlichen Überblick über das Sicherheitsniveau.
- **Nachteile:**
    - Erfordert eine komplexe Konfiguration und Feinabstimmung.
    - Kann rechenintensiv sein.

**Zusammenfassend**

- Ein IDS verwendet eine Kombination dieser Methoden, um Angriffe zu erkennen.
- Die Wahl der Methoden hängt von den spezifischen Sicherheitsanforderungen und dem Bedrohungsszenario ab.
- Die Weiter entwicklung des IDS bereiches führt dazu das immer mehr Künstliche Intelligenz genutzt wird um die Erkennung zu verbessern.