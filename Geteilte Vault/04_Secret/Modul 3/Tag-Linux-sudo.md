---
created: 2025-02-24T20:12
updated: 2025-02-24T20:14
---
# Tagesnotiz
###### Linux Konfiguration `sudo`
* [ ] Die `/etc/sudoers.d` Datei
* [ ] Struktur eines Eintrages: `user   host = (runas_user) command`
* [ ] Beispiel mit Tick, Trick und Track
```bash
tick    ALL=(ALL) /usr/bin/docker
trick   ALL=(ALL) NOPASSWD: /usr/bin/apt
track   kali=(ALL) /home/track/echo
```

# Zusätzliche Infos
Editieren von `/etc/sudoers` Datei zwingend mit `sudo visudo`
Für komplexere Systeme Konfigurationsdatei in Ordner `/etc/sudoers.d` hinzufügen

Editor konfigurieren

 ```bash
sudo EDITOR=vim visudo
sudo export VISUAL=nano
sudo export EDITOR=nano
```

This to set a new editor globally
```bash
sudo update-alternatives --set editor /usr/bin/nano
```

Sudoers File configuration

```bash
user   host = (runas_user) command
```

`host(user:group) cmds`
- **root** ALL=(ALL:ALL) ALL - Dies gilt für den Benutzer root
- root **ALL**=(ALL:ALL) ALL - Diese Regel gilt für alle Benutzer root, die sich von allen Hosts aus anmelden
- root ALL=(**ALL**:ALL) ALL - Der Benutzer root kann als alle Benutzer Befehle ausführen
- root ALL=(ALL:**ALL**) ALL - Der Benutzer root kann als alle Gruppen Befehle ausführen
- root ALL=(ALL:ALL) **ALL** - Diese Regeln gelten für alle Befehle
