
NTFS, das New Technology File System, ist ein von Microsoft entwickeltes Dateisystem, das seit 1993 in Betriebssystemen der Windows-NT-Reihe verwendet wird. Es bietet eine Reihe von Vorteilen gegenüber älteren Dateisystemen wie FAT und FAT32, insbesondere hinsichtlich der Datensicherheit und der Unterstützung großer Dateien und Partitionen.

- **Erstveröffentlichung**: NTFS wurde im Juli 1993 mit der Einführung von Windows NT 3.1 veröffentlicht.
- **Partitionskennung**: Die Partitionskennung für NTFS ist 0x07 im MBR und EBD0A0A2-B9E5-4433-87C0-68B6B72699C7 im GPT.
- **Verzeichnisstruktur**: NTFS verwendet einen B±Baum für die Verzeichnisstruktur.
- **Dateien und Defektblockliste**: Dateien werden in einer Bitmap oder Extents verwaltet, ebenso die Defektblockliste.
- **Dateigröße**: Eine einzelne Datei kann bis zu 16 TiB (ca. 17,1 TB) groß sein, wobei theoretisch 16 EiB (ca. 18 EB) möglich sind.
- **Anzahl der Dateien**: Bis zu 4.294.967.295 (2^32-1) Dateien können im Dateisystem gespeichert werden.
- **Dateinamen**: Dateinamen können bis zu 255 Zeichen lang sein, wobei bestimmte Zeichen wie `\\ : * ? " < > |` und `\0` (NUL) nicht erlaubt sind.
- **Datumsangaben**: NTFS speichert Datumsangaben für Erzeugung, Änderung, Metadaten-Änderung und letzter Zugriff.
- **Zeitstempel-Auflösung**: Die Zeitstempel-Auflösung beträgt 100 ns.
- **Forks**: NTFS unterstützt Forks, was die Möglichkeit bietet, mehrere Datenströme für eine Datei zu speichern.
- **Dateiattribute**: Es gibt verschiedene Attribute wie schreibgeschützt, versteckt, System-Datei und Archiv.
- **Dateirechte-Verwaltung**: NTFS verwendet Access Control Lists (ACLs) für die Verwaltung der Zugriffsberechtigungen.
- **Komprimierung und Verschlüsselung**: Transparenzkomprimierung und -verschlüsselung sind unterstützt, wobei die Verschlüsselung ab Windows 2000 mit DESX, ab Windows XP mit Triple DES und ab Windows XP Service Pack 1 mit AES implementiert wurde.
- **Unterstützung durch andere Betriebssysteme**: NTFS kann mit Treibern von Linux, MS-DOS, Windows 9x und macOS verwendet werden, obwohl es Einschränkungen gibt.


### Fat Datensystem

Die File Allocation Table (FAT) ist ein Dateisystem, das von Microsoft in den 1970er-Jahren entwickelt wurde. Es ist ein System, das Dateien und Verzeichnisse auf einem Datenträger den entsprechenden Clustern zuordnet. Die wichtigsten Elemente der FAT sind:

- **Freier Cluster**: Ein Cluster, der noch nicht von einer Datei verwendet wird.
- **Defekter Cluster**: Ein Cluster, der beschädigt ist und nicht mehr verwendet werden kann.
- **Letzter Cluster einer Clusterkette**: Der letzte Cluster einer Kette von Clustern, die eine Datei bilden.
- **Sonstiger Cluster einer Clusterkette**: Ein Cluster, der Teil einer Kette von Clustern ist, die eine Datei bilden, aber nicht der letzte Cluster in der Kette ist.

Die ersten Versionen von FAT waren 8-Bit-Varianten, gefolgt von 12-, 16- und 32-Bit-Varianten (FAT12, FAT16, FAT32), die größere maximal mögliche Dateigrößen und Partitionsgrößen ermöglichten. FAT32 ist eine der verbreitetsten Versionen und unterstützt 32-Bit-Betriebssysteme.

Ein weiterer relevantes Dateisystem, das auf FAT basiert, ist exFAT (Extended File Allocation Table), das speziell für Flash-Speicher entwickelt wurde und 2006 eingeführt wurde. Es unterstützt größere Dateigrößen und Partitionen als FAT32 und ist von Windows Vista ab SP1 und neueren Windows-Versionen sowie von Apple-Computern ab Mac OS X Snow Leopard, Version 10.6.5, unterstützt.

Darüber hinaus gibt es eine medizinische Bedeutung von FAT, die sich auf eine spezielle Technik in bildgebenden Verfahren wie der Magnetresonanztomographie (MRT) bezieht. Diese Technik dient dazu, Fettgewebe in den Bildern hervorzuheben oder zu unterdrücken, um bestimmte Strukturen oder Bereiche im Körper besser sichtbar zu machen.

