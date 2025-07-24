
Authentifizierung im Netzwerk ist ein Vorgang bei dem festgestellt wird, wer eine Person oder eine Maschine ist. Im echten Leben weisen wir uns durch Unterschriften, Pässe und Karten aus. In Netzwerken ist die Authentifizierung durch die räumliche Trennung erschwert. Hier greift man auf asymmetrische Schlüssel, Zertifikate und andere Authentifizierungsmechanismen zurück.

Knackpunkt bei jeder Authentifizierung im Netzwerk ist die Übertragung der Zugangsdaten. Zum Beispiel Benutzername und Passwort. Erfolgt die Übertragung unverschlüsselt, dann kann ein Angreifer die Zugangsdaten abhören und für seine Angriffsversuche missbrauchen.

Im Prinzip ist die Authentifizierung wichtiger als die Verschlüsselung. Denn eine verschlüsselte Kommunikation ist sinnlos, wenn ich nicht sicher sein kann, mit wem ich verbunden bin. Im schlechtesten Fall einige ich mich mit der falschen Gegenstelle auf eine verschlüsselte Kommunikation. Die Daten bekommt dann jemand, der sie nicht bekommen darf.

Im Zusammenhang mit der „Authentifizierung“ tauchen auch häufig die Begriffe "Autorisierung" und „Authentisierung“ auf.

- „Autorisierung“ ist der Vorgang, bei dem ermittelt wird, welche Berechtigung die Person oder Maschine hat und was sie machen darf.
- "Authentifizieren" bzw. "Authentifizierung" würde demnach bedeuten, dass eine elektronische Unterschrift oder Identität beglaubigt bzw. dessen Echtheit bezeugt wird.
- "Authentisieren" bzw. "Authentisierung" würde demnach bedeutet, dass der Nutzer oder Absender seine Identität glaubwürdig machen soll.  
    

In der deutschen Sprache gibt es einen Unterschied zwischen "authentifizieren" und "authentisieren". Im Duden steht dazu folgende Erläuterung:

> **au|then|ti|fi|zie|ren:** die Echtheit bezeugen oder beglaubigen  
> **au|then|ti|sie|ren:** glaubwürdig oder rechtsgültig machen

In der Praxis und im allgemeinen Sprachgebrauch wird zwischen beiden Formen jedoch nicht immer unterschieden. Im Allgemeinen spricht man auch dann von Authentifizierung, wenn die Authentisierung gemeint ist. In der englischen Sprache macht man keinen Unterschied zwischen „Authentifizierung“ und „Authentisierung“. Hier heißt es einfach „Authentication“.

### Übersicht: Authentifizierung

- Nutzer-Authentifizierung im Internet
- Authentifizierung mit Pre-Shared-Key (Passwort)
- Authentifizierung mit Zertifikat
- Kerberos
- SecurI

### Nutzer-Authentifizierung im Internet

Bei der Nutzer-Authentifizierung im Netzwerk geht es darum, dass ein Benutzer, Nutzer oder User persönlich von einem Dienst identifiziert wird, um Zugang zu einem Account, Daten oder Dienst zu erhalten.  
Typischerweise erfolgt die Nutzer-Authentifizierung über Benutzername und Passwort. Weil diese Zugangsdaten geklaut werden können, werden Zugänge durch eine 2-Faktor-Authentifizierung gesichert.  
Neuere Verfahren kommen ganz ohne Passwort aus und identifizieren den Nutzer anhand des Besitzes eines Geräts.

- [Nutzer-Authentifizierung im Internet](https://www.elektronik-kompendium.de/sites/net/2809021.htm)
- [2FA - Zwei-Faktor-Authentifizierung](https://www.elektronik-kompendium.de/sites/net/2511301.htm)
- [FIDO2 - Fast IDentity Online Version 2](https://www.elektronik-kompendium.de/sites/net/2809031.htm)
- [Passkeys](https://www.elektronik-kompendium.de/sites/net/2809051.htm)

### Authentifizierung mit Pre-Shared-Key (Passwort)

Ein Pre-Shared-Key ist ein Geheimnis, dass vor der Authentifizierung ausgetauscht werden muss. Also beide Seiten der Kommunikation „wissen“ müssen. Es handelt sich dabei um einen unsignierten Schlüssel, der frei wählbar ist.  
Damit ein unsignierter Schlüssel ein wenig Sicherheit verspricht, sollte es sich dabei um ein sehr schwer zu erratendes Passwort handeln. In der Regel erreicht man das dadurch, dass das Passwort möglichst viele Stellen lang ist und dass jede Stelle eine große Anzahl unterschiedlicher Zeichen umfassen kann.  
Wer das Passwort kennt, bekommt Zugang zu einem gesicherten Netzwerk. Das bedeutet auch, wer ungewollt an das Passwort gelangt, der kann einen fremden Dienst nutzen oder fremde Daten lesen.  
Sobald auch nur der Verdacht besteht, dass ein Passwort Dritten bekannt sein könnte, muss es sofort ausgetauscht werden.

- [Passwort, Pin und Passphrase](https://www.elektronik-kompendium.de/sites/net/2009021.htm)

### Authentifizierung mit Zertifikat

Zertifikate werden nicht nur bei der Authentifizierung, sondern auch bei der gesicherten Übertragung von E-Mails, dem Webseiten-Abruf (SSL/TLS) oder dem Code-Signing verwendet.  
Bei der Authentifizierung mit Zertifikaten kommen asymmetrische Verfahren zum Einsatz, die mit einem Schlüsselpaar zur Verschlüsselung oder zum Schlüsselaustausch arbeiten.  
Das Schlüsselpaar besteht aus einem öffentlichen Schlüssel, auch Public-Key genannt, und einem geheimen Schlüssel, auch Private-Key genannt. Während der Public-Key zum Beispiel in einem Zertifikat öffentlich gemacht wird, bleibt der Private-Key unter Verschluss.  
Bei X.509v3-Zertifikaten wird der öffentliche Schlüssel an eine Identität gekoppelt und durch eine Zertifizierungsstelle bzw. Certification Authority (CA) beglaubigt.  
Der Einsatz von Zertifikaten zieht also immer einen hohen Verwaltungsaufwand nach sich. Für eine zertifikatbasierte Authentifizierungsmethode ist eine Organisation und Infrastruktur notwendig, die Zertifikate beantragt, ausstellt und verteilt. Das machen eine oder mehrere Zertifizierungsstellen respektive eine Public Key Infrastructure (PKI).

### Software für die Verwaltung von Zertifikaten

- Windows Server
- OpenCA
- TinyCA
- Easy-RA (OpenVPN)

### Zero Trust

Zero Trust ist ein Sicherheitskonzept, bei dem generell jedem Netzwerkverkehr, unabhängig von seiner Herkunft, misstraut wird. Teil des Konzepts ist, dass jeder Zugriff einer Zugangskontrolle und jede Verbindung einer Verschlüsselung unterliegt.

- [Zero Trust](https://www.elektronik-kompendium.de/sites/net/2512031.htm)

### Übersicht: Protokolle für die Authentifizierung

- [PAP - Password Authentication Protocol](https://www.elektronik-kompendium.de/sites/net/0906161.htm)
- [CHAP - Challenge Handshake Authentication Protocol](https://www.elektronik-kompendium.de/sites/net/0906171.htm)
- [MS-CHAP - Microsoft CHAP](https://www.elektronik-kompendium.de/sites/net/0906181.htm)
- [EAP - Extensible Authentication Protocol](https://www.elektronik-kompendium.de/sites/net/1409231.htm)

### Übersicht: Authentifizierungsverfahren

- [Passwort, Pin und Passphrase](https://www.elektronik-kompendium.de/sites/net/2009021.htm)
- [2FA - Zwei-Faktor-Authentifizierung](https://www.elektronik-kompendium.de/sites/net/2511301.htm)
- [FIDO2](https://www.elektronik-kompendium.de/sites/net/2809031.htm)
- [Passkeys](https://www.elektronik-kompendium.de/sites/net/2809051.htm)
- [IEEE 802.1x / RADIUS](https://www.elektronik-kompendium.de/sites/net/1409281.htm)