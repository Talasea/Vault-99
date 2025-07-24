
Sicherheitskonzepte basieren auf der Analyse möglicher Angriffs- und Schadenszenarien. Anschließend wird das Schutzniveau definiert. Ein allgemein gültiges Sicherheitskonzept gibt es demnach nicht. Fast alle Sicherheitskonzepte in der Informations- und Netzwerktechnik verfolgen unterschiedliche, teilweise sogar gegenläufige Ziele.  
Die verschiedenen Sicherheitskonzepte unterscheiden sich meist nur in ihrer Zusammensetzung der eingesetzten Techniken, Verfahren und Mechanismen. Die Anwendung eines bestimmten Sicherheitskonzepts geht dabei beispielhaft auf eines der folgenden Schutzziele zurück.

- Daten gegen Verlust sichern (Datensicherheit)
- Daten gegen Diebstahl sichern (Datenschutz)
- Daten gegen Manipulation sichern (Datenintegrität)
- unbefugten Informationsgewinn (Verlust der Vertraulichkeit)
- unbefugte Modifikation von Information (Verlust der Integrität)
- unbefugte Beeinträchtigung der Funktionalität (Verlust der Verfügbarkeit)

Die unterschiedlichen Konzepte verbinden meist mehrere Schutzziele, für die es verschiedene technische Verfahren und Standards gibt. Wenn man Sicherheit in der Informations- und Netzwerktechnik wirklich ernst nimmt, dann kombiniert man mehrere Verfahren miteinander. Je nach Sicherheitsanforderungen muss das eine oder andere Konzept härter (= aufwändiger zu umgehen) sein.


### Sicherheitskriterien

Für verschiedene Personenkreise (Bürger, Experten, Unternehmen, Netzanbieter) in verschiedenen Staaten, in politischen und öffentlichen Organisationen (Politiker, Parteien, Geheimdienste, Polizei) sind jeweils unterschiedliche Sicherheitskriterien wichtig. Hierbei muss man berücksichtigen, dass der Bürger gerne seine Privacy (Privatsphäre) gewahrt sieht und sich wünscht, dass staatliche Behörden möglichst wenig Secrecy (Geheimhaltung) betreiben. Anders herum möchte der Staat die Secrecy (Geheimhaltung) gewahrt sehen und die Privacy (Privatsphäre) seiner Bürger aufweichen. Hierbei stehen sich jeweils Machtanspruch des Staates und das Misstrauen der Bürger gegenüber.

- Abrechenbarkeit (Accountability)
- Abstreitbarkeit (Repudiation)
- Anonymität (Anonymity)
- Authentizität/Echtheit (Authenticity)
- Funktionssicherheit (Safety)
- Identifizierung (Authentication)
- Informationssicherheit (Security)
- Integrität (Integrity)
- Verbindlichkeit/Nichtabstreitbarkeit (Non Repudiation)
- Verfügbarkeit (Availability)
- Vertraulichkeit (Confidentiality)
- Zugangskontrolle (Access Control)

Die Liste ist als unvollständig anzusehen.

### Anonymität (Anonymity)

Anonymität bedeutet, dass kein Rückschluss auf den Urheber von Daten und Kommunikation erfolgen kann.

### Authentizität/Echtheit (Authenticity)

Bei der Echtheitsprüfung geht es um die Authentizität der Kommunikationspartner. Bei den eingesetzten Verfahren wird festgestellt, ob der Kommunikationspartner auch tatsächlich der ist, für den er sich ausgibt. Hierbei wird eine eindeutige Zuordnung zwischen Absender und Nachricht gefordert.

### Funktionssicherheit (Safety)

Die Funktionssicherheit fordert, dass sich ein System konform zur erwarteten Funktionalität verhält. Das es also so funktioniert, wie es vorgesehen ist. Die eingesetzten Verfahren nehmen eine entsprechende Funktionsprüfung vor.

### Informationssicherheit (Security)

Die Informationssicherheit ist ein weit gefasster Begriff, der sich auf den Schutz der technischen Verarbeitung von Informationen bezieht. Sie ist Bestandteil der Funktionssicherheit. Bei der Informationssicherheit geht es speziell darum zu verhindern, dass Datenmanipulationen möglich sind oder unbefugt Informationen veröffentlicht werden.

### Integrität (Integrity)

Fast alle Daten und Nachrichten werden inzwischen digital verarbeitet. Privat und wirtschaftlich sind wir von der Integrität der Daten abhängig. Doch Daten und Nachricht können auf dem Weg durchs Netz unbemerkt verändert werden. Es muss deshalb die Integrität von Daten geprüft werden. Dazu zählen Mechanismen und Verfahren, die die Echtheit von Daten prüfen. Allerdings können sie nicht vor Manipulation schützen, sondern nur davor warnen.  
Wenn bei der Prüfung der Integrität eine Anomalie festgestellt wird, dann muss es sich dabei nicht zwangsläufig um eine Manipulation handeln. Es kann sich auch um einen Übertragungsfehler oder eine Funktionsstörung handeln.

### Vertraulichkeit (Confidentiality)

Bei der Vertraulichkeit geht es darum dafür zu sorgen, dass niemand Einblick in die Daten und Kommunikation erhält. Hier steht die Verschlüsselung der Daten und Kommunikation im Vordergrund. Eine wirksame Verschlüsselung erfolgt dabei Ende-zu-Ende. Das bezieht die Übertragung und Speicherung der Daten vom Sender zum Empfänger ein.

### Zugangskontrolle (Access Control)

Die Zugangskontrolle stellt sicher, dass nur zugelassene Benutzer einen Server oder Dienst benutzen können oder Zugang zu einem Netzwerk erhalten. Typischerweise erfolgt die Zugangskontrolle per Benutzername und Passwort. Alternativ per Zertifikat.  
Häufig wird die Zugangskontrolle mit der Echtheitsprüfung kombiniert.

### Beispiel: Sicherheitskonzept für ein VPN

- Authentizität
- Vertraulichkeit
- Integrität
- Zugangskontrolle

### Sicherheitskonzept aus der Sicht eines Anwenders

Für den Anwender ist es wichtig, seine Privatsphäre zu schützen, ohne dabei in seiner Meinungsfreiheit oder im Informationsaustausch eingeschränkt zu sein. Gleichzeitig möchte der Anwender Informationen im Internet auf ihren Wahrheitsgehalt überprüfen. Hierbei ergeben sich 4 Schutzziele, die aus Sicht des Anwenders bei der Nutzung des Internets wichtig sind.

- Privacy: Schutz der Privatsphäre
- Accountability: Nachweis, wer für bestimmte Handlungen im Netz verantwortlich ist
- Compliance: Einhaltung von Vereinbarungen
- Trust: Vertrauen in die Richtigkeit von Daten und Diensten

Ein Problem dabei ist, dass sich die einzelnen Konzepte gegenseitig behindern. Wenn man zum Beispiel auf den Schutz der Privatsphäre komplett verzichtet, dann kann man feststellen, wer was im Netz getan hat und kann dann auch auf die Richtigkeit von Daten über die Vertrauenswürdigkeit von Personen schließen. Wenn man nun die Privatsphäre dadurch schützt, dass jeder sich anonym im Netz bewegen kann, dann wird das mit der Verantwortlichkeit von Handlungen und die Richtigkeit von Daten schwierig einzuhalten. Im Prinzip geht es darum, wie man die Privatsphäre und Anonymität im Internet schützen kann und trotzdem die Möglichkeit hat, Verantwortliche bei Fehlverhalten zur Rechenschaft zu ziehen.

### Sicherheitskonzept: Anonymisierung durch Verschlüsselung

Sicherheitsexperten gehen davon aus, dass jegliche Verschlüsselung irgendwann gebrochen wird. Das bedeutet auch, dass alle verschlüsselten Daten irgendwann entschlüsselt werden können. Konsequent in die Zukunft gedacht, bedeutet das, dass Verschlüsselung eigentlich nichts bringt. Aus diesem Grund gibt es das Konzept der Anonymisierung, bei der nicht die Verschlüsselung das Ziel ist, sondern eine nachträglich Identifikation der Kommunikationsteilnehmer verhindert wird. Das funktioniert natürlich nur dann, wenn innerhalb der Kommunikation keine personenbezogenen Daten ausgetauscht werden.

- Encryption: Verschlüsselung, damit während der Kommunikation niemand die Nachrichten lesen kann.
- Authentication: Beglaubigung, damit man sicher sein kann, dass der Empfänger derjenige ist, für den man ihn hält.
- Deniability: Abstreitbarkeit, weil nachträglich keine Nachricht einem bestimmten Absender zugeordnet werden kann.
- Perfect Forward Secrecy: Folgenlosigkeit, damit bei Verlust des privaten Schlüssels keine Kompromittierung der bisherigen Kommunikation möglich ist.

Die praktische Umsetzung dieses Konzepts ist Off-the-Record Messaging.

### Zero Trust

Zero Trust ist ein Sicherheitskonzept, bei dem generell jedem Netzwerkverkehr, unabhängig von seiner Herkunft, misstraut wird. Teil des Konzepts ist, dass jeder Zugriff einer Zugangskontrolle und jede Verbindung einer Verschlüsselung unterliegt.

- [Zero Trust](https://www.elektronik-kompendium.de/sites/net/2512031.htm)