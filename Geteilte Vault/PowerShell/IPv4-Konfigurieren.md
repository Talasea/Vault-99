---
created: 2024-12-01T08:51
updated: 2024-12-01T08:52
---
Namen der Netzwerkinterfaces bekommen

```powershell
Get-NetAdapter # Beispiele: "Ethernet", "Ethernet 2"
```

Neue IPv4 Adresse setzen 

```powershell
New-NetIPAddress -InterfaceAlias "Ethernet 2" -IPAddress "192.168.1.220" -PrefixLength 24 
New-NetIPAddress -InterfaceAlias "Ethernet 2" -IPAddress "192.168.1.220" -PrefixLength 24 -DefaultGateway "192.168.1.1" # default GW wird auch gesetzt
```

IPv4 Adresse löschen

```powershell
Remove-NetIPAddress -InterfaceAlias "Ethernet 2" -IPAddress "192.168.1.200"
```
