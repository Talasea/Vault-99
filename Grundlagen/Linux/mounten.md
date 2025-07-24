**Was bedeutet "Mounten" in Linux?**

Stellen wir uns vor, wir haben verschiedene Speichergeräte – Festplatten, SSDs, USB-Sticks, Netzwerkfreigaben – die alle Daten enthalten. Damit unser Linux-System auf diese Daten zugreifen kann, müssen diese Speichergeräte in die bestehende Verzeichnisstruktur des Systems "eingehängt" werden. Dieser Vorgang wird als **Mounten** bezeichnet.

Man kann es sich wie das Einbinden einer neuen Festplatte in einen Schreibtisch vorstellen. Die Festplatte selbst existiert, aber um auf die darin enthaltenen Dokumente zugreifen zu können, muss sie in den Schreibtisch integriert werden, sodass sie Teil des gesamten Ablagesystems wird.

**Das zentrale Konzept: Der Mount Point**

Der Ort im bestehenden Dateisystem, an dem ein externes Dateisystem eingehängt wird, nennt man **Mount Point**. Dies ist ein leerer Ordner (oder sollte idealerweise leer sein) im Dateisystem. Nach dem Mounten erscheint der Inhalt des externen Dateisystems an diesem Mount Point.

Das Root-Dateisystem (`/`) ist das erste Dateisystem, das während des Bootvorgangs gemountet wird. Alle anderen Dateisysteme werden dann unterhalb dieses Root-Dateisystems eingehängt.

**Warum ist Mounten notwendig?**

- **Strukturierung der Daten:** Es ermöglicht eine logische Organisation der Daten über verschiedene Speichergeräte hinweg.
- **Zugriffskontrolle:** Durch das Mounten können Berechtigungen und Zugriffsrechte auf die Inhalte des gemounteten Dateisystems festgelegt werden.
- **Verwaltung von Speicherressourcen:** Es erlaubt dem Systemadministrator, den verfügbaren Speicherplatz auf verschiedenen Geräten effizient zu nutzen.
- **Abstraktion:** Anwendungen müssen sich nicht um die physische Lage der Daten kümmern, sondern greifen einfach über die Verzeichnisstruktur darauf zu.

**Der Mount-Befehl:**

Das zentrale Werkzeug in Linux zum Mounten von Dateisystemen ist der Befehl `mount`. Die grundlegende Syntax lautet:

Bash

```
sudo mount <Gerät> <Mount Point>
```

- `<Gerät>`: Gibt das zu mountende Speichergerät an. Dies kann der Gerätename einer Partition sein (z.B. `/dev/sdb1`), ein Dateiname einer Loopback-Datei oder eine Netzwerkfreigabe (z.B. `//server/share /mnt/share`).
- `<Mount Point>`: Gibt den Pfad im lokalen Dateisystem an, wo das Gerät eingehängt werden soll (z.B. `/mnt/usb`, `/data`).

**Wichtige Optionen des `mount`-Befehls:**

Der `mount`-Befehl bietet zahlreiche Optionen, um das Mount-Verhalten zu beeinflussen. Einige wichtige sind:

- `-t <Dateisystemtyp>`: Gibt den Typ des Dateisystems an (z.B. `ext4`, `ntfs`, `vfat`, `iso9660`). Linux versucht oft, den Typ automatisch zu erkennen, aber es ist manchmal notwendig, ihn explizit anzugeben.
- `-o <Optionen>`: Ermöglicht die Angabe verschiedener Mount-Optionen, die das Verhalten des Dateisystems beeinflussen. Einige gängige Optionen sind:
    - `ro`: Mountet das Dateisystem schreibgeschützt (read-only). Wichtig für Sicherheit und um unbeabsichtigte Änderungen zu verhindern.
    - `rw`: Mountet das Dateisystem mit Lese- und Schreibzugriff (read-write).
    - `noexec`: Verhindert die Ausführung von Binärdateien auf dem gemounteten Dateisystem. Eine wichtige Sicherheitsmaßnahme, z.B. für temporäre Verzeichnisse oder USB-Sticks unbekannter Herkunft.
    - `nosuid`: Deaktiviert die Behandlung von Set-User-ID (SUID) und Set-Group-ID (SGID) Bits auf dem gemounteten Dateisystem. Reduziert das Risiko von Privilege Escalation.
    - `nodev`: Verhindert die Interpretation von Geräte-Spezialdateien auf dem gemounteten Dateisystem.
    - `user`: Erlaubt normalen Benutzern, das Dateisystem zu mounten (wenn in `/etc/fstab` entsprechend konfiguriert).
    - `defaults`: Verwendet die Standard-Mount-Optionen.

**Beispiele für das Mounten:**

- **Mounten einer USB-Festplatte (angenommen als `/dev/sdb1` und der Mount Point ist `/mnt/usb`):**
    
    Bash
    
    ```
    sudo mount /dev/sdb1 /mnt/usb
    ```
    
- **Mounten einer ISO-Datei schreibgeschützt nach `/mnt/iso`:**
    
    Bash
    
    ```
    sudo mount -o loop,ro datei.iso /mnt/iso
    ```
    
- **Mounten einer Netzwerkfreigabe (NFS):**
    
    Bash
    
    ```
    sudo mount -t nfs server:/pfad/zur/freigabe /mnt/nfs
    ```
    

**Das Aushängen (Unmounten) von Dateisystemen:**

Bevor ein gemountetes Dateisystem wieder entfernt oder anderweitig verwendet werden kann, muss es **ausgehängt** (unmounted) werden. Dies stellt sicher, dass alle Schreiboperationen abgeschlossen sind und keine Daten verloren gehen. Der Befehl hierfür lautet `umount`:

Bash

```
sudo umount <Mount Point>
```

oder

Bash

```
sudo umount <Gerät>
```

**Wichtige Hinweise zum Unmounten:**

- Kein Benutzer darf sich in einem Verzeichnis innerhalb des Mount Points aufhalten, wenn das Dateisystem ausgehängt werden soll.
- Alle Anwendungen, die Dateien auf dem gemounteten Dateisystem geöffnet haben, müssen geschlossen werden.

**Automatisches Mounten mit `/etc/fstab`:**

Das manuelle Mounten mit dem `mount`-Befehl ist für temporäre Aktionen nützlich. Für permanentere Mounts, z.B. beim Systemstart, wird die Konfigurationsdatei `/etc/fstab` (File System Table) verwendet.

In `/etc/fstab` werden Einträge für Dateisysteme definiert, die beim Booten automatisch gemountet werden sollen. Jede Zeile in `/etc/fstab` enthält typischerweise sechs Felder:

1. `<Gerät>`: Das zu mountende Gerät (wie beim `mount`-Befehl).
2. `<Mount Point>`: Der Einhängepunkt.
3. `<Dateisystemtyp>`: Der Typ des Dateisystems.
4. `<Mount-Optionen>`: Eine durch Kommata getrennte Liste von Mount-Optionen.
5. `<Dump>`: Wird vom `dump`-Befehl verwendet (meistens `0`).
6. `<Pass>`: Die Reihenfolge, in der Dateisysteme beim Booten auf Fehler überprüft werden (Root-Dateisystem ist `1`, andere meistens `2` oder `0` für keine Überprüfung).

**Beispiel eines `/etc/fstab`-Eintrags:**

```
/dev/sdb1        /mnt/daten       ext4    defaults        0       2
/dev/cdrom       /media/cdrom     iso9660 ro,user,noauto 0       0
//server/share   /mnt/share      cifs    guest,uid=1000,gid=1000 0       0
```

- Die erste Zeile mountet die Partition `/dev/sdb1` nach `/mnt/daten` mit den Standardoptionen und führt eine Fehlerprüfung nach dem Root-Dateisystem durch.
- Die zweite Zeile ermöglicht normalen Benutzern das schreibgeschützte Mounten der CD-ROM unter `/media/cdrom`, aber nicht automatisch beim Booten (`noauto`).
- Die dritte Zeile mountet eine CIFS-Netzwerkfreigabe unter `/mnt/share` als Gast und setzt die Benutzer- und Gruppen-ID des Mount-Owners.

Nachdem `/etc/fstab` bearbeitet wurde, kann der Befehl `sudo mount -a` verwendet werden, um alle in der Datei definierten Dateisysteme zu mounten (die noch nicht gemountet sind).

**Relevanz für Systemadministratoren und Penetrationstester:**

- **Systemadministration:** Das korrekte Mounten von Dateisystemen ist essenziell für die Funktionalität des Systems. Fehler in `/etc/fstab` können zu Bootproblemen führen. Die Auswahl der richtigen Mount-Optionen (z.B. `noexec`, `nosuid`, `nodev`, `ro`) ist wichtig für die Sicherheit und Stabilität des Systems.
- **Penetration Testing:**
    - **Enumeration:** Die Ausgabe des `mount`-Befehls oder der Inhalt von `/etc/fstab` kann Informationen über gemountete Dateisysteme, deren Typen und Mount-Optionen liefern. Dies kann Hinweise auf potenzielle Schwachstellen geben (z.B. schreibbare Netzwerkfreigaben, ausführbare Dateisysteme in ungewöhnlichen Orten).
    - **Post-Exploitation:** Nach einem erfolgreichen Zugriff kann das Wissen über Mount Points genutzt werden, um Dateien abzulegen oder zu verändern. Das Mounten eigener Speichergeräte (z.B. USB-Sticks) kann für die Exfiltration von Daten oder das Einschleusen von Tools relevant sein (wobei hier die `noexec`-Option eine wichtige Schutzmaßnahme darstellt).
    - **Sicherheitskonfiguration:** Als Penetration Tester ist es wichtig zu prüfen, ob kritische Dateisysteme mit restriktiven Optionen wie `noexec`, `nosuid` und `nodev` gemountet sind, um das Risiko von Privilege Escalation zu minimieren.

**Zusammenfassend lässt sich sagen:**

Das Mounten von Dateisystemen ist ein grundlegendes Konzept in Linux, das die Verwaltung von Speicherressourcen und die Strukturierung von Daten ermöglicht. Das Verständnis des `mount`- und `umount`-Befehls sowie der Konfigurationsdatei `/etc/fstab` ist für jeden Linux-Anwender und insbesondere für Systemadministratoren unerlässlich. Auch für Penetration Tester liefert das Wissen über gemountete Dateisysteme wichtige Informationen für die Analyse der Systemkonfiguration und potenzieller Sicherheitslücken.