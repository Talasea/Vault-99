
## Startup config

Die Start-Up-Konfiguration eines Switches bezieht sich auf die Einstellungen, die beim ersten Start oder nach einem Neustart angewendet werden. Hier sind einige Schritte und Befehle, die Sie verwenden können, um die Start-Up-Konfiguration eines Switches zu verwalten:

- **Befehl “copy running-config startup-config”**: Dieser Befehl kopiert die aktuelle Konfiguration (running-config) in die Start-Up-Konfiguration (startup-config). Dies ist nützlich, um Änderungen zu speichern, die Sie an der aktuellen Konfiguration vorgenommen haben.
- **Befehl “show running-config”**: Mit diesem Befehl können Sie die aktuelle Konfiguration des Switches anzeigen, die während der Laufzeit angewendet wird.
- **Befehl “show startup-config”**: Dieser Befehl zeigt die Konfiguration an, die beim Start des Switches angewendet wird.
- **Konfigurationsassistenten**: Cisco Switches bieten oft einen Assistenten für die ersten Schritte an, der Ihnen hilft, grundlegende Einstellungen wie IP-Adresse, Hostname und VLANs zu konfigurieren.
- **Backup der Konfiguration**: Sie können die Start-Up-Konfiguration auf einem TFTP-Server speichern, um eine Sicherungskopie zu erstellen. Dazu verwenden Sie den Befehl “copy startup-config tftp:” gefolgt von der IP-Adresse des TFTP-Servers und dem Dateinamen.

Diese Schritte helfen Ihnen, die Start-Up-Konfiguration Ihres Switches effektiv zu verwalten und sicherzustellen, dass er nach einem Neustart die gewünschten Einstellungen verwendet.

<font color="#ff0000">sie befindet sich im nicht flüchtigen speicher</font>

### Running Conf.

Die aktuelle Konfiguration eines Switches kann über die Befehlszeile (CLI) abgerufen und bearbeitet werden. Hier sind einige wichtige Punkte zur Verwaltung der “running configuration” auf einem Cisco Switch:

- **Abfragen der aktuellen Konfiguration**: Der Befehl `show running-config` zeigt die aktuelle Konfiguration des Switches an. Diese enthält alle Einstellungen, die seit dem letzten Neustart oder der letzten Speicherung der Konfiguration geändert wurden.
    
- **Speichern der aktuellen Konfiguration**: Um die aktuelle Konfiguration zu speichern, damit sie nach einem Neustart beibehalten wird, wird der Befehl `copy running-config startup-config` verwendet. Dies speichert die aktuelle Konfiguration in der “startup configuration” im NVRAM (non-volatile RAM).
    
- **Bearbeiten der aktuellen Konfiguration**: Die aktuelle Konfiguration kann über den Befehl `configure terminal` bearbeitet werden. Hier können Einstellungen wie Hostname, Passwörter, VLANs und andere Netzwerkparameter geändert werden.
    
- **Zurücksetzen der Konfiguration**: Wenn die Konfiguration zurückgesetzt werden soll, kann der Switch neu geladen werden (`reload`) oder manuell zurückgesetzt werden, um die Standardeinstellungen wiederherzustellen. Bevor der Switch neu geladen wird, sollte die aktuelle Konfiguration optional gespeichert werden.
    

Diese Schritte helfen, die Verwaltung und Sicherung der Konfiguration eines Cisco Switches zu erleichtern.