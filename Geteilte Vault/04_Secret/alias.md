---
created: 1970-01-01T01:00
updated: 2025-01-20T17:04
---
rough mini guide

Um einen Alias zu erstellen gehen wir wie folgt vor

Wir bearbeiten die .zshrc config und fügen dort unseren alias hinzu. 

Der Alias hat folgenden syntax:

alias beispiel=”cd /var/www/html”

Wir finden die .zshrc datei im Home verzeichnis des Users.

Beispiel für Kali
/home/kali/.zshrc
q
andere Linux system nutzen evntuell eine andere datei. Hier sind die gängisten Beispiele.


    Bash – ~/.bashrc
    ZSH – ~/.zshrc
    Fish – ~/.config/fish/config.fish

Bash ist oft bei debian, zsh bei kali oder arch, fish ist recht selten

wir können die Datei mit Kali öffnen
nano /home/kali/.zshrc

Wenn wir fertig sind müssen wir die Console neu starten. Das geht mit dem  source befehl. 

Kali bsp. 
 source ~/.zshrc


danach können wir unseren alias benutzen.