# Begriff: A-Record

## 1. Kerndefinition

Ein **A-Record** (Address Record) ist ein fundamentaler Eintragstyp im Domain Name System (DNS). Seine Hauptaufgabe ist es, einen für Menschen lesbaren Host- oder Domainnamen (z. B. `www.google.de`) in die zugehörige, für Computer verständliche **IPv4-Adresse** (z. B. `142.250.185.227`) zu übersetzen. Dieser Prozess ist die Grundlage für das Surfen im Internet, wie wir es kennen.

## 2. Detaillierte Erläuterung / Funktionsweise

Der A-Record ist der einfachste und am häufigsten verwendete DNS-Eintrag zur Namensauflösung.

### 2.1 Schlüsselkomponenten

Ein typischer A-Record besteht aus:

- **Hostname:** Der Name, der aufgelöst werden soll (z. B. `www` oder `@` für die Hauptdomain).
    
- **TTL (Time To Live):** Ein Wert in Sekunden, der angibt, wie lange der Eintrag von anderen DNS-Servern zwischengespeichert (gecacht) werden darf, bevor er erneut angefragt werden muss.
    
- **Typ:** `A`
    
- **Wert:** Die IPv4-Adresse, auf die der Hostname verweist.
    

### 2.2 Prozess und Zweck

Wenn ein Benutzer eine Webseite in seinem Browser aufruft, geschieht im Hintergrund Folgendes:

1. Der Computer des Benutzers (der DNS-Client) sendet eine Anfrage an einen DNS-Server: "Wie lautet die IP-Adresse für `www.beispiel.com`?"
    
2. Der DNS-Server durchsucht seine Zonendatei nach dem A-Record für `www.beispiel.com`.
    
3. Er findet den Eintrag und antwortet mit der zugehörigen IPv4-Adresse.
    
4. Der Browser des Benutzers verwendet diese IP-Adresse, um eine direkte Verbindung mit dem Webserver aufzubauen und die Seite zu laden.
    

## 3. Einordnung in den Gesamtkontext

Der A-Record ist ein zentraler Baustein des **DNS**. Er arbeitet im Verbund mit anderen wichtigen Record-Typen:

- **AAAA-Record:** Das Pendant zum A-Record, das einen Hostnamen auf eine **IPv6-Adresse** abbildet.
    
- **CNAME-Record:** Erstellt einen Alias, der einen Hostnamen auf einen anderen Hostnamen verweist.
    
- **MX-Record:** Definiert die für eine Domain zuständigen Mailserver.
    
- **NS-Record:** Gibt an, welche Nameserver für eine Domain autoritativ sind.
    

## 4. Sicherheitsaspekte

Die Korrektheit und Integrität von A-Records sind entscheidend für die Sicherheit. Angreifer können versuchen, diese zu manipulieren:

- **DNS-Spoofing / Cache Poisoning:** Ein Angreifer fälscht DNS-Antworten, um einen falschen A-Record in den Cache eines DNS-Servers einzuschleusen. Benutzer, die diesen Server nutzen, werden dann unbemerkt auf eine bösartige Webseite (z. B. eine Phishing-Seite) umgeleitet.
    
- **Schutzmaßnahmen:** Technologien wie **DNSSEC (Domain Name System Security Extensions)** dienen dazu, DNS-Antworten digital zu signieren und so ihre Authentizität und Integrität sicherzustellen.
    

## 5. Praxisbeispiel / Analogie

Ein A-Record funktioniert wie das **Adressbuch in Ihrem Smartphone**. Sie speichern einen Kontakt unter dem Namen **"Pizzeria Roma" (Hostname)**, damit Sie sich nicht die komplexe Telefonnummer **(IPv4-Adresse)** merken müssen. Wenn Sie anrufen möchten, tippen Sie auf den Namen, und Ihr Telefon wählt automatisch die richtige Nummer. Das DNS macht genau dasselbe für das Internet.

## 6. Fazit / Bedeutung für IT-Profis

Ohne A-Records wäre das moderne Internet nicht nutzbar. Sie sind das absolute Fundament der Namensauflösung für IPv4. Jeder IT-Profi, der mit Webseiten, Netzwerkdiensten oder der allgemeinen Fehlerbehebung zu tun hat, muss die Funktion und Konfiguration von A-Records sicher beherrschen.