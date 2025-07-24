
Unter Verschlüsselung versteht man Verfahren und Algorithmen, die Daten mittels digitaler bzw. elektronischer Codes oder Schlüssel inhaltlich in eine nicht lesbare Form umwandeln. Diesen Vorgang bezeichnet man als Verschlüsseln. Gleichzeitig wird dafür gesorgt, dass nur mit dem Wissen eines Schlüssels die geheimen Daten wieder entschlüsselt werden können.  
Anstatt von Verschlüsselung spricht man auch von Chiffrierung, was das gleiche meint.

### Verschlüsselungsalgorithmus

Ein Verschlüsselungsalgorithmus ist eine mathematische Funktion, der man den Klartext und einen Schlüssel übergibt. Die Ausgabe ist ein Geheimtext, der keinen Rückschluss auf den Klartext erlaubt. Nur mit Kenntnis des Schlüssels kann man mit der selben mathematischen Funktion den Geheimtext wieder in den Klartext umwandeln.  
Von einem guten Verschlüsselungsalgorithmus weiß man, dass die Funktionsweise der mathematischen Funktion bekannt sein darf und die Daten nur mit Hilfe des Schlüssels entschlüsselt werden können. Und da das Verfahren bekannt ist, weiß man unter welchen Annahmen das Verfahren funktioniert und kann es überprüfen und auf Schwachstellen testen. Auf diese Weise kann man sicherstellen, dass ein Verschlüsselungsalgorithmus für einen bestimmten Anwendungsfall sicher genug ist.

### Verschlüsselungsverfahren

Ein Verschlüsselungsverfahren besteht aus einem Algorithmus zum Verschlüsseln und Entschlüsseln, sowie Verfahren zum Schlüsselaustausch, Prüfung der Authentizität und Integrität.  
Die bekannten Verschlüsselungsverfahren teilen sich in symmetrische, asymmetrische und hybride Verschlüsselungsverfahren auf. Bei den hybriden Verschlüsselungsverfahren wird ein symmetrisches und asymmetrisches Verschlüsselungsverfahren miteinander kombiniert.

### Symmetrische Verschlüsselung

![Symmetrische Verschlüsselung](https://www.elektronik-kompendium.de/sites/net/bilder/19070411.png)

Die symmetrische Verschlüsselung wird auch als Secret-Key-Verfahren bezeichnet. Es basiert auf einer mathematischen Funktion, die einen Klartext in Abhängigkeit eines Schlüssels (digitaler Code) in einen Geheimtext umwandelt. Beim Entschlüsseln wird der Geheimtext mit dem selben Schlüssel wieder in den Klartext umgewandelt.  
Eine symmetrische Verschlüsselung eignet sich am besten für das Verschlüsseln von Dateien, Verzeichnissen und Laufwerken. Bei der Datenübertragung sind diese Verfahren weniger geeignet, weil man sich um einen sicheren Schlüsselaustausch und deren Verteilung kümmern muss.

- [Symmetrische Kryptografie](https://www.elektronik-kompendium.de/sites/net/1910101.htm)

### Asymmetrische Verschlüsselung

![Asymmetrische Verschlüsselung](https://www.elektronik-kompendium.de/sites/net/bilder/19070412.png)

Die asymmetrische Verschlüsselung wird auch als Public-Key-Verfahren bezeichnet. Der wesentliche Unterschied zur symmetrischen Verschlüsselung ist, dass die asymmetrische Verschlüsselung mit zwei Schlüsseln (unterschiedliche digitale Codes) arbeitet. Einen zum Verschlüsseln und den anderen zum Entschlüsseln. Wobei der Schlüssel zum Verschlüsseln öffentlich ist und der Schlüssel zum Entschlüsseln geheim bleiben muss. Man spricht auch vom Public-Key und vom Private-Key.  
Beide Schlüssel sind ein Schlüsselpaar, dass dem Empfänger einer Nachricht gehört.  
Damit ein Sender einem Empfänger eine verschlüsselte Nachricht schicken kann, muss der Empfänger seinen öffentlichen Schlüssel dem Absender bekannt machen.

- [Asymmetrische Kryptografie](https://www.elektronik-kompendium.de/sites/net/1910111.htm)

### Digitaler bzw. elektronischer Schlüssel

Man spricht von digitalen oder elektronischen Schlüsseln, wobei damit das selbe gemeint ist. Der digitale Schlüssel ist eine Bitfolge, deren Länge in Bit angegeben ist. Alle Verschlüsselungsverfahren benötigen den digitalen Schlüssel als individuellen Bestandteil der Verschlüsselung.  
Von einem guten Verschlüsselungsverfahren erwartet man, dass ein Angreifer ohne Kenntnis des Schlüssels keine Chance hat, an den Klartext zu kommen. Gleichzeitig möchte man, dass der Sender mit Hilfe des Schlüssels schnell verschlüsseln und der Empfänger schnell entschlüsseln kann.

Ein Kriterium für die Sicherheit einer Verschlüsselung ist die Anzahl möglicher Schlüssel und eine möglichst überschaubare Anzahl schwacher Schlüssel. Ein Schlüssel mit einer Länge von 1.024 Bit, also eine Folge von 1.024 Nullen und Einsen, ist sicherer als ein Schlüssel mit nur 64 Bit.  
Selbst wenn man weiß, wie die Verschlüsselung arbeitet, müsste man alle möglichen Schlüssel durchprobieren, um irgendwann den richtigen Schlüssel zu bekommen. Selbst bei einem relativ unsicheren Schlüssel kann bei ausreichender Länge der Sicherheitspuffer groß genug sein. In der Regel gilt, je länger ein Schlüssel ist, desto schwieriger ist es an eine verschlüsselte Information ohne Schlüssel zukommen.

- [Digitale Schlüssel](https://www.elektronik-kompendium.de/sites/net/1909011.htm)

### Stromchiffren und Blockchiffren

Bei Stromchiffren bzw. Stream-Cipher werden die Daten am Stück verschlüsselt. Diese Art und Weise der Verschlüsselung kommt aber nicht so häufig vor. Viel häufiger werden Blockchiffren bei der Verschlüsselung verwendet.  
Bei Blockchiffren bzw. Block-Cipher werden die Daten blockweise zu einer festgelegten Größe einzeln und hintereinander verschlüsselt.

- [Stromchiffren / Stream-Cipher](https://www.elektronik-kompendium.de/sites/net/1911011.htm)
- [Blockchiffren / Block-Cipher](https://www.elektronik-kompendium.de/sites/net/1911041.htm)

### Kryptografische Protokolle / Verschlüsselungsverfahren

Um wirkungsvoll verschlüsseln zu können reicht es nicht aus, einen wirkungsvollen Verschlüsselungsalgorithmus zu haben, sondern man muss auch die verschiedenen Probleme bei der Übertragung von Daten und der Kommunikation lösen. Zu diesem Zweck fasst man verschiedene kryptografische Verfahren zusammen. Daraus entstehen dann standardisierte Verschlüsselungsverfahren bzw. kryptografische Protokolle.

- [Kryptografische Protokolle](https://www.elektronik-kompendium.de/sites/net/0908071.htm)

### Wie sicher ist Verschlüsselung?

Die Geschichte der Kryptografie lehrt uns, dass man neuen Verfahren grundsätzlich nicht trauen darf. Die meisten neuen Algorithmen werden nach kurzer Zeit oder auch etwas später geknackt, das heißt Vereinfachungsmechanismen gefunden. Nur ein paar Algorithmen bleiben übrig, bei denen auch nach Jahren alle Angriffe erfolglos blieben oder theoretischer Natur sind.  
Trotzdem bleibt es schwierig Aussagen zu treffen, welche Verfahren wirklich sicher sind. Irgendwann wird jedes Verfahren gebrochen, die Schlüssel müssen länger gemacht oder die Verfahren verändert werden.

Verschlüsselung ist immer ein Spagat zwischen Sicherheit und Komfort. Absolute Sicherheit gibt es nicht. Man kann nur den Aufwand erhöhen. Mit Verschlüsselung erkauft man sich also nur Zeit, bis jemand einen Weg findet, an den Klartext der verschlüsselten Daten zu kommen.  
Im Gegensatz zu oft verlautbarten Mitteilungen sind Geheimdienste nicht in der Lage jede Verschlüsselung zu knacken. Eine starke Verschlüsselung ist sicher. Voraussetzung ist natürlich, dass die Schlüssel lang genug sind, das zum privaten, geheimen Schlüssel zugehörige Passwort stark genug und der geheime Schlüssel auch geheim ist und bleibt. Und, dass die Verfahren und Implementierungen keine Hintertüren enthalten.  
Generell kann man sagen, das bestätigen Krypto-Experten, dass eine gut und sauber implementierte Verschlüsselung sicher ist. Das gilt natürlich nur unter der Voraussetzung, dass die eingesetzten Implementierungen keine Hintertüren aufweisen.

- [Verschlüsselung prüfen](https://www.elektronik-kompendium.de/sites/net/2005261.htm)
- [Kryptografische Verfahren und ihre Sicherheit (Übersicht)](https://www.elektronik-kompendium.de/sites/net/2006261.htm)
- [Homomorphe Verschlüsselung](https://www.elektronik-kompendium.de/sites/net/2606151.htm)