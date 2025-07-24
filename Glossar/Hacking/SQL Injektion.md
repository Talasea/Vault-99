


**Szenario:**

Wir nehmen an, wir haben eine Webanwendung mit einem Login-Formular gefunden. Wir vermuten, dass diese Webanwendung anfällig für SQL Injection sein könnte und möchten versuchen, uns **ohne korrekte Benutzerdaten** anzumelden, also die Authentifizierung zu "bypassen".

**Benötigte Werkzeuge:**

- **Webbrowser:** Für den Zugriff auf das Login-Formular und das Absenden von Anfragen.
- **Optional: Ein Web-Proxy-Tool (z.B. Burp Suite, OWASP ZAP):** Für fortgeschrittenere Analysen und das Abfangen von HTTP-Anfragen und -Antworten. Für diese grundlegende Anleitung ist es nicht zwingend erforderlich, kann aber hilfreich sein, um den Prozess besser zu verstehen.

**Schritt-für-Schritt-Anleitung für eine SQL Injection Authentication Bypass Attacke:**

**Schritt 1: Ziel-Login-Formular identifizieren**

1. **Suchen Sie nach einem Login-Formular:** Identifizieren Sie in der Webanwendung eine Seite, die ein Login-Formular enthält. Dies ist typischerweise eine Seite mit Feldern für Benutzername und Passwort sowie einem "Login" oder "Anmelden" Button.
2. **Testumgebung:** Stellen Sie sicher, dass Sie diese Schritte **ausschließlich in einer kontrollierten Testumgebung** durchführen. Dies kann eine lokal installierte, absichtlich verwundbare Webanwendung sein (z.B. OWASP Juice Shop, Damn Vulnerable Web App - DVWA) oder eine speziell dafür freigegebene Testumgebung. **Keine Live-Systeme oder Webseiten ohne explizite Erlaubnis testen!**

**Schritt 2: Login-Formular analysieren**

1. **HTML-Quellcode untersuchen:** Öffnen Sie im Webbrowser den Quellcode der Login-Seite (Rechtsklick auf die Seite -> "Seitenquelltext anzeigen" oder ähnlich, je nach Browser).
2. **Formular-Struktur untersuchen:** Suchen Sie im Quellcode nach dem `<form>`-Tag. Achten Sie auf:
    - **`action`-Attribut:** Die URL, an die das Formular gesendet wird, wenn es abgeschickt wird.
    - **`method`-Attribut:** Die HTTP-Methode, die verwendet wird (meistens `POST` oder `GET`).
    - **`<input>`-Felder:** Identifizieren Sie die `<input>`-Felder für Benutzername und Passwort. Achten Sie auf die `name`-Attribute dieser Felder (z.B. `username`, `password`, `login`, etc.). Diese `name`-Attribute sind wichtig, da sie die Parameternamen bestimmen, die beim Absenden des Formulars verwendet werden.
        
        [![Bildmotiv: Browser Developer Tools Inspecting Login Form](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLYczePbaJ3wOZPsUDzQa3l1yFPlyhzVDGRvHZp2FNpRQ31DI7NJhLzCbCJtCW)Wird in einem neuen Fenster geöffnet](https://zapier.com/blog/inspect-element-tutorial/)[![](https://encrypted-tbn3.gstatic.com/favicon-tbn?q=tbn:ANd9GcSQT-00Q3FW6hYohbUt4QeWUQCyjXSDYt3xH9cAe-A9DZWRp6raGMxoTHodHZTrJhDH2EcjQaPQTLUBZlamqQapsAbvwQ)zapier.com](https://zapier.com/blog/inspect-element-tutorial/)
        
        Browser Developer Tools Inspecting Login Form
        
3. **Funktionsweise verstehen (optional):** Versuchen Sie, die grundlegende Funktionsweise des Login-Formulars zu verstehen. Was passiert, wenn Sie korrekte/falsche Benutzerdaten eingeben? Gibt es Fehlermeldungen? Werden Sie auf eine andere Seite weitergeleitet?

**Schritt 3: SQL Injection Payload erstellen**

1. **Grundlegende SQL Injection Payload für Authentication Bypass:** Für eine einfache SQL Injection Authentication Bypass Attacke verwenden wir eine Payload, die eine immer wahre Bedingung in der SQL-Abfrage erzeugt. Ein gängiges Beispiel ist:
    
    SQL
    
    ```
    ' OR '1'='1
    ```
    
    Dieser SQL-Code-Snippet wird in ein Eingabefeld (meist das Benutzername-Feld) eingefügt. Das Ziel ist, dass dieser Code in die SQL-Abfrage der Webanwendung **injiziert** wird und die Logik der Abfrage so verändert, dass sie immer "wahr" zurückliefert, unabhängig von den tatsächlich eingegebenen Benutzerdaten.
    
2. **Erklärung der Payload `' OR '1'='1`:**
    
    - Angenommen, die originale SQL-Abfrage der Webanwendung sieht in etwa so aus:
        
        SQL
        
        ```
        SELECT * FROM users WHERE username = '<BenutzernameEingabe>' AND password = '<PasswortEingabe>'
        ```
        
    - Wenn wir im Benutzername-Feld den Payload `' OR '1'='1` eingeben und ein beliebiges Passwort (oder auch leer lassen), wird die Abfrage (vereinfacht) zu:
        
        SQL
        
        ```
        SELECT * FROM users WHERE username = ''' OR '1'='1' AND password = '<PasswortEingabe>'
        ```
        
    - Die Bedingung `username = ''' OR '1'='1'` wird immer **wahr** sein. Warum?
        
        - `username = ''` (Benutzername ist leer oder ein beliebiger Wert) - kann falsch sein.
        - `'1'='1'` - ist immer **wahr**.
        - `OR` - Wenn eine Seite der `OR`-Verknüpfung wahr ist, ist die gesamte Bedingung wahr.
    - Daher wird die `WHERE`-Klausel immer wahr sein, **unabhängig vom eingegebenen Benutzernamen und Passwort**. Die SQL-Abfrage wird also _alle_ Benutzer aus der `users`-Tabelle zurückgeben. In vielen fehlerhaften Implementierungen prüft die Anwendung dann nur, _ob_ überhaupt Benutzer gefunden wurden, und nicht _ob_ die korrekten Anmeldedaten eingegeben wurden. Wenn also mindestens ein Benutzer gefunden wird (was in der Regel der Fall ist), wird die Authentifizierung **bypasst** und der Zugriff gewährt.
        

**Schritt 4: Payload in das Login-Formular eingeben**

1. **Payload in das Benutzername-Feld eingeben:** In der Login-Seite, geben Sie den SQL Injection Payload `' OR '1'='1` in das Feld für den **Benutzernamen** ein. **Achtung:** Die genaue Payload kann je nach System und Filter variieren. Es gibt auch Varianten wie `admin' OR 1=1--` , `') OR ('1'='1` oder numerische Bypässe, die in anderen Szenarien besser funktionieren könnten. Für dieses Beispiel konzentrieren wir uns auf `' OR '1'='1`.
2. **Beliebiges Passwort eingeben (oder Feld leer lassen):** Im Feld für das **Passwort** können Sie einen beliebigen Wert eingeben oder das Feld leer lassen. Da die Authentifizierung durch den SQL Injection Bypass umgangen wird, ist der Wert im Passwortfeld irrelevant.
3. **Login-Formular absenden:** Klicken Sie auf den "Login", "Anmelden" oder entsprechenden Button, um das Formular abzusenden.

**Schritt 5: Ergebnis beobachten**

1. **Erfolgreicher Bypass (Erwartetes Ergebnis bei Verwundbarkeit):** Wenn die Webanwendung **verwundbar für SQL Injection** ist und der Payload erfolgreich funktioniert, sollten Sie **erfolgreich eingeloggt** werden, **auch ohne korrekte Benutzerdaten**. Dies kann sich äußern durch:
    - Weiterleitung auf eine Seite, die normalerweise nur authentifizierten Benutzern zugänglich ist (z.B. eine Dashboard-Seite, eine Admin-Seite).
    - Änderung des Seiteninhalts, die anzeigt, dass Sie eingeloggt sind (z.B. Anzeige Ihres Benutzernamens, Zugriff auf zusätzliche Funktionen).
    - Keine Fehlermeldung beim Login-Versuch, sondern einfach erfolgreicher Zugriff.
2. **Fehlgeschlagener Bypass (Mögliche Ergebnisse bei Nicht-Verwundbarkeit oder Filterung):** Wenn die Attacke **nicht erfolgreich** ist, können folgende Szenarien eintreten:
    - **Login-Fehlermeldung:** Die Webanwendung zeigt eine Fehlermeldung an, die auf ungültige Anmeldedaten hinweist (z.B. "Falscher Benutzername oder Passwort"). Dies deutet darauf hin, dass die Payload nicht erfolgreich war oder die Anwendung besser gegen SQL Injection geschützt ist.
    - **Allgemeine Fehlerseite oder unerwartetes Verhalten:** In manchen Fällen kann eine fehlerhafte Payload zu einer allgemeinen Fehlerseite der Anwendung führen, oder zu einem unerwarteten Verhalten.
    - **Keine Änderung, Login-Formular bleibt unverändert:** Die Seite bleibt einfach beim Login-Formular, ohne eine Fehlermeldung oder Weiterleitung.

**Schritt 6 (Optional, für fortgeschrittene Analyse): Verwendung eines Web-Proxy-Tools (z.B. Burp Suite)**

1. **Web-Proxy starten und konfigurieren:** Starten Sie ein Web-Proxy-Tool wie Burp Suite und konfigurieren Sie Ihren Browser so, dass der Traffic über den Proxy geleitet wird.
    
    [![Bildmotiv: Burp Suite Proxy Intercepting Request](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS_jaYmtEB5a6uFowPlM3P_ezCULfiiQ0geEaXUkiHCZ2bw0N059npcDn2nu_-k)Wird in einem neuen Fenster geöffnet](https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcSxfJeSK8mtGAwiVGbeKAuDnhRJtTZgNesse2ItF6RV1gsfTdlh0kNdFv6klqXIrZAeVTgjy1HF9hT8BVNMf-FUrxvvfKIflg5c)portswigger.net](https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic)
    
    Burp Suite Proxy Intercepting Request
    
2. **Login-Versuch über Proxy durchführen:** Wiederholen Sie die Schritte 4 und 5, während der Web-Proxy aktiv ist.
3. **HTTP-Anfrage und -Antwort im Proxy untersuchen:** Im Proxy-Tool können Sie nun die HTTP-Anfrage (die vom Browser an den Server gesendet wird) und die HTTP-Antwort (die vom Server zurückkommt) abfangen und detailliert untersuchen.
    - **Anfrage (Request):** Überprüfen Sie die gesendeten Parameter (Benutzername, Passwort) und ob die SQL Injection Payload korrekt übertragen wurde.
    - **Antwort (Response):** Untersuchen Sie den HTTP-Statuscode, die Header und den Body der Antwort. Suchen Sie nach Hinweisen auf Erfolg oder Misserfolg des Login-Versuchs, Fehlermeldungen oder interessante Informationen.
4. **Payloads anpassen und weiter testen:** Mit einem Proxy-Tool können Sie die Anfrage einfach modifizieren und verschiedene SQL Injection Payloads testen, um zu sehen, welche funktionieren oder wie die Anwendung reagiert. Sie können die Anfrage auch wiederholt senden ("Repeater"-Funktion in Burp Suite) und verschiedene Parameter manipulieren.

**Wichtige Hinweise und Sicherheitsvorkehrungen:**

- **Ethische und rechtliche Aspekte (erneute, dringende Warnung):** Das **unbefugte** Ausführen dieser Schritte ist **illegal**. Führen Sie diese Experimente nur in **autorisierten Testumgebungen** durch. Der Zweck dieser Anleitung ist es, die Vorgehensweise bei einer SQL Injection Authentication Bypass Attacke zu demonstrieren und zu verdeutlichen, wie wichtig sichere Programmierung ist.
- **Variationen von SQL Injection:** Die hier gezeigte Payload `' OR '1'='1` ist nur ein sehr einfaches Beispiel. Es gibt viele verschiedene Arten von SQL Injection und zahlreiche komplexere Payloads und Techniken, um Filter zu umgehen und unterschiedliche Datenbanktypen und -konfigurationen auszunutzen.
- **Blind SQL Injection:** In manchen Fällen gibt die Webanwendung keine direkten Fehlermeldungen aus, die auf eine SQL Injection Schwachstelle hinweisen. In solchen Fällen kann man **Blind SQL Injection** Techniken anwenden, bei denen man versucht, Informationen indirekt zu extrahieren, z.B. durch Timing-basierte Angriffe oder durch Analyse des Antwortverhaltens bei unterschiedlichen Eingaben.
- **Moderne Webanwendungen sind oft besser geschützt:** Moderne Webentwicklungsframeworks und Best Practices helfen, SQL Injection Schwachstellen zu vermeiden. Viele Anwendungen setzen **Parameterized Queries (Prepared Statements)** oder **Object-Relational Mappers (ORMs)** ein, die SQL Injection Angriffe erheblich erschweren. Dennoch sind SQL Injection Schwachstellen auch heute noch anzutreffen, insbesondere in älteren oder schlecht gewarteten Anwendungen.

**Zusammenfassend:** Diese Schritt-für-Schritt-Anleitung demonstriert eine grundlegende SQL Injection Authentication Bypass Attacke. Es ist wichtig zu verstehen, dass dies nur eine _Art_ von Bypass-Attacke ist und es viele andere Techniken gibt, um Sicherheitsmechanismen zu umgehen. Sichere Softwareentwicklung, regelmäßige Sicherheitsüberprüfungen und das Verständnis für Angriffsmethoden sind entscheidend, um sich vor solchen Angriffen zu schützen



Beispiel 


**Verwundbarer Code (demonstrativ - NICHT für Produktion verwenden!):**

PHP

```
<?php

$host = 'localhost'; // Ihr Datenbank-Host
$benutzer = 'db_benutzer'; // Ihr Datenbank-Benutzer
$passwort = 'db_passwort'; // Ihr Datenbank-Passwort
$datenbankname = 'meine_datenbank'; // Ihr Datenbank-Name

$verbindung = new mysqli($host, $benutzer, $passwort, $datenbankname);

if ($verbindung->connect_error) {
    die("Verbindung zur Datenbank fehlgeschlagen: " . $verbindung->connect_error);
}

$login_erfolgreich = false;
$fehlermeldung = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $benutzername_eingabe = $_POST['benutzername'];
    $passwort_eingabe = $_POST['passwort'];

    // **VERWUNDBARER CODE - DIREKTE EINBETTUNG VON BENUTZEREINGABEN IN DIE SQL-ABFRAGE**
    $sql = "SELECT * FROM benutzer WHERE benutzername = '" . $benutzername_eingabe . "' AND passwort = '" . $passwort_eingabe . "'";

    $resultat = $verbindung->query($sql);

    if ($resultat->num_rows == 1) {
        $login_erfolgreich = true;
    } else {
        $fehlermeldung = "Ungültiger Benutzername oder Passwort.";
    }
}

$verbindung->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Verwundbares Login-Formular (DEMO - NICHT FÜR PRODUKTION!)</title>
</head>
<body>
    <h1>Verwundbares Login-Formular (DEMO - NICHT FÜR PRODUKTION!)</h1>

    <?php if (!empty($fehlermeldung)) : ?>
        <p style="color: red;"><?php echo $fehlermeldung; ?></p>
    <?php endif; ?>

    <?php if ($login_erfolgreich) : ?>
        <p style="color: green;">Login erfolgreich! Willkommen im System.</p>
        <?php else : ?>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <label for="benutzername">Benutzername:</label><br>
            <input type="text" id="benutzername" name="benutzername"><br><br>

            <label for="passwort">Passwort:</label><br>
            <input type="password" id="passwort" name="passwort"><br><br>

            <input type="submit" value="Login">
        </form>
    <?php endif; ?>

    <p style="font-size: smaller; color: gray;">**DEMO-CODE - NICHT FÜR PRODUKTION VERWENDEN! DIESER CODE IST VERWUNDBAR GEGEN SQL INJECTION.**</p>
</body>
</html>
```

**Erläuterung des verwundbaren Codes:**

1. **Datenbankverbindung:** Der Code stellt eine Verbindung zu einer MySQL-Datenbank her. Sie müssen die Platzhalter `$host`, `$benutzer`, `$passwort` und `$datenbankname` durch Ihre tatsächlichen Datenbankdaten ersetzen, wenn Sie diesen Code lokal testen möchten (aber **bitte nur in einer isolierten Testumgebung!**).
    
2. **Login-Formular:** Ein einfaches HTML-Formular mit Feldern für Benutzername und Passwort wird angezeigt.
    
3. **Verarbeitung des Formulars (POST-Request):** Wenn das Formular abgeschickt wird (`POST`-Request), werden die eingegebenen Werte für Benutzername und Passwort aus `$_POST` abgerufen.
    
4. ****SQL-Abfrage (VERWUNDBAR):** Hier liegt das Kernproblem. Die eingegebenen Werte `$benutzername_eingabe` und `$passwort_eingabe` werden **direkt und ungefiltert** in die SQL-Abfrage eingebettet:
    
    PHP
    
    ```
    $sql = "SELECT * FROM benutzer WHERE benutzername = '" . $benutzername_eingabe . "' AND passwort = '" . $passwort_eingabe . "'";
    ```
    
    **Dies ist extrem gefährlich, da ein Angreifer hier beliebigen SQL-Code in die Abfrage einschleusen kann.**
    
5. **Ausführung der Abfrage:** Die SQL-Abfrage wird ausgeführt.
    
6. **Login-Prüfung:** Wenn die Abfrage genau einen Datensatz zurückliefert (`$resultat->num_rows == 1`), wird der Login als erfolgreich betrachtet. Andernfalls wird eine Fehlermeldung angezeigt.
    

**Wie man diesen Code mit SQL Injection angreift (Demonstration):**

1. **Greifen Sie auf die Seite mit dem verwundbaren Login-Formular zu** in Ihrer Testumgebung.
    
2. **Geben Sie im Feld "Benutzername" folgende Payload ein:**
    
    ```
    ' OR '1'='1
    ```
    
3. **Lassen Sie das Feld "Passwort" leer oder geben Sie einen beliebigen Wert ein.**
    
4. **Klicken Sie auf "Login".**
    

**Erwartetes Ergebnis:**

Sie sollten **erfolgreich eingeloggt** werden, **auch wenn Sie keinen gültigen Benutzernamen und kein gültiges Passwort eingegeben haben.**

**Warum funktioniert der SQL Injection Bypass?**

- Durch die Eingabe von `' OR '1'='1` im Benutzername-Feld wird die SQL-Abfrage manipuliert.
    
- Die originale SQL-Abfrage könnte so aussehen:
    
    SQL
    
    ```
    SELECT * FROM benutzer WHERE benutzername = 'eingegebener_benutzername' AND passwort = 'eingegebenes_passwort'
    ```
    
- Nach der SQL-Injection wird die Abfrage zu (vereinfacht dargestellt):
    
    SQL
    
    ```
    SELECT * FROM benutzer WHERE benutzername = ''' OR '1'='1' AND passwort = 'eingegebenes_passwort'
    ```
    
- Die Bedingung `benutzername = ''' OR '1'='1'` wird **immer wahr** sein. Warum?
    
    - `benutzername = ''` (Benutzername ist leer - kann falsch sein)
    - `'1'='1'` (immer wahr)
    - `OR`: Wenn eine Seite der `OR`-Verknüpfung wahr ist, ist die gesamte Bedingung wahr.
- Dadurch liefert die SQL-Abfrage **alle Benutzerdatensätze** aus der `benutzer`-Tabelle zurück.
    
- Der verwundbare Code prüft nur, ob _mindestens ein_ Ergebnis zurückkommt (`$resultat->num_rows == 1`), und betrachtet den Login dann als erfolgreich. Da die manipulierte Abfrage alle Benutzer liefert, ist die Bedingung erfüllt und der Bypass gelingt.
    

**Wie man diesen Code sicher macht (Verwendung von Prepared Statements):**

Der sicherste Weg, SQL Injection zu verhindern, ist die Verwendung von **Prepared Statements** (auch bekannt als **Parameterized Queries**). Prepared Statements trennen die SQL-Abfragelogik von den Benutzerdaten. Platzhalter werden in der Abfrage verwendet, und die Benutzerdaten werden separat und sicher an die Abfrage übergeben. Die Datenbank behandelt die Benutzerdaten dann immer als Daten und nicht als ausführbaren Code.

Hier ist der **sichere Code** (als Vergleich und zur Demonstration der sicheren Vorgehensweise):

PHP

```
<?php

$host = 'localhost'; // Ihr Datenbank-Host
$benutzer = 'db_benutzer'; // Ihr Datenbank-Benutzer
$passwort = 'db_passwort'; // Ihr Datenbank-Passwort
$datenbankname = 'meine_datenbank'; // Ihr Datenbank-Name

$verbindung = new mysqli($host, $benutzer, $passwort, $datenbankname);

if ($verbindung->connect_error) {
    die("Verbindung zur Datenbank fehlgeschlagen: " . $verbindung->connect_error);
}

$login_erfolgreich = false;
$fehlermeldung = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $benutzername_eingabe = $_POST['benutzername'];
    $passwort_eingabe = $_POST['passwort'];

    // **SICHERER CODE - VERWENDUNG VON PREPARED STATEMENTS**
    $sql = "SELECT * FROM benutzer WHERE benutzername = ? AND passwort = ?";
    $stmt = $verbindung->prepare($sql); // Prepared Statement vorbereiten
    $stmt->bind_param("ss", $benutzername_eingabe, $passwort_eingabe); // Parameter binden (ss = string, string)
    $stmt->execute(); // Abfrage ausführen
    $resultat = $stmt->get_result(); // Ergebnis holen


    if ($resultat->num_rows == 1) {
        $login_erfolgreich = true;
    } else {
        $fehlermeldung = "Ungültiger Benutzername oder Passwort.";
    }
    $stmt->close(); // Statement schließen
}

$verbindung->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Sicheres Login-Formular (DEMO)</title>
</head>
<body>
    <h1>Sicheres Login-Formular (DEMO)</h1>

    <?php if (!empty($fehlermeldung)) : ?>
        <p style="color: red;"><?php echo $fehlermeldung; ?></p>
    <?php endif; ?>

    <?php if ($login_erfolgreich) : ?>
        <p style="color: green;">Login erfolgreich! Willkommen im System.</p>
        <?php else : ?>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <label for="benutzername">Benutzername:</label><br>
            <input type="text" id="benutzername" name="benutzername"><br><br>

            <label for="passwort">Passwort:</label><br>
            <input type="password" id="passwort" name="passwort"><br><br>

            <input type="submit" value="Login">
        </form>
    <?php endif; ?>

    <p style="font-size: smaller; color: gray;">**DEMO-CODE - SICHER GEGEN SQL INJECTION DURCH VERWENDUNG VON PREPARED STATEMENTS.**</p>
</body>
</html>
```

**Erläuterung des sicheren Codes (Prepared Statements):**

1. **Prepared Statement vorbereiten:**
    
    PHP
    
    ```
    $sql = "SELECT * FROM benutzer WHERE benutzername = ? AND passwort = ?";
    $stmt = $verbindung->prepare($sql);
    ```
    
    Hier wird die SQL-Abfrage mit Platzhaltern `?` für die Benutzerdaten vorbereitet. Die Abfragelogik ist nun vom Dateninput getrennt.
    
2. **Parameter binden:**
    
    PHP
    
    ```
    $stmt->bind_param("ss", $benutzername_eingabe, $passwort_eingabe);
    ```
    
    Die Methode `bind_param()` bindet die Variablen `$benutzername_eingabe` und `$passwort_eingabe` an die Platzhalter in der vorbereiteten Abfrage. Das `"ss"` gibt an, dass beide Parameter vom Typ String sind. **Wichtig:** Die Datenbank-API behandelt die gebundenen Parameter nun als _Daten_ und nicht als ausführbaren Code. SQL Injection Payloads werden daher nicht als SQL-Befehle interpretiert, sondern als normale Zeichenketten behandelt.
    
3. **Abfrage ausführen und Ergebnis holen:** Die Abfrage wird wie zuvor ausgeführt und das Ergebnis verarbeitet.
    

**Testen des sicheren Codes:**

Wenn Sie den **sicheren Code** verwenden und versuchen, die gleiche SQL Injection Payload (`' OR '1'='1`) im Benutzername-Feld einzugeben, **wird der Login-Bypass nicht funktionieren.** Die Anwendung sollte Sie **nicht** einloggen, da Prepared Statements die Payload als literal String behandeln und nicht als SQL-Code interpretieren.

**Zusammenfassend:**

Dieser Code demonstriert deutlich das **Risiko der direkten Einbettung von Benutzereingaben in SQL-Abfragen** und zeigt, wie einfach eine SQL-Injection-Authentication-Bypass-Attacke in solchen Fällen ist. Der **sichere Code mit Prepared Statements** verdeutlicht die korrekte und sichere Vorgehensweise, um SQL Injection zu verhindern.

**Wichtige Punkte zur Prävention von SQL Injection (als Zusammenfassung):**

- **Verwenden Sie IMMER Prepared Statements (Parameterized Queries)** oder ORMs (Object-Relational Mappers), die Prepared Statements intern verwenden, um Datenbankabfragen zu erstellen.
- **Vermeiden Sie dynamische SQL-Abfragen**, bei denen Benutzerdaten direkt in SQL-Strings konkateniert werden.
- **Validieren und filtern Sie Benutzereingaben** (als _zusätzliche_ Verteidigungsebene, aber nicht als Ersatz für Prepared Statements). Beachten Sie jedoch, dass Filter leicht umgangen werden können und Prepared Statements die primäre Schutzmaßnahme sind.
- **Wenden Sie das Prinzip der geringsten Privilegien an** für Datenbankbenutzer. Geben Sie Datenbankbenutzern nur die minimal notwendigen Berechtigungen.
- **Führen Sie regelmäßige Sicherheitsaudits und Penetrationstests durch**, um SQL-Injection-Schwachstellen in Ihren Anwendungen zu finden und zu beheben.