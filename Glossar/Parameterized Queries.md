Parameterized Queries, auch bekannt als **Prepared Statements**, sind eine fundamentale und essenzielle Technik in der Datenbankprogrammierung, um SQL-Abfragen sicher und effizient auszuführen. Sie lösen ein großes Sicherheitsproblem und verbessern oft die Performance.

**Was sind Parameterized Queries?**

Stellen Sie sich vor, Sie möchten Daten in eine Datenbank einfügen oder abfragen, wobei Teile der Abfrage von Benutzereingaben stammen. Ohne Parameterized Queries würde man die Benutzereingaben direkt in den SQL-Code einfügen, etwa so:

SQL

```
SELECT * FROM users WHERE username = 'Benutzername_aus_Eingabe';
```

Bei Parameterized Queries wird der SQL-Code hingegen so formuliert, dass für die variablen Teile (die Benutzereingaben) **Platzhalter** verwendet werden, anstatt die Werte direkt einzufügen. Die tatsächlichen Werte werden dann **separat** an die Datenbank übergeben.

Ein Beispiel dafür könnte so aussehen (die genaue Syntax hängt von der verwendeten Programmiersprache und Datenbank-API ab):

SQL

```
// SQL-Abfrage mit Platzhalter
String sql = "SELECT * FROM users WHERE username = ?";

// Wert, der vom Benutzer kommt
String username = "Benutzername_aus_Eingabe";

// Abfrage vorbereiten und Parameter binden
PreparedStatement statement = connection.prepareStatement(sql);
statement.setString(1, username); // Der Wert wird dem Platzhalter zugeordnet

// Abfrage ausführen
ResultSet result = statement.executeQuery();
```

**Warum sind Parameterized Queries so wichtig?**

1. **Schutz vor SQL-Injection (Sicherheit):** Dies ist der **wichtigste Grund**. Ohne Parameterized Queries könnte ein Angreifer schädlichen SQL-Code in die Benutzereingabe einschleusen. Wenn diese Eingabe direkt in die Abfrage eingebaut wird, interpretiert die Datenbank den eingeschleusten Code als Teil der SQL-Anweisung und führt ihn aus.
    
    - **Beispiel für SQL-Injection (ohne Parameterized Query):** Wenn der Benutzer als "Benutzername" folgendes eingibt: `' OR 1=1 --` Würde die Abfrage zu: `SELECT * FROM users WHERE username = '' OR 1=1 --'` Das `--` am Ende kommentiert den Rest der Abfrage aus, und `OR 1=1` macht die Bedingung immer wahr. Der Angreifer könnte so Zugriff auf alle Benutzerdaten erhalten, ohne ein Passwort zu kennen.
    
    Mit Parameterized Queries wird die Benutzereingabe **immer als reiner Datenwert** behandelt und niemals als ausführbarer SQL-Code. Die Datenbank kann den Unterschied zwischen Befehl und Daten klar erkennen. Selbst wenn der Benutzer `' OR 1=1 --` eingibt, wird dies einfach als der gesamte Benutzername gespeichert oder gesucht, nicht als Code ausgeführt.
    
2. **Performance-Verbesserung:** Da die Struktur der SQL-Abfrage (mit den Platzhaltern) immer gleich bleibt, kann die Datenbank den **Ausführungsplan (Execution Plan)** dieser Abfrage einmal kompilieren und optimieren. Bei jeder weiteren Ausführung mit anderen Parametern kann dieser vorbereitete Plan einfach wiederverwendet werden. Dies spart der Datenbank die Zeit und Ressourcen, die für das erneute Parsen und Optimieren der Abfrage bei jeder Ausführung anfallen würden, was besonders bei häufig wiederholten Abfragen zu einer deutlichen Leistungssteigerung führt.
    
3. **Bessere Lesbarkeit und Wartbarkeit des Codes:** Die Trennung von SQL-Struktur und Daten macht den Code klarer und leichter verständlich. Es ist offensichtlicher, welche Teile der Abfrage fix sind und welche von Benutzereingaben stammen.
    
4. **Handhabung von Sonderzeichen:** Parameterized Queries kümmern sich automatisch um die korrekte Maskierung von Sonderzeichen (wie z.B. Anführungszeichen) in den übergebenen Daten. Man muss sich also keine Gedanken mehr darüber machen, ob ein Benutzername wie "O'Malley" zu Syntaxfehlern führt.
    

**Wie funktionieren sie technisch?**

1. **Vorbereitung (Prepare):** Die Anwendung sendet die SQL-Abfrage mit den Platzhaltern an die Datenbank. Die Datenbank parst diese Abfrage, erstellt einen Ausführungsplan und speichert ihn unter Umständen zwischen.
2. **Bindung (Bind):** Die Anwendung sendet die tatsächlichen Werte für die Platzhalter separat an die Datenbank.
3. **Ausführung (Execute):** Die Datenbank führt die vorbereitete Abfrage mit den gebundenen Werten aus.

Zusammenfassend sind Parameterized Queries eine Best Practice in der Datenbankprogrammierung, die **unverzichtbar** für die Sicherheit Ihrer Anwendung vor SQL-Injection-Angriffen ist und gleichzeitig die Performance und Wartbarkeit des Codes verbessert.