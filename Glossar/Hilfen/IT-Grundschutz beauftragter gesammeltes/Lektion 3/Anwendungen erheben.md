
## IT-Grundschutz: Anwendungen erheben

Die Erhebung von Anwendungen ist ein wichtiger Bestandteil der Strukturanalyse im IT-Grundschutz. Sie dient dazu, die IT-Lösungen zu identifizieren, die für die Unterstützung der Geschäftsprozesse und Fachaufgaben der Institution eingesetzt werden.

### Welche Anwendungen sind relevant?

Bei der Erhebung von Anwendungen sind alle IT-Lösungen zu berücksichtigen, die einen **Bedarf an Schutz** haben. Dies sind in der Regel Anwendungen, die **wesentliche Informationen** verarbeiten oder für **kritische Geschäftsprozesse** eingesetzt werden.

### Wie werden Anwendungen erhoben?

Für die Erhebung von Anwendungen bieten sich folgende Methoden an:

- **Gespräche und Workshops**: Gespräche mit Benutzern, Anwendungs- und Geschäftsprozessverantwortlichen sowie Mitarbeitern der IT-Abteilung können wertvolle Informationen liefern.
- **Vorhandene Dokumentationen**: Es können bereits Inventare, Anwendungskataloge oder ähnliche Dokumentationen vorhanden sein.

### Welche Angaben sind zu erfassen?

Für jede als wesentlich identifizierte Anwendung sollten folgende Angaben in einer Tabelle erfasst werden:

- **Kennung**: Eine eindeutige Nummer oder ein Kürzel für die Anwendung.
- **Name**: Der Name der Anwendung.
- **Beschreibung**: Eine kurze Beschreibung des Ziels, der Funktion und der verarbeiteten Informationen.
- **Verantwortliche**: Die für die Anwendung Verantwortlichen.
- **Benutzer**: Die Benutzer der Anwendung.

**Beispiel:**

|Kennung|Name|Beschreibung|Verantwortliche|Benutzer|
|---|---|---|---|---|
|A001|Textverarbeitung|Office-Produkt zur Verarbeitung von Geschäftsinformationen.|IT-Betrieb|Alle Mitarbeiter|
|A002|Lotus Notes|Anwendung für E-Mail, Termine und Kontakte.|IT-Betrieb|Alle Mitarbeiter|
|A009|Auftrags- und Kundenverwaltung|Datenbankgestützte Anwendung zur Verarbeitung von Kunden- und Auftragsdaten.|Marketing & Vertrieb|Marketing & Vertrieb|

In Google Sheets exportieren

### Abhängigkeiten zwischen Anwendungen und Geschäftsprozessen

Zusätzlich zu den oben genannten Angaben müssen Sie die **Abhängigkeiten** zwischen Anwendungen und Geschäftsprozessen oder Fachaufgaben dokumentieren. Das heißt, Sie müssen festhalten, in welchen Prozessen und Fachaufgaben eine gegebene Anwendung benutzt wird.

**Beispiel:**

|Anwendung|Geschäftsprozess|
|---|---|
|A001|Produktion, Angebotswesen, Auftragsabwicklung, Einkauf, Disposition|
|A002|Alle Geschäftsprozesse|
|A009|Angebotswesen, Auftragsabwicklung|

In Google Sheets exportieren

### Granularität der Erfassung

Achten Sie bei der Erfassung der Anwendungen auf eine **angemessene Granularität**. Das heißt, Sie sollten die Anwendungen nicht zu fein (z.B. einzelne Bestandteile eines Office-Produkts) aber auch nicht zu grob (z.B. alle Anwendungen eines Herstellers) betrachten.

### Beispiel: RECPLAST GmbH

Die RECPLAST GmbH hat im Rahmen der Strukturanalyse folgende Anwendungen erfasst:

|Kennung|Name|Beschreibung|Verantwortliche|Benutzer|
|---|---|---|---|---|
|A001|Textverarbeitung|Office-Produkt zur Verarbeitung von Geschäftsinformationen.|IT-Betrieb|Alle Mitarbeiter|
|A002|Lotus Notes|Anwendung für E-Mail, Termine und Kontakte.|IT-Betrieb|Alle Mitarbeiter|
|A009|Auftrags- und Kundenverwaltung|Datenbankgestützte Anwendung zur Verarbeitung von Kunden- und Auftragsdaten.|Marketing & Vertrieb|Marketing & Vertrieb|
|A010|Active Directory|Verzeichnisdienst zur Verwaltung von Benutzerinformationen.|IT-Betrieb|Administratoren|
|A013|Druckservice BG|Druckservice für den Standort Bad Godesberg.|IT-Betrieb|Mitarbeiter in Bad Godesberg|
|A014|Druckservice Beuel|Druckservice für den Standort Beuel.|IT-Betrieb|Mitarbeiter in Beuel|
|A015|Firewall|Firewall zur Absicherung des Firmennetzwerks.|IT-Betrieb|Alle Mitarbeiter|
|A016|TK-Vermittlung|Telefonanlage zur Vermittlung von Telefongesprächen und Faxnachrichten.|IT-Betrieb|Alle Mitarbeiter|

In Google Sheets exportieren

Die Zuordnung der Anwendungen zu den Geschäftsprozessen ist in der folgenden Tabelle dargestellt:

|Anwendung|Produktion|Angebotswesen|Auftragsabwicklung|Einkauf|Disposition|
|---|---|---|---|---|---|
|A001|X|X|X|X|X|
|A002|X|X|X|X|X|
|A009||X|X|||
|A010|X|X|X|X|X|
|A013|X|X|X|X|X|
|A014|X|X|X|X|X|
|A015|X|X|X|X|X|
|A016|X|X|X|X|X|

In Google Sheets exportieren

### Fazit

Die Erhebung von Anwendungen ist ein wichtiger Schritt bei der Erstellung eines Sicherheitskonzepts nach IT-Grundschutz. Sie ermöglicht es, die IT-Lösungen zu identifizieren, die für die Unterstützung der Geschäftsprozesse und Fachaufgaben der Institution eingesetzt werden und einen Schutzbedarf haben.