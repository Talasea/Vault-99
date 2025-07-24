---
created: 2024-11-13T12:11
updated: 2024-11-13T13:11
---
# Active Directory
# DNS Server 
## Installation
1. Den `Server-Manager` aufrufen und Rollen und Features hinzufügen

![[Windows-Server-DNS-Server-installieren.png]]

2. Die Rolle `DNS Server` hinzufügen
3. Durch die Installationshilfe klicken
4. Rolle wird installiert (etwas Geduld) 
5. Den Server neu starten

## Konfiguration
1. Den `DNS-Manger` öffnen
![[Windows-Server-DNS-Manager.png]]
2. Neue `Forward Lookup` Zone erstellen
![[Windows-Server-Neue-DNSZone.png]]

3. In der neuen Zone, Rechtsklick und neuen Host anlegen
![[Windows-Server-Neuen-DNSHost.png]]