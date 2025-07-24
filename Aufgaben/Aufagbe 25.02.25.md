

#### Untersuche mit Wireshark einen TLS handshake zu der Webseite https://www.nist.gov/. * Welche cipher suite wird in deinem Handshake ausgewählt?


- **Wireshark starten:** Öffne Wireshark und wähle die Netzwerkschnittstelle aus, über die du den Datenverkehr erfassen möchtest (in der Regel die, die mit deinem Internet verbunden ist).
    
- **Aufzeichnung starten:** Klicke auf den "Hai"-Symbol, um die Aufzeichnung des Netzwerkverkehrs zu starten.
    
- **Website besuchen:** Öffne deinen Webbrowser und rufe die Website `https://www.nist.gov/` auf. Dadurch wird ein TLS-Handshake zwischen deinem Browser und dem Server von NIST initiiert.
    
- **Aufzeichnung stoppen:** Kehre zu Wireshark zurück und klicke auf das rote Quadrat-Symbol, um die Aufzeichnung zu stoppen, sobald die Seite geladen ist.
    
- **TLS-Handshake filtern:** In Wireshark kannst du den erfassten Datenverkehr filtern, um nur die TLS-Handshake-Pakete anzuzeigen. Gib in das Filterfeld oben `tls.handshake.type == 1` ein und drücke die Eingabetaste. Dies zeigt die "Client Hello"-Nachricht des TLS-Handshake.
    ![[Pasted image 20250225133430.png]]
- **"Client Hello" untersuchen:** Klicke auf die "Client Hello"-Nachricht in der Liste der Pakete. Im unteren Bereich von Wireshark werden die Details des Pakets angezeigt.
    ![[Pasted image 20250225132851.png]]
- **Cipher Suites finden:** Scrolle in den Details der "Client Hello"-Nachricht nach unten, bis du den Abschnitt "Cipher Suites" findest. Hier siehst du eine Liste der vom Client (deinem Browser) unterstützten Verschlüsselungssätze.
    
- **"Server Hello" untersuchen:** Suche nach der "Server Hello"-Nachricht (in der Regel das nächste Paket nach dem "Client Hello"). Diese Nachricht enthält die vom Server ausgewählte Cipher Suite.
    ![[Pasted image 20250225132931.png]]
- **Ausgewählte Cipher Suite identifizieren:** Klicke auf die "Server Hello"-Nachricht. In den Details findest du den Abschnitt "Cipher Suite", der die vom Server gewählte Verschlüsselungssuite angibt.

![[Pasted image 20250225142711.png]]


## Schritte

1. **"Server Hello" auswählen:** Klicke in Wireshark auf die "Server Hello"-Nachricht, die auf die "Client Hello"-Nachricht folgt.



![[Pasted image 20250225132851.png]]




1. **Details anzeigen:** Im unteren Bereich von Wireshark werden die Details des Pakets angezeigt. Scrolle nach unten zum Abschnitt "Cipher Suite".


![[Pasted image 20250225132931.png]]



1. **Cipher Suite identifizieren:** Hier findest du die vom Server gewählte Cipher Suite. Sie wird in der Regel als hexadezimaler Wert oder als eine Kombination von Abkürzungen dargestellt.


![[Pasted image 20250225133013.png]]






2. **Cipher Suite-Spezifikation suchen:** Um die Bedeutung der Abkürzungen und die enthaltenen Algorithmen zu verstehen, musst du die Spezifikation der TLS-Cipher Suites konsultieren. Eine gute Ressource ist die offizielle IANA-Liste der TLS-Cipher Suites:
    - [https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-4](https://www.google.com/search?q=https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml%23tls-parameters-4)

![[Pasted image 20250225133224.png]]





![[Pasted image 20250225133339.png]]





3. **Cipher Suite-Details interpretieren:** In der IANA-Liste kannst du nach der spezifischen Cipher Suite suchen, die in deinem Handshake ausgewählt wurde. Die Liste enthält detaillierte Informationen über die enthaltenen Algorithmen, wie z. B.:
    - **Key Exchange Algorithm:** Der Algorithmus, der für den Austausch der kryptografischen Schlüssel verwendet wird (z. B. RSA, Diffie-Hellman).
    - **Cipher Algorithm:** Der Algorithmus, der für die Verschlüsselung der übertragenen Daten verwendet wird (z. B. AES, ChaCha20).
    - **MAC Algorithm:** Der Algorithmus, der für die Erstellung von Message Authentication Codes (MACs) verwendet wird, um die Integrität der Daten zu gewährleisten (z. B. SHA256, SHA384).



