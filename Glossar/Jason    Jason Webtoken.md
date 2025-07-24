JSON (JavaScript Object Notation) ist ein leichtgewichtiges Datenformat, das für den einfachen Datenaustausch zwischen Anwendungen konzipiert wurde. Es ist sowohl für Menschen leicht lesbar als auch für Maschinen leicht zu verarbeiten und basiert auf einer Teilmenge der JavaScript-Syntax.

**Möglichkeiten von JSON:**

- **Datenübertragung:** JSON ist das De-facto-Standardformat für die Übertragung strukturierter Daten über das Internet, insbesondere in Webanwendungen und APIs (Application Programming Interfaces). Es wird häufig verwendet, um Daten vom Server an den Client (z. B. einen Webbrowser oder eine mobile App) und umgekehrt zu senden.
- **Konfigurationsdateien:** JSON eignet sich hervorragend zum Speichern von Konfigurationsdaten für Anwendungen und Systeme. Es ist einfacher zu lesen und zu bearbeiten als ältere Formate wie XML oder INI-Dateien.
- **Datenspeicherung:** JSON kann in NoSQL-Datenbanken wie MongoDB oder Couchbase direkt als Dokumentformat gespeichert und abgerufen werden. Dies ermöglicht eine flexible und schemalose Datenhaltung.
- **Interprozesskommunikation:** JSON kann als Format für die Kommunikation zwischen verschiedenen Prozessen auf demselben oder verschiedenen Systemen verwendet werden.
- **Serialisierung und Deserialisierung:** Viele Programmiersprachen bieten Bibliotheken zum einfachen Serialisieren (Umwandeln von Objekten in JSON-Strings) und Deserialisieren (Umwandeln von JSON-Strings in Objekte) von Datenstrukturen.

**Erstellung von JSON:**

JSON-Daten bestehen aus Schlüssel-Wert-Paaren. Die grundlegenden Datentypen und Strukturen in JSON sind:

- **Objekte:** Eine ungeordnete Sammlung von Schlüssel-Wert-Paaren, eingeschlossen in geschweifte Klammern `{}`. Schlüssel müssen Strings in doppelten Anführungszeichen sein. Werte können primitive Datentypen (String, Zahl, Boolean, null), andere Objekte oder Arrays sein.
    
    JSON
    
    ```
    {
      "name": "John Doe",
      "age": 30,
      "isStudent": false,
      "address": {
        "street": "123 Main St",
        "city": "Anytown"
      }
    }
    ```
    
- **Arrays:** Eine geordnete Liste von Werten, eingeschlossen in eckige Klammern `[]`. Werte in einem Array können beliebigen gültigen JSON-Datentyp haben.
    
    JSON
    
    ```
    {
      "hobbies": ["reading", "hiking", "coding"],
      "grades": [85, 92, 78]
    }
    ```
    
- **Primitive Datentypen:**
    - **String:** Eine Zeichenkette in doppelten Anführungszeichen (z. B. `"hello"`).
    - **Number:** Eine numerische Zahl (ganz oder mit Dezimalstellen, z. B. `42`, `3.14`).
    - **Boolean:** Ein Wahrheitswert (`true` oder `false`).
    - **null:** Ein leerer Wert (`null`).

**Worauf Sie bei der Erstellung von JSON achten müssen:**

- **Syntax:** JSON hat eine strenge Syntax. Achten Sie auf korrekte Klammern (geschweifte für Objekte, eckige für Arrays), Anführungszeichen (doppelte für Schlüssel und Strings), Kommas (zur Trennung von Schlüssel-Wert-Paaren und Array-Elementen) und Doppelpunkte (zur Trennung von Schlüsseln und Werten).
- **Schlüssel als Strings:** Alle Schlüssel in JSON-Objekten müssen Strings sein und in doppelten Anführungszeichen stehen.
- **Keine Kommentare:** JSON unterstützt keine Kommentare im Standard. Wenn Sie Kommentare benötigen, sollten Sie ein anderes Format oder eine Erweiterung von JSON verwenden.
- **Datentypen:** Seien Sie sich der unterstützten Datentypen bewusst. Funktionen oder Datentypen, die spezifisch für Programmiersprachen sind, können in JSON nicht direkt dargestellt werden und müssen gegebenenfalls in unterstützte Typen umgewandelt werden (z. B. Datumsangaben als Strings im ISO 8601-Format).
- **Encoding:** Verwenden Sie UTF-8 als Standardzeichenkodierung für JSON-Dateien, um eine korrekte Darstellung von Sonderzeichen und internationalen Zeichen sicherzustellen.
- **Validierung:** Verwenden Sie JSON-Validatoren (online-Tools oder Bibliotheken in Ihrer Programmiersprache), um sicherzustellen, dass Ihr JSON-Dokument syntaktisch korrekt ist. Dies ist besonders wichtig bei der Verarbeitung von JSON-Daten aus externen Quellen.
- **Sicherheit:**
    - **Deserialisierung von nicht vertrauenswürdigen Daten:** Seien Sie vorsichtig beim Deserialisieren von JSON-Daten aus unbekannten oder nicht vertrauenswürdigen Quellen. Abhängig von der verwendeten Bibliothek und Programmiersprache könnten Schwachstellen in der Deserialisierungslogik ausgenutzt werden (z. B. Deserialisierungsangriffe).
    - **Sensible Daten:** Vermeiden Sie die Speicherung sensibler oder geheimer Informationen direkt in ungeschützten JSON-Dateien, insbesondere in Client-seitigen Anwendungen. Verwenden Sie geeignete Verschlüsselungsmechanismen, wenn sensible Daten in JSON übertragen oder gespeichert werden müssen.
    - **Cross-Site Scripting (XSS):** Wenn JSON-Daten, die Benutzereingaben enthalten, direkt in Webseiten gerendert werden, ohne vorherige Maskierung oder Validierung, kann dies zu XSS-Schwachstellen führen. Stellen Sie sicher, dass alle externen Daten, die in Webseiten eingebettet werden, entsprechend behandelt werden.







-----

Webtoken 

-----


JSON Web Token (JWT) ist ein offener Standard (RFC 7519), der eine kompakte und in sich geschlossene Möglichkeit zur sicheren Übertragung von Informationen zwischen Parteien als JSON-Objekt definiert. Diese Informationen können als Behauptungen (Claims) über eine Entität (z. B. einen Benutzer) codiert werden. JWTs werden häufig für Authentifizierung und Autorisierung in Webanwendungen und APIs verwendet.

**Aufbau eines JWT:**

Ein JWT besteht aus drei durch Punkte (`.`) getrennten Teilen:

1. **Header (Kopfzeile):**
    
    - Der Header enthält Metadaten über das Token selbst. Er ist ein JSON-Objekt, das typischerweise zwei Schlüssel enthält:
        - `alg`: Gibt den verwendeten Signaturalgorithmus an (z. B. HS256, RS256).
        - `typ`: Gibt den Typ des Tokens an, der in den meisten Fällen `"JWT"` ist.
    - Der Header wird Base64-URL-kodiert.
    - **Beispiel Header:**
        
        JSON
        
        ```
        {
          "alg": "HS256",
          "typ": "JWT"
        }
        ```
        
2. **Payload (Nutzlast):**
    
    - Die Payload enthält die Behauptungen (Claims). Claims sind Aussagen über eine Entität und können in drei Kategorien unterteilt werden:
        - **Registered Claims (Registrierte Ansprüche):** Vordefinierte, optionale Claims, die eine nützliche und interoperable Menge von Metadaten bereitstellen (z. B. `iss` (issuer), `sub` (subject), `aud` (audience), `exp` (expiration time), `nbf` (not before), `iat` (issued at), `jti` (JWT ID)). Die Verwendung dieser Claims wird empfohlen, um die Interoperabilität zu verbessern.
        - **Public Claims (Öffentliche Ansprüche):** Claims, deren Namen im IANA JSON Web Token Registry registriert sind oder als URI definiert wurden, um Namenskollisionen zu vermeiden.
        - **Private Claims (Private Ansprüche):** Benutzerdefinierte Claims, die spezifische Informationen zwischen den beteiligten Parteien austauschen sollen. Bei der Verwendung privater Claims ist Vorsicht geboten, da sie keine Standardisierung aufweisen und es zu Namenskollisionen kommen kann.
    - Die Payload ist ein JSON-Objekt, das diese Claims als Schlüssel-Wert-Paare enthält.
    - Die Payload wird ebenfalls Base64-URL-kodiert.
    - **Beispiel Payload:**
        
        JSON
        
        ```
        {
          "sub": "user123",
          "name": "John Doe",
          "admin": true,
          "iat": 1678886400,
          "exp": 1678890000
        }
        ```
        
3. **Signature (Signatur):**
    
    - Die Signatur dient dazu, die Integrität des Headers und der Payload zu gewährleisten und sicherzustellen, dass das Token nicht manipuliert wurde. Sie wird erzeugt, indem der Base64-URL-kodierte Header, ein Punkt (`.`) und die Base64-URL-kodierte Payload genommen und mit dem im Header angegebenen Algorithmus signiert werden.
    - Der Signaturalgorithmus verwendet entweder einen **Secret (für symmetrische Algorithmen wie HS256)** oder ein **Public/Private-Key-Paar (für asymmetrische Algorithmen wie RS256)**.
        - Bei symmetrischen Algorithmen wird dasselbe Secret sowohl zum Signieren als auch zum Verifizieren des Tokens verwendet. Daher muss das Secret sicher zwischen dem Aussteller und dem Verifizierer geteilt werden.
        - Bei asymmetrischen Algorithmen wird der Private Key zum Signieren des Tokens verwendet, und der entsprechende Public Key wird zum Verifizieren der Signatur verwendet. Der Public Key kann sicher an Dritte weitergegeben werden, ohne die Sicherheit des Private Keys zu gefährden.
    - Die Signatur wird ebenfalls Base64-URL-kodiert.
    - **Beispiel Signatur (hängt vom verwendeten Algorithmus und Secret/Key ab):**
        
        ```
        dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
        ```
        

**Vollständiges JWT:**

Ein vollständiges JWT sieht wie folgt aus:

```
<Base64URL-kodierter Header>.<Base64URL-kodierte Payload>.<Base64URL-kodierte Signatur>
```

**Beispiel eines vollständigen JWT:**

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTY3ODg4NjQwMCwiZXhwIjoxNjc4ODkwMDAwfQ.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

**Wichtige Aspekte bei der Verwendung von JWTs:**

- **Sicherheit des Secrets/Private Keys:** Das Secret (bei symmetrischen Algorithmen) oder der Private Key (bei asymmetrischen Algorithmen) muss sicher verwaltet und vor unbefugtem Zugriff geschützt werden. Ein kompromittiertes Secret/Private Key ermöglicht es Angreifern, gültige JWTs zu erstellen.
- **Auswahl des richtigen Algorithmus:** Die Wahl des Signaturalgorithmus hat erhebliche Auswirkungen auf die Sicherheit. Stärkere Algorithmen wie RS256 werden gegenüber schwächeren oder veralteten Algorithmen bevorzugt.
- **Ablaufzeit (Expiration Time - `exp` Claim):** JWTs sollten eine angemessene, aber begrenzte Gültigkeitsdauer haben, um das Risiko der Verwendung kompromittierter oder abgelaufener Tokens zu minimieren.
- **Überprüfung der Signatur:** Beim Empfang eines JWT muss die Signatur immer mit dem entsprechenden Secret oder Public Key verifiziert werden, um sicherzustellen, dass das Token nicht manipuliert wurde und vom erwarteten Aussteller stammt.
- **Speicherung von JWTs im Client:** Bei der Verwendung von JWTs in Webanwendungen ist die sichere Speicherung im Client wichtig. Häufige Methoden sind Local Storage oder Session Storage, aber diese sind anfällig für Cross-Site Scripting (XSS)-Angriffe. HTTP-only Cookies bieten einen besseren Schutz gegen XSS.
- **Widerruf von JWTs:** Im Gegensatz zu Session-IDs haben JWTs von Natur aus keinen Mechanismus zum Widerruf. Wenn ein Token widerrufen werden muss (z. B. nach dem Abmelden eines Benutzers oder bei einer Sicherheitsverletzung), sind zusätzliche Maßnahmen erforderlich, wie z. B. das Führen einer Blacklist abgelehnter Tokens oder die Verwendung von kurzlebigen Tokens in Kombination mit Refresh Tokens.
- **Vermeidung der Speicherung sensibler Daten in der Payload:** Obwohl die Payload Base64-URL-kodiert ist (und somit nicht direkt verschlüsselt), kann sie leicht dekodiert werden. Daher sollten keine hochsensiblen oder geheimen Informationen direkt in der Payload gespeichert werden. Solche Informationen sollten idealerweise nur serverseitig verwaltet und bei Bedarf über eine sichere Verbindung abgerufen werden.

JWTs bieten eine flexible und standardisierte Methode zur sicheren Übertragung von Informationen. Durch die Beachtung der oben genannten Aspekte können sie effektiv für Authentifizierung und Autorisierung in modernen Anwendungen eingesetzt werden.


[[70b7d0cba49abd90f1d66fc0d5dad808_MD5.jpeg|Open: Pasted image 20250318104641.png]]


![[70b7d0cba49abd90f1d66fc0d5dad808_MD5.jpeg]]





Die **Token-basierte Authentifizierung** ist ein Verfahren, bei dem ein Benutzer nach erfolgreicher Authentifizierung (z.B. durch Eingabe von Benutzername und Passwort) ein eindeutiges **Token** erhält. Dieses Token dient fortan als Nachweis der Identität des Benutzers für nachfolgende Anfragen an den Server. Der Benutzer muss seine Anmeldedaten nicht bei jeder Anfrage erneut senden.

**JSON Web Token (JWT)** ist ein weit verbreiteter Standard für die Erstellung von Zugriffstoken. Es handelt sich um ein kompaktes, URL-sicheres JSON-Objekt, das Informationen zwischen Parteien sicher übertragen kann. Die Sicherheit wird durch eine digitale Signatur gewährleistet.

**Die Funktionsweise der Token-basierten Authentifizierung mit JWT lässt sich in folgenden Schritten zusammenfassen:**

1. **Authentifizierung:**
    
    - Der Benutzer sendet seine Anmeldedaten (z.B. Benutzername und Passwort) an den Server.
    - Der Server überprüft die Anmeldedaten. Sind diese korrekt, erstellt der Server ein JWT.
2. **JWT-Erstellung:** Ein JWT besteht aus drei Teilen, die durch Punkte (`.`) voneinander getrennt sind:
    
    - **Header:** Enthält Metadaten über das Token, typischerweise den verwendeten Algorithmus zum Signieren des Tokens (z.B. HS256) und den Typ des Tokens (immer "JWT"). Der Header wird Base64URL-kodiert.
    - **Payload (Nutzdaten):** Enthält die eigentlichen Informationen (sogenannte "Claims"). Dies können Informationen über den Benutzer (z.B. Benutzer-ID, Name, Rollen) oder andere relevante Daten sein. Es gibt "registrierte Claims" (z.B. `iss` für Aussteller, `sub` für Subjekt, `exp` für Ablaufdatum), "öffentliche Claims" (die frei definiert werden können) und "private Claims" (benutzerdefinierte Claims für die Anwendung). Auch der Payload wird Base64URL-kodiert.
    - **Signature (Signatur):** Wird erzeugt, indem der kodierte Header, der kodierte Payload und ein geheimer Schlüssel (der nur dem Server bekannt ist) mit dem im Header angegebenen Algorithmus (z.B. HMACSHA256) gehasht werden. Die Signatur dient dazu, die Integrität des Tokens zu gewährleisten und sicherzustellen, dass es nach der Ausstellung nicht manipuliert wurde.
3. **Token-Übermittlung:**
    
    - Der Server sendet das erstellte JWT zurück an den Client (z.B. im Antwortkörper einer erfolgreichen Login-Anfrage oder als Cookie).
4. **Autorisierung bei nachfolgenden Anfragen:**
    
    - Wenn der Client auf geschützte Ressourcen zugreifen möchte, sendet er das JWT im `Authorization`-Header der HTTP-Anfrage (üblicherweise mit dem `Bearer`-Schema, z.B. `Authorization: Bearer <JWT>`). Das Token kann auch in Cookies oder im Anfragekörper übermittelt werden, dies sind jedoch weniger verbreitete Ansätze für API-Authentifizierung.
5. **Token-Verifizierung:**
    
    - Der Server empfängt die Anfrage mit dem JWT.
    - Er extrahiert das JWT aus dem Header (oder der entsprechenden Stelle).
    - Der Server verifiziert die Signatur des JWT mit seinem geheimen Schlüssel und dem im Header angegebenen Algorithmus.
    - Ist die Signatur gültig, bedeutet dies, dass das Token nicht manipuliert wurde und vom ausstellenden Server stammt.
    - Der Server überprüft optional weitere Claims im Payload, z.B. das Ablaufdatum (`exp`). Ist das Token abgelaufen, wird die Anfrage abgelehnt.
6. **Zugriff gewähren:**
    
    - Wenn die Signatur gültig ist und alle relevanten Claims (z.B. Ablaufdatum) positiv überprüft wurden, identifiziert der Server den Benutzer anhand der Informationen im Payload des JWT und gewährt Zugriff auf die angeforderte Ressource.

**Vorteile der Token-basierten Authentifizierung mit JWT:**

- **Statelessness (Zustandslosigkeit):** Der Server muss keine Sitzungsinformationen für jeden Benutzer speichern. Das Token selbst enthält alle notwendigen Informationen zur Identifizierung. Dies erleichtert die Skalierbarkeit von Anwendungen.
- **Sicherheit:** Die Signatur schützt vor Manipulationen des Tokens. Die Verwendung eines starken geheimen Schlüssels ist entscheidend.
- **Plattformunabhängigkeit:** JWTs sind ein Standard und können in verschiedenen Umgebungen und mit verschiedenen Technologien verwendet werden.
- **Granulare Zugriffskontrolle:** Der Payload kann spezifische Berechtigungen und Rollen des Benutzers enthalten, die zur Steuerung des Zugriffs auf Ressourcen verwendet werden können.
- **Leichtgewichtigkeit:** JWTs sind relativ klein und können effizient über das Netzwerk übertragen werden.

**Wichtige Aspekte:**

- **Sicherer geheimer Schlüssel:** Der geheime Schlüssel muss sicher auf dem Server gespeichert und niemals an Clients weitergegeben werden.
- **Ablaufdatum (Expiration):** JWTs sollten ein angemessenes Ablaufdatum haben, um das Risiko bei einem kompromittierten Token zu begrenzen.
- **Refresh Tokens:** Um zu vermeiden, dass sich Benutzer nach Ablauf des Tokens erneut vollständig authentifizieren müssen, werden oft "Refresh Tokens" eingesetzt. Diese haben eine längere Gültigkeitsdauer und können verwendet werden, um neue Access Tokens zu erhalten.
- **Sichere Übertragung:** JWTs sollten über sichere Verbindungen (HTTPS) übertragen werden, um Abfangen zu verhindern.

Zusammenfassend ermöglicht die Token-basierte Authentifizierung mit JWT eine sichere und zustandslose Möglichkeit, Benutzer zu authentifizieren und zu autorisieren, ohne dass der Server für jede Sitzung persistenten Speicher benötigt. Das JWT dient als digitaler Ausweis des Benutzers für nachfolgende Anfragen.


