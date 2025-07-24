[[IT_Grundschutz_Kompendium_Edition2023 (1).pdf]]

**IT-Grundschutz-Kompendium: Das Herzstück des IT-Grundschutzes**

Das IT-Grundschutz-Kompendium ist eine umfangreiche Sammlung von _Bausteinen_, _Gefährdungen_ und _Anforderungen_ (Sicherheitsmaßnahmen). Es dient als _zentrale Ressource_ für die Umsetzung des IT-Grundschutzes nach der Methodik des BSI-Standards 200-2. Das Kompendium wird regelmäßig aktualisiert, um neuen Bedrohungen und Technologien Rechnung zu tragen.

**Ziel des IT-Grundschutz-Kompendiums**

- **Konkrete Hilfestellung:** Bereitstellung _detaillierter_ und _praxisorientierter_ Empfehlungen für die Absicherung von IT-Systemen und Informationen.
- **Modularer Aufbau:** Ermöglichung einer _flexiblen_ und _bedarfsgerechten_ Auswahl von Sicherheitsmaßnahmen.
- **Umfassende Abdeckung:** Berücksichtigung _aller_ relevanten Aspekte der Informationssicherheit (von organisatorischen über infrastrukturelle bis hin zu technischen Maßnahmen).
- **Anpassbarkeit:** Unterstützung verschiedener Sicherheitsstufen (Basis, Standard, Hoch) und die Möglichkeit der Anpassung an spezifische Risiken.

**Struktur des IT-Grundschutz-Kompendiums**

Das Kompendium ist in _Schichten_ und _Bausteine_ gegliedert. Diese Struktur ermöglicht eine systematische Modellierung der IT-Landschaft einer Organisation und die Auswahl der relevanten Sicherheitsmaßnahmen.

- **Schichten:** Das Kompendium ist in fünf Schichten unterteilt, die die verschiedenen Ebenen einer IT-Infrastruktur abbilden:
    
    1. **Übergreifende Aspekte (APP):** Allgemeine Sicherheitsanforderungen, die für die gesamte Organisation gelten (z.B. Sicherheitsleitlinie, Organisation, Personal, Notfallvorsorge, Datenschutz).
    2. **Infrastruktur (INF):** Anforderungen an Gebäude, Räume, Verkabelung, Stromversorgung, Klimatisierung, etc.
    3. **IT-Systeme (SYS):** Anforderungen an Hardware und Software (z.B. Server, Clients, Betriebssysteme, Virtualisierung, mobile Geräte).
    4. **Netze (NET):** Anforderungen an die Netzwerksicherheit (z.B. LAN, WLAN, WAN, Fernzugriff, Firewalls).
    5. **Anwendungen (OPS):** Anforderungen an die Sicherheit von Anwendungen (z.B. Webanwendungen, Datenbanken, E-Mail, Cloud-Dienste).
- **Bausteine:** Innerhalb jeder Schicht ist das Kompendium in _Bausteine_ unterteilt. Jeder Baustein beschreibt einen bestimmten _Aspekt_ der IT-Sicherheit (z.B. "SYS.1.1 Allgemeiner Server", "NET.3.2 Firewall", "APP.4.1 Kryptokonzept").
    

**Inhalt eines Bausteins**

Jeder Baustein im Kompendium enthält die folgenden Informationen:

1. **Beschreibung:**
    
    - Erläuterung des Bausteins und seines Zwecks.
    - Abgrenzung zu anderen Bausteinen.
    - Hinweise zur Anwendung.
2. **Gefährdungen:**
    
    - Eine Liste _typischer Bedrohungen_, die den Baustein betreffen (z.B. "G 0.25 Ausspähen von Informationen (Spionage)", "G 0.18 Fehlplanung oder fehlende Anpassung", "G 0.45 Schadprogramme").
    - Jede Gefährdung ist mit einer eindeutigen Kennung versehen (z.B. "G 0.25").
    - Die Gefährdungen sind _nicht abschließend_; Organisationen können bei Bedarf eigene, spezifische Gefährdungen hinzufügen.
3. **Anforderungen:**
    
    - Eine Liste _konkreter Sicherheitsmaßnahmen_ (Anforderungen), die umgesetzt werden müssen, um den Gefährdungen zu begegnen.
    - Jede Anforderung ist mit einer eindeutigen Kennung versehen (z.B. "SYS.1.1.A1 Erstellung einer Richtlinie für Server (B)", "SYS.1.1.A5 Härtung des Betriebssystems (S)").
    - Die Anforderungen sind in drei Kategorien unterteilt:
        - **(B) Basis-Anforderungen:** Grundlegende Sicherheitsmaßnahmen, die _immer_ umgesetzt werden sollten (entsprechen der Basis-Absicherung nach BSI-Standard 200-2).
        - **(S) Standard-Anforderungen:** Erweiterte Sicherheitsmaßnahmen, die für Organisationen mit _normalem_ oder _erhöhtem_ Schutzbedarf empfohlen werden (entsprechen der Standard-Absicherung nach BSI-Standard 200-2).
        - **(H) Hohe Anforderungen:** Zusätzliche Sicherheitsmaßnahmen für Organisationen mit _sehr hohem_ Schutzbedarf oder bei Vorliegen spezifischer Risiken.
    - Für jede Anforderung gibt es eine detaillierte Beschreibung, Hinweise zur Umsetzung und ggf. Verweise auf weiterführende Informationen.
    - Die Anforderungen sind mit _MUSS_, _SOLLTE_ und _KANN_ gekennzeichnet
        - **MUSS-Anforderungen**: Diese Basisanforderungen sind grundsätzlich umzusetzen
        - **SOLLTE-Anforderungen**: Haben empfehlenden Charakter.
        - **KANN-Anforderungen:** Sind optional.

**Beispiel: Baustein SYS.1.1 Allgemeiner Server**

- **Beschreibung:** Dieser Baustein behandelt allgemeine Sicherheitsanforderungen für Server, unabhängig von ihrem spezifischen Einsatzzweck (z.B. Dateiserver, Webserver, Datenbankserver).
- **Gefährdungen (Auswahl):**
    - G 0.14 Ausfall oder Störung von Dienstleistungen
    - G 0.18 Fehlplanung oder fehlende Anpassung
    - G 0.19 Offenlegung schützenswerter Informationen
    - G 0.21 Manipulation von Hard- oder Software
    - G 0.22 Diebstahl von Geräten, Datenträgern oder Dokumenten
    - G 0.25 Ausspähen von Informationen (Spionage)
    - G 0.26 Unbefugtes Eindringen in IT-Systeme
    - G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
    - G 0.45 Schadprogramme
- **Anforderungen (Auswahl):**
    - **SYS.1.1.A1 Erstellung einer Richtlinie für Server (B):** Es muss eine Richtlinie erstellt werden, die die grundlegenden Sicherheitsanforderungen für Server festlegt (z.B. Installation, Konfiguration, Wartung, Zugriffsbeschränkungen).
    - **SYS.1.1.A3 Auswahl eines geeigneten Server-Betriebssystems (B):** Es muss ein Server-Betriebssystem ausgewählt werden, das den Sicherheitsanforderungen entspricht und regelmäßig mit Sicherheitsupdates versorgt wird.
    - **SYS.1.1.A5 Härtung des Betriebssystems (S):** Das Betriebssystem des Servers muss gehärtet werden, um die Angriffsfläche zu reduzieren (z.B. Deaktivierung unnötiger Dienste, restriktive Konfiguration der Firewall, Installation von Virenschutzsoftware).
    - **SYS.1.1.A11 Protokollierung sicherheitsrelevanter Ereignisse (S):** Sicherheitsrelevante Ereignisse auf dem Server müssen protokolliert werden, um Angriffe und Fehlfunktionen erkennen und nachvollziehen zu können.
    - **SYS.1.1.A14 Schutz vor Schadprogrammen (H):** Es müssen zusätzliche Maßnahmen zum Schutz vor Schadprogrammen implementiert werden (z.B. Einsatz von Application Whitelisting, regelmäßige Sicherheitsüberprüfungen).

**Nutzung des IT-Grundschutz-Kompendiums**

Das IT-Grundschutz-Kompendium wird im Rahmen der IT-Grundschutz-Methodik (BSI-Standard 200-2) wie folgt genutzt:

1. **Strukturanalyse:** Die IT-Landschaft der Organisation wird erfasst und in einem Informationsverbund modelliert.
2. **Schutzbedarfsfeststellung:** Für jedes Objekt im Informationsverbund wird der Schutzbedarf ermittelt (hinsichtlich Vertraulichkeit, Integrität und Verfügbarkeit).
3. **Modellierung:** Die relevanten Bausteine aus dem Kompendium werden den Objekten im Informationsverbund zugeordnet. Dabei werden die Anforderungen (Basis, Standard, Hoch) an den Schutzbedarf angepasst.
4. **IT-Grundschutz-Check:** Der Ist-Zustand der IT-Sicherheit wird mit den Soll-Anforderungen aus der Modellierung verglichen. Sicherheitslücken werden identifiziert.
5. **Risikoanalyse (optional):** Bei Bedarf (insbesondere bei hohem Schutzbedarf) wird eine detailliertere Risikoanalyse durchgeführt, um zusätzliche, spezifische Risiken zu identifizieren und zu bewerten.
6. **Umsetzung der Maßnahmen:** Die ausgewählten Sicherheitsmaßnahmen werden umgesetzt und dokumentiert.
7. **Aufrechterhaltung und kontinuierliche Verbesserung:** Die Wirksamkeit der Maßnahmen wird regelmäßig überprüft und an neue Bedrohungen und Veränderungen angepasst.

**Vorteile des IT-Grundschutz-Kompendiums**

- **Praxisorientiert:** Bietet konkrete und detaillierte Anweisungen für die Umsetzung von Sicherheitsmaßnahmen.
- **Umfassend:** Deckt alle relevanten Aspekte der Informationssicherheit ab.
- **Modular:** Ermöglicht eine flexible und bedarfsgerechte Auswahl von Sicherheitsmaßnahmen.
- **Aktuell:** Wird regelmäßig aktualisiert, um neuen Bedrohungen und Technologien Rechnung zu tragen.
- **Kostenlos:** Ist als kostenloser Download auf der Website des BSI verfügbar.

**Nachteile des IT-Grundschutz-Kompendiums**

- **Umfangreich:** Kann für Einsteiger überwältigend wirken.
- **Komplex:** Die Anwendung erfordert ein gewisses Maß an Fachwissen und Erfahrung im Bereich Informationssicherheit.
- **Dokumentationsaufwand:** Die Umsetzung des IT-Grundschutzes ist mit einem gewissen Dokumentationsaufwand verbunden.

**Zusammenfassung**

Das IT-Grundschutz-Kompendium ist ein mächtiges Werkzeug für die Umsetzung von Informationssicherheit. Es bietet eine umfassende Sammlung von Bausteinen, Gefährdungen und Anforderungen, die Organisationen dabei unterstützen, ein angemessenes Sicherheitsniveau für ihre IT-Systeme und Informationen zu erreichen und aufrechtzuerhalten. Die systematische Anwendung des Kompendiums im Rahmen der IT-Grundschutz-Methodik ermöglicht eine strukturierte und nachvollziehbare Vorgehensweise zur Verbesserung der Informationssicherheit.

Ich hoffe, diese ausführliche Erklärung des IT-Grundschutz-Kompendiums ist hilfreich für dich und entspricht den Anforderungen deiner Rolle als Systemadministrator, Sicherheitsbeauftragter und Spezialist für Cyber-Sicherheit.




Das **IT-Grundschutz-Kompendium** des Bundesamts für Sicherheit in der Informationstechnik (BSI) ist ein umfassendes Regelwerk und eine Sammlung von Best Practices für die Informationssicherheit. Es dient Organisationen jeder Größe als **Anleitung zur systematischen Umsetzung von IT-Sicherheit**. Ziel ist es, ein angemessenes Schutzniveau für die IT-Systeme und die darin verarbeiteten Informationen zu erreichen.

Das Kompendium ist modular aufgebaut und deckt verschiedene Aspekte der Informationssicherheit ab. Die Grafik, die Sie beigefügt haben, zeigt einige dieser wichtigen Module. Gerne gehe ich detaillierter auf die **vier prominent hervorgehobenen Punkte** ein und erläutere diese:

**1. Risikoanalyse: Identifizierung von Risiken und Schwachstellen in IT-Systemen und -Prozessen.**

- **Was bedeutet Risikoanalyse im IT-Grundschutz-Kontext?** Die Risikoanalyse ist der **erste und fundamentale Schritt** im IT-Grundschutzprozess. Bevor Sicherheitsmaßnahmen ergriffen werden können, muss man verstehen, **welche Risiken überhaupt bestehen** und **wo die Schwachstellen liegen**. Es geht darum, potenzielle Bedrohungen und die Verwundbarkeit der IT-Systeme und Geschäftsprozesse systematisch zu identifizieren und zu bewerten.
    
- **Ziele der Risikoanalyse:**
    
    - **Identifizierung von schützenswerten Objekten:** Welche Assets (z.B. Daten, Systeme, Anwendungen, Gebäude, Personal) sind für die Organisation kritisch und müssen besonders geschützt werden?
    - **Ermittlung von Bedrohungen:** Welche Gefahren können diesen Assets schaden? (z.B. Cyberangriffe, Naturkatastrophen, menschliches Fehlverhalten, technische Ausfälle).
    - **Analyse von Schwachstellen:** Wo sind die Schwachpunkte in der IT-Infrastruktur, Organisation oder Prozessen, die Bedrohungen ausnutzen könnten? (z.B. ungepatchte Software, fehlende Zugriffskontrollen, mangelndes Sicherheitsbewusstsein der Mitarbeiter).
    - **Bewertung des Risikos:** Wie wahrscheinlich ist es, dass eine Bedrohung eine Schwachstelle ausnutzt, und welche potenziellen Schäden könnten dadurch entstehen? (Dies führt zur Risikomatrix, die wir bereits besprochen haben).
- **Methoden im IT-Grundschutz:** Das IT-Grundschutz-Kompendium empfiehlt strukturierte Methoden zur Risikoanalyse. Dazu gehören beispielsweise:
    
    - **Workshop-basierte Risikoanalysen:** Experten aus verschiedenen Bereichen (IT, Fachabteilungen, Management) arbeiten zusammen, um Risiken zu identifizieren und zu bewerten.
    - **Checklisten und Kataloge:** Das BSI stellt umfangreiche Kataloge mit möglichen Bedrohungen und Schwachstellen bereit, die als Grundlage für die Analyse dienen.
    - **Szenario-basierte Analyse:** Mögliche Angriffsszenarien oder Schadensfälle werden durchgespielt, um die potenziellen Auswirkungen und die Schwachstellen zu erkennen.
- **Ergebnis der Risikoanalyse:** Das Ergebnis der Risikoanalyse ist eine **Risikobewertung**, die priorisierte Risiken und identifizierte Schwachstellen auflistet. Diese bildet die Grundlage für die Auswahl und Implementierung geeigneter Sicherheitsmaßnahmen.
    

**2. Sicherheitsmaßnahmen: Empfehlungen zur Implementierung von Sicherheitsmaßnahmen wie Zugriffskontrolle, Verschlüsselung und Datensicherung.**

- **Was sind Sicherheitsmaßnahmen im IT-Grundschutz-Kontext?** Nachdem die Risiken identifiziert wurden, geht es darum, **geeignete Sicherheitsmaßnahmen zu definieren und umzusetzen**, um diese Risiken zu minimieren oder zu eliminieren. Das IT-Grundschutz-Kompendium bietet einen umfassenden **Katalog an bewährten Sicherheitsmaßnahmen**, die in verschiedenen Schutzbausteinen (z.B. Organisation, Personal, Hardware, Software, Kommunikation) organisiert sind.
    
- **Beispiele für Sicherheitsmaßnahmen (aus dem Bild genannt):**
    
    - **Zugriffskontrolle:** Regelt, wer auf welche IT-Systeme, Anwendungen und Daten zugreifen darf. Dies umfasst Maßnahmen wie Benutzerkonten, Passwörter, Berechtigungskonzepte, Multi-Faktor-Authentifizierung etc. Ziel ist es, unbefugten Zugriff zu verhindern und sicherzustellen, dass nur autorisierte Personen Zugriff auf sensible Informationen haben.
    - **Verschlüsselung:** Schützt die Vertraulichkeit von Daten sowohl bei der Speicherung (Data-at-Rest) als auch bei der Übertragung (Data-in-Transit). Durch Verschlüsselung werden Daten unlesbar gemacht für Unbefugte. Beispiele sind Festplattenverschlüsselung, E-Mail-Verschlüsselung, SSL/TLS für Webkommunikation.
    - **Datensicherung (Backup):** Sichert regelmäßig Daten, um Datenverlust bei Ausfällen, Beschädigungen oder Cyberangriffen zu verhindern. Wichtige Aspekte sind die Backup-Strategie (vollständig, inkrementell, differentiell), die Speicherung der Backups (lokal, extern, Cloud) und die regelmäßige Überprüfung der Wiederherstellbarkeit.
- **Weitere Kategorien von Sicherheitsmaßnahmen im IT-Grundschutz:** Das Kompendium deckt ein breites Spektrum an Sicherheitsmaßnahmen ab, u.a.:
    
    - **Organisatorische Maßnahmen:** Sicherheitsrichtlinien, Prozesse, Verantwortlichkeiten, Schulungen, Awareness-Kampagnen.
    - **Personelle Maßnahmen:** Sicherheitsüberprüfungen von Personal, Schulungen, Vertraulichkeitsvereinbarungen.
    - **Technische Maßnahmen:** Firewalls, Intrusion Detection Systeme (IDS), Antivirus-Software, Patch-Management, Härtung von Systemen, Protokollierung und Monitoring.
    - **Bauliche und physikalische Maßnahmen:** Zutrittskontrollsysteme für Gebäude und Rechenzentren, Einbruchmeldeanlagen, Brandschutz, Klimatisierung.
- **Auswahl und Implementierung von Sicherheitsmaßnahmen:** Die Auswahl der geeigneten Sicherheitsmaßnahmen hängt von den Ergebnissen der Risikoanalyse und dem Schutzbedarf der jeweiligen Assets ab. Das IT-Grundschutz-Kompendium hilft bei der Auswahl, indem es für verschiedene Schutzziele (Vertraulichkeit, Integrität, Verfügbarkeit) und verschiedene Bereiche (z.B. Server, Clients, Netzwerke, Anwendungen) konkrete Maßnahmen empfiehlt.
    

**3. Notfallmanagement: Planung und Vorbereitung auf Notfälle und Krisensituationen.**

- **Was bedeutet Notfallmanagement im IT-Grundschutz-Kontext?** Trotz aller Präventionsmaßnahmen ist es nicht immer möglich, alle Sicherheitsvorfälle zu verhindern. Daher ist ein **strukturiertes Notfallmanagement unerlässlich**. Es umfasst die Planung und Vorbereitung auf den Fall, dass es zu einem Sicherheitsvorfall kommt, der den IT-Betrieb oder kritische Geschäftsprozesse beeinträchtigt.
    
- **Ziele des Notfallmanagements:**
    
    - **Minimierung von Schäden:** Die Auswirkungen von Notfällen sollen so gering wie möglich gehalten werden.
    - **Schnelle Wiederherstellung des Betriebs:** IT-Systeme und Geschäftsprozesse sollen im Notfall so schnell wie möglich wiederhergestellt werden.
    - **Kontinuität der Geschäftsprozesse:** Kritische Geschäftsprozesse sollen auch im Notfall möglichst aufrechterhalten werden.
    - **Einhaltung gesetzlicher und regulatorischer Anforderungen:** Viele Gesetze und Vorschriften (z.B. DSGVO, KRITIS-Gesetzgebung) fordern ein funktionierendes Notfallmanagement.
- **Bestandteile des Notfallmanagements im IT-Grundschutz:**
    
    - **Notfallvorsorge:** Proaktive Maßnahmen zur Vorbereitung auf Notfälle. Dazu gehören die Erstellung von Notfallplänen, die Definition von Verantwortlichkeiten, die Beschaffung von Notfallausrüstung und die Durchführung von Notfallübungen.
    - **Notfallerkennung:** Prozesse und Systeme, um Notfälle frühzeitig zu erkennen und zu melden (z.B. Monitoring-Systeme, Incident-Response-Teams).
    - **Notfallbewältigung:** Maßnahmen zur Reaktion auf einen eingetretenen Notfall, z.B. die Aktivierung von Notfallplänen, die Durchführung von Wiederherstellungsmaßnahmen, die Kommunikation mit Stakeholdern.
    - **Notfallnachsorge:** Analyse des Notfalls, Ableitung von Verbesserungsmaßnahmen für die Prävention und das Notfallmanagement, Aktualisierung der Notfallpläne.
- **Beispiele für Notfälle im IT-Bereich:**
    
    - Cyberangriffe (z.B. Ransomware-Angriffe, DDoS-Angriffe)
    - Technische Ausfälle (z.B. Serverausfall, Netzausfall, Stromausfall)
    - Naturkatastrophen (z.B. Brand, Wasserschaden)
    - Menschliches Fehlverhalten (z.B. versehentliches Löschen von Daten)

**4. Sicherheitsmanagement: Organisation und Durchführung von Sicherheitsprozessen und -aktivitäten.**

- **Was bedeutet Sicherheitsmanagement im IT-Grundschutz-Kontext?** IT-Sicherheit ist keine einmalige Aufgabe, sondern ein **kontinuierlicher Prozess**. Das Sicherheitsmanagement umfasst die **organisatorischen Strukturen, Prozesse und Verantwortlichkeiten**, die notwendig sind, um IT-Sicherheit dauerhaft zu gewährleisten und kontinuierlich zu verbessern.
    
- **Ziele des Sicherheitsmanagements:**
    
    - **Etablierung einer Sicherheitskultur:** Sicherheit soll als wichtiger Wert in der Organisation verankert werden.
    - **Kontinuierliche Verbesserung der Sicherheit:** Die Sicherheitsmaßnahmen sollen regelmäßig überprüft, angepasst und verbessert werden, um mit neuen Bedrohungen Schritt zu halten.
    - **Effektive Steuerung und Kontrolle der IT-Sicherheit:** Das Management soll einen Überblick über den Sicherheitsstatus haben und in der Lage sein, Sicherheitsmaßnahmen zu steuern und zu kontrollieren.
    - **Compliance mit Gesetzen und Standards:** Das Sicherheitsmanagement soll sicherstellen, dass die Organisation die relevanten Gesetze, Vorschriften und Standards (z.B. DSGVO, ISO 27001, IT-Grundschutz) einhält.
- **Kernbereiche des Sicherheitsmanagements im IT-Grundschutz:**
    
    - **Sicherheitsorganisation:** Definition von Verantwortlichkeiten für IT-Sicherheit, Einrichtung eines Security-Teams oder eines Sicherheitsbeauftragten, Etablierung von Kommunikationskanälen für Sicherheitsfragen.
    - **Sicherheitsrichtlinien und -standards:** Erstellung und Pflege von verbindlichen Sicherheitsrichtlinien, die die Erwartungen und Vorgaben für das Verhalten der Mitarbeiter und den Umgang mit IT-Systemen festlegen.
    - **Sicherheitsbewusstsein und Schulungen:** Durchführung regelmäßiger Schulungen und Awareness-Kampagnen, um das Sicherheitsbewusstsein der Mitarbeiter zu fördern.
    - **Sicherheitsüberprüfung und -audit:** Regelmäßige Überprüfung der Wirksamkeit der Sicherheitsmaßnahmen durch interne Audits oder externe Penetrationstests.
    - **Security Monitoring und Incident Management:** Implementierung von Systemen zur Überwachung der IT-Sicherheit und zur schnellen Reaktion auf Sicherheitsvorfälle (siehe auch Notfallmanagement).
    - **Change Management:** Kontrollierter Prozess für Änderungen an IT-Systemen und -Konfigurationen, um sicherzustellen, dass Sicherheitsaspekte bei Änderungen berücksichtigt werden.
    - **Kontinuierlicher Verbesserungsprozess (KVP):** Regelmäßige Überprüfung und Anpassung des Sicherheitsmanagementsystems, um die Effektivität und Angemessenheit der Sicherheitsmaßnahmen zu gewährleisten.

**Zusammenfassend lässt sich sagen, dass das IT-Grundschutz-Kompendium einen umfassenden Rahmen für die IT-Sicherheit bietet.** Die **Risikoanalyse** bildet die Grundlage, die **Sicherheitsmaßnahmen** setzen die notwendigen Schutzvorkehrungen um, das **Notfallmanagement** sichert die Reaktionsfähigkeit im Krisenfall, und das **Sicherheitsmanagement** stellt sicher, dass IT-Sicherheit als kontinuierlicher Prozess in der Organisation etabliert und gelebt wird. Die **Dokumentation**, die im Bild als fünfter Punkt erwähnt wird, ist ein integraler Bestandteil aller Phasen und Bereiche des IT-Grundschutzes, da eine umfassende Dokumentation die Grundlage für Transparenz, Nachvollziehbarkeit und die kontinuierliche Verbesserung der IT-Sicherheit bildet.