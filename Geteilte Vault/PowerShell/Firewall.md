---
created: 2024-12-01T08:49
updated: 2024-12-01T08:50
---
Info über die drei Firewall Profile ausgeben lassen

```powershell
 Get-NetFirewallProfile
```

Alle Firewallregeln ausgeben lassen (standardmäßig sehr viel Ausgabe!)

```powershell
Get-NetFirewallRule
```

Firewall Profile aktivieren oder deaktivieren

```powershell
# Deaktiviert die Firewall für das öffentliche Profil
Set-NetFirewallProfile -Profile Public -Enabled False
# Aktivert die Firewall für das private Profil
Set-NetFirewallProfile -Profile Private -Enabled True
```

Firewallregel aktivieren oder deaktivieren basierend auf dem Namen der Regel

```powershell
Disable-NetFirewallRule -DisplayName "Allow ICMP"
Enable-NetFirewallRule -DisplayName "Allow ICMP"
```