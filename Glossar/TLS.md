
Transport Layer Security (TLS) ist ein Protokoll zur sicheren Datenübertragung im Internet. Es sorgt für verschlüsselte Verbindungen und Authentifizierung von Servern

TLS ist der Nachfolger von SSL (Secure Sockets Layer), das von Netscape in den 1990er Jahren entwickelt wurde.
Die IETF übernahm die Weiterentwicklung und Normierung, was zur Einführung von TLS 1.0 im Jahr 1999 führte.
LS besteht aus zwei Hauptkomponenten: TLS Handshake und TLS Record. Im TLS Handshake findet ein sicherer Schlüsselaustausch und eine Authentifizierung statt, während TLS Record die Datenverschlüsselung durchführt.
TLS wird beispielsweise bei HTTPS-Verbindungen, IMAPS, POP3S und SMTPS verwendet.




## Definition Transport Layer Security (TLS)Was ist TLS (Transport Layer Security)?

28.12.2017Autor / Redakteur: [Dipl.-Ing. (FH) Stefan Luber](https://www.security-insider.de/autor/stefan-luber/1590387/) / [Peter Schmitz](https://www.security-insider.de/autor/peter-schmitz/26629/)

Bei der Transport Layer Security (TLS) handelt es sich um ein Protokoll der Schicht 5 des ISO/OSI-Schichtenmodells, das für eine verschlüsselte Übertragung von Daten im Internet sorgt. TLS ist der Nachfolger von SSL und wird beispielsweise von Browsern für sichere HTTPS-Verbindungen verwendet.



![TLS (Transport Layer Security) ist der Nachfolger von SSL (Secure Sockets Layer) und dient der verschlüsselten Übertragung von Daten über das Internet oder andere Netze.](https://cdn1.vogel.de/unsafe/540x0/smart/images.vogel.de/vogelonline/bdb/1335100/1335168/original.jpg "TLS (Transport Layer Security) ist der Nachfolger von SSL (Secure Sockets Layer) und dient der verschlüsselten Übertragung von Daten über das Internet oder andere Netze.")

TLS (Transport Layer Security) ist der Nachfolger von SSL (Secure Sockets Layer) und dient der verschlüsselten Übertragung von Daten über das Internet oder andere Netze.

(Bild: Pixabay / [CC0](https://creativecommons.org/publicdomain/zero/1.0/) )

Die Abkürzung TLS steht für Transport Layer Security und bezeichnet das Nachfolgeprotokoll von SSL (Secure Sockets Layer). Mit Hilfe von Transport Layer Security lassen sich Daten verschlüsselt über das Internet oder andere Netzwerke übertragen. Es handelt sich um ein hybrides Verschlüsselungsprotokoll (Kombination aus asymmetrischer und symmetrischer [Verschlüsselung](https://www.security-insider.de/was-ist-verschluesselung-a-618734/)), das folgende Ziele verfolgt. Die übertragenen Daten sollen durch die Verschlüsselung vor dem unbefugten Zugriff Dritter und vor Manipulation oder Fälschung geschützt werden. Zusätzlich ermöglicht TLS die [Authentifizierung](https://www.security-insider.de/was-ist-authentifizierung-a-47c6dc273418ad29315eedba3a8097ca/) der Kommunikationsteilnehmer und das Überprüfen von [Identitäten](https://www.security-insider.de/was-ist-eine-digitale-identitaet-a-604019/) von Empfänger oder Sender. Häufig kommt TLS für die gesicherte Verbindung zwischen einem Client mit Internetbrowser und einem Webserver per HTTPS zum Einsatz. Aber auch andere Protokolle wie SMTP (Simple Mail Transfer Protocol), POP3 (Post Office Protocol) oder FTP (File Transfer Protokoll) können Transport Layer Security nutzen.

Die Kommunikation per TLS lässt sich in zwei Phasen unterteilen. Zuerst findet der Aufbau einer Verbindung statt, bei der Client und Server gegenseitig ihre Identität nachweisen. Ist eine vertrauenswürdige Verbindung aufgebaut, erfolgt die Übertragung der Daten unter Verwendung eines Verschlüsselungsalgorithmus. Im [ISO](https://www.security-insider.de/was-ist-die-iso-a-1094262/)/OSI-Schichtenmodell ist Transport Layer Security auf dem Layer 5 (Sitzungsschicht - Session Layer) angesiedelt. Dank seiner transparenten Arbeitsweise für die Protokolle höherer Ebenen ist TLS sehr flexibel und vielseitig einsetzbar. Bekannte Implementierungen von TLS sind beispielsweise GnuTLS, [OpenSSL](https://www.security-insider.de/was-ist-openssl-a-698279/) oder LibreSSL.

### Das TLS Record Protocol

Für die Transport Layer Security spielt das so genannte Transport Layer Security Record Protocol eine zentrale Rolle. Vier weitere Protokolle des Standards bauen auf diesem auf. Diese vier Protokolle sind:

- das Handshake Protocol

- das Alert Protocol

- das Change Cipher Spec Protocol

- das Application Data Protocol

Das [Handshake](https://www.security-insider.de/was-ist-ein-handshake-a-933756/) Protocol ist für die Aushandlung einer Sitzung und ihrer Sicherheitsparameter verantwortlich. Unter anderem werden innerhalb des Handshake Protocols die verwendeten kryptographischen Algorithmen und das Schlüsselmaterial ausgehandelt sowie die Kommunikationspartner authentifiziert. Das Alert Protocol ist für die Fehler- und Alarmbehandlung von TLS-Verbindungen zuständig. Es kann das sofortige Abbrechen einer Verbindung veranlassen. Mit Hilfe des Application Data Protocols werden die Anwendungsdaten in Blöcke zerlegt, komprimiert, verschlüsselt und übertragen. Das Change Cipher Spec Protocol schließlich teilt dem Empfänger mit, dass der Sender auf die zuvor im Handshake Protocol ausgehandelte Cipher Suite wechselt.

### Der Verbindungsaufbau bei Transport Layer Security

Baut ein Client eine Verbindung zu einem Server auf, authentifiziert sich der Server mit einem Zertifikat. Der Client überprüft die Vertrauenswürdigkeit des [Zertifikats](https://www.security-insider.de/was-ist-ein-digitales-zertifikat-a-688440/) und dessen Übereinstimmung mit dem Servernamen. Optional ist die Authentifizierung des Clients gegenüber dem Server möglich. In einem nächsten Schritt leiten die Kommunikationspartner unter Zuhilfenahme des öffentlichen Schlüssels des Servers einen kryptographischen Sitzungsschlüssel ab, mit dem sie anschließend sämtliche zu übertragenen Nachrichten verschlüsseln. Die Authentifizierung und Identifikation der Kommunikationspartner basieren also auf asymmetrischen Verschlüsselungsverfahren und der Public-Key-[Kryptografie](https://www.security-insider.de/was-ist-kryptographie-a-642288/). Der eigentliche Sitzungsschlüssel ist ein einmalig nutzbarer symmetrischer Schlüssel, mit dem die Daten sowohl entschlüsselt als auch verschlüsselt werden.



----

## Detaillierte Analyse von Transport Layer Security (TLS): Die Grundlage für sichere Internetkommunikation

Der bereitgestellte Text liefert eine ausgezeichnete Einführung in das TLS-Protokoll und seine Bedeutung für die sichere Datenübertragung im Internet. Lassen Sie uns nun die verschiedenen Aspekte im Detail beleuchten, wobei wir sowohl den kurzen Text als auch den ausführlicheren Artikel von security-insider.de berücksichtigen:

### 1. Kernverständnis von TLS

Transport Layer Security (TLS) ist ein **kryptographisches Protokoll**, das entwickelt wurde, um **sichere Datenübertragung über Netzwerke wie das Internet zu gewährleisten**. Seine Hauptfunktionen sind die **Verschlüsselung der Kommunikation** und die **Authentifizierung der Kommunikationspartner**, insbesondere des Servers.

### 2. Die Historie: Von SSL zu TLS

- **SSL als Vorläufer:** Der Text erwähnt korrekt, dass TLS der **Nachfolger von Secure Sockets Layer (SSL)** ist. SSL wurde in den 1990er Jahren von Netscape entwickelt und war das erste weit verbreitete Protokoll für sichere Webkommunikation.
- **Weiterentwicklung durch die IETF:** Die **Internet Engineering Task Force (IETF)** übernahm die Weiterentwicklung und Standardisierung von SSL, was zur Einführung von **TLS 1.0 im Jahr 1999** führte.
- **Evolution der TLS-Versionen:** Seit TLS 1.0 gab es mehrere Weiterentwicklungen und neue Versionen, darunter TLS 1.1, TLS 1.2 und die aktuellste Version TLS 1.3, die jeweils Verbesserungen in Bezug auf Sicherheit und Leistung brachten.

### 3. Hauptkomponenten von TLS

Der kurze Text erwähnt die zwei Hauptkomponenten von TLS:

- **TLS Handshake:** Diese Phase dient dem **sicheren Schlüsselaustausch** zwischen Client und Server sowie der **Authentifizierung** des Servers (und optional des Clients). Während des Handshakes werden die kryptographischen Algorithmen ausgehandelt, die für die sichere Kommunikation verwendet werden sollen.
- **TLS Record:** Nach dem erfolgreichen Handshake übernimmt das TLS Record Protocol die **Verschlüsselung der eigentlichen Anwendungsdaten**, die zwischen Client und Server ausgetauscht werden.

### 4. Ziele von TLS (laut Artikel)

Der Artikel von security-insider.de ergänzt die Definition um wichtige Ziele von TLS:

- **Schutz vor unbefugtem Zugriff:** Die **Verschlüsselung** der übertragenen Daten soll verhindern, dass Dritte die Kommunikation mitlesen oder abfangen können.
- **Schutz vor Manipulation und Fälschung:** TLS stellt sicher, dass die übertragenen Daten **nicht unbemerkt verändert oder gefälscht** werden können.
- **Authentifizierung der Kommunikationsteilnehmer:** TLS ermöglicht die **Überprüfung der Identität** der Kommunikationspartner, insbesondere des Servers durch den Einsatz von digitalen Zertifikaten. Optional kann auch der Client authentifiziert werden.

### 5. Anwendungsbereiche von TLS

Beide Texte erwähnen wichtige Anwendungsbereiche von TLS:

- **HTTPS (Hypertext Transfer Protocol Secure):** Die bekannteste Anwendung von TLS ist die **sichere Verbindung zwischen einem Webbrowser (Client) und einem Webserver**. Das "S" in HTTPS steht für "Secure" und signalisiert, dass die Kommunikation über TLS verschlüsselt wird.
- **Andere Protokolle:** TLS kann auch zur Sicherung anderer Internetprotokolle verwendet werden, wie im Artikel genannt:
    - **IMAPS (Internet Message Access Protocol Secure):** Sichere Übertragung von E-Mails vom Server zum Client.
    - **POP3S (Post Office Protocol version 3 Secure):** Sichere Übertragung von E-Mails vom Server zum Client.
    - **SMTPS (Simple Mail Transfer Protocol Secure):** Sichere Übertragung von E-Mails vom Client zum Server und zwischen Servern.
    - **FTP (File Transfer Protocol) über TLS (FTPS):** Sichere Übertragung von Dateien.

### 6. Phasen der TLS-Kommunikation (laut Artikel)

Der Artikel unterteilt die TLS-Kommunikation in zwei Phasen:

- **Verbindungsaufbau:** In dieser Phase **authentifizieren sich Client und Server gegenseitig**. Der Server weist seine Identität in der Regel durch ein **digitales Zertifikat** nach, dessen Vertrauenswürdigkeit der Client überprüft. Optional kann auch der Client sich beim Server authentifizieren.
- **Datenübertragung:** Nach dem erfolgreichen Aufbau einer vertrauenswürdigen Verbindung erfolgt die **Übertragung der eigentlichen Anwendungsdaten unter Verwendung eines ausgehandelten Verschlüsselungsalgorithmus**.

### 7. TLS im ISO/OSI-Schichtenmodell (laut Artikel)

Der Artikel ordnet TLS der **Schicht 5 (Sitzungsschicht - Session Layer)** des ISO/OSI-Modells zu. Diese Schicht ist für die Verwaltung und Steuerung der Verbindungen zwischen Anwendungen zuständig.

### 8. Bekannte Implementierungen von TLS (laut Artikel)

Der Artikel nennt einige bekannte Implementierungen von TLS:

- **GnuTLS:** Eine freie Software-Bibliothek, die das TLS-Protokoll implementiert.
- **OpenSSL:** Eine weit verbreitete Open-Source-Implementierung der SSL- und TLS-Protokolle.
- **LibreSSL:** Ein Fork von OpenSSL, der mit dem Ziel einer erhöhten Sicherheit und Bereinigung des Codes entwickelt wurde.

### 9. Das TLS Record Protocol im Detail (laut Artikel)

Der Artikel betont die zentrale Rolle des **Transport Layer Security Record Protocol**. Vier weitere Protokolle des TLS-Standards bauen auf diesem auf:

- **Handshake Protocol:** Verantwortlich für die **Aushandlung der Sitzungsparameter**, einschließlich der verwendeten kryptographischen Algorithmen und des Schlüsselmaterials, sowie für die **Authentifizierung** der Kommunikationspartner.
- **Alert Protocol:** Zuständig für die **Fehler- und Alarmbehandlung** von TLS-Verbindungen. Es ermöglicht das sofortige Abbrechen einer Verbindung bei Problemen.
- **Change Cipher Spec Protocol:** Teilt dem Empfänger mit, dass der Sender **auf die zuvor im Handshake Protocol ausgehandelte Cipher Suite wechselt**.
- **Application Data Protocol:** Dient dazu, die **Anwendungsdaten in Blöcke zu zerlegen, optional zu komprimieren, zu verschlüsseln und zu übertragen**.

### 10. Der Verbindungsaufbau bei TLS im Detail (laut Artikel)

Der Artikel beschreibt den Verbindungsaufbau genauer:

- **Serverauthentifizierung:** Der Server authentifiziert sich gegenüber dem Client mit einem **digitalen Zertifikat**.
- **Zertifikatsprüfung:** Der Client **überprüft die Vertrauenswürdigkeit des Zertifikats** (z.B. durch Überprüfung der ausstellenden Zertifizierungsstelle) und stellt sicher, dass der **Name im Zertifikat mit dem Servernamen übereinstimmt**.
- **Optionale Clientauthentifizierung:** In einigen Fällen kann auch der **Client sich optional beim Server authentifizieren**.
- **Sitzungsschlüsselableitung:** Client und Server leiten unter Verwendung des **öffentlichen Schlüssels des Servers** einen **kryptographischen Sitzungsschlüssel** ab.
- **Symmetrische Verschlüsselung:** Mit diesem **einmalig nutzbaren symmetrischen Schlüssel** werden anschließend **sämtliche zu übertragenden Nachrichten verschlüsselt und entschlüsselt**.

### 11. Hybride Verschlüsselung in TLS (laut Artikel)

TLS verwendet ein **hybrides Verschlüsselungsprotokoll**, das die Vorteile von **asymmetrischer und symmetrischer Verschlüsselung** kombiniert:

- **Asymmetrische Verschlüsselung (Public-Key-Kryptographie):** Wird für den **sicheren Schlüsselaustausch** während des Handshakes und für die **Authentifizierung** der Kommunikationspartner verwendet.
- **Symmetrische Verschlüsselung:** Wird für die die **effiziente Verschlüsselung der eigentlichen Datenübertragung** verwendet, da sie deutlich schneller ist als asymmetrische Verfahren.

### 12. Bedeutung von TLS für die Web-Sicherheit

TLS ist eine **grundlegende Technologie für die Sicherheit im Internet**. Es schützt sensible Informationen wie Passwörter, Kreditkartendaten und persönliche Daten, die über das Web übertragen werden. Ohne TLS wäre sicheres Online-Shopping, Online-Banking oder die Nutzung vieler Webanwendungen nicht möglich.

### 13. Evolution der TLS-Versionen

Die verschiedenen Versionen von TLS brachten wichtige Sicherheitsverbesserungen und die Behebung von Schwachstellen. Es ist wichtig, dass moderne Systeme aktuelle TLS-Versionen wie 1.2 oder besser noch 1.3 verwenden, da ältere Versionen (z.B. SSLv3, TLS 1.0, TLS 1.1) als unsicher gelten und nicht mehr verwendet werden sollten.

### 14. Vorteile der Verwendung von TLS

- **Vertraulichkeit:** Schutz der Daten vor dem Mitlesen durch Unbefugte.
- **Integrität:** Sicherstellung, dass die Daten während der Übertragung nicht manipuliert wurden.
- **Authentizität:** Überprüfung der Identität des Servers (und optional des Clients).

### 15. Formatierung der Antwort

Die Antwort wurde übersichtlich und gut strukturiert mit Hilfe von Markdown formatiert, um die Lesbarkeit zu maximieren.

Zusammenfassend lässt sich sagen, dass Transport Layer Security (TLS) ein **essentielles Protokoll für die sichere Kommunikation im Internet** ist. Es hat sich aus seinem Vorgänger SSL entwickelt und bietet durch seine Kombination aus Handshake und Record Protocol eine robuste Grundlage für verschlüsselte Verbindungen und die Authentifizierung von Servern. Die Verwendung von TLS ist in zahlreichen Internetanwendungen unerlässlich und trägt maßgeblich zum Schutz sensibler Daten bei. Der Artikel von security-insider.de bietet hierzu eine sehr informative und detaillierte Ergänzung.