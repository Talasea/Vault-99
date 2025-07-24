
Der Drei-Wege-Handschlag, auch als Three-Way-Handshake bezeichnet, ist ein Verfahren, das in TCP/IP-Netzwerken verwendet wird, um eine Verbindung zwischen einem Client und einem Server herzustellen. Dieser Prozess besteht aus drei Schritten, bei denen sowohl Client als auch Server Synchronisierungs- und Bestätigungspakete austauschen müssen, bevor der eigentliche Datenkommunikationsprozess beginnt.

1. **SYN-Paket**: Der Client sendet ein SYN-Paket an den Server, um eine Verbindung anzufragen.
    
2. **SYN-ACK-Paket**: Der Server antwortet mit einem SYN-ACK-Paket, das eine Bestätigung des Empfangs des SYN-Pakets und eine Anfrage zur Bestätigung der Verbindung enthält.
    
3. **ACK-Paket**: Der Client bestätigt die Verbindung durch das Senden eines ACK-Pakets an den Server.
    

Dieser Prozess gewährleistet, dass beide Enden der Verbindung sicher und verlustfrei kommunizieren können. Der Drei-Wege-Handschlag ist ein wesentlicher Bestandteil des TCP-Protokolls und wird verwendet, um eine sichere und zuverlässige Datenübertragung zu gewährleisten.

![[Pasted image 20250224093057.png]]![[Pasted image 20250224093109.png]]




-----



# Der TCP Drei-Wege-Handschlag: Das Fundament zuverlässiger Netzwerkkommunikation

Der vorliegende Text beschreibt korrekt den grundlegenden Ablauf des TCP Drei-Wege-Handschlags. Für angehende IT-Experten ist es jedoch entscheidend, die tieferliegenden Mechanismen und die Bedeutung dieses Prozesses für die Zuverlässigkeit und Funktionsweise des Internets zu verstehen.

**Warum überhaupt ein "Handschlag"? Die Notwendigkeit des Verbindungsaufbaus**

Im Gegensatz zu verbindungslosen Protokollen wie UDP (User Datagram Protocol) ist TCP (Transmission Control Protocol) ein **verbindungsorientiertes Protokoll**. Das bedeutet, bevor tatsächlich Daten zwischen zwei Anwendungen über das Netzwerk ausgetauscht werden können, muss eine **dedizierte Verbindung** zwischen dem Client und dem Server aufgebaut werden. Der Drei-Wege-Handschlag ist genau dieser Prozess, der sicherstellt, dass beide Kommunikationspartner bereit sind und die Grundlagen für eine zuverlässige Datenübertragung gelegt werden.

**Die detaillierten Schritte des Drei-Wege-Handschlags:**

Lassen Sie uns die einzelnen Schritte genauer unter die Lupe nehmen:

1. **SYN-Paket (Synchronize): Der Client initiiert die Verbindung**
    
    - **Aktion:** Der Client, der eine Verbindung zum Server aufbauen möchte (z.B. ein Webbrowser, der eine Webseite anfordert), sendet ein TCP-Segment mit dem **SYN-Flag** (Synchronize Sequence Number) gesetzt.
    - **Inhalt:** Dieses Paket enthält wichtige Informationen:
        - **Quell-Port:** Der Port, den der Client für diese Verbindung verwenden wird (oft ein zufälliger, ephemerer Port).
        - **Ziel-Port:** Der Port, an dem der Server auf Verbindungsanfragen lauscht (z.B. Port 80 für HTTP, Port 443 für HTTPS).
        - **Initial Sequence Number (ISN) des Clients:** Eine zufällige Zahl, die als Startpunkt für die Sequenznummerierung der vom Client gesendeten Daten dient. Diese Zufälligkeit ist wichtig für die Sicherheit, um beispielsweise SYN-Flood-Angriffe zu erschweren.
        - **Optionale TCP-Optionen:** Der Client kann in diesem Paket auch verschiedene TCP-Optionen aushandeln, z.B. die maximale Segmentgröße (MSS) oder die Verwendung von Fenstern zur Flusskontrolle.
    - **Zweck:** Der Client signalisiert dem Server seine Absicht, eine Verbindung aufzubauen, und teilt ihm seine Startsequenznummer mit.
2. **SYN-ACK-Paket (Synchronize-Acknowledge): Die Antwort des Servers**
    
    - **Aktion:** Wenn der Server die SYN-Anfrage vom Client empfängt und bereit ist, die Verbindung zu akzeptieren (der angefragte Dienst lauscht auf dem Ziel-Port), antwortet er mit einem TCP-Segment, bei dem sowohl das **SYN-Flag** als auch das **ACK-Flag** (Acknowledgement) gesetzt sind.
    - **Inhalt:** Dieses Paket enthält folgende Informationen:
        - **Quell-Port:** Der Port, an dem der Server auf Verbindungen lauscht (der gleiche wie der Ziel-Port im SYN-Paket des Clients).
        - **Ziel-Port:** Der Port, den der Client im SYN-Paket als Quell-Port verwendet hat.
        - **Acknowledge Number:** Diese Nummer bestätigt den Empfang des SYN-Pakets vom Client. Sie ist auf die **Sequenznummer des Clients plus eins** gesetzt (ISN_Client + 1). Dies signalisiert dem Client, dass der Server das SYN-Paket erfolgreich empfangen hat und das nächste erwartete Byte vom Client die Sequenznummer ISN_Client + 1 hätte.
        - **Initial Sequence Number (ISN) des Servers:** Eine eigene zufällige Zahl, die als Startpunkt für die Sequenznummerierung der vom Server gesendeten Daten dient.
        - **Optionale TCP-Optionen:** Der Server kann ebenfalls TCP-Optionen aushandeln oder dem Client Optionen vorschlagen.
    - **Zweck:** Der Server bestätigt den Empfang der Verbindungsanfrage des Clients und signalisiert gleichzeitig seine Bereitschaft zur Verbindung, indem er seine eigene Startsequenznummer mitteilt und den Empfang des SYN des Clients bestätigt.
3. **ACK-Paket (Acknowledge): Die Bestätigung des Clients**
    
    - **Aktion:** Nachdem der Client das SYN-ACK-Paket vom Server erhalten hat, sendet er ein letztes TCP-Segment mit dem **ACK-Flag** gesetzt.
    - **Inhalt:** Dieses Paket enthält:
        - **Quell-Port:** Der Port, den der Client für diese Verbindung verwendet.
        - **Ziel-Port:** Der Port, an dem der Server auf Verbindungen lauscht.
        - **Acknowledge Number:** Diese Nummer bestätigt den Empfang des SYN-ACK-Pakets vom Server. Sie ist auf die **Sequenznummer des Servers plus eins** gesetzt (ISN_Server + 1). Dies signalisiert dem Server, dass der Client das SYN des Servers erfolgreich empfangen hat und das nächste erwartete Byte vom Server die Sequenznummer ISN_Server + 1 hätte.
        - **Sequenznummer:** Die Sequenznummer des Clients wird hier um eins erhöht (ISN_Client + 1), da der Client im vorherigen Schritt effektiv ein "virtuelles Byte" (das SYN-Flag) gesendet hat.
        - **Keine Nutzdaten:** In diesem dritten Schritt werden in der Regel noch keine eigentlichen Anwendungsdaten übertragen. Die Verbindung ist nun etabliert.
    - **Zweck:** Der Client bestätigt den Empfang der Antwort des Servers und signalisiert, dass die Verbindung nun beidseitig aufgebaut ist und die Datenübertragung beginnen kann.

**Die Bedeutung von Sequenz- und Bestätigungsnummern:**

Die zufälligen Initial Sequence Numbers (ISNs) und die darauf aufbauenden Sequenz- und Bestätigungsnummern sind essenziell für die **Zuverlässigkeit und geordnete Übertragung** von Daten in TCP. Sie ermöglichen es:

- **Doppelte oder verlorene Pakete zu erkennen:** Empfänger können anhand der Sequenznummern feststellen, ob Pakete fehlen oder mehrfach angekommen sind.
- **Pakete in der richtigen Reihenfolge zusammenzusetzen:** Da IP-Pakete über verschiedene Wege im Netzwerk geroutet werden können, erreichen sie das Ziel möglicherweise nicht in der gesendeten Reihenfolge. Die Sequenznummern ermöglichen es dem Empfänger, die Daten korrekt zu ordnen.
- **Den Fluss der Daten zu kontrollieren:** Durch die Verwendung von Fenstern und Bestätigungsnummern können Sender und Empfänger aushandeln, wie viele Daten gleichzeitig übertragen werden sollen, um eine Überlastung des Netzwerks oder des Empfängers zu vermeiden.

**Zustandsübergänge während des Handschlags:**

Der Drei-Wege-Handschlag führt zu spezifischen Zustandsübergängen auf beiden Seiten der Verbindung:

- **Client:**
    - **CLOSED:** Ausgangszustand.
    - **SYN_SENT:** Nach dem Senden des SYN-Pakets.
    - **ESTABLISHED:** Nach dem Empfang des SYN-ACK und dem Senden des ACK-Pakets. Nun können Daten übertragen werden.
- **Server:**
    - **LISTEN:** Der Server wartet auf eingehende Verbindungen an einem bestimmten Port.
    - **SYN_RCVD:** Nach dem Empfang des SYN-Pakets vom Client.
    - **ESTABLISHED:** Nach dem Empfang des ACK-Pakets vom Client. Die Verbindung ist bereit.

**Der Vollständigkeit halber: Der Vier-Wege-Handschlag zum Verbindungsabbau**

Es ist auch wichtig zu wissen, dass das Beenden einer TCP-Verbindung einen ähnlichen, aber etwas längeren Prozess erfordert, der als **Vier-Wege-Handschlag** bezeichnet wird. Hierbei senden Client und Server jeweils ein FIN-Paket (Finish), um das Ende ihrer jeweiligen Sendeseite der Verbindung zu signalisieren, und bestätigen den Empfang des FIN-Pakets des anderen mit einem ACK-Paket.

**Sicherheitsaspekte des Drei-Wege-Handschlags:**

Obwohl der Drei-Wege-Handschlag die Grundlage für zuverlässige Verbindungen bildet, kann er auch Ziel von Angriffen sein:

- **SYN-Flood-Angriff:** Ein Angreifer sendet eine große Anzahl von SYN-Paketen mit gefälschten Absenderadressen an den Server. Der Server antwortet auf jede Anfrage mit einem SYN-ACK und reserviert Ressourcen für die vermeintliche Verbindung. Da die ACK-Pakete des Clients aufgrund der gefälschten Adressen nie ankommen, bleiben die Verbindungen im Zustand SYN_RCVD hängen und die Ressourcen des Servers werden erschöpft, was zu einem Denial-of-Service (DoS) führen kann. Moderne Betriebssysteme und Firewalls verfügen über Mechanismen, um solche Angriffe zu mitigieren (z.B. SYN-Cookies).

**Analogie zur realen Welt:**

Stellen Sie sich vor, Sie rufen jemanden am Telefon an:

1. **SYN:** Sie (der Client) sagen "Hallo?" (Verbindungsanfrage).
2. **SYN-ACK:** Die andere Person (der Server) antwortet "Hallo, ich habe Sie gehört, wer ist da?" (Bestätigung und Gegenfrage).
3. **ACK:** Sie (der Client) sagen "Ich bin's, [Ihr Name]." (Bestätigung der Gegenfrage).

Nun steht die "Verbindung" und Sie können miteinander sprechen (Daten austauschen).

**Bedeutung für angehende IT-Experten:**

Das Verständnis des TCP Drei-Wege-Handschlags ist für angehende IT-Experten aus mehreren Gründen unerlässlich:

- **Grundlegendes Netzwerkverständnis:** Es ist ein Kernkonzept, das die Basis für das Verständnis der Funktionsweise des Internets und vieler Netzwerkprotokolle bildet.
- **Fehlerbehebung:** Bei Netzwerkproblemen ist das Wissen über den Verbindungsaufbau oft entscheidend, um die Ursache des Problems zu finden (z.B. wenn eine Verbindung nicht zustande kommt).
- **Sicherheitsanalyse:** Das Erkennen von Anomalien im Verbindungsaufbau kann auf Sicherheitsvorfälle hindeuten (z.B. SYN-Flood-Angriffe).
- **Anwendungsentwicklung:** Entwickler müssen die Grundlagen der TCP-Verbindungen verstehen, um robuste und zuverlässige Netzwerkanwendungen zu erstellen.
- **Netzwerkdiagnose:** Tools wie Wireshark ermöglichen es, den Netzwerkverkehr auf Paketebene zu analysieren, und das Verständnis des Drei-Wege-Handschlags ist unerlässlich, um diese Analysen durchzuführen.

Indem Sie die Details des TCP Drei-Wege-Handschlags verstehen, legen Sie ein wichtiges Fundament für Ihr weiteres Studium und Ihre Karriere im Bereich der Informationstechnologie. Es ist ein Konzept, das Ihnen immer wieder begegnen wird und dessen Beherrschung Ihnen einen klaren Vorteil verschafft.