
### 1. Kerndefinition

Die **CIA-Triade** ist ein fundamentales und weithin anerkanntes Modell der Informationssicherheit, das die drei wichtigsten Schutzziele für Daten und Systeme definiert: **Vertraulichkeit (Confidentiality)**, **Integrität (Integrity)** und **Verfügbarkeit (Availability)**. Dieses Modell dient als Leitfaden für die Entwicklung von Sicherheitsrichtlinien, die Bewertung von Risiken und die Implementierung von Schutzmaßnahmen. Das Hauptziel ist es, ein Gleichgewicht zwischen diesen drei Aspekten zu finden, um Informationen umfassend zu schützen.

### 2. Detaillierte Erläuterung / Funktionsweise

**Die drei Säulen der Triade:**

**1. Vertraulichkeit (Confidentiality):**

- **Ziel:** Sicherstellen, dass Informationen nur von autorisierten Personen oder Systemen eingesehen oder offengelegt werden. Es geht darum, Daten vor unbefugtem Zugriff zu schützen und Geheimnisse zu wahren.
    
- **Verletzung:** Spionage, Datendiebstahl, unachtsamer Umgang mit sensiblen Daten (z. B. Liegenlassen von Dokumenten), Man-in-the-Middle-Angriffe.
    
- **Typische Schutzmaßnahmen:**
    
    - **Verschlüsselung:** Umwandlung von Daten in eine unlesbare Form (sowohl bei der Speicherung, _Data at Rest_, als auch bei der Übertragung, _Data in Transit_).
        
    - **Zugriffskontrolle:** Authentifizierung (Wer bist du?) und Autorisierung (Was darfst du?) durch Passwörter, Multi-Faktor-Authentifizierung (MFA) und Berechtigungskonzepte (z. B. Role-Based Access Control).
        
    - **Physische Sicherheit:** Absicherung von Serverräumen und Geräten.
        

**2. Integrität (Integrity):**

- **Ziel:** Gewährleisten, dass Daten korrekt, vollständig und vertrauenswürdig sind. Es muss sichergestellt werden, dass Informationen während der Speicherung oder Übertragung nicht unbemerkt und unautorisiert verändert, hinzugefügt oder gelöscht werden.
    
- **Verletzung:** Manipulation von Banktransaktionen, Verfälschung von Protokolldateien, Einschleusung von Malware in Software-Updates.
    
- **Typische Schutzmaßnahmen:**
    
    - **Hashing:** Erstellung eines eindeutigen "Fingerabdrucks" (Hash-Wert) von Daten. Jede noch so kleine Änderung an den Daten führt zu einem völlig anderen Hash-Wert und macht die Manipulation sofort erkennbar.
        
    - **Digitale Signaturen:** Kombination aus Hashing und asymmetrischer Kryptografie, um sowohl die Integrität als auch die Authentizität des Absenders sicherzustellen.
        
    - **Versionierung und Change Control:** Protokollierung von Änderungen an Daten oder Konfigurationen.
        

**3. Verfügbarkeit (Availability):**

- **Ziel:** Sicherstellen, dass Systeme, Netzwerke und Daten für autorisierte Benutzer jederzeit zugänglich und nutzbar sind, wenn sie benötigt werden. Es geht um die Aufrechterhaltung des Betriebs und die Vermeidung von Ausfällen.
    
- **Verletzung:** Denial-of-Service (DoS)-Angriffe, Ransomware-Verschlüsselung, Hardware-Ausfälle, Stromausfälle, Naturkatastrophen.
    
- **Typische Schutzmaßnahmen:**
    
    - **Redundanz:** Einsatz von redundanten Komponenten (Festplatten in einem RAID-Verbund, mehrere Netzteile, geclusterte Server).
        
    - **Backups und Disaster Recovery:** Regelmäßige Datensicherungen und ein Notfallplan zur Wiederherstellung von Systemen nach einem Totalausfall.
        
    - **DoS-Schutzmechanismen:** Systeme zur Erkennung und Abwehr von Überlastungsangriffen.
        
    - **Lastverteilung (Load Balancing):** Verteilung des Datenverkehrs auf mehrere Server, um die Last zu verteilen und den Ausfall eines einzelnen Servers zu kompensieren.
        

### 3. Einordnung in den Gesamtkontext

Die CIA-Triade ist das **Grundgerüst der Informationssicherheit**. Nahezu jedes Sicherheitskonzept, jede Technologie und jede Richtlinie lässt sich einem oder mehreren dieser drei Ziele zuordnen.

- **Beziehung zu anderen Modellen:** Während die CIA-Triade die Kernziele definiert, wird sie oft durch weitere Konzepte ergänzt, um ein umfassenderes Bild zu zeichnen. Dazu gehören:
    
    - **Authentizität (Authenticity):** Die zweifelsfreie Feststellung der Identität eines Benutzers oder Systems.
        
    - **Nichtabstreitbarkeit (Non-Repudiation):** Die Sicherstellung, dass eine Partei eine durchgeführte Aktion (z. B. das Senden einer Nachricht) später nicht leugnen kann.
        
    - **Zurechenbarkeit (Accountability):** Die Möglichkeit, Aktionen eindeutig einem Benutzer zuzuordnen (oft durch Logging).
        
- **Spannungsfeld:** Die drei Ziele stehen oft in einem Spannungsverhältnis zueinander. Eine Erhöhung der Sicherheit in einem Bereich kann ein anderes Ziel beeinträchtigen. Beispiel: Extrem komplexe Passwortrichtlinien (gut für die Vertraulichkeit) können dazu führen, dass Benutzer ihre Passwörter aufschreiben, was die Vertraulichkeit wieder schwächt. Sehr strenge Firewall-Regeln (gut für Vertraulichkeit/Integrität) können legitime Anfragen blockieren und so die Verfügbarkeit einschränken.
    

### 4. Sicherheitsaspekte

Die CIA-Triade _ist_ das Framework zur Analyse von Sicherheitsaspekten. Jeder Angriff auf ein IT-System lässt sich als Angriff auf mindestens eines der drei Schutzziele klassifizieren.

- **Phishing-Angriff:** Primär ein Angriff auf die **Vertraulichkeit** (Erlangung von Anmeldedaten). Sekundär oft auch auf die **Integrität** (wenn der Angreifer sich dann anmeldet und Daten manipuliert).
    
- **Ransomware-Angriff:** Primär ein Angriff auf die **Verfügbarkeit** (Daten sind nicht mehr zugänglich) und die **Integrität** (Daten sind verschlüsselt/verändert). Oft auch auf die **Vertraulichkeit**, wenn mit der Veröffentlichung der Daten gedroht wird.
    
- **DDoS-Angriff (Distributed Denial of Service):** Ein reiner Angriff auf die **Verfügbarkeit**.
    

Die Analyse von Sicherheitsvorfällen anhand der CIA-Triade hilft Organisationen, die Art und den Umfang eines Angriffs zu verstehen und gezielte Gegenmaßnahmen zu ergreifen.

### 5. Praxisbeispiel / Analogie

**Praxisbeispiel:** Eine Online-Banking-Anwendung muss alle drei Schutzziele der CIA-Triade erfüllen.

- **Vertraulichkeit:** Ihr Kontostand und Ihre Transaktionsdaten müssen geheim bleiben. Dies wird durch eine verschlüsselte Verbindung (HTTPS) und eine sichere Anmeldung (Passwort + MFA) gewährleistet. Nur Sie können Ihre Daten einsehen.
    
- **Integrität:** Wenn Sie 100 € überweisen, muss sichergestellt sein, dass auch genau 100 € beim Empfänger ankommen und nicht 10 € oder 1.000 €. Dies wird durch Transaktionsprotokolle, Prüfsummen und sichere Datenbankoperationen sichergestellt.
    
- **Verfügbarkeit:** Sie müssen sich jederzeit bei Ihrem Konto anmelden und Transaktionen durchführen können. Die Bank stellt dies durch redundante Server, Notstromversorgungen und Schutz vor DDoS-Angriffen sicher.
    

**Analogie:** Die CIA-Triade lässt sich mit dem **Schutz eines handschriftlichen, versiegelten Briefes** vergleichen.

- **Vertraulichkeit:** Das **Wachssiegel** auf dem Brief stellt sicher, dass nur der vorgesehene Empfänger den Inhalt lesen kann. Wird das Siegel gebrochen, ist die Vertraulichkeit verletzt.
    
- **Integrität:** Das **unversehrte Siegel** und der **unveränderte Inhalt** des Briefes garantieren die Integrität. Ein Riss im Umschlag oder eine durchgestrichene Zeile würde die Integrität verletzen.
    
- **Verfügbarkeit:** Der Brief muss vom **Postdienst zuverlässig zugestellt** werden, damit der Empfänger ihn erhält. Geht der Brief verloren oder wird er absichtlich zurückgehalten, ist die Verfügbarkeit nicht gegeben.
    

### 6. Fazit / Bedeutung für IT-Profis

Die CIA-Triade ist für jeden IT-Profi, insbesondere im Bereich der Cybersicherheit, ein unverzichtbares gedankliches Werkzeug. Sie bietet eine einfache, aber kraftvolle Struktur, um über Sicherheitsrisiken nachzudenken, Schutzmaßnahmen zu planen und die Auswirkungen von Sicherheitsvorfällen zu bewerten. In jeder Diskussion über Sicherheit, bei jedem Systemdesign und bei jeder Risikobewertung sollten die Fragen "Wie schützen wir die Vertraulichkeit?", "Wie gewährleisten wir die Integrität?" und "Wie sichern wir die Verfügbarkeit?" im Mittelpunkt stehen.