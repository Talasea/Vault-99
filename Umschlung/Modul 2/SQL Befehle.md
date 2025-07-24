# https://learnsql.de/blog/die-wichtigsten-sql-befehle/

Die wichtigsten SQL-Befehle

Die wichtigsten SQL-Befehle umfassen verschiedene Kategorien und Funktionen:

- **SELECT**: Wird verwendet, um Daten aus einer oder mehreren Tabellen abzurufen. Es ist der häufigste Befehl in SQL.26
    
- **INSERT INTO**: Erlaubt es, neue Datensätze in eine Tabelle einzufügen.26
    
- **UPDATE**: Wird verwendet, um bestehende Datensätze in einer Tabelle zu aktualisieren.26
    
- **DELETE**: Entfernt Datensätze aus einer Tabelle.26
    
- **CREATE TABLE**: Erstellt eine neue Tabelle in der Datenbank.16
    
- **DROP TABLE**: Löscht eine Tabelle vollständig aus der Datenbank.16
    
- **ALTER**: Ändert die Struktur einer Tabelle, wie zum Beispiel durch Hinzufügen oder Entfernen von Spalten.2
    
- **UNION**: Kombiniert die Ergebnisse mehrerer SELECT-Abfragen.26
    
- **COUNT**: Zählt die Anzahl der Datensätze oder Werte.2
    
- **SUM**: Berechnet die Summe der Werte in einer Spalte.2
    
- **GROUP BY**: Bildet Teilmengen der Daten, um Aggregatfunktionen anzuwenden.6
    
- **WHERE**: Beschränkt die Abfrage auf Datensätze, die ein gegebenes Prädikat erfüllen.16
    
- **ORDER BY**: Sortiert die Ergebnisse einer Abfrage nach bestimmten Spalten.6
    
- **JOIN**: Verknüpft Daten aus mehreren Tabellen.



-------

### SELECT

Die SELECT-Anweisung wird oft als der wichtigste SQL-Befehl bezeichnet. Die meisten Abfragen, die Sie als SQL-Student oder -Spezialist schreiben werden, beginnen mit diesem Befehl.

`SELECT` SELECT wird verwendet, um Daten aus einer Datenbank abzurufen. Die Syntax für die Anweisung `SELECT` lautet wie folgt:

|   |
|---|
|`SELECT` `column1, column2, ...`<br><br>`FROM` `table_name;`|

Hier sind `column1`, `column2`, ... die Namen der Spalten, aus denen Sie Daten abrufen möchten. `table_name` ist der Name der Tabelle, aus der Sie die Daten abrufen wollen.

Sie können auch das Symbol * verwenden, um Daten aus allen Spalten einer Tabelle abzurufen. Wenn Sie zum Beispiel alle Daten aus einer Tabelle namens **`customers`**abrufen möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`SELECT` `*`<br><br>`FROM` `customers;`|

Weitere Beispiele für `SELECT` finden Sie in unserem Artikel [How Do You Write a SELECT Statement in SQL?](https://learnsql.de/blog/wie-schreibt-man-eine-select-anweisung-in-sql/)

Der beste Weg, SQL zu lernen, ist durch Übung. Probiere unseren interaktiven [SQL für Anfänger](https://learnsql.de/kurs/sql-abfragen?itm_source=lsqlBlog&itm_campaign=_default&itm_medium=text&itm_content=course-sql-queries-3)-Kurs aus.

### WHERE

Mit diesem SQL-Befehl können Sie die Daten filtern, die Sie auswählen. Die Klausel `WHERE` folgt auf die FROM-Klausel in einer `SELECT`, `UPDATE` oder `DELETE` Anweisung. Sie gibt eine oder mehrere Bedingungen an, die erfüllt sein müssen, damit die Anweisung ausgeführt werden kann. Sie wird oft von einem oder mehreren [logischen Operatoren oder Vergleichsoperatoren](https://www.w3schools.com/sql/sql_operators.asp) begleitet.

Die grundlegende Syntax einer `WHERE` Klausel lautet:

|   |
|---|
|`SELECT` `column1, column2, ...`<br><br>`FROM` `table_name`<br><br>`WHERE` `condition;`|

In dieser Syntax sind `column1`, `column2`, `…` die Namen der Spalten, in denen die gewünschten Daten gespeichert sind; `table_name` ist der Name der Tabelle, die die Daten enthält. Der Parameter `condition` gibt die Bedingung an, die erfüllt sein muss, damit die Anweisung ausgeführt wird.

Der Parameter condition kann einen oder mehrere logische Operatoren enthalten, z. B. `AND`, `OR` und `NOT`; er kann auch einen oder mehrere Vergleichsoperatoren enthalten, z. B. is equal to (=), does not equal (<>), less than (<), larger than (>), less than or equal to (<=) und greater than or equal to (>=). Sie können auch Funktionen und Unterabfragen verwenden, um komplexere Bedingungen zu erstellen.

Schauen wir uns ein einfaches Beispiel an. Nehmen wir an, Sie haben eine Tabelle mit dem Namen **`employees`** mit den Spalten `id`, `name`, `age` und `department`. Sie möchten die Informationen für alle Mitarbeiter abrufen, die jünger als 30 Jahre sind. Dazu können Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`SELECT` `*`<br><br>`FROM` `employees`<br><br>`WHERE` `age < 30;`|

In diesem Beispiel wird die `WHERE` Klausel verwendet, um die Bedingung festzulegen, dass nur Mitarbeiter mit einem Alter von weniger als 30 Jahren in die Ergebnismenge aufgenommen werden sollen. Das bedeutet, dass das Ergebnis dieser Abfrage alle Zeilen in der Tabelle **`employees`** Tabelle sein, bei denen der Wert in der Spalte Alter kleiner als 30 ist.

Die Beherrschung des WHERE-Befehls ist für jeden, der SQL verwenden möchte, unerlässlich. In unserer [vollständigen Anleitung zum WHERE-Befehl](https://learnsql.de/blog/der-vollstaendige-leitfaden-zur-sql-where-klausel/) finden Sie weitere Informationen und Beispiele.

### INSERT

Die INSERT-Anweisung ist einer der SQL-Befehle, mit denen Sie Daten in Datenbanktabellen ändern können; sie fügt einer Tabelle neue Daten hinzu. Die Syntax für die Anweisung `INSERT` lautet wie folgt:

|   |
|---|
|`INSERT` `INTO` `table_name (column1, column2, ...)`<br><br>`VALUES` `(value1, value2, ...);`|

Hier, **`table_name`** der Name der Tabelle, `column1`, `column2`, ... die Namen der Spalten, zu denen Sie Daten hinzufügen möchten, und `value1`, `value2`, ... die Werte, die Sie zu diesen Spalten hinzufügen möchten.

Wenn Sie zum Beispiel einen neuen Kunden zur Tabelle **`customers`**einen neuen Kunden hinzufügen möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`INSERT` `INTO` `customers (customer_name, customer_email, customer_phone)`<br><br>`VALUES` `(``'John Doe'``,` `'john.doe@example.com'``,` `'123-456-7890'``);`|

Weitere Informationen zu diesem SQL-Befehl finden Sie in dem Artikel [Was ist die INSERT-Anweisung in SQL?](https://learnsql.de/blog/was-ist-die-insert-anweisung-in-sql/)

### UPDATE

Die Anweisung `UPDATE` wird verwendet, um bestehende Daten in einer Datenbank zu ändern. Die Syntax für die Anweisung `UPDATE` lautet wie folgt:

|   |
|---|
|`UPDATE` `table_name`<br><br>`SET` `column1 = value1, column2 = value2, ...`<br><br>`WHERE` `condition;`|

Hier ist `table_name` der Name der Tabelle. `column1` , `column2`, ... sind die Namen der Spalten, die Sie ändern möchten, und `value1`, `value2`, ... sind die neuen Werte, die Sie für diese Spalten festlegen möchten. `condition` schließlich ist das Kriterium für die Auswahl der zu ändernden Zeilen.

Wenn Sie zum Beispiel die E-Mail-Adresse eines Kunden mit dem Namen "John Doe" in der Tabelle **`customers`**aktualisieren möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`UPDATE` `customers`<br><br>`SET` `customer_email =` `'johndoe@example.com'`<br><br>`WHERE` `customer_name =` `'John Doe'``;`|

### DELETE

Die Anweisung `DELETE` wird verwendet, um Daten aus einer Datenbank zu löschen. Die Syntax für die Anweisung `DELETE` lautet wie folgt:

|   |
|---|
|`DELETE` `FROM` `table_name`<br><br>`WHERE` `condition;`|

`table_name` ist der Name der Tabelle, aus der Sie Daten entfernen möchten, und `condition` ist das Kriterium für die Auswahl der zu entfernenden Zeilen.

Wenn Sie zum Beispiel den Kunden mit dem Namen "John Doe" aus der Tabelle **`customers`**löschen möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`DELETE` `FROM` `customers`<br><br>`WHERE` `customer_name =` `'John Doe'``;`|

Es gibt noch zwei weitere SQL-Befehle, die auf den ersten Blick eine ähnliche Aufgabe erfüllen: `TRUNCATE` und `DROP`. In SQL-Einstellungsgesprächen werden Sie oft nach den Unterschieden zwischen diesen Befehlen gefragt. Glücklicherweise haben wir dafür einen Artikel: [TRUNCATE TABLE vs. DELETE vs. DROP TABLE: Entfernen von Tabellen und Daten in SQL](https://learnsql.de/blog/truncate-table-vs-delete-vs-drop-table-entfernen-von-tabellen-und-daten-in-sql/).

[LearnSQL.de](https://learnsql.de/?itm_source=lsqlBlog&itm_campaign=_default&itm_medium=text&itm_content=platform-3) ist eine Online-Plattform, die dir hilft, SQL zu meistern. Sie bietet 10+ interaktive Kurse, die von Anfänger bis Fortgeschritten reichen. Jeder Kurs vermittelt sowohl theoretisches Wissen als auch praktische Übungen, damit du diese neuen Ideen festigen kannst.

### ORDER BY

Die `ORDER BY` Klausel wird verwendet, um die Ergebnismenge einer `SELECT` Anweisung entweder in aufsteigender (A-Z, 1-10) oder absteigender (Z-A, 10-1) Reihenfolge zu sortieren. Die Syntax für die `ORDER BY` Klausel lautet wie folgt:

|   |
|---|
|`SELECT` `column1, column2, ...`<br><br>`FROM` `table_name O`<br><br>`ORDER` `BY` `column_name` `ASC``\|``DESC``;`|

Hier ist `column_name` der Name der Spalte, nach der die Ergebnismenge sortiert werden soll, und `ASC` oder `DESC` gibt an, ob die Sortierreihenfolge aufsteigend oder absteigend sein soll. Wenn die Reihenfolge nicht angegeben wird (weder `ASC` noch `DESC` werden geschrieben), wird die Reihenfolge standardmäßig aufsteigend festgelegt.

Wenn Sie zum Beispiel alle Kunden aus einer Tabelle namens **`customers`** abrufen und sie nach ihren Namen in aufsteigender Reihenfolge sortieren möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`SELECT` `*` `FROM` `customers`<br><br>`ORDER` `BY` `customer_name` `ASC``;`|

Mit diesem SQL-Befehl lassen sich noch weitere Tricks anwenden, z. B. das Sortieren nach mehreren Spalten. Wenn Sie mehr darüber erfahren möchten, lesen Sie unsere [ausführliche Anleitung zu ORDER BY](https://learnsql.de/blog/eine-ausfuehrliche-anleitung-zu-sql-order-by/) .

### GRUPPE BY

Die GROUP BY-Klausel wird verwendet, um Zeilen zu gruppieren, die in einer bestimmten Spalte die gleichen Werte haben. Die Klausel `GROUP BY` wird häufig verwendet, wenn die Aufgabe z. B. lautet: "Finde den Durchschnittspreis pro Produktkategorie". Die Syntax für die `GROUP BY` Klausel lautet wie folgt:

|   |
|---|
|`SELECT` `column1, column2, ...`<br><br>`FROM` `table_name`<br><br>`GROUP` `BY` `column_name;`|

Hier ist `column_name` der Name der Spalte, nach der Sie gruppieren möchten.

Um den Durchschnittspreis pro Produktkategorie aus der Tabelle **`products`**zu ermitteln, verwenden Sie die folgende SQL-Anweisung:

|   |
|---|
|`SELECT` `category,` `AVG``(price)`<br><br>`FROM` `products`<br><br>`GROUP` `BY` `category;`|

Eine ausführliche Erklärung und weitere Beispiele finden Sie in unserem Artikel [Was ist GROUP BY in SQL?](https://learnsql.de/blog/was-ist-group-by-in-sql/)

### JOIN

Die JOIN-Klausel wird verwendet, um Zeilen aus zwei oder mehr Tabellen auf der Grundlage übereinstimmender Werte in einer bestimmten Spalte zu kombinieren. Es gibt verschiedene Arten von `JOIN` -Klauseln in SQL, darunter `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` und `FULL OUTER JOIN`. Die Syntax für die `INNER JOIN` Klausel ist wie folgt:

|   |
|---|
|`SELECT` `column1, column2, ...`<br><br>`FROM` `table1`<br><br>`INNER` `JOIN` `table2`<br><br>`ON` `table1.column_name = table2.column_name;`|

Hier, **`table1`** und **`table2`** die Namen der Tabellen, die Sie verknüpfen wollen, und `column_name` der Name der Spalte, die zur Verknüpfung der beiden Tabellen verwendet wird.

Wenn Sie zum Beispiel alle Bestellungen mit den entsprechenden Kundennamen aus zwei Tabellen namens **`orders`** und **`customers`**abrufen möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`SELECT` `orders.order_id, customers.customer_name`<br><br>`FROM` `orders`<br><br>`INNER` `JOIN` `customers`<br><br>`ON` `orders.customer_id = customers.customer_id;`|

Diese Abfrage sucht in der Spalte `customer_id` in **`orders`** und auf die Spalte **`customer_id`** Spalte in Kunden. Wenn diese beiden Spalten übereinstimmende Werte haben, gibt die Abfrage die Bestell-ID aus der Tabelle **`orders`** Tabelle zusammen mit der `customer_name` aus der **`customers`** Tabelle zurück. Die übereinstimmenden Kunden-IDs bedeuten, dass dieser Kunde diese Bestellung aufgegeben hat.

JOIN ist einer der komplizierteren und vielfältigeren der gängigen SQL-Befehle. Wenn Sie mehr darüber erfahren möchten, lesen Sie unseren Artikel [What Are the Different SQL JOIN Types?](https://learnsql.de/blog/was-sind-die-verschiedenen-sql-join-typen/)

Verbessere deine SQL-JOIN-Fähigkeiten mit unserem speziellen interaktiven Kurs, [SQL-JOINs](https://learnsql.de/kurs/joins?itm_source=lsqlBlog&itm_campaign=_default&itm_medium=text&itm_content=course-joins-3)!

### CREATE

Die Anweisung `CREATE` wird verwendet, um ein neues Datenbankobjekt zu erstellen, z. B. eine Tabelle, eine Ansicht oder einen Index. Die Syntax für die Anweisung `CREATE` variiert je nach Art des Objekts, das Sie erstellen möchten. Hier ist ein Beispiel für die Erstellung einer neuen Tabelle:

|   |
|---|
|`CREATE` `TABLE` `table_name (`<br><br>  `column1 datatype,`<br><br>  `column2 datatype,`<br><br>  `column3 datatype,`<br><br>  `...`<br><br>`);`|

Hier, **`table_name`** der Name der Tabelle, die Sie erstellen möchten, und `column1`, `column2`, `column3`, ... sind die Namen der Spalten. Die Art der Daten, die jede Spalte speichert (Text, ganze Zahlen, Dezimalzahlen usw.), wird durch `datatype` angegeben.

Wenn Sie zum Beispiel eine neue Tabelle erstellen möchten **`products`** mit Spalten für die Produkt-ID, den Produktnamen und den Preis erstellen möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`CREATE` `TABLE` `products (`<br><br>  `product_id` `INT` `PRIMARY` `KEY``,`<br><br>  `product_name` `VARCHAR``(50),`<br><br>  `price` `DECIMAL``(10, 2)`<br><br>`);`|

Weitere Informationen über `PRIMARY KEY` und andere Aspekte der Tabellenerstellung finden Sie in unserem Artikel [How to Create Your First Table in SQL](https://learnsql.com/blog/how-to-create-table-sql/).

### ALTER

Die ALTER-Anweisung wird verwendet, um die Struktur eines bestehenden Datenbankobjekts, wie z. B. einer Tabelle oder eines [Views](https://learnsql.com/blog/sql-view/), zu ändern. Die Syntax für die `ALTER` Anweisung variiert je nach Art des Objekts, das Sie ändern möchten. Hier ein Beispiel für das [Hinzufügen einer neuen Spalte zu einer bestehenden Tabelle](https://learnsql.com/cookbook/how-to-add-a-column-in-sql/):

|   |
|---|
|`ALTER` `TABLE` `table_name`<br><br>`ADD` `column_name datatype;`|

Hier, **`table_name`** ist der Name der Tabelle, die Sie ändern wollen, **`column_name`** ist der Name der neuen Spalte, und `datatype` ist der Datentyp der neuen Spalte.

Wenn Sie zum Beispiel eine neue Spalte mit dem Namen `description` zu einer bestehenden Tabelle mit dem Namen **`products`**eine neue Spalte mit dem Namen hinzufügen möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`ALTER` `TABLE` `products`<br><br>`ADD` `description` `VARCHAR``(100);`|

Ein weiteres Beispiel für die Verwendung der Anweisung `ALTER` ist die Änderung des Datentyps oder der Größe einer vorhandenen Spalte. Wenn Sie zum Beispiel den Datentyp der Spalte `price` in der Tabelle **`products`** Tabelle von `DECIMAL(10,2)` auf `DECIMAL(12,2)` ändern möchten, würden Sie die folgende SQL-Anweisung verwenden:

|   |
|---|
|`ALTER` `TABLE` `products`<br><br>`ALTER` `COLUMN` `price` `DECIMAL``(12,2);`|