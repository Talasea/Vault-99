**`df` – Die Übersicht über den Festplattenspeicher**

Der Befehl `df` steht für **"disk free"** und liefert uns eine übersichtliche Darstellung des belegten und freien Speicherplatzes auf den verschiedenen Dateisystemen, die auf unserem Linux-System gemountet sind. Er ist ein essenzielles Werkzeug, um den Überblick über die Speicherauslastung zu behalten und Engpässe frühzeitig zu erkennen.

**Die grundlegende Ausgabe von `df`:**

Ohne zusätzliche Optionen liefert der `df`-Befehl eine tabellarische Ausgabe mit folgenden Spalten:

- **Filesystem:** Zeigt das gemountete Dateisystem an (oft der Gerätename der Partition oder die Netzwerkadresse).
- **1K-blocks:** Gibt die Gesamtgröße des Dateisystems in 1-Kilobyte-Blöcken an.
- **Used:** Zeigt den belegten Speicherplatz in 1-Kilobyte-Blöcken an.
- **Available:** Zeigt den freien Speicherplatz in 1-Kilobyte-Blöcken an.
- **Use%:** Gibt den prozentualen Anteil des belegten Speicherplatzes an.
- **Mounted on:** Zeigt den Mount Point an, unter dem das Dateisystem eingehängt ist.

**Ein typisches Beispiel für die Ausgabe von `df`:**

```
Filesystem     1K-blocks   Used Available Use% Mounted on
udev             8138388      0   8138388   0% /dev
tmpfs            1630084   9188   1620896   1% /run
/dev/sda1      244853504 18876544 213998880   9% /
tmpfs            8150416      0   8150416   0% /dev/shm
tmpfs               5120      4      5116   1% /run/lock
/dev/sdb1      488386584 286547896 177298688  62% /data
tmpfs            1630084      0   1630084   0% /run/user/1000
```

In dieser Ausgabe sehen wir Informationen über verschiedene Dateisysteme, einschließlich der Root-Partition (`/`), einer separaten Datenpartition (`/data`) und temporärer Dateisysteme (`tmpfs`). Die Spalte `Use%` ist besonders nützlich, um schnell zu erkennen, welche Dateisysteme sich dem kritischen Bereich nähern.

**Wichtige Optionen des `df`-Befehls:**

Der `df`-Befehl bietet verschiedene Optionen, um die Ausgabe anzupassen und nützlichere Informationen zu erhalten:

- `-h` oder `--human-readable`: Zeigt die Größen in für Menschen lesbaren Formaten an (z.B. 1G, 500M, 20K) anstelle von Kilobyte-Blöcken. Dies ist in den meisten Fällen die bevorzugte Option.
    
    Bash
    
    ```
    df -h
    ```
    
    ```
    Filesystem      Size  Used Avail Use% Mounted on
    udev            7.8G     0  7.8G   0% /dev
    tmpfs           1.6G  9.0M  1.6G   1% /run
    /dev/sda1       234G   18G  204G   9% /
    tmpfs           7.8G     0  7.8G   0% /dev/shm
    tmpfs           5.0M  4.0K  5.0M   1% /run/lock
    /dev/sdb1       466G  273G  169G  62% /data
    tmpfs           1.6G     0  1.6G   0% /run/user/1000
    ```
    
- `-T` oder `--print-type`: Zeigt den Typ des Dateisystems in einer zusätzlichen Spalte an.
    
    Bash
    
    ```
    df -hT
    ```
    
    ```
    Filesystem     Type      Size  Used Avail Use% Mounted on
    udev           devtmpfs  7.8G     0  7.8G   0% /dev
    tmpfs          tmpfs     1.6G  9.0M  1.6G   1% /run
    /dev/sda1      ext4      234G   18G  204G   9% /
    tmpfs          tmpfs     7.8G     0  7.8G   0% /dev/shm
    tmpfs          tmpfs     5.0M  4.0K  5.0M   1% /run/lock
    /dev/sdb1      ext4      466G  273G  169G  62% /data
    tmpfs          tmpfs     1.6G     0  1.6G   1% /run/user/1000
    ```
    
- `-a` oder `--all`: Zeigt auch Dateisysteme an, die mit der Option `-i` in `/etc/fstab` als "ignore" markiert sind oder Pseudo-Dateisysteme ohne tatsächlichen Speicherplatz.
    
- `-i` oder `--inodes`: Zeigt Informationen über die Inode-Nutzung anstelle der Blocknutzung. Inodes sind Datenstrukturen, die Metadaten über Dateien speichern (z.B. Berechtigungen, Eigentümer, Größe, Zeitstempel). Ein Mangel an freien Inodes kann dazu führen, dass keine neuen Dateien erstellt werden können, auch wenn noch freier Speicherplatz vorhanden ist.
    
    Bash
    
    ```
    df -i
    ```
    
- `-l` oder `--local`: Beschränkt die Ausgabe auf lokale Dateisysteme und blendet Netzwerk-Dateisysteme (wie NFS oder CIFS) aus.
    
- `-P` oder `--portability`: Verwendet ein portables Ausgabeformat, das in Skripten leichter zu verarbeiten ist.
    
- `--exclude-type=<Typ>`: Blendet Dateisysteme eines bestimmten Typs aus (z.B. `--exclude-type=tmpfs`).
    
- `--output[=<Felder>]`: Ermöglicht eine benutzerdefinierte Ausgabe mit spezifischen Feldern.
    

**Anwendungsfälle für Systemadministratoren:**

- **Überwachung des Speicherplatzes:** Regelmäßige Überprüfung der `df`-Ausgabe hilft, Engpässe auf kritischen Partitionen (z.B. `/`, `/var`, `/tmp`) frühzeitig zu erkennen und Gegenmaßnahmen einzuleiten (z.B. Aufräumen von Dateien, Erweitern von Dateisystemen).
- **Fehlerbehebung:** Wenn Anwendungen Fehler aufgrund von fehlendem Speicherplatz melden, ist `df` das erste Werkzeug zur Diagnose.
- **Planung von Kapazitätserweiterungen:** Die langfristige Beobachtung der Speicherauslastung hilft bei der Planung zukünftiger Hardware-Upgrades.
- **Überprüfung von Mounts:** `df` zeigt, welche Dateisysteme aktuell gemountet sind und an welchem Mount Point, was bei der Überprüfung der Konfiguration hilfreich ist.

**Relevanz für Penetration Tester:**

- **Footprinting und Enumeration:** Die Ausgabe von `df -hT` kann Informationen über die Größe und den Typ der verschiedenen Dateisysteme liefern. Dies kann Hinweise auf die Systemkonfiguration und potenzielle interessante Bereiche für weitere Untersuchungen geben.
- **Erkennen von Mount Points:** Das Wissen über Mount Points ist wichtig, um zu verstehen, wo sich potenziell sensible Daten befinden könnten (z.B. unterhalb von `/mnt`, `/media` oder benutzerdefinierten Mount Points).
- **Analyse von Berechtigungen:** In Kombination mit anderen Befehlen (z.B. `ls -l`) kann `df` helfen zu verstehen, auf welchen Dateisystemen möglicherweise unsichere Berechtigungen konfiguriert sind, die zu einem unbefugten Zugriff führen könnten.
- **Ausnutzung von Speicherplatzmangel:** In seltenen Fällen kann ein absichtlich herbeigeführter Speicherplatzmangel (Denial of Service) die Stabilität des Systems beeinträchtigen. `df` ist das Werkzeug, um dies zu verifizieren.
- **Post-Exploitation:** Nach dem Erlangen von Zugriff kann `df` nützlich sein, um zu identifizieren, wo genügend freier Speicherplatz vorhanden ist, um eigene Tools oder Backdoors abzulegen. Das Wissen über die Mount-Optionen (die mit `mount` oder in `/proc/mounts` eingesehen werden können) ist hier ebenfalls relevant (z.B. um zu prüfen, ob `noexec` aktiv ist).

**Wichtige Überlegungen:**

- Die von `df` angezeigten Werte sind Momentaufnahmen. Die Speicherauslastung kann sich schnell ändern.
- Die Interpretation der Ausgabe erfordert ein grundlegendes Verständnis der Linux-Dateisystemstruktur und der üblichen Mount Points.
- Bei Netzwerk-Dateisystemen kann die angezeigte Größe und Verfügbarkeit von den Quoten und der Auslastung auf dem Server abhängen.

**Zusammenfassend lässt sich sagen:**

Der Befehl `df` ist ein unverzichtbares Werkzeug in der Linux-Kommandozeile, um sich einen schnellen und präzisen Überblick über die Festplattenauslastung zu verschaffen. Ob zur täglichen Systemüberwachung, zur Fehlerbehebung oder zur Analyse aus der Sicherheitsperspektive – `df` liefert wertvolle Informationen über den Zustand der Speicherressourcen unseres Systems.