Die Festlegung von Ausfallzeiten, insbesondere die **Festlegung von Wiederherstellungszeiten (RTO)** und **Wiederherstellungspunkten (RPO)**, ist ein kritischer Bestandteil der Planung für Geschäftskontinuität und Disaster Recovery. Diese Werte bestimmen, wie schnell und wie umfassend Ihr Unternehmen nach einer Störung den Betrieb wieder aufnehmen muss.

Hier ist eine detaillierte Anleitung, wie Sie RTO und RPO berechnen und festlegen können:

**1. Verständnis von RTO und RPO**

Es ist wichtig, zuerst die grundlegenden Definitionen von RTO und RPO zu verstehen:

- **Recovery Time Objective (RTO) / Wiederherstellungszeit:** Dies ist die **maximale akzeptable Ausfallzeit** für eine bestimmte IT-Ressource oder einen Geschäftsprozess. Mit anderen Worten, es ist die Zeitspanne, innerhalb derer der Betrieb nach einer Unterbrechung wiederhergestellt sein muss, um inakzeptable Folgen für das Unternehmen zu vermeiden. Die RTO wird in Zeiteinheiten gemessen (z.B. Stunden, Minuten).
    
    - **Beispiel:** Eine RTO von 4 Stunden für ein E-Commerce-System bedeutet, dass das System innerhalb von 4 Stunden nach einer Störung wieder voll funktionsfähig sein muss, um erhebliche Umsatzverluste zu vermeiden.
- **Recovery Point Objective (RPO) / Wiederherstellungspunkt:** Dies ist der **maximale akzeptable Datenverlust in der Zeit**, gemessen ab dem Zeitpunkt des letzten bekannten guten Daten-Backups im Falle eines IT-Ausfalls. Die RPO bestimmt, wie aktuell die Daten sein müssen, die bei der Wiederherstellung zur Verfügung stehen. Auch die RPO wird in Zeiteinheiten gemessen (z.B. Stunden, Minuten, Tage).
    
    - **Beispiel:** Eine RPO von 1 Stunde für eine Datenbank bedeutet, dass im schlimmsten Fall Daten von maximal einer Stunde verloren gehen dürfen. Sie müssen also mindestens stündliche Backups durchführen, um dieses Ziel zu erreichen.

_(Dieses Bild würde eine einfache Zeitleiste darstellen, die den Zeitpunkt eines Ausfalls, die RTO (Zeit bis zur Wiederherstellung) und die RPO (Datenverlust in der Zeit vor dem Ausfall) visuell erklärt.)_

_

[![[45cf4ca49ffed7d089489e83b6a16bab_MD5.png]]Wird in einem neuen Fenster geöffnet](https://www.techtarget.com/searchstorage/feature/What-is-the-difference-between-RPO-and-RTO-from-a-backup-perspective)[![[91b1d6e40a7dca04b977701fbd479c00_MD5.png]]www.techtarget.com](https://www.techtarget.com/searchstorage/feature/What-is-the-difference-between-RPO-and-RTO-from-a-backup-perspective)

RTO and RPO Timeline Diagram



_

**Wichtiger Unterschied:**

- **RTO konzentriert sich auf die Betriebs**wiederherstellung (wie schnell muss der Betrieb wieder laufen?).
- **RPO konzentriert sich auf die Daten**wiederherstellung (wie viele Daten dürfen maximal verloren gehen?).

**2. Schritte zur Berechnung und Festlegung von RTO und RPO**

Die Festlegung von RTO und RPO ist ein geschäftsorientierter Prozess, der ein tiefes Verständnis der Geschäftsprozesse und deren Abhängigkeiten von IT-Systemen erfordert. Hier sind die wichtigsten Schritte:

**a) Durchführung einer Business Impact Analysis (BIA) / Geschäftsauswirkungsanalyse:**

Die BIA ist der **Grundstein** für die Festlegung von RTO und RPO. Sie hilft Ihnen zu verstehen:

- **Kritische Geschäftsprozesse:** Identifizieren Sie die wichtigsten Geschäftsprozesse, die für das Überleben und den Erfolg Ihres Unternehmens unerlässlich sind. Denken Sie an Kernfunktionen wie Vertrieb, Produktion, Kundenservice, Finanzen usw.
- **Abhängigkeiten:** Analysieren Sie, welche IT-Systeme, Anwendungen, Daten, Ressourcen und Personal diese kritischen Prozesse benötigen, um zu funktionieren. Identifizieren Sie Engpässe und Single Points of Failure.
- **Auswirkungen von Ausfallzeiten:** Bewerten Sie die **quantitativen und qualitativen** Auswirkungen von Ausfallzeiten für jeden kritischen Geschäftsprozess. Dies umfasst:
    - **Finanzielle Verluste:** Umsatzeinbußen, Vertragsstrafen, erhöhte Betriebskosten, Cashflow-Probleme.
    - **Reputationsschäden:** Verlust des Kundenvertrauens, Imageschäden, negative Presse.
    - **Gesetzliche und regulatorische Konsequenzen:** Verstöße gegen Compliance-Anforderungen, Bußgelder.
    - **Betriebliche Auswirkungen:** Verzögerungen in der Produktion, Unzufriedenheit der Mitarbeiter, Verlust von Wettbewerbsvorteilen.

_(Dieses Bild würde ein Flussdiagramm darstellen, das die Schritte einer BIA visualisiert, beginnend mit der Identifizierung kritischer Prozesse, der Analyse von Abhängigkeiten, der Bewertung von Auswirkungen und der Dokumentation der Ergebnisse.)_

_

[![[176aed45313634fb1d68acbe07e6267f_MD5.png]]Wird in einem neuen Fenster geöffnet](https://help.archerirm.cloud/busres_impact_610/en-us/Content/Solutions/BusResiliency/br_bia_design.htm)[![](https://encrypted-tbn3.gstatic.com/favicon-tbn?q=tbn:ANd9GcT2jQ1ezyux2GeaxlCI-lZBI3kTgZ2hCQeXU9l2Dwi6gl1vt9wKUAoT6sBD9thhvaIt5hWrH9grLXprCdHBg5P-fjUeUiQa-jJRQbHwo4M)help.archerirm.cloud](https://help.archerirm.cloud/busres_impact_610/en-us/Content/Solutions/BusResiliency/br_bia_design.htm)

Business Impact Analysis (BIA) Process Diagram



_

**b) Priorisierung der Geschäftsprozesse und IT-Systeme:**

Basierend auf den Ergebnissen der BIA priorisieren Sie die Geschäftsprozesse und die zugehörigen IT-Systeme nach ihrer Kritikalität. Prozesse und Systeme mit den **höchsten Auswirkungen** bei einem Ausfall erhalten die **niedrigsten (kürzesten)** RTO- und RPO-Werte.

**c) Festlegung der RTO- und RPO-Werte für priorisierte Prozesse und Systeme:**

Für jeden priorisierten Geschäftsprozess und jedes zugehörige IT-System legen Sie **realistische und messbare** RTO- und RPO-Werte fest. Berücksichtigen Sie dabei:

- **Akzeptable Ausfallzeit:** Wie lange kann der Prozess maximal ausfallen, bevor inakzeptable Schäden entstehen? Dies bestimmt die RTO.
- **Akzeptabler Datenverlust:** Wie viele Daten dürfen maximal verloren gehen? Dies bestimmt die RPO.
- **Technische Machbarkeit:** Sind die gewünschten RTO- und RPO-Werte mit den verfügbaren oder geplanten Technologien und Ressourcen technisch umsetzbar und kosteneffizient?
- **Kosten:** Niedrigere RTO- und RPO-Werte erfordern in der Regel höhere Investitionen in Backup- und Wiederherstellungstechnologien, Redundanz, Hochverfügbarkeit usw. Führen Sie eine **Kosten-Nutzen-Analyse** durch, um ein angemessenes Gleichgewicht zwischen Kosten und Risikominimierung zu finden.

**d) Dokumentation und Abstimmung:**

Dokumentieren Sie die festgelegten RTO- und RPO-Werte **klar und präzise** für alle relevanten Geschäftsprozesse und IT-Systeme. Stimmen Sie diese Werte mit den **relevanten Stakeholdern** ab, einschließlich der Geschäftsleitung, der Fachabteilungen und der IT-Abteilung. Stellen Sie sicher, dass alle Beteiligten die Werte verstehen und akzeptieren.

**e) Regelmäßige Überprüfung und Aktualisierung:**

RTO- und RPO-Werte sind **nicht statisch**. Geschäftsprozesse, IT-Systeme, Risiken und technologische Möglichkeiten verändern sich im Laufe der Zeit. **Überprüfen und aktualisieren Sie die RTO- und RPO-Werte regelmäßig** (mindestens jährlich oder bei wesentlichen Änderungen im Unternehmen), um sicherzustellen, dass sie weiterhin relevant und angemessen sind. Wiederholen Sie die BIA in regelmäßigen Abständen.

**3. Faktoren, die RTO und RPO beeinflussen**

Verschiedene Faktoren beeinflussen die Festlegung von RTO und RPO:

- **Branche und Geschäftsart:** Branchen mit hohen regulatorischen Anforderungen (z.B. Finanzdienstleistungen, Gesundheitswesen) oder kritischen Infrastrukturen benötigen oft niedrigere RTO- und RPO-Werte.
- **Größe des Unternehmens:** Größere Unternehmen mit komplexeren IT-Infrastrukturen und globalen Operationen haben möglicherweise unterschiedliche RTO- und RPO-Anforderungen für verschiedene Geschäftsbereiche.
- **Kritikalität der Daten:** Systeme, die hochsensible oder geschäftskritische Daten verarbeiten (z.B. Kundendaten, Finanzdaten, geistiges Eigentum), erfordern in der Regel niedrigere RPO-Werte.
- **Budget:** Die verfügbaren finanziellen Ressourcen für Disaster Recovery-Lösungen und Infrastruktur beeinflussen die realisierbaren RTO- und RPO-Werte.
- **Technologische Möglichkeiten:** Fortschritte in den Bereichen Backup, Replikation, Cloud-Computing und Hochverfügbarkeit können helfen, niedrigere RTO- und RPO-Werte kosteneffizienter zu erreichen.
- **Risikobereitschaft des Unternehmens:** Die allgemeine Risikobereitschaft des Unternehmens und die Akzeptanz potenzieller Ausfallschäden spielen eine Rolle bei der Festlegung der RTO- und RPO-Ziele.

**4. Beispiele für RTO- und RPO-Werte (Richtwerte):**

Die folgenden Werte sind **nur Richtwerte** und müssen an die spezifischen Bedürfnisse und Anforderungen Ihres Unternehmens angepasst werden:

|Geschäftsprozess / System|RTO (Richtwert)|RPO (Richtwert)|Begründung|
|:--|:-:|:-:|:--|
|E-Commerce-Website|1-4 Stunden|1-2 Stunden|Hohe Umsatzauswirkungen bei Ausfall, Kundenverlust, Wettbewerbsdruck.|
|Kernbankensystem|< 1 Stunde|< 30 Minuten|Kritische Finanztransaktionen, regulatorische Anforderungen, hohe Sensibilität.|
|Produktionssteuerungssystem|2-8 Stunden|1-4 Stunden|Produktionsausfälle, Lieferkettenunterbrechungen, Effizienzverluste.|
|E-Mail-System|4-12 Stunden|2-4 Stunden|Kommunikationsausfälle, operative Einschränkungen, wichtig für interne/externe Kommunikation.|
|Datei-Server (Allgemeine Daten)|8-24 Stunden|4-8 Stunden|Abhängig von der Art der gespeicherten Daten und deren Kritikalität.|
|Entwicklungsumgebung|24-48 Stunden|12-24 Stunden|Geringere unmittelbare Auswirkung auf den laufenden Betrieb, aber wichtig für Innovation.|

In Google Sheets exportieren

**5. Tools und Techniken für die Festlegung von RTO und RPO:**

- **Vorlagen für Business Impact Analysis (BIA):** Verwenden Sie vorgefertigte Vorlagen, um die Datenerfassung und -analyse im Rahmen der BIA zu strukturieren.
- **Risk-Assessment-Frameworks:** Nutzen Sie etablierte Rahmenwerke zur Risikobewertung, um potenzielle Bedrohungen und Schwachstellen zu identifizieren.
- **Kosten-Nutzen-Analyse-Tools:** Verwenden Sie Tabellenkalkulationsprogramme oder spezielle Software, um die Kosten verschiedener Disaster Recovery-Strategien und die damit verbundenen Nutzen zu vergleichen.
- **Workshops und Interviews:** Führen Sie Workshops mit Fachexperten und Interviews mit Verantwortlichen der Geschäftsprozesse durch, um detaillierte Informationen zu sammeln und Konsens zu erzielen.
- **Disaster Recovery Planung Software:** Es gibt Softwarelösungen, die den gesamten Disaster Recovery Planungsprozess unterstützen können, einschließlich der BIA, der Festlegung von RTO und RPO und der Erstellung von Wiederherstellungsplänen.

**Zusammenfassend lässt sich sagen, dass die Berechnung und Festlegung von RTO und RPO ein wichtiger Schritt in der Entwicklung einer robusten Disaster Recovery Strategie ist. Es erfordert ein tiefes Verständnis Ihrer Geschäftsprozesse, deren Abhängigkeiten und die potenziellen Auswirkungen von Ausfallzeiten. Durch eine systematische Vorgehensweise und die Einbeziehung der relevanten Stakeholder können Sie realistische und effektive RTO- und RPO-Werte definieren, die Ihr Unternehmen im Falle einer Störung optimal schützen.**
















**Festlegung der Maximalen Ausfallzeit (RTO - Recovery Time Objective)**

Die **Recovery Time Objective (RTO)**, also die **maximale Ausfallzeit**, definiert den **Zeitraum**, innerhalb dessen ein Geschäftsprozess, eine Ressource oder ein System nach einer Unterbrechung **wiederhergestellt sein muss**, um unakzeptable Folgen für das Unternehmen zu vermeiden. Die Festlegung des RTO ist ein **entscheidender Schritt** in der BIA und erfordert eine sorgfältige Analyse der Auswirkungen von Ausfallzeiten.

**Berechnung und Festlegung des RTO - Schritt für Schritt:**

1. **Analyse der Auswirkungen von Ausfallzeiten (Impact Analyse):**
    
    - **Basis ist Ihre Impact Analyse Tabelle:** Die Tabelle, die Sie in Ihrer BIA erstellt haben (siehe oben), ist der **Ausgangspunkt**. Sie haben dort für jeden kritischen Geschäftsprozess die potenziellen Auswirkungen eines Ausfalls in verschiedenen Schadenskategorien (Finanziell, Reputationsschaden, Operativ, Rechtlich, Sicherheit) bewertet.
    - **Detaillierung der Auswirkungen nach Zeit:** Gehen Sie nun einen Schritt weiter und **betrachten Sie die Auswirkungen _zeitlich gestaffelt_**. Fragen Sie sich für jeden kritischen Prozess:
        - **Was sind die Auswirkungen, wenn der Prozess 1 Stunde ausfällt?**
        - **Was sind die Auswirkungen, wenn der Prozess 4 Stunden ausfällt?**
        - **Was sind die Auswirkungen, wenn der Prozess 8 Stunden ausfällt?**
        - **Was sind die Auswirkungen, wenn der Prozess 24 Stunden ausfällt?**
        - **... und so weiter.**
    - **Schadenshöhe quantifizieren (sofern möglich):** Versuchen Sie, die **Schäden in den verschiedenen Kategorien _möglichst konkret zu quantifizieren_**. Dies kann in finanziellen Werten (Umsatzverlust pro Stunde, potenzielle Bussgelder), messbaren operativen Einschränkungen (Anzahl der nicht bearbeiteten Kundenanfragen pro Stunde) oder qualitativen Bewertungen (Reputationsschaden: "gering", "mittel", "hoch", "katastrophal") erfolgen.
2. **Bestimmung der Toleranzgrenze:**
    
    - **Schadensakzeptanz des Unternehmens:** Bewerten Sie, **welchen maximalen Schaden** das Unternehmen in den verschiedenen Kategorien **tolerieren kann**, ohne dass es zu existenziellen Bedrohungen, unzumutbaren Beeinträchtigungen des Geschäftsbetriebs oder inakzeptablen Reputationsverlusten kommt.
    - **Identifizierung des "Kipppunkts":** Suchen Sie nach dem **Zeitpunkt**, ab dem die Auswirkungen eines Ausfalls **untragbar** werden. Dies ist der Punkt, an dem der Schaden **exponentiell ansteigt** oder ein **kritischer Schwellenwert** überschritten wird. Dieser Zeitpunkt ist ein wichtiger Indikator für das RTO.
3. **Berücksichtigung von externen Faktoren:**
    
    - **Service Level Agreements (SLAs) mit Kunden:** Haben Sie **vertragliche Zusicherungen** gegenüber Ihren Kunden bezüglich der Verfügbarkeit des Passwortmanagers (SLAs)? Diese SLAs setzen **harte Grenzen** für die maximal tolerierbare Ausfallzeit. Die RTOs für kritische Prozesse müssen **innerhalb der SLA-Vorgaben** liegen.
    - **Gesetzliche und regulatorische Vorgaben:** Gibt es **gesetzliche oder regulatorische Anforderungen** (z.B. Datenschutzgesetze, Branchenstandards), die bestimmte maximale Ausfallzeiten vorschreiben? Auch diese Vorgaben müssen bei der Festlegung des RTO berücksichtigt werden.
    - **Wettbewerbssituation:** In einem **wettbewerbsintensiven Markt** kann bereits eine kurze Ausfallzeit zu einem **Verlust von Kunden an die Konkurrenz** führen. Dies sollte in die RTO-Festlegung einfließen.
4. **Bewertung der technischen Machbarkeit und Kosten:**
    
    - **Technische Möglichkeiten der Wiederherstellung:** Analysieren Sie, **welche technischen Maßnahmen** (z.B. Redundanz, Backup-Systeme, Notfallpläne) zur Verfügung stehen, um den jeweiligen Geschäftsprozess innerhalb eines bestimmten Zeitrahmens wiederherzustellen.
    - **Kosten der Wiederherstellung:** Bewerten Sie die **Kosten**, die mit der Implementierung und dem Betrieb dieser Wiederherstellungsmaßnahmen verbunden sind. **Kürzere RTOs erfordern in der Regel höhere Investitionen** in Infrastruktur, Personal und Prozesse.
    - **Abwägung von Kosten und Nutzen:** Es ist ein **Kompromiss** zwischen dem **gewünschten RTO (kurze Ausfallzeit)** und den **Kosten für die Erreichung dieses RTOs**. Sie müssen die **Kosten der Wiederherstellung** gegen den **potenziellen Schaden durch einen Ausfall** abwägen. Ein sehr kurzes RTO für einen weniger kritischen Prozess ist möglicherweise nicht wirtschaftlich.
5. **Festlegung des RTO und Dokumentation der Begründung:**
    
    - **Realistisches und ambitioniertes RTO festlegen:** Basierend auf der Analyse der Auswirkungen, der Toleranzgrenze, externen Faktoren und der technischen Machbarkeit legen Sie ein **realistisches, aber dennoch ambitioniertes RTO** für jeden kritischen Geschäftsprozess fest. Das RTO sollte so kurz wie möglich sein, aber auch **wirtschaftlich und technisch umsetzbar**.
    - **Begründung dokumentieren:** **Dokumentieren Sie _detailliert_**, **warum Sie das jeweilige RTO festgelegt haben**. Beziehen Sie sich auf die analysierten Auswirkungen, die Toleranzgrenze, SLAs, regulatorische Vorgaben, technische Machbarkeit und die Kosten-Nutzen-Abwägung. Diese Begründung ist wichtig für die Nachvollziehbarkeit und spätere Überprüfung des RTO.

**Beispiel für die RTO-Festlegung am Prozess "Bereitstellung Passwortmanager":**

- **Auswirkungenanalyse (zeitlich gestaffelt):**
    - **1 Stunde Ausfall:** Geringe finanzielle Verluste, geringer Reputationsschaden, Benutzer leicht eingeschränkt.
    - **4 Stunden Ausfall:** Moderate finanzielle Verluste, moderater Reputationsschaden, Benutzer stärker eingeschränkt, Beginnende Unzufriedenheit.
    - **8 Stunden Ausfall:** Deutliche finanzielle Verluste, deutlicher Reputationsschaden, erhebliche operative Einschränkungen, Kunden beginnen sich nach Alternativen umzusehen.
    - **24 Stunden Ausfall:** Erhebliche finanzielle Verluste, erheblicher Reputationsschaden, massiver operativer Schaden, hoher Kundenverlust wahrscheinlich.
- **Toleranzgrenze:** Das Unternehmen kann maximal 4 Stunden Ausfallzeit ohne unzumutbare Schäden tolerieren. Ab 8 Stunden wird es kritisch.
- **Externe Faktoren:** SLAs mit Kunden garantieren 99,9% Verfügbarkeit, was rechnerisch ca. 4,3 Stunden Ausfallzeit pro Monat erlaubt, aber längere _zusammenhängende_ Ausfälle müssen vermieden werden. Der Wettbewerb ist stark, längere Ausfälle schaden dem Image massiv.
- **Technische Machbarkeit und Kosten:** Eine vollständige Redundanz der Produktionsinfrastruktur ist teuer, aber technisch realisierbar. Eine weniger aufwendige Lösung mit einer RTO von < 4 Stunden ist wirtschaftlich vertretbar.
- **Festlegung RTO:** **< 4 Stunden (Ideal < 1 Stunde)** wird als realistisches und ambitioniertes RTO für die "Bereitstellung Passwortmanager" festgelegt. Eine Begründung wird detailliert dokumentiert.

**Festlegung des Maximalen Datenverlusts (RPO - Recovery Point Objective)**

Die **Recovery Point Objective (RPO)** definiert den **maximal tolerierbaren Datenverlust** in der Zeit, gemessen ab dem Zeitpunkt eines Ausfalls. Es bestimmt, **wie weit in die Vergangenheit** die Daten maximal zurückreichen dürfen, wenn ein System wiederhergestellt wird. Ein kurzes RPO bedeutet, dass im Falle eines Ausfalls nur sehr wenige Daten verloren gehen dürfen.

**Berechnung und Festlegung des RPO - Schritt für Schritt:**

1. **Analyse der Datensensitivität und -volatilität:**
    
    - **Datenkritikalität:** Bewerten Sie, **wie kritisch die Daten** sind, die von dem jeweiligen Geschäftsprozess verarbeitet werden. Handelt es sich um hochsensible Benutzerdaten (wie Passwörter im Passwortmanager), kritische Transaktionsdaten oder weniger sensible Informationen? **Je kritischer die Daten, desto kürzer sollte das RPO sein.**
    - **Datenvolatilität (Änderungsfrequenz):** Analysieren Sie, **wie häufig sich die Daten ändern**. Werden die Daten in diesem Prozess sehr häufig aktualisiert (z.B. sekündlich, minütlich, stündlich) oder eher selten (täglich, wöchentlich)? **Je höher die Datenvolatilität, desto kürzer sollte das RPO sein, um Datenverlust zu minimieren.**
2. **Bewertung der Auswirkungen von Datenverlust:**
    
    - **Geschäftliche Konsequenzen des Datenverlusts:** Bewerten Sie die **Auswirkungen eines Datenverlusts** für den jeweiligen Geschäftsprozess. Welche **geschäftlichen Konsequenzen** hätte es, wenn Daten der letzten Stunde, der letzten 24 Stunden oder des letzten Tages verloren gingen? Berücksichtigen Sie:
        - **Datenintegrität und -konsistenz:** Würde ein Datenverlust die **Integrität und Konsistenz der Daten** beeinträchtigen und zu Fehlfunktionen oder falschen Entscheidungen führen?
        - **Finanzielle Auswirkungen:** Entstehen **direkte finanzielle Verluste** durch Datenverlust (z.B. verlorene Transaktionen, nicht fakturierbare Leistungen)?
        - **Reputationsschaden:** Führt Datenverlust zu **Vertrauensverlust bei Kunden** oder negativer Presse? (Besonders kritisch bei Passwortmanagern!)
        - **Rechtliche und regulatorische Konsequenzen:** Verletzt ein Datenverlust **Datenschutzgesetze** oder andere Vorschriften? (DSGVO bei Benutzerdaten!)
3. **Berücksichtigung von Wiederherstellungsanforderungen:**
    
    - **Anforderungen an die Datenkonsistenz:** In manchen Fällen ist es extrem wichtig, dass die **Daten nach einer Wiederherstellung _vollständig konsistent_** sind, d.h. keine Transaktionen verloren gehen oder inkonsistente Zustände entstehen. In solchen Fällen ist ein **RPO von 0 (oder nahezu 0)** erforderlich.
    - **Anforderungen an die Datenvollständigkeit:** Auch die **Vollständigkeit der Daten** kann entscheidend sein. Je wichtiger es ist, dass _alle_ Datenpunkte wiederhergestellt werden (z.B. bei Audit-Trails, Compliance-Daten), desto kürzer sollte das RPO sein.
4. **Bewertung der technischen Machbarkeit und Kosten:**
    
    - **Technische Möglichkeiten der Datensicherung:** Analysieren Sie, **welche technischen Methoden** (z.B. regelmäßige Backups, kontinuierliche Datensicherung, Datenbankreplikation) zur Verfügung stehen, um ein bestimmtes RPO zu erreichen.
    - **Kosten der Datensicherung:** Bewerten Sie die **Kosten** für die Implementierung und den Betrieb dieser Datensicherungsmethoden. **Kürzere RPOs erfordern in der Regel aufwendigere und teurere Datensicherungslösungen** (z.B. häufigere Backups, Continuous Data Protection).
    - **Abwägung von Kosten und Nutzen:** Auch beim RPO müssen Sie die **Kosten der Datensicherung** gegen den **potenziellen Schaden durch Datenverlust** abwägen. Ein extrem kurzes RPO (z.B. 0) ist sehr teuer und möglicherweise nur für absolut kritische Daten gerechtfertigt.
5. **Festlegung des RPO und Dokumentation der Begründung:**
    
    - **Realistisches und angemessenes RPO festlegen:** Basierend auf der Analyse der Datensensitivität, der Auswirkungen von Datenverlust, Wiederherstellungsanforderungen und der technischen Machbarkeit legen Sie ein **realistisches und angemessenes RPO** für jeden kritischen Geschäftsprozess fest. Das RPO sollte so kurz wie nötig sein, aber auch **wirtschaftlich und technisch umsetzbar**.
    - **Begründung dokumentieren:** **Dokumentieren Sie _detailliert_**, **warum Sie das jeweilige RPO festgelegt haben**. Beziehen Sie sich auf die analysierte Datensensitivität, die Auswirkungen des Datenverlusts, Wiederherstellungsanforderungen, technische Machbarkeit und die Kosten-Nutzen-Abwägung. Diese Begründung ist essenziell für die Nachvollziehbarkeit und spätere Überprüfung des RPO.

**Beispiel für die RPO-Festlegung am Prozess "Verschlüsselung/Speicherung Passwörter":**

- **Analyse der Datensensitivität und -volatilität:**
    - **Datenkritikalität:** **Extrem hoch**. Passwörter sind die sensibelsten Daten. Kompromittierung hätte katastrophale Folgen.
    - **Datenvolatilität:** Relativ gering, Passwörter ändern sich nicht ständig, aber es gibt regelmäßige Aktualisierungen durch Benutzer.
- **Auswirkungen von Datenverlust:**
    - **Datenintegrität und -konsistenz:** Verlust der Passwortdatenbank wäre verheerend. Integrität und Konsistenz der verbleibenden Daten wären fragwürdig.
    - **Finanzielle Auswirkungen:** Enorme finanzielle Schäden durch Bussgelder, Schadenersatz, Imageverlust.
    - **Reputationsschaden:** **Katastrophal**. Vollständiger Vertrauensverlust.
    - **Rechtliche und regulatorische Konsequenzen:** Schwerwiegendste Verstöße gegen Datenschutzgesetze (DSGVO).
- **Wiederherstellungsanforderungen:** **Absolute Datenkonsistenz und -vollständigkeit _unerlässlich_**. Kein Datenverlust akzeptabel.
- **Technische Machbarkeit und Kosten:** Kontinuierliche Datenbankreplikation und sehr häufige Backups sind technisch machbar und angesichts der Risiken und potenziellen Schäden **absolut notwendig und wirtschaftlich gerechtfertigt**.
- **Festlegung RPO:** **< 1 Stunde (Ideal 0)** wird als RPO für den Prozess "Verschlüsselung/Speicherung Passwörter" festgelegt. **Ideal RPO = 0** wird angestrebt, was durch geeignete technische Maßnahmen (z.B. synchrone Datenbankreplikation) erreicht werden soll. Die Begründung wird umfassend dokumentiert.

**Zusammenfassend lässt sich sagen, dass die Festlegung von RTO und RPO ein iterativer Prozess ist, der eine detaillierte Analyse der Geschäftsprozesse, ihrer Auswirkungen, der Daten, der externen Faktoren und der technischen Möglichkeiten erfordert. Es ist ein Zusammenspiel aus _Business Impact Analyse_, _Risikobewertung_, _Kosten-Nutzen-Abwägung_ und _technischer Expertise_. Die festgelegten RTOs und RPOs sind entscheidend für die Entwicklung effektiver Wiederherstellungsstrategien und Notfallpläne.**