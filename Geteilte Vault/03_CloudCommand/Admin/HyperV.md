---
created: 2024-11-11T10:15
updated: 2024-11-14T09:55
---
# Grundlegendes

Default path to Virtual Hard Disks
```
C:\ProgramData\Microsoft\Windows\Virtual Hard Disks\
```

# VM Installationen
## Kali Linux
Installiert mittels vordefinierter VM von der offiziellen Kali Webseite
## Windows Server 2022
Installiert mit einer .iso Datei (funktioniert auch auf jeder Hardware)

Ggfs. Screenshots bezüglich wichtiger Konfigurationsoptionen bei der Installation

# Konfiguration
## Switch
Einen neuen Switch kann ich über `Manager für virtuelle Switches` anlegen
![[HyperV-Konfiguration-Neuer-Switch.png]]

Sobald der Switch angelegt wurde, kann eine virtuelle Maschine mit diesem verbunden werden.
Dafür muss eine zusätzliche Netzwerkkarte zu der Maschine hinzugefügt werden.

![[HyperV-Switch-Neue-Netzwerkkarte.png]]

## Netzwerk
Die virtuellen Maschinen _sollten_ mit dem Default Switch verbunden sein

![[HyperV-Konfiguration-Detault-Switch.png]]
