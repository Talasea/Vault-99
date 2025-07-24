
**Kapitel 1: Die Grundlagen – Was ist die Konsole und warum nutzen?**

- **Was ist die Konsole (Terminal)?** Die Konsole ist eine textbasierte Schnittstelle zu deinem Betriebssystem. Anstatt mit grafischen Symbolen und Fenstern zu interagieren, gibst du Befehle in Textform ein.
- **Warum die Konsole nutzen?**
    - **Effizienz:** Viele Aufgaben lassen sich schneller und präziser über die Konsole erledigen.
    - **Flexibilität:** Die Konsole bietet Zugriff auf fortgeschrittene Funktionen und Einstellungen.
    - **Automatisierung:** Wiederkehrende Aufgaben können mit Skripten automatisiert werden.
    - **Fehlerbehebung:** Bei Problemen liefert die Konsole oft detailliertere Informationen.
    - **Server-Management:** Für viele IT-Aufgaben ist die Konsole unerlässlich.
- **Wie öffne ich die Konsole in Parrot OS?** In den meisten Linux-Distributionen, einschließlich Parrot OS, kannst du die Konsole öffnen, indem du die Tastenkombination `Strg + Alt + T` drückst. Du findest sie auch oft im Anwendungsmenü unter "Terminal" oder "Systemwerkzeuge".

**Kapitel 2: Erste Schritte – Navigation im Dateisystem**

In der Konsole navigierst du durch dein Dateisystem, ähnlich wie im Windows Explorer. Hier sind die wichtigsten Befehle:

- `pwd` (print working directory): Zeigt dir den aktuellen Ordner (das "aktuelle Arbeitsverzeichnis") an, in dem du dich gerade befindest.
- `ls` (list): Zeigt eine Liste der Dateien und Ordner im aktuellen Verzeichnis an.
    - `ls -l`: Zeigt eine detailliertere Liste mit Informationen wie Dateigröße, Berechtigungen und Änderungsdatum.
    - `ls -a`: Zeigt auch versteckte Dateien und Ordner an (beginnen mit einem Punkt).
    - `ls -h`: Zeigt Dateigrößen in einem für Menschen lesbaren Format (z.B. 1K, 234M, 2G).
    - Du kannst Optionen kombinieren, z.B. `ls -alh`.
- `cd` (change directory): Ändert das aktuelle Verzeichnis.
    - `cd <Verzeichnisname>`: Wechselt in den angegebenen Ordner. Beispiel: `cd Dokumente`
    - `cd ..`: Wechselt in den übergeordneten Ordner.
    - `cd ~`: Wechselt in dein Home-Verzeichnis.
    - `cd /`: Wechselt in das Wurzelverzeichnis (der oberste Ordner des Systems).

**Kapitel 3: Umgang mit Dateien und Ordnern**

Hier sind Befehle, um Dateien und Ordner zu erstellen, zu bearbeiten und zu verwalten:

- `mkdir <Verzeichnisname>` (make directory): Erstellt einen neuen Ordner. Beispiel: `mkdir Projekte`
- `rmdir <Verzeichnisname>` (remove directory): Löscht einen leeren Ordner.
- `rm <Dateiname>` (remove): Löscht eine Datei.
    - `rm -r <Verzeichnisname>`: Löscht einen Ordner und alle darin enthaltenen Dateien und Unterordner (Vorsicht!).
    - `rm -f <Dateiname>`: Erzwingt das Löschen ohne Nachfrage (Vorsicht!).
    - `rm -rf <Verzeichnisname>`: Erzwingt das rekursive Löschen ohne Nachfrage (Äußerste Vorsicht!).
- `touch <Dateiname>`: Erstellt eine leere Datei oder aktualisiert den Zeitstempel einer existierenden Datei.
- `cp <Quelle> <Ziel>` (copy): Kopiert eine Datei oder einen Ordner.
    - `cp datei.txt kopie.txt`: Kopiert `datei.txt` nach `kopie.txt` im selben Verzeichnis.
    - `cp datei.txt /home/benutzer/Dokumente/`: Kopiert `datei.txt` in den Ordner `Dokumente`.
    - `cp -r <Ordner> <Ziel>`: Kopiert einen Ordner rekursiv (mit allen Inhalten).
- `mv <Quelle> <Ziel>` (move): Verschiebt eine Datei oder einen Ordner oder benennt ihn um.
    - `mv datei.txt neuer_name.txt`: Benennt `datei.txt` in `neuer_name.txt` um.
    - `mv datei.txt /home/benutzer/Downloads/`: Verschiebt `datei.txt` in den Ordner `Downloads`.

**Kapitel 4: Software installieren und verwalten (APT)**

Parrot OS basiert auf Debian, daher verwendest du den Paketmanager `apt` (Advanced Package Tool).

- `sudo apt update`: Aktualisiert die Liste der verfügbaren Softwarepakete aus den konfigurierten Quellen. Dies solltest du regelmäßig tun. `sudo` erlaubt dir, Befehle mit Administratorrechten auszuführen (du wirst nach deinem Passwort gefragt).
- `sudo apt upgrade`: Führt ein Upgrade aller installierten Pakete auf die neuesten verfügbaren Versionen durch.
- `sudo apt install <Paketname>`: Installiert ein neues Softwarepaket. Beispiel: `sudo apt install firefox`
- `sudo apt remove <Paketname>`: Deinstalliert ein Softwarepaket, behält aber Konfigurationsdateien.
- `sudo apt purge <Paketname>`: Deinstalliert ein Softwarepaket und entfernt auch die zugehörigen Konfigurationsdateien.
- `sudo apt search <Suchbegriff>`: Sucht nach Softwarepaketen, die den angegebenen Suchbegriff enthalten.

**Kapitel 5: Wichtige Befehle für den Alltag**

- `cat <Dateiname>`: Zeigt den Inhalt einer Textdatei in der Konsole an.
- `less <Dateiname>`: Zeigt den Inhalt einer Textdatei seitenweise an. Du kannst mit den Pfeiltasten navigieren und mit `q` beenden.
- `head <Dateiname>`: Zeigt die ersten paar Zeilen einer Datei an (standardmäßig 10).
    - `head -n <Anzahl> <Dateiname>`: Zeigt die ersten `<Anzahl>` Zeilen an.
- `tail <Dateiname>`: Zeigt die letzten paar Zeilen einer Datei an (standardmäßig 10). Nützlich für Logdateien.
    - `tail -n <Anzahl> <Dateiname>`: Zeigt die letzten `<Anzahl>` Zeilen an.
    - `tail -f <Dateiname>`: Zeigt die letzten Zeilen an und verfolgt die Datei weiter, d.h., neue Zeilen, die zur Datei hinzugefügt werden, werden in Echtzeit angezeigt.
- `grep <Suchmuster> <Dateiname>`: Sucht in einer Datei nach Zeilen, die das angegebene Suchmuster enthalten.
    - `grep "fehler" logdatei.txt`: Findet alle Zeilen in `logdatei.txt`, die das Wort "fehler" enthalten.
- `history`: Zeigt eine Liste der zuvor eingegebenen Befehle an. Du kannst `!n` verwenden, um den n-ten Befehl in der Liste auszuführen (z.B. `!5`). Mit den Pfeiltasten nach oben kannst du durch deine vorherigen Befehle blättern.
- `man <Befehl>`: Zeigt die "Manual Page" (Handbuchseite) für den angegebenen Befehl an. Sehr hilfreich, um mehr über die Optionen und die Verwendung eines Befehls zu erfahren. Beispiel: `man ls`. Du navigierst mit den Pfeiltasten und beendest mit `q`.
- `top` oder `htop`: Zeigt eine dynamische Übersicht der Systemauslastung und der laufenden Prozesse an. `htop` ist oft benutzerfreundlicher. Beende mit `q`.
- `ps aux`: Zeigt eine Liste aller laufenden Prozesse an.
- `kill <Prozess-ID>`: Beendet einen laufenden Prozess. Du musst die Prozess-ID (PID) aus der Ausgabe von `top`, `htop` oder `ps aux` kennen.
- `df -h`: Zeigt den Festplattenverbrauch an (in einem für Menschen lesbaren Format).
- `du -h`: Zeigt die Größe von Dateien und Verzeichnissen an (in einem für Menschen lesbaren Format).
    - `du -sh <Verzeichnis>`: Zeigt die Gesamtgröße eines Verzeichnisses an.
- `ip a` oder `ifconfig`: Zeigt Informationen über deine Netzwerkschnittstellen an (z.B. IP-Adresse).

**Kapitel 6: Tipps für den Alltag**

- **Tab-Vervollständigung:** Wenn du in der Konsole einen Befehl oder einen Dateinamen eingibst, drücke die Tab-Taste. Die Konsole versucht, den Rest zu vervollständigen. Wenn es mehrere Möglichkeiten gibt, drücke zweimal Tab, um eine Liste der Optionen anzuzeigen.
- **Pfeiltasten:** Nutze die Pfeiltasten nach oben und unten, um durch deine vorherigen Befehle zu blättern.
- **Copy & Paste:** In den meisten Terminal-Emulatoren kannst du Text mit `Strg + Shift + C` (Kopieren) und `Strg + Shift + V` (Einfügen) verwenden.
- **Experimentiere!** Die beste Art, die Konsole zu lernen, ist durch Ausprobieren. Sei aber vorsichtig mit Befehlen wie `rm -rf` und führe sie nur aus, wenn du genau weißt, was sie tun.
- **Suche im Internet:** Wenn du nicht weißt, wie ein bestimmter Befehl funktioniert oder wie du eine bestimmte Aufgabe in der Konsole erledigen kannst, suche einfach im Internet. Es gibt unzählige Ressourcen und Foren, die dir weiterhelfen können.

**Kapitel 7: Nächste Schritte**

Dies ist nur ein kleiner Einblick in die Welt der Linux-Konsole. Es gibt noch viel mehr zu entdecken! Hier sind einige Ideen für deine nächsten Schritte:

- **Lerne mehr über Shell-Skripting:** Damit kannst du mehrere Befehle in einer Datei zusammenfassen und automatisieren.
- **Erforsche fortgeschrittenere Befehle:** Es gibt viele nützliche Befehle für spezielle Aufgaben.
- **Passe deine Shell an:** Du kannst das Aussehen und Verhalten deiner Konsole anpassen.
- **Nutze die Konsole für alltägliche Aufgaben:** Versuche, so viele Aufgaben wie möglich über die Konsole zu erledigen, z.B. Dateien verwalten, Software installieren oder Systeminformationen abrufen.


## Neues Kapitel 8: Textmanipulation – Kopieren und Einfügen in Dateien

Dieses Kapitel konzentriert sich auf Befehle, mit denen du Text aus einer Datei kopieren und in eine andere Datei an einer bestimmten Stelle einfügen kannst.

**1.1 Text aus einer Datei kopieren**

- **`cat` Befehl:** Der einfachste Weg, den Inhalt einer Datei anzuzeigen und somit zum Kopieren (manuell oder über Pipes) bereitzustellen.
    
    Bash
    
    ```
    cat quelldatei.txt
    ```
    
    _Erklärung:_ Dieser Befehl gibt den gesamten Inhalt der Datei `quelldatei.txt` auf der Konsole aus. Du kannst die Ausgabe dann manuell kopieren oder mit Pipes weiterverarbeiten.
    
- **`sed` Befehl (Selektive Ausgabe):** Nützlich, um nur bestimmte Zeilen oder Textmuster aus einer Datei zu kopieren.
    
    Bash
    
    ```
    # Die Zeilen 5 bis 10 ausgeben
    sed -n '5,10p' quelldatei.txt
    
    # Alle Zeilen ausgeben, die das Wort "wichtig" enthalten
    sed -n '/wichtig/p' quelldatei.txt
    ```
    
    _Erklärung:_ * `-n`: Unterdrückt die Standardausgabe. * `'5,10p'`: Gibt die Zeilen 5 bis 10 aus (`p` steht für print). * `'/wichtig/p'`: Gibt alle Zeilen aus, die das Muster "wichtig" enthalten.
    
- **`awk` Befehl (Spaltenweise Verarbeitung):** Ideal, um bestimmte Spalten oder Felder aus einer Datei zu extrahieren.
    
    Bash
    
    ```
    # Die erste Spalte einer durch Leerzeichen getrennten Datei ausgeben
    awk '{print $1}' quelldatei.txt
    
    # Die zweite und dritte Spalte einer durch Komma getrennten Datei ausgeben
    awk -F',' '{print $2, $3}' quelldatei.csv
    ```
    
    _Erklärung:_ * `'{print $1}'`: Gibt die erste Spalte aus. `$2`, `$3` usw. stehen für die folgenden Spalten. * `-F','`: Setzt das Feldtrennzeichen auf Komma.
    

**1.2 Text in eine andere Datei an einer bestimmten Zeile einfügen**

Der `sed` Befehl ist hier besonders mächtig.

- **Text vor einer bestimmten Zeile einfügen:**
    
    Bash
    
    ```
    # Den Inhalt von 'einzufuegender_text.txt' vor Zeile 5 in 'zieldatei.txt' einfügen
    sed -i '5 r einzufuegender_text.txt' zieldatei.txt
    
    # Einen festen Text vor Zeile 10 in 'zieldatei.txt' einfügen
    sed -i '10 i Neuer Text, der eingefügt wird' zieldatei.txt
    ```
    
    _Erklärung:_ * `-i`: Bearbeitet die Datei direkt (in-place). Sei vorsichtig bei der Verwendung! Du kannst auch `-i.bak` verwenden, um eine Sicherungskopie zu erstellen. * `'5 r einzufuegender_text.txt'`: Liest den Inhalt von `einzufuegender_text.txt` und fügt ihn vor Zeile 5 in `zieldatei.txt` ein (`r` steht für read). * `'10 i Neuer Text, der eingefügt wird'`: Fügt den angegebenen Text vor Zeile 10 ein (`i` steht für insert).
    
- **Text nach einer bestimmten Zeile einfügen:**
    
    Bash
    
    ```
    # Den Inhalt von 'einzufuegender_text.txt' nach Zeile 8 in 'zieldatei.txt' einfügen
    sed -i '8 a einzufuegender_text.txt' zieldatei.txt
    
    # Einen festen Text nach Zeile 12 in 'zieldatei.txt' einfügen
    sed -i '12 a Noch mehr Text, der angehängt wird' zieldatei.txt
    ```
    
    _Erklärung:_ * `'8 a einzufuegender_text.txt'`: Liest den Inhalt von `einzufuegender_text.txt` und fügt ihn nach Zeile 8 in `zieldatei.txt` ein (`a` steht für append).
    

**1.3 Kombinieren von Befehlen (Piping)**

Du kannst die Ausgabe eines Befehls direkt in einen anderen leiten, um komplexere Aufgaben zu erledigen.

Bash

```
# Die Zeilen 3 bis 7 aus 'quelldatei.txt' kopieren und vor Zeile 2 in 'zieldatei.txt' einfügen
sed -n '3,7p' quelldatei.txt | sed -i '2 r /dev/stdin' zieldatei.txt
```

_Erklärung:_ * `sed -n '3,7p' quelldatei.txt`: Gibt die Zeilen 3 bis 7 von `quelldatei.txt` aus. * `|`: Leitet die Ausgabe des ersten `sed`-Befehls an den zweiten `sed`-Befehl weiter. * `sed -i '2 r /dev/stdin' zieldatei.txt`: Liest die Eingabe vom Standardeingabestrom (`/dev/stdin`, was die Ausgabe des vorherigen Befehls ist) und fügt sie vor Zeile 2 in `zieldatei.txt` ein.

## Neues Kapitel 2: Indexformen und Dateisystemsuche

Dieses Kapitel behandelt Befehle, die dir helfen, Dateien und Verzeichnisse effizient zu finden und zu verwalten.

**2.1 Der `locate` Befehl (Indexbasierte Suche)**

- **Grundlegende Suche:**
    
    Bash
    
    ```
    locate dateiname.txt
    ```
    
    _Erklärung:_ Durchsucht eine Datenbank (den Index) nach Dateien oder Verzeichnissen, deren Namen `dateiname.txt` enthalten.
    
- **Reguläre Ausdrücke:**
    
    Bash
    
    ```
    locate "*.jpg"
    locate "dokument*"
    ```
    
    _Erklärung:_ Verwendet Platzhalter (`*`) für flexiblere Suchmuster.
    
- **Aktualisieren der Datenbank:**
    
    Bash
    
    ```
    sudo updatedb
    ```
    
    _Erklärung:_ Aktualisiert die `locate`-Datenbank. Dies ist notwendig, wenn du kürzlich Dateien erstellt oder verschoben hast und `locate` diese nicht findet.
    

**2.2 Der `find` Befehl (Echtzeit-Suche)**

Der `find` Befehl ist mächtiger, da er das Dateisystem in Echtzeit durchsucht.

- **Suche nach Dateinamen:**
    
    Bash
    
    ```
    find /pfad/zum/verzeichnis -name "gesuchter_name.txt"
    find . -name "*.pdf"
    ```
    
    _Erklärung:_ * `/pfad/zum/verzeichnis`: Der Startpunkt der Suche. Verwende `.` für das aktuelle Verzeichnis. * `-name`: Sucht nach Dateien oder Verzeichnissen mit dem exakten Namen. * `-iname`: Wie `-name`, aber ignoriert die Groß-/Kleinschreibung.
    
- **Suche nach Dateityp:**
    
    Bash
    
    ```
    find . -type f  # Nur Dateien finden
    find / -type d  # Nur Verzeichnisse finden
    find . -type l  # Nur symbolische Links finden
    ```
    
    _Erklärung:_ `-type` ermöglicht die Suche nach bestimmten Dateitypen (`f` für Datei, `d` für Verzeichnis, `l` für symbolischen Link usw.).
    
- **Suche basierend auf Änderungszeiten:**
    
    Bash
    
    ```
    find . -mtime -7  # Dateien, die in den letzten 7 Tagen geändert wurden
    find . -mtime +30 # Dateien, die älter als 30 Tage sind
    find . -atime -1  # Dateien, auf die in den letzten 24 Stunden zugegriffen wurde
    ```
    
    _Erklärung:_ * `-mtime`: Sucht nach Dateien basierend auf der letzten Änderungszeit (in Tagen). * `-atime`: Sucht nach Dateien basierend auf der letzten Zugriffszeit (in Tagen). * Ein Minuszeichen (`-`) bedeutet "weniger als", ein Pluszeichen (`+`) bedeutet "mehr als".
    
- **Ausführen von Befehlen auf gefundene Dateien:**
    
    Bash
    
    ```
    find . -name "*.tmp" -exec rm {} \;
    find . -type f -name "*.txt" -exec chmod 644 {} \;
    ```
    
    _Erklärung:_ * `-exec befehl {} \;`: Führt den angegebenen `befehl` auf jede gefundene Datei aus. `{}` wird durch den Pfad der gefundenen Datei ersetzt, und `\;` beendet den Befehl.
    

## Neues Kapitel 8.1: Dateigröße und Änderungsdaten im Blick

Dieses Kapitel zeigt dir, wie du Dateien nach ihrer Größe filtern und Informationen über ihre Änderungsdaten anzeigen kannst.

**3.1 Anzeigen von Dateien mit bestimmten Größen**

- **`ls` Befehl mit Größenangaben:**
    
    Bash
    
    ```
    ls -lh
    ```
    
    _Erklärung:_ Zeigt eine detaillierte Liste der Dateien und Verzeichnisse im aktuellen Verzeichnis an. Die Option `-h` stellt die Größen in einem für Menschen lesbaren Format (z.B. 1K, 234M, 2G) dar.
    
- **Filtern mit `find` nach Größe:**
    
    Bash
    
    ```
    find . -size +1G  # Dateien finden, die größer als 1 Gigabyte sind
    find /var/log -size -10M # Dateien im Verzeichnis /var/log finden, die kleiner als 10 Megabyte sind
    find . -size 50M  # Dateien finden, die exakt 50 Megabyte groß sind
    ```
    
    _Erklärung:_ * `-size`: Sucht nach Dateien basierend auf ihrer Größe. * `+`: Größer als. * `-`: Kleiner als. * Ohne Vorzeichen: Exakt diese Größe. * Mögliche Einheiten sind: `c` (Bytes), `k` (Kilobytes), `M` (Megabytes), `G` (Gigabytes).
    
- **Kombinieren von `ls` und anderen Befehlen zur Größenfilterung:**
    
    Bash
    
    ```
    ls -l | awk '$5 > 1000000 {print $9}' # Dateien auflisten, die größer als 1MB sind (Größe in Bytes)
    ```
    
    _Erklärung:_ * `ls -l`: Gibt die detaillierte Liste aus. * `| awk ...`: Leitet die Ausgabe an `awk` weiter. * `'$5 > 1000000 {print $9}'`: `awk` verarbeitet jede Zeile. `$5` repräsentiert die Spalte mit der Dateigröße (in Bytes), `$9` die Spalte mit dem Dateinamen. Diese Anweisung gibt nur die Dateinamen aus, deren Größe größer als 1.000.000 Bytes ist.
    

**3.2 Anzeigen und Filtern nach Dateiänderungszeiten**

- **`ls` Befehl mit detaillierten Zeitangaben:**
    
    Bash
    
    ```
    ls -l --full-time
    ls -lt  # Nach Änderungszeit sortieren (neueste zuerst)
    ls -ltr # Nach Änderungszeit sortieren (älteste zuerst)
    ```
    
    _Erklärung:_ * `--full-time`: Zeigt die Änderungszeit mit voller Genauigkeit an. * `-t`: Sortiert die Ausgabe nach der Änderungszeit. * `-r`: Kehrt die Sortierreihenfolge um.
    
- **Filtern mit `find` nach Änderungsdatum:**
    
    Bash
    
    ```
    find . -mtime 0  # Dateien, die heute geändert wurden
    find . -mtime -3 # Dateien, die in den letzten 3 Tagen geändert wurden
    find /var/log -mtime +90 # Dateien im Verzeichnis /var/log, die älter als 90 Tage sind
    ```
    
    _Erklärung:_ (Siehe Erklärung im Kapitel 2.2 zum `find` Befehl)
    
- **Filtern nach bestimmten Zeiträumen mit `find`:**
    
    Bash
    
    ```
    find . -newermt "2025-03-20" ! -newermt "2025-03-22" # Dateien, die zwischen dem 20. und 22. März 2025 geändert wurden
    ```
    
    _Erklärung:_ * `-newermt`: Sucht nach Dateien, die neuer als die angegebene Zeit sind. * `! -newermt`: Negiert die Bedingung, sucht also nach Dateien, die nicht neuer als die angegebene Zeit sind.



## Kapitel 9: Penetration Testing und Sicherheit – Wichtige Befehle unter Parrot OS

Dieses Kapitel führt dich in einige der wichtigsten Konsolenbefehle und Tools ein, die in Parrot OS für Penetrationstests und Sicherheitsaudits verwendet werden. Parrot OS ist speziell auf diese Bereiche ausgerichtet und bietet eine Vielzahl vorinstallierter Werkzeuge.

**9.1 Informationsbeschaffung (Information Gathering)**

Der erste Schritt in jedem Penetrationstest ist das Sammeln von Informationen über das Zielsystem oder Netzwerk.

- **Netzwerkinformationen:**
    
    - `ip a`: Zeigt die Netzwerkschnittstellen und deren Konfiguration (IP-Adressen, MAC-Adressen etc.).
    - `ifconfig`: Ein älteres, aber immer noch nützliches Tool zur Anzeige und Konfiguration von Netzwerkschnittstellen.
    - `netstat -tulnp`: Zeigt offene Netzwerkverbindungen, Listening-Ports und zugehörige Prozesse.
    - `ss -tulnp`: Ein modernerer Nachfolger von `netstat` mit ähnlicher Funktionalität.
    - `route -n`: Zeigt die Routing-Tabelle des Systems.
    - `arp -a`: Zeigt den ARP-Cache (Zuordnung von IP- zu MAC-Adressen im lokalen Netzwerk).
    - `ping <ziel-ip-oder-hostname>`: Überprüft die Erreichbarkeit eines Hosts.
    - `traceroute <ziel-ip-oder-hostname>`: Zeigt den Pfad, den Pakete zu einem Ziel nehmen.
- **DNS-Informationen:**
    
    - `dig <ziel-hostname> [type]`: Ein mächtiges Tool zur Abfrage von DNS-Servern (z.B. `dig example.com A`, `dig example.com MX`).
    - `nslookup <ziel-hostname> [server]`: Ein einfacheres Tool zur DNS-Abfrage.
- **Host- und Service-Erkennung:**
    
    - `nmap <ziel-ip-oder-netzwerk>`: Ein vielseitiges Tool für Portscanning, Service-Erkennung und Betriebssystemerkennung.
        - `nmap -sS <ziel-ip>`: SYN-Scan (Stealth-Scan).
        - `nmap -sV <ziel-ip>`: Erkennt die Versionen der laufenden Dienste.
        - `nmap -O <ziel-ip>`: Versucht, das Betriebssystem zu erkennen.
        - `nmap -p <port1>,<port2>,... <ziel-ip>`: Scannt spezifische Ports.
        - `nmap -p- <ziel-ip>`: Scannt alle 65535 Ports.
        - `nmap --script vuln <ziel-ip>`: Führt Nmap-Skripte zur Erkennung bekannter Schwachstellen aus.
- **Webserver-Informationen:**
    
    - `curl -I <ziel-url>`: Zeigt die HTTP-Header einer Webseite an.
    - `wget --spider <ziel-url>`: Überprüft, ob eine Webseite existiert, ohne den Inhalt herunterzuladen.
    - Tools wie `whatweb <ziel-url>` (oft vorinstalliert in Parrot OS) können weitere Informationen über die verwendete Technologie einer Webseite liefern.

**9.2 Schwachstellenscans (Vulnerability Scanning)**

Nach der Informationsbeschaffung geht es darum, potenzielle Schwachstellen im Zielsystem zu identifizieren.

- **OpenVAS / Greenbone Security Assistant:** Eine umfassende Open-Source-Lösung für Schwachstellenmanagement (oft über eine Web-Oberfläche zugänglich, kann aber auch über die Kommandozeile gesteuert werden).
- **Nessus (kommerziell, aber mit einer kostenlosen "Essentials"-Version):** Ein weit verbreiteter kommerzieller Schwachstellenscanner (ebenfalls oft mit Web-Interface).
- **Nikto:** Ein Webserver-Scanner, der nach bekannten Schwachstellen und Konfigurationsfehlern sucht (`nikto -h <ziel-url>`).
- **OWASP ZAP (Zed Attack Proxy):** Ein Open-Source-Webanwendungs-Sicherheitsscanner (hauptsächlich GUI-basiert, bietet aber auch Kommandozeilen-Optionen).

**9.3 Ausnutzung (Exploitation)**

Dieser Abschnitt behandelt Befehle und Frameworks, die zur Ausnutzung gefundener Schwachstellen verwendet werden können.

- **Metasploit Framework:** Ein sehr mächtiges Framework für Penetrationstests, das eine große Sammlung von Exploits und Payloads bietet (wird über die Konsole mit `msfconsole` gestartet).
- **Searchsploit:** Ein Kommandozeilen-Tool zum Durchsuchen der Exploit-Datenbank von Exploit-DB (`searchsploit <suchbegriff>`).
- **Manuelle Ausnutzung:** In vielen Fällen erfordert das Ausnutzen von Schwachstellen das Verständnis der Schwachstelle und die manuelle Interaktion mit dem Zielsystem über die Konsole (z.B. mit Tools wie `netcat` oder spezifischen Exploits in Python oder anderen Sprachen).
    - `netcat -nv <ziel-ip> <ziel-port>` (oder `nc -nv <ziel-ip> <ziel-port>`): Ein vielseitiges Netzwerk-Tool zum Senden und Empfangen von Daten über TCP oder UDP.

**9.4 Post-Exploitation**

Nachdem ein System kompromittiert wurde, können verschiedene Befehle und Tools verwendet werden, um die Kontrolle zu behalten, weitere Informationen zu sammeln und sich möglicherweise im Netzwerk auszubreiten.

- **Grundlegende Systembefehle:**
    
    - `whoami`: Zeigt den aktuellen Benutzernamen an.
    - `id`: Zeigt die Benutzer- und Gruppen-IDs an.
    - `uname -a`: Zeigt Systeminformationen (Kernel-Version, Architektur etc.).
    - `cat /etc/passwd`: Zeigt die Benutzerkonten (oft nur Hash-Werte).
    - `cat /etc/shadow`: Enthält die Passwort-Hashes (oft nur mit Root-Rechten lesbar).
    - `ls -la`: Zeigt alle Dateien und Verzeichnisse mit detaillierten Berechtigungen an.
    - `pwd`: Zeigt das aktuelle Arbeitsverzeichnis an.
    - `cd <verzeichnis>`: Wechselt das Verzeichnis.
    - `mkdir <verzeichnis>`: Erstellt ein neues Verzeichnis.
    - `rm <datei>`: Löscht eine Datei.
    - `ps aux`: Zeigt alle laufenden Prozesse an.
    - `kill <prozess-id>`: Beendet einen Prozess.
- **Datenübertragung:**
    
    - `scp <quelle> <ziel>`: Sicheres Kopieren von Dateien über SSH.
    - `wget <url>`: Herunterladen von Dateien aus dem Internet.
- **Privilege Escalation (Rechteausweitung):** Dies beinhaltet oft die Suche nach Konfigurationsfehlern oder bekannten Schwachstellen im System, um höhere Berechtigungen (z.B. Root-Zugriff) zu erlangen. Es gibt keine spezifischen "Befehle" dafür, sondern eher Techniken und Exploits, die oft manuell oder mit Hilfe von Frameworks wie Metasploit angewendet werden.
    

**9.5 Drahtlose Sicherheit (Wireless Security)**

Parrot OS enthält viele Tools für das Testen der Sicherheit von drahtlosen Netzwerken.

- **Aircrack-ng Suite:** Eine Sammlung von Tools für das Abfangen und Analysieren von WLAN-Traffic sowie das Knacken von WEP/WPA/WPA2-Passwörtern.
    
    - `airodump-ng <schnittstelle>`: Erfasst WLAN-Pakete.
    - `aireplay-ng`: Sendet gefälschte WLAN-Pakete für verschiedene Angriffe.
    - `aircrack-ng`: Knackt WEP/WPA/WPA2-Passwörter.
    - `wash`: Erkennt WPS-fähige Access Points.
    - `reaver`: Brute-Force-Angriff auf WPS.
- **Bettercap:** Ein mächtiges Tool für verschiedene Arten von Netzwerkangriffen, einschließlich WLAN-Sniffing und Man-in-the-Middle-Angriffe.
    

**9.6 Webanwendungssicherheit (Web Application Security)**

Parrot OS bietet verschiedene Tools zum Testen der Sicherheit von Webanwendungen.

- **Burp Suite (kommerziell, aber mit einer kostenlosen Community Edition):** Ein umfassendes Tool für Webanwendungs-Penetrationstests (hauptsächlich GUI-basiert).
- **OWASP ZAP (siehe 9.2):** Ein Open-Source-Webanwendungs-Sicherheitsscanner.
- **SQLmap:** Ein Tool zur Automatisierung der Erkennung und Ausnutzung von SQL-Injection-Schwachstellen (`sqlmap -u <ziel-url>`).
- **XSSer:** Ein Framework zum automatisierten Testen auf Cross-Site Scripting (XSS)-Schwachstellen.

**9.7 Berichterstellung und Analyse**

Nach einem Penetrationstest ist es wichtig, die Ergebnisse zu dokumentieren und zu analysieren.

- **`script` Befehl:** Startet eine Shell-Sitzung, die alle Befehle und Ausgaben in einer Datei aufzeichnet (`script output.txt`).
- **Manuelle Protokollierung:** Das Erstellen von Notizen und Screenshots ist unerlässlich.
- **Tools für Berichterstellung:** Es gibt verschiedene Tools (oft GUI-basiert), die bei der Erstellung von professionellen Penetrationstestberichten helfen.

**Wichtiger Hinweis:**

Die in diesem Kapitel erwähnten Befehle und Tools sind mächtig und sollten nur in einer legalen und ethischen Umgebung verwendet werden, mit der ausdrücklichen Genehmigung des Eigentümers des Zielsystems oder Netzwerks. Unbefugte Nutzung kann schwerwiegende rechtliche Konsequenzen haben.



## Kapitel 10: Netzwerk, Ports und Firewalls – Befehle für die Netzwerkverwaltung

Dieses Kapitel behandelt wichtige Konsolenbefehle unter Parrot OS, die dir helfen, dein Netzwerk zu verstehen, offene Ports zu analysieren und die Firewall zu konfigurieren.

**10.1 Netzwerkkonfiguration und -informationen**

Dieser Abschnitt befasst sich mit Befehlen, um grundlegende Netzwerkinformationen anzuzeigen und Netzwerkschnittstellen zu konfigurieren.

- **Anzeigen von Netzwerkschnittstellen:**
    
    - `ip a` oder `ip addr show`: Zeigt detaillierte Informationen zu allen Netzwerkschnittstellen, einschließlich IP-Adressen, MAC-Adressen und Status.
    - `ifconfig`: Ein älteres Tool, das ebenfalls Informationen zu Netzwerkschnittstellen anzeigt und grundlegende Konfigurationen ermöglicht.
    - `iwconfig`: Zeigt Informationen zu drahtlosen Netzwerkschnittstellen an (SSID, Frequenz, Signalstärke etc.).
- **Konfigurieren von Netzwerkschnittstellen (erfordert oft Root-Rechte):**
    
    - `ip addr add <ip-adresse>/<netzmaske> dev <schnittstelle>`: Fügt einer Schnittstelle eine IP-Adresse hinzu.
    - `ip addr del <ip-adresse>/<netzmaske> dev <schnittstelle>`: Entfernt eine IP-Adresse von einer Schnittstelle.
    - `ip link set dev <schnittstelle> up`: Aktiviert eine Netzwerkschnittstelle.
    - `ip link set dev <schnittstelle> down`: Deaktiviert eine Netzwerkschnittstelle.
    - `dhclient <schnittstelle>`: Fordert eine IP-Adresse von einem DHCP-Server an.
- **Anzeigen und Konfigurieren der Routing-Tabelle:**
    
    - `ip r` oder `ip route show`: Zeigt die aktuelle Routing-Tabelle des Systems.
    - `route -n`: Eine weitere Möglichkeit, die Routing-Tabelle anzuzeigen (numerische Adressen).
    - `ip route add default via <gateway-ip>`: Fügt eine Standardroute hinzu.
    - `ip route del default via <gateway-ip>`: Entfernt die Standardroute.
- **DNS-Konfiguration:**
    
    - Die DNS-Server werden normalerweise über DHCP bezogen oder in der Datei `/etc/resolv.conf` konfiguriert. Du kannst den Inhalt dieser Datei mit `cat /etc/resolv.conf` anzeigen.
- **Hostname-Informationen:**
    
    - `hostname`: Zeigt den Hostnamen des Systems an.
    - `hostnamectl`: Ermöglicht die Abfrage und Änderung des Hostnamens und anderer systembezogener Einstellungen.

**10.2 Portverwaltung und -analyse**

Dieser Abschnitt behandelt Befehle, um offene Ports zu überprüfen und Netzwerkverbindungen zu analysieren.

- **Anzeigen offener Ports und zugehöriger Prozesse:**
    
    - `netstat -tulnp`: Zeigt alle aktiven TCP- und UDP-Verbindungen, Listening-Ports und die zugehörigen Prozess-IDs (erfordert oft Root-Rechte).
        - `-t`: Nur TCP-Verbindungen.
        - `-u`: Nur UDP-Verbindungen.
        - `-l`: Nur Listening-Sockets.
        - `-n`: Zeigt numerische Adressen und Ports (keine Hostnamen oder Dienstnamen).
        - `-p`: Zeigt die Prozess-ID und den Programmnamen.
    - `ss -tulnp`: Ein modernerer Nachfolger von `netstat` mit ähnlicher Funktionalität und oft detaillierteren Informationen.
    - `lsof -i -P -n`: Listet offene Dateien auf, die mit Netzwerkverbindungen in Verbindung stehen.
        - `-i`: Nur Netzwerkdateien.
        - `-P`: Zeigt Portnummern anstelle von Dienstnamen.
        - `-n`: Zeigt numerische Hostadressen anstelle von Hostnamen.
- **Netzwerkverkehrsanalyse:**
    
    - `tcpdump [optionen]`: Ein mächtiges Kommandozeilen-Tool zur Erfassung und Analyse von Netzwerkverkehr.
        - `tcpdump -i <schnittstelle>`: Erfasst den gesamten Verkehr auf der angegebenen Schnittstelle.
        - `tcpdump -i <schnittstelle> port <portnummer>`: Erfasst nur Verkehr auf dem angegebenen Port.
        - `tcpdump -i <schnittstelle> src <ip-adresse>`: Erfasst nur Verkehr von der angegebenen IP-Adresse.
        - `tcpdump -i <schnittstelle> dst <ip-adresse>`: Erfasst nur Verkehr zur angegebenen IP-Adresse.
        - `tcpdump -i <schnittstelle> tcp`: Erfasst nur TCP-Verkehr.
        - `tcpdump -i <schnittstelle> udp`: Erfasst nur UDP-Verkehr.
        - `tcpdump -w <dateiname.pcap> -i <schnittstelle>`: Speichert den erfassten Verkehr in einer Datei für spätere Analyse (z.B. mit Wireshark).
    - `tshark`: Die Kommandozeilenversion von Wireshark, die ebenfalls zur Analyse von Netzwerkverkehr verwendet werden kann.
- **Portscanning:**
    
    - `nmap <ziel-ip-oder-hostname>`: Ein vielseitiges Tool für Portscanning und Service-Erkennung (siehe auch Kapitel 9).
        - `nmap -p <portbereich> <ziel-ip>`: Scannt einen bestimmten Portbereich.
        - `nmap -sT <ziel-ip>`: TCP Connect Scan (erfordert eine vollständige TCP-Verbindung).
        - `nmap -sU <ziel-ip>`: UDP Scan.

**10.3 Firewall-Verwaltung**

Eine Firewall ist ein wesentliches Sicherheitswerkzeug, um unerwünschten Netzwerkverkehr zu blockieren. Unter Linux, und somit auch in Parrot OS, ist `iptables` traditionell das Standard-Firewall-Tool. Neuere Systeme verwenden oft `nftables`. Parrot OS kann auch `ufw` (Uncomplicated Firewall) als benutzerfreundlichere Schnittstelle für `iptables` anbieten.

- **`iptables` (mächtig, aber komplex):**
    
    - **Anzeigen der aktuellen Regeln:** `sudo iptables -L -n -v`
        - `-L`: Listet die Regeln auf.
        - `-n`: Zeigt numerische Adressen und Ports.
        - `-v`: Zeigt ausführliche Informationen.
    - **Erlauben von eingehendem Verkehr auf einem bestimmten Port (z.B. TCP Port 80):** `sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT`
        - `-A INPUT`: Fügt eine Regel zur INPUT-Kette hinzu (eingehender Verkehr).
        - `-p tcp`: Gibt das Protokoll (TCP) an.
        - `--dport 80`: Gibt den Zielport (80) an.
        - `-j ACCEPT`: Legt die Aktion auf "Akzeptieren" fest.
    - **Blockieren von eingehendem Verkehr von einer bestimmten IP-Adresse:** `sudo iptables -A INPUT -s <ip-adresse> -j DROP`
        - `-s <ip-adresse>`: Gibt die Quell-IP-Adresse an.
        - `-j DROP`: Legt die Aktion auf "Verwerfen" fest (keine Antwort an den Absender).
    - **Verwerfen von ausgehendem Verkehr zu einem bestimmten Port:** `sudo iptables -A OUTPUT -p tcp --dport 25 -j DROP`
        - `-A OUTPUT`: Fügt eine Regel zur OUTPUT-Kette hinzu (ausgehender Verkehr).
    - **Löschen einer Regel (erfordert genaue Kenntnis der Regelnummer oder -spezifikation):**
        - Zuerst die Regeln mit `sudo iptables -L --line-numbers` anzeigen, um die Zeilennummern zu sehen.
        - Dann die Regel mit der Nummer `X` löschen: `sudo iptables -D INPUT X`
    - **Speichern der `iptables`-Regeln (systemabhängig, oft mit `sudo iptables-save > /etc/iptables/rules.v4`):** Die genaue Methode kann je nach Parrot OS-Version variieren.
- **`nftables` (der moderne Nachfolger von `iptables`):**
    
    - **Anzeigen der aktuellen Regeln:** `sudo nft list ruleset`
    - Die Syntax von `nftables` unterscheidet sich deutlich von `iptables`. Informationen zur Verwendung von `nftables` würden den Rahmen dieses Kapitels sprengen, aber es ist wichtig zu wissen, dass dies die moderne Firewall-Lösung unter Linux ist.
- **`ufw` (Uncomplicated Firewall) – eine benutzerfreundliche Schnittstelle für `iptables`:**
    
    - **Aktivieren von `ufw`:** `sudo ufw enable`
    - **Deaktivieren von `ufw`:** `sudo ufw disable`
    - **Status von `ufw` anzeigen:** `sudo ufw status`
    - **Eingehenden Verkehr auf einem bestimmten Port erlauben (z.B. TCP Port 22 für SSH):** `sudo ufw allow 22/tcp`
    - **Eingehenden Verkehr von einer bestimmten IP-Adresse erlauben:** `sudo ufw allow from <ip-adresse>`
    - **Eingehenden Verkehr zu einem bestimmten Port von einer bestimmten IP-Adresse erlauben:** `sudo ufw allow from <ip-adresse> to any port <portnummer>`
    - **Eingehenden Verkehr auf einem bestimmten Port verweigern:** `sudo ufw deny <portnummer>/<protokoll>`
    - **Regel löschen:** `sudo ufw delete allow <portnummer>/<protokoll>`

Dieses Kapitel bietet eine Einführung in die wichtigsten Befehle für die Netzwerkverwaltung, Portanalyse und Firewall-Konfiguration unter Parrot OS. Die genaue Verwendung und Konfiguration kann je nach spezifischem Anwendungsfall variieren. Es ist ratsam, die Manual Pages (`man <befehl>`) für detailliertere Informationen zu den einzelnen Befehlen zu konsultieren.








|   |   |   |
|---|---|---|
|Alltagsszenario|Konsolenbefehl(e)|Erklärung und Anwendung im Alltag|
|Einen neuen Ordner für meine Fotos erstellen|mkdir Bilder/Urlaub2024|Erstellt einen neuen Ordner namens "Urlaub2024"  <br>innerhalb des Ordners "Bilder" in deinem Home-Verzeichnis. .|
|Sehen, welche Dateien in meinem Download-Ordner sind|ls Downloads|Zeigt alle Dateien und Ordner an,  <br>die sich in deinem Download-Ordner befinden.|
|Eine heruntergeladene Datei in meinen Dokumente-Ordner verschieben|mv Downloads/wichtige_datei.pdf Dokumente/|Verschiebt die Datei "wichtige_datei.pdf" aus dem  <br>Download-Ordner in den Dokumente-Ordner.|
|Den Inhalt einer Textdatei schnell überfliegen|less Dokumente/notizen.txt|Öffnet die Datei "notizen.txt" im "less"-Viewer,  <br>sodass du den Inhalt seitenweise lesen kannst.  <br>Nützlich, um Notizen, Konfigurationsdateien oder Logdateien anzusehen,  <br>ohne einen separaten Editor zu öffnen.|
|Nach einer bestimmten Datei suchen, deren Namen ich nicht genau kenne|find . -name "*rechnung*.pdf"|Sucht im aktuellen Verzeichnis (.) und allen Unterverzeichnissen nach Dateien,  <br>deren Name das Wort "rechnung" enthält und mit ".pdf" endet. Sehr hilfreich,  <br>wenn du eine Datei suchst, aber dich nicht mehr genau an den Namen erinnerst.|
|Den Speicherplatz auf meiner Festplatte überprüfen|df -h|Zeigt den belegten und freien Speicherplatz auf deinen Festplattenpartitionen an.  <br>Wichtig, um zu wissen, wie viel Speicherplatz du noch hast.|
|Ein neues Programm installieren (z.B. VLC Media Player)|sudo apt install vlc|Installiert den VLC Media Player über den Paketmanager.  <br>Ermöglicht es dir, neue Software direkt über die Konsole zu installieren.|
|Die installierte Software auf den neuesten Stand bringen|sudo apt update && sudo apt upgrade|Aktualisiert zuerst die Liste der verfügbaren Softwarepakete und  <br>führt dann ein Upgrade aller installierten Pakete durch.  <br>Wichtig für die Sicherheit und Stabilität deines Systems.|
|Ein Programm deinstallieren (z.B. ein Testprogramm)|sudo apt remove testprogramm|Deinstalliert das Programm "testprogramm".  <br>Hilfreich, um nicht mehr benötigte Software zu entfernen.|
|Herausfinden, welche IP-Adresse mein Computer hat|ip a oder ifconfig|Zeigt Informationen über deine Netzwerkschnittstellen an, einschließlich  <br>deiner IP-Adresse.  <br>Nützlich, wenn du dich mit Netzwerkeinstellungen beschäftigen musst.|
|Alle laufenden Programme sehen, die viel Ressourcen verbrauchen|htop|Öffnet den interaktiven Prozessmonitor htop, der dir zeigt, welche  <br>Programme gerade laufen und wie viel CPU und Speicher sie verwenden.  <br>Hilfreich, um ressourcenintensive  <br>Prozesse zu identifizieren und gegebenenfalls zu beenden.  <br>Beende htop mit q.|
|Einen bestimmten Prozess beenden, der nicht reagiert (z.B. mit der Prozess-ID 1234)|kill 1234|Beendet den Prozess mit der angegebenen Prozess-ID (PID).  <br>Du findest die PID in der Ausgabe von top, htop oder ps aux. Nützlich,  <br>um Programme zu beenden, die sich aufgehängt haben.|
|Die letzten Zeilen einer Protokolldatei ansehen, um Fehler zu finden|tail -n 20 /var/log/syslog|Zeigt die letzten 20 Zeilen der Systemprotokolldatei an.  <br>Hilfreich bei der Fehlersuche, um kürzlich aufgetretene Probleme zu identifizieren.|
|Nach einem bestimmten Wort in einer Datei suchen (z.B. "Fehler")|grep "Fehler" /var/log/meinprogramm.log|Sucht in der Datei "/var/log/meinprogramm.log" nach Zeilen,  <br>die das Wort "Fehler" enthalten. Nützlich,  <br>um spezifische Informationen in großen Dateien zu finden.|
|Den Inhalt einer Webseite im Terminal anzeigen (nur Text)|curl https://www.google.de|Lädt den Quellcode der Webseite von Google herunter und zeigt ihn im Terminal an.  <br>Kann nützlich sein, um schnell Informationen  <br>zu überprüfen oder für einfache Webseiten ohne viel Formatierung.|
|Die Historie meiner letzten Befehle ansehen|history|Zeigt eine Liste der Befehle an, die du kürzlich in der Konsole eingegeben hast.  <br>Du kannst dann mit !n einen bestimmten Befehl erneut ausführen  <br>(wobei n die Nummer des Befehls in der Liste ist).|
|Mehr über einen bestimmten Befehl erfahren (z.B. ls)|man ls|Öffnet die Handbuchseite (Manual Page) für den Befehl ls.  <br>Hier findest du detaillierte Informationen über die Verwendung  <br>des Befehls und seine verschiedenen Optionen. Beende die Handbuchseite mit q.|
|Eine einfache Textdatei erstellen oder bearbeiten|nano datei.txt|Öffnet den einfachen Texteditor nano in der Konsole.  <br>Du kannst hier Text eingeben und speichern.  <br>Nützlich für schnelle Notizen oder kleine Konfigurationsänderungen.  <br>Speichern mit Strg + O, Beenden mit Strg + X.|
|Einen laufenden Befehl im Hintergrund ausführen|long_running_command &|Fügt ein & am Ende eines Befehls hinzu, um ihn im Hintergrund auszuführen.  <br>Das Terminal wird sofort wieder für neue Befehle verfügbar.  <br>Nützlich für zeitaufwendige Aufgaben, die du nicht aktiv beobachten musst.  <br>Du kannst die laufenden Hintergrundprozesse  <br>mit jobs anzeigen und sie bei Bedarf mit fg %n  <br>(wobei n die Jobnummer ist) in den Vordergrund holen.|


|   |   |   |
|---|---|---|
|Alltagsszenario|Konsolenbefehl(e)|Erklärung und Anwendung im Alltag|
|Überprüfen, ob eine bestimmte Webseite erreichbar ist|ping google.com|Sendet kleine Datenpakete an den Server von Google und misst die Antwortzeit.  <br>Nützlich, um zu überprüfen, ob deine Internetverbindung funktioniert oder ob ein  <br>bestimmter Server erreichbar ist. Drücke Strg + C, um den Ping zu stoppen.|
|Den Netzwerkverkehr auf meinem Computer beobachten|tcpdump oder sudo tcpdump|Zeigt den Netzwerkverkehr in Echtzeit an. Für fortgeschrittene Nutzer, um  <br>Netzwerkprobleme zu diagnostizieren oder den Datenverkehr zu analysieren.  <br>sudo ist oft erforderlich, um alle Pakete sehen zu können.|
|Eine Datei komprimieren, um Speicherplatz  <br>zu sparen oder sie einfacher zu versenden|tar -czvf archiv.tar.gz meine_dateien/|Erstellt ein komprimiertes Archiv (im gzip-Format) des Ordners "meine_dateien".  <br>Nützlich, um mehrere Dateien oder Ordner in einer einzigen, kleineren Datei zu bündeln.  <br>tar ist das Archivierungsprogramm, -c steht für create, -z für gzip, -v für verbose (zeigt die verarbeiteten Dateien an),  <br>und -f gibt den Namen des Archivs an.|
|Ein komprimiertes Archiv entpacken|tar -xzvf archiv.tar.gz|Entpackt das Archiv "archiv.tar.gz". -x steht für extract.|
|Eine einzelne Datei aus einem Archiv anzeigen, ohne es zu entpacken|`tar -tzvf archiv.tar.gz|grep gesuchte_datei.txt`|
|Die aktuelle Systemzeit und das Datum anzeigen|date|Zeigt die aktuelle Systemzeit und das Datum an. Einfach und nützlich, um die Systemuhr zu überprüfen.|
|Die Uptime des Systems anzeigen (wie lange der Computer schon läuft)|uptime|Zeigt an, wie lange dein System schon läuft, wie viele Benutzer angemeldet sind und die durchschnittliche Systemlast.  <br>Interessant, um die Stabilität des Systems zu beurteilen.|
|Informationen über meinen Prozessor (CPU) anzeigen|lscpu|Zeigt detaillierte Informationen über deine CPU an, wie z.B. Modell, Anzahl der Kerne und Architekturen. Für technisch interessierte Nutzer.|
|Informationen über den Arbeitsspeicher (RAM) anzeigen|free -h|Zeigt die aktuelle Speicherauslastung deines Systems an (gesamt, belegt, frei, etc.)  <br>in einem für Menschen lesbaren Format. Hilfreich, um zu beurteilen, ob dein System genügend Arbeitsspeicher hat.|
|Die Auslastung der einzelnen CPU-Kerne beobachten|mpstat -P ALL|Zeigt die Auslastung jedes einzelnen CPU-Kerns an. Für fortgeschrittene Nutzer, um die Verteilung der Last auf die Prozessoren zu analysieren.|
|Einen Textbefehl oder die Ausgabe eines anderen Befehls in eine Datei umleiten|ls -l > dateien.txt|Speichert die detaillierte Liste der Dateien und Ordner im aktuellen Verzeichnis in der Datei "dateien.txt".  <br>Das > Symbol leitet die Standardausgabe um. Wenn die Datei nicht existiert, wird sie erstellt. Wenn sie existiert, wird sie überschrieben.|
|Die Ausgabe eines Befehls an einen anderen Befehl weiterleiten (Piping)|`cat meine_grosse_datei.txt|grep "wichtig"`|
|Einen Befehl mit Administratorrechten ausführen|sudo <befehl>|Ermöglicht es dir, Befehle als Superuser (Administrator) auszuführen. Oft benötigt, um Systemänderungen vorzunehmen,  <br>Software zu installieren oder bestimmte Konfigurationsdateien zu bearbeiten.  <br>Du wirst nach deinem Passwort gefragt. Sei vorsichtig bei der Verwendung von sudo.|
|Die Konfigurationsdatei eines Programms bearbeiten (z.B. mit nano)|sudo nano /etc/network/interfaces|Öffnet die Netzwerkkonfigurationsdatei mit dem Texteditor nano als Administrator.  <br>Ermöglicht es dir, wichtige Systemeinstellungen zu bearbeiten. Sei vorsichtig beim Bearbeiten von Systemdateien.|
|Einen Dienst (Service) neu starten (z.B. den Netzwerkdienst)|sudo systemctl restart networking|Startet den Netzwerkdienst neu. Nützlich, wenn du Netzwerkeinstellungen geändert hast oder es Probleme mit der Netzwerkverbindung gibt.  <br>systemctl ist das Werkzeug zur Verwaltung von Systemdiensten.|
|Den Status eines Dienstes überprüfen|sudo systemctl status networking|Zeigt den aktuellen Status des Netzwerkdienstes an (z.B. ob er läuft, aktiv ist oder Fehler aufgetreten sind). Hilfreich bei der Fehlersuche.|
|Einen Alias für einen häufig verwendeten Befehl erstellen|alias ll='ls -lha'|Erstellt einen Alias namens ll, der den Befehl ls -lha ausführt. Du kannst diesen Alias in deiner Shell-Konfigurationsdatei  <br>(z.B. .bashrc oder .zshrc) speichern, um ihn dauerhaft zu machen.  <br>Spart Zeit und Tipparbeit. Gib einfach ll ein, um die detaillierte Dateiliste anzuzeigen.|
|Die aktuelle Verzeichnisstruktur als Baum anzeigen|tree (muss ggf. mit sudo apt install tree installiert werden)|Zeigt die Verzeichnisstruktur des aktuellen Ordners und seiner Unterordner in einer baumartigen Ansicht an.  <br>Sehr hilfreich, um einen schnellen Überblick über die Organisation von Dateien und Ordnern zu bekommen.|
|Eine Datei oder einen Ordner rekursiv kopieren  <br>und dabei die Berechtigungen beibehalten|cp -rp quelle_ordner ziel_ordner|Kopiert den Ordner "quelle_ordner" und alle seine Unterordner und Dateien rekursiv (-r)  <br>und behält dabei die ursprünglichen Berechtigungen (-p) bei.  <br>Wichtig, wenn du Sicherungskopien erstellst oder Dateien zwischen Systemen verschiebst.|



|   |   |   |
|---|---|---|
|Alltagsszenario|Konsolenbefehl(e)|Erklärung und Anwendung im Alltag|
|Einen neuen Benutzer auf meinem System hinzufügen|sudo adduser neuer_benutzer|Erstellt einen neuen Benutzeraccount mit dem Namen "neuer_benutzer".  <br>Du wirst nach einem Passwort und weiteren Informationen gefragt.  <br>Nützlich, wenn mehrere Personen denselben Computer nutzen oder  <br>du einen separaten Account für bestimmte Zwecke erstellen möchtest.|
|Das Passwort eines bestehenden Benutzers ändern|sudo passwd benutzername|Ermöglicht es dir, das Passwort für den Benutzer "benutzername" zu ändern.  <br>Du wirst nach dem neuen Passwort gefragt. Wichtig für die Sicherheit deines Systems.|
|Einen Benutzer zu einer bestimmten Gruppe hinzufügen (z.B. zur Gruppe "sudo" für Administratorrechte)|sudo usermod -aG sudo benutzername|Fügt den Benutzer "benutzername" zur Gruppe "sudo" hinzu.  <br>Dadurch kann dieser Benutzer Befehle mit sudo ausführen.  <br>Sei vorsichtig bei der Vergabe von Administratorrechten. -aG steht für "append to group".|
|Informationen über einen bestimmten Benutzer anzeigen|id benutzername|Zeigt die Benutzer-ID (UID), die Gruppen-ID (GID) und die  <br>Gruppenzugehörigkeiten des Benutzers "benutzername" an.|
|Einen laufenden Prozess nach seinem Namen suchen und beenden|pkill -f programmname|Sucht nach allen Prozessen,  <br>deren Name oder Befehlszeile "programmname" enthält und beendet sie  <br>. Nützlich, um Programme zu beenden, deren Prozess-ID du nicht kennst  <br>. Sei vorsichtig, um nicht versehentlich wichtige Prozesse zu beenden.|
|Die Sortierung der Ausgabe eines Befehls ändern (z.B. nach Dateigröße)|`ls -lh|sort -hr -k 5`|
|Die Ausgabe eines Befehls filtern und nur bestimmte Zeilen anzeigen|`cat grosse_logdatei.txt|grep "WARNUNG"|
|Die Unterschiede zwischen zwei Textdateien anzeigen|diff datei1.txt datei2.txt|Zeigt die Unterschiede zeilenweise zwischen "datei1.txt" und "datei2.txt" an  <br>. Nützlich, um Änderungen in Konfigurationsdateien oder Code zu verfolgen.|
|Den Inhalt einer Datei oder die Ausgabe eines Befehls in die Zwischenablage kopieren (erfordert xclip oder xsel)|`cat datei.txt|xclip -selection clipboardodercat datei.txt|
|Text aus der Zwischenablage in die Konsole einfügen|xclip -o -selection clipboard oder xsel -b -o|Fügt den Inhalt der Zwischenablage in die Konsole ein.  <br>Nützlich, um lange Befehle oder Text aus anderen Anwendungen einzufügen.|
|Eine Datei herunterladen (z.B. von einer Webseite)|wget https://beispiel.de/datei.zip|Lädt die Datei "datei.zip" von der angegebenen URL  <br>herunter und speichert sie im aktuellen Verzeichnis.  <br>Nützlich, um Dateien direkt aus dem Internet in der Konsole herunterzuladen.|
|Eine Webseite nur auf Fehler überprüfen (HTTP-Statuscodes)|curl -I https://www.google.de|Sendet eine Anfrage an die Webseite und zeigt nur die Header-Informationen an,  <br>einschließlich des HTTP-Statuscodes. Nützlich, um schnell zu überprüfen,  <br>ob eine Webseite erreichbar ist (Statuscode 200 OK) oder ob es Fehler gibt (z.B. 404 Not Found).|
|Die aktuelle Konfiguration meines Netzwerks anzeigen|ip addr show|Zeigt detaillierte Informationen über alle Netzwerkschnittstellen, einschließlich IP-Adressen,  <br>MAC-Adressen und Status. Eine umfassendere Alternative zu ip a.|
|Die Routing-Tabelle meines Systems anzeigen|ip route show|Zeigt die Routing-Tabelle an, die bestimmt, wie Datenpakete im Netzwerk weitergeleitet werden.  <br>Für fortgeschrittene Nutzer zur Diagnose von Netzwerkproblemen.|
|DNS-Informationen für eine Domain abfragen|dig google.com oder nslookup google.com|Fragt die DNS-Server nach Informationen über die Domain "google.com"  <br>ab, z.B. die zugehörige IP-Adresse. Nützlich,  <br>um DNS-Probleme zu untersuchen. dig ist in der Regel detaillierter.|
|Den Verlauf der Netzwerkverbindungen meines Systems anzeigen|netstat -tulnp oder ss -tulnp|Zeigt eine Liste der aktiven und passiven Netzwerkverbindungen an,  <br>einschließlich der verwendeten Ports und der zugehörigen Prozesse.  <br>Nützlich, um zu sehen, welche Programme Netzwerkverbindungen herstellen.  <br>ss ist ein modernerer Nachfolger von netstat.|
|Den Hostnamen meines Computers herausfinden|hostname|Zeigt den Namen deines Computers im Netzwerk an.|
|Eine einfache HTTP-Server in meinem aktuellen Verzeichnis starten (für schnelles Teilen von Dateien)|python3 -m http.server (für Python 3) oder python -m SimpleHTTPServer 8000 (für Python 2)|Startet einen einfachen Webserver im aktuellen Verzeichnis.  <br>Du kannst dann über einen Webbrowser im lokalen Netzwerk auf die Dateien  <br>in diesem Verzeichnis zugreifen (standardmäßig auf Port 8000).  <br>Nützlich für das schnelle Teilen von Dateien ohne komplizierte Konfiguration.  <br>Beende den Server mit Strg + C.|
|Die Anzahl der Wörter, Zeilen und Zeichen in einer Datei zählen|wc datei.txt|Zeigt die Anzahl der Zeilen, Wörter und Zeichen in der Datei "datei.txt" an.  <br>Nützlich für einfache Textanalyse.|