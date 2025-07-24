```
/ (Root)
├── bin/           (Binaries: Essenzielle ausführbare Programme)
├── boot/          (Bootloader-Dateien, Kernel)
├── dev/           (Gerätedateien)
├── etc/           (Konfigurationsdateien)
│   ├── network/
│   ├── X11/
│   ├── ...
├── home/          (Benutzerverzeichnisse)
│   └── benutzer1/
│       ├── Dokumente/
│       ├── Bilder/            
│       ├── ...
├── lib/           (Essenzielle Bibliotheken)
│   └── ld-linux.so.*
│   └── libc.so.*
├── lib64/         (64-Bit-Bibliotheken)
├── media/         (Einhängepunkt für Wechselmedien)
├── mnt/           (Temporärer Einhängepunkt für Dateisysteme)
├── opt/           (Optionale Softwarepakete)
├── proc/          (Prozessinformationen (virtuelles Dateisystem))
├── root/          (Home-Verzeichnis des Root-Benutzers)
├── run/           (Laufzeitdaten seit dem letzten Systemstart)
├── sbin/          (System-Binaries: Systemverwaltungsbefehle)
├── srv/           (Daten für vom System bereitgestellte Dienste)
├── sys/           (Kernel- und Geräteinformationen (virtuelles Dateisystem))
├── tmp/           (Temporäre Dateien)
├── usr/           (Benutzerbezogene Programme und Daten)
│   ├── bin/       (Benutzerbezogene ausführbare Programme)
│   ├── include/   (Header-Dateien für Entwicklung)
│   ├── lib/       (Benutzerbezogene Bibliotheken)
│   ├── local/     (Lokal installierte Software)
│   │   ├── bin/
│   │   ├── lib/
│   └── share/     (Archivunabhängige Daten)
└── var/           (Variable Daten: Logs, Spool-Dateien etc.)
    ├── log/
    ├── spool/
    ├── tmp/       (Oftmals ein Symlink zu /tmp)
    └── ...
```

content_copydownload

Use code [with caution](https://support.google.com/legal/answer/13505487).

**Erläuterung der wichtigsten Verzeichnisse:**

- **/ (Root):** Das oberste Verzeichnis des gesamten Dateisystems. Alle anderen Verzeichnisse sind Unterverzeichnisse von Root.
    
- **/bin/ (Binaries):** Enthält essentielle ausführbare Programme, die für den grundlegenden Betrieb des Systems benötigt werden (z.B. ls, cp, mv).
    
- **/boot/:** Beinhaltet Dateien, die für den Bootvorgang des Systems notwendig sind, wie den Kernel und den Bootloader (z.B. GRUB).
    
- **/dev/ (Devices):** Stellt Gerätedateien dar. Linux behandelt Hardware als Dateien, die in diesem Verzeichnis zu finden sind (z.B. Festplatten, Tastatur, Maus).
    
- **/etc/ (Et cetera):** Enthält systemweite Konfigurationsdateien für das Betriebssystem und installierte Programme.
    
- **/home/:** Das Basisverzeichnis für die persönlichen Verzeichnisse der Benutzer (außer dem Root-Benutzer). Jeder Benutzer hat hier ein eigenes Unterverzeichnis.
    
- **/lib/ (Libraries):** Enthält essentielle Bibliotheken, die von den Programmen in /bin/ und /sbin/ benötigt werden.
    
- **/lib64/:** Enthält 64-Bit-Versionen der Bibliotheken in /lib/ auf 64-Bit-Systemen.
    
- **/media/:** Ein typischer Einhängepunkt für Wechselmedien wie USB-Sticks oder DVDs.
    
- **/mnt/ (Mount):** Wird traditionell für das temporäre Einhängen anderer Dateisysteme verwendet. Heutzutage wird oft /media/ für Wechselmedien bevorzugt.
    
- **/opt/ (Optional):** Enthält optionale Softwarepakete, die nicht Teil der Standardinstallation sind. Oft werden hier Programme von Drittanbietern installiert.
    
- **/proc/ (Processes):** Ein virtuelles Dateisystem, das Informationen über laufende Prozesse und den Kernel im Speicher bereitstellt. Die Dateien hier existieren nicht wirklich auf der Festplatte.
    
- **/root/:** Das Home-Verzeichnis des Root-Benutzers (Superuser). Es ist getrennt von den normalen Benutzerverzeichnissen aus Sicherheitsgründen.
    
- **/run/:** Enthält temporäre Laufzeitdaten seit dem letzten Systemstart. Dieses Verzeichnis ist relativ neu und löst einige Probleme mit älteren Methoden zur Speicherung temporärer Daten.
    
- **/sbin/ (System Binaries):** Enthält Systemverwaltungsbefehle, die in der Regel nur vom Root-Benutzer ausgeführt werden dürfen (z.B. fdisk, reboot).
    
- **/srv/ (Service):** Enthält Daten für vom System bereitgestellte Dienste (z.B. Webserver-Daten).
    
- **/sys/ (System):** Ein weiteres virtuelles Dateisystem, das Informationen über das System und dessen Hardware bereitstellt.
    
- **/tmp/ (Temporary):** Enthält temporäre Dateien, die von Programmen erstellt werden. Der Inhalt dieses Verzeichnisses wird in der Regel beim Systemneustart oder regelmäßig gelöscht.
    
- **/usr/ (User):** Enthält die Mehrheit der benutzerbezogenen Programme, Bibliotheken, Dokumentationen und anderen Dateien. Es ist oft in weitere Unterverzeichnisse unterteilt:
    
    - **/usr/bin/:** Benutzerbezogene ausführbare Programme (die nicht essentiell für den Systemstart sind).
        
    - **/usr/include/:** Header-Dateien für die Softwareentwicklung.
        
    - **/usr/lib/:** Benutzerbezogene Bibliotheken.
        
    - **/usr/local/:** Hier werden üblicherweise lokal kompilierte oder installierte Programme abgelegt, die nicht von der Paketverwaltung des Systems stammen. Es hat eine ähnliche Struktur wie /usr/.
        
    - **/usr/share/:** Architekturunabhängige Daten wie Dokumentation, Icons und Konfigurationsvorlagen.
        
- **/var/ (Variable):** Enthält variable Daten, die sich während des Betriebs des Systems ändern können, wie z.B.:
    
    - **/var/log/:** System- und Anwendungsprotokolle (Logs).
        
    - **/var/spool/:** Warteschlangen für verschiedene Dienste (z.B. Druckaufträge, E-Mails).
        
    - **/var/tmp/:** Temporäre Dateien, die im Gegensatz zu /tmp/ Systemneustarts überdauern können (aber nicht garantiert).