
**Was ist Post-Incident Activity?**

Die Post-Incident Activity (oder auch Post-Mortem-Analyse, Lessons Learned, Incident Review) bezeichnet die Aktivitäten, die **nachdem** ein Vorfall (Incident) behoben und der normale Betrieb wiederhergestellt wurde, durchgeführt werden. Ihr Hauptziel ist es, aus dem Vorfall zu lernen, die Ursachen zu verstehen, die Reaktion darauf zu bewerten und Maßnahmen zu definieren, um zukünftige Vorfälle zu verhindern oder deren Auswirkungen zu minimieren.

Es geht dabei nicht darum, Schuld zuzuweisen, sondern eine offene und konstruktive Analyse durchzuführen, um die Prozesse, Systeme und das Wissen im Unternehmen zu verbessern.

**Die typischen Phasen der Post-Incident Activity:**

1. **Vorbereitung:**
    
    - **Festlegen des Zeitrahmens:** Wann soll die Analyse stattfinden? Idealerweise zeitnah nach dem Vorfall, wenn die Erinnerungen noch frisch sind.
    - **Auswahl der Teilnehmer:** Wer sollte an der Analyse teilnehmen? In der Regel gehören dazu die Personen, die direkt in die Reaktion auf den Vorfall involviert waren, sowie Vertreter relevanter Teams (z.B. Entwicklung, Betrieb, Sicherheit).
    - **Sammeln von Daten:** Alle relevanten Informationen zum Vorfall sollten zusammengetragen werden, wie z.B.:
        - Zeitstempel und Chronologie des Vorfalls
        - Auswirkungen auf den Betrieb und die Nutzer
        - Durchgeführte Maßnahmen zur Behebung
        - Kommunikationsprotokolle
        - Logdateien, Monitoring-Daten etc.
2. **Durchführung der Analyse (Post-Incident Review Meeting):**
    
    - **Offene und wertschätzende Atmosphäre schaffen:** Betonen, dass es um Lernen und Verbesserung geht, nicht um Schuldzuweisung.
    - **Chronologische Darstellung des Vorfalls:** Gemeinsam den Ablauf des Vorfalls rekonstruieren.
    - **Identifizierung der Ursachen:** Warum ist der Vorfall passiert? Hierbei können verschiedene Methoden angewendet werden, wie z.B. die 5-Why-Methode oder das Ishikawa-Diagramm (Fischgräten-Diagramm). Es ist wichtig, die _grundlegenden_ Ursachen (Root Causes) zu finden, nicht nur die Symptome.
    - **Bewertung der Reaktion:** Was lief gut bei der Reaktion auf den Vorfall? Was hätte besser laufen können?
    - **Identifizierung von Verbesserungspotenzial:** Welche konkreten Maßnahmen können ergriffen werden, um ähnliche Vorfälle in Zukunft zu verhindern oder deren Auswirkungen zu reduzieren?
    - **Priorisierung der Maßnahmen:** Welche Maßnahmen sind am wichtigsten und sollten zuerst umgesetzt werden?
    - **Zuweisung von Verantwortlichkeiten und Deadlines:** Wer ist für die Umsetzung welcher Maßnahme verantwortlich und bis wann soll diese abgeschlossen sein?
3. **Dokumentation und Nachverfolgung:**
    
    - **Erstellung eines Post-Incident Reports:** Dieser Bericht fasst die Analyseergebnisse, die identifizierten Ursachen und die beschlossenen Maßnahmen zusammen. Er sollte für alle relevanten Stakeholder zugänglich sein.
    - **Verfolgung der Umsetzung der Maßnahmen:** Es muss sichergestellt werden, dass die beschlossenen Maßnahmen auch tatsächlich umgesetzt werden. Dies kann durch regelmäßige Überprüfungen und Fortschrittsberichte erfolgen.
    - **Überprüfung der Wirksamkeit der Maßnahmen:** Nach einer gewissen Zeit sollte überprüft werden, ob die umgesetzten Maßnahmen die gewünschte Wirkung erzielt haben.

**Warum ist Post-Incident Activity wichtig?**

- **Lernen aus Fehlern:** Sie ermöglicht es, aus vergangenen Vorfällen zu lernen und die gleichen Fehler in Zukunft zu vermeiden.
- **Verbesserung der Prozesse:** Sie deckt Schwachstellen in den Prozessen auf und ermöglicht deren Optimierung.
- **Stärkung der Resilienz:** Sie trägt dazu bei, die Widerstandsfähigkeit der Systeme und Organisation gegenüber zukünftigen Vorfällen zu erhöhen.
- **Verbesserung der Kommunikation und Zusammenarbeit:** Der gemeinsame Analyseprozess fördert die Zusammenarbeit und das Verständnis zwischen verschiedenen Teams.
- **Wissensaufbau:** Die Dokumentation der Vorfälle und der daraus gezogenen Lehren baut wertvolles Wissen im Unternehmen auf.

**Referenzen und weiterführende Informationen:**

Hier sind einige allgemeine Bereiche und Konzepte, die die Post-Incident Activity behandeln und als Referenzen dienen können:

- **ITIL (Information Technology Infrastructure Library):** ITIL ist ein Framework für das IT-Service-Management und beinhaltet einen detaillierten Prozess für das Incident Management, einschließlich der Post-Incident Review.
- **SRE (Site Reliability Engineering):** SRE-Prinzipien, insbesondere das Konzept des "Blameless Postmortem", legen großen Wert auf die Analyse von Vorfällen ohne Schuldzuweisung, um daraus zu lernen und die Zuverlässigkeit von Systemen zu verbessern.
- **Agile und DevOps Praktiken:** In agilen und DevOps-Umgebungen sind Post-Incident Reviews ein fester Bestandteil des kontinuierlichen Verbesserungsprozesses.
- **Projektmanagement:** Auch im Projektmanagement werden nach Abschluss von Projekten oder nach dem Auftreten von Problemen "Lessons Learned"-Sitzungen durchgeführt, die ähnliche Ziele verfolgen wie die Post-Incident Activity.
- **Cybersecurity Incident Response Frameworks:** Frameworks wie NIST Cybersecurity Framework oder ISO 27001 beinhalten Phasen der Analyse und Verbesserung nach einem Sicherheitsvorfall.

**Spezifische Ressourcen (allgemeine Suchbegriffe für deine Recherche):**

- **Post-Incident Review Template**
- **Post-Mortem Analysis Guide**
- **Blameless Postmortem Principles**
- **ITIL Incident Management Process**
- **SRE Postmortem Practices**

Indem du nach diesen Begriffen suchst, findest du zahlreiche Artikel, Blogbeiträge, Vorlagen und Leitfäden, die dir helfen können, die Post-Incident Activity in deiner Organisation effektiv zu implementieren und durchzuführen.



Beispiel : 


praktisches Beispiel, das die Wirkungsweise der Post-Incident Activity verdeutlicht:

**Szenario:**

Ein beliebtes Online-Versandhaus erlebt am Black Friday, seinem umsatzstärksten Tag des Jahres, einen schwerwiegenden Ausfall seiner Bestellabwicklungssysteme. Kunden können keine Artikel in den Warenkorb legen oder Bestellungen abschließen. Der Ausfall dauert insgesamt drei Stunden und führt zu erheblichen Umsatzeinbußen und verärgerten Kunden in den sozialen Medien.

**Post-Incident Activity:**

Nachdem der Ausfall behoben wurde und die Systeme wieder stabil laufen, wird eine Post-Incident Activity durchgeführt.

1. **Vorbereitung:**
    
    - Ein Team aus Vertretern der IT-Abteilung (Entwicklung, Betrieb, Datenbank), des Kundenservice und des Business-Teams wird zusammengestellt.
    - Alle relevanten Daten werden gesammelt:
        - Zeitstempel des Ausfalls und der Wiederherstellung
        - Fehlermeldungen und Logdateien der betroffenen Systeme
        - Monitoring-Daten zur Systemauslastung
        - Anzahl der Kundenbeschwerden beim Kundenservice
        - Geschätzter Umsatzverlust
2. **Durchführung der Analyse (Post-Incident Review Meeting):**
    
    - **Chronologische Darstellung:** Das Team geht den Ablauf des Vorfalls detailliert durch: Wann wurde der Ausfall bemerkt? Welche ersten Maßnahmen wurden ergriffen? Wann wurde die Ursache identifiziert und behoben?
    - **Identifizierung der Ursachen:**
        - **Erste Annahme:** Zunächst wurde vermutet, dass die hohe Last am Black Friday die Systeme überfordert hat.
        - **Tiefergehende Analyse:** Durch die Analyse der Logdateien und der Systemauslastung stellt sich heraus, dass ein kürzlich durchgeführtes Software-Update in der Bestellabwicklungssoftware einen Fehler enthielt, der unter hoher Last zu einem Speicherleck führte. Dieses Speicherleck führte schließlich zum Absturz der Systeme.
        - **Weitere Ursachen:** Es wird auch festgestellt, dass die automatischen Warnmeldungen des Monitoring-Systems für diesen spezifischen Fehler nicht ausreichend konfiguriert waren, wodurch die Reaktion verzögert wurde. Außerdem gab es keinen klaren Eskalationspfad für kritische Ausfälle während des Black Fridays.
    - **Bewertung der Reaktion:**
        - **Positiv:** Die IT-Abteilung hat schnell reagiert und das Problem letztendlich behoben.
        - **Negativ:** Die anfängliche Fehlersuche dauerte zu lange, da die falsche Ursache vermutet wurde. Die fehlenden spezifischen Warnmeldungen und der unklare Eskalationspfad haben die Reaktionszeit ebenfalls verlängert.
    - **Identifizierung von Verbesserungspotenzial:**
        - **Technische Maßnahmen:**
            - Rollback des fehlerhaften Software-Updates auf eine stabile Version als schnelle Lösung.
            - Behebung des Speicherlecks im Software-Update durch die Entwicklungsabteilung und erneute, gründlichere Tests vor der nächsten Bereitstellung.
            - Verbesserung der Testprozesse, insbesondere für Last- und Stresstests vor wichtigen Ereignissen wie dem Black Friday.
            - Konfiguration spezifischer Warnmeldungen im Monitoring-System für kritische Fehler in der Bestellabwicklung.
        - **Prozessuale Maßnahmen:**
            - Implementierung eines klar definierten und kommunizierten Eskalationspfads für kritische Ausfälle, insbesondere während kritischer Geschäftszeiten.
            - Überprüfung und Verbesserung des Deployment-Prozesses für Software-Updates, einschließlich einer besseren Koordination und Kommunikation zwischen den Teams.
            - Durchführung von "Chaos Engineering"-Übungen, um die Resilienz der Systeme unter Last zu testen und potenzielle Schwachstellen frühzeitig zu erkennen.
        - **Kommunikative Maßnahmen:**
            - Verbesserung der internen Kommunikation während eines Ausfalls, um alle relevanten Teams auf dem Laufenden zu halten.
            - Entwicklung eines Kommunikationsplans für Kunden im Falle eines größeren Ausfalls.
3. **Dokumentation und Nachverfolgung:**
    
    - Ein detaillierter Post-Incident Report wird erstellt, der die Ursachen, die Bewertung der Reaktion und die beschlossenen Maßnahmen zusammenfasst.
    - Für jede Maßnahme wird ein Verantwortlicher und eine Deadline festgelegt.
    - Der Fortschritt der Umsetzung der Maßnahmen wird regelmäßig in Team-Meetings überprüft.

**Wirkungsweise in diesem Beispiel:**

- **Identifizierung der wahren Ursache:** Anstatt sich auf die offensichtliche Vermutung der Überlastung zu verlassen, führte die detaillierte Analyse zur Identifizierung des fehlerhaften Software-Updates als eigentliche Ursache.
- **Ableitung konkreter Verbesserungsmaßnahmen:** Die Analyse führte zu einer Liste spezifischer technischer, prozessualer und kommunikativer Maßnahmen, die darauf abzielen, ähnliche Vorfälle in Zukunft zu verhindern oder deren Auswirkungen zu minimieren.
- **Verantwortlichkeiten und Zeitrahmen:** Durch die Zuweisung von Verantwortlichkeiten und Deadlines wird sichergestellt, dass die beschlossenen Maßnahmen auch tatsächlich umgesetzt werden.
- **Langfristige Verbesserung:** Die Implementierung der Verbesserungsmaßnahmen, wie z.B. verbesserte Testprozesse und ein klarer Eskalationspfad, wird die Stabilität und Resilienz der Systeme langfristig erhöhen und die Wahrscheinlichkeit zukünftiger Ausfälle reduzieren.
- **Lernen für die Zukunft:** Das Unternehmen hat aus diesem kritischen Vorfall gelernt und kann seine Prozesse und Systeme verbessern, um in Zukunft besser auf ähnliche Situationen vorbereitet zu sein.

Dieses Beispiel zeigt, wie die Post-Incident Activity über die reine Behebung eines Problems hinausgeht und einen strukturierten Ansatz bietet, um aus Fehlern zu lernen und die Organisation kontinuierlich zu verbessern.